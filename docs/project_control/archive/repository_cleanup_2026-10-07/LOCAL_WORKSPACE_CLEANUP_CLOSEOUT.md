# Local Workspace Cleanup Closeout｜2026-10-07

Status: `COMPLETE / HISTORICAL MATERIAL ARCHIVED BEFORE DELETE / ACTIVE LOCAL CONSOLE PRESERVED`

## 1. Scope

This closeout records local-storage cleanup only. It does not change Story Shot approval state, formal GitHub assets, or Git history.

## 2. Initial local observation

Current repository root:

`/Users/caroline/诡舍/黑衣夫人/black_lady_short_01`

Initial observed size:

- current repository working directory: approximately `2.1G`
- parent `黑衣夫人` directory: approximately `5.7G`
- legacy workspace `black_lady_short_01_legacy_20260912`: approximately `3.5G`

The largest legacy usage was rebuildable engineering/runtime material, not current canonical project assets.

## 3. Duplicate intake cleanup

`PNG_INTAKE_2026-09-21`:

- files: 21
- exact SHA-256 matches in current repository: 21
- unique: 0
- disposition: SAFE TO DELETE

`PNG_INTAKE_HOLD_2026-09-21`:

- files: 3
- exact duplicates: 0
- all three were visually reviewed as old HOLD reference experiments, UUID-named, unregistered, unreferenced by current GitHub and absent from Drive canonical storage
- disposition: SAFE TO DELETE as non-adopted historical HOLD material

## 4. Legacy engineering cleanup

The 3.5G legacy workspace contained large rebuildable environments and retired experiment dependencies including Python virtual environments, Node modules, embedded Node runtime, Remotion runtime/cache and AdvancedLivePortrait experiment dependencies/models.

After dependency cleanup:

- legacy workspace: approximately `1.1G`
- legacy engineering after second cleanup: approximately `4.4M`
- total remaining legacy workspace: approximately `477M`

## 5. Unique legacy production boundary

Exact SHA-256 comparison of legacy `production/` against the current repository found:

- files: 198
- exact matches: 11
- unique: 187
- matched bytes: 24,432,618
- unique bytes: 456,066,028

Therefore the remaining legacy production content was **not** deleted as duplicate material. It was archived first.

## 6. Legacy archive verification

Archive:

`BLACK_LADY_LEGACY_20260912_ARCHIVE_20261007.tar.gz`

Local pre-upload verification:

- tar content test: PASS
- SHA-256: `46948e4c730a329edad8a94f8b1d908ebfc8136723d65d7d4366f7bd94f63534`

Google Drive:

- location: `Black Lady Project / 99_Archive`
- file ID: `1uXEgSEvWy9_YxU8X7oTKeyWtdV-TYwgX`
- bytes: `478,080,466`

Drive original bytes were materialized back and independently SHA-256 checked:

`46948e4c730a329edad8a94f8b1d908ebfc8136723d65d7d4366f7bd94f63534`

Result:

`DRIVE EXACT BINARY VERIFICATION = PASS`

External file-level SHA manifest:

- `BLACK_LADY_LEGACY_20260912_SHA256_20261007.txt`
- Drive file ID: `1XHb-ZGaiXPBML1ZMDTQACFJXx9MF8vK2`
- bytes: `71,955`

Only after this verification was local legacy deletion permitted.

## 7. Historical UI archive

Former local folder:

`/Users/caroline/诡舍/UI`

Contained five Production Console V1.0 Fixed Install history files. All 5/5 are archived under:

`Black Lady Project / 99_Archive / Production_Console_History / 2026-10-03_V1.0_FixedInstall`

Folder ID:

`1D5yEkNBWBKNNqVANnAG8ERrpLKtE4g9v`

After Drive presence verification, local deletion was permitted.

## 8. Preserved active/local-only boundaries

Do not treat the cleanup as permission to delete:

- `BlackLadyLocalConsole/` — active local Production Console runtime
- `BlackLadyLocalConsolePrivate/` — private/local-only Console data
- current canonical GitHub-controlled Story Shot / Character / Scene / Prop assets
- canonical `source_material/`
- local ignored source audio or current working assets unless separately reviewed

## 9. Local Git state at closeout inspection

Observed before EOD closeout:

- branch: `feature/production-console-v1-1`
- local HEAD: `ea0e3a0`
- origin/main: `097cc7603b18ede8d7cf92053cb100971555012b`
- visible untracked: `BlackLadyLocalConsole/`, `BlackLadyLocalConsolePrivate/`

Therefore local storage cleanup is complete, but **local main synchronization is not established by this closeout**.

Next formal local session must begin with branch/status inspection and fast-forward local main verification.
