#!/usr/bin/env python3
"""Non-canonical full 64s S02-B integration with single registered M01 engine.

Uses exactly the previously PO-accepted M01 calibrated candle centers where
available, refuses old V007 rejected masks for all other timeline nodes.
Delivers full-duration preview plus A/B with original AAC packet stream copy.
NO claim of all-candle coverage or canonical publication.
"""
import contextlib,hashlib,json,pathlib,subprocess,sys,zipfile
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
OUT=ROOT/"_m01_s02b_v016_full_integration"
VIDEO=OUT/"S02_B_M01_V016_FULL_LENGTH_REGISTERED_CANDLE_PREVIEW_V001.mp4"
AB=OUT/"S02_B_M01_V016_FULL_LENGTH_V006_VS_M01_AB_V001.mp4"
REPORT=OUT/"S02_B_M01_V016_INTEGRATION_QC.json"
TEMP=OUT/"S02_B_M01_V016_SILENT_INTERMEDIATE.mp4"
TEMP_AB=OUT/"S02_B_M01_V016_AB_VIDEO_ONLY_INTERMEDIATE.mp4"

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

def main():
 OUT.mkdir(exist_ok=True)
 if m01.sha(SOURCE)!=SOURCE_SHA:raise ValueError("ORIGINAL_BASE_SHA_MISMATCH")
 timeline=json.loads(EDL.read_text())["timeline"]
 assert len(timeline)==17 and timeline[0]["start_frame"]==0 and timeline[-1]["end_frame_exclusive"]==TOTAL
 assert all(a["end_frame_exclusive"]==b["start_frame"] for a,b in zip(timeline,timeline[1:]))
 assert len(set(x["id"] for x in timeline))==17
 assert set(ACTIVE).issubset(set(x["id"] for x in timeline))
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
  enabled=x["id"] in ACTIVE
  spanstats[x["id"]]={"start_frame":x["start_frame"],"end_frame_exclusive":x["end_frame_exclusive"],
   "total_frames":x["end_frame_exclusive"]-x["start_frame"],"lighting_added":enabled,
   "status":"REGISTERED_SINGLE_ENGINE_VISUAL_REVIEW_PENDING" if enabled else "ORIGINAL_SOURCE_RAW_FRAMES_UNALTERED__FLAME_REGISTRATION_NOT_APPROVED",
   "reason":None if enabled else "Rejected or unregistered V007 guessed light spots are NOT promoted into M01; no synthetic candle effect",
   "frames_with_raw_change":0,"max_raw_rgb_delta":0,
   "raw_unauthorized_changes":0,"registered_source_count":len(infos[x["id"]]["profile"]["fixtures"]) if enabled else 0,
   "raw_first_frame_original":None,"raw_last_frame_original":None}
 frameidx=0
 try:
  with zipfile.ZipFile(infos["N17"]["mask"]["path"],"r") as z:
   for seg in timeline:
    id=seg["id"];registered=id in ACTIVE;stat=spanstats[id]
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
       flames=info["static"]
       absolute=i
       # Map the full source shot span onto its calibrated 90-frame envelope.
       # Prevent a false light jump at editorial cuts even when shot duration differs.
       relative=round(i*(p["render"]["frames"]-1)/(length-1))
      new,stats=m01.calculate_frame(original,p,absolute,relative,person,unsure,flames)
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
 assert all(spanstats[s]["frames_with_raw_change"]>0 for s in ACTIVE),"REGISTERED_SEGMENT_NO_PERCEPTIBLE_CHANGE"
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
 "drawtext=text='B M01 V016 REVIEW':fontsize=29:fontcolor=white:x=24:y=18[b];"
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
 rep={"schema":"S02_B_M01_V016_PARTIAL_REGISTERED_FULL_LENGTH_INTEGRATION",
   "status":"FULL_LENGTH_VIDEO_RENDERED_THREE_REGISTERED_LIGHTING_NODES_FOURTEEN_PASS_THROUGH_PENDING_PO_AND_CALIBRATION",
   "source_exact_sha256":SOURCE_SHA,
   "source_limit":"V006 reconstructed rough candidate not original unavailable V005",
   "renderer":"scripts/s02b_m01_v016_full_length_safe_integration.py",
   "common_engine":"scripts/m01_engine_v1.py",
   "total_timeline_nodes":len(timeline),"total_frames":TOTAL,"fps":FPS,"duration_seconds":TOTAL/FPS,
   "registered_nodes":list(ACTIVE),"registered_node_count":len(ACTIVE),
   "pass_through_unverified_count":len(timeline)-len(ACTIVE),
   "reviewed_enabled_frames":enabled_frame_count,
   "registered_coverage_percent":round(100*enabled_frame_count/TOTAL,2),
   "all_registered_candles_rendered_by_same_m01_core":True,
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
   "full_s02b_m01_coverage_approved":False,"person_full_gt_approved":False,
   "PO_final_full_video_approval":False,"no_canonical_publication":True,"no_main_merge":True}
 REPORT.write_text(json.dumps(rep,ensure_ascii=False,indent=2)+"\n")
 print("S02B_M01_V016_FULL_LENGTH_SAFELY_INTEGRATED_REVIEW_READY",json.dumps({k:v for k,v in rep.items() if k!="per_shot"},ensure_ascii=False),flush=True)
if __name__=="__main__":main()
