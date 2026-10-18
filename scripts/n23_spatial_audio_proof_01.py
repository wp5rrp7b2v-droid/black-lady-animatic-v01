#!/usr/bin/env python3
"""N23 spatial-sound minimum proof — noncanonical, no extra paid services.
A original V018 AAC; B mix of original decoded soundtrack plus quiet, real
public-domain church/stone-floor footsteps and its natural recorded reverb.
Only sound differs. No alteration of V018 or existing visual pixels.
"""
from pathlib import Path
import hashlib, json, subprocess, urllib.request, math
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
VIDEO=ROOT/"production/environment_dynamic/review_candidates/S02_B_M01_V018_FULL_LENGTH_C_VISIBLE_REVIEW/S02_B_M01_V018_FULL_LENGTH_MORE_VISIBLE_C_GROUP_PREVIEW_V001.mp4"
VIDEO_SHA="6897b1ac246e4c30d84aca3b80003a58d7bae86eb7631272fe28253b23a01427"
OUT=ROOT/"production/video_candidates/review/n23_spatial_audio_proof_01"
SFX_URL="https://upload.wikimedia.org/wikipedia/commons/d/d5/Church_people_walking_steps_with_reverb.ogg"
SFX_SHA1="8b2a6abb78bad2c5def0ab4496c4330472601445"
SFX_ORIGIN="https://commons.wikimedia.org/wiki/File:Church_people_walking_steps_with_reverb.ogg"
FIRST,LAST,FPS=1366,1448,30
N=LAST-FIRST
RATE=48000
def run(*items):
    return subprocess.run([str(x) for x in items],check=True,capture_output=True).stdout
def hexsha(path,algorithm="sha256"):
    h=hashlib.new(algorithm)
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()
def aud_hash(path):
    return hashlib.sha256(run("ffmpeg","-v","error","-i",path,"-map","0:a:0",
        "-c:a","copy","-f","adts","pipe:1")).hexdigest()
def video_hash(path):
    return hashlib.sha256(run("ffmpeg","-v","error","-i",path,"-map","0:v:0",
        "-c:v","copy","-f","h264","pipe:1")).hexdigest()
def count_frames(path):
    data=json.loads(run("ffprobe","-v","error","-count_frames","-select_streams","v:0",
          "-show_entries","stream=nb_read_frames,width,height,r_frame_rate",
          "-of","json",path))
    info=data["streams"][0]
    assert int(info["width"])==720 and int(info["height"])==1280 and info["r_frame_rate"]=="30/1",info
    return int(info["nb_read_frames"])
def get_pcm(path):
    raw=run("ffmpeg","-v","error","-i",path,"-map","0:a:0","-ac","2","-ar",str(RATE),
            "-f","f32le","-acodec","pcm_f32le","pipe:1")
    return np.frombuffer(raw,dtype="<f4").copy().reshape(-1,2)
def rms(a):
    return float(np.sqrt(np.mean(np.square(a.astype(np.float64)))))
def download_sfx(path):
    request=urllib.request.Request(SFX_URL,headers={"User-Agent":"BlackLadyEducationalAudioProof/1.0 (GitHub Actions; Wikimedia Commons PD audio metadata verified)"})
    with urllib.request.urlopen(request,timeout=45) as resp:
        size=0
        with open(path,"wb") as file:
            while True:
                data=resp.read(65536)
                if not data:break
                size+=len(data)
                assert size < 3_000_000,"Unexpected remote file size"
                file.write(data)
    actual=hexsha(path,"sha1")
    assert actual==SFX_SHA1,(actual,SFX_SHA1)
    return size
def pick_footsteps(sfx,length):
    """Find a non-silent ~2.73s passage with transient rises; log selection.
    Selection is a reproducible heuristic, NOT a semantic footstep detector."""
    block=int(RATE*0.075)
    mono=np.mean(sfx,axis=1)
    total=sfx.shape[0]
    best_score=-1
    best_start=None
    for start_sec in np.arange(1.5,min(25,(total-length)/RATE-0.5),0.5):
        start=int(round(start_sec*RATE))
        raw=mono[start:start+length]
        chunks=len(raw)//block
        if chunks<10:continue
        env=np.sqrt(np.mean(raw[:chunks*block].reshape(chunks,block).astype(np.float64)**2,axis=1))
        rise=np.maximum(0,np.diff(env))
        # Reward real attacks (shoes) without choosing simply the loudest room chatter.
        score=(np.sum(rise)+0.04*np.percentile(env,85))/(np.median(env)+0.012)
        if score>best_score:
            best_score=score;best_start=start
    if best_start is None:raise AssertionError("Recorded SFX too short")
    return sfx[best_start:best_start+length].copy(),best_start/RATE,best_score
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    assert VIDEO.exists() and hexsha(VIDEO)==VIDEO_SHA,"Approved V018 exact source failed"
    sfx_file=OUT/"PUBLIC_DOMAIN_CHURCH_FOOTSTEPS_SOURCE.ogg"
    size=download_sfx(sfx_file)
    a_video=OUT/"_original_picture_silent.mp4"
    original_adts=OUT/"_original_packet_audio.aac"
    a_out=OUT/"N23_AUDIO_A_V018_ORIGINAL.mp4"
    b_out=OUT/"N23_AUDIO_B_STONE_FOOTSTEPS_SPACE_CANDIDATE_V001.mp4"
    ab_out=OUT/"N23_AUDIO_AB_A_THEN_B_LISTENING_COMPARISON.mp4"
    sound_raw=OUT/"_temp_B_stereo.f32"
    # Exact decoded 82-frame video from the original V018 timeline; both A and B
    # use this same stream with bitstream copy, so neither changes visual content.
    filter=f"[0:v]trim=start_frame={FIRST}:end_frame={LAST},setpts=PTS-STARTPTS[v]"
    run("ffmpeg","-v","error","-y","-i",VIDEO,
        "-filter_complex",filter,"-map","[v]","-an",
        "-frames:v",str(N),"-c:v","libx264","-preset","fast",
        "-crf","18","-pix_fmt","yuv420p",a_video)
    assert count_frames(a_video)==N
    run("ffmpeg","-v","error","-y","-ss",f"{FIRST/FPS:.6f}",
        "-i",VIDEO,"-t",f"{N/FPS:.6f}","-map","0:a:0","-c:a","copy",
        "-f","adts",original_adts)
    run("ffmpeg","-v","error","-y","-i",a_video,"-i",original_adts,
        "-map","0:v:0","-map","1:a:0","-c:v","copy","-c:a","copy",
        "-movflags","+faststart",a_out)
    assert count_frames(a_out)==N
    # Read A decoded PCM once; B includes A at unity with independent overlay.
    original=get_pcm(a_out)
    assert len(original)>int(RATE*2.5)
    sfx_pcm=np.frombuffer(run("ffmpeg","-v","error","-i",sfx_file,
        "-af","highpass=f=110,lowpass=f=3300","-ar",str(RATE),"-ac","2",
        "-f","f32le","pipe:1"),dtype="<f4").copy().reshape(-1,2)
    excerpt,start,transient=pick_footsteps(sfx_pcm,len(original))
    t=np.arange(len(original))/RATE
    # Spatial positioning: footsteps recede toward camera-right with a soft lead-in/out.
    fadein=np.minimum(1,t/.22)
    fadeout=np.minimum(1,(t[-1]-t)/.22)
    distance=np.interp(t,[0,t[-1]],[0.85,0.48])
    envelope=np.clip(fadein*fadeout*distance,0,1)
    overlay=excerpt*envelope[:,None]*np.array([.72,1.0],dtype=np.float32)[None,:]
    orig_rms=rms(original)
    recording_rms=rms(overlay)
    assert orig_rms>0.0002 and recording_rms>0.00002
    # Noticeable but quieter than the story/narration. Never attenuate original audio.
    scale=0.24*orig_rms/recording_rms
    extra=overlay*scale
    mix=original+extra
    for _ in range(20):
        if float(np.max(np.abs(mix)))<=0.985:break
        extra*=0.87;mix=original+extra
    assert np.max(np.abs(mix))<=0.985,"Original audio has insufficient mix headroom"
    assert np.max(np.abs(extra))>0
    assert np.allclose(mix-extra,original,atol=1e-6)
    mix.astype("<f4").tofile(sound_raw)
    run("ffmpeg","-v","error","-y","-i",a_video,"-f","f32le",
        "-ar",str(RATE),"-ac","2","-i",sound_raw,
        "-map","0:v:0","-map","1:a:0","-c:v","copy",
        "-c:a","aac","-b:a","192k","-movflags","+faststart",b_out)
    assert count_frames(b_out)==N
    v_ahash=video_hash(a_out)
    v_bhash=video_hash(b_out)
    assert v_ahash==v_bhash,"A/B source video bitstreams differ"
    assert aud_hash(a_out)==hexsha(original_adts), "A original AAC packets changed"
    assert aud_hash(b_out)!=aud_hash(a_out),"B audio was not changed"
    # Sequential review of the very same N23 picture, first A then B.
    filter_ab=(
      "[0:v]setpts=PTS-STARTPTS,drawtext=text='A ORIGINAL':fontcolor=white:"
      "fontsize=27:x=20:y=26:box=1:boxcolor=black@0.7[a];"
      "[1:v]setpts=PTS-STARTPTS,drawtext=text='B FOOTSTEPS + SPACE':"
      "fontcolor=white:fontsize=27:x=20:y=26:box=1:boxcolor=black@0.7[b];"
      "[0:a]aresample=48000,asetpts=PTS-STARTPTS[a0];"
      "[1:a]aresample=48000,asetpts=PTS-STARTPTS[a1];"
      "[a][a0][b][a1]concat=n=2:v=1:a=1[vo][ao]"
    )
    run("ffmpeg","-v","error","-y","-i",a_out,"-i",b_out,
        "-filter_complex",filter_ab,"-map","[vo]","-map","[ao]",
        "-c:v","libx264","-preset","fast","-crf","21","-pix_fmt","yuv420p",
        "-c:a","aac","-b:a","192k","-fps_mode:v","passthrough",
        "-movflags","+faststart",ab_out)
    assert count_frames(ab_out)==N*2
    report={
       "experiment":"N23_SPATIAL_AUDIO_MINIMUM_PROOF_V001",
       "review":"TECHNICAL_PASS_PO_LISTENING_REVIEW_PENDING",
       "original_V018_sha256":VIDEO_SHA,
       "shot":"N23","source_frame_inclusive":[FIRST,LAST-1],
       "frames_each":N,"fps":FPS,"picture_elementary_h264_sha256_A_equals_B":v_ahash,
       "original_A_AAC_ADTS_sha256":aud_hash(a_out),
       "extracted_source_AAC_ADTS_sha256":hexsha(original_adts),
       "B_AAC_ADTS_sha256":aud_hash(b_out),
       "A_B_audio_intentionally_different":True,
       "B_audio_unity_original_plus_independent_foley":True,
       "B_mix_pcm_peak":float(np.max(np.abs(mix))),
       "B_overlay_to_A_rms_ratio":rms(extra)/orig_rms,
       "B_audio_sample_rate":RATE,
       "SFX_public_domain_source_page":SFX_ORIGIN,
       "SFX_download_url":SFX_URL,"SFX_source_bytes":size,
       "SFX_source_sha1":hexsha(sfx_file,"sha1"),
       "selected_sfx_offset_sec":start,"selection_method":"transient_rise_heuristic",
       "source_recording_contains_possible_distant_murmurs":True,
       "foley_treatment":"HP 110 Hz, LP 3300 Hz, L/R bias, .22s fades, recession",
       "source_original_AAC_kept_separate":True,
       "no_visual_edit":True,"no_transition_edit":True,"no_paid_video_AI":True,
       "no_modification_to_V018_or_canonical_files":True,
       "pending_review":"Does added real-world room sound improve spatial depth without masking narration or sounding out of place?",
       "files":{"A":a_out.name,"B":b_out.name,"AB":ab_out.name},
       "sha256":{"A":hexsha(a_out),"B":hexsha(b_out),"AB":hexsha(ab_out)}
    }
    (OUT/"N23_SPATIAL_AUDIO_QC_V001.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    (OUT/"SOUND_PROVENANCE_AND_LIMITS.md").write_text(
        "# N23 Spatial Audio SFX\n\n"
        "Recorded by stephan (2007): Church people walking steps with reverb; "
        "Wikimedia Commons / PDSounds, public domain.\n\n"
        f"Source page: {SFX_ORIGIN}\n\n"
        f"Original SHA1: {SFX_SHA1}\n\n"
        "The recording includes footsteps, room reverb and some crowd murmurs. "
        "It is an independent candidate sound layer, not scene-accurate ground truth. "
        "Audible sound quality and any overlap with narration require Product Owner review. "
        "No audio enhancement is authorized for formal S02-B without separate approval.\n")
    for file in [a_video,original_adts,sound_raw]:
        file.unlink(missing_ok=True)
    print(json.dumps(report,indent=2,ensure_ascii=False),flush=True)
if __name__=="__main__":main()
