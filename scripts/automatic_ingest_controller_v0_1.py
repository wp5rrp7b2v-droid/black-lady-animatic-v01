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
import os
import re
import shutil
import subprocess
import sys
import tempfile
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
RELATIONS = Path("production/asset_registry/asset_relations.jsonl")
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


def jsonl_bytes(rows: list[dict]) -> bytes:
    return b"".join((json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8") for row in rows)


def fsync_dir(path: Path) -> None:
    directory_fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(directory_fd)
    finally:
        os.close(directory_fd)


def atomic_bytes(path: Path, data: bytes) -> None:
    """Replace one file durably. The caller owns cross-file rollback."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as out:
            out.write(data)
            out.flush()
            os.fsync(out.fileno())
        os.replace(name, path)
        fsync_dir(path.parent)
    finally:
        Path(name).unlink(missing_ok=True)


def safe_registered_path(repo: Path, uri: str) -> Path:
    rel = Path(uri)
    if rel.is_absolute() or ".." in rel.parts or not uri.startswith("production/image_library/character_references/"):
        raise IngestError("Registered storage path escape")
    path = repo / rel
    if path.is_symlink() or not path.resolve().is_relative_to(repo.resolve()):
        raise IngestError("Registered storage path escape or symlink")
    return path


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
    p.add_argument("--supersede-current", action="store_true")
    p.add_argument(
        "--adopt-existing",
        action="store_true",
        help="Adopt a byte-identical PNG already published at its exact canonical Git path; never copy/rewrite it.",
    )
    p.add_argument(
        "--reserve-version",
        action="append",
        type=int,
        default=[],
        help="Explicitly reserve an intentionally rejected/do-not-ingest version number. Reservations must be contiguous.",
    )
    p.add_argument("--inspect-current", action="store_true", help="Read-only launcher preflight")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--no-pull", action="store_true")
    p.add_argument("--no-push", action="store_true")
    return p.parse_args()


def main() -> int:
    a = parse_args()
    if not a.po_approved and not a.inspect_current:
        raise IngestError("Blocked: --po-approved is required after explicit Product Owner approval.")
    if a.inspect_current and a.supersede_current:
        raise IngestError("--inspect-current cannot be combined with --supersede-current")
    if a.inspect_current and (a.adopt_existing or a.reserve_version):
        raise IngestError("--inspect-current cannot be combined with adoption/version-reservation flags")
    if a.adopt_existing and a.supersede_current:
        raise IngestError("--adopt-existing cannot be combined with --supersede-current")
    if a.reserve_version and not a.adopt_existing:
        raise IngestError("--reserve-version is allowed only with --adopt-existing")

    source = Path(a.source).expanduser().resolve()
    validate_png(source)

    repo = repo_root()
    registry_path = repo / REGISTRY
    audit_path = repo / AUDIT
    relations_path = repo / RELATIONS

    pre_staged = git(repo, "diff", "--cached", "--name-only").stdout.strip()
    if pre_staged:
        raise IngestError("Pre-existing staged changes detected:\n" + pre_staged)

    if not a.dry_run and not a.inspect_current and not a.no_pull:
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
    if a.inspect_current:
        if len(runtime_current) > 1:
            raise IngestError("Multiple runtime CURRENT assets")
        old = runtime_current[0] if runtime_current else None
        print(json.dumps({
            "status": "CURRENT_FOUND" if old else "NO_CURRENT",
            "old_asset_id": old.get("asset_id") if old else None,
            "old_filename": old.get("filename") if old else None,
            "new_filename": source.name,
            "migration_only": bool(migrated_current and not old),
        }, ensure_ascii=False))
        return 0

    digest = sha256(source)
    for r in manifest:
        if r.get("mapping_status") == "CONFIRMED" and r.get("sha256") == digest:
            raise IngestError(f"DUPLICATE_BINARY: {r.get('canonical_filename')}")
    for r in registry:
        if r.get("sha256") == digest:
            raise IngestError(f"DUPLICATE_BINARY: {r.get('asset_id')}")

    old = None
    if a.supersede_current:
        if len(runtime_current) == 0 and migrated_current:
            raise IngestError("LEGACY_CURRENT_NOT_RUNTIME_MANAGED")
        if len(runtime_current) != 1:
            raise IngestError(f"Controlled supersession requires exactly one runtime CURRENT; found {len(runtime_current)}")
        old = runtime_current[0]
        if old.get("approval_status") != "APPROVED" or old.get("lifecycle") != "CURRENT":
            raise IngestError("Old CURRENT must be APPROVED and CURRENT")
        old_path = safe_registered_path(repo, str(old.get("storage_uri", "")))
        if old_path.name != old.get("filename") or not old_path.is_file():
            raise IngestError("Old CURRENT file missing or filename mismatch")
        if sha256(old_path) != old.get("sha256"):
            raise IngestError("SHA mismatch for old CURRENT")
        if digest == old.get("sha256"):
            raise IngestError("DUPLICATE_BINARY")
    elif migrated_current or runtime_current:
        raise IngestError(
            f"Single Current conflict for {entity}/{role}/{variant}/{state}. "
            "Use explicit --supersede-current with --po-approved for controlled replacement."
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

    next_version = max(versions, default=0) + 1
    reserved = list(a.reserve_version or [])
    if len(reserved) != len(set(reserved)) or any(v <= 0 for v in reserved):
        raise IngestError("Version safety: --reserve-version values must be unique positive integers")
    if old is not None and reserved:
        raise IngestError("Version safety: controlled supersession cannot reserve skipped versions")

    if old is not None:
        version_no = next_version
    elif a.adopt_existing and filename_version is not None and filename_version > next_version:
        required = list(range(next_version, filename_version))
        if sorted(reserved) != required:
            raise IngestError(
                "Version safety: filename skips version(s); acknowledge every skipped version "
                "contiguously with --reserve-version"
            )
        version_no = filename_version
    else:
        if reserved:
            raise IngestError("Version safety: reservation supplied but no adopt-existing version gap exists")
        version_no = next_version

    if old is not None and version_no != int(old.get("version_no") or 0) + 1:
        raise IngestError("Version safety: new version must equal old version + 1")
    if filename_version is not None and filename_version != version_no:
        raise IngestError(
            f"Filename version V{filename_version:03d} does not match next version V{version_no:03d}"
        )
    vtag = f"V{version_no:03d}"
    filename = f"{entity}_{role}_{variant}_{state}_{vtag}.png"
    rel_target = entity_dir(entity) / filename
    target = repo / rel_target

    if a.adopt_existing:
        if source != target.resolve():
            raise IngestError(
                "Adopt-existing requires --source to be the exact canonical target path"
            )
        if target.is_symlink() or not target.is_file():
            raise IngestError("Adopt-existing requires an existing regular canonical PNG")
        tracked = git(repo, "ls-files", "--error-unmatch", "--", rel_target.as_posix(), check=False)
        if tracked.returncode != 0:
            raise IngestError("Adopt-existing requires the canonical PNG to be Git-tracked")
        binary_dirty = git(repo, "status", "--porcelain", "--", rel_target.as_posix()).stdout.strip()
        if binary_dirty:
            raise IngestError("Adopt-existing requires the canonical PNG to have no uncommitted changes")
        if sha256(target) != digest:
            raise IngestError("Adopt-existing canonical SHA mismatch")
    elif target.exists() or target.is_symlink():
        raise IngestError(f"Target already exists: {rel_target}")
    asset_id = next_asset_id(manifest, registry)
    relations = load_jsonl(relations_path) if old is not None else []
    if old is not None:
        if any(r.get("source_asset_id") == asset_id or
               (r.get("relation_type") == "SUPERSEDES" and r.get("target_asset_id") == old.get("asset_id"))
               for r in relations):
            raise IngestError("Contradictory or duplicate SUPERSEDES relation")
        if asset_id == old.get("asset_id"):
            raise IngestError("SUPERSEDES source and target must differ")
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
    relation = None
    if old is not None:
        superseded_event = {
            "event_id": event_id(),
            "event_time": timestamp,
            "event_type": "ASSET_SUPERSEDED",
            "entity_id": entity,
            "asset_id": old["asset_id"],
            "actor_type": "PRODUCT_OWNER",
            "actor_id": "PRODUCT_OWNER",
            "previous_value": {"lifecycle": "CURRENT"},
            "new_value": {"lifecycle": "SUPERSEDED", "superseded_by": asset_id},
            "reason": "Product Owner approved controlled replacement of CURRENT asset.",
            "task_id": a.task_id,
            "source_reference": a.source_reference,
        }
        events.append(superseded_event)
        events[1]["new_value"]["supersedes_asset_id"] = old["asset_id"]
        relation = {
            "source_asset_id": asset_id,
            "relation_type": "SUPERSEDES",
            "target_asset_id": old["asset_id"],
            "created_at": timestamp,
            "created_by_event_id": superseded_event["event_id"],
        }

    result = {
        "status": "DRY_RUN" if a.dry_run else "READY",
        "mode": (
            "SUPERSEDE_CURRENT" if old is not None
            else "ADOPT_EXISTING" if a.adopt_existing
            else "NORMAL_INGEST"
        ),
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
    if old is not None:
        result.update({
            "old_asset_id": old["asset_id"], "old_filename": old["filename"],
            "old_version": int(old["version_no"]), "new_asset_id": asset_id,
            "new_filename": filename, "new_version": version_no,
            "relation": "NEW SUPERSEDES OLD",
        })

    if a.dry_run:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    touched = [REGISTRY.as_posix(), AUDIT.as_posix()]
    if not a.adopt_existing:
        touched.insert(0, rel_target.as_posix())
    if old is not None:
        touched.append(RELATIONS.as_posix())
    dirty = git(repo, "status", "--porcelain", "--", *touched).stdout.strip()
    if dirty:
        raise IngestError("Pre-existing changes in ingest targets:\n" + dirty)

    file_paths = [registry_path, audit_path] + ([relations_path] if old is not None else [])
    before = {path: path.read_bytes() if path.exists() else None for path in file_paths}
    updated_registry = [({**r, "lifecycle": "SUPERSEDED"} if r is old else r) for r in registry] + [asset]
    registry_data = jsonl_bytes(updated_registry) if old is not None else (before[registry_path] or b"") + jsonl_bytes([asset])
    audit_data = (before[audit_path] or b"") + jsonl_bytes(events)
    relation_data = (before.get(relations_path) or b"") + jsonl_bytes([relation]) if relation else None

    def write_and_stage_formal_files() -> None:
        atomic_bytes(registry_path, registry_data)
        if relation_data is not None:
            atomic_bytes(relations_path, relation_data)
        atomic_bytes(audit_path, audit_data)
        git(repo, "add", "--", *touched)
        actual_staged = set(git(repo, "diff", "--cached", "--name-only").stdout.splitlines())
        if actual_staged != set(touched):
            raise IngestError(
                "Safety stop: staged set differs from expected.\n"
                f"Expected: {sorted(touched)}\nActual: {sorted(actual_staged)}"
            )

    if a.adopt_existing:
        # The canonical PNG is already the approved Git-tracked binary. Never copy, delete,
        # rewrite, re-encode, replace, or stage it in adoption mode.
        binary_before = sha256(target)
        try:
            write_and_stage_formal_files()
            # Check the binary invariant before creating a commit so rollback remains complete.
            if sha256(target) != binary_before or binary_before != digest:
                raise IngestError("Adopt-existing invariant failed: canonical PNG bytes changed")
            git(repo, "commit", "-m", f"P0.2 adopt {entity} {role} {vtag}")
        except Exception as write_error:
            git(repo, "reset", "HEAD", "--", *touched, check=False)
            rollback_errors = []
            for path, data in before.items():
                try:
                    if data is None:
                        path.unlink(missing_ok=True)
                    else:
                        atomic_bytes(path, data)
                except OSError as e:
                    rollback_errors.append(f"{path}: {e}")
            if rollback_errors:
                raise IngestError("Rollback failed: " + "; ".join(rollback_errors)) from write_error
            raise
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        fd, copied_name = tempfile.mkstemp(prefix=f".{filename}.", dir=target.parent)
        try:
            with os.fdopen(fd, "wb") as out, source.open("rb") as incoming:
                shutil.copyfileobj(incoming, out)
                out.flush()
                os.fsync(out.fileno())
            if sha256(Path(copied_name)) != digest:
                raise IngestError("SHA mismatch after copy; ingest aborted.")
            # All pre-write checks are complete; roll back every formal file on any write/stage/commit failure.
            try:
                os.replace(copied_name, target)
                fsync_dir(target.parent)
                write_and_stage_formal_files()
                git(repo, "commit", "-m", f"P0.2 {'supersede' if old else 'ingest'} {entity} {role} {vtag}")
            except Exception as write_error:
                git(repo, "reset", "HEAD", "--", *touched, check=False)
                rollback_errors = []
                for path, data in before.items():
                    try:
                        if data is None:
                            path.unlink(missing_ok=True)
                        else:
                            atomic_bytes(path, data)
                    except OSError as e:
                        rollback_errors.append(f"{path}: {e}")
                target.unlink(missing_ok=True)
                if rollback_errors:
                    raise IngestError("Rollback failed: " + "; ".join(rollback_errors)) from write_error
                raise
        finally:
            Path(copied_name).unlink(missing_ok=True)

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
