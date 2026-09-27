# N12｜Reference Delivery Bundle Design V0.1

Status: `DRAFT / PRODUCT OWNER REVIEW / NOT YET BUILT`

Date: 2026-09-27

Target bundle ID: `N12_REFERENCE_DELIVERY_BUNDLE_V001`

Working shot: `N12｜Cross + Rigid Smile Detail`

Target generation: `N12 Candidate 01`

Transport rule: RC-022 / RC-023  
Story Shot governance: RC-024 / RC-025

## 1. Bundle objective

Deliver the minimum canonical references needed to generate N12 with:

- stable Neil identity;
- correct formal butler clothing;
- current castle-entrance / inside-threshold continuity;
- enough upper-chest coverage to place one simple cross;
- a small rigid closed-mouth smile;
- no drift back to exterior-platform composition;
- no dependency on the not-yet-archived N11 binary.

The cross is required by source narration but is not treated as a separate canonical Prop Asset in this bundle.

## 2. Proposed reference set

Reference count: `5`

### A. Character authority — 3 PNG

#### 1. AST_IMG_000028｜FACE_FRONT

Path:
`production/image_library/character_references/neil/CHAR_NEIL_FACE_FRONT_DEFAULT_DEFAULT_V001.png`

Locked identity:
- SHA-256: `e75f0cba8f48d948069b978d86d46e96f7f5f0abd7a40341a5f92e006cb18939`
- byte size: `2517908`
- Git blob: `f3e74a06562d8751dd84c0d228b486769abdd254`

Responsibility:
`NEIL_FACE_IDENTITY_AUTHORITY`

Purpose:
Primary face identity, age structure, mouth/cheek proportions and grooming.

#### 2. AST_IMG_000027｜FACE_3Q_LEFT

Path:
`production/image_library/character_references/neil/CHAR_NEIL_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`

Locked identity:
- SHA-256: `252f18eff4511a6b1255c751448a7fb667ad68ea2f9ebae49824ce3f453ea037`
- byte size: `2529346`
- Git blob: `0d2638f02caa2697220f0073109fedac50e68246`

Responsibility:
`NEIL_3Q_IDENTITY_AND_CAMERA_ANGLE_AUTHORITY`

Purpose:
Supports mild 3/4 facial angle without exterior Story Shot composition bias.

#### 3. AST_IMG_000026｜BODY_FRONT

Path:
`production/image_library/character_references/neil/CHAR_NEIL_BODY_FRONT_DEFAULT_DEFAULT_V001.png`

Locked identity:
- SHA-256: `f78ccfc252d2ed0cb31117ce1dae4c84893c5e52611a27fac161c8e6d014cf3d`
- byte size: `2605161`
- Git blob: `59939fba0a02b9364dbdc2d9ff8203fb57efa7f4`

Responsibility:
`NEIL_BODY_AND_COSTUME_STRUCTURE_AUTHORITY`

Purpose:
Locks upper-torso proportion, black formal butler clothing and white shirt while allowing N12 to include upper chest.

### B. Scene authority — 1 PNG

#### 4. AST_IMG_000052｜CASTLE ENTRANCE SCENE MASTER

Path:
`production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`

Locked identity:
- SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- byte size: `2305753`
- Git blob: `e4dafe096f5c5c8782257030a5a659aeec7808f9`

Responsibility:
`SCENE_FACT_AUTHORITY`

Purpose:
Locks castle entrance architecture and DAY / DOOR_OPEN facts.

### C. Continuity reference — 1 PNG

#### 5. N01｜Castle Pause

Path:
`production/image_library/approved/story_shots/N01_CASTLE_PAUSE_APPROVED_V001.png`

Locked identity:
- SHA-256: `a96d52410c1645711545c80b7fe4e3eaa3e8f00b088ebaaea210bbdbec84557b`
- byte size: `2687303`
- Git blob: `d55d2c218926c0b916c67d34979887315c351a1c`

Responsibility:
`POST_OPENING_INSIDE_THRESHOLD_CONTINUITY`

Purpose:
Only to preserve the post-Opening fact that Neil has already crossed inside and waits for the arriving guests.

Restriction:
N01 must not control N12 composition, smile shape, crop or cross placement.

## 3. Why N11 is not included

N11 Rebuild Candidate 01 has been Product Owner approved overall, but the user explicitly chose to defer upload / canonical publication / Story Shot registration until later S02-A batch archival.

Therefore:

- N11 is not yet a canonical Story Shot binary in GitHub;
- the formal bundle must not depend on an unpublished candidate;
- N12 must remain generatable from already-canonical authorities.

This preserves the locked production rule that formal Bundle inputs come from canonical approved assets rather than local/rejected/unpublished candidates.

## 4. Why N09 and N10 are excluded

### N09

N09 places Neil outside on the entrance platform.

That conflicts with current S02-A continuity, where Neil is already inside.

### N10

N10 provides a subtle smile, but it belongs to the earlier exterior pre-turn beat.

Using it as a baseline reference risks:

- pulling Neil back outside;
- reproducing a natural/subtle smile rather than the later rigid smile;
- importing Opening composition into the S02-A observation sequence.

Therefore N10 is not needed.

## 5. Why no separate cross asset is included

The source narration directly establishes:

`Neil wears a cross around his neck.`

No current canonical standalone cross Prop Asset is required to generate this Story Shot.

For N12, the cross should be generated as a simple, realistic, non-ornate pendant under director instruction.

This does **not** create or register a new Prop Asset.

If later production reveals recurring continuity problems with the cross, a separate formal prop-control decision can be made. That is not required for N12 V001.

## 6. Authority precedence

1. `NEIL_FACE_IDENTITY_AUTHORITY`
2. `NEIL_3Q_IDENTITY_AND_CAMERA_ANGLE_AUTHORITY`
3. `NEIL_BODY_AND_COSTUME_STRUCTURE_AUTHORITY`
4. `SCENE_FACT_AUTHORITY`
5. `POST_OPENING_INSIDE_THRESHOLD_CONTINUITY`
6. `DIRECTOR_NARRATIVE_INSTRUCTION_FOR_CROSS_AND_RIGID_SMILE`

The last item is not a binary authority; it is the locked story/performance instruction.

## 7. Director lock to embed in WORK_HANDOFF

- 9:16 vertical.
- Medium close-up / head + upper chest.
- Neil's face remains the primary subject.
- One simple metallic cross is clearly visible but secondary to the face.
- Cross must not glow, enlarge, or dominate composition.
- Smile is small, closed-mouth, rigid, socially polite but emotionally unconvincing.
- No teeth.
- Eyes do not fully participate in the smile.
- Neil remains pale, around fifty, same identity and formal butler clothing.
- Neil remains inside the entrance, facing outward and waiting.
- No turn / step / speaking / greeting gesture.
- No hands / waist / lower torso.
- Dark interior background remains soft and subordinate.
- No exterior-platform composition.
- No horror-poster / vampire / religious-icon treatment.

## 8. Bundle validation requirements

Before artifact upload, all five inputs must pass:

- canonical path existence;
- regular-file / no-symlink check;
- Registry or Story Shot Index authority check;
- approval status;
- lifecycle status;
- byte size;
- SHA-256;
- Git blob SHA;
- PNG signature + dimensions;
- byte-identical copy into bundle;
- final bundle revalidation.

Any mismatch = `FAIL CLOSED`.

## 9. Artifact design

Artifact name:
`N12_REFERENCE_DELIVERY_BUNDLE_V001`

Contents:

`delivery_manifest.json`  
`WORK_HANDOFF.md`  
`visual_refs/AST_IMG_000028__CHAR_NEIL_FACE_FRONT_DEFAULT_DEFAULT_V001.png`  
`visual_refs/AST_IMG_000027__CHAR_NEIL_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`  
`visual_refs/AST_IMG_000026__CHAR_NEIL_BODY_FRONT_DEFAULT_DEFAULT_V001.png`  
`visual_refs/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`  
`continuity_refs/N01__N01_CASTLE_PAUSE_APPROVED_V001.png`

Retention:
`7 days`

Manual Product Owner reference upload:
`0`

## 10. Build boundary

Current stage is Bundle design only.

Not yet authorized:

- creating the temporary GitHub Actions workflow;
- building the artifact;
- Work image generation;
- Story Shot registration;
- batch archival.

Next:
`Product Owner review → Bundle build → Work generation`
