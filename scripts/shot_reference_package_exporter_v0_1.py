#!/usr/bin/env python3
"""Build a verified, fail-closed Shot reference package."""
import argparse, json, shutil, subprocess, tempfile
from datetime import datetime, timezone
from pathlib import Path
import resolver_asset_source_v0_1 as asset_source
import shot_reference_resolver_v0_1 as resolver
ROOT=Path(__file__).resolve().parents[1]
VERSION="SHOT_REFERENCE_PACKAGE_EXPORTER_V0_1"

def _commit(root):
    try: return subprocess.check_output(["git","rev-parse","HEAD"], cwd=root, text=True, stderr=subprocess.DEVNULL).strip()
    except (OSError, subprocess.SubprocessError): return "UNKNOWN"

def export(output, spec_path=None, root=ROOT, generated_at=None):
    root=Path(root); output=Path(output)
    if not output.is_absolute(): output=root/output
    if output.exists() or output.is_symlink(): raise ValueError("Package destination already exists")
    result=resolver.resolve(spec_path, root); spec=resolver.load_spec(spec_path, root)
    package_id=f'{spec["shot_id"]}_REFERENCE_PACKAGE_V{spec["spec_version"]:03d}'
    if output.name != package_id or output.parent.resolve() != output.parent or output.parent.is_symlink():
        raise ValueError("Package must use canonical direct-child name")
    selected=list(result["resolved"])
    if result["shot_evidence"]["status"]=="RESOLVED": selected.append({"kind":"SHOT_EVIDENCE", **result["shot_evidence"]})
    manifest={"package_id":package_id,"shot_spec_id":spec["shot_spec_id"],"shot_id":spec["shot_id"],"source_commit":_commit(root),"resolver_version":result["resolver_version"],"exporter_version":VERSION,"generated_at":generated_at or datetime.now(timezone.utc).isoformat(),"scene_state":result["scene_state"],"resolved_assets":[],"reference_gaps":result["reference_gaps"],"shot_evidence_gaps":result["shot_evidence_gaps"],"blockers":result["blockers"],"generation_allowed":result["generation_allowed"],"status":result["status"]}
    staging=Path(tempfile.mkdtemp(prefix=".shot_package_",dir=output.parent))
    try:
        (staging/"visual_refs").mkdir(); (staging/"evidence"/"approved_a04_source_reference").mkdir(parents=True)
        (staging/"shot_spec_snapshot.json").write_text(json.dumps(spec,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        for item in selected:
            row=item["asset"]; source=asset_source.source_path(row,root); delivered=row["filename"]
            destination=(staging/"evidence"/"approved_a04_source_reference"/delivered if item["kind"]=="SHOT_EVIDENCE" else staging/"visual_refs"/delivered)
            shutil.copyfile(source,destination)
            if asset_source.sha256(destination)!=row["sha256"] or destination.stat().st_size!=row["byte_size"]: raise ValueError("Copied binary integrity failure")
            manifest["resolved_assets"].append({k:row.get(k) for k in ("asset_id","entity_id","shot_id","asset_class","role","variant","state","version_no","approval_status","lifecycle","authority_class","resolver_usage","sha256","byte_size","storage_uri")} | {"delivered_filename":delivered,"selection_reason":item["kind"]})
        (staging/"package_manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        staging.rename(output)
    finally:
        if staging.exists(): shutil.rmtree(staging)
    return manifest

def main():
    p=argparse.ArgumentParser(); p.add_argument("output",type=Path); p.add_argument("--spec"); p.add_argument("--root",type=Path,default=ROOT); a=p.parse_args()
    print(json.dumps(export(a.output,a.spec,a.root),ensure_ascii=False,indent=2))
if __name__=="__main__": main()
