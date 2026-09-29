# N16｜Reference Delivery Bundle Design V0.1

Status: `PRODUCT OWNER APPROVED / BUILT / 6 OF 6 EXACT VERIFICATION PASS / READY FOR WORK GENERATION`

Date: 2026-09-29

Target bundle:

`N16_REFERENCE_DELIVERY_BUNDLE_V001`

Target generation:

`N16 Candidate 01`

Parent authorities:

- `S02-B Director Shot Design V0.1 / PRODUCT OWNER APPROVED + LOCKED`
- `N16 Scene Reference Design V0.1 / PRODUCT OWNER APPROVED + LOCKED`

## 1. N16 Director lock

N16 = `Sister Question`.

Source-audio scope:

`01:18.750 → 01:28.120`

Locked composition:

- 9:16 vertical cinematic audio-comic still;
- medium two-shot;
- Ning Qiushui on screen-left, facing / turning screen-right;
- Jun Luyuan on screen-right, facing / turning screen-left;
- Jun is the speaking emphasis;
- Ning is calm, restrained, clearly readable but secondary;
- both are already on the interior side / threshold zone of the castle entrance;
- still-open castle entrance may remain visible as secondary continuity;
- Neil is not a subject.

## 2. Canonical reference set

Reference count:

`6`

### REF-01｜Jun Luyuan Character Reference Sheet

- asset_id: `AST_IMG_000057`
- entity_id: `CHAR_JUN_LUYUAN`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- path: `production/image_library/derived_reference_sheets/jun_luyuan/CHAR_JUN_LUYUAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- SHA-256: `e8a0410cfc176ec9d6446b84f89b2c12d0683ec32b927c90353e850c416d909e`
- byte_size: `969995`
- Git blob: `d11db79f4ceab2bb52139bfb8805f7c8f09b0cfc`
- responsibility:
  - primary Jun identity;
  - hairstyle;
  - wardrobe;
  - overall body / proportion continuity.

### REF-02｜Jun Luyuan FACE_3Q_LEFT

- asset_id: `AST_IMG_000072`
- entity_id: `CHAR_JUN_LUYUAN`
- role: `FACE_3Q_LEFT`
- asset_class: `ATOMIC`
- authority_class: `AUXILIARY`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- provenance: `COMPLETE`
- path: `production/image_library/character_references/jun_luyuan/CHAR_JUN_LUYUAN_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- SHA-256: `be9f1f39ae303a61a79746b25a0f9f8153797b179ef85d07a5c2fdf1ce02d01b`
- byte_size: `2002451`
- Git blob: `821c892ffea59ef0739f86585c6c5f8bd1168264`
- responsibility:
  - Jun screen-right → screen-left conversational face direction;
  - facial structure / likeness at the required 3/4 angle.

### REF-03｜Ning Qiushui Character Reference Sheet

- asset_id: `AST_IMG_000060`
- entity_id: `CHAR_NING_QIUSHUI`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- path: `production/image_library/derived_reference_sheets/ning_qiushui/CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- SHA-256: `15ec6c2682da0fe2502267bde21e9bc0bd7104bbf3e6041521121cc69a0e77be`
- byte_size: `1123635`
- Git blob: `b674733242ab5d603dc42c53b8f7582003064499`
- responsibility:
  - primary Ning identity;
  - hairstyle;
  - wardrobe;
  - overall body / proportion continuity.

### REF-04｜Ning Qiushui FACE_3Q_RIGHT

- asset_id: `AST_IMG_000033`
- entity_id: `CHAR_NING_QIUSHUI`
- role: `FACE_3Q_RIGHT`
- asset_class: `ATOMIC`
- authority_class: `AUXILIARY`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- provenance: `PARTIAL`
- path: `production/image_library/character_references/ning_qiushui/CHAR_NING_QIUSHUI_FACE_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`
- SHA-256: `7d2292494ab010b324e608f792912fd2d49766318e279bbe22170445464a5c1e`
- byte_size: `2688985`
- Git blob: `6b6a802b67a966f8439c5b000f01d00be422f545`
- responsibility:
  - Ning screen-left → screen-right conversational face direction.
- restriction:
  - directional support only;
  - COMPLETE Ning Character Reference Sheet remains the primary identity authority.

### REF-05｜Castle Entrance Scene Master

- asset_id: `AST_IMG_000052`
- entity_id: `SCENE_CASTLE_ENTRANCE`
- role: `SCENE_MASTER`
- variant / state: `DEFAULT / DAY_DOOR_OPEN`
- authority_class: `MASTER`
- approval / lifecycle / resolver: `APPROVED / CURRENT / CONDITIONAL`
- provenance: `COMPLETE`
- path: `production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- byte_size: `2305753`
- Git blob: `e4dafe096f5c5c8782257030a5a659aeec7808f9`
- responsibility:
  - castle-entrance identity / topology;
  - DAY state;
  - OPEN main-door state;
  - threshold / exterior stone-step relationship.
- restriction:
  - does not dictate N16 camera / blocking / focal length.

### REF-06｜A03 Interior Reverse Continuity

- shot_id: `A03`
- role: `STORY_SHOT_CONTINUITY`
- title: `门内反拍`
- approval / lifecycle: `APPROVED / CURRENT`
- path: `production/image_library/approved/A_Series/A03_REBOOT_approved_v001.png`
- byte_size: `2875484`
- Git blob: `94d11064522425d908b1756fb0d845107c46a4e1`
- SHA-256:
  - compute and record during Bundle build from the canonical binary;
  - no guessed value may be introduced.
- responsibility:
  - interior-side entrance continuity;
  - prevent spatial reset to the exterior welcome staging.
- restriction:
  - continuity authority only;
  - no literal composition copy;
  - no architecture override against AST_IMG_000052.

## 3. Authority precedence

1. `N16 Director Shot Design` — narrative / photography / blocking lock.
2. `AST_IMG_000057` — Jun primary identity continuity.
3. `AST_IMG_000072` — Jun required left-facing 3/4 angle.
4. `AST_IMG_000060` — Ning primary identity continuity.
5. `AST_IMG_000033` — Ning required right-facing 3/4 angle.
6. `AST_IMG_000052` — castle-entrance scene facts / DAY_DOOR_OPEN.
7. `A03` — interior-side shot continuity only.

Conflict rules:

- Reference Sheets win identity conflicts over migrated angle auxiliaries.
- Directional atomic face references control the required reciprocal face orientation.
- Scene Master wins architecture / scene-state conflicts.
- Director lock wins shot photography / blocking.
- A03 may never override Scene Master facts.

## 4. Explicit exclusions

Do not include in `N16_REFERENCE_DELIVERY_BUNDLE_V001`:

- N03;
- N14;
- A05;
- any Neil character asset;
- N11 / N12;
- First Hall Scene Master;
- A07;
- MANOR_GATE Scene Master;
- any rejected / superseded candidate;
- any internet or non-canonical reference.

Reason:

The six locked references already cover all required identity, direction, scene-state and continuity authorities. Additional inputs would add spatial / subject leakage without adding necessary authority.

## 5. WORK_HANDOFF locks

`WORK_HANDOFF.md` must instruct Work to generate exactly:

`N16 Candidate 01`

Generation requirements:

- 9:16 vertical;
- cinematic audio-comic still frame;
- medium two-shot;
- Ning Qiushui on screen-left;
- Jun Luyuan on screen-right;
- Jun looks toward Ning and is the speaking emphasis;
- Ning looks toward Jun with restrained, calm attention;
- both identities must remain faithful to their canonical references;
- preserve established wardrobe and body proportions;
- both characters are already inside / at the interior side of the castle entrance threshold;
- the still-open main door may remain visible only as secondary continuity;
- daylight from outside is allowed;
- natural conversational posture;
- no melodramatic grief;
- no visible comforting embrace / hand-on-shoulder reassurance;
- no exaggerated talking gesture;
- no pointing;
- no direct gaze into camera;
- no posed two-person publicity-photo feeling;
- no Neil;
- no key / waist / pocket emphasis;
- no rain;
- no storm foreshadowing;
- no hall establishment;
- no mural corridor.

Narrative tone:

`quiet personal question / restrained answer / transitional threshold conversation`

## 6. Planned artifact layout

`N16_REFERENCE_DELIVERY_BUNDLE_V001/`

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- `character_authority/AST_IMG_000057__CHAR_JUN_LUYUAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `character_authority/AST_IMG_000072__CHAR_JUN_LUYUAN_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- `character_authority/AST_IMG_000060__CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `character_authority/AST_IMG_000033__CHAR_NING_QIUSHUI_FACE_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`
- `scene_authority/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- `continuity_refs/A03__A03_REBOOT_approved_v001.png`

Retention target:

`7 days`

Product Owner manual reference upload:

`0`

Transport:

`GitHub Actions → short-lived Artifact → Work automatic acquisition`

Codex:

`NOT PART OF THIS STORY SHOT BUNDLE PATH`

## 7. Planned delivery_manifest.json requirements

For every reference entry, record at minimum:

- reference_id / asset_id or shot_id;
- entity_id where applicable;
- role;
- authority purpose;
- canonical path;
- filename;
- approval status;
- lifecycle;
- resolver_usage where applicable;
- expected SHA-256 when registry-locked;
- computed SHA-256;
- expected byte_size;
- actual byte_size;
- expected Git blob;
- actual Git blob;
- PNG signature result;
- dimensions;
- byte-identical-copy result.

Bundle-level fields:

- bundle_id: `N16_REFERENCE_DELIVERY_BUNDLE_V001`;
- target_shot_id: `N16`;
- sequence_id: `S02-B`;
- target_candidate: `N16 Candidate 01`;
- source_commit;
- build_run_id;
- created_at;
- reference_count: `6`;
- all_reference_checks_pass;
- generation_allowed.

This preserves the project-level global Story Shot ID rule:

`shot_id=N16`

while sequence ownership is stored separately:

`sequence_id=S02-B`.

## 8. Build validation contract

Bundle construction must fail closed unless all `6/6` references pass:

1. required reference cardinality = exactly 6;
2. Registry / Story Shot Index lookup returns the intended unique record;
3. entity / role / asset-class / authority identity matches;
4. approval_status = APPROVED;
5. lifecycle = CURRENT;
6. resolver_usage is allowed where applicable;
7. canonical path exists;
8. file is a regular file and not a symlink;
9. expected byte_size matches actual;
10. registry SHA-256 matches actual for REF-01 through REF-05;
11. expected Git blob matches actual;
12. PNG signature is valid;
13. dimensions are readable;
14. artifact copy is byte-identical to canonical binary;
15. copied artifact is revalidated after assembly.

A03 special rule:

- Story Shot Index path + byte size + Git blob must match;
- Bundle build must compute A03 SHA-256 from the canonical binary and record it in the manifest;
- no synthetic / guessed A03 SHA is permitted.

Required result:

`PASS: 6/6 exact canonical reference binaries verified`

Only then:

`GENERATION_ALLOWED = TRUE`

Any mismatch:

`GENERATION_ALLOWED = FALSE`

and Artifact must not be treated as a valid production Bundle.

## 9. Planned build outputs

Expected Artifact name:

`N16_REFERENCE_DELIVERY_BUNDLE_V001`

Expected evidence after a future authorized build:

- workflow source commit;
- GitHub Actions run ID;
- job ID;
- Artifact ID;
- Artifact digest;
- artifact size;
- 6/6 exact binary verification;
- each canonical SHA / byte size / Git blob;
- A03 build-computed SHA-256;
- final `GENERATION_ALLOWED` result.

## 10. Current boundary

This document is Bundle Design only.

Current disposition:

`N16 REFERENCE DELIVERY BUNDLE DESIGN V0.1 = PRODUCT OWNER APPROVED / BUILT / 6 OF 6 PASS / READY FOR WORK`

Not authorized yet:

- GitHub Actions Bundle construction;
- Work automatic artifact acquisition;
- N16 Candidate 01 generation;
- Story Shot publication / registration.


## 11. Build result

Product Owner approved this Bundle Design and authorized construction.

The approved Generic Story Shot Reference Bundle Builder was used.

- source commit: `4a9df630c36e2fc92ada929fcd80403ab57c74e3`
- workflow run ID: `36514238747`
- job ID: `109232868440`
- artifact ID: `11010505345`
- artifact name: `N16_REFERENCE_DELIVERY_BUNDLE_V001`
- artifact digest: `sha256:e44c4fc8e9b8d1499af8866ac601137dd315ac1f386a544eec19b709ac5cd0ff`
- artifact size: `11932780` bytes
- expires at: `2026-10-06T02:47:42Z`
- exact canonical reference verification: `6/6 PASS`
- A03 computed SHA-256: `5dc075a6f917fb7fdc05cf299315675bfdd5db4a0d737518ef4aafeacc78ee1e`
- post-artifact independent verification: `PASS`
- `GENERATION_ALLOWED=TRUE`
- Product Owner manual reference upload: `0`

Build record:

`docs/project_control/gates/P0_3_video_pipeline/n16_reference_delivery_bundle_v001_build_record_2026-09-29.md`

Current boundary:

The Bundle is valid and ready for Work automatic acquisition. Work image generation has not yet been executed.
