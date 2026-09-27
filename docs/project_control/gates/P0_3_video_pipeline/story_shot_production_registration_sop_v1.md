# Story Shot Production & Registration SOP V1

Status: **ACTIVE / PROJECT STANDARD**

Effective date: 2026-09-27

Rule change: **RC-024**

Scope: all new formal `STORY_SHOT` image production and registration in 《诡舍·黑衣夫人》.

## 1. Standard flow

`Director Design → Reference Delivery Bundle → Work Generation → Product Owner Approval → Original PNG Upload → Binary Verification → Exact-Blob Canonical Rename → Story Shot Index Registration → Registration Verification → Project Control Closeout`

## 2. Step rules

### Step 1｜Director Design
Chat defines and locks:
- narrative function / story beat;
- shot size, camera angle, composition;
- character pose, gaze, expression and action;
- scene relationship and continuity with adjacent shots;
- prohibited states / duplication boundaries.

No image generation starts before the shot function and visual boundary are clear.

### Step 2｜Reference Delivery Bundle
Formal references must come from canonical GitHub assets selected through Registry / Resolver.

Baseline:
`GitHub canonical assets → Resolver / Registry → Reference Delivery Bundle`

Bundle must record at minimum:
- canonical path;
- reference role / authority;
- source commit;
- SHA-256;
- byte size.

Normal manual Product Owner reference upload = **0**.

### Step 3｜Work Generation
Work must:
1. obtain the formal Bundle;
2. materialize the actual PNG references;
3. revalidate manifest / SHA / byte size as required;
4. generate only the requested Candidate.

No missing-reference generation. Delivery failure = **FAIL CLOSED**.

### Step 4｜Director + Product Owner Review
Chat performs director review; Product Owner makes the final approval decision.

Only an explicit Product Owner approval may promote a Candidate to formal Story Shot.

`CANDIDATE / REJECTED / WIP`:
- do not enter the formal library;
- do not enter Story Shot Index;
- do not become canonical production references.

### Step 5｜Original PNG Upload
After approval, Product Owner uploads the exact final source PNG to:

`production/image_library/approved/story_shots/`

Requirements:
- original PNG only;
- no screenshot;
- no re-save / re-encode;
- no manual quality conversion.

Temporary UUID filename is allowed at upload stage.

### Step 6｜Binary Verification
Before canonical rename, GitHub-side verification must check:
- valid PNG;
- expected dimensions;
- byte size;
- SHA-256;
- Git blob SHA.

The verification result must be retained as run / artifact / log evidence.

### Step 7｜Canonical Rename by Exact Git Blob Reuse
Formal naming follows the approved Story Shot naming rule.

Example:
`<UUID>.png → N07_NEIL_SPEAKING_STATE_C_APPROVED_V001.png`

Rename must reuse the exact uploaded Git blob.

Mandatory condition:
`rename_preserved_exact_git_blob = true`

No PNG re-encode is permitted during canonicalization.

### Step 8｜Story Shot Index Registration
Register the approved shot in:

`production/story_shots/story_shot_index.jsonl`

Required identity / governance fields include:
- `shot_id`;
- `asset_class = STORY_SHOT`;
- `approval_status = APPROVED`;
- `lifecycle = CURRENT`;
- canonical path / filename;
- dimensions;
- byte size;
- Git blob SHA;
- locked SHA-256 identity;
- binary verification evidence;
- story beat;
- characters;
- scene;
- continuity tags;
- approved date;
- provenance.

### Step 9｜Registration Verification
After registration, independently verify:

`Canonical PNG ↔ Story Shot Index`

Must confirm:
- file exists and is valid;
- SHA-256 matches;
- byte size matches;
- dimensions match;
- Git blob matches;
- canonical path matches;
- approval / lifecycle fields match;
- exact-blob rename flag is true.

Any mismatch = **FAIL CLOSED** and registration is not complete.

### Step 10｜Project Control Closeout
After successful registration verification:
- update Decision Log when a formal creative / governance decision was made;
- update Execution Log;
- update Project State;
- update current Gate README / progress when affected;
- refresh Dashboard when current state / next action changes;
- remove temporary Bundle / upload-verification / registration-verification workflows after evidence is captured.

## 3. Hard gates

A Story Shot is formally complete only when all four gates are satisfied:

1. **PO APPROVED**
2. **CANONICAL BINARY PUBLISHED**
3. **STORY SHOT INDEX REGISTERED**
4. **REGISTRATION VERIFICATION PASS**

Image approval alone is not formal registration.

GitHub upload alone is not formal registration.

Index entry without binary verification is not formal registration.

## 4. Role split

- **Chat**: director design, shot boundary, review, governance design, registration orchestration, Project Control closeout.
- **GitHub / Actions**: canonical storage, Resolver / Registry evidence, Bundle delivery, binary verification, immutable Git identity.
- **Work**: consume verified Bundle and generate Candidate images.
- **Product Owner**: final visual approval and upload of the approved original PNG when formal registration requires source publication.
- **Codex**: not part of the normal Story Shot image production / registration baseline; use only when a genuine local engineering task requires it.

## 5. Governing principles

1. **Only Product Owner-approved images enter the formal Story Shot system.**
2. **Formal registration preserves the exact approved PNG binary.**
3. **Work receives references through canonical GitHub / Resolver / Bundle delivery, not ad-hoc manual reference selection.**
4. **All identity-critical steps are evidence-based and fail closed on mismatch.**
5. **Project Control must be closed out after each formal registration so the next session can resume from GitHub main without Chat-history dependence.**

## 6. Relationship to existing rules

This SOP operationalizes and combines:
- RC-021｜Story Shot admission / unified asset model;
- RC-022｜canonical GitHub → Resolver / Registry → Bundle → Work delivery;
- RC-023｜GitHub Actions artifact delivery and no routine manual reference upload;
- RC-014｜mandatory Project Control cross-file closeout;
- RC-012｜local sync reminder after canonical GitHub writes.

If a later rule changes this SOP, retain this file as historical evidence and record the replacement in Rules Change Log.
