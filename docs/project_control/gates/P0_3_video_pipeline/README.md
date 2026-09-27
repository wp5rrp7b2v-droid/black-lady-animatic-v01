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

## Opening V2 Contextual Proof Review V001｜2026-09-27

Status: `TECHNICAL_RENDER_PASS / READY_FOR_PRODUCT_OWNER_CONTEXTUAL_REVIEW / TIMING NOT LOCKED`

Review-method correction:

- the seven 3-second files were only local listening windows around candidate cut points;
- they were never intended as equal 3-second final segmentation;
- isolated pause review proved insufficient because edit quality depends on picture + uninterrupted speech + narrative rhythm;
- therefore Draft 01 timing is now judged in the complete audiovisual proof first.

Formal technical evidence:

- sequence: `A01 → A02 → N06 → N02 → N07 → N03 → N04 → N08 → N09 → N10 → N05 → N01`
- workflow run: `36294677578`
- artifact: `P03_OPENING_V2_PROOF_REVIEW_V001`
- artifact ID: `10923721767`
- artifact digest: `sha256:e928f8f91f578159e16711c64f6fa215a347603563901d13bee332b2981d3af2`
- output MP4 SHA-256: `d538c87e8da781aec61401b2c7a01ce5e25a4ad0de038299d598685d376e771e`
- output: 1080×1920 / H.264 yuv420p / 30 fps / 991 decoded frames / continuous AAC audio
- full decode QC: PASS

The current internal cut positions remain Draft 01 candidates and are not director-locked. Product Owner must review the complete 33-second audio-image sequence before timing changes or P0.3 approval.

## Opening V2 Proof Review V002｜2026-09-27

Status: `TECHNICAL_RENDER_PASS / READY_FOR_PRODUCT_OWNER_CONTEXTUAL_REVIEW / TIMING NOT LOCKED`

V002 preserves the V001 12-shot sequence, uninterrupted canonical audio and Draft 01 timing map, while enriching only restrained 2D editorial language.

Added treatment:

- A01 fade in from black and N01 fade out to black;
- selected 3–6 frame dissolves rather than dissolving every cut;
- restrained blur/focus dissolves on N08→N09 and N10→N05;
- differentiated static / push / pull / slight horizontal drift behavior;
- light vignette-based focus guidance on selected shots;
- one short N05 shake/settle event only.

Explicit exclusions remain:

- no 2.5D depth warp;
- no character deformation;
- no Story Shot replacement;
- no canonical audio speed change;
- no final timing lock.

Technical evidence:

- source commit: `3c90d484ebb958b3b1988ceb8ba8f0e6aa21bb4a`
- workflow run: `36296689531`
- artifact: `P03_OPENING_V2_PROOF_REVIEW_V002`
- artifact ID: `10924430609`
- artifact digest: `sha256:323a48034e45562b5153d635dbe565f51211d81a694c44202b6da92e4deba2ac`
- output MP4 SHA-256: `70d7922244161dd216a26446fd75531db20eea0ac7fc25f567f6ff14e2746e3a`
- output byte size: `18,892,138`
- output: 1080×1920 / H.264 yuv420p / 30 fps / 991 decoded frames / continuous AAC audio
- full decode QC: PASS

Next step is Product Owner contextual review. P0.3 remains IN PROGRESS and no final timing lock is claimed.

## Opening V2 V002 Product Owner Review｜2026-09-27

Product Owner result: `ARTISTIC ENRICHMENT NOT APPROVED / DIFFERENCE NOT PERCEPTIBLE`

The V002 technical render remains valid evidence, but its editorial treatment was too conservative to create a meaningful perceptual change versus V001.

Implication:

- retain the successful 12-shot sequence and audio/story alignment;
- do not revert to 2.5D or character-warp techniques;
- V003 should make transitions, motion amplitude, focus shifts and the N05 action accent clearly visible while remaining controlled;
- P0.3 remains IN PROGRESS and no final timing lock or gate PASS is claimed.

## Opening V2 Proof Review V003｜2026-09-27

Status: `TECHNICAL_RENDER_PASS / READY_FOR_PRODUCT_OWNER_CONTEXTUAL_REVIEW / TIMING NOT LOCKED`

V003 is the stronger editorial-enrichment build after Product Owner found V002 too subtle to perceive.

Preserved:

- 12-shot sequence unchanged;
- uninterrupted canonical source audio unchanged;
- Draft 01 timing unchanged;
- approved Story Shot binaries unchanged.

Stronger but controlled treatment:

- 12-frame opening fade-in and closing fade-out;
- selected 6–12 frame dissolves;
- 12-frame blur/focus dissolves up to about 5.5 px blur;
- character pushes generally 3–5% where appropriate;
- N08 architectural push to 6.5%;
- N03 4% pull-back plus 16 px horizontal drift;
- stronger focus/vignette guidance;
- one N05 9 px / 10-frame settle-shake.

Technical execution:

- initial run `36297396556` failed at render because `react=19.2.4` and `react-dom=19.2.3` were mismatched;
- dependency versions were aligned to 19.2.4 / 19.2.4;
- successful run: `36297467856`;
- artifact: `P03_OPENING_V2_PROOF_REVIEW_V003`;
- artifact ID: `10924960913`;
- artifact digest: `sha256:cdafde226070f8eec26c71eec628d2107e1fca39fb4acd0d33ed952292d1dce4`;
- output MP4 SHA-256: `b6914ca1910ef0078876fc8063d079870df6927a4f1f2a7291ddf6d43ab4968f`;
- output byte size: `21,326,666`;
- output: 1080×1920 / H.264 yuv420p / 30 fps / 991 decoded frames / continuous AAC audio;
- full decode QC: PASS.

Next step is Product Owner contextual review. P0.3 remains IN PROGRESS; no final timing lock or Gate PASS is claimed.

## libopenshot Camera Motion Proof V001｜2026-09-27

Status: `TECHNICAL_RENDER_PASS / READY_FOR_PRODUCT_OWNER_MOTION_REVIEW / MOTION-ONLY SPIKE`

Purpose: compare libopenshot curve-based multi-keyframe camera motion against the current Remotion V003 approach before any full Opening V2 migration.

Scope:

- N08 — brief hold → accelerating architectural push → slight overshoot → settle
- N03 — pull-back + lateral observation drift → settle
- N05 — action push + directional reframe + brief settle-shake + micro rotation

Execution path:

`approved canonical PNGs → libopenshot Python bindings / Bezier keyframes → PNG frame sequence → FFmpeg H.264 MP4`

Technical evidence:

- first run `36298583006` failed with SIGSEGV because libopenshot Timeline stores raw clip pointers while Python/SWIG objects were garbage-collected;
- explicit keepalive references fixed the object lifetime issue;
- successful run: `36298639226`;
- artifact: `P03_LIBOPENSHOT_CAMERA_MOTION_PROOF_V001`;
- artifact ID: `10923993594`;
- artifact digest: `sha256:b8986b111a523d2d036dc53cab88d22c7952e9d544c7540fad37f5d08b8871bf`;
- output MP4 SHA-256: `4582f00d89a4df65497be3c1f1ba34801671c9fc8bc1b802519d61f05f141a88`;
- output byte size: `5,279,475`;
- output: 1080×1920 / H.264 yuv420p / 30 fps / 228 decoded frames / 7.600 sec;
- audio: NONE / motion-only spike;
- full decode QC: PASS.

This proof is not an Opening V2 edit, does not alter canonical Story Shots, and does not claim P0.3 PASS. Full Opening V2 migration is blocked on Product Owner review of whether the motion is meaningfully more cinematic than Remotion V003.

## Opening V2 libopenshot Full Proof V001｜2026-09-27

Status: `TECHNICAL_RENDER_PASS / READY_FOR_PRODUCT_OWNER_CONTEXTUAL_REVIEW / TIMING NOT LOCKED`

Chat designed the complete 12-shot cinematic motion plan and directly wrote the executable libopenshot spec/workflow. GitHub Actions rendered the complete Opening V2 proof.

Preserved:

- approved/current canonical Story Shot binaries;
- sequence: A01 → A02 → N06 → N02 → N07 → N03 → N04 → N08 → N09 → N10 → N05 → N01;
- Draft 01 timing: 991 frames / 30 fps / 33.033333 sec;
- continuous canonical source audio without speed change.

Director motion design:

- A01/N08: spatial attraction with hold → push → settle / overshoot;
- A02/N06/N07/N04/N09/N10: varied dialogue/portrait focus movement rather than one repeated template;
- N03: reaction pull-back + lateral drift + settle;
- N05: action peak using push + directional reframe + brief settle-shake + micro rotation;
- N01: quiet pull-back and fade.

Technical evidence:

- source commit: `f4fc68678fc52d71d0e82773f5f3372b67b9c01b`;
- successful run: `36299431486`;
- artifact: `P03_OPENING_V2_LIBOPENSHOT_FULL_PROOF_V001`;
- artifact ID: `10925078297`;
- artifact digest: `sha256:4f6545e1094344919330823e34d2e088bf78c2eabbf1d89d4e686547f6d1a6ab`;
- MP4 SHA-256: `e821b8a76af3bd5f6e7c776e81cc907f1873a3a7dc4f96173b2ceefe16972385`;
- MP4 byte size: `19,750,380`;
- output: 1080×1920 / H.264 yuv420p / 30 fps / 991 decoded frames / continuous AAC audio;
- full decode QC: PASS.

This remains a contextual review build. No final timing lock and no P0.3 Gate PASS are claimed.

## Editing Workflow Framework V1｜2026-09-27

Status: `ACTIVE / REFERENCE FRAMEWORK / NON-TEMPLATE`

Product Owner registered the V002 production logic as the reusable editing process reference under RC-026.

Reusable workflow:

`Canonical story/audio context → Chat director/edit design → contextual timeline → canonical input verification → engine implementation → scene-specific motion/transition treatment → continuous source-audio assembly where appropriate → GitHub Actions render/QC → full-context Product Owner review → targeted iteration`

Formal reference:

`docs/project_control/gates/P0_3_video_pipeline/editing_workflow_framework_v1.md`

Important boundary:

- V002 is a reference implementation, not a universal edit template;
- its 12-shot count, 991-frame map, cut points, motion values, transitions and Remotion implementation are not inherited automatically;
- every later edit must redesign timing, shot behavior and editorial treatment from the actual story/audio/action/space/emotional context;
- the render engine is an execution layer and may change;
- technical QC PASS never substitutes for full-context Product Owner artistic review or P0.3 approval.
