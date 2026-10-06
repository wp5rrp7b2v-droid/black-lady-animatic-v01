# N25｜Scene Reference Design V0.1

Date:

`2026-10-06`

Status:

`DESIGN COMPLETE / WAITING PRODUCT OWNER APPROVAL`

Shot:

`N25｜Rain-Day Rule — Neil Answers Without Turning`

Upper authority:

- `N25 Node-Level Director Shot Design V0.3｜PRODUCT OWNER APPROVED / LOCKED`
- active sequence: `N23 → N24 → A06 → N25 → N26 → N27`
- direct preceding editorial shot: `A06｜门不关`
- Work direct-image limit: `<= 5`

## 1. Scene-reference objective

N25 must visually return from A06's static open-door insert to Neil.

First read:

`NEIL IS MOVING TOWARD THE FRONT / DEEPER INTERIOR`

Second read:

`HE ANSWERS WITHOUT TURNING BACK`

Third read:

`THE GROUP IS STILL MOSTLY PAUSED AND PREPARING TO FOLLOW`

The scene reference set must therefore prioritize:

`NEIL IDENTITY + REAR / REAR-3Q BODY ORIENTATION + INNER-LOBBY DEPTH + SECONDARY PAUSED-GROUP CONTINUITY`

## 2. Reference priority

Locked priority:

`NEIL IDENTITY > NO-TURN-BACK BODY ORIENTATION > INNER-LOBBY SPACE > SECONDARY GROUP CONTINUITY > A06 DOOR CONTINUITY`

A06 remains editorial evidence only and is intentionally not delivered as a direct generation image.

## 3. Direct reference 01 — Neil Character Reference Sheet

`AST_IMG_000059`

Canonical path:

`production/image_library/derived_reference_sheets/neil/CHAR_NEIL_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Authority:

`DERIVED CHARACTER REFERENCE SHEET / CURRENT / APPROVED`

Exact identity data:

- SHA-256: `964445754ec69dcfeace287d46b2964a6d5044c59950c5ede5553859e1e229de`
- bytes: `840,092`
- Git blob: `4f818f91f706bf680b455557eefa43c24594b977`

Purpose:

- overall Neil identity consolidation;
- age / pallor / facial family;
- wardrobe family;
- body / face relationship.

Must NOT control:

- sheet layout;
- multi-pose duplication;
- shot composition.

## 4. Direct reference 02 — Neil REAR_3Q_RIGHT

`AST_IMG_000066`

Canonical path:

`production/image_library/character_references/neil/CHAR_NEIL_REAR_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`

Exact identity data:

- SHA-256: `7f8cb635945e20035ba1b39dafecdf4caecc520d8e8794f67e39c2cfa1a6dad6`
- bytes: `1,656,490`
- Git blob: `7616c7ccce52f0754e3e4c11f89a288db2186330`

Purpose:

- primary N25 body orientation;
- rear / side-back silhouette;
- restrained facial visibility compatible with speaking;
- walking-away direction without turning back.

Hard rule:

`DO NOT CONVERT REAR-3Q INTO A TURNED-BACK DIALOGUE POSE`

Neil's head remains aligned generally with his walking direction.

## 5. Direct reference 03 — Neil BODY_BACK

`AST_IMG_000025`

Canonical path:

`production/image_library/character_references/neil/CHAR_NEIL_BODY_BACK_DEFAULT_DEFAULT_V001.png`

Exact identity data:

- SHA-256: `cba43e22ca16a538a197a877fea81bb5086a12caf2a8be11090aa00d6f285060`
- bytes: `2,584,766`
- Git blob: `484e1827cc0fdb589f665efe1adae6d3b0903a0b`

Purpose:

- body proportion;
- back silhouette;
- wardrobe / coat continuity;
- no-turn-back action protection.

This reference outranks any temptation to rotate Neil into a frontal speaking pose.

## 6. Direct reference 04 — Castle Entrance Inner Lobby

`AST_IMG_000108｜SCENE_CASTLE_ENTRANCE_INNER_LOBBY`

Canonical path:

`production/image_library/scene_masters/castle_entrance_inner_lobby/SCENE_CASTLE_ENTRANCE_INNER_LOBBY_SCENE_MASTER_DEFAULT_DEFAULT_V001.png`

Exact scene data:

- dimensions: `1448 × 1086`
- SHA-256: `f16d98a977eb73c75249cd3692ebfce9e3cd12cfbcbdb171d5b652149cb7c1a3`
- bytes: `2,541,370`
- Git blob: `91471e32dab1c7b51b7e718ffd539305d81daf85`

Purpose:

- immediate inner-lobby architecture;
- deeper-interior direction;
- warm low-key light family;
- paused-group holding-area depth;
- one-beat transition toward deeper castle.

Must NOT force:

- exact empty-room 4:3 framing;
- centered architectural symmetry;
- First Hall;
- visible main entrance door.

## 7. Direct reference 05 — Generic Guest REAR_3Q Authority

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`

Canonical path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q.png`

Exact controlled-reference data:

- dimensions: `1536 × 1024`
- SHA-256: `52ae779b86ca28e38c50bdf7bf935d08e25769d6ec9bcc73e71b9701f6604756`
- bytes: `2,373,958`
- Git blob: `3b72a8b8f0230231f3e2a6b0f7947f3c96b4a400`

Purpose:

- 2–4 secondary guests;
- rear / side-back body and wardrobe continuity;
- paused / reorienting group context;
- natural partial bodies in multiple depth planes.

Must NOT control:

- 2×5 board layout;
- all ten guests appearing;
- queue;
- synchronized movement;
- equal spacing.

## 8. Direct-reference cap

`5 / 5 DIRECT IMAGES`

No sixth image.

No silent addition of:

- A06;
- N24 final frame;
- Castle Entrance V002;
- Neil frontal face;
- First Hall.

## 9. A06 as non-delivered editorial evidence

A06 controls only:

`THE CASTLE MAIN DOOR IS STILL OPEN`

A06 immediately precedes N25 in edit order.

Reason for excluding A06 from direct generation input:

`N25 MUST CUT BACK TO NEIL, NOT VISUALLY REPEAT THE DOOR INSERT`

Therefore the N25 image should contain no major door / exterior composition.

## 10. N24 as non-delivered character-position evidence

N24 establishes:

- group paused;
- Guang Yong just asked the question;
- Neil was on the entrance-side / camera-side axis;
- Neil was not visible.

N25 resumes after A06 with Neil already beginning to move toward the front / deeper interior.

N24 should not be delivered as a direct visual input because:

- its frontal Guang Yong composition is the opposite grammar of N25;
- it could pull Guang Yong back into first-subject status;
- it is not needed to establish scene geometry now that AST_IMG_000108 exists.

## 11. Recommended N25 screen construction

Target:

`9:16 VERTICAL`

Preferred composition:

- Neil = midground / forward-midground;
- Neil = rear-3Q / side-back;
- Neil visibly walking toward deeper interior;
- camera = slightly behind / lateral to the paused group;
- 2–4 guests occupy foreground / side / deeper layers;
- group remains mostly stationary;
- some shoulders / partial bodies may enter foreground;
- Neil remains first subject through motion and placement, not through frontal face size.

Do not require full-body Neil if a medium / medium-wide crop reads movement more naturally.

## 12. Movement direction

Scene Reference V0.1 does NOT yet freeze a left/right screen direction.

Locked spatial rule instead:

`FROM ENTRANCE-SIDE / REAR-SIDE OF GROUP → TOWARD DEEPER-INTERIOR / FUTURE LEADING POSITION`

The final left/right screen vector may be chosen at Bundle / Work composition stage according to the best fit with AST_IMG_000108.

What must remain invariant:

- Neil walks away from the entrance-side position;
- Neil does not walk back toward the door;
- Neil does not face the camera;
- Neil does not turn toward Guang Yong.

## 13. Neil speaking behavior

Dialogue:

`城堡大门只会在下雨天关闭`

Visual speech rule:

- speech may be implied by slight side-profile mouth visibility;
- clear lip-reading is not required;
- do not sacrifice the no-turn-back action to expose the mouth;
- no hand gesture required;
- no dramatic expression.

Performance:

`CALM / ROUTINE / DETACHED`

## 14. Group behavior

Background / foreground guests:

- 2–4 visible;
- multiple depths;
- mostly paused;
- subtle reorientation toward Neil allowed;
- one person may shift weight or begin to turn;
- no coordinated walking yet.

Guang Yong:

- optional;
- if visible, secondary;
- no repeated direct-camera dialogue pose;
- no requirement to identify him clearly.

## 15. Environment / lighting

Use AST_IMG_000108 as scene authority.

Maintain:

- warm-dark low-key interior;
- restrained amber / tungsten practicals;
- dark stone / wood;
- readable blacks;
- low-to-moderate saturation;
- shared environmental lighting across Neil and guests;
- clean image without dirty noise.

Do NOT increase overall brightness.

## 16. Door / exterior suppression

Automatic FAIL if:

- main door becomes visible as a major object;
- bright exterior opening appears;
- blue sky / trees appear;
- doorway becomes first or second visual subject;
- door closing is shown;
- rain is shown.

A06 already owns the door beat.

## 17. First Hall suppression

Automatic FAIL if:

- fireplace appears;
- formal main hall is established;
- large reception hall scale appears;
- grand staircase appears;
- deep next-space climax appears.

N25 remains inside the entrance-lobby transition.

## 18. Neil identity fail-safe

Automatic FAIL if:

- face / hair / pallor / age drift;
- coat / wardrobe drift;
- body silhouette changes materially;
- Neil becomes a different male guest;
- rear-3Q orientation turns into a frontal portrait.

Priority if references conflict:

`NEIL IDENTITY > NO-TURN-BACK ACTION > EXACT FACE VISIBILITY`

## 19. Recommended next Bundle

Create:

`N25_REFERENCE_DELIVERY_BUNDLE_V001｜Design V0.1`

with exactly five direct images:

1. `AST_IMG_000059`
2. `AST_IMG_000066`
3. `AST_IMG_000025`
4. `AST_IMG_000108`
5. `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`

Hard cap:

`5 / 5 DIRECT IMAGES`

## 20. Current gate

`WAITING PRODUCT OWNER APPROVAL`

Not yet authorized:

- N25 Bundle build;
- Work generation;
- Candidate 01;
- N26 production.
