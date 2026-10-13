# S02-B｜宁秋水反应插镜｜B V002 声学停顿校准试剪

Date: 2026-10-13

**STATUS: B V002 PRODUCT OWNER APPROVED FOR LOCAL EDITORIAL TIMING / NOT VERIFIED WORD-LEVEL ASR / NO FORMAL MASTER PUBLICATION / APPROVED CANONICAL V001 UNCHANGED**

## Authorization / upstream decisions

PO approved **B V001 local editorial treatment** with `B版通过` (Decision Log `BL-D-176`). PO next instructed **“下一步：精确对白对齐”**, authorizing an evidence-driven local timing refinement and review, **not a canonical master replacement or Story Shot registration**.

Upstream:
- `S02_B_ASSEMBLY_APPROVED_V001.mp4`: 64.250s, SHA256 `8ec47720b5641412b2ebd1e082bf058244d6b07fbe97500b56a8ef830bf2042a` independently reconfirmed; unchanged.
- `TAIL_NING_REACTION_TEST_01 Candidate 01`: 941×1672, 2,471,479 bytes, SHA256 `cbac98a82763c6c930a3c820c917f4b9b8bc2ed300a49b48143b8b1cd9486c9c`, staging intake Run `38400935301` PASS.
- A original master tail review source: `S02B_NING_REACTION_AB_A_CANONICAL_TAIL_REVIEW.mp4`; SHA256 `f23a0738b3660cd1f68079aca3985173fc562e025d16b5f4663d3f87aaf64932`, 7.783s. This A file is a review derivative, not the approved 64.25s canonical binary.
- Previously PO-approved B V001 review: `S02B_NING_REACTION_AB_B_INSERT_PROVISIONAL_V001.mp4`, SHA256 `2822343f1ef9dea14ba2536fd108276a379fec8326edf87bcb233304a67fe4d6`, 7.783s.

## Audio transcript and evidence-grade limitations

The canonical `source_material/S3_audio_transcript/S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001.csv` contains:
- `S3-MVP1-0020`: “城堡大门只会在下雨天关闭”, source approx 02:15.000–02:19.500;
- `S3-MVP1-0021`: “这是夫人的要求。各位，请随我来”, source approx 02:19.000–02:23.000.
- Both are `REVIEWED_TRANSCRIPT`, not verified cut-authority timestamps. They may only guide search.

`docs/project_control/gates/P0_3_video_pipeline/s02_b_audio_only_qc_v001_approval_2026-09-29.md` historically reports **closing phrase** “各位，请随我来” end approx source time **00:02:22.560** (mapped to 63.810 in the 64.25s approved S02-B section). This is historical automatic alignment evidence, not a guarantee for all word starts. GitHub Actions run `36505933111` listed **zero currently accessible artifacts** on 2026-10-13, so the original word-level report cannot be independently reopened.

A spectrogram and bandpass speech-energy RMS plot were computed directly from the exact approved master. They show a relatively strong sound cluster through ~60.6s, a lower-energy interval, and renewed prominent sound at approximately ~62.15s. This supports locating a **plausible sentence/pause transition**, but acoustic envelope **cannot identify Chinese words**. No reliable installed Chinese ASR or direct auditory transcription was available in this runtime. Accordingly `这是夫人的要求` exact last syllable and `各位` exact onset are **UNVERIFIED / NO WORD-LEVEL PASS**.

## V002 controlled picture edit — exact frame-based review experiment

- Output: `S02B_NING_REACTION_AB_B_SPEECH_PAUSE_ALIGNED_REVIEW_V002.mp4`
- Output byte size: **707,624 bytes**
- Output SHA256: `748ce5d1648cc2ae1a690278584ee2dad380c3e7984e2a114a4a1c62eae3aab5`
- Output: 720×1280 / H.264 / 30fps / 233 video frames / 7.783s / AAC audio unchanged from A, copied by bitstream `-c:a copy`.
- Uses approved local A tail as picture/audio reference; original source timeline `56.466667→64.250000`.
- Inserts PO-approved Ning Candidate 01 image for **exactly video frame indices 116–168 inclusive, 53 frames, 1.766667s**.
- On original S02-B V001 source timeline, the picture interval corresponds to **approx 60.333334–62.100000s**, last boundary chosen before the next strong audio onset near ~62.15.
- Direct cut structure: N25 visual → independent Ning reaction → existing N26 visual, eliminating any short N26 flash-before-insert.
- Compared with B V001 test interval **60.333334–61.733334s** (~1.4s), V002 retains the same entry and prolongs the reaction **by ~0.366667s**, delaying exit to the observed acoustic gap before the next prominent voice sound.
- No interpolation, AI-created motion, repeated digital push or generative image editing.

### Binary and timeline QC

Independent ffmpeg/ffprobe inspection confirmed:
- A, B V001, and B V002 all **233 video frames**, **366 audio AAC frames**, **7.783s**.
- Their decoded PCM audio SHA256 is exactly identical:
  `229b550f5ce8689de72719e34e72e7e3471e7e8bedc518093633144390833baf`; decoded audio byte size `1495040` each. No audio word time shift, insertion, duplication, stretch, or missing audio between A/B versions.
- Frame-level RGB comparison at 120×212: exactly **53 frames (116–168)** differ substantially from A (`MAE>12`). Frames before 116 and from 169 onward differ only due to video re-encoding (outside overlay mean absolute pixel difference 0.260 and 0.135; maximum <0.264).
- Both source approved master and exact PO candidate PNG hashes independently reconfirmed; no canonical or candidate binary edited.
- H.264 video re-encoding pertains only to temporary review MP4, not source master.

## Gate conclusion

- `B V001 EDITORIAL TREATMENT`: PO APPROVED, authoritative baseline.
- `B V002 ACOUSTIC PAUSE CUT`: **TECHNICAL FRAME QC PASS / PRODUCT OWNER APPROVED 2026-10-13 FOR LOCAL EDITORIAL TIMING**.
- `B V002 ORIGINAL AUDIO IDENTITY ACROSS A/B`: **PASS**.
- `EXACT SPOKEN WORD ONSET/OFFSET IDENTIFICATION`: **PENDING / CAN'T ASSERT FROM WAVEFORM ALONE**.
- `S02_B_ASSEMBLY_V001 64.25s`: APPROVED / CANONICAL / UNCHANGED.
- `STORY SHOT INDEX + VIDEO INDEX`: UNCHANGED.
- `N27 ABSORBED`: UNCHANGED.
- `P0.3`: IN PROGRESS.

**Next:** PO has approved the rendered B V002 local edit as seen. Before marking “精确对白逐字对齐 PASS”, obtain trustworthy direct-auditory or Chinese-ASR forced-alignment evidence and verify entry/exit against `这是夫人的要求。各位，请随我来。`. Do not promote canonical by assumption.

Local review MP4 and waveform plots are in conversation artifacts only; no video added to formal repository or Drive.

## 2026-10-13｜Product Owner review closeout (addendum)

Product Owner responded **“批准”** immediately after viewing the linked `S02B_NING_REACTION_AB_B_SPEECH_PAUSE_ALIGNED_REVIEW_V002.mp4` and being asked to approve the B V002 revised timing. The exact approved review-file identity was reconfirmed from the locally mounted file without re-encoding:

- Filename: `S02B_NING_REACTION_AB_B_SPEECH_PAUSE_ALIGNED_REVIEW_V002.mp4`
- Byte size: `707624`
- SHA256: `748ce5d1648cc2ae1a690278584ee2dad380c3e7984e2a114a4a1c62eae3aab5`
- Running time: `7.783s`; Ning insert exactly 53 frames (`116–168`), ≈1.766667s.
- **PO decision: B V002 local timing/visual edit APPROVED AS REVIEWED.** This replaces B V001 as the preferred *local treatment candidate* for the Ning reaction, while leaving B V001's historical PO approval intact.
- Audio PCM identity across A, B V001, B V002 remains technically verified; **phoneme/word-level identification of the two Chinese phrases is still unverified**. PO approval means the *auditioned edit is acceptable*, not that waveform measurement proves syllable boundaries.
- Before any official full-length S02-B V002 publication, retain explicit authorization and new-version review gate; do not overwrite S02-B V001. Canonical PNG publication and Story Shot Index registration remain separately gated. No N27 production.
- This status supersedes all earlier **“PO V002 REVIEW PENDING”** phrases above while preserving their prior-stage audit history.
