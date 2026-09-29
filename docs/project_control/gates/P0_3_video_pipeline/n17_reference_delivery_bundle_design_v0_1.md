# N17｜Reference Delivery Bundle Design V0.1

Status: `PRODUCT OWNER APPROVED / BUILD AUTHORIZED`

Date: 2026-09-29

Target bundle:

`N17_REFERENCE_DELIVERY_BUNDLE_V001`

Target generation:

`N17 Candidate 01`

Parent authorities:

- `S02-B Director Shot Design V0.1 / PRODUCT OWNER APPROVED + LOCKED`
- `N17 Scene Reference Design V0.2 / PRODUCT OWNER APPROVED + LOCKED`

## 1. N17 Director lock

N17 = `Blood-Door Warning`.

Source-audio scope:

`01:28.120 → 01:40.700`

Locked visual progression:

`N16 balanced medium two-shot / Jun speaking emphasis → N17 Ning-dominant close-up / survival-warning emphasis`

Locked composition:

- 9:16 vertical cinematic audio-comic still;
- close-up / tight medium-close;
- Ning Qiushui is the clear primary subject;
- Ning remains on screen-left / oriented toward screen-right;
- Jun Luyuan remains on screen-right only as secondary listener;
- Jun may appear as partial cheek / shoulder edge or soft foreground 3/4 listener;
- framing is visibly tighter than N16;
- background architecture is subordinate / shallow-depth;
- same castle-entrance interior / threshold state;
- DAY / DOOR_OPEN continuity remains valid even if only a small fragment is visible;
- no Neil;
- no literal visualization of survival rules;
- no lecture or reprimand staging.

Narrative tone:

`experienced warning / restrained vigilance / practical familiarity`

## 2. Canonical reference set

Reference count:

`6`

### REF-01｜Ning Qiushui Character Reference Sheet

- reference_id: `AST_IMG_000060`
- source_type: `ASSET`
- entity_id: `CHAR_NING_QIUSHUI`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- provenance: `COMPLETE`
- canonical_path: `production/image_library/derived_reference_sheets/ning_qiushui/CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- SHA-256: `15ec6c2682da0fe2502267bde21e9bc0bd7104bbf3e6041521121cc69a0e77be`
- byte_size: `1123635`
- Git blob: `b674733242ab5d603dc42c53b8f7582003064499`
- destination_group: `character_authority`
- authority_purpose: `NING_PRIMARY_IDENTITY_CONTINUITY`

Responsibility:

- primary Ning identity;
- hairstyle;
- wardrobe;
- facial / body proportion continuity.

N17 is Ning-dominant, so this is the highest character-identity authority in the Bundle.

---

### REF-02｜Ning Qiushui FACE_3Q_RIGHT

- reference_id: `AST_IMG_000033`
- source_type: `ASSET`
- entity_id: `CHAR_NING_QIUSHUI`
- role: `FACE_3Q_RIGHT`
- asset_class: `ATOMIC`
- authority_class: `AUXILIARY`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- provenance: `PARTIAL`
- canonical_path: `production/image_library/character_references/ning_qiushui/CHAR_NING_QIUSHUI_FACE_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`
- SHA-256: `7d2292494ab010b324e608f792912fd2d49766318e279bbe22170445464a5c1e`
- byte_size: `2688985`
- Git blob: `6b6a802b67a966f8439c5b000f01d00be422f545`
- destination_group: `character_authority`
- authority_purpose: `NING_RIGHT_FACING_3Q_DIRECTION`

Responsibility:

- Ning screen-left → screen-right conversational direction;
- facial structure support at the intended 3/4 angle.

Restriction:

- directional support only;
- the COMPLETE Character Reference Sheet remains primary identity authority.

---

### REF-03｜Jun Luyuan Character Reference Sheet

- reference_id: `AST_IMG_000057`
- source_type: `ASSET`
- entity_id: `CHAR_JUN_LUYUAN`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- provenance: `COMPLETE`
- canonical_path: `production/image_library/derived_reference_sheets/jun_luyuan/CHAR_JUN_LUYUAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- SHA-256: `e8a0410cfc176ec9d6446b84f89b2c12d0683ec32b927c90353e850c416d909e`
- byte_size: `969995`
- Git blob: `d11db79f4ceab2bb52139bfb8805f7c8f09b0cfc`
- destination_group: `character_authority`
- authority_purpose: `JUN_SECONDARY_LISTENER_IDENTITY_CONTINUITY`

Responsibility:

- preserve Jun identity / hair / wardrobe even when partly cropped or softly focused.

---

### REF-04｜Jun Luyuan FACE_3Q_LEFT

- reference_id: `AST_IMG_000072`
- source_type: `ASSET`
- entity_id: `CHAR_JUN_LUYUAN`
- role: `FACE_3Q_LEFT`
- asset_class: `ATOMIC`
- authority_class: `AUXILIARY`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- provenance: `COMPLETE`
- canonical_path: `production/image_library/character_references/jun_luyuan/CHAR_JUN_LUYUAN_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- SHA-256: `be9f1f39ae303a61a79746b25a0f9f8153797b179ef85d07a5c2fdf1ce02d01b`
- byte_size: `2002451`
- Git blob: `821c892ffea59ef0739f86585c6c5f8bd1168264`
- destination_group: `character_authority`
- authority_purpose: `JUN_LEFT_FACING_LISTENER_DIRECTION`

Responsibility:

- Jun screen-right → screen-left listening direction;
- prevent face-direction / likeness drift if Jun's face remains visible.

---

### REF-05｜Castle Entrance Scene Master / DAY_DOOR_OPEN

- reference_id: `AST_IMG_000052`
- source_type: `ASSET`
- entity_id: `SCENE_CASTLE_ENTRANCE`
- role: `SCENE_MASTER`
- asset_class: `ATOMIC`
- authority_class: `MASTER`
- approval / lifecycle / resolver: `APPROVED / CURRENT / CONDITIONAL`
- provenance: `COMPLETE`
- canonical_path: `production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- byte_size: `2305753`
- Git blob: `e4dafe096f5c5c8782257030a5a659aeec7808f9`
- destination_group: `scene_authority`
- authority_purpose: `CASTLE_ENTRANCE_DAY_DOOR_OPEN_SCENE_AUTHORITY`

Responsibility:

- castle-entrance identity / topology;
- DAY state;
- OPEN main-door state;
- threshold continuity.

Restriction:

- close-up photography may obscure most architecture;
- Scene Master owns scene facts, not the amount of background shown.

---

### REF-06｜N16 Immediate Story Shot Continuity

- reference_id: `N16`
- source_type: `STORY_SHOT`
- shot_id: `N16`
- title: `Sister Question`
- approval / lifecycle: `APPROVED / CURRENT`
- canonical_path: `production/image_library/approved/story_shots/N16_SISTER_QUESTION_APPROVED_V001.png`
- SHA-256: `b26fb7d64a60fbd28d39b0ae22f7c85df18d4f947f31a3591c847dd5e1acf406`
- byte_size: `1942422`
- Git blob: `44971dd53e37cd1b582bcf5094b0f09cb8e0647d`
- destination_group: `continuity_refs`
- authority_purpose: `IMMEDIATE_N16_TO_N17_DIALOGUE_CONTINUITY`

Responsibility:

- immediate shot-to-shot wardrobe continuity;
- Ning-left / Jun-right geography;
- reciprocal eye-line;
- local light continuity;
- same interior entrance / threshold state;
- quiet conversation continuity.

Required controlled change:

- N17 must not duplicate N16 composition;
- N17 must be visibly tighter;
- Ning becomes primary;
- Jun becomes secondary;
- background becomes less important.

## 3. Authority precedence

1. `S02-B Director Shot Design V0.1` — narrative / shot function.
2. `N17 Scene Reference Design V0.2` — close-up composition lock.
3. `AST_IMG_000060` — Ning primary identity.
4. `AST_IMG_000033` — Ning right-facing 3/4 support.
5. `AST_IMG_000057` — Jun identity continuity.
6. `AST_IMG_000072` — Jun left-facing listening support.
7. `AST_IMG_000052` — castle-entrance scene facts / DAY_DOOR_OPEN.
8. `N16` — immediate shot-to-shot continuity.

Conflict rules:

- COMPLETE Character Reference Sheets win identity conflicts.
- Directional atomic face references control conversational orientation.
- Scene Master wins scene-state / architecture conflicts.
- N16 controls immediate continuity but cannot override Character or Scene Master authority.
- Director / Scene Reference locks control final framing and narrative emphasis.

## 4. Explicit exclusions

Do not include in `N17_REFERENCE_DELIVERY_BUNDLE_V001`:

- A03;
- N03;
- N14;
- A05;
- A07;
- any Neil character reference;
- First Hall Scene Master;
- MANOR_GATE Scene Master;
- N18–N22;
- rejected / superseded candidates;
- any internet / non-canonical image.

Reason:

The six locked references fully cover identity, face direction, scene state and immediate continuity. Extra images would increase subject / spatial leakage without adding necessary authority.

## 5. WORK_HANDOFF locks

`WORK_HANDOFF.md` must instruct Work to generate exactly:

`N17 Candidate 01`

Generation requirements:

- 9:16 vertical cinematic audio-comic still;
- close-up / tight medium-close;
- Ning Qiushui is the dominant primary subject;
- Ning remains screen-left / oriented screen-right;
- Jun Luyuan remains screen-right only as secondary listener;
- preferred Jun treatment: partial cheek / shoulder edge OR softly focused 3/4 foreground;
- Jun must remain recognizable but must not compete with Ning;
- visibly tighter framing than N16;
- preserve N16 wardrobe / local-light / left-right continuity;
- preserve canonical Ning and Jun identities;
- preserve CASTLE_ENTRANCE / DAY / DOOR_OPEN scene state;
- background architecture subordinate / softly out of focus;
- Ning expression = calm / experienced / focused / mildly serious;
- Jun expression = attentive / neutral / not frightened;
- Ning may appear lightly speaking, but no exaggerated mouth-open state;
- no direct camera gaze.

Explicit exclusions:

- Neil;
- finger pointing;
- lecture / classroom pose;
- reprimand pose;
- large teaching gesture;
- heroic exposition;
- fear / panic;
- rain;
- wet clothing;
- storm foreshadowing;
- rule text;
- floating warning symbols;
- staring-eye graphics;
- highlighted “do not touch” props;
- key / waist / pocket emphasis;
- hall establishment;
- mural corridor;
- beauty portrait;
- promotional character portrait;
- extreme close-up.

Narrative tone:

`practical survival warning / quiet experienced vigilance`

## 6. Planned artifact layout

`N17_REFERENCE_DELIVERY_BUNDLE_V001/`

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- `character_authority/AST_IMG_000060__CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `character_authority/AST_IMG_000033__CHAR_NING_QIUSHUI_FACE_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`
- `character_authority/AST_IMG_000057__CHAR_JUN_LUYUAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `character_authority/AST_IMG_000072__CHAR_JUN_LUYUAN_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- `scene_authority/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- `continuity_refs/N16__N16_SISTER_QUESTION_APPROVED_V001.png`

Retention target:

`7 days`

Product Owner manual reference upload:

`0`

Transport:

`GitHub Actions → short-lived Artifact → Work automatic acquisition`

Codex:

`NOT PART OF THIS STORY SHOT BUNDLE PATH`

## 7. Planned Bundle Spec contract

Future spec path after explicit Product Owner build authorization:

`production/bundle_specs/N17_REFERENCE_DELIVERY_BUNDLE_V001.json`

The spec must use:

- schema_version: `1.0`
- bundle_id: `N17_REFERENCE_DELIVERY_BUNDLE_V001`
- target_shot_id: `N17`
- sequence_id: `S02-B`
- target_candidate: `N17 Candidate 01`
- retention_days: `7`
- manual_product_owner_reference_upload: `0`
- builder_version: `STORY_SHOT_REFERENCE_BUNDLE_BUILDER_V1`

No new per-shot workflow is allowed.

The existing fixed workflow must be used:

`.github/workflows/story-shot-reference-bundle-builder.yml`

## 8. Build validation contract

Future Bundle construction must fail closed unless all `6/6` references pass:

1. required reference cardinality = exactly 6;
2. Registry / Story Shot Index lookup returns the intended unique record;
3. entity / role / authority identity matches where applicable;
4. approval_status = APPROVED;
5. lifecycle = CURRENT;
6. resolver_usage allowed where applicable;
7. canonical path matches the locked path;
8. file exists as a regular non-symlink;
9. exact byte size matches;
10. exact SHA-256 matches;
11. exact Git blob matches;
12. PNG signature valid;
13. dimensions readable;
14. artifact copy byte-identical to canonical binary;
15. final post-assembly artifact revalidation passes.

N16 continuity special rule:

- unlike the historical A03 case, N16 already has a formally locked SHA-256 identity in Story Shot Index;
- therefore N16 must use direct exact verification of SHA-256 / byte_size / Git blob;
- no `COMPUTE_FROM_LOCKED_PATH_SIZE_GIT_BLOB` fallback is needed.

Required builder result:

`PASS: 6/6 exact canonical reference binaries verified`

Only then:

`GENERATION_ALLOWED = TRUE`

Any mismatch:

`GENERATION_ALLOWED = FALSE`

and Work must not generate N17 from that Artifact.

## 9. Planned build outputs

Expected Artifact name:

`N17_REFERENCE_DELIVERY_BUNDLE_V001`

Expected build evidence after future authorization:

- source commit;
- GitHub Actions run ID;
- job ID;
- Artifact ID;
- Artifact digest;
- Artifact size;
- expiry;
- 6/6 exact binary verification;
- each reference SHA-256 / byte_size / Git blob;
- post-artifact independent verification;
- final `GENERATION_ALLOWED` result.

## 10. Current boundary

This document is Bundle Design only.

Current disposition:

`N17 REFERENCE DELIVERY BUNDLE DESIGN V0.1 = PRODUCT OWNER APPROVED / BUILD AUTHORIZED`

Not authorized yet:

- N17 Bundle Spec creation;
- GitHub Actions Bundle construction;
- Artifact production;
- Work artifact acquisition;
- N17 Candidate 01 generation;
- Story Shot publication / registration.


## 11. Product Owner approval

On 2026-09-29, the Product Owner explicitly approved this Bundle Design.

Authorized next step:

- create `production/bundle_specs/N17_REFERENCE_DELIVERY_BUNDLE_V001.json`;
- run the existing Generic Story Shot Reference Bundle Builder V1;
- verify the resulting Artifact and exact 6/6 canonical inputs.

Still not authorized by this approval:

- N17 image generation before Bundle verification PASS;
- Story Shot publication / registration.
