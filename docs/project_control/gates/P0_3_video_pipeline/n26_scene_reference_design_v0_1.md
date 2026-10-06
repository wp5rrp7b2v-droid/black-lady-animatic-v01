# N26｜Scene Reference Design V0.1

Date:

`2026-10-06`

Status:

`DESIGN COMPLETE / WAITING PRODUCT OWNER APPROVAL`

Shot:

`N26｜Lady's Rule and Forward Motion — Neil Explains and Leads the Group On`

Upper authority:

- `N26 Node-Level Director Shot Design V0.1｜PRODUCT OWNER APPROVED / LOCKED`
- `S02-B N26 / N27 Merge Decision｜PRODUCT OWNER APPROVED / LOCKED`
- active sequence tail: `N23 → N24 → A06 → N25 → N26`
- N27 = `ABSORBED INTO N26`
- Work direct-image limit = `<= 5`

## 1. Scene-reference objective

N26 must advance directly from the approved N25 image.

Primary requirements:

`NEIL CONTINUITY + NING QIUSHUI REINTRODUCTION + JUN LUYUAN REINTRODUCTION + GROUP STARTS FOLLOWING + INNER-LOBBY TRANSITION`

The reference set must solve all of these within exactly five direct images.

## 2. Reference strategy

N25 approved Story Shot is used directly as the Neil / immediate-continuity reference.

Reason:

- N25 already contains the approved Neil identity in the exact preceding action state;
- N25 already establishes his current wardrobe, side-back orientation, lighting integration, and position among the guest group;
- using N25 directly frees reference capacity for Ning Qiushui and Jun Luyuan;
- a second Neil atomic reference would be lower-value duplication under the five-image cap.

Important:

`N25 CONTROLS CONTINUITY, NOT COMPOSITION COPY.`

N26 must advance beyond N25.

## 3. Reference priority

Locked priority:

`N25 NEIL CONTINUITY > NING IDENTITY > JUN IDENTITY > INNER-LOBBY SPACE > GENERIC GROUP FLOW`

If crowd completeness conflicts with named-character identity:

`NEIL / NING / JUN IDENTITY WINS`

## 4. Direct reference 01 — N25 Approved Story Shot

Reference:

`N25｜Rain-Day Rule — Neil Answers Without Turning｜APPROVED STORY SHOT`

Canonical path:

`production/image_library/approved/story_shots/N25_RAIN_DAY_RULE_NEIL_ANSWERS_WITHOUT_TURNING_APPROVED_V001.png`

Exact data:

- dimensions: `941 × 1672`
- byte size: `2,749,858`
- SHA-256: `b855040e30e014275920a1aaebf24c1ea4abb0623708f9901e47214b4dc27733`
- Git blob: `8e523285a832496f1e316fd20737293668cf18db`

Authority purpose:

`IMMEDIATE PRECEDING SHOT / NEIL IDENTITY / WARDROBE / LIGHTING / IN-GROUP MOVEMENT CONTINUITY`

Controls:

- Neil appearance;
- Neil clothing;
- warm low-key integration;
- Neil already moving among the group;
- continuity from N25 into N26.

Must NOT control:

- exact N25 framing;
- exact N25 body placement;
- group-still-paused behavior.

N26 must advance to:

`NEIL LEADS / GROUP BEGINS FOLLOWING`

## 5. Direct reference 02 — Ning Qiushui Character Reference Sheet

`AST_IMG_000060`

Canonical path:

`production/image_library/derived_reference_sheets/ning_qiushui/CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Exact data:

- entity: `CHAR_NING_QIUSHUI`
- role: `CHARACTER_REFERENCE_SHEET`
- asset class: `DERIVED_REFERENCE`
- approval: `APPROVED`
- lifecycle: `CURRENT`
- resolver usage: `DEFAULT`
- SHA-256: `15ec6c2682da0fe2502267bde21e9bc0bd7104bbf3e6041521121cc69a0e77be`
- byte size: `1,123,635`
- Git blob: `b674733242ab5d603dc42c53b8f7582003064499`

Authority purpose:

`PRIMARY NING QIUSHUI IDENTITY / WARDROBE / BODY-PROPORTION CONSOLIDATION`

Controls:

- face;
- hairstyle;
- age;
- body proportions;
- wardrobe family.

Hard rule:

`NING QIUSHUI MUST NOT PUT HANDS IN POCKETS`

Must not control:

- reference-sheet layout;
- duplicated Ning figures;
- posed frontal composition.

## 6. Direct reference 03 — Jun Luyuan Character Reference Sheet

`AST_IMG_000057`

Canonical path:

`production/image_library/derived_reference_sheets/jun_luyuan/CHAR_JUN_LUYUAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Exact data:

- entity: `CHAR_JUN_LUYUAN`
- role: `CHARACTER_REFERENCE_SHEET`
- asset class: `DERIVED_REFERENCE`
- approval: `APPROVED`
- lifecycle: `CURRENT`
- resolver usage: `DEFAULT`
- SHA-256: `e8a0410cfc176ec9d6446b84f89b2c12d0683ec32b927c90353e850c416d909e`
- byte size: `969,995`
- Git blob: `d11db79f4ceab2bb52139bfb8805f7c8f09b0cfc`

Authority purpose:

`PRIMARY JUN LUYUAN IDENTITY / WARDROBE / BODY-PROPORTION CONSOLIDATION`

Controls:

- face;
- hairstyle;
- age;
- body proportions;
- wardrobe family.

Must not control:

- reference-sheet layout;
- duplicated Jun figures;
- posed frontal composition.

## 7. Direct reference 04 — Castle Entrance Inner Lobby

`AST_IMG_000108｜SCENE_CASTLE_ENTRANCE_INNER_LOBBY`

Canonical path:

`production/image_library/scene_masters/castle_entrance_inner_lobby/SCENE_CASTLE_ENTRANCE_INNER_LOBBY_SCENE_MASTER_DEFAULT_DEFAULT_V001.png`

Exact data:

- dimensions: `1448 × 1086`
- SHA-256: `f16d98a977eb73c75249cd3692ebfce9e3cd12cfbcbdb171d5b652149cb7c1a3`
- byte size: `2,541,370`
- Git blob: `91471e32dab1c7b51b7e718ffd539305d81daf85`

Authority purpose:

`INNER-LOBBY GEOMETRY / DEEPER-INTERIOR DIRECTION / WARM LOW-KEY LIGHT FAMILY`

Controls:

- entrance-inner-lobby architecture;
- inward transition direction;
- stone / dark wood family;
- group movement depth.

Must not force:

- empty-room composition;
- centered symmetry;
- full First Hall reveal;
- visible main entrance door.

## 8. Direct reference 05 — Generic Guest REAR_3Q

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`

Canonical path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q.png`

Exact data:

- approval: `PRODUCT_OWNER_APPROVED`
- lifecycle: `CURRENT`
- dimensions: `1536 × 1024`
- SHA-256: `52ae779b86ca28e38c50bdf7bf935d08e25769d6ec9bcc73e71b9701f6604756`
- byte size: `2,373,958`
- Git blob: `3b72a8b8f0230231f3e2a6b0f7947f3c96b4a400`

Authority purpose:

`GENERIC FOLLOWER IDENTITY / WARDROBE / SIDE-BACK / REAR-3Q GROUP-FLOW SUPPORT`

Controls:

- anonymous guest identity family;
- side-back / rear-3Q silhouette;
- additional follower flow.

Must not control:

- 2×5 board layout;
- all ten guests appearing;
- equal spacing;
- synchronized gait;
- single-file queue.

## 9. Direct-reference cap

`5 / 5 DIRECT IMAGES`

Exactly:

1. N25 Approved Story Shot
2. AST_IMG_000060｜Ning Qiushui Character Reference Sheet
3. AST_IMG_000057｜Jun Luyuan Character Reference Sheet
4. AST_IMG_000108｜Castle Entrance Inner Lobby
5. Generic Guest REAR_3Q

No sixth image.

Do not silently add:

- Neil atomic reference;
- N24;
- A06;
- First Hall;
- additional Ning or Jun atomic angles.

## 10. Named-character composition rule

Neil:

- first subject;
- forward-leading movement;
- side / side-back / rear-3Q preferred;
- no formal stop-and-address pose.

Ning Qiushui:

- key secondary;
- clearly recognizable;
- moving / preparing to follow;
- no hands in pockets;
- no direct camera stare.

Jun Luyuan:

- key secondary;
- clearly recognizable;
- moving / following;
- no direct camera stare.

Ning + Jun:

`STAGGERED / DIFFERENT DEPTH / DIFFERENT SCREEN POSITION`

Forbidden:

- frontal two-person portrait;
- matching pose;
- shoulder-to-shoulder symmetry;
- pair isolated from crowd.

## 11. Group scale

N26 should read as a larger cohort than just three named characters.

Preferred visible people:

`NEIL + NING + JUN + 3–5 GENERIC GUESTS`

Not all figures need full-body visibility.

Use:

- foreground partial bodies;
- midground named characters;
- deeper generic followers;
- natural occlusion.

The frame should feel like a moving slice of a larger group.

## 12. Movement progression

N25:

`NEIL MOVES / GROUP MOSTLY PAUSED`

N26:

`NEIL LEADS / GROUP BEGINS FOLLOWING`

Required:

- Neil has a slight forward lead;
- Ning and Jun are visibly entering the group flow;
- other guests begin moving with varied strides;
- no synchronized start.

## 13. Camera / frame

Target:

`9:16 VERTICAL`

Preferred:

`MEDIUM-WIDE / OBLIQUE GROUP TRANSITION`

Camera should allow:

- Neil to remain first read;
- Ning and Jun to be separately readable;
- several generic followers to occupy multiple depth planes;
- movement toward deeper interior.

Do not flatten everyone across one horizontal line.

## 14. Space boundary

Still:

`CASTLE_ENTRANCE_INNER_LOBBY / EXITING TOWARD DEEPER CASTLE`

Allowed:

- stronger inward direction than N25;
- partial passage / arch cue;
- more forward depth.

Forbidden:

- full First Hall establishment;
- fireplace;
- dining hall;
- grand staircase;
- main entrance door;
- exterior;
- rain.

## 15. Lighting / integration

Maintain:

- warm low-key;
- restrained amber / tungsten;
- natural skin;
- textured blacks;
- restrained saturation;
- no brightness lift;
- common environmental light across all people;
- natural contact shadows;
- no cutout edges.

This is especially important because three named identities plus generic guests must read as one physical cohort, not separate pasted layers.

## 16. Identity priority under failure

If generation struggles:

1. Neil continuity from N25
2. Ning identity
3. Jun identity
4. scene continuity
5. generic crowd completeness

Do not sacrifice Ning or Jun identity just to show more anonymous guests.

## 17. Hard fail

Automatic FAIL if:

- Neil identity drifts from N25;
- Ning identity drifts;
- Jun identity drifts;
- Ning puts hands in pockets;
- Ning + Jun become a posed frontal pair;
- Neil + Ning + Jun become a three-person poster;
- group remains fully static like N25;
- group forms a queue;
- synchronized gait;
- door / exterior returns;
- First Hall / fireplace appears;
- bags / luggage;
- studio-bright light;
- pasted-on / cutout layers.

## 18. Recommended Bundle

Next if approved:

`N26_REFERENCE_DELIVERY_BUNDLE_V001｜Design V0.1`

Direct images:

1. `N25 APPROVED STORY SHOT`
2. `AST_IMG_000060`
3. `AST_IMG_000057`
4. `AST_IMG_000108`
5. `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`

## 19. Current gate

`WAITING PRODUCT OWNER APPROVAL`

Not yet authorized:

- N26 Bundle;
- Work generation;
- Candidate 01;
- any separate N27 production.
