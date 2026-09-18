#!/usr/bin/env python3
"""Fail-closed Shot Spec reference resolver for AO-06 (v0.1)."""
import argparse, json
from pathlib import Path
import resolver_asset_source_v0_1 as assets

ROOT = Path(__file__).resolve().parents[1]
SPEC = Path("production/shot_specs/A04_SPEC_V001.json")
ENTITIES = Path("production/asset_registry/entity_registry.jsonl")
VERSION = "SHOT_REFERENCE_RESOLVER_V0_1"
ROLES = {"COSTUME": "COSTUME_MASTER", "PROP": "PROP_MASTER"}


def load_spec(path=None, root=ROOT):
    data = json.loads((Path(path) if path else Path(root) / SPEC).read_text(encoding="utf-8"))
    required = {"shot_spec_id", "shot_id", "spec_version", "characters", "scene", "costumes", "props", "shot_photography", "generation_policy"}
    if not required <= data.keys() or data["generation_policy"].get("silent_fallback") is not False:
        raise ValueError("Invalid fail-closed Shot Spec")
    if data["shot_spec_id"] != f'{data["shot_id"]}_SPEC_V{data["spec_version"]:03d}':
        raise ValueError("Shot Spec identity/version mismatch")
    return data


def _entities(root):
    path = Path(root) / ENTITIES
    return {row["entity_id"]: row for row in (json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip())}


def resolve_atomic(entity_id, entity_type, role, variant, state, root=ROOT):
    known = _entities(root)
    if entity_id not in known:
        return {"status": "REFERENCE_GAP", "entity_id": entity_id, "reason": "UNKNOWN_ENTITY"}
    if known[entity_id].get("entity_type") != entity_type:
        return {"status": "REFERENCE_GAP", "entity_id": entity_id, "reason": "ENTITY_TYPE_MISMATCH"}
    rows = [r for r in assets.read_runtime_registry(root) if r.get("entity_id") == entity_id and r.get("asset_class") == "ATOMIC" and r.get("role") == role and r.get("variant") == variant and r.get("state") == state and r.get("approval_status") == "APPROVED" and r.get("lifecycle") == "CURRENT" and r.get("resolver_usage") not in (None, "NEVER")]
    if not rows:
        return {"status": "REFERENCE_GAP", "entity_id": entity_id, "reason": "NO_ELIGIBLE_FORMAL_ASSET"}
    if len(rows) != 1:
        return {"status": "REFERENCE_GAP", "entity_id": entity_id, "reason": "AMBIGUOUS_CURRENT"}
    row = assets.normalize(rows[0], "RUNTIME_REGISTRY")
    try:
        path = assets.source_path(row, root)
    except ValueError as exc:
        return {"status": "REFERENCE_GAP", "entity_id": entity_id, "reason": "INTEGRITY_FAILURE", "detail": str(exc)}
    if not path.is_file():
        return {"status": "REFERENCE_GAP", "entity_id": entity_id, "reason": "MISSING_FILE"}
    if assets.sha256(path) != row.get("sha256") or path.stat().st_size != row.get("byte_size"):
        return {"status": "REFERENCE_GAP", "entity_id": entity_id, "reason": "INTEGRITY_FAILURE"}
    return {"status": "RESOLVED", "entity_id": entity_id, "asset": row}


def _shot_evidence(spec, root):
    rows = [r for r in assets.read_runtime_registry(root)
            if r.get("asset_class") == "SHOT"
            and r.get("shot_id") == spec["shot_id"]
            and r.get("role") == "SHOT_MASTER"
            and r.get("variant") == "DEFAULT"
            and r.get("state") == "DEFAULT"
            and r.get("approval_status") == "APPROVED"
            and r.get("resolver_usage") not in (None, "NEVER")
            and r.get("lifecycle") in ("CURRENT", "ARCHIVED")]
    if not rows:
        return {"status": "SHOT_EVIDENCE_GAP", "shot_id": spec["shot_id"], "reason": "APPROVED_A04_SOURCE_NOT_MATERIALIZED"}
    if len(rows) != 1:
        return {"status": "SHOT_EVIDENCE_GAP", "shot_id": spec["shot_id"], "reason": "AMBIGUOUS_APPROVED_SHOT_EVIDENCE"}
    row = assets.normalize(rows[0], "RUNTIME_REGISTRY")
    row["shot_id"] = rows[0].get("shot_id")
    try: path = assets.source_path(row, root)
    except ValueError as exc: return {"status": "SHOT_EVIDENCE_GAP", "shot_id": spec["shot_id"], "reason": "INTEGRITY_FAILURE", "detail": str(exc)}
    if not path.is_file() or assets.sha256(path) != row.get("sha256") or path.stat().st_size != row.get("byte_size"):
        return {"status": "SHOT_EVIDENCE_GAP", "shot_id": spec["shot_id"], "reason": "INTEGRITY_FAILURE"}
    return {"status": "RESOLVED", "shot_id": spec["shot_id"], "asset": row}


def resolve(spec_path=None, root=ROOT):
    spec = load_spec(spec_path, root)
    results = []
    for item in spec["characters"]:
        try: result = assets.resolve_character_reference_sheet(item["entity_id"], root)
        except ValueError as exc: result = {"status": "REFERENCE_GAP", "entity_id": item["entity_id"], "reason": "AMBIGUOUS_CURRENT", "detail": str(exc)}
        results.append({"kind": "CHARACTER", **result})
    try: scene = assets.resolve_scene(spec["scene"]["entity_id"], spec["scene"]["required_state"], root)
    except ValueError as exc: scene = {"status": "REFERENCE_GAP", "entity_id": spec["scene"]["entity_id"], "reason": "INTEGRITY_OR_AMBIGUITY", "detail": str(exc)}
    results.append({"kind": "SCENE", **scene})
    for key, kind in (("costumes", "COSTUME"), ("props", "PROP")):
        for item in spec[key]:
            results.append({"kind": kind, **resolve_atomic(item["entity_id"], kind, ROLES[kind], item["variant"], item["state"], root)})
    evidence = _shot_evidence(spec, root)
    gaps = [r for r in results if r["status"] != "RESOLVED"]
    blockers = [{"type": r.get("reason", "REQUIRED_REFERENCE_GAP"), "entity_id": r.get("entity_id")} for r in gaps]
    if evidence["status"] != "RESOLVED": blockers.append({"type": "SHOT_EVIDENCE_GAP", "reason": evidence["reason"]})
    allowed = not blockers
    return {"resolver_version": VERSION, "shot_spec_id": spec["shot_spec_id"], "shot_id": spec["shot_id"], "scene_state": spec["scene"]["required_state"], "resolved": [r for r in results if r["status"] == "RESOLVED"], "reference_gaps": gaps, "shot_evidence": evidence, "shot_evidence_gaps": [] if evidence["status"] == "RESOLVED" else [evidence], "blockers": blockers, "generation_allowed": allowed, "status": "READY_FOR_GENERATION" if allowed else "BLOCKED"}


def main():
    p=argparse.ArgumentParser(); p.add_argument("--spec"); p.add_argument("--root", type=Path, default=ROOT); a=p.parse_args()
    print(json.dumps(resolve(a.spec, a.root), ensure_ascii=False, indent=2))
if __name__ == "__main__": main()
