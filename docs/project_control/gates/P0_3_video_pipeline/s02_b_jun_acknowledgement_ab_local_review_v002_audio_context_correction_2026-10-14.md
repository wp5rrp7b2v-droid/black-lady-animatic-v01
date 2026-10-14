# S02-B｜君鹭远认可回应近景｜局部 A/B V002 完整旁白上下文修复

Date: 2026-10-14
Status: LOCAL EDITORIAL REVIEW V002 RENDERED AND VERIFIED / PO REVIEW PENDING / NO CANONICAL PUBLICATION / NO STORY SHOT REGISTRATION

## Trigger

PO watched local A/B V001 and reported: **“B的台词不完整”**.
The prior local A and B were trimmed to a 3.733333-second window (34.666667 to 38.400000 of approved V003), which cut mid-narration. This was an **editorial context window error**, not a fault in the approved Jun PNG.
**Do not present V001 for further approval.**

## Source authority preserved

- Full approved editorial baseline: `S02_B_ASSEMBLY_REVIEW_V003_N16N17_V004_NING_REACTION.mp4`.
- Baseline SHA-256: `827905c725ec0bc8c6b5fb169d8bc623c45c51c5c6c6fd514bb27f718cf10141`.
- Includes previously approved N16–N17 V004 and Ning tail reaction B V002, neither altered.
- Single PO-approved Jun close-up is GitHub-staged exact binary:
  `staging/story_shot_candidates/S02B_JUN_ACKNOWLEDGEMENT_TEST_01/城堡烛光下的专注侧颜.png`.
- PNG SHA256: `1af236000b271d327278e82bf3e744fee08bd49682966eb5fa75f731a67c46e7`; verified by GitHub Actions Run `38507541961`, PASS.

## Corrected local V002 editorial plan

Use the actual V003 cut boundaries at 30 fps, determined by video decoding rather than guessed clip times:

| Meaning | Exact source frame | Seconds |
|---|---:|---:|
| Start of context shot block | 839 | 27.966667 |
| N20→N21 original cut | 1078 | 35.933333 |
| New Jun reaction ends after 36 frames | 1114 | 37.133333 |
| Existing N21→N22 cut | 1222 | 40.733333 |
| End of entire N20/Jun/N21/N22 context before next shot | 1366 exclusive | 45.533333 |

Both A and B use frames 839 through 1365 inclusive: **527 frames / 17.566667 sec / 720×1280 / 30 fps**.

- A: original V003 video 839:1366, unchanged visual content.
- B: original V003 video 839:1078 + static PO-approved Jun PNG (36 frames) + original V003 video 1114:1366.
- B **replaces** 36 existing N21 frames (1.2 sec); no additional timing and no modifications to upstream/downstream sequence.
- Both use exactly the same continuous soundtrack sourced from V003, with sample boundaries 839×1600 and 1366×1600 samples at 48 kHz, encoded **once** to AAC and stream-copied into both local reviews.
- No transcription, retiming, rearrangement, new speech, synthetic voice, or word-level speech gate was used; natural editorial context is for PO to judge.

## Delivered local A/B review derivatives (not on GitHub; short-lived chat review)

- A `S02_B_N20_N21_CONTEXT_A_V002_FULL_LINES.mp4`:
  - byte size: `1749535`
  - SHA256: `f92346794be5c0cbe0abe0c71204d83c05aee5f6b8bf8bbcaac0b98b1d9b93c6`
- B `S02_B_N20_JUN_ACK_N21_CONTEXT_B_V002_FULL_LINES.mp4`:
  - byte size: `1921005`
  - SHA256: `ce56520f6149fe9a74c688842c9ed9e8306e54f4cd6423adfb7484c54a9423f3`

Local technical QC:

- Each clip: H264 720×1280, 30 fps, **527 frames**, **17.566667 sec**.
- Video full decode: A PASS / B PASS.
- Audio decoded PCM hashes in A and B: **identical**, SHA256 `b9919496dc368e31c021e6c59d449eef97974544f3d4eb8e5b538febe8203c90`.
- Decoded audio bytes: `3375104` in both.
- Source V003 soundtrack's meaning and full order unchanged; compression re-encoding of local derivative means do NOT assert the local AAC decode is bit-identical to the source master.
- No source master binary modified.
- These are review derivatives, **not authorized for canonical video publication**, and this receipt does NOT constitute Product Owner editorial approval of B V002.

## Follow-up

Ask PO to view corrected A/B, determine B accepted/needs adjustment. If accepted, proceed only under separately authorized scope for new official full video master and Story Shot publication/registration. Keep V003 baseline and the approved source PNG intact.
