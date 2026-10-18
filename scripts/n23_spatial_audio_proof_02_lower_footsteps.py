#!/usr/bin/env python3
"""N23 Spatial Audio V002 — reduce only the already-existing V001 footsteps by 15%.
Original V018 and archived V001 trial are immutable. Output is review-only.
"""
from pathlib import Path
import hashlib
import json
import math
import subprocess
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "production/video_candidates/review/n23_spatial_audio_proof_01"
A = DIR / "N23_AUDIO_A_V018_ORIGINAL.mp4"
B1 = DIR / "N23_AUDIO_B_STONE_FOOTSTEPS_SPACE_CANDIDATE_V001.mp4"
SFX = DIR / "PUBLIC_DOMAIN_CHURCH_FOOTSTEPS_SOURCE.ogg"
B2 = DIR / "N23_AUDIO_B_STONE_FOOTSTEPS_SPACE_CANDIDATE_V002.mp4"
COMPARE = DIR / "N23_AUDIO_B_V001_VS_V002_LISTENING_COMPARISON.mp4"
REPORT = DIR / "N23_SPATIAL_AUDIO_V002_QC.json"
EXPECTED_A = "2d885c6ac63481781571e8d054f1c2645c0ae96c2ebc664e17370b30a97d2f42"
EXPECTED_B1 = "3c246a4fa6c7bb804a650e389f5d648b7f565b8a74e9bdcb88ca1f22de21a908"
EXPECTED_SFX_SHA1 = "8b2a6abb78bad2c5def0ab4496c4330472601445"
RATE, FRAMES, FPS = 48000, 82, 30
FOOTSTEP_FACTOR = 0.85  # V002 = 85% of V001 added-footstep gain (15% lower)
ORIGINAL_SFX_OFFSET = 6.5

def run(*argv):
    return subprocess.run([str(x) for x in argv], check=True, capture_output=True).stdout

def digest(path, algorithm="sha256"):
    h=hashlib.new(algorithm)
    with open(path,"rb") as fp:
        for part in iter(lambda:fp.read(1048576),b""):h.update(part)
    return h.hexdigest()

def get_pcm(path, args=None):
    prefix=["ffmpeg","-v","error","-i",path]
    if args:prefix.extend(args)
    prefix.extend(["-ar",str(RATE),"-ac","2","-f","f32le","-acodec","pcm_f32le","pipe:1"])
    return np.frombuffer(run(*prefix),dtype="<f4").copy().reshape(-1,2)

def rms(x):
    return float(np.sqrt(np.mean(x.astype(np.float64)**2)))

def video_bitstream_hash(p):
    return hashlib.sha256(run("ffmpeg","-v","error","-i",p,"-map","0:v:0",
              "-c:v","copy","-f","h264","pipe:1")).hexdigest()

def get_frames(p):
    j=json.loads(run("ffprobe","-v","error","-count_frames","-select_streams","v:0",
      "-show_entries","stream=nb_read_frames,r_frame_rate,width,height","-of","json",p))
    s=j["streams"][0]
    assert s["r_frame_rate"]=="30/1"
    assert int(s["width"])==720 and int(s["height"])==1280
    return int(s["nb_read_frames"])

def main():
    for f in [A,B1,SFX]:assert f.exists(),f
    assert digest(A)==EXPECTED_A, "A archive changed"
    assert digest(B1)==EXPECTED_B1, "B V001 archive changed"
    assert digest(SFX,"sha1")==EXPECTED_SFX_SHA1, "SFX archive changed"
    assert not B2.exists(), "Fail closed: do not overwrite a candidate V002"
    assert not COMPARE.exists(), "Fail closed: do not overwrite comparison V002"
    assert get_frames(A)==get_frames(B1)==FRAMES
    picture_sha=video_bitstream_hash(A)
    assert picture_sha==video_bitstream_hash(B1)

    original=get_pcm(A)
    recorded=get_pcm(SFX,args=["-af","highpass=f=110,lowpass=f=3300"])
    start=int(ORIGINAL_SFX_OFFSET*RATE)
    assert start+len(original)<=len(recorded)
    excerpt=recorded[start:start+len(original)].copy()
    t=np.arange(len(original))/RATE
    fadein=np.minimum(1,t/.22)
    fadeout=np.minimum(1,(t[-1]-t)/.22)
    distance=np.interp(t,[0,t[-1]],[.85,.48])
    envelope=np.clip(fadein*fadeout*distance,0,1)
    overlay=excerpt*envelope[:,None]*np.array([.72,1.0],dtype=np.float32)[None,:]
    orig_rms=rms(original)
    foot_rms=rms(overlay)
    assert orig_rms>.0002 and foot_rms>.00002
    extra=overlay*(.24*orig_rms/foot_rms)
    mix1=original+extra
    for _ in range(20):
        if float(np.max(np.abs(mix1)))<=.985:break
        extra*=.87
        mix1=original+extra
    assert float(np.max(np.abs(mix1)))<=.985
    baseline_ratio=rms(extra)/orig_rms
    assert abs(baseline_ratio-0.1374954264)<0.001, (
      "V001 footstep reconstruction differs; stop",baseline_ratio)

    extra2=extra*FOOTSTEP_FACTOR
    mix2=original+extra2
    assert float(np.max(np.abs(mix2)))<=.985,"V002 clipping detected"
    assert np.allclose(mix2-extra2,original,atol=1e-6)
    tmp=DIR/"_TEMP_B2_MIX.f32"
    try:
        mix2.astype("<f4").tofile(tmp)
        run("ffmpeg","-v","error","-y","-i",A,
            "-f","f32le","-ar",str(RATE),"-ac","2","-i",tmp,
            "-map","0:v:0","-map","1:a:0","-c:v","copy",
            "-c:a","aac","-b:a","192k","-movflags","+faststart",B2)
    finally:
        tmp.unlink(missing_ok=True)
    assert get_frames(B2)==FRAMES
    assert video_bitstream_hash(B2)==picture_sha,"Picture changed"
    # Compare already-rendered B1 and new B2, preserving natural audiovisual sequence.
    filt=(
        "[0:v]setpts=PTS-STARTPTS,drawtext=text='B V001':"
        "fontcolor=white:fontsize=28:x=18:y=22:box=1:boxcolor=black@0.65[v0];"
        "[1:v]setpts=PTS-STARTPTS,drawtext=text='B V002 LIGHTER FOOTSTEPS':"
        "fontcolor=white:fontsize=28:x=18:y=22:box=1:boxcolor=black@0.65[v1];"
        "[0:a]aresample=48000,asetpts=PTS-STARTPTS[a0];"
        "[1:a]aresample=48000,asetpts=PTS-STARTPTS[a1];"
        "[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]")
    run("ffmpeg","-v","error","-y","-i",B1,"-i",B2,
        "-filter_complex",filt,"-map","[v]","-map","[a]",
        "-c:v","libx264","-crf","21","-preset","fast","-pix_fmt","yuv420p",
        "-c:a","aac","-b:a","192k","-fps_mode:v","passthrough",
        "-movflags","+faststart",COMPARE)
    assert get_frames(COMPARE)==FRAMES*2
    assert digest(A)==EXPECTED_A and digest(B1)==EXPECTED_B1
    result={
      "experiment":"N23_SPATIAL_AUDIO_V002_LOWER_FOOTSTEPS",
      "status":"TECHNICAL_PASS_PO_LISTENING_REVIEW_PENDING",
      "PO_feedback":"脚步声可以稍微轻一点点",
      "original_B_V001_sha256":EXPECTED_B1,
      "footstep_gain_from_V001":FOOTSTEP_FACTOR,
      "footstep_reduction_percent":15,
      "reconstructed_V001_foley_to_original_rms":baseline_ratio,
      "V002_foley_to_original_rms":rms(extra2)/orig_rms,
      "original_soundtrack_underlay_unchanged_at_PCM_mix_input":True,
      "V001_other_sound_effect_parameters_unchanged":True,
      "no_effects_added_or_transitions_modified":True,
      "A_B1_B2_source_picture_elementary_stream_sha256":picture_sha,
      "frame_count_B_V001":FRAMES,
      "frame_count_B_V002":get_frames(B2),
      "comparison_frame_count":get_frames(COMPARE),
      "mix_peak_B_V002":float(np.max(np.abs(mix2))),
      "SFX_exact_sha1":EXPECTED_SFX_SHA1,
      "SFX_original_reused_without_download":True,
      "no_paid_AI_services":True,
      "candidate_requires_PO_visual_audio_approval":True,
      "archived_A_sha256":EXPECTED_A,
      "archived_B_V001_sha256_after":digest(B1),
      "B_V002_sha256":digest(B2),
      "comparison_sha256":digest(COMPARE)
    }
    REPORT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(result,ensure_ascii=False,indent=2),flush=True)

if __name__=="__main__":
    main()
