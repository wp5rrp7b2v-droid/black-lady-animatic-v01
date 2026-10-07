# Repository Cleanup Archive｜2026-10-07

Status: `CLEANUP BRANCH / PENDING MERGE`

Baseline commit:

`6f6dff4edd943cd4f870c789f25c52602a836ccf`

Purpose: remove files proven to have no current project dependency, and move uncertain or historically valuable material out of active execution paths without discarding its exact Git blobs.

## Deleted from active tree

The following obsolete smoke-test system was removed rather than archived because it was self-contained and its only active consumer was the retired workflow itself:

- `.github/workflows/build-animatic-artifact.yml`
- `scripts/render_animatic_from_payload.sh`
- `artifact_payload/sh01.b64.part01`
- `artifact_payload/sh01.b64.part02`
- `artifact_payload/sh01.b64.part03`
- `artifact_payload/sh01.b64.part04`
- `artifact_payload/sh02.b64.part01`
- `artifact_payload/sh02.b64.part02`
- `artifact_payload/sh02.b64.part03`

Total removed from the current working tree: 5,034,360 bytes.

The deleted objects remain recoverable from Git history.

## Archived, not deleted

The following material had historical / audit / experimental value or residual uncertainty, so it was moved under this archive with exact existing blob identities preserved:

### Retired workflows

- `.github/workflows/manor-gate-scene-reference-delivery-bundle-v001.yml`
- `.github/workflows/p03-n15-reference-delivery-bundle-v001.yml`
- `.github/workflows/p03-libopenshot-camera-motion-proof-v001.yml`
- `.github/workflows/p03-opening-v2-libopenshot-full-proof-v001.yml`
- `.github/workflows/p03-opening-v2-proof-review-v001.yml`
- `.github/workflows/p03-opening-v2-proof-review-v002.yml`
- `.github/workflows/p03-opening-v2-proof-review-v003.yml`
- `.github/workflows/render-sh05-remotion.yml`

### Historical proof implementations

- `openshot-camera-motion-proof-v001/`
- `openshot-opening-v2-full-proof-v001/`
- `remotion-opening-v2-review/`
- `remotion-opening-v2-review-v002/`
- `remotion-opening-v2-review-v003/`
- `remotion-sh05/`

Archive path rule:

`docs/project_control/archive/repository_cleanup_2026-10-07/original/<original path>`

This preserves the original relative path below the archive root so provenance remains explicit.

## Explicitly not touched

No cleanup change was made to:

- `production/image_library/` canonical or superseded formal assets;
- `production/asset_registry/`;
- `production/story_shots/`;
- `production/video/`;
- current Project Control state;
- active generic Story Shot bundle / intake workflows;
- `staging/d069_a04_intake/A04_REBOOT_approved_v001.png`, because the retained D069 regression test still consumes it;
- CURRENT Scene / Character / Prop assets.

## Expected operational effect

The retired workflows are removed from `.github/workflows/`, so they cannot continue creating normal Actions noise from their former triggers.

In the pre-cleanup sample of the latest 100 workflow runs:

- `Build animatic artifact`: 40 runs;
- `MANOR GATE Scene Reference Delivery Bundle V001`: 24 runs, all failed;
- `N15 Reference Delivery Bundle V001`: 23 runs, all failed.

The cleanup therefore removes the three largest known obsolete trigger sources without changing the current Story Shot production chain.
