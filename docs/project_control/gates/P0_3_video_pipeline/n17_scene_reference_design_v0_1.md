# N17｜Scene Reference Design V0.1

Status: `DRAFT / READY FOR PRODUCT OWNER REVIEW`

Date: 2026-09-29

## 1. Shot authority

Parent sequence:

`S02-B Director Shot Design V0.1 / PRODUCT OWNER APPROVED + LOCKED`

Shot:

`N17｜Blood-Door Warning`

Canonical source-audio scope:

`01:28.120 → 01:40.700`

Narrative function:

Ning Qiushui stops the sister discussion and redirects Jun Luyuan to the practical Blood Door survival rules. Jun acknowledges that he remembers.

Production status:

`NEW STORY SHOT / NOT YET GENERATED`

This document defines reference authority only.

Not authorized here:

- Reference Delivery Bundle build
- Work image generation
- candidate approval
- Story Shot publication / registration
- S02-B assembly

## 2. Composition lock for reference selection

N17 is the direct conversational continuation of N16.

Locked visual relationship:

- Ning Qiushui remains on screen-left;
- Jun Luyuan remains on screen-right;
- Ning turns / faces screen-right toward Jun;
- Jun faces screen-left toward Ning;
- medium / medium-close two-shot;
- Ning is the primary visual subject;
- Jun remains clearly readable as listener but is secondary;
- camera may be slightly tighter and more Ning-weighted than N16;
- both remain inside / at the interior side of the castle entrance transition zone;
- the open entrance / daylight may remain as subordinate continuity but must not dominate;
- posture is restrained and practical;
- no large teaching gesture.

Visual progression from N16:

`Jun-speaking emphasis → Ning-speaking emphasis`

The cut should feel like the same conversation continuing, not a new location or reset.

## 3. Required canonical reference set

### R1｜Ning Qiushui Character Reference Sheet

Asset ID:

`AST_IMG_000060`

Entity:

`CHAR_NING_QIUSHUI`

Role:

`CHARACTER_REFERENCE_SHEET`

Canonical path:

`production/image_library/derived_reference_sheets/ning_qiushui/CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Registry state:

- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- resolver_usage: `DEFAULT`
- provenance_status: `COMPLETE`
- SHA-256: `15ec6c2682da0fe2502267bde21e9bc0bd7104bbf3e6041521121cc69a0e77be`
- byte_size: `1123635`
- Git blob: `b674733242ab5d603dc42c53b8f7582003064499`

Authority:

Primary Ning identity, hairstyle, wardrobe and body-proportion continuity.

Because N17 is Ning-dominant, this is the highest character-identity authority in the shot.

Must not determine:

- final camera;
- final pose;
- Jun placement;
- scene geometry.

---

### R2｜Ning Qiushui FACE_3Q_RIGHT

Asset ID:

`AST_IMG_000033`

Entity:

`CHAR_NING_QIUSHUI`

Role:

`FACE_3Q_RIGHT`

Canonical path:

`production/image_library/character_references/ning_qiushui/CHAR_NING_QIUSHUI_FACE_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`

Registry state:

- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- resolver_usage: `DEFAULT`
- authority_class: `AUXILIARY`
- provenance_status: `PARTIAL`
- SHA-256: `7d2292494ab010b324e608f792912fd2d49766318e279bbe22170445464a5c1e`
- byte_size: `2688985`
- Git blob: `6b6a802b67a966f8439c5b000f01d00be422f545`

Authority:

Directional facial authority for Ning on screen-left speaking toward Jun on screen-right.

Boundary:

This reference controls conversational face direction and facial structure support only. The COMPLETE Character Reference Sheet remains primary identity authority.

---

### R3｜Jun Luyuan Character Reference Sheet

Asset ID:

`AST_IMG_000057`

Entity:

`CHAR_JUN_LUYUAN`

Role:

`CHARACTER_REFERENCE_SHEET`

Canonical path:

`production/image_library/derived_reference_sheets/jun_luyuan/CHAR_JUN_LUYUAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Registry state:

- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- resolver_usage: `DEFAULT`
- provenance_status: `COMPLETE`
- SHA-256: `e8a0410cfc176ec9d6446b84f89b2c12d0683ec32b927c90353e850c416d909e`
- byte_size: `969995`
- Git blob: `d11db79f4ceab2bb52139bfb8805f7c8f09b0cfc`

Authority:

Primary Jun identity, hairstyle, clothing and body-proportion continuity.

N17 must keep Jun recognizable as the same listener from N16 even though he is visually secondary.

---

### R4｜Jun Luyuan FACE_3Q_LEFT

Asset ID:

`AST_IMG_000072`

Entity:

`CHAR_JUN_LUYUAN`

Role:

`FACE_3Q_LEFT`

Canonical path:

`production/image_library/character_references/jun_luyuan/CHAR_JUN_LUYUAN_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`

Registry state:

- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- resolver_usage: `DEFAULT`
- provenance_status: `COMPLETE`
- SHA-256: `be9f1f39ae303a61a79746b25a0f9f8153797b179ef85d07a5c2fdf1ce02d01b`
- byte_size: `2002451`
- Git blob: `821c892ffea59ef0739f86585c6c5f8bd1168264`

Authority:

Directional face reference for Jun on screen-right listening toward Ning on screen-left.

Use intent:

Natural attentive listening; not fear, shock or melodrama.

---

### R5｜Castle Entrance Scene Master — DAY / DOOR OPEN

Asset ID:

`AST_IMG_000052`

Entity:

`SCENE_CASTLE_ENTRANCE`

Role:

`SCENE_MASTER`

State:

`DAY_DOOR_OPEN`

Canonical path:

`production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`

Registry state:

- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- resolver_usage: `CONDITIONAL`
- provenance_status: `COMPLETE`
- SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- byte_size: `2305753`
- Git blob: `e4dafe096f5c5c8782257030a5a659aeec7808f9`

Scene facts owned by this reference:

- castle-entrance identity;
- large double main door;
- DAY state;
- main door OPEN;
- threshold / exterior-step relationship.

Authority boundary:

Scene Master locks scene facts, not N17 photography. N17 may frame tighter than N16 and may show only part of the doorway / environment.

---

### R6｜N16 Story Shot — Immediate Conversation Continuity

Story Shot:

`N16｜Sister Question`

Canonical path:

`production/image_library/approved/story_shots/N16_SISTER_QUESTION_APPROVED_V001.png`

Story Shot state:

- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- dimensions: `941x1672`
- byte_size: `1942422`
- SHA-256: `b26fb7d64a60fbd28d39b0ae22f7c85df18d4f947f31a3591c847dd5e1acf406`
- Git blob: `44971dd53e37cd1b582bcf5094b0f09cb8e0647d`

Authority:

Immediate previous-shot continuity:

- Ning remains screen-left;
- Jun remains screen-right;
- reciprocal conversational eye-line;
- same entrance-interior / threshold spatial state;
- same wardrobe and local lighting continuity;
- same quiet low-key conversational tone.

N17 must evolve the visual emphasis from Jun to Ning without appearing to relocate the pair.

Authority boundary:

N16 is a continuity reference, not a composition template.

N17 must not simply duplicate N16.

Required visual change:

- slightly tighter / more Ning-weighted framing;
- Ning becomes primary speaker;
- Jun becomes listener;
- practical vigilance replaces the more personal tone of N16.

## 4. Minimum reference set decision

N17 minimum formal reference set:

`6 references`

1. AST_IMG_000060 — Ning Character Reference Sheet
2. AST_IMG_000033 — Ning FACE_3Q_RIGHT
3. AST_IMG_000057 — Jun Character Reference Sheet
4. AST_IMG_000072 — Jun FACE_3Q_LEFT
5. AST_IMG_000052 — Castle Entrance Scene Master / DAY_DOOR_OPEN
6. N16 — immediate approved Story Shot continuity

This set is sufficient to establish:

- both identities;
- reciprocal face directions;
- Ning-primary / Jun-secondary dialogue relationship;
- canonical castle-entrance scene state;
- exact continuity from the immediately preceding approved Story Shot.

No additional reference is required for N17 V0.1.

## 5. Explicit exclusions

### A03｜门内反拍

`EXCLUDE`

Reason:

A03 was useful for N16 because there was not yet an approved S02-B predecessor.

N17 now has N16 as a stronger and more immediate continuity authority. Adding A03 would be redundant and could pull the framing back toward older entrance photography.

### N03｜Visitor Reaction

`EXCLUDE`

Reason:

N03 belongs to the exterior Opening state. It would introduce incorrect spatial bias.

### N14｜First-Encounter Importance

`EXCLUDE`

Reason:

N14 is Ning-focused but uses Neil as the visual referent. N17 must remain a Ning–Jun private rules conversation and must not reintroduce Neil.

### A05｜钥匙空特写

`EXCLUDE`

Reason:

N17 has already moved beyond the no-key reveal. Key / waist / pocket imagery has no authority over this shot.

### A07 / FIRST_HALL

`EXCLUDE`

Reason:

S02-B has not yet reached the hall-establishment narrative owner.

### Future N18–N22 material

`EXCLUDE`

Reason:

No future shot may influence N17 production before it exists and is approved.

## 6. Generation interpretation locks

N17 should communicate:

`experienced warning / restrained vigilance / practical familiarity`

Ning:

- calm;
- focused;
- experienced;
- speaking quietly and directly;
- no heroic posture;
- no lecturing performance.

Jun:

- attentive;
- listening;
- not frightened;
- not visibly distressed;
- no exaggerated reaction.

Do not visualize the survival rules literally.

Forbidden examples:

- rain overlays;
- wet-clothing imagery;
- floating rule text;
- fantasy warning symbols;
- staring-eye graphics;
- objects highlighted as “do not touch” props.

The rules live in the audio. The still image should show the interpersonal state.

## 7. Authority precedence

1. `S02-B Director Shot Design V0.1` — narrative / shot-function / framing intent
2. `AST_IMG_000060` — Ning primary identity authority
3. `AST_IMG_000033` — Ning required conversational direction
4. `AST_IMG_000057` — Jun primary identity authority
5. `AST_IMG_000072` — Jun required listening direction
6. `AST_IMG_000052` — scene geometry / DAY_DOOR_OPEN facts
7. `N16` — immediate shot-level spatial / wardrobe / lighting / dialogue continuity

Conflict rules:

- COMPLETE Character Reference Sheets win identity conflicts;
- atomic 3Q references control directional support;
- Scene Master wins castle-entrance state / architecture conflicts;
- N16 controls immediate shot-to-shot continuity but cannot override Character or Scene Master authority;
- Director Shot Design controls photography and narrative emphasis.

## 8. Proposed Bundle handoff intent

If Product Owner approves this Scene Reference Design, the next step is:

`N17 Reference Delivery Bundle Design V0.1`

Expected Bundle count:

`6 canonical references`

Expected generation target:

`N17 Candidate 01`

No Bundle has been built yet.

## 9. Review gate

Current disposition:

`N17 SCENE REFERENCE DESIGN V0.1 = READY FOR PRODUCT OWNER REVIEW`

Product Owner approval is required before:

- locking the six-reference set;
- creating N17 Bundle Spec;
- Generic Story Shot Bundle Builder execution;
- Work generation.
