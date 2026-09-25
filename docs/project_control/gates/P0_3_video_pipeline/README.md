# P0.3｜视频制作与剪辑 Pipeline 再验证

Status: `IN PROGRESS / CINEMATIC AUDIO-COMIC ROUTE ACTIVE / NOT YET VALIDATED`

Prerequisite:

- P0.1 = PASS / PRODUCT OWNER APPROVED
- P0.2 = PASS / PRODUCT OWNER APPROVED

P0.3 owns validation of the path from approved visual assets + canonical source audio to an acceptable final audiovisual result.

## Locked scope

P0.3 must validate, with real project material rather than design-only documentation:

- historical failure review;
- story-beat / shot planning against canonical source audio;
- canonical source-audio retrieval and extraction;
- approved Story Shot production and continuity;
- edit / framing / crop / restrained zoom as visual-reading tools;
- optional AI video / motion generation only where it materially improves selected shots;
- Remotion responsibility boundary;
- timing / continuity / dialogue completeness;
- a representative real audiovisual result as feasibility evidence.

## Historical evidence retained

2026-09-23 established:

- more stills + hard cuts alone can remain slideshow-like;
- Remotion bitmap pan / zoom is not a spatial reconstruction engine;
- A01 DepthFlow single-shot 2.5D was technically viable enough to test further.

2026-09-25 superseding artistic evidence:

- the real `A01 → Wide → Tight → A02` 4-shot 2.5D sequence caused visible character deformation;
- Product Owner judged the character-shot 2.5D route unacceptable;
- character-shot single-image DepthFlow / 2.5D is therefore no longer the current main production path.

This does not erase the technical evidence. Environment-only parallax may still be used selectively if useful.

## Current main validation route

`CINEMATIC AUDIO COMIC`

Core production logic:

`canonical story/audio → story beat → composition → automatically retrieve minimum necessary approved references → generate Story Shot → Product Owner PASS/FAIL → targeted local edit only when needed → approved Story Shot library → edit`

Rules:

- story determines composition;
- composition determines which references are needed;
- candidates / rejected / WIP do not enter the formal library;
- only Product Owner-approved Story Shots are stored and indexed;
- once composition and identities are basically correct, small fixes use local edit / inpainting rather than full-image regeneration;
- normal cuts remain valid;
- crop / restrained zoom guide viewer attention; they are not treated as fake physical camera reconstruction;
- AI video remains an optional enhancement for selected key shots, not the current blocker;
- Remotion remains compositor / timing / canonical-audio / SFX / output layer.

## Story Shot model

A01–A07 and later N01-style additions are one logical asset class:

`STORY_SHOT`

A / N prefixes are historical IDs only. They do not represent different asset systems.

- Existing A01–A07 paths remain unchanged to avoid breaking historical references.
- New approved Story Shots use the generic approved Story Shot storage root.
- A unified Story Shot index makes all approved Story Shots retrievable by story beat, characters, scene and continuity.
- Do not duplicate A01–A07 binaries merely to normalize directory layout.

Index:

`production/image_library/approved/story_shots/story_shot_index.json`

## Current approved addition

`N01` = Product Owner approved.

Narrative function:

- Neil has finished the welcome speech and moved to / waits at the castle doorway;
- the 16 visitors remain outside, curiously observing the surroundings;
- Jun Luyuan stands beside Ning Qiushui;
- Ning Qiushui and Jun Luyuan identity consistency passed Product Owner review;
- Jun Luyuan final pose passed Product Owner review.

Approved source identity:

- PNG
- 941 × 1672
- 2,687,303 bytes
- SHA-256: `a96d52410c1645711545c80b7fe4e3eaa3e8f00b088ebaaea210bbdbec84557b`

Canonical binary publication is the remaining closeout step for N01.

## Immediate next step

1. publish the exact approved N01 binary to the canonical Story Shot path and verify SHA / byte size;
2. finalize the unified Story Shot index against the published binary;
3. build the Opening Audio-Comic Proof using existing approved A01 + A02 + N01 + canonical audio;
4. judge pacing, visual-reading flow and slideshow risk before generating more Story Shots;
5. only then expand full-chapter visual coverage.

See:

- `p0_3_progress_closeout_2026-09-23.md`
- `p0_3_progress_closeout_2026-09-25.md`

No P0.3 PASS claim is permitted until representative production evidence is sufficient and Product Owner explicitly approves the Gate.
