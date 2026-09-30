# N21 Reference Delivery Bundle V002｜Build Record

Date: 2026-09-30

Status: `PASS / GENERATION_ALLOWED=TRUE`

## Bundle identity

- Bundle ID: `N21_REFERENCE_DELIVERY_BUNDLE_V002`
- Target: `N21 Candidate 01`
- Spec: `production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V002.json`
- Spec commit: `26aebca839ec5016762bed92bc9b52a5aa430b99`

## GitHub Actions

- Workflow: `Story Shot Reference Bundle Builder`
- Workflow file: `.github/workflows/story-shot-reference-bundle-builder.yml`
- Run ID: `36699004641`
- Job ID: `109833744730`
- Conclusion: `SUCCESS`

Builder output:

`PASS: 2/2 exact canonical reference binaries verified`

`GENERATION_ALLOWED=TRUE`

## Artifact

- Artifact name: `N21_REFERENCE_DELIVERY_BUNDLE_V002`
- Artifact ID: `11088797193`
- ZIP size: `4306690 bytes`
- Artifact digest: `sha256:e3ec3be6f1a75eae6507801a776bcf2a6e07312d2a26a91909466a73b805f4dc`
- Expires: `2026-10-07T09:53:51Z`

## Formal references

1. `AST_IMG_000052` — Castle Entrance Scene Master
2. `N20` — approved immediate Story Shot continuity

No Su Xiaoxiao / Liao Jian / Wen Qingya / Guang Yong Character Reference Sheets are included.

## Independent Artifact verification

Chat independently downloaded the Artifact ZIP and verified the exact archive and both enclosed PNG binaries.

ZIP:

- downloaded ZIP SHA-256: `e3ec3be6f1a75eae6507801a776bcf2a6e07312d2a26a91909466a73b805f4dc`
- GitHub Artifact digest: `sha256:e3ec3be6f1a75eae6507801a776bcf2a6e07312d2a26a91909466a73b805f4dc`
- result: `MATCH`

Reference verification:

| Reference | Bytes | Dimensions | SHA-256 | Git blob | PNG signature | Result |
|---|---:|---|---|---|---|---|
| AST_IMG_000052 | 2305753 | 941×1672 | d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961 | e4dafe096f5c5c8782257030a5a659aeec7808f9 | PASS | PASS |
| N20 | 2022630 | 941×1672 | a61ab1310e86938b2a416516138981aafaf421add44c1a9d5a80d0ff9ec59a9e | 58e145a51c3f993827e5e47964ad0e7f9dd9f0aa | PASS | PASS |

Independent result:

`2/2 PASS`

Manifest:

- bundle_id: `N21_REFERENCE_DELIVERY_BUNDLE_V002`
- target_shot_id: `N21`
- target_candidate: `N21 Candidate 01`
- reference_count: `2`
- all_reference_checks_pass: `true`
- generation_allowed: `true`
- manual_product_owner_reference_upload: `0`
- overall_result: `PASS`

## Work handoff verification

The Artifact contains:

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- `scene_authority/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- `immediate_story_continuity/N20__N20_DO_NOT_TOUCH_THINGS_APPROVED_V001.png`

The Work handoff explicitly carries the approved N21 controls:

- sixteen-person story truth;
- do not force sixteen equally clear faces / bodies;
- approximately 4–6 comparatively readable figures preferred;
- entrance → interior global movement direction;
- local asynchronous gait / body states;
- natural occlusion / depth / cropping;
- no lineup / publicity-photo staging;
- no clone faces / repeated bodies;
- limited frontal faces / complex hand exposure;
- Ning / Jun secondary continuity figures;
- Neil absent;
- no named-character-seeding task;
- no First Hall reveal;
- N20 color/look continuity.

## Production disposition

`N21_REFERENCE_DELIVERY_BUNDLE_V002 = VERIFIED / READY FOR WORK GENERATION`

N21 Candidate 01 generation may now proceed through Work using this exact Artifact.

Manual Product Owner reference upload:

`0`

Do not use V001 for N21 generation.

Do not start N22.
