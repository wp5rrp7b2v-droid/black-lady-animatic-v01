# P0.3 Editing Workflow Framework V1

Status: `ACTIVE / REFERENCE FRAMEWORK / NON-TEMPLATE`

Effective date: 2026-09-27  
Governance: RC-026  
Reference implementation: `P03_OPENING_V2_PROOF_REVIEW_V002`

## 1. Purpose

This document registers a reusable editing **process framework** for later `诡舍·黑衣夫人` sequences.

It is **not** a fixed shot template, timing template, transition preset, motion preset, or mandatory Remotion implementation.

The project may reuse the workflow logic while redesigning the actual edit for each story beat according to:

- source audio and dialogue semantics;
- narrative purpose;
- available Story Shots;
- character performance and spatial continuity;
- emotional rhythm;
- shot-to-shot contrast;
- the strengths and limits of the selected rendering tool.

V002 is retained as the clearest current reference implementation of this process, not as a visual preset to copy.

## 2. Reusable workflow

### Stage 1 — Source / story analysis

Read the canonical source audio and relevant story/transcript context first.

Determine:

- what is being said or narrated;
- where the semantic beats are;
- which actions, reactions, expressions, spaces, or objects must be shown;
- where continuity or suspense requires a visual hold rather than a cut.

The edit starts from story and audio meaning, not from effects.

### Stage 2 — Director / editor design in Chat

Chat designs the sequence before engineering execution.

Depending on the scene, this may include:

- shot order;
- shot function;
- candidate cut points;
- duration / rhythm;
- visual emphasis;
- whether a shot should remain static or move;
- transition type;
- focus / motion / shake / crop / reframe treatment;
- entry and exit behavior.

No timing or treatment is inherited automatically from another sequence.

### Stage 3 — Contextual timeline design

Build the audiovisual timeline around the current story beat.

The timeline may use transcript boundaries, dialogue phrases, action beats, reaction beats, low-energy valleys, visual continuity, or intentional holds.

A prior timeline may be reused only when it remains narratively correct.

The V002 `991-frame / 12-shot` map is therefore a reference example only, not a project-wide timing template.

### Stage 4 — Canonical input verification

Before render, verify the actual inputs selected for this edit:

- approved/current Story Shot identity;
- canonical path;
- SHA-256 where locked;
- Git blob identity;
- byte size;
- dimensions / media validity;
- canonical audio identity.

Do not silently substitute previews, re-encoded images, stale shots, or non-canonical audio.

### Stage 5 — Engineering implementation

Translate the Chat-designed timeline into the chosen rendering engine.

The implementation engine is replaceable. Examples include:

- Remotion;
- libopenshot;
- another approved NLE/render path.

The engine executes the edit; it does not decide the story design.

### Stage 6 — Scene-specific editorial treatment

Add only the motion and transitions that serve the current scene.

Possible treatments include:

- static hold;
- push / pull;
- lateral drift / reframe;
- dissolve;
- blur/focus transition;
- fade;
- vignette/focus emphasis;
- selective shake or rotation;
- other restrained 2D treatment.

There is no requirement that every shot move, or that every sequence use the same transition vocabulary.

V002's light scale/drift/dissolve treatment is a reference example, not a mandatory recipe.

### Stage 7 — Continuous source-audio assembly

Where the source scene is meant to play continuously, preserve one uninterrupted canonical audio track and cut/re-time the picture around it.

Do not fragment, re-time, or rebuild the source audio merely to make a visual template fit.

Any deliberate audio edit must be separately justified and traceable.

### Stage 8 — GitHub Actions render + technical QC

Render through the approved project execution path and verify the produced media.

Typical checks include:

- expected sequence/timeline;
- frame count / fps;
- duration;
- resolution;
- video codec / pixel format;
- audio stream presence and continuity where required;
- full decode;
- SHA-256 / byte size;
- artifact publication.

Exact output specifications may change by delivery target, but deviations must be explicit.

### Stage 9 — Full-context Product Owner review

Primary artistic review is the complete audiovisual context.

Do not approve an edit solely from isolated micro-clips, individual transitions, or technical PASS.

Product Owner reviews:

- audio/story alignment;
- narrative readability;
- cut rhythm;
- shot duration;
- slideshow risk;
- whether motion helps or distracts;
- whether transitions feel motivated;
- emotional continuity.

### Stage 10 — Targeted iteration

After review, revise the specific weak points rather than automatically increasing effects across the whole sequence.

Examples:

- move one cut point;
- hold one shot longer;
- remove motion from one shot;
- strengthen one action beat;
- replace one transition;
- change a shot rather than forcing an effect to solve a composition problem.

A new iteration must remain driven by the scene, not by the previous version's parameter pattern.

## 3. Core principle

The reusable production logic is:

`Canonical story/audio context → Chat director/edit design → contextual timeline → canonical input verification → engine implementation → scene-specific motion/transition treatment → continuous source-audio assembly where appropriate → GitHub Actions render/QC → full-context PO review → targeted iteration`

The reusable asset is the **decision-and-execution process**, not V002's exact shot count, frame map, scale values, transitions, or Remotion code.

## 4. V002 reference value

`P03_OPENING_V2_PROOF_REVIEW_V002` is retained as a useful reference because it demonstrates:

- story/audio alignment established before visual enrichment;
- one continuous canonical audio track;
- a director-designed shot timeline;
- canonical Story Shot verification;
- restrained 2D editorial treatment layered after the edit structure;
- GitHub Actions render and technical QC;
- full-sequence Product Owner review.

Its specific artistic result was not final and does not become a universal production preset.

## 5. Authority boundary

This framework governs the **editing workflow method** only.

It does not override:

- Story Shot production / registration authority under RC-024 / RC-025;
- Product Owner-only Gate / Phase approval;
- sequence-specific director decisions;
- future tool-specific technical constraints.

When a later sequence needs a different timeline, motion language, transition style, or rendering engine, that variation is expected and should be designed explicitly.
