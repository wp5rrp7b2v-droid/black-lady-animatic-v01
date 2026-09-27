# P0.3｜视频制作与剪辑 Pipeline 再验证

Status: `IN PROGRESS / CINEMATIC AUDIO-COMIC ROUTE ACTIVE / NOT YET VALIDATED`

Prerequisite:

- P0.1 = PASS / PRODUCT OWNER APPROVED
- P0.2 = PASS / PRODUCT OWNER APPROVED

P0.3 owns validation of the path from approved visual assets + canonical source audio to an acceptable final audiovisual result.

## Locked scope

P0.3 must validate, with real project material rather than design-only documentation:

- historical failure review;
- story-beat / shot planning against canonical source audio;
- canonical source-audio retrieval and extraction;
- approved Story Shot production and continuity;
- edit / framing / crop / restrained zoom as visual-reading tools;
- optional AI video / motion generation only where it materially improves selected shots;
- Remotion responsibility boundary;
- timing / continuity / dialogue completeness;
- a representative real audiovisual result as feasibility evidence.

## Historical evidence retained

2026-09-23 established:

- more stills + hard cuts alone can remain slideshow-like;
- Remotion bitmap pan / zoom is not a spatial reconstruction engine;
- A01 DepthFlow single-shot 2.5D was technically viable enough to test further.

2026-09-25 superseding artistic evidence:

- the real `A01 → Wide → Tight → A02` 4-shot 2.5D sequence caused visible character deformation;
- Product Owner judged the character-shot 2.5D route unacceptable;
- character-shot single-image DepthFlow / 2.5D is therefore no longer the current main production path.

This does not erase the technical evidence. Environment-only parallax may still be used selectively if useful.

## Current main validation route

`CINEMATIC AUDIO COMIC`

Core production logic:

`canonical story/audio → story beat → composition → automatically retrieve minimum necessary approved references → generate Story Shot → Product Owner PASS/FAIL → targeted local edit only when needed → approved Story Shot library → edit`

Rules:

- story determines composition;
- composition determines which references are needed;
- candidates / rejected / WIP do not enter the formal library;
- only Product Owner-approved Story Shots are stored and indexed;
- once composition and identities are basically correct, small fixes use local edit / inpainting rather than full-image regeneration;
- normal cuts remain valid;
- crop / restrained zoom guide viewer attention; they are not treated as fake physical camera reconstruction;
- AI video remains an optional enhancement for selected key shots, not the current blocker;
- Remotion remains compositor / timing / canonical-audio / SFX / output layer.

## Locked Work image-generation delivery chain

For formal Story Shot / visual generation executed in Work, the production path is locked as:

`GitHub canonical assets → Resolver / Registry validation → Reference Delivery Bundle → Work automatic PNG acquisition → image generation`

Operational boundary:

- GitHub remains canonical binary authority.
- Resolver / Registry selects and validates the minimum necessary CURRENT / APPROVED references.
- A traceable Reference Delivery Bundle transports the exact PNG binaries and their manifest to Work.
- Standard implementation = GitHub Actions / repo-native automated runner builds the bundle from canonical repo inputs and publishes a short-lived workflow artifact.
- Work automatically downloads that artifact through the connected GitHub capability, unpacks and revalidates it, then supplies the PNGs to image generation.
- The Product Owner does not locally build or upload the ZIP; normal manual reference upload count is 0.
- Codex / Local Terminal are not part of this standard delivery path and must not be introduced merely to build the Bundle.
- Work generates only after the Bundle PNGs are materially available and validated.
- Direct private-GitHub PNG browsing/fetching is not the production baseline.
- Product Owner is not expected to routinely hand-pick, download, ZIP or re-upload canonical references.
- Delivery failure is fail-closed: no formal generation proceeds without the required verified references.
- Any temporary exception requires explicit provenance and Product Owner authorization.

This rule is project-level governance under RC-022 / BL-D-070 and applies to N03 and subsequent formal Work-based image generation.

## Locked Story Shot production + registration SOP

RC-024 standardizes the complete formal Story Shot lifecycle as:

`Director Design → Reference Delivery Bundle → Work Generation → Product Owner Approval → Original PNG Upload → Binary Verification → Exact-Blob Canonical Rename → Story Shot Index Registration → Registration Verification → Project Control Closeout`

Formal SOP:

`docs/project_control/gates/P0_3_video_pipeline/story_shot_production_registration_sop_v1.md`

Hard completion gates:

1. Product Owner approved;
2. canonical binary published;
3. Story Shot Index registered;
4. registration verification PASS.

Approval alone, upload alone, or index registration without binary identity verification does not constitute formal completion.

### Authority / precedence

- This README is a Gate summary, not the primary operational SOP.
- Story Shot operational authority: `story_shot_production_registration_sop_v1.md` + RC-024 / RC-025.
- P0.2 Asset Registry `SHOT` rules continue to govern Asset Registry records; they do not retroactively rename or auto-register P0.3 `STORY_SHOT` records.
- Product Owner upload in the Story Shot SOP is final approved-output publication only; normal reference delivery remains automated with manual PO reference upload = 0.

## Story Shot model

Product Owner approved the following model on 2026-09-25:

- A01–A07 and later N01-style additions are one logical asset class: `STORY_SHOT`;
- A / N prefixes are historical IDs only and do not represent different asset systems;
- only Product Owner-approved Story Shots may enter the formal library and registration;
- candidate / rejected / WIP outputs do not enter the formal library or registration;
- existing A01–A07 must not be renamed or duplicated merely to normalize the model;
- later production must make approved Story Shots retrievable by story beat, characters, scene and continuity.

Implementation boundary for 2026-09-25 was historical and is now superseded by the implemented Story Shot system.

Implementation status as of 2026-09-27:

`IMPLEMENTED / ACTIVE / 17 APPROVED STORY SHOTS / OPENING V2 STORY-SHOT SET COMPLETE`

- machine-readable index: `production/story_shots/story_shot_index.jsonl`;
- registered approved Story Shots: A01–A07 + N01–N10 = 17;
- A01–A07 remain at their legacy `production/image_library/approved/A_Series/` paths and are not duplicated;
- N01–N10 are canonically published under `production/image_library/approved/story_shots/`;
- exact upload-to-canonical renames reuse the original Git blobs with no PNG re-encode;
- N08–N10 upload verification run: `36247789055`;
- N06–N07 upload verification run: `36289949835`;
- N08 SHA-256: `6bda5a8cb4d04d15071f95c6b3fdce09b10230ac95100d59aabf5bad4aef1bb4`;
- N09 SHA-256: `5e76be2c9815a6caa2d8688d1879bb5ddaad78352b6440ed220dd08332a5e0ac`;
- N10 SHA-256: `14dbf276dbf9ef6c7de84570d46f40230daa3ba53a304ccdc05645c58e9f6e54`.

## Current Opening V2 Story Shot state

Product Owner-approved / formally registered additions now include:

- N06 = Neil Speaking State A / Candidate 02;
- N07 = Neil Speaking State C / Candidate 01;
- N08 = Castle Entrance Architecture / Candidate 01;
- N09 = Neil Formal Butler Descriptor / Candidate 03;
- N10 = Neil Subtle Smile / Candidate 01.

Locked narrative / spatial boundaries:

- N08 makes the castle itself the subject for the narrator beat “巨大的褐色古堡前”;
- N09 keeps Neil clearly outside on the castle entrance platform with the open double doors behind him;
- N10 is a restrained closed-mouth slight-smile beat only; no teeth, speech, turn or step;
- N05 remains the later turn / threshold-action shot.

Opening V2 planned sequence:

`A01 → A02 → N06 → N02 → N07 → N03 → N04 → N08 → N09 → N10 → N05 → N01`

Opening V2 Story-Shot Set is now complete and fully covered by approved Story Shots.

## Immediate next step

1. assemble the revised 12-shot Opening V2 proof from canonical source audio + approved Story Shots;
2. re-review audio/action alignment, cut rhythm, narrative readability, slideshow risk and restrained 2D motion;
3. do not claim P0.3 PASS until representative production evidence is sufficient and Product Owner explicitly approves the Gate.

See:

- `story_shot_production_registration_sop_v1.md`
- `p0_3_progress_closeout_2026-09-23.md`
- `p0_3_progress_closeout_2026-09-25.md`

No P0.3 PASS claim is permitted until representative production evidence is sufficient and Product Owner explicitly approves the Gate.

## Opening V2 Audio Alignment Analysis V001｜2026-09-27

Status: `GITHUB ACTIONS ANALYSIS PASS / INTERNAL CUTS CANDIDATE ONLY / DIRECTOR LOCK PENDING`

Canonical input:

- `staging/p0_3_a01_a02_transition_validation/AUDIO_MVP1_CANONICAL_V001.m4a`
- SHA-256: `8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0`
- duration: `359.141995 sec`
- Opening analysis scope: `00:00.000–00:33.020`

Successful GitHub Actions evidence:

- workflow run: `36293571350`
- artifact: `P03_OPENING_V2_AUDIO_ALIGNMENT_ANALYSIS_V001`
- artifact ID: `10922898643`
- artifact digest: `sha256:2da55ec3eaec37038642ad27a39e3e77e59dcc9a6b62eeb93c5d3847455764b0`

Verified fixed transcript boundaries:

- `A01→A02 = 3.250s`
- `A02→N06 = 6.550s`
- `N04→N08 = 19.700s`
- `N05→N01 = 30.030s`
- `N01→END = 33.020s`

Acoustic candidate internal boundaries:

- `N06→N02 = 8.940s`
- `N02→N07 = 11.200s`
- `N07→N03 = 13.200s`
- `N03→N04 = 15.310s` — weak / edge-of-search-window candidate; do not lock yet
- `N08→N09 = 21.620s`
- `N09→N10 = 24.420s`
- `N10→N05 = 27.160s`

Important interpretation:

- multi-threshold `silencedetect` found no true silence interval in the 0–33.020s opening window; the source contains continuous underlying audio energy;
- therefore the internal points above are low-energy-valley candidates refined around transcript-semantic targets, not final edit boundaries;
- the next step is director review / semantic alignment, with targeted human-listening or stronger speech-text alignment only where a candidate is ambiguous;
- no source-audio speed change and no destructive audio edit occurred.
