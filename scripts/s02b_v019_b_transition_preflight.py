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
      "output_class":"NONCANONICAL_REVIEW_ONLY"
    }
    (OUT/"CUT_PREFLIGHT_REPORT_V001.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
    print("COMPLETE",sheet,flush=True)
if __name__ == "__main__":
    main()
