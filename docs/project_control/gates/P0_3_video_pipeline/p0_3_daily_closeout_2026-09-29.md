# P0.3 Daily Closeout｜2026-09-29

Status: `COMPLETE / EOD CLOSEOUT / S02-B ACTIVE / N19 CREATIVE REDESIGN PENDING / R138`

## 1. End-of-day authoritative state

- P0.1: `PASS / PRODUCT OWNER APPROVED`
- P0.2: `PASS / PRODUCT OWNER APPROVED`
- P0.3: `IN PROGRESS / CINEMATIC AUDIO-COMIC ROUTE ACTIVE / NOT YET VALIDATED`
- S02-A: `FORMALLY CLOSED`
- S02-B: `ACTIVE`
- Formally closed S02-B Story Shots today: `N16 / N17 / N18`
- Current active Story Shot: `N19`
- Current blocker: `CREATIVE COMPOSITION / SPATIAL INTEGRATION ONLY`
- Technical Bundle blocker: `NONE`

## 2. N16 formal completion

N16 was completed through the full formal production chain:

`Product Owner Approval → Exact Binary Verification → Canonical Publication → Story Shot Registration → Registration Verification → Project Control Closeout`

Canonical binary:

`production/image_library/approved/story_shots/N16_SISTER_QUESTION_APPROVED_V001.png`

Exact identity:

- dimensions: `941x1672`
- byte_size: `1942422`
- SHA-256: `b26fb7d64a60fbd28d39b0ae22f7c85df18d4f947f31a3591c847dd5e1acf406`
- Git blob: `44971dd53e37cd1b582bcf5094b0f09cb8e0647d`

Formal evidence:

- exact verification run: `36521093516`
- canonical publication commit: `c8fa5dc9f8b75ce7cb7c6f01899cbf45745558eb`
- Story Shot registration commit: `2de7c5eec0cf4223dbb04f12fb38f20dbe3860ca`
- registration verification run: `36530978877`

Result:

`N16 = FORMALLY CLOSED`

## 3. N17 + N18 formal archival completion

N17 and N18 were both Product Owner approved and then completed together through the automated formal archival chain.

Workflow run:

`36574163058`

N17 canonical:

`production/image_library/approved/story_shots/N17_BLOOD_DOOR_WARNING_APPROVED_V001.png`

- selected source: `N17 Candidate 03`
- byte_size: `1671344`
- SHA-256: `bd31599978d927cbd3748dc77073503c78cf87ccc68b21458de08625ebbfa3a3`
- Git blob: `c5020af8fa61225f0e4a88104990c1663fddcec9`

N18 canonical:

`production/image_library/approved/story_shots/N18_CLEAR_SKY_DOUBT_APPROVED_V001.png`

- selected source: `N18 Candidate 04｜Clean Regeneration`
- byte_size: `2158626`
- SHA-256: `18746fdde8a3b7699061fd6f4a8a6b666d50001250a2df902bb3b5995e7e2613`
- Git blob: `039471efd721fa5f822c4fb8ec933b4893f91641`

Shared formal evidence:

- exact-blob canonical publication commit: `c211475b78a8a800ff55fbf76201707a5f1bf3f8`
- Story Shot registration commit: `41e0a829419ff0f975e8bc6acce8e4f8c85ecb2e`
- Project Control closeout commit: `0f24df9f15744cbccfadb3d74c4ff07508ac0e1d`
- exact binary / registration verification: `PASS`

Results:

`N17 = FORMALLY CLOSED`

`N18 = FORMALLY CLOSED`

## 4. Pipeline automation conclusion

Two separate automation conclusions were proven today.

### 4.1 Generic Reference Delivery Bundle Builder

The permanent generic Story Shot Reference Bundle Builder remains the formal Bundle path:

- workflow: `.github/workflows/story-shot-reference-bundle-builder.yml`
- builder: `scripts/story_shot_reference_bundle_builder_v1.py`
- per-shot control: `production/bundle_specs/*.json`

It was used successfully again for N19.

### 4.2 Approved-binary archival automation

For N17 + N18, after the Product Owner manually uploaded the exact approved PNG binaries once, the remaining chain was successfully automated:

`Exact Binary Verification → Canonical Publication → Story Shot Registration → Registration Verification → Project Control Closeout`

This substantially reduces repeated manual status handoffs.

Important boundary:

- the N17/N18 archival implementation is currently a proven shot-specific automation pattern;
- it is NOT yet a fully generalized reusable Story Shot Approved Binary Archival Builder;
- manual Product Owner upload of the approved original PNG remains the current formal binary handoff;
- future generalization is an improvement item, not a completed capability.

## 5. S02-B Director Design revision

The original N19 beat was split because its two clauses carry different physical actions.

Approved revised progression:

`N16 → N17 → N18 → N19 → N20 → N21 → N22 → A06 → N23`

N19 owns:

`这里面瞬息万变，等你多来几次就知道了。`

Visual intent:

- Ning and Jun remain at the entrance;
- both look toward the exterior;
- Ning responds from experience;
- no inward walking yet.

N20 owns:

`进去之后也记得不要乱碰东西。`

Visual intent:

- doorway pause ends;
- both begin moving inward;
- Ning leads while continuing the practical reminder.

The Product Owner auditory wording `不要乱碰东西` is authoritative for production and overrides the older searchable S3 wording `不要乱放东西`.

Downstream renumbering:

- old N20 → `N21｜Sixteen Guests Enter`
- old N21 → `N22｜Neil Leads Inward`
- A06 remains unchanged
- old N22 → `N23｜Rain-Day Door Rule`

Director authority:

`S02-B Director Shot Design V0.2 / PRODUCT OWNER APPROVED / LOCKED`

## 6. N19 authority and Bundle completion

Locked Scene Reference Design:

`N19 Scene Reference Design V0.2`

Verified Bundle:

`N19_REFERENCE_DELIVERY_BUNDLE_V001`

Reference set:

1. `AST_IMG_000060` — Ning Character Reference Sheet
2. `AST_IMG_000057` — Jun Character Reference Sheet
3. `N17 canonical`
4. `N18 canonical`
5. `AST_IMG_000052` — Castle Entrance Scene Master / DAY_DOOR_OPEN

Build evidence:

- source / spec commit: `214af57acd778a208361cc5a73a2bd68052736ff`
- workflow run: `36576705556`
- job: `109434070260`
- Artifact ID: `11037987128`
- Artifact size: `8182280`
- digest: `sha256:b6aa9142bbeded26909c84faacbf69e93dde63f8ba0d3508df54d44402674276`
- exact reference verification: `5/5 PASS`
- independent downloaded-artifact verification: `PASS`
- `GENERATION_ALLOWED=TRUE`

Technical conclusion:

`N19 Bundle is valid and is NOT the cause of the current visual problem.`

## 7. N19 Candidate review result

### Candidate 01

Result:

`REJECTED`

Main problems:

- did not convincingly read as both characters looking through the doorway;
- front-facing / presentation-like body arrangement;
- clear cutout / pasted-in feeling;
- weak spatial integration between characters and architecture.

### Candidate 02

Result:

`REJECTED`

Final Product Owner feedback:

1. cutout feeling remained unresolved;
2. composition was very strange;
3. the two characters still did not actually look outside through the doorway.

No N19 candidate is approved at EOD.

Formal review checkpoint:

`docs/project_control/gates/P0_3_video_pipeline/n19_candidate_review_checkpoint_2026-09-29.md`

## 8. N19 creative conclusion

The failure is not primarily an eye-direction problem.

The unresolved problem is the full spatial geometry:

`camera → character placement → body angle → doorway → exterior gaze target → architectural integration`

Next N19 attempt must be:

`Candidate 03｜Clean Regeneration`

Do NOT edit Candidate 01 or Candidate 02.

Preferred next design direction:

- camera deeper inside the castle looking diagonally toward the doorway;
- observational medium two-shot;
- Jun nearer the door;
- Jun looks horizontally THROUGH the doorway toward courtyard / tree line;
- Ning half a step behind / further inside;
- Ning also looks through the doorway while speaking;
- bodies not parallel;
- crop approximately mid-thigh upward;
- architectural occlusion / subject overlap should integrate the figures into the space;
- environment lighting, edge light, contact shadow, depth of field and sharpness must be unified;
- restrained shoulder contact may be attempted only if anatomy remains natural.

The goal must read instantly as:

`They are standing inside the castle and looking through the open doorway outside.`

## 9. Bundle reuse rule for Candidate 03

The current N19 reference Bundle remains valid because the canonical authority set has not changed.

Therefore:

- do not rebuild the Bundle solely because Candidate 01 / 02 were rejected;
- before Candidate 03 generation, create a formal Candidate 03 execution patch that supersedes the failed compositions;
- continue using the verified five-reference Bundle unless the reference strategy itself is changed.

## 10. End-of-day boundary

Completed today:

- N16 formal closeout;
- N17 formal closeout;
- N18 formal closeout;
- N17/N18 automated post-upload archival validation;
- S02-B Director Design V0.2;
- N19 Scene Reference Design V0.2;
- N20 Scene Reference Design V0.1;
- N19 Reference Delivery Bundle V001 build + 5/5 verification;
- N19 Candidate 01 review;
- N19 Candidate 02 review.

Not completed:

- N19 approved image;
- N19 canonical publication / registration;
- N20 generation;
- N21 / N22 / N23 production;
- S02-B assembly;
- P0.3 Gate approval.

## 11. Project Control checkpoint

- Project State: `R138`
- Decision records: `BL-D-083 / BL-D-084`
- N19 review checkpoint: `docs/project_control/gates/P0_3_video_pipeline/n19_candidate_review_checkpoint_2026-09-29.md`

## 12. Resume point

Next session must resume from:

`N19 Candidate 03｜Clean Regeneration design + execution patch`

First action:

`Review and lock the Candidate 03 spatial-composition patch before sending Work to generate.`

Do not start N20 until N19 has an approved Story Shot candidate.

Do not reopen N16 / N17 / N18 unless the Product Owner explicitly authorizes a revision.
