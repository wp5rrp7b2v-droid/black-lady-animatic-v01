# Generic Story Shot Reference Bundle Builder V1

Status: `IMPLEMENTED / VERIFIED / N16 FIRST PRODUCTION PASS`

Date: 2026-09-29

## Objective

Replace per-shot GitHub Actions workflow creation with one reusable builder.

Permanent route:

`Chat Bundle Design → bundle spec JSON → fixed GitHub Action → verified Artifact → Work → Product Owner → Chat closeout`

## Canonical paths

- Workflow: `.github/workflows/story-shot-reference-bundle-builder.yml`
- Builder: `scripts/story_shot_reference_bundle_builder_v1.py`
- Specs: `production/bundle_specs/*.json`

## Trigger

The fixed workflow runs on:

- `workflow_dispatch`
- push changes under `production/bundle_specs/*.json`

The workflow must determine the changed / selected spec and call the fixed builder.

## Bundle Spec contract

Each spec must contain:

- schema_version
- bundle_id
- target_shot_id
- sequence_id
- target_candidate
- retention_days
- manual_product_owner_reference_upload
- references[]
- work_handoff

Each reference must contain:

- reference_id
- source_type: ASSET or STORY_SHOT
- canonical_path
- destination_group
- authority_purpose
- expected approval/lifecycle/resolver where applicable
- expected SHA-256 when locked
- expected byte_size
- expected Git blob

## Generation Interface Compatibility

For Story Shot Bundles that will be passed directly to the Work image-generation interface:

- maximum direct referenced images: `5`
- Bundle Design must satisfy `references.length <= 5` before Formal Build authorization when all references are intended as direct image inputs
- do not wait until Work generation to discover this limit
- if more than five evidentiary images exist, Chat must reduce them during Bundle Design by removing redundant direct-image evidence or by keeping lower-priority material as non-delivered Project Control evidence
- Work must never silently omit, merge, substitute, or choose among an over-limit reference set
- a Bundle with more than five direct generation images is not executable as-is even if all binaries exact-verify successfully

This rule was locked after N24 Candidate 01 Attempt 01 on 2026-10-06, when the generation interface rejected six `referenced_image_paths` before image creation.

## Validation contract

Builder must fail closed unless every reference passes:

1. unique registry / Story Shot lookup
2. identity / role / authority check where applicable
3. approval status
4. lifecycle
5. resolver usage where applicable
6. canonical path
7. regular-file / no-symlink
8. exact byte size
9. exact SHA-256 where locked
10. exact Git blob
11. valid PNG signature
12. readable dimensions
13. byte-identical artifact copy
14. final artifact revalidation

Only when all references pass:

`generation_allowed = true`

Otherwise:

`generation_allowed = false`

and Artifact must not be used for Work generation.

## Artifact contents

`<bundle_id>/`

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- reference binaries grouped by destination_group

Artifact retention defaults to 7 days.

## Governance

- Product Owner manual reference upload = 0 by default.
- The builder does not choose creative references; Chat / locked Bundle Design does.
- The builder only validates and transports canonical binaries.
- No image generation occurs inside the builder.
- No Story Shot registration occurs inside the builder.
- Existing N11–N15 workflows remain historical evidence; new shots should use this generic builder.
- Global Story Shot ID and sequence ownership remain separate: e.g. `shot_id=N16`, `sequence_id=S02-B`.


## Implementation verification

Implementation completed on 2026-09-29.

- workflow: `.github/workflows/story-shot-reference-bundle-builder.yml`
- builder: `scripts/story_shot_reference_bundle_builder_v1.py`
- first production spec: `production/bundle_specs/N16_REFERENCE_DELIVERY_BUNDLE_V001.json`
- verification run: `36514238747`
- first production artifact: `N16_REFERENCE_DELIVERY_BUNDLE_V001`
- artifact ID: `11010505345`
- artifact digest: `sha256:e44c4fc8e9b8d1499af8866ac601137dd315ac1f386a544eec19b709ac5cd0ff`
- exact reference result: `6/6 PASS`
- post-artifact independent verification: `PASS`
- manual Product Owner reference upload: `0`

Operational rule from N17 onward:

`Create / update Bundle Spec JSON only; do not create a new per-shot workflow unless the Generic Builder itself requires controlled revision.`
