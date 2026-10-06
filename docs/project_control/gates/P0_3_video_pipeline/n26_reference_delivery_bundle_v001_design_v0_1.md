# N26_REFERENCE_DELIVERY_BUNDLE_V001｜Design V0.1

Date:

`2026-10-06`

Status:

`DESIGN COMPLETE / WAITING PRODUCT OWNER APPROVAL`

Target:

`N26 Candidate 01｜Clean Regeneration`

Upper authorities:

1. `N26 Node-Level Director Shot Design V0.1｜PRODUCT OWNER APPROVED / LOCKED`
2. `N26 Scene Reference Design V0.1｜PRODUCT OWNER APPROVED / LOCKED`
3. `S02-B N26 / N27 Merge Decision｜PRODUCT OWNER APPROVED / LOCKED`
4. Active sequence tail: `N23 → N24 → A06 → N25 → N26`
5. N27 = `ABSORBED INTO N26`
6. Work direct-image limit: `<= 5`

## 1. Bundle purpose

Create a five-reference executable package optimized for:

`N25→N26 NEIL CONTINUITY + NING QIUSHUI REINTRODUCTION + JUN LUYUAN REINTRODUCTION + GROUP FOLLOW MOTION + INNER-LOBBY TRANSITION`

N26 must advance beyond N25.

N25 establishes Neil moving among a mostly paused group.

N26 must read:

`NEIL LEADS / GROUP BEGINS FOLLOWING`

while Neil says:

`这是夫人的要求。各位，请随我来。`

## 2. Direct visual inputs — EXACTLY 5

### 1. N25 APPROVED STORY SHOT

Shot ID:

`N25`

Title:

`Rain-Day Rule — Neil Answers Without Turning`

Canonical path:

`production/image_library/approved/story_shots/N25_RAIN_DAY_RULE_NEIL_ANSWERS_WITHOUT_TURNING_APPROVED_V001.png`

Authority purpose:

`IMMEDIATE PRECEDING SHOT / NEIL IDENTITY / WARDROBE / LIGHTING / IN-GROUP MOVEMENT CONTINUITY`

Exact authority facts:

- asset class: `STORY_SHOT`
- approval: `APPROVED`
- lifecycle: `CURRENT`
- dimensions: `941 × 1672`
- SHA-256: `b855040e30e014275920a1aaebf24c1ea4abb0623708f9901e47214b4dc27733`
- byte size: `2749858`
- Git blob: `8e523285a832496f1e316fd20737293668cf18db`

Controls:

- Neil identity;
- Neil wardrobe;
- Neil's immediate prior movement state;
- warm low-key lighting integration;
- Neil already spatially embedded among the group.

Must NOT control:

- exact N25 composition;
- exact N25 body placement;
- N25 group-still-mostly-paused motion state.

N26 must visibly advance to:

`NEIL LEADS / GROUP BEGINS FOLLOWING`

### 2. AST_IMG_000060｜NING QIUSHUI CHARACTER REFERENCE SHEET

Canonical path:

`production/image_library/derived_reference_sheets/ning_qiushui/CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Authority purpose:

`PRIMARY NING QIUSHUI IDENTITY / WARDROBE / BODY-PROPORTION CONSOLIDATION`

Exact authority facts:

- entity: `CHAR_NING_QIUSHUI`
- role: `CHARACTER_REFERENCE_SHEET`
- asset class: `DERIVED_REFERENCE`
- authority class: `DERIVED`
- approval: `APPROVED`
- lifecycle: `CURRENT`
- resolver usage: `DEFAULT`
- SHA-256: `15ec6c2682da0fe2502267bde21e9bc0bd7104bbf3e6041521121cc69a0e77be`
- byte size: `1123635`
- Git blob: `b674733242ab5d603dc42c53b8f7582003064499`

Hard rule:

`NING QIUSHUI MUST NOT PUT HANDS IN POCKETS`

Must not control:

- reference-sheet layout;
- duplicate Ning figures;
- frontal hero pose;
- paired portrait with Jun.

### 3. AST_IMG_000057｜JUN LUYUAN CHARACTER REFERENCE SHEET

Canonical path:

`production/image_library/derived_reference_sheets/jun_luyuan/CHAR_JUN_LUYUAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Authority purpose:

`PRIMARY JUN LUYUAN IDENTITY / WARDROBE / BODY-PROPORTION CONSOLIDATION`

Exact authority facts:

- entity: `CHAR_JUN_LUYUAN`
- role: `CHARACTER_REFERENCE_SHEET`
- asset class: `DERIVED_REFERENCE`
- authority class: `DERIVED`
- approval: `APPROVED`
- lifecycle: `CURRENT`
- resolver usage: `DEFAULT`
- SHA-256: `e8a0410cfc176ec9d6446b84f89b2c12d0683ec32b927c90353e850c416d909e`
- byte size: `969995`
- Git blob: `d11db79f4ceab2bb52139bfb8805f7c8f09b0cfc`

Must not control:

- reference-sheet layout;
- duplicate Jun figures;
- frontal hero pose;
- posed pairing with Ning.

### 4. AST_IMG_000108｜SCENE_CASTLE_ENTRANCE_INNER_LOBBY

Canonical path:

`production/image_library/scene_masters/castle_entrance_inner_lobby/SCENE_CASTLE_ENTRANCE_INNER_LOBBY_SCENE_MASTER_DEFAULT_DEFAULT_V001.png`

Authority purpose:

`INNER-LOBBY GEOMETRY / DEEPER-INTERIOR DIRECTION / WARM LOW-KEY LIGHT FAMILY`

Exact authority facts:

- entity: `SCENE_CASTLE_ENTRANCE_INNER_LOBBY`
- role: `SCENE_MASTER`
- asset class: `ATOMIC`
- authority class: `MASTER`
- approval: `APPROVED`
- lifecycle: `CURRENT`
- resolver usage: `CONDITIONAL`
- dimensions: `1448 × 1086`
- SHA-256: `f16d98a977eb73c75249cd3692ebfce9e3cd12cfbcbdb171d5b652149cb7c1a3`
- byte size: `2541370`
- Git blob: `91471e32dab1c7b51b7e718ffd539305d81daf85`

Controls:

- entrance-inner-lobby geometry;
- movement toward deeper castle;
- stone / dark-wood environment;
- warm low-key light family;
- multi-depth group movement space.

Must not force:

- empty-room composition;
- centered symmetry;
- 4:3 framing;
- full First Hall reveal;
- visible main entrance door.

### 5. BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q

Canonical path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q.png`

Manifest:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q.manifest.json`

Authority purpose:

`GENERIC FOLLOWER IDENTITY / WARDROBE / SIDE-BACK / REAR-3Q GROUP-FLOW SUPPORT`

Exact authority facts:

- source type: `CONTROLLED_REFERENCE`
- classification: `P0.3_CONTROLLED_PRODUCTION_REFERENCE`
- approval: `PRODUCT_OWNER_APPROVED`
- lifecycle: `CURRENT`
- dimensions: `1536 × 1024`
- SHA-256: `52ae779b86ca28e38c50bdf7bf935d08e25769d6ec9bcc73e71b9701f6604756`
- byte size: `2373958`
- Git blob: `3b72a8b8f0230231f3e2a6b0f7947f3c96b4a400`

Controls:

- 3–5 generic followers;
- side-back / rear-3Q identity family;
- wardrobe continuity;
- irregular multi-depth cohort movement.

Must not control:

- 2×5 board layout;
- all ten guests appearing;
- equal spacing;
- synchronized gait;
- single-file queue.

## 3. Direct-reference cap

`5 / 5 DIRECT IMAGES`

Hard rule:

- no sixth image;
- no silent substitution;
- no hidden extra visual input;
- no automatic addition of Neil atomic references;
- no automatic addition of N24 or A06;
- no additional Ning / Jun atomic angle unless the Bundle is redesigned and re-approved.

## 4. Named-character hierarchy

### Neil

`FIRST SUBJECT`

Required:

- slightly leading the cohort;
- still moving;
- side / side-back / rear-3Q acceptable;
- no formal stop-and-address pose;
- no need to fully turn toward the group.

### Ning Qiushui

`KEY SECONDARY FOLLOWER`

Required:

- clearly recognizable;
- integrated into group motion;
- not posed;
- not looking directly at camera;
- hands natural.

Hard rule:

`NO HANDS IN POCKETS`

### Jun Luyuan

`KEY SECONDARY FOLLOWER`

Required:

- clearly recognizable;
- integrated into group motion;
- not posed;
- not looking directly at camera.

## 5. Ning + Jun composition rule

They may appear in the same frame but must remain:

`STAGGERED / DIFFERENT DEPTH / DIFFERENT SCREEN POSITION`

Automatic FAIL if they become:

- shoulder-to-shoulder;
- frontal paired portrait;
- symmetrical duo;
- isolated pair separate from the group;
- matching gaze / matching pose.

Neil + Ning + Jun must not form a three-person publicity portrait.

## 6. Group scale

Preferred visible people:

`NEIL + NING + JUN + 3–5 GENERIC GUESTS`

Not everyone needs full-body visibility.

Use:

- partial foreground figures;
- midground named characters;
- deeper anonymous followers;
- natural overlap;
- irregular spacing.

The frame should read as:

`A MOVING SLICE OF THE LARGER COHORT`

not a complete posed cast lineup.

## 7. Movement ownership

N25:

`NEIL MOVES / GROUP MOSTLY REMAINS PAUSED`

N26:

`NEIL LEADS / GROUP BEGINS FOLLOWING`

N26 must visibly advance from the N25 state.

Required:

- Neil has a small forward lead;
- Ning and Jun are entering the forward flow;
- several generic guests begin moving;
- strides and timing remain irregular;
- no synchronized start.

## 8. Dialogue / performance

N26 owns both formerly split lines:

`这是夫人的要求。各位，请随我来。`

Neil performance:

`CALM / ROUTINE / MATTER-OF-FACT / LIGHTLY DETACHED`

Do not stage as:

- warning speech;
- theatrical command;
- formal stop;
- dramatic turn-back.

The invitation should feel procedural and natural.

## 9. Camera / composition

Target:

`9:16 VERTICAL`

Preferred:

`MEDIUM-WIDE / OBLIQUE GROUP TRANSITION`

Camera should allow:

- Neil first read;
- Ning separately recognizable;
- Jun separately recognizable;
- several generic guests across multiple depth planes;
- directional motion toward deeper interior.

Avoid:

- one flat horizontal line;
- symmetrical cast grouping;
- frontal group portrait;
- single-file procession.

## 10. Scene boundary

Scene:

`CASTLE_ENTRANCE_INNER_LOBBY / EXITING TOWARD DEEPER CASTLE`

Allowed:

- stronger inward direction than N25;
- passage / arch cues;
- more active forward depth.

Forbidden:

- full First Hall establishment;
- fireplace;
- dining hall;
- grand staircase;
- main entrance door as subject;
- exterior sky / trees;
- rain;
- door-closing action.

## 11. Lighting / integration

Maintain:

- warm low-key interior;
- restrained amber / tungsten practicals;
- natural skin;
- textured blacks;
- restrained saturation;
- no overall brightness lift;
- shared light direction / color temperature;
- natural contact shadow;
- no cutout edges.

Critical integration rule:

`NEIL + NING + JUN + GENERIC GUESTS MUST READ AS ONE PHYSICAL COHORT IN ONE SPACE`

not separate image layers.

## 12. Identity priority under generation pressure

If the image model cannot satisfy everything equally:

1. Neil continuity from N25
2. Ning Qiushui identity
3. Jun Luyuan identity
4. Scene continuity
5. Generic guest completeness

Do not sacrifice named-character identity merely to increase crowd count.

## 13. Candidate mode

Target:

`N26 Candidate 01`

Generation mode:

`CLEAN REGENERATION`

Output target:

- `Exactly 1 × PNG`
- `9:16 vertical`
- `941 × 1672 preferred`
- cinematic audio-comic still

Generation is not authorized by Bundle Design approval alone.

## 14. Work handoff core requirements

The later Bundle Spec / `WORK_HANDOFF.md` must state:

1. Direct generation references are EXACTLY 5.
2. Active sequence tail is `N23 → N24 → A06 → N25 → N26`.
3. N27 is absorbed into N26 and must not be generated separately.
4. N26 dialogue = `这是夫人的要求。各位，请随我来。`
5. N25 Approved Story Shot is continuity authority, not composition-copy authority.
6. Neil remains first subject.
7. Neil now has a slight forward lead.
8. Ning Qiushui and Jun Luyuan must both be recognizable.
9. Ning and Jun must be staggered, not posed together.
10. Ning Qiushui must not put hands in pockets.
11. Group movement must visibly advance to `GROUP BEGINS FOLLOWING`.
12. Use 3–5 generic guests as supporting cohort flow where composition permits.
13. No queue / equal spacing / synchronized gait.
14. No visible main entrance door / exterior / rain.
15. No full First Hall / fireplace / grand staircase.
16. Maintain warm low-key inner-lobby lighting.
17. No bags / luggage.
18. No pasted-on / cutout character layers.
19. Before any generation, Work must revalidate all five Bundle references exactly.
20. Any SHA / byte / Git-blob / manifest failure means `STOP / DO NOT GENERATE`.

## 15. Explicit direct-input exclusions

- Neil Character Reference Sheet as a sixth image;
- Neil atomic profile / rear-3Q as a sixth image;
- N24 Story Shot;
- A06;
- First Hall;
- Castle Entrance V002 / AST_IMG_000105;
- extra Ning atomic references;
- extra Jun atomic references;
- any sixth image;
- any independent N27 generation reference set.

## 16. Production path if approved

1. Create `production/bundle_specs/N26_REFERENCE_DELIVERY_BUNDLE_V001.json` with `build_authorized=false`.
2. Trigger validation-only Generic Story Shot Reference Bundle Builder.
3. Require `5/5 exact`.
4. Require Artifact count = `0`.
5. Record validation-only result.
6. Separate Product Owner authorization for Formal Build + Artifact Exact Verification.
7. Formal Build produces one verified Bundle Artifact.
8. Separate Product Owner authorization for N26 Candidate 01 Work generation.
9. Work generates `Exactly 1 × PNG` and stops.
10. No separate N27 production.

## 17. Current gate

`WAITING PRODUCT OWNER APPROVAL`

Not yet authorized:

- N26 Bundle Spec activation;
- validation-only run;
- Formal Build;
- Work generation;
- Candidate 01;
- any separate N27 production.
