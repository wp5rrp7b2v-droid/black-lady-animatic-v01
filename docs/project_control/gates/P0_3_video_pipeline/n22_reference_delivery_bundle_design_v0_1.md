# N22｜Reference Delivery Bundle Design V0.1

Status: `PRODUCT OWNER APPROVED / LOCKED / FORMAL BUILD PASS / 5 OF 5 EXACT VERIFIED / INDEPENDENT ARTIFACT VERIFIED`

Date: 2026-10-02

Target shot:

`N22｜People in the Flow — Ning Observational POV`

Target candidate after separate build + generation authorization:

`N22 Candidate 01｜Clean Regeneration`

Target bundle:

`N22_REFERENCE_DELIVERY_BUNDLE_V001`

Director authority:

`N22 Node-Level Director Shot Design V0.1 / PRODUCT OWNER APPROVED + LOCKED`

Scene Reference authority:

`N22 Scene Reference Design V0.1 / PRODUCT OWNER APPROVED + LOCKED`

Project state at design start:

`R186`

---

## 1. DESIGN OBJECTIVE

Build the smallest practical formal generation package that can support:

- Su Xiaoxiao identity;
- Liao Jian identity;
- Wen Qingya identity;
- Guang Yong identity;
- Castle Entrance / interior-transition scene identity;

while preserving N22's core visual requirement:

`OBSERVED GROUP FRAGMENT / NOT FOUR-PERSON CAST SHOT`

The Bundle must not convert reference presence into:

- fixed screen position;
- fixed left/right order;
- equal prominence;
- fixed pose;
- cast-lineup blocking;
- four-character hero ensemble.

---

## 2. BUNDLE PRINCIPLE

Locked principle:

`MINIMUM NECESSARY AUTHORITY / FIVE INPUTS ONLY FOR FIRST PROOF`

Formal reference count:

`5`

No additional references may be added to V001 before Candidate 01 evidence.

Reason:

The current critical uncertainty is whether four named identities can coexist naturally in one frame.

Adding more visual authorities before the first test would make failure diagnosis less reliable.

---

## 3. FORMAL REFERENCE SET

### REF-01｜Su Xiaoxiao Character Reference Sheet

- reference_id: `AST_IMG_000061`
- source_type: `ASSET`
- entity_id: `CHAR_SU_XIAOXIAO`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- canonical_path: `production/image_library/derived_reference_sheets/su_xiaoxiao/CHAR_SU_XIAOXIAO_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- expected_sha256: `e869d118e22e50cfe6e6280632da4534e660dc74ec96cf3871099b87cf42701a`
- expected_byte_size: `700794`
- expected_git_blob: `2b584d4172484216478319025440b16ba7c2859a`
- destination_group: `identity_primary`
- authority_purpose: `SU_XIAOXIAO_PRIMARY_IDENTITY_AUTHORITY`

Controls:

- Su Xiaoxiao identity;
- face / hair / approved normal-state appearance;
- default clothing language.

Must not control:

- exact pose;
- exact shot angle;
- exact screen position;
- glamour staging;
- future character reveal.

---

### REF-02｜Liao Jian Character Reference Sheet

- reference_id: `AST_IMG_000058`
- source_type: `ASSET`
- entity_id: `CHAR_LIAO_JIAN`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- canonical_path: `production/image_library/derived_reference_sheets/liao_jian/CHAR_LIAO_JIAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- expected_sha256: `3f2f01fea63401a3726abdf5053e75361d5d43091830ce8e1636883bd1cd6817`
- expected_byte_size: `650562`
- expected_git_blob: `f8b600e49c0bd40177c723d9c0abd474678f41c2`
- destination_group: `identity_primary`
- authority_purpose: `LIAO_JIAN_PRIMARY_IDENTITY_AUTHORITY`

Controls:

- Liao Jian identity;
- face / hair / approved normal-state appearance;
- fit young-man body read.

Must not control:

- bodybuilding exaggeration;
- exact pose;
- exact screen position;
- couple staging with Su Xiaoxiao.

---

### REF-03｜Wen Qingya Character Reference Sheet

- reference_id: `AST_IMG_000062`
- source_type: `ASSET`
- entity_id: `CHAR_WEN_QINGYA`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- canonical_path: `production/image_library/derived_reference_sheets/wen_qingya/CHAR_WEN_QINGYA_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- expected_sha256: `09551f02ad9cd4d3ae8e4483d017c230877165c4b88346ff9762527246569f0c`
- expected_byte_size: `641800`
- expected_git_blob: `e391622643034485dc4e9a862ba29cde72cdeefd`
- destination_group: `identity_secondary`
- authority_purpose: `WEN_QINGYA_SECONDARY_IDENTITY_AUTHORITY`

Controls:

- Wen Qingya identity;
- normal-state appearance;
- round-frame glasses / cultured read when naturally visible.

Must not force:

- clean frontal face;
- equal prominence with Tier 1;
- formal introduction staging.

---

### REF-04｜Guang Yong Character Reference Sheet

- reference_id: `AST_IMG_000056`
- source_type: `ASSET`
- entity_id: `CHAR_GUANG_YONG`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- canonical_path: `production/image_library/derived_reference_sheets/guang_yong/CHAR_GUANG_YONG_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- expected_sha256: `2a98e74ddba60a259758643b56ffddafd5a7cb30de040880f991fb47216b45fb`
- expected_byte_size: `475761`
- expected_git_blob: `e37ad60d933c3fdc434768bb449019146eb9333e`
- destination_group: `identity_secondary`
- authority_purpose: `GUANG_YONG_SECONDARY_IDENTITY_AUTHORITY`

Controls:

- Guang Yong identity;
- shorter / slightly chubby silhouette;
- approved normal-state appearance.

Must not force:

- clean frontal hero face;
- equal prominence with Tier 1;
- isolated introduction staging.

---

### REF-05｜Castle Entrance Scene Master

- reference_id: `AST_IMG_000052`
- source_type: `ASSET`
- entity_id: `SCENE_CASTLE_ENTRANCE`
- role: `SCENE_MASTER`
- asset_class: `ATOMIC`
- authority_class: `MASTER`
- approval / lifecycle / resolver: `APPROVED / CURRENT / CONDITIONAL`
- state: `DAY_DOOR_OPEN`
- canonical_path: `production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- expected_sha256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- expected_byte_size: `2305753`
- expected_git_blob: `e4dafe096f5c5c8782257030a5a659aeec7808f9`
- destination_group: `scene_authority`
- authority_purpose: `CASTLE_ENTRANCE_IDENTITY_OPEN_DOOR_MATERIAL_STATE`

Controls:

- Castle Entrance identity;
- open-door state;
- stable architectural / material facts.

Must not control:

- exact camera;
- centered architecture;
- empty-scene composition;
- exterior-dominant lighting;
- monumental scale;
- full First Hall reveal.

---

## 4. REFERENCE ORDER RULE

The Bundle may store references in deterministic semantic order:

1. Su Xiaoxiao;
2. Liao Jian;
3. Wen Qingya;
4. Guang Yong;
5. Castle Entrance.

But Work must receive the explicit rule:

`REFERENCE ORDER ≠ SCREEN POSITION ≠ CHARACTER LEFT/RIGHT ORDER ≠ BLOCKING ORDER ≠ PROMINENCE EQUALITY`

No reference order may be interpreted as compositional placement.

---

## 5. EXCLUDED INPUTS

Do not include in V001:

- N20 canonical Story Shot;
- N21 Candidate 01–08;
- N21 Threshold Transition Environment Reference;
- N21 Crowd Body/Wardrobe Reference;
- CHARACTER_VISUAL_STYLE_REFERENCE_V001;
- Ning Qiushui Character Reference;
- Jun Luyuan Character Reference;
- Neil Character Reference;
- Atomic face / body / profile / rear-3Q images for the four N22 named seeds;
- A03 / A06 / A07;
- First Hall Scene Master;
- mural corridor references;
- internet / non-canonical imagery.

Reason:

`REDUCE VISUAL AUTHORITY CONFLICT / PRESERVE DIAGNOSTIC CLARITY`

---

## 6. N20 CONTINUITY DISPOSITION

N20 remains:

`DIRECTOR-LEVEL LOOK / CONTINUITY AUTHORITY ONLY`

It is not a Bundle image input.

The Work handoff must nevertheless lock:

- dim warm amber / tungsten practical-light interior;
- low-key exposure;
- natural skin;
- restrained saturation;
- moderate cinematic contrast;
- textured dark clothing / stone;
- no direct exterior sunlight flooding floor or bodies;
- limited entrance-to-interior transition scale;
- no full hall establishment.

If Candidate 01 fails only in look continuity while identity and composition pass, a later targeted look-control revision may be considered.

Do not pre-emptively add N20 now.

---

## 7. WORK HANDOFF｜CANDIDATE 01

Title:

`N22｜People in the Flow — Ning Observational POV｜Candidate 01`

Generation mode:

`CLEAN REGENERATION`

Output limit:

`EXACTLY 1 PNG`

After one PNG:

`STOP / WAIT FOR PRODUCT OWNER REVIEW`

### Required visual read

Primary read:

`AN OBSERVED FRAGMENT OF A LARGER MIXED GROUP`

Secondary read:

`SOME INDIVIDUAL PEOPLE MAY MATTER LATER`

N22 is not:

- a full-cohort scale shot;
- a four-character cast shot;
- a lineup;
- a formal introduction scene.

### Character hierarchy

Tier 1 comparatively readable:

- Su Xiaoxiao;
- Liao Jian.

Tier 2 secondary / partial:

- Wen Qingya;
- Guang Yong.

Additional unnamed participants are allowed as:

- cropped shoulders;
- partial bodies;
- rear-facing figures;
- side-facing figures;
- shadowed figures;
- deeper soft-focus figures.

No hard visible-person count.

No requirement that all four named faces be fully visible simultaneously.

### Blocking

Global flow:

`GENERALLY DEEPER INTO CASTLE`

Local human states:

`ASYNCHRONOUS / NON-CHOREOGRAPHED`

Allow:

- one walking;
- one slowing;
- one briefly looking around;
- one partially stopped;
- uneven spacing;
- differing body angles;
- natural overlap;
- partial occlusion.

Avoid:

- single-file queue;
- shoulder-to-shoulder row;
- symmetrical V / arc;
- shared stride phase;
- all heads turned same direction;
- all faces toward camera;
- cast photo / team poster.

### POV

Ning-attributed observation may be conveyed by:

- edit continuity alone; or
- a small cropped / soft shoulder-back edge cue.

Ning is not a required visible subject.

If adding Ning damages composition, omit him.

### Space

Scene:

`CASTLE_ENTRANCE → INTERIOR TRANSITION ZONE`

Architecture:

- off-axis;
- subordinate;
- partially obscured;
- supporting, not spectacular.

Avoid:

- giant centered arch;
- huge symmetrical double doors;
- strong central vanishing point;
- cathedral-scale architecture;
- full First Hall;
- long corridor reveal.

### Neil / Jun

Neil:

`DO NOT EMPHASIZE / PREFER ABSENT`

N23 owns Neil's directional turn.

Jun:

`NOT REQUIRED`

Neither may become an unintended subject.

---

## 8. HARD EXCLUSIONS FOR WORK

Exclude:

- exact 16-person proof;
- explicit 8-men / 8-women counting composition;
- four named characters lined up together;
- promotional ensemble;
- all four equally clear;
- fixed left-to-right order derived from reference order;
- synchronized walking;
- central procession;
- military / ceremonial formation;
- repeated clone faces or bodies;
- exaggerated gestures;
- complex interlocking hand contact;
- luggage / backpacks / travel bags;
- fantasy adventurer costumes;
- spectral / undead styling;
- monumental Gothic showcase;
- global orange cast;
- bright daylight interior reset;
- Neil hero framing;
- Ning / Jun hero two-shot;
- N23 direction-change action.

---

## 9. AUTHORITY PRECEDENCE

1. N22 Director Shot Design V0.1
2. N22 Scene Reference Design V0.1
3. Tier 1 Character Reference Sheets
4. Tier 2 Character Reference Sheets
5. Castle Entrance Scene Master
6. N20 written look / continuity standard

Conflict rules:

- Director Design controls narrative function, hierarchy, framing and blocking.
- Character Sheets control identity, not pose or location.
- Scene Master controls scene facts, not shot composition.
- N20 controls look continuity only through the written contract.
- No image reference may override the Director requirement that the frame remain an observed group fragment.

---

## 10. PLANNED ARTIFACT STRUCTURE

`N22_REFERENCE_DELIVERY_BUNDLE_V001/`

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- `identity_primary/AST_IMG_000061__CHAR_SU_XIAOXIAO_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `identity_primary/AST_IMG_000058__CHAR_LIAO_JIAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `identity_secondary/AST_IMG_000062__CHAR_WEN_QINGYA_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `identity_secondary/AST_IMG_000056__CHAR_GUANG_YONG_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `scene_authority/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`

Retention:

`7 days`

Product Owner manual reference upload:

`0`

Transport:

`GitHub Actions → Artifact → Work automatic acquisition`

Codex:

`NOT PART OF THIS STORY SHOT BUNDLE PATH`

---

## 11. BUILDER CONTRACT

Use existing workflow only:

`.github/workflows/story-shot-reference-bundle-builder.yml`

Builder:

`STORY_SHOT_REFERENCE_BUNDLE_BUILDER_V1`

Do not create an N22-specific workflow.

Planned Bundle Spec path after separate Product Owner approval:

`production/bundle_specs/N22_REFERENCE_DELIVERY_BUNDLE_V001.json`

The spec should initially be committed with:

`build_authorized=false`

for validation-only preflight if a staged authorization boundary is desired.

Formal Artifact build requires separate Product Owner authorization and:

`build_authorized=true`

No image generation is authorized by spec creation or validation-only success.

---

## 12. BUILD VALIDATION

Builder must fail closed unless all 5/5 references pass:

- canonical path;
- declared reference identity;
- APPROVED status;
- CURRENT lifecycle;
- resolver eligibility where applicable;
- exact byte size;
- exact SHA-256;
- exact Git blob;
- PNG signature;
- readable dimensions;
- byte-identical copy into Artifact;
- post-assembly revalidation.

Required validation result:

`PASS: 5/5 exact canonical reference binaries verified`

Only a formally authorized build may then report:

`GENERATION_ALLOWED=TRUE`

Validation-only preflight must not create a production Artifact.

---

## 13. MINIMUM PROOF / DIAGNOSTIC GATE

After later successful Bundle build and separate Product Owner generation authorization:

`N22 Candidate 01 = EXACTLY ONE PNG`

### PASS

Reference architecture passes if:

- Su identity preserved;
- Liao identity preserved;
- Wen remains usable as secondary seed;
- Guang remains usable as secondary seed;
- image reads as a larger-group fragment;
- no four-person lineup;
- scene reads as entrance/interior transition;
- architecture remains subordinate;
- N20 warm low-key continuity broadly holds;
- no Neil / Jun leakage as unintended subjects.

### FAIL-A｜Identity collapse

If Tier 1 identity fails:

`TARGETED CHARACTER AUTHORITY REVIEW`

Do not add all Atomic assets.

Only the failing character may receive targeted augmentation in a later Bundle revision.

### FAIL-B｜Poster / lineup

If identity is good but composition becomes a four-person ensemble:

`REDUCE NAMED CHARACTER COMPLEXITY`

Preserve:

- Su Xiaoxiao;
- Liao Jian;

and only one Tier 2 readable seed.

Do not add more references.

### FAIL-C｜Look continuity failure

If identity + composition pass but look is too bright / cold / inconsistent:

`TARGETED LOOK-CONTINUITY REVIEW`

Consider one controlled look authority only after diagnosis.

Do not automatically inject N20 raw Story Shot.

### FAIL-D｜Scene identity failure

If Castle Entrance continuity fails:

`REVIEW SCENE MASTER USAGE`

Do not automatically reuse N21 environment reference.

---

## 14. CURRENT BOUNDARY

Current status:

`PRODUCT OWNER APPROVED / LOCKED / FORMAL BUILD PASS / 5 OF 5 EXACT VERIFIED / INDEPENDENT ARTIFACT VERIFIED`

Formal build result:

- spec revision: `V001-R2`
- authorization commit: `8cc4a9dbc959c8fa9f49d5e6a2b36649a53d58d3`
- workflow run: `36962281468`
- job: `110698343917`
- Builder verification: `PASS: 5/5 exact canonical reference binaries verified`
- `GENERATION_ALLOWED=TRUE`
- Artifact ID: `11208576712`
- Artifact size: `4,752,815 bytes`
- Artifact digest: `sha256:301a127df57e197580c0b87aa0beb7d59c2687d3edd16686c10caa8f841f5c58`
- independent ZIP digest: `MATCH`
- independent reference verification: `5/5 PASS`

Build record:

`docs/project_control/gates/P0_3_video_pipeline/n22_reference_delivery_bundle_v001_build_record_2026-10-02.md`

Current authorization boundary:

- formal Bundle: `READY`
- Work generation: `NOT AUTHORIZED`
- Candidate 01: `NOT AUTHORIZED`
- N23: `NOT AUTHORIZED`

Next step:

`PRODUCT OWNER N22 CANDIDATE 01 WORK GENERATION AUTHORIZATION`
