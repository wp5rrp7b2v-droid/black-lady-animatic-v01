#!/usr/bin/env python3
"""N23 ambient air minimal video proof. No AI video, character animation, or transition editing.
A V018 frames 1366..1447 -> B subtle fixed-architecture-mask haze/dust -> A/B.
Review-only GitHub branch. No modification of canonical files.
"""
from pathlib import Path
import hashlib
import json
import math
import subprocess
import os
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "production/environment_dynamic/review_candidates/S02_B_M01_V018_FULL_LENGTH_C_VISIBLE_REVIEW/S02_B_M01_V018_FULL_LENGTH_MORE_VISIBLE_C_GROUP_PREVIEW_V001.mp4"
SHA256 = "6897b1ac246e4c30d84aca3b80003a58d7bae86eb7631272fe28253b23a01427"
OUT = ROOT / "production/video_candidates/review/n23_environment_micro_dynamic_proof_01"
W, H, FPS = 720, 1280, 30
FIRST, LAST = 1366, 1448
N = LAST - FIRST
BYTES_PER_FRAME = W * H * 3

def run(*args):
    print("RUN:",str(args[0]), " ".join(map(str,args[1:5])), flush=True)
    return subprocess.run([str(a) for a in args], check=True, capture_output=True).stdout

def sha(path):
    with open(path, "rb") as f:
        return hashlib.file_digest(f,"sha256").hexdigest()

def frames(path, expected_size=(W,H)):
    p=json.loads(run("ffprobe","-v","error","-count_frames","-select_streams","v:0",
        "-show_entries","stream=nb_read_frames,width,height,r_frame_rate",
        "-of","json",path))
    s=p["streams"][0]
    assert (int(s["width"]),int(s["height"]),s["r_frame_rate"]) == (*expected_size,"30/1"),s
    return int(s["nb_read_frames"])

def packet_hash(path):
    raw=run("ffmpeg","-v","error","-i",path,"-map","0:a:0","-c:a","copy","-f","adts","pipe:1")
    return hashlib.sha256(raw).hexdigest()

def read_exact(stream,n):
    data=bytearray()
    while len(data)<n:
        new=stream.read(n-len(data))
        if not new:
            raise ValueError(f"Incomplete raw RGB frame {len(data)}/{n}")
        data.extend(new)
    return bytes(data)

def make_ambient(frame, t, particles, gx, gy):
    """Restrict all changes to high architectural backdrop, above heads."""
    input_rgb=frame.astype(np.float32)
    luminance=input_rgb[:,:,0]*.299+input_rgb[:,:,1]*.587+input_rgb[:,:,2]*.114
    # Top-only background matte: y<370 with a soft tail, x<110 untouched.
    ymask=np.clip((375-gy)/90,0,1) * np.clip((gx-108)/100,0,1)
    # Keep bright sconce/fire sources untouched; no new full-screen flashes.
    protect=np.clip((145-luminance)/60,0,1)
    back=ymask*protect
    # Drifting, low-opacity cool veil in the far upper architecture, not over any person.
    cx=525+9*np.sin(t*.7)
    cy=145+5*np.sin(t*.9)
    field=np.exp(-(((gx-cx)/260)**2 + ((gy-cy)/185)**2)*0.5)
    fog_alpha=0.026*field*back
    # Do not brighten any channel globally. Dimming upper stone < 5 levels.
    output=input_rgb*(1.0-fog_alpha[:,:,None])
    # Sparse coherent dust motes: not noisy grain, different phases and slow motion.
    for p in particles:
        px=p["x"]+p["dx"]*t
        py=p["y"]+p["dy"]*t
        sigma=p["sigma"]
        x0=max(0,int(px-4*sigma)); x1=min(W,int(px+4*sigma)+1)
        y0=max(0,int(py-4*sigma)); y1=min(H,int(py+4*sigma)+1)
        if x1<=x0 or y1<=y0:continue
        xx=gx[y0:y1,x0:x1]
        yy=gy[y0:y1,x0:x1]
        flare=.55+.45*(.5+.5*math.sin(1.5*t+p["phase"]))
        alpha=.17*flare*np.exp(-((xx-px)**2+(yy-py)**2)/(2*sigma*sigma))
        alpha*=back[y0:y1,x0:x1]
        rgb=np.array((135,132,122),dtype=np.float32)
        region=output[y0:y1,x0:x1]
        output[y0:y1,x0:x1]=region*(1-alpha[:,:,None])+rgb*alpha[:,:,None]
    result=np.clip(np.rint(output),0,255).astype(np.uint8)
    # Exact processing-stage pixel preservation for character/body/crowd zone.
    assert np.array_equal(result[376:,:,:],frame[376:,:,:]),"Subject zone modified"
    assert np.array_equal(result[:,:108,:],frame[:,:108,:]),"Left architecture edge modified"
    return result

def mux(silent,audio,out):
    run("ffmpeg","-v","error","-y","-i",silent,"-i",audio,"-map","0:v:0",
        "-map","1:a:0","-c:v","copy","-c:a","copy","-movflags","+faststart",out)

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    assert SOURCE.is_file(), "Exact approved V018 missing"
    assert sha(SOURCE)==SHA256, "V018 source mismatched"
    A_SILENT=OUT/"_tmp_A_video_silent.mp4"
    B_SILENT=OUT/"_tmp_B_video_silent.mp4"
    AUDIO=OUT/"_tmp_audio_source.aac"
    A=OUT/"N23_A_V018_ORIGINAL_SEGMENT_REVIEW.mp4"
    B=OUT/"N23_B_AMBIENT_AIR_MICRO_DYNAMIC_CANDIDATE_V001.mp4"
    AB=OUT/"N23_A_B_SIDE_BY_SIDE_AMBIENT_AIR_REVIEW_V001.mp4"
    # Exact source-frame selection, not nearest keyframe cut.
    filter=f"[0:v]trim=start_frame={FIRST}:end_frame={LAST},setpts=PTS-STARTPTS[v]"
    run("ffmpeg","-v","error","-y","-i",SOURCE,"-filter_complex",filter,
        "-map","[v]","-an","-frames:v",str(N),"-c:v","libx264",
        "-preset","fast","-crf","17","-pix_fmt","yuv420p",A_SILENT)
    assert frames(A_SILENT)==N
    # A packet-level audio excerpt; no AAC encoding, mixing or retiming.
    run("ffmpeg","-v","error","-y","-ss",f"{FIRST/FPS:.6f}",
        "-i",SOURCE,"-t",f"{N/FPS:.6f}","-map","0:a:0",
        "-c:a","copy","-f","adts",AUDIO)
    mux(A_SILENT,AUDIO,A)
    # Read B source from the same A-exact video frame sequence.
    reader=subprocess.Popen(["ffmpeg","-v","error","-i",str(A_SILENT),
                             "-map","0:v:0","-f","rawvideo","-pix_fmt","rgb24","pipe:1"],
                             stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
    writer=subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo",
                             "-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),
                             "-i","pipe:0","-an","-c:v","libx264","-crf","18",
                             "-preset","fast","-pix_fmt","yuv420p",str(B_SILENT)],
                             stdin=subprocess.PIPE,stderr=subprocess.DEVNULL)
    rng=np.random.default_rng(23017)
    particles=[]
    for _ in range(13):
        particles.append(dict(x=float(rng.uniform(245,680)),
            y=float(rng.uniform(65,270)),
            dx=float(rng.uniform(-1.3,1.3)),
            dy=float(rng.uniform(-4.2,-1.5)),
            phase=float(rng.uniform(0,2*math.pi)),
            sigma=float(rng.uniform(1.8,4.0))))
    gx,gy=np.meshgrid(np.arange(W,dtype=np.float32),
                      np.arange(H,dtype=np.float32))
    altered=0
    maximum=0
    upperdiff=0
    try:
        for i in range(N):
            raw=read_exact(reader.stdout,BYTES_PER_FRAME)
            frame=np.frombuffer(raw,dtype=np.uint8).reshape((H,W,3)).copy()
            edited=make_ambient(frame,i/FPS,particles,gx,gy)
            difference=np.abs(edited.astype(np.int16)-frame.astype(np.int16))
            altered+=int(np.any(difference!=0,axis=2).sum())
            maximum=max(maximum,int(difference.max()))
            upperdiff+=int(np.sum(difference[:376]))
            writer.stdin.write(edited.tobytes())
            if i==N//2:
                Image.fromarray(frame).save(OUT/"N23_ORIGINAL_MIDFRAME.jpg",quality=92)
                Image.fromarray(edited).save(OUT/"N23_AMBIENT_MIDFRAME.jpg",quality=92)
        writer.stdin.close()
        assert reader.wait()==0,"A source video decode failed"
        assert writer.wait()==0,"B render failed"
    finally:
        if reader.poll() is None:reader.kill()
        if writer.poll() is None:writer.kill()
    assert frames(B_SILENT)==N
    mux(B_SILENT,AUDIO,B)
    assert frames(A)==frames(B)==N,"A/B frame count differs"
    a_hash,b_hash=packet_hash(A),packet_hash(B)
    assert a_hash==b_hash,"N23 A/B AAC packet hashes differ"
    run("ffmpeg","-v","error","-y","-i",A,"-i",B,
        "-filter_complex","[0:v]scale=540:960[a];[1:v]scale=540:960[b];[a][b]hstack=inputs=2[v]",
        "-map","[v]","-map","0:a:0","-c:v","libx264","-preset","fast",
        "-crf","22","-pix_fmt","yuv420p","-c:a","copy",
        "-movflags","+faststart",AB)
    assert frames(AB, expected_size=(1080,960))==N
    assert packet_hash(AB)==a_hash
    report=dict(
        project="BLACK-LADY-001",
        shot="N23",type="SINGLE_SHOT_ENVIRONMENT_MICRO_DYNAMIC_PROOF_01",
        status="TECHNICAL_PASS_PO_VISUAL_REVIEW_PENDING",
        original_V018_sha256=SHA256,
        time_range_seconds=[round(FIRST/FPS,6),round(LAST/FPS,6)],
        source_frames=[FIRST,LAST-1],frame_count=N,
        fps=FPS,resolution=[W,H],
        allowed_regions="Upper-background only, y<376,x>108, excluding bright flames/fixtures",
        processing_stage_pixels_y_376_plus_changed=0,
        processing_stage_pixels_x_0_107_changed=0,
        effect_components=["small sparse drifting dust","very low contrast upper-arch air veil"],
        actual_changed_upper_pixels_accumulated=altered,
        maximum_raw_pixel_delta=maximum,raw_rgb_delta_sum_upper=upperdiff,
        audio_AAC_ADTS_SHA256_A_B_AB=a_hash,
        source_audio_no_reencode=True,
        no_AI_video=True,no_character_motion=True,no_transition_change=True,
        visual_result_not_yet_approved=True,
        visual_caveat="A/B encoded H264 naturally produces small compression differences outside mask; processing-stage zero-difference is the preservation proof.",
        filenames={"A":A.name,"B":B.name,"AB":AB.name},
        A_sha256=sha(A),B_sha256=sha(B),AB_sha256=sha(AB)
    )
    (OUT/"N23_ENV_MICRO_DYNAMIC_QC_V001.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(report,ensure_ascii=False),flush=True)
    for p in (A_SILENT,B_SILENT,AUDIO):
        p.unlink(missing_ok=True)

if __name__=="__main__":
    main()
