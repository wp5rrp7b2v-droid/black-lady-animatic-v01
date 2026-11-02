#!/usr/bin/env python3
import argparse, hashlib, json, shutil, struct, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "production/asset_registry/asset_registry.jsonl"
STORY_INDEX = ROOT / "production/story_shots/story_shot_index.jsonl"

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def git_blob(path):
    return subprocess.check_output(["git","hash-object",str(path)], cwd=ROOT, text=True).strip()

def image_dimensions(path, expected_format="PNG"):
    # Byte-preserving validation: the approved original JPEG is never converted.
    with path.open("rb") as fp:
        data = fp.read()
    if expected_format == "PNG":
        if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
            raise ValueError(f"Invalid PNG signature: {path}")
        return struct.unpack(">II", data[16:24])
    if expected_format != "JPEG":
        raise ValueError(f"Unsupported reference format: {expected_format}")
    if len(data) < 12 or data[:3] != b"\xff\xd8\xff" or data[-2:] != b"\xff\xd9":
        raise ValueError(f"Invalid JPEG signature: {path}")
    pos = 2
    while pos < len(data):
        if data[pos] != 0xff:
            raise ValueError(f"Invalid JPEG marker at offset {pos}: {path}")
        while pos < len(data) and data[pos] == 0xff:
            pos += 1
        marker = data[pos]
        pos += 1
        if marker in (0xd8, 0xd9):
            continue
        if marker == 0xda:
            break
        if pos + 2 > len(data):
            raise ValueError(f"Truncated JPEG marker: {path}")
        length = int.from_bytes(data[pos:pos + 2], "big")
        if length < 2 or pos + length > len(data):
            raise ValueError(f"Invalid JPEG marker length: {path}")
        if marker in (0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7,
                      0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf):
            if length < 7:
                raise ValueError(f"Invalid JPEG SOF: {path}")
            return (int.from_bytes(data[pos + 5:pos + 7], "big"),
                    int.from_bytes(data[pos + 3:pos + 5], "big"))
        pos += length
    raise ValueError(f"JPEG SOF marker absent: {path}")

def rows(path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

def safe_source(rel):
    p = ROOT / rel
    if not p.is_file() or p.is_symlink() or p.resolve() != p:
        raise ValueError(f"Invalid canonical source: {rel}")
    return p

def verify_ref(ref, registry_rows, story_rows):
    source_type = ref["source_type"]
    if source_type == "ASSET":
        matches = [r for r in registry_rows if r.get("asset_id") == ref["reference_id"]]
        if len(matches) != 1:
            raise ValueError(f"Asset cardinality mismatch: {ref['reference_id']}")
        row = matches[0]
        for key in ("entity_id","role","asset_class","authority_class","approval_status","lifecycle","resolver_usage"):
            expected = ref.get(key)
            if expected is not None and row.get(key) != expected:
                raise ValueError(f"{ref['reference_id']} {key} mismatch")
        if row.get("storage_uri") != ref["canonical_path"]:
            raise ValueError(f"{ref['reference_id']} canonical path mismatch")
        if row.get("byte_size") != ref["expected_byte_size"]:
            raise ValueError(f"{ref['reference_id']} registry byte size mismatch")
        if ref.get("expected_sha256") and row.get("sha256") != ref["expected_sha256"]:
            raise ValueError(f"{ref['reference_id']} registry SHA mismatch")
    elif source_type == "STORY_SHOT":
        matches = [r for r in story_rows if r.get("shot_id") == ref["shot_id"]]
        if len(matches) != 1:
            raise ValueError(f"Story Shot cardinality mismatch: {ref['shot_id']}")
        row = matches[0]
        for key in ("approval_status","lifecycle"):
            if row.get(key) != ref[key]:
                raise ValueError(f"{ref['reference_id']} {key} mismatch")
        if row.get("canonical_path") != ref["canonical_path"]:
            raise ValueError(f"{ref['reference_id']} canonical path mismatch")
        if row.get("byte_size") != ref["expected_byte_size"]:
            raise ValueError(f"{ref['reference_id']} index byte size mismatch")
        if row.get("github_blob_sha") != ref["expected_git_blob"]:
            raise ValueError(f"{ref['reference_id']} index blob mismatch")
    elif source_type == "CONTROLLED_REFERENCE":
        manifest_rel = ref.get("manifest_path")
        if not manifest_rel:
            raise ValueError(f"{ref['reference_id']} manifest_path missing")
        manifest_path = safe_source(manifest_rel)
        try:
            controlled = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception as exc:
            raise ValueError(f"{ref['reference_id']} invalid controlled-reference manifest") from exc

        required_manifest = {
            "reference_id": ref["reference_id"],
            "classification": ref["classification"],
            "approval_status": ref["approval_status"],
            "lifecycle": ref["lifecycle"],
            "authority_scope": ref["authority_scope"],
            "canonical_path": ref["canonical_path"],
        }
        for key, expected in required_manifest.items():
            if controlled.get(key) != expected:
                raise ValueError(f"{ref['reference_id']} manifest {key} mismatch")

        output = controlled.get("output")
        if not isinstance(output, dict):
            raise ValueError(f"{ref['reference_id']} manifest output missing")

        expected_output = {
            "byte_size": ref["expected_byte_size"],
            "sha256": ref["expected_sha256"],
            "git_blob": ref["expected_git_blob"],
        }
        if ref.get("expected_width") is not None:
            expected_output["width"] = ref["expected_width"]
        if ref.get("expected_height") is not None:
            expected_output["height"] = ref["expected_height"]
        for key, expected in expected_output.items():
            if output.get(key) != expected:
                raise ValueError(f"{ref['reference_id']} manifest output {key} mismatch")

        expected_format = ref.get("expected_format", "PNG")
        if expected_format not in ("PNG", "JPEG") or output.get("format") != expected_format:
            raise ValueError(f"{ref['reference_id']} manifest output format mismatch")
        if controlled.get("approved_binary", {}).get("sha256") != ref["expected_sha256"]:
            raise ValueError(f"{ref['reference_id']} approved binary SHA mismatch")
        if controlled.get("approved_binary", {}).get("byte_size") != ref["expected_byte_size"]:
            raise ValueError(f"{ref['reference_id']} approved binary byte size mismatch")
    else:
        raise ValueError(f"Unsupported source type: {source_type}")

    src = safe_source(ref["canonical_path"])
    actual_sha = sha256(src)
    actual_size = src.stat().st_size
    actual_blob = git_blob(src)
    expected_format = ref.get("expected_format", "PNG")
    width, height = image_dimensions(src, expected_format)
    if source_type == "STORY_SHOT":
        if ref.get("expected_sha256") and row.get("sha256_locked_identity") != ref["expected_sha256"]:
            raise ValueError(f"{ref['reference_id']} story shot indexed SHA mismatch")
        if row.get("image_format", "PNG") != expected_format:
            raise ValueError(f"{ref['reference_id']} story shot image format mismatch")

    if actual_size != ref["expected_byte_size"]:
        raise ValueError(f"{ref['reference_id']} byte size mismatch")
    if actual_blob != ref["expected_git_blob"]:
        raise ValueError(f"{ref['reference_id']} Git blob mismatch")
    if ref.get("expected_sha256") and actual_sha != ref["expected_sha256"]:
        raise ValueError(f"{ref['reference_id']} SHA mismatch")
    if ref.get("expected_width") is not None and width != ref["expected_width"]:
        raise ValueError(f"{ref['reference_id']} width mismatch")
    if ref.get("expected_height") is not None and height != ref["expected_height"]:
        raise ValueError(f"{ref['reference_id']} height mismatch")

    return src, actual_sha, actual_size, actual_blob, width, height

def load_spec(spec_path):
    spec_path = (ROOT / spec_path).resolve()
    if not spec_path.is_file() or spec_path.is_symlink():
        raise ValueError("Invalid spec path")
    if spec_path.parent != (ROOT / "production/bundle_specs").resolve():
        raise ValueError("Spec must live directly under production/bundle_specs")

    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    required = {"schema_version","bundle_id","target_shot_id","sequence_id","target_candidate","references","work_handoff"}
    if not required <= spec.keys():
        raise ValueError("Bundle spec missing required fields")
    if not isinstance(spec["references"], list) or not spec["references"]:
        raise ValueError("Reference set is empty")
    if spec.get("build_authorized", True) not in (True, False):
        raise ValueError("build_authorized must be boolean when present")
    return spec


def validate_only(spec_path):
    spec = load_spec(spec_path)
    registry_rows = rows(REGISTRY)
    story_rows = rows(STORY_INDEX)
    verified = []
    for ref in spec["references"]:
        src, actual_sha, actual_size, actual_blob, width, height = verify_ref(ref, registry_rows, story_rows)
        verified.append({
            "reference_id": ref["reference_id"],
            "source_type": ref["source_type"],
            "canonical_path": ref["canonical_path"],
            "computed_sha256": actual_sha,
            "actual_byte_size": actual_size,
            "actual_git_blob": actual_blob,
            "dimensions": {"width": width, "height": height},
            "format_signature": "PASS",
            "source_format": ref.get("expected_format", "PNG"),
        })
    print(f"VALIDATION_PASS: {len(verified)}/{len(spec['references'])} exact canonical references verified")
    print("BUILD_AUTHORIZED=" + ("TRUE" if spec.get("build_authorized", True) else "FALSE"))
    print("GENERATION_ALLOWED=FALSE")
    print("BUNDLE_ID=" + spec["bundle_id"])
    return verified


def build(spec_path):
    spec = load_spec(spec_path)
    if spec.get("build_authorized", True) is not True:
        print("BUILD_AUTHORIZED=FALSE")
        print("GENERATION_ALLOWED=FALSE")
        print("BUNDLE_BUILD_SKIPPED=TRUE")
        print("BUNDLE_ID=" + spec["bundle_id"])
        return None

    out = ROOT / spec["bundle_id"]
    if out.exists() or out.is_symlink():
        raise ValueError(f"Refusing to overwrite existing output: {out.name}")

    registry_rows = rows(REGISTRY)
    story_rows = rows(STORY_INDEX)
    manifest_refs = []
    out.mkdir()

    try:
        for ref in spec["references"]:
            src, actual_sha, actual_size, actual_blob, width, height = verify_ref(ref, registry_rows, story_rows)
            group = ref["destination_group"]
            group_dir = out / group
            group_dir.mkdir(exist_ok=True)
            dst = group_dir / f"{ref['reference_id']}__{src.name}"
            shutil.copyfile(src, dst)
            if sha256(dst) != actual_sha or dst.stat().st_size != actual_size or git_blob(dst) != actual_blob:
                raise ValueError(f"Byte-identical copy verification failed: {ref['reference_id']}")
            manifest_refs.append({
                **ref,
                "computed_sha256": actual_sha,
                "actual_byte_size": actual_size,
                "actual_git_blob": actual_blob,
                "dimensions": {"width": width, "height": height},
                "format_signature": "PASS",
            "source_format": ref.get("expected_format", "PNG"),
                "byte_identical_copy": "PASS",
                "bundle_path": dst.relative_to(out).as_posix()
            })

        manifest = {
            "bundle_id": spec["bundle_id"],
            "target_shot_id": spec["target_shot_id"],
            "sequence_id": spec["sequence_id"],
            "target_candidate": spec["target_candidate"],
            "reference_count": len(manifest_refs),
            "all_reference_checks_pass": True,
            "generation_allowed": True,
            "manual_product_owner_reference_upload": spec.get("manual_product_owner_reference_upload",0),
            "references": manifest_refs,
            "overall_result": "PASS"
        }
        (out / "delivery_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        h = spec["work_handoff"]
        lines = [f"# {h.get('title', spec['target_candidate'])}", "", "## Requirements"]
        lines += [f"- {x}" for x in h.get("requirements",[])]
        lines += ["", "## Exclusions"]
        lines += [f"- {x}" for x in h.get("exclusions",[])]
        lines += ["", "## Verification", "- Revalidate every delivered PNG/JPEG exact binary against delivery_manifest.json before generation.", "- If any check fails, do not generate."]
        (out / "WORK_HANDOFF.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

        for ref in manifest_refs:
            p = out / ref["bundle_path"]
            if sha256(p) != ref["computed_sha256"] or p.stat().st_size != ref["actual_byte_size"] or git_blob(p) != ref["actual_git_blob"]:
                raise ValueError(f"Final artifact revalidation failed: {ref['reference_id']}")

        print(f"PASS: {len(manifest_refs)}/{len(spec['references'])} exact canonical reference binaries verified")
        print("GENERATION_ALLOWED=TRUE")
        print("BUNDLE_ID=" + spec["bundle_id"])
        return out
    except Exception:
        if out.exists():
            shutil.rmtree(out)
        raise

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--spec", required=True)
    p.add_argument("--validate-only", action="store_true")
    a = p.parse_args()
    if a.validate_only:
        validate_only(a.spec)
    else:
        build(a.spec)

if __name__ == "__main__":
    main()
