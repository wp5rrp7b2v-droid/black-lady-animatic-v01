#!/usr/bin/env python3
"""Export a manifest-verified P1 Character reference package (v0.2)."""

import argparse
import hashlib
import json
import re
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import resolver_asset_source_v0_1 as resolver


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = Path(
    "docs/project_control/gates/P0_2_visual_assets/migration_evidence/"
    "character_asset_migration_manifest_v1.json"
)
ASSET_ROOT = Path("production/image_library/character_references")
OUTPUT_ROOT = Path("tmp/reference_packages")
ANCHORS_BY_TARGET = {
    "PROFILE_LEFT": (
        ("FACE_FRONT", "人物身份与正面五官主锚点"),
        ("PROFILE_RIGHT", "现有相反方向侧脸，用于侧脸轮廓与结构"),
        ("FACE_3Q_RIGHT", "右前方三分之四视角，辅助理解头脸立体结构"),
        ("BODY_FRONT", "正面体型、服装及整体人物结构"),
    ),
    "PROFILE_RIGHT": (
        ("FACE_FRONT", "人物身份与正面五官主锚点"),
        ("PROFILE_LEFT", "现有相反方向侧脸，用于侧脸轮廓与结构"),
        ("FACE_3Q_LEFT", "左前方三分之四视角，辅助理解头脸立体结构"),
        ("BODY_FRONT", "正面体型、服装及整体人物结构"),
    ),
    "REAR_3Q_LEFT": (
        ("FACE_FRONT", "人物身份与正面五官主锚点"),
        ("REAR_3Q_RIGHT", "现有相反方向后侧视角，用于背面轮廓与结构"),
        ("FACE_3Q_RIGHT", "右前方三分之四视角，辅助理解头脸立体结构"),
        ("BODY_BACK", "背面体型、服装及整体人物结构"),
    ),
    "REAR_3Q_RIGHT": (
        ("FACE_FRONT", "人物身份与正面五官主锚点"),
        ("REAR_3Q_LEFT", "现有相反方向后侧视角，用于背面轮廓与结构"),
        ("FACE_3Q_LEFT", "左前方三分之四视角，辅助理解头脸立体结构"),
        ("BODY_BACK", "背面体型、服装及整体人物结构"),
    ),
}
STAMP_RE = re.compile(r"_\d{8}T\d{12}Z$")


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def package_root():
    root = ROOT.resolve() / OUTPUT_ROOT
    if root.is_symlink() or root.resolve() != root:
        raise ValueError("Reference package root is redirected; operation blocked")
    return root


def package_name(wave_id, entity, target_role):
    if not re.fullmatch(r"[A-Z][A-Z0-9_]*", wave_id):
        raise ValueError("Wave ID must contain only uppercase letters, digits, and underscores")
    if not re.fullmatch(r"CHAR_[A-Z0-9_]+", entity):
        raise ValueError("Entity must be a canonical CHAR_ identifier")
    if target_role not in ANCHORS_BY_TARGET:
        raise ValueError(f"Unsupported target role: {target_role}")
    return f"{wave_id}_{entity.removeprefix('CHAR_')}_{target_role}"


def package_identity_matches(path, metadata):
    """Accept the v0.1 marker and v0.2 marker, only at their named location."""
    entity = metadata.get("entity_id")
    role = metadata.get("target_role")
    if not isinstance(entity, str) or not re.fullmatch(r"CHAR_[A-Z0-9_]+", entity):
        return False
    if role not in ANCHORS_BY_TARGET:
        return False
    base = STAMP_RE.sub("", path.name)
    suffix = f"_{entity.removeprefix('CHAR_')}_{role}"
    if not base.endswith(suffix):
        return False
    wave = base[:-len(suffix)]
    if not re.fullmatch(r"[A-Z][A-Z0-9_]*", wave):
        return False
    return metadata.get("wave_id", wave) == wave


def is_verified_old_package(path):
    """Verify marker, identity, exact contents, and every copied PNG before deletion."""
    if path.is_symlink() or not path.is_dir() or path.resolve().parent != package_root():
        return False
    marker = path / "package.json"
    if marker.is_symlink() or not marker.is_file():
        return False
    try:
        metadata = json.loads(marker.read_text(encoding="utf-8"))
        if (metadata.get("source_manifest") != MANIFEST.as_posix()
                or not package_identity_matches(path, metadata)):
            return False
        assets = metadata.get("selected_assets")
        if not isinstance(assets, list) or not assets:
            return False
        expected = {"package.json"}
        for item in assets:
            name = item["canonical_filename"]
            reference = path / name
            if (not isinstance(name, str) or Path(name).name != name
                    or not name.endswith(".png") or name in expected
                    or reference.is_symlink() or not reference.is_file()
                    or not re.fullmatch(r"[a-f0-9]{64}", item["sha256"])
                    or sha256(reference) != item["sha256"]):
                return False
            expected.add(name)
        return {p.name for p in path.iterdir()} == expected
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError):
        return False


def verify_package(output, package):
    marker = output / "package.json"
    if marker.is_symlink() or json.loads(marker.read_text(encoding="utf-8")) != package:
        raise ValueError("Generated package.json failed verification")
    if not is_verified_old_package(output):
        raise ValueError("Generated reference PNG SHA or package identity failed verification")


def cleanup_old_reference_packages(current_package_path):
    """Keep the verified current package; delete only other verified packages."""
    root = package_root()
    current = Path(current_package_path)
    if current.is_symlink() or current.resolve().parent != root or not current.is_dir():
        raise ValueError("Current package is outside tmp/reference_packages/")
    if not is_verified_old_package(current):
        raise ValueError("Current package failed exporter verification; cleanup blocked")
    current = current.resolve()
    verified_old = []
    for old in root.iterdir():
        if old == current:
            continue
        if old.is_symlink():
            raise ValueError(f"Symlink in reference package root; cleanup blocked: {old.name}")
        if not old.is_dir():
            continue
        if old.resolve().parent != root:
            raise ValueError(f"Package path escapes reference package root: {old.name}")
        if not is_verified_old_package(old):
            continue
        verified_old.append(old)
    for old in verified_old:
        shutil.rmtree(old)
    return len(verified_old)


def export(entity, target_role, output, wave_id="P1_WAVE1"):
    package_name(wave_id, entity, target_role)
    all_assets = resolver.load_assets(ROOT)
    entity_assets = [a for a in all_assets if a["entity_id"] == entity]
    if not entity_assets:
        raise ValueError(f"Entity not found in unified asset source: {entity}")

    current = resolver.eligible_current_assets(ROOT, entity)
    by_key = {(a["role"], a["variant"], a["state"]): a for a in current}
    if any(a["role"] == target_role and a["lifecycle"] == "CURRENT"
           for a in entity_assets):
        raise ValueError(f"Target role {target_role} already has a CURRENT asset")

    warnings = [f"{target_role} is a REFERENCE_GAP; this package supplies production anchors."]
    selected = []
    for role, reason in ANCHORS_BY_TARGET[target_role]:
        row = by_key.get((role, "DEFAULT", "DEFAULT"))
        if row is None:
            warnings.append(f"{role}: no eligible CURRENT / APPROVED / CONFIRMED DEFAULT asset")
            continue
        path = resolver.source_path(row, ROOT)
        if not path.is_file():
            warnings.append(f"{role}: canonical PNG missing: {row['storage_uri']}")
            continue
        actual_sha = sha256(path)
        if actual_sha != row.get("sha256"):
            raise ValueError(f"SHA-256 mismatch for {row['filename']}")
        selected.append((row, path, reason, actual_sha))
    if not selected:
        raise ValueError("No eligible, existing, SHA-verified anchors were found")

    output = Path(output)
    root = package_root()
    if output.is_symlink() or output.resolve().parent != root or not re.fullmatch(
            re.escape(package_name(wave_id, entity, target_role)) + r"(?:_\d{8}T\d{12}Z)?", output.name):
        raise ValueError("Output must be a safely named direct child of tmp/reference_packages/")
    if output.exists():
        raise ValueError(f"Output already exists; refusing to overwrite: {output}")

    package = {
        "entity_id": entity,
        "target_role": target_role,
        "wave_id": wave_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "package_status": "TEST COMPLETE / WAITING PRODUCT OWNER REVIEW",
        "target_role_status": "REFERENCE_GAP",
        "source_manifest": MANIFEST.as_posix(),
        "source_registry": resolver.REGISTRY.as_posix(),
        "selected_assets": [
            {
                "role": row["role"],
                "canonical_filename": row["filename"],
                "source_path": row["storage_uri"],
                "source_layer": row["source_layer"],
                "asset_id": row["asset_id"],
                "sha256": actual_sha,
                "selection_reason": reason,
            }
            for row, _, reason, actual_sha in selected
        ],
        "reference_gap": True,
        "warnings": warnings,
    }
    root.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".reference_package_", dir=root))
    try:
        for row, path, _, actual_sha in selected:
            destination = staging / row["filename"]
            shutil.copyfile(path, destination)
            if sha256(destination) != actual_sha:
                raise ValueError(f"Copied PNG failed SHA-256 check: {destination.name}")
        (staging / "package.json").write_text(
            json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        staging.rename(output)
        verify_package(output, package)
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return package


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entity", required=True)
    parser.add_argument("--target-role", required=True)
    parser.add_argument("--wave-id", default="P1_WAVE1")
    parser.add_argument("--output", type=Path, help="Optional safely named output directory")
    args = parser.parse_args()
    try:
        name = package_name(args.wave_id, args.entity, args.target_role)
        output = args.output or ROOT / OUTPUT_ROOT / name
        if not output.is_absolute():
            output = ROOT / output
        if args.output is None and output.exists():
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
            output = output.with_name(f"{name}_{stamp}")
        package = export(args.entity, args.target_role, output, args.wave_id)
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        parser.exit(1, f"Export failed: {exc}\n")
    print(f"CURRENT_PACKAGE: {output}")
    try:
        cleaned = cleanup_old_reference_packages(output)
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print("CLEANED_OLD_PACKAGES: incomplete")
        parser.exit(1, f"CLEANUP_STATUS: BLOCKED ({exc}); current package preserved\n")
    print(f"CLEANED_OLD_PACKAGES: {cleaned}")
    print("CLEANUP_STATUS: COMPLETE")
    print(f"Status: {package['package_status']}; selected: {len(package['selected_assets'])}")
    for item in package["selected_assets"]:
        print(f"- {item['role']}: {item['canonical_filename']} — {item['selection_reason']}")
    for warning in package["warnings"]:
        print(f"WARNING: {warning}")


if __name__ == "__main__":
    main()
