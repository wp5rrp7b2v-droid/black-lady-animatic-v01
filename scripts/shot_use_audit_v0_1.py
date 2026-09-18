#!/usr/bin/env python3
"""Immutable Shot use records, reverse audit, and isolated USES_REFERENCE transactions."""
import json, os, tempfile
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
USE_ROOT=Path("production/audit/shot_use_records")
RELATIONS=Path("production/asset_registry/asset_relations.jsonl")
AUDIT=Path("production/asset_registry/audit_event_log.jsonl")
REQUIRED={"use_record_id","shot_spec_id","shot_id","package_id","source_commit","resolver_version","input_asset_ids","input_versions","input_sha256","input_order","delivery_artifact_digest","generation_environment","request_or_proof_identifier","manual_product_owner_reference_upload_count","service_input_sha_receipt","result","created_at"}

def validate_use_record(row):
    if not REQUIRED <= row.keys(): raise ValueError(f"Missing use-record fields: {sorted(REQUIRED-row.keys())}")
    n=len(row["input_asset_ids"])
    if not all(len(row[k])==n for k in ("input_versions","input_sha256","input_order")): raise ValueError("Input arrays differ in length")
    if row["input_order"] != list(range(1,n+1)) or len(set(row["input_asset_ids"]))!=n: raise ValueError("Invalid input order or duplicate asset")
    if row["service_input_sha_receipt"]!="NOT_AVAILABLE": raise ValueError("Unsupported service receipt claim")
    return row

def write_use_record(row, root=ROOT):
    validate_use_record(row); base=Path(root)/USE_ROOT; base.mkdir(parents=True,exist_ok=True)
    target=base/f'{row["use_record_id"]}.json'
    if target.exists() or target.is_symlink(): raise FileExistsError("Use record is immutable")
    flags=os.O_WRONLY|os.O_CREAT|os.O_EXCL
    fd=os.open(target,flags,0o444)
    with os.fdopen(fd,"w",encoding="utf-8") as stream: json.dump(row,stream,ensure_ascii=False,indent=2); stream.write("\n")
    return target

def _records(root):
    base=Path(root)/USE_ROOT
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(base.glob("*.json"))] if base.exists() else []

def query_shot(shot_id, root=ROOT):
    return [{"use_record_id":r["use_record_id"],"shot_spec_id":r["shot_spec_id"],"shot_id":r["shot_id"],"package_id":r["package_id"],"input_asset_ids":r["input_asset_ids"],"input_versions":r["input_versions"],"input_sha256":r["input_sha256"],"input_order":r["input_order"],"scene_state":r.get("scene_state"),"blockers":r.get("blockers",[]),"generation_environment":r["generation_environment"],"request_or_proof_identifier":r["request_or_proof_identifier"],"created_at":r["created_at"]} for r in _records(root) if r["shot_id"]==shot_id]

def query_asset(asset_id, root=ROOT):
    return [{"use_record_id":r["use_record_id"],"shot_id":r["shot_id"],"package_id":r["package_id"],"created_at":r["created_at"],"request_or_proof_identifier":r["request_or_proof_identifier"]} for r in _records(root) if asset_id in r["input_asset_ids"]]

def query_relations(asset_id, direction="forward", root=ROOT):
    rows=[json.loads(x) for x in (Path(root)/RELATIONS).read_text(encoding="utf-8").splitlines() if x.strip()]
    key="source_asset_id" if direction=="forward" else "target_asset_id"
    if direction not in ("forward","reverse"): raise ValueError("Invalid direction")
    return [r for r in rows if r.get("relation_type")=="USES_REFERENCE" and r.get(key)==asset_id]

def add_uses_reference(source_asset_id,target_asset_id,root=ROOT,fail_after_relation=False):
    root=Path(root); registry=[json.loads(x) for x in (root/"production/asset_registry/asset_registry.jsonl").read_text().splitlines() if x.strip()]
    by_id={r["asset_id"]:r for r in registry}
    if source_asset_id==target_asset_id: raise ValueError("Self relation forbidden")
    if by_id.get(source_asset_id,{}).get("asset_class")!="SHOT": raise ValueError("USES_REFERENCE source must be SHOT")
    if target_asset_id not in by_id: raise ValueError("Unknown target")
    relpath=root/RELATIONS; auditpath=root/AUDIT
    relations=[json.loads(x) for x in relpath.read_text().splitlines() if x.strip()]
    if any(r.get("relation_type")=="USES_REFERENCE" and r.get("source_asset_id")==source_asset_id and r.get("target_asset_id")==target_asset_id for r in relations): raise ValueError("Duplicate USES_REFERENCE")
    now=datetime.now(timezone.utc).isoformat()
    event_id=f"EVT_USE_{source_asset_id}_{target_asset_id}"
    relation={"relation_id":f"REL_USE_{source_asset_id}_{target_asset_id}","relation_type":"USES_REFERENCE","source_asset_id":source_asset_id,"target_asset_id":target_asset_id,"created_at":now,"created_by_event_id":event_id,"task_id":"D-069/AO-06"}
    event={"event_id":event_id,"event_type":"RELATION_CREATED","event_time":now,"actor_type":"SYSTEM","actor_id":"SHOT_USE_AUDIT_V0_1","asset_id":source_asset_id,"entity_id":None,"previous_value":None,"new_value":relation,"reason":"Proven current formal output reference use","source_reference":"validated immutable use record","task_id":"D-069/AO-06"}
    old_rel=relpath.read_bytes(); old_audit=auditpath.read_bytes()
    try:
        relpath.write_bytes(old_rel+(json.dumps(relation,separators=(",",":"))+"\n").encode())
        if fail_after_relation: raise RuntimeError("injected transaction failure")
        auditpath.write_bytes(old_audit+(json.dumps(event,separators=(",",":"))+"\n").encode())
    except Exception:
        relpath.write_bytes(old_rel); auditpath.write_bytes(old_audit); raise
    return relation
