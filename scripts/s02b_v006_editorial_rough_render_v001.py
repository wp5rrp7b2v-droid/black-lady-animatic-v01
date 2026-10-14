#!/usr/bin/env python3
"""S02-B V006 independent noncanonical preview render; no media or registry mutation."""
import hashlib
import json
import os
import pathlib
import struct
import subprocess
import sys
from PIL import Image, ImageEnhance

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / "_v006_rough_work"
STORY_INDEX = ROOT / "production/story_shots/story_shot_index.jsonl"
EDL = ROOT / "production/editorial_specs/S02_B_V006_CINEMATIC_ROUGH_EDL_V001.json"
OUTPUT = WORK / "S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_REVIEW_V001.mp4"
W, H, FPS = 720, 1280, 30
NEW1 = "S02B_V006_NING_WARNING_JUN_SHOULDER_OTS_TEST_01"
NEW2 = "S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01"

APPROVED_STAGING = {
    "JUN_APPROVED_REACTION": {
        "path": "staging/story_shot_candidates/S02B_JUN_ACKNOWLEDGEMENT_TEST_01/城堡烛光下的专注侧颜.png",
        "sha256": "1af236000b271d327278e82bf3e744fee08bd49682966eb5fa75f731a67c46e7",
        "size": 2015907,
        "blob": "1236d88ca8f3e57e23a2372a17b2eae11a33559b",
        "width":941,"height":1672,
    },
    "NING_REACTION_APPROVED": {
        "path": "staging/story_shot_candidates/TAIL_NING_REACTION_TEST_01/TAIL_NING_REACTION_TEST_01_CANDIDATE_01_PO_APPROVED.png",
        "sha256": "cbac98a82763c6c930a3c820c917f4b9b8bc2ed300a49b48143b8b1cd9486c9c",
        "size": 2471479,
        "blob": "907c4cdbd875d67399258dceb29eedd9f8038946",
        "width":941,"height":1672,
    },
    "A06": {
        "path": "production/image_library/approved/A_Series/A06_REBOOT_approved_v001.png",
        "sha256": "fdfa27c14f09425c04785808ecd7432aca7c1d29870a8a5f33cba9a38b62e827",
        "size": 3139664,
        "blob": "1023a67d96a8820def1259e3b0568c259ee55433",
        "width":941,"height":1672,
    },
}

SOURCE_FILES = {
    "v004": WORK / "S02B_N16_N17_V004_QUALITY_TEST.mp4",
    "audio": WORK / "S02_B_DIRECTOR_REVIEW_V001.mp4"
}
SOURCE_SHAS = {
    "v004": "7f30596a60ada54a8393f8207ad7f59f92702ca8278d0bd257fc258911877018",
    "audio": "8ec47720b5641412b2ebd1e082bf058244d6b07fbe97500b56a8ef830bf2042a"
}
# No zero-keyframe blending, no universal scale pulses; only few motivated restrained micro reframings.
MOVES = {
    "N18":(1.022,1.014,0.53,0.50,0.50,0.50),
    "N19":(1.012,1.020,0.50,0.50,0.50,0.50),
    "N20_FIRST":(1.014,1.014,0.51,0.50,0.50,0.50),
    "N21":(1.015,1.015,0.50,0.50,0.50,0.50),
    "N22_FIRST":(1.010,1.010,0.50,0.50,0.50,0.50),
    "N23":(1.010,1.010,0.50,0.50,0.50,0.50),
    "N24":(1.025,1.025,0.53,0.53,0.5,0.5),
}

def sha(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""):
            h.update(b)
    return h.hexdigest()

def blob(path):
    return subprocess.check_output(["git","hash-object",str(path)],cwd=ROOT,text=True).strip()

def probe(path):
    r=subprocess.run(["ffprobe","-v","error","-show_entries","format=duration,size:stream=codec_type,codec_name,nb_frames,width,height,r_frame_rate","-of","json",str(path)],capture_output=True,text=True,check=True)
    return json.loads(r.stdout)

def check_image(path, expected):
    if not path.is_file():raise ValueError(f"MISSING_SOURCE:{path}")
    raw_head=path.open("rb").read(24)
    assert raw_head[:8]==bytes((137,80,78,71,13,10,26,10))
    width,height=struct.unpack(">II",raw_head[16:24])
    actual={"path":str(path.relative_to(ROOT)),"sha256":sha(path),"size":path.stat().st_size,
            "blob":blob(path),"width":width,"height":height}
    for k in ["sha256","size","blob","width","height"]:
        if expected.get(k) is not None and actual[k]!=expected[k]:
            raise ValueError(f"IMAGE_IDENTITY_MISMATCH {path}: {k} expected={expected[k]} actual={actual[k]}")
    return actual

def crop_frame(img, fraction, params):
    # Image source stays untouched; only temporary decoded preview canvas is reframed.
    z0,z1,cx0,cx1,cy0,cy1=params
    z=z0+(z1-z0)*fraction
    cx=cx0+(cx1-cx0)*fraction
    cy=cy0+(cy1-cy0)*fraction
    sw,sh=img.size
    aspect=W/H
    cw=min(sw,sh*aspect)/z
    ch=cw/aspect
    left=max(0,min(sw-cw,cx*sw-cw/2))
    top=max(0,min(sh-ch,cy*sh-ch/2))
    # Pillow crop uses float boxes; copied temporary video frames only.
    return img.crop((left,top,left+cw,top+ch)).resize((W,H), Image.Resampling.LANCZOS)

def main():
    edl=json.loads(EDL.read_text(encoding="utf-8"))
    assert edl["format"]["fps_num"]==30 and edl["format"]["width"]==720 and edl["format"]["height"]==1280
    assert edl["format"]["video_frames"]==1927
    segments=edl["timeline"]
    assert segments[0]["start_frame"]==0 and segments[-1]["end_frame_exclusive"]==1927
    assert len(segments)==17
    for a,b in zip(segments,segments[1:]):
        assert a["end_frame_exclusive"]==b["start_frame"],"NONCONTIGUOUS_TIMELINE"
    assert sum(x["duration_frames"] for x in segments)==1927
    assert segments[0]["source_shot_id"]=="N16" and segments[2]["end_frame_exclusive"]==658
    assert [x for x in segments if x["id"]=="V006_NEW_01"][0]["source_shot_id"]==NEW1
    assert [x for x in segments if x["id"]=="V006_NEW_02"][0]["source_shot_id"]==NEW2
    WORK.mkdir(exist_ok=True)
    for key,path in SOURCE_FILES.items():
        assert path.is_file(),f"MISSING_EXTERNAL_ARTIFACT:{path}"
        assert sha(path)==SOURCE_SHAS[key],f"HISTORICAL_ARTIFACT_HASH_MISMATCH:{key}"
    p=probe(SOURCE_FILES["v004"])
    v=[s for s in p["streams"] if s["codec_type"]=="video"][0]
    assert int(v["nb_frames"])==658 and (v["width"],v["height"])==(720,1280)
    assert v["r_frame_rate"]=="30/1"
    pa=probe(SOURCE_FILES["audio"])
    audio=[s for s in pa["streams"] if s["codec_type"]=="audio"]
    assert len(audio)==1 and audio[0]["codec_name"]=="aac"
    assert float(pa["format"]["duration"])>=64.25

    rowmap={x["shot_id"]:x for x in map(json.loads,STORY_INDEX.read_text(encoding="utf-8").splitlines())}
    shots={}
    verified=[]
    for seg in segments[3:]:
        sid=seg["source_shot_id"]
        if seg["id"] in APPROVED_STAGING or sid=="A06":
            key=seg["id"] if seg["id"] in APPROVED_STAGING else "A06"
            ident=APPROVED_STAGING[key];path=ROOT/ident["path"]
        elif sid in rowmap:
            rec=rowmap[sid]
            assert rec["approval_status"]=="APPROVED" and rec["lifecycle"]=="CURRENT"
            path=ROOT/rec["canonical_path"]
            ident={"sha256":rec["sha256_locked_identity"],"blob":rec["github_blob_sha"],"size":rec["byte_size"],
                   "width":rec["dimensions"]["width"],"height":rec["dimensions"]["height"]}
        else:raise ValueError(f"UNRESOLVED_STORY_IMAGE:{seg['id']}:{sid}")
        if str(path) not in shots:
            verified.append(check_image(path,ident))
        shots[seg["id"]]=path

    video_only=WORK/"S02_B_V006_CINEMATIC_ROUGH_VIDEO_ONLY_V001.mp4"
    cmd=["ffmpeg","-hide_banner","-loglevel","error","-y",
         "-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-framerate",str(FPS),"-i","pipe:0",
         "-an","-c:v","libx264","-preset","veryfast","-crf","18","-pix_fmt","yuv420p",
         "-r",str(FPS),"-movflags","+faststart",str(video_only)]
    encoder=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    decoded=subprocess.Popen(["ffmpeg","-hide_banner","-loglevel","error","-i",str(SOURCE_FILES["v004"]),
          "-map","0:v:0","-f","rawvideo","-pix_fmt","rgb24","-vsync","0","pipe:1"],stdout=subprocess.PIPE)
    framebytes=W*H*3
    count=0
    try:
        for i in range(658):
            data=decoded.stdout.read(framebytes)
            if len(data)!=framebytes: raise RuntimeError(f"LOCKED_V004_FRAME_SHORT:{i}:{len(data)}")
            encoder.stdin.write(data);count+=1
        decoded.stdout.close()
        if decoded.wait()!=0: raise RuntimeError("LOCKED_V004_DECODE_FAILED")
        print("LOCKED_V004_DECODED_FRAMES=658",flush=True)
        for seg in segments[3:]:
            dur=seg["duration_frames"]
            src=Image.open(shots[seg["id"]]).convert("RGB")
            move=MOVES.get(seg["id"],(1.0,1.0,0.5,0.5,0.5,0.5))
            if move[0]==move[1] and move[2]==move[3] and move[4]==move[5]:
                frame=crop_frame(src,0,move).tobytes()
                for i in range(dur):encoder.stdin.write(frame)
            else:
                for i in range(dur):
                    frame=crop_frame(src,i/max(dur-1,1),move).tobytes()
                    encoder.stdin.write(frame)
            count+=dur
            print(f"SEGMENT={seg['id']} FRAMES={dur} ABS_END={count}",flush=True)
    finally:
        encoder.stdin.close()
    rc=encoder.wait()
    assert rc==0, f"VIDEO_ENCODE_FAILED:{rc}"
    assert count==1927, f"OUTPUT_FRAMES_INVALID:{count}"
    outprobe=probe(video_only);v=[x for x in outprobe["streams"] if x["codec_type"]=="video"][0]
    assert int(v["nb_frames"])==1927
    # Remux the EXACT approved V001 AAC packets as a continuous unedited source stream.
    mux=["ffmpeg","-hide_banner","-loglevel","error","-y","-i",str(video_only),
         "-i",str(SOURCE_FILES["audio"]),"-map","0:v:0","-map","1:a:0",
         "-c:v","copy","-c:a","copy","-copyts","-start_at_zero","-movflags","+faststart",str(OUTPUT)]
    subprocess.run(mux,check=True)
    final=probe(OUTPUT);outv=[s for s in final["streams"] if s["codec_type"]=="video"][0]
    outa=[s for s in final["streams"] if s["codec_type"]=="audio"][0]
    assert outv["nb_frames"]=="1927" and outa["codec_name"]=="aac"
    subprocess.run(["ffmpeg","-v","error","-xerror","-i",str(OUTPUT),"-map","0:v:0","-f","null","-"],check=True)
    subprocess.run(["ffmpeg","-v","error","-xerror","-i",str(OUTPUT),"-map","0:a:0","-f","null","-"],check=True)
    manifest={
        "status":"REVIEW_ONLY_NONCANONICAL_NOT_PO_APPROVED",
        "version":"S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_REVIEW_V001",
        "provenance_limit":"V005 REVIEW MP4 SOURCE SHA ffd811... IS NOT AVAILABLE; this is a reconstructed rough cut from verified V004 first 658 frames, exact approved PNGs and approved V001 continuous AAC. DO NOT CLAIM BYTE-EXACT OR PIXEL-EXACT V005 CONTINUITY.",
        "v005_reference_not_available":edl["parent_video_sha256"],
        "first_658_frames":"decoded from PO-approved V004 segment; H264 review derivative has one recompression but no changes to source",
        "source_v004":{"sha256":SOURCE_SHAS["v004"],"artifact_id":11748263727,"frames":658},
        "approved_source_audio":{"sha256":SOURCE_SHAS["audio"],"artifact_id":11600040686,"audio_policy":"AAC STREAM_COPY_FROM_APPROVED_S02B_V001; NO CUT/MIX/RETIME"},
        "output":{"path":str(OUTPUT.relative_to(ROOT)),"sha256":sha(OUTPUT),"byte_size":OUTPUT.stat().st_size,"probe":final},
        "verified_source_images":verified,
        "node_count":len(segments),"frames":1927,"fps":30,"width":720,"height":1280,
        "approval":"CANDIDATE_ROUGH_REVIEW_ONLY; MUST RECEIVE PO VIDEO REVIEW; NO_CANONICAL_PUBLICATION",
        "edl_status_override":"two missing shots now APPROVED/CURRENT in registry; this renderer resolves them by exact shot_id",
        "preserved_assets":True,"video_index_mutated":False,"main_merged":False
    }
    (WORK/"RENDER_MANIFEST.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("V006_RECONSTRUCTED_ROUGH_RENDER_SUCCESS",json.dumps({"sha256":manifest["output"]["sha256"],"size":manifest["output"]["byte_size"],"frames":1927,"audio":"V001_AAC_STREAM_COPY","source_pngs":len(verified)},ensure_ascii=False),flush=True)

if __name__=="__main__":
    main()
