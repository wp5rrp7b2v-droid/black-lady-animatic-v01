# N23｜Reference Delivery Bundle Design V0.1

Status: `DRAFT / WAITING PRODUCT OWNER APPROVAL / BUNDLE SPEC NOT AUTHORIZED`

Date: 2026-10-02

Target:

`N23｜Neil at the Open Door — Watches the Group Enter`

Parent authority:

- `N23 Node-Level Director Shot Design V0.2`
- `N23 Scene Reference Design V0.1`
- `S02-B Director Shot Design V0.3 + Review Patch 01`

Proposed Bundle ID:

`N23_REFERENCE_DELIVERY_BUNDLE_V001`

Target Candidate:

`N23 Candidate 01`

Builder:

`STORY_SHOT_REFERENCE_BUNDLE_BUILDER_V1`

---

## 1. DESIGN GOAL

Deliver the minimum canonical reference set required for Work to generate N23 while preserving:

- same-cohort continuity from N22;
- Castle Entrance / DAY_DOOR_OPEN scene facts;
- Neil identity;
- Guang Yong's low-weight backward-attention continuity.

The Bundle must not determine the composition by reference-image layout.

Composition authority remains the approved N23 Director Shot + Scene Reference Design.

---

## 2. PROPOSED REFERENCE SET

Reference count:

`4`

### Reference 01｜N22 canonical Story Shot

Source type:

`STORY_SHOT`

Reference identity:

`N22 / N22_PEOPLE_IN_THE_FLOW_APPROVED_V001.png`

Canonical path:

`production/image_library/approved/story_shots/N22_PEOPLE_IN_THE_FLOW_APPROVED_V001.png`

Exact identity:

- dimensions: `941 × 1672`
- byte size: `1,834,637`
- SHA-256: `6d1ed04106bb35943d752113e17d5f36fd2d55b29f4234e13177c7f8b6496f3a`
- Git blob: `a0f38041c10e4eb13a5a915a5d2f7bf22f85a2cf`
- approval_status: `APPROVED`
- lifecycle: `CURRENT`

Destination group:

`crowd_continuity`

Authority purpose:

`SAME_COHORT_CLOTHING_DENSITY_REALISM_WARM_DARK_CONTINUITY_ONLY`

It MAY prove:

- this is the same cohort;
- clothing world;
- broad body-proportion range;
- group density;
- human realism;
- warm-dark continuity;
- Guang Yong's already-established backward-attention behavior as visual evidence.

It MUST NOT prove:

- N23 camera position;
- N23 camera direction;
- N23 screen positions;
- N23 left/right layout;
- Su Xiaoxiao or Liao Jian prominence;
- exact blocking;
- exact gaze pattern;
- exact foreground/background assignment.

Hard rule:

`N22 IS CONTINUITY AUTHORITY, NOT A COMPOSITION TEMPLATE`

---

### Reference 02｜Castle Entrance Scene Master

Reference ID:

`AST_IMG_000052`

Source type:

`ASSET`

Entity:

`SCENE_CASTLE_ENTRANCE`

Role:

`SCENE_MASTER`

State:

`DAY_DOOR_OPEN`

Canonical path:

`production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`

Exact identity:

- byte size: `2,305,753`
- SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- Git blob: `e4dafe096f5c5c8782257030a5a659aeec7808f9`

Destination group:

`scene_authority`

Authority purpose:

`CASTLE_ENTRANCE_DOOR_IDENTITY_MATERIAL_SCALE_DAY_DOOR_OPEN_THRESHOLD_FACTS`

It locks scene facts only.

It does not lock N23 photography.

---

### Reference 03｜Neil Character Reference Sheet

Reference ID:

`AST_IMG_000059`

Source type:

`ASSET`

Entity:

`CHAR_NEIL`

Role:

`CHARACTER_REFERENCE_SHEET`

Canonical path:

`production/image_library/derived_reference_sheets/neil/CHAR_NEIL_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Exact identity:

- byte size: `840,092`
- SHA-256: `964445754ec69dcfeace287d46b2964a6d5044c59950c5ede5553859e1e229de`
- Git blob: `4f818f91f706bf680b455557eefa43c24594b977`

Destination group:

`identity_primary`

Authority purpose:

`NEIL_IDENTITY_COSTUME_PROPORTIONS_NORMAL_RESTRAINED_BUTLER_APPEARANCE`

It locks:

- Neil identity;
- age;
- hair;
- costume;
- body proportions;
- baseline restrained demeanor.

It does NOT control:

- screen position;
- pose;
- gaze direction;
- door interaction.

Those remain governed by N23 shot design.

---

### Reference 04｜Guang Yong Character Reference Sheet

Reference ID:

`AST_IMG_000056`

Source type:

`ASSET`

Entity:

`CHAR_GUANG_YONG`

Role:

`CHARACTER_REFERENCE_SHEET`

Canonical path:

`production/image_library/derived_reference_sheets/guang_yong/CHAR_GUANG_YONG_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Exact identity:

- byte size: `475,761`
- SHA-256: `2a98e74ddba60a259758643b56ffddafd5a7cb30de040880f991fb47216b45fb`
- Git blob: `e37ad60d933c3fdc434768bb449019146eb9333e`

Destination group:

`continuity_secondary`

Authority purpose:

`GUANG_YONG_IDENTITY_FOR_LOW_WEIGHT_BACKWARD_ATTENTION_CONTINUITY_TO_A06`

Hard prominence cap:

`TERTIARY CONTINUITY CUE ONLY`

Guang Yong must not become:

- first-glance subject;
- foreground portrait;
- equal co-lead with Neil;
- obvious speaking subject.

If Guang identity/reference pressure destabilizes N23, the next correction should reduce his visual prominence rather than increase reference complexity.

---

## 3. REFERENCE HIERARCHY

Formal hierarchy:

`SHOT DESIGN + SCENE REFERENCE DESIGN > REFERENCE IMAGE COMPOSITION`

Within the Bundle:

`Neil identity + Castle scene facts + N22 cohort continuity > Guang Yong tertiary identity cue`

The reference list order has no compositional meaning.

Hard rule:

`REFERENCE ORDER ≠ SCREEN POSITION ≠ LEFT/RIGHT ORDER ≠ BLOCKING ORDER ≠ PROMINENCE EQUALITY`

---

## 4. CAMERA INSTRUCTION TO BE EMBEDDED IN WORK HANDOFF

The later Work handoff must explicitly state:

`The camera is inside the castle, deeper than the threshold, offset to one side, looking diagonally back toward the open entrance. The group is moving from the doorway into the castle interior, generally toward the camera-side / deeper interior space. The image must NOT read as people leaving the castle.`

Work is NOT free to reinterpret:

- which side of the threshold contains the camera;
- lens direction;
- group travel direction;
- Neil's doorway position;
- open-door state;
- Neil walking-away timing.

Work may resolve only:

- minor body spacing;
- natural overlap;
- stride phase;
- partial occlusion;
- subtle head orientation;
- vertical-frame balancing.

---

## 5. TARGET 9:16 COMPOSITION CONTRACT

Output target:

`9:16 / 941 × 1672`

First read:

`PEOPLE ARE ENTERING THE CASTLE`

Second read:

`NEIL REMAINS BESIDE THE OPEN DOOR AND IS NOT CLOSING IT`

Tertiary read, only if naturally available:

`GUANG YONG REMAINS MORE AWARE OF THE DOOR / NEIL THAN THE OTHER GUESTS`

Automatic FAIL:

`FIRST-GLANCE READ = PEOPLE LEAVING THE CASTLE`

---

## 6. N22 CONTINUITY CONTRACT

N23 must feel like another camera observing the same cohort / continuous event.

Preserve from N22:

- clothing world;
- body-proportion range;
- crowd realism;
- approximate density;
- warm-dark lighting family;
- natural overlap.

Do not preserve mechanically:

- exact positions;
- exact faces visible;
- Su/Liao prominence;
- exact spacing;
- exact gaze directions.

Su Xiaoxiao / Liao Jian Character Reference Sheets are intentionally NOT included in V001.

Reason:

N23 is not another named-character seeding frame, and extra identity references would increase the risk of recreating the N22 ensemble.

---

## 7. EXPLICIT EXCLUSIONS FROM BUNDLE V001

Do not include:

- the horizontal N23 explanatory diagram created in Chat;
- any generated camera sketch;
- N21 Candidate images;
- N21 controlled human/environment references;
- Su Xiaoxiao Character Reference Sheet;
- Liao Jian Character Reference Sheet;
- Wen Qingya Character Reference Sheet;
- Ning Qiushui Character Reference Sheet;
- Jun Luyuan Character Reference Sheet;
- N20 raw Story Shot;
- First Hall Scene Master;
- A06 Story Shot;
- external images;
- style-board assets.

The horizontal explanatory diagram remains:

`INVALID FOR FORMAL EXECUTION / NOT A BUNDLE INPUT`

---

## 8. LIGHTING CONTRACT

Use N22 + approved Director rules to maintain:

- warm amber / tungsten practical family;
- low-key interior;
- restrained saturation;
- natural skin;
- dark-texture retention;
- moderate cinematic contrast.

Exterior daylight may be visible through the open door, but must remain controlled.

Prohibit:

- white portal;
- broad floor light band;
- exterior-dominant frame;
- glossy mirror-like floor.

---

## 9. WORK GENERATION MODE AFTER LATER AUTHORIZATION

Planned:

`N23 Candidate 01｜Clean Regeneration`

Candidate generation count:

`Exactly 1 PNG`

Candidate 01 is NOT authorized by this Bundle Design.

Formal generation requires:

1. Bundle Design Product Owner approval;
2. Bundle Spec creation with `build_authorized=false`;
3. validation-only exact-match PASS;
4. separate Product Owner authorization for formal Bundle build;
5. formal Artifact build + independent verification;
6. separate Product Owner Candidate 01 Work-generation authorization.

---

## 10. MINIMUM REFERENCE TEST

The four-reference set is considered sufficient if it can independently answer:

- Who is Neil? → AST_IMG_000059
- What door / scene state is this? → AST_IMG_000052
- Which cohort / visual continuity is continuing? → N22 canonical Story Shot
- Who is the low-weight future questioner if readable? → AST_IMG_000056
- Where is the camera / which way are people moving? → approved N23 Scene Reference Design text authority, NOT inferred from the reference pixels.

This separation is intentional.

---

## 11. CURRENT GATE

Status:

`DRAFT / WAITING PRODUCT OWNER APPROVAL`

If approved, next authorized step:

`CREATE N23_REFERENCE_DELIVERY_BUNDLE_V001 SPEC WITH build_authorized=false + VALIDATION-ONLY PREPARATION`

Still not authorized:

- formal Artifact build;
- Work generation;
- Candidate 01;
- Canonical Publication;
- Story Shot Registration;
- N24.
