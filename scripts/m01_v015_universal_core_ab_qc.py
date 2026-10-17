#!/usr/bin/env python3
"""M01 V015 evidence-based core/halo A-B comparison and fail-closed QC."""
import hashlib,importlib.util,json,pathlib,subprocess
import numpy as np
from PIL import Image
ROOT=pathlib.Path(__file__).resolve().parents[1]
S=importlib.util.spec_from_file_location("m01",ROOT/"scripts/m01_engine_v1.py")
m=importlib.util.module_from_spec(S);S.loader.exec_module(m)
REF={
"N23":("0c9bf4cf8a901ac0cf7b306faf8cfd6e0cf650beb1cbc025cd3847e2f047fc0e","M01_N23_N17_NATURAL_V012_REVIEW_V001.mp4"),
"NEW02":("3899aaa97266af2a6133ee7210e97340aaf70921dbfe7c38dafdcf7eda54de02","M01_NEW02_N17_NATURAL_V012_REVIEW_V001.mp4")}
def create_ref_ab(oldpath,newpath,out):
    filter_graph=("[0:v]drawtext=text='V012 PO ACCEPTABLE':fontcolor=white:fontsize=23:x=16:y=16,"
        "pad=iw:ih+55:0:55:black[a];"
        "[1:v]drawtext=text='V015 CORE + HALO':fontcolor=white:fontsize=23:x=16:y=16,"
        "pad=iw:ih+55:0:55:black[b];[a][b]hstack=inputs=2[v]")
    subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-xerror","-y",
        "-i",str(oldpath),"-i",str(newpath),"-filter_complex",filter_graph,
        "-map","[v]","-c:v","libx264","-preset","veryfast","-crf","21",
        "-pix_fmt","yuv420p","-r","30","-frames:v","90",
        "-movflags","+faststart",str(out)],check=True)
def run(out):
 out=pathlib.Path(out)
 results=[]
 for shot,(refsha,oldvideo) in REF.items():
  accepted=ROOT/"production/environment_dynamic/review_candidates/M01_V12_NATURAL_AB"/shot/oldvideo
  assert m.sha(accepted)==refsha,("CHANGED_PO_APPROVED_V012",shot)
  p=m.read_profile(f"{shot}_UNIFIED_CANDLE_PO_REVIEW_V015.json")
  prior=m.read_profile(f"{shot}_N17_NATURAL_V012.json")
  source,unused=m.load_inputs(p)
  assert m.sha(source)==p["source"]["sha256"]==prior["source"]["sha256"]
  masks=m.load_static_flame_masks(p)
  assert len(masks)=={"N23":5,"NEW02":11}[shot]
  with Image.open(source) as im:
   rgb=np.asarray(im.convert("RGB").resize((720,1280),Image.Resampling.LANCZOS)).copy()
  permitted=np.zeros((1280,720),bool)
  for fixture in p["fixtures"]:
   if "core_static_flame_id" not in fixture:continue
   x0,y0,x1,y1=fixture["region"]["roi_px"]
   permitted[y0:y1,x0:x1]=True
   assert masks[fixture["core_static_flame_id"]].any()
  core_union=np.logical_or.reduce(list(masks.values()))
  core_changed_frames=0;delta_max=0;core_changed_pixels=0
  for frame in (7,13,21,29,37,46,55,63,72,82):
   before,_=m.calculate_frame(rgb,prior,frame,frame)
   after,_=m.calculate_frame(rgb,p,frame,frame,flame_by_index=masks)
   changed=np.any(before!=after,axis=2)
   assert not np.any(changed & ~permitted),("V012_VISUAL_CHANGE_OUTSIDE_REAL_CORE_REGION",shot,frame)
   n=int(np.sum(changed & core_union))
   core_changed_pixels+=n
   core_changed_frames+=int(n>0)
   delta_max=max(delta_max,int(np.abs(after.astype(np.int16)-before.astype(np.int16)).max()))
  assert core_changed_frames>=3,(shot,core_changed_frames)
  assert 0<delta_max<=20,(shot,delta_max)
  shotdir=out/shot
  qc=json.loads((shotdir/"M01_ENGINE_V1_PILOT_QC.json").read_text())
  assert qc["status"]=="COMMON_ENGINE_TECHNICAL_PILOT_PO_REVIEW_PENDING"
  assert qc["changed_protected_pixels"]==0 and qc["changed_pixels_outside_authorized"]==0
  assert not qc["person_protection_ground_truth_approved"] and not qc["release_allowed"]
  assert qc["frame_count"]==90 and qc["fps"]==30
  new=shotdir/qc["video_file"]
  side=shotdir/f"M01_{shot}_V012_BASELINE_VS_UNIFIED_FLAME_V015_AB_V001.mp4"
  create_ref_ab(accepted,new,side)
  for file in [side,new,shotdir/qc["comparison_file"]]:
   assert file.is_file()
   subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-xerror","-i",str(file),
      "-map","0:v:0","-f","null","-"],check=True)
  results.append({
   "shot":shot,"approved_flame_centers":len(masks),
   "candidate_core_pixel_count":int(sum(x.sum() for x in masks.values())),
   "sampled_frames_with_changed_core":core_changed_frames,
   "sampled_core_pixel_changes":core_changed_pixels,
   "max_raw_rgb_delta_added_over_accepted_V012":delta_max,
   "accepted_V012_unchanged_sha256":refsha,
   "candidate_video":qc["video_file"],"candidate_video_sha256":qc["video_sha256"],
   "original_vs_candidate_ab":qc["comparison_file"],"original_vs_candidate_ab_sha256":qc["comparison_sha256"],
   "v012_vs_candidate_ab":side.name,"v012_vs_candidate_ab_sha256":m.sha(side),
   "mask_manifest_path":p["static_core_masks"]["manifest_path"],
   "mask_manifest_sha256":p["static_core_masks"]["manifest_sha256"],
   "atlas_sha256":p["_atlas_sha256"]})
 summary={
 "schema":"M01_V015_UNIVERSAL_CANDLE_AB_TECHNICAL_QC",
 "status":"SAME_ENGINE_TWO_APPROVED_CENTER_CANDIDATE_AB_TECHNICAL_PASS_PO_VISUAL_PENDING",
 "engine":"scripts/m01_engine_v1.py",
 "source_centers_approved_only":True,"machine_flame_core_shapes_PO_approved":False,
 "style_reference":"M01_STYLE_BASELINE_V012",
 "person_ground_truth_approved":False,"render_to_canonical_authorized":False,
 "main_merge_authorized":False,"cross_scene_reuse_approved":False,"review_output":results}
 (out/"M01_V015_TWO_AB_REVIEW_QC.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
 print("M01_V015_UNIVERSAL_CORE_PLUS_HALO_QC_PASS",json.dumps(results,ensure_ascii=False),flush=True)
if __name__=="__main__":
 import argparse
 a=argparse.ArgumentParser();a.add_argument("--root",required=True)
 x=a.parse_args();run(x.root)
