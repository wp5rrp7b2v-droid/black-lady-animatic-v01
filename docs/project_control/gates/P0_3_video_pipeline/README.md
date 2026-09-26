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

## Locked Work image-generation delivery chain

For formal Story Shot / visual generation executed in Work, the production path is locked as:

`GitHub canonical assets → Resolver / Registry validation → Reference Delivery Bundle → Work automatic PNG acquisition → image generation`

Operational boundary:

- GitHub remains canonical binary authority.
- Resolver / Registry selects and validates the minimum necessary CURRENT / APPROVED references.
- A traceable Reference Delivery Bundle transports the exact PNG binaries and their manifest to Work.
- Work generates only after the Bundle PNGs are materially available and validated.
- Direct private-GitHub PNG browsing/fetching is not the production baseline.
- Product Owner is not expected to routinely hand-pick, download, ZIP or re-upload canonical references.
- Delivery failure is fail-closed: no formal generation proceeds without the required verified references.
- Any temporary exception requires explicit provenance and Product Owner authorization.

This rule is project-level governance under RC-022 / BL-D-070 and applies to N03 and subsequent formal Work-based image generation.

## Story Shot model

Product Owner approved the following model on 2026-09-25:

- A01–A07 and later N01-style additions are one logical asset class: `STORY_SHOT`;
- A / N prefixes are historical IDs only and do not represent different asset systems;
- only Product Owner-approved Story Shots may enter the formal library and registration;
- candidate / rejected / WIP outputs do not enter the formal library or registration;
- existing A01–A07 must not be renamed or duplicated merely to normalize the model;
- later production must make approved Story Shots retrievable by story beat, characters, scene and continuity.

Implementation boundary for 2026-09-25:

`MODEL APPROVED / LIBRARY + INDEX IMPLEMENTATION DEFERRED TO NEXT SESSION`

No formal Story Shot index or N01 canonical registration is created as part of today's closeout.

Implementation status as of 2026-09-26:

`IMPLEMENTED / ACTIVE / N01 FORMALLY REGISTERED`

- machine-readable index: `production/story_shots/story_shot_index.jsonl`;
- registered approved Story Shots: A01–A07 + N01 = 8;
- A01–A07 remain at their legacy `production/image_library/approved/A_Series/` paths and are not duplicated;
- N01 canonical path: `production/image_library/approved/story_shots/N01_CASTLE_PAUSE_APPROVED_V001.png`;
- N01 canonical rename reused the exact uploaded Git blob `d55d2c218926c0b916c67d34979887315c351a1c`;
- N01 byte size = 2,687,303, matching the approved identity;
- locked approved SHA-256 remains `a96d52410c1645711545c80b7fe4e3eaa3e8f00b088ebaaea210bbdbec84557b`;
- direct SHA-256 recheck of the GitHub binary remains a non-blocking local verification item because the temporary GitHub Actions verifier failed before executing steps.

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

N01 is visually approved, canonically published and formally registered. Its approved source identity remains locked; GitHub byte size and exact Git-blob preservation are verified. Direct SHA-256 recheck remains pending local verification and is non-blocking for the Opening Audio-Comic Proof.

## Immediate next step

1. build the Opening Audio-Comic Proof using existing approved A01 + A02 + N01 + canonical audio;
2. judge pacing, visual-reading flow and slideshow risk before generating more Story Shots;
3. identify only the additional Story Shots actually required by the proof;
4. expand full-chapter visual coverage only after the representative proof is reviewed.

See:

- `p0_3_progress_closeout_2026-09-23.md`
- `p0_3_progress_closeout_2026-09-25.md`

No P0.3 PASS claim is permitted until representative production evidence is sufficient and Product Owner explicitly approves the Gate.
