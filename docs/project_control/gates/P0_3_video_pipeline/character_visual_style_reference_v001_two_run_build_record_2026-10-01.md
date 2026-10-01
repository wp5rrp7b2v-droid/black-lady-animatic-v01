# Character Visual Style Reference V001｜Deterministic Two-Run Build Record

Date: 2026-10-01

Status:

`TECHNICAL DETERMINISM PASS / DIRECTOR VISUAL PREFLIGHT PASS / PRODUCT OWNER VISUAL REVIEW REQUIRED / NOT CANONICALLY PUBLISHED`

Reference ID:

`CHARACTER_VISUAL_STYLE_REFERENCE_V001`

## 1. Product Owner authorization

Product Owner authorized:

`Deterministic Builder Implementation + Two-Run Proof`

Authorization did not include:

- canonical publication;
- CONTROLLED_REFERENCE delivery integration;
- N21 Bundle V004;
- N21 Candidate 05;
- N22.

## 2. Implementation

Workflow:

`.github/workflows/character-visual-style-reference-v001-determinism.yml`

Workflow creation commit:

`2253465effd32201b3cdd03cd3daa3e4ca043624`

Builder:

`scripts/build_character_visual_style_reference_v001.py`

Builder implementation commit / proof source commit:

`a38a4471f521c3008dc32edb6cf6eaa069bf0f22`

Locked crop plan:

`production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.crop_plan.json`

## 3. Pinned build environment

- Python: `3.12.14`
- Python minor contract: `3.12`
- Pillow: `11.3.0`
- resize: `PIL.Image.Resampling.LANCZOS`
- PNG save: `optimize=False / compress_level=9`
- output: `1536×1024 / RGB / PNG`

No generative processing is used.

## 4. GitHub Actions result

- Workflow Run ID: `36822615026`
- Job ID: `110241244661`
- Conclusion: `SUCCESS`
- Artifact: `CHARACTER_VISUAL_STYLE_REFERENCE_V001_TWO_RUN_PROOF`
- Artifact ID: `11143724172`
- Artifact size: `2603204 bytes`
- Artifact digest: `sha256:91d93bcccceafb5ef47eca5dd6d8f91054e84f87f755785ee2581638f4af55ef`
- Expires: `2026-10-08T06:01:42Z`

## 5. Two-run proof

Build A:

- SHA-256: `8d650483b6e082a80d41d93e14c7957595c451097aac63f3c84cbcc1ddc7ce41`
- bytes: `1301730`

Build B:

- SHA-256: `8d650483b6e082a80d41d93e14c7957595c451097aac63f3c84cbcc1ddc7ce41`
- bytes: `1301730`

Comparison:

- SHA equality: `PASS`
- byte-size equality: `PASS`
- direct byte comparison (`cmp`): `PASS`

Result:

`TWO_RUN_BYTE_IDENTITY=PASS`

## 6. Independent Chat verification

Chat independently downloaded Artifact `11143724172`.

ZIP:

- downloaded SHA-256:
  `91d93bcccceafb5ef47eca5dd6d8f91054e84f87f755785ee2581638f4af55ef`
- GitHub Artifact digest:
  `sha256:91d93bcccceafb5ef47eca5dd6d8f91054e84f87f755785ee2581638f4af55ef`
- result: `MATCH`

Independent PNG verification:

- Run A: `1536×1024 / RGB / PNG / 1301730 bytes / SHA MATCH`
- Run B: `1536×1024 / RGB / PNG / 1301730 bytes / SHA MATCH`
- direct byte identity: `PASS`

## 7. Director visual preflight

Preflight result:

`PASS / READY FOR PRODUCT OWNER VISUAL REVIEW`

Observed board characteristics:

- 4 partial face / hair / skin panels;
- 2 clothing-material / partial upper-torso panels;
- no complete Story Shot;
- no complete person;
- no complete full-body outfit;
- no Ning Qiushui;
- no Jun Luyuan;
- no group staging;
- no story-space composition;
- no image captions / names / IDs;
- landscape contact-sheet form remains visually distinct from 9:16 Story Shots.

This Director preflight does not substitute for Product Owner visual approval.

## 8. Current disposition

`CHARACTER_VISUAL_STYLE_REFERENCE_V001 = TECHNICALLY DETERMINISTIC / PRODUCT OWNER VISUAL REVIEW REQUIRED`

Not authorized:

- canonical publication;
- formal P0.3 controlled-reference publication;
- Bundle Builder `CONTROLLED_REFERENCE` integration;
- N21 Bundle V004;
- Candidate 05;
- N22.

RISK-003 remains ACTIVE.

Next:

`PRODUCT OWNER VISUAL REVIEW OF STYLE BOARD`
