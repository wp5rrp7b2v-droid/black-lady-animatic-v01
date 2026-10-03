# N23 Candidate 03｜Reference Architecture V0.1

Status:

`PROPOSED / SLOT 3 MICRO-CORRECTION PRODUCT OWNER APPROVED AND INCORPORATED / FINAL ARCHITECTURE APPROVAL STILL REQUIRED / DIRECT VISUAL CAP = 5`

Date:

`2026-10-03`

Target:

`N23 Candidate 03`

Parent strategy:

`N23 Candidate 03 Correction Strategy V0.1`

---

## 1. REFERENCE-BUDGET RULE

Direct generation-image budget:

`MAXIMUM 5`

This is a hard Candidate 03 production rule.

No later Bundle design may silently add a sixth direct visual reference.

If more evidence is needed:

`COMPRESS / CROP / CONTROL / REMOVE`

not:

`ADD ANOTHER DIRECT IMAGE`

---

## 2. FIVE-SLOT ARCHITECTURE

### SLOT 1｜Door identity / scene fact

Planned reference:

`N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001`

Source:

`AST_IMG_000052`

Type:

`CONTROLLED_REFERENCE / DETERMINISTIC CROP`

Purpose:

`DOOR IDENTITY / MATERIAL / SCALE / OPEN STATE ONLY`

Why not full Scene Master:

`REDUCE EXTERIOR-LIGHT / FLOOR-REFLECTION PHOTOGRAPHIC PRESSURE`

---

### SLOT 2｜Neil identity

Reference:

`AST_IMG_000073`

Entity:

`CHAR_NEIL`

Role:

`FACE_3Q_RIGHT`

Approval:

`APPROVED / CURRENT`

Exact identity:

- byte size: `1,738,212`
- SHA-256: `92ef0fc973093c7cc99f3b70f3aab1fabd09d2d82c29921e72065f0d7b9ac366`
- Git blob: `8179b112aae5253c0f8d9dffe4cfe451d94dacbc`

Purpose:

`ANGLE-SPECIFIC NEIL FACE IDENTITY LOCK`

The reference angle does not override shot-specific subtle gaze / head-turn amount.

---

### SLOT 3｜Guang identity only

Reference:

`AST_IMG_000011`

Entity:

`CHAR_GUANG_YONG`

Role:

`FACE_FRONT`

Authority:

`MASTER`

Approval:

`APPROVED / CURRENT`

Resolver usage:

`DEFAULT`

Exact identity:

- byte size: `2,903,455`
- SHA-256: `7f88a3f8d68dbfea0058ff0379d0164380722d96ae1774364bcd8b79367ad6f5`
- Git blob: `5490cd3101d0d878ef77b4a3a164ea2231bf3817`

Purpose:

`GUANG IDENTITY ONLY`

Why FACE_FRONT replaces FACE_3Q_RIGHT:

- `RIGHT` means face/nose toward screen-right under project orientation governance;
- Candidate 03 requires Guang's body to keep moving screen-right while retaining a small backward-attention cue toward frame-left / Neil / the open door;
- a FACE_3Q_RIGHT image would add unnecessary opposite head-direction pressure;
- FACE_FRONT is the more neutral identity anchor.

Shot-specific head direction and behavior come from SLOT 5 plus written shot authority. SLOT 3 must not override them.

---

### SLOT 4｜Anonymous crowd identity pool

Reference:

`BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_REAR_3Q`

Purpose:

`GENERIC GUEST A–J SIDE-BACK / REAR-3Q IDENTITY CONTINUITY`

Why REAR_3Q only:

- enough rear-side identity evidence;
- avoids the Candidate 02 full-BACK procession pressure;
- preserves more lateral body readability.

Non-delivered governance:

`GENERIC GUEST FRONT = GLOBAL IDENTITY AUTHORITY / FRONT WINS`

---

### SLOT 5｜N22 motion / behavior continuity

Planned reference:

`N23_N22_MOTION_OBSERVATION_REFERENCE_V001`

Source:

`N22_PEOPLE_IN_THE_FLOW_APPROVED_V001.png`

Type:

`CONTROLLED_REFERENCE / DETERMINISTIC TWO-PANEL CROP`

Purpose:

- N22→N23 movement continuity;
- lateral screen-right travel language;
- asynchronous walking / observing;
- Guang Yong backward-awareness behavior.

Hard boundary:

`FULL N22 STORY SHOT IS NOT DELIVERED`

---

## 3. EXCLUDED DIRECT INPUTS

Do not deliver:

- `AST_IMG_000052` full Scene Master;
- `AST_IMG_000059` Neil Character Reference Sheet;
- `AST_IMG_000013` Guang REAR_3Q_RIGHT;
- `AST_IMG_000010` Guang FACE_3Q_RIGHT;
- Generic Guest BACK;
- Generic Guest FRONT;
- Generic Guest LEFT_PROFILE;
- full N22 canonical Story Shot;
- Candidate 02;
- any N21-specific human reference;
- Character Visual Style Reference.

---

## 4. WHY THIS FITS THE FAILURE EVIDENCE

Candidate 02 failure → Candidate 03 slot response:

### Motion axis failed
→ SLOT 5 adds N22-derived motion evidence.

### Guang observation disappeared
→ SLOT 3 locks Guang identity only with a neutral FACE_FRONT anchor; SLOT 5 locks the backward-awareness behavior and shot-specific head-direction cue.

### Neil identity drifted
→ SLOT 2 replaces broad Character Sheet pressure with angle-specific face identity.

### Crowd became too back-facing
→ SLOT 4 keeps REAR_3Q and removes BACK.

### Lighting remained too bright
→ SLOT 1 replaces full Scene Master with door-only controlled crop.

No failure currently justifies a sixth direct image.

---

## 5. PRIORITY ORDER

Shot-specific authority:

`CANDIDATE 03 STRATEGY + N23 SCENE REFERENCE > REFERENCE PIXEL COMPOSITION`

Direct-reference semantic priority:

1. Neil identity — SLOT 2
2. motion / Guang behavior — SLOT 5
3. door identity — SLOT 1
4. Generic Guest identity — SLOT 4
5. Guang identity detail — SLOT 3

This priority list does NOT imply screen prominence.

---

## 6. BUILD DEPENDENCIES

Bundle V003 cannot be designed as final until SLOT 1 and SLOT 5 controlled references exist and are approved.

Required intermediate gates:

### Gate A
`N23_CASTLE_ENTRANCE_DOOR_CONTROL_REFERENCE_V001｜Exact Crop Plan`

### Gate B
`N23_N22_MOTION_OBSERVATION_REFERENCE_V001｜Exact Crop Plan`

### Gate C
`Deterministic Build + Exact Binary Verification for both controlled references`

Only then:

`N23_REFERENCE_DELIVERY_BUNDLE_V003 DESIGN`

---

## 7. CURRENT GATE

Status:

`PROPOSED / SLOT 3 MICRO-CORRECTION INCORPORATED / WAITING PRODUCT OWNER FINAL APPROVAL`

Product Owner has approved only the Slot 3 micro-correction:

`AST_IMG_000010 FACE_3Q_RIGHT → AST_IMG_000011 FACE_FRONT / IDENTITY ONLY`

The complete five-slot architecture is still waiting final Product Owner approval.

No controlled-reference build, Bundle V003 work, or image generation is authorized.
