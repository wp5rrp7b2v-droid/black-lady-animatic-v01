#!/usr/bin/env python3
"""M01 V018: lift only S02-B's twelve C-group candle sources in an unchanged common renderer.

Keeps original source, approved N17/N23/NEW02 profiles, actual source coordinates,
temporal signals, image footprint, original AAC and two intentional passthrough shots.
Produces a complete 64.23s effect plus source A/B and direct V017-vs-V018 A/B.
V018 is only a new Product Owner review candidate, not an approved visual master.
"""
import hashlib,importlib.util,json,pathlib,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("s02b_v017",ROOT/"scripts/s02b_m01_v017_full_15_shot_candle_review.py")
render=importlib.util.module_from_spec(spec)
spec.loader.exec_module(render)
PREV_ROOT=ROOT/"production/environment_dynamic/review_candidates/S02_B_M01_V017_FULL_LENGTH_ALL_CANDLE_SOURCES_REVIEW"
PREV_VIDEO=PREV_ROOT/"S02_B_M01_V017_FULL_LENGTH_REGISTERED_CANDLE_PREVIEW_V001.mp4"
PREV_QC=PREV_ROOT/"S02_B_M01_V017_INTEGRATION_QC.json"
PREV_VIDEO_SHA="2f12fd18000f8f515f62b7e1d79bd9456d897e69ce22a20398480039e6446327"
PREV_QC_GIT_BLOB_SHA="dba82d4dc540f0cfb179d2cdc913c30b8d64d899"
BASE_ATLAS=ROOT/"production/environment_dynamic/m01_engine_v1/M01_S02B_V017_REAL_SOURCE_DRAFT_ATLAS.json"
NEW_ATLAS=ROOT/"production/environment_dynamic/m01_engine_v1/M01_S02B_V018_MORE_VISIBLE_C_GROUP_DRAFT_ATLAS.json"
OUT=ROOT/"_m01_s02b_v018_c_more_visible"
EXTRA_AB=OUT/"S02_B_M01_V018_FULL_LENGTH_V017_VS_V018_AB_V001.mp4"
SILENT_AB=OUT/"S02_B_M01_V018_SIDE_BY_SIDE_SILENT_TEMP.mp4"
ALL_ACTIVE=frozenset(render.ACTIVE)
NO_CANDLE={"N16_PART_2","N19"}

def check_inputs():
 assert render.m01.sha(PREV_VIDEO)==PREV_VIDEO_SHA,"PREVIOUS_REVIEW_VIDEO_CHANGED"
 data=PREV_QC.read_bytes()
 blob_sha=hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()
 assert blob_sha==PREV_QC_GIT_BLOB_SHA,"PREVIOUS_REVIEW_QC_CHANGED"
 old=json.loads(BASE_ATLAS.read_text());new=json.loads(NEW_ATLAS.read_text())
 assert new["status"]=="M01_V018_C_GROUP_MORE_VISIBLE_PO_REVIEW_ONLY"
 assert new["sources"]==old["sources"],"CANDLE_LOCATIONS_CHANGED"
 assert new["carry_approved"]==old["carry_approved"],"APPROVED_SHOT_SET_CHANGED"
 assert new["deliberate_no_supported_flame"]==old["deliberate_no_supported_flame"],"PASS_THROUGH_SET_CHANGED"
 assert set(new["sources"]).isdisjoint(ALL_ACTIVE|NO_CANDLE)
 assert len(new["sources"])==12
 so, sn=old["style"],new["style"]
 expected=set(["name","core_gain_rgb","halo_gain_per_flame_rgb"])
 assert {k for k in so if so[k]!=sn[k]}==expected, "UNINTENDED_STYLE_CHANGE"
 assert so["core_gain_rgb"]==[14,10,4] and sn["core_gain_rgb"]==[21,15,6]
 assert so["halo_gain_per_flame_rgb"]==[1.6,0.85,0.22]
 assert sn["halo_gain_per_flame_rgb"]==[3.2,1.7,0.45]
 assert sn["halo_sigma_px"]==so["halo_sigma_px"]==[21,33]
 assert sn["halo_roi_radii_px"]==so["halo_roi_radii_px"]==[40,52]
 assert sn["halo_fast_harmonics_mix"]==so["halo_fast_harmonics_mix"]==0.22
 assert sn["core_search_radii_px"]==so["core_search_radii_px"]
 assert sn["core_mask_ellipse_px"]==so["core_mask_ellipse_px"]
 assert sn["temporal_signal"]==so["temporal_signal"]=="unsynced_independent"
 assert old["original_source"]==new["original_source"]
 assert new["invariants"]==old["invariants"]
 return old,new,json.loads(PREV_QC.read_text())

def make_side_by_side():
 filter_graph=("[0:v]pad=iw:ih+72:0:72:black,"
 "drawtext=text='A V017 C GROUP':fontsize=29:fontcolor=white:x=24:y=18[a];"
 "[1:v]pad=iw:ih+72:0:72:black,"
 "drawtext=text='B V018 MORE VISIBLE':fontsize=29:fontcolor=white:x=24:y=18[b];"
 "[a][b]hstack=inputs=2[v]")
 subprocess.run(["ffmpeg","-hide_banner","-v","error","-xerror","-y",
 "-i",str(PREV_VIDEO),"-i",str(render.VIDEO),"-filter_complex",filter_graph,
 "-map","[v]","-an","-c:v","libx264","-preset","veryfast","-crf","22",
 "-pix_fmt","yuv420p","-r","30","-frames:v",str(render.TOTAL),
 "-movflags","+faststart",str(SILENT_AB)],check=True)
 subprocess.run(["ffmpeg","-hide_banner","-v","error","-xerror","-y",
 "-i",str(SILENT_AB),"-i",str(render.SOURCE),"-map","0:v:0","-map","1:a:0",
 "-c:v","copy","-c:a","copy","-copyts","-start_at_zero",
 "-movflags","+faststart",str(EXTRA_AB)],check=True)
 out=render.probe(EXTRA_AB)
 v=next(s for s in out["streams"] if s["codec_type"]=="video")
 assert (int(v["nb_frames"]),v["width"],v["height"],v["r_frame_rate"])==(1927,1440,1352,"30/1")
 assert render.audio_packets(EXTRA_AB)==render.audio_packets(render.SOURCE),"V017_V018_AB_SOURCE_AAC_DIFFERENCE"
 subprocess.run(["ffmpeg","-hide_banner","-v","error","-xerror","-i",str(EXTRA_AB),
 "-map","0:v:0","-f","null","-"],check=True)
 SILENT_AB.unlink(missing_ok=True)

def main():
 original,new,oldqc=check_inputs()
 OUT.mkdir(exist_ok=True)
 render.OUT=OUT
 render.VIDEO=OUT/"S02_B_M01_V018_FULL_LENGTH_MORE_VISIBLE_C_GROUP_PREVIEW_V001.mp4"
 render.AB=OUT/"S02_B_M01_V018_FULL_LENGTH_V006_VS_V018_AB_V001.mp4"
 render.REPORT=OUT/"S02_B_M01_V018_INTEGRATION_QC.json"
 render.TEMP=OUT/"S02_B_M01_V018_SILENT_INTERMEDIATE.mp4"
 render.TEMP_AB=OUT/"S02_B_M01_V018_AB_VIDEO_ONLY_INTERMEDIATE.mp4"
 render.DRAFT_ATLAS=NEW_ATLAS
 # Uses exact same tested core calculate_frame() and V017 full-timeline
 # integration code; only the draft Atlas's two C-group amplitude vectors vary.
 render.main()
 make_side_by_side()
 j=json.loads(render.REPORT.read_text())
 oldshots=oldqc["per_shot"];shots=j["per_shot"]
 assert set(shots)==set(oldshots) and len(shots)==17
 assert j["source_exact_sha256"]==oldqc["source_exact_sha256"]
 assert j["total_frames"]==1927 and j["applied_lit_footage_percent"]==88.22
 for shot in ALL_ACTIVE|NO_CANDLE:
  for key in ("start_frame","end_frame_exclusive","total_frames",
              "frames_with_raw_change","max_raw_rgb_delta","registered_source_count"):
   assert shots[shot][key]==oldshots[shot][key],("APPROVED_OR_PASSTHROUGH_FRAME_DRIFT",shot,key)
  assert shots[shot]["raw_first_frame_original"] and shots[shot]["raw_last_frame_original"]
 boosted=[];weak=[]
 for shot in sorted(new["sources"]):
  a,b=oldshots[shot],shots[shot]
  assert b["registered_source_count"]==a["registered_source_count"]
  assert b["real_source_core_frames"]==a["real_source_core_frames"]
  assert b["real_source_core_pixels"]==a["real_source_core_pixels"]
  assert b["raw_first_frame_original"] and b["raw_last_frame_original"]
  assert b["max_raw_rgb_delta"]<=32,("C_GROUP_TOO_BRIGHT",shot,b["max_raw_rgb_delta"])
  assert b["max_raw_rgb_delta"]>=a["max_raw_rgb_delta"],("AMPLITUDE_WEAKER_THAN_V017",shot)
  boosted.append(b["max_raw_rgb_delta"]-a["max_raw_rgb_delta"])
  weak.append({"shot":shot,"V017_max_rgb":a["max_raw_rgb_delta"],"V018_max_rgb":b["max_raw_rgb_delta"],
     "increase":boosted[-1]})
 assert sum(v>0 for v in boosted)>=10,("NOT_PERCEPTIBLY_BOOSTED_ENOUGH_SHOTS",boosted)
 assert sum(boosted)/len(boosted)>=3,("C_GROUP_DELTA_INSUFFICIENT",boosted)
 assert j["audio_identical_source_AAC_packet_hash_and_timestamps"]
 assert not j["candidate_flame_positions_po_approved"]
 assert not j["full_s02b_m01_coverage_approved"]
 assert not j["PO_final_full_video_approval"] and j["no_main_merge"] and j["no_canonical_publication"]
 j["schema"]="S02_B_M01_V018_MORE_VISIBLE_C_GROUP_FULL_LENGTH_INTEGRATION"
 j["status"]="S02B_V018_ONLY_12_C_GROUP_INTENSITIES_BOOSTED_AB_RENDERED_TECHNICAL_PASS_PO_VISUAL_REVIEW_PENDING"
 j["renderer"]="scripts/s02b_m01_v018_c_strength_full_video.py (reuses unchanged S02B V017 integrator and M01 core)"
 j["style_parameter_change"]={
  "group":"C_ONLY_12_SHOTS",
  "V017_core_gain_rgb":[14,10,4],"V018_core_gain_rgb":[21,15,6],
  "V017_halo_gain_rgb":[1.6,0.85,0.22],"V018_halo_gain_rgb":[3.2,1.7,0.45],
  "halo_sigma_px_unchanged":[21,33],"halo_roi_radius_px_unchanged":[40,52],
  "halo_fast_harmonics_mix_unchanged":0.22,"same_unique_source_points":True,
  "time_signal_unchanged":True,"approved_three_shots_unchanged":True,
  "no_candle_two_shots_unchanged":True}
 j["V017_previous_review_video_sha256"]=PREV_VIDEO_SHA
 j["V017_previous_qc_git_blob_sha1"]=PREV_QC_GIT_BLOB_SHA
 j["C_group_actual_max_change_comparison"]=weak
 j["C_group_max_rgb_mean_increase"]=round(sum(boosted)/len(boosted),2)
 j["previous_v017_to_v018_ab"]={"file":EXTRA_AB.name,"sha256":render.m01.sha(EXTRA_AB),
  "bytes":EXTRA_AB.stat().st_size}
 j["user_feedback"]="C部分感觉还是不够明显 — increase C candle and local halo modestly; avoid broad strong flashing"
 j["PO_visual_review_pending"]=True
 render.REPORT.write_text(json.dumps(j,ensure_ascii=False,indent=2)+"\n")
 assert render.m01.sha(PREV_VIDEO)==PREV_VIDEO_SHA
 assert render.m01.sha(PREV_QC)==PREV_QC_SHA
 print("M01_S02B_V018_C_GROUP_MORE_VISIBLE_FULL_AND_AB_READY",json.dumps({
  "full":j["preview"],"original_ab":j["ab"],"v017_vs_v018":j["previous_v017_to_v018_ab"],
  "C_group_max_changes":weak,"average_C_delta_increase":j["C_group_max_rgb_mean_increase"],
  "approved_three_changed":False},ensure_ascii=False),flush=True)
if __name__=="__main__":main()
