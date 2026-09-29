# N16 Scene Reference Design V0.1

Status: `DRAFT / READY FOR PRODUCT OWNER REVIEW / NOT LOCKED`

Date: 2026-09-29

## 1. Shot authority

Parent sequence:

`S02-B Director Shot Design V0.1 / PRODUCT OWNER APPROVED + LOCKED`

Shot:

`N16｜Sister Question`

Canonical source-audio scope:

`01:18.750 → 01:28.120`

Narrative function:

Jun Luyuan asks Ning Qiushui whether his sister previously worked in a place like this. Ning gives a restrained, brief response.

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

N16 uses an inward-facing two-character composition:

- Ning Qiushui: screen-left, facing / turning toward screen-right;
- Jun Luyuan: screen-right, facing / turning toward screen-left;
- Jun is the speaking emphasis;
- Ning remains clearly readable but visually calmer / secondary;
- medium two-shot;
- both characters are already inside / at the interior side of the castle entrance threshold;
- the still-open castle entrance may remain readable behind them as continuity, but must not dominate;
- Neil is not a subject in this shot.

This composition determines the directional atomic references below.

## 3. Required canonical reference set

### R1｜Jun Luyuan Character Reference Sheet

Asset ID:

`AST_IMG_000057`

Entity:

`CHAR_JUN_LUYUAN`

Role:

`CHARACTER_REFERENCE_SHEET`

Canonical path:

`production/image_library/derived_reference_sheets/jun_luyuan/CHAR_JUN_LUYUAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Registry state:

- approval_status: APPROVED
- lifecycle: CURRENT
- resolver_usage: DEFAULT
- provenance_status: COMPLETE
- SHA-256: `e8a0410cfc176ec9d6446b84f89b2c12d0683ec32b927c90353e850c416d909e`
- byte size: `969995`

Authority:

Primary Jun identity / hairstyle / clothing / body-proportion continuity across views.

Must not determine:

- final camera angle;
- final pose;
- castle geometry.

---

### R2｜Jun Luyuan FACE_3Q_LEFT

Asset ID:

`AST_IMG_000072`

Entity:

`CHAR_JUN_LUYUAN`

Role:

`FACE_3Q_LEFT`

Canonical path:

`production/image_library/character_references/jun_luyuan/CHAR_JUN_LUYUAN_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`

Registry state:

- approval_status: APPROVED
- lifecycle: CURRENT
- resolver_usage: DEFAULT
- provenance_status: COMPLETE
- SHA-256: `be9f1f39ae303a61a79746b25a0f9f8153797b179ef85d07a5c2fdf1ce02d01b`
- byte size: `2002451`

Authority:

Primary face-angle authority for Jun as the screen-right speaker looking toward Ning on screen-left.

Use intent:

Natural 3/4 conversational visibility rather than strict side-profile presentation.

Must preserve:

- young male identity;
- established hair shape;
- established facial proportions;
- non-melodramatic expression.

---

### R3｜Ning Qiushui Character Reference Sheet

Asset ID:

`AST_IMG_000060`

Entity:

`CHAR_NING_QIUSHUI`

Role:

`CHARACTER_REFERENCE_SHEET`

Canonical path:

`production/image_library/derived_reference_sheets/ning_qiushui/CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Registry state:

- approval_status: APPROVED
- lifecycle: CURRENT
- resolver_usage: DEFAULT
- provenance_status: COMPLETE
- SHA-256: `15ec6c2682da0fe2502267bde21e9bc0bd7104bbf3e6041521121cc69a0e77be`
- byte size: `1123635`

Authority:

Primary Ning identity / hairstyle / clothing / body-proportion continuity.

Must not determine:

- final pose;
- final camera;
- Jun placement;
- scene geometry.

---

### R4｜Ning Qiushui FACE_3Q_RIGHT

Asset ID:

`AST_IMG_000033`

Entity:

`CHAR_NING_QIUSHUI`

Role:

`FACE_3Q_RIGHT`

Canonical path:

`production/image_library/character_references/ning_qiushui/CHAR_NING_QIUSHUI_FACE_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`

Registry state:

- approval_status: APPROVED
- lifecycle: CURRENT
- resolver_usage: DEFAULT
- authority_class: AUXILIARY
- provenance_status: PARTIAL
- SHA-256: `7d2292494ab010b324e608f792912fd2d49766318e279bbe22170445464a5c1e`
- byte size: `2688985`

Authority:

Directional face reference for Ning on screen-left looking toward Jun on screen-right.

Boundary:

This is a valid CURRENT / DEFAULT resolver asset despite its migrated PARTIAL provenance. It supplements, but does not replace, the COMPLETE Ning Character Reference Sheet as primary identity authority.

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

- approval_status: APPROVED
- lifecycle: CURRENT
- resolver_usage: CONDITIONAL
- provenance_status: COMPLETE
- SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- byte size: `2305753`

Scene facts owned by this reference:

- large double main door;
- interior entrance connects directly through the threshold to exterior stone steps;
- exterior stone steps descend from the threshold;
- exterior court / road continues beyond;
- woods exist farther outside;
- current state is DAY;
- main door is OPEN.

Authority boundary:

Scene Master locks scene facts, not N16 photography. Camera position, focal length, character blocking, depth of field and local exposure remain shot-variable.

---

### R6｜A03 Story Shot — Interior Reverse Continuity

Story Shot:

`A03｜门内反拍`

Canonical path:

`production/image_library/approved/A_Series/A03_REBOOT_approved_v001.png`

Story Shot state:

- approval_status: APPROVED
- lifecycle: CURRENT
- byte size: `2875484`
- Git blob: `94d11064522425d908b1756fb0d845107c46a4e1`

Authority:

Shot-level continuity cue only:

- camera is on / near the interior side of the castle entrance;
- the entrance is read from inside rather than resetting to the exterior welcome staging;
- threshold direction remains compatible with the approved Opening / S02-A spatial continuity.

Authority boundary:

A03 does not override the Scene Master’s architecture or state facts and must not force N16 to copy A03 composition literally.

## 4. Minimum reference set decision

N16 minimum formal reference set:

`6 references`

1. AST_IMG_000057 — Jun Character Reference Sheet
2. AST_IMG_000072 — Jun FACE_3Q_LEFT
3. AST_IMG_000060 — Ning Character Reference Sheet
4. AST_IMG_000033 — Ning FACE_3Q_RIGHT
5. AST_IMG_000052 — Castle Entrance Scene Master / DAY_DOOR_OPEN
6. A03 — approved Story Shot continuity reference

This set is sufficient to establish:

- both identities;
- both wardrobe / body-continuity baselines;
- intended reciprocal face directions;
- canonical entrance geometry and open-door state;
- interior-side spatial continuity.

No additional reference is required for N16 V0.1.

## 5. Explicit exclusions

### N03｜Visitor Reaction

`EXCLUDE`

Reason:

Although it contains Ning + Jun together, N03 belongs to the exterior Opening state. Using it risks pulling N16 back outside and contradicting the locked S02-B interior-threshold continuity.

It is therefore not needed even as a composition reference.

### N14｜First-Encounter Importance

`EXCLUDE`

Reason:

N14 is useful for Ning’s recent S02-A state but includes Neil as the referent. N16 deliberately transfers narrative focus away from Neil. The COMPLETE Ning Reference Sheet + FACE_3Q_RIGHT already provide sufficient Ning authority without Neil leakage.

### A05｜No-Key Insert

`EXCLUDE`

Reason:

A05 owns the immediately preceding no-key reveal but is a prop/waist insert and contributes no useful N16 character or spatial authority.

### Neil references

`EXCLUDE ALL`

Reason:

Neil is not a subject in N16. Adding Neil references creates unnecessary subject leakage.

### First Hall Scene Master / A07

`EXCLUDE`

Reason:

N16 remains at the castle entrance / threshold zone. Full hall establishment belongs to a later sequence.

### MANOR_GATE references

`EXCLUDE`

Reason:

The manor perimeter gate is a different scene entity and has no authority over the castle entrance.

## 6. Generation-facing scene constraints

When N16 later enters Work generation, the Reference Delivery Bundle must communicate these constraints in addition to the six binaries:

- 9:16 vertical target;
- cinematic audio-comic still frame;
- medium two-shot;
- Jun screen-right / Ning screen-left;
- Jun speaking emphasis;
- Jun looks toward Ning;
- Ning calm, reserved, not comforting;
- both already on the interior side / threshold zone;
- open castle entrance may remain visible as secondary continuity;
- normal daylight entering from outside is allowed;
- no rain;
- no ominous storm;
- no Neil;
- no key / waist insert emphasis;
- no hall establishment;
- no mural corridor;
- no exaggerated dialogue gestures;
- no direct look to camera;
- no posed publicity-photo feeling.

## 7. Reference integrity requirements for later Bundle stage

The later N16 Reference Delivery Bundle must fail closed unless:

- all Asset Registry references still resolve to APPROVED + CURRENT;
- resolver_usage remains DEFAULT / CONDITIONAL as specified;
- exact canonical paths exist;
- SHA-256 matches registry values for R1–R5;
- byte size matches registry values for R1–R5;
- A03 path / byte size / Git blob match Story Shot Index;
- all copied PNG binaries are byte-identical to canonical sources.

If any identity check fails:

`GENERATION_ALLOWED = FALSE`

## 8. Review gate

Product Owner review is required before this reference design is locked.

Approval of this document would authorize only the next stage:

`N16 Reference Delivery Bundle Design`

It would not by itself authorize:

- Bundle construction;
- Work generation;
- candidate approval;
- formal publication / Story Shot registration.

Current disposition:

`N16 SCENE REFERENCE DESIGN V0.1 = READY FOR PRODUCT OWNER REVIEW / NOT LOCKED`
