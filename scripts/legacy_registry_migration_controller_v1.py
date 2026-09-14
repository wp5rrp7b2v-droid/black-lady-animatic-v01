#!/usr/bin/env python3
"""
AO-02 Legacy Registry Migration Controller V1.0

Migrates the 48 D-059 CONFIRMED + APPROVED legacy Character assets into the
formal long-term Asset Registry / Audit model.

Safety model:
- no PNG copy/rename/regeneration
- default is read-only dry-run; --apply is required to mutate
- deterministic AST_IMG_000001..000048 allocation
- all validation completes before any write
- cross-file rollback on write failure
- idempotent: successful second run => ALREADY_APPLIED / NO CHANGE
- partial/conflicting migration => stop without self-repair
- no Git pull/commit/push; publication is a separate boundary

No third-party dependencies.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import tempfile
import uuid
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

VERSION = "1.0"
TASK_ID = "P0.2-04/AO-02"
MIGRATION_SOURCE = "D-059"

MANIFEST = Path(
    "docs/project_control/gates/P0_2_visual_assets/"
    "migration_evidence/character_asset_migration_manifest_v1.csv"
)
REGISTRY = Path("production/asset_registry/asset_registry.jsonl")
RELATIONS = Path("production/asset_registry/asset_relations.jsonl")
AUDIT = Path("production/asset_registry/audit_event_log.jsonl")
MIGRATION_MAP = Path(
    "docs/project_control/gates/P0_2_visual_assets/"
    "migration_evidence/ao02_legacy_asset_registry_migration_map_v1.csv"
)

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
ASSET_ID_RE = re.compile(r"AST_IMG_(\d{6})$")
EXPECTED_ELIGIBLE = 48
EXPECTED_FIRST_ID = 1
EXPECTED_LAST_ID = 48
EXCLUDED_LEGACY_ID = "CHAR_NEIL_REAR_TURN_45_SUPPLEMENTARY"

MAP_FIELDS = [
    "legacy_asset_id",
    "asset_id",
    "canonical_entity_id",
    "role",
    "variant",
    "state",
    "version_no",
    "lifecycle",
    "canonical_filename",
    "storage_uri",
    "sha256",
    "migration_status",
]


class MigrationError(RuntimeError):
    pass


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def event_id() -> str:
    return "EVT_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ_") + uuid.uuid4().hex[:8].upper()


def repo_root() -> Path:
    import subprocess

    r = subprocess.run(
        ["git", "-C", str(Path(__file__).resolve().parent), "rev-parse", "--show-toplevel"],
        text=True,
        capture_output=True,
    )
    if r.returncode:
        raise MigrationError("Script must run inside the black_lady_short_01 Git repository.")
    return Path(r.stdout.strip()).resolve()


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise MigrationError(f"Missing CSV: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows: list[dict] = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            rows.append(json.loads(raw))
        except json.JSONDecodeError as exc:
            raise MigrationError(f"Invalid JSONL: {path}:{line_no}") from exc
    return rows


def jsonl_bytes(rows: list[dict]) -> bytes:
    return b"".join(
        (json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")
        for row in rows
    )


def csv_bytes(rows: list[dict], fields: list[str]) -> bytes:
    buf = io.StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue().encode("utf-8")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_png(path: Path) -> None:
    if not path.is_file():
        raise MigrationError(f"Canonical PNG missing: {path}")
    if path.is_symlink():
        raise MigrationError(f"Canonical PNG must not be a symlink: {path}")
    with path.open("rb") as f:
        if f.read(8) != PNG_MAGIC:
            raise MigrationError(f"Not a valid PNG by signature: {path}")


def parse_positive_int(value: str, label: str) -> int:
    try:
        result = int(value)
    except (TypeError, ValueError) as exc:
        raise MigrationError(f"Invalid integer {label}: {value!r}") from exc
    if result < 1:
        raise MigrationError(f"{label} must be >= 1: {result}")
    return result


def normalize_approval_date(value: str, legacy_asset_id: str) -> str:
    value = (value or "").strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise MigrationError(
            f"Missing or invalid provable approval date for {legacy_asset_id}: {value!r}"
        )
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError as exc:
        raise MigrationError(
            f"Invalid approval calendar date for {legacy_asset_id}: {value!r}"
        ) from exc
    return value + "T00:00:00Z"


def eligible_manifest_rows(manifest: list[dict[str, str]]) -> list[dict[str, str]]:
    rows = [
        row
        for row in manifest
        if row.get("mapping_status") == "CONFIRMED"
        and row.get("approval_status") == "APPROVED"
        and (row.get("target_storage_path") or "").strip()
        and (row.get("canonical_filename") or "").strip()
    ]
    if len(rows) != EXPECTED_ELIGIBLE:
        raise MigrationError(
            f"Eligible migration count must be exactly {EXPECTED_ELIGIBLE}; found {len(rows)}"
        )
    return rows


def validate_exclusion(manifest: list[dict[str, str]]) -> None:
    matches = [r for r in manifest if r.get("legacy_asset_id") == EXCLUDED_LEGACY_ID]
    if len(matches) != 1:
        raise MigrationError(
            f"Expected exactly one excluded Neil legacy row {EXCLUDED_LEGACY_ID}; found {len(matches)}"
        )
    row = matches[0]
    if row.get("mapping_status") != "MAPPING_REQUIRED":
        raise MigrationError(
            f"Excluded Neil row must remain MAPPING_REQUIRED; found {row.get('mapping_status')!r}"
        )
    if (row.get("target_storage_path") or "").strip():
        raise MigrationError("Excluded Neil row unexpectedly has a canonical target path")


def deterministic_sort_key(row: dict[str, str]):
    return (
        row.get("canonical_entity_id") or "",
        row.get("new_role") or "",
        row.get("variant") or "",
        row.get("state") or "",
        parse_positive_int(row.get("version_no") or "", "version_no"),
        row.get("canonical_filename") or "",
    )


def validate_manifest_row(repo: Path, row: dict[str, str]) -> dict:
    legacy_id = (row.get("legacy_asset_id") or "").strip()
    if not legacy_id:
        raise MigrationError("Eligible manifest row missing legacy_asset_id")

    entity = (row.get("canonical_entity_id") or "").strip()
    role = (row.get("new_role") or "").strip()
    variant = (row.get("variant") or "").strip()
    state = (row.get("state") or "").strip()
    lifecycle = (row.get("lifecycle") or "").strip()
    authority = (row.get("authority_class") or "").strip()
    resolver_usage = (row.get("resolver_usage") or "").strip()
    filename = (row.get("canonical_filename") or "").strip()
    storage_uri = (row.get("target_storage_path") or "").strip()
    digest = (row.get("sha256") or "").strip().lower()
    mime_type = (row.get("mime_type") or "").strip().lower()
    version_no = parse_positive_int(row.get("version_no") or "", "version_no")
    expected_size = parse_positive_int(row.get("byte_size") or "", "byte_size")

    if not re.fullmatch(r"CHAR_[A-Z0-9_]+", entity):
        raise MigrationError(f"Invalid canonical entity for {legacy_id}: {entity!r}")
    if not re.fullmatch(r"[A-Z0-9_]+", role):
        raise MigrationError(f"Invalid role for {legacy_id}: {role!r}")
    if not re.fullmatch(r"[A-Z0-9_]+", variant):
        raise MigrationError(f"Invalid variant for {legacy_id}: {variant!r}")
    if not re.fullmatch(r"[A-Z0-9_]+", state):
        raise MigrationError(f"Invalid state for {legacy_id}: {state!r}")
    if lifecycle not in {"CURRENT", "SUPERSEDED", "DEPRECATED", "ARCHIVED"}:
        raise MigrationError(f"Invalid lifecycle for {legacy_id}: {lifecycle!r}")
    if authority not in {
        "MASTER", "AUXILIARY", "DERIVED", "CONTINUITY", "SUPPLEMENTARY", "LEGACY_SUPPLEMENTARY"
    }:
        raise MigrationError(f"Invalid authority_class for {legacy_id}: {authority!r}")
    if resolver_usage not in {"DEFAULT", "CONDITIONAL", "NEVER"}:
        raise MigrationError(f"Invalid resolver_usage for {legacy_id}: {resolver_usage!r}")
    if mime_type != "image/png":
        raise MigrationError(f"MIME must be image/png for {legacy_id}; found {mime_type!r}")
    if not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise MigrationError(f"Invalid SHA-256 for {legacy_id}")

    rel = Path(storage_uri)
    if rel.is_absolute() or ".." in rel.parts:
        raise MigrationError(f"Unsafe storage path for {legacy_id}: {storage_uri}")
    if not storage_uri.startswith("production/image_library/character_references/"):
        raise MigrationError(f"Unexpected storage root for {legacy_id}: {storage_uri}")
    if rel.name != filename:
        raise MigrationError(f"Filename/storage mismatch for {legacy_id}")

    path = repo / rel
    validate_png(path)
    actual_size = path.stat().st_size
    if actual_size != expected_size:
        raise MigrationError(
            f"Byte-size mismatch for {legacy_id}: manifest={expected_size}, actual={actual_size}"
        )
    actual_sha = sha256(path)
    if actual_sha != digest:
        raise MigrationError(
            f"SHA mismatch for {legacy_id}: manifest={digest}, actual={actual_sha}"
        )

    approved_at = normalize_approval_date(row.get("legacy_review_date") or "", legacy_id)

    return {
        "legacy_asset_id": legacy_id,
        "entity_id": entity,
        "role": role,
        "variant": variant,
        "state": state,
        "version_no": version_no,
        "lifecycle": lifecycle,
        "authority_class": authority,
        "resolver_usage": resolver_usage,
        "filename": filename,
        "storage_uri": storage_uri,
        "sha256": digest,
        "byte_size": expected_size,
        "approved_at": approved_at,
    }


def validate_existing_runtime(registry: list[dict]) -> None:
    ids = {r.get("asset_id") for r in registry}
    expected = {"AST_IMG_000049", "AST_IMG_000050", "AST_IMG_000051"}
    if ids != expected:
        raise MigrationError(
            "Pre-AO-02 runtime Registry must contain exactly AST_IMG_000049..000051; "
            f"found {sorted(str(x) for x in ids)}"
        )


def migration_state(registry: list[dict], map_path: Path) -> str:
    legacy = [
        r for r in registry
        if isinstance(r.get("asset_id"), str)
        and ASSET_ID_RE.fullmatch(r["asset_id"])
        and EXPECTED_FIRST_ID <= int(r["asset_id"][-6:]) <= EXPECTED_LAST_ID
    ]
    if not legacy and not map_path.exists():
        return "NOT_APPLIED"
    if len(legacy) == EXPECTED_ELIGIBLE and map_path.exists():
        return "POSSIBLY_APPLIED"
    return "PARTIAL_OR_CONFLICTING_MIGRATION"


def current_key(asset: dict):
    return (
        asset.get("entity_id"),
        asset.get("role"),
        asset.get("variant"),
        asset.get("state"),
    )


def version_key(asset: dict):
    return current_key(asset) + (int(asset.get("version_no") or 0),)


def validate_combined_registry(rows: list[dict]) -> None:
    seen_ids: set[str] = set()
    seen_storage: set[str] = set()
    seen_versions: set[tuple] = set()
    current_counts: defaultdict[tuple, int] = defaultdict(int)

    for row in rows:
        asset_id = str(row.get("asset_id") or "")
        storage_uri = str(row.get("storage_uri") or "")
        if asset_id in seen_ids:
            raise MigrationError(f"Duplicate Asset ID: {asset_id}")
        seen_ids.add(asset_id)
        if storage_uri in seen_storage:
            raise MigrationError(f"Duplicate storage URI: {storage_uri}")
        seen_storage.add(storage_uri)
        vk = version_key(row)
        if vk in seen_versions:
            raise MigrationError(f"Duplicate entity/role/variant/state/version: {vk}")
        seen_versions.add(vk)
        if row.get("lifecycle") == "CURRENT":
            current_counts[current_key(row)] += 1

    conflicts = [key for key, count in current_counts.items() if count > 1]
    if conflicts:
        raise MigrationError(f"Single Current conflict(s): {conflicts}")


def planned_legacy_assets(repo: Path, manifest: list[dict[str, str]], ingested_at: str) -> tuple[list[dict], list[dict]]:
    eligible = eligible_manifest_rows(manifest)
    validated = [validate_manifest_row(repo, row) for row in eligible]
    by_legacy = {item["legacy_asset_id"]: item for item in validated}
    if len(by_legacy) != EXPECTED_ELIGIBLE:
        raise MigrationError("Duplicate legacy_asset_id among eligible rows")

    sorted_source = sorted(eligible, key=deterministic_sort_key)
    assets: list[dict] = []
    map_rows: list[dict] = []

    for index, source_row in enumerate(sorted_source, EXPECTED_FIRST_ID):
        item = by_legacy[source_row["legacy_asset_id"]]
        asset_id = f"AST_IMG_{index:06d}"
        asset = {
            "asset_id": asset_id,
            "entity_id": item["entity_id"],
            "shot_id": None,
            "media_code": "IMG",
            "asset_class": "ATOMIC",
            "role": item["role"],
            "variant": item["variant"],
            "state": item["state"],
            "version_no": item["version_no"],
            "approval_status": "APPROVED",
            "lifecycle": item["lifecycle"],
            "authority_class": item["authority_class"],
            "resolver_usage": item["resolver_usage"],
            "provenance_status": "PARTIAL",
            "filename": item["filename"],
            "storage_uri": item["storage_uri"],
            "sha256": item["sha256"],
            "mime_type": "image/png",
            "byte_size": item["byte_size"],
            "approved_at": item["approved_at"],
            "approval_time_precision": "DATE_ONLY",
            "ingested_at": ingested_at,
            "legacy_asset_id": item["legacy_asset_id"],
            "migration_source": MIGRATION_SOURCE,
            "task_id": TASK_ID,
            "source_reference": "AO-02 Long-term Registry Migration Design V1 / D-059 Migration Manifest",
            "controller_version": VERSION,
        }
        assets.append(asset)
        map_rows.append({
            "legacy_asset_id": item["legacy_asset_id"],
            "asset_id": asset_id,
            "canonical_entity_id": item["entity_id"],
            "role": item["role"],
            "variant": item["variant"],
            "state": item["state"],
            "version_no": item["version_no"],
            "lifecycle": item["lifecycle"],
            "canonical_filename": item["filename"],
            "storage_uri": item["storage_uri"],
            "sha256": item["sha256"],
            "migration_status": "MIGRATED",
        })

    if assets[0]["asset_id"] != "AST_IMG_000001" or assets[-1]["asset_id"] != "AST_IMG_000048":
        raise MigrationError("Deterministic legacy Asset ID range is not 000001..000048")
    return assets, map_rows


def provable_relations(combined: list[dict], existing_relations: list[dict], timestamp: str) -> tuple[list[dict], list[dict]]:
    groups: defaultdict[tuple, list[dict]] = defaultdict(list)
    for asset in combined:
        groups[current_key(asset)].append(asset)

    existing_keys = {
        (r.get("source_asset_id"), r.get("relation_type"), r.get("target_asset_id"))
        for r in existing_relations
    }
    new_relations: list[dict] = []
    relation_events: list[dict] = []

    for key, members in groups.items():
        members = sorted(members, key=lambda a: int(a.get("version_no") or 0))
        # Conservative evidence rule: only an unambiguous two-version pair is inferred.
        if len(members) != 2:
            continue
        old, new = members
        if old.get("lifecycle") != "SUPERSEDED" or new.get("lifecycle") != "CURRENT":
            continue
        if int(new.get("version_no") or 0) <= int(old.get("version_no") or 0):
            continue
        relation_key = (new["asset_id"], "SUPERSEDES", old["asset_id"])
        if relation_key in existing_keys:
            continue
        evt_id = event_id()
        relation = {
            "source_asset_id": new["asset_id"],
            "relation_type": "SUPERSEDES",
            "target_asset_id": old["asset_id"],
            "created_at": timestamp,
            "created_by_event_id": evt_id,
        }
        event = {
            "event_id": evt_id,
            "event_time": timestamp,
            "event_type": "RELATION_CREATED",
            "entity_id": new.get("entity_id"),
            "asset_id": new["asset_id"],
            "actor_type": "SYSTEM",
            "actor_id": "LEGACY_REGISTRY_MIGRATION_CONTROLLER_V1",
            "previous_value": None,
            "new_value": {
                "relation_type": "SUPERSEDES",
                "source_asset_id": new["asset_id"],
                "target_asset_id": old["asset_id"],
            },
            "reason": "AO-02 created an unambiguous formally evidenced SUPERSEDES relation.",
            "task_id": TASK_ID,
            "source_reference": "AO-02 Long-term Registry Migration Design V1 / D-059 Migration Manifest",
        }
        new_relations.append(relation)
        relation_events.append(event)
        existing_keys.add(relation_key)

    return new_relations, relation_events


def migration_events(assets: list[dict], timestamp: str) -> list[dict]:
    rows = []
    for asset in assets:
        rows.append({
            "event_id": event_id(),
            "event_time": timestamp,
            "event_type": "ASSET_MIGRATED",
            "entity_id": asset["entity_id"],
            "asset_id": asset["asset_id"],
            "actor_type": "SYSTEM",
            "actor_id": "LEGACY_REGISTRY_MIGRATION_CONTROLLER_V1",
            "previous_value": None,
            "new_value": {
                "migration_source": MIGRATION_SOURCE,
                "legacy_asset_id": asset["legacy_asset_id"],
                "storage_uri": asset["storage_uri"],
                "sha256": asset["sha256"],
                "lifecycle": asset["lifecycle"],
                "provenance_status": "PARTIAL",
            },
            "reason": "AO-02 migrated an already-approved D-059 legacy asset into the formal long-term Registry/Audit model.",
            "task_id": TASK_ID,
            "source_reference": "AO-02 Long-term Registry Migration Design V1 / D-059 Migration Manifest",
        })
    return rows


def validate_applied_state(registry: list[dict], map_path: Path, manifest: list[dict[str, str]]) -> None:
    legacy_assets = [
        r for r in registry
        if isinstance(r.get("asset_id"), str)
        and ASSET_ID_RE.fullmatch(r["asset_id"])
        and EXPECTED_FIRST_ID <= int(r["asset_id"][-6:]) <= EXPECTED_LAST_ID
    ]
    if len(legacy_assets) != EXPECTED_ELIGIBLE or not map_path.is_file():
        raise MigrationError("PARTIAL_OR_CONFLICTING_MIGRATION")

    map_rows = load_csv(map_path)
    if len(map_rows) != EXPECTED_ELIGIBLE:
        raise MigrationError("PARTIAL_OR_CONFLICTING_MIGRATION: migration map row count mismatch")

    eligible = eligible_manifest_rows(manifest)
    expected_ids = {f"AST_IMG_{i:06d}" for i in range(1, EXPECTED_LAST_ID + 1)}
    if {r.get("asset_id") for r in legacy_assets} != expected_ids:
        raise MigrationError("PARTIAL_OR_CONFLICTING_MIGRATION: legacy Asset ID set mismatch")
    if {r.get("asset_id") for r in map_rows} != expected_ids:
        raise MigrationError("PARTIAL_OR_CONFLICTING_MIGRATION: migration map Asset ID set mismatch")

    # Recompute the deterministic identity mapping without changing timestamps.
    sorted_source = sorted(eligible, key=deterministic_sort_key)
    expected_pairs = {
        source["legacy_asset_id"]: f"AST_IMG_{index:06d}"
        for index, source in enumerate(sorted_source, 1)
    }
    actual_pairs = {r.get("legacy_asset_id"): r.get("asset_id") for r in legacy_assets}
    map_pairs = {r.get("legacy_asset_id"): r.get("asset_id") for r in map_rows}
    if actual_pairs != expected_pairs or map_pairs != expected_pairs:
        raise MigrationError("PARTIAL_OR_CONFLICTING_MIGRATION: deterministic mapping mismatch")


def fsync_dir(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def atomic_write(path: Path, data: bytes) -> None:
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


def commit_files_atomically(files: dict[Path, bytes], inject_failure_after: int | None = None) -> None:
    before = {path: path.read_bytes() if path.exists() else None for path in files}
    written = 0
    try:
        for path, data in files.items():
            atomic_write(path, data)
            written += 1
            if inject_failure_after is not None and written >= inject_failure_after:
                raise OSError("AO02_TEST_INJECTED_WRITE_FAILURE")
    except Exception as exc:
        rollback_errors = []
        for path, old in before.items():
            try:
                if old is None:
                    path.unlink(missing_ok=True)
                else:
                    atomic_write(path, old)
            except Exception as rollback_exc:  # pragma: no cover - catastrophic filesystem case
                rollback_errors.append(f"{path}: {rollback_exc}")
        if rollback_errors:
            raise MigrationError("Rollback failed: " + "; ".join(rollback_errors)) from exc
        raise MigrationError(f"Transaction failed and was rolled back: {exc}") from exc


def plan(repo: Path) -> dict:
    manifest = load_csv(repo / MANIFEST)
    validate_exclusion(manifest)
    registry_path = repo / REGISTRY
    relations_path = repo / RELATIONS
    audit_path = repo / AUDIT
    map_path = repo / MIGRATION_MAP

    registry = load_jsonl(registry_path)
    state = migration_state(registry, map_path)
    if state == "PARTIAL_OR_CONFLICTING_MIGRATION":
        raise MigrationError("PARTIAL_OR_CONFLICTING_MIGRATION")
    if state == "POSSIBLY_APPLIED":
        validate_applied_state(registry, map_path, manifest)
        return {
            "status": "ALREADY_APPLIED",
            "change": "NO CHANGE",
            "migrated_count": EXPECTED_ELIGIBLE,
            "asset_id_range": "AST_IMG_000001..AST_IMG_000048",
        }

    validate_existing_runtime(registry)
    timestamp = now_utc()
    assets, map_rows = planned_legacy_assets(repo, manifest, timestamp)
    combined = assets + registry
    validate_combined_registry(combined)

    existing_relations = load_jsonl(relations_path)
    existing_audit = load_jsonl(audit_path)
    new_relations, relation_events = provable_relations(combined, existing_relations, timestamp)
    asset_events = migration_events(assets, timestamp)

    files = {
        registry_path: jsonl_bytes(combined),
        relations_path: jsonl_bytes(existing_relations + new_relations),
        audit_path: jsonl_bytes(existing_audit + asset_events + relation_events),
        map_path: csv_bytes(map_rows, MAP_FIELDS),
    }

    return {
        "status": "READY_TO_APPLY",
        "timestamp": timestamp,
        "source_count": len(manifest),
        "eligible_count": len(assets),
        "migrated_count": len(assets),
        "excluded_legacy_asset_id": EXCLUDED_LEGACY_ID,
        "asset_id_range": "AST_IMG_000001..AST_IMG_000048",
        "runtime_asset_ids_preserved": ["AST_IMG_000049", "AST_IMG_000050", "AST_IMG_000051"],
        "single_current_validation": "PASS",
        "sha_storage_validation": "PASS",
        "relations_to_create": len(new_relations),
        "migration_events_to_create": len(asset_events),
        "relation_events_to_create": len(relation_events),
        "files": files,
    }


def public_result(result: dict) -> dict:
    return {k: v for k, v in result.items() if k != "files"}


def parse_args():
    p = argparse.ArgumentParser(description="AO-02 Legacy Registry Migration Controller V1.0")
    p.add_argument("--apply", action="store_true", help="Apply the validated migration transaction")
    p.add_argument(
        "--inject-failure-after",
        type=int,
        default=None,
        help=argparse.SUPPRESS,
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()
    repo = repo_root()
    result = plan(repo)

    if result["status"] == "ALREADY_APPLIED":
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    if not args.apply:
        out = public_result(result)
        out["status"] = "DRY_RUN_PASS"
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0

    commit_files_atomically(result["files"], inject_failure_after=args.inject_failure_after)

    # Re-read and verify the final state before reporting success.
    manifest = load_csv(repo / MANIFEST)
    registry = load_jsonl(repo / REGISTRY)
    validate_applied_state(registry, repo / MIGRATION_MAP, manifest)
    validate_combined_registry(registry)

    out = public_result(result)
    out["status"] = "APPLIED"
    out["migration_map"] = MIGRATION_MAP.as_posix()
    out["asset_registry"] = REGISTRY.as_posix()
    out["asset_relations"] = RELATIONS.as_posix()
    out["audit_event_log"] = AUDIT.as_posix()
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except MigrationError as exc:
        print(f"[AO02 BLOCKED] {exc}", file=os.sys.stderr)
        raise SystemExit(2)
