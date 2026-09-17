"""Verified Character and state-aware Entity resolver asset view."""

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
DERIVED_REFERENCE_ROOT = Path("production/image_library/derived_reference_sheets")
SCENE_ASSET_ROOT = Path("production/image_library/scene_masters")
SCENE_PROFILES = Path("production/asset_registry/scene_state_profiles.json")
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
        "byte_size": row.get("byte_size"),
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
            and re.fullmatch(r"(?:CHAR|SCENE|PROP|COSTUME)_[A-Z0-9_]+",
                             asset["entity_id"]) is not None)


def source_path(asset, root=ROOT):
    """Reject absolute, traversal, redirected, or noncanonical source paths."""
    root = Path(root).resolve()
    uri = asset["storage_uri"]
    name = asset["filename"]
    entity_id = asset.get("entity_id") or ""
    is_derived = asset.get("asset_class") == "DERIVED_REFERENCE"
    asset_kind = "Derived Reference" if is_derived else ("Scene" if entity_id.startswith("SCENE_") else "Character")
    if not isinstance(uri, str) or not uri or "\\" in uri:
        raise ValueError(f"Invalid {asset_kind} storage URI: {uri}")
    relative = PurePosixPath(uri)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"{asset_kind} storage path escape: {uri}")
    asset_root = (DERIVED_REFERENCE_ROOT if is_derived else
                  (SCENE_ASSET_ROOT if asset_kind == "Scene" else ASSET_ROOT))
    canonical_root = root / asset_root
    if canonical_root.resolve() != canonical_root:
        raise ValueError(f"Canonical {asset_kind} storage root is redirected")
    if not isinstance(name, str) or PurePosixPath(name).name != name or not name.endswith(".png"):
        raise ValueError(f"Invalid canonical {asset_kind} filename: {name}")
    path = root / Path(*relative.parts)
    if (path.name != name or not path.is_relative_to(canonical_root)
            or path.resolve() != path):
        raise ValueError(f"{asset_kind} storage path escape or symlink: {uri}")
    return path


def dependency_status(sheet, root=ROOT):
    """Compute derived dependency freshness; never persist eligibility as a flag."""
    root = Path(root)
    runtime = {row["asset_id"]: row for row in read_runtime_registry(root)}
    relations = []
    relation_path = root / "production/asset_registry/asset_relations.jsonl"
    if relation_path.exists():
        with relation_path.open(encoding="utf-8") as stream:
            relations = [json.loads(line) for line in stream if line.strip()]
    dependency_ids = [r["target_asset_id"] for r in relations
                      if r.get("source_asset_id") == sheet["asset_id"]
                      and r.get("relation_type") == "DERIVED_FROM"]
    if not dependency_ids:
        return {"status": "DEPENDENCY_STALE", "reason": "MISSING_DEPENDENCIES"}
    for asset_id in dependency_ids:
        asset = runtime.get(asset_id)
        if asset is None:
            return {"status": "DEPENDENCY_STALE", "reason": "MISSING_DEPENDENCY", "asset_id": asset_id}
        if (asset.get("asset_class") != "ATOMIC" or asset.get("approval_status") != "APPROVED"
                or asset.get("lifecycle") != "CURRENT" or asset.get("resolver_usage") == "NEVER"):
            return {"status": "DEPENDENCY_STALE", "reason": "INVALID_DEPENDENCY_STATE", "asset_id": asset_id}
        try:
            path = source_path(normalize(asset, "RUNTIME_REGISTRY"), root)
        except ValueError:
            return {"status": "DEPENDENCY_STALE", "reason": "INVALID_DEPENDENCY_PATH", "asset_id": asset_id}
        if not path.is_file() or sha256(path) != asset.get("sha256"):
            return {"status": "DEPENDENCY_STALE", "reason": "DEPENDENCY_INTEGRITY_INVALID", "asset_id": asset_id}
    return {"status": "FRESH", "dependency_asset_ids": dependency_ids}


def read_runtime_registry(root=ROOT):
    rows = []
    with (Path(root) / REGISTRY).open(encoding="utf-8") as stream:
        for line in stream:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def resolve_character_reference_sheet(entity_id, root=ROOT):
    """Resolve a formal fresh Sheet separately from unchanged Atomic resolution."""
    rows = [row for row in read_runtime_registry(root)
            if row.get("entity_id") == entity_id
            and row.get("asset_class") == "DERIVED_REFERENCE"
            and row.get("role") == "CHARACTER_REFERENCE_SHEET"
            and row.get("approval_status") == "APPROVED"
            and row.get("lifecycle") == "CURRENT"]
    if not rows:
        return {"status": "REFERENCE_GAP", "entity_id": entity_id,
                "reason": "NO_FORMAL_CHARACTER_REFERENCE_SHEET"}
    if len(rows) != 1:
        raise ValueError(f"Duplicate CURRENT Character Reference Sheet for {entity_id}")
    sheet = rows[0]
    status = dependency_status(sheet, root)
    if status["status"] != "FRESH":
        return {"status": "REFERENCE_GAP", "entity_id": entity_id,
                "reason": "DEPENDENCY_STALE", "dependency_detail": status}
    normalized = normalize(sheet, "RUNTIME_REGISTRY")
    path = source_path(normalized, root)
    if not path.is_file() or sha256(path) != sheet.get("sha256"):
        return {"status": "REFERENCE_GAP", "entity_id": entity_id,
                "reason": "SHEET_INTEGRITY_INVALID"}
    return {"status": "RESOLVED", "entity_id": entity_id,
            "dependency_status": "FRESH", "asset": normalized}


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


def load_scene_profiles(root=ROOT):
    """Load the executable Scene/State model and reject malformed profiles."""
    model = json.loads((Path(root) / SCENE_PROFILES).read_text(encoding="utf-8"))
    scenes = model.get("scene_entities")
    if not isinstance(scenes, list):
        raise ValueError("Scene profile model must contain scene_entities")
    by_id = {}
    for scene in scenes:
        scene_id = scene.get("scene_id")
        if not isinstance(scene_id, str) or not re.fullmatch(r"SCENE_[A-Z0-9_]+", scene_id):
            raise ValueError(f"Invalid Scene entity id: {scene_id}")
        if scene_id in by_id:
            raise ValueError(f"Duplicate Scene entity: {scene_id}")
        by_id[scene_id] = scene
    return by_id


def _state_matches(profile, required_state):
    """Require every explicitly requested dimension to match exactly."""
    if required_state is None:
        required_state = {}
    if isinstance(required_state, str):
        required_state = {"profile_id": required_state}
    if not isinstance(required_state, dict):
        raise ValueError("required_state must be a mapping or profile id")
    if not required_state:
        return False
    available = {"profile_id": profile.get("profile_id"), **profile.get("facts", {})}
    return all(key in available and available[key] == value
               for key, value in required_state.items())


def resolve_scene(scene_id, required_state, root=ROOT):
    """Resolve one state-matched Scene Master, or report a safe REFERENCE_GAP."""
    scene = load_scene_profiles(root).get(scene_id)
    if scene is None:
        return {"status": "REFERENCE_GAP", "entity_id": scene_id,
                "required_state": required_state, "reason": "UNKNOWN_SCENE"}

    matching_profiles = [profile for profile in scene.get("state_profiles", [])
                         if profile.get("status") == "APPROVED"
                         and _state_matches(profile, required_state)]
    assets = eligible_current_assets(root, scene_id)
    matches = []
    for profile in matching_profiles:
        for asset in assets:
            if (asset["asset_id"] == profile.get("source_master_asset_id")
                    and asset["role"] == "SCENE_MASTER"
                    and asset["variant"] == scene.get("variant")
                    and asset["state"] == profile.get("profile_id")):
                matches.append((profile, asset))
    if not matches:
        return {"status": "REFERENCE_GAP", "entity_id": scene_id,
                "required_state": required_state, "reason": "NO_STATE_MATCHED_SCENE_MASTER"}
    if len(matches) != 1:
        raise ValueError(f"Ambiguous eligible Scene Master for {scene_id}: {len(matches)}")
    profile, asset = matches[0]
    return {"status": "RESOLVED", "entity_id": scene_id,
            "state_profile": profile["profile_id"], "state_facts": profile["facts"],
            "asset": asset}


def resolve_entity_reference(entity_id, required_state, root=ROOT):
    """Extensible Entity entry point; absent Prop/Costume references fail safely."""
    if isinstance(entity_id, str) and entity_id.startswith("SCENE_"):
        return resolve_scene(entity_id, required_state, root)
    if isinstance(entity_id, str) and entity_id.startswith(("PROP_", "COSTUME_")):
        return {"status": "REFERENCE_GAP", "entity_id": entity_id,
                "required_state": required_state, "reason": "NO_ELIGIBLE_FORMAL_ASSET"}
    raise ValueError(f"Unsupported state-aware entity: {entity_id}")
