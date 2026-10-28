#!/usr/bin/env python3
"""Opening Enhance Pilot V001: source-locked, 10.33s review-only A/B."""
import hashlib
import json
import pathlib
import subprocess
import sys

BASE = pathlib.Path.cwd()
OUT = BASE / "_opening_enhance_pilot_v001"
OUT.mkdir(exist_ok=True)
SRC = OUT / "P03_OPENING_V2_APPROVED_V001_SOURCE_EXACT.mp4"
SOURCE_GIT_COMMIT = "208566291a5531cb34ad05e50e56e0a9fcc51c02"
SOURCE_GIT_BLOB = "9b4ef42d9eceb5d7f1eb190d508d6749ccf4b70e"
SOURCE_SHA256 = "70d7922244161dd216a26446fd75531db20eea0ac7fc25f567f6ff14e2746e3a"
SOURCE_SIZE = 18892138
START_FRAME, END_FRAME = 591, 901
FPS = 30
NFRAMES = END_FRAME - START_FRAME
A = OUT / "OPENING_ENHANCE_PILOT_V001_A_ORIGINAL_19p70_to_30p03.mp4"
B = OUT / "OPENING_ENHANCE_PILOT_V001_B_REFRAMED_19p70_to_30p03.mp4"
AB = OUT / "OPENING_ENHANCE_PILOT_V001_SIDE_BY_SIDE.mp4"

def run(*args):
    print("$", " ".join(map(str, args)), flush=True)
    subprocess.run(list(map(str, args)), check=True)

def output(*args):
    return subprocess.check_output(list(map(str, args)), text=True).strip()

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def probe(path):
    return json.loads(output("ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", path))

def image_path(prefix):
    base = BASE / "production" / "image_library" / "approved" / "story_shots"
    matches = list(base.glob(prefix + "*.png"))
    if len(matches) != 1:
        raise RuntimeError(f"Expected single canonical PNG for {prefix}, found {matches}")
    signature = matches[0].read_bytes()[:8]
    if signature != b"\x89PNG\r\n\x1a\n":
        raise RuntimeError(f"Not a real PNG: {matches[0]}")
    return matches[0]

# Reacquire the pre-migration canonical MP4 at its known original Git commit.
run("git", "fetch", "--no-tags", "--depth=1", "origin", SOURCE_GIT_COMMIT)
with open(SRC, "wb") as f:
    subprocess.run(["git", "cat-file", "blob", SOURCE_GIT_BLOB], stdout=f, check=True)
if SRC.stat().st_size != SOURCE_SIZE or sha256(SRC) != SOURCE_SHA256:
    raise RuntimeError("FAIL: historical master exact SHA/size mismatch")
meta = probe(SRC)
videos = [x for x in meta["streams"] if x["codec_type"] == "video"]
audios = [x for x in meta["streams"] if x["codec_type"] == "audio"]
if len(videos) != 1 or not audios or int(videos[0]["width"]) != 1080 or int(videos[0]["height"]) != 1920 or int(videos[0]["nb_frames"]) != 991:
    raise RuntimeError("FAIL: source codec/frame identity mismatch")
print("PASS: original Opening V001 SHA-256, size, frame count and streams", flush=True)

# Original segment A: decode and trim by locked frame indices; audio remains uninterrupted.
audio_filter = "atrim=start=19.7:duration=10.333333333,asetpts=PTS-STARTPTS"
run(
    "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", SRC,
    "-filter_complex", f"[0:v]trim=start_frame={START_FRAME}:end_frame={END_FRAME},setpts=PTS-STARTPTS[v];[0:a]{audio_filter}[a]",
    "-map", "[v]", "-map", "[a]",
    "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
    "-r", "30", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
    "-movflags", "+faststart", A
)

# Candidate B uses only the already-approved atomic Story Shot PNG bytes.
# This pilot does not create depth/3D, change faces, add speech or regenerate images.
# Selective frame language: establish architecture; hold character entrance;
# allow a full static read of subtle smile; accent a shift in turn/action.
shots = [
    ("N08_", 58, "scale=1160:2062:flags=lanczos,crop=1080:1920:x='40-12*n/58':y='75-26*n/58',setsar=1"),
    ("N09_", 84, "scale=1140:2027:flags=lanczos,crop=1080:1920:x='30+11*n/84':y='53-8*n/84',setsar=1"),
    ("N10_", 82, "scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920,setsar=1"),
    ("N05_", 86, "scale=1140:2027:flags=lanczos,crop=1080:1920:x='30-12*n/86':y='53+9*n/86',setsar=1"),
]
parts = []
evidence = []
for prefix, frames, filt in shots:
    img = image_path(prefix)
    part = OUT / f"{prefix.strip('_')}_{frames}f.mp4"
    run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-loop", "1", "-framerate", "30", "-i", img,
        "-vf", filt + ",fps=30,format=yuv420p",
        "-frames:v", frames, "-an", "-c:v", "libx264", "-preset", "medium",
        "-crf", "19", "-pix_fmt", "yuv420p", part)
    parts.append(part)
    evidence.append({"shot": prefix.strip("_"), "frames": frames, "source_path": str(img.relative_to(BASE)), "source_sha256": sha256(img), "treatment": filt})
concat = OUT / "part_list.txt"
concat.write_text("".join(f"file '{x.name}'\n" for x in parts), encoding="utf-8")
silent = OUT / "B_video_only.mp4"
run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", concat,
    "-c:v", "copy", "-an", silent)
run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", silent, "-i", SRC,
    "-filter_complex", f"[1:a]{audio_filter}[a]",
    "-map", "0:v:0", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
    "-ar", "48000", "-ac", "2", "-movflags", "+faststart", B)

# Readable video comparison without hiding either version or needing two players.
run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", A, "-i", B,
    "-filter_complex", "[0:v]scale=540:960:flags=lanczos[left];[1:v]scale=540:960:flags=lanczos[right];[left][right]hstack=inputs=2[v]",
    "-map", "[v]", "-map", "0:a:0", "-c:v", "libx264", "-preset", "medium", "-crf", "21",
    "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", "-frames:v", NFRAMES, AB)

# A/B quality gate: exact frame counts, original user audio PCM identity between A and B.
report = {}
for name, path in [("A", A), ("B", B), ("AB", AB)]:
    info = probe(path)
    v = next(x for x in info["streams"] if x["codec_type"] == "video")
    aud = [x for x in info["streams"] if x["codec_type"] == "audio"]
    if int(v["nb_frames"]) != NFRAMES or not aud:
        raise RuntimeError(f"FAIL: {name} frame/audio verification: {v.get('nb_frames')}, aud={len(aud)}")
    run("ffmpeg", "-v", "error", "-xerror", "-i", path, "-f", "null", "-")
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", str(path),
                                   "-map", "0:a:0", "-ac", "2", "-ar", "48000",
                                   "-c:a", "pcm_s16le", "-f", "s16le", "-"])
    report[name] = {"file": path.name, "sha256": sha256(path), "size": path.stat().st_size,
                    "width": v["width"], "height": v["height"], "frames": int(v["nb_frames"]),
                    "audio_pcm_sha256": hashlib.sha256(raw).hexdigest()}
if report["A"]["audio_pcm_sha256"] != report["B"]["audio_pcm_sha256"]:
    raise RuntimeError("FAIL: source audio A/B PCM mismatch")
manifest = {
  "status": "TECHNICAL_PASS_ONLY__PO_VISUAL_REVIEW_PENDING",
  "pilot": "OPENING_ENHANCE_PILOT_V001",
  "base_master": {"sha256": SOURCE_SHA256, "byte_size": SOURCE_SIZE, "git_blob": SOURCE_GIT_BLOB},
  "range": {"start_frame": START_FRAME, "end_frame_exclusive": END_FRAME, "fps": FPS,
            "start_seconds": 19.7, "end_seconds_exclusive": END_FRAME / FPS},
  "frame_count": NFRAMES, "new_shots": 0, "shot_sources": evidence, "outputs": report,
  "original_master_unchanged": True, "story_shot_index_unchanged": True, "video_index_unchanged": True,
  "visual_approval": "PENDING", "full_opening_replacement": "NOT_AUTHORIZED",
  "notes": "Exploratory static-PNG reframing, not 2.5D and not an approved cinematic improvement. PO judges AB."
}
(OUT / "MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(OUT / "README_ZH.md").write_text(
    "# Opening Enhance Pilot V001（试验候选，未批准）\n\n"
    "A 为原批准 MP4 的 19.70–30.03 秒声画裁切；B 为 N08/N09/N10/N05 四张获批正式 PNG 的选择性 2D 重构。\n"
    "同长度、同一连续原音；原母版和正式索引均未修改。\n\n"
    "重点判断：镜头内容、运动与停顿是否比原版更自然；如果不明显或变差，判定 FAIL，不扩大制作。\n",
    encoding="utf-8")
print("PASS: technical QC; source and A/B audio PCM are verified. VISUAL PASS NOT CLAIMED.", flush=True)
print(json.dumps({x: {k:v for k,v in y.items() if k!="audio_pcm_sha256"} for x,y in report.items()},indent=2))
