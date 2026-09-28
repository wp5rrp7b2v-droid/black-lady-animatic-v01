import hashlib, json, os, pathlib, shutil, struct, subprocess

ROOT=pathlib.Path.cwd().resolve()
OUT=ROOT/"N15_REFERENCE_DELIVERY_BUNDLE_V001"
(OUT/"scene_authority").mkdir(parents=True,exist_ok=True)
(OUT/"continuity_refs").mkdir(parents=True,exist_ok=True)

def check(rel,size,blob,dims=None,sha=None):
    p=ROOT/rel
    if not p.is_file() or p.is_symlink(): raise SystemExit("INVALID_FILE "+rel)
    b=p.read_bytes()
    if len(b)!=size: raise SystemExit("SIZE_MISMATCH "+rel)
    if b[:8].hex()!="89504e470d0a1a0a": raise SystemExit("PNG_FAIL "+rel)
    w,h=struct.unpack(">II",b[16:24])
    if dims and (w,h)!=dims: raise SystemExit("DIMS_MISMATCH "+rel)
    s=hashlib.sha256(b).hexdigest()
    if sha and s!=sha: raise SystemExit("SHA_MISMATCH "+rel)
    g=hashlib.sha1(b"blob "+str(len(b)).encode()+bytes([0])+b).hexdigest()
    if g!=blob: raise SystemExit("BLOB_MISMATCH "+rel)
    return p,b,s,w,h

reg=[json.loads(x) for x in (ROOT/"production/asset_registry/asset_registry.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
rr=[x for x in reg if x.get("asset_id")=="AST_IMG_000084"]
if len(rr)!=1: raise SystemExit("AST_IMG_000084_CARDINALITY_FAIL")
for k,v in {"entity_id":"SCENE_MANOR_GATE","role":"SCENE_MASTER","approval_status":"APPROVED","lifecycle":"CURRENT","authority_class":"MASTER"}.items():
    if rr[0].get(k)!=v: raise SystemExit("REGISTRY_FAIL "+k)

idx=[json.loads(x) for x in (ROOT/"production/story_shots/story_shot_index.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
aa=[x for x in idx if x.get("shot_id")=="A01" and x.get("approval_status")=="APPROVED" and x.get("lifecycle")=="CURRENT"]
if len(aa)!=1: raise SystemExit("A01_INDEX_FAIL")

mp,mb,msha,mw,mh=check("production/image_library/scene_masters/manor_gate/SCENE_MANOR_GATE_SCENE_MASTER_DEFAULT_DAY_CLOSED_V001.png",3279563,"ac1dfb7be2069848917afb9749de6c8ebc54d3e5",(941,1671),"95b3bebce1b2e9be72d5a2bc99665a4a99719eb0f4146e40a562210bd982e278")
ap,ab,asha,aw,ah=check("production/image_library/approved/A_Series/A01_REBOOT_approved_v001.png",3399726,"35769a40dc1fd559d97908235f6a6024562b71b7")

pairs=[(mp,OUT/"scene_authority"/"AST_IMG_000084__SCENE_MANOR_GATE_SCENE_MASTER_DEFAULT_DAY_CLOSED_V001.png",mb),(ap,OUT/"continuity_refs"/"A01__A01_REBOOT_approved_v001.png",ab)]
for src,dst,b in pairs:
    shutil.copyfile(src,dst)
    if dst.read_bytes()!=b: raise SystemExit("COPY_IDENTITY_FAIL")

manifest={"bundle_id":"N15_REFERENCE_DELIVERY_BUNDLE_V001","target":"N15 Candidate 01","source_commit":os.environ.get("SOURCE_COMMIT") or subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"reference_count":2,"manual_product_owner_reference_upload":0,"references":[{"id":"AST_IMG_000084","entity_id":"SCENE_MANOR_GATE","authority":"SCENE_IDENTITY_GEOMETRY_MASTER","sha256":msha,"byte_size":len(mb),"dimensions":f"{mw}x{mh}","git_blob":"ac1dfb7be2069848917afb9749de6c8ebc54d3e5"},{"id":"A01","authority":"WORLD_EXTERIOR_CINEMATIC_CONTINUITY_ONLY","sha256":asha,"byte_size":len(ab),"dimensions":f"{aw}x{ah}","git_blob":"35769a40dc1fd559d97908235f6a6024562b71b7"}],"authority_precedence":["N15_DIRECTOR_SHOT_DESIGN","AST_IMG_000084","A01"],"excluded":["AST_IMG_000052","ALL_CHARACTER_REFERENCES","N14","A05","KEY_LOCK_IMAGERY","HISTORICAL_MANOR_GATE_CANDIDATES","INTERNET_REFERENCES"]}
(OUT/"delivery_manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
handoff="# N15 WORK HANDOFF\n\nGenerate exactly one N15 Candidate 01.\n\n9:16 vertical. View from inside estate toward the outer manor gate. AST_IMG_000084 is the sole MANOR_GATE identity/geometry authority. Preserve Gate + Boundary + Road and internal-road -> gate -> external-road. A01 is world/exterior cinematic continuity only and must never override gate geometry. Make the shot more cinematic than the neutral Scene Master; do not simply copy its 3/4 reference composition. Prefer distance, depth and a distant-final-endpoint feeling. Gate closed and sole narrative subject. ZERO characters, Neil, keys, chains, padlock emphasis, opening action, character POV, or evidence the characters have discovered the gate. Tone: quiet spatial foreshadowing / restrained unease / distant endpoint. Not horror poster, ruin, fantasy gate or castle entrance. Stop after Candidate 01 and return for Product Owner review. Do not register or formalize it.\n"
(OUT/"WORK_HANDOFF.md").write_text(handoff,encoding="utf-8")
for _,dst,b in pairs:
    if dst.read_bytes()!=b: raise SystemExit("FINAL_REVALIDATION_FAIL")
print("PASS: 2/2 exact canonical reference binaries verified")
print("A01_SHA256="+asha)
print("MANOR_GATE_SHA256="+msha)
