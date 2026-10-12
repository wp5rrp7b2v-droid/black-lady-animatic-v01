# S02-B｜N16–N17 V004 画质修正版（非正式试剪）

2026-10-12 PO direction: retain V003's 6-node timing and variable transitions, improve sharpness by reducing over-cropping, start directly from both canonical approved PNG files, avoid re-encoding a pre-compressed MP4.

- 21.950 sec / 658 frames / 720 × 1280, N16 and N17 original stills only.
- Maximum crop change relative to full 940px image: 1.288×; every crop uses at least 734 native source px, no horizontal upscaling needed to output 720.
- Same 6 editorial segments: 69 / 95 / 117 / 91 / 175 / 111 frames, with continuous camera transitions (1→2, 4→5), purposeful speaker cuts (2→3, 3→4), and 5-frame softened reaction transition (5→6).
- Decode source PNGs and sample each output frame directly from approved source. Encode final video once; audio encoded AAC-LC stereo 44.1kHz; produce independent MP3 fallback.
- Verify originals: dimensions, SHA-256, Git blob, file bytes; verify canonical audio SHA256; full output decode, duration, FPS, frame count and non-silent AAC.
- V001 remains the only PO-approved canonical S02-B cut; V004 is review-only. No Story Shot changes, no Video Index entry, no P0.3 advancement.
- No local Mac sync required during daylight; daily evening closeout cadence RC-029 remains.

## 2026-10-12 V004 verified render

- Successful GitHub Actions run: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/38253241059
- Artifact `11748263727` / `S02B_N16_N17_V004_QUALITY_TEST`
- ZIP SHA256 `29c9ff13b8f08517d0929e15b256c2fe2ddc969bc64c5ac1e4f39019da91ebeb` independently matched after artifact retrieval. ZIP integrity PASS.
- MP4 SHA256 `7f30596a60ada54a8393f8207ad7f59f92702ca8278d0bd257fc258911877018`, size `7,180,406` bytes; independently matched rendered manifest PASS.
- Video H.264 High, `720×1280`, 30fps, **658 frames**; stream/container duration `21.933333s` (658/30), equivalent to the original trial's nominal 21.95 sec editorial scope within one frame. Full media decode PASS.
- Audio AAC-LC, 44.1 kHz 2-channel, mean volume -15.7 dB and max -0.5 dB (non-silent). Independent MP3 included for player troubleshooting.
- Crop windows minimum 734 native pixels wide, reducing tight-zoom softening versus V003; direct original approved PNG pixel source, no iterative H.264 recompression.
- Qualitative quality improvement awaits Product Owner viewing. Noncanonical review-only; V001 and official Video Index unchanged.
- Early attempts on this branch: `38252586634` used slow apt setup, `38253090143` failed because FFmpeg was not preinstalled. `38253241059` succeeded after explicit installation. Only final successful artifact is the review candidate.
