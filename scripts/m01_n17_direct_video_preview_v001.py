#!/usr/bin/env python3
"""N17 M01 real video RESULT preview. Only the approved 4 actual flames.

Produces a 12.5667-second preview and readable synchronized A/B comparison.
Uses frame-aligned existing A1 person masks; no repeated model inference, no
ground truth promotion, no modifications to approved videos or canonical assets.
"""
import hashlib, json, math, pathlib, subprocess, zipfile, time
import numpy as np
from PIL import Image

ROOT=pathlib.Path(__file__).resolve().parents[1]
SOURCE=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
AUDIT=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002/a1_n17_full_frame_masks_v001/M01_A1_N17_ALL_377_FRAMES_PROTECTION_FLAME_QA_V001.json"
MASKPACK=AUDIT.parent/"M01_A1_N17_MACHINE_MASK_PROPOSALS_377_FRAMES_V001.zip"
APPROVAL=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002/A1_N17_PO_POSITION_APPROVAL_2026-10-17.json"
OUT=ROOT/"_m01_n17_visual_result_v001"
START,END,W,H,FPS=281,658,720,1280,30
COUNT=END-START
SRC_SHA="7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402"
VIDEO="M01_N17_CANDLE_ENGINE_RESULT_REVIEW_V001.mp4"
AB="M01_N17_ORIGINAL_VS_CANDLE_RESULT_AB_V001.mp4"
REPORT="M01_N17_CANDLE_ENGINE_RESULT_QC_V001.json"
def digest(p):
 h=hashlib.sha256()
 with p.open("rb") as stream:
  for data in iter(lambda:stream.read(1048576),b""):h.update(data)
 return h.hexdigest()
def ffprobe(path):
 return json.loads(subprocess.check_output(["ffprobe","-v","error","-show_entries",
   "stream=index,codec_type,codec_name,width,height,nb_frames,r_frame_rate:format=duration",
   "-of","json",str(path)],text=True))
def bitmask(data):
 return np.unpackbits(np.frombuffer(data,dtype=np.uint8),
     bitorder="little",count=W*H).reshape(H,W).astype(bool)
def raw_exact():
 cmd=["ffmpeg","-hide_banner","-loglevel","error","-xerror","-i",str(SOURCE),
   "-map","0:v:0","-vf",f"select=between(n\\,{START}\\,{END-1})",
   "-vsync","vfr","-pix_fmt","rgb24","-f","rawvideo","pipe:1"]
 return subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
def lum_flicker(time_s,phase):
 # soft independent dual-oscillation, not one synchronized global flicker.
 return (.56*math.sin(time_s*2*math.pi*(1.05+.12*phase)+phase*1.7)+
         .28*math.sin(time_s*2*math.pi*(2.13+.15*phase)+.9+phase*2.1)+
         .16*math.sin(time_s*2*math.pi*(3.36+.10*phase)+1.1+phase*1.2))
def source_light_m01(rgb,person,uncertain,core_masks,records,frame_id,halo_coords):
 # In this shot, only upper-right wall/candle is animated. No full-scene glow.
 # Float RGBA-like computed additive warmth; preserves all protected people and uncertain boundaries.
 output=rgb.astype(np.float32)
 ys,xs=np.ogrid[:H,:W]
 xcrop=slice(525,720);ycrop=slice(0,320)
 rx=xs[:,xcrop].astype(np.float32)
 ry=ys[ycrop,:].astype(np.float32)
 region=output[ycrop,xcrop]
 base=rgb[ycrop,xcrop].astype(np.float32)
 prot=person[ycrop,xcrop]|uncertain[ycrop,xcrop]
 frame_local=frame_id-START
 # F542-F552: cross-faded light gradually appears as image changes.
 # Source flame already exists before signal begins; do not synthesize lights.
 appearance=np.clip((frame_id-542)/10,0,1)
 # avoid cut boundary effect at end of approved N17 still
 ending=np.clip((END-1-frame_id)/7,0,1)
 gate=float(min(appearance,ending))
 if gate<=0:
  return rgb.tobytes(),{"gate":0,"changed":0,"protected_changed":0,"max_abs_delta":0}
 time_s=frame_local/FPS
 additive=np.zeros(region.shape,dtype=np.float32)
 # Local wall reflected light is weaker than flame itself, independent per source.
 for j,track in enumerate(halo_coords):
  fx,fy=float(track[0]),float(track[1])
  flicker=lum_flicker(time_s,j+1)
  # Modulation around input natural brightness: changes observable but subdued.
  gaussian=np.exp(-.5*(((rx-fx)/49)**2+((ry-fy)/69)**2)).astype(np.float32)
  gain=(7.5*flicker+1.6*math.sin(time_s*math.pi*1.55+(j*.93)))
  additive += gaussian[:,:,None]*np.array([gain,gain*.57,gain*.18],dtype=np.float32)
 # Stable non-candle regions remain unchanged, no frame-wide multiplication.
 additive*=gate
 proposed=np.clip(base+additive,0,255)
 # Flame core is stronger, source glow remains low; use frame-derived four mask proposals.
 for j,mask in enumerate(core_masks):
  center=records[j]["track_center_px"]
  cx,cy=(float(center[0]),float(center[1]))
  yy0=max(0,int(cy)-14);yy1=min(320,int(cy)+15)
  xx0=max(525,int(cx)-10);xx1=min(720,int(cx)+11)
  if yy1<=yy0 or xx1<=xx0:continue
  flame=mask[yy0:yy1,xx0:xx1]
  # core mask comes from observed bright original video pixel only; no synthetic flame silhouette.
  delta=gate*lum_flicker(time_s,j+1)*np.array([29.0,20.0,9.0],dtype=np.float32)
  current=proposed[yy0:yy1,xx0-525:xx1-525]
  flame_safe=flame & ~prot[yy0:yy1,xx0-525:xx1-525]
  current[flame_safe]=np.clip(current[flame_safe]+delta,0,255)
 # Never modify any pixel matching the per-frame people OR uncertain bbox regions.
 proposed[prot]=base[prot]
 # Explicit spatial effect window: x>=525,y<=320
 output[ycrop,xcrop]=proposed
 encoded=np.clip(output,0,255).astype("uint8")
 diff=np.any(encoded!=rgb,axis=2)
 full_protect=person|uncertain
 assert not np.any(diff&full_protect)
 # Outside fixed local ROI stays raw-exact.
 outside=diff.copy();outside[ycrop,xcrop]=False
 assert not np.any(outside)
 return encoded.tobytes(),{"gate":round(gate,3),"changed":int(diff.sum()),
  "protected_changed":0,"max_abs_delta":int(np.max(np.abs(encoded.astype(np.int16)-rgb.astype(np.int16))))}

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 assert digest(SOURCE)==SRC_SHA,"V006_SOURCE_CHANGED"
 audit=json.loads(AUDIT.read_text())
 approval=json.loads(APPROVAL.read_text())
 assert audit["source_frame_count"]==COUNT and audit["source_video_sha256"]==SRC_SHA
 assert approval["approval_scope"]=="PO_VISUAL_APPROVED_F601_LOCATOR_CENTERS_ONLY"
 assert approval["source_frame"]==601 and len(approval["flames"])==4
 assert digest(MASKPACK)==audit["mask_package_sha256"]
 frames={r["frame_index"]:r for r in audit["frames"]}
 track_source=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002/a1_n17_flame_locator_v002/M01_A1_N17_LATE_CANDLE_LOCATOR_V002.json"
 track=json.loads(track_source.read_text())
 track_frames=np.array([r["frame"] for r in track["source_tracks"]],dtype=float)
 coords=np.array([[[f["brightness_peak_candidate_px"][0],f["brightness_peak_candidate_px"][1]] for f in s["flames"]] for s in track["source_tracks"]],dtype=float)
 stem=OUT/"n17_effect_videoonly.mp4"
 enc=subprocess.Popen(["ffmpeg","-hide_banner","-v","error","-y",
  "-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-framerate",str(FPS),"-i","pipe:0",
  "-an","-c:v","libx264","-preset","veryfast","-crf","18","-pix_fmt","yuv420p","-r",str(FPS),
  "-movflags","+faststart",str(stem)],stdin=subprocess.PIPE)
 dec=raw_exact()
 result=[]
 try:
  with zipfile.ZipFile(MASKPACK) as z:
   for idx in range(START,END):
    n=W*H*3
    parts=[]
    while n:
     chunk=dec.stdout.read(n)
     if not chunk:raise RuntimeError(f"SHORT_VIDEO_FRAME_{idx}")
     n-=len(chunk);parts.append(chunk)
    raw=b"".join(parts)
    assert hashlib.sha256(raw).hexdigest()==frames[idx]["decoded_source_rgb_sha256"]
    rgb=np.frombuffer(raw,dtype=np.uint8).reshape(H,W,3).copy()
    person=bitmask(z.read(frames[idx]["person_mask_file"]))
    uncertain=bitmask(z.read(frames[idx]["uncertainty_file"]))
    if idx>=550:
     masks=[bitmask(z.read(x["path"])) for x in frames[idx]["flame_core_mask_files"]]
     candle=frames[idx]["flame_core_proposals"]
    else:
     masks=[np.zeros((H,W),dtype=bool) for _ in range(4)]
     # Pre-F550 transition starts with haloes only; no in-frame source-created flame pixels.
     candle=[]
    clamped=float(min(max(idx,550),645))
    halo_coords=np.column_stack([np.interp(clamped,track_frames,coords[:,j,0]) for j in range(4)]).T
    halo_coords[:,1]=[np.interp(clamped,track_frames,coords[:,j,1]) for j in range(4)] if False else halo_coords[:,1]
    # Explicit interpolated normalized centers j x 2, safe on constant scene ROI.
    anchors=np.array([[np.interp(clamped,track_frames,coords[:,j,0]),
                       np.interp(clamped,track_frames,coords[:,j,1])] for j in range(4)])
    if not candle:
     candle=[{"track_center_px":list(anchors[j])} for j in range(4)]
    edited,stat=source_light_m01(rgb,person,uncertain,masks,candle,idx,anchors)
    enc.stdin.write(edited)
    result.append({"frame_index":idx,**stat})
  assert dec.stdout.read(1)==b""
 finally:
  dec.stdout.close();enc.stdin.close()
 err=dec.stderr.read().decode(errors="replace");dec.stderr.close()
 assert dec.wait()==0,err[-800:]
 assert enc.wait()==0
 assert len(result)==COUNT
 assert all(r["protected_changed"]==0 for r in result)
 assert result[0]["changed"]==0 and result[-1]["changed"]==0
 assert any(r["changed"]>1000 for r in result),"RESULT_EFFECT_INVISIBLE"
 # N17 audio: source original editorial waveform, sliced at absolute 30 fps frame time.
 # Same trimmed N17 audio is mapped onto effect and comparison; no soundtrack replacement.
 effect=OUT/VIDEO
 subprocess.run(["ffmpeg","-hide_banner","-v","error","-y",
   "-i",str(stem),"-ss",f"{START/FPS:.9f}","-t",f"{COUNT/FPS:.9f}",
   "-i",str(SOURCE),"-map","0:v:0","-map","1:a:0","-c:v","copy","-c:a","aac",
   "-b:a","160k","-shortest","-movflags","+faststart",str(effect)],check=True)
 ab=OUT/AB
 subprocess.run(["ffmpeg","-hide_banner","-v","error","-y",
   "-i",str(SOURCE),"-i",str(effect),
   "-filter_complex",
   f"[0:v]trim=start_frame={START}:end_frame={END},setpts=PTS-STARTPTS,"
   "drawtext=text='ORIGINAL':fontcolor=white:fontsize=34:x=18:y=24,"
   "pad=iw:ih+60:0:60:black[a];"
   "[1:v]setpts=PTS-STARTPTS,"
   "drawtext=text='M01 CANDLE PREVIEW':fontcolor=white:fontsize=34:x=18:y=24,"
   "pad=iw:ih+60:0:60:black[b];"
   "[a][b]hstack=inputs=2[v]",
   "-map","[v]","-map","1:a:0","-c:v","libx264","-preset","veryfast",
   "-crf","21","-pix_fmt","yuv420p","-c:a","copy","-r",str(FPS),
   "-frames:v",str(COUNT),"-movflags","+faststart",str(ab)],check=True)
 stem.unlink(missing_ok=True)
 for p in (effect,ab):
  info=ffprobe(p)
  v=next(s for s in info["streams"] if s["codec_type"]=="video")
  assert int(v["nb_frames"])==COUNT,(p.name,v)
  assert v["r_frame_rate"]=="30/1"
  assert next(s for s in info["streams"] if s["codec_type"]=="audio")["codec_name"]=="aac"
 # Output two review videos; do not update M01 stage gate without PO.
 report={"task":"M01_N17_CANDLE_ENGINE_DIRECT_VISUAL_RESULT_V001",
  "status":"REVIEW_MP4_RENDERED_PO_VISUAL_DECISION_PENDING",
  "source_video_sha256":SRC_SHA,
  "scope":"N17_ONLY_PREVIEW_NOT_MASTER",
  "source_frame_range":[START,END-1],"frames":COUNT,"fps":FPS,
  "duration_seconds":COUNT/FPS,
  "reference_flames":"N17_RIGHT_SCONCE_01_4_CENTERS_PO_APPROVED_F601",
  "effect":"Independent per-candle warm glow, light-bound core flicker, soft transition with preexisting crossfade",
  "mask_provenance_sha256":digest(MASKPACK),
  "individual_candle_signals":4,
  "exclude_people_and_bbox_uncertain_regions_in_all_frames":True,
  "modified_pixels_outside_spatial_candle_window":0,
  "modified_person_or_uncertain_pixels_raw":sum(x["protected_changed"] for x in result),
  "changed_raw_frame_count":sum(x["changed"]>0 for x in result),
  "max_raw_rgb_delta":max(x["max_abs_delta"] for x in result),
  "approved_original_visual":True,"new_video_PO_approved":False,
  "video":{"file":VIDEO,"sha256":digest(effect),"size":effect.stat().st_size},
  "comparison":{"file":AB,"sha256":digest(ab),"size":ab.stat().st_size},
  "frames_summary":{"first":result[0],"middle":result[310],"last":result[-1]},
  "no_canonical_publication":True,"no_main_merge":True,
  "original_source_unchanged":digest(SOURCE)==SRC_SHA,
  "batch_gate":"HOLD","only_review_output":True}
 (OUT/REPORT).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 print("N17_M01_REAL_VIDEO_REVIEW_OUTPUT_READY",json.dumps({
  "video":report["video"],"ab":report["comparison"],
  "effect_changed_frames":report["changed_raw_frame_count"],
  "max_raw_delta":report["max_raw_rgb_delta"],
  "mask_infringement":0,"po_approval":False},ensure_ascii=False),flush=True)
if __name__=="__main__":main()
