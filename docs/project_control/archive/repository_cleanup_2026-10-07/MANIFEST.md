# Repository Cleanup Archive｜2026-10-07

Status: `VERIFIED / PRODUCT OWNER AUTHORIZED / DRIVE ARCHIVE MIGRATED`

Baseline commit:

`6f6dff4edd943cd4f870c789f25c52602a836ccf`

Purpose: keep GitHub focused on current execution/runtime/governance while preserving retired historical material in Google Drive with exact provenance.

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

## Historical archive migrated to Google Drive

The former GitHub archive subtree:

`docs/project_control/archive/repository_cleanup_2026-10-07/original/`

contained:

- file count: 116
- total original bytes: 5,488,370

This retired material was exported by one-time GitHub Actions Run:

- Run ID: `37602987338`
- Artifact ID: `11473995756`
- Artifact name: `REPOSITORY_CLEANUP_2026-10-07_ORIGINAL_ARCHIVE`
- Artifact ZIP bytes: `5,203,773`
- Artifact SHA-256: `f8295133c62b81f9ee3fbae13f89da4551b9d1bb2b8d8901e33c868a5cbdd0d7`
- Source commit: `8278516b6f5f3cb982309dd3ab478fb35d860c59`

The export contains:

- the complete retired archive subtree;
- `SHA256SUMS.txt` for file-level SHA-256 verification;
- `GIT_BLOBS.txt` for Git blob provenance;
- `EXPORT_RECEIPT.txt`;
- `ARCHIVE_SHA256.txt`;
- `repository_cleanup_2026-10-07_original.zip`.

Google Drive destination:

`Black Lady Project / 99_Archive / GitHub_Repository_Cleanup_2026-10-07`

Drive file:

- file ID: `1RZr321qx4FvGia6MzYbv_kwYr5g-tqwZ`
- name: `REPOSITORY_CLEANUP_2026-10-07_ORIGINAL_ARCHIVE.zip`
- stored bytes: `5,203,773`

Verification result:

`GITHUB ARTIFACT SIZE == DRIVE STORED SIZE`

`LOCAL ARTIFACT SHA-256 == GITHUB ARTIFACT DIGEST`

The retired `original/` subtree is therefore permitted to leave the GitHub active tree. The original Git objects remain recoverable from Git history.

## Previously archived categories

The migrated archive includes retired workflows, historical proof implementations, retired scripts, and historical staging candidates that were previously preserved below:

`docs/project_control/archive/repository_cleanup_2026-10-07/original/<original path>`

## Explicitly not touched

No cleanup change was made to:

- `production/image_library/` canonical or superseded formal assets;
- `production/asset_registry/`;
- `production/story_shots/`;
- `production/video/`;
- `source_material/` canonical story sources;
- current Project Control state;
- active generic Story Shot bundle / intake workflows;
- `staging/d069_a04_intake/A04_REBOOT_approved_v001.png`, because the retained D069 regression test still consumes it;
- CURRENT Scene / Character / Prop assets.

## Repository storage rule after this migration

GitHub retains material that participates in current execution, canonical registration, exact verification, reproducible build logic, tests, or active project governance.

Google Drive is the long-term archive location for retired files that no longer participate in the active execution graph.

This migration does not rewrite Git history.
