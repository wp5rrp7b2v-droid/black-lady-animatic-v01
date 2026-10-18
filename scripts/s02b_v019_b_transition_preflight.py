#!/usr/bin/env python3
"""Read-only V018 camera-cut preflight for S02-B V019-B exploration.
No frame synthesis, image warp, audio retime, canonical mutation, or AI generation.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
from PIL import Image, ImageDraw, ImageOps, ImageStat

REPO = Path(__file__).resolve().parents[1]
SRC = REPO / "production/environment_dynamic/review_candidates/S02_B_M01_V018_FULL_LENGTH_C_VISIBLE_REVIEW/S02_B_M01_V018_FULL_LENGTH_MORE_VISIBLE_C_GROUP_PREVIEW_V001.mp4"
EXPECTED_SHA = "6897b1ac246e4c30d84aca3b80003a58d7bae86eb7631272fe28253b23a01427"
OUT = REPO / "production/video_candidates/review/v019_b_transition_preflight_v001"
CUTS = [
    ("N21_TO_N22", 1222),
    ("N22_TO_NEW02", 1299),
    ("NEW02_TO_N23", 1366),
]
FPS = 30
def run(*args):
    print("RUN:", " ".join(str(a) for a in args), flush=True)
    return subprocess.run([str(a) for a in args], check=True, text=True, capture_output=True)
def main():
    OUT.mkdir(parents=True, exist_ok=True)
    h = hashlib.file_digest(open(SRC, "rb"), "sha256").hexdigest()
    assert h == EXPECTED_SHA, f"Input V018 SHA mismatch: {h}"
    probe = json.loads(run("ffprobe", "-v", "error", "-show_entries",
        "stream=codec_type,nb_frames,r_frame_rate,width,height:format=duration",
        "-of", "json", SRC).stdout)
    video = next(s for s in probe["streams"] if s["codec_type"] == "video")
    assert video["r_frame_rate"] == "30/1", video
    assert video["width"] == 720 and video["height"] == 1280
    assert int(video["nb_frames"]) == 1927, video
    chosen = [x for _, cut in CUTS for x in (cut-1, cut)]
    expression = "+".join(f"eq(n\\,{x})" for x in chosen)
    run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", SRC, "-vf", "select=" + expression + ",scale=360:640:flags=lanczos",
        "-fps_mode", "vfr", "-q:v", "3", OUT / "frame_%02d.jpg")
    frames = [OUT / f"frame_{i:02d}.jpg" for i in range(1,7)]
    assert all(f.exists() for f in frames), frames
    font_color = "#FFFFFF"
    canvas = Image.new("RGB", (3*360, 2*680), "#171717")
    draw = ImageDraw.Draw(canvas)
    checks = []
    for i, ((name, cut), f1, f2) in enumerate(zip(CUTS, frames[::2], frames[1::2])):
        pair = []
        for j, path in enumerate([f1, f2]):
            im = Image.open(path).convert("RGB")
            lum = ImageStat.Stat(im.convert("L")).mean[0]
            darkedge = ImageStat.Stat(im.convert("L").crop((0,0,45,640))).mean[0]
            rightedge = ImageStat.Stat(im.convert("L").crop((315,0,360,640))).mean[0]
            x = i*360
            y = j*680+24
            canvas.paste(im, (x,y))
            draw.text((x+8, j*680+4), f"{name} | {'BEFORE' if j == 0 else 'AFTER'} | #{cut-1+j}", fill=font_color)
            pair.append({"frame": cut-1+j, "mean_luminance": round(lum,2),
                         "left_edge_luminance": round(darkedge,2),
                         "right_edge_luminance": round(rightedge,2)})
        checks.append({"cut":name, "cut_frame":cut,"time_seconds":cut/30, "adjacent_frames": pair})
    sheet = OUT / "CUT_CONTACT_SHEET_V001.jpg"
    canvas.save(sheet, quality=87, optimize=True)
    # Source-equivalent contextual sample: frames 1174..1483 are not re-timed;
    # a review extraction only, never a new canonical sequence.
    run("ffmpeg", "-hide_banner","-loglevel","error","-y",
        "-ss", f"{1114/FPS:.6f}", "-i", SRC,
        "-t", f"{(1448-1114)/FPS:.6f}",
        "-map","0:v:0","-map","0:a:0","-c:v","libx264","-preset","veryfast",
        "-crf","22","-pix_fmt","yuv420p","-c:a","copy","-movflags","+faststart",
        OUT / "A_V018_ORIGINAL_4_SHOT_CONTEXT_REVIEW.mp4")
    # Non-destructive editorial alternative B: use only original V018 frames.
    # Re-order NEW02 and N22 without constructing intermediate human motion.
    a_path = OUT / "A_V018_ORIGINAL_4_SHOT_CONTEXT_REVIEW.mp4"
    b_silent = OUT / "B_REORDER_NO_AUDIO_INTERMEDIATE.mp4"
    b_path = OUT / "B_VISUAL_RELATION_REORDER_CONTEXT_REVIEW.mp4"
    ab_path = OUT / "AB_A_ORIGINAL_B_REORDER_SIDE_BY_SIDE.mp4"
    parts = [("N21",1114,1222), ("NEW02",1299,1366),
             ("N22",1222,1299), ("N23",1366,1448)]
    filt = "[0:v]split=4[t0][t1][t2][t3];" + ";".join(
        f"[t{i}]trim=start_frame={a}:end_frame={b},setpts=PTS-STARTPTS[p{i}]"
        for i, (_name,a,b) in enumerate(parts)
    ) + ";[p0][p1][p2][p3]concat=n=4:v=1:a=0[outv]"
    run("ffmpeg","-hide_banner","-loglevel","error","-y","-i",SRC,
        "-filter_complex",filt,"-map","[outv]","-an",
        "-c:v","libx264","-preset","veryfast","-crf","22",
        "-pix_fmt","yuv420p","-movflags","+faststart",b_silent)
    run("ffmpeg","-hide_banner","-loglevel","error","-y",
        "-i",b_silent,"-i",a_path,"-map","0:v:0","-map","1:a:0",
        "-c:v","copy","-c:a","copy","-movflags","+faststart",b_path)
    def decoded_frames(p):
        info=json.loads(run("ffprobe","-v","error","-count_frames",
            "-select_streams","v:0","-show_entries","stream=nb_read_frames",
            "-of","json",p).stdout)
        return int(info["streams"][0]["nb_read_frames"])
    frame_total=sum(b-a for _,a,b in parts)
    a_frames=decoded_frames(a_path)
    b_frames=decoded_frames(b_path)
    assert a_frames==frame_total==b_frames, (
        "Frame mismatch",a_frames,b_frames,frame_total)
    # Both review movies copy the same AAC packets from the exact A source.
    def aac_stream_hash(p):
        aac=run("ffmpeg","-hide_banner","-loglevel","error",
            "-i",p,"-map","0:a:0","-c:a","copy","-f","adts","-").stdout
        # Python text capture is inappropriate for raw ADTS: use a file instead.
    audio_hashes=[]
    for label,path in [("A",a_path),("B",b_path)]:
        audio_file=OUT / f"{label}_REVIEW_AUDIO_COPY.aac"
        run("ffmpeg","-hide_banner","-loglevel","error","-y","-i",path,
            "-map","0:a:0","-c:a","copy","-f","adts",audio_file)
        with open(audio_file,"rb") as fp:
            audio_hashes.append(hashlib.file_digest(fp,"sha256").hexdigest())
        audio_file.unlink()
    assert audio_hashes[0]==audio_hashes[1], "A/B encoded AAC packets not identical"
    run("ffmpeg","-hide_banner","-loglevel","error","-y",
        "-i",a_path,"-i",b_path,"-filter_complex",
        "[0:v][1:v]hstack=inputs=2[outv]",
        "-map","[outv]","-map","0:a:0",
        "-c:v","libx264","-preset","veryfast","-crf","24",
        "-pix_fmt","yuv420p","-c:a","copy","-movflags","+faststart",ab_path)
    b_silent.unlink()
    summary = {
      "source":"V018 exact visual-approved clip","source_sha256":h,
      "status":"CUT_CANDIDATE_PREFLIGHT_ONLY_NOT_VIDEO_APPROVED",
      "no_paid_video_ai": True,"no_original_approved_binaries_changed":True,
      "fps":FPS,"expected_total_frames":1927,
      "review_span_frames":[1114,1448],"review_span_seconds":[round(1114/30,6),round(1448/30,6)],
      "cuts":checks,
      "interpretation":"Numerical edge/luma readings do not prove spatial/eyeline/movement continuity. Judge actual images before any B/C treatment.",
      "next_gate":"Select one cut after image review; design B hard cut timing/visual relationship. Try C only if visible real foreground cover exists; no synthetic wipe.",
      "audio_policy":"Original V018 AAC copied as-is into context excerpt; no time stretching or remixing.",
      "output_class":"NONCANONICAL_REVIEW_ONLY",
      "ab_test":{"A_sequence":["N21","N22","NEW02","N23"],"B_sequence":["N21","NEW02","N22","N23"],"frames_each":frame_total,"audio_aac_sha256_A_equals_B":audio_hashes[0],"audio_packet_equal":True,"editorial_semantic_status":"PENDING_PO_LISTENING_AND_VISUAL_REVIEW","no_frame_generation":True,"C_occlusion":"NOT_RENDERED_REQUIRES_REAL_MOVING_OCCLUDER_EVIDENCE"}
    }
    (OUT/"CUT_PREFLIGHT_REPORT_V001.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
    print("COMPLETE",sheet,flush=True)
if __name__ == "__main__":
    main()
