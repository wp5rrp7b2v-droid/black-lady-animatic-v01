# Story Shot Registry

Logical asset class: `STORY_SHOT`

Rules:
- A/N prefixes are historical IDs only.
- Only Product Owner-approved Story Shots are registered here.
- Candidate / rejected / WIP images are excluded.
- Legacy A01–A07 remain in `production/image_library/approved/A_Series/` and are not duplicated or renamed.
- New approved Story Shots use `production/image_library/approved/story_shots/`.
- `story_shot_index.jsonl` is the machine-readable logical index.

Current approved Story Shot count: **12**
- A01–A07: 7 legacy approved Story Shots
- N01–N05: 5 approved Story Shots

Opening Audio-Comic Proof sequence:
`A01 → A02 → N02 → N03 → N04 → N05 → N01`

Canonical N-series files:
- `N01_CASTLE_PAUSE_APPROVED_V001.png`
- `N02_NEIL_CONTINUED_EXPLANATION_APPROVED_V001.png`
- `N03_VISITOR_REACTION_APPROVED_V001.png`
- `N04_NEIL_WELCOME_CLOSING_APPROVED_V001.png`
- `N05_NEIL_TURN_THRESHOLD_ACTION_APPROVED_V001.png`

Binary verification:
- N01 locked SHA-256: `a96d52410c1645711545c80b7fe4e3eaa3e8f00b088ebaaea210bbdbec84557b`; rechecked by GitHub Actions on 2026-09-26: **SHA_MATCH**.
- N02–N05 exact uploaded binaries were verified by GitHub Actions run `36232083006` before canonical registration.
- N02–N05 canonical renames reuse the exact uploaded Git blobs; no re-encode or binary mutation occurred.

N05 boundary:
- Interior decorative details visible in N05 are shot-background expression only.
- They do **not** become canonical Scene Facts unless separately approved and registered.
