# 《诡舍·黑衣夫人》S02-B V006｜电影化重构粗剪 Review V001｜Render & Independent QC Receipt

Date: 2026-10-14

**GATE: REVIEW MP4 RENDERED / INDEPENDENT POST-DOWNLOAD QC PASS / NO PO FULL-VIDEO APPROVAL / NO VIDEO MASTER MODIFICATION / NO MAIN MERGE.**

## Scope and important source limitation

Product Owner directed **“开始粗剪”**, authorizing V006 rough-cut candidate assembly and review, not final video publication, modification of approved masters, Story Shot changes or merging to main.

The existing Director Design V0.2 and EDL V001 prescribed `S02_B_ASSEMBLY_REVIEW_V005_JUN_APPROVED_A06_ON_TURN_CINEMATIC_TRANSITIONS.mp4` as a parent source, with locked SHA-256 `ffd811370e77293e5f519020d611aeaef37590979d5922d5ce715a1cb508d63c`. **This V005 file could not be located in the available GitHub/Google Drive sources at render time**. It must NOT be claimed that this preview reproduces every V005 visual frame or has the V005 AAC stream.

To make a testable candidate without silently fabricating that parent media, Chat assembled an explicitly named **RECONSTRUCTED ROUGH REVIEW** using:
- The actual previously approved N16–N17 V004 source `S02B_N16_N17_V004_QUALITY_TEST.mp4` for video frames **0–657** (658 decoded source frames, re-encoded once into new review video; does not mutate source).
- All remaining frames **658–1926** rendered from original approved Story Shots including exact NEW-01 and NEW-02, plus the separately PO-selected original Jun acknowledgment and Ning B V002 reaction staging PNGs.
- **Uninterrupted approved full S02-B V001 AAC packets STREAM COPIED unchanged** from `S02_B_DIRECTOR_REVIEW_V001.mp4`, not re-mixed or retimed. This is an audibly continuous canonical-approved audio source but is not independently asserted to be binary-identical to missing V005 source.

No new story image was generated and no previously approved PNG was altered or resaved by this procedure. Transformations occur solely inside the temporary video derivative.

## Inputs exact provenance

- Review branch: `review/s02b-jun-nod-insert-20261014`.
- Original locked V004 N16–N17 segment: GitHub Actions Run `38253241059` Artifact `11748263727`; file `S02B_N16_N17_V004_QUALITY_TEST.mp4`; file SHA-256 `7f30596a60ada54a8393f8207ad7f59f92702ca8278d0bd257fc258911877018`. **658 frames** at 30 fps, 720×1280, 21.93333s.
- Original V001 full video used strictly for its approved AAC: Run `37894629986`, Artifact `11600040686`, video SHA-256 `8ec47720b5641412b2ebd1e082bf058244d6b07fbe97500b56a8ef830bf2042a`.
- NEW-01 PO-approved immutable canonical image: `production/image_library/approved/story_shots/S02B_V006_NEW01_NING_WARNING_JUN_OTS_APPROVED_V001.png`, locked SHA-256 `f3002984a377a31e05cd7490e914c0da4009509c8ddb5eaf45a5d45144775989`, blob `7fedcdc93f2b366d1a8597e86ffe8c99006ce027`.
- NEW-02 PO-approved immutable canonical image: `production/image_library/approved/story_shots/S02B_V006_NEW02_CROWD_INTERIOR_SIDE_DEPTH_APPROVED_V001.png`, locked SHA-256 `d1866a667d7a24b8c5ae5b7670486b8b312e6f4a8fbce457763668e84d843bd4`, blob `d8feba3692ebe25afd0e51f5e3ab32358ea19ded`.
- Approved Jun acknowledgment image: `staging/story_shot_candidates/S02B_JUN_ACKNOWLEDGEMENT_TEST_01/城堡烛光下的专注侧颜.png`, SHA-256 `1af236000b271d327278e82bf3e744fee08bd49682966eb5fa75f731a67c46e7`.
- Approved Ning reaction B V002 image: `staging/story_shot_candidates/TAIL_NING_REACTION_TEST_01/TAIL_NING_REACTION_TEST_01_CANDIDATE_01_PO_APPROVED.png`, SHA-256 `cbac98a82763c6c930a3c820c917f4b9b8bc2ed300a49b48143b8b1cd9486c9c`.
- All 14 original PNGs used in reconstructed sequence independently validated against Story Shot Index or locked candidate exact delivery identity: SHA-256, Git blob, size and dimensions PASS, no unauthorized substitution.
- Source approved N21 941×1671 PNG dimension exception was not resized as a saved asset; conversion to 720×1280 is only for temporary editorial video frames.

## Deterministic editorial timeline

- Director Design: `docs/project_control/gates/P0_3_video_pipeline/s02_b_v006_cinematic_language_director_design_v0_2_2026-10-14.md`.
- Historical design EDL: `production/editorial_specs/S02_B_V006_CINEMATIC_ROUGH_EDL_V001.json` (retained untouched).
- Render resolved record: `production/editorial_specs/S02_B_V006_CINEMATIC_ROUGH_EDL_V002_RENDERED_RECONSTRUCTED_REVIEW.json`.
- Engineer source: `scripts/s02b_v006_editorial_rough_render_v001.py`.
- Workflow: `.github/workflows/s02b-v006-cinematic-reconstructed-rough-render-v001.yml`.
- Cut map: **17 nodes / 1927 contiguous frames / 30 fps**, no gaps or overlaps.
- NEW-01 insert **frames 996–1077** (82 frames, 33.200–35.933s) and Jun PO selected reaction frames 1078–1113.
- NEW-02 insert **frames 1299–1365** (67 frames, 43.300–45.533s), between N22 and N23.
- Ning reaction B V002 **frames 1810–1862** (53 frames, 60.333–62.100s).
- A06 now enters at **frame 1448** (48.267s), before N24 question. Video scene order is not an approval of transcript syllable alignment.
- Preexisting image masters, sound and existing approved MP4s were untouched.
- No universal repeated scale pulsing or GIF character micro-action; few mild video-only reframing moves, predominantly motivated hard cuts.

## Render run

- First engineering attempt Run `38569441905` failed before rendering, due to missing `ffmpeg` dependency on runner; historical source binary and EDL verification had passed. No video produced in that attempt.
- After adding explicit Ubuntu `ffmpeg` and Pillow install, **GitHub Actions Run `38569617657` SUCCESS**, all render, full decode and artifact upload steps passed.
- Workflow SHA commit: `903e6c5f46724129a0eab845eca830a84fc3f04e`.
- URL: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/38569617657
- Output Artifact ID: **`11897595436`**.
- Artifact name: **`S02B_V006_CINEMATIC_RECONSTRUCTED_ROUGH_REVIEW_V001`**.
- Artifact ZIP size: **8,571,085 bytes**.
- Artifact ZIP SHA-256: **`5c80a14adf5ae4762d05c8fdd5f730cfe53af9dfc54d65acd7fb738cc7852965`**.
- Artifact expires: **2026-10-21T13:11:58Z**.
- MP4 filename: `S02_B_V006_CINEMATIC_ROUGH_RECONSTRUCTED_REVIEW_V001.mp4`.
- Exact MP4 SHA-256: **`7af0982385c877b159f053233378b98c2c035ce19df257a6e65077dfbaa33402`**.
- MP4 size: **8,712,713 bytes**.
- Format: H.264 720×1280, 30 fps, **1,927 video frames**; AAC, **3,013 audio packets**; full container duration **64.250 s**.
- ffmpeg full video decode + audio decode: **PASS**.

## Independent post-download Artifact checks

The actual GitHub Actions Artifact `11897595436` ZIP was downloaded through GitHub and inspected independently:
- ZIP file length matches GitHub (8,571,085 bytes).
- Original ZIP SHA-256 matches recorded GitHub artifact digest, **MATCH**.
- ZIP CRC integrity **PASS**.
- ZIP contains exactly output MP4 and `RENDER_MANIFEST.json`.
- Original MP4 extracted without re-encoding. Byte size and independently recalculated SHA-256 agree with the embedded render manifest and workflow log.
- Independent `ffprobe` confirms H264 1927 frames, 720×1280 30fps, AAC, 64.250-second container.
- Independent `ffmpeg -xerror` whole-file video+audio decode: **PASS**.
- **AAC packet-level exact comparison with approved V001 source:** both have exactly **3,013 packets**; for every packet its payload SHA-256, duration and pts_time are identical in V001 and the V006 rough review. This independently proves **no audio change in packet contents or timing** relative to the approved V001 stream.

## Governance / approval boundary

**Current final disposition: V006 RECONSTRUCTED ROUGH CUT / TECHNICAL PASS / READY FOR FULL-CONTEXT PO VIEWING / NOT A PO-APPROVED FINAL VIDEO.**

- Production Video Index unchanged (Git blob `84fb0f70ebd92536b95c6b01c6ac69a27a6986c7` at checkpoint).
- No overwrite or replacement of `S02_B_ASSEMBLY_APPROVED_V001.mp4`.
- NEW-01, NEW-02, N16–N26 Story Shot registrations and original PNGs unchanged.
- No canonical review MP4 publication, no final registration, no main merge.
- Next decision: PO reviews entire 64.25s clip, particularly NEW-01/N20 handoff, NEW-02 crowd camera, N23→A06 on turn, A06→N24 vocal J-cut, and Ning B V002 tail. Any change remains a fresh noncanonical review iteration until separate PO authorization.
