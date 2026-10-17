#!/usr/bin/env python3
"""M01 universal still-frame flame masks from PO-approved V014 actual candle centers.

No new guessed points. Binary masks are clipped to small validated flame ellipses
and selected only from actual warm source pixels in SHA-pinned approved stills.
Produces candidate source masks, a new V015 per-shot Scene Light Atlas, and
inspection images; artwork remains unapproved and no shot/master is changed.
"""
import argparse,base64,hashlib,json,pathlib,zipfile,collections,copy
import numpy as np
from PIL import Image,ImageDraw,ImageFont
import importlib.util
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("engine",ROOT/"scripts/m01_engine_v1.py")
eng=importlib.util.module_from_spec(spec);spec.loader.exec_module(eng)
DRAFT=ROOT/"production/environment_dynamic/benchmarks/m01_stage_a_v002/M01_V014_TRUE_FLAME_CENTERS_VISUAL_CORRECTION_CANDIDATE.json"
def local_mask(rgb,x,y,shot,flame_id):
  # Small geometry bound, then conservative physical RGB test (not bright-wall search).
  is_deep=("DEEP" in flame_id or "RIGHT_" in flame_id)
  sx,sy=(5,8) if is_deep else (6,11)
  h,w=rgb.shape[:2]
  x0=max(0,x-10);x1=min(w,x+11);y0=max(0,y-16);y1=min(h,y+17)
  ys,xs=np.ogrid[y0:y1,x0:x1]
  ell=((xs-x)/sx)**2+((ys-y)/sy)**2<=1
  tile=rgb[y0:y1,x0:x1].astype(np.int16)
  R,G,B=tile[:,:,0],tile[:,:,1],tile[:,:,2]
  # Saturated flame cores can have nearly equal channels, but orange wall
  # outside small elliptical hotspot is excluded by spatial constraint.
  warm=(R>=210)&(G>=145)&(R>=G+5)&(G>=B+8)
  allowed=ell & warm
  # Local connectivity to approved flame center within a tiny 4-px seed radius.
  near=((xs-x)**2+(ys-y)**2)<=4**2
  candidates=np.argwhere(allowed & near)
  if not len(candidates):raise RuntimeError(f"NO_ILLUMINATED_CORE_NEAR_APPROVED_CENTER_{shot}_{flame_id}_{x}_{y}")
  center_dist=(candidates[:,1]+x0-x)**2+(candidates[:,0]+y0-y)**2
  cy,cx=map(int,candidates[int(np.argmin(center_dist))])
  todo=collections.deque([(cy,cx)]);connected=np.zeros_like(allowed,bool)
  connected[cy,cx]=True
  while todo:
    py,px=todo.popleft()
    for yy in range(max(py-1,0),min(py+2,allowed.shape[0])):
      for xx in range(max(px-1,0),min(px+2,allowed.shape[1])):
        if allowed[yy,xx] and not connected[yy,xx]:
          connected[yy,xx]=True;todo.append((yy,xx))
  count=int(connected.sum())
  if not 6<=count<=230:raise RuntimeError(f"FLAME_CONNECTED_CORE_AREA_IMPLAUSIBLE_{shot}_{flame_id}_{count}")
  yy,xx=np.nonzero(connected)
  xc=xx+x0;yc=yy+y0
  if np.linalg.norm([xc.mean()-x,yc.mean()-y])>5:raise RuntimeError(f"FLAME_MASK_CENTER_DRIFT_{shot}_{flame_id}")
  mask=np.zeros((h,w),dtype=bool);mask[y0:y1,x0:x1]=connected
  return mask,{"mask_pixels":count,"bounds_px":[int(xc.min()),int(yc.min()),int(xc.max()+1),int(yc.max()+1)],
               "mask_centroid_px":[round(float(xc.mean()),2),round(float(yc.mean()),2)],
               "max_offset":[int(abs(xc-x).max()),int(abs(yc-y).max())],
               "method":"RGB-WARM_CONNECTED_REAL_PIXELS_ELLIPSE_LOCAL_AROUND_PO_APPROVED_CENTER"}

def viz(rgb,points,masks):
  im=Image.fromarray(rgb).convert("RGB")
  image=im.copy();d=ImageDraw.Draw(image)
  try:font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",16)
  except OSError:font=ImageFont.load_default()
  for p in points:
    x,y=p["center"]
    mask=masks[p["id"]]
    yy,xx=np.where(mask)
    # outline pixel-connected core mask in cyan; leave original photo intact elsewhere
    xy=[(int(xx[i]),int(yy[i])) for i in range(len(xx))]
    for xx0,yy0 in xy:
      d.point((xx0,yy0),fill=(35,230,230))
    d.ellipse((x-6,y-6,x+6,y+6),outline=(255,40,215),width=1)
  d.rectangle((0,1194,720,1280),fill=(10,12,15))
  d.text((12,1210),f"{len(points)} PO-APPROVED CENTERS | MACHINE CORE MASK CANDIDATES",font=font,fill=(240,239,230))
  d.text((12,1240),"CYAN=actual image pixel core proposal. No synthesized flames.",font=font,fill=(255,215,151))
  return image

def run(shot,out):
 out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=True)
 draft=json.loads(DRAFT.read_text())
 assert draft["status"]=="CHAT_DIRECT_VISUAL_SOURCE_INSPECTION_PENDING_PO_APPROVAL" or draft["status"]=="PO_APPROVED_CENTER_LOCATIONS_ONLY"
 approved=draft["shots"][shot]["flames"]
 source_profile=eng.read_profile(draft["shots"][shot]["source_profile"])
 src,_=eng.load_inputs(source_profile)
 assert source_profile["source"]["type"]=="still_png"
 with Image.open(src) as f:rgb=np.asarray(f.convert("RGB").resize((720,1280),Image.Resampling.LANCZOS)).copy()
 masks={}
 manifest={"schema":"M01_V015_APPROVED_CENTER_REAL_PIXEL_MASK_MANIFEST",
   "status":"APPROVED_CENTERS_MACHINE_MASKS_PO_VIDEO_REVIEW_PENDING",
   "source_sha256":source_profile["source"]["sha256"],
   "source_path":source_profile["source"]["path"],
   "centers_approval_source":"PO approved V014 corrected visual diagrams in chat",
   "centers_draft_sha256":eng.sha(DRAFT),"coordinate_space":"720x1280",
   "flame_count":len(approved),"flames":{},
   "full_person_gt_approved":False,"flame_core_shapes_PO_approved":False,"release_allowed":False}
 pack=out/f"{shot}_PO_CENTERS_REAL_PIXEL_CORE_CANDIDATES_V015.zip"
 with zipfile.ZipFile(pack,"w",compression=zipfile.ZIP_DEFLATED) as z:
  for p in approved:
   fid=p["id"];x,y=p["center"]
   mask,metrics=local_mask(rgb,x,y,shot,fid)
   masks[fid]=mask
   filename=f"masks/{fid}.bitpack"
   z.writestr(filename,np.packbits(mask,axis=None,bitorder="little").tobytes())
   manifest["flames"][fid]={"approved_center":[x,y],"mask_filename":filename,**metrics}
 assert len(masks)==len(approved)
 manifest_name=out/f"{shot}_STATIC_CORE_MASK_MANIFEST_V015.json"
 manifest_name.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
 profile=copy.deepcopy(source_profile)
 profile.pop("_atlas_path");profile.pop("_atlas_sha256")
 profile["profile_id"]=f"{shot}_UNIFIED_CANDLE_PO_REVIEW_V015"
 profile["unified_flame_engine"]["registration_status"]="PO_CENTERS_APPROVED_STATIC_CORE_MASK_QC_PASS_VIDEO_PO_REVIEW_PENDING"
 profile["unified_flame_engine"]["flame_core_source"]="V014_PO_APPROVED_VISUAL_CENTERS_RESTRICTED_SOURCE_PIXEL_CONNECTED_MASKS"
 profile["unified_flame_engine"]["po_core_registration_approved"]=True
 profile["unified_flame_engine"]["human_gt_approved"]=False
 profile["unified_flame_engine"]["flame_shape_ground_truth_approved"]=False
 profile["unified_flame_engine"]["same_common_engine_module"]=True
 profile["static_core_masks"]={"zip_path":f"production/environment_dynamic/m01_engine_v1/masks_v015/{shot}/{pack.name}",
   "zip_sha256":eng.sha(pack),"manifest_path":f"production/environment_dynamic/m01_engine_v1/masks_v015/{shot}/{manifest_name.name}",
   "manifest_sha256":eng.sha(manifest_name),"flame_ids":[p["id"] for p in approved]}
 for f in profile["fixtures"]:
  f["flame_core_registration"]="V012_STYLE_REFLECTOR_ONLY"
 profile["fixtures"].extend(
  {"id":p["fixture"],"individual_source_id":p["id"],
   "center_px":p["center"],
   "region":{"kind":"gaussian","sigma_px":[7.0,11.0],
     "roi_px":[max(0,p["center"][0]-11),max(0,p["center"][1]-18),
               min(720,p["center"][0]+12),min(1280,p["center"][1]+19)],
     "weight":1,"tapers":[]},
   "phase":round(0.7+i*.317,4),
   "core_static_flame_id":p["id"],
   "core_gain_rgb":[14,10,4],
   "halo_gain_rgb":[0.9,0.55,0.15],
   "flame_core_registration":"APPROVED_CENTER_MASK_CANDIDATE_PO_REVIEW",
   "same_signal_drives_core_and_halo":True}
  for i,p in enumerate(approved))
 profile["review_status"]="PILOT_REFERENCE_ONLY"
 profile["registration_status"]="PO_APPROVED_CENTERS_CORE_SHAPES_MACHINE_PROPOSALS_PO_VIDEO_PENDING"
 profile["render_full_flame_output_authorized"]=False
 profile["release_allowed"]=False
 profile["flame_core_visual_mask_report"]="M01_V015_FLAME_CORE_MASK_REVIEW_ONLY"
 dst=out/f"{shot}_UNIFIED_CANDLE_PO_REVIEW_V015.json"
 dst.write_text(json.dumps(profile,ensure_ascii=False,indent=2)+"\n")
 qc={"shot":shot,"flame_count":len(approved),"source_exact":eng.sha(src)==source_profile["source"]["sha256"],
     "mask_pack_sha256":eng.sha(pack),"manifest_sha256":eng.sha(manifest_name),
     "PO_approved_center_count":len(approved),"machine_core_shape_PO_approved":False,
     "people_mask_GT_approved":False,"release_allowed":False}
 reviewed=viz(rgb,approved,masks)
 pic=out/f"{shot}_V015_REAL_SOURCE_CORE_MASK_QA.jpg"
 reviewed.save(pic,quality=92,subsampling=0,optimize=True)
 qc["source_core_mask_overlay_sha256"]=eng.sha(pic)
 (out/f"{shot}_MASK_BUILD_QC_V015.json").write_text(json.dumps(qc,indent=2)+"\n")
 print("M01_V015_REAL_SOURCE_MASKS_BUILT",qc,flush=True)
if __name__=="__main__":
 a=argparse.ArgumentParser()
 a.add_argument("--shot",required=True,choices=["N23","NEW02"])
 a.add_argument("--out",required=True)
 x=a.parse_args();run(x.shot,x.out)
