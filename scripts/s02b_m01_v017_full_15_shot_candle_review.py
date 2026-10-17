#!/usr/bin/env python3
"""Non-canonical full 64s S02-B integration with single registered M01 engine.

Uses exactly the previously PO-accepted M01 calibrated candle centers where
available, refuses old V007 rejected masks for all other timeline nodes.
Delivers full-duration preview plus A/B with original AAC packet stream copy.
NO claim of all-candle coverage or canonical publication.
"""
import contextlib,hashlib,json,pathlib,subprocess,sys,zipfile
from collections import deque
import numpy as np
from PIL import Image
import importlib.util
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("m01_engine_v1",ROOT/"scripts/m01_engine_v1.py")
m01=importlib.util.module_from_spec(spec);spec.loader.exec_module(m01)
W,H,FPS,TOTAL=720,1280,30,1927
SOURCE=ROOT/"production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
SOURCE_SHA="7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402"
EDL=ROOT/"production/editorial_specs/S02_B_V006_CINEMATIC_ROUGH_EDL_V001.json"
ACTIVE={
"N17":"N17_APPROVED_VISUAL_RESULT_V001.json",
"V006_NEW_02":"NEW02_UNIFIED_CANDLE_PO_REVIEW_V015.json",
"N23":"N23_UNIFIED_CANDLE_PO_REVIEW_V015.json"
}
EXPECTED_VIDEO_SHAS={
"N23":"2b5dd22ea0e0a845107963c3a274f1e54d89d546ff01cd5fdcbfc210e9eff801",
"NEW02":"db55f740f0fa659c87978dd63cade34443e44365be989c791a27ba08b0e2168a"
}
EXPECTED_N17_APPROVED="46eb426b0f01ded40b749d892ec4b85b8f3715450a25fee748779e7185bcdd62"
DRAFT_ATLAS=ROOT/"production/environment_dynamic/m01_engine_v1/M01_S02B_V017_REAL_SOURCE_DRAFT_ATLAS.json"
OUT=ROOT/"_m01_s02b_v017_full_integration"
VIDEO=OUT/"S02_B_M01_V017_FULL_LENGTH_REGISTERED_CANDLE_PREVIEW_V001.mp4"
AB=OUT/"S02_B_M01_V017_FULL_LENGTH_V006_VS_M01_AB_V001.mp4"
REPORT=OUT/"S02_B_M01_V017_INTEGRATION_QC.json"
TEMP=OUT/"S02_B_M01_V017_SILENT_INTERMEDIATE.mp4"
TEMP_AB=OUT/"S02_B_M01_V017_AB_VIDEO_ONLY_INTERMEDIATE.mp4"

def probe(path):
 return json.loads(subprocess.check_output(["ffprobe","-v","error",
  "-show_entries","stream=codec_type,codec_name,nb_frames,width,height,r_frame_rate:format=duration",
  "-of","json",str(path)],text=True))
def audio_packets(path):
 j=json.loads(subprocess.check_output(["ffprobe","-v","error","-select_streams","a:0",
  "-show_packets","-show_entries","packet=pts_time,duration_time,data_hash","-show_data_hash","sha256",
  "-of","json",str(path)],text=True))
 return [(r.get("pts_time"),r.get("duration_time"),r.get("data_hash")) for r in j["packets"]]
def exact_read(stream,n):
 parts=[]
 while n:
  chunk=stream.read(n)
  if not chunk:raise RuntimeError("SHORT_DECODED_SOURCE_VIDEO")
  parts.append(chunk);n-=len(chunk)
 return b"".join(parts)

def build_profile(shot,segment,atlas):
 styles=atlas["style"]
 frames=segment["end_frame_exclusive"]-segment["start_frame"]
 fixtures=[]
 for i,flame in enumerate(atlas["sources"][shot]["centers"]):
  cx,cy=flame["point_px"]
  assert 0<=cx<W and 0<=cy<550,("SOURCE_CORE_OUTSIDE_ARCHITECTURE_LIGHT_REGION",shot,cx,cy)
  rx,ry=styles["halo_roi_radii_px"]
  fixtures.append({"id":flame["id"],"individual_source_id":flame["id"],
   "center_px":[cx,cy],"phase":round(.73+i*.347,4),"core_bitpack_index":i+1,
   "core_gain_rgb":styles["core_gain_rgb"],"halo_gain_rgb":styles["halo_gain_per_flame_rgb"],
   "region":{"kind":"gaussian","sigma_px":styles["halo_sigma_px"],
     "roi_px":[max(0,cx-rx),max(0,cy-ry),min(W,cx+rx+1),min(H,cy+ry+1)],
     "weight":1,"tapers":[]}})
 p={"schema":"M01_SCENE_LIGHT_ATLAS_V1","profile_id":shot+"_SOURCE_V017","scene_id":shot,
 "review_status":"PILOT_REFERENCE_ONLY","registration_status":"UNSEEN_ACTUAL_SOURCE_VISUAL_DRAFT_PO_VIDEO_PENDING",
 "source":{"type":"video_mp4","path":str(SOURCE.relative_to(ROOT)),"sha256":SOURCE_SHA,"input_dimensions":[W,H]},
 "render":{"width":W,"height":H,"fps":FPS,"frames":frames,"frame_start":segment["start_frame"],"preserve_audio":False},
 "temporal":{"style":styles["temporal_signal"],"rgb_cap":styles["halo_gain_per_flame_rgb"],
   "envelope":"sin_soft_edges","halo_fast_harmonics_mix":styles["halo_fast_harmonics_mix"]},
 "protection":{"mode":"roi_only_unverified","do_not_claim_complete_person_protection":True},
 "fixtures":fixtures,"release_allowed":False}
 m01.validate(p)
 return p

def find_real_source_core(rgb,center,style):
 cx,cy=map(int,center)
 rx,ry=style["core_search_radii_px"]
 sx,sy=style["core_mask_ellipse_px"]
 x0=max(0,cx-rx-2);x1=min(W,cx+rx+3)
 y0=max(0,cy-ry-2);y1=min(H,cy+ry+3)
 tile=rgb[y0:y1,x0:x1].astype(np.int16)
 yy,xx=np.ogrid[y0:y1,x0:x1]
 R,G,B=tile[:,:,0],tile[:,:,1],tile[:,:,2]
 bright=(R>=196)&(G>=127)&(R>=G+3)&(G>=B+6)
 allowed=bright&((((xx-cx)/rx)**2+((yy-cy)/ry)**2)<=1)
 nearest=((xx-cx)**2+(yy-cy)**2)<=max(5,rx-2)**2
 pts=np.argwhere(allowed&nearest)
 if not len(pts):return None,0
 py,px=map(int,min(pts,key=lambda t:(int(t[1])+x0-cx)**2+(int(t[0])+y0-cy)**2))
 xx0,yy0=px+x0,py+y0
 ell=(((xx-xx0)/sx)**2+((yy-yy0)/sy)**2)<=1
 valid=bright&ell
 if not valid[py,px]:return None,0
 conn=np.zeros(valid.shape,bool);conn[py,px]=True
 q=deque([(py,px)])
 while q:
  vy,vx=q.popleft()
  for y in range(max(0,vy-1),min(valid.shape[0],vy+2)):
   for x in range(max(0,vx-1),min(valid.shape[1],vx+2)):
    if valid[y,x] and not conn[y,x]:
     conn[y,x]=True;q.append((y,x))
 n=int(conn.sum())
 if not 4<=n<=220:return None,0
 mask=np.zeros((H,W),bool);mask[y0:y1,x0:x1]=conn
 return mask,n

def main():
 OUT.mkdir(exist_ok=True)
 if m01.sha(SOURCE)!=SOURCE_SHA:raise ValueError("ORIGINAL_BASE_SHA_MISMATCH")
 timeline=json.loads(EDL.read_text())["timeline"]
 assert len(timeline)==17 and timeline[0]["start_frame"]==0 and timeline[-1]["end_frame_exclusive"]==TOTAL
 assert all(a["end_frame_exclusive"]==b["start_frame"] for a,b in zip(timeline,timeline[1:]))
 assert len(set(x["id"] for x in timeline))==17
 assert set(ACTIVE).issubset(set(x["id"] for x in timeline))
 atlas=json.loads(DRAFT_ATLAS.read_text())
 assert atlas["schema"]=="M01_S02B_V017_VISUAL_CANDLE_CANDIDATE_ATLAS"
 assert atlas["original_source"]["sha256"]==SOURCE_SHA
 assert not atlas["invariants"]["old_v007_wrong_source_masks_reused"]
 assert not (set(ACTIVE)&set(atlas["sources"]))
 assert len(atlas["sources"])==12 and len(atlas["deliberate_no_supported_flame"])==2
 assert set(ACTIVE)|set(atlas["sources"])|set(atlas["deliberate_no_supported_flame"])=={x["id"] for x in timeline}
 infos={}
 for shot,config in ACTIVE.items():
  p=m01.read_profile(config)
  # Input provenance for the main 377-frame N17 must equal this exact source.
  if shot=="N17":
   assert p["source"]["sha256"]==SOURCE_SHA and p["source"]["type"]=="video_mp4"
   assert p["render"]["frame_start"]==281 and p["render"]["frames"]==377
   mask=m01.load_inputs(p)[1]
   static={}
  else:
   assert p["source"]["type"]=="still_png" and p["render"]["frames"]==90
   mask=None
   static=m01.load_static_flame_masks(p)
   expected={"N23":5,"V006_NEW_02":11}[shot]
   assert len(static)==expected
   sshot="NEW02" if shot=="V006_NEW_02" else shot
   if m01.sha(ROOT/"production/environment_dynamic/review_candidates/M01_V015_UNIVERSAL_CANDLE_AB"/sshot/f"M01_{sshot}_UNIFIED_CANDLE_PO_REVIEW_V015_REVIEW_V001.mp4")!=EXPECTED_VIDEO_SHAS[sshot]:
    raise ValueError("PO_APPROVED_2SHOT_REFERENCE_BINARY_CHANGED")
  infos[shot]={"profile":p,"mask":mask,"static":static}
 assert m01.sha(ROOT/"production/environment_dynamic/review_candidates/M01_N17_CANDLE_MOTION_RESULT_V001/M01_N17_CANDLE_ENGINE_RESULT_REVIEW_V001.mp4")==EXPECTED_N17_APPROVED
 for seg in timeline:
  if seg["id"] in atlas["sources"]:
   profile=build_profile(seg["id"],seg,atlas)
   infos[seg["id"]]={"profile":profile,"mask":None,"static":{}}
 inp=probe(SOURCE)
 ins=next(s for s in inp["streams"] if s["codec_type"]=="video")
 assert (ins["width"],ins["height"],ins["r_frame_rate"],int(ins["nb_frames"]))==(W,H,"30/1",TOTAL)
 source_audio=audio_packets(SOURCE)
 assert len(source_audio)==3013
 dec=subprocess.Popen(["ffmpeg","-hide_banner","-v","error","-xerror","-i",str(SOURCE),
   "-map","0:v:0","-vsync","0","-f","rawvideo","-pix_fmt","rgb24","pipe:1"],stdout=subprocess.PIPE)
 encoder=subprocess.Popen(["ffmpeg","-hide_banner","-v","error","-xerror","-y",
   "-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-framerate",str(FPS),
   "-i","pipe:0","-an","-c:v","libx264","-preset","ultrafast","-crf","18",
   "-pix_fmt","yuv420p","-r",str(FPS),"-movflags","+faststart",str(TEMP)],stdin=subprocess.PIPE)
 spanstats={}
 for x in timeline:
  enabled=x["id"] in infos
  spanstats[x["id"]]={"start_frame":x["start_frame"],"end_frame_exclusive":x["end_frame_exclusive"],
   "total_frames":x["end_frame_exclusive"]-x["start_frame"],"lighting_added":enabled,
   "status":"PO_APPROVED_THREE_SHOT_REVIEW" if x["id"] in ACTIVE else ("V017_SOURCE_FRAME_LOCATOR_PO_REVIEW_PENDING" if enabled else "PASS_THROUGH_NO_VISIBLE_CANDLE"),
   "reason":None if enabled else "Original footage has no registered visible candle; no synthesized light",
   "frames_with_raw_change":0,"max_raw_rgb_delta":0,
   "raw_unauthorized_changes":0,"registered_source_count":len(infos[x["id"]]["profile"]["fixtures"]) if enabled else 0,
   "real_source_core_frames":0,"real_source_core_pixels":0,
   "raw_first_frame_original":None,"raw_last_frame_original":None}
 frameidx=0
 try:
  with zipfile.ZipFile(infos["N17"]["mask"]["path"],"r") as z:
   for seg in timeline:
    id=seg["id"];registered=id in infos;stat=spanstats[id]
    length=stat["total_frames"]
    for i in range(length):
     raw=exact_read(dec.stdout,W*H*3)
     if registered:
      info=infos[id];p=info["profile"]
      original=np.frombuffer(raw,dtype=np.uint8).reshape(H,W,3).copy()
      if id=="N17":
       expected_frame=info["mask"]["frames"][frameidx]
       if hashlib.sha256(raw).hexdigest()!=expected_frame["decoded_source_rgb_sha256"]:
        raise ValueError("N17_VIDEO_FRAME_SHA_DRIFT")
       person,unsure,flames=m01.per_frame_masks(info["mask"],z,frameidx)
       absolute=frameidx;relative=i
      else:
       person=np.zeros((H,W),bool)
       unsure=np.zeros((H,W),bool)
       absolute=i;relative=i
       if id in atlas["sources"]:
        flames={};selected=[]
        for fi,fixture in enumerate(p["fixtures"],1):
         mask,count=find_real_source_core(original,fixture["center_px"],atlas["style"])
         if mask is None:continue
         flames[fi]=mask;selected.append(fixture)
         stat["real_source_core_pixels"]+=count
        stat["real_source_core_frames"]+=int(bool(flames))
        curr={**p,"fixtures":selected}
        absolute=frameidx
       else:
        flames=info["static"]
        curr=p
        relative=round(i*(p["render"]["frames"]-1)/(length-1))
      if id=="N17":curr=p
      new,stats=m01.calculate_frame(original,curr,absolute,relative,person,unsure,flames)
      if stats["protected_changed"] or stats["outside_authorized"]:
       raise ValueError("RAW_REGION_VIOLATION")
      if stats["max_delta"]>40:raise ValueError("OUT_OF_STYLE_FLASH_CAP")
      stat["frames_with_raw_change"]+=int(stats["changed"]>0)
      stat["max_raw_rgb_delta"]=max(stat["max_raw_rgb_delta"],stats["max_delta"])
      encoded=new.tobytes()
      if i==0:stat["raw_first_frame_original"]=not stats["changed"]
      if i==length-1:stat["raw_last_frame_original"]=not stats["changed"]
     else:
      encoded=raw
      if i==0:stat["raw_first_frame_original"]=True
      if i==length-1:stat["raw_last_frame_original"]=True
     encoder.stdin.write(encoded)
     frameidx+=1
     if frameidx%300==0:print("M01_FULL_LENGTH_FRAME_PROGRESS",frameidx,flush=True)
   if dec.stdout.read(1):raise ValueError("EXTRA_SOURCE_FRAMES")
 finally:
  encoder.stdin.close();dec.stdout.close()
 assert dec.wait()==0 and encoder.wait()==0
 assert frameidx==TOTAL
 assert all(s["raw_first_frame_original"] and s["raw_last_frame_original"] for s in spanstats.values()),"EDIT_CUT_BOUNDARY_DRIFT"
 assert all(spanstats[s]["frames_with_raw_change"]>0 for s in ACTIVE),"APPROVED_CORE_SEGMENT_NOT_RENDERED"
 for shot in atlas["sources"]:
  ss=spanstats[shot]
  if ss["real_source_core_frames"]<max(3,int(ss["total_frames"]*.2)):
   raise RuntimeError(f"V017_FLAME_REGISTRATION_FAILED_CLOSED:{shot}:{ss['real_source_core_frames']}")
  if ss["frames_with_raw_change"]<3:raise RuntimeError(f"V017_NO_EFFECT:{shot}")
 subprocess.run(["ffmpeg","-hide_banner","-v","error","-xerror","-y",
  "-i",str(TEMP),"-i",str(SOURCE),"-map","0:v:0","-map","1:a:0",
  "-c:v","copy","-c:a","copy","-copyts","-start_at_zero",
  "-movflags","+faststart",str(VIDEO)],check=True)
 result=probe(VIDEO)
 v=next(s for s in result["streams"] if s["codec_type"]=="video")
 assert (v["width"],v["height"],v["r_frame_rate"],int(v["nb_frames"]))==(W,H,"30/1",TOTAL)
 assert audio_packets(VIDEO)==source_audio,"APPROVED_AUDIO_PACKET_IDENTITY_CHANGED"
 filter_graph=("[0:v]pad=iw:ih+72:0:72:black,"
 "drawtext=text='A V006 SOURCE':fontsize=29:fontcolor=white:x=24:y=18[a];"
 "[1:v]pad=iw:ih+72:0:72:black,"
 "drawtext=text='B M01 V017 REVIEW':fontsize=29:fontcolor=white:x=24:y=18[b];"
 "[a][b]hstack=inputs=2[v]")
 # First encode only the hstack video. Then reuse source audio through the
 # SAME video-only + untouched source AAC remux strategy as the preview.
 # Muxing AAC alongside a filtered hstack previously changed packet timestamps.
 subprocess.run(["ffmpeg","-hide_banner","-v","error","-xerror","-y",
  "-i",str(SOURCE),"-i",str(VIDEO),"-filter_complex",filter_graph,
  "-map","[v]","-an","-c:v","libx264","-preset","veryfast",
  "-crf","22","-pix_fmt","yuv420p","-r","30","-frames:v",str(TOTAL),
  "-movflags","+faststart",str(TEMP_AB)],check=True)
 subprocess.run(["ffmpeg","-hide_banner","-v","error","-xerror","-y",
  "-i",str(TEMP_AB),"-i",str(SOURCE),"-map","0:v:0","-map","1:a:0",
  "-c:v","copy","-c:a","copy","-copyts","-start_at_zero",
  "-movflags","+faststart",str(AB)],check=True)
 abprobe=probe(AB)
 av=next(s for s in abprobe["streams"] if s["codec_type"]=="video")
 assert (int(av["nb_frames"]),av["width"],av["height"],av["r_frame_rate"])==(TOTAL,1440,1352,"30/1")
 assert audio_packets(AB)==source_audio,"AB_ORIGINAL_AUDIO_PACKET_IDENTITY_CHANGED"
 for path in (VIDEO,AB):
  for st in ("v:0","a:0"):
   subprocess.run(["ffmpeg","-hide_banner","-v","error","-xerror","-i",str(path),"-map","0:"+st,"-f","null","-"],check=True)
 assert m01.sha(SOURCE)==SOURCE_SHA
 TEMP.unlink(missing_ok=True)
 TEMP_AB.unlink(missing_ok=True)
 enabled_frame_count=sum(s["total_frames"] for s in spanstats.values() if s["lighting_added"])
 rep={"schema":"S02_B_M01_V017_ALL_CANDLE_LIT_FULL_LENGTH_INTEGRATION",
   "status":"S02B_15_CANDLE_LIT_NODES_RENDERED_FROM_REAL_SOURCE_CANDIDATES_PO_VIDEO_REVIEW_PENDING",
   "source_exact_sha256":SOURCE_SHA,
   "source_limit":"V006 reconstructed rough candidate not original unavailable V005",
   "renderer":"scripts/s02b_m01_v017_full_length_safe_integration.py",
   "common_engine":"scripts/m01_engine_v1.py",
   "total_timeline_nodes":len(timeline),"total_frames":TOTAL,"fps":FPS,"duration_seconds":TOTAL/FPS,
   "registered_nodes":list(ACTIVE),"registered_node_count":len(ACTIVE),
   "candidate_nodes":sorted(atlas["sources"]),"candidate_node_count":len(atlas["sources"]),
   "pass_through_non_candle_nodes":atlas["deliberate_no_supported_flame"],"pass_through_non_candle_count":2,
   "reviewed_enabled_frames":enabled_frame_count,
   "applied_lit_footage_percent":round(100*enabled_frame_count/TOTAL,2),
   "all_15_candle_shots_rendered_by_same_m01_core":True,
   "flame_candidate_atlas_sha256":m01.sha(DRAFT_ATLAS),
   "candidate_flame_positions_po_approved":False,
   "old_v007_po_rejected_guessed_masks_reused":False,
   "N17_approved_reference_binary_preserved":True,
   "N23_NEW02_po_approved_v015_reference_binaries_preserved":True,
   "per_shot":spanstats,
   "preview":{"file":VIDEO.name,"sha256":m01.sha(VIDEO),"bytes":VIDEO.stat().st_size},
   "ab":{"file":AB.name,"sha256":m01.sha(AB),"bytes":AB.stat().st_size},
   "audio_identical_source_AAC_packet_hash_and_timestamps":True,
   "input_video_unchanged":True,"official_video_index_unchanged":True,
   "original_story_shot_images_unchanged":True,
   "all_17_shots_have_real_flame_effects":False,
   "all_15_identified_candle_lit_shots_have_candidate_effects":True,
   "full_s02b_m01_coverage_approved":False,"person_full_gt_approved":False,
   "PO_final_full_video_approval":False,"no_canonical_publication":True,"no_main_merge":True}
 REPORT.write_text(json.dumps(rep,ensure_ascii=False,indent=2)+"\n")
 print("S02B_M01_V017_FULL_CANDLE_SOURCE_CANDIDATE_REVIEW_READY",json.dumps({k:v for k,v in rep.items() if k!="per_shot"},ensure_ascii=False),flush=True)
if __name__=="__main__":main()
