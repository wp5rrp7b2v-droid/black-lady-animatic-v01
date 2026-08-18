#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PAYLOAD_DIR="$REPO_ROOT/artifact_payload"
WORK_DIR="${RUNNER_TEMP:-${TMPDIR:-/tmp}}/black-lady-animatic-${GITHUB_RUN_ID:-local}-$$"
OUTPUT_PATH="${1:-$PWD/black_lady_animatic_cloud_smoke_test_02.mp4}"

cleanup() {
  rm -rf "$WORK_DIR"
}
trap cleanup EXIT
mkdir -p "$WORK_DIR" "$(dirname "$OUTPUT_PATH")"

restore_image() {
  local shot="$1"
  local destination="$2"
  local parts=("$PAYLOAD_DIR/${shot}.b64.part"*)
  if [[ ! -e "${parts[0]}" ]]; then
    echo "No payload parts found for $shot" >&2
    return 1
  fi
  cat "${parts[@]}" | base64 --decode > "$destination"
  test -s "$destination"
}

restore_image sh01 "$WORK_DIR/sh01.png"
restore_image sh02 "$WORK_DIR/sh02.png"

ffmpeg -hide_banner -loglevel warning -y \
  -loop 1 -framerate 24 -i "$WORK_DIR/sh01.png" \
  -loop 1 -framerate 24 -i "$WORK_DIR/sh02.png" \
  -filter_complex "\
[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,\
zoompan=z='if(lte(on,16),1,1+0.035*(on-16)/67)':\
x='(iw-iw/zoom)/2':y='(ih-ih/zoom)*0.70':d=84:s=1080x1920:fps=24,\
setsar=1,setpts=N/(24*TB)[sh01];\
[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,\
zoompan=z='1+0.012*on/59':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)*0.55':\
d=60:s=1080x1920:fps=24,setsar=1,setpts=N/(24*TB)[sh02];\
[sh01][sh02]concat=n=2:v=1:a=0,format=yuv420p[outv]" \
  -map "[outv]" -frames:v 144 -r 24 -an \
  -c:v libx264 -preset medium -crf 18 -movflags +faststart "$OUTPUT_PATH"

test -s "$OUTPUT_PATH"
printf 'Rendered %s\n' "$OUTPUT_PATH"
