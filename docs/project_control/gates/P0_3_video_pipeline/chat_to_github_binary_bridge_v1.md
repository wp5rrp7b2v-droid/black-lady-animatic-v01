# CHAT_TO_GITHUB_BINARY_BRIDGE_V1

Status: `REAL TEST BLOCKED / SOURCE BINARY VERIFIED / GITHUB FILE-HANDLE UPLOAD CAPABILITY MISSING`

Date: 2026-09-29

## Objective

Move Story Shot candidate delivery responsibility from Work to Chat:

`Work = binary producer → Chat = GitHub delivery / verification / publication control plane`

N16 Candidate 01 is the first real test.

## Source binary

Chat has direct access to the Product Owner-approved N16 Candidate 01 conversation attachment and re-read the original bytes.

Verified identity:

- dimensions: `941x1672`
- byte_size: `1942422`
- SHA-256: `b26fb7d64a60fbd28d39b0ae22f7c85df18d4f947f31a3591c847dd5e1acf406`
- Git blob: `44971dd53e37cd1b582bcf5094b0f09cb8e0647d`
- PNG signature: `PASS`

This exactly matches the Product Owner approval checkpoint and N16 Candidate Delivery Spec.

## Real Chat-side transport test

Available Chat GitHub write capabilities were inspected.

Confirmed available:
- UTF-8 file creation/update;
- Git blob creation from supplied UTF-8/base64 text content;
- Git tree / commit / ref mutation;
- workflow and Project Control writes.

Missing capability:
- no supported GitHub action currently accepts a Chat conversation attachment, local container path, file ID, or file URI as a raw binary upload source.

Therefore Chat cannot safely pass the existing 1,942,422-byte PNG from the conversation file store directly into GitHub without introducing an unsupported transport workaround.

## Safety / integrity boundary

The following are explicitly rejected as production solutions:

- screenshot;
- re-encode;
- image regeneration;
- converting and manually reconstructing the binary through ad-hoc base64 chunk files;
- using a different copy without exact-source verification;
- repeated Work upload attempts after an upload-control interruption.

The canonical candidate binary remains unchanged and un-published.

## Current result

`SOURCE_BINARY_EXACT_VERIFICATION = PASS`

`CHAT_TO_GITHUB_BINARY_DELIVERY = BLOCKED_ON_FILE_HANDLE_UPLOAD_CAPABILITY`

`CANDIDATE_INTAKE_VERIFIED = NOT YET RUN`

`PRODUCT_OWNER_MANUAL_GITHUB_UPLOAD = 0 SO FAR`

No canonical publication or Story Shot registration was performed.

## Preferred resolution

Use a Chat-accessible authorized computer/filesystem terminal integration so Chat can operate the user's existing Git working copy and authentication directly, while preserving exact source bytes.

Once connected, the target operation remains:

`staging/story_shot_candidates/N16/N16_Candidate_01_APPROVED.png`

and must verify against the locked SHA-256 / byte size / dimensions / Git blob before push.
