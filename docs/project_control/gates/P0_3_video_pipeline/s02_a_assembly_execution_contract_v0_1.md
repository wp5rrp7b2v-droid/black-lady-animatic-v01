# S02-A Assembly Execution Contract V0.1

Status: PRODUCT OWNER APPROVED / LOCKED
Date: 2026-09-28
Scope: P0.3 / S02-A
Sequence: N11 → N12 → A04 → N14 → N15 → A05

## Canonical audio
AUDIO_MVP1_CANONICAL_V001
Audio remains timing authority. No speed change, re-recording, AI voice, or dialogue repositioning.

## Locked timeline
| Shot | IN | OUT | Duration |
|---|---:|---:|---:|
| N11 | 00:32.900 | 00:39.100 | 6.200s |
| N12 | 00:39.100 | 00:46.360 | 7.260s |
| A04 | 00:46.360 | 00:56.260 | 9.900s |
| N14 | 00:56.260 | 01:03.520 | 7.260s |
| N15 | 01:03.520 | 01:10.940 | 7.420s |
| A05 | 01:10.940 | 01:18.750 | 7.810s |

Assembly proof range: 00:32.900 → 01:18.750 (45.850s).

## Canonical visual inputs
- N11: production/image_library/approved/story_shots/N11_NEIL_ABNORMAL_PORTRAIT_APPROVED_V001.png
  - bytes 2538801
  - git blob f5efde465dcadd1490f2064c6db39e1d5f194dc6
  - SHA-256 09d45c1b27fbd2aea68c818677d9656a2ae7f39296f80f6db622118312aebcc5
- N12: production/image_library/approved/story_shots/N12_NEIL_CROSS_RIGID_SMILE_APPROVED_V001.png
  - bytes 2434337
  - git blob 853d04f5ed8a2e1845ce1dfa9cef5c02f123124b
  - SHA-256 d94dc3623ba1abc55aa86c8b646d7876d097433bfadb70291bfa9c68cffc030b
- A04: production/image_library/approved/A_Series/A04_REBOOT_approved_v001.png
  - bytes 2486659
  - git blob fd05cae8618d7daa16c16658b29d25ab65052fbb
- N14: production/image_library/approved/story_shots/N14_FIRST_ENCOUNTER_IMPORTANCE_APPROVED_V001.png
  - bytes 2500282
  - git blob e32c03bc21efcd0eda98d2e9868a64915583b19f
  - SHA-256 0474003a1d6d48a652935033f17560d0ee1d689caadbdb7d4af72560477844f1
- N15: production/image_library/approved/story_shots/N15_LOCKED_GATE_FORESHADOWING_APPROVED_V001.png
  - bytes 2583010
  - git blob 4d9ca2dcd33df32294ff9b928bf3ab88d63c7487
  - SHA-256 2712321ca6348cc39234f8ae65bcdb0fd2e6b2faf0b56dcc94a51235011d1191
- A05: production/image_library/approved/A_Series/A05_REBOOT_approved_v001.png
  - bytes 2289774
  - git blob 9445c9b89b6665bc027385f13821a4ede6892c10

## Transform policy
N11/N12/A04/N14/A05: non-destructive whole-frame Scale / Position / Crop only. No DepthFlow, character 2.5D, AI interpolation, or generative character motion.

N15 special motion:
- direct-cut entry
- rotation -3.5° → 0°
- scale 103% → 105%
- first ~1.6s: slow roll back to level plus subtle push-in
- remainder: extremely slow push-in
- gate remains visual center
- no generated motion in fog, trees, or gate
- N15 → A05 at 01:10.940: HARD CUT

All other shot boundaries: direct cut.

## Output proof
- 941 × 1672
- 9:16
- 45.850s target assembly range
- no subtitles, BGM, extra SFX, or complex effects in first proof

## Governance
This contract is the execution authority for the next S02-A Assembly Input Bundle. Any timing, source binary, N15 motion-language, or transition change requires Product Owner approval before execution.
