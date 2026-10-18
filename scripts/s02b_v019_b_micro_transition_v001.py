#!/usr/bin/env python3
"""Noncanonical V019-B cut-ease visual A/B. Reuses PO-approved reordering unchanged.
Source B frames are untouched except for explicitly listed 4-frame windows.
No human reenactment, no AI generation, no time stretch; audio AAC copied.
"""
from pathlib import Path
import hashlib, json, subprocess
from PIL import Image, ImageDraw
ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/"production/video_candidates/review/v019_b_transition_preflight_v001"
SRC=DIR/"B_VISUAL_RELATION_REORDER_CONTEXT_REVIEW.mp4"
OUT=DIR/"B2_MICRO_DISSOLVE_4FRAME_CONTEXT_REVIEW.mp4"
AB=DIR/"AB_B_APPROVED_ORDER_VS_B2_TRANSITION_EASE.mp4"
CONTACT=DIR/"B2_TRANSITION_BEFORE_AFTER_FRAMES.jpg"
REPORT=DIR/"B2_MICRO_TRANSITION_QC.json"
W,H,FPS,N=720,1280,30,334
FRAME_BYTES=W*H*3
# Relative zero-indexed cuts in the approved ordering N21 -> NEW02 -> N22 -> N23
# Preserve strong eyeline-motivated N22 -> N23 hard cut at frame 252.
TARGET_CUTS=(108,175)
def cmd(*args):
    p=subprocess.run([str(a) for a in args],check=True,capture_output=True)
    return p.stdout
def packet_hash(p):
    return hashlib.sha256(cmd("ffmpeg","-v","error","-i",p,"-map","0:a:0",
                   "-c:a","copy","-f","adts","pipe:1")).hexdigest()
def frames(p):
    return int(json.loads(cmd("ffprobe","-v","error","-count_frames",
        "-select_streams","v:0","-show_entries","stream=nb_read_frames",
        "-of","json",p))["streams"][0]["nb_read_frames"])
def blend_rgb(a,b,alpha):
    return Image.blend(Image.frombytes("RGB",(W,H),a),
                       Image.frombytes("RGB",(W,H),b),alpha).tobytes()
def main():
    assert SRC.exists(), "Missing previously archived approved-order B review"
    assert frames(SRC)==N, "Original B does not have exactly 334 frames"
    src_sha=hashlib.file_digest(open(SRC,"rb"),"sha256").hexdigest()
    reader=subprocess.Popen(["ffmpeg","-v","error","-i",str(SRC),
        "-map","0:v:0","-f","rawvideo","-pix_fmt","rgb24","pipe:1"],
        stdout=subprocess.PIPE)
    writer=subprocess.Popen(["ffmpeg","-v","error","-y",
        "-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}",
        "-r",str(FPS),"-i","pipe:0","-i",str(SRC),
        "-map","0:v:0","-map","1:a:0","-c:v","libx264",
        "-preset","veryfast","-crf","19","-pix_fmt","yuv420p",
        "-c:a","copy","-movflags","+faststart",str(OUT)],
        stdin=subprocess.PIPE)
    def readexact(count):
        bb=bytearray()
        while len(bb)<count:
            add=reader.stdout.read(count-len(bb))
            if not add: raise RuntimeError("Incomplete raw input at "+str(len(bb)))
            bb.extend(add)
        return bytes(bb)
    cut_starts={c-2:c for c in TARGET_CUTS}
    i=0
    preview=[]
    try:
        while i<N:
            if i in cut_starts:
                c=cut_starts[i]
                a,b,d,e=[readexact(FRAME_BYTES) for _ in range(4)]
                raw=[a,b,d,e]
                # Deliberately subtle 100-130ms mix:
                # most information in each frame remains from its own original shot.
                edited=[
                    blend_rgb(a,d,0.08),blend_rgb(b,e,0.20),
                    blend_rgb(b,d,0.80),blend_rgb(a,e,0.92)]
                for rawframe,newframe in zip(raw,edited):
                    preview.append((i,rawframe,newframe))
                    writer.stdin.write(newframe)
                    i+=1
            else:
                writer.stdin.write(readexact(FRAME_BYTES))
                i+=1
        writer.stdin.close()
        assert reader.wait()==0, "Failed video decode"
        assert writer.wait()==0, "Failed video encode"
    finally:
        if reader.poll() is None:reader.kill()
        if writer.poll() is None:writer.kill()
    assert frames(OUT)==N, f"B2 wrong frames: {frames(OUT)}"
    audio_src=packet_hash(SRC)
    audio_out=packet_hash(OUT)
    assert audio_src==audio_out, "AAC packet hash mismatch"
    # Human-reviewable two-up: same full B edit vs only 4-frame window changes.
    cmd("ffmpeg","-v","error","-y","-i",SRC,"-i",OUT,
        "-filter_complex","[0:v]scale=540:960[a];[1:v]scale=540:960[b];[a][b]hstack=inputs=2[v]",
        "-map","[v]","-map","0:a:0","-c:v","libx264","-preset","veryfast",
        "-crf","23","-pix_fmt","yuv420p","-c:a","copy","-movflags","+faststart",AB)
    assert frames(AB)==N
    assert packet_hash(AB)==audio_src
    # show only original and blended frames within each altered window
    canvas=Image.new("RGB",(4*240,4*456),(17,17,17))
    d=ImageDraw.Draw(canvas)
    for k,(f_idx,orig,new) in enumerate(preview):
        group=k//4
        offset=k%4
        for row,raw in enumerate((orig,new)):
            im=Image.frombytes("RGB",(W,H),raw).resize((240,427))
            x=offset*240;y=(group*2+row)*456+22
            canvas.paste(im,(x,y))
            d.text((x+4,y-18),f"cut {TARGET_CUTS[group]}  f{f_idx} {'B' if row==0 else 'B2'}",fill="white")
    canvas.save(CONTACT,quality=85)
    report={
      "status":"REVIEW_CANDIDATE_TECHNICAL_PASS_PENDING_PO",
      "approved_reorder_preserved": ["N21","NEW02","N22","N23"],
      "source_B_sha256":src_sha,
      "source_B2_sha256":hashlib.file_digest(open(OUT,"rb"),"sha256").hexdigest(),
      "frame_count":N,
      "cut_frames":{"N21_NEW02":108,"NEW02_N22":175,"N22_N23":252},
      "edited_windows":[[106,109],[173,176]],
      "N22_N23_hard_cut":"PRESERVED",
      "source_AAC_packet_sha256":audio_src,
      "B2_AAC_packet_sha256":audio_out,
      "AB_AAC_packet_sha256":packet_hash(AB),
      "aesthetic_status":"PENDING_ACTUAL_VISUAL_REVIEW",
      "risk":"Short dissolves may create double-exposure/ghosting; no assertion of artistic PASS.",
      "source_V018":"6897b1ac246e4c30d84aca3b80003a58d7bae86eb7631272fe28253b23a01427",
      "visual_B_approved_scope":"REORDER_ONLY",
      "canonical_or_main_change":False,
      "new_AIG_video":False
    }
    REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps(report,indent=2,ensure_ascii=False),flush=True)
if __name__=="__main__":main()
