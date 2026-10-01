# N21 Reference Delivery Bundle V003｜Build Record

Date: 2026-10-01

Status: `PASS / GENERATION_ALLOWED=TRUE / READY FOR WORK GENERATION`

## Bundle identity

- Bundle ID: `N21_REFERENCE_DELIVERY_BUNDLE_V003`
- Target: `N21 Candidate 04`
- Spec: `production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V003.json`
- Spec commit: `6a03dc80fb7cf75ca5908d5ed364fed45fd988a8`

## GitHub Actions

- Workflow: `Story Shot Reference Bundle Builder`
- Workflow file: `.github/workflows/story-shot-reference-bundle-builder.yml`
- Run ID: `36817339701`
- Job ID: `110225166295`
- Conclusion: `SUCCESS`

Builder output:

`PASS: 2/2 exact canonical reference binaries verified`

`GENERATION_ALLOWED=TRUE`

## Artifact

- Artifact name: `N21_REFERENCE_DELIVERY_BUNDLE_V003`
- Artifact ID: `11141917821`
- ZIP size: `4606668 bytes`
- Artifact digest: `sha256:8be16a3538394046d1a875ff6a5e4802dd097bd52c44e8efd863af8807d9eaa0`
- Expires: `2026-10-08T04:55:22Z`

## Formal references

1. `AST_IMG_000052` — Castle Entrance Scene Master / space authority
2. `N03` — approved Story Shot / character visual-style authority

## Independent verification

Chat independently downloaded the Artifact ZIP.

ZIP:

- downloaded bytes: `4606668`
- downloaded SHA-256: `8be16a3538394046d1a875ff6a5e4802dd097bd52c44e8efd863af8807d9eaa0`
- GitHub Artifact digest: `sha256:8be16a3538394046d1a875ff6a5e4802dd097bd52c44e8efd863af8807d9eaa0`
- result: `MATCH`

Reference verification:

| Reference | Bytes | Dimensions | SHA-256 | PNG Signature | Result |
|---|---:|---|---|---|---|
| AST_IMG_000052 | 2305753 | 941×1672 | d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961 | PASS | PASS |
| N03 | 2321221 | 941×1672 | 0e5022a59d7e33e30e0fdea74c966ff8e84a3084ca869fcbc4d76052e8ec6c22 | PASS | PASS |

Independent result:

`2/2 PASS`

Manifest:

- reference_count: `2`
- all_reference_checks_pass: `true`
- generation_allowed: `true`
- manual_product_owner_reference_upload: `0`
- overall_result: `PASS`

## Work handoff boundary

- `AST_IMG_000052` controls only space / architecture / open-door threshold facts.
- `N03` controls only character visual style and multi-person rendering language.
- N03 does not control Ning / Jun identity, exact people, composition, pose, eyeline or exterior scene state.
- N20 is Director continuity review only and is not delivered as a formal generation input.
- Candidate 01–03 are negative lessons only and are not generation inputs or edit bases.
- Candidate 04 must be Clean Regeneration.

## Production disposition

`N21_REFERENCE_DELIVERY_BUNDLE_V003 = VERIFIED / READY FOR WORK GENERATION`

Candidate 04 may proceed through Work using this exact Artifact.

RISK-003 remains ACTIVE until a real candidate demonstrates acceptable balance and receives Product Owner approval.

Do not start N22.
