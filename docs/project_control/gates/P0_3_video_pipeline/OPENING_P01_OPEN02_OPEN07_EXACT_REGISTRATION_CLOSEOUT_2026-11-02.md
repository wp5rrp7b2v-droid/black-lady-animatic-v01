# Opening P01 OPEN-02—OPEN-07｜Exact Binary Canonical Publication & Story Shot Registration Closeout
Date: 2026-11-02
Status: **COMPLETE / 6 PO APPROVED / 6 ORIGINAL PNG EXACTLY PUBLISHED / 6 UNIQUE INDEX ROWS / INDEPENDENT GITHUB ACTIONS SUCCESS**
Scope: Opening P01's six story frames only, not full video/audio approval nor overall P0.3 Gate PASS.

## Product Owner decision and source
Product Owner on 2026-11-02 approved all six final corrected outputs and explicitly authorized **no further correction to 05**. Six images were manually uploaded by the Product Owner directly to GitHub `main` under `staging/story_shot_candidates/OPENING_P01_02_07/`. Google Drive was not used for this intake, publication, or verification.

Source files retained their actual candidate sequence numbers 02/C02, 03/C01, 04/C01, 05/C03, 06/C02, 07/C01; filename changes do not modify binary content.

## Independently verified actual PNG identities
| OPEN | Final selected output | Exact bytes | Dimensions | Original SHA-256 | Git blob SHA-1 | Canonical name |
|---|---|---:|---|---|---|---|
| 02 | Candidate 02 | 1858578 | 941×1672 | `46cf528130b8517640ed5a1e8a4cc5353a3c52bebf454ce7342ee6b73308213b` | `73508692f0020e19668f7c6a18a4ddc47fb5d1c0` | `OPENING_P01_OPEN_02_JUN_RESOLVE_APPROVED_V001.png` |
| 03 | Candidate 01 | 1996398 | 941×1672 | `887269a8901cf2c31eefb66fc85948c6c418f38db958e56b2b86c19206839e82` | `8b6cfc1c99f1a53adac8134fd04c7932bd6ed1a6` | `OPENING_P01_OPEN_03_BAI_CAUTION_APPROVED_V001.png` |
| 04 | Candidate 01 | 1843383 | 941×1672 | `3ca90105eac44518bdb2fda53f5d4d807909b32184e6408fd560d3cd613971ed` | `31d1f560da5f2f7b34469ea2ae7776c8081dc23e` | `OPENING_P01_OPEN_04_NING_VOLUNTEERS_APPROVED_V001.png` |
| 05 | Candidate 03 | 1911603 | 941×1671 | `e8f240159c4c8fce8bc5131db1ed1c79c401a93eaf744926efe674d7f90596aa` | `2bc55d0ffb1e9ac32bed51ae9c7b07442d28e94e` | `OPENING_P01_OPEN_05_JUN_GRATEFUL_APPROVED_V001.png` |
| 06 | Candidate 02 | 2028458 | 941×1672 | `81fc76ad24933ae6045867a3b2f4300ed2061a123e5fff59bf7505e3b2aba38c` | `b1b4a61518ee1f86ae3bde33643bbb741d3a591c` | `OPENING_P01_OPEN_06_JUN_BURDEN_APPROVED_V001.png` |
| 07 | Candidate 01 | 2101419 | 941×1672 | `f63487a767d93dbb8bb10ef9eca36c45e6ffff39ca43f309150d805472645140` | `bf1bb114a32865edadbee49a4a1a685ff8d2ee53` | `OPENING_P01_OPEN_07_DECISION_CLOSE_APPROVED_V001.png` |

Original 05 is **941×1671** with an approved one-pixel height exception. Exact original kept; no resizing, padding, re-encoding or visual modification. The other five retain their actual original 941×1672 PNGs.

## Actual GitHub evidence
- Source preflight Actions **41454472126**, job **125307522512**, SUCCESS: independently computed SHA-256, validated original uploaded Git blob, exact byte size, PNG signature and dimensions, six unique image identities.
- Canonical publication + Story Shot Index and audit events committed atomically at `5c7f1aacadb6f2257d22cd3b847dc97ac2669c66`; Git tree directly reuses all six original Git blob IDs, without new image generation.
- Canonical directory: `production/image_library/approved/story_shots/`.
- Story Shot Registry: `production/story_shots/story_shot_index.jsonl`, **36→42**, one APPROVED/CURRENT record for each `OPENING_P01_OPEN_02` through `OPENING_P01_OPEN_07`.
- Audit log: `production/asset_registry/audit_event_log.jsonl`, **200→218** (6 approvals, 6 canonical publications, 6 registrations).
- Post-registration independent Actions **41455337719**, job **125310474154**, SUCCESS, `OPENING_P01_02_07_REGISTRATION_EXACT_PASS__42_STORY_SHOTS`. It reread all six staging originals, checked source PNG hash/blob/size/shape, verified that each canonical PNG is **byte-for-byte identical** to its corresponding original, confirmed all six index records are unique APPROVED/CURRENT, and confirmed 42 total rows.
- Related preexisting regressions all SUCCESS on publication commit: first P01 JPEG **41455337643**, Bai C06 **41455337573**, Bai 3Q-left **41455337723**, Bai PROFILE_LEFT **41455337510**. The old OPEN01 verification was made count-growth safe without changing its binary identity checks.

## Unchanged and open gates
- P01 OPEN01 approved JPEG and residential Scene Anchor unchanged; original 192.257s approved audio untouched; previously published other Story Shots unchanged.
- Formal Videos Index remains **3**, original Opening V001 not replaced. No new video was created or claimed approved.
- Remaining next proof: build/read an Opening P01 six-frame audiovisual assembly using approved original audio and review actual dialogue/shot cuts for timing and cinematic continuity. Approximate shot timestamps are not independently locked word-level EDL.
- P0.3 stays **IN PROGRESS**. Today's Mac local sync has **not** been independently confirmed; GitHub main remains canonical, and local sync requires user terminal evidence.
- No Google Drive access was performed for this batch.

**Minimum proof achieved:** six PO-approved originals manually uploaded to GitHub were exact-binary published and uniquely registered; independent CI proved 6/6 original↔canonical equality and 42-index consistency.
