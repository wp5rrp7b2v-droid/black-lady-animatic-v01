#!/usr/bin/env python3
import argparse, hashlib, json, shutil, struct, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "production/asset_registry/asset_registry.jsonl"
STORY_INDEX = ROOT / "production/story_shots/story_shot_index.jsonl"

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def git_blob(path):
    return subprocess.check_output(["git","hash-object",str(path)], cwd=ROOT, text=True).strip()

def png_dimensions(path):
    data = path.read_bytes()[:24]
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"Invalid PNG signature: {path}")
    return struct.unpack(">II", data[16:24])

def rows(path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

def safe_source(rel):
    p = ROOT / rel
    if not p.is_file() or p.is_symlink() or p.resolve() != p:
        raise ValueError(f"Invalid canonical source: {rel}")
    return p

def verify_ref(ref, registry_rows, story_rows):
    source_type = ref["source_type"]
    if source_type == "ASSET":
        matches = [r for r in registry_rows if r.get("asset_id") == ref["reference_id"]]
        if len(matches) != 1:
            raise ValueError(f"Asset cardinality mismatch: {ref['reference_id']}")
        row = matches[0]
        for key in ("entity_id","role","asset_class","authority_class","approval_status","lifecycle","resolver_usage"):
            expected = ref.get(key)
            if expected is not None and row.get(key) != expected:
                raise ValueError(f"{ref['reference_id']} {key} mismatch")
        if row.get("storage_uri") != ref["canonical_path"]:
            raise ValueError(f"{ref['reference_id']} canonical path mismatch")
        if row.get("byte_size") != ref["expected_byte_size"]:
            raise ValueError(f"{ref['reference_id']} registry byte size mismatch")
        if ref.get("expected_sha256") and row.get("sha256") != ref["expected_sha256"]:
            raise ValueError(f"{ref['reference_id']} registry SHA mismatch")
    elif source_type == "STORY_SHOT":
        matches = [r for r in story_rows if r.get("shot_id") == ref["shot_id"]]
        if len(matches) != 1:
            raise ValueError(f"Story Shot cardinality mismatch: {ref['shot_id']}")
        row = matches[0]
        for key in ("approval_status","lifecycle"):
            if row.get(key) != ref[key]:
                raise ValueError(f"{ref['reference_id']} {key} mismatch")
        if row.get("canonical_path") != ref["canonical_path"]:
            raise ValueError(f"{ref['reference_id']} canonical path mismatch")
        if row.get("byte_size") != ref["expected_byte_size"]:
            raise ValueError(f"{ref['reference_id']} index byte size mismatch")
        if row.get("github_blob_sha") != ref["expected_git_blob"]:
            raise ValueError(f"{ref['reference_id']} index blob mismatch")
    elif source_type == "CONTROLLED_REFERENCE":
        manifest_rel = ref.get("manifest_path")
        if not manifest_rel:
            raise ValueError(f"{ref['reference_id']} manifest_path missing")
        manifest_path = safe_source(manifest_rel)
        try:
            controlled = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception as exc:
            raise ValueError(f"{ref['reference_id']} invalid controlled-reference manifest") from exc

        required_manifest = {
            "reference_id": ref["reference_id"],
            "classification": ref["classification"],
            "approval_status": ref["approval_status"],
            "lifecycle": ref["lifecycle"],
            "authority_scope": ref["authority_scope"],
            "canonical_path": ref["canonical_path"],
        }
        for key, expected in required_manifest.items():
            if controlled.get(key) != expected:
                raise ValueError(f"{ref['reference_id']} manifest {key} mismatch")

        output = controlled.get("output")
        if not isinstance(output, dict):
            raise ValueError(f"{ref['reference_id']} manifest output missing")

        expected_output = {
            "byte_size": ref["expected_byte_size"],
            "sha256": ref["expected_sha256"],
            "git_blob": ref["expected_git_blob"],
        }
        if ref.get("expected_width") is not None:
            expected_output["width"] = ref["expected_width"]
        if ref.get("expected_height") is not None:
            expected_output["height"] = ref["expected_height"]
        for key, expected in expected_output.items():
            if output.get(key) != expected:
                raise ValueError(f"{ref['reference_id']} manifest output {key} mismatch")

        if output.get("format") != "PNG":
            raise ValueError(f"{ref['reference_id']} manifest output format mismatch")
        if controlled.get("approved_binary", {}).get("sha256") != ref["expected_sha256"]:
            raise ValueError(f"{ref['reference_id']} approved binary SHA mismatch")
        if controlled.get("approved_binary", {}).get("byte_size") != ref["expected_byte_size"]:
            raise ValueError(f"{ref['reference_id']} approved binary byte size mismatch")
    else:
        raise ValueError(f"Unsupported source type: {source_type}")

    src = safe_source(ref["canonical_path"])
    actual_sha = sha256(src)
    actual_size = src.stat().st_size
    actual_blob = git_blob(src)
    width, height = png_dimensions(src)

    if actual_size != ref["expected_byte_size"]:
        raise ValueError(f"{ref['reference_id']} byte size mismatch")
    if actual_blob != ref["expected_git_blob"]:
        raise ValueError(f"{ref['reference_id']} Git blob mismatch")
    if ref.get("expected_sha256") and actual_sha != ref["expected_sha256"]:
        raise ValueError(f"{ref['reference_id']} SHA mismatch")
    if ref.get("expected_width") is not None and width != ref["expected_width"]:
        raise ValueError(f"{ref['reference_id']} width mismatch")
    if ref.get("expected_height") is not None and height != ref["expected_height"]:
        raise ValueError(f"{ref['reference_id']} height mismatch")

    return src, actual_sha, actual_size, actual_blob, width, height

def build(spec_path):
    spec_path = (ROOT / spec_path).resolve()
    if not spec_path.is_file() or spec_path.is_symlink():
        raise ValueError("Invalid spec path")
    if spec_path.parent != (ROOT / "production/bundle_specs").resolve():
        raise ValueError("Spec must live directly under production/bundle_specs")

    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    required = {"schema_version","bundle_id","target_shot_id","sequence_id","target_candidate","references","work_handoff"}
    if not required <= spec.keys():
        raise ValueError("Bundle spec missing required fields")
    if not isinstance(spec["references"], list) or not spec["references"]:
        raise ValueError("Reference set is empty")

    out = ROOT / spec["bundle_id"]
    if out.exists() or out.is_symlink():
        raise ValueError(f"Refusing to overwrite existing output: {out.name}")

    registry_rows = rows(REGISTRY)
    story_rows = rows(STORY_INDEX)
    manifest_refs = []
    out.mkdir()

    try:
        for ref in spec["references"]:
            src, actual_sha, actual_size, actual_blob, width, height = verify_ref(ref, registry_rows, story_rows)
            group = ref["destination_group"]
            group_dir = out / group
            group_dir.mkdir(exist_ok=True)
            dst = group_dir / f"{ref['reference_id']}__{src.name}"
            shutil.copyfile(src, dst)
            if sha256(dst) != actual_sha or dst.stat().st_size != actual_size or git_blob(dst) != actual_blob:
                raise ValueError(f"Byte-identical copy verification failed: {ref['reference_id']}")
            manifest_refs.append({
                **ref,
                "computed_sha256": actual_sha,
                "actual_byte_size": actual_size,
                "actual_git_blob": actual_blob,
                "dimensions": {"width": width, "height": height},
                "png_signature": "PASS",
                "byte_identical_copy": "PASS",
                "bundle_path": dst.relative_to(out).as_posix()
            })

        manifest = {
            "bundle_id": spec["bundle_id"],
            "target_shot_id": spec["target_shot_id"],
            "sequence_id": spec["sequence_id"],
            "target_candidate": spec["target_candidate"],
            "reference_count": len(manifest_refs),
            "all_reference_checks_pass": True,
            "generation_allowed": True,
            "manual_product_owner_reference_upload": spec.get("manual_product_owner_reference_upload",0),
            "references": manifest_refs,
            "overall_result": "PASS"
        }
        (out / "delivery_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        h = spec["work_handoff"]
        lines = [f"# {h.get('title', spec['target_candidate'])}", "", "## Requirements"]
        lines += [f"- {x}" for x in h.get("requirements",[])]
        lines += ["", "## Exclusions"]
        lines += [f"- {x}" for x in h.get("exclusions",[])]
        lines += ["", "## Verification", "- Revalidate every delivered PNG against delivery_manifest.json before generation.", "- If any check fails, do not generate."]
        (out / "WORK_HANDOFF.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

        for ref in manifest_refs:
            p = out / ref["bundle_path"]
            if sha256(p) != ref["computed_sha256"] or p.stat().st_size != ref["actual_byte_size"] or git_blob(p) != ref["actual_git_blob"]:
                raise ValueError(f"Final artifact revalidation failed: {ref['reference_id']}")

        print(f"PASS: {len(manifest_refs)}/{len(spec['references'])} exact canonical reference binaries verified")
        print("GENERATION_ALLOWED=TRUE")
        print("BUNDLE_ID=" + spec["bundle_id"])
        return out
    except Exception:
        if out.exists():
            shutil.rmtree(out)
        raise

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--spec", required=True)
    a = p.parse_args()
    build(a.spec)

if __name__ == "__main__":
    main()
