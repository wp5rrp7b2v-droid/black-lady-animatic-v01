#!/usr/bin/env python3
"""Fail-closed Shot Spec reference resolver for AO-06 (v0.1)."""
import argparse
import json
from pathlib import Path, PurePosixPath

import resolver_asset_source_v0_1 as assets

ROOT = Path(__file__).resolve().parents[1]
SPEC = Path("production/shot_specs/A04_SPEC_V001.json")
VERSION = "SHOT_REFERENCE_RESOLVER_V0_1"


def load_spec(path=None, root=ROOT):
    data = json.loads((Path(path) if path else Path(root) / SPEC).read_text(encoding="utf-8"))
    required = {
        "shot_spec_id",
        "shot_id",
        "spec_version",
        "characters",
        "scene",
        "appearance_continuity",
        "shot_photography",
        "shot_evidence",
        "generation_policy",
    }
    if not required <= data.keys() or data["generation_policy"].get("silent_fallback") is not False:
        raise ValueError("Invalid fail-closed Shot Spec")
    if data["shot_spec_id"] != f'{data["shot_id"]}_SPEC_V{data["spec_version"]:03d}':
        raise ValueError("Shot Spec identity/version mismatch")
    if data.get("costumes") or data.get("props"):
        raise ValueError("A04 Review Patch 02 forbids formal Costume/Prop requirements")
    continuity = data["appearance_continuity"]
    if len(continuity) != 1 or continuity[0].get("entity_id") != "CHAR_NEIL":
        raise ValueError("A04 requires exactly one Neil appearance-continuity record")
    if continuity[0].get("formal_asset_required") is not False:
        raise ValueError("Neil appearance continuity must not require a standalone formal asset")
    if "WHITE_POCKET_HANDKERCHIEF_VISIBLE" in continuity[0].get("constraints", []):
        raise ValueError("White pocket handkerchief is not an A04 required continuity fact")
    return data


def _safe_evidence_path(spec, root):
    evidence = spec["shot_evidence"]
    uri = evidence.get("storage_uri")
    filename = evidence.get("filename")
    if not isinstance(uri, str) or not uri or "\\" in uri:
        raise ValueError("Invalid Shot evidence storage URI")
    rel = PurePosixPath(uri)
    if rel.is_absolute() or ".." in rel.parts:
        raise ValueError("Shot evidence storage path escape")
    if rel.as_posix() != "staging/d069_a04_intake/A04_REBOOT_approved_v001.png":
        raise ValueError("Unexpected A04 evidence path")
    if filename != "A04_REBOOT_approved_v001.png" or rel.name != filename:
        raise ValueError("A04 evidence filename mismatch")
    root = Path(root).resolve()
    path = root / Path(*rel.parts)
    if path.resolve() != path:
        raise ValueError("Shot evidence path is redirected")
    return path


def _shot_evidence(spec, root):
    evidence = spec["shot_evidence"]
    try:
        path = _safe_evidence_path(spec, root)
    except ValueError as exc:
        return {
            "status": "SHOT_EVIDENCE_GAP",
            "shot_id": spec["shot_id"],
            "reason": "INTEGRITY_FAILURE",
            "detail": str(exc),
        }
    if evidence.get("approval_status") != "APPROVED":
        return {
            "status": "SHOT_EVIDENCE_GAP",
            "shot_id": spec["shot_id"],
            "reason": "EVIDENCE_NOT_APPROVED",
        }
    if evidence.get("resolver_usage") != "EVIDENCE_ONLY":
        return {
            "status": "SHOT_EVIDENCE_GAP",
            "shot_id": spec["shot_id"],
            "reason": "INVALID_EVIDENCE_USAGE",
        }
    if not path.is_file():
        return {
            "status": "SHOT_EVIDENCE_GAP",
            "shot_id": spec["shot_id"],
            "reason": "APPROVED_A04_SOURCE_NOT_MATERIALIZED",
        }
    actual_size = path.stat().st_size
    actual_sha = assets.sha256(path)
    if actual_size != evidence.get("byte_size") or actual_sha != evidence.get("sha256"):
        return {
            "status": "SHOT_EVIDENCE_GAP",
            "shot_id": spec["shot_id"],
            "reason": "INTEGRITY_FAILURE",
            "actual_byte_size": actual_size,
            "actual_sha256": actual_sha,
        }
    return {
        "status": "RESOLVED",
        "shot_id": spec["shot_id"],
        "evidence": {
            "filename": evidence["filename"],
            "storage_uri": evidence["storage_uri"],
            "sha256": evidence["sha256"],
            "byte_size": evidence["byte_size"],
            "approval_status": evidence["approval_status"],
            "provenance_status": evidence["provenance_status"],
            "resolver_usage": evidence["resolver_usage"],
            "historical_uses_reference_policy": evidence["historical_uses_reference_policy"],
        },
    }


def resolve(spec_path=None, root=ROOT):
    spec = load_spec(spec_path, root)
    results = []

    for item in spec["characters"]:
        try:
            result = assets.resolve_character_reference_sheet(item["entity_id"], root)
        except ValueError as exc:
            result = {
                "status": "REFERENCE_GAP",
                "entity_id": item["entity_id"],
                "reason": "AMBIGUOUS_CURRENT",
                "detail": str(exc),
            }
        results.append({"kind": "CHARACTER", **result})

    try:
        scene = assets.resolve_scene(
            spec["scene"]["entity_id"],
            spec["scene"]["required_state"],
            root,
        )
    except ValueError as exc:
        scene = {
            "status": "REFERENCE_GAP",
            "entity_id": spec["scene"]["entity_id"],
            "reason": "INTEGRITY_OR_AMBIGUITY",
            "detail": str(exc),
        }
    results.append({"kind": "SCENE", **scene})

    evidence = _shot_evidence(spec, root)
    gaps = [r for r in results if r["status"] != "RESOLVED"]
    blockers = [
        {"type": r.get("reason", "REQUIRED_REFERENCE_GAP"), "entity_id": r.get("entity_id")}
        for r in gaps
    ]
    if evidence["status"] != "RESOLVED":
        blockers.append({"type": "SHOT_EVIDENCE_GAP", "reason": evidence["reason"]})

    allowed = not blockers
    return {
        "resolver_version": VERSION,
        "shot_spec_id": spec["shot_spec_id"],
        "shot_id": spec["shot_id"],
        "scene_state": spec["scene"]["required_state"],
        "appearance_continuity": spec["appearance_continuity"],
        "resolved": [r for r in results if r["status"] == "RESOLVED"],
        "reference_gaps": gaps,
        "shot_evidence": evidence,
        "shot_evidence_gaps": [] if evidence["status"] == "RESOLVED" else [evidence],
        "blockers": blockers,
        "generation_allowed": allowed,
        "status": "READY_FOR_GENERATION" if allowed else "BLOCKED",
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--spec")
    p.add_argument("--root", type=Path, default=ROOT)
    a = p.parse_args()
    print(json.dumps(resolve(a.spec, a.root), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
