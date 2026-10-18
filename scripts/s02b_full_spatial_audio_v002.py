#!/usr/bin/env python3
"""S02-B full-length restrained spatial-footstep sound proof.
PO direction 2026-10-18: apply where appropriate, do not overwhelm the original.
Audio-only change between the rendered ordered-A and mixed-B; both use approved
N21->NEW02->N22->N23 ordering, preserve all timeline length and canonical assets.
No paid AI, no other new visual treatments, no canonical publication.
"""
from pathlib import Path
import hashlib
import json
import math
import subprocess
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "production/video_candidates/review/s02b_full_spatial_audio_v001"
SOURCE = ROOT / "production/environment_dynamic/review_candidates/S02_B_M01_V018_FULL_LENGTH_C_VISIBLE_REVIEW/S02_B_M01_V018_FULL_LENGTH_MORE_VISIBLE_C_GROUP_PREVIEW_V001.mp4"
SOURCE_SHA = "6897b1ac246e4c30d84aca3b80003a58d7bae86eb7631272fe28253b23a01427"
SFX = ROOT / "production/video_candidates/review/n23_spatial_audio_proof_01/PUBLIC_DOMAIN_CHURCH_FOOTSTEPS_SOURCE.ogg"
SFX_SHA1 = "8b2a6abb78bad2c5def0ab4496c4330472601445"
N23_V002 = ROOT / "production/video_candidates/review/n23_spatial_audio_proof_01/N23_AUDIO_B_STONE_FOOTSTEPS_SPACE_CANDIDATE_V002.mp4"
N23_V002_SHA = "9b58bd86c47d276daffb40e24d34c3d88303b847d8c271c3f8bb90df123c709e"
EDL = ROOT / "production/editorial_specs/S02_B_V006_CINEMATIC_ROUGH_EDL_V002_RENDERED_RECONSTRUCTED_REVIEW.json"
FPS, RATE, FRAMES = 30, 48000, 1927
SAMPLES_PER_FRAME = RATE // FPS
A = OUT / "S02_B_V019_SPATIAL_AUDIO_A_APPROVED_ORDER_ORIGINAL_SOUND.mp4"
A_EXPECTED_SHA = "2defc8989a038822f39284eed815499a4f4812996b5ff8103a7ad298a81a0250"
B = OUT / "S02_B_V019_SPATIAL_AUDIO_B_FULL_CANDIDATE_V002.mp4"
AB = OUT / "S02_B_V019_SPATIAL_AUDIO_A_B_SELECTED_EXCERPTS_V002.mp4"
REPORT = OUT / "S02_B_V019_SPATIAL_AUDIO_FULL_QC_V002.json"
EXCERPT_LIST = [
    ("N21_THROUGH_N23", 1114, 1448),    # full movement group and reviewed N23
    ("A06_N24", 1448, 1694),            # steps retreat while someone asks about the door
    ("N25_TO_N26", 1694, 1927),         # rain-day explanation through final group exit
]
# Ambience applied ONLY where picture supports ongoing footsteps.
# N23 reuses the approved V002 source offset, EQ and relative sound level.
# No feet in N16..N20 (discussion), N24 (questioning pause), or Ning close reaction.
CUES = [
    {"shot":"N21_NEW02_N22_COHORT", "start":1114, "end":1366, "source_sec":13.0,
     "relative_rms":0.080, "fade_in":.42, "fade_out":.22, "direction":[.77,1.0],
     "movement":"cohort walks past entrance and inward", "speech_guard":True},
    {"shot":"N23_NEIL_OPEN_DOOR_APPROVED_V002", "start":1366, "end":1448, "source_sec":6.5,
     "relative_rms":0.11687111244, "fade_in":.22, "fade_out":.22, "direction":[.72,1.0],
     "movement":"people pass Neil; reuse PO-approved local sound profile", "speech_guard":False},
    {"shot":"A06_NEIL_START_MOVING", "start":1448, "end":1575, "source_sec":3.0,
     "relative_rms":0.050, "fade_in":.26, "fade_out":.42, "direction":[.92,1.0],
     "movement":"guide leaves open doorway; fewer receding steps", "speech_guard":True},
    {"shot":"N25_NEIL_WALKS_WHILE_ANSWERING", "start":1694, "end":1810, "source_sec":19.0,
     "relative_rms":0.054, "fade_in":.28, "fade_out":.42, "direction":[.95,1.0],
     "movement":"guide moving amid group during rain-day answer", "speech_guard":True},
    {"shot":"N26_DEEPER_INTO_CASTLE", "start":1863, "end":1927, "source_sec":10.0,
     "relative_rms":0.058, "fade_in":.25, "fade_out":.35, "direction":[.92,1.0],
     "movement":"final group walking inward", "speech_guard":True},
]
def call(*argv):
    cmd=[str(x) for x in argv]
    return subprocess.run(cmd,check=True,capture_output=True).stdout
def digest(p,which="sha256"):
    h=hashlib.new(which)
    with open(p,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()
def ffinfo(p):
    return json.loads(call("ffprobe","-v","error","-show_entries",
            "stream=codec_type,r_frame_rate,nb_frames,width,height,sample_rate,channels:format=duration",
            "-of","json",p))
def count_frames(p):
    obj=json.loads(call("ffprobe","-v","error","-count_frames",
          "-select_streams","v:0","-show_entries","stream=nb_read_frames,width,height,r_frame_rate",
          "-of","json",p))
    s=obj["streams"][0]
    assert int(s["width"])==720 and int(s["height"])==1280 and s["r_frame_rate"]=="30/1",s
    return int(s["nb_read_frames"])
def video_sha(p):
    return hashlib.sha256(call("ffmpeg","-v","error","-i",p,
        "-map","0:v:0","-c:v","copy","-f","h264","pipe:1")).hexdigest()
def original_aac(p):
    return hashlib.sha256(call("ffmpeg","-v","error","-i",p,
        "-map","0:a:0","-c:a","copy","-f","adts","pipe:1")).hexdigest()
def pcm(p, filters=None):
    args=["ffmpeg","-v","error","-i",p]
    if filters:args+=["-af",filters]
    args+=["-map","0:a:0","-ac","2","-ar",str(RATE),"-f","f32le","-acodec","pcm_f32le","pipe:1"]
    return np.frombuffer(call(*args),dtype="<f4").copy().reshape(-1,2)
def rms(x):
    return float(np.sqrt(np.mean(x.astype(np.float64)**2)))
def env(shape,fin,fout):
    t=np.arange(shape,dtype=np.float64)/RATE
    return (np.minimum(1.,t/max(fin,.001))*
            np.minimum(1.,(t[-1]-t)/max(fout,.001))).astype(np.float32)
def source_audio_segment(sfx,source_sec,samples):
    start=int(round(source_sec*RATE))
    if start+samples>len(sfx):
        # Deterministic fallback anchored to end, never read out of range.
        start=max(0,len(sfx)-samples-200)
    assert start+samples <= len(sfx),(start,samples,len(sfx))
    return sfx[start:start+samples].copy(),start/RATE
def speech_guard(original,clip):
    """Keep supplemental sound quiet during stronger original audio regions.
    A sound-energy proxy, NOT a speech classifier. One-sided reduction only.
    """
    interval=RATE//10
    energy=[]
    for i in range(0,len(original),interval):
        block=original[i:i+interval]
        energy.append(rms(block))
    energy=np.array(energy)
    pivot=max(float(np.median(energy)),0.002)
    # Duck stronger original-audio moments by up to 30%, not make them louder.
    reduction=np.clip((energy/(pivot+1e-8)-.85)*.20,0,.30)
    gains=1.0-reduction
    points=(np.arange(len(gains),dtype=np.float64)+.5)*interval
    values=np.interp(np.arange(len(original)),points,gains,left=gains[0],right=gains[-1])
    return (clip*values[:,None].astype(np.float32)),float(reduction.max())
def ratio_limit(original,fx,limit):
    """Cap added RMS in any 100 ms window, gently smoothing with interpolation."""
    block=RATE//10
    control=[]
    for j in range(0,len(original),block):
        or_rms=rms(original[j:j+block])
        fx_rms=rms(fx[j:j+block])
        # Smaller signal when no speech; avoid making extra prominent in silence.
        permitted=min(limit*max(or_rms,.0016),.0075)
        control.append(min(1.,permitted/max(fx_rms,1e-10)))
    control=np.asarray(control,dtype=np.float64)
    points=(np.arange(len(control))+.5)*block
    gains=np.interp(np.arange(len(original)),points,control,
        left=control[0],right=control[-1])
    return fx*gains[:,None].astype(np.float32),float(np.min(gains))
def render_ordered_base():
    # Ordering approved by PO: N21 -> NEW02 -> N22 -> N23. No other changes.
    # Source V018 picture is re-encoded only because order is not stream-copy aligned.
    parts=[(0,1114),(1114,1222),(1299,1366),(1222,1299),(1366,1927)]
    splits="".join(f"[s{i}]" for i in range(len(parts)))
    filters=f"[0:v]split={len(parts)}{splits};"
    for i,(start,stop) in enumerate(parts):
        filters+=(f"[s{i}]trim=start_frame={start}:end_frame={stop},"
                  f"setpts=PTS-STARTPTS[p{i}];")
    filters+="".join(f"[p{i}]" for i in range(len(parts)))+f"concat=n={len(parts)}:v=1:a=0[v]"
    call("ffmpeg","-v","error","-y","-i",SOURCE,"-filter_complex",filters,
         "-map","[v]","-map","0:a:0","-c:v","libx264","-preset","medium",
         "-crf","16","-pix_fmt","yuv420p","-r",str(FPS),"-c:a","copy",
         "-movflags","+faststart",A)
    assert count_frames(A)==FRAMES,"Reorder edited timeline or frames unexpectedly"
    assert original_aac(A)==original_aac(SOURCE),"Original AAC packet stream changed"
    print("SOURCE_TO_A_PASS",digest(SOURCE),digest(A),flush=True)

def make_excerpt_comparison():
    # A and B have same picture, differ only in low-volume sound augmentation.
    # Use sample-rich 11.13s core A/B one after the other (no SFX-only interlude).
    start,end=EXCERPT_LIST[0][1:]
    start_sec=start/FPS
    dur=(end-start)/FPS
    flt=(
       f"[0:v]trim=start_frame={start}:end_frame={end},setpts=PTS-STARTPTS,"
       "drawtext=text='A ORIGINAL SOUND':fontcolor=white:fontsize=24:"
       "x=16:y=24:box=1:boxcolor=black@0.6[va];"
       f"[1:v]trim=start_frame={start}:end_frame={end},setpts=PTS-STARTPTS,"
       "drawtext=text='B WITH SPATIAL FOLEY':fontcolor=white:fontsize=24:"
       "x=16:y=24:box=1:boxcolor=black@0.6[vb];"
       f"[0:a]atrim=start={start_sec:.8f}:duration={dur:.8f},"
       "asetpts=PTS-STARTPTS[aa];"
       f"[1:a]atrim=start={start_sec:.8f}:duration={dur:.8f},"
       "asetpts=PTS-STARTPTS[ab];"
       "[va][aa][vb][ab]concat=n=2:v=1:a=1[v][a]")
    call("ffmpeg","-v","error","-y","-i",A,"-i",B,
         "-filter_complex",flt,"-map","[v]","-map","[a]",
         "-c:v","libx264","-preset","veryfast","-crf","21","-pix_fmt","yuv420p",
         "-c:a","aac","-b:a","192k","-fps_mode:v","passthrough",
         "-movflags","+faststart",AB)
    assert count_frames(AB)==(end-start)*2

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    for p in (SOURCE,SFX,N23_V002,EDL):
        assert p.exists(),f"missing input: {p}"
    assert digest(SOURCE)==SOURCE_SHA,"V018 exact identity FAIL"
    assert digest(SFX,"sha1")==SFX_SHA1,"Reference recorded audio SHA1 FAIL"
    assert digest(N23_V002)==N23_V002_SHA,"PO approved N23 B V002 binary mismatch"
    assert count_frames(SOURCE)==FRAMES
    assert all(not p.exists() for p in (B,AB,REPORT)),"Append-only: V002 output already exists"
    edl=json.loads(EDL.read_text())
    nodes=edl["timeline"]
    assert len(nodes)==17 and nodes[-1]["end_frame_exclusive"]==FRAMES
    assert {n["id"]:n["start_frame"] for n in nodes}["N23"]==1366
    assert A.exists() and digest(A)==A_EXPECTED_SHA,"Earlier ordered-A image/audio baseline changed"
    assert original_aac(A)==original_aac(SOURCE),"A original packets changed"
    source_original=pcm(A)
    print("PCM_ORIGINAL",source_original.shape,flush=True)
    full_length=len(source_original)
    assert full_length>=FRAMES*SAMPLES_PER_FRAME,"Truncated source PCM"
    added=np.zeros_like(source_original,dtype=np.float32)
    record=pcm(SFX,"highpass=f=110,lowpass=f=3300")
    stats=[]
    for cue in CUES:
        l,r=cue["start"]*SAMPLES_PER_FRAME,cue["end"]*SAMPLES_PER_FRAME
        scene_orig=source_original[l:r]
        samples=r-l
        seed,offset=source_audio_segment(record,cue["source_sec"],samples)
        t=np.arange(samples,dtype=np.float32)/RATE
        distance=np.interp(t,[0,float(samples/RATE)],[.85,.48]).astype(np.float32)
        layer=seed*(env(samples,cue["fade_in"],cue["fade_out"])*distance)[:,None]
        layer*=np.array(cue["direction"],dtype=np.float32)[None,:]
        o_rms=rms(scene_orig)
        layer_rms=rms(layer)
        assert o_rms>0.0002 and layer_rms>0.00003,(cue["shot"],o_rms,layer_rms)
        gain=cue["relative_rms"]*o_rms/layer_rms
        layer*=gain
        if cue["speech_guard"]:
            layer,ducked=speech_guard(scene_orig,layer)
        else:ducked=0.
        # All cues limited by per-100ms local program RMS; for N23 preserve
        # V002 average loudness target as far as original audio headroom allows.
        if cue["shot"]=="N23_NEIL_OPEN_DOOR_APPROVED_V002":
            # Do not suppress N23 after PO explicitly approved this profile.
            scale_min=1.0
        else:
            layer,scale_min=ratio_limit(scene_orig,layer,.16)
        added[l:r]+=layer
        stats.append({
          "shot":cue["shot"],"source_frames":[cue["start"],cue["end"]],
          "timeline_sec":[cue["start"]/FPS,cue["end"]/FPS],
          "reason":cue["movement"],
          "relative_layer_rms_to_original":rms(layer)/o_rms,
          "target_ratio":cue["relative_rms"],
          "speech_energy_ducking_applied":cue["speech_guard"],
          "max_speech_ducking_factor":ducked,
          "min_100ms_relative_scale":scale_min,
          "source_sample_offset_sec":offset,
          "fade_in_out_seconds":[cue["fade_in"],cue["fade_out"]],
          "recorded_sfx_sha1":SFX_SHA1
        })
    combined=source_original+added
    for iteration in range(25):
        peak=float(np.max(np.abs(combined)))
        if peak<=.985:break
        added*=.88
        combined=source_original+added
    peak=float(np.max(np.abs(combined)))
    assert peak<=.985,f"Mixing would clip: {peak}"
    n23_l,n23_r=1366*SAMPLES_PER_FRAME,1448*SAMPLES_PER_FRAME
    n23_final_ratio=rms(added[n23_l:n23_r])/rms(source_original[n23_l:n23_r])
    assert .105 <= n23_final_ratio <= .13, (
        "N23 approved V002 level not preserved in full context",n23_final_ratio)
    assert np.allclose(combined-added,source_original,atol=2e-6),"Original PCM altered"
    assert np.count_nonzero(added[:1114*SAMPLES_PER_FRAME])==0, "Added steps to conversation opening"
    assert np.count_nonzero(added[1575*SAMPLES_PER_FRAME:1694*SAMPLES_PER_FRAME])==0,"Added footsteps to question pause"
    assert np.count_nonzero(added[1810*SAMPLES_PER_FRAME:1863*SAMPLES_PER_FRAME])==0,"Added footsteps to reaction"
    temp=OUT/"_tmp_b_mix_48k_stereo.f32"
    try:
        combined.astype("<f4").tofile(temp)
        call("ffmpeg","-v","error","-y","-i",A,
          "-f","f32le","-ar",str(RATE),"-ac","2","-i",temp,
          "-map","0:v:0","-map","1:a:0",
          "-c:v","copy","-c:a","aac","-b:a","256k",
          "-movflags","+faststart",B)
    finally:
        temp.unlink(missing_ok=True)
    assert count_frames(B)==FRAMES
    expected_pic_sha=video_sha(A)
    assert video_sha(B)==expected_pic_sha,"A/B picture elementary streams differ"
    assert original_aac(A)==original_aac(SOURCE),"Input original track changed"
    assert original_aac(B)!=original_aac(A),"Did not create audio augmentation"
    assert digest(SOURCE)==SOURCE_SHA and digest(N23_V002)==N23_V002_SHA
    make_excerpt_comparison()
    assert video_sha(A)==video_sha(B),"A/B comparison altered picture"
    report={
       "project":"BLACK-LADY-001",
       "candidate":"S02_B_V019_SPATIAL_AUDIO_FULL_V002",
       "status":"TECHNICAL_PASS_PO_FULL_LENGTH_REVIEW_PENDING",
       "source_V018_exact_sha256":SOURCE_SHA,
       "N23_reference_PO_approved_V002_sha256":N23_V002_SHA,
       "scope":"full S02-B 1927 frames; selected walking beats only",
       "video_approved_reorder":["N21","V006_NEW_02","N22_FIRST","N23"],
       "other_cut_positions":"unchanged",
       "full_video_frames_A_B":FRAMES,
       "N23_full_context_foley_to_original_RMS":n23_final_ratio,
       "N23_V002_PO_approved_reference_foley_to_original_RMS":0.11687111244,
       "N23_reference_level_gate":"PASS within 0.105..0.130",
       "fps":FPS,"format":"720x1280",
       "input_aac_adts_sha256":original_aac(SOURCE),
       "A_original_AAC_packet_equal_source":True,
       "B_reencoded_AAC_due_to_mixing":True,
       "original_audio_PCM_unity_in_B_mix_input":True,
       "full_A_B_picture_elementary_H264_SHA256":expected_pic_sha,
       "audio_added_only_in_walking_story_shots":[x["shot"] for x in stats],
       "selected_cues":stats,
       "no_footsteps_in_nonmovement_shots":True,
       "original_audio_energy_overlays":"conservative, max 100ms window; reduce overlay on high program energy",
       "mix_peak":peak,
       "added_footsteps_overall_relative_rms":rms(added)/rms(source_original),
       "sfx_public_domain":"https://commons.wikimedia.org/wiki/File:Church_people_walking_steps_with_reverb.ogg",
       "sfx_sha1":SFX_SHA1,
       "sfx_contains_some_room_murmurs":True,
       "audio_limitations":"Sound energy ducking is not a semantic speech detector; actual listening is required. N23 same approved SFX settings but remixed against full source (not binary-identical to prior isolated V002).",
       "full_audio_context_PO_approval":False,
       "artistic_approval_not_implied":True,
       "no_paid_AI_video":True,"no_new_images":True,
       "V018_canonical_unchanged":True,
       "no_main_merge":True,
       "A_full_review_sha256":digest(A),
       "B_full_review_sha256":digest(B),
       "AB_selected_excerpt_sha256":digest(AB)
    }
    REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps(report,ensure_ascii=False,indent=2),flush=True)

if __name__=="__main__":
    main()
