#!/usr/bin/env python3
import argparse, hashlib, json, struct, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_ROOT = ROOT / "production/candidate_delivery_specs"
EVIDENCE_ROOT = ROOT / "_candidate_intake_evidence"

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def git_blob(path):
    return subprocess.check_output(["git","hash-object",str(path)], cwd=ROOT, text=True).strip()

def png_dimensions(path):
    with path.open("rb") as f:
        data = f.read(24)
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("PNG_SIGNATURE_FAIL")
    return struct.unpack(">II", data[16:24])

def load_specs():
    specs=[]
    for p in sorted(SPEC_ROOT.glob("*.json")):
        spec=json.loads(p.read_text(encoding="utf-8"))
        specs.append((p,spec))
    return specs

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--candidate", required=True)
    args=ap.parse_args()

    candidate_rel=args.candidate.replace("\\","/")
    if not candidate_rel.startswith("staging/story_shot_candidates/"):
        raise SystemExit("INVALID_STAGING_PATH")

    candidate=(ROOT/candidate_rel).resolve()
    if not candidate.is_file() or candidate.is_symlink():
        raise SystemExit("CANDIDATE_NOT_REGULAR_FILE")
    if not str(candidate).startswith(str((ROOT/"staging/story_shot_candidates").resolve())):
        raise SystemExit("CANDIDATE_PATH_ESCAPE")

    matches=[]
    for spec_path,spec in load_specs():
        if spec.get("target_staging_path")==candidate_rel:
            matches.append((spec_path,spec))
    if len(matches)!=1:
        raise SystemExit(f"SPEC_CARDINALITY_FAIL={len(matches)}")

    spec_path,spec=matches[0]
    exp=spec["expected_identity"]

    actual_size=candidate.stat().st_size
    actual_sha=sha256(candidate)
    actual_blob=git_blob(candidate)
    width,height=png_dimensions(candidate)

    checks={
        "target_path_match": spec["target_staging_path"]==candidate_rel,
        "png_signature": True,
        "width_match": width==exp["width"],
        "height_match": height==exp["height"],
        "byte_size_match": actual_size==exp["byte_size"],
        "sha256_match": actual_sha==exp["sha256"],
        "git_blob_match": actual_blob==exp["git_blob_sha1"],
        "product_owner_status_approved": spec.get("product_owner_status")=="APPROVED",
        "reencode_forbidden": spec.get("constraints",{}).get("reencode_allowed") is False,
        "resize_forbidden": spec.get("constraints",{}).get("resize_allowed") is False,
        "screenshot_forbidden": spec.get("constraints",{}).get("screenshot_allowed") is False,
    }
    ok=all(checks.values())

    EVIDENCE_ROOT.mkdir(exist_ok=True)
    evidence={
        "bridge_version":"STORY_SHOT_CANDIDATE_DELIVERY_BRIDGE_V1",
        "spec_path":spec_path.relative_to(ROOT).as_posix(),
        "shot_id":spec["shot_id"],
        "sequence_id":spec["sequence_id"],
        "candidate_id":spec["candidate_id"],
        "candidate_path":candidate_rel,
        "expected_identity":exp,
        "actual_identity":{
            "format":"PNG",
            "width":width,
            "height":height,
            "byte_size":actual_size,
            "sha256":actual_sha,
            "git_blob_sha1":actual_blob,
        },
        "checks":checks,
        "candidate_intake_verified":ok,
        "downstream_canonical_target":spec["downstream_canonical_target"],
        "manual_product_owner_github_upload_required":spec.get("constraints",{}).get("manual_product_owner_github_upload_required",True),
    }
    out=EVIDENCE_ROOT/"candidate_intake_verification.json"
    out.write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

    print(f"SHOT_ID={spec['shot_id']}")
    print(f"CANDIDATE_ID={spec['candidate_id']}")
    print(f"CANDIDATE_PATH={candidate_rel}")
    print(f"BYTE_SIZE={actual_size}")
    print(f"SHA256={actual_sha}")
    print(f"GIT_BLOB={actual_blob}")
    print(f"DIMENSIONS={width}x{height}")
    print("CANDIDATE_INTAKE_VERIFIED=" + ("TRUE" if ok else "FALSE"))
    print("MANUAL_PRODUCT_OWNER_GITHUB_UPLOAD_REQUIRED=" + ("TRUE" if evidence["manual_product_owner_github_upload_required"] else "FALSE"))
    if not ok:
        raise SystemExit("CANDIDATE_INTAKE_VERIFICATION_FAIL")

if __name__=="__main__":
    main()
