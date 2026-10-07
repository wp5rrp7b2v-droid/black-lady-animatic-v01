# Repository Cleanup Phase 3｜2026-10-07

Status: `EXECUTED UNDER PRODUCT OWNER CLEANUP AUTHORIZATION`

Baseline main commit:

`b5c394f8ed400f08b997ccafc5275fe4f7a6790c`

## Scope

Review and clean the remaining active `scripts/`, legacy trigger files, and `staging/` leftovers after workflow archival.

## Archived scripts

The following scripts are tied to already-closed, archived workflows or one-off formalization tasks. Their exact Git blobs are preserved under the repository cleanup archive:

- `scripts/archive_s02_b_n17_n18_v001.py`
- `scripts/build_character_visual_style_reference_v001.py`
- `scripts/build_n15_reference_delivery_bundle_v001.py`
- `scripts/build_n21_castle_entrance_door_identity_reference_v001.py`
- `scripts/build_n23_castle_entrance_door_control_reference_v001.py`
- `scripts/build_s02_a_assembly_input_bundle_v001.py`
- `scripts/build_s02_a_audio_boundary_patch_v001.py`

## Archived trigger

- `.github/p03_opening_v2_audio_alignment_trigger.txt`

Its only corresponding workflow has already been archived, so the trigger no longer has an active consumer.

## Archived historical staging candidates

- `staging/p0_3_a01_a02_transition_validation/BRIDGE_A01_A02_TIGHT_CANDIDATE.png`
- `staging/p0_3_a01_a02_transition_validation/BRIDGE_A01_A02_WIDE_CANDIDATE.png`

These were historical transition candidates, not canonical assets and not inputs to the current generic Story Shot production workflows.

## Retained active scripts

The following scripts remain active because they are consumed by the current generic Story Shot chain, retained regression tests, the local ingest launcher, or current asset/resolver infrastructure:

- `scripts/automatic_ingest_controller_v0_1.py`
- `scripts/character_reference_sheet_builder_v0_1.py`
- `scripts/character_reference_sheet_formalizer_v0_1.py`
- `scripts/legacy_registry_migration_controller_v1.py`
- `scripts/reference_package_exporter_v0_1.py`
- `scripts/resolver_asset_source_v0_1.py`
- `scripts/shot_reference_package_exporter_v0_1.py`
- `scripts/shot_reference_resolver_v0_1.py`
- `scripts/shot_use_audit_v0_1.py`
- `scripts/story_shot_candidate_intake_verifier_v1.py`
- `scripts/story_shot_reference_bundle_builder_v1.py`

## Retained staging

### Canonical audio retained

`staging/p0_3_a01_a02_transition_validation/AUDIO_MVP1_CANONICAL_V001.m4a`

Reason: P0.3 remains active and the locked S02-A Assembly Execution Contract explicitly names `AUDIO_MVP1_CANONICAL_V001` as the canonical audio / timing authority. It remains potentially required by future assembly work and must not be treated as disposable staging.

### A04 regression fixture retained

`staging/d069_a04_intake/A04_REBOOT_approved_v001.png`

Reason: `tests/test_d069_a04_shot_pipeline.py` consumes this exact evidence binary.

### Story Shot directory placeholders retained

The N21/N23/N24/N25 `.gitkeep` files remain unchanged. They cost no meaningful storage and avoid introducing unnecessary assumptions into staging-path behavior.

## Archive path rule

All archived files preserve their original relative path below:

`docs/project_control/archive/repository_cleanup_2026-10-07/original/`

## Safety boundary

No production asset, canonical video, Story Shot index, Asset Registry, Project Control state, active generic workflow, active Story Shot script, canonical audio binary, or regression fixture is modified in this phase.
