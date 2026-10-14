# S02-B｜完整 Review V004：君鹭远 B V002 + A06/N24 交换镜头顺序

Date: 2026-10-14
Status: **REVIEW V004 RENDERED / TECHNICAL QC PASS / PO VIDEO APPROVAL PENDING / OFFICIAL CANONICAL V001 UNCHANGED**

## Current PO decisions
1. PO approved **Jun local B V002**: `S02_B_N20_JUN_ACK_N21_CONTEXT_B_V002_FULL_LINES.mp4`, including 36 frames / 1.2s of the independently verified PO-selected Jun PNG.
2. PO demanded that **A06 (open castle door) and N24 (Guang Yong's question) reverse visual order**.
3. Revised visual order: `N23 → A06 → N24 → N25`.
4. This 2026-10-14 direction overrides the 2026-10-06 sequence-order correction in `s02_b_sequence_order_correction_n24_a06_n25_2026-10-06.md`, while preserving the historical record.
5. PO has not approved publication of this new **full-length V004**. The Jun local insert is editorially approved, not an authorization to publish V004.

## Sources and identity
- Parent: `S02_B_ASSEMBLY_REVIEW_V003_N16N17_V004_NING_REACTION.mp4`
- Parent SHA256: `827905c725ec0bc8c6b5fb169d8bc623c45c51c5c6c6fd514bb27f718cf10141`, bytes 10,347,019, 720×1280, 30 fps, 1927 video frames, 64.250s duration.
- Jun PO-selected original: `staging/story_shot_candidates/S02B_JUN_ACKNOWLEDGEMENT_TEST_01/城堡烛光下的专注侧颜.png` in review branch, 941×1672, 2,015,907 bytes, SHA256 `1af236000b271d327278e82bf3e744fee08bd49682966eb5fa75f731a67c46e7`; staging exact binary verification GitHub Actions run `38507541961`, PASS.

## Rendered V004 review-only video
- Name: `S02_B_ASSEMBLY_REVIEW_V004_JUN_B_V002_A06_BEFORE_N24.mp4`
- **SHA256: `dd07d3ee4bdbd719a159396fc938570d893c097dc3bb5380fccf14bf3802adb2`**
- Bytes: **10,476,438**
- 720×1280, 30fps, **1927 frames** (video 64.233333s), original AAC audio stream length **64.250000s**, 3,013 AAC packets, container 64.250000s.
- Audio treatment: **stream copy of original V003 AAC**, no remix, cut, fade, speech alignment, or re-encode.
- Full video decode: **PASS**.
- V003↔V004 decoded 48 kHz stereo PCM SHA256 **exact match**: `1952b8abb045aeccb25f4205078b83f66e4d3f62767ee6cdf9b375efe5d78cd8`.
- V003↔V004 AAC ADTS bitstream hashes **exact match**: `d1e12748ce836c6c191148c3abf10b3a5144a932042c6474512303c79b87e5e9`.

## Exact frame-level visual edit map (source V003 → V004)
| Rendered frames (exclusive end) | Source | Notes |
|---|---|---|
| 0:1078 | V003 0:1078 | Entire previously approved N16–N17 V004 beginning + through N20 unchanged in source |
| 1078:1114 | PO-selected Jun approved PNG repeated for 36 frames | Jun response, 1.2s, local B V002 approved |
| 1114:1566 | V003 1114:1566 | N21, N22, N23 etc identical sequence |
| 1566:1629 | V003 1631:1694 | A06 moved before N24, **63 frames** |
| 1629:1694 | V003 1566:1631 | N24 Guang Yong question moved after A06, **65 frames** |
| 1694:1927 | V003 1694:1927 | N25, Ning reaction B V002 and N26 preserved |

- The original 128-frame N24+A06 block is reordered without adding or deleting frames; N25 retains the original position at frame 1694.
- 18 visual sample source-to-output checks spanning approved intro, Jun adjacency, N23, relocated A06/N24, N25, Ning reaction and tail: all pass using mean absolute pixel delta below 0.77 8-bit/channel (difference is normal H.264 re-encoding).
- The approved still binaries are not modified; **only the rendered review MP4 is re-encoded**.

## Short local review excerpt
- `S02_B_A06_N24_REORDER_LOCAL_REVIEW_V001.mp4` (source 49.0–59.5s of V004)
- SHA256: `c279985e327b9e83823f5d639e0b9a81e9b46ebf7397bee7518ae3538f80e2fc`
- Bytes: `1,040,436`; 10.5s; video full decode PASS.
- Excerpt only for visual order audit, not an independent new audio authority.

## PO decision gate / non-actions
- Present V004 64.250s for PO review, with 10.5s local cue.
- Do not declare V004 approved before new PO review.
- Do not upload or replace official canonical `S02_B_ASSEMBLY_APPROVED_V001.mp4`, video index, Story Shot Index, or Project Control dashboard from a review experiment.
- Render files are local current-conversation review derivatives; this persistent design/QC/receipt record is committed to review branch, not main. Publication and canonical storage require a separate approved gate.
