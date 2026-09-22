#!/usr/bin/env python3
"""AO-04 deterministic, non-generative Character Reference Sheet builder."""
import argparse
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = Path("production/asset_registry/asset_registry.jsonl")
ENTITIES = Path("production/asset_registry/entity_registry.jsonl")
CANDIDATE_ROOT = Path("production/image_library/derived_reference_sheets/_candidate")
BUILDER_VERSION = "0.1"
STATUS = "WAITING_PRODUCT_OWNER_VISUAL_APPROVAL"
TIER_A = [(x, x) for x in ("FACE_FRONT", "FACE_3Q_LEFT", "FACE_3Q_RIGHT", "PROFILE_LEFT", "PROFILE_RIGHT", "REAR_3Q_LEFT", "REAR_3Q_RIGHT", "BODY_FRONT", "BODY_BACK")]
TIER_B = [("FACE_FRONT", "FACE_FRONT"), ("FACE_3Q_PRIMARY", "FACE_3Q_{side}"), ("PROFILE_PRIMARY", "PROFILE_{side}"), ("REAR_3Q_PRIMARY", "REAR_3Q_{side}"), ("BODY_FRONT", "BODY_FRONT"), ("BODY_BACK", "BODY_BACK")]
TIER_C = [("FACE_IDENTITY", "FACE_FRONT"), ("BODY_FRONT", "BODY_FRONT"), ("REAR_OR_BACK", "BODY_BACK")]
EXPECTED = {"CHAR_NING_QIUSHUI":9,"CHAR_JUN_LUYUAN":9,"CHAR_NEIL":9,"CHAR_BLACK_LADY":9,"CHAR_WEN_QINGYA":6,"CHAR_SU_XIAOXIAO":6,"CHAR_LIAO_JIAN":6,"CHAR_CASTLE_YOUNG_MASTER":6,"CHAR_GUANG_YONG":3}


def digest(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()


def read_jsonl(path):
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]


def layout(entity):
    tier=entity["character_tier"]
    if tier=="A": return TIER_A, (3,3)
    if tier=="B": return [(logical, role.format(side=entity["primary_side"])) for logical,role in TIER_B], (2,3)
    if tier=="C": return TIER_C, (3,1)
    raise ValueError(f"Unsupported character tier: {tier}")


def select_atomic_assets(root, entity, registry=None):
    root=Path(root)
    rows=registry if registry is not None else read_jsonl(root/REGISTRY)
    wanted={role for _,role in layout(entity)[0]}
    selected={}
    for row in rows:
        if not (row.get("entity_id")==entity["entity_id"] and row.get("asset_class")=="ATOMIC" and row.get("approval_status")=="APPROVED" and row.get("lifecycle")=="CURRENT" and row.get("resolver_usage")=="DEFAULT" and row.get("variant")=="DEFAULT" and row.get("state")=="DEFAULT" and row.get("role") in wanted): continue
        key=row["role"]
        if key in selected: raise ValueError(f"Duplicate DEFAULT CURRENT Atomic role: {entity['entity_id']} {key}")
        p=root/row["storage_uri"]
        if not p.is_file() or p.resolve()!=p or digest(p)!=row["sha256"]: raise ValueError(f"Invalid source integrity: {row['asset_id']}")
        selected[key]=row
    return selected


def _font(): return ImageFont.load_default()


def build_one(root, entity, output_root=None, registry=None):
    root=Path(root); mapping,grid=layout(entity); selected=select_atomic_assets(root,entity,registry)
    cell_w,cell_h,meta_h=480,540,62
    sheet=Image.new("RGB",(grid[0]*cell_w,grid[1]*cell_h),(38,40,44)); draw=ImageDraw.Draw(sheet); font=_font()
    sources=[]; gaps=[]
    for i,(logical,role) in enumerate(mapping):
        x=(i%grid[0])*cell_w; y=(i//grid[0])*cell_h
        draw.rectangle((x+4,y+4,x+cell_w-5,y+cell_h-5),fill=(235,235,232),outline=(110,110,110),width=2)
        row=selected.get(role)
        if row:
            with Image.open(root/row["storage_uri"]) as src:
                src=src.convert("RGB"); src.thumbnail((cell_w-16,cell_h-meta_h-16),Image.Resampling.LANCZOS)
                px=x+(cell_w-src.width)//2; py=y+8+(cell_h-meta_h-16-src.height)//2
                sheet.paste(src,(px,py))
            label=f"{logical} -> {role}\n{row['asset_id']} V{row['version_no']:03d}"
            sources.append({"selected_canonical_slot":logical,"asset_id":row["asset_id"],"version_no":row["version_no"],"role":row["role"],"filename":row["filename"],"sha256":row["sha256"],"lifecycle":row["lifecycle"],"approval_status":row["approval_status"]})
        else:
            label=f"{logical} -> {role}\nREFERENCE_GAP"; gaps.append(logical)
            bbox=draw.textbbox((0,0),"REFERENCE_GAP",font=font); draw.text((x+(cell_w-(bbox[2]-bbox[0]))//2,y+(cell_h-meta_h)//2),"REFERENCE_GAP",fill=(150,30,30),font=font)
        draw.rectangle((x+5,y+cell_h-meta_h,x+cell_w-5,y+cell_h-5),fill=(218,218,214)); draw.multiline_text((x+12,y+cell_h-meta_h+9),label,fill=(15,15,15),font=font,spacing=4)
    outbase=Path(output_root) if output_root else root/CANDIDATE_ROOT
    outdir=outbase/entity["entity_id"].lower(); outdir.mkdir(parents=True,exist_ok=True)
    filename=f"{entity['entity_id']}_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png"; png=outdir/filename
    sheet.save(png,format="PNG",optimize=False,compress_level=9)
    candidate_relative_path=(CANDIDATE_ROOT/entity["entity_id"].lower()/filename).as_posix()
    manifest={"entity_id":entity["entity_id"],"character_tier":entity["character_tier"],"primary_side":entity["primary_side"],"role":"CHARACTER_REFERENCE_SHEET","variant":"DEFAULT","state":"DEFAULT","builder_version":BUILDER_VERSION,"candidate_status":STATUS,"sources":sources,"explicit_gap_slots":gaps,"sheet_filename":filename,"expected_candidate_path":candidate_relative_path,"sheet_sha256":digest(png),"byte_size":png.stat().st_size}
    mp=outdir/(filename.removesuffix(".png")+".manifest.json"); mp.write_text(json.dumps(manifest,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    return manifest,png,mp


def build_all(root=ROOT, output_root=None, enforce_expected=True):
    root=Path(root); entities=[e for e in read_jsonl(root/ENTITIES) if e.get("entity_type")=="CHARACTER" and e.get("entity_status")=="ACTIVE"]
    if {e["entity_id"] for e in entities} != set(EXPECTED): raise ValueError("Character Entity prerequisite mismatch")
    live={e["entity_id"]:len(select_atomic_assets(root,e)) for e in entities}
    if enforce_expected and live != EXPECTED: raise RuntimeError(f"LIVE_COVERAGE_MISMATCH expected={EXPECTED} actual={live}")
    return [build_one(root,e,output_root) for e in sorted(entities,key=lambda x:x["entity_id"])]


def main():
    p=argparse.ArgumentParser(); p.add_argument("--root",type=Path,default=ROOT); p.add_argument("--output-root",type=Path); p.add_argument("--no-expected-check",action="store_true"); a=p.parse_args()
    results=build_all(a.root,a.output_root,not a.no_expected_check)
    print(json.dumps({"status":STATUS,"candidates":[m for m,_,_ in results],"selected_dependencies":sum(len(m["sources"]) for m,_,_ in results)},ensure_ascii=False,indent=2))
if __name__=="__main__": main()
