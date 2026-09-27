import hashlib, json, shutil, struct, subprocess
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
REPO = PROJECT.parent
WORK = PROJECT / "work"
INPUTS = WORK / "inputs"
OUT = PROJECT / "out" / "P03_LIBOPENSHOT_CAMERA_MOTION_PROOF_V001"
INPUTS.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)

SHOTS = ["N08", "N03", "N05"]

def require(ok, msg):
    if not ok:
        raise RuntimeError(msg)

def git(*args):
    return subprocess.check_output(["git","-C",str(REPO),*args], text=True).strip()

state = json.loads((REPO/"docs/project_control/core/project_state.json").read_text())
require(state.get("state_revision") == "R095", f"expected R095, got {state.get('state_revision')}")
require(state.get("current_task") == "P0.3｜OPENING V2 V003 CONTEXTUAL REVIEW", "unexpected current task")

records = [json.loads(x) for x in (REPO/"production/story_shots/story_shot_index.jsonl").read_text().splitlines() if x.strip()]
registry = {r["shot_id"]: r for r in records}

manifest = {
    "source_commit": git("rev-parse","HEAD"),
    "purpose": "libopenshot camera-motion spike only; not production edit; motion-only proof without program audio",
    "shots": []
}

for sid in SHOTS:
    require(sid in registry, f"missing story shot {sid}")
    rec = registry[sid]
    require(rec.get("approval_status") == "APPROVED", f"{sid} not approved")
    require(rec.get("lifecycle") == "CURRENT", f"{sid} not current")
    rel = rec["canonical_path"]
    path = REPO / rel
    require(path.is_file() and not path.is_symlink(), f"{sid} not regular file")
    data = path.read_bytes()
    require(data[:8] == b"\x89PNG\r\n\x1a\n" and data[12:16] == b"IHDR", f"{sid} invalid PNG")
    width,height = struct.unpack(">II", data[16:24])
    require((width,height) == (941,1672), f"{sid} unexpected dimensions {width}x{height}")
    sha256 = hashlib.sha256(data).hexdigest()
    blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    require(blob == git("rev-parse", f"HEAD:{rel}"), f"{sid} git blob mismatch")
    require(len(data) == rec["byte_size"], f"{sid} byte size mismatch")
    require(blob == rec["github_blob_sha"], f"{sid} index blob mismatch")
    if rec.get("sha256_locked_identity"):
        require(sha256 == rec["sha256_locked_identity"], f"{sid} SHA256 mismatch")
    dst = INPUTS / f"{sid}.png"
    shutil.copyfile(path, dst)
    require(hashlib.sha256(dst.read_bytes()).hexdigest() == sha256, f"{sid} copy mismatch")
    manifest["shots"].append({
        "shot_id": sid,
        "canonical_path": rel,
        "sha256": sha256,
        "github_blob_sha": blob,
        "byte_size": len(data),
        "dimensions": [width,height]
    })

(WORK/"input_manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(manifest,ensure_ascii=False,indent=2))
