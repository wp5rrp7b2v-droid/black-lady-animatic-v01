# N24｜Scene Reference Design V0.4

Date:

`2026-10-06`

Status:

`DESIGN COMPLETE / WAITING PRODUCT OWNER APPROVAL`

Supersedes:

`N24 Scene Reference Design V0.3`

Upper authority:

- `N24 Node-Level Director Shot Design V0.4｜PRODUCT OWNER APPROVED / LOCKED`
- sequence: `N23 → A06 → N24 → N25 → N26 → N27`
- Work direct-image limit: `<= 5`
- new scene authority: `AST_IMG_000108｜SCENE_CASTLE_ENTRANCE_INNER_LOBBY`

## 1. Scene-reference objective

N24 is now a stationary question shot.

The group has already entered and paused.

Camera is positioned on / near the entrance-side axis and faces inward toward Guang Yong.

The shot must read as:

`GUANG YONG IN FRONT / PAUSED GUESTS DISPERSED BEHIND HIM / ENTRANCE-SIDE LIGHT INDICATES WHERE NEIL AND THE DOOR ARE`

The door itself is not required in frame.

Neil may remain off-screen.

## 2. Why V0.3 is superseded

V0.3 still proposed:

`AST_IMG_000105｜SCENE_CASTLE_ENTRANCE V002`

as the scene input.

Product Owner correctly identified a generation risk:

`THE SOURCE IMAGE MAY PULL THE CASTLE DOOR BACK INTO THE SHOT`

That risk is now removed by the newly approved dedicated environment asset:

`AST_IMG_000108｜SCENE_CASTLE_ENTRANCE_INNER_LOBBY`

This Scene Master was specifically created from the correct camera side:

`AT / NEAR THE MAIN DOOR THRESHOLD → LOOKING INWARD INTO THE CASTLE`

and provides the holding-area geometry without making the main door the visual subject.

## 3. Reference priority

Locked priority for the next Bundle:

`GUANG YONG IDENTITY > INNER LOBBY GEOMETRY > BACKGROUND GUEST IDENTITY > EDITORIAL DOOR CONTINUITY > NEIL DIRECT VISIBILITY`

The direct-reference allocation should therefore use the five available image slots as follows.

## 4. Direct reference 01 — Guang Yong Character Reference Sheet

`AST_IMG_000056`

Canonical path:

`production/image_library/derived_reference_sheets/guang_yong/CHAR_GUANG_YONG_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Authority:

`DERIVED CHARACTER REFERENCE SHEET / CURRENT / APPROVED`

Exact identity data:

- SHA-256: `2a98e74ddba60a259758643b56ffddafd5a7cb30de040880f991fb47216b45fb`
- bytes: `475,761`
- Git blob: `e37ad60d933c3fdc434768bb449019146eb9333e`

Purpose:

- overall Guang Yong identity consolidation;
- face/body/wardrobe relationship;
- reduce generic-man substitution.

Must NOT control:

- sheet layout;
- shot composition;
- multi-pose duplication.

## 5. Direct reference 02 — Guang Yong FACE_3Q_RIGHT

`AST_IMG_000010`

Canonical path:

`production/image_library/character_references/guang_yong/CHAR_GUANG_YONG_FACE_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`

Exact identity data:

- SHA-256: `ee8f6e72345046f2c96376d932565533fd3c3c4a96035458dd768083a639ab4b`
- bytes: `2,928,885`
- Git blob: `68baca3dcfc732a16d6e2edc100031f4f337c5d3`

Purpose:

- face structure;
- hair;
- age impression;
- natural speaking face;
- frontal / slight-3Q identity suitable for addressing entrance-side Neil.

## 6. Direct reference 03 — Guang Yong BODY_FRONT

`AST_IMG_000009`

Canonical path:

`production/image_library/character_references/guang_yong/CHAR_GUANG_YONG_BODY_FRONT_DEFAULT_DEFAULT_V001.png`

Exact identity data:

- SHA-256: `60005a45f2c89bceb463183c9fa4acee2b6ad0eebabadf8b825bc5e877b85b6e`
- bytes: `2,852,067`
- Git blob: `975574aac0b469b49a11f474264c5bda3e44f6e9`

Purpose:

- short male body proportion;
- naturally slightly chubby build;
- wardrobe authority;
- prevent tall / athletic reinterpretation.

## 7. Direct reference 04 — Inner Lobby Scene Master

`AST_IMG_000108｜SCENE_CASTLE_ENTRANCE_INNER_LOBBY`

Canonical path:

`production/image_library/scene_masters/castle_entrance_inner_lobby/SCENE_CASTLE_ENTRANCE_INNER_LOBBY_SCENE_MASTER_DEFAULT_DEFAULT_V001.png`

Exact scene data:

- dimensions: `1448 × 1086`
- SHA-256: `f16d98a977eb73c75249cd3692ebfce9e3cd12cfbcbdb171d5b652149cb7c1a3`
- bytes: `2,541,370`
- Git blob: `91471e32dab1c7b51b7e718ffd539305d81daf85`

Purpose:

- correct inward-looking entrance-lobby geometry;
- camera-side spatial baseline;
- paused-group holding area;
- warm low-key interior material / light family;
- entrance direction may be inferred from edge / directional light.

Must NOT force:

- exact 4:3 composition into 9:16;
- empty-room composition;
- perfectly centered architecture;
- visible main door;
- First Hall;
- fireplace.

## 8. Direct reference 05 — Generic Guest FRONT Authority

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_FRONT`

Canonical path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_FRONT.png`

Exact controlled-reference data:

- dimensions: `1536 × 1024`
- SHA-256: `ef6c1b65c8d2f41db70b77b8621ec5d9ade41ad43811d2ddda88a2c14c357a23`
- bytes: `2,335,288`
- Git blob: `d8ff2d789a352475daa945d22a0a65112c72a682`

Purpose:

- anonymous guest identity / wardrobe family;
- front / front-3Q-compatible paused background;
- support 2–4 secondary guests dispersed behind Guang Yong.

Must NOT control:

- 2×5 board composition;
- all ten guests appearing;
- equal spacing;
- lineup;
- posed group portrait.

## 9. Non-delivered continuity evidence

The following remain valid Project Control evidence but should NOT be direct image inputs for the next Bundle:

### A06

Purpose:

`EDITORIAL FACT — THE CASTLE DOOR REMAINS OPEN`

Reason for exclusion:

N24 should not visually repeat the door-establishment shot.

### N23

Purpose:

`EARLIER ENTRANCE-SEQUENCE CONTINUITY`

Reason for exclusion:

Too early in the edit and no unique N24 visual authority.

### AST_IMG_000105｜SCENE_CASTLE_ENTRANCE V002

Purpose:

`BROADER CASTLE ENTRANCE ARCHITECTURAL HISTORY`

Reason for exclusion:

Direct use risks making the door / exterior opening visually dominant again.

### Neil character reference

Purpose:

`CHARACTER CONTINUITY IF NEIL MUST LATER BE VISIBLE`

Reason for exclusion in first V0.4 attempt:

Neil is on / near the camera-side entrance axis and may remain off-screen. A direct Neil reference would consume a scarce identity slot and increase the chance of creating a competing second subject.

## 10. Expected N24 composition

The direct reference set should support:

- 9:16 vertical Story Shot;
- Guang Yong foreground / near-midground;
- frontal or slight 3Q;
- stopped;
- naturally speaking;
- gaze directed toward entrance-side Neil / just off-camera;
- 2–4 guests dispersed behind him;
- background guests paused, not walking;
- irregular spacing / occlusion;
- no lineup;
- no marching;
- entrance direction suggested by controlled light;
- no need to show the main door;
- Neil may remain off-screen;
- inner lobby architecture remains clearly subordinate to Guang Yong.

## 11. Lighting interpretation

Use AST_IMG_000108 to establish:

- warm low-key interior;
- restrained amber practical light;
- dark stone / wood material family;
- deep but readable blacks.

For N24 specifically:

- entrance-side light should be a subtle directional cue only;
- do not increase overall exposure;
- do not introduce a bright outdoor opening;
- do not turn the frame into a backlit doorway shot.

## 12. Guang Yong identity fail-safe

Because Candidate 01 drifted severely, identity protection is stronger than before.

Automatic FAIL if:

- face does not match Guang Yong authority;
- hairstyle drifts;
- age impression drifts;
- body becomes taller / athletic;
- body loses naturally slightly chubby build;
- wardrobe family drifts;
- he reads as a generic middle-aged man.

If the three Guang Yong references conflict in pose/composition, identity traits win and pose must follow Director Design V0.4.

## 13. Scene / crowd fail-safe

Automatic FAIL if:

- visible main door becomes first or second visual subject;
- bright exterior dominates;
- room reads as First Hall;
- fireplace appears;
- crowd appears in a line / queue;
- crowd appears synchronized;
- background looks like a formal audience;
- Generic Guest board grid leaks into composition;
- empty architecture overwhelms Guang Yong.

## 14. Recommended next Bundle

Create:

`N24_REFERENCE_DELIVERY_BUNDLE_V004｜Design V0.1`

with exactly five direct images:

1. `AST_IMG_000056`
2. `AST_IMG_000010`
3. `AST_IMG_000009`
4. `AST_IMG_000108`
5. `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_FRONT`

Hard cap:

`5 / 5 DIRECT IMAGES`

No sixth image.

## 15. Current gate

`WAITING PRODUCT OWNER APPROVAL`
