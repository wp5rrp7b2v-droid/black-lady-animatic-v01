# N23_REFERENCE_DELIVERY_BUNDLE_V003｜Design V0.1

Date:

`2026-10-03`

Status:

`PROPOSED / PRODUCT OWNER REVIEW REQUIRED / BUNDLE SPEC + VALIDATION + FORMAL BUILD NOT YET AUTHORIZED`

Target:

`N23｜Neil at the Open Door — Watches the Group Enter｜Candidate 03`

Generation mode after later authorization:

`CLEAN REGENERATION / EXACTLY 1 PNG / 941 × 1672`

Direct visual input rule:

`MAXIMUM 5 / CURRENT V003 = 4`

No fifth reference is added merely to fill the cap.

---

## 1. DIRECT VISUAL INPUTS

### SLOT 1｜Door Control

Reference:

`N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001`

Canonical path:

`production/controlled_references/n23/N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001.png`

Exact identity:

- dimensions: `315 × 1265`
- mode: `RGB`
- byte size: `546,543`
- SHA-256: `5718ce8c68069ca41143d666406a8c4cec3c285837a861337da758769bbfb652`
- Git blob: `88eaa11f441a4c7c341dcbde04cb9f529f9ca6af`
- canonical publication commit: `74c4cea6d52358e038e112427a411f9d348ede52`

Controls only:

- physical right-side entrance door leaf beside Neil;
- approved door material / carving;
- open-door state / local door angle;
- local Neil-side door relation.

Explicitly does NOT control:

`CAMERA / PERSPECTIVE / SCREEN PLACEMENT / LIGHTING COMPOSITION`

### SLOT 2｜Neil identity

Reference:

`AST_IMG_000073｜CHAR_NEIL｜FACE_3Q_RIGHT`

Canonical path:

`production/image_library/character_references/neil/CHAR_NEIL_FACE_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`

Exact identity:

- byte size: `1,738,212`
- SHA-256: `92ef0fc973093c7cc99f3b70f3aab1fabd09d2d82c29921e72065f0d7b9ac366`
- Git blob: `8179b112aae5253c0f8d9dffe4cfe451d94dacbc`

Controls:

`NEIL IDENTITY ONLY`

Shot authority controls exact body / head / gaze.

### SLOT 3｜Guang Yong identity

Reference:

`AST_IMG_000011｜CHAR_GUANG_YONG｜FACE_FRONT`

Canonical path:

`production/image_library/character_references/guang_yong/CHAR_GUANG_YONG_FACE_FRONT_DEFAULT_DEFAULT_V001.png`

Exact identity:

- byte size: `2,903,455`
- SHA-256: `7f88a3f8d68dbfea0058ff0379d0164380722d96ae1774364bcd8b79367ad6f5`
- Git blob: `5490cd3101d0d878ef77b4a3a164ea2231bf3817`

Controls:

`GUANG IDENTITY ONLY`

It must not control shot-specific head direction.

### SLOT 4｜Generic Guest REAR_3Q

Reference:

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`

Canonical path:

`production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q.png`

Exact identity:

- dimensions: `1536 × 1024`
- mode: `RGBA`
- byte size: `2,373,958`
- SHA-256: `52ae779b86ca28e38c50bdf7bf935d08e25769d6ec9bcc73e71b9701f6604756`
- Git blob: `3b72a8b8f0230231f3e2a6b0f7947f3c96b4a400`

Controls:

- generic Guest A–J side-back / rear-3Q identity continuity;
- hairstyle / garment silhouette / footwear continuity.

Must NOT control:

- crowd formation;
- 2×5 layout;
- scene composition;
- lighting;
- named-character identity.

Global rule remains:

`FRONT WINS`

---

## 2. CAMERA / COMPOSITION INTERPRETATION — WRITTEN INSTRUCTION ONLY

No additional camera-reference image will be created.

Work must follow this interpretation:

`CAMERA IS INSIDE THE CASTLE, LOOKING OBLIQUELY TOWARD NEIL AT THE PHYSICAL RIGHT SIDE OF THE OPEN ENTRANCE.`

Important distinction:

`PHYSICAL RIGHT-SIDE DOOR LEAF ≠ REQUIRED SCREEN-RIGHT PLACEMENT`

The Door Control reference identifies the correct physical door side only.

Work must NOT inherit from Door Control / AST_IMG_000052:

- frontal inside-to-outside camera;
- source-image perspective;
- source-image screen-left / screen-right placement;
- centered bright portal composition;
- source-image daylight pattern;
- source-image floor reflection.

N23 screen composition remains governed by the locked Scene Reference:

- open entrance / controlled exterior cue = LEFT region;
- Neil = beside the door / approximately LEFT-CENTER;
- deeper castle interior = RIGHT;
- crowd travel = LEFT → RIGHT;
- most visible people = already to Neil's RIGHT.

The camera is:

`INTERIOR-SIDE / OBLIQUE / BROADSIDE-FIRST / DEPTH-SECOND`

Do not create a centered portal establishing shot.

---

## 3. NEIL STAGING

Neil:

- remains beside the physical right-side door leaf;
- is near-frontal to camera;
- body does not walk away;
- does not touch / close the door;
- head / eyes turn subtly toward frame-right;
- watches the tail of the group already inside;
- does not look primarily toward the outside.

Neil is the principal readable human anchor of N23.

Door is environment / story evidence, not the visual protagonist.

---

## 4. CROWD MOTION

First read:

`LEFT → RIGHT LATERAL SCREEN TRAVEL`

Second read:

`MODEST RECESSION INTO DEEPER INTERIOR`

Required:

- hips / torso / feet support rightward travel;
- side / side-back / rear-3Q bodies preferred;
- asynchronous stride;
- natural spacing;
- most people already right of Neil;
- approximately 3–5 generic Guests / partial bodies;
- do not force all ten Guests.

Automatic fail:

- full-back procession straight into depth;
- single-file queue;
- synchronized walking;
- crowd merely placed on right without readable rightward motion.

---

## 5. GUANG YONG

If visible:

- already farther right with the group;
- body continues screen-right;
- head / attention may retain a small backward cue toward frame-left / Neil / open entrance;
- remains tertiary;
- no full torso turn back;
- no reaction portrait.

This behavior is a written shot requirement and is not claimed as visually proven by a direct action reference.

---

## 6. LIGHTING

`INTERIOR DOMINANT / WARM LOW-KEY`

Exterior:

`SMALL CONTROLLED CUE ONLY`

Do not reproduce:

- large blue / white exterior field;
- bright centered portal;
- broad cool floor reflection;
- glossy floor as a compositional feature.

---

## 7. GLOBAL FAIL CONDITIONS

Reject if any of the following appears:

- wrong physical door side beside Neil;
- camera copies Door Control / Scene Master frontal viewpoint;
- entrance becomes central bright focal point;
- crowd moves mainly away from camera rather than left→right;
- Neil identity drifts;
- Neil looks outside / left instead of toward group tail;
- Guang becomes co-lead or fully turns back;
- generic crowd becomes a board-like formation / queue;
- backpack / shoulder bag / luggage appears;
- staged two-person front-facing photo composition;
- cutout / pasted-on character look;
- strong studio lighting.

---

## 8. EXCLUDED DIRECT INPUTS

Do not deliver:

- full `AST_IMG_000052`;
- `AST_IMG_000059` Neil Character Sheet;
- `AST_IMG_000013` Guang REAR_3Q_RIGHT;
- `AST_IMG_000010` Guang FACE_3Q_RIGHT;
- Generic Guest BACK;
- Generic Guest FRONT;
- Generic Guest LEFT_PROFILE;
- full N22 canonical Story Shot;
- Candidate 02;
- any fifth image without new Product Owner-approved evidence.

---

## 9. BUNDLE V003 PASS TEST

Bundle V003 design passes only if:

1. exactly 4 direct PNG references are delivered;
2. each source matches the exact identity above;
3. Door Control is the canonical approved `5718ce...` binary;
4. Work handoff contains the camera / composition interpretation in Section 2;
5. Door Control is explicitly marked `NO CAMERA / NO COMPOSITION INHERITANCE`;
6. no excluded image is delivered;
7. Candidate 03 remains `CLEAN REGENERATION`;
8. generation remains blocked until later Product Owner authorization.

---

## 10. CURRENT GATE

Current:

`BUNDLE V003 DESIGN / PRODUCT OWNER REVIEW`

Not yet authorized:

- Bundle V003 Spec;
- Validation-only;
- Formal Build;
- Work Candidate 03 generation;
- Candidate 04;
- N24;
- Story Shot publication / registration.

Next after Product Owner approval:

`BUNDLE V003 SPEC → VALIDATION-ONLY → FORMAL BUILD`
