"""Unified, verified Character resolver view for migration and runtime assets."""

import hashlib
import json
import re
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = Path(
    "docs/project_control/gates/P0_2_visual_assets/migration_evidence/"
    "character_asset_migration_manifest_v1.json"
)
REGISTRY = Path("production/asset_registry/asset_registry.jsonl")
ASSET_ROOT = Path("production/image_library/character_references")
SOURCES = {"MIGRATION_MANIFEST", "RUNTIME_REGISTRY"}


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalize(row, source_layer):
    """Keep source provenance while exposing one common Character asset schema."""
    if source_layer not in SOURCES:
        raise ValueError(f"Unsupported asset source layer: {source_layer}")
    migration = source_layer == "MIGRATION_MANIFEST"
    return {
        "source_layer": source_layer,
        "asset_id": None if migration else row.get("asset_id"),
        "entity_id": row.get("canonical_entity_id" if migration else "entity_id"),
        "role": row.get("new_role" if migration else "role"),
        "variant": row.get("variant"),
        "state": row.get("state"),
        "version_no": row.get("version_no"),
        "approval_status": row.get("approval_status"),
        "lifecycle": row.get("lifecycle"),
        "authority_class": row.get("authority_class"),
        "resolver_usage": row.get("resolver_usage"),
        "filename": row.get("canonical_filename" if migration else "filename"),
        "storage_uri": row.get("target_storage_path" if migration else "storage_uri"),
        "sha256": row.get("sha256"),
        "mapping_status": row.get("mapping_status") if migration else "RUNTIME_NATIVE",
        "asset_class": None if migration else row.get("asset_class"),
    }


def load_assets(root=ROOT):
    """Load both layers, including inactive records for inspection."""
    root = Path(root)
    migration = json.loads((root / MANIFEST).read_text(encoding="utf-8"))
    if not isinstance(migration, list):
        raise ValueError("Migration manifest must be a JSON list")
    registry_path = root / REGISTRY
    runtime = []
    if registry_path.exists():
        with registry_path.open(encoding="utf-8") as stream:
            for line_no, line in enumerate(stream, 1):
                if line.strip():
                    try:
                        row = json.loads(line)
                    except json.JSONDecodeError as exc:
                        raise ValueError(f"Runtime Registry line {line_no} is invalid JSON") from exc
                    if not isinstance(row, dict):
                        raise ValueError(f"Runtime Registry line {line_no} is not an object")
                    runtime.append(row)
    return ([normalize(row, "MIGRATION_MANIFEST") for row in migration]
            + [normalize(row, "RUNTIME_REGISTRY") for row in runtime])


def metadata_eligible(asset):
    if (asset["approval_status"] != "APPROVED"
            or asset["lifecycle"] != "CURRENT"
            or asset["resolver_usage"] in (None, "NEVER")):
        return False
    if asset["source_layer"] == "MIGRATION_MANIFEST":
        return asset["mapping_status"] == "CONFIRMED"
    return (asset["asset_class"] == "ATOMIC"
            and isinstance(asset["entity_id"], str)
            and re.fullmatch(r"CHAR_[A-Z0-9_]+", asset["entity_id"]) is not None)


def source_path(asset, root=ROOT):
    """Reject absolute, traversal, redirected, or noncanonical source paths."""
    root = Path(root).resolve()
    uri = asset["storage_uri"]
    name = asset["filename"]
    if not isinstance(uri, str) or not uri or "\\" in uri:
        raise ValueError(f"Invalid Character storage URI: {uri}")
    relative = PurePosixPath(uri)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"Character storage path escape: {uri}")
    canonical_root = root / ASSET_ROOT
    if canonical_root.resolve() != canonical_root:
        raise ValueError("Canonical Character storage root is redirected")
    if not isinstance(name, str) or PurePosixPath(name).name != name or not name.endswith(".png"):
        raise ValueError(f"Invalid canonical Character filename: {name}")
    path = root / Path(*relative.parts)
    if (path.name != name or not path.is_relative_to(canonical_root)
            or path.resolve() != path):
        raise ValueError(f"Character storage path escape or symlink: {uri}")
    return path


def eligible_current_assets(root=ROOT, entity_id=None):
    """Return verified CURRENT assets, deduping only identical cross-source records."""
    candidates = [asset for asset in load_assets(root)
                  if (entity_id is None or asset["entity_id"] == entity_id)
                  and metadata_eligible(asset)]
    by_key = {}
    for asset in candidates:
        key = (asset["entity_id"], asset["role"], asset["variant"], asset["state"])
        previous = by_key.get(key)
        if previous is None:
            by_key[key] = asset
            continue
        if previous["source_layer"] == asset["source_layer"]:
            raise ValueError(f"Duplicate eligible CURRENT asset for {key}")
        fingerprint = lambda row: (row["filename"], row["sha256"], row["version_no"])
        if fingerprint(previous) != fingerprint(asset):
            raise ValueError(f"CROSS_SOURCE_SINGLE_CURRENT_CONFLICT for {key}: "
                             f"{previous['filename']} vs {asset['filename']}")
        if asset["source_layer"] == "RUNTIME_REGISTRY":
            by_key[key] = asset

    verified = []
    for asset in by_key.values():
        path = source_path(asset, root)
        if not path.is_file():
            continue
        if sha256(path) != asset["sha256"]:
            raise ValueError(f"SHA-256 mismatch for {asset['filename']} ({asset['source_layer']})")
        verified.append(asset)
    return verified
