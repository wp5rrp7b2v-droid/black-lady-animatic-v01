#!/usr/bin/env python3
"""M01 v1 configurable candle engine; review pilots only.

Core algorithm has NO shot IDs, fixed candle coordinates, input timecuts,
or path-bound source logic. All registered sources, camera-relative geometry,
flame visibility, human exclusion, and effect style are loaded from a versioned
Scene Light Atlas JSON.

S02-B pilot / cross-scene release gates remain BLOCKED until separately accepted.
"""
from __future__ import annotations
import argparse,hashlib,io,json,math,pathlib,subprocess,sys,zipfile
import numpy as np
from PIL import Image

ROOT=pathlib.Path(__file__).resolve().parents[1]
PROFILE_DIR=ROOT/"production/environment_dynamic/m01_engine_v1/profiles"
W,H=720,1280
def sha(path):
 h=hashlib.sha256()
 with pathlib.Path(path).open("rb") as f:
  for chunk in iter(lambda:f.read(1024*1024),b""):h.update(chunk)
 return h.hexdigest()
def path_from_repo(s):
 p=pathlib.PurePosixPath(s)
 if p.is_absolute() or ".." in p.parts or not p.parts:raise ValueError("INVALID_REPOSITORY_PATH")
 dest=(ROOT/pathlib.Path(*p.parts)).resolve()
 if ROOT.resolve() not in dest.parents:raise ValueError("PATH_OUTSIDE_REPOSITORY")
 return dest
def read_profile(name):
 if name=="auto":raise ValueError("CALIBRATION_REQUIRED__UNREGISTERED_SCENE__NO_AUTOMATIC_RENDER")
 if "/" in name or "\\" in name or not name.endswith(".json"):raise ValueError("INVALID_PROFILE_NAME")
 p=PROFILE_DIR/name
 if not p.is_file():raise ValueError("CALIBRATION_REQUIRED__PROFILE_NOT_REGISTERED")
 j=json.loads(p.read_text())
 validate(j)
 j["_atlas_sha256"]=sha(p)
 j["_atlas_path"]=str(p.relative_to(ROOT))
 return j

def validate(p):
 assert p["schema"]=="M01_SCENE_LIGHT_ATLAS_V1"
 assert p["review_status"] in ("PILOT_REFERENCE_ONLY","PO_VISUAL_STYLE_APPROVED_N17_RESULT_ONLY")
 assert p["release_allowed"] is False
 assert p["source"]["type"] in ("still_png","video_mp4")
 size=p["render"]
 assert (size["width"],size["height"],size["fps"])==(W,H,30)
 assert 1<size["frames"]<=5000 and size["frame_start"]>=0
 assert len(p["fixtures"])>0
 assert len({x["individual_source_id"] for x in p["fixtures"]})==len(p["fixtures"]),"DUPLICATE_SOURCE_ID"
 assert p["protection"]["mode"] in ("roi_only_unverified","bitpack_masks_unverified")
 assert p["protection"]["do_not_claim_complete_person_protection"] is True
 assert p["temporal"]["style"] in ("n23_paced","unsynced_independent")
 if "unified_flame_engine" in p:
  u=p["unified_flame_engine"]
  assert u["schema"]=="M01_UNIFIED_FLAME_PROVENANCE_V013"
  assert u["one_candle_algorithm"] is True
  assert u["canonical_temporal_signal"]==p["temporal"]["style"]=="unsynced_independent"
  assert all(f["same_signal_drives_core_and_halo"] is True for f in p["fixtures"])
  assert p["render_full_flame_output_authorized"] is False
  assert u["registration_status"] in ("PENDING_CALIBRATION_NO_NEW_FLAME_RENDER","PROVISIONAL_EXISTING_CORE_MASKS_VISUAL_REFERENCE","PO_CENTERS_APPROVED_STATIC_CORE_MASK_QC_PASS_VIDEO_PO_REVIEW_PENDING")
  if u["registration_status"]=="PENDING_CALIBRATION_NO_NEW_FLAME_RENDER":
   assert all(f["flame_core_registration"]=="NOT_REGISTERED_CORE_CANDIDATE_REQUIRED" for f in p["fixtures"])
  elif u["registration_status"]=="PROVISIONAL_EXISTING_CORE_MASKS_VISUAL_REFERENCE":
   assert all(f["flame_core_registration"]=="PROPOSED_MACHINE_MASK_CORE_PRESENT" for f in p["fixtures"])
  else:
   assert p["source"]["type"]=="still_png"
   assert "static_core_masks" in p
   ids=p["static_core_masks"]["flame_ids"]
   assert len(ids)>0 and len(ids)==len(set(ids))
   idx=[f["core_static_flame_id"] for f in p["fixtures"] if "core_static_flame_id" in f]
   assert len(idx)==len(ids) and set(idx)==set(ids)
   assert all(f["flame_core_registration"] in ("APPROVED_CENTER_MASK_CANDIDATE_PO_REVIEW","V012_STYLE_REFLECTOR_ONLY") for f in p["fixtures"])
   assert all(f["flame_core_registration"]=="APPROVED_CENTER_MASK_CANDIDATE_PO_REVIEW" for f in p["fixtures"] if "core_static_flame_id" in f)
   assert all(f["flame_core_registration"]=="V012_STYLE_REFLECTOR_ONLY" for f in p["fixtures"] if "core_static_flame_id" not in f)
   assert all(f["region"]["roi_px"][0]<=f["center_px"][0]<f["region"]["roi_px"][2] and f["region"]["roi_px"][1]<=f["center_px"][1]<f["region"]["roi_px"][3] for f in p["fixtures"] if "core_static_flame_id" in f)


 if "halo_fast_harmonics_mix" in p["temporal"]:
  mix=p["temporal"]["halo_fast_harmonics_mix"]
  assert isinstance(mix,(int,float)) and math.isfinite(float(mix)) and 0<=mix<=1,"BAD_HALO_HARMONICS_MIX"
 if p["source"]["type"]=="still_png":assert size["frame_start"]==0
 for fixture in p["fixtures"]:
  assert isinstance(fixture["id"],str) and fixture["id"]
  reg=fixture["region"]
  assert reg["kind"]=="gaussian"
  x0,y0,x1,y1=reg["roi_px"]
  sx,sy=reg["sigma_px"]
  assert all(math.isfinite(float(v)) for v in [x0,y0,x1,y1,sx,sy])
  assert 0<=x0<x1<=W and 0<=y0<y1<=H
  assert sx>0 and sy>0
  assert 0<float(reg["weight"])<=1.5
  if "track_px" in fixture:
   pts=fixture["track_px"]
   assert len(pts)>=2
   assert all(a[0]<b[0] for a,b in zip(pts,pts[1:]))
  if "visibility_keyframes" in fixture:
   keys=fixture["visibility_keyframes"]
   assert all(a[0]<b[0] for a,b in zip(keys,keys[1:]))
   assert all(0<=frame<size["frames"] for frame,_ in keys),"VISIBILITY_KEYS_MUST_USE_CLIP_LOCAL_FRAMES"
   assert all(0<=v<=1 for _,v in keys)
  for fade in reg.get("tapers",[]):
   assert fade["axis"] in ("x","y")
   assert fade["from"]<fade["to"]
   assert all(0<=fade[k]<=1 for k in ("from_weight","to_weight"))

def load_inputs(profile):
 src=path_from_repo(profile["source"]["path"])
 assert src.is_file(),"MISSING_INPUT"
 assert sha(src)==profile["source"]["sha256"],"SOURCE_BINARY_IDENTITY_MISMATCH"
 mask=None
 pp=profile["protection"]
 if pp["mode"]=="bitpack_masks_unverified":
  root=path_from_repo(pp["mask_zip"])
  assert root.is_file() and sha(root)==pp["mask_zip_sha256"],"MASK_BINARY_IDENTITY_MISMATCH"
  audit=json.loads(path_from_repo(pp["audit_json"]).read_text())
  assert audit["source_video_sha256"]==profile["source"]["sha256"]
  mask={"path":root,"frames":{x["frame_index"]:x for x in audit["frames"]},
        "sha256":pp["mask_zip_sha256"]}
  span=range(profile["render"]["frame_start"],profile["render"]["frame_start"]+profile["render"]["frames"])
  assert all(i in mask["frames"] for i in span),"MASK_FRAMES_MISSING"
 return src,mask

def load_static_flame_masks(profile):
 """Load real-source-pixel masks once. Existing N17 temporal bitpack path unchanged."""
 data=profile.get("static_core_masks")
 if data is None:return {}
 zip_path=path_from_repo(data["zip_path"])
 manifest_path=path_from_repo(data["manifest_path"])
 assert zip_path.is_file() and sha(zip_path)==data["zip_sha256"],"STATIC_FLAME_PACK_SHA_MISMATCH"
 assert manifest_path.is_file() and sha(manifest_path)==data["manifest_sha256"],"STATIC_FLAME_MANIFEST_SHA_MISMATCH"
 manifest=json.loads(manifest_path.read_text())
 assert manifest["source_sha256"]==profile["source"]["sha256"],"STATIC_FLAME_SOURCE_SHA_MISMATCH"
 assert manifest["status"]=="APPROVED_CENTERS_MACHINE_MASKS_PO_VIDEO_REVIEW_PENDING"
 assert set(manifest["flames"])==set(data["flame_ids"])
 out={}
 with zipfile.ZipFile(zip_path) as z:
  for name in data["flame_ids"]:
   record=manifest["flames"][name]
   center=record["approved_center"]
   f=next(x for x in profile["fixtures"] if x.get("core_static_flame_id")==name)
   assert center==f["center_px"],"STATIC_FLAME_CENTER_NOT_PO_APPROVED"
   mask=packmask(z,record["mask_filename"])
   assert int(mask.sum())==record["mask_pixels"]>0
   cx,cy=center
   assert mask[cy,cx] or np.any(mask[max(0,cy-3):cy+4,max(0,cx-3):cx+4])
   yy,xx=np.where(mask)
   assert np.max(np.abs(xx-cx))<=10 and np.max(np.abs(yy-cy))<=17,"FLAME_MASK_TOO_BROAD"
   out[name]=mask
 return out

def signal(t,phase,style):
 if style=="n23_paced":
  # Preserve the approved style's frequency/rhythm; phases are fixture-local.
  return (.50*math.sin(2*math.pi*.94*t+phase)
      +.32*math.sin(2*math.pi*2.07*t+.64+phase*1.13)
      +.18*math.sin(2*math.pi*3.06*t+1.4+phase*.79))
 return (.56*math.sin(t*2*math.pi*(1.05+.12*phase)+phase*1.7)
      +.28*math.sin(t*2*math.pi*(2.13+.15*phase)+.9+phase*2.1)
      +.16*math.sin(t*2*math.pi*(3.36+.10*phase)+1.1+phase*1.2))

def visibility(f,relative,frame_count,mode):
 if "visibility_keyframes" in f:
  keys=f["visibility_keyframes"]
  return float(np.interp(relative,[a[0] for a in keys],[a[1] for a in keys]))
 if mode=="sin_soft_edges":
  return math.sin(math.pi*relative/(frame_count-1))**1.2
 return 1.0

def frame_center(f,absolute):
 if "track_px" in f:
  pairs=f["track_px"]
  return (float(np.interp(absolute,[p[0] for p in pairs],[p[1] for p in pairs])),
    float(np.interp(absolute,[p[0] for p in pairs],[p[2] for p in pairs])))
 return [float(v) for v in f["center_px"]]

def open_ffmpeg_source(source,profile):
 size=profile["render"]
 if profile["source"]["type"]=="still_png":
  with Image.open(source) as im:
   if list(im.size)!=profile["source"]["input_dimensions"]:raise ValueError("SOURCE_DIMENSION_MISMATCH")
   data=np.asarray(im.convert("RGB").resize((W,H),Image.Resampling.LANCZOS)).copy()
  return None,data
 start=size["frame_start"]
 end=start+size["frames"]-1
 cmd=["ffmpeg","-hide_banner","-loglevel","error","-xerror","-i",str(source),
  "-map","0:v:0","-vf",f"select=between(n\\,{start}\\,{end})",
  "-vsync","vfr","-pix_fmt","rgb24","-f","rawvideo","pipe:1"]
 return subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE),None

def next_frame(dec,still):
 if still is not None:return still.copy()
 n=W*H*3
 chunks=[]
 while n:
  x=dec.stdout.read(n)
  if not x:raise RuntimeError("SOURCE_DECODING_SHORT_FRAME")
  chunks.append(x);n-=len(x)
 return np.frombuffer(b"".join(chunks),dtype=np.uint8).reshape(H,W,3).copy()

def packmask(z,key):
 data=z.read(key)
 assert len(data)==W*H//8,("BAD_MASK_LENGTH",key)
 return np.unpackbits(np.frombuffer(data,dtype=np.uint8),bitorder="little",count=W*H).reshape(H,W).astype(bool)

def per_frame_masks(mask,z,idx):
 if mask is None:return np.zeros((H,W),bool),np.zeros((H,W),bool),{}
 row=mask["frames"][idx]
 people=packmask(z,row["person_mask_file"])
 unsure=packmask(z,row["uncertainty_file"])
 flame={p["source_index"]:packmask(z,p["path"]) for p in row["flame_core_mask_files"]}
 return people,unsure,flame

def calculate_frame(rgb,profile,absolute,relative,person=None,uncertain=None,flame_by_index=None):
 """Common pixel renderer. No frame is replaced or geometry generated."""
 if rgb.shape!=(H,W,3) or rgb.dtype!=np.uint8:raise ValueError("RGB_FRAME_SHAPE_OR_TYPE")
 person=np.zeros((H,W),bool) if person is None else person
 uncertain=np.zeros((H,W),bool) if uncertain is None else uncertain
 flame_by_index={} if flame_by_index is None else flame_by_index
 assert person.shape==(H,W) and uncertain.shape==(H,W)
 protect=person|uncertain
 result=rgb.copy()
 authorized=np.zeros((H,W),bool)
 effects=0
 for fi,f in enumerate(profile["fixtures"]):
  gain=visibility(f,relative,profile["render"]["frames"],profile["temporal"]["envelope"])
  if gain<=0:continue
  reg=f["region"]
  x0,y0,x1,y1=[int(round(v)) for v in reg["roi_px"]]
  center=frame_center(f,absolute)
  sx,sy=reg["sigma_px"]
  yy,xx=np.ogrid[y0:y1,x0:x1]
  local=(np.exp(-.5*(((xx-center[0])/sx)**2+((yy-center[1])/sy)**2))*reg["weight"]).astype(np.float32)
  for taper in reg.get("tapers",[]):
   axis=xx if taper["axis"]=="x" else yy
   alpha=np.clip((axis-taper["from"])/(taper["to"]-taper["from"]),0,1)
   local*=taper["from_weight"]*(1-alpha)+taper["to_weight"]*alpha
  local[local<.003]=0
  allowed=(local>0)&(~protect[y0:y1,x0:x1])
  if not allowed.any():continue
  t=relative/profile["render"]["fps"]
  phase=float(f["phase"])
  full_signal=signal(t,phase,profile["temporal"]["style"])
  # Independent candle-core response is unchanged. Slow architectural reflected
  # light may attenuate high harmonics: large walls must not strobe like flames.
  # Optional per-Atlas control; default 1.0 preserves existing approved N17.
  mix=float(profile["temporal"].get("halo_fast_harmonics_mix",1.0))
  if profile["temporal"]["style"]=="unsynced_independent":
   slow_component=.56*math.sin(t*2*math.pi*(1.05+.12*phase)+phase*1.7)
  else:
   slow_component=.50*math.sin(2*math.pi*.94*t+phase)
  halo_signal=slow_component*(1-mix)+full_signal*mix
  amps=np.array(f.get("halo_gain_rgb",profile["temporal"]["rgb_cap"]),dtype=np.float32)
  delta=halo_signal*gain*local[:,:,None]*amps[None,None,:]
  roi=result[y0:y1,x0:x1].astype(np.float32)
  changed=np.clip(roi+delta,0,255).astype(np.uint8)
  masked=result[y0:y1,x0:x1]
  masked[allowed]=changed[allowed]
  authorized[y0:y1,x0:x1]|=allowed
  effects+=1
  if "core_bitpack_index" in f or "core_static_flame_id" in f:
   mask_key=int(f["core_bitpack_index"]) if "core_bitpack_index" in f else f["core_static_flame_id"]
   mask=flame_by_index.get(mask_key)
   if mask is not None:
    # Don't create fire before the source is visible / mask exists.
    safe=mask[y0:y1,x0:x1]&(~protect[y0:y1,x0:x1])
    if safe.any():
     fire=masked.astype(np.float32)
     flame_change=full_signal*gain*np.array(f["core_gain_rgb"],dtype=np.float32)
     flame_new=np.clip(fire+flame_change,0,255).astype(np.uint8)
     masked[safe]=flame_new[safe]
     authorized[y0:y1,x0:x1]|=safe
 changed_any=np.any(result!=rgb,axis=2)
 if np.any(changed_any&protect):raise RuntimeError("PERSON_PROTECTION_VIOLATION")
 if np.any(changed_any&~authorized):raise RuntimeError("OUTSIDE_REGION_MODIFICATION")
 return result,{"changed":int(changed_any.sum()),"max_delta":int(np.max(np.abs(result.astype(np.int16)-rgb.astype(np.int16)))),
  "protected_changed":0,"outside_authorized":0,"sources_applied":effects}

def encode_video(raw_dir,name,frames,fps):
 output=raw_dir/name
 args=["ffmpeg","-hide_banner","-loglevel","error","-y","-f","rawvideo",
  "-pix_fmt","rgb24","-s",f"{W}x{H}","-framerate",str(fps),"-i","pipe:0",
  "-an","-c:v","libx264","-preset","veryfast","-crf","18",
  "-pix_fmt","yuv420p","-r",str(fps),"-movflags","+faststart",str(output)]
 return output,subprocess.Popen(args,stdin=subprocess.PIPE)

def post_audio(video,src,profile):
 if not profile["render"]["preserve_audio"]:return
 suffix=video.with_name(video.stem+"_silent.mp4")
 video.rename(suffix)
 size=profile["render"]
 subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-i",str(suffix),
   "-ss",f"{size['frame_start']/size['fps']:.9f}",
   "-t",f"{size['frames']/size['fps']:.9f}","-i",str(src),"-map","0:v:0","-map","1:a:0",
   "-c:v","copy","-c:a","aac","-b:a","160k","-shortest",
   "-movflags","+faststart",str(video)],check=True)
 suffix.unlink()

def create_ab(output,source,profile,effect):
 size=profile["render"]
 is_still=profile["source"]["type"]=="still_png"
 srcvideo=["-loop","1","-framerate",str(size["fps"]),"-i",str(source)] if is_still else ["-i",str(source)]
 trim=(f"trim=start_frame={size['frame_start']}:end_frame={size['frame_start']+size['frames']},"
       if not is_still else f"trim=end_frame={size['frames']},")
 filters=(f"[0:v]{trim}setpts=PTS-STARTPTS,scale={W}:{H},"
   "drawtext=text='ORIGINAL':fontcolor=white:fontsize=26:x=18:y=18,"
   "pad=iw:ih+60:0:60:black[a];"
   "[1:v]setpts=PTS-STARTPTS,"
   "drawtext=text='M01 ENGINE V1':fontcolor=white:fontsize=26:x=18:y=18,"
   "pad=iw:ih+60:0:60:black[b];"
   "[a][b]hstack=inputs=2[v]")
 args=["ffmpeg","-hide_banner","-loglevel","error","-y",
   *srcvideo,"-i",str(effect),"-filter_complex",filters,
   "-map","[v]"]
 if size["preserve_audio"]:args+=["-map","1:a:0","-c:a","copy"]
 args+=["-c:v","libx264","-preset","veryfast","-crf","21",
        "-pix_fmt","yuv420p","-r",str(size["fps"]),
        "-frames:v",str(size["frames"]),"-movflags","+faststart",str(output)]
 subprocess.run(args,check=True)

def video_data(path):
 j=json.loads(subprocess.check_output(["ffprobe","-v","error",
     "-show_entries","stream=codec_type,codec_name,width,height,nb_frames,r_frame_rate:format=duration",
     "-of","json",str(path)],text=True))
 v=next(x for x in j["streams"] if x["codec_type"]=="video")
 return {"frames":int(v["nb_frames"]),"width":v["width"],"height":v["height"],
     "fps":v["r_frame_rate"],"duration_seconds":float(j["format"]["duration"]),
     "audio":any(s["codec_type"]=="audio" for s in j["streams"])}

def run(name,output,mode,ab):
 output=pathlib.Path(output)
 output.mkdir(parents=True,exist_ok=True)
 try:profile=read_profile(name)
 except (ValueError,AssertionError) as exc:
  report={"schema":"M01_ENGINE_V1_RESULT","status":"CALIBRATION_REQUIRED",
    "error":str(exc),"release_allowed":False,"rendered":False}
  (output/"M01_ENGINE_V1_FAIL_CLOSED.json").write_text(json.dumps(report,indent=2)+"\n")
  print("CALIBRATION_REQUIRED",str(exc),file=sys.stderr)
  return 3
 src,mask=load_inputs(profile)
 if mode=="pilot" and profile.get("unified_flame_engine",{}).get("registration_status")=="PENDING_CALIBRATION_NO_NEW_FLAME_RENDER":
  report={"schema":"M01_ENGINE_V1_RESULT","status":"CALIBRATION_REQUIRED",
    "reason":"VISIBLE_FLAME_CORES_NOT_REGISTERED__ONE_ENGINE_NO_SYNTHETIC_FLAMES",
    "profile_id":profile["profile_id"],"source_sha256":sha(src),
    "rendered":False,"release_allowed":False,
    "legacy_V012_ambient_visual_reference_unchanged":True}
  (output/"M01_ENGINE_V1_FAIL_CLOSED.json").write_text(json.dumps(report,indent=2)+"\n")
  print("CALIBRATION_REQUIRED",report["reason"],file=sys.stderr)
  return 3
 if mode=="review_full":
  raise ValueError("REVIEW_FULL_NOT_YET_RELEASED_NEEDS_CROSS_SCENE_ACCEPTANCE")
 if mode=="diagnostic":
  summary={"schema":"M01_ENGINE_V1_RESULT","status":"DIAGNOSTIC_PROFILE_SOURCE_SHA_PASS",
    "profile_id":profile["profile_id"],"input_sha256":sha(src),
    "atlas_sha256":profile["_atlas_sha256"],"protection":profile["protection"]["mode"],
    "fixture_count":len(profile["fixtures"]),"registered_candle_count":len(profile["fixtures"]),
    "full_person_protection_approved":False,"rendered":False,"release_allowed":False}
  (output/"M01_ENGINE_V1_DIAGNOSTIC.json").write_text(json.dumps(summary,indent=2)+"\n")
  print("M01_ENGINE_V1_DIAGNOSTIC_SOURCE_PROFILE_PASS",profile["profile_id"])
  return 0
 if mode!="pilot":raise ValueError("UNKNOWN_MODE")
 static_flames=load_static_flame_masks(profile)
 dec,still=open_ffmpeg_source(src,profile)
 name_safe=profile["profile_id"]
 video,encoder=encode_video(output,f"M01_{name_safe}_REVIEW_V001.mp4",profile["render"]["frames"],profile["render"]["fps"])
 stats=[]
 start=profile["render"]["frame_start"]
 count=profile["render"]["frames"]
 try:
  with zipfile.ZipFile(mask["path"]) if mask else _null_zip() as z:
   for k in range(count):
    source=next_frame(dec,still)
    absolute=start+k
    if mask and "decoded_source_rgb_sha256" in mask["frames"][absolute]:
     assert hashlib.sha256(source.tobytes()).hexdigest()==mask["frames"][absolute]["decoded_source_rgb_sha256"],"SOURCE_FRAME_HASH_DRIFT"
    person,uncertain,flames=per_frame_masks(mask,z,absolute)
    if static_flames:
     flames.update(static_flames)
    new,stat=calculate_frame(source,profile,absolute,k,person,uncertain,flames)
    encoder.stdin.write(new.tobytes())
    stats.append(stat)
  if dec and dec.stdout.read(1)!=b"":raise RuntimeError("SOURCE_EXTRA_FRAMES")
 finally:
  encoder.stdin.close()
  if dec:
   dec.stdout.close()
   err=dec.stderr.read().decode(errors="replace");dec.stderr.close()
   assert dec.wait()==0,err[-400:]
 assert encoder.wait()==0
 post_audio(video,src,profile)
 comparison=None
 if ab:
  comparison=output/f"M01_{name_safe}_AB_V001.mp4"
  create_ab(comparison,src,profile,video)
 metadata=video_data(video)
 assert metadata["frames"]==count
 assert metadata["width"]==W and metadata["height"]==H
 assert metadata["fps"]=="30/1"
 assert metadata["audio"]==profile["render"]["preserve_audio"]
 assert sha(src)==profile["source"]["sha256"],"SOURCE_MUTATED"
 report={"schema":"M01_ENGINE_V1_RESULT","status":"COMMON_ENGINE_TECHNICAL_PILOT_PO_REVIEW_PENDING",
  "profile":profile["profile_id"],"atlas_file":profile["_atlas_path"],"atlas_sha256":profile["_atlas_sha256"],
  "source_sha256":profile["source"]["sha256"],"fixture_count":len(profile["fixtures"]),
  "frame_count":count,"fps":30,"video_file":video.name,"video_sha256":sha(video),"video_bytes":video.stat().st_size,
  "video_probe":metadata,
  "comparison_file":comparison.name if comparison else None,
  "comparison_sha256":sha(comparison) if comparison else None,
  "changed_frames":sum(x["changed"]>0 for x in stats),
  "max_raw_rgb_delta":max(x["max_delta"] for x in stats),
  "changed_protected_pixels":sum(x["protected_changed"] for x in stats),
  "changed_pixels_outside_authorized":sum(x["outside_authorized"] for x in stats),
  "each_flame_independent_signal":True,
  "person_protection_ground_truth_approved":False,"release_allowed":False,
  "approved_scene_light_atlas_for_batch":False,
  "no_canonical_publication":True,"no_main_merge":True}
 (output/"M01_ENGINE_V1_PILOT_QC.json").write_text(json.dumps(report,indent=2)+"\n")
 print("M01_COMMON_ENGINE_V1_PILOT_COMPLETE",json.dumps({k:v for k,v in report.items() if k not in ("video_probe",)},ensure_ascii=False),flush=True)
 return 0

class _null_zip:
 def __enter__(self):return None
 def __exit__(self,*args):return False

if __name__=="__main__":
 parser=argparse.ArgumentParser(description="M01 reusable configured candle pilot; never publish main")
 parser.add_argument("--profile",required=True,help="Atlas JSON file name under profiles/ or 'auto' to fail closed")
 parser.add_argument("--output-dir",required=True)
 parser.add_argument("--mode",choices=["diagnostic","pilot","review_full"],default="diagnostic")
 parser.add_argument("--ab",action="store_true")
 args=parser.parse_args()
 try:sys.exit(run(args.profile,args.output_dir,args.mode,args.ab))
 except Exception as exc:
  output=pathlib.Path(args.output_dir)
  output.mkdir(parents=True,exist_ok=True)
  (output/"M01_ENGINE_V1_EXECUTION_ERROR.json").write_text(json.dumps({
    "schema":"M01_ENGINE_V1_RESULT","status":"ENGINE_RUN_FAILED_CLOSED",
    "error":repr(exc),"publication_allowed":False},indent=2)+"\n")
  print("ENGINE_RUN_FAILED_CLOSED",repr(exc),file=sys.stderr)
  sys.exit(2)
