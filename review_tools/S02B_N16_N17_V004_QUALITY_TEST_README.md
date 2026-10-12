# S02-B｜N16–N17 V004 画质修正版（非正式试剪）

2026-10-12 PO direction: retain V003's 6-node timing and variable transitions, improve sharpness by reducing over-cropping, start directly from both canonical approved PNG files, avoid re-encoding a pre-compressed MP4.

- 21.950 sec / 658 frames / 720 × 1280, N16 and N17 original stills only.
- Maximum crop change relative to full 940px image: 1.288×; every crop uses at least 734 native source px, no horizontal upscaling needed to output 720.
- Same 6 editorial segments: 69 / 95 / 117 / 91 / 175 / 111 frames, with continuous camera transitions (1→2, 4→5), purposeful speaker cuts (2→3, 3→4), and 5-frame softened reaction transition (5→6).
- Decode source PNGs and sample each output frame directly from approved source. Encode final video once; audio encoded AAC-LC stereo 44.1kHz; produce independent MP3 fallback.
- Verify originals: dimensions, SHA-256, Git blob, file bytes; verify canonical audio SHA256; full output decode, duration, FPS, frame count and non-silent AAC.
- V001 remains the only PO-approved canonical S02-B cut; V004 is review-only. No Story Shot changes, no Video Index entry, no P0.3 advancement.
- No local Mac sync required during daylight; daily evening closeout cadence RC-029 remains.
