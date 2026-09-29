# STORY_SHOT_CANDIDATE_DELIVERY_BRIDGE_V1

Status: `PRODUCT OWNER APPROVED / IMPLEMENTATION ACTIVE / N16 FIRST REAL VALIDATION`

Date: 2026-09-29

## 1. Objective

Remove routine Product Owner manual upload of approved Story Shot PNGs to GitHub.

New candidate-delivery path:

`Work generation → Work exact original PNG delivery to GitHub staging → Generic Candidate Intake Verification → Product Owner decision → Approval Spec → Exact Canonical Promotion → Story Shot Registration → Registration Verification`

Product Owner manual GitHub PNG upload target:

`0`

## 2. Boundary

This bridge transports and verifies the exact generated candidate binary.

It does not:
- choose the creative winner;
- regenerate or edit the image;
- re-encode / resize / screenshot the PNG;
- canonically publish an unapproved candidate;
- register a Story Shot before approval.

## 3. Canonical staging path rule

`staging/story_shot_candidates/<SHOT_ID>/<CANDIDATE_FILENAME>.png`

Example:

`staging/story_shot_candidates/N16/N16_Candidate_01_APPROVED.png`

Staging files are not canonical Story Shots.

## 4. Candidate Delivery Spec

Per candidate:

`production/candidate_delivery_specs/<SHOT_ID>_<CANDIDATE>_DELIVERY_V001.json`

Spec locks:
- shot_id
- sequence_id
- candidate_id
- source Bundle identity
- target staging path
- expected dimensions
- expected byte size
- expected SHA-256
- expected Git blob
- approval state
- downstream canonical target after approval

## 5. Generic intake verifier

Fixed implementation:
- script: `scripts/story_shot_candidate_intake_verifier_v1.py`
- workflow: `.github/workflows/story-shot-candidate-intake-verifier.yml`

On a staging PNG push, verifier must:
1. locate exactly one matching Candidate Delivery Spec;
2. verify PNG signature;
3. verify dimensions;
4. verify exact byte size;
5. verify SHA-256;
6. verify Git blob;
7. verify target path;
8. emit an immutable verification evidence artifact.

Only exact match:

`CANDIDATE_INTAKE_VERIFIED=TRUE`

Mismatch:

`CANDIDATE_INTAKE_VERIFIED=FALSE`

and downstream publication must fail closed.

## 6. N16 first real validation

Source:
`N16 Candidate 01`

Product Owner decision:
`APPROVED`

Expected exact binary identity:
- dimensions: `941x1672`
- byte size: `1942422`
- SHA-256: `b26fb7d64a60fbd28d39b0ae22f7c85df18d4f947f31a3591c847dd5e1acf406`
- Git blob: `44971dd53e37cd1b582bcf5094b0f09cb8e0647d`

Target staging path:
`staging/story_shot_candidates/N16/N16_Candidate_01_APPROVED.png`

N16 is the first real bridge validation. No substitute binary is permitted.

## 7. Operational rule after validation

For future Story Shots:
- Work delivers the original generated candidate to staging before or at Product Owner review;
- Product Owner only reviews and says approve/reject;
- no routine manual GitHub PNG upload is required;
- canonical promotion reuses the exact verified staging blob.
