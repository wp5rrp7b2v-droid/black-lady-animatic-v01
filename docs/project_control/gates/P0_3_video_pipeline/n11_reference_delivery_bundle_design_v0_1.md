# N11｜Reference Delivery Bundle Design V0.1

Status: `PRODUCT OWNER APPROVED / BUILT / 6 OF 6 EXACT VERIFICATION PASS / READY FOR WORK GENERATION`

Target bundle ID: `N11_REFERENCE_DELIVERY_BUNDLE_V001`

Working shot: `N11｜Neil Abnormal Portrait`

Target generation: `N11 Candidate 01`

Transport rule: RC-022 / RC-023  
Story Shot governance: RC-024 / RC-025

## 1. Bundle objective

Deliver only the minimum references needed for Work to generate N11 with:

- stable Neil identity;
- stable formal butler clothing;
- correct castle entrance / open-door scene facts;
- corrected spatial continuity: Neil is already **inside** the threshold and facing outward;
- no leakage of later N12 cross/smile emphasis;
- no leakage of later N13/N15/A05 waist/key narrative.

This bundle is a short-lived transport artifact, not a formal Asset.

## 2. Proposed reference set

Reference count: `6`

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
Primary face identity, age structure, grooming, facial proportions.

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
Supports the mild 3/4 observational angle while preserving identity.

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
Locks black butler suit / white shirt / body structure without importing an exterior Story Shot composition.

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

### C. Story Shot continuity — 2 PNG

#### 5. N01｜Castle Pause

Path:
`production/image_library/approved/story_shots/N01_CASTLE_PAUSE_APPROVED_V001.png`

Locked identity:
- SHA-256: `a96d52410c1645711545c80b7fe4e3eaa3e8f00b088ebaaea210bbdbec84557b`
- byte size: `2687303`
- Git blob: `d55d2c218926c0b916c67d34979887315c351a1c`

Responsibility:
`IMMEDIATE_PREVIOUS_OPENING_END_STATE_CONTINUITY`

Purpose:
Immediate predecessor continuity after Neil's threshold action and the waiting state of the group.

Restriction:
N01 is continuity-only. It may not override Neil identity or Scene Master facts, and N11 must not simply copy N01 composition.

#### 6. A03｜门内反拍

Path:
`production/image_library/approved/A_Series/A03_REBOOT_approved_v001.png`

Locked index identity:
- byte size: `2875484`
- Git blob: `94d11064522425d908b1756fb0d845107c46a4e1`
- approval: `APPROVED / CURRENT`

Responsibility:
`INTERIOR_SIDE_ENTRANCE_SPATIAL_REFERENCE_ONLY`

Purpose:
Supports the interior-side / open-door spatial reading for N11.

Bundle-build rule:
The build workflow must compute and record the actual SHA-256 from the canonical A03 binary and verify byte size + Git blob before publication. No guessed SHA is permitted.

Restriction:
A03 may guide spatial relationship only; it cannot override the Scene Master.

## 3. Why N09 is deliberately excluded

N09 is a strong Neil costume/detail reference, but its locked story function places Neil **outside** on the entrance platform.

Because Product Owner has corrected N11 to an inside-threshold state, including N09 would create a conflicting spatial cue.

Costume/body continuity is therefore sourced from canonical BODY_FRONT instead.

## 4. Why N05 is deliberately excluded

N05 proves the threshold-crossing action, but N11 begins after that action is complete.

N01 is the immediate Opening end-state reference and is therefore more relevant.

If later generation repeatedly regresses Neil back outside, N05 may be added in a controlled Bundle V002 as movement-history evidence. It is not baseline input for V001.

## 5. Authority precedence

1. `NEIL_FACE_IDENTITY_AUTHORITY`
2. `NEIL_3Q_IDENTITY_AND_CAMERA_ANGLE_AUTHORITY`
3. `NEIL_BODY_AND_COSTUME_STRUCTURE_AUTHORITY`
4. `SCENE_FACT_AUTHORITY`
5. `IMMEDIATE_PREVIOUS_OPENING_END_STATE_CONTINUITY`
6. `INTERIOR_SIDE_ENTRANCE_SPATIAL_REFERENCE_ONLY`

Story Shot continuity must never override canonical character or scene authority.

## 6. Director lock to embed in WORK_HANDOFF

- Neil has already crossed inside the open castle entrance.
- He stands clearly on the interior side, facing outward toward the arriving guests.
- Medium close-up / chest-up.
- Near eye-level, mild 3/4 observational angle.
- Pale skin and roughly fifty-year-old appearance must read.
- Still / controlled / waiting.
- Mouth closed.
- No friendly smile.
- No exaggerated rigid grin.
- Cross may be incidentally visible but is not the focus.
- No turn / step / hand gesture.
- No waist close-up, keys, or no-keys reveal.
- N12 owns cross + rigid-smile emphasis.
- A05 later owns the explicit no-keys reveal.

## 7. Bundle validation requirements

Before artifact upload, all 6 inputs must pass:

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

## 8. Artifact design

Artifact name:
`N11_REFERENCE_DELIVERY_BUNDLE_V001`

Contents:

`delivery_manifest.json`  
`WORK_HANDOFF.md`  
`visual_refs/AST_IMG_000028__CHAR_NEIL_FACE_FRONT_DEFAULT_DEFAULT_V001.png`  
`visual_refs/AST_IMG_000027__CHAR_NEIL_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`  
`visual_refs/AST_IMG_000026__CHAR_NEIL_BODY_FRONT_DEFAULT_DEFAULT_V001.png`  
`visual_refs/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`  
`continuity_refs/N01__N01_CASTLE_PAUSE_APPROVED_V001.png`  
`continuity_refs/A03__A03_REBOOT_approved_v001.png`

Retention:
`7 days`

Manual Product Owner reference upload:
`0`

## 9. Build result

- Product Owner approved Bundle Design V0.1 on 2026-09-27.
- Workflow source commit: `ac83d41398f8fe7d6f3ef0ef24ca1921e8804909`
- Successful run: `36303103682`
- Artifact ID: `10925624760`
- Artifact digest: `sha256:f2bba3b9dcb3a064c20b4cdc2267d8bc7862ec9c8d9f20d700ae6b5715aa2c4f`
- Exact reference verification: `6/6 PASS`
- A03 computed SHA-256: `5dc075a6f917fb7fdc05cf299315675bfdd5db4a0d737518ef4aafeacc78ee1e`

Formal build record:

`docs/project_control/gates/P0_3_video_pipeline/n11_reference_delivery_bundle_v001_build_record_2026-09-27.md`

## 10. Production boundary

Bundle design and build are complete.

Authorized next step:

- ChatGPT Work may use `N11_REFERENCE_DELIVERY_BUNDLE_V001` to generate exactly one `N11 Candidate 01`.

Still not authorized:

- N12 generation;
- N11 Story Shot registration before Product Owner approval;
- S02-A final timeline lock;
- P0.3 Gate PASS.
