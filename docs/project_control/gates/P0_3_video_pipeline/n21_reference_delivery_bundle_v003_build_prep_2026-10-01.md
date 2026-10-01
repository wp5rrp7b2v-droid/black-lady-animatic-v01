# N21 Reference Delivery Bundle V003｜Build Preparation

Date: 2026-10-01

Status: `SPEC CREATED / AUTO BUILD EXPECTED FROM MAIN PUSH / CANDIDATE 04 NOT YET AUTHORIZED`

## Authority

- Scene Reference: `N21 Scene Reference Design V0.4 / PO APPROVED + LOCKED`
- Bundle Design: `N21 Reference Delivery Bundle Design V0.3 / PO APPROVED + LOCKED`

## Spec

`production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V003.json`

Formal reference count:

`2`

1. `AST_IMG_000052` — space / architecture authority
2. `N03` — character visual-style / multi-person rendering-language authority

## Expected builder

`.github/workflows/story-shot-reference-bundle-builder.yml`

The generic builder is configured to auto-run on a main-branch push that changes `production/bundle_specs/*.json`.

Required result before Work:

- workflow conclusion = SUCCESS;
- `PASS: 2/2 exact canonical reference binaries verified`;
- `GENERATION_ALLOWED=TRUE`;
- artifact name = `N21_REFERENCE_DELIVERY_BUNDLE_V003`;
- independent artifact ZIP digest verification;
- independent 2/2 enclosed PNG verification.

## Current boundary

Do not send Work generation instructions until real Run / Job / Artifact / digest values have been read back and independently checked.

Candidate 04 remains:

`NOT AUTHORIZED FOR GENERATION YET`
