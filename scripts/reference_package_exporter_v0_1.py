#!/usr/bin/env python3
"""Export a small, manifest-verified Character reference package (v0.1)."""

import argparse
import hashlib
import json
import re
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = Path(
    "docs/project_control/gates/P0_2_visual_assets/migration_evidence/"
    "character_asset_migration_manifest_v1.json"
)
ASSET_ROOT = Path("production/image_library/character_references")
OUTPUT_ROOT = Path("tmp/reference_packages")
TARGET_ROLE = "PROFILE_LEFT"
ANCHORS = (
    ("FACE_FRONT", "人物身份与正面五官主锚点"),
    ("PROFILE_RIGHT", "现有相反方向侧脸，用于侧脸轮廓与结构"),
    ("FACE_3Q_RIGHT", "右前方三分之四视角，辅助理解头脸立体结构"),
    ("BODY_FRONT", "正面体型、服装及整体人物结构"),
)


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def source_path(row):
    relative = Path(row["target_storage_path"])
    resolved = (ROOT / relative).resolve()
    asset_root = (ROOT / ASSET_ROOT).resolve()
    if relative.is_absolute() or not resolved.is_relative_to(asset_root):
        raise ValueError(f"Asset path escapes canonical Character directory: {relative}")
    if resolved.name != row["canonical_filename"] or resolved.suffix.lower() != ".png":
        raise ValueError(f"Canonical filename/path mismatch: {relative}")
    return resolved


def eligible(row):
    return (
        row.get("approval_status") == "APPROVED"
        and row.get("mapping_status") == "CONFIRMED"
        and row.get("lifecycle") == "CURRENT"
        and row.get("resolver_usage") not in (None, "NEVER")
    )


def cleanup_old_reference_packages(current_package_path):
    """Delete only verified packages produced by this exporter, inside its tmp root."""
    root = ROOT.resolve() / OUTPUT_ROOT
    if root.is_symlink() or root.resolve() != root:
        raise ValueError("Reference package root is redirected; cleanup blocked")
    current_path = Path(current_package_path)
    if current_path.is_symlink() or current_path.resolve().parent != root or not current_path.is_dir():
        raise ValueError("Current package is outside tmp/reference_packages/")
    current = current_path.resolve()
    cleaned = 0
    for old in root.iterdir():
        if old == current or old.is_symlink() or not old.is_dir():
            continue
        if old.resolve().parent != root or not re.fullmatch(
            r"P1_WAVE1_[A-Z0-9_]+_PROFILE_LEFT(?:_\d{8}T\d{12}Z)?", old.name
        ):
            continue
        if not is_verified_old_package(old):
            continue
        shutil.rmtree(old)
        cleaned += 1
    return cleaned


def current_package_path_entity(name):
    base = re.sub(r"_\d{8}T\d{12}Z$", "", name)
    return "CHAR_" + base.removeprefix("P1_WAVE1_").removesuffix("_PROFILE_LEFT")


def is_verified_old_package(path):
    marker = path / "package.json"
    if marker.is_symlink() or not marker.is_file():
        return False
    try:
        metadata = json.loads(marker.read_text(encoding="utf-8"))
        if (metadata.get("source_manifest") != MANIFEST.as_posix()
                or metadata.get("target_role") != TARGET_ROLE
                or metadata.get("entity_id") != current_package_path_entity(path.name)):
            return False
        assets = metadata.get("selected_assets")
        if not isinstance(assets, list) or not assets:
            return False
        expected = {"package.json"}
        for item in assets:
            name = item["canonical_filename"]
            reference = path / name
            if (Path(name).name != name or not name.endswith(".png")
                    or name in expected or reference.is_symlink()
                    or not reference.is_file() or sha256(reference) != item["sha256"]):
                return False
            expected.add(name)
        return {p.name for p in path.iterdir()} == expected
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError):
        return False


def verify_package(output, package):
    if json.loads((output / "package.json").read_text(encoding="utf-8")) != package:
        raise ValueError("Generated package.json failed verification")
    for item in package["selected_assets"]:
        reference = output / item["canonical_filename"]
        if not reference.is_file() or sha256(reference) != item["sha256"]:
            raise ValueError(f"Generated PNG failed verification: {reference.name}")


def export(entity, target_role, output):
    if not re.fullmatch(r"CHAR_[A-Z0-9_]+", entity):
        raise ValueError("Entity must be a canonical CHAR_ identifier")
    if target_role != TARGET_ROLE:
        raise ValueError("v0.1 only supports target role PROFILE_LEFT")
    rows = json.loads((ROOT / MANIFEST).read_text(encoding="utf-8"))
    entity_rows = [r for r in rows if r.get("canonical_entity_id") == entity]
    if not entity_rows:
        raise ValueError(f"Entity not found in migration manifest: {entity}")

    current = [r for r in entity_rows if eligible(r)]
    by_key = {}
    for row in current:
        key = (row.get("new_role"), row.get("variant"), row.get("state"))
        if key in by_key:
            raise ValueError(f"Duplicate eligible CURRENT asset for {key}: "
                             f"{by_key[key]['canonical_filename']} and {row['canonical_filename']}")
        by_key[key] = row

    if any(r.get("new_role") == target_role for r in current):
        raise ValueError(f"Target role {target_role} already has an eligible CURRENT asset")

    warnings = [f"{target_role} is a REFERENCE_GAP; this package supplies production anchors."]
    selected = []
    for role, reason in ANCHORS:
        candidates = [r for r in current if r.get("new_role") == role
                      and r.get("variant") == "DEFAULT" and r.get("state") == "DEFAULT"]
        if not candidates:
            warnings.append(f"{role}: no eligible CURRENT / APPROVED / CONFIRMED DEFAULT asset")
            continue
        row = candidates[0]
        path = source_path(row)
        if not path.is_file():
            warnings.append(f"{role}: canonical PNG missing: {row['target_storage_path']}")
            continue
        actual_sha = sha256(path)
        if actual_sha != row.get("sha256"):
            raise ValueError(f"SHA-256 mismatch for {row['canonical_filename']}")
        selected.append((row, path, reason, actual_sha))

    if not selected:
        raise ValueError("No eligible, existing, SHA-verified anchors were found")
    if output.exists():
        raise ValueError(f"Output already exists; refusing to overwrite: {output}")

    package = {
        "entity_id": entity,
        "target_role": target_role,
        "package_status": "TEST COMPLETE / WAITING PRODUCT OWNER REVIEW",
        "target_role_status": "REFERENCE_GAP",
        "source_manifest": MANIFEST.as_posix(),
        "selected_assets": [
            {
                "role": row["new_role"],
                "canonical_filename": row["canonical_filename"],
                "source_path": row["target_storage_path"],
                "sha256": actual_sha,
                "selection_reason": reason,
            }
            for row, _, reason, actual_sha in selected
        ],
        "reference_gap": True,
        "warnings": warnings,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    root = ROOT.resolve() / OUTPUT_ROOT
    if root.is_symlink() or root.resolve() != root or output.resolve().parent != root:
        raise ValueError("Output must be a direct child of tmp/reference_packages/")
    staging = Path(tempfile.mkdtemp(prefix=".reference_package_", dir=output.parent))
    try:
        for row, path, _, actual_sha in selected:
            destination = staging / row["canonical_filename"]
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
    parser.add_argument("--output", type=Path, help="Optional output directory")
    args = parser.parse_args()
    output = args.output or (
        ROOT / OUTPUT_ROOT / f"P1_WAVE1_{args.entity.removeprefix('CHAR_')}_{args.target_role}"
    )
    if not output.is_absolute():
        output = ROOT / output
    if args.output is None and output.exists():
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        output = output.with_name(f"{output.name}_{stamp}")
    try:
        package = export(args.entity, args.target_role, output)
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
