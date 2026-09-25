# P0.3 Progress Closeout｜2026-09-25

Status: `IN PROGRESS / CINEMATIC AUDIO-COMIC ROUTE ACTIVE / NOT YET VALIDATED`

## 1. Why the P0.3 direction changed

The real four-shot proof:

`A01 → Wide → Tight → A02`

confirmed that single-image 2.5D / DepthFlow cannot be the current main production route for character shots.

Product Owner review:

- characters visibly deformed across the sequence;
- the route was explicitly judged unacceptable;
- technical success of a renderer is not sufficient evidence of production usability.

Therefore:

`CHARACTER-SHOT 2.5D = REJECTED AS CURRENT MAIN PRODUCTION ROUTE`

The 2026-09-23 technical evidence remains historical evidence; it is not deleted or rewritten.

## 2. Current P0.3 main validation route

P0.3 now validates a cinematic audio-comic workflow:

`canonical story/audio → story beat → composition → automatic minimum-reference retrieval → Story Shot generation → PO review → targeted local edit if needed → approved Story Shot → edit`

Key boundaries:

- original audiobook remains the audio foundation;
- no AI dubbing and no source-audio speed change;
- visual flow is driven by changing story information, not by mechanically moving one still;
- normal cuts are valid;
- crop / restrained zoom are visual-reading tools;
- Remotion remains the edit / timing / audio / SFX / output layer;
- AI video may later enhance selected key shots but is not the current blocker.

## 3. Story Shot asset model approved

Product Owner approved one unified logical asset class:

`STORY_SHOT`

A01–A07 and later N01-style images are the same kind of narrative composition asset.

Rules:

1. A / N prefixes are historical IDs only; they do not create separate asset systems.
2. Only Product Owner-approved Story Shots enter the formal library and index.
3. Candidate / rejected / WIP images do not enter the formal library and are not registered.
4. Approved Story Shots must be retrievable later as continuity / composition references.
5. Existing A01–A07 paths remain unchanged to avoid breaking historical references.
6. Do not duplicate A01–A07 binaries merely to normalize paths.
7. A unified index provides the logical Story Shot library across legacy and new paths.

Unified index:

`production/image_library/approved/story_shots/story_shot_index.json`

## 4. N01 production result

N01 was iteratively corrected by targeted local edits rather than full-image regeneration.

Final Product Owner review:

- Ning Qiushui identity consistency: PASS;
- Jun Luyuan identity consistency: PASS;
- Jun Luyuan pose: PASS;
- final N01: PRODUCT OWNER APPROVED.

Narrative definition:

- Neil has completed the welcome speech and waits at / near the doorway;
- the 16 visitors remain outside and observe the surroundings;
- Jun Luyuan stands beside Ning Qiushui;
- group attention is distributed across the environment rather than uniformly toward Neil.

Approved source identity:

- target filename: `N01_CASTLE_PAUSE_APPROVED_V001.png`
- dimensions: 941 × 1672
- byte size: 2,687,303
- SHA-256: `a96d52410c1645711545c80b7fe4e3eaa3e8f00b088ebaaea210bbdbec84557b`

Target canonical path:

`production/image_library/approved/story_shots/N01_CASTLE_PAUSE_APPROVED_V001.png`

Current publication boundary:

`PO APPROVED / EXACT SOURCE LOCKED / CANONICAL BINARY PUBLICATION PENDING`

Do not regenerate, re-encode, resize or screenshot the approved N01 source during publication.

## 5. Current proof objective

Do not mass-produce additional Story Shots yet.

Next representative proof:

`A01 + A02 + N01 + canonical audio → Opening Audio-Comic Proof`

The proof must answer:

- does the visual reading flow follow the story;
- does the edit still feel like a slideshow;
- are cuts / crops / restrained zoom sufficient for this opening;
- where are additional Story Shots actually required.

Only after this proof is reviewed should full-chapter Story Shot coverage expand.

## 6. P0.3 gate status

P0.3 remains:

`IN PROGRESS / NOT YET VALIDATED`

No P0.3 PASS claim is made.

## 7. Resume point

1. publish the exact approved N01 binary and verify SHA / byte size;
2. change N01 index publication status from pending to canonical;
3. build the Opening Audio-Comic Proof;
4. Product Owner reviews narrative flow and slideshow risk;
5. then determine the next missing Story Shot(s).

