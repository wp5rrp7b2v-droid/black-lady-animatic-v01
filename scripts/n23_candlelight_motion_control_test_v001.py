#!/usr/bin/env python3
"""Deterministic non-generative N23 original-binary-locked candlelight control pilot.

This IS NOT a character motion video: Neil and the guests remain still.
Only localized candle illumination varies in temporary video frames.
"""
import hashlib
import json
import math
import pathlib
import struct
import subprocess
import sys

import numpy as np
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / "production/image_library/approved/story_shots/N23_NEIL_AT_OPEN_DOOR_APPROVED_V001.png"
OUTPUT_DIR = ROOT / "_n23_candlelight_control"
OUTPUT = OUTPUT_DIR / "N23_CANDLELIGHT_MOTION_CONTROL_TEST_V001.mp4"
EVIDENCE = OUTPUT_DIR / "N23_CANDLELIGHT_MOTION_CONTROL_TEST_V001_EVIDENCE.json"
EXPECTED_SHA256 = "2d94488e36d878ccb6ae7c3f9f3bf2a122eebca5ae01ad0e5b3105de4d535973"
EXPECTED_BLOB = "649ed97addf97f126a05e12d43325720a624ea19"
FPS, FRAMES, WIDTH, HEIGHT = 30, 90, 720, 1280

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    raw = SOURCE.read_bytes()
    assert len(raw) == 2697400
    assert sha256(SOURCE) == EXPECTED_SHA256
    assert raw[:8] == bytes((137,80,78,71,13,10,26,10))
    assert struct.unpack(">II", raw[16:24]) == (941, 1672)
    blob = hashlib.sha1(("blob " + str(len(raw)) + "\0").encode("ascii") + raw).hexdigest()
    assert blob == EXPECTED_BLOB
    with Image.open(SOURCE) as source:
        assert source.size == (941,1672)
        original = np.asarray(source.convert("RGB").resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)).copy()

    y,x = np.ogrid[:HEIGHT,:WIDTH]
    # Soft taper applies candlelight ONLY to approved architectural light areas.
    left = np.exp(-0.5 * (((x-231)/99)**2 + ((y-128)/111)**2))
    left *= np.clip((286-y)/48,0,1)
    upper = np.exp(-0.5 * (((x-711)/36)**2 + ((y-123)/55)**2)) * np.clip((x-690)/17,0,1)
    lower = np.exp(-0.5 * (((x-712)/38)**2 + ((y-433)/60)**2)) * np.clip((x-694)/17,0,1)
    mask = (left + .64*upper + .60*lower).astype("float32")
    mask[mask < .003] = 0
    assert int(np.count_nonzero(mask)) < .20 * WIDTH * HEIGHT, "Mask too broad, risk changing people"
    tint = np.array([12,7,1.7], dtype=np.float32)
    OUTPUT_DIR.mkdir(exist_ok=True)
    cmd=["ffmpeg","-hide_banner","-loglevel","error","-y",
         "-f","rawvideo","-vcodec","rawvideo","-pix_fmt","rgb24",
         "-s",f"{WIDTH}x{HEIGHT}","-r",str(FPS),"-i","pipe:0",
         "-an","-c:v","libx264","-preset","veryfast","-crf","18",
         "-pix_fmt","yuv420p","-movflags","+faststart",str(OUTPUT)]
    encoder = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    max_raw_diff=0
    max_changed_outside=0
    max_changed_pixels=0
    for i in range(FRAMES):
        t = i/FPS
        envelope = math.sin(math.pi*i/(FRAMES-1))**1.2
        signal = (.50*math.sin(2*math.pi*.94*t)
                  +.32*math.sin(2*math.pi*2.07*t+.64)
                  +.18*math.sin(2*math.pi*3.06*t+1.4))
        delta = (envelope*signal)*(mask[:,:,None]*tint[None,None,:])
        frame = np.clip(original.astype("float32")+delta,0,255).astype("uint8")
        differs = np.any(frame!=original,axis=-1)
        max_changed_outside = max(max_changed_outside,int(np.count_nonzero(differs & (mask==0))))
        max_changed_pixels = max(max_changed_pixels,int(np.count_nonzero(differs)))
        max_raw_diff = max(max_raw_diff,int(np.abs(frame.astype("int16")-original.astype("int16")).max()))
        encoder.stdin.write(frame.tobytes())
    encoder.stdin.close()
    assert encoder.wait()==0,"FFMPEG_ENCODING_FAILURE"
    assert max_changed_outside==0,"PERSON_OR_BACKGROUND_UNAUTHORIZED_PIXEL_CHANGE"
    assert max_raw_diff <= 12,"EXCESSIVE_CANDLELIGHT_INTENSITY_CHANGE"
    assert subprocess.run(["ffmpeg","-v","error","-xerror","-i",str(OUTPUT),"-f","null","-"],check=False).returncode==0
    parsed=json.loads(subprocess.check_output(["ffprobe","-v","error","-show_entries",
       "stream=nb_frames,width,height,r_frame_rate:format=duration","-of","json",str(OUTPUT)],text=True))
    assert int(parsed["streams"][0]["nb_frames"])==FRAMES
    assert int(parsed["streams"][0]["width"])==WIDTH
    assert int(parsed["streams"][0]["height"])==HEIGHT
    report={
       "gate":"N23_STAGE_A_CANDLELIGHT_CONTROL_TEST_V001",
       "status":"TECHNICAL_PASS_PO_VISUAL_REVIEW_PENDING",
       "source_png":str(SOURCE.relative_to(ROOT)),
       "source_original_sha256":EXPECTED_SHA256,
       "source_git_blob":EXPECTED_BLOB,
       "source_original_bytes":len(raw),
       "source_unmodified":True,
       "render_type":"LOCALIZED_CANDLELIGHT_CONTROL_ONLY",
       "human_walk":"NOT_IMPLEMENTED",
       "neil_head_or_gaze_motion":"NOT_IMPLEMENTED",
       "camera_motion":"NONE",
       "video_only_reframe_to_720x1280":True,
       "fps":FPS,
       "frames":FRAMES,
       "dimensions":[WIDTH,HEIGHT],
       "duration_seconds":FRAMES/FPS,
       "raw_pixel_max_delta":max_raw_diff,
       "changed_pixels_outside_approved_light_regions":max_changed_outside,
       "max_changed_pixels_per_frame":max_changed_pixels,
       "video_sha256":sha256(OUTPUT),
       "video_bytes":OUTPUT.stat().st_size,
       "audio":"NONE",
       "canonical_story_shot_changed":False,
       "v006_candidate_changed":False,
       "main_merged":False
    }
    EVIDENCE.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("N23_STAGE_A_TECHNICAL_CONTROL=PASS")
    print("SOURCE_EXACT_SHA256=PASS")
    print("RAW_PIXEL_PROTECTION_OUTSIDE_LIGHT_REGION=PASS")
    print("HUMAN_MOTION_IMPLEMENTED=FALSE")
    print("CANDIDATE_VIDEO_SHA256="+report["video_sha256"])
    print("CANDIDATE_VIDEO_BYTES="+str(report["video_bytes"]))

if __name__ == "__main__":
    main()
