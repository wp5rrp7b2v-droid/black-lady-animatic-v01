#!/usr/bin/env python3
"""NEW02 V003: direct N23 approved candle rhythm/intensity transfer, WITHOUT dust.

Uses N23 exact timing and RGB tint in adapted architectural-only candlelight masks.
This is a review-only derived video, never person movement or modified Story Shot.
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
SOURCE = ROOT / "production/image_library/approved/story_shots/S02B_V006_NEW02_CROWD_INTERIOR_SIDE_DEPTH_APPROVED_V001.png"
OUTPUT_DIR = ROOT / "_new02_m01_v003_n23_paced_control"
OUTPUT = OUTPUT_DIR / "NEW02_M01_N23_PACED_CANDLELIGHT_TEST_V003.mp4"
EVIDENCE = OUTPUT_DIR / "NEW02_M01_N23_PACED_CANDLELIGHT_TEST_V003_EVIDENCE.json"
EXPECTED_SHA256 = "d1866a667d7a24b8c5ae5b7670486b8b312e6f4a8fbce457763668e84d843bd4"
EXPECTED_BLOB = "d8feba3692ebe25afd0e51f5e3ab32358ea19ded"
FPS, FRAMES, WIDTH, HEIGHT = 30, 90, 720, 1280

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    raw = SOURCE.read_bytes()
    assert len(raw) == 1963410
    assert sha256(SOURCE) == EXPECTED_SHA256
    assert raw[:8] == bytes((137,80,78,71,13,10,26,10))
    assert struct.unpack(">II", raw[16:24]) == (941, 1672)
    blob = hashlib.sha1(("blob " + str(len(raw)) + "\0").encode("ascii") + raw).hexdigest()
    assert blob == EXPECTED_BLOB
    with Image.open(SOURCE) as source:
        assert source.size == (941,1672)
        original = np.asarray(source.convert("RGB").resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)).copy()

    # Reuse NEW02 approved architectural candle ROI only. Temporal terms, 3-second
    # shape, slow/fine N23 amplitude and RGB tint BELOW are taken verbatim
    # from scripts/n23_candlelight_motion_control_test_v001.py.
    profile = json.loads((ROOT / "production/environment_dynamic/shot_profiles/NEW02_M01_M03_TEST_V001.json").read_text())
    assert profile["source_identity"]["sha256"] == EXPECTED_SHA256
    mask = np.zeros((HEIGHT, WIDTH), dtype=np.float32)
    allowed = np.zeros((HEIGHT, WIDTH), dtype=bool)
    for spot in profile["candlelight"]["anchors"]:
        x0,x1,y0,y1 = spot["roi"]
        xi0,xi1 = int(x0*WIDTH), int(np.ceil(x1*WIDTH))
        yi0,yi1 = int(y0*HEIGHT), int(np.ceil(y1*HEIGHT))
        assert 0 <= xi0 < xi1 <= WIDTH and 0 <= yi0 < yi1 < int(.40*HEIGHT)
        yy,xx=np.ogrid[yi0:yi1,xi0:xi1]
        cx,cy=spot["center"]; sx,sy=spot["radius"]
        local = np.exp(-.5*((((xx+.5)/WIDTH-cx)/sx)**2 + (((yy+.5)/HEIGHT-cy)/sy)**2)).astype("float32")
        local[local < .003] = 0
        mask[yi0:yi1,xi0:xi1] += local
        allowed[yi0:yi1,xi0:xi1] |= local > 0
    mask=np.clip(mask,0,1)
    mask[mask < .003] = 0
    assert np.count_nonzero(mask)>0
    assert int(np.count_nonzero(mask)) < .20 * WIDTH * HEIGHT, "Mask too broad, risk changing people"
    assert np.count_nonzero(mask[int(.4*HEIGHT):,:]) == 0
    assert not np.any((mask > 0) & ~allowed)
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
    first_matches = last_matches = False
    for i in range(FRAMES):
        t = i/FPS
        envelope = math.sin(math.pi*i/(FRAMES-1))**1.2
        signal = (.50*math.sin(2*math.pi*.94*t)
                  +.32*math.sin(2*math.pi*2.07*t+.64)
                  +.18*math.sin(2*math.pi*3.06*t+1.4))
        delta = (envelope*signal)*(mask[:,:,None]*tint[None,None,:])
        frame = np.clip(original.astype("float32")+delta,0,255).astype("uint8")
        if i == 0: first_matches = bool(np.array_equal(frame, original))
        if i == FRAMES-1: last_matches = bool(np.array_equal(frame, original))
        differs = np.any(frame!=original,axis=-1)
        max_changed_outside = max(max_changed_outside,int(np.count_nonzero(differs & (mask==0))))
        max_changed_pixels = max(max_changed_pixels,int(np.count_nonzero(differs)))
        max_raw_diff = max(max_raw_diff,int(np.abs(frame.astype("int16")-original.astype("int16")).max()))
        encoder.stdin.write(frame.tobytes())
    encoder.stdin.close()
    assert encoder.wait()==0,"FFMPEG_ENCODING_FAILURE"
    assert max_changed_outside==0,"PERSON_OR_BACKGROUND_UNAUTHORIZED_PIXEL_CHANGE"
    assert max_raw_diff <= 12,"EXCESSIVE_CANDLELIGHT_INTENSITY_CHANGE"
    assert first_matches and last_matches
    assert max_raw_diff > 0
    assert subprocess.run(["ffmpeg","-v","error","-xerror","-i",str(OUTPUT),"-f","null","-"],check=False).returncode==0
    parsed=json.loads(subprocess.check_output(["ffprobe","-v","error","-show_entries",
       "stream=nb_frames,width,height,r_frame_rate:format=duration","-of","json",str(OUTPUT)],text=True))
    assert int(parsed["streams"][0]["nb_frames"])==FRAMES
    assert int(parsed["streams"][0]["width"])==WIDTH
    assert int(parsed["streams"][0]["height"])==HEIGHT
    report={
       "gate":"NEW02_M01_N23_PACED_CANDLELIGHT_CONTROL_V003",
       "status":"TECHNICAL_PASS_PO_VISUAL_REVIEW_PENDING",
       "source_png":str(SOURCE.relative_to(ROOT)),
       "source_original_sha256":EXPECTED_SHA256,
       "source_git_blob":EXPECTED_BLOB,
       "source_original_bytes":len(raw),
       "source_unmodified":True,
       "render_type":"EXACT_N23_PACED_LOCALIZED_CANDLELIGHT_CONTROL_ONLY",
       "temporal_algorithm_reference":"scripts/n23_candlelight_motion_control_test_v001.py",
       "dust_particles":0,
       "enabled_modules":["M01"],
       "first_last_raw_equal_original":first_matches and last_matches,
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
       "authorized_candle_mask_pixels":int(np.count_nonzero(mask)),
       "video_sha256":sha256(OUTPUT),
       "video_bytes":OUTPUT.stat().st_size,
       "audio":"NONE",
       "canonical_story_shot_changed":False,
       "v006_candidate_changed":False,
       "main_merged":False
    }
    EVIDENCE.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("NEW02_N23_PACED_M01_V003_TECHNICAL_PASS")
    print("SOURCE_EXACT_SHA256=PASS")
    print("RAW_PIXEL_PROTECTION_OUTSIDE_LIGHT_REGION=PASS")
    print("HUMAN_MOTION_IMPLEMENTED=FALSE")
    print("DUST_PARTICLES=0")
    print("CANDIDATE_VIDEO_SHA256="+report["video_sha256"])
    print("CANDIDATE_VIDEO_BYTES="+str(report["video_bytes"]))

if __name__ == "__main__":
    main()
