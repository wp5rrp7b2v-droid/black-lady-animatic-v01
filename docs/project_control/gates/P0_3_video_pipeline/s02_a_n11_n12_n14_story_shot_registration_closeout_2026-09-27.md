# S02-A｜N11 / N12 / N14 Story Shot Registration Closeout

Status: `COMPLETE / RC-024 FOUR GATES PASS`

Date: 2026-09-27

## 1. Scope

This closeout formalizes the three Product Owner-approved S02-A Story Shots:

- N11 Candidate 03
- N12 Candidate 02
- N14 Candidate 01

N13 remains cancelled / rejected and is not registered.

## 2. Gate 1｜Product Owner approval

PASS.

- N11 Candidate 03: APPROVED
- N12 Candidate 02: APPROVED
- N14 Candidate 01: APPROVED

## 3. Gate 2｜Canonical binary published

PASS.

Correct original source upload commit:

`ebe1361664f27dd1fa17b866e0d529f7128abf46`

Upload verification workflow commit:

`bcf71b71047d783ac8074c2cbdb7480c1ebd5fdf`

Upload verification:

- run: `36324358350`
- job: `108634127720`
- result: `SUCCESS / OVERALL_RESULT=PASS`
- artifact: `N11_N12_N14_UPLOAD_VERIFICATION_V001`
- artifact ID: `10933591429`
- artifact digest: `sha256:363db1043e92ef5e14c59a4bc9fe57b93c7875d190be23567334b51cc08cca3b`

Verified exact source identities:

| Shot | SHA-256 | Bytes | Git blob | Dimensions |
|---|---|---:|---|---|
| N11 | `09d45c1b27fbd2aea68c818677d9656a2ae7f39296f80f6db622118312aebcc5` | 2538801 | `f5efde465dcadd1490f2064c6db39e1d5f194dc6` | 941×1672 |
| N12 | `d94dc3623ba1abc55aa86c8b646d7876d097433bfadb70291bfa9c68cffc030b` | 2434337 | `853d04f5ed8a2e1845ce1dfa9cef5c02f123124b` | 941×1672 |
| N14 | `0474003a1d6d48a652935033f17560d0ee1d689caadbdb7d4af72560477844f1` | 2500282 | `e32c03bc21efcd0eda98d2e9868a64915583b19f` | 941×1672 |

Canonical exact-blob publication commit:

`caff3cef027366b75e2ced5b04f363ed6a89b5f6`

Canonical files:

- `production/image_library/approved/story_shots/N11_NEIL_ABNORMAL_PORTRAIT_APPROVED_V001.png`
- `production/image_library/approved/story_shots/N12_NEIL_CROSS_RIGID_SMILE_APPROVED_V001.png`
- `production/image_library/approved/story_shots/N14_FIRST_ENCOUNTER_IMPORTANCE_APPROVED_V001.png`

Exact Git blobs were reused. No PNG re-encode occurred.

The first incorrect upload batch from commit `1e91d5f33017122e78196ed573a8f4d80e3aca9d` was not registered; those temporary binaries were removed from the current tree during canonical publication.

## 4. Gate 3｜Story Shot Index registered

PASS.

Registration commit:

`f301eff807434552e52d78070a8d06e492c1ae06`

Index:

`production/story_shots/story_shot_index.jsonl`

Records added:

`N11 / N12 / N14`

Registered Story Shot count after this batch:

`20`

N13 is intentionally absent.

## 5. Gate 4｜Registration verification

PASS.

Registration verification workflow commit:

`a9906c814d7093d8302b8afa2274bc5e63444f38`

Verification:

- run: `36324545377`
- job: `108634649651`
- conclusion: `SUCCESS`
- artifact: `N11_N12_N14_REGISTRATION_VERIFICATION_V001`
- artifact ID: `10933043856`
- artifact digest: `sha256:f0ec1acc11572c3127067af58d0cdedafe21f672118a8c29da16d168b5bdf3e1`

Log result:

- `N11_PASS ... INDEX_MATCH=YES`
- `N12_PASS ... INDEX_MATCH=YES`
- `N14_PASS ... INDEX_MATCH=YES`
- `STAGING_CLEANUP_PASS`
- `OVERALL_RESULT=PASS`

## 6. RC-024 result

All four completion gates are satisfied:

1. PRODUCT_OWNER_APPROVED = PASS
2. CANONICAL_BINARY_PUBLISHED = PASS
3. STORY_SHOT_INDEX_REGISTERED = PASS
4. REGISTRATION_VERIFICATION_PASS = PASS

Therefore:

`N11 / N12 / N14 = FORMALLY ARCHIVED / REGISTERED / CURRENT`

## 7. End-of-day boundary

S02-A remains in progress.

Current formal sequence:

`N11 → N12 → A04 → N14 → N15 → A05`

N13 remains cancelled.

N15 Director Shot Design V0.1 is not approved. Before continuing N15, resume with the source-novel fact check requested by the Product Owner:

`verify which door ultimately requires the key for escape, then redesign N15 if needed.`
