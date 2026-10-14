# 《诡舍·黑衣夫人》｜S02-B V006 NEW-01｜Canonical Publication + Story Shot Registration + Independent Verification Closeout

Date: 2026-10-14

**FINAL: PRODUCT OWNER APPROVED / EXACT BINARY CANONICAL PUBLICATION PASS / STORY SHOT REGISTERED / INDEPENDENT VERIFICATION PASS / REVIEW-BRANCH CLOSEOUT COMPLETE / NO MAIN MERGE / VIDEO MASTER UNCHANGED.**

## 1. Authorized scope

The Product Owner expressly approved `V006 NEW-01 Candidate 01` **Exact Binary Canonical Publication, Story Shot Registration and Registration Verification**, preserving immutable SHA-256 `f3002984a377a31e05cd7490e914c0da4009509c8ddb5eaf45a5d45144775989` and Git blob `7fedcdc93f2b366d1a8597e86ffe8c99006ce027`. PO prohibited re-encoding/resizing/source editing, changing S02-B video masters, or merging `main`.

Publication and registration executed only on:
`review/s02b-jun-nod-insert-20261014`

## 2. Approved image and binary identity

- Shot ID: `S02B_V006_NING_WARNING_JUN_SHOULDER_OTS_TEST_01`.
- Candidate: NEW-01 Candidate 01; PO-approved original chat upload `烛光回廊里的轻声提醒(1).png`, GitHub staging filename `烛光回廊里的轻声提醒.png`.
- Canonical file: `production/image_library/approved/story_shots/S02B_V006_NEW01_NING_WARNING_JUN_OTS_APPROVED_V001.png`.
- Original size: **1,840,569 bytes**, dimensions **941×1672**, PNG.
- SHA-256 exact: **`f3002984a377a31e05cd7490e914c0da4009509c8ddb5eaf45a5d45144775989`**.
- Git blob exact: **`7fedcdc93f2b366d1a8597e86ffe8c99006ce027`**.
- Staging canonical copy operation: Git tree blob reuse, same SHA-1, without any re-encoding or new blob generation.
- GitHub publication commit: **`bf691be07dec671be0ebe95fbd1202c73a69566a`**, identified by GitHub commit file metadata as `renamed` / `changes=0`.
- Staging PNG removed. The staging README and approval evidence remain as historical audit data, not as a duplicate approved image.

## 3. Candidate Intake and authoritative reference Bundle

- Reference Bundle V001 Validation-only exact 5/5: Run `38540725413` SUCCESS.
- Formal Bundle V001 exact 5/5 and evidence: Run `38541197812`, Artifact `11882167307`, SUCCESS.
- Exact candidate intake: Run **`38549255960`**, job `115802904615`, **PASS**.
- Intake evidence Artifact **`11885418671`**, sha256 ZIP `ace9ff436b8925cdfe92dbaf5d8784d879b8743b097ad6393032886986d971d8`.

## 4. Canonical Publication independent verification

- Dedicated workflow: `.github/workflows/s02b-v006-new01-canonical-exact-publication-v001.yml`.
- Publication verification Run **`38550411737`**, job **`115806713023`**, **completed / success**.
- Run URL: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/38550411737
- Exact immutable target: publication commit `bf691be07dec671be0ebe95fbd1202c73a69566a`, verified separately after publishing, with Git rename detection disabled in `git diff` and `core.quotePath=false` for original Chinese staging basename.
- Verifier logs:
  - `NEW01_CANONICAL_PUBLICATION=PASS`
  - `SHA256_MATCH=YES`
  - `BLOB_MATCH=YES`
  - `DIMENSIONS_MATCH=YES`
  - `STAGING_CLEANUP_PASS`
  - `PUBLICATION_CHANGE_SCOPE=EXACT_TWO_PATHS`
  - `VIDEO_MASTER_UNCHANGED=YES`
- Evidence Artifact **`11886158054`**; ZIP SHA256 **`c190c9317cd750d2f488e0df7271c89968e7ce6db1584ca7b89724a5f92ca489`**.

**Transparent test recovery:** Initial publication workflow runs `38550158188`, `38550297215` failed due to the verification tool's misunderstanding of Git rename detection and Git's quoted non-ASCII pathname output. They did not flag an actual PNG mismatch. Workflow was fixed, then independently re-executed against the **same immutable exact publication commit**; `38550411737` succeeded. The earlier candidate-intake run `38550158473` was spuriously triggered by deletion of the staging PNG after exact-blob move and failed because expected candidate no longer exists in staging; the previously completed original staging intake `38549255960` remains the authoritative PASS. No re-upload or candidate change occurred.

## 5. Story Shot Index registration

- Registration file: `production/story_shots/story_shot_index.jsonl`.
- Registration commit: **`e9c7d8e66ba9d6e0bc27e9d9acee999560b2c9f1`**.
- New `shot_id`: **`S02B_V006_NING_WARNING_JUN_SHOULDER_OTS_TEST_01`**.
- New status: `STORY_SHOT / APPROVED / CURRENT`, scene `CASTLE_ENTRANCE_INNER_LOBBY`, characters `NING_QIUSHUI`, `JUN_LUYUAN`.
- Canonical binary path, size, SHA-256, Git blob and 941×1672 dimensions stored in exact new row.
- The index contained **32** prior rows and now has **33** rows, with exactly **one** NEW-01 row. The original 32 rows were preserved byte-for-byte in the original prefix.
- Provisional editorial placement **33.200–35.933s** (frames 996–1078), immediately before the separately approved Jun B V002 close-up, is an edit proposal, not an exact word-level audio alignment approval.

## 6. Independent registration verification

- Workflow: `.github/workflows/s02b-v006-new01-story-shot-registration-verification-v001.yml`.
- Run **`38550572156`**, job **`115807241318`**, **completed / success**.
- URL: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/38550572156
- Evidence Artifact **`11886273141`**, ZIP SHA256 `ba43a8ab63527e10f1c6ef14df92be515cdfb507e2b6653e99aa4d50631b8104`.
- Independent proof:
  - `NEW01_STORY_SHOT_REGISTRATION=PASS`
  - `SHA_MATCH=YES`
  - `BLOB_MATCH=YES`
  - `DIMENSIONS_MATCH=YES`
  - `INDEX_UNIQUENESS=PASS`
  - `PREEXISTING_INDEX_UNCHANGED=YES`
  - `STAGING_CLEANUP_PASS`
  - `VIDEO_MASTER_UNCHANGED=YES`
  - `REGISTRATION_OVERALL_RESULT=PASS`
- Registration commit changed **only** `production/story_shots/story_shot_index.jsonl`; approved PNG canonical path, all existing approved images, video assets and existing Video Index were not mutated.

## 7. GitHub readback / no-main-merge evidence

Independent post-registration GitHub tree and index readback:
- Canonical file still points to Git blob `7fedcdc93f2b366d1a8597e86ffe8c99006ce027`, 1,840,569 bytes.
- No original staging PNG remains.
- NEW-01 row found exactly once among 33 total Story Shot registrations.
- Video Index blob stayed `84fb0f70ebd92536b95c6b01c6ac69a27a6986c7`.
- `main` HEAD at this post-verification checkpoint remains **`2dc97261be34988d836a7c29840bc07af04df6c5`**, unchanged from pre-publication observation.
- `review/s02b-jun-nod-insert-20261014` at registration checkpoint HEAD **`e9c7d8e66ba9d6e0bc27e9d9acee999560b2c9f1`**; this gate's receipt commit will advance only the review-branch HEAD.

## 8. Final gate disposition

**NEW-01 formal Story Shot = APPROVED / EXACT-BINARY CANONICAL / REGISTERED / VERIFICATION PASS / PROJECT CONTROL GATE RECEIPT CLOSED on review branch.**

Explicit non-actions:
- **No merge to main**.
- **No S02-B V001/V003/V004/V005 master video alteration**.
- **No video rendering/V006 editorial approval**.
- **No re-encoding or alternate candidate**.
- **No approval for NEW-02**, which remains a separate storyboard/reference/bundle and Work candidate production task.

Next independent task: V006 NEW-02 Scene Reference and 5/5 Reference Delivery Bundle validation, subject to the appropriate PO approval gates.
