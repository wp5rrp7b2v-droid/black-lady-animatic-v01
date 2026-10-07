import hashlib, json, os, pathlib, shutil, struct, subprocess

ROOT=pathlib.Path.cwd().resolve()
OUT=ROOT/"S02_A_ASSEMBLY_INPUT_BUNDLE_V001"
VIS=OUT/"visuals"
AUD=OUT/"audio"
CTL=OUT/"control"
for d in (VIS,AUD,CTL): d.mkdir(parents=True,exist_ok=True)

shots=[
("N11","production/image_library/approved/story_shots/N11_NEIL_ABNORMAL_PORTRAIT_APPROVED_V001.png",2538801,"f5efde465dcadd1490f2064c6db39e1d5f194dc6","09d45c1b27fbd2aea68c818677d9656a2ae7f39296f80f6db622118312aebcc5"),
("N12","production/image_library/approved/story_shots/N12_NEIL_CROSS_RIGID_SMILE_APPROVED_V001.png",2434337,"853d04f5ed8a2e1845ce1dfa9cef5c02f123124b","d94dc3623ba1abc55aa86c8b646d7876d097433bfadb70291bfa9c68cffc030b"),
("A04","production/image_library/approved/A_Series/A04_REBOOT_approved_v001.png",2486659,"fd05cae8618d7daa16c16658b29d25ab65052fbb",None),
("N14","production/image_library/approved/story_shots/N14_FIRST_ENCOUNTER_IMPORTANCE_APPROVED_V001.png",2500282,"e32c03bc21efcd0eda98d2e9868a64915583b19f","0474003a1d6d48a652935033f17560d0ee1d689caadbdb7d4af72560477844f1"),
("N15","production/image_library/approved/story_shots/N15_LOCKED_GATE_FORESHADOWING_APPROVED_V001.png",2583010,"4d9ca2dcd33df32294ff9b928bf3ab88d63c7487","2712321ca6348cc39234f8ae65bcdb0fd2e6b2faf0b56dcc94a51235011d1191"),
("A05","production/image_library/approved/A_Series/A05_REBOOT_approved_v001.png",2289774,"9445c9b89b6665bc027385f13821a4ede6892c10",None),
]
audio=("AUDIO_MVP1_CANONICAL_V001","staging/p0_3_a01_a02_transition_validation/AUDIO_MVP1_CANONICAL_V001.m4a",4957338,"abaa3f56619cbbfc16bb545c4938d0066c3be736","8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0")
contract="docs/project_control/gates/P0_3_video_pipeline/s02_a_assembly_execution_contract_v0_1.md"

idx=[json.loads(x) for x in (ROOT/"production/story_shots/story_shot_index.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
records=[]
def gitblob(b):
    return hashlib.sha1(b"blob "+str(len(b)).encode()+bytes([0])+b).hexdigest()
for sid,rel,size,blob,locked_sha in shots:
    rr=[x for x in idx if x.get("shot_id")==sid and x.get("approval_status")=="APPROVED" and x.get("lifecycle")=="CURRENT"]
    if len(rr)!=1: raise SystemExit(f"INDEX_CARDINALITY_FAIL {sid}")
    if rr[0].get("canonical_path")!=rel: raise SystemExit(f"INDEX_PATH_FAIL {sid}")
    p=ROOT/rel
    b=p.read_bytes()
    if len(b)!=size: raise SystemExit(f"SIZE_MISMATCH {sid}")
    if b[:8]!=bytes.fromhex("89504e470d0a1a0a"): raise SystemExit(f"PNG_FAIL {sid}")
    w,h=struct.unpack(">II",b[16:24])
    if (w,h)!=(941,1672): raise SystemExit(f"DIMS_MISMATCH {sid} {w}x{h}")
    sha=hashlib.sha256(b).hexdigest()
    gb=gitblob(b)
    if gb!=blob: raise SystemExit(f"BLOB_MISMATCH {sid}")
    if locked_sha and sha!=locked_sha: raise SystemExit(f"SHA_MISMATCH {sid}")
    dst=VIS/(sid+"__"+p.name)
    shutil.copyfile(p,dst)
    if dst.read_bytes()!=b: raise SystemExit(f"COPY_FAIL {sid}")
    records.append({"shot_id":sid,"canonical_path":rel,"bundle_path":str(dst.relative_to(OUT)),"byte_size":size,"dimensions":f"{w}x{h}","sha256":sha,"git_blob":gb})

aid,arel,asize,ablob,asha=audio
ap=ROOT/arel; ab=ap.read_bytes()
if len(ab)!=asize: raise SystemExit("AUDIO_SIZE_MISMATCH")
if hashlib.sha256(ab).hexdigest()!=asha: raise SystemExit("AUDIO_SHA_MISMATCH")
if gitblob(ab)!=ablob: raise SystemExit("AUDIO_BLOB_MISMATCH")
adst=AUD/ap.name; shutil.copyfile(ap,adst)
if adst.read_bytes()!=ab: raise SystemExit("AUDIO_COPY_FAIL")

cp=ROOT/contract
if not cp.is_file(): raise SystemExit("CONTRACT_MISSING")
ct=cp.read_text(encoding="utf-8")
if "PRODUCT OWNER APPROVED / LOCKED" not in ct: raise SystemExit("CONTRACT_NOT_LOCKED")
shutil.copyfile(cp,CTL/cp.name)

timeline=[
{"shot":"N11","in":"00:32.900","out":"00:39.100","duration_s":6.200},
{"shot":"N12","in":"00:39.100","out":"00:46.360","duration_s":7.260},
{"shot":"A04","in":"00:46.360","out":"00:56.260","duration_s":9.900},
{"shot":"N14","in":"00:56.260","out":"01:03.520","duration_s":7.260},
{"shot":"N15","in":"01:03.520","out":"01:10.940","duration_s":7.420},
{"shot":"A05","in":"01:10.940","out":"01:18.750","duration_s":7.810},
]
manifest={"bundle_id":"S02_A_ASSEMBLY_INPUT_BUNDLE_V001","status":"VERIFIED_INPUT_BUNDLE","source_commit":os.environ.get("SOURCE_COMMIT") or subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"manual_upload_count":0,"assembly_range":{"in":"00:32.900","out":"01:18.750","duration_s":45.850},"sequence":["N11","N12","A04","N14","N15","A05"],"visual_inputs":records,"audio_input":{"id":aid,"canonical_path":arel,"bundle_path":str(adst.relative_to(OUT)),"byte_size":asize,"sha256":asha,"git_blob":ablob},"execution_contract":{"canonical_path":contract,"bundle_path":str((CTL/cp.name).relative_to(OUT)),"sha256":hashlib.sha256(cp.read_bytes()).hexdigest()},"timeline":timeline,"transition_policy":"DIRECT_CUT_ALL; N15_TO_A05_HARD_CUT","n15_motion":{"rotation_deg":[-3.5,0.0],"scale_percent":[103.0,105.0],"roll_to_level_s":1.6,"rule":"gate remains visual center; no generated fog/tree/gate motion"},"output_proof":{"width":941,"height":1672,"aspect":"9:16","subtitles":False,"bgm":False,"extra_sfx":False}}
(OUT/"assembly_manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
(OUT/"WORK_HANDOFF.md").write_text("# S02-A ASSEMBLY WORK HANDOFF\n\nUse only the verified files in this bundle. Assemble exactly N11 → N12 → A04 → N14 → N15 → A05 against the canonical audio and locked timeline in assembly_manifest.json. Preserve exact source images; motion is non-destructive whole-frame transform only. N15 alone uses the locked -3.5°→0° roll-in plus 103%→105% push-in, with ~1.6s roll-to-level. All cuts direct; N15→A05 at 01:10.940 is a hard cut. First proof: 941x1672, no subtitles/BGM/extra SFX. Do not modify registries or Project Control. Return the assembled proof for Product Owner review.\n",encoding="utf-8")
print("PASS: 6/6 canonical Story Shot binaries verified")
print("PASS: canonical audio SHA/BLOB/SIZE verified")
print("PASS: locked execution contract included")
for r in records: print(f'{r["shot_id"]}_SHA256={r["sha256"]}')
print("AUDIO_SHA256="+asha)
print("OVERALL_RESULT=PASS")
