# P0.3 Daily Closeout｜2026-09-30

Status: `COMPLETE / EOD CLOSEOUT / S02-B ACTIVE / N21 STRATEGY REVIEW PENDING`

## 1. End-of-day authoritative state

- P0.1: `PASS / PRODUCT OWNER APPROVED`
- P0.2: `PASS / PRODUCT OWNER APPROVED`
- P0.3: `IN PROGRESS / CINEMATIC AUDIO-COMIC ROUTE ACTIVE / NOT YET VALIDATED`
- S02-A: `FORMALLY CLOSED`
- S02-B: `ACTIVE`
- N16 / N17 / N18 / N19 / N20: `APPROVED / CANONICAL / REGISTERED / VERIFIED / CLOSED`
- Current active Story Shot: `N21`
- N21 approved candidate: `NONE`
- N21 Candidate 04: `NOT AUTHORIZED`

## 2. N20 formal completion

N20 was completed through the full formal Story Shot chain.

Canonical:

`production/image_library/approved/story_shots/N20_DO_NOT_TOUCH_THINGS_APPROVED_V001.png`

Exact identity:

- dimensions: `941x1672`
- byte_size: `2022630`
- SHA-256: `a61ab1310e86938b2a416516138981aafaf421add44c1a9d5a80d0ff9ec59a9e`
- Git blob: `58e145a51c3f993827e5e47964ad0e7f9dd9f0aa`

Formal evidence:

- exact verification run: `36663290811`
- canonical publication commit: `230cdbd8e3e78e4211a287eaffe5073f5231485e`
- Story Shot registration commit: `6381aa74cd7f959b65798d1eb21db5fa8ee99f96`
- registration verification run: `36663515652`

Result:

`N20 = FORMALLY CLOSED`

## 3. S02-B V0.3 audience-retention revision

The Product Owner approved and locked:

`S02-B Director Shot Design V0.3 + Review Patch 01`

The revised high-level production baseline from N21 onward includes:

1. narrative value;
2. effective visual change;
3. natural in-story character performance;
4. spatial depth;
5. Ning as sequence-level observational anchor;
6. differentiated character function;
7. exact composition deferred to each node;
8. visual-tone continuity from generation stage.

Critical governance clarification:

`LOCK NODE FUNCTION + HIGH-LEVEL RULES / DO NOT PRE-LOCK EVERY SHOT'S EXACT COMPOSITION`

The revised downstream sequence is:

`N21 → N22 → N23 → N24 → A06 → N25 → N26 → N27`

## 4. N21 responsibility redesign

N21 was separated from the old named-character-seeding burden.

Locked N21 core:

`GROUP SCALE + CASTLE ENTRY CONTINUITY`

Named-character seeding for Su Xiaoxiao / Liao Jian / Wen Qingya / Guang Yong was moved to N22.

Crowd production rules introduced today:

- do not require sixteen equally clear faces / bodies;
- natural crowd movement is more important than a literal group portrait;
- one global movement direction with local asynchrony;
- posed / cloned / publicity-photo crowd staging fails Director Review;
- same-space / same-time color continuity with N20 is mandatory.

## 5. N21 Scene Reference / Bundle redesign

Old:

`N21_REFERENCE_DELIVERY_BUNDLE_V001`

remains technically valid `6/6 PASS` but is historical and superseded for N21 generation.

New:

`N21_REFERENCE_DELIVERY_BUNDLE_V002`

formal references:

1. `AST_IMG_000052` — Castle Entrance Scene Master
2. `N20` — immediate Story Shot continuity

Build evidence:

- spec commit: `26aebca839ec5016762bed92bc9b52a5aa430b99`
- workflow run: `36699004641`
- job: `109833744730`
- Artifact ID: `11088797193`
- artifact size: `4306690 bytes`
- digest: `sha256:e3ec3be6f1a75eae6507801a776bcf2a6e07312d2a26a91909466a73b805f4dc`
- builder exact verification: `2/2 PASS`
- independent downloaded-artifact verification: `2/2 PASS`
- `GENERATION_ALLOWED=TRUE`

Technical conclusion:

`N21 BUNDLE V002 IS VALID; CURRENT FAILURE IS CREATIVE / GENERATION QUALITY, NOT BUNDLE INTEGRITY`

## 6. N21 Candidate 01–03 review

No candidate was Product Owner approved.

### Candidate 01

Main failure:

`FRONTAL ENSEMBLE / HERO-DUO DOMINANCE / CHOREOGRAPHED CROWD / OVER-BRIGHT LOOK`

### Candidate 02

Improved crowd naturalism, but failed:

`ENTRY-SPACE GEOMETRY + ADVENTURE / THREAT READ`

Product Owner described the result as closer to a commuter crowd than entering a Blood Door adventure.

### Candidate 03

Improved:

- dark / unknown atmosphere;
- reduced crowd size;
- spatial compression;
- reduced commuter feeling.

Still failed:

- Jun Luyuan hunched rear-view posture;
- Ning Qiushui identity drift;
- excess protagonist visual weight;
- residual orderly queue feeling.

Review checkpoint:

`docs/project_control/gates/P0_3_video_pipeline/n21_candidate_review_checkpoint_2026-09-30.md`

## 7. Key conclusion from the three attempts

The working conclusion is not that more prompt rules are required.

Observed production problem:

`MULTI-PERSON GENERATION SHOWS A REPEATED TRADEOFF BETWEEN CROWD COMPOSITION / ATMOSPHERE / CHARACTER IDENTITY / BODY PERFORMANCE`

The Product Owner specifically judged the latest character-shape failures as generation failure rather than a missing-rule problem.

Root cause is not formally proven and must not be recorded as a confirmed model degradation.

## 8. N21 next-strategy direction

Preferred direction for next review:

`SIMPLIFY THE SHOT FUNCTION BEFORE GENERATING AGAIN`

Candidate principle under consideration:

`16 = NARRATIVE FACT / NOT SINGLE-FRAME COUNTING REQUIREMENT`

Potential N21 role:

`COHORT / THRESHOLD MOOD SHOT`

Possible simplifications:

- fewer visible people;
- more cropping / occlusion / silhouettes;
- no requirement that Ning / Jun be clearly identifiable;
- prioritize unknown / danger / transition atmosphere;
- main door optional if its inclusion harms composition;
- later nodes recover named-character readability.

This strategy is not yet locked as Candidate 04 authority.

## 9. End-of-day boundary

Completed today:

- N20 formal closeout;
- S02-B V0.3 audience-retention redesign;
- Review Patch 01 / eight high-level production rules;
- N21 Node-Level Director Shot Design V0.1;
- N21 Scene Reference Design V0.3;
- N21 Bundle V002 design;
- N21 Bundle V002 build + independent 2/2 verification;
- N21 Candidate 01 review;
- N21 Candidate 02 review;
- N21 Candidate 03 review;
- N21 multi-person generation failure-pattern assessment.

Not completed:

- N21 approved Story Shot;
- N21 canonical publication / registration;
- N22 onward production;
- S02-B assembly;
- P0.3 Gate approval.

## 10. Resume point

Next session must resume from:

`N21 TASK-SCOPE SIMPLIFICATION / DIRECTOR STRATEGY REVIEW`

First action:

Review whether N21 should formally become a smaller, partially obscured cohort / threshold mood shot with no requirement to visibly prove all sixteen participants or clearly identify Ning / Jun.

Do not generate Candidate 04 before that decision.

Do not start N22.
