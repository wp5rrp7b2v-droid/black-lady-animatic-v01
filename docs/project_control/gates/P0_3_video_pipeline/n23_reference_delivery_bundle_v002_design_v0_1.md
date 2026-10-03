# N23｜Reference Delivery Bundle V002 Design V0.1

Status:

`PRODUCT OWNER APPROVED / LOCKED / SPEC + VALIDATION-ONLY AUTHORIZED`

Date:

`2026-10-03`

Target:

`N23｜Neil at the Open Door — Watches the Group Enter｜Candidate 02`

Bundle ID:

`N23_REFERENCE_DELIVERY_BUNDLE_V002`

Parent authorities:

- `N23 Scene Reference Design V0.2.1 / PRODUCT OWNER APPROVED / LOCKED`
- `N23 Candidate 02 Correction Strategy V0.2 / PRODUCT OWNER APPROVED / LOCKED`
- `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001 / CLOSED`

Generation mode after later authorization:

`CLEAN REGENERATION`

Planned output:

`EXACTLY 1 × PNG / 941 × 1672`

---

## 1. DESIGN GOAL

Deliver the minimum direct reference set needed for Candidate 02 to preserve:

- Castle Entrance identity / DAY_DOOR_OPEN facts;
- Neil identity;
- low-weight Guang Yong continuity;
- controlled reusable anonymous Guest identities;
- rear / side-back crowd continuity appropriate to the approved N23 camera.

The Bundle must break the Candidate 01 failure pattern:

- N22-like frontal ensemble;
- excessive named-character readability;
- Guang Yong over-prominence;
- bright exterior / floor spill;
- bag-like foreground ambiguity.

The Bundle does NOT control composition by reference-board layout.

Composition authority remains:

`N23 SCENE REFERENCE DESIGN V0.2.1 + CANDIDATE 02 CORRECTION STRATEGY V0.2`

---

## 2. FORMAL DIRECT REFERENCE SET

Direct visual reference count:

`5`

No sixth visual reference is proposed.

---

### Reference 01｜AST_IMG_000052

Reference ID:

`AST_IMG_000052`

Source type:

`ASSET`

Entity:

`SCENE_CASTLE_ENTRANCE`

Role:

`SCENE_MASTER`

Asset class:

`ATOMIC`

Authority class:

`MASTER`

Approval:

`APPROVED / CURRENT`

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

`CASTLE_ENTRANCE_DOOR_IDENTITY_MATERIAL_SCALE_DAY_DOOR_OPEN_FACTS_ONLY`

It MAY control:

- same entrance identity;
- door material;
- door scale;
- open-door state;
- threshold scene facts.

It MUST NOT control:

- doorway screen-center placement;
- N23 camera axis;
- N23 crowd blocking;
- exterior brightness;
- floor reflection;
- photographic composition.

Hard rule:

`SCENE FACT AUTHORITY ≠ PHOTOGRAPHY AUTHORITY`

---

### Reference 02｜AST_IMG_000059

Reference ID:

`AST_IMG_000059`

Source type:

`ASSET`

Entity:

`CHAR_NEIL`

Role:

`CHARACTER_REFERENCE_SHEET`

Asset class:

`DERIVED_REFERENCE`

Authority class:

`DERIVED`

Approval:

`APPROVED / CURRENT`

Canonical path:

`production/image_library/derived_reference_sheets/neil/CHAR_NEIL_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Exact identity:

- byte size: `840,092`
- SHA-256: `964445754ec69dcfeace287d46b2964a6d5044c59950c5ede5553859e1e229de`
- Git blob: `4f818f91f706bf680b455557eefa43c24594b977`

Destination group:

`identity_primary`

Authority purpose:

`NEIL_IDENTITY_COSTUME_PROPORTIONS_RESTRAINED_BUTLER_APPEARANCE`

It controls:

- Neil identity;
- age;
- hair;
- costume;
- body proportion;
- restrained baseline demeanor.

It does NOT control:

- Neil screen position;
- gaze;
- pose;
- door interaction.

N23 Scene Reference V0.2.1 controls those shot-specific facts.

---

### Reference 03｜AST_IMG_000013

Reference ID:

`AST_IMG_000013`

Source type:

`ASSET`

Entity:

`CHAR_GUANG_YONG`

Role:

`REAR_3Q_RIGHT`

Asset class:

`ATOMIC`

Authority class:

`AUXILIARY`

Resolver usage:

`CONDITIONAL`

Approval:

`APPROVED / CURRENT`

Canonical path:

`production/image_library/character_references/guang_yong/CHAR_GUANG_YONG_REAR_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`

Exact identity:

- byte size: `2,906,146`
- SHA-256: `848d350468f67704d932fbdfe030201dbd815b333db22e874864cd82f9755f60`
- Git blob: `d4b9bb9dec872a35fb8ca8524bd8dfa059dfdfd6`

Destination group:

`named_continuity_tertiary`

Authority purpose:

`LOW_WEIGHT_GUANG_YONG_REAR_3Q_CONTINUITY_ONLY`

Hard prominence cap:

`TERTIARY CONTINUITY CUE ONLY`

Guang Yong must not become:

- first-glance subject;
- foreground portrait;
- equal co-lead with Neil;
- obvious speaking subject.

A clean readable face is NOT required.

---

### Reference 04｜Generic Guest REAR_3Q

Reference ID:

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`

Source type:

`CONTROLLED_REFERENCE`

Classification:

`P0.3_CONTROLLED_PRODUCTION_REFERENCE`

Approval:

`PRODUCT_OWNER_APPROVED / CURRENT`

Authority scope:

`PROJECT_LEVEL_GENERIC_GUEST_CROWD_A_TO_J_REAR_3Q_IDENTITY`

Canonical path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q.png`

Manifest path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q.manifest.json`

Exact identity:

- 1536 × 1024
- RGBA / 8-bit
- byte size: `2,373,958`
- SHA-256: `52ae779b86ca28e38c50bdf7bf935d08e25769d6ec9bcc73e71b9701f6604756`
- Git blob: `3b72a8b8f0230231f3e2a6b0f7947f3c96b4a400`

Destination group:

`generic_crowd_identity_primary`

Authority purpose:

`PRIMARY_GENERIC_GUEST_SIDE_BACK_REAR_3Q_IDENTITY_CONTINUITY`

It MAY control:

- Guest A–J rear-3Q identity continuity;
- rear-side hairstyle silhouette;
- body-build continuity;
- garment identity;
- footwear continuity.

It MUST NOT control:

- 2×5 layout;
- number of guests visible;
- screen direction;
- N23 blocking;
- queue formation;
- camera geometry.

---

### Reference 05｜Generic Guest BACK

Reference ID:

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_BACK`

Source type:

`CONTROLLED_REFERENCE`

Classification:

`P0.3_CONTROLLED_PRODUCTION_REFERENCE`

Approval:

`PRODUCT_OWNER_APPROVED / CURRENT`

Authority scope:

`PROJECT_LEVEL_GENERIC_GUEST_CROWD_A_TO_J_BACK_IDENTITY`

Canonical path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_BACK.png`

Manifest path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_BACK.manifest.json`

Exact identity:

- 1536 × 1024
- RGBA / 8-bit
- byte size: `2,378,771`
- SHA-256: `dbde5e5a4df213c19439016c675e1fb40e999577b1cfd4ec92f04c13471db13f`
- Git blob: `dcef9dc08cb72d15826ec18abb7f3fa2bb5cd22f`

Destination group:

`generic_crowd_identity_secondary`

Authority purpose:

`SECONDARY_GENERIC_GUEST_FULL_BACK_IDENTITY_CONTINUITY`

It MAY control:

- rear head silhouette;
- rear hair;
- shoulder/back width;
- garment back;
- rear lower-body geometry;
- footwear-back continuity.

It MUST NOT control:

- N23 composition;
- all-ten casting;
- board spacing;
- synchronized walking.

---

## 3. NON-DELIVERED GOVERNANCE AUTHORITY

### Generic Guest FRONT

Reference ID:

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_FRONT`

Status for Candidate 02:

`GLOBAL IDENTITY GOVERNANCE AUTHORITY / NOT A DIRECT VISUAL BUNDLE INPUT`

Reason:

FRONT remains the Core Set's global identity authority and conflict resolver, but direct delivery would add unnecessary frontal-face / identity-display pressure.

Conflict rule:

`IF A DELIVERED GENERIC VIEW CONFLICTS WITH FRONT GLOBAL IDENTITY, FRONT WINS`

This rule is embedded in Work handoff text without delivering FRONT pixels.

---

### Generic Guest LEFT_PROFILE

Status for Candidate 02:

`AVAILABLE CONTROLLED REFERENCE / NOT A DIRECT VISUAL BUNDLE INPUT`

Reason:

Its approved body/nose direction is screen-left while N23 crowd movement is hard-locked LEFT → RIGHT.

Direct inclusion adds avoidable direction ambiguity and additional profile-face pressure.

This exclusion is shot-specific and does not change project-level authority.

---

## 4. REMOVED / EXCLUDED INPUTS

### N22 canonical Story Shot

Status:

`DIRECTOR-LEVEL CONTINUITY CHECK ONLY / NOT DELIVERED TO WORK`

Reason:

Candidate 01 demonstrated direct N22-pixel pressure toward:

- N22-like camera family;
- face-readable named ensemble;
- Su / Liao / Guang prominence;
- frontal crowd behavior.

---

### AST_IMG_000056｜Guang Yong Character Reference Sheet

Status:

`EXCLUDED`

Replaced for C02 by:

`AST_IMG_000013 / REAR_3Q_RIGHT`

Reason:

reduce Guang Yong face / identity prominence while keeping enough continuity.

---

### CHARACTER_VISUAL_STYLE_REFERENCE_V001

Status:

`EXCLUDED`

Reason:

unnecessary multi-character face/body pressure for this minimum proof.

---

### N21_CROWD_BODY_WARDROBE_REFERENCE_V001

Status:

`EXCLUDED`

Reason:

N21-specific authority scope; Generic Guest Core Set now supplies project-level anonymous crowd identity support.

---

### Generic Guest FRONT / LEFT_PROFILE

Status:

`NOT DIRECT BUNDLE INPUTS FOR C02`

They remain governed assets, not deleted or superseded.

---

## 5. AUTHORITY HIERARCHY

Highest shot-specific authority:

`N23 SCENE REFERENCE DESIGN V0.2.1 + CANDIDATE 02 CORRECTION STRATEGY V0.2`

They control:

- camera;
- left/right geometry;
- crowd travel direction;
- Neil position / gaze;
- story timing;
- visual hierarchy.

Direct-reference hierarchy:

1. `AST_IMG_000052` — scene facts only
2. `AST_IMG_000059` — Neil identity
3. `Generic Guest REAR_3Q` — primary anonymous crowd identity geometry
4. `Generic Guest BACK` — secondary anonymous crowd back identity
5. `AST_IMG_000013` — Guang Yong tertiary continuity

Within Generic Guest identity conflicts:

`FRONT WINS`

Hard rule:

`REFERENCE ORDER ≠ SCREEN POSITION ≠ PROMINENCE ≠ BLOCKING`

---

## 6. CROWD CASTING CONTRACT

The Core Set is an identity pool, not a mandatory ten-person shot list.

Candidate 02 target:

`APPROXIMATELY 4–6 VISIBLE GENERIC GUESTS / PARTIAL BODIES`

Use identities from Guest A–J.

Do not invent a completely unrelated anonymous crowd when controlled Guest identities are available.

Do not force all ten into the image.

Allowed:

- full bodies;
- partial bodies;
- natural occlusion;
- rear-3Q;
- side-back;
- back;
- unequal stride phases.

Forbidden:

- 2×5 board layout;
- lineup;
- single-file queue;
- identity showcase;
- synchronized walking;
- equal spacing.

Hard rule:

`IDENTITY BOARD LAYOUT ≠ STORY SHOT BLOCKING`

---

## 7. GUEST I / GUANG YONG COLLISION CONTROL

Guest I is a Generic Guest with:

- muscular build;
- black sleeveless top;
- short stiff hair;
- tattoo/body-marking identity.

Guang Yong is a separate named character.

For Candidate 02:

`GUEST I IS NOT REQUIRED TO APPEAR`

If Guest I appears:

- maintain clear visual separation from Guang Yong;
- do not use Guest I as Guang Yong substitute;
- do not transfer tattoo/clothing traits between them;
- keep Guest I anonymous/subordinate.

---

## 8. N23 SCREEN GEOMETRY HARD LOCK

`LEFT = OPEN CASTLE DOOR + CONTROLLED EXTERIOR LIGHT`

`CROWD = LEFT → RIGHT`

`RIGHT = DEEPER CASTLE INTERIOR`

`NEIL = BESIDE OPEN DOOR / NEAR-FRONTAL / HEAD-EYES SLIGHTLY RIGHT`

Story moment:

`TAIL END OF ENTRY / ALMOST EVERYONE ALREADY INSIDE`

Preferred crowd state:

- majority of visible people already right of Neil;
- at most final entrant / partial body near threshold;
- crowd mass middle-right / right;
- darker interior dominates.

Camera:

`SIDE / BROADSIDE THRESHOLD VIEW / MILDLY ELEVATED`

Do not return to:

`INTERIOR LOOKING BACK TOWARD PEOPLE APPROACHING LENS`

---

## 9. LIGHTING CONTRACT

Exterior light:

`SMALL CONTROLLED LEFT-EDGE SPATIAL CUE`

Interior:

`DOMINANT WARM LOW-KEY EXPOSURE WORLD`

Prohibit:

- white portal;
- exterior-dominant frame;
- broad daylight floor band;
- glossy reflection strip;
- giant bright symmetrical entrance.

---

## 10. ACCESSORY HARD FAIL

Prohibit:

- backpack;
- shoulder bag;
- handbag;
- luggage;
- travel bag;
- crossbody strap;
- ambiguous bag-like foreground object.

Any such read:

`SELF-CHECK = FAIL`

---

## 11. WORK HANDOFF REQUIREMENTS FOR FUTURE SPEC

Future Bundle V002 Work handoff must explicitly state, in substance:

1. Candidate 02 = CLEAN REGENERATION.
2. Output = exactly one 941×1672 PNG.
3. Camera is side/broadside near the castle threshold.
4. Open door + controlled exterior light are LEFT.
5. Crowd has almost finished entering and continues LEFT → RIGHT into darker interior.
6. Most visible crowd is already RIGHT of Neil.
7. Neil remains beside door, near-frontal, head/eyes slightly RIGHT toward group tail.
8. Generic Guest REAR_3Q + BACK control anonymous crowd identity only, not board layout.
9. Use approximately 4–6 Guest A–J identities / partial bodies; do not force all ten.
10. FRONT is non-delivered global identity conflict authority; FRONT WINS.
11. LEFT_PROFILE is not delivered and must not be inferred as screen-direction authority.
12. Guang Yong is low-weight tertiary continuity only.
13. Guest I is not required and must not merge with Guang Yong.
14. N22 is not a generation image.
15. No queue / lineup / synchronized steps / bags.
16. Generate one image and stop for Product Owner review.

---

## 12. MINIMUM REFERENCE TEST

The five direct inputs are sufficient if they independently answer:

- What entrance / door state is this? → `AST_IMG_000052`
- Who is Neil? → `AST_IMG_000059`
- Who is Guang Yong if a low-weight continuity cue is used? → `AST_IMG_000013`
- Who are the anonymous guests from side-back / rear-3Q? → `Generic Guest REAR_3Q`
- Who are the anonymous guests from behind? → `Generic Guest BACK`
- Where is the camera / which direction is the group moving? → `N23 Scene Reference V0.2.1 text authority`, not inferred from pixels.

No additional direct visual input is required for Candidate 02 minimum proof.

---

## 13. FUTURE BUILD SEQUENCE

If Product Owner approves this Bundle Design:

1. create `N23_REFERENCE_DELIVERY_BUNDLE_V002` formal Spec with:
   `build_authorized=false`
2. builder validation-only exact check;
3. require:
   `5/5 EXACT PASS`
4. no Artifact at validation-only stage;
5. separate Product Owner authorization for formal build;
6. set only:
   `build_authorized=true` and revision increment;
7. formal Artifact build;
8. independently verify Artifact ZIP digest and all five delivered visual binaries;
9. separately authorize Candidate 02 Work generation;
10. Work auto-acquires verified Artifact;
11. Work revalidates:
   `5/5 MATCH`
12. generate exactly one Candidate 02 PNG;
13. stop for Product Owner review.

---

## 14. CURRENT GATE

Status:

`PRODUCT OWNER APPROVED / LOCKED`

Still NOT authorized:

- Bundle V002 Spec;
- validation-only run;
- formal Artifact build;
- Candidate 02 Work generation;
- Candidate 03;
- N21;
- N24;
- Canonical Publication;
- Story Shot Registration.
