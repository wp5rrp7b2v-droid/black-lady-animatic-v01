# N13｜Reference Delivery Bundle Design V0.1

Status: `PRODUCT OWNER APPROVED / BUILT / 5 OF 5 EXACT VERIFICATION PASS / READY FOR WORK GENERATION`

Date: 2026-09-27

Target bundle ID: `N13_REFERENCE_DELIVERY_BUNDLE_V001`

Target generation: `N13 Candidate 01`

Transport: RC-022 / RC-023  
Story Shot governance: RC-024 / RC-025

## 1. Objective

Deliver the minimum canonical references required to generate N13 as a downward-attention transition toward Neil's waist without prematurely revealing that the waist is empty.

## 2. Locked reference set

Reference count: `5`

### AST_IMG_000028｜Neil FACE_FRONT

Path:
`production/image_library/character_references/neil/CHAR_NEIL_FACE_FRONT_DEFAULT_DEFAULT_V001.png`

- SHA-256: `e75f0cba8f48d948069b978d86d46e96f7f5f0abd7a40341a5f92e006cb18939`
- bytes: `2517908`
- Git blob: `f3e74a06562d8751dd84c0d228b486769abdd254`

Responsibility:
`NEIL_FACE_IDENTITY_AUTHORITY`

### AST_IMG_000027｜Neil FACE_3Q_LEFT

Path:
`production/image_library/character_references/neil/CHAR_NEIL_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`

- SHA-256: `252f18eff4511a6b1255c751448a7fb667ad68ea2f9ebae49824ce3f453ea037`
- bytes: `2529346`
- Git blob: `0d2638f02caa2697220f0073109fedac50e68246`

Responsibility:
`NEIL_3Q_IDENTITY_AUTHORITY`

### AST_IMG_000026｜Neil BODY_FRONT

Path:
`production/image_library/character_references/neil/CHAR_NEIL_BODY_FRONT_DEFAULT_DEFAULT_V001.png`

- SHA-256: `f78ccfc252d2ed0cb31117ce1dae4c84893c5e52611a27fac161c8e6d014cf3d`
- bytes: `2605161`
- Git blob: `59939fba0a02b9364dbdc2d9ff8203fb57efa7f4`

Responsibility:
`NEIL_BODY_COSTUME_AND_TORSO_STRUCTURE_AUTHORITY`

This is the most important binary authority for N13 because the shot must read the vest / jacket / near-waist region correctly.

### AST_IMG_000052｜Castle Entrance Scene Master

Path:
`production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`

- SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- bytes: `2305753`
- Git blob: `e4dafe096f5c5c8782257030a5a659aeec7808f9`

Responsibility:
`SCENE_FACT_AUTHORITY`

### N01｜Castle Pause

Path:
`production/image_library/approved/story_shots/N01_CASTLE_PAUSE_APPROVED_V001.png`

- SHA-256: `a96d52410c1645711545c80b7fe4e3eaa3e8f00b088ebaaea210bbdbec84557b`
- bytes: `2687303`
- Git blob: `d55d2c218926c0b916c67d34979887315c351a1c`

Responsibility:
`POST_OPENING_INSIDE_THRESHOLD_CONTINUITY`

Restriction:
N01 proves only that Neil is already inside and facing the arriving group. It must not dictate N13 framing.

## 3. Explicit exclusions

Do not include:

- N11 Candidate 03 — creatively approved but not yet canonically published;
- N12 Candidate 02 — creatively approved but not yet canonically published;
- N09 — exterior-platform continuity conflict;
- N10 — exterior state + smile-performance bias;
- A05 — owns the reveal and would risk leaking "empty waist / no keys";
- all rejected or superseded candidates.

## 4. Why A05 is intentionally excluded

A05 is canonical and approved, but its narrative authority is the answer.

N13 must only guide attention toward the waist.

Using A05 as a generation reference creates an avoidable risk that the model will reproduce the answer too early.

Therefore A05 remains downstream editorial continuity, not an N13 Bundle input.

## 5. Authority precedence

1. `NEIL_BODY_COSTUME_AND_TORSO_STRUCTURE_AUTHORITY`
2. `NEIL_FACE_IDENTITY_AUTHORITY`
3. `NEIL_3Q_IDENTITY_AUTHORITY`
4. `SCENE_FACT_AUTHORITY`
5. `POST_OPENING_INSIDE_THRESHOLD_CONTINUITY`
6. `DIRECTOR_NARRATIVE_LOCK: APPROACH_WAIST_WITHOUT_REVEAL`

## 6. WORK_HANDOFF lock

- 9:16 vertical.
- Torso transition shot / lower medium close-up.
- Primary visual interest moves downward toward vest / jacket / near-waist region.
- Neil remains inside the entrance, facing outward and still.
- No hands, gestures, turn, step, speaking or clothing adjustment.
- Cross / chain are not narrative subjects.
- Do not show keys.
- Do not make the absence of keys obvious.
- Do not expose the entire waist region cleanly.
- Preserve some occlusion / crop / jacket overlap so the viewer is led toward the answer but cannot yet read it.
- No full-body framing.
- No exterior-platform composition.
- No clothing-catalog pose.
- A05 remains the exclusive reveal.

## 7. Validation

Before artifact upload, all five inputs must pass:

- canonical path;
- regular file / no symlink;
- Registry / Story Shot Index identity;
- approval / lifecycle;
- byte size;
- SHA-256;
- Git blob SHA;
- PNG signature + dimensions;
- byte-identical copy;
- final bundle revalidation.

Any mismatch = `FAIL CLOSED`.

## 8. Artifact layout

`N13_REFERENCE_DELIVERY_BUNDLE_V001/`

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- `visual_refs/AST_IMG_000028__CHAR_NEIL_FACE_FRONT_DEFAULT_DEFAULT_V001.png`
- `visual_refs/AST_IMG_000027__CHAR_NEIL_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- `visual_refs/AST_IMG_000026__CHAR_NEIL_BODY_FRONT_DEFAULT_DEFAULT_V001.png`
- `visual_refs/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- `continuity_refs/N01__N01_CASTLE_PAUSE_APPROVED_V001.png`

Retention:
`7 days`

Manual Product Owner reference upload:
`0`

## 9. Build result

- Source commit: `bdd2480fb995462f89ea51400d02b0135912ce42`
- Run: `36314032099`
- Job: `108605228883`
- Artifact ID: `10930326122`
- Artifact digest: `sha256:0b40fd3e34b18297c679c2e307f2e4d6480e90c2eef1697adcbdd8b15d8d6fb7`
- Exact verification: `5/5 PASS`

Build record:

`docs/project_control/gates/P0_3_video_pipeline/n13_reference_delivery_bundle_v001_build_record_2026-09-27.md`

## 10. Current boundary

Reference set and design are approved.

The bundle has been built and verified. The next authorized step is Work generation of exactly one N13 Candidate 01.
