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

## Approved video canonical storage migration

The two approved video masters were moved out of the GitHub active tree after exact-binary verification and are now stored in Google Drive under:

`Black Lady Project / 07_Video`

Migration verification:

- one-time export run: `37604481036`
- Artifact ID: `11474341592`
- Artifact digest: `sha256:36c0e388ae2b6c6d99fedb3cb3cf2f666f393e3419f4ff98b9178c89e87933b1`
- source verification: byte size + SHA-256 PASS before export
- Drive verification: each uploaded MP4 was downloaded back from Drive and SHA-256 rechecked exactly
- final migration commit: `097cc7603b18ede8d7cf92053cb100971555012b`
- temporary export workflow removed after migration

Canonical storage records:

1. `P03_OPENING_V2_APPROVED_V001.mp4`
   - Drive file ID: `1WZe51k7yQF6rdmcFxVAbeYVuoEjYNVd_`
   - bytes: `18,892,138`
   - SHA-256: `70d7922244161dd216a26446fd75531db20eea0ac7fc25f567f6ff14e2746e3a`
   - former Git blob: `9b4ef42d9eceb5d7f1eb190d508d6749ccf4b70e`

2. `S02_A_ASSEMBLY_APPROVED_V001.mp4`
   - Drive file ID: `1S_4ozuVSTuKqFjZfFRsncFcEWxJXVhMB`
   - bytes: `6,822,004`
   - SHA-256: `937008e11d20892ea0a17be64719a19cb131d174871930bc29004a678bb58ed1`
   - former Git blob: `bcd3fef7a8d600c95cb4d7242d411cc0df41859c`

`production/video/video_index.jsonl` remains in GitHub as the authoritative control/provenance record and now points to Google Drive canonical storage. Git history was not rewritten.

## Local workspace cleanup and historical archival

The local cleanup was performed conservatively: rebuildable dependencies/caches were deleted first; unique historical project material was archived to Google Drive before local deletion.

### Legacy workspace

Original local legacy directory:

`black_lady_short_01_legacy_20260912`

Observed before cleanup:

- total: approximately `3.5G`
- engineering: approximately `3.0G`
- production: approximately `459M`

Rebuildable legacy dependencies were removed locally, including old Python virtual environments, Node modules, embedded Node runtime, Remotion runtime/cache and retired AdvancedLivePortrait experiment dependencies/models. The legacy directory was reduced to approximately `477M`.

The remaining historical content was archived as:

`BLACK_LADY_LEGACY_20260912_ARCHIVE_20261007.tar.gz`

Google Drive destination:

`Black Lady Project / 99_Archive`

Drive archive:

- file ID: `1uXEgSEvWy9_YxU8X7oTKeyWtdV-TYwgX`
- bytes: `478,080,466`
- SHA-256: `46948e4c730a329edad8a94f8b1d908ebfc8136723d65d7d4366f7bd94f63534`

File-level manifest:

- name: `BLACK_LADY_LEGACY_20260912_SHA256_20261007.txt`
- Drive file ID: `1XHb-ZGaiXPBML1ZMDTQACFJXx9MF8vK2`
- bytes: `71,955`

Verification:

- local tar content test: PASS
- Drive archive materialized back as original bytes: PASS
- Drive SHA-256 == local pre-upload SHA-256: PASS

After verification, the local legacy directory and temporary local archive copy were permitted to be deleted.

### Historical Production Console UI archive

The former local `../../UI` folder contained five V1.0 Fixed Install history files. They were archived 5/5 to:

`Black Lady Project / 99_Archive / Production_Console_History / 2026-10-03_V1.0_FixedInstall`

Drive folder ID:

`1D5yEkNBWBKNNqVANnAG8ERrpLKtE4g9v`

The folder contains exactly the two V1.0 ZIP snapshots, one JSON record snapshot and two DOCX development/source-archive records. After Drive presence verification, the local UI history folder was permitted to be deleted.


## Previously archived categories

The migrated archive includes retired workflows, historical proof implementations, retired scripts, and historical staging candidates that were previously preserved below:

`docs/project_control/archive/repository_cleanup_2026-10-07/original/<original path>`

## Explicitly not touched

No cleanup change was made to:

- `production/image_library/` canonical or superseded formal assets;
- `production/asset_registry/`;
- `production/story_shots/`;
- `production/video/video_index.jsonl` control/provenance record (approved MP4 binaries were migrated to Google Drive as documented above);
- `source_material/` canonical story sources;
- current Project Control state;
- active generic Story Shot bundle / intake workflows;
- `staging/d069_a04_intake/A04_REBOOT_approved_v001.png`, because the retained D069 regression test still consumes it;
- CURRENT Scene / Character / Prop assets.

## Repository storage rule after this migration

GitHub retains material that participates in current execution, canonical registration, exact verification, reproducible build logic, tests, or active project governance.

Google Drive is the long-term archive location for retired files that no longer participate in the active execution graph.

This migration does not rewrite Git history.
