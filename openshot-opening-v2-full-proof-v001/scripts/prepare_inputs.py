import hashlib, json, shutil, struct, subprocess
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
REPO = PROJECT.parent
SPEC = json.loads((PROJECT/"shot_motion_spec.json").read_text())
WORK = PROJECT/"work"
INPUTS = WORK/"inputs"
OUT = PROJECT/"out"/SPEC["project"]
INPUTS.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)

def require(ok,msg):
    if not ok: raise RuntimeError(msg)

def git(*args):
    return subprocess.check_output(["git","-C",str(REPO),*args],text=True).strip()

state=json.loads((REPO/"docs/project_control/core/project_state.json").read_text())
require(state.get("state_revision")=="R096", f"expected R096, got {state.get('state_revision')}")
require(state.get("current_task")=="P0.3｜LIBOPENSHOT CAMERA MOTION PROOF V001 REVIEW","unexpected current task")

sequence=SPEC["sequence"]
frame_map=[(s["start_frame"],s["duration_frames"]) for s in SPEC["shots"]]
require(sequence==[s["shot_id"] for s in SPEC["shots"]],"sequence/spec mismatch")
require(frame_map==[(0,98),(98,99),(197,71),(268,68),(336,60),(396,63),(459,132),(591,58),(649,84),(733,82),(815,86),(901,90)],"frame map mismatch")
require(SPEC["total_frames"]==991 and SPEC["fps"]==30,"composition timing mismatch")

records=[json.loads(x) for x in (REPO/"production/story_shots/story_shot_index.jsonl").read_text().splitlines() if x.strip()]
registry={r["shot_id"]:r for r in records}
manifest={"source_commit":git("rev-parse","HEAD"),"state_revision":"R096","shots":[]}

for sid in sequence:
    require(sid in registry,f"missing registry record {sid}")
    rec=registry[sid]
    require(rec.get("approval_status")=="APPROVED" and rec.get("lifecycle")=="CURRENT",f"{sid} not approved/current")
    rel=rec["canonical_path"]
    path=REPO/rel
    require(path.is_file() and not path.is_symlink(),f"{sid} not regular file")
    data=path.read_bytes()
    require(data[:8]==b"\x89PNG\r\n\x1a\n" and data[12:16]==b"IHDR",f"{sid} invalid PNG")
    width,height=struct.unpack(">II",data[16:24])
    require((width,height)==(941,1672),f"{sid} unexpected dimensions {width}x{height}")
    sha=hashlib.sha256(data).hexdigest()
    blob=hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
    require(blob==git("rev-parse",f"HEAD:{rel}"),f"{sid} git blob mismatch")
    require(len(data)==rec["byte_size"],f"{sid} byte mismatch")
    require(blob==rec["github_blob_sha"],f"{sid} registry blob mismatch")
    if rec.get("sha256_locked_identity"):
        require(sha==rec["sha256_locked_identity"],f"{sid} sha mismatch")
    shutil.copyfile(path,INPUTS/f"{sid}.png")
    manifest["shots"].append({"shot_id":sid,"canonical_path":rel,"sha256":sha,"github_blob_sha":blob,"byte_size":len(data),"dimensions":[width,height]})

audio_rel=SPEC["audio"]["canonical_path"]
audio_path=REPO/audio_rel
adata=audio_path.read_bytes()
asha=hashlib.sha256(adata).hexdigest()
require(asha==SPEC["audio"]["sha256"],"canonical audio SHA mismatch")
ablob=hashlib.sha1(b"blob "+str(len(adata)).encode()+b"\0"+adata).hexdigest()
require(ablob==git("rev-parse",f"HEAD:{audio_rel}"),"audio git blob mismatch")
shutil.copyfile(audio_path,WORK/"opening_audio.m4a")
manifest["audio"]={"canonical_path":audio_rel,"sha256":asha,"github_blob_sha":ablob,"byte_size":len(adata),"source_start_sec":0,"source_end_sec":991/30}
manifest["overall_input_validation"]="PASS"
(WORK/"input_manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(manifest,ensure_ascii=False,indent=2))
