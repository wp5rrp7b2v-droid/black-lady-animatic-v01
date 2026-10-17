#!/usr/bin/env python3
"""Non-approving real-pixel candidate search for M01 Unified Flame Engine V013.

Use original SHA-pinned stills and *existing* known architectural light ROI
to propose actual luminous hot spots. This NEVER calls a light source confirmed,
NEVER touches core code or approved source, and NEVER synthesizes a flame.

The output is a visual review diagram with every proposal on its source image.
Unknown or ambiguous sources remain CALIBRATION_REQUIRED for actual engine use.
"""
import argparse,hashlib,json,pathlib
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageFilter

ROOT=pathlib.Path(__file__).resolve().parents[1]
W,H=720,1280
from importlib import util
spec=util.spec_from_file_location("m01",ROOT/"scripts/m01_engine_v1.py")
m01=util.module_from_spec(spec)
spec.loader.exec_module(m01)

def candidate_search(image,fixture):
 r=fixture["region"]
 xx0,yy0,xx1,yy1=(int(round(v)) for v in r["roi_px"])
 # Registration proposals are restricted to known historical light regions.
 rgb=np.asarray(image)[yy0:yy1,xx0:xx1].astype(np.float32)
 rr,gg,bb=rgb[:,:,0],rgb[:,:,1],rgb[:,:,2]
 if not rr.size:return [],{"count_pixels":0,"warm_pixels":0}
 # Conservative "hot warm core" hypothesis, not a truth label. Bright wall,
 # pale stone or skin can be false positives and must be visually reviewed.
 gate=(rr>=160)&(gg>=90)&(rr>gg+12)&(gg>bb+8)
 hot=int(gate.sum())
 if hot==0:return [],{"count_pixels":int(rr.size),"warm_pixels":hot,"reason":"NO_BRIGHT_WARM_CANDIDATE"}
 blurred=np.asarray(image.filter(ImageFilter.GaussianBlur(radius=5)).crop((xx0,yy0,xx1,yy1))).astype(np.float32)
 local=(rr-blurred[:,:,0])*.66+(gg-blurred[:,:,1])*.34
 # If no apparent local peak, do not invent an emitter from flat wall glow.
 score=np.where(gate & (local>=8),local+rr*.024,-np.inf)
 yy,xx=np.nonzero(np.isfinite(score))
 if len(xx)==0:return [],{"count_pixels":int(rr.size),"warm_pixels":hot,"reason":"NO_DISTINCT_LOCAL_CORE"}
 indices=np.argsort(score[yy,xx])[::-1]
 chosen=[]
 for ind in indices[:min(len(indices),4000)]:
  x,y=int(xx[ind])+xx0,int(yy[ind])+yy0
  if any((x-v["x"])**2+(y-v["y"])**2 < 18**2 for v in chosen):continue
  chosen.append({"x":x,"y":y,"score":round(float(score[y-yy0,x-xx0]),1),
   "rgb":np.asarray(image)[y,x].tolist(),"status":"UNVERIFIED_WARM_PIXEL_HYPOTHESIS_NOT_FLAME_GT"})
  if len(chosen)==5:break
 return chosen,{"count_pixels":int(rr.size),"warm_pixels":hot,"distinct_peak_pixels":len(xx),
  "reason":"NONPO_PROPOSALS_REQUIRING_VISUAL_REVIEW"}

def annotate(image,report):
 image=image.copy()
 d=ImageDraw.Draw(image,"RGB")
 try:
  font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",17)
 except OSError:font=ImageFont.load_default()
 d.rectangle((0,0,719,35),fill=(15,15,18))
 d.text((10,8),report["profile_id"]+" | UNVERIFIED CANDIDATES",font=font,fill=(244,244,244))
 for i,fixture in enumerate(report["fixtures"]):
  x0,y0,x1,y1=[int(round(v)) for v in fixture["roi_px"]]
  d.rectangle((x0,y0,x1-1,y1-1),outline=(255,180,45),width=2)
  d.text((max(2,x0+2),max(38,y0+2)),f"{i+1}: {fixture['id'][:22]}",font=font,fill=(255,214,72),
   stroke_width=1,stroke_fill=(8,8,8))
  for k,hot in enumerate(fixture["candidate_pixels"]):
   x,y=hot["x"],hot["y"]
   d.ellipse((x-9,y-9,x+9,y+9),outline=(238,55,219),width=3)
   d.line((x-14,y,x+14,y),fill=(238,55,219),width=1)
   d.line((x,y-14,x,y+14),fill=(238,55,219),width=1)
   if k==0:d.text((min(W-45,x+10),max(39,y-14)),f"{i+1}",font=font,fill=(255,255,255))
 return image

def run(profile_name,dest):
 dest=pathlib.Path(dest)
 dest.mkdir(parents=True,exist_ok=True)
 p=m01.read_profile(profile_name)
 u=p.get("unified_flame_engine",{})
 assert u.get("registration_status")=="PENDING_CALIBRATION_NO_NEW_FLAME_RENDER"
 assert p["source"]["type"]=="still_png","CALIBRATION_ONLY_STILL_PNG_V013"
 src,_=m01.load_inputs(p)
 with Image.open(src) as f:
  image=f.convert("RGB").resize((W,H),Image.Resampling.LANCZOS)
 props=[]
 for f in p["fixtures"]:
  c,summary=candidate_search(image,f)
  props.append({"id":f["individual_source_id"],"fixture":f["id"],
     "roi_px":f["region"]["roi_px"],"candidate_pixels":c,"search_statistics":summary,
     "approved_flame_cores":0,"individual_light_has_verified_flame":False,
     "human_overlap_protection_verified":False})
 report={"schema":"M01_UNIFIED_CANDLE_FLAME_REGISTRATION_PROPOSALS_V013",
   "status":"CALIBRATION_REQUIRED_NO_FLAME_CORE_REGISTRATION",
   "profile_id":p["profile_id"],"profile_sha256":p["_atlas_sha256"],
   "source_png":p["source"]["path"],"exact_source_sha256":p["source"]["sha256"],
   "source_unchanged":m01.sha(src)==p["source"]["sha256"],
   "one_algorithm_for_core_and_halo":True,
   "reference_style":"M01_STYLE_BASELINE_V012",
   "roi_scope":"PREVIOUS_PO_ACCEPTABLE_V012_ARCHITECTURAL_LIGHT_AREAS_AS_HYPOTHESIS_SEARCH_BOUNDARY",
   "candidate_method":"BRIGHT_WARM_PIXEL_LOCAL_CONTRAST_NONAUTHORITATIVE",
   "camera_scale":[W,H],"fixtures":props,
   "aggregate_candidate_count":sum(len(f["candidate_pixels"]) for f in props),
   "registration_PO_approved":False,"people_mask_ground_truth_approved":False,
   "full_engine_flame_render_authorized":False,
   "no_fabricated_flames":True,"original_png_unmodified":True,
   "no_video_or_master_replacement":True,"no_main_merge":True,
   "next":"Inspect candidate overlay against source, confirm or reject actual cores; no automatic promotion."}
 visual=annotate(image,report)
 suffix=p["profile_id"]
 overlay=dest/f"{suffix}_SOURCE_CANDIDATE_OVERLAY_V001.jpg"
 visual.save(overlay,quality=92,subsampling=0)
 with Image.open(overlay) as chk:assert chk.size==(W,H)
 report["review_overlay"]=overlay.name
 report["review_overlay_sha256"]=m01.sha(overlay)
 report_path=dest/f"{suffix}_CANDIDATE_QC.json"
 report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 print(json.dumps({"status":report["status"],"profile":suffix,
   "proposals":report["aggregate_candidate_count"],"figures":len(props),
   "overlay_sha256":report["review_overlay_sha256"]},ensure_ascii=False))
 return report

if __name__=="__main__":
 ap=argparse.ArgumentParser()
 ap.add_argument("--profile",required=True)
 ap.add_argument("--out",required=True)
 args=ap.parse_args()
 run(args.profile,args.out)
