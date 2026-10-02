# N22｜Reference Delivery Bundle V003 Design V0.1

Status: `PRODUCT OWNER APPROVED / LOCKED / BUNDLE V003 SPEC + VALIDATION-ONLY PREPARATION NEXT`

Date: 2026-10-02

Target shot:

`N22｜People in the Flow — Ning Observational POV`

Target candidate:

`N22 Candidate 03｜Clean Regeneration`

Target Bundle:

`N22_REFERENCE_DELIVERY_BUNDLE_V003`

Evidence authority:

- `N22 Candidate 02 Review Closeout / NOT APPROVED / LIGHTING PASS / ENSEMBLE FAIL`
- `N22 Candidate 03 Correction Strategy V0.1 / PRODUCT OWNER APPROVED + LOCKED`

---

## 1. CHANGE CONTROL

This is a narrow revision of Bundle V002.

Bundle V002 proved:

- Candidate 02 lighting correction works;
- Castle Entrance scene identity remains stable;
- Su Xiaoxiao identity remains stable;
- Liao Jian identity remains stable;
- foreground anonymous obstruction helps restore larger-group context.

Bundle V003 changes only the remaining failed variable:

`NAMED-CHARACTER ENSEMBLE PRESSURE`

### Removed

`AST_IMG_000056｜CHAR_GUANG_YONG Character Reference Sheet`

Reason:

Candidate 02 showed that Guang Yong remained too readable and continued to reinforce a three-character ensemble.

### Preserved

- Su Xiaoxiao identity authority;
- Liao Jian identity authority;
- Castle Entrance scene authority;
- Candidate 02 written lighting contract.

No successful Candidate 02 lighting/scene control is reopened.

---

## 2. FORMAL REFERENCE SET

Reference count:

`3`

### REF-01｜Su Xiaoxiao

- reference_id: `AST_IMG_000061`
- entity_id: `CHAR_SU_XIAOXIAO`
- role: `CHARACTER_REFERENCE_SHEET`
- canonical_path: `production/image_library/derived_reference_sheets/su_xiaoxiao/CHAR_SU_XIAOXIAO_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- expected_sha256: `e869d118e22e50cfe6e6280632da4534e660dc74ec96cf3871099b87cf42701a`
- expected_byte_size: `700794`
- expected_git_blob: `2b584d4172484216478319025440b16ba7c2859a`
- destination_group: `identity_primary`
- authority: `ONLY FIRST-GLANCE READABLE NAMED IDENTITY`

### REF-02｜Liao Jian

- reference_id: `AST_IMG_000058`
- entity_id: `CHAR_LIAO_JIAN`
- role: `CHARACTER_REFERENCE_SHEET`
- canonical_path: `production/image_library/derived_reference_sheets/liao_jian/CHAR_LIAO_JIAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- expected_sha256: `3f2f01fea63401a3726abdf5053e75361d5d43091830ce8e1636883bd1cd6817`
- expected_byte_size: `650562`
- expected_git_blob: `f8b600e49c0bd40177c723d9c0abd474678f41c2`
- destination_group: `identity_secondary`
- authority: `SECOND-GLANCE / PARTIAL NAMED IDENTITY`

### REF-03｜Castle Entrance Scene Master

- reference_id: `AST_IMG_000052`
- entity_id: `SCENE_CASTLE_ENTRANCE`
- role: `SCENE_MASTER`
- state: `DAY_DOOR_OPEN`
- canonical_path: `production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- expected_sha256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- expected_byte_size: `2305753`
- expected_git_blob: `e4dafe096f5c5c8782257030a5a659aeec7808f9`
- destination_group: `scene_authority`
- authority: `SCENE FACT AUTHORITY`

---

## 3. EXPLICITLY EXCLUDED

Do not include in V003:

- `AST_IMG_000056 / Guang Yong`;
- `AST_IMG_000062 / Wen Qingya`;
- Candidate 01 or Candidate 02 pixels;
- N20 raw Story Shot;
- CHARACTER_VISUAL_STYLE_REFERENCE_V001;
- N21 controlled references;
- Ning Qiushui;
- Jun Luyuan;
- Neil;
- Atomic face / profile / rear anchors for Su or Liao;
- any new external imagery.

Reason:

`MINIMUM-VARIABLE REDUCTION / DIAGNOSTIC CLARITY`

---

## 4. CHARACTER HIERARCHY CONTRACT

Candidate 03 hierarchy is asymmetric by design.

### Su Xiaoxiao

Role:

`ONLY FIRST-GLANCE READABLE NAMED CHARACTER`

Requirements:

- off-center;
- readable but naturally integrated into group flow;
- no isolated hero pose;
- no frontal portrait staging;
- not full-body dominant by default;
- gaze independent from Liao.

### Liao Jian

Role:

`SECOND-GLANCE / PARTIAL NAMED CHARACTER`

Requirements:

- visually smaller than Su;
- one spatial layer behind or laterally offset;
- side / 3/4 / partial face preferred;
- partial overlap by unnamed person or architecture preferred;
- must not share Su's focal plane;
- full frontal face not required;
- must not read as equal co-lead.

Hard hierarchy rule:

`SU READS FIRST / LIAO IS DISCOVERED SECOND`

---

## 5. GAZE DE-SYNCHRONIZATION CONTRACT

New hard rule:

`NO SHARED ATTENTION EVENT`

Su and Liao must not look toward the same off-screen point.

Preferred:

- Su scans one side of the interior or nearby people;
- Liao looks deeper ahead or toward a different local spatial cue.

Unnamed participants should also vary gaze/head/body directions.

N22 is not a collective reaction shot.

---

## 6. COMPOSITION CONTRACT

Target read:

`PASSING OBSERVATIONAL GROUP SLICE`

not:

`SU + LIAO DUO SHOT`

Preferred visual grammar:

`foreground anonymous obstruction → Su readable off-center → unnamed midground interruption → Liao partial/offset → deeper anonymous flow`

Hard rules:

- no clean visual corridor linking Su and Liao as a pair;
- no symmetric spacing;
- no matched stride phase;
- no matched body angle;
- no matched gaze;
- no shoulder-to-shoulder duo;
- no centered two-person composition;
- at least one foreground anonymous occluder;
- at least one unnamed midground interruption between/across Su-Liao grouping.

Reference order remains non-compositional:

`REFERENCE ORDER ≠ SCREEN POSITION ≠ LEFT/RIGHT ORDER ≠ BLOCKING ORDER ≠ PROMINENCE EQUALITY`

---

## 7. LIGHTING / SPACE LOCK

Carry Candidate 02 lighting result forward unchanged.

Target:

`INTERIOR DOMINANT / EXTERIOR TRACE ONLY`

Keep:

- warm dim interior dominant;
- exterior doorway mostly off-frame;
- bright exterior region approximately `≤10–15%`;
- no broad white daylight beam on floor;
- floor dark / warm / low-reflectance;
- wall sconces / candles as practical light;
- natural skin tones;
- no global orange cast;
- architecture subordinate and off-axis.

Important:

No new lighting reference is introduced in V003.

If Candidate 03 lighting regresses despite unchanged written controls, that will be treated as a separate diagnostic branch later.

---

## 8. UNNAMED CROWD ROLE

Unnamed participants are mandatory structural elements.

They should:

- break Su/Liao pairing;
- create foreground occlusion;
- create uneven depth;
- interrupt clean eye-lines;
- vary head/torso orientation;
- suggest a larger group.

They must not:

- become a queue;
- create a symmetric formation;
- clone faces;
- all look the same direction.

---

## 9. CANDIDATE 03 WORK HANDOFF

Generation mode:

`CLEAN REGENERATION`

Candidate 02:

`NEGATIVE ENSEMBLE EVIDENCE / POSITIVE LIGHTING EVIDENCE — NOT PIXEL BASE`

Output limit after later separate authorization:

`EXACTLY 1 PNG`

Required first-glance read:

`SU XIAOXIAO INSIDE A MESSY GROUP FLOW`

Required second-glance discovery:

`LIAO JIAN IS ALSO PRESENT, BUT NOT AS AN EQUAL CO-LEAD`

Do not communicate:

- duo partnership;
- shared discovery;
- synchronized attention;
- formal named-character introduction.

---

## 10. BUILDER PLAN

Use existing:

`.github/workflows/story-shot-reference-bundle-builder.yml`

Builder:

`STORY_SHOT_REFERENCE_BUNDLE_BUILDER_V1`

No N22-specific workflow.

Planned future spec:

`production/bundle_specs/N22_REFERENCE_DELIVERY_BUNDLE_V003.json`

Initial spec state after separate approval:

`build_authorized=false`

First run:

`VALIDATION-ONLY`

Formal build remains separately gated.

---

## 11. PLANNED ARTIFACT STRUCTURE

`N22_REFERENCE_DELIVERY_BUNDLE_V003/`

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- `identity_primary/AST_IMG_000061__CHAR_SU_XIAOXIAO_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `identity_secondary/AST_IMG_000058__CHAR_LIAO_JIAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `scene_authority/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`

Retention:

`7 days`

Manual Product Owner reference upload:

`0`

---

## 12. VALIDATION REQUIREMENT

Validation-only must fail closed unless all 3/3 canonical references pass:

- canonical path;
- declared identity;
- approval status;
- CURRENT lifecycle;
- resolver eligibility;
- exact byte size;
- SHA-256;
- Git blob;
- PNG signature / readability.

Required validation result:

`VALIDATION_PASS: 3/3 exact canonical references verified`

Validation-only must produce:

- `BUILD_AUTHORIZED=FALSE`
- `GENERATION_ALLOWED=FALSE`
- no production Artifact.

---

## 13. MINIMUM PROOF AFTER LATER BUILD

After separate V003 approval, validation pass, formal build and Candidate 03 authorization:

`1 × N22 Candidate 03 PNG`

### PASS

Candidate 03 passes if:

1. Su identity remains stable.
2. Su is the only clearly readable named face at first glance.
3. Liao remains plausibly recognizable on second glance.
4. Liao is smaller / offset / partially interrupted.
5. Su + Liao do not read as a hero pair.
6. Su + Liao do not share gaze direction.
7. unnamed participants visually separate them.
8. frame reads as a passing observational group slice.
9. Candidate 02 lighting gains are preserved.
10. architecture remains subordinate.

### FAIL-A｜Still reads as a duo

Next reduction:

`SU XIAOXIAO ONLY`

Do not add references.

### FAIL-B｜Liao identity disappears completely

Next branch:

`TARGETED LIAO IDENTITY REVIEW`

Do not restore Guang Yong.

### FAIL-C｜Lighting regresses

Next branch:

`TARGETED LOOK-CONTROL REVIEW`

Do not reopen character-reference count.

---

## 14. CURRENT BOUNDARY

Current status:

`PRODUCT OWNER APPROVED / LOCKED`

Authorized next step:

- create `N22_REFERENCE_DELIVERY_BUNDLE_V003.json` with `build_authorized=false`;
- prepare validation-only execution using the existing Generic Story Shot Reference Bundle Builder.

Still not authorized:

- `build_authorized=true`;
- formal Bundle V003 Artifact build;
- Candidate 03 generation;
- N23.

Approval authority:

`PRODUCT OWNER EXPLICIT AUTHORIZATION IN CHAT / 2026-10-02`

Next step:

`N22 BUNDLE V003 SPEC + VALIDATION-ONLY PREPARATION`
