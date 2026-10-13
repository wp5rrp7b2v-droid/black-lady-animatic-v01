# S02-B｜宁秋水规则反应插镜｜Candidate 01 PO 视觉批准与源文件精确身份

Date: 2026-10-13

**STATUS: PRODUCT OWNER APPROVED (VISUAL CANDIDATE FOR EDITORIAL A/B) / LOCAL UPLOADED SOURCE EXACTLY IDENTIFIED / GITHUB CANDIDATE INTAKE PENDING / NOT A CANONICAL REGISTERED STORY SHOT**

## 1. Decision and scope

Product Owner explicitly said **“批准这张”** and uploaded `image(20261013-124113).png` in the same conversation after requesting Work to create exactly one Ning Qiushui reaction insert and refining the reaction away from a posed standalone portrait.

Accepted narrative: Ning Qiushui hears Neil say “这是夫人的要求”, briefly and subtly fixes his attention toward frame left, still part of the moving group inside the castle inner lobby. Dark warm N26-aligned side-front 3/4 view; identity/wardrobe and supporting figures preserve established family.

- Test identifier: `TAIL_NING_REACTION_TEST_01`
- Candidate identifier: `TAIL_NING_REACTION_TEST_01 Candidate 01`
- Project Owner decision: `APPROVED FOR ONE-SHOT EDITORIAL A/B TEST`
- Is this a new formal N27? **NO**. N27 remains absorbed into approved N26.
- Is this a replacement for approved N26? **NO**. The existing N26 canonical PNG remains unchanged.
- Is this final insertion into approved S02-B V001? **NO**; exact audio splice timing and editorial A/B acceptance remain pending.
- This visual approval is **not** implicit authorization for Story Shot Index registration, canonical publication, or master video replacement.

## 2. Uploaded exact original PNG identity

Source: **user-provided original file** in the current Chat conversation:

`/mnt/data/image(20261013-124113).png` (temporary mounted source path; not a canonical GitHub path).

Independent local verification on the raw uploaded PNG bytes:

- PNG format verification via Pillow: **PASS**
- Dimensions: `941 × 1672`
- Color mode: `RGBA`
- Byte size: `2471479`
- SHA-256: `cbac98a82763c6c930a3c820c917f4b9b8bc2ed300a49b48143b8b1cd9486c9c`
- Calculated Git blob SHA1, using `SHA1("blob " + size + NUL + bytes)`: `907c4cdbd875d67399258dceb29eedd9f8038946`

These values are for **this exact user-uploaded file**. Do not re-save, resize, screenshot, re-encode, or substitute any other draft.

This proves source-file identity and correct dimensions on local intake only; no GitHub-side candidate intake workflow or canonical exact-blob publication has yet run.

## 3. Upstream formal Bundle

- Bundle: `TAIL_NING_REACTION_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001`
- Run: `38333161748`
- Artifact: `11783891178`
- Artifact digest: `sha256:314b5bdac45e8cde34f90c3c195bff5544fedbaec69d45264f07051088dca5c6`
- Reference source exact verification: **3/3 PASS**.
- Original N25/N26 exact-source visual gate: completed and recorded at
  `docs/project_control/gates/P0_3_video_pipeline/s02_b_ning_rule_reaction_n25_n26_exact_png_visual_gate_2026-10-13.md`.

## 4. Next evidence gate — staging intake

The standing SOP `story_shot_production_registration_sop_v1.md` states that Product Owner approval alone is not formal registration; GitHub must receive the **exact original PNG**, then perform exact Git binary and registration verification.

Proposed staging path for optional next intake:

`staging/story_shot_candidates/TAIL_NING_REACTION_TEST_01/TAIL_NING_REACTION_TEST_01_CANDIDATE_01_PO_APPROVED.png`

If the Project Owner uses the local Production Console or GitHub to upload the file, do it byte-identically; Chat must compare uploaded blob SHA to `907c4cdbd875d67399258dceb29eedd9f8038946` and byte-size `2471479`, then validate SHA-256, PNG dimensions and candidate Delivery Spec before any downstream use.

**As of this record, the staging PNG has not been independently observed and GitHub-side intake is not passed. Do not mark staging/publishing/registration PASS on the strength of local hashing.**

After staging exact match, the next narrative gate is: one shortest N25 → new Ning reaction → original N26 **original-audio** local A/B test and PO approval, with no pre-emptive canonical video replacement. Timing of “这是夫人的要求” is still unknown and must be measured.

## 5. Status and restrictions

| Item | Status |
|---|---|
| PO visual candidate approval | **APPROVED** |
| Uploaded PNG local exact identity | **VERIFIED** |
| GitHub staging candidate bytes | **PENDING** |
| Candidate intake Actions | **NOT RUN** |
| Formal Story Shot canonical publication | **NOT AUTHORIZED / NOT DONE** |
| Story Shot Index registration | **NOT DONE** |
| S02-B approved 64.250s V001 video master | **UNCHANGED** |
| N25, N26 approved PNG | **UNCHANGED** |
| N27 absorbed in N26 | **UNCHANGED** |
| P0.3 | **IN PROGRESS** |

Next controlled step: exact original binary staging + intake verification, then short editorial A/B with source-audio continuity, followed by separate PO editing decision. Do not auto-publish the test shot as N27 or replace N26.
