#!/usr/bin/env python3
"""N17 temporal mask audit: all 377 source frames, four approved F601 center points.

Output is a fail-closed review-only dataset. Flame silhouettes and people masks
are machine PROPOSALS, not human-validated Ground Truth. A workflow PASS means
the exact-source evidence package was created, not safety/production approval.
"""
from __future__ import annotations
import hashlib, io, json, pathlib, subprocess, time, zipfile
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
from ultralytics import YOLO
import ultralytics

ROOT=pathlib.Path(__file__).resolve().parents[1]
BASE=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002"
SOURCE=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
BENCH=BASE/"evidence/M01_STAGE_A_MACHINE_BENCHMARK_V002.json"
EDL=ROOT/"production/editorial_specs/S02_B_V006_CINEMATIC_ROUGH_EDL_V001.json"
APPROVAL=BASE/"A1_N17_PO_POSITION_APPROVAL_2026-10-17.json"
TRACK=BASE/"a1_n17_flame_locator_v002/M01_A1_N17_LATE_CANDLE_LOCATOR_V002.json"
OUT=ROOT/"_m01_stage_a1_n17_all_frame_masks_v001"
OUTPUT_JSON="M01_A1_N17_ALL_377_FRAMES_PROTECTION_FLAME_QA_V001.json"
MASK_ZIP="M01_A1_N17_MACHINE_MASK_PROPOSALS_377_FRAMES_V001.zip"
PREVIEW="M01_A1_N17_377_FRAME_CANDLE_PERSON_PROTECTION_QA_V001.jpg"
N_FIRST,N_LAST=281,657
W,H=720,1280
SAMPLE=[281,337,469,520,540,550,580,601,630,645,657]
VISIBILITY_FIRST_VERIFIED_CANDIDATE=550
COLORS=[(244,37,190),(54,234,241),(253,204,65),(110,237,82)]

def sha(data):
 h=hashlib.sha256()
 if isinstance(data,pathlib.Path):
  with data.open("rb") as f:
   for b in iter(lambda:f.read(1048576),b""):h.update(b)
 else:h.update(data)
 return h.hexdigest()
def ft(n):
 path="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
 return ImageFont.truetype(path,n) if pathlib.Path(path).exists() else ImageFont.load_default()
def exact_source_stream():
 cmd=["ffmpeg","-hide_banner","-loglevel","error","-xerror",
      "-i",str(SOURCE),"-map","0:v:0",
      "-vf",f"select=between(n\\,{N_FIRST}\\,{N_LAST})",
      "-vsync","vfr","-pix_fmt","rgb24","-f","rawvideo","pipe:1"]
 return subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
def person_segments(rgb,model):
 prediction=model.predict(rgb,classes=[0],conf=.14,iou=.55,
     imgsz=640,retina_masks=True,device="cpu",verbose=False)[0]
 seg=np.zeros((H,W),np.uint8)
 bbox=np.zeros((H,W),np.uint8)
 n=len(prediction.boxes) if prediction.boxes is not None else 0
 raw_masks=prediction.masks.data.cpu().numpy() if prediction.masks is not None else np.empty((0,H,W))
 details=[]
 for j in range(n):
  b=prediction.boxes[j]
  box=[int(round(float(x))) for x in b.xyxy[0].cpu().numpy()]
  x0,y0,x1,y1=box
  x0=max(0,x0-10);y0=max(0,y0-10);x1=min(W,x1+10);y1=min(H,y1+10)
  bbox[y0:y1,x0:x1]=1
  if j<len(raw_masks):
   m=raw_masks[j]
   if m.shape!=(H,W):m=cv2.resize(m.astype(np.float32),(W,H),interpolation=cv2.INTER_NEAREST)
   seg[m>.45]=1
  details.append({"bbox":[x0,y0,x1,y1],"model_confidence":round(float(b.conf[0]),4),
      "instance_mask_present":j<len(raw_masks)})
 seg=cv2.dilate(seg,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(27,27)))
 uncertain=(bbox>0)&(seg==0)
 return seg.astype(bool),uncertain,details
def flame_tracks():
 track=json.loads(TRACK.read_text())
 approval=json.loads(APPROVAL.read_text())
 assert approval["approval_scope"]=="PO_VISUAL_APPROVED_F601_LOCATOR_CENTERS_ONLY"
 assert approval["source_frame"]==601 and len(approval["flames"])==4
 assert track["source_flames_count_candidate"]==4
 samples=track["source_tracks"]
 keys=[s["frame"] for s in samples]
 assert keys==[550,580,601,630,645]
 coords={}
 for j in range(4):
  data=[]
  for s in samples:
   xy=s["flames"][j]["brightness_peak_candidate_px"]
   assert xy is not None
   data.append(xy)
  coords[j]=np.array(data,np.float32)
 f601=[s for s in samples if s["frame"]==601][0]
 for j,item in enumerate(approval["flames"]):
  assert item["center_px"]==f601["flames"][j]["brightness_peak_candidate_px"]
 return np.array(keys,dtype=np.float32),coords,approval
def four_flame_masks(rgb,person,uncertain,frame_index,track_keys,tracks):
 """Diagnostic flame-core proposals, impossible to promote without human review."""
 red=rgb[:,:,0].astype(np.int16)
 green=rgb[:,:,1].astype(np.int16)
 blue=rgb[:,:,2].astype(np.int16)
 warm=(red>=188)&(green>=133)&(red>=green-17)&(red-blue>=26)&(green-blue>=13)
 mask_stack=[]
 candidate=[]
 reserved=np.zeros((H,W),bool)
 human_conflicts=0
 bbox_uncertainty_conflicts=0
 for j in range(4):
  center=[float(np.interp(frame_index,track_keys,tracks[j][:,0])),
          float(np.interp(frame_index,track_keys,tracks[j][:,1]))]
  x,y=center
  x0=max(0,int(x)-9);x1=min(W,int(x)+11)
  y0=max(0,int(y)-13);y1=min(H,int(y)+15)
  yy,xx=np.ogrid[y0:y1,x0:x1]
  ell=(((xx-x)/8.2)**2+((yy-y)/11.0)**2)<=1
  local=warm[y0:y1,x0:x1]&ell&(~reserved[y0:y1,x0:x1])
  # First detect conflicts before clipping, then remove people to ensure explicit safety.
  human_conflicts+=int(np.count_nonzero(local&person[y0:y1,x0:x1]))
  bbox_uncertainty_conflicts+=int(np.count_nonzero(local&uncertain[y0:y1,x0:x1]))
  local &= ~person[y0:y1,x0:x1]
  local &= ~uncertain[y0:y1,x0:x1]
  result=np.zeros((H,W),dtype=bool)
  result[y0:y1,x0:x1]=local
  reserved|=result
  num=int(local.sum())
  cy,cx=np.nonzero(result)
  centroid=[round(float(cx.mean()),2),round(float(cy.mean()),2)] if num else None
  mask_stack.append(result)
  candidate.append({
    "flame_id":f"N17_RIGHT_SCONCE_01_FLAME_{j+1:02d}",
    "track_center_px":[round(x,2),round(y,2)],
    "proposed_core_pixels":num,
    "proposed_core_centroid_px":centroid,
    "core_size_and_visibility_needs_visual_review":num<3 or num>150,
    "frame_flame_core_approved":False})
 return mask_stack,candidate,human_conflicts,bbox_uncertainty_conflicts

def bitpacked(mask):
 # Explicit file format: little-endian row-major 720x1280 uint8 binary mask, bitorder="little".
 return np.packbits(mask.astype(np.uint8).ravel(),bitorder="little").tobytes()
def review_annotated(rgb,mask,uncertain,flames,idx):
 original=Image.fromarray(rgb,"RGB").resize((360,640),Image.Resampling.LANCZOS)
 out=rgb.astype(np.float32)
 out[mask]=out[mask]*.58+np.array([28,98,250])*.42
 ys,xs=np.indices((H,W),dtype=np.int16)
 hatch=uncertain & (((xs+ys)%20)<2)
 out[hatch]=out[hatch]*.25+np.array([255,151,21])*.75
 if flames is not None:
  for j,fl in enumerate(flames):
   where=fl.astype(bool)
   if np.any(where):
    out[where]=out[where]*.30+np.array(COLORS[j],dtype=np.float32)*.70
 display=Image.fromarray(np.clip(out,0,255).astype(np.uint8))
 d=ImageDraw.Draw(display)
 if flames is not None:
  for j,fl in enumerate(flames):
   xy=np.argwhere(fl)
   if xy.size:
    xx=int(np.mean(xy[:,1]));yy=int(np.mean(xy[:,0]))
    d.ellipse([xx-11,yy-11,xx+11,yy+11],outline=COLORS[j],width=3)
    d.text((max(0,min(xx+15,690)),max(0,yy-16)),str(j+1),font=ft(23),
       fill=(255,255,255),stroke_width=2,stroke_fill=(0,0,0))
 second=display.resize((360,640),Image.Resampling.LANCZOS)
 panel=Image.new("RGB",(740,684),(16,17,19))
 d2=ImageDraw.Draw(panel)
 panel.paste(original,(8,36))
 panel.paste(second,(378,36))
 d2.text((8,7),f"N17 F{idx} SOURCE",font=ft(19),fill="white")
 d2.text((380,7),"PERSON BLUE / CORE COLORS",font=ft(17),fill="white")
 return panel

def main():
 spec=json.loads(BENCH.read_text())
 assert spec["source_video_sha256"]==sha(SOURCE)
 by={x["shot_id"]:x for x in spec["samples"]}
 n17=by["N17"]
 indexes={f["frame_index"]:f for f in n17["frames"]}
 keys,track,approval=flame_tracks()
 model=YOLO("yolo11n-seg.pt")
 model_hash=sha(pathlib.Path("yolo11n-seg.pt"))
 assert model_hash==spec["segmentation_model_sha256"],"PERSON_MODEL_BINARY_DRIFT"
 OUT.mkdir(parents=True,exist_ok=True)
 maskzip=OUT/MASK_ZIP
 proc=exact_source_stream()
 nbytes=W*H*3
 frames=[]
 preview={}
 start=time.monotonic()
 try:
  with zipfile.ZipFile(maskzip,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
   for idx in range(N_FIRST,N_LAST+1):
    payload=bytearray()
    while len(payload)<nbytes:
     part=proc.stdout.read(nbytes-len(payload))
     if not part:raise RuntimeError(f"TRUNCATED_INPUT_FRAME_{idx}")
     payload.extend(part)
    rgb=np.frombuffer(bytes(payload),dtype=np.uint8).reshape(H,W,3).copy()
    raw_sha=sha(payload)
    if idx in indexes:assert raw_sha==indexes[idx]["decoded_rgb_sha256"],f"EXACT_BENCHMARK_FRAME_DRIFT_{idx}"
    person,uncertain,detected=person_segments(rgb,model)
    # Before first observed candle, no flame reconstruction is allowed. The real
    # boundary needs visual confirmation and this audit does not infer it.
    light_state="CANDIDATE_VISIBLE_REQUIRES_CONFIRMATION" if idx>=550 else ("NO_VISIBLE_LIGHT_AT_VERIFIED_SAMPLES_ONLY" if idx in (337,469,520) else "UNDETERMINED_PENDING_VISUAL_ONSET")
    flames=None; candidates=[];hits=uncertain_hits=0
    if idx>=550:
     flames,candidates,hits,uncertain_hits=four_flame_masks(rgb,person,uncertain,idx,keys,track)
     assert len(flames)==4
     assert all(np.count_nonzero(fl&person)==0 for fl in flames)
     assert all(np.count_nonzero(fl&uncertain)==0 for fl in flames)
    person_blob=bitpacked(person)
    uncertainty_blob=bitpacked(uncertain)
    pname=f"persons/F{idx:04d}.bitpack"
    upath=f"uncertain_bbox_regions/F{idx:04d}.bitpack"
    z.writestr(pname,person_blob)
    z.writestr(upath,uncertainty_blob)
    mask_files=[]
    for j,fl in enumerate(flames or []):
     key=f"flames_{j+1:02d}/F{idx:04d}.bitpack"
     blob=bitpacked(fl)
     z.writestr(key,blob)
     mask_files.append({"path":key,"sha256":sha(blob),"source_index":j+1})
    frames.append({
     "frame_index":idx,"decoded_source_rgb_sha256":raw_sha,
     "detected_people_count":len(detected),
     "person_mask_pixels":int(person.sum()),
     "bbox_only_uncertainty_pixels":int(uncertain.sum()),
     "person_mask_file":pname,"person_mask_sha256":sha(person_blob),
     "uncertainty_file":upath,"uncertainty_sha256":sha(uncertainty_blob),
     "light_visibility_state":light_state,
     "flame_core_mask_files":mask_files,
     "flame_core_proposals":candidates,
     "pre_exclusion_person_collision_pixels":hits,
     "pre_exclusion_bbox_uncertainty_collision_pixels":uncertain_hits,
     "mask_person_intersection_after_exclusion":0,
     "frame_protection_ground_truth_approved":False,
     "flame_shape_ground_truth_approved":False})
    if idx in SAMPLE:
     preview[idx]=review_annotated(rgb,person,uncertain,flames,idx)
    if (idx-N_FIRST+1)%60==0:print("FRAMES_PROCESSED",idx-N_FIRST+1,flush=True)
   assert proc.stdout.read(1)==b""
 finally:
  proc.stdout.close()
 err=proc.stderr.read().decode(errors="replace");proc.stderr.close()
 rc=proc.wait()
 assert rc==0,err[-1000:]
 assert len(frames)==377
 # Build contact sheet of immutable exact source frames and diagnostic proposals.
 panel_w,panel_h=740,684
 overview=Image.new("RGB",(panel_w*3,panel_h*4),(13,14,16))
 for i,idx in enumerate(SAMPLE):
  row,col=divmod(i,3)
  overview.paste(preview[idx],(col*panel_w,row*panel_h))
 picture=OUT/PREVIEW
 overview.save(picture,"JPEG",quality=80,optimize=True)
 (OUT/(PREVIEW+".b64.txt")).write_text(__import__("base64").b64encode(picture.read_bytes()).decode()+"\n")
 from collections import Counter
 all_states=Counter(x["light_visibility_state"] for x in frames)
 detections_low=sum(f["detected_people_count"]==0 for f in frames)
 flagged_core=sum(any(x["core_size_and_visibility_needs_visual_review"] for x in f["flame_core_proposals"]) for f in frames)
 prehuman=sum(f["pre_exclusion_person_collision_pixels"] for f in frames)
 preunc=sum(f["pre_exclusion_bbox_uncertainty_collision_pixels"] for f in frames)
 summary={
  "schema":"M01_A1_N17_ALL_FRAME_FLAME_PERSON_MACHINE_AUDIT_V001",
  "status":"MACHINE_MASKS_BUILT__VISUAL_GT_PENDING__BATCH_HOLD",
  "source_video_sha256":spec["source_video_sha256"],
  "source_EDL":str(EDL.relative_to(ROOT)),
  "start_frame":N_FIRST,"end_frame_inclusive":N_LAST,
  "source_frame_count":len(frames),
  "source_frame_identity_checks":sorted(indexes),
  "PO_approved_frame_601_centers":[x["center_px"] for x in approval["flames"]],
  "PO_approval_scope":approval["approval_scope"],
  "registered_fixture_id":"N17_RIGHT_SCONCE_01",
  "person_model_file":"yolo11n-seg.pt","person_model_sha256":model_hash,
  "person_mask_algorithm":"YOLO11n instance segmentation @640, conf 0.14, dilated 13px",
  "bbox_uncertainty":"expanded person detection boxes outside segment masks retained as separate fail-closed region",
  "mask_pack_format":"ZIP DEFLATED containing bitpack little-endian (row-major 1280x720, one bit per pixel)",
  "mask_package":MASK_ZIP,"mask_package_sha256":sha(maskzip),
  "preview":PREVIEW,"preview_sha256":sha(picture),
  "source_light_visibility_states":dict(all_states),
  "unverified_light_first_seen_window":"F520 absent, F550 present at sampled times; onset not proved at intervening frames",
  "human_detection_zero_person_frames":detections_low,
  "flame_frames_needing_segmentation_visual_review":flagged_core,
  "candidate_flame_pixels_pre_exclusion_intersecting_person":prehuman,
  "candidate_flame_pixels_pre_exclusion_intersecting_bbox_uncertainty":preunc,
  "all_mask_person_intersections_after_exclusion":0,
  "all_frame_person_protection_approved":False,
  "all_frame_flame_shapes_approved":False,
  "automatic_light_registration_release":False,
  "s02b_pilot_approved":False,
  "cross_scene_engine_approved":False,
  "m01_batch_gate":"HOLD",
  "no_video_rendered":True,"no_main_merge":True,
  "elapsed_processing_seconds":round(time.monotonic()-start,2),
  "frames":frames}
 (OUT/OUTPUT_JSON).write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
 assert sha(SOURCE)==spec["source_video_sha256"]
 print("M01_N17_377_FRAME_MACHINE_MASK_DATASET_COMPLETED_NOT_GT",json.dumps({
  "frames":len(frames),"sampled":SAMPLE,"person_detect_zero_frames":detections_low,
  "core_warnings":flagged_core,
  "human_preclip_pixels":prehuman,
  "bbox_only_preclip_pixels":preunc,
  "mask_sha256":summary["mask_package_sha256"],
  "elapsed_seconds":summary["elapsed_processing_seconds"]},ensure_ascii=False),flush=True)
if __name__=="__main__":
 main()
