# S02-B｜宁秋水反应插镜 Candidate 01｜GitHub Exact Intake & Local A/B Trial

Date: 2026-10-13

**STATUS: CANDIDATE INTAKE VERIFIED EXACT / LOCAL NONCANONICAL A-B GENERATED / EDITORIAL TEST AWAITING PO APPROVAL / NO CANONICAL PUBLICATION / NO MASTER MODIFICATION**

## 1. PO-approved image / GitHub staging

Original Product Owner-approved `TAIL_NING_REACTION_TEST_01 Candidate 01` remains a **test-only insert**, not a replacement for approved N26.

Candidate local file (original uploaded source renamed by byte-for-byte copy only): `TAIL_NING_REACTION_TEST_01_CANDIDATE_01_PO_APPROVED.png`.

- GitHub staging path: `staging/story_shot_candidates/TAIL_NING_REACTION_TEST_01/TAIL_NING_REACTION_TEST_01_CANDIDATE_01_PO_APPROVED.png`
- User's GitHub upload commit: `b12d5c51cac78d4cda052c0b3df829086bc35cfc`
- GitHub file size: **2,471,479 bytes**
- GitHub blob SHA: `907c4cdbd875d67399258dceb29eedd9f8038946` — EXACT approved local blob MATCH.
- On-run recomputed SHA256: `cbac98a82763c6c930a3c820c917f4b9b8bc2ed300a49b48143b8b1cd9486c9c` — EXACT approved source MATCH.
- PNG dimensions: **941×1672**.
- Candidate delivery spec: `production/candidate_delivery_specs/TAIL_NING_REACTION_TEST_01_CANDIDATE_01_DELIVERY_V001.json`.
- GitHub URL: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/blob/main/staging/story_shot_candidates/TAIL_NING_REACTION_TEST_01/TAIL_NING_REACTION_TEST_01_CANDIDATE_01_PO_APPROVED.png

## 2. Actions exact intake evidence

- Workflow: Story Shot Candidate Intake Verifier
- Trigger: User's staging PNG upload / push
- Run: **38400935301**
- Job: **115308072859**
- Run final status: completed / success
- Logs: `CANDIDATE_INTAKE_VERIFIED=TRUE`
- Logs match `SHOT_ID`, candidate path, PNG bytes, dimensions, SHA256 and blob to approved source.
- Evidence Artifact ID: **11814559907**
- Evidence Artifact name: `STORY_SHOT_CANDIDATE_INTAKE_VERIFICATION`
- Artifact ZIP GitHub digest: `sha256:dd549e67110c3288a5b5db16952da3fb430d7ed025a483028124f8994796ca50`
- Independently downloaded Artifact ZIP digest: EXACT MATCH (same SHA256).
- ZIP `testzip()`: PASS
- `candidate_intake_verification.json`: `candidate_intake_verified=true`; all eleven bool checks true; expected_identity === actual_identity for exact binary fields.
- This PASS is the GitHub-side candidate staging identity check only. It does **not** elevate the test candidate to formal Story Shot.

## 3. Controlled local A/B comparison

Two **local, noncanonical, review-only MP4 excerpts** derived from the already approved canonical S02-B V001 master:

Approved master: `S02_B_ASSEMBLY_APPROVED_V001.mp4`, SHA256 `8ec47720b5641412b2ebd1e082bf058244d6b07fbe97500b56a8ef830bf2042a`, duration 64.250 s, 720×1280 30fps.

Source Review Manifest (GitHub Actions run 37894629986, Artifact 11600040686) lists N25 relative timeline 56.49–60.34 and N26 60.34–64.25. Manifest explicitly marks cut policy `EDITORIAL PROVISIONAL / NOT EXACT SPEECH ALIGNMENT`.

Both local A/B test exports:
- Trim the identical approved source range **56.466667–64.250 seconds**, 7.783 second output.
- Preserve audio content/order/continuity and relative timing; same AAC re-encoding settings for both test files. **Independently decoded PCM audio SHA256 is identical across A and B**: `229b550f5ce8689de72719e34e72e7e3471e7e8bedc518093633144390833baf`. No speech repeats/stretch/missing interval introduced between A and B.
- A: `S02B_NING_REACTION_AB_A_CANONICAL_TAIL_REVIEW.mp4` (**locally rendered excerpt of approved version**, not the original canonical video file), 453,502 bytes, SHA256 `f23a0738b3660cd1f68079aca3985173fc562e025d16b5f4663d3f87aaf64932`.
- B: `S02B_NING_REACTION_AB_B_INSERT_PROVISIONAL_V001.mp4`, 604,306 bytes, SHA256 `2822343f1ef9dea14ba2536fd108276a379fec8326edf87bcb233304a67fe4d6`.
- B overlays the independent Ning Candidate 01 PNG for approx **1.400 seconds** between original master absolute video times **60.333334–61.733334s** (relative preview 3.866667–5.266667s), between N25 visual exit and N26 continuation; normal picture resumes afterwards.
- Overlay candidate PNG is resized **only within the noncanonical review MP4** to the approved master's 720×1280 frame size; staging/original PNG remains untouched.
- Same timeline length; no new formal Story Shot ID, no changes to approved N25 or N26 PNG, no new registered N27.
- Visual quick-check: before and after insert, A/B frames are materially identical except minor normal codec context differences; during insert B shows approved Ning reaction; neither source master nor approved original PNG was modified.

**Critical editorial limitation:** 60.333334–61.733334 is a **trial cut chosen at N26 picture onset**, **NOT** measured character/word-level alignment for “这是夫人的要求”. Product Owner must view and decide the relative impact; final microcut placement remains to be aligned to the original voice line before any publication/version promotion. This trial is a proof-of-concept, not a final audio master.

Local A/B videos are exported to the conversation's container for PO review; **not uploaded to GitHub/Drive and not canonical**.

## 4. Immutable safeguards and next gate

- PO visually approved this Candidate 01 PNG; now GitHub **exact staging intake PASSED**.
- Next gate: **PO editorial A/B review** — evaluate whether reaction improves the rule beat and feels natural; if YES, separately authorize precise audio alignment / official new-video proposal, not overwrite approved V001.
- Story Shot Index presently has 32 records; **no `TAIL_NING_REACTION_TEST_01` record**.
- Video Index remains three approved records, unchanged.
- Approved S02-B V001 64.250 seconds remains exact immutable.
- Existing N25/N26 images remain canonical and unchanged.
- Tail V001/V002 experimental cuts remain NOT APPROVED / HOLD.
- No canonical image promotion, no Story Shot registration, no video master replacement, no P0.3 gate PASS.
