# S02-A Assembly Proof V002 — Execution Patch

Status: PRODUCT OWNER AUTHORIZED / READY FOR WORK
Date: 2026-09-28

## Authority
S02_A_AUDIO_ONLY_QC_PROOF_V001 received PRODUCT OWNER AUDIO QC PASS.

## V002 delta from V001
Only the audio start boundary changes:
- V001: 00:32.900
- V002: 00:33.020
- End remains: 01:18.750
- V002 duration: 45.730 s

## Locked visual sequence
N11 → N12 → A04 → N14 → N15 → A05

## Locked V002 timeline
- N11 00:33.020 → 00:39.100 (6.080 s)
- N12 00:39.100 → 00:46.360 (7.260 s)
- A04 00:46.360 → 00:56.260 (9.900 s)
- N14 00:56.260 → 01:03.520 (7.260 s)
- N15 01:03.520 → 01:10.940 (7.420 s)
- A05 01:10.940 → 01:18.750 (7.810 s)

## Audio
Canonical source: AUDIO_MVP1_CANONICAL_V001
Use exactly 00:33.020 → 01:18.750.
The PO-approved Audio-Only QC Proof is the auditory acceptance authority.

## Visual/motion policy
All six approved source images remain unchanged.
N15 motion remains locked:
- Rotation -3.5° → 0°
- Scale 103% → 105%
- first ~1.6 s roll-to-level, then extremely slow push
All cuts remain direct; N15 → A05 at 01:10.940 remains HARD CUT.
No DepthFlow, character 2.5D, AI interpolation, generative character motion, subtitles, BGM, or extra SFX.

## Output
S02_A_ASSEMBLY_PROOF_V002.mp4
941×1672, 9:16, 45.730 s target.

## Gate
Return proof + technical QC to Product Owner. Do not update Story Shot Registry, Asset Registry, or Project Control; do not merge/formalize the proof.
