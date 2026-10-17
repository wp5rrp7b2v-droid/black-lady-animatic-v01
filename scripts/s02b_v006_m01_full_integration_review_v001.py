#!/usr/bin/env python3
"""S02-B V006 full-length one-candidate M01-only integration.
PO authorization 2026-10-17. Strictly review-only; never alter approved PNG,
source V006, official video index, approved audio, or main. No M02-M05.
"""
import hashlib
import json
import math
import pathlib
import struct
import subprocess

import numpy as np
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUTDIR = ROOT / "_s02b_v006_m01_full_review"
SOURCE = ROOT / "production/video_candidates/assets/S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_CANDIDATE_V001.mp4"
OUTPUT = OUTDIR / "S02_B_V006_CINEMATIC_ROUGH_M01_INTEGRATED_REVIEW_V001.mp4"
REPORT = OUTDIR / "M01_FULL_INTEGRATION_QC_V001.json"
VIDEO_ONLY = OUTDIR / "m01_video_only_intermediate.mp4"
BASE_SHA = "7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402"
W, H, FPS, FRAMES = 720, 1280, 30, 1927
SHOTS = [
    ("NEW02", 1299, 1366,
     "production/image_library/approved/story_shots/S02B_V006_NEW02_CROWD_INTERIOR_SIDE_DEPTH_APPROVED_V001.png",
     "d1866a667d7a24b8c5ae5b7670486b8b312e6f4a8fbce457763668e84d843bd4",
     1963410, "d8feba3692ebe25afd0e51f5e3ab32358ea19ded"),
    ("N23", 1366, 1448,
     "production/image_library/approved/story_shots/N23_NEIL_AT_OPEN_DOOR_APPROVED_V001.png",
     "2d94488e36d878ccb6ae7c3f9f3bf2a122eebca5ae01ad0e5b3105de4d535973",
     2697400, "649ed97addf97f126a05e12d43325720a624ea19"),
]

def digest(p):
    d = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1024*1024), b""):
            d.update(b)
    return d.hexdigest()

def getblob(raw):
    return hashlib.sha1(("blob " + str(len(raw)) + "\0").encode() + raw).hexdigest()

def probe(p):
    return json.loads(subprocess.check_output(["ffprobe","-v","error","-show_entries",
        "stream=index,codec_type,codec_name,nb_frames,width,height,r_frame_rate:format=duration",
        "-of","json",str(p)],text=True))

def packet_signature(p):
    data=json.loads(subprocess.check_output(["ffprobe","-v","error","-select_streams","a:0",
        "-show_packets","-show_entries","packet=pts_time,duration_time,data_hash",
        "-show_data_hash","sha256","-of","json",str(p)],text=True))
    return [(x.get("pts_time"),x.get("duration_time"),x.get("data_hash"))
            for x in data["packets"]]

def new02_mask():
    profile=json.loads((ROOT/"production/environment_dynamic/shot_profiles/NEW02_M01_M03_TEST_V001.json").read_text())
    assert profile["source_identity"]["sha256"]==SHOTS[0][4]
    m=np.zeros((H,W),dtype=np.float32)
    a=np.zeros((H,W),dtype=bool)
    for spot in profile["candlelight"]["anchors"]:
        x0,x1,y0,y1=spot["roi"]
        xa,xb=int(x0*W),int(np.ceil(x1*W))
        ya,yb=int(y0*H),int(np.ceil(y1*H))
        assert 0<=xa<xb<=W and 0<=ya<yb<int(.40*H)
        yy,xx=np.ogrid[ya:yb,xa:xb]
        cx,cy=spot["center"]; sx,sy=spot["radius"]
        local=np.exp(-.5*((((xx+.5)/W-cx)/sx)**2+(((yy+.5)/H-cy)/sy)**2)).astype("float32")
        local[local<.003]=0
        m[ya:yb,xa:xb]+=local
        a[ya:yb,xa:xb]|=local>0
    m=np.clip(m,0,1)
    m[m<.003]=0
    assert not np.any((m>0)&~a)
    assert np.count_nonzero(m[int(.4*H):,:])==0
    return m

def n23_mask():
    y,x=np.ogrid[:H,:W]
    left=np.exp(-.5*(((x-231)/99)**2+((y-128)/111)**2))
    left*=np.clip((286-y)/48,0,1)
    upper=np.exp(-.5*(((x-711)/36)**2+((y-123)/55)**2))*np.clip((x-690)/17,0,1)
    lower=np.exp(-.5*(((x-712)/38)**2+((y-433)/60)**2))*np.clip((x-694)/17,0,1)
    m=(left+.64*upper+.60*lower).astype("float32")
    m[m<.003]=0
    return m

def main():
    OUTDIR.mkdir(exist_ok=True)
    assert digest(SOURCE)==BASE_SHA, "V006_SOURCE_SHA_MISMATCH"
    s=probe(SOURCE)
    v=next(x for x in s["streams"] if x["codec_type"]=="video")
    assert (v["width"],v["height"],v["r_frame_rate"],int(v["nb_frames"]))==(W,H,"30/1",FRAMES)
    assert len([x for x in s["streams"] if x["codec_type"]=="audio"])==1
    masks={"NEW02":new02_mask(),"N23":n23_mask()}
    for name,start,end,p,expected,nbytes,blob in SHOTS:
        raw=(ROOT/p).read_bytes()
        assert len(raw)==nbytes and hashlib.sha256(raw).hexdigest()==expected
        assert getblob(raw)==blob and raw[:8]==b"\x89PNG\r\n\x1a\n"
        assert struct.unpack(">II",raw[16:24])==(941,1672)
        assert 0<np.count_nonzero(masks[name])<.2*W*H
        assert start<end
    src=subprocess.Popen(["ffmpeg","-hide_banner","-loglevel","error","-xerror",
        "-i",str(SOURCE),"-map","0:v:0","-f","rawvideo","-pix_fmt","rgb24",
        "-vsync","0","pipe:1"],stdout=subprocess.PIPE)
    enc=subprocess.Popen(["ffmpeg","-hide_banner","-loglevel","error","-y",
        "-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}",
        "-framerate",str(FPS),"-i","pipe:0","-an","-c:v","libx264",
        "-preset","veryfast","-crf","18","-pix_fmt","yuv420p","-r",str(FPS),
        "-movflags","+faststart",str(VIDEO_ONLY)],stdin=subprocess.PIPE)
    count=0
    states={k:{"frames":0,"max_raw_channel_delta":0,"changed_pixels_outside_mask":0,
               "first_boundary_matches":False,"last_boundary_matches":False}
            for k in masks}
    rgb_tint=np.array([12,7,1.7],dtype=np.float32)
    try:
        for i in range(FRAMES):
            raw=src.stdout.read(W*H*3)
            assert len(raw)==W*H*3, f"SHORT_DECODE_FRAME_{i}"
            matched=[x for x in SHOTS if x[1]<=i<x[2]]
            assert len(matched)<=1
            if matched:
                name,start,end,*_=matched[0]
                n=end-start; k=i-start; t=k/FPS
                envelope=math.sin(math.pi*k/(n-1))**1.2
                signal=(.50*math.sin(2*math.pi*.94*t)
                        +.32*math.sin(2*math.pi*2.07*t+.64)
                        +.18*math.sin(2*math.pi*3.06*t+1.4))
                original=np.frombuffer(raw,dtype=np.uint8).reshape(H,W,3)
                delta=(envelope*signal)*masks[name][:,:,None]*rgb_tint[None,None,:]
                edited=np.clip(original.astype("float32")+delta,0,255).astype(np.uint8)
                diff=np.any(edited!=original,axis=2)
                state=states[name]
                state["frames"]+=1
                state["max_raw_channel_delta"]=max(state["max_raw_channel_delta"],
                    int(np.abs(edited.astype(np.int16)-original.astype(np.int16)).max()))
                state["changed_pixels_outside_mask"]=max(state["changed_pixels_outside_mask"],
                    int(np.count_nonzero(diff&(masks[name]==0))))
                if k==0: state["first_boundary_matches"]=bool(np.array_equal(edited,original))
                if k==n-1:state["last_boundary_matches"]=bool(np.array_equal(edited,original))
                raw=edited.tobytes()
            enc.stdin.write(raw)
            count+=1
    finally:
        src.stdout.close()
        enc.stdin.close()
    assert src.wait()==0 and enc.wait()==0, "SOURCE_DECODE_OR_VIDEO_ENCODE_ERROR"
    assert count==FRAMES
    for name,start,end,*_ in SHOTS:
        x=states[name]
        assert x["frames"]==end-start and 0<x["max_raw_channel_delta"]<=12
        assert x["changed_pixels_outside_mask"]==0
        assert x["first_boundary_matches"] and x["last_boundary_matches"]
    subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y",
        "-i",str(VIDEO_ONLY),"-i",str(SOURCE),"-map","0:v:0","-map","1:a:0",
        "-c:v","copy","-c:a","copy","-copyts","-start_at_zero",
        "-movflags","+faststart",str(OUTPUT)],check=True)
    p=probe(OUTPUT)
    vv=next(x for x in p["streams"] if x["codec_type"]=="video")
    assert (vv["width"],vv["height"],vv["r_frame_rate"],int(vv["nb_frames"]))==(W,H,"30/1",FRAMES)
    assert len([x for x in p["streams"] if x["codec_type"]=="audio"])==1
    for stream in ("v:0","a:0"):
        subprocess.run(["ffmpeg","-hide_banner","-v","error","-xerror","-i",str(OUTPUT),
                        "-map","0:"+stream,"-f","null","-"],check=True)
    a_before=packet_signature(SOURCE);a_after=packet_signature(OUTPUT)
    assert len(a_before)==3013 and a_before==a_after,"AAC_PACKET_EXACT_FAILED"
    assert digest(SOURCE)==BASE_SHA,"V006_SOURCE_CHANGED"
    for name,start,end,path,expected,_,_ in SHOTS:
        assert digest(ROOT/path)==expected,"APPROVED_PNG_CHANGED"
    result={"task_id":"S02B_V006_M01_FULL_INTEGRATION_REVIEW_01",
      "gate":"TECHNICAL_PASS_REVIEW_ONLY_PO_PENDING","source_video_sha256":BASE_SHA,
      "source_kind":"RECONSTRUCTED_ROUGH_REVIEW_NOT_EXACT_V005",
      "output_filename":OUTPUT.name,"output_sha256":digest(OUTPUT),
      "output_bytes":OUTPUT.stat().st_size,"frames":FRAMES,"fps":FPS,
      "width":W,"height":H,"duration_container_seconds":float(p["format"]["duration"]),
      "source_audio":"UNMODIFIED_S02B_V006_APPROVED_V001_AAC_PACKET_STREAM_COPY",
      "audio_packet_count":len(a_after),"audio_packet_hash_and_pts_duration_match":True,
      "segments":{"NEW02":[1299,1366],"N23":[1366,1448]},"m01_only":True,
      "m02_m03_m04_m05_disabled":True,"input_pngs_unchanged":True,
      "input_video_unchanged":True,"official_video_index_unchanged":True,
      "unmodified_spans_written_from_source_decoded_frames":True,
      "note":"Output video reencoded once: decoded non-target input frames fed unchanged to encoder, but H264 compression need not be pixel/byte identical.",
      "states":states,"canonical_publication":False,"main_merge":False,
      "po_full_video_approval":False}
    REPORT.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
    print("S02B_V006_M01_FULL_REVIEW_PASS",json.dumps(result,ensure_ascii=False),flush=True)
    VIDEO_ONLY.unlink(missing_ok=True)

if __name__=="__main__":
    main()
