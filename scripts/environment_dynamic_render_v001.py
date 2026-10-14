#!/usr/bin/env python3
"""Read-only approved still -> M01 candlelight + M03 sparse dust. Review video ONLY.

Works from independently verified canonical PNG; effects on temporary decoded
video frames, never the PNG file. Does not animate any character or camera.
"""
import argparse
import hashlib
import json
import math
import pathlib
import random
import struct
import subprocess

import numpy as np
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()


def git_blob(raw):
    return hashlib.sha1(("blob " + str(len(raw)) + "\0").encode("ascii") + raw).hexdigest()


def roi_slices(roi, w, h):
    x0 = int(max(0, min(w, math.floor(roi[0] * w))))
    x1 = int(max(0, min(w, math.ceil(roi[1] * w))))
    y0 = int(max(0, min(h, math.floor(roi[2] * h))))
    y1 = int(max(0, min(h, math.ceil(roi[3] * h))))
    assert x1 > x0 and y1 > y0, (roi, w, h)
    return slice(y0, y1), slice(x0, x1)


def candle_components(profile, w, h):
    components = []
    allowed = np.zeros((h, w), dtype=bool)
    for spot in profile["candlelight"]["anchors"]:
        ry, rx = roi_slices(spot["roi"], w, h)
        yy, xx = np.ogrid[ry.start:ry.stop, rx.start:rx.stop]
        cx, cy = spot["center"]
        sx, sy = spot["radius"]
        m = np.exp(-.5 * ((((xx + .5) / w - cx) / sx) ** 2
                          + (((yy + .5) / h - cy) / sy) ** 2)).astype(np.float32)
        m[m < .010] = 0
        allowed[ry, rx] |= m > 0
        components.append((spot, m, ry, rx))
    return components, allowed


def dust_components(profile, w, h):
    rnd = random.Random(profile["random_seed"])
    particles = []
    allowed = np.zeros((h, w), dtype=bool)
    for field in profile["dust"]["regions"]:
        ry, rx = roi_slices(field["roi"], w, h)
        allowed[ry, rx] = True
        for _ in range(field["count"]):
            x = rnd.uniform(rx.start + 7, rx.stop - 7)
            y = rnd.uniform(ry.start + 7, ry.stop - 7)
            vx = rnd.uniform(-1.9, 1.9)
            vy = rnd.uniform(-5.5, -2.0)
            radius = rnd.uniform(1.1, 2.3)
            intensity = rnd.uniform(4.5, 10.5)
            phase = rnd.uniform(0, 2 * math.pi)
            particles.append((x, y, vx, vy, radius, intensity, phase, rx, ry))
    assert len(particles) == profile["dust"]["particle_budget"]
    return particles, allowed


def render(root, profile_path):
    p = json.loads(profile_path.read_text(encoding="utf-8"))
    assert p["schema"] == "ENVIRONMENT_DYNAMIC_SHOT_PROFILE_V001"
    assert p["enabled_modules"] == ["M01", "M03"]
    assert p["status"] == "RENDER_AUTHORIZED_FOR_ONE_PREVIEW_PO_VISUAL_PENDING"
    source = root / p["source_canonical_path"]
    assert source.is_file() and not source.is_symlink(), "SOURCE_CANONICAL_PNG_MISSING"
    raw = source.read_bytes()
    ident = p["source_identity"]
    assert len(raw) == ident["bytes"] and sha256(source) == ident["sha256"]
    assert git_blob(raw) == ident["git_blob"]
    assert raw[:8] == bytes((137, 80, 78, 71, 13, 10, 26, 10))
    assert struct.unpack(">II", raw[16:24]) == (ident["width"], ident["height"])

    out = p["output"]
    w, h, n, fps = [out[k] for k in ("width", "height", "frames", "fps")]
    assert out["audio"] is False and n == 120 and fps == 30 and (w, h) == (720, 1280)
    with Image.open(source) as im:
        assert im.size == (ident["width"], ident["height"])
        base_u8 = np.asarray(im.convert("RGB").resize((w, h), Image.Resampling.LANCZOS),
                             dtype=np.uint8)
    base_float = base_u8.astype(np.float32)
    candles, candle_mask = candle_components(p, w, h)
    motes, dust_mask = dust_components(p, w, h)
    effect_mask = candle_mask | dust_mask

    assert int(np.count_nonzero(effect_mask)) < int(.16 * w * h), "EFFECT_REGION_TOO_LARGE"
    assert not np.any(effect_mask[int(.415 * h):, :]), "PROTECTED_LOWER_REGION_CHANGED"

    video = root / out["relative_path"]
    video.parent.mkdir(parents=True, exist_ok=True)
    command = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
               "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
               "-framerate", str(fps), "-i", "pipe:0", "-an",
               "-c:v", "libx264", "-preset", "medium", "-crf", "18",
               "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(video)]
    encoder = subprocess.Popen(command, stdin=subprocess.PIPE)

    outside = 0
    max_delta = 0
    max_changed = 0
    candle_activity = 0.0
    dust_activity = 0.0
    first_matches = last_matches = False

    for i in range(n):
        t = i / fps
        envelope = math.sin(math.pi * i / (n - 1)) ** 1.2
        arr = base_float.copy()
        for spot, mask, ry, rx in candles:
            phase = spot["phase"]
            harmonic = (0.58 * math.sin(2 * math.pi * .89 * t + phase)
                        + 0.26 * math.sin(2 * math.pi * 1.71 * t + .67 * phase)
                        + 0.16 * math.sin(2 * math.pi * 2.93 * t + 1.39 * phase))
            mod = envelope * harmonic * spot["strength"]
            if abs(mod) < .001:
                continue
            arr[ry, rx, :] += (mod * mask)[:, :, None] * np.array(
                [1, .64, .18], dtype=np.float32)
            candle_activity += abs(mod)
        for x0, y0, vx, vy, radius, magnitude, phase, rx, ry in motes:
            x = x0 + vx * t
            y = y0 + vy * t
            if not (rx.start + 3 <= x < rx.stop - 3
                    and ry.start + 3 <= y < ry.stop - 3):
                continue
            xs = slice(max(rx.start, int(x - 3 * radius)),
                       min(rx.stop, int(x + 3 * radius) + 2))
            ys = slice(max(ry.start, int(y - 3 * radius)),
                       min(ry.stop, int(y + 3 * radius) + 2))
            if xs.stop <= xs.start or ys.stop <= ys.start:
                continue
            yy, xx = np.ogrid[ys.start:ys.stop, xs.start:xs.stop]
            glow = np.exp(-.5 * ((xx - x) ** 2 + (yy - y) ** 2) /
                          radius ** 2).astype(np.float32)
            amp = envelope * (.83 + .17 * math.sin(2 * math.pi * .19 * t + phase)) * magnitude
            arr[ys, xs, :] += amp * glow[:, :, None] * np.array(
                [.96, .80, .55], dtype=np.float32)
            dust_activity += amp

        frame = np.clip(np.rint(arr), 0, 255).astype(np.uint8)
        different = np.any(frame != base_u8, axis=-1)
        outside = max(outside, int(np.count_nonzero(different & ~effect_mask)))
        max_changed = max(max_changed, int(np.count_nonzero(different)))
        max_delta = max(max_delta,
                        int(np.abs(frame.astype(np.int16) -
                                   base_u8.astype(np.int16)).max()))
        if i == 0:
            first_matches = bool(np.array_equal(frame, base_u8))
        if i == n - 1:
            last_matches = bool(np.array_equal(frame, base_u8))
        encoder.stdin.write(frame.tobytes())

    encoder.stdin.close()
    assert encoder.wait() == 0, "FFMPEG_ENCODER_FAILED"
    assert first_matches and last_matches, "RAW_START_END_NOT_IDENTICAL"
    assert outside == 0, "OUTSIDE_ALLOWED_ENVIRONMENT_PIXELS_CHANGED"
    assert max_delta <= p["intensity_cap_rgb"], "RAW_RGB_DELTA_TOO_HIGH"
    assert max_changed > 0 and candle_activity > 0 and dust_activity > 0

    probe = json.loads(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries",
         "stream=codec_name,codec_type,nb_frames,width,height,r_frame_rate:format=duration",
         "-of", "json", str(video)], text=True))
    tracks = probe["streams"]
    assert len(tracks) == 1
    assert tracks[0]["codec_type"] == "video" and tracks[0]["codec_name"] == "h264"
    assert tracks[0]["nb_frames"] == str(n) and tracks[0]["r_frame_rate"] == f"{fps}/1"
    assert (tracks[0]["width"], tracks[0]["height"]) == (w, h)
    assert abs(float(probe["format"]["duration"]) - n / fps) < .01
    subprocess.run(["ffmpeg", "-v", "error", "-xerror", "-i", str(video),
                    "-f", "null", "-"], check=True)
    assert sha256(source) == ident["sha256"] and source.read_bytes() == raw

    report = {
        "schema": "ENVIRONMENT_DYNAMIC_TEST_EVIDENCE_V001",
        "profile_id": p["profile_id"],
        "gate": "TECHNICAL_PASS_PO_VISUAL_PENDING",
        "shot_id": p["shot_id"],
        "modules": p["enabled_modules"],
        "source_original": p["source_canonical_path"],
        "source_png_sha256": ident["sha256"],
        "source_git_blob": ident["git_blob"],
        "source_png_bytes": len(raw),
        "source_png_unmodified": True,
        "video_path": out["relative_path"],
        "video_sha256": sha256(video),
        "video_bytes": video.stat().st_size,
        "frames": n, "fps": fps,
        "resolution": {"width": w, "height": h},
        "duration_seconds": n / fps,
        "raw_pixel_changed_outside_effect_regions": outside,
        "max_raw_channel_delta": max_delta,
        "max_changed_pixels_in_single_frame": max_changed,
        "authorized_effect_roi_pixels": int(np.count_nonzero(effect_mask)),
        "authorized_effect_roi_fraction": float(np.count_nonzero(effect_mask) / (w * h)),
        "first_and_last_raw_frames_equal_original": first_matches and last_matches,
        "dust_particle_budget": len(motes), "audio_streams": 0,
        "persons_animated": False, "camera_moved": False,
        "original_story_shot_changed": False,
        "v006_candidate_changed": False,
        "main_merged": False,
        "encoding_note": "H264 has normal lossy pixel changes; pre-encoding RGB was altered only in explicitly authorized architecture/dust areas",
        "po_video_status": "REVIEW_PENDING"
    }
    receipt = video.parent / (video.stem + "_EVIDENCE.json")
    receipt.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8")
    print("NEW02_ENV_DYNAMIC_RENDER_TECHNICAL_PASS")
    print("NEW02_APPROVED_SOURCE_SHA256_MATCH=TRUE")
    print("NEW02_RAW_OUTSIDE_EFFECT_REGION_CHANGED_PIXELS=0")
    print(f"NEW02_MAX_RAW_CHANNEL_DELTA={max_delta}")
    print("NEW02_FIRST_LAST_RAW_FRAMES_IDENTITY=PASS")
    print("NEW02_120_FRAMES_FULL_DECODE=PASS")
    print("NEW02_PO_VISUAL_REVIEW=PENDING")
    print("NEW02_MP4_SHA256=" + report["video_sha256"])
    print("NEW02_MP4_BYTES=" + str(report["video_bytes"]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True)
    parser.add_argument("--repo-root", default=str(ROOT))
    args = parser.parse_args()
    render(pathlib.Path(args.repo_root), pathlib.Path(args.repo_root) / args.profile)
