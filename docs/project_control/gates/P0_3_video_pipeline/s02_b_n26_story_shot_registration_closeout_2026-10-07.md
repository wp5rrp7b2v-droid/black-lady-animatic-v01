# S02-B｜N26 Story Shot Registration Closeout

Date:

`2026-10-07`

Status:

`COMPLETE / PRODUCT OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED`

Shot:

`N26｜Lady's Rule and Forward Motion — Neil Explains and Leads the Group On`

Selected final result:

`N26 Candidate 03｜Controlled Modification`

N27 disposition:

`ABSORBED INTO N26 / NO SEPARATE STORY SHOT PRODUCTION`

## 1. Product Owner approval

The Product Owner explicitly approved N26 Candidate 03 on 2026-10-07.

Candidate lineage:

1. `Candidate 01` — rejected because Ning Qiushui and Jun Luyuan identity drifted.
2. `Candidate 02` — clean regeneration from the formal V002 identity-rescue Bundle; identity stabilized, but Ning/Jun depth separation and lighting restraint still failed the locked target.
3. `Candidate 03` — controlled modification of Candidate 02; Jun moved farther back/right relative to Ning and overall brightness / orange saturation was reduced while preserving character identity and walking motion.

Approval record:

`docs/project_control/gates/P0_3_video_pipeline/n26_candidate_03_approval_publication_prep_2026-10-07.md`

## 2. Exact approved binary

- format: `PNG`
- dimensions: `941 × 1672`
- mode: `RGBA`
- byte size: `2,504,586`
- SHA-256: `8dcd5f5449ad6429f45e7b4f59ce15bfd574eeb8aa45a83d4e4132df3cf436d9`
- Git blob: `a5ce429689a99437773385e25b9813745e380f74`

Approved source in Chat:

`image(20261007-021456).png`

## 3. Formal Bundle provenance

Bundle:

`N26_REFERENCE_DELIVERY_BUNDLE_V002`

Formal Build:

- workflow: `Story Shot Reference Bundle Builder`
- run: `37553891715`
- job: `112575513404`
- Artifact ID: `11453927794`
- Artifact size: `8,574,181 bytes`
- Artifact digest: `sha256:f7fdb72eb39aeea743dfd61707a817d5fae8cba34a0b924210985ecf34a3dd10`
- ZIP digest: `EXACT MATCH`
- references: `5/5 EXACT MATCH`
- WORK_HANDOFF: `PASS`

Formal Build record:

`docs/project_control/gates/P0_3_video_pipeline/n26_reference_delivery_bundle_v002_build_record_2026-10-07.md`

## 4. Candidate Intake Verification

Delivery Spec:

`production/candidate_delivery_specs/N26_CANDIDATE_03_DELIVERY_V001.json`

Staging path:

`staging/story_shot_candidates/N26/N26_Candidate_03_APPROVED.png`

Upload commit:

`3fdb72180038ece5bccf511ca023cda9a3d85c14`

Workflow:

`Story Shot Candidate Intake Verifier`

- run: `37562546224`
- job: `112602858354`
- evidence Artifact ID: `11457263413`
- evidence Artifact digest: `sha256:a6ae23c749d8561cde913ca76d0826f9e46b037ae5194ed9e333e44143eb6776`

Verified actual:

- byte size: `2,504,586`
- SHA-256: `8dcd5f5449ad6429f45e7b4f59ce15bfd574eeb8aa45a83d4e4132df3cf436d9`
- Git blob: `a5ce429689a99437773385e25b9813745e380f74`
- dimensions: `941 × 1672`

Result:

`CANDIDATE_INTAKE_VERIFIED = TRUE`

Intake record:

`docs/project_control/gates/P0_3_video_pipeline/n26_candidate_03_intake_verification_record_2026-10-07.md`

## 5. Canonical Publication

Canonical path:

`production/image_library/approved/story_shots/N26_LADYS_RULE_AND_FORWARD_MOTION_APPROVED_V001.png`

Workflow:

`N26 Canonical Exact-Blob Publication V001`

- run: `37563432085`
- job: `112605657063`
- publication commit: `e7d0e712c996fdc473ebcfa638f1ab1cc54aac8f`

Workflow result:

- `SOURCE_SIZE=2504586`
- `SOURCE_SHA256=8dcd5f5449ad6429f45e7b4f59ce15bfd574eeb8aa45a83d4e4132df3cf436d9`
- `SOURCE_GIT_BLOB=a5ce429689a99437773385e25b9813745e380f74`
- `EXACT_BLOB_PRESERVED=YES`
- `OVERALL_RESULT=PASS`

Independent canonical Git blob check:

`a5ce429689a99437773385e25b9813745e380f74`

Staging PNG after publication:

`ABSENT`

No resize, re-encode, recompression, screenshot substitution, crop, color change or other pixel mutation occurred during canonicalization.

Publication record:

`docs/project_control/gates/P0_3_video_pipeline/n26_canonical_publication_record_2026-10-07.md`

## 6. Story Shot Registration

Story Shot Index:

`production/story_shots/story_shot_index.jsonl`

Registration commit:

`feeff654439e01b6d163bb5c1b707144baf100ca`

Registered identity:

- shot_id: `N26`
- asset_class: `STORY_SHOT`
- approval_status: `APPROVED`
- lifecycle: `CURRENT`
- title: `Lady's Rule and Forward Motion`
- scene: `CASTLE_ENTRANCE_INNER_LOBBY`
- characters: `NEIL / NING_QIUSHUI / JUN_LUYUAN`
- timeline: `after N25 / source dialogue approx 02:19.000-02:23.000 / exact N26 micro-cut deferred`

Story beat:

Neil closes the entrance-door explanation, resumes clear leadership and leads the group deeper into the castle while Ning Qiushui and Jun Luyuan follow as recognizable, staggered secondary figures within the moving cohort.

Story Shot Index count after registration:

`32 APPROVED / CURRENT records`

## 7. Timeline evidence boundary

Source transcript:

`source_material/S3_audio_transcript/S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001.csv`

Relevant row:

`S3-MVP1-0021 / Neil / 00:02:19.000 → 00:02:23.000 / 这是夫人的要求。各位，请随我来`

The transcript itself marks this timing as:

`approx TC ... not an extraction boundary`

Therefore N26 registration intentionally does NOT convert this approximate source timing into an unverified exact edit boundary.

Exact N26 micro-cut remains deferred to assembly / edit validation.

## 8. Registration Verification

Workflow:

`N26 Story Shot Registration Verification V001`

Run:

`37563567464`

Job:

`112606088099`

Conclusion:

`SUCCESS`

Verified output:

- `N26_PASS`
- `SHA_MATCH=YES`
- `BLOB_MATCH=YES`
- `INDEX_MATCH=YES`
- `DIMENSIONS_MATCH=YES`
- `STAGING_CLEANUP_PASS`
- `OVERALL_RESULT=PASS`

## 9. N27 merge disposition

Product Owner decision remains active:

`N27 IS ABSORBED INTO N26`

N26 now contains both functions:

- `这是夫人的要求。`
- `各位，请随我来。`
- rule-source close;
- Neil resumes leadership;
- group begins following toward deeper interior.

No separate N27:

- Director Design;
- Scene Reference;
- Bundle;
- Candidate;
- Canonical Publication;
- Registration.

## 10. Final disposition

`N26 = FORMALLY CLOSED / CANONICAL / REGISTERED / VERIFIED`

Canonical active sequence tail:

`N23 → N24 → A06 → N25 → N26`

P0.3 remains:

`IN PROGRESS / CINEMATIC AUDIO-COMIC ROUTE ACTIVE / NOT YET FINALLY VALIDATED`

This N26 closeout does not itself complete the P0.3 gate.

No later Story Shot is automatically started by this closeout.
