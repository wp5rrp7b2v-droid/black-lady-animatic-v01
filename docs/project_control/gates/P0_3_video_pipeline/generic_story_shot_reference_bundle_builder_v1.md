# Generic Story Shot Reference Bundle Builder V1

Status: `PRODUCT OWNER APPROVED FOR IMPLEMENTATION`

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
