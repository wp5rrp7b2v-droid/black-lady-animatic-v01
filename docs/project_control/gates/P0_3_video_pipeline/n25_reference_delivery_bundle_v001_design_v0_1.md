# N25_REFERENCE_DELIVERY_BUNDLE_V001｜Design V0.1

Date:

`2026-10-06`

Status:

`DESIGN COMPLETE / WAITING PRODUCT OWNER APPROVAL`

Target:

`N25 Candidate 01｜Clean Regeneration`

Upper authorities:

1. `S02-B Sequence Order Correction｜N23 → N24 → A06 → N25 → N26 → N27`
2. `N25 Node-Level Director Shot Design V0.3｜PRODUCT OWNER APPROVED / LOCKED`
3. `N25 Scene Reference Design V0.1｜PRODUCT OWNER APPROVED / LOCKED`
4. Work direct-image limit: `<= 5`

## 1. Bundle purpose

Build a five-reference executable package optimized for:

`NEIL IDENTITY + REAR/PROFILE SPEAKING ORIENTATION + NO-TURN-BACK MOTION + INNER-LOBBY CONTINUITY + SECONDARY PAUSED GROUP`

The Bundle must support a clean cut from A06's open-door insert back to Neil without reintroducing the door visually.

## 2. Direct visual inputs — EXACTLY 5

### 1. AST_IMG_000059｜CHAR_NEIL_CHARACTER_REFERENCE_SHEET V001

Canonical path:

`production/image_library/derived_reference_sheets/neil/CHAR_NEIL_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Authority purpose:

`PRIMARY OVERALL NEIL IDENTITY CONSOLIDATION`

Exact authority facts:

- entity: `CHAR_NEIL`
- role: `CHARACTER_REFERENCE_SHEET`
- asset class: `DERIVED_REFERENCE`
- authority class: `DERIVED`
- approval: `APPROVED`
- lifecycle: `CURRENT`
- resolver usage: `DEFAULT`
- SHA-256: `964445754ec69dcfeace287d46b2964a6d5044c59950c5ede5553859e1e229de`
- byte size: `840092`
- Git blob: `4f818f91f706bf680b455557eefa43c24594b977`

Controls:

- Neil overall identity;
- age / pallor;
- face family;
- wardrobe family.

Must not control:

- sheet layout;
- multi-pose duplication;
- Story Shot composition.

### 2. AST_IMG_000066｜CHAR_NEIL_REAR_3Q_RIGHT V001

Canonical path:

`production/image_library/character_references/neil/CHAR_NEIL_REAR_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`

Authority purpose:

`PRIMARY N25 REAR-3Q BODY ORIENTATION / NO-TURN-BACK MOVEMENT`

Exact authority facts:

- entity: `CHAR_NEIL`
- role: `REAR_3Q_RIGHT`
- asset class: `ATOMIC`
- authority class: `AUXILIARY`
- approval: `APPROVED`
- lifecycle: `CURRENT`
- resolver usage: `DEFAULT`
- SHA-256: `7f8cb635945e20035ba1b39dafecdf4caecc520d8e8794f67e39c2cfa1a6dad6`
- byte size: `1656490`
- Git blob: `7616c7ccce52f0754e3e4c11f89a288db2186330`

Controls:

- side-back / rear-3Q silhouette;
- walking-away body direction;
- partial face visibility;
- protection against frontal dialogue posing.

Hard rule:

`DO NOT TURN NEIL BACK TOWARD GUANG YONG OR CAMERA`

### 3. AST_IMG_000065｜CHAR_NEIL_PROFILE_RIGHT V001

Canonical path:

`production/image_library/character_references/neil/CHAR_NEIL_PROFILE_RIGHT_DEFAULT_DEFAULT_V001.png`

Authority purpose:

`RIGHT-SIDE FACE GEOMETRY / NATURAL SPEAKING PROFILE / HEAD-FORWARD CONTINUITY`

Exact authority facts:

- entity: `CHAR_NEIL`
- role: `PROFILE_RIGHT`
- asset class: `ATOMIC`
- authority class: `AUXILIARY`
- approval: `APPROVED`
- lifecycle: `CURRENT`
- resolver usage: `DEFAULT`
- SHA-256: `17dff7f50b7392915db6d74f1d04b506f2de884e9069ba11f9013bbe2fce8262`
- byte size: `1693697`
- Git blob: `0a4dd1af179e9e03d4786266ab65b6bea726ecec`

Controls:

- side-profile facial identity;
- natural mouth visibility compatible with speech;
- head orientation remaining generally forward.

Does not authorize:

- full profile portrait;
- stationary speaking pose;
- eye contact with camera.

### 4. AST_IMG_000108｜SCENE_CASTLE_ENTRANCE_INNER_LOBBY V001

Canonical path:

`production/image_library/scene_masters/castle_entrance_inner_lobby/SCENE_CASTLE_ENTRANCE_INNER_LOBBY_SCENE_MASTER_DEFAULT_DEFAULT_V001.png`

Authority purpose:

`INNER-LOBBY GEOMETRY / DEEPER-INTERIOR DIRECTION / LOW-KEY LIGHT FAMILY`

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

- entrance-inner-lobby architecture;
- direction toward deeper castle;
- warm low-key interior;
- usable multi-depth guest placement.

Must not force:

- empty-room framing;
- centered symmetry;
- 4:3 output;
- First Hall reveal;
- visible main entrance door.

### 5. BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q

Canonical path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q.png`

Manifest:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q.manifest.json`

Authority purpose:

`SECONDARY PAUSED / REORIENTING GUEST IDENTITY AND REAR-3Q WARDROBE FAMILY`

Exact authority facts:

- classification: `P0.3_CONTROLLED_PRODUCTION_REFERENCE`
- approval: `PRODUCT_OWNER_APPROVED`
- lifecycle: `CURRENT`
- dimensions: `1536 × 1024`
- SHA-256: `52ae779b86ca28e38c50bdf7bf935d08e25769d6ec9bcc73e71b9701f6604756`
- byte size: `2373958`
- Git blob: `3b72a8b8f0230231f3e2a6b0f7947f3c96b4a400`

Controls:

- 2–4 secondary anonymous guests;
- rear / side-back continuity;
- clothing family;
- paused / subtle reorientation context.

Must not control:

- 2×5 board layout;
- all ten guests appearing;
- equal spacing;
- synchronized walking;
- queue.

## 3. Direct-reference cap

`5 / 5 DIRECT IMAGES`

Hard rule:

- no sixth image;
- no silent substitution;
- no hidden extra image;
- no automatic addition of A06 or N24;
- no additional Neil reference unless this Bundle is redesigned and re-approved.

## 4. Non-delivered continuity evidence

### A06｜门不关

Role:

`DIRECT PRECEDING EDITORIAL SHOT / OPEN-DOOR FACT`

A06 is deliberately excluded from the direct image set.

Reason:

`A06 ALREADY OWNS THE DOOR INSERT; N25 MUST CUT BACK TO NEIL AND MUST NOT REPEAT THE DOOR VISUALLY.`

### N24｜Guang Yong Questions the Open Door

Role:

`UPSTREAM DIALOGUE / PAUSED-GROUP CONTINUITY`

N24 is deliberately excluded from direct generation input.

Reason:

- its frontal Guang Yong composition conflicts with N25's side/rear Neil grammar;
- it could incorrectly preserve Guang Yong as first subject;
- AST_IMG_000108 already supplies scene geometry.

## 5. N25 shot reading

First read:

`NEIL IS MOVING TOWARD THE FRONT / DEEPER INTERIOR`

Second read:

`NEIL ANSWERS WITHOUT TURNING BACK`

Third read:

`THE GROUP IS STILL MOSTLY PAUSED / PREPARING TO FOLLOW`

Dialogue:

`城堡大门只会在下雨天关闭`

## 6. Neil blocking

Neil:

- first visual subject;
- midground / forward-midground;
- side-back / rear-3Q dominant;
- moving naturally toward deeper interior;
- head generally aligned with movement;
- does not turn toward Guang Yong;
- does not look at camera;
- does not stop;
- speech may be indicated through slight profile mouth visibility.

Required emotional register:

`CALM / ROUTINE / MATTER-OF-FACT / SLIGHTLY DETACHED`

No warning gesture.

No pointing.

No dramatic pause.

## 7. Group blocking

Use:

`2–4 SECONDARY GUESTS`

They should:

- occupy irregular positions;
- use multiple depth planes;
- remain mostly paused;
- allow subtle weight shift / body reorientation toward Neil;
- appear as one shared physical space with Neil.

They must not:

- start synchronized walking;
- form a queue;
- form a neat audience;
- all face the same direction;
- compete with Neil.

Guang Yong is optional and secondary only.

## 8. Motion ownership

Locked:

`NEIL MOVES / GROUP MOSTLY REMAINS PAUSED`

This protects the downstream division:

- N25 = rain-day rule + Neil regains leading position;
- N26 = `这是夫人的要求`;
- N27 = `各位，请随我来` + stronger group-follow movement.

## 9. Environment

Scene:

`CASTLE_ENTRANCE_INNER_LOBBY / TRANSITION TOWARD DEEPER CASTLE`

Maintain:

- warm low-key interior;
- restrained amber / tungsten practicals;
- natural skin;
- dark stone / wood;
- textured blacks;
- restrained saturation;
- shared environmental lighting across Neil and guests;
- clarity without increased overall exposure.

## 10. Explicit environmental exclusions

Do not show:

- castle main door as a visible subject;
- exterior sky;
- exterior trees;
- bright exterior wash;
- rain;
- door-closing action;
- First Hall;
- fireplace;
- dining space;
- grand staircase;
- new major room.

## 11. Identity / composition hard fails

Automatic FAIL if:

- Neil identity drifts;
- Neil becomes another male guest;
- Neil faces camera;
- Neil turns back to answer Guang Yong;
- Neil stops for a speech;
- image reads as a frontal dialogue portrait;
- entire group is already walking;
- background guests become a flat single layer;
- queue / equal spacing appears;
- backpack / shoulder bag / crossbody bag / handbag / luggage appears;
- bright studio light appears;
- dirty noise / cutout edges appear.

## 12. Candidate mode

Target:

`N25 Candidate 01`

Generation mode:

`CLEAN REGENERATION`

Output target:

- `Exactly 1 × PNG`
- `9:16 vertical`
- `941 × 1672 preferred`
- cinematic audio-comic still

Generation is NOT authorized by Bundle Design approval alone.

## 13. Work handoff core requirements

The later Bundle Spec / WORK_HANDOFF must state:

1. Direct generation references are EXACTLY 5.
2. Active sequence is `N23 → N24 → A06 → N25 → N26 → N27`.
3. A06 immediately precedes N25 but is NOT a direct generation image.
4. First subject is Neil.
5. Neil is already moving toward deeper interior / future leading position.
6. Neil answers `城堡大门只会在下雨天关闭`.
7. Neil does not turn back.
8. Neil does not look at camera.
9. Group remains mostly paused / just reorienting.
10. Use 2–4 secondary guests only.
11. No visible main door / exterior / rain.
12. No First Hall / fireplace.
13. Maintain warm low-key inner-lobby lighting.
14. No bags / luggage.
15. No queue / synchronized movement / pasted-on look.
16. Before any generation, Work must revalidate all five Bundle references exactly; any SHA / byte / Git-blob / manifest mismatch means STOP.

## 14. Explicit direct-input exclusions

- A06 as direct image;
- N24 as direct image;
- AST_IMG_000025 BODY_BACK;
- Neil FACE_FRONT;
- Neil BODY_FRONT;
- Castle Entrance V002 / AST_IMG_000105;
- First Hall;
- any sixth image;
- old N25 V0.1 or V0.2 composition assumptions.

## 15. Production path if approved

1. Create `production/bundle_specs/N25_REFERENCE_DELIVERY_BUNDLE_V001.json` with `build_authorized=false`.
2. Push spec to trigger validation-only Generic Story Shot Reference Bundle Builder.
3. Require `5/5 exact`.
4. Require Artifact count = `0` during validation-only.
5. Record validation result.
6. Separate Product Owner authorization for Formal Build + Artifact Exact Verification.
7. Formal Build produces one verified Bundle Artifact.
8. Separate Product Owner authorization for N25 Candidate 01 Work generation.
9. Work generates Exactly 1 PNG and stops.

## 16. Current gate

`WAITING PRODUCT OWNER APPROVAL`

Not yet authorized:

- N25 Bundle Spec activation;
- Validation-only build;
- Formal Bundle Build;
- Work generation;
- Candidate 01;
- N26 production.
