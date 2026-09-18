# AO-05｜Multi-reference Robustness Proof Failure｜2026-09-18

Status: `CANONICAL_BINARY_MATERIALIZATION_FAILED / FAIL CLOSED / FALLBACK REQUIRED`

Source branch: `main`

Source commit: `c2854ffce17351f97e8b44feaec534ffc78ad6c6`

Environment: `ChatGPT Work`

## RUN A

Expected formal input set:

- `AST_IMG_000056 / CHARACTER_REFERENCE_SHEET`
- `AST_IMG_000011 / FACE_FRONT`
- `AST_IMG_000009 / BODY_FRONT`
- `AST_IMG_000008 / BODY_BACK`

Observed:

- Registry identity / filename / path / state matched for 4/4.
- Formal Registry state was CURRENT / APPROVED for 4/4.
- Three large Atomic PNG binaries could not be materialized through the available Work GitHub file/blob/raw interfaces.
- No complete four-file byte set was available for independent SHA256 verification.
- Image-generation environment was not invoked.
- `loaded_reference_count=0`.
- `proof_generated=NO`.
- `manual_product_owner_reference_upload_count=0`.

Result: `CANONICAL_BINARY_MATERIALIZATION_FAILED`.

## RUN B

`NOT_STARTED` because RUN A failed closed before generation.

Repeatability: `NOT_TESTED`.

## Interpretation

This is a transport/materialization failure, not evidence that the image-generation environment cannot accept multiple references.

The Product Owner was not asked to manually upload references, so the no-manual-upload rule remained intact.

## Required fallback

Proceed to the already-approved design fallback:

`GitHub Actions → manifest-verified short-lived Delivery Bundle artifact → Work`

The fallback must package the exact formal binaries with Asset ID / path / SHA / byte-size manifest, then Work must independently materialize the bundle and complete multi-reference + repeatability validation.
