# N13_REFERENCE_DELIVERY_BUNDLE_V001｜Build Design + Execution Prep

Status: `EXECUTED / BUILD SUCCESS / 5 OF 5 PASS`

Date: 2026-09-27

## 1. Execution target

Create one temporary GitHub Actions workflow:

`.github/workflows/p03-n13-reference-delivery-bundle-v001.yml`

Its only production purpose is to build:

`N13_REFERENCE_DELIVERY_BUNDLE_V001`

from the five locked canonical references in:

`docs/project_control/gates/P0_3_video_pipeline/n13_reference_delivery_bundle_design_v0_1.md`

## 2. Trigger strategy

When Product Owner authorizes actual construction:

- add / activate the workflow on `main`;
- use a path-scoped push trigger on the workflow file so the build runs immediately from the exact source commit;
- do not use Codex or Local Terminal merely to build the Bundle.

## 3. Required workflow checks

The workflow must fail closed unless all 5 references pass:

1. Registry / Story Shot Index cardinality;
2. entity / role / authority identity;
3. approval status = APPROVED;
4. lifecycle = CURRENT;
5. expected canonical path;
6. expected byte size;
7. expected SHA-256;
8. expected Git blob SHA;
9. PNG signature;
10. PNG dimensions readable;
11. source is regular file and not symlink;
12. byte-identical copy into artifact;
13. final artifact revalidation.

Expected final line:

`PASS: 5/5 exact canonical reference binaries verified`

## 4. Manifest requirements

`delivery_manifest.json` must contain:

- bundle ID;
- target `N13_CANDIDATE_01`;
- source commit;
- reference count = 5;
- exact identity for every input;
- authority precedence;
- explicit exclusions;
- manual PO reference upload = 0;
- director lock;
- overall result.

Explicit exclusions must include:

- N11 unpublished final candidate;
- N12 unpublished final candidate;
- N09;
- N10;
- A05;
- all rejected / superseded candidates.

## 5. WORK_HANDOFF requirements

Must explicitly state:

- this is not the reveal shot;
- viewer attention moves downward toward the waist;
- entire waist answer-zone must not be cleanly exposed;
- no keys;
- equally important: no obvious "no keys";
- vest / jacket / crop / occlusion should preserve uncertainty;
- Neil is static and inside the entrance;
- no hands / movement;
- A05 exclusively owns the reveal.

## 6. Expected post-build evidence

On success, capture:

- workflow source commit;
- workflow run ID;
- job ID;
- job conclusion;
- artifact ID;
- artifact name;
- artifact digest;
- artifact size;
- expiry;
- 5/5 verification log evidence.

Then write:

`docs/project_control/gates/P0_3_video_pipeline/n13_reference_delivery_bundle_v001_build_record_2026-09-27.md`

and advance Project Control to Work generation.

## 7. Execution result

- Product Owner authorized construction.
- Workflow created: `.github/workflows/p03-n13-reference-delivery-bundle-v001.yml`
- Source commit: `bdd2480fb995462f89ea51400d02b0135912ce42`
- Run: `36314032099`
- Job: `108605228883`
- Result: `SUCCESS`
- Artifact ID: `10930326122`
- Digest: `sha256:0b40fd3e34b18297c679c2e307f2e4d6480e90c2eef1697adcbdd8b15d8d6fb7`
- Verification: `5/5 exact canonical reference binaries verified`

Build record:

`docs/project_control/gates/P0_3_video_pipeline/n13_reference_delivery_bundle_v001_build_record_2026-09-27.md`

## 8. Boundary

Execution is complete. Work generation of N13 Candidate 01 is now authorized. No N15 work or Story Shot registration before N13 Product Owner review.
