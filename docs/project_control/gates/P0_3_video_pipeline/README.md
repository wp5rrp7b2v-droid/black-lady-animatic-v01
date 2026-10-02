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

## Opening V001 Product Owner Approval + Canonical Archive｜2026-09-27

Status: `PRODUCT_OWNER APPROVED / CANONICAL MASTER ARCHIVED / LOCKED`

The Product Owner explicitly approved the uploaded `P03_OPENING_V2_PROOF_REVIEW_V002.mp4` as the formal Opening video.

Canonical master:

- video ID: `OPENING_V001`
- path: `production/video/approved/opening/P03_OPENING_V2_APPROVED_V001.mp4`
- SHA-256: `70d7922244161dd216a26446fd75531db20eea0ac7fc25f567f6ff14e2746e3a`
- byte size: `18892138`
- Git blob: `9b4ef42d9eceb5d7f1eb190d508d6749ccf4b70e`
- publication commit: `208566291a5531cb34ad05e50e56e0a9fcc51c02`
- archive verification run: `36300993520`
- archive receipt artifact ID: `10925990918`
- exact V002 binary / no re-encode
- remote binary verification: PASS

The uploaded attachment independently matched the historical V002 output and passed full media decode.

Selection result:

- V002 = selected / approved Opening master;
- V003 and libopenshot variants = retained as historical technical/artistic evidence, not selected masters.

Formal closeout:

`docs/project_control/gates/P0_3_video_pipeline/opening_v001_approval_closeout_2026-09-27.md`

Important: this selection is specific to the Opening result. RC-026 remains active: future edits reuse the process framework, not V002's exact timing/effects/template.

P0.3 remains `IN PROGRESS / NOT YET VALIDATED`; the next task is post-Opening story/audio breakdown and sequence-specific production design.

## S02-A Shot Plan V0.1｜2026-09-27

Status: `PRODUCT OWNER APPROVED / STORY SHOT PRODUCTION NEXT`

Approved structure:

`N11 NEW → N12 NEW → A04 REUSE → N13 NEW → N15 NEW → A05 REUSE`

Production count:

- 4 new Story Shots: N11 / N12 / N13 / N15
- 2 reused approved Story Shots: A04 / A05

Narrative lock:

- A05 owns the explicit reveal that Neil's waist is empty / no keys are present.
- N13 and N15 may build visual attention and suspense around the waist/key-holder hypothesis but must not reveal the answer early.
- Shot functions are approved; final cut frames are not yet locked.

Formal plan:

`docs/project_control/gates/P0_3_video_pipeline/s02_a_shot_plan_v0_1.md`

Current task:

`N11｜Neil Abnormal Portrait｜Director Shot Design V0`

Design path:

`docs/project_control/gates/P0_3_video_pipeline/n11_director_shot_design_v0.md`

N11 generation is not authorized until Product Owner approves the Director Shot Design.

## N11 Director Design V0.1 + Bundle Design V0.1｜2026-09-27

N11 Director Shot Design V0.1 status:

`PRODUCT OWNER APPROVED`

Locked correction:

- Neil has already crossed the threshold;
- he waits on the interior side of the open entrance;
- he faces outward toward the arriving guests;
- N11 is an observational medium close-up, not another welcome/action shot.

Approved design:

`docs/project_control/gates/P0_3_video_pipeline/n11_director_shot_design_v0_1.md`

Reference Delivery Bundle Design V0.1 status:

`DRAFT / PRODUCT OWNER REVIEW / NOT YET BUILT`

Proposed six-reference set:

- Neil FACE_FRONT;
- Neil FACE_3Q_LEFT;
- Neil BODY_FRONT;
- Castle Entrance Scene Master DAY/DOOR_OPEN;
- N01 immediate previous Opening end-state continuity;
- A03 interior-side entrance spatial continuity.

N09 is excluded because its story state places Neil outside the threshold. N05 is excluded from the baseline because N01 is the more immediate end-state reference; N05 may be added only if generation later shows spatial regression.

Bundle design:

`docs/project_control/gates/P0_3_video_pipeline/n11_reference_delivery_bundle_design_v0_1.md`

No temporary workflow, artifact build, Work generation, or N11 Story Shot registration has been authorized yet.

## N11 Reference Delivery Bundle V001｜Built 2026-09-27

Status: `BUILT / 6 OF 6 EXACT VERIFICATION PASS / READY FOR WORK GENERATION`

Product Owner approved Bundle Design V0.1. Chat then executed the existing locked RC-022 / RC-023 delivery path directly through GitHub Actions.

- workflow: `.github/workflows/p03-n11-reference-delivery-bundle-v001.yml`
- source commit: `ac83d41398f8fe7d6f3ef0ef24ca1921e8804909`
- run: `36303103682`
- job: `108574387646`
- artifact: `N11_REFERENCE_DELIVERY_BUNDLE_V001`
- artifact ID: `10925624760`
- artifact digest: `sha256:f2bba3b9dcb3a064c20b4cdc2267d8bc7862ec9c8d9f20d700ae6b5715aa2c4f`
- exact verification: `6/6 PASS`
- Product Owner manual reference upload: `0`

Build record:

`docs/project_control/gates/P0_3_video_pipeline/n11_reference_delivery_bundle_v001_build_record_2026-09-27.md`

Next:

`Work automatic artifact acquisition + revalidation → generate N11 Candidate 01 only → Product Owner review`

Do not start N12 or register N11 before N11 Candidate 01 is explicitly approved.

## N11 Redesign V0.2｜2026-09-27

Status: `DIRECTOR SHOT DESIGN V0.2 / PRODUCT OWNER REVIEW`

Reason for redesign:

- prior N11 attempts over-weighted the “inside doorway” constraint;
- composition widened into doorway / architectural portraiture;
- Neil became too formal / ceremonial;
- cross emphasis increased and consumed N12's narrative function.

V0.2 resets the composition while preserving the narrative beat.

Key locks:

- upper-chest-up tight medium close-up;
- Neil face is dominant;
- Neil is inside the threshold, but the spatial proof is subtle;
- use one-sided door-edge foreground occlusion, not a full doorway;
- cross preferably not visible;
- no hands / waist / floor / steps / full threshold;
- no failed N11 candidate may be used as reference.

Proposed Bundle V002:

Neil FACE_FRONT + FACE_3Q_LEFT + BODY_FRONT + Castle Entrance Scene Master + N01.

A03 is removed from the baseline.

Design:

`docs/project_control/gates/P0_3_video_pipeline/n11_director_shot_design_v0_2.md`

No Bundle V002 or generation authorized yet.

## N11 Reference Delivery Bundle V002｜Built 2026-09-27

Status: `BUILT / 5 OF 5 EXACT VERIFICATION PASS / READY FOR WORK GENERATION`

Product Owner approved N11 Director Shot Design V0.2 and Bundle V002.

Chat executed the locked RC-022 / RC-023 path directly; Codex and Local Terminal were not introduced.

- workflow: `.github/workflows/p03-n11-reference-delivery-bundle-v002.yml`
- source commit: `e2b8568f20ba8ee4e044a725d56624e6cbd9b733`
- run: `36305485637`
- job: `108581173489`
- artifact: `N11_REFERENCE_DELIVERY_BUNDLE_V002`
- artifact ID: `10927315457`
- artifact digest: `sha256:a00cb07e9875afd5f63b1303c8722955d8cf25800aab4990946c5dc9f2df2b7e`
- exact verification: `5/5 PASS`
- manual Product Owner reference upload: `0`
- explicit exclusions: A03 / N05 / N09 / all failed N11 candidates

Build record:

`docs/project_control/gates/P0_3_video_pipeline/n11_reference_delivery_bundle_v002_build_record_2026-09-27.md`

Next:

`Work automatic artifact acquisition + revalidation → fresh N11 Rebuild Candidate 01 → Product Owner review`

## N11 Rebuild Candidate 01 Review｜2026-09-27

Status: `NOT FINAL APPROVED / TARGETED EDIT TO CANDIDATE 02 AUTHORIZED`

Product Owner review:

Accepted and must be preserved:

- Neil identity;
- inside-door spatial relationship;
- single-side doorway cue;
- closed-mouth waiting state;
- no cross emphasis;
- dark subordinate interior background.

Needs correction:

1. tighten to true upper-chest-up framing;
2. reduce warm/red healthy skin tone and establish natural pallor.

Boundary:

- Candidate 02 is a targeted edit of Candidate 01;
- do not fully regenerate;
- do not move Neil deeper inside;
- do not change expression, identity, costume or background structure;
- do not reintroduce cross, hands, waist, floor, steps or full doorway.

## N12 Director Shot Design V0.1｜2026-09-27

Status: `DRAFT / PRODUCT OWNER REVIEW`

Before N12:

- Product Owner clarified N11 Rebuild Candidate 01 is **overall approved**.
- The prior “targeted Candidate 02 edit” interpretation is superseded.
- N11 will be archived / registered later together with the later S02-A approved shots.

N12 function:

`cross + rigid closed-mouth smile detail`

Key director locks:

- medium close-up / head + upper chest;
- Neil remains inside the open entrance, facing outward and waiting;
- cross is clearly visible but secondary to Neil's face;
- smile is small, closed-mouth, socially polite but emotionally rigid;
- no teeth / broad grin / villain smirk;
- no hands / waist / action;
- pallor remains continuous from N11;
- no religious-symbol hero shot or horror-poster treatment.

Design:

`docs/project_control/gates/P0_3_video_pipeline/n12_director_shot_design_v0_1.md`

## N12 Reference Delivery Bundle Design V0.1｜2026-09-27

Status: `DRAFT / PRODUCT OWNER REVIEW`

Proposed reference set:

- Neil FACE_FRONT;
- Neil FACE_3Q_LEFT;
- Neil BODY_FRONT;
- Castle Entrance Scene Master;
- N01 post-Opening inside-threshold continuity.

Explicit exclusions:

- N11 approved candidate: not yet canonically published because batch archival is deferred;
- N09: exterior-platform state conflict;
- N10: exterior subtle-smile state may bias both space and expression.

No standalone cross Prop Asset is required for V001; source narration + Director lock authorizes a simple realistic metallic cross in this Story Shot.

Bundle design:

`docs/project_control/gates/P0_3_video_pipeline/n12_reference_delivery_bundle_design_v0_1.md`

No workflow, artifact build or N12 generation yet.

## N12 Reference Delivery Bundle V001｜Built 2026-09-27

Status: `BUILT / 5 OF 5 EXACT VERIFICATION PASS / READY FOR WORK GENERATION`

Product Owner approved Bundle Design V0.1. Chat executed the existing locked RC-022 / RC-023 delivery path directly through GitHub Actions.

- workflow: `.github/workflows/p03-n12-reference-delivery-bundle-v001.yml`
- source commit: `45d1dd4da22f1c30f4131d57cafa9a51f6d6b42d`
- run: `36307403582`
- job: `108586621481`
- artifact: `N12_REFERENCE_DELIVERY_BUNDLE_V001`
- artifact ID: `10927392671`
- artifact digest: `sha256:e035ffc7d0f965b389e6e21054d5b7a63c1b31e5ef1e13f0242eb810320e70ed`
- exact verification: `5/5 PASS`
- Product Owner manual reference upload: `0`

Build record:

`docs/project_control/gates/P0_3_video_pipeline/n12_reference_delivery_bundle_v001_build_record_2026-09-27.md`

Next:

`Work automatic artifact acquisition + revalidation → generate N12 Candidate 01 only → Product Owner review`

Do not register Story Shot or batch-archive before N12 Candidate 01 is explicitly approved.

## S02-A N11 + N12 Approval Checkpoint｜2026-09-27

Status: `PRODUCT OWNER APPROVED / BATCH ARCHIVAL DEFERRED`

Final creative selections:

- N11 = `Candidate 03`
  - visible metal chain;
  - cross pendant hidden by waistcoat/clothing;
  - earlier N11 Candidate 01/02 are not final and must not be batch-archived.
- N12 = `Candidate 02`
  - rigid closed-mouth smile;
  - one clearly readable metallic cross;
  - Candidate 01 superseded.

Formal binary publication / Story Shot registration is intentionally deferred until the later S02-A batch archival pass.

Approval checkpoint:

`docs/project_control/gates/P0_3_video_pipeline/s02_a_n11_n12_approval_checkpoint_2026-09-27.md`

Next:
`N13 Director Shot Design`

## N13 Bundle Build Preparation｜2026-09-27

Status: `DESIGN APPROVED / BUILD PREP READY / NOT YET BUILT`

Narrative lock:

`move attention toward Neil's waist without revealing that it is empty`

Reference set:

- Neil FACE_FRONT;
- Neil FACE_3Q_LEFT;
- Neil BODY_FRONT;
- Castle Entrance Scene Master;
- N01 inside-threshold continuity.

Excluded:

- unpublished N11 Candidate 03;
- unpublished N12 Candidate 02;
- N09 / N10;
- A05 reveal shot;
- all rejected / superseded candidates.

Documents:

- `docs/project_control/gates/P0_3_video_pipeline/n13_director_shot_design_v0_1.md`
- `docs/project_control/gates/P0_3_video_pipeline/n13_reference_delivery_bundle_design_v0_1.md`
- `docs/project_control/gates/P0_3_video_pipeline/n13_reference_delivery_bundle_v001_build_prep.md`

Next:
`Product Owner build authorization → GitHub Actions real build → 5/5 verification → Work N13 Candidate 01`

## N13 Reference Delivery Bundle V001｜Built 2026-09-27

Status: `BUILT / 5 OF 5 EXACT VERIFICATION PASS / READY FOR WORK GENERATION`

- workflow: `.github/workflows/p03-n13-reference-delivery-bundle-v001.yml`
- source commit: `bdd2480fb995462f89ea51400d02b0135912ce42`
- run: `36314032099`
- job: `108605228883`
- artifact: `N13_REFERENCE_DELIVERY_BUNDLE_V001`
- artifact ID: `10930326122`
- artifact digest: `sha256:0b40fd3e34b18297c679c2e307f2e4d6480e90c2eef1697adcbdd8b15d8d6fb7`
- artifact size: `12637035` bytes
- exact verification: `5/5 PASS`
- Product Owner manual reference upload: `0`

Build record:

`docs/project_control/gates/P0_3_video_pipeline/n13_reference_delivery_bundle_v001_build_record_2026-09-27.md`

Narrative protection remains locked:

- N13 guides attention toward the waist;
- no keys;
- no obvious "no keys";
- no clean full-waist answer-zone;
- A05 owns the reveal.

Next:

`Work automatic artifact acquisition + revalidation → N13 Candidate 01 → Product Owner review`

## S02-A Shot Plan V0.2 + N14 Design｜2026-09-27

Status: `SHOT PLAN V0.2 PRODUCT OWNER APPROVED / N14 DESIGN IN REVIEW`

Revised sequence:

`N11 → N12 → A04 → N14 → N15 → A05`

Changes:

- N13 cancelled as a formal Story Shot; its Bundle/Candidate remain historical evidence only and must not be registered.
- N14 = prior-experience judgment: the first person encountered after entering a Blood Door is often important.
- N15 = butler-role inference + likely key-holder hypothesis.
- no N16.
- A05 retains the waist-check / no-keys reveal.

Documents:

- `docs/project_control/gates/P0_3_video_pipeline/s02_a_shot_plan_v0_2.md`
- `docs/project_control/gates/P0_3_video_pipeline/n14_director_shot_design_v0_1.md`

Next:
`Product Owner review of N14 Director Shot Design V0.1`

## N14 Reference Delivery Bundle Design V0.1｜2026-09-27

Status: `DIRECTOR DESIGN PRODUCT OWNER APPROVED / BUNDLE DESIGN IN REVIEW / NOT YET BUILT`

Director lock:

- Ning Qiushui primary;
- tight / medium close-up;
- shallow depth of field;
- calm / experienced / analytical;
- Neil only as a soft out-of-focus referent;
- no keys / waist / key-holder inference.

Proposed five-reference bundle:

`A04 + AST_IMG_000034 + AST_IMG_000032 + AST_IMG_000026 + AST_IMG_000052`

Document:

`docs/project_control/gates/P0_3_video_pipeline/n14_reference_delivery_bundle_design_v0_1.md`

Next:
`Product Owner review → Build Prep`

## N14 Reference Delivery Bundle V001｜Built 2026-09-27

Status: `BUILT / 5 OF 5 EXACT VERIFICATION PASS / READY FOR WORK GENERATION`

- workflow: `.github/workflows/p03-n14-reference-delivery-bundle-v001.yml`
- source commit: `ae34a3a5722473f1888d23db2f1f9a596f6978bb`
- run: `36317403211`
- job: `108614612409`
- artifact: `N14_REFERENCE_DELIVERY_BUNDLE_V001`
- artifact ID: `10931321832`
- artifact digest: `sha256:40236e5e4d33f1d0a5b76eef455ff51ca688238fef42fdb054987ecc60bc317a`
- artifact size: `12618491` bytes
- exact verification: `5/5 PASS`
- A04 computed SHA-256: `8111a2d80bb68efe99bc723d197a580b5bfed3d64a1ffeb3848db9260bb50398`
- Product Owner manual reference upload: `0`

Build prep:

`docs/project_control/gates/P0_3_video_pipeline/n14_reference_delivery_bundle_v001_build_prep.md`

Build record:

`docs/project_control/gates/P0_3_video_pipeline/n14_reference_delivery_bundle_v001_build_record_2026-09-27.md`

Next:

`Work automatic artifact acquisition + revalidation → N14 Candidate 01 → Product Owner review`

## N14 Candidate 01 Approval + N15 Director Design｜2026-09-27

N14 status:

`PRODUCT OWNER APPROVED / FINAL CREATIVE SELECTION / PENDING BATCH ARCHIVAL`

Approved binary identity:

- dimensions: `941 × 1672`
- bytes: `2500282`
- SHA-256: `0474003a1d6d48a652935033f17560d0ee1d689caadbdb7d4af72560477844f1`

Approval checkpoint:

`docs/project_control/gates/P0_3_video_pipeline/s02_a_n14_approval_checkpoint_2026-09-27.md`

N15 status:

`DIRECTOR SHOT DESIGN V0.1 / PRODUCT OWNER REVIEW`

Narrative function:

`butler role → plausible key-holder hypothesis`

Design path:

`docs/project_control/gates/P0_3_video_pipeline/n15_director_shot_design_v0_1.md`

Critical boundary:

- no visible keys;
- no clean waist exposure;
- no empty-waist conclusion;
- A05 retains exclusive reveal authority.

## N11 / N12 / N14 Story Shot Registration Closeout｜2026-09-27

Status: `COMPLETE / RC-024 FOUR GATES PASS`

- correct source upload commit: `ebe1361664f27dd1fa17b866e0d529f7128abf46`
- upload verification run: `36324358350` / PASS
- upload verification artifact: `10933591429`
- canonical exact-blob publication commit: `caff3cef027366b75e2ced5b04f363ed6a89b5f6`
- Story Shot Index registration commit: `f301eff807434552e52d78070a8d06e492c1ae06`
- registration verification run: `36324545377` / PASS
- registration verification artifact: `10933043856`
- result: `N11_PASS / N12_PASS / N14_PASS / INDEX_MATCH=YES / STAGING_CLEANUP_PASS / OVERALL_RESULT=PASS`
- registered Story Shot count: `20`
- N13: `CANCELLED / NOT REGISTERED`

Closeout:

`docs/project_control/gates/P0_3_video_pipeline/s02_a_n11_n12_n14_story_shot_registration_closeout_2026-09-27.md`

Next session:

`source novel key / escape-door fact check → revise N15 Director Shot Design`

## S02-A Assembly V001 Formal Closeout｜2026-09-28

Status: `PRODUCT_OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED / FORMALLY CLOSED`

Final sequence:

`N11 → N12 → A04 → N14 → N15 → A05`

Canonical audio:

`00:33.020 → 01:18.750` / `45.730s`

Canonical video:

`production/video/approved/s02_a/S02_A_ASSEMBLY_APPROVED_V001.mp4`

Formal identity:

- Video ID: `S02_A_ASSEMBLY_V001`
- SHA-256: `937008e11d20892ea0a17be64719a19cb131d174871930bc29004a678bb58ed1`
- Git blob: `bcd3fef7a8d600c95cb4d7242d411cc0df41859c`
- byte size: `6822004`
- media: `942×1672 / 30fps / H.264 yuv420p / AAC 48kHz stereo / 45.730s`

Completion evidence:

- Exact Binary Verification run `36427746113`: PASS
- Canonical Publication run `36428710030`: PASS
- Publication commit `e577cd09c5ba333b7659dc08bc0898a5596edbb5`
- Video Index registration commit `ed99eba7b780f6455323d035fdb4148f5c465dc1`
- Registration Verification run `36430256742`: PASS
- Decision `BL-D-077`
- Formal closeout: `s02_a_assembly_v001_formal_closeout_2026-09-28.md`

Current P0.3 boundary:

- S02-A is complete and no longer active.
- N13 remains cancelled / historical evidence only.
- P0.3 remains `IN PROGRESS / NOT YET VALIDATED`.
- No P0.3 PASS is claimed.
- Next sequence starts after canonical audio `01:18.750`, only after Product Owner authorization.

## EOD Resume Point｜2026-09-28

Daily closeout:

`docs/project_control/gates/P0_3_video_pipeline/p0_3_daily_closeout_2026-09-28.md`

Resume next session from:

`post-01:18.750 narrative/audio breakdown → next sequence Director Design`

Do not reopen S02-A unless Product Owner explicitly authorizes a revision.



## S02-B Current Active State｜2026-09-30 EOD

Status:

`S02-B ACTIVE / N21 TASK-SCOPE SIMPLIFICATION PENDING / C04 NOT AUTHORIZED`

Formally closed Story Shots:

`N16 / N17 / N18 / N19 / N20`

Current registered Story Shot count:

`26`

N21 current facts:

- Director Shot Design V0.1: Product Owner approved / locked;
- Scene Reference Design V0.3: Product Owner approved / locked, production use paused pending scope review;
- Bundle V002: technically valid `2/2 PASS`, Artifact ID `11088797193`, further use paused;
- Candidate 01: not accepted;
- Candidate 02: not accepted;
- Candidate 03: not accepted;
- Candidate 04: not authorized;
- N22: not started.

Current blocker:

`RISK-003 / MULTI-PERSON GENERATION TRADEOFF: CROWD COMPOSITION / ATMOSPHERE / CHARACTER IDENTITY / BODY PERFORMANCE`

Resume next session from:

`N21 TASK-SCOPE SIMPLIFICATION / DIRECTOR STRATEGY REVIEW`

Do not generate Candidate 04 before the revised N21 single-frame responsibility is explicitly locked.


## N21 Scene Reference V0.4｜2026-10-01

Status:

`PRODUCT OWNER APPROVED / LOCKED`

N21 responsibility is now simplified to:

`THRESHOLD TRANSITION + UNKNOWN-SPACE MOOD`

Current locks:

- 16 participants remain a canonical story fact but are not a single-frame counting requirement;
- approximately 4–6 readable figures are sufficient;
- Ning / Jun are not mandatory identity targets and must not dominate;
- character visual style continuity is a hard Director gate;
- proposed next Bundle formal references are `AST_IMG_000052 + N03_VISITOR_REACTION_APPROVED_V001.png`;
- N20 is Director continuity review only, not a proposed formal generation input;
- Bundle V002 remains technically valid but its creative scope is superseded;
- Candidate 04 remains NOT AUTHORIZED;
- N22 remains NOT STARTED;
- RISK-003 remains ACTIVE pending candidate evidence and Product Owner approval.

Design authority:

`docs/project_control/gates/P0_3_video_pipeline/n21_scene_reference_design_v0_4.md`

Next:

`N21_REFERENCE_DELIVERY_BUNDLE_V003 DESIGN`

Do not build Bundle V003 or generate Candidate 04 before separate Product Owner approval of the Bundle design.


## N21 Reference Delivery Bundle V003｜2026-10-01

Status:

`VERIFIED / 2 OF 2 PASS / GENERATION_ALLOWED=TRUE / READY FOR WORK GENERATION`

- Run: `36817339701`
- Job: `110225166295`
- Artifact: `11141917821`
- Digest: `sha256:8be16a3538394046d1a875ff6a5e4802dd097bd52c44e8efd863af8807d9eaa0`
- Formal inputs: `AST_IMG_000052 + N03`
- Independent verification: `2/2 PASS`
- Manual PO upload: `0`
- Candidate 04: `AUTHORIZED FOR WORK CLEAN REGENERATION`
- N22: `NOT STARTED`
- RISK-003: `ACTIVE / REAL CANDIDATE EVIDENCE REQUIRED`

Next:

`Work → N21 Candidate 04 only → Product Owner review`


## N21 Candidate 04 Review｜2026-10-01

Status:

`NOT APPROVED / REFERENCE CONTENT LEAKAGE`

- Candidate 04 used verified Bundle V003; technical transport / exact-binary integrity remained valid.
- Human visual quality and body stability improved relative to Candidate 03.
- Main failure: N03 as a complete Story Shot style input leaked concrete wardrobe / figure configuration into the new render.
- Bundle V003 is therefore `TECHNICALLY VALID / CREATIVE REFERENCE STRATEGY FAILED`.
- N03 must not be reused as N21 formal style-generation input.
- Candidate 05 remains `NOT AUTHORIZED`.
- RISK-003 remains `ACTIVE`.
- Product Owner approved next step: `Character Visual Style Reference V0.1｜Design`.

Review record:

`docs/project_control/gates/P0_3_video_pipeline/n21_candidate_04_review_2026-10-01.md`


## Character Visual Style Reference V001｜Exact Crop Plan｜2026-10-01

Status:

`PRODUCT OWNER APPROVED / EXACT 6-PANEL CROP PLAN LOCKED / BUILD PREP READY / NOT YET BUILT`

- Source inspection: run `36820797772` / Artifact `11143985053` / 6 of 6 PASS.
- Machine crop plan: `production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.crop_plan.json`.
- Board: `1536×1024` landscape / 3×2 / neutral gray / no labels.
- Sources: Guang Yong, Su Xiaoxiao, Liao Jian, Wen Qingya Atomic assets only.
- Ning / Jun, complete Story Shots and Character Reference Sheets remain excluded.
- No generative processing is permitted.
- Formal builder must be deterministic and prove identical SHA-256 across two runs before publication.
- Candidate 05 remains `NOT AUTHORIZED`.

Build-prep record:

`docs/project_control/gates/P0_3_video_pipeline/character_visual_style_reference_v001_exact_crop_plan_and_build_prep_2026-10-01.md`

Next:

`Product Owner authorization → deterministic builder implementation + two-run proof`


## Character Visual Style Reference V001｜Two-Run Proof｜2026-10-01

Status:

`TECHNICAL DETERMINISM PASS / DIRECTOR VISUAL PREFLIGHT PASS / PRODUCT OWNER VISUAL REVIEW REQUIRED`

- workflow run: `36822615026`
- job: `110241244661`
- artifact: `CHARACTER_VISUAL_STYLE_REFERENCE_V001_TWO_RUN_PROOF`
- artifact ID: `11143724172`
- artifact digest: `sha256:91d93bcccceafb5ef47eca5dd6d8f91054e84f87f755785ee2581638f4af55ef`
- Python: `3.12.14`
- Pillow: `11.3.0`
- Run A / B output SHA-256: `8d650483b6e082a80d41d93e14c7957595c451097aac63f3c84cbcc1ddc7ce41`
- Run A / B bytes: `1301730`
- SHA / byte-size / direct byte identity: `PASS`
- independent verification: `PASS`
- canonical publication: `NOT AUTHORIZED`
- Candidate 05: `NOT AUTHORIZED`

Build record:

`docs/project_control/gates/P0_3_video_pipeline/character_visual_style_reference_v001_two_run_build_record_2026-10-01.md`

Next:

`Product Owner visual review of the deterministic Style Board`


## Character Visual Style Reference V001｜PO Visual Approval｜2026-10-01

Status:

`PRODUCT OWNER APPROVED / EXACT BINARY IDENTITY LOCKED / CANONICAL PUBLICATION NEXT`

- dimensions: `1536×1024`
- mode / format: `RGB / PNG`
- byte size: `1301730`
- SHA-256: `8d650483b6e082a80d41d93e14c7957595c451097aac63f3c84cbcc1ddc7ce41`
- proof run: `36822615026`
- proof Artifact: `11143724172`
- authority: `STYLE ONLY / NO NAMED IDENTITY / NO SHOT CONTENT`
- canonical publication: `PENDING`
- Candidate 05: `NOT AUTHORIZED`

Approval record:

`docs/project_control/gates/P0_3_video_pipeline/character_visual_style_reference_v001_po_visual_approval_2026-10-01.md`

Next:

`Exact-binary canonical publication + post-publication verification`


## Character Visual Style Reference V001｜Canonical Publication｜2026-10-01

Status:

`PRODUCT OWNER APPROVED / CANONICAL PUBLISHED / REMOTE EXACT-BINARY VERIFIED`

- canonical PNG: `production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.png`
- canonical manifest: `production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.manifest.json`
- publication run: `36823958149`
- publication job: `110245367477`
- publication commit: `36f146655fa9334d399fd3369f267dd406963ab2`
- dimensions: `1536×1024`
- bytes: `1301730`
- SHA-256: `8d650483b6e082a80d41d93e14c7957595c451097aac63f3c84cbcc1ddc7ce41`
- Git blob: `216b1739db17cb3b183d613e4aefa6374d1088e2`
- post-publication remote verification: `PASS`
- proof Artifact: `11144775274`
- RISK-003: `ACTIVE`
- Candidate 05: `NOT AUTHORIZED`

Closeout:

`docs/project_control/gates/P0_3_video_pipeline/character_visual_style_reference_v001_canonical_publication_closeout_2026-10-01.md`

Next:

`CONTROLLED_REFERENCE Delivery Support + N21 Bundle V004 Design`


## CONTROLLED_REFERENCE + N21 Bundle V004 Design｜2026-10-01

Status:

`PRODUCT OWNER APPROVED / LOCKED / IMPLEMENTATION NOT YET AUTHORIZED`

Formal V004 reference set:

1. `AST_IMG_000052` — spatial authority only
2. `CHARACTER_VISUAL_STYLE_REFERENCE_V001` — human visual-style authority only

Explicitly excluded:

- N03
- N20
- all named-character Character Sheets
- A07
- N21 Candidate 01–04

CONTROLLED_REFERENCE must validate canonical PNG + sidecar manifest + approval/lifecycle/authority + SHA/bytes/Git blob + PNG readability + byte-identical artifact copy.

Candidate 05 remains `NOT AUTHORIZED`.

Design:

`docs/project_control/gates/P0_3_video_pipeline/controlled_reference_delivery_and_n21_bundle_v004_design_v0_1.md`

Next:

`Product Owner authorization → CONTROLLED_REFERENCE Builder Support + N21 Bundle V004 Spec / Build Preparation`


## N21 Reference Delivery Bundle V004｜Support + Spec｜2026-10-01

Status:

`CONTROLLED_REFERENCE SUPPORT COMPLETE / SPEC LOCKED / VALIDATION-ONLY 2 OF 2 PASS / FORMAL BUILD NOT AUTHORIZED`

- spec: `production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V004.json`
- spec revision: `V004-R2`
- build gate: `build_authorized=false`
- formal refs: `AST_IMG_000052 + CHARACTER_VISUAL_STYLE_REFERENCE_V001`
- validation-only run: `36826494510`
- job: `110253232876`
- result: `2/2 PASS`
- generation: `GENERATION_ALLOWED=FALSE`
- build: `SKIPPED`
- Artifact upload: `SKIPPED`
- historical pre-gate Artifact `11144634603`: `DO NOT USE`
- Candidate 05: `NOT AUTHORIZED`

Corrected boundary record:

`docs/project_control/gates/P0_3_video_pipeline/n21_reference_delivery_bundle_v004_build_prep_2026-10-01.md`

Next:

`Product Owner authorization → Formal N21 V004 Build + Exact Verification`


## N21 Reference Delivery Bundle V004｜Formal Build｜2026-10-01

Status:

`FORMAL / 2 OF 2 PASS / INDEPENDENTLY VERIFIED / GENERATION_ALLOWED=TRUE / CANDIDATE 05 AUTHORIZATION NEXT`

- spec: `V004-R3`
- build gate: `true`
- formal run: `36826967264`
- job: `110254694293`
- formal Artifact: `11145497260`
- Artifact size: `3596063 bytes`
- Artifact digest: `sha256:0b3227f30d8156ed7be3f421f5b43d9233aba4fc609dedd09d76f4f1dc0ea27d`
- builder result: `2/2 PASS / GENERATION_ALLOWED=TRUE`
- independent ZIP digest: `MATCH`
- independent manifest / both PNG exact identities: `PASS`
- historical pre-gate Artifact `11144634603`: `DO NOT USE`
- Candidate 05: `NOT YET AUTHORIZED`

Build record:

`docs/project_control/gates/P0_3_video_pipeline/n21_reference_delivery_bundle_v004_build_record_2026-10-01.md`

Next:

`Product Owner authorization → N21 Candidate 05 Work generation`


## N21 Candidate 05｜Work Generation Authorization｜2026-10-01

Status:

`PRODUCT OWNER AUTHORIZED / ONE PNG ONLY / PRODUCT OWNER REVIEW NEXT`

- mode: `CLEAN REGENERATION`
- formal Bundle: `N21_REFERENCE_DELIVERY_BUNDLE_V004`
- formal Artifact: `11145497260`
- Bundle exact verification: `2/2 PASS`
- Bundle-level `GENERATION_ALLOWED=TRUE`
- Work must independently revalidate before generation.
- Candidate 01–04 are not generation inputs.
- Generate exactly one PNG and stop.
- Candidate 06: `NOT AUTHORIZED`
- N22: `NOT STARTED`

Authorization:

`docs/project_control/gates/P0_3_video_pipeline/n21_candidate_05_work_generation_authorization_2026-10-01.md`

Next:

`N21 Candidate 05 Product Owner Review`


## N21 Candidate 05 / 06 Review｜2026-10-01

Status:

`CANDIDATE 05 NOT APPROVED / CANDIDATE 06 NOT APPROVED / CANDIDATE 07 NOT AUTHORIZED`

- C05: style mitigation improved; queue / expedition-team feel remained.
- C06: entrance larger and bags removed, but became over-monumental / too brightly daylit; color-light continuity and crowd staging still failed.
- V004: remains technically valid.
- RISK-003: `ACTIVE`.
- N22: `NOT STARTED`.

Review:

`docs/project_control/gates/P0_3_video_pipeline/n21_candidate_05_06_review_2026-10-01.md`

Next:

`Director Strategy Review before Candidate 07`


## N21 Director Strategy Review｜Before Candidate 07｜2026-10-01

Status:

`DIRECTOR RECOMMENDATION LOCK / PRODUCT OWNER REVIEW REQUIRED / CANDIDATE 07 NOT AUTHORIZED`

Key finding:

- N20 = preferred tonal / lighting continuity authority.
- AST_IMG_000052 remains canonical scene-fact authority but is not recommended as a direct C07 generation image because its centered bright-sky doorway can overdrive monumental / daylight-heavy results.
- Do not keep adding prompt rules to V004.
- Recommended next asset: `N21_ENVIRONMENT_CONTINUITY_REFERENCE_V001` built deterministically from environment-only Scene Master + N20 crops.
- Future C07: partial off-axis large doorway, interior-side oblique camera, dim warm N20-like world, staggered non-queue crowd, upright bodies, no bags.
- V004 remains technically valid; Candidate 07 remains `NOT AUTHORIZED`.

Review:

`docs/project_control/gates/P0_3_video_pipeline/n21_director_strategy_review_before_candidate_07_2026-10-01.md`

Next:

`Product Owner review → N21_ENVIRONMENT_CONTINUITY_REFERENCE_V001 Design`


## N21 Threshold Transition Environment Reference V001｜Formal Closeout｜2026-10-01

Status:

`PRODUCT OWNER APPROVED / CANONICAL / EXACT VERIFIED / CLOSED`

- reference: `N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001`
- classification: `P0.3_CONTROLLED_PRODUCTION_REFERENCE`
- authority: `N21_THRESHOLD_TRANSITION_ENVIRONMENT_ONLY`
- canonical PNG: `production/environment_references/n21_threshold_transition/N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001.png`
- canonical manifest: `production/environment_references/n21_threshold_transition/N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001.manifest.json`
- exact identity: `941x1672 / RGBA / 3394494 bytes / SHA-256 dd1b2dc6...9a4f13 / blob 35805794...20fc8`
- publication commit: `7108530b3bbed4bf01aac73c164978210545e4a9`
- verification run: `36857195935` / job `110352417813` / `EXACT_BINARY_MATCH=YES`
- not a Story Shot; not a primary Scene Master; not a strict reverse-angle reconstruction; does not replace `AST_IMG_000052`.
- no P0.2 Asset Registry schema extension.

Closeout:

`docs/project_control/gates/P0_3_video_pipeline/n21_threshold_transition_environment_reference_v001_closeout_2026-10-01.md`

Next:

`N21_REFERENCE_DELIVERY_BUNDLE_V005 DESIGN`


## N21 Reference Delivery Bundle V005｜Design V0.1｜2026-10-01

Status:

`DIRECTOR DESIGN COMPLETE / PRODUCT OWNER REVIEW REQUIRED / BUILD NOT AUTHORIZED`

Proposed formal inputs:

1. `N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001` — environment / threshold / lighting / tonal authority only.
2. `CHARACTER_VISUAL_STYLE_REFERENCE_V001` — human visual-style authority only.

Excluded from direct generation input:

- `AST_IMG_000052`
- N20
- all complete Story Shots
- all complete Scene Masters
- named-character sheets
- N21 Candidate 01–06

Next:

`Product Owner review → V005 Spec + validation-only prep`

Candidate 07 remains `NOT AUTHORIZED`.


## N21 Reference Delivery Bundle V005｜Approval + Validation-Only｜2026-10-01

Status:

`PRODUCT OWNER APPROVED / SPEC CREATED / VALIDATION 2 OF 2 PASS / FORMAL BUILD NOT AUTHORIZED`

- spec: `production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V005.json`
- spec commit: `e05b5cefb1be29b5724c4bf782f149a99d2c040c`
- validation run: `36859052785`
- job: `110358458769`
- exact validation: `2/2 PASS`
- `BUILD_AUTHORIZED=FALSE`
- `GENERATION_ALLOWED=FALSE`
- Artifact count: `0`
- Candidate 07: `NOT AUTHORIZED`
- N22: `NOT STARTED`

Next:

`Product Owner authorization → Formal V005 Build + Exact Verification`


## N21 Reference Delivery Bundle V005｜Formal Build + Exact Verification｜2026-10-01

Status:

`FORMAL BUILD PASS / 2 OF 2 EXACT VERIFIED / INDEPENDENT ARTIFACT VERIFIED / GENERATION_ALLOWED TRUE / C07 NOT AUTHORIZED`

- spec: `production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V005.json`
- revision: `V005-R2`
- authorization commit: `5dcb51deb9f00b01ee36a1e9290a23dbb60c6e8f`
- run: `36859705482`
- job: `110360617971`
- Artifact: `11161920411`
- Artifact size: `4697710`
- Artifact digest: `sha256:358ea894249d88e93047eabbfeb760196a34c29afdfa2a82277fc875560ecb58`
- exact verification: `2/2 PASS`
- independent ZIP verification: `MATCH`
- bundle-level `GENERATION_ALLOWED=TRUE`
- Candidate 07: `NOT AUTHORIZED`
- N22: `NOT STARTED`

Next:

`Product Owner authorization → N21 Candidate 07 Work generation`


## N21 Candidate 07｜Work Generation Authorization｜2026-10-01

Status:

`PRODUCT OWNER AUTHORIZED / ONE PNG ONLY / WAITING WORK OUTPUT`

- mode: `CLEAN REGENERATION`
- Bundle: `N21_REFERENCE_DELIVERY_BUNDLE_V005`
- Artifact: `11161920411`
- pre-generation verification: `2/2 exact required`
- generation count: `1 PNG`
- Candidate 08: `NOT AUTHORIZED`
- N22: `NOT STARTED`

Authorization record:

`docs/project_control/gates/P0_3_video_pipeline/n21_candidate_07_work_generation_authorization_2026-10-01.md`

Next:

`Work generation → Product Owner review`


## N21 Crowd Body/Wardrobe Reference V001｜Human-Only Route｜2026-10-01

Status:

`DESIGN LOCKED / INPUT SPEC CREATED / VALIDATION 4 OF 4 PASS / FORMAL BUILD NOT AUTHORIZED`

- target: `N21_CROWD_BODY_WARDROBE_REFERENCE_V001 Candidate 01`
- input bundle: `N21_CROWD_BODY_WARDROBE_REFERENCE_INPUT_BUNDLE_V001`
- inputs: `AST_IMG_000051 / AST_IMG_000064 / AST_IMG_000068 / AST_IMG_000075`
- validation run: `36865944026`
- validation job: `110381336287`
- exact validation: `4/4 PASS`
- Artifact count: `0`
- formal build: `NOT AUTHORIZED`
- Work generation: `NOT AUTHORIZED`
- N21 Candidate 07: `NOT APPROVED / REVIEW CLOSED`
- N21 Candidate 08: `NOT STARTED`
- N22: `NOT STARTED`

Next:

`Product Owner authorization → Formal human-only input Bundle build`


## N21 Crowd Body/Wardrobe Reference Input Bundle V001｜Formal Build｜2026-10-01

Status:

`FORMAL BUILD PASS / 4 OF 4 EXACT VERIFIED / INDEPENDENT ARTIFACT VERIFIED / WORK GENERATION NOT AUTHORIZED`

- run: `36866387094`
- job: `110382804693`
- Artifact: `11163447680`
- Artifact size: `7404683`
- Artifact digest: `sha256:79c150bc3caf4648b4935a411585d155228fea4b0c2e85959c83a51c4d7a69e1`
- exact verification: `4/4 PASS`
- independent ZIP verification: `MATCH`
- bundle-level `GENERATION_ALLOWED=TRUE`
- human-only Candidate 01: `NOT AUTHORIZED`
- N21 Candidate 08: `NOT STARTED`
- N22: `NOT STARTED`

Next:

`Product Owner authorization → Work generation of N21_CROWD_BODY_WARDROBE_REFERENCE_V001 Candidate 01`


## N21 Crowd Body/Wardrobe Reference V001｜Candidate 01 Work Authorization｜2026-10-01

Status:

`PRODUCT OWNER AUTHORIZED / ONE PNG ONLY / WAITING WORK OUTPUT`

- Bundle Artifact: `11163447680`
- exact verification before generation: `4/4 required`
- output: `1 PNG`
- background: transparent / neutral only
- Candidate 02: `NOT AUTHORIZED`
- N21 Candidate 08: `NOT STARTED`
- N22: `NOT STARTED`
- canonical publication: `NOT AUTHORIZED`

Next:

`Work generation → Product Owner review`


## N21 Crowd Body/Wardrobe Reference V001｜Closeout｜2026-10-01

Status:

`PRODUCT OWNER APPROVED / CANONICAL / EXACT VERIFIED / CLOSED`

- approved candidate: `Candidate 03`
- canonical PNG: `production/human_references/n21_crowd_body_wardrobe/N21_CROWD_BODY_WARDROBE_REFERENCE_V001.png`
- manifest: `production/human_references/n21_crowd_body_wardrobe/N21_CROWD_BODY_WARDROBE_REFERENCE_V001.manifest.json`
- dimensions: `1536×1024`
- mode: `RGBA`
- bytes: `1418940`
- SHA-256: `73bb645e5a22cccb53faf8eb2d4b8fc0b876980e7520a2bc54daab1207439dc6`
- Git blob: `2b86ab207ee60ba0cd2de277bb55900b8854099c`
- intake verify: `36873981603 / 110408581874 / PASS`
- canonical publication: `e1d3a82da4b96eb0f20f2a629ef1140d4668b650`
- canonical verify: `36874219371 / 110409384685 / PASS`
- temporary staging / verifiers: `CLEANED`
- N21 Candidate 08: `NOT STARTED`
- N22: `NOT STARTED`

Next proposed design:

`N21_REFERENCE_DELIVERY_BUNDLE_V006 = Threshold Environment Reference + Crowd Body/Wardrobe Reference`

Do not build or generate until separate Product Owner approval.

## Generic Guest Crowd Core Set V001｜FRONT Board Bundle V001｜2026-10-02

Status:

`FORMAL BUILD PASS / 4 OF 4 EXACT VERIFIED / INDEPENDENT ARTIFACT VERIFIED / CANDIDATE 01 NOT AUTHORIZED`

- Bundle Design V0.1: Product Owner APPROVED / LOCKED.
- reference set: `AST_IMG_000042 / AST_IMG_000046 / AST_IMG_000022 / AST_IMG_000009`.
- validation-only run: `37019842679 / 110879793932 / 4/4 PASS / no Artifact`.
- formal-build authorization commit: `8e5c51ac841992a319921ce2db959a9eae7d5fe3`.
- formal run: `37020135208`.
- formal job: `110880801633`.
- Artifact: `11231259655`.
- Artifact size: `11,200,536 bytes`.
- Artifact digest: `sha256:336340a61feb7808006b4dd0c9d067a03c6ba8a4d3e4124ba08e039bc06efd07`.
- independent ZIP digest: `MATCH`.
- independent delivered-reference verification: `4/4 PASS`.
- Product Owner manual reference upload: `0`.
- bundle-level `generation_allowed=true`; governance-level Work generation remains `NOT AUTHORIZED`.
- LEFT / RIGHT / BACK remain blocked.
- N23 Candidate 02 remains paused; N21 remains HOLD.

Next:

`Product Owner authorization → FRONT BOARD Candidate 01 / Clean Regeneration / exactly one PNG`

