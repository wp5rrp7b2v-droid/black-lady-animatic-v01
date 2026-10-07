# Workflow Archive Phase 2｜2026-10-07

Status: `PRODUCT OWNER APPROVED / EXECUTED ON CLEANUP BRANCH`

Baseline main commit:

`5036868e1ad9563c38ee53597273885365da7b50`

## Decision

The remaining 58 active workflow files were reviewed by trigger scope and production role.

Retain as active:

- `.github/workflows/story-shot-reference-bundle-builder.yml`
- `.github/workflows/story-shot-candidate-intake-verifier.yml`

Archive, without changing file contents:

- all other 56 workflow files.

## Rationale

The two retained workflows are generic, cross-shot production infrastructure for the current Story Shot chain.

The archived workflows are tied to closed Story Shots, closed audio/video stages, fixed historical reference publication, one-off verification/publication tasks, or historical character/scene/reference preparation.

Several historical Story Shot registration workflows listened to `production/story_shots/story_shot_index.jsonl`, causing old N19-N26 validations to run again whenever later Story Shots were registered. Moving them out of `.github/workflows/` prevents this historical fan-out while preserving their exact Git blobs for audit and reconstruction.

## Archive location

Each archived workflow keeps its original filename under:

`docs/project_control/archive/repository_cleanup_2026-10-07/original/.github/workflows/`

No workflow content is rewritten during archival.

## Safety boundary

This phase does not modify:

- production assets;
- asset registry;
- Story Shot index;
- video index;
- Project Control state;
- bundle specs;
- candidate delivery specs;
- current Story Shot scripts;
- staging binaries;
- tests.

The next cleanup phase may review scripts and trigger files formerly used only by these archived workflows, but no such dependent file is deleted in this phase.
