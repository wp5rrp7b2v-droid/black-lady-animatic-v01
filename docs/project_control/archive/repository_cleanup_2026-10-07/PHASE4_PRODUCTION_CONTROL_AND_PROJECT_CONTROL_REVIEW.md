# Repository Cleanup Phase 4｜2026-10-07

Status: `EXECUTED UNDER PRODUCT OWNER CLEANUP AUTHORIZATION`

Baseline main commit:

`4bf5bdeca88f8c0c7d586f9a32b45e13a0c8ef18`

## Production control review

Reviewed:

- `production/bundle_specs/`
- `production/candidate_delivery_specs/`
- `production/publication_requests/`
- `source_material/`
- remaining `production/` top-level structures
- `docs/project_control/`

### Retained production control JSON

No Bundle Spec, Candidate Delivery Spec, or Publication Request was moved in this phase.

Reason:

- `docs/project_control/core/project_state.json` contains direct original-path references to multiple Bundle Specs and Candidate Delivery Specs;
- CURRENT controlled-reference manifests preserve Publication Request paths as provenance;
- moving those files would create broken audit/provenance paths even though their production action is complete.

The files are therefore production evidence, not disposable working files.

### Production image library verification

- 151 tracked files under `production/image_library/`;
- no duplicate Git blobs;
- no Registry/Story Shot references point to missing image-library files;
- nine Character Reference Sheet candidate manifests remain required by retained regression tests and builder validation.

## Archived obsolete Project Control trigger

Archived with exact Git blob preserved:

`docs/project_control/triggers/n17_n18_formal_archival.trigger`

Reason: its corresponding N17/N18 formal-archival workflow has already been archived, so this trigger no longer has an active consumer.

Archive destination:

`docs/project_control/archive/repository_cleanup_2026-10-07/original/docs/project_control/triggers/n17_n18_formal_archival.trigger`

## Dashboard repair

`docs/project_control/dashboard/dashboard.html` was stale at R332 / 2026-10-06 and still displayed N26 as unfinished with 31 registered Story Shots.

It has been refreshed as a compact derived dashboard aligned to Project State R337:

- N26 formally closed / canonical / registered / verified;
- 32 Story Shots;
- N27 absorbed into N26;
- next Story Shot not started;
- local main re-sync remains the next local formal-operation prerequisite;
- Production Console Q4 E2E PASS / Q5 not authorized;
- dashboard remains explicitly non-SSOT.

The previous dashboard version remains recoverable from Git history; no separate binary archive is required for this derived view.

## Source-material integrity finding

A pre-existing baseline inconsistency was identified and intentionally NOT repaired in this cleanup phase:

- `source_material/S2_black_lady/README.md` and `docs/project_control/core/project_state.json` both declare
  `source_material/S2_black_lady/S2_SOURCE_BLACK_LADY_TEXT_V001.txt`
  as `CANONICAL / LOCKED`;
- the file is absent from current main;
- Git commit history for that exact path is empty, indicating it has not previously existed at that repository path.

Expected locked SHA-256 recorded by Project Control:

`159fbba18c8a9be5fee2c47d5a4e244b72d375c5f19bd2e285fc1fbe688ed5e6`

This is a source-baseline integrity gap, not a cleanup target. No reconstruction or replacement was attempted without a separate Product Owner decision and exact-source verification.

## Safety boundary

No production binary, Registry, Story Shot Index, Video Index, CURRENT controlled reference, source novel, audio transcript, canonical audio, active workflow, or active script is changed by the cleanup portion of this phase.
