#!/usr/bin/env python3
"""
Automatic Ingest Controller V0.1
《诡舍·黑衣夫人》轻量正式图片入库工具。

V0.1 scope:
- Character PNG only
- explicit Product Owner approval required
- checks Single Current against D-059 migration manifest + new runtime registry
- canonical rename + SHA-256 + local canonical storage
- Asset Registry + append-only Audit Event Log
- stages only files touched by this ingest
- commit + push to origin/main

No third-party dependencies.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

VERSION = "0.1"
MANIFEST = Path(
    "docs/project_control/gates/P0_2_visual_assets/"
    "migration_evidence/character_asset_migration_manifest_v1.csv"
)
REGISTRY = Path("production/asset_registry/asset_registry.jsonl")
AUDIT = Path("production/asset_registry/audit_event_log.jsonl")
RECEIPTS = Path("tmp/ingest_receipts")

CORE_ROLES = {
    "FACE_FRONT", "FACE_3Q_LEFT", "FACE_3Q_RIGHT",
    "PROFILE_LEFT", "PROFILE_RIGHT",
    "REAR_3Q_LEFT", "REAR_3Q_RIGHT",
    "BODY_FRONT", "BODY_BACK",
}
EXTRA_ROLES = {
    "UPPER_BODY_3Q_RIGHT",
    "STRUCTURE_FRONT_3Q_BODY_RIGHT",
    "REAR_TURN_45",
}
AUTHORITIES = {
    "MASTER", "AUXILIARY", "DERIVED", "CONTINUITY",
    "SUPPLEMENTARY", "LEGACY_SUPPLEMENTARY",
}
RESOLVER_USAGE = {"DEFAULT", "CONDITIONAL", "NEVER"}
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


class IngestError(RuntimeError):
    pass


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    r = subprocess.run(["git", "-C", str(repo), *args], text=True, capture_output=True)
    if check and r.returncode:
        raise IngestError((r.stderr or r.stdout).strip())
    return r


def repo_root() -> Path:
    r = subprocess.run(
        ["git", "-C", str(Path(__file__).resolve().parent), "rev-parse", "--show-toplevel"],
        text=True, capture_output=True
    )
    if r.returncode:
        raise IngestError("Script must run inside the black_lady_short_01 Git repository.")
    return Path(r.stdout.strip()).resolve()


def token(v: str, label: str) -> str:
    v = v.strip().upper()
    if not re.fullmatch(r"[A-Z0-9_]+", v):
        raise IngestError(f"Invalid {label}: {v}")
    return v


def validate_png(path: Path) -> None:
    if not path.is_file():
        raise IngestError(f"Source file not found: {path}")
    with path.open("rb") as f:
        if f.read(8) != PNG_MAGIC:
            raise IngestError("V0.1 only accepts real PNG files.")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest(repo: Path) -> list[dict[str, str]]:
    p = repo / MANIFEST
    if not p.exists():
        raise IngestError(f"Missing migration manifest: {p}")
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for i, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if raw.strip():
            try:
                rows.append(json.loads(raw))
            except json.JSONDecodeError as e:
                raise IngestError(f"Invalid JSONL: {path}:{i}") from e
    return rows


def append_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def entity_dir(entity: str) -> Path:
    if not entity.startswith("CHAR_"):
        raise IngestError("V0.1 supports Character entities only.")
    slug = entity.removeprefix("CHAR_").lower()
    return Path("production/image_library/character_references") / slug


def migration_rows(manifest, entity, role, variant, state):
    return [
        r for r in manifest
        if r.get("canonical_entity_id") == entity
        and r.get("new_role") == role
        and r.get("variant") == variant
        and r.get("state") == state
        and r.get("mapping_status") == "CONFIRMED"
    ]


def parse_canonical_filename(filename: str, manifest: list[dict], registry: list[dict]):
    """Match complete known tokens, never infer underscore boundaries by position."""
    if not re.fullmatch(r"CHAR_[A-Z0-9_]+_V\d{3}\.png", filename):
        raise IngestError("Filename must be a canonical Character PNG ending in _V###.png")
    entities = {r.get("canonical_entity_id") for r in manifest} | {
        r.get("entity_id") for r in registry
    }
    variants = {"DEFAULT"} | {r.get("variant") for r in manifest + registry}
    states = {"DEFAULT"} | {r.get("state") for r in manifest + registry}
    version = int(filename[-7:-4])
    matches = [
        (entity, role, variant, state, version)
        for entity in entities if entity and re.fullmatch(r"CHAR_[A-Z0-9_]+", entity)
        for role in CORE_ROLES | EXTRA_ROLES
        for variant in variants if variant and re.fullmatch(r"[A-Z0-9_]+", variant)
        for state in states if state and re.fullmatch(r"[A-Z0-9_]+", state)
        if filename == f"{entity}_{role}_{variant}_{state}_V{version:03d}.png"
    ]
    if len(matches) != 1:
        raise IngestError("Canonical filename cannot be parsed unambiguously")
    return matches[0]


def next_asset_id(manifest: list[dict[str, str]], registry: list[dict]) -> str:
    confirmed = sum(
        1 for r in manifest
        if r.get("mapping_status") == "CONFIRMED" and r.get("target_storage_path")
    )
    highest = confirmed
    for r in registry:
        m = re.fullmatch(r"AST_IMG_(\d{6})", str(r.get("asset_id", "")))
        if m:
            highest = max(highest, int(m.group(1)))
    return f"AST_IMG_{highest + 1:06d}"


def event_id() -> str:
    return "EVT_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ_") + uuid.uuid4().hex[:8].upper()


def parse_args():
    p = argparse.ArgumentParser(description="Automatic Ingest Controller V0.1")
    p.add_argument("--source", required=True)
    p.add_argument("--entity")
    p.add_argument("--role")
    p.add_argument("--variant")
    p.add_argument("--state")
    p.add_argument("--from-filename", action="store_true")
    p.add_argument("--authority", default="AUXILIARY", choices=sorted(AUTHORITIES))
    p.add_argument("--resolver-usage", default="DEFAULT", choices=sorted(RESOLVER_USAGE))
    p.add_argument("--task-id", default="P0.2-03")
    p.add_argument("--source-reference", default="PO approval in main Chat")
    p.add_argument("--po-approved", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--no-pull", action="store_true")
    p.add_argument("--no-push", action="store_true")
    return p.parse_args()


def main() -> int:
    a = parse_args()
    if not a.po_approved:
        raise IngestError("Blocked: --po-approved is required after explicit Product Owner approval.")

    source = Path(a.source).expanduser().resolve()
    validate_png(source)

    repo = repo_root()
    registry_path = repo / REGISTRY
    audit_path = repo / AUDIT

    pre_staged = git(repo, "diff", "--cached", "--name-only").stdout.strip()
    if pre_staged:
        raise IngestError("Pre-existing staged changes detected:\n" + pre_staged)

    if not a.dry_run and not a.no_pull:
        git(repo, "pull", "--ff-only", "origin", "main")

    manifest = load_manifest(repo)
    registry = load_jsonl(registry_path)
    if a.from_filename:
        if any((a.entity, a.role, a.variant, a.state)):
            raise IngestError("--from-filename cannot be combined with explicit identity fields")
        entity, role, variant, state, filename_version = parse_canonical_filename(
            source.name, manifest, registry
        )
    else:
        if not a.entity or not a.role:
            raise IngestError("--entity and --role are required unless --from-filename is used")
        entity = token(a.entity, "entity")
        role = token(a.role, "role")
        variant = token(a.variant or "DEFAULT", "variant")
        state = token(a.state or "DEFAULT", "state")
        filename_version = None
    if role not in CORE_ROLES | EXTRA_ROLES:
        raise IngestError(f"Role not allowed by V0.1: {role}")
    if not any(r.get("canonical_entity_id") == entity for r in manifest):
        raise IngestError(f"Unknown entity: {entity}")

    digest = sha256(source)

    for r in manifest:
        if r.get("mapping_status") == "CONFIRMED" and r.get("sha256") == digest:
            raise IngestError(f"Same binary already exists: {r.get('canonical_filename')}")
    for r in registry:
        if r.get("sha256") == digest:
            raise IngestError(f"Same binary already registered: {r.get('asset_id')}")

    migrated = migration_rows(manifest, entity, role, variant, state)
    migrated_current = [r for r in migrated if r.get("lifecycle") == "CURRENT"]
    runtime_current = [
        r for r in registry
        if r.get("entity_id") == entity
        and r.get("role") == role
        and r.get("variant") == variant
        and r.get("state") == state
        and r.get("lifecycle") == "CURRENT"
    ]
    if migrated_current or runtime_current:
        raise IngestError(
            f"Single Current conflict for {entity}/{role}/{variant}/{state}. "
            "V0.1 intentionally does not supersede automatically."
        )

    versions = []
    for r in migrated:
        try:
            versions.append(int(r.get("version_no") or 0))
        except ValueError:
            pass
    for r in registry:
        if (
            r.get("entity_id") == entity
            and r.get("role") == role
            and r.get("variant") == variant
            and r.get("state") == state
        ):
            versions.append(int(r.get("version_no") or 0))

    version_no = max(versions, default=0) + 1
    if filename_version is not None and filename_version != version_no:
        raise IngestError(
            f"Filename version V{filename_version:03d} does not match next version V{version_no:03d}"
        )
    vtag = f"V{version_no:03d}"
    filename = f"{entity}_{role}_{variant}_{state}_{vtag}.png"
    rel_target = entity_dir(entity) / filename
    target = repo / rel_target
    asset_id = next_asset_id(manifest, registry)
    timestamp = now_utc()

    asset = {
        "asset_id": asset_id,
        "entity_id": entity,
        "shot_id": None,
        "media_code": "IMG",
        "asset_class": "ATOMIC",
        "role": role,
        "variant": variant,
        "state": state,
        "version_no": version_no,
        "approval_status": "APPROVED",
        "lifecycle": "CURRENT",
        "authority_class": a.authority,
        "resolver_usage": a.resolver_usage,
        "provenance_status": "COMPLETE",
        "filename": filename,
        "storage_uri": rel_target.as_posix(),
        "sha256": digest,
        "mime_type": "image/png",
        "byte_size": source.stat().st_size,
        "approved_at": timestamp,
        "ingested_at": timestamp,
        "task_id": a.task_id,
        "source_reference": a.source_reference,
        "controller_version": VERSION,
    }

    events = [
        {
            "event_id": event_id(),
            "event_time": timestamp,
            "event_type": "ASSET_APPROVED",
            "entity_id": entity,
            "asset_id": asset_id,
            "actor_type": "PRODUCT_OWNER",
            "actor_id": "PRODUCT_OWNER",
            "previous_value": None,
            "new_value": {"approval_status": "APPROVED"},
            "reason": "Explicit Product Owner approval before formal ingest.",
            "task_id": a.task_id,
            "source_reference": a.source_reference,
        },
        {
            "event_id": event_id(),
            "event_time": timestamp,
            "event_type": "ASSET_INGESTED",
            "entity_id": entity,
            "asset_id": asset_id,
            "actor_type": "SYSTEM",
            "actor_id": "AUTOMATIC_INGEST_CONTROLLER_V0.1",
            "previous_value": None,
            "new_value": {
                "storage_uri": rel_target.as_posix(),
                "sha256": digest,
                "lifecycle": "CURRENT",
                "resolver_usage": a.resolver_usage,
            },
            "reason": "Automatic formal ingest of an approved production asset.",
            "task_id": a.task_id,
            "source_reference": a.source_reference,
        },
    ]

    result = {
        "status": "DRY_RUN" if a.dry_run else "READY",
        "asset_id": asset_id,
        "entity_id": entity,
        "role": role,
        "version_no": version_no,
        "filename": filename,
        "canonical_filename": filename,
        "storage_uri": rel_target.as_posix(),
        "sha256": digest,
        "byte_size": source.stat().st_size,
    }

    if a.dry_run:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    if target.exists():
        raise IngestError(f"Target already exists: {rel_target}")

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    if sha256(target) != digest:
        target.unlink(missing_ok=True)
        raise IngestError("SHA mismatch after copy; ingest aborted.")

    append_jsonl(registry_path, [asset])
    append_jsonl(audit_path, events)

    touched = [rel_target.as_posix(), REGISTRY.as_posix(), AUDIT.as_posix()]
    git(repo, "add", "--", *touched)

    actual_staged = set(git(repo, "diff", "--cached", "--name-only").stdout.splitlines())
    if actual_staged != set(touched):
        git(repo, "reset", "HEAD", "--", *touched, check=False)
        raise IngestError(
            "Safety stop: staged set differs from expected.\n"
            f"Expected: {sorted(touched)}\nActual: {sorted(actual_staged)}"
        )

    git(repo, "commit", "-m", f"P0.2 ingest {entity} {role} {vtag}")
    commit_sha = git(repo, "rev-parse", "HEAD").stdout.strip()

    push_status = "SKIPPED"
    if not a.no_push:
        r = git(
            repo, "-c", "http.postBuffer=524288000",
            "push", "origin", "main", check=False
        )
        if r.returncode:
            raise IngestError(
                f"Local commit {commit_sha} created but push failed:\n"
                f"{(r.stderr or r.stdout).strip()}\n"
                "Fix network and run: git push origin main"
            )
        push_status = "PUSHED"

    result.update({
        "status": "COMPLETE",
        "git_commit": commit_sha,
        "push_status": push_status,
        "completed_at": now_utc(),
        "asset_registry": REGISTRY.as_posix(),
        "audit_log": AUDIT.as_posix(),
    })

    receipt_dir = repo / RECEIPTS
    receipt_dir.mkdir(parents=True, exist_ok=True)
    receipt = receipt_dir / f"{asset_id}_{entity}_{role}_{vtag}.json"
    receipt.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except IngestError as e:
        print(f"[INGEST BLOCKED] {e}", file=sys.stderr)
        raise SystemExit(2)
