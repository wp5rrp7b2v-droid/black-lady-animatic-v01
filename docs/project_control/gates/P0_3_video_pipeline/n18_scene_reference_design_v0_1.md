# N18｜Scene Reference Design V0.1

Status: `DRAFT / READY FOR PRODUCT OWNER REVIEW`

Date: 2026-09-29

## 1. Shot authority

Parent sequence:

`S02-B Director Shot Design V0.1 / PRODUCT OWNER APPROVED + LOCKED`

Shot:

`N18｜Clear-Sky Doubt`

Canonical source-audio scope:

`01:40.700 → 01:46.720`

Narrative function:

Jun Luyuan observes that the weather looks fine and questions whether rain is likely.

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

N18 deliberately shifts away from the tight Ning-dominant dialogue cut-in.

Visual progression:

`N17 Ning close-up / warning → N18 Jun medium shot / gaze toward daylight outside`

Locked composition:

- Jun Luyuan is the sole clear primary subject;
- medium shot, profile / 3Q-profile oriented;
- Jun remains inside / near the interior side of the castle entrance;
- Jun turns his gaze toward the still-open main door and visible daylight outside;
- the open doorway / exterior daylight must be clearly readable enough to support the spoken thought that the weather appears fine;
- Jun remains more important than the architecture;
- exterior mood is calm, bright, apparently stable;
- no storm cue;
- no rain;
- no ominous weather treatment;
- main door remains OPEN.

Preferred directional logic:

- Jun is positioned toward the right or center-right of frame;
- his gaze travels toward screen-left / left-front where the bright opening is readable;
- the exterior daylight becomes the visual counterpoint to the audio warning already established.

## 3. Required canonical reference set

N18 is intentionally designed around a maximum of `5 formal visual references`, matching the currently known generation-interface limit.

### R1｜Jun Luyuan Character Reference Sheet

Asset ID:

`AST_IMG_000057`

Entity:

`CHAR_JUN_LUYUAN`

Role:

`CHARACTER_REFERENCE_SHEET`

Canonical path:

`production/image_library/derived_reference_sheets/jun_luyuan/CHAR_JUN_LUYUAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Exact identity:

- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- resolver_usage: `DEFAULT`
- provenance_status: `COMPLETE`
- SHA-256: `e8a0410cfc176ec9d6446b84f89b2c12d0683ec32b927c90353e850c416d909e`
- byte_size: `969995`
- Git blob: `d11db79f4ceab2bb52139bfb8805f7c8f09b0cfc`

Authority:

Primary Jun identity / hairstyle / wardrobe / proportion continuity.

---

### R2｜Jun Luyuan PROFILE_LEFT V002

Asset ID:

`AST_IMG_000063`

Entity:

`CHAR_JUN_LUYUAN`

Role:

`PROFILE_LEFT`

Canonical path:

`production/image_library/character_references/jun_luyuan/CHAR_JUN_LUYUAN_PROFILE_LEFT_DEFAULT_DEFAULT_V002.png`

Exact identity:

- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- resolver_usage: `DEFAULT`
- provenance_status: `COMPLETE`
- SHA-256: `8bc4ca3ab9f5f2b9e8603918c147211ad8234e80c0b527fa45c880879a8ee71c`
- byte_size: `1938522`
- Git blob: `8c2f2287412717a14ff54714bc38f7e1f3569518`

Authority:

Primary profile-direction authority for Jun turning his attention toward the open doorway / daylight at frame-left.

This is the preferred angle anchor for N18.

---

### R3｜Jun Luyuan FACE_3Q_LEFT

Asset ID:

`AST_IMG_000072`

Entity:

`CHAR_JUN_LUYUAN`

Role:

`FACE_3Q_LEFT`

Canonical path:

`production/image_library/character_references/jun_luyuan/CHAR_JUN_LUYUAN_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`

Exact identity:

- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- resolver_usage: `DEFAULT`
- provenance_status: `COMPLETE`
- SHA-256: `be9f1f39ae303a61a79746b25a0f9f8153797b179ef85d07a5c2fdf1ce02d01b`
- byte_size: `2002451`
- Git blob: `821c892ffea59ef0739f86585c6c5f8bd1168264`

Authority:

Secondary angle support when the final composition lands between strict profile and 3/4.

Use intent:

Keep Jun recognizable while allowing a more natural glance toward the doorway rather than forcing a rigid 90-degree profile.

---

### R4｜Castle Entrance Scene Master — DAY / DOOR OPEN

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

Exact identity:

- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- resolver_usage: `CONDITIONAL`
- provenance_status: `COMPLETE`
- SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- byte_size: `2305753`
- Git blob: `e4dafe096f5c5c8782257030a5a659aeec7808f9`

Authority:

- castle-entrance identity;
- main door OPEN;
- DAY state;
- bright exterior / threshold relationship;
- exterior stone-step / courtyard direction.

N18 specifically depends on this reference more strongly than N17 because the doorway / weather state is part of the visual beat.

---

### R5｜N16 Story Shot — Canonical Threshold Continuity

Story Shot:

`N16｜Sister Question`

Canonical path:

`production/image_library/approved/story_shots/N16_SISTER_QUESTION_APPROVED_V001.png`

Exact identity:

- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- dimensions: `941x1672`
- byte_size: `1942422`
- SHA-256: `b26fb7d64a60fbd28d39b0ae22f7c85df18d4f947f31a3591c847dd5e1acf406`
- Git blob: `44971dd53e37cd1b582bcf5094b0f09cb8e0647d`

Authority:

Canonical continuity for:

- Jun's current wardrobe;
- local entrance-side lighting;
- interior-threshold spatial state;
- established S02-B visual continuity.

Boundary:

N16 is continuity authority only. N18 must not repeat the N16 two-shot composition.

## 4. Why N17 is not a formal reference yet

`N17 Candidate 03` is Product Owner approved but its approved original PNG has not yet completed:

- GitHub upload;
- Exact Binary Verification;
- Canonical Publication;
- Story Shot Registration;
- Registration Verification.

Therefore N17 must not silently become a formal Bundle authority before evening archival.

This does not block N18 because the five canonical references above already cover all necessary identity, direction, scene-state and threshold-continuity facts.

## 5. Minimum reference set decision

N18 minimum formal reference set:

`5 references`

1. AST_IMG_000057 — Jun Character Reference Sheet
2. AST_IMG_000063 — Jun PROFILE_LEFT V002
3. AST_IMG_000072 — Jun FACE_3Q_LEFT
4. AST_IMG_000052 — Castle Entrance Scene Master / DAY_DOOR_OPEN
5. N16 — canonical threshold continuity

This set fits the current image-generation input ceiling without any temporary collage or controlled input reduction.

## 6. Explicit exclusions

Do not include:

- N17 approved-but-unpublished candidate;
- Ning character references;
- Neil character references;
- A03;
- N03;
- N14;
- A05;
- A06;
- A07;
- First Hall Scene Master;
- MANOR_GATE Scene Master;
- N19–N22;
- any weather reference depicting rain / clouds / storm;
- rejected or superseded candidates;
- internet / non-canonical references.

## 7. Generation interpretation locks

N18 should communicate:

`the weather visibly looks fine right now`

Jun:

- thoughtful rather than frightened;
- looking outward;
- mild uncertainty / questioning;
- not smiling broadly;
- not alarmed;
- no exaggerated gesture;
- no direct camera gaze.

Environment:

- calm daylight;
- blue / bright sky or sunlit exterior may be visible;
- no rain;
- no dark storm cloud;
- no lightning;
- no supernatural weather cue;
- open door remains clearly open.

Visual contradiction:

The picture should look safe enough that Jun's doubt makes sense.

The danger remains in the audio / prior warning, not in the weather image.

## 8. Authority precedence

1. `S02-B Director Shot Design V0.1`
2. `AST_IMG_000057` — Jun identity
3. `AST_IMG_000063` — preferred left-profile direction
4. `AST_IMG_000072` — 3/4-left angle support
5. `AST_IMG_000052` — DAY / DOOR_OPEN / exterior-light scene authority
6. `N16` — canonical S02-B threshold / wardrobe / local-light continuity

Conflict rules:

- Character Reference Sheet wins identity conflicts.
- PROFILE_LEFT / FACE_3Q_LEFT control gaze direction support.
- Scene Master wins doorway and weather-state conflicts.
- N16 cannot override Scene Master facts.
- Director Design controls final framing and narrative emphasis.

## 9. Proposed Bundle handoff

If Product Owner approves this Scene Reference Design:

Next step:

`N18 Reference Delivery Bundle Design V0.1`

Expected Bundle count:

`5 canonical references`

Expected generation target:

`N18 Candidate 01`

No Bundle has been built yet.

## 10. Review gate

Current disposition:

`N18 SCENE REFERENCE DESIGN V0.1 = READY FOR PRODUCT OWNER REVIEW`

Product Owner approval is required before Bundle design/build or Work generation.
