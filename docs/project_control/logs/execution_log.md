# Execution Log｜BLACK-LADY-001

## 2026-09-27｜N11 N12 N14 Story Shot Final Registration

- Product Owner requested end-of-day archival for N11 / N12 / N14 under the locked RC-024 process.
- Correct original PNGs were published in commit `ebe1361664f27dd1fa17b866e0d529f7128abf46`.
- Upload verification workflow run `36324358350`, job `108634127720`: SUCCESS / OVERALL_RESULT=PASS.
- Upload verification artifact `10933591429`, digest `sha256:363db1043e92ef5e14c59a4bc9fe57b93c7875d190be23567334b51cc08cca3b`.
- Exact identities:
  - N11: SHA-256 `09d45c1b27fbd2aea68c818677d9656a2ae7f39296f80f6db622118312aebcc5` / 2,538,801 bytes / blob `f5efde465dcadd1490f2064c6db39e1d5f194dc6`.
  - N12: SHA-256 `d94dc3623ba1abc55aa86c8b646d7876d097433bfadb70291bfa9c68cffc030b` / 2,434,337 bytes / blob `853d04f5ed8a2e1845ce1dfa9cef5c02f123124b`.
  - N14: SHA-256 `0474003a1d6d48a652935033f17560d0ee1d689caadbdb7d4af72560477844f1` / 2,500,282 bytes / blob `e32c03bc21efcd0eda98d2e9868a64915583b19f`.
- Exact-blob canonical publication commit: `caff3cef027366b75e2ced5b04f363ed6a89b5f6`; no PNG re-encode.
- Formal canonical filenames:
  - `N11_NEIL_ABNORMAL_PORTRAIT_APPROVED_V001.png`
  - `N12_NEIL_CROSS_RIGID_SMILE_APPROVED_V001.png`
  - `N14_FIRST_ENCOUNTER_IMPORTANCE_APPROVED_V001.png`
- Story Shot Index registration commit: `f301eff807434552e52d78070a8d06e492c1ae06`.
- Registration verification run `36324545377`, job `108634649651`: SUCCESS.
- Registration verification artifact `10933043856`, digest `sha256:f0ec1acc11572c3127067af58d0cdedafe21f672118a8c29da16d168b5bdf3e1`.
- Verification result: N11/N12/N14 PASS, INDEX_MATCH=YES, STAGING_CLEANUP_PASS, OVERALL_RESULT=PASS.
- The earlier incorrect upload batch from commit `1e91d5f33017122e78196ed573a8f4d80e3aca9d` was never registered and its temporary binaries were removed from the current tree.
- Story Shot Index now contains 20 APPROVED/CURRENT records.
- N13 remains cancelled / rejected / unregistered.
- EOD pause: do not continue the existing Neil-focused N15 design before checking the canonical novel for the actual key → escape-door chain.

## 2026-09-27｜N14 Candidate 01 PO Approval + N15 Design Start

- N14 Candidate 01 generated from verified N14_REFERENCE_DELIVERY_BUNDLE_V001; Work reported 5/5 MATCH.
- Product Owner explicitly approved N14 Candidate 01.
- Approved source identity recorded: 941×1672 / 2500282 bytes / SHA-256 `0474003a1d6d48a652935033f17560d0ee1d689caadbdb7d4af72560477844f1`.
- N14 is the final creative selection but remains unpublished/unregistered pending the planned S02-A batch archival.
- Began N15 Director Shot Design V0.1.
- N15 narrative function: apply N14's general experience rule specifically to Neil — butler role → plausible key-holder.
- N15 design uses a restrained reverse observation / role-establishing shot of Neil; no keys, no clean waist exposure, no empty-waist answer.
- A05 remains exclusive reveal owner.

## 2026-09-27｜N14 Reference Delivery Bundle V001 Built

- Product Owner approved N14 Bundle Design and authorized real construction.
- Chat followed the locked Story Shot route directly; no Codex handoff was used.
- Added workflow `.github/workflows/p03-n14-reference-delivery-bundle-v001.yml`.
- Source commit: `ae34a3a5722473f1888d23db2f1f9a596f6978bb`.
- GitHub Actions run `36317403211`, job `108614612409`: SUCCESS.
- Artifact `N14_REFERENCE_DELIVERY_BUNDLE_V001`, ID `10931321832`, digest `sha256:40236e5e4d33f1d0a5b76eef455ff51ca688238fef42fdb054987ecc60bc317a`.
- Artifact size: `12618491` bytes; expires 2026-10-04.
- Five of five canonical references passed exact verification.
- A04 exact SHA-256 computed from the locked canonical binary: `8111a2d80bb68efe99bc723d197a580b5bfed3d64a1ffeb3848db9260bb50398`.
- Product Owner manual reference upload = 0.
- Next: Work generates N14 Candidate 01 only; no N15 or Story Shot registration before review.

## 2026-09-27｜N14 Director Approval + Bundle Design Start

- Product Owner approved N14 Director Shot Design V0.1.
- Locked visual strategy: Ning Qiushui as clear primary subject; tight / medium close-up; shallow depth of field; calm experienced analytical state; Neil only as a soft out-of-focus referent.
- Began N14 Reference Delivery Bundle Design V0.1.
- Proposed minimum canonical reference set: A04 continuity + Ning FACE_FRONT + Ning BODY_FRONT + Neil BODY_FRONT + Castle Entrance Scene Master.
- Explicitly excluded N13, A05, unpublished N11/N12 final candidates, future N15 and key/waist imagery.
- No Bundle build or Work generation yet.

## 2026-09-27｜S02-A V0.2 Restructure + N14 Design Start

- Product Owner rejected the original N13 structural concept after reviewing Candidate 01.
- Product Owner determined N13 should not remain an independent formal Story Shot; its waist-observation function is absorbed into A05.
- The long reasoning narration is restructured:
  - N14 = prior-experience rule: first person encountered after entering a Blood Door is often important;
  - N15 = butler as important manor role + likely key-holder inference;
  - no N16.
- Formal S02-A V0.2 sequence: `N11 → N12 → A04 → N14 → N15 → A05`.
- N13_REFERENCE_DELIVERY_BUNDLE_V001 and N13 Candidate 01 are retained only as historical process evidence; N13 Candidate 01 is rejected and must not be registered.
- Began N14 Director Shot Design V0.1 with Ning Qiushui as primary subject and Neil only as a soft secondary referent.
- No N14 Bundle or generation yet.

## 2026-09-27｜N13 Reference Delivery Bundle V001 Built

- Product Owner authorized real N13 Bundle construction.
- Chat followed the locked Story Shot path directly; no Codex handoff was used.
- Added workflow `.github/workflows/p03-n13-reference-delivery-bundle-v001.yml`.
- Source commit: `bdd2480fb995462f89ea51400d02b0135912ce42`.
- GitHub Actions run `36314032099`, job `108605228883`: SUCCESS.
- Artifact `N13_REFERENCE_DELIVERY_BUNDLE_V001`, ID `10930326122`, digest `sha256:0b40fd3e34b18297c679c2e307f2e4d6480e90c2eef1697adcbdd8b15d8d6fb7`.
- Artifact size: `12637035` bytes; expires 2026-10-04.
- Five of five canonical references passed exact SHA-256 / byte-size / Git-blob / byte-identical-copy verification.
- Product Owner manual reference upload = 0.
- A05 remains excluded to preserve exclusive no-keys reveal authority.
- Next: Work generates N13 Candidate 01 only; no N15 or Story Shot registration before review.

## 2026-09-27｜N13 Bundle Design Approved + Build Prep

- Product Owner advanced N13 into Reference Delivery Bundle design, then into N13_REFERENCE_DELIVERY_BUNDLE_V001 build design / execution preparation.
- Formalized N13 Director Shot Design V0.1 as approved.
- Formalized N13 Reference Delivery Bundle Design V0.1 as approved.
- Locked minimum canonical set = 5: Neil FACE_FRONT / FACE_3Q_LEFT / BODY_FRONT + Castle Entrance Scene Master + N01 continuity.
- N11 Candidate 03 and N12 Candidate 02 remain creatively approved but unpublished, therefore excluded from formal Bundle inputs.
- N09/N10 excluded for exterior-state bias.
- A05 explicitly excluded because it owns the "waist empty / no keys" reveal and could leak the answer into N13.
- Prepared fail-closed GitHub Actions build contract; no workflow or artifact build executed yet.
- Next: Product Owner authorizes real Bundle construction.

## 2026-09-27｜N11 Candidate 03 + N12 Candidate 02 Final Creative Approval

- Product Owner approved `N11 Candidate 03` as the final N11 creative selection.
- N11 Candidate 03 retains a visible metal chain while the cross pendant itself is hidden by the waistcoat/clothing, preserving N12 as the explicit cross-reveal shot.
- N11 Rebuild Candidate 01 is superseded for final use.
- N11 Candidate 02 is rejected for final use because its generated cross did not match the approved N12 cross design.
- Product Owner had already approved `N12 Candidate 02` as the final N12 creative selection; N12 Candidate 01 is superseded.
- Per Product Owner instruction, N11 and N12 are not individually published/registered yet. Formal binary publication and Story Shot registration are deferred to a later S02-A batch archival pass.
- Next: N13 Director Shot Design.

## 2026-09-27｜N12 Reference Delivery Bundle V001 Built

- Product Owner approved N12 Reference Delivery Bundle Design V0.1.
- Chat followed the locked P0.3 Story Shot reference-delivery path directly; no Codex handoff was used.
- Added temporary workflow `.github/workflows/p03-n12-reference-delivery-bundle-v001.yml`.
- Source commit: `45d1dd4da22f1c30f4131d57cafa9a51f6d6b42d`.
- GitHub Actions run `36307403582`, job `108586621481`: SUCCESS.
- Artifact `N12_REFERENCE_DELIVERY_BUNDLE_V001`, ID `10927392671`, digest `sha256:e035ffc7d0f965b389e6e21054d5b7a63c1b31e5ef1e13f0242eb810320e70ed`.
- Five of five canonical references passed exact SHA-256 / byte-size / Git-blob / byte-identical-copy validation.
- Product Owner manual reference upload = 0.
- Next: Work automatically acquires the artifact, revalidates manifest, and generates N12 Candidate 01 only.
- No Story Shot registration or S02-A batch archival yet.

## 2026-09-27｜N12 Director Approval + Bundle Design Start

- Product Owner approved N12 Director Shot Design V0.1.
- Began N12 Reference Delivery Bundle Design V0.1.
- Proposed minimum canonical set = 5: Neil FACE_FRONT / FACE_3Q_LEFT / BODY_FRONT + Castle Entrance Scene Master + N01 post-Opening continuity.
- N11 is deliberately not used because it is approved but awaiting later S02-A batch publication/registration.
- N09 and N10 are excluded to avoid exterior spatial bias and earlier natural-smile bias.
- No standalone cross Prop Asset is required for N12 V001; one simple realistic cross is authorized by source narration and the director lock.
- No bundle workflow or image generation executed yet.

## 2026-09-27｜N11 Overall Approval Clarification + N12 Design Start

- Product Owner clarified the prior "批准" meant N11 Rebuild Candidate 01 was approved overall, not approval of a targeted-edit plan.
- R105's Candidate 02 interpretation is superseded.
- N11 Rebuild Candidate 01 status is now `PRODUCT OWNER APPROVED / PENDING BATCH ARCHIVAL`.
- Product Owner requested later S02-A Story Shots be produced first and archived/registered together afterward.
- No N11 Candidate 02 is required.
- Began `N12 Director Shot Design V0.1`.
- N12 narrative function: clearly visible cross + small rigid closed-mouth smile, escalating unease without overt horror.
- No N12 Bundle or generation yet.

## 2026-09-27｜N11 Rebuild Candidate 01 Review

- Product Owner reviewed N11 Rebuild Candidate 01.
- Candidate 01 is not final-approved.
- PASS/preserve: Neil identity, inside-door spatial relation, closed-mouth waiting state, single-side doorway cue, dark subordinate background, no cross emphasis.
- Targeted corrections authorized for Candidate 02:
  1. crop/recompose to true upper-chest-up framing;
  2. reduce warm/red healthy skin tone to natural pale low-blood-color complexion.
- Full regeneration is explicitly not authorized.
- Do not alter spatial blocking, identity, costume, expression or background structure.
- Next: Work targeted edit → N11 Rebuild Candidate 02 → Product Owner review.

## 2026-09-27｜N11 Reference Delivery Bundle V002 Built

- Product Owner approved N11 Director Shot Design V0.2 and V002 bundle construction.
- Chat followed the already-locked Story Shot reference-delivery process directly; no Codex handoff was used.
- Added temporary workflow `.github/workflows/p03-n11-reference-delivery-bundle-v002.yml`.
- Source commit: `e2b8568f20ba8ee4e044a725d56624e6cbd9b733`.
- Run `36305485637`, job `108581173489`: SUCCESS.
- Artifact `N11_REFERENCE_DELIVERY_BUNDLE_V002`, ID `10927315457`, digest `sha256:a00cb07e9875afd5f63b1303c8722955d8cf25800aab4990946c5dc9f2df2b7e`.
- Five of five canonical references passed exact SHA-256 / byte-size / Git-blob / byte-identical-copy validation.
- V002 reference set: Neil FACE_FRONT / FACE_3Q_LEFT / BODY_FRONT + Castle Entrance Scene Master + N01.
- A03, N05, N09 and all failed N11 candidates are explicitly excluded.
- Next: Work automatically acquires the artifact, revalidates 5/5, and generates one fresh N11 Rebuild Candidate 01.
- No N12 work or N11 Story Shot registration yet.

## 2026-09-27｜N11 Redesign V0.2 Start

- Product Owner rejected the two newest N11 correction outputs and requested a restart of the shot.
- Review determined the failure is compositional, not identity/governance: doorway proof became dominant, framing widened, and the cross became too prominent.
- Began `N11 Director Shot Design V0.2`.
- V0.2 hard-locks an upper-chest-up observational portrait with only a subtle one-sided door-edge foreground cue.
- Neil must remain clearly inside the entrance, but architecture is subordinate.
- Cross should preferably not appear.
- Proposed Bundle V002 removes A03 and retains Neil FACE_FRONT / FACE_3Q_LEFT / BODY_FRONT + Castle Entrance Scene Master + N01.
- Failed N11 candidates are explicitly excluded as future image references.
- No Bundle V002 build or image generation yet.

## 2026-09-27｜N11 Reference Delivery Bundle V001 Built

- Product Owner approved N11 Reference Delivery Bundle Design V0.1.
- Chat followed the locked P0.3 image-generation path directly; no Codex handoff was required.
- Added temporary workflow `.github/workflows/p03-n11-reference-delivery-bundle-v001.yml`.
- Source commit: `ac83d41398f8fe7d6f3ef0ef24ca1921e8804909`.
- GitHub Actions run `36303103682`, job `108574387646`: SUCCESS.
- Artifact `N11_REFERENCE_DELIVERY_BUNDLE_V001`, ID `10925624760`, digest `sha256:f2bba3b9dcb3a064c20b4cdc2267d8bc7862ec9c8d9f20d700ae6b5715aa2c4f`.
- Six of six canonical references passed exact SHA-256 / byte-size / Git-blob / byte-identical-copy validation.
- A03 computed canonical SHA-256: `5dc075a6f917fb7fdc05cf299315675bfdd5db4a0d737518ef4aafeacc78ee1e`.
- Product Owner manual reference upload = 0.
- Next: Work automatically acquires the artifact, revalidates manifest, and generates N11 Candidate 01 only.
- No N11 Story Shot registration and no N12 production yet.
- P0.3 remains IN PROGRESS / NOT YET VALIDATED.

## 2026-09-27｜N11 Director Design V0.1 Approval + Bundle Design Start

- Product Owner corrected and approved N11 spatial continuity: Neil has already crossed the threshold and is waiting on the interior side of the open entrance, facing outward.
- Formalized `docs/project_control/gates/P0_3_video_pipeline/n11_director_shot_design_v0_1.md` as PRODUCT OWNER APPROVED.
- Began `N11 Reference Delivery Bundle Design V0.1`.
- Proposed bundle count = 6: Neil FACE_FRONT / FACE_3Q_LEFT / BODY_FRONT + Castle Entrance Scene Master + N01 immediate Opening end-state continuity + A03 interior-side entrance spatial continuity.
- N09 excluded to avoid conflicting outside-threshold spatial authority.
- N05 excluded from V001 baseline because N01 is the immediate post-action state; N05 remains an optional controlled fallback if generation regresses spatially.
- No bundle workflow or image generation executed yet.
- P0.3 remains IN PROGRESS / NOT YET VALIDATED.

## 2026-09-27｜S02-A Six-Shot Plan Approval + N11 Design Start

- Product Owner approved the post-Opening S02-A visual structure.
- Formal sequence: N11 NEW → N12 NEW → A04 REUSE → N13 NEW → N15 NEW → A05 REUSE.
- New production count = 4 Story Shots; reused approved shots = 2.
- A05 retains exclusive reveal authority for "Neil's waist is empty / no keys"; N13/N15 may create suspense but may not reveal the answer early.
- Added `docs/project_control/gates/P0_3_video_pipeline/s02_a_shot_plan_v0_1.md`.
- Began `N11｜Neil Abnormal Portrait｜Director Shot Design V0`.
- N11 design uses current/approved Neil character authority and Opening entrance continuity.
- No N11 image generation or registration has been authorized yet.
- P0.3 remains IN PROGRESS / NOT YET VALIDATED.

## 2026-09-27｜Opening V001 Product Owner Approval + Canonical Archive

- Product Owner explicitly approved uploaded `P03_OPENING_V2_PROOF_REVIEW_V002.mp4` as the formal Opening video.
- Chat runtime independently inspected the uploaded attachment: SHA-256 `70d7922244161dd216a26446fd75531db20eea0ac7fc25f567f6ff14e2746e3a`, `18892138` bytes, 1080×1920, H.264/yuv420p, 30fps, 991 frames, AAC 48kHz stereo, full decode PASS.
- Attachment identity exactly matched the historical V002 render.
- One-off archive workflow first run `36300965829` failed only because FFmpeg was not preinstalled on the clean runner; no publication occurred.
- Workflow was corrected to install FFmpeg.
- Archive verification run `36300993520` then PASSed all steps: historical artifact download, SHA/bytes/media identity, full decode, exact-binary copy, Git publication, remote blob/size verification, receipt publication.
- Canonical master: `production/video/approved/opening/P03_OPENING_V2_APPROVED_V001.mp4`.
- Canonical SHA-256: `70d7922244161dd216a26446fd75531db20eea0ac7fc25f567f6ff14e2746e3a`; byte size: `18892138`; Git blob: `9b4ef42d9eceb5d7f1eb190d508d6749ccf4b70e`.
- Publication commit: `208566291a5531cb34ad05e50e56e0a9fcc51c02`.
- Approval/archive receipt artifact ID: `10925990918`.
- Registered `OPENING_V001` in `production/video/video_index.jsonl`.
- Opening V001 is now APPROVED / LOCKED. V003 and libopenshot proofs remain retained evidence and are not selected Opening masters.
- RC-026 remains the editing-process framework: future sequences reuse the workflow, not V002's exact visual/timing template.
- P0.3 remains IN PROGRESS / NOT YET VALIDATED.
- Next: post-Opening story/audio breakdown and sequence-specific production design.

## 2026-09-27｜Editing Workflow Framework V1 Registration

- Product Owner requested that the V002 production workflow be retained as a reference for future editing work.
- Explicit boundary: this is a reusable process framework, not a fixed visual/timing template.
- Registered RC-026 and added `docs/project_control/gates/P0_3_video_pipeline/editing_workflow_framework_v1.md`.
- Reusable lifecycle: canonical story/audio context → Chat director/edit design → contextual timeline → canonical input verification → engine implementation → scene-specific motion/transition treatment → continuous source audio where appropriate → GitHub Actions render/QC → full-context PO review → targeted iteration.
- V002's 12-shot count, 991-frame map, exact cut points, motion/transition parameters and Remotion implementation are not locked for future sequences.
- Later edits must be redesigned from the actual plot, dialogue/narration, action, character performance, spatial continuity and emotional rhythm.
- Rendering engine remains an execution choice, not the source of editorial decisions.
- P0.3 remains IN PROGRESS / NOT YET VALIDATED.

## 2026-09-27｜Opening V2 libopenshot Full Proof V001

- Product Owner confirmed Chat can directly design the complete 12-shot motion plan and communicate with GitHub Actions without a Codex handoff.
- Chat completed the director-level 12-shot Cinematic Motion Spec and wrote the libopenshot full-proof workflow/scripts directly to canonical main.
- Canonical Story Shots and audio were verified before render.
- GitHub Actions run `36299431486` rendered the complete 991-frame sequence successfully.
- Artifact `P03_OPENING_V2_LIBOPENSHOT_FULL_PROOF_V001`, ID `10925078297`, digest `sha256:4f6545e1094344919330823e34d2e088bf78c2eabbf1d89d4e686547f6d1a6ab`.
- Technical QC PASS: 1080×1920, H.264/yuv420p, 30 fps, 991 decoded frames, 33.033333 sec, continuous AAC audio, full decode PASS.
- MP4 SHA-256: `e821b8a76af3bd5f6e7c776e81cc907f1873a3a7dc4f96173b2ceefe16972385`.
- Sequence, Story Shot binaries and Draft 01 timing remain unchanged.
- No final timing lock and no P0.3 PASS claimed.
- Next: Product Owner contextual review of the complete libopenshot edit versus Remotion V003.

## 2026-09-27｜libopenshot Camera Motion Proof V001

- Product Owner requested direct Chat + GitHub Actions execution of a libopenshot camera-motion test before any full Opening V2 migration.
- Scope locked to approved canonical Story Shots N08, N03 and N05.
- Built a new GitHub Actions path using Ubuntu + `python3-openshot` + Python bindings.
- First run `36298583006` reached libopenshot rendering but crashed with SIGSEGV in `Timeline::find_intersecting_clips`.
- Root cause: Timeline retained raw pointers while Python/SWIG reader/clip objects were garbage-collected after helper return.
- Added explicit reader/clip keepalive references.
- Run `36298639226` then completed successfully.
- Motion design:
  - N08: hold → architectural push → overshoot → settle
  - N03: pull-back + lateral observation drift → settle
  - N05: action push + reframe + settle-shake + micro rotation
- Artifact `P03_LIBOPENSHOT_CAMERA_MOTION_PROOF_V001`, ID `10923993594`, digest `sha256:b8986b111a523d2d036dc53cab88d22c7952e9d544c7540fad37f5d08b8871bf`.
- Technical QC PASS: 1080×1920, H.264/yuv420p, 30 fps, 228 frames, 7.600 sec, full decode PASS.
- MP4 SHA-256: `4582f00d89a4df65497be3c1f1ba34801671c9fc8bc1b802519d61f05f141a88`.
- This is motion-only technical evidence; no Opening V2 migration, no final edit approval and no P0.3 PASS claimed.
- Next: Product Owner compares libopenshot motion quality with Remotion V003.

## 2026-09-27｜Opening V2 Proof Review V003

- Product Owner approved proceeding directly to a complete V003 using Chat + GitHub Actions.
- V003 preserves the now-working 12-shot sequence, uninterrupted canonical audio and Draft 01 timing.
- Editorial treatment was strengthened one perceptible tier above V002: longer dissolves, stronger push/pull/drift, stronger focus/vignette cues, blur/focus transitions, and a clearer but still restrained N05 action accent.
- Initial run `36297396556` failed because React dependencies were mismatched (`react 19.2.4` / `react-dom 19.2.3`).
- Dependency versions were corrected to `19.2.4 / 19.2.4`.
- GitHub Actions run `36297467856` then completed successfully.
- Artifact `P03_OPENING_V2_PROOF_REVIEW_V003`, ID `10924960913`, digest `sha256:cdafde226070f8eec26c71eec628d2107e1fca39fb4acd0d33ed952292d1dce4`.
- Technical QC PASS: 1080×1920, H.264/yuv420p, 30 fps, 991 decoded frames, continuous AAC audio, full decode PASS.
- MP4 SHA-256: `b6914ca1910ef0078876fc8063d079870df6927a4f1f2a7291ddf6d43ab4968f`.
- No P0.3 PASS and no final timing lock claimed.
- Next: Product Owner full-sequence contextual review.

## 2026-09-27｜V002 Product Owner Review

- Product Owner reviewed `P03_OPENING_V2_PROOF_REVIEW_V002`.
- Feedback: no meaningful perceptual difference from V001.
- Technical render/QC remains valid, but V002 did not meet the intended artistic enrichment objective.
- Decision: retain the current successful audio/story alignment and 12-shot order; proceed to V003 with stronger, clearly perceptible but controlled editorial motion/transition/focus treatment.
- No P0.3 PASS and no final timing lock claimed.

## 2026-09-27｜Opening V2 Proof Review V002

- Product Owner requested richer image transitions and context-sensitive 2D motion while preserving the now-working audio/story alignment.
- Chat implemented V002 directly in GitHub and triggered GitHub Actions; no Codex handoff was required.
- V002 preserves the 12-shot sequence, uninterrupted canonical source audio and Draft 01 timing.
- Added selective dissolves, two blur/focus dissolves, varied static/push/pull/light-drift motion, light focus/vignette treatment and one restrained N05 shake/settle event.
- GitHub Actions run `36296689531` completed successfully.
- Artifact `P03_OPENING_V2_PROOF_REVIEW_V002`, ID `10924430609`, digest `sha256:323a48034e45562b5153d635dbe565f51211d81a694c44202b6da92e4deba2ac`.
- Technical QC PASS: 1080×1920, H.264/yuv420p, 30 fps, 991 decoded frames, continuous AAC audio, full decode PASS.
- MP4 SHA-256: `70d7922244161dd216a26446fd75531db20eea0ac7fc25f567f6ff14e2746e3a`.
- No P0.3 PASS and no final timing lock claimed.
- Next: Product Owner full-sequence contextual review.

## 2026-09-27｜Opening V2 Contextual Proof Review V001

- Product Owner rejected isolated 3-second cut-point listening as the primary approval method because the perceived pauses felt unnatural and timing must be judged with the images.
- Clarification: the 3-second clips were centered review windows, not equal-duration final segmentation.
- Review method changed to full-context audiovisual proof first.
- GitHub Actions run `36294677578` rendered the complete 12-shot Opening V2 sequence against one uninterrupted canonical audio track.
- Artifact `P03_OPENING_V2_PROOF_REVIEW_V001`, ID `10923721767`, digest `sha256:e928f8f91f578159e16711c64f6fa215a347603563901d13bee332b2981d3af2`.
- Technical QC PASS: 1080×1920, H.264/yuv420p, 30 fps, 991 decoded frames, continuous AAC audio, full decode PASS.
- MP4 SHA-256: `d538c87e8da781aec61401b2c7a01ce5e25a4ad0de038299d598685d376e771e`.
- Internal cut points remain provisional; no timing lock and no P0.3 PASS claimed.
- Next: Product Owner full-sequence artistic review, then targeted timing / motion / shot-order revision if needed.

## 2026-09-27｜Opening V2 Audio Alignment Analysis V001

- Chat created and executed a GitHub Actions analysis workflow against the exact canonical audio binary.
- Canonical audio identity passed: SHA-256 `8d0d12d3af5e2c15032912605c0d1b3f3e892fe24918a7064864b136987737a0`, byte size `4,957,338`, duration `359.141995 sec`.
- Successful run: `36293571350`.
- Artifact: `P03_OPENING_V2_AUDIO_ALIGNMENT_ANALYSIS_V001`, artifact ID `10922898643`, digest `sha256:2da55ec3eaec37038642ad27a39e3e77e59dcc9a6b62eeb93c5d3847455764b0`.
- Analysis scope: `00:00.000–00:33.020`.
- Fixed VERIFIED transcript boundaries retained: `3.250 / 6.550 / 19.700 / 30.030 / 33.020 sec`.
- Internal acoustic candidates produced: `8.940 / 11.200 / 13.200 / 15.310 / 21.620 / 24.420 / 27.160 sec`.
- Multi-threshold silence detection did not find true silence intervals in the opening window; candidates therefore use transcript-semantic rough targets refined by local low-energy valleys.
- `N03→N04 = 15.310s` hit the edge of its ±0.90s search window and remains specifically untrusted until director / listening review.
- No final internal cut point was auto-approved; director lock remains pending.
## 2026-09-27｜RC-025 Rule Consistency Audit

- Reviewed current rule-bearing documents across Project Control after RC-024 Story Shot SOP standardization.
- Resolved the main scope conflict between P0.2 Asset Registry `asset_class=SHOT` and P0.3 `asset_class=STORY_SHOT`: they are now explicitly separate data layers and may not be silently dual-registered.
- Clarified that P0.2 SHOT naming (`<SHOT_ID>_<ROLE>_<VARIANT>_<STATE>_V###`) applies to Asset Registry-managed SHOT assets; existing Story Shot operational filenames N01–N10 remain unchanged under RC-024/RC-025.
- Clarified that Product Owner upload of an approved final Story Shot PNG is final-output publication, not reference upload. RC-022/RC-023 manual PO reference upload baseline remains `0`.
- Reconciled the long-term Automatic Ingest goal with the currently verified Story Shot publication bridge. PO does not perform canonical naming, index registration, hashes, version relations, or registration verification.
- Corrected stale Governance statements: repository visibility is public, D-### progression is no longer hardcoded, and the historical P0 'no A08/later shots' boundary no longer blocks representative Story Shot production required for P0.3 validation.
- Added Project Control rule-precedence guidance so Gate summaries do not become parallel rule authorities.
- Removed stale pre-approval / not-yet-validated wording from the current P0.2 Visual Asset baseline, Naming Rules, and Registry Schema while preserving their historical sequence as historical notes.
- Consistency result: `PASS / CONFLICTS RESOLVED`.
## 2026-09-27｜RC-024 Story Shot Production + Registration SOP

- Product Owner requested the proven Story Shot generation and registration process be standardized as a formal project rule.
- Added `docs/project_control/gates/P0_3_video_pipeline/story_shot_production_registration_sop_v1.md`.
- Locked standard lifecycle: `Director Design → Reference Delivery Bundle → Work Generation → Product Owner Approval → Original PNG Upload → Binary Verification → Exact-Blob Canonical Rename → Story Shot Index Registration → Registration Verification → Project Control Closeout`.
- Formal completion requires four gates: PO APPROVED + canonical binary published + Story Shot Index registered + registration verification PASS.
- SOP operationalizes RC-021 / RC-022 / RC-023 and RC-014; binary identity mismatches remain FAIL CLOSED.
- Normal Work reference delivery remains automated through canonical GitHub / Resolver / Bundle; manual Product Owner reference upload baseline remains 0.
- Codex is not part of the normal Story Shot image production / registration baseline.

## 2026-09-27｜N06-N07 Story Shot Final Registration

- Product Owner approved N06 Candidate 02 and N07 Candidate 01 for Opening V2.
- Product Owner uploaded the two final PNGs into `production/image_library/approved/story_shots/`; upload verification workflow run `36289949835` independently verified the exact uploaded binaries.
- Verification result: `PASS`; both files are PNG 941×1672 and their SHA-256 / byte sizes / Git blob SHAs matched the repository binaries.
- Post-registration verification run `36290165666` independently returned `N06_PASS`, `N07_PASS`, `INDEX_MATCH=YES` for both files and `OVERALL_RESULT=PASS`; evidence artifact `10921183606`, digest `sha256:2c9ac4376f9532b87920aedb093eccc9b7d3226040f8ec49669acd464ef3e5dc`.
- Upload UUID → formal canonical mapping:
  - `6ef6a4b1-e823-40f4-be98-e7d658fdaddc.png` → `N06_NEIL_SPEAKING_STATE_A_APPROVED_V001.png`
  - `33e88fb0-a959-4ab1-937c-bdd1269d7bc1.png` → `N07_NEIL_SPEAKING_STATE_C_APPROVED_V001.png`
- Canonical rename commit: `af88935298cc25b0f153b6824cf4719326762745`; exact Git blobs were reused with no PNG re-encode.
- Canonical identities:
  - N06: SHA-256 `50f17c152477cef2fcdc8e1a61e5a7c42f5d32512e19c92bdbed544d465effc5` / 1,851,865 bytes / Git blob `aa43a519fe7953a9626d47f71acf76908ed40389`.
  - N07: SHA-256 `fc2d4f7f09a1c7cc8012176ef885d3f4b3ae449741b3bd2d4ad075fb91188dd9` / 1,983,362 bytes / Git blob `379b8a209a8d6da709dc15bcb645972016176169`.
- Story Shot index now contains 17 approved records: A01–A07 + N01–N10.
- Opening V2 planned sequence is now fully covered by approved Story Shots: `A01 → A02 → N06 → N02 → N07 → N03 → N04 → N08 → N09 → N10 → N05 → N01`.
- N06 performance lock: restrained speaking gesture kept close to the body; no smile, turn, or step.
- N07 performance/composition lock: right-front 25°–35° speaking state, figure biased right, gaze to off-screen visitors at frame left, hands quiet; no smile, turn, or step.
- Next production step: assemble and review the revised 12-shot Opening V2 proof; P0.3 remains NOT YET VALIDATED.

## 2026-09-26｜P0.3 Daily Closeout

- End-of-day status: `PAUSED FOR DAY / P0.3 IN PROGRESS / OPENING V2 STORY-SHOT EXPANSION ACTIVE / N06-N07 NEXT`.
- Opening V1 30-second proof achieved technical render PASS but was not artistically approved; insufficient visual coverage and narration/action timing mismatch triggered the 12-shot Opening V2 expansion.
- N08 Candidate 01, N09 Candidate 03 and N10 Candidate 01 are Product Owner approved, exact-source verified and formally registered as approved/current Story Shots.
- Formal Work delivery chain was executed for N08/N09/N10 with manual Product Owner reference upload = 0.
- Additional end-of-day verification run `36248526501` independently passed all three canonical PNGs at 941×1672 with SHA-256 / byte-size / Git-blob checks.
- Approved Story Shot count: `15` = A01–A07 + N01–N05 + N08–N10.
- Opening V2 planned sequence: `A01 → A02 → N06 → N02 → N07 → N03 → N04 → N08 → N09 → N10 → N05 → N01`.
- N06 / N07 remain pending and are the next production task.
- PR #16 remains OPEN / NOT MERGED as historical Opening V1 technical-proof evidence; P0.3 remains NOT YET VALIDATED.
- Full daily closeout: `docs/project_control/gates/P0_3_video_pipeline/p0_3_progress_closeout_2026-09-26.md`.
- Temporary N08/N09/N10 delivery and verification workflows were removed after evidence capture.

## 2026-09-26｜N08-N10 Story Shot Final Registration

- Product Owner approved N08 Candidate 01, N09 Candidate 03, and N10 Candidate 01 for Opening V2.
- Product Owner uploaded the three final PNGs into `production/image_library/approved/story_shots/`; upload verification workflow run `36247789055` staged and independently verified the exact uploaded binaries.
- Verification result: `PASS`; all three files are PNG 941×1672 and their SHA-256 / byte sizes / Git blob SHAs matched the repository binaries.
- Upload UUID → formal canonical mapping:
  - `c01710f7-2b7b-44b6-814b-8f93401b30a3.png` → `N08_CASTLE_ENTRANCE_ARCHITECTURE_APPROVED_V001.png`
  - `39b24dd5-3959-47f9-af27-98d782b7a5ed.png` → `N09_NEIL_FORMAL_BUTLER_DESCRIPTOR_APPROVED_V001.png`
  - `e44b1fa8-ad0d-4838-92c5-0021ef2ebfb6.png` → `N10_NEIL_SUBTLE_SMILE_APPROVED_V001.png`
- Canonical rename commit: `80bb54d1ed7878676e52ffc1fdb50b2f6897e94f`; exact Git blobs were reused with no PNG re-encode.
- Canonical identities:
  - N08: SHA-256 `6bda5a8cb4d04d15071f95c6b3fdce09b10230ac95100d59aabf5bad4aef1bb4` / 2,794,372 bytes / Git blob `58b41dff1993455dcaac263a1275b973c131ba5b`.
  - N09: SHA-256 `5e76be2c9815a6caa2d8688d1879bb5ddaad78352b6440ed220dd08332a5e0ac` / 2,281,168 bytes / Git blob `9ba7456b1133efe9f449ec199ecd8d1a018b2e45`.
  - N10: SHA-256 `14dbf276dbf9ef6c7de84570d46f40230daa3ba53a304ccdc05645c58e9f6e54` / 1,822,641 bytes / Git blob `23be40b7f338e903a6f60c61d995667cb8affdce`.
- Story Shot index now contains 15 approved records: A01–A07 + N01–N05 + N08–N10.
- Opening V2 planned sequence is `A01 → A02 → N06 → N02 → N07 → N03 → N04 → N08 → N09 → N10 → N05 → N01`.
- N06 and N07 remain pending; therefore the Opening V2 Story-Shot Set is not yet complete.
- N09 spatial lock: Neil stands clearly outside on the castle entrance platform with the open double doors behind him.
- N10 expression lock: restrained closed-mouth slight smile only; no teeth, speech, turn, or step.
- Next production step: design and produce N06 / N07, then assemble the revised Opening V2 proof.

## 2026-09-26｜N02–N05 Story Shot Final Registration

- Product Owner approved and locked N02, N03 Candidate 02, N04 Candidate 01, and N05 Candidate 01.
- Opening 30-second Story Shot chain is now locked as `A01 → A02 → N02 → N03 → N04 → N05 → N01`.
- Product Owner uploaded the four final PNGs into `production/image_library/approved/story_shots/`; temporary UUID filenames were mapped by exact byte size and then verified by GitHub Actions run `36232083006`.
- Registration verifier result: `PASS`; all four files are PNG 941×1672 and their SHA-256 / byte sizes were independently calculated on the GitHub runner.
- Canonical SHA-256:
  - N02: `56ff80f51b38c05c0305c40b6a97947d992a544f2454e4a339684b80783c8e50` / 2,514,132 bytes.
  - N03: `0e5022a59d7e33e30e0fdea74c966ff8e84a3084ca869fcbc4d76052e8ec6c22` / 2,321,221 bytes.
  - N04: `183a409864b2c58186cfa34896e459cd6491e67098c0810614205eca9b534e02` / 2,286,766 bytes.
  - N05: `0b9690739e63d253ac643ae66acb4653818f4c45898c3b5db83e9de0236536ab` / 2,383,088 bytes.
- UUID uploads were canonically renamed by Git tree blob reuse, preserving exact Git blobs with no PNG re-encode:
  - `N02_NEIL_CONTINUED_EXPLANATION_APPROVED_V001.png`
  - `N03_VISITOR_REACTION_APPROVED_V001.png`
  - `N04_NEIL_WELCOME_CLOSING_APPROVED_V001.png`
  - `N05_NEIL_TURN_THRESHOLD_ACTION_APPROVED_V001.png`
- `production/story_shots/story_shot_index.jsonl` now contains 12 approved Story Shots: A01–A07 + N01–N05.
- N01 locked SHA-256 was also rechecked successfully by GitHub Actions; the previous pending-SHA note is closed.
- N05 interior decorative details remain shot-background expression only and are not promoted to canonical Scene Facts.
- Next production step: assemble and review the real 30-second Opening Audio-Comic Proof using canonical audio and the locked seven-shot sequence.

## 2026-09-26｜Story Shot Registration + Project Control Consistency Repair

- Unified `STORY_SHOT` implementation completed in Chat-led GitHub work; no Codex task number consumed.
- Machine-readable index created at `production/story_shots/story_shot_index.jsonl` with 8 approved records: A01–A07 + N01.
- Legacy A01–A07 binaries remain unchanged at `production/image_library/approved/A_Series/`; no duplicate normalization copy was created.
- N01 canonical publication completed at `production/image_library/approved/story_shots/N01_CASTLE_PAUSE_APPROVED_V001.png`.
- N01 canonical rename reused the exact uploaded Git blob `d55d2c218926c0b916c67d34979887315c351a1c`; byte size remains 2,687,303.
- Locked approved N01 SHA-256 remains `a96d52410c1645711545c80b7fe4e3eaa3e8f00b088ebaaea210bbdbec84557b`; direct GitHub-binary SHA-256 recheck is pending local verification because the temporary Actions verifier failed before executing steps. This is recorded as non-blocking.
- Project Control advanced to R082.
- Corrected stale current-state fields that incorrectly left AO-06 / D-069 open. AO-06 remains `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED 2026-09-22`; P0.2 remains `PASS / PRODUCT OWNER APPROVED`.
- Dashboard metadata/body aligned to `V055 / Derived from R082 / Updated 2026-09-26`.
- Next active production step: Opening Audio-Comic Proof using A01 + A02 + N01 + canonical audio.

## 2026-09-25｜P0.3 Route Pivot + N01 Story Shot Approval

- Product Owner rejected the real `A01 → Wide → Tight → A02` 2.5D sequence as a production path because characters visibly deformed; character-shot single-image 2.5D is no longer the P0.3 main route.
- Current P0.3 validation route changed to cinematic audio comic: canonical story/audio + approved Story Shots + normal cuts + restrained crop/zoom; AI video remains optional for selected key shots only.
- N01 was produced through composition correction plus targeted local edits for Ning Qiushui identity, Jun Luyuan identity and Jun Luyuan pose; Product Owner approved the final N01.
- N01 approved source identity: 941×1672 PNG / 2,687,303 bytes / SHA-256 `a96d52410c1645711545c80b7fe4e3eaa3e8f00b088ebaaea210bbdbec84557b`.
- Product Owner approved the unified `STORY_SHOT` model: A/N prefixes are historical only; only approved Story Shots may be admitted; candidate/rejected/WIP are excluded.
- No Story Shot library/index implementation or N01 formal registration is performed in today's closeout; these are explicitly deferred to the next work session.
- N01 approved source must not be regenerated or re-encoded before tomorrow's formal registration.
- Next-session order: Story Shot library/index implementation → N01 exact-source registration → Opening Audio-Comic Proof using A01 + A02 + N01 + canonical audio.

## 2026-09-21｜Character Visual Completion + 21 Binary Canonical Publication

- Product Owner approved Castle Young Master `REAR_3Q_LEFT V001` and all six Black Lady P3 lateral views; Character Core visual production therefore reached `63/63 PO APPROVED` with visual gap `0`.
- The 21 pending approved PNGs were consolidated outside the repo, UUID/unrelated files were separated, canonical filenames were verified, and source→repo copies passed `21/21 exact-byte SHA_MATCH` before staging.
- Git staging was restricted to exactly the 21 Character Core PNGs; unrelated untracked `black_lady_character_asset_migration_v1.zip` and `production/audio/` were not staged.
- Local publication commit: `b9bafa2af4b9be8aadf2bd2abe79b724837eff88` — `Publish 21 approved character core view PNGs`.
- First standard push failed with `Empty reply from server`; retry using temporary `http.postBuffer=524288000` succeeded. GitHub main independently verified at the same commit.
- GitHub commit contains the intended 21 PNG additions; all 21 committed binaries were re-read via Git object and independently verified `21/21 SHA_MATCH` against approved source identities.
- No Asset Registry/Audit mutation was performed. Formal Core Coverage remains `42/63 = 66.7%`.
- Engineering boundary identified: `automatic_ingest_controller_v0_1.py` expects canonical target not to exist, so direct ingest of these already-published binaries would fail closed with `Target already exists`.
- Next proposed Codex Cloud task: `D-070｜Published Binary Adoption + 21-Asset Automatic Ingest`; NOT STARTED tonight and D-number is consumed only when execution actually launches.
- AO-06 / D-069 remains OPEN and mandatory for P0.2 final closeout. P0.2 remains ACTIVE; P0.3 remains QUEUED / DO NOT START EARLY.

## 2026-09-18｜Daily Closeout / D-069 Engineering Foundation Merge

- PR #10 reviewed head `7cf9e82cf937bc4150c83bcf0fc04e57e334e824` merged to `main` as `68716eae9e73a1ee1891dfde6ac5c7ea4d578cce`.
- Merge scope = D-069 engineering foundation + Review Patch 01 only; AO-06 remains IN PROGRESS and is not Product Owner approved.
- Post-merge Registry truth cross-check: Asset 62 / Entity 13 / Relations 44 / Audit 78 / Formal SHOT 0 / COSTUME 0 / PROP 0 / live USES_REFERENCE 0.
- Project Control advanced to R054 and end-of-day state is `PAUSED / RESUME SAME D-069`.
- Current hard evidence gap: approved A04 binary is not materialized in current Runtime Registry.
- Historical A-Series registration indicates a likely legacy Shot migration/recovery gap; do not regenerate A04.
- Neil Costume/Cross modeling boundary was questioned by Product Owner today; no new model decision locked. Review next session before creating any new visual Asset.
- P1 Wave 2 remains HOLD; P0.3 remains QUEUED; D-070 remains unallocated.
- Daily cross-file consistency closeout recorded in `gates/P0_2_visual_assets/daily_closeout_2026-09-18.md`.


## 2026-09-18｜D-069 Review Patch 01

- Corrected R053 nested checkpoint/AO-06 state; resume remains the same D-069 after evidence is supplied.
- Recorded PR #10 / `codex/a04` / review-start remote head `351a41b9452eafc01e724fd6f36f9edb6793c627`; PR remains open and must not be merged.
- Enforced Character Sheet `resolver_usage != NEVER`, exact A04 evidence `DEFAULT/DEFAULT`, and Schema V0.3 `created_by_event_id` relation/audit cross-reference.
- No live Registry mutation and no live `USES_REFERENCE` write.


## 2026-09-18｜D-069 AO-06 Stage 3 first-run engineering checkpoint

- Baseline `0208a31f...` / R052 verified; 68 tests / OK.
- Added executable A04 spec, fail-closed resolver/package, immutable use-record and reverse audit, plus isolated `USES_REFERENCE` transaction proof.
- Added Costume/Prop semantic Entities only; no visual Asset was fabricated.
- Search found no provenance-verifiable approved A04 binary and no dedicated approved Costume/Cross reference.
- Truthful state: `ENGINEERING FOUNDATION COMPLETE / BLOCKED_ON_APPROVED_A04_BINARY / BLOCKED_ON_COSTUME_PROP_EVIDENCE`; `generation_allowed=false`; no live `USES_REFERENCE`.


## 2026-09-18｜AO-06 Stage 2 Product Owner Approval

Status: `APPROVED / D-069 STAGE 3 NEXT`

- Product Owner 明确批准 `AO-06 Stage 2｜A04 Real Shot Spec V0.1 + Resolver Contract`。
- A04 executable Shot Spec structure 正式锁定。
- Required resolved anchors：`CHAR_NING_QIUSHUI / AST_IMG_000060`、`CHAR_NEIL / AST_IMG_000059`、`SCENE_CASTLE_ENTRANCE / DAY_DOOR_OPEN / AST_IMG_000052`。
- Required current gaps：`COSTUME_NEIL_DEFAULT`、`PROP_NEIL_CROSS`；任一 required gap 存在时必须 `generation_allowed=false`。
- White pocket handkerchief 锁定为 `COSTUME_NEIL_DEFAULT` required component，不建立独立 fabricated Prop。
- Exact Shot photography 必须来自真实 approved A04 source evidence，不得从 Scene Master 或聊天记忆猜测。
- Historical A04 不允许重建/补造历史 `USES_REFERENCE`。
- AO-06 当前真实 use 必须进入 immutable validation use record；live `USES_REFERENCE` 只允许指向真实、可证明输入的已批准 formal output。
- Product Owner 授权下一 Codex 工程任务编号：`D-069`，用于 AO-06 Stage 3 implementation + real validation。
- P1 Wave 2 / P0.3 继续 HOLD / QUEUED。

## 2026-09-18｜AO-06 Stage 2｜A04 Real Shot Spec + Resolver Contract Ready

Status: `READY_FOR_PRODUCT_OWNER_REVIEW`

- Stage 2 design follows Product Owner-approved Stage 1 without changing A04 narrative facts.
- A04 executable Shot Spec candidate separates required Characters, state-aware Scene, required Costume/Prop continuity, action semantics, negative-continuity boundary, and Shot-photography evidence.
- Current expected Resolver result:
  - `CHAR_NING_QIUSHUI → AST_IMG_000060 / RESOLVED`;
  - `CHAR_NEIL → AST_IMG_000059 / RESOLVED`;
  - `SCENE_CASTLE_ENTRANCE + DAY_DOOR_OPEN → AST_IMG_000052 / RESOLVED`;
  - `COSTUME_NEIL_DEFAULT → REFERENCE_GAP`;
  - `PROP_NEIL_CROSS → REFERENCE_GAP`.
- White pocket handkerchief is modeled as a required component of `COSTUME_NEIL_DEFAULT`, not a separate fabricated Prop.
- Any required REFERENCE_GAP blocks generation; no Character asset may silently satisfy a Costume/Prop requirement.
- Exact A04 Shot photography remains evidence-bound and may only be populated after the approved A04 source is materialized.
- Historical A04 provenance must remain honest: if A04 Shot Master is formalized with `provenance_status=PARTIAL`, no historical `USES_REFERENCE` relations may be backfilled from memory.
- AO-06 actual use will be captured in an immutable validation use record. `USES_REFERENCE` direction is locked candidate as `formal output SHOT asset → actual reference asset`; relation/reverse-query behavior can be tested in an isolated registry transaction without polluting live history. Live relation write requires a genuinely approved formal output with provable input use.
- No D-069 allocated by Stage 2 design.

## 2026-09-18｜AO-06 Stage 1 Product Owner Approval

Status: `APPROVED / STAGE 2 NEXT`

- Product Owner 明确批准 AO-06 Stage 1。
- Canonical validation Shot 锁定为 `A04`。
- A04 Scene requirement 锁定为 `SCENE_CASTLE_ENTRANCE / DAY_DOOR_OPEN`。
- Required Characters 锁定为 `CHAR_NING_QIUSHUI + CHAR_NEIL`。
- Neil default butler costume、cross、white handkerchief 被确认是 AO-06 的 Costume/Prop continuity requirements；当前正式 Runtime 仍无 `COSTUME_*` / `PROP_*` assets，因此 Stage 2 必须显式处理 REFERENCE_GAP，不得冒充已正式化资产。
- A04 不承载 A05 的 `keys absent` insert fact；若未来需要，必须建模为 negative continuity / forbidden presence，而不是 fabricated Prop asset。
- Exact Shot photography 仅能来自 approved A04 evidence；不得从 Scene Master 或 chat memory 推断为正式 camera metadata。
- Stage 2 next：`A04 Real Shot Spec V0.1 + Resolver Contract`。
- No D-069 allocated.

## 2026-09-18｜AO-06 Stage 1｜A04 Selection + Fact Boundary Ready

Status: `READY_FOR_PRODUCT_OWNER_REVIEW`

- AO-06 Stage 1 compared A01–A07 and recommends canonical Shot `A04`.
- A04 is preferred because it covers two Characters + state-aware Castle Entrance + Neil Costume/Prop continuity without A01 crowd complexity or A05 detail-insert over-specialization.
- Current Registry independently verified: `SHOT=0 / PROP=0 / COSTUME=0`.
- Formal anchors available now: `AST_IMG_000060 / CHAR_NING_QIUSHUI Reference Sheet`, `AST_IMG_000059 / CHAR_NEIL Reference Sheet`, `AST_IMG_000052 / SCENE_CASTLE_ENTRANCE / DAY_DOOR_OPEN`.
- Proposed A04 executable gaps: `COSTUME_NEIL_DEFAULT`, `PROP_NEIL_CROSS`; white pocket handkerchief treated as a required Costume component proposal. None are claimed formal yet.
- A04 does not inherit A05's “keys absent” insert fact. Any absence rule must be represented as negative continuity, not a fabricated Prop asset.
- Scene Facts vs Shot Photography boundary remains locked; camera/lens/composition cannot be invented from the Scene Master or chat memory.
- No D-069 allocated; no Registry/Relation/Audit production mutation performed.

## 2026-09-18｜AO-05 Final Product Owner Acceptance

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`

- Product Owner 于 2026-09-18 明确批准 AO-05 最终验收。
- Primary single-reference Delivery Path 已 PASS；Fallback Artifact Bridge 已完成 RUN A / RUN B 多 reference + repeatability 真实验证。
- 两轮均使用同一 formal input set：`AST_IMG_000056 / 000011 / 000009 / 000008`，4/4 SHA match，loaded_reference_count=`4`，proof generated，manual Product Owner reference upload=`0`。
- 所有 proof 均为 `NON-PRODUCTION`；未 ingest、未登记 Asset ID、未改变 Character Core Coverage。
- D-069 未分配；AO-05 不需要额外 Codex 工程任务即可完成 DoD。
- 残余审计限制：image-generation service 当前不返回独立 consumed-input SHA / cryptographic receipt。Product Owner 明确接受该限制为 non-blocking residual audit risk，并要求未来能力允许时补齐。
- 该限制登记为 `RISK-002 / ACCEPTED / NON-BLOCKING / DEFERRED IMPROVEMENT`。
- 临时 `.github/workflows/ao05-fallback-artifact-bridge.yml` 在 AO-05 closeout 中删除；已生成 artifact 按 GitHub retention policy 自动过期。
- AO-06 成为下一正式任务；P1 Wave 2 与 P0.3 继续 HOLD / QUEUED。
- Closeout evidence：`docs/project_control/gates/P0_2_visual_assets/ao05_closeout_2026-09-18.md`。

## 2026-09-18｜AO-05 Fallback Robustness Proof｜PASS

Status: `ROBUSTNESS PASS / READY_FOR_FINAL_PRODUCT_OWNER_ACCEPTANCE`

- Work 自动下载 GitHub Actions artifact `10536850548`；Product Owner 未手工下载或上传 reference。
- Received ZIP bytes: `9,094,747`.
- ZIP SHA256 independently verified: `a0923387923798a77ea02837e2f7eb3917ac45360e523d06345fccba8b2fb65d`.
- Environment: `ChatGPT Work / built-in image generation`.
- RUN A exact inputs: `AST_IMG_000056 / 000011 / 000009 / 000008`; 4/4 binaries materialized; 4/4 SHA matched; loaded_reference_count=`4`; proof `AO05_FALLBACK_MULTIREF_RUN_A` generated; manual Product Owner reference uploads=`0`.
- RUN B independently re-read the same ZIP, extracted to an independent directory, recalculated all four hashes, confirmed the same four Asset IDs and SHA values, loaded_reference_count=`4`, and generated `AO05_FALLBACK_MULTIREF_RUN_B`; manual Product Owner reference uploads=`0`.
- `input_set_identical_between_runs=YES`.
- `multi_reference_delivery=PASS`.
- `repeatability=PASS`.
- Both proofs are `NON-PRODUCTION`; neither was ingested or registered; Core Coverage unchanged.
- No GitHub / Registry mutation occurred in Work; D-069 remains reservation-only and was not allocated.
- Evidence boundary: image generation did not emit an independent input-SHA receipt; evidence is canonical GitHub runner verification + artifact digest + Work-side independent byte/SHA validation + actual four-reference generation calls.
- Two consecutive successful runs prove repeatability for this validated path; they do not assert indefinite long-term service stability.
- AO-05 remains `IN PROGRESS` until explicit Product Owner final acceptance.

## 2026-09-18｜AO-05 Fallback Artifact Bridge｜READY

Status: `FALLBACK ARTIFACT READY / WORK ROBUSTNESS VALIDATION PENDING`

- Product Owner authorized establishment of AO-05 Fallback Artifact Bridge.
- Temporary workflow created at `.github/workflows/ao05-fallback-artifact-bridge.yml`.
- Initial workflow revision had a YAML block-scalar syntax error and failed before jobs started; it was corrected immediately without any production mutation.
- Corrected workflow commit: `775238d05278af963d6e673063ce71ae522c18d1`.
- Successful workflow run: `35319662012`.
- Bundle ID / artifact name: `AO05_GUANG_YONG_DELIVERY_BUNDLE_V001`.
- Artifact ID: `10536850548`.
- Artifact size: `9,094,747 bytes`.
- Artifact ZIP digest: `sha256:a0923387923798a77ea02837e2f7eb3917ac45360e523d06345fccba8b2fb65d`.
- Artifact expires: `2026-09-25T07:29:39Z`.
- Source set exactly: `AST_IMG_000056 / 000011 / 000009 / 000008`.
- GitHub runner verified Registry identity/state, canonical file existence, exact SHA256 and byte size for all 4; copied bundle bytes were re-hashed; a second pre-upload verification passed `4/4 exact binaries`.
- Bundle contains 6 files: 4 visual references + `delivery_manifest.json` + `WORK_HANDOFF.md`.
- No Product Owner reference upload was required; no Registry or formal Asset mutation occurred; D-069 remains unallocated.
- Next validation occurs in Work: artifact download/materialization → manifest + byte verification → multi-reference RUN A → independent repeatability RUN B.

## 2026-09-18｜AO-05 Multi-reference Robustness Proof｜CANONICAL_BINARY_MATERIALIZATION_FAILED

Status: `FAIL CLOSED / FALLBACK REQUIRED / AO-05 REMAINS IN PROGRESS`

- Work 读取 main 四份事实源并确认 R044 / ROBUSTNESS VALIDATION PENDING。
- RUN A 在 binary acquisition 阶段停止；generation environment 未调用。
- `AST_IMG_000056`：GitHub file API 返回 Reference Sheet Base64；本轮未以统一多文件路径完成 materialization / SHA receipt。
- `AST_IMG_000011 / AST_IMG_000009 / AST_IMG_000008`：file API 返回空 binary content / metadata only；blob read 触发 UnicodeDecodeError；raw blob path 被 UTF-8-only interface 拒绝。
- 因无法取得四张可独立哈希的 bytes，`sha256_verified=0/4`，`loaded_reference_count=0`，proof 未生成。
- RUN B：NOT STARTED，因此 repeatability 未测试。
- Product Owner manual reference upload count = `0`；未通过人工上传规避失败。
- 失败边界明确定位为 Work 当前 GitHub binary materialization transport；不等于 multi-reference image generation unsupported。
- 未修改 GitHub/Registry/正式 Asset；未分配 D-069；AO-06 / P1 Wave 2 / P0.3 均未启动。
- 下一步采用 AO-05 已预定义 fallback：`GitHub Actions → short-lived manifest-verified Delivery Bundle artifact → Work`。

## 2026-09-18｜AO-05 Primary Delivery Path Proof｜PASS

Status: `PRIMARY DELIVERY PATH PASS / ROBUSTNESS VALIDATION PENDING`

- Work 读取 GitHub main / Project Control，确认 source revision R043 / AO-05 DESIGN IN PROGRESS。
- 验证对象：`AST_IMG_000056 / CHAR_GUANG_YONG_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`。
- GitHub / Registry 独立事实：`APPROVED / CURRENT / DERIVED / DEFAULT`；canonical path 正确；byte_size=`475761`；SHA256=`2a98e74ddba60a259758643b56ffddafd5a7cb30de040880f991fb47216b45fb`。
- Work 从 GitHub 自动 materialize 正式 PNG，无 Product Owner 手工挑图或上传。
- Work receipt：received byte size `475761`，received SHA256 与 expected 完全一致。
- 正式 reference binary 已通过 Work 的 image-production path 作为真实视觉参考输入，并成功生成 `AO05_DELIVERY_PROOF_ONLY`。
- Proof 明确为 `NON-PRODUCTION`；未进入 Asset Registry；未改变 Core Coverage；未启动 P1 Wave 2。
- Product Owner manual reference file upload count = `0`。
- 能力边界：单文件路径已证明；生成服务未给出独立 input-SHA receipt，因此证据链为 GitHub canonical bytes + Work 本地 SHA 核验 + 实际 reference path 调用 + proof generation。
- 尚未验证 multi-file delivery 与 repeated-run stability；AO-05 不标记 COMPLETE。
- D-069 仍 `RESERVATION ONLY / NOT ALLOCATED / NOT EXECUTED`。

## 2026-09-18｜AO-05 Delivery Bridge Design Start

Status: `DESIGN IN PROGRESS / CHAT / NO D-NUMBER ALLOCATED`

- Product Owner 明确启动 AO-05。
- AO-05 继续遵守既有完成标准：Reference Package 必须稳定进入实际 image-production / generation environment；输入 Asset ID / version / SHA 可追踪；减少 Product Owner 逐张挑图、上传和搬运；不得把仍需人工的环节描述为自动化完成。
- 本阶段先由 Chat 完成 Delivery Bridge V0.1 设计，不分配 D-069。
- 设计原则：AO-05 不新增 Resolver 选图权威，不修改 AO-04 Formal Assets；Delivery Bridge 只消费既有 Resolver / Reference Package 输出并负责可验证交付。
- 当前无 blocker；AO-06、P1 Wave 2、P0.3 继续保持原有 HOLD / PENDING / QUEUED 边界。

## 2026-09-18｜AO-04 Final Product Owner Acceptance

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`

- Product Owner 于 2026-09-18 明确批准 AO-04 最终验收。
- 最终 DoD 基线：9 个 Character Entity；9 张 formal Derived Character Reference Sheets；42 个实际 Atomic dependencies；21 个明确 `REFERENCE_GAP`；63 个 Tier Core slots。
- Formal Asset IDs：`AST_IMG_000054–AST_IMG_000062`。
- Stage B publication commit：`09b9e2c44f8f2f78c1d102f3d141263074316310`，已 remote verified。
- 9 张 canonical PNG 与已批准 Candidate SHA / byte size 一致；全部 dependency status `FRESH`；Resolver 9/9 RESOLVED；Single Current 与 idempotency 验证通过。
- 完整仓库回归：`68 tests / OK`。
- AO-04 不改变 Character Core Coverage：`42/63 = 66.7%`；`REFERENCE_GAP=21`。
- 临时 D-068 Stage A review workflow 与 Stage B publication workflow 在最终验收后删除，避免进入最终 merge。
- AO-05 成为下一正式任务，但尚未启动；AO-06 仍 PENDING；P1 Wave 2 继续 HOLD；P0.3 继续 QUEUED。
- Completion evidence：`docs/project_control/gates/P0_2_visual_assets/ao04_closeout_2026-09-18.md`。

## 2026-09-18｜D-068 Stage B Engineering Complete / Remote Verified

- Product Owner 已于 2026-09-18 视觉批准全部 9 张 Stage A Candidate Character Reference Sheets，并授权 Stage B。
- GitHub Actions workflow `D-068 Stage B Publication`（run `35308216933`）在真实 `codex/ao-04` 分支执行并成功完成。
- Stage B publication commit：`09b9e2c44f8f2f78c1d102f3d141263074316310`；PR #9 远端 head 已独立核对为同一 SHA，PR 保持 OPEN / NOT MERGED。
- 同一 formal transaction commit 原子发布 12 个文件：9 张 canonical formal PNG + `asset_registry.jsonl` + `asset_relations.jsonl` + `audit_event_log.jsonl`。
- 正式结果：Asset Registry `62` 条；其中 AO-04 formal `DERIVED_REFERENCE=9`（`AST_IMG_000054–000062`）；AO-04 `DERIVED_FROM=42`；D-068/AO-04 `ASSET_FORMALIZED=9`。
- 9 张正式 PNG 的 SHA256 / byte size 与 Product Owner 已批准 Candidate manifests 逐一一致；Character Core Coverage 保持 `42/63 = 66.7%`，`REFERENCE_GAP=21`，未生成任何新人物视角。
- 9 张 Sheet 均验证为 `CURRENT / APPROVED / DERIVED / DEFAULT`，dependency status 全部 `FRESH`，Character Reference Sheet Resolver 9/9 RESOLVED。
- Idempotency：第二次执行 formalizer 返回 `ALREADY_FORMALIZED`，Registry / Relations / Audit / 9 PNG hashes 无变化。
- 完整仓库回归：`68 tests / OK`。
- Binary publication blocker 已解除。AO-04 仍保持 `IN PROGRESS`，当前状态为 `STAGE B ENGINEERING COMPLETE / REMOTE VERIFIED / READY_FOR_FINAL_PRODUCT_OWNER_ACCEPTANCE`。
- 未启动 AO-05；D-069 仍为 reservation only；P1 Wave 2 继续 HOLD；P0.3 继续 QUEUED；PR #9 不得 merge，等待 Product Owner 最终 AO-04 DoD 验收。
- Completion evidence：`docs/project_control/gates/P0_2_visual_assets/d068_stage_b_engineering_complete_2026-09-18.md`。

## 2026-09-18｜D-068 Stage B authorization and publication preflight

- Product Owner visually approved all 9 Stage A Candidate Sheets and authorized D-068 Stage B.
- Rehydration preflight passed: `9 manifests / 9 PNGs / 9/9 filename / 9/9 SHA256 / 9/9 byte size / 42 dependencies / 21 REFERENCE_GAP / 63 slots`.
- Stage B stopped before formalizer execution because the recorded Codex PR publisher cannot publish the nine required canonical formal PNG binaries and this checkout cannot verify supplied remote head `ebed801fdc5b35ceb000516b7352fd7241ceebf5`.
- Status: `BLOCKED_ON_FORMAL_BINARY_PUBLICATION`. D-068 formal state remains `DERIVED_REFERENCE=0 / DERIVED_FROM=0 / D-068 ASSET_FORMALIZED=0`; no prospective Asset ID was allocated.
- The temporary Candidate review workflow remains present because cleanup is authorized only after successful Stage B formalization and validation.
- AO-04 remains `IN PROGRESS`; D-069 remains reservation-only; AO-05 remains not started; PR #9 remains `OPEN / DO NOT MERGE`.
- Blocker evidence: `docs/project_control/gates/P0_2_visual_assets/d068_stage_b_formal_binary_publication_blocker_2026-09-18.md`.

## 2026-09-18｜D-068 Stage A Review Patch 01

- Continued the existing D-068 / AO-04 Stage A task; D-069 remains reservation-only and was not allocated or executed.
- Enforced `variant=DEFAULT` and `state=DEFAULT` in Atomic Candidate input selection, with negative regression coverage for non-default required-role rows, duplicate/default-slot ambiguity, and false Core-slot satisfaction.
- Complete repository suite: `68 tests / OK`.
- Rebuilt all 9 Candidate PNGs into a temporary review directory without overwriting the locked baseline: `9/9 SHA256 MATCH`; `42 selected dependencies / 21 explicit REFERENCE_GAP / 63 Tier Core slots`.
- Formal registry remains unchanged: `DERIVED_REFERENCE=0 / DERIVED_FROM=0`. AO-04 remains `IN PROGRESS`; Stage B and AO-05 were not started.
- Final state: `D-068 STAGE A ENGINEERING CLEAN / WAITING_PRODUCT_OWNER_VISUAL_APPROVAL / PR #9 OPEN / DO NOT MERGE`.

## 2026-09-17｜D-068 AO-04 Stage A engineering

- Project Control advanced `R039 → R040`; Dashboard advanced `V018 → V019`.
- AO-04 state: `IN PROGRESS / AO-04A PRODUCT OWNER APPROVED / D-068 STAGE A ENGINEERING COMPLETE / WAITING_PRODUCT_OWNER_VISUAL_APPROVAL`.
- Registered exactly nine stable Character Entities and appended nine `ENTITY_CREATED` audit events; both existing Scene Entities remain unchanged.
- Live preflight reconciled exactly `42 / 63` selected Atomic Core dependencies and `21` explicit gaps.
- Generated exactly nine deterministic, non-generative Candidate PNGs plus manifests outside the Formal Asset Registry.
- Implemented computed `FRESH / DEPENDENCY_STALE`, separate derived-reference resolution, fail-closed Stage B formalizer, and AO-04 tests. Full suite: `66 tests / OK`.
- No formal Derived Asset IDs or `DERIVED_FROM` relations were created. Stage B was not executed.
- AO-05 remains PENDING; P1 Wave 2 remains HOLD; P0.3 remains QUEUED.
- Publication transport boundary: Candidate PNG binary files are `CLOUD_REVIEW_ARTIFACT / NOT FORMAL ASSET / NOT INCLUDED IN STAGE A PR DUE TO CODEX PR BINARY TRANSPORT LIMITATION`. The nine PNGs remain byte-identical in the Codex Cloud workspace for Product Owner visual review; their filenames, expected logical paths, SHA256, byte sizes, dependency lineage, populated slots and explicit gaps remain recorded in the nine version-controlled manifests. This transport boundary does not alter Candidate approval status, dependency lineage, AO-04A authority, or the mandatory Product Owner approval stop.
本文件记录实际工程执行结果。只保留足以追溯结论的关键事实、证据、失败原因和最终结果；完整脚本、媒体文件、Commit 和工程资产由 GitHub / Local project 保存。

## Restart Baseline｜2026-09-11

- 项目进入 P0｜项目重启与基础能力再验证。
- 通过 `arch3d-reconstruction` 的 Project Control System 2.0 作为参考，继承 SSOT / Gate / Decision / Execution / Acceptance / Dashboard 派生化的管理思想。
- 旧《黑衣夫人》工程执行历史不在本次雏形中重写；后续只迁移仍会影响当前生产判断的必要事实。

## Historical Carry-forward｜PRE-AUDIT

以下只作为重启审计输入，不等于新的正式 Gate 结论：

- 历史 Codex 工程编号已到 D-056。
- D-056｜SOURCE_AUDIO_INDEX_V001 已建立原音频导航索引；历史使用证明不能直接把 ASR segment 时间边界当正式剪辑边界。
- A01–A07 存在已批准静态视觉版本；是否进入最终镜头序列待重新验证。
- A08_REBOOT 当前保持 HOLD。
- Remotion 已验证能够完成静态图、音频、帧级时间线到 MP4 的工程合成；过往 Animatic / 剪辑结果未达到成片要求。

## Current Execution State

- P0.1：PASS / PRODUCT OWNER APPROVED
- P0.2：ACTIVE / APPROVED-OPEN CLOSEOUT / AO-01 + AO-02 + AO-03 + AO-07 COMPLETE / AO-04 NEXT
- P0.3：QUEUED / DO NOT START EARLY
- 当前实际 Codex 工程编号：D-067；D-067 已 `COMPLETE / REMOTE VERIFIED / PRODUCT OWNER APPROVED`
- 下一 Codex 工程编号仅在新的 Codex 工程任务实际启动时使用：D-068；本次 Project Control consistency closeout 不占 D-###
- RISK-001：CONTROLLED / MITIGATION VERIFIED
- P1 Wave 2：HOLD UNTIL AO-04～AO-06 COMPLETE / VERIFIED
- TEMP_CLOUD_ONLY_MODE_V1：APPROVED / EFFECTIVE / TIME-BOXED THROUGH 2026-09-20
- Current formal task：AO-04｜9 Derived Character Reference Sheets + dependency/staleness｜NEXT

## AO-03 Product Owner Closeout｜2026-09-17

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`

Execution route: `CHAT REVIEW + GITHUB MERGE + PROJECT CONTROL CLOSEOUT / NO NEW D-NUMBER`

- AO-03 final DoD reviewed against approved AO-03A/B contract and D-067 implementation.
- `SCENE_CASTLE_ENTRANCE` and `SCENE_FIRST_HALL` verified as executable Stable Scene Entities.
- `AST_IMG_000052` and `AST_IMG_000053` verified as approved/current/master Scene Masters with source SHA preserved.
- Scene Facts / controlled State / Shot-variable Photography separation verified.
- State-aware Resolver verified to resolve DAY+OPEN and FIREPLACE_EXTINGUISHED and return `REFERENCE_GAP` for CLOSED / NIGHT / BURNING / missing-state / explicit-vs-UNSPECIFIED mismatches.
- D-067 full regression evidence: `54 tests / OK`; no implementation or regression blocker remained.
- Product Owner explicitly approved AO-03 on 2026-09-17.
- GitHub PR `#6｜AO-03: add executable Scene registry and state-aware resolver` merged.
- Merge SHA：`b16ffdd5f1c57f0b2c28acdee3caac656afb91a3`。
- Closeout evidence：`docs/project_control/gates/P0_2_visual_assets/ao03_closeout_2026-09-17.md`。
- Closeout evidence commit：`6d87401984b7dfe5f4a75db7b262f4fc684de9e5`。
- AO-03 final status：`COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`。
- P0.2 remains ACTIVE；P1 Wave 2 remains HOLD；P0.3 remains QUEUED。
- Next formal dependency：`AO-04 → AO-05 → AO-06`。

## D-067｜AO-03 Scene Registry + State-Aware Resolver｜ENGINEERING IMPLEMENTED / 2026-09-17

- Source checkout：`15ab19dd4c28257b47f7b6d79f852429ca772e7c`；work reference：`work`。
- 开始前确认 live Asset Registry 最大编号为 `AST_IMG_000051`；为两张既有 approved Scene Master 分配 `AST_IMG_000052`、`AST_IMG_000053`，未创建重复版本。
- 两个源 PNG 仅作 canonical rename / move，图像内容未修改；formalized SHA-256 分别保持 `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961` 与 `ce043c8adb244ce8f07a34f1a2b047b4d7ba41f72cdf777e3cd1877f4ac8b413`。
- 新增 executable Entity / Scene State Profile 数据；State facts 为多维显式字段，Shot Photography 只保留字段边界而不写入 Stable Scene Facts。
- Resolver 保留 Character migration/runtime、SHA、canonical path 与 Single Current 行为，并新增 Scene Master 显式 state subset match；NIGHT / CLOSED / BURNING / explicit-vs-UNSPECIFIED 均返回 `REFERENCE_GAP`。
- 完整测试：`python -m unittest discover -s tests -p 'test_*.py'` → `54 tests / OK`，覆盖既有 Character resolver、ingest、supersession、reference-package 与 AO-02 migration regression。
- 本节记录工程交付时的历史状态；AO-03 最终完成与 Product Owner 批准见上方 `AO-03 Product Owner Closeout｜2026-09-17`。

## Project Control Baseline Commit｜APPROVED / 2026-09-11

- Product Owner 批准 Dashboard V002。
- canonical repo 指定为 `wp5rrp7b2v-droid/black-lady-animatic-v01`。
- 本次 Project Control 建立属于项目管理落档，不占用新的 Codex D-###。

## Project Control Structure 1.1｜2026-09-12

- `docs/project_control/` 从平铺结构重构为 `core/`、`logs/`、`gates/`、`dashboard/`、`archive/`。
- `source_material/` 从 Project Control 中独立出来，用于正式源数据。
- 仓库已确认处于 Private 状态。
- 本次属于项目控制结构维护，不占用 Codex D-###。

## P0.1-04｜S1 Full Novel Lock｜COMPLETE / 2026-09-12

- Product Owner 指定当前上传的完整《诡舍》原文为唯一 S1 canonical source。
- 正式文件名：`S1_SOURCE_NOVEL_FULL_V001.txt`。
- 文件规格：UTF-8 plain text、BOM none、LF、6,480,028 bytes、2,289,031 characters。
- 章节标题范围：第1章至第1002章《新世界（结局）》；检测到 1001 个章节标题。
- SHA-256：`f9ec03ed71a9302b8811c0038a708f3323c1bfeadf1afdcbab498dd1df3b0e2e`。
- 源文件未检测到 `第461章` 标题；登记为 `SOURCE-NATIVE NUMBERING ANOMALY`，保持正文原样，不补写、不重编号。
- P0.1 当前推进至 P0.1-05：原始有声小说音频实体登记与 S3 转写/校验体系建立。

## AM Checkpoint｜2026-09-12｜PAUSED / RESUME AFTERNOON

上午阶段工作已完成并在此收口，下午从 P0.1-05 继续，不回退重做已完成步骤。

### 1. Project Control / Repo

- `docs/project_control/` 已完成 Structure 1.1 重构：`core/`、`logs/`、`gates/`、`dashboard/`、`archive/`。
- 正式源数据与 Project Control 分离，进入仓库根目录 `source_material/`。
- canonical repo：`wp5rrp7b2v-droid/black-lady-animatic-v01`，Private。
- 本地正式工作目录：`/Users/caroline/诡舍/黑衣夫人/black_lady_short_01`。
- 本地目录已完成迁移并重新与远程 `main` 对齐。

### 2. Local Git cleanup / network handling

- 仓库级 `.gitignore` 已加入 `.DS_Store`，避免 macOS 元数据污染版本库。
- 本地 commit 已正常 rebase 到远程最新 Project Control 基线并 push。
- GitHub HTTPS 链路曾出现 443 timeout / `Empty reply from server` / `unexpected disconnect while reading sideband packet`。
- 当前仓库使用 `HTTP/1.1`；为提高上传稳定性，将 `http.postBuffer` 调整为 `16777216`（16 MiB）。
- 最终 S1 push 成功；本轮网络问题不再作为当前 blocker。

### 3. S1 canonical source

- `S1_SOURCE_NOVEL_FULL_V001.txt` 已完成 canonical lock。
- 本地与 GitHub `main` 正式路径：`source_material/S1_novel/S1_SOURCE_NOVEL_FULL_V001.txt`。
- GitHub 远程文件大小核验：6,480,028 bytes。
- GitHub blob SHA：`f089b5d63ded4be6f90af0ad845f6fdaa4959b84`。
- S1 正文已真正进入远程仓库，不再只是元数据登记。
- P0.1-04：COMPLETE。

### 4. Source baseline at checkpoint

- S1：CANONICAL / LOCKED / REMOTE VERIFIED。
- S2：CANONICAL / LOCKED。
- S3：NOT ESTABLISHED。
- 原始有声小说音频：已知存在，但 canonical 文件名、路径、格式、时长、SHA-256 尚未登记。
- D-056 `SOURCE_AUDIO_INDEX_V001`：仅作为导航索引，不作为正式剪辑时间边界。

### 5. Gate / blocker / hold

- P0.1：ACTIVE / BUILDING。
- P0.2：QUEUED。
- P0.3：QUEUED。
- Overall Gate Progress：0 / 3 PASS。
- 当前 blocker：NONE。
- A08_REBOOT：继续 HOLD。
- 新 Codex D-###：NONE；如后续需要工程执行，下一编号仍为 D-057。

### 6. Resume point

下午唯一恢复点：

`P0.1-05｜登记原始有声小说音频实体，并建立 S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001 的结构、验证等级与小样校验方法。`

恢复顺序：

1. 盘点《黑衣夫人》原始有声小说音频文件；
2. 锁定 canonical 音频实体：文件名、格式、时长、SHA-256、存储路径；
3. 选取一小段真实音频；
4. 建立 S3 数据结构；
5. 对小样进行真实音频逐段校验；
6. 再判断 P0.1 是否达到 PASS 条件。

## PM Scope Lock｜2026-09-12｜MVP1 Start = S2 Chapter 134

- Product Owner 明确：第一个 MVP 的正式故事起点从 S2 第134章《【黑衣夫人】参观》开始。
- 第133章不进入 MVP1 正式成片，只保留为前置语境。
- 因此 P0.1-05 不再以“准备完整《黑衣夫人》全部有声书”为前提，而改为先建立服务 MVP1 的原音获取、准备、登记、转写与校验能力。
- 历史 `ScreenRecording_09-08-2026_21-33-06_audio.m4a` 经核验为 2,636,183 bytes、195.844989 sec、AAC 2ch 44.1kHz，SHA-256=`abaaab1c0c8362e6d61268ba09b0f0ce6cb915cf49c046fd3b32c49405746551`；Product Owner 确认其仅为测试片段。
- 上述音频正式降级为 `NON-CANONICAL TEST AUDIO`，不得作为 MVP1 canonical audio baseline。

## PM Audio Capture Verification｜2026-09-12｜MVP1 crosses into Chapter 135

- Product Owner 提供新的正式候选录屏：`ScreenRecording_09-12-2026 13-40-39_1.MP4`。
- RAW_CAPTURE 规格：235,987,834 bytes；381.958333 sec；视频 H.264 1284×2778 / 60fps；音频 AAC 2ch / 44.1kHz；SHA-256=`9bab514775f0771987b094cdd9394b81d6a49a7bace995ef9ad4dbcce448abd1`。
- 录屏画面确认对应有声小说 `097【黑衣夫人】主人`。
- 录屏开头显示“欢迎各位来到艾伦古堡”等内容，与 S2 第134章开头一致。
- 对照录屏画面与 S2：约在有声小说播放器 05:05–05:10 左右，内容已由第134章进入第135章开头；后续出现黑裙、黑色高跟鞋、红色指甲油、莫妮卡夫人入座等第135章早段内容。
- 录屏末段约播放器 06:20，已经到莫妮卡夫人入座、众人开始跟随入座附近。因此 MVP1 的实际内容跨度不是“第134章 only”。
- 已从 RAW_CAPTURE 中以 stream copy 方式无重编码提取原 AAC 音轨：`AUDIO_MVP1_CAPTURE_EXTRACT_V001.m4a`。
- RAW_AUDIO_EXTRACT 规格：5,244,616 bytes；381.941995 sec；AAC 2ch / 44.1kHz；SHA-256=`d9a297b275a2fc42b85fa7b26407c4824c17efc63d1b9d148470f224d96be7f2`。
- 当前状态：`RAW_AUDIO_EXTRACT / CANONICAL CANDIDATE`。由于录屏本身可能含极短的起止操作冗余，尚未直接晋级为 `CANONICAL_AUDIO`。
- 正式范围规则修正：MVP1 从 S2 第134章开头起，终点按真实有声小说连续音频边界锁定；原文章节只作为内容映射锚点。当前映射终点在 S2 第135章开头。
- 下一步：锁定 canonical audio 的精确起止内容与时间码，再建立覆盖该完整音频跨度的 S3。

## P0.1 Final Closeout｜2026-09-12｜PASS / PRODUCT OWNER APPROVED

- `AUDIO_MVP1_CANONICAL_V001.m4a` 完成正式边界锁定；起点完整保留“欢迎各位来到艾伦古堡”，终点完整保留“而后又匆匆离去备餐”。
- S3 `S3_SOURCE_AUDIO_BL_TRANSCRIPT_V001.csv` 建立完整 MVP1 searchable index：41 segments，其中 9 VERIFIED、32 REVIEWED searchable entries。
- 开头 / 中段 / 后段检索抽查均可唯一命中正确候选原音区域。
- Product Owner 明确批准 P0.1 正式 PASS；精确 shot-driven audio retrieval / extraction 转入 P0.3。

## P0.2 Character Asset System Build｜2026-09-13

### D-059｜Character Asset Migration V1

Status: `COMPLETE / REMOTE VERIFIED`

- 48 张 approved Character PNG 迁入 `production/image_library/character_references/`。
- CSV + JSON Migration Manifest 发布到 `docs/project_control/gates/P0_2_visual_assets/migration_evidence/`。
- Remote commit: `d9fb763fb63e57023aa2cf11119c9be1bef037d6`。
- Neil `rear_turn_45` legacy asset 保持 `MAPPING_REQUIRED / NOT MIGRATED`。

### D-060｜Reference Package Exporter V0.1

Status: `TEST APPROVED / PRODUCT OWNER APPROVED`

- 测试对象：`CHAR_NING_QIUSHUI → PROFILE_LEFT`。
- 自动选出 `FACE_FRONT / PROFILE_RIGHT / FACE_3Q_RIGHT / BODY_FRONT`。
- 4/4 SHA source/copy/manifest PASS；正确识别目标 `PROFILE_LEFT = REFERENCE_GAP`。
- 验证结论：`Canonical Character Assets → automatic selection → local Reference Package` 成立。
- Approval record commit: `7142ddf9c82c63f0a479f56d57de9e2996b540de`。

### Automatic Ingest Controller V0.1｜First Live Ingest

- Automatic Ingest Controller 与 Runtime Registry 建立并投入真实 Character asset ingest。
- 首个真实资产：`CHAR_NING_QIUSHUI_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`。
- Asset ID：`AST_IMG_000049`；首次 ingest commit：`65e7fbec9acbe970797479ae523abf9f9e4f55df`。
- Registry 写入 `APPROVED / CURRENT / AUXILIARY / DEFAULT`；Audit 写入 `ASSET_APPROVED + ASSET_INGESTED`。
- 后续发现该 V001 画幅不符合项目 9:16 Character reference 标准，因此保留历史记录但不作为最终现行版本。

### D-061｜One-click Character Ingest + Cleanup

Status: `COMPLETE / REMOTE VERIFIED`

- 提供 `Black_Lady_Ingest.command` 一键入口；Product Owner 确认后选择 canonical PNG，即可调用 controller 完成正式 ingest。
- 加入 Reference Package cleanup、staging safety、dry-run/network boundary 等保护。
- Commit: `200cb06ce366c650b4f1389108765996b8f15332`。

### D-062｜P1 Character Reference Package Generalization

Status: `COMPLETE / REMOTE VERIFIED`

- Exporter 泛化至 P1 `PROFILE_LEFT / PROFILE_RIGHT / REAR_3Q_LEFT / REAR_3Q_RIGHT`。
- opposite-side 仅作为 reference selection，不允许 silent mirror inference。
- Commit: `a480dc0a64b2e63221122dce238d5c35634a77b1`。

### D-063｜Unified Migration + Runtime Character Asset Resolution

Status: `COMPLETE / REMOTE VERIFIED`

- Migration Manifest 与 Runtime Registry 统一进入 Character current/reference resolution。
- Runtime 新资产可立即参与 Current detection / reference selection。
- Exact duplicate 跨源时仅同 filename/version/SHA 允许 runtime wins；不同 Current 仍视为冲突。
- Commit: `e85f749ef72fb722c631472eb0af8bb2b0b7bc7e`。

### D-064｜Controlled Current Supersession

Status: `COMPLETE / REMOTE VERIFIED`

- 新增受控 CURRENT 替换能力；必须同时显式满足 `--supersede-current` 与 `--po-approved`。
- 正常 ingest 发现已有 CURRENT 仍默认 BLOCK。
- Supersession 写入 Registry lifecycle 更新、`NEW SUPERSEDES OLD` Relation、Audit `ASSET_SUPERSEDED`，旧文件保留。
- Commit: `6735c44374713d7470888dfb4d20e52af804cb42`。

### Ning PROFILE_LEFT V002｜Real Controlled Supersession

- GitHub HTTPS 初次运行出现 `Empty reply from server`；进一步测试发现默认 HTTP/2 链路报 `curl: (16) Error in the HTTP2 framing layer`。
- 对该仓库切换 Git HTTP/1.1 后链路恢复；网络问题不再作为 blocker。
- `CHAR_NING_QIUSHUI_PROFILE_LEFT_DEFAULT_DEFAULT_V002.png` 正式 ingest：`AST_IMG_000050`。
- V002 设为 CURRENT；V001 `AST_IMG_000049` 转为 SUPERSEDED。
- Supersession commit: `eba06283cccd10a22addd02307c9012cc06d3ac0`。

### D-065｜macOS Bash Launcher Fix

Status: `COMPLETE / REMOTE VERIFIED`

- 真实普通新增路径暴露 macOS Bash 3.2 + `set -u` + empty array expansion：`supersede_args[@]: unbound variable`。
- 修复方式：保留 `set -u`，拆分 CURRENT_FOUND supersede 与 NO_CURRENT normal ingest 两条明确 controller 调用路径。
- macOS `/bin/bash` NO_CURRENT / SUPERSEDE runtime 均 PASS；controller regression 10 项 PASS。
- Commit: `57495a7b0a9e189098e2b8310e76d98f7b0beb2d`。
- 全量 39 项测试存在 1 项既有 Resolver assertion failure：测试仍期待旧 `AST_IMG_000049`，而合法 supersession 后 CURRENT 已为 `AST_IMG_000050`；该问题登记为 non-blocking stale test expectation。

### Ning REAR_3Q_LEFT V001｜Real Normal Ingest

- `CHAR_NING_QIUSHUI_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png` 正式 ingest 成功。
- Asset ID：`AST_IMG_000051`。
- 状态：`APPROVED / CURRENT / AUXILIARY / DEFAULT`。
- Audit：`ASSET_APPROVED + ASSET_INGESTED`。
- Commit: `a90854dee5f2cef736b622650a2120b22bc8279e`。

## P0.2-03｜P1 Wave 1 Closeout｜2026-09-13

Status: `COMPLETE / CONTINUE P1`

- 宁秋水 `PROFILE_LEFT`：COMPLETE；CURRENT = `AST_IMG_000050 / V002`。
- 宁秋水 `REAR_3Q_LEFT`：COMPLETE；CURRENT = `AST_IMG_000051 / V001`。
- Live Core Coverage：`42 / 63 = 66.7%`。
- Remaining Core View Gap：`21`。
- P1 progress：`2 / 10 complete`，`8 / 10 remaining`。
- 宁秋水 Tier A current coverage：`8 / 9`；剩余 `FACE_3Q_LEFT` 属于非当前 P1 target。
- 下一正式 P1 target：`CHAR_JUN_LUYUAN PROFILE_LEFT`，随后 `REAR_3Q_LEFT`。

## End-of-Day Engineering State｜2026-09-13

- P0.1：PASS / PRODUCT OWNER APPROVED。
- P0.2：ACTIVE / P1 CHARACTER GAP PRODUCTION。
- P0.3：QUEUED。
- 当前 Codex 工程编号已到 D-065；下一新的工程任务编号从 D-066 继续。
- Current blocker：NONE。
- 非阻塞技术债：Resolver regression test 仍写死旧 Asset ID；后续应改为断言当前有效版本语义。

## D-066｜AO-01 Four Registers Final Reconciliation｜2026-09-14

Status: `COMPLETE / PENDING_REMOTE_PUBLICATION`

- Four named legacy CSVs unavailable in current worktree, untracked files, and reachable Git history; no reconstruction. Baseline evidence commit `0bdb5798f4cd8c9ce82d4c9d9ae65d5a9503d67c` published to origin/main after an initial network failure.
- BL-D-028 locks all four out of Current authority; old-row orphan/duplicate/path/naming checks remain `UNKNOWN / SOURCE UNAVAILABLE`.
- Available 48 D-059 canonical PNGs and 3 Runtime PNGs verified; 39 tests pass; no duplicate Current. Current Shot Spec validation remains AO-06.
- Project Control cross-file closeout recorded; updated evidence publication and HEAD/origin-main verification still required. AO-02 not started; P1 Wave 2 HOLD.

### D-066｜AO-01 remote verification

- Product Owner decision and pending closeout commit `43d8fa4f8e4068298058f1aad0bc410193b6c0d3` pushed; fresh fetch confirmed `HEAD == origin/main`.
- AO-01 updated to `COMPLETE / VERIFIED` in Project Control revision R032. AO-02 remains NEXT / NOT STARTED; P1 Wave 2 HOLD.

## AO-02｜Legacy Character Assets → Long-term Registry / Audit｜2026-09-14

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`

Execution route: `CHAT + TERMINAL / NO CODEX D-NUMBER`

- AO-02 Design V1 was completed and locked in Chat before implementation.
- Dedicated migration controller: `scripts/legacy_registry_migration_controller_v1.py`.
- Automated tests: `tests/test_ao02_legacy_registry_migration.py`.
- Pre-apply dry-run: 48 eligible / 48 migrated planned; Single Current PASS; SHA/storage PASS; one provable SUPERSEDES relation.
- Formal migration backfilled `AST_IMG_000001–000048` for 48 D-059 `CONFIRMED + APPROVED` legacy Character assets.
- Existing Runtime `AST_IMG_000049–000051` preserved unchanged.
- Neil `CHAR_NEIL_REAR_TURN_45_SUPPLEMENTARY` remained `MAPPING_REQUIRED / NOT MIGRATED`。
- Post-migration counts: Asset Registry `51`; Asset Relations `2`; Audit Event Log `56`; migration map `48` rows + header.
- Character PNGs and D-059 CSV/JSON Manifest remained unchanged.
- Automated migration tests: `5/5 PASS` including deterministic mapping, rollback, partial-migration block, idempotency, and eligible-count guard.
- Real second run returned `ALREADY_APPLIED / NO CHANGE`.
- Migration commit: `4803b928baaa38d875e9c6edd46f4a458e627b61`.
- Terminal publication check: `FINAL_STATUS=REMOTE_VERIFIED`; GitHub main independently confirmed the same commit.
- Completion evidence: `docs/project_control/gates/P0_2_visual_assets/ao02_legacy_asset_registry_migration_v1.md`.
- Product Owner explicitly approved AO-02 on 2026-09-14.
- Project Control advanced to revision `R033`; AO-03 is NEXT; P1 Wave 2 remains HOLD.

AO-02 does not consume D-067. Per RC-015, only work actually executed by Codex consumes a D-### number.

## AO-07｜GitHub Network Resilience / Recovery Method｜2026-09-14

Status: `COMPLETE / VERIFIED / PRODUCT OWNER APPROVED`

Execution route: `CHAT + TERMINAL EVIDENCE + GITHUB CLOSEOUT / NO CODEX D-NUMBER`

- Existing dynamic helper `$HOME/.local/bin/git-proxy-auto` validated on the Black Lady repo.
- Real verification chain completed: `ls-remote` PASS → `pull --ff-only` PASS → `push` PASS → local HEAD / remote main SHA MATCH.
- HTTP/1.1 retained as safe fallback; dynamic proxy port is discovered at runtime and not persisted.
- AO-02 migration publication used the same connectivity path and reached `REMOTE_VERIFIED`.
- Real second migration run returned `ALREADY_APPLIED / NO CHANGE`, proving publication retry must not trigger re-ingest or duplicate Asset IDs.
- Formal lightweight Recovery Runbook completed with connectivity preflight and diagnosis order: DNS → HTTPS → remote → HTTP version → proxy/VPN → credential → repo reachability.
- `PENDING_REMOTE_PUBLICATION` entry/exit/recovery rules locked.
- Push ACK loss and remote mismatch handling locked; force push is prohibited for recovery.
- Controlled failure→recovery requirement satisfied by real transient incidents (`443 timeout`, `Empty reply from server`, HTTP/2 framing error, unexpected disconnect) followed by verified recovery/publication.
- Product Owner explicitly approved AO-07 on 2026-09-14.
- Decision: `BL-D-030`。
- Completion evidence: `docs/project_control/gates/P0_2_visual_assets/ao07_github_network_resilience_progress_v1.md`。
- `RISK-001` downgraded from OPEN to `CONTROLLED / MITIGATION VERIFIED`。
- Project Control advanced to revision `R034`; AO-03 remains NEXT; P1 Wave 2 is now blocked only by AO-03～AO-06。

AO-07 does not consume D-067. Per RC-015, only work actually executed by Codex consumes a D-### number.

## AO-03A｜Fact Boundary + Executable Spec Design V0.1｜2026-09-15

Status: `APPROVED / PRODUCT OWNER APPROVED`

Execution route: `CHAT DESIGN + GITHUB CLOSEOUT / NO CODEX D-NUMBER`

- Product Owner explicitly approved AO-03A on 2026-09-15; decision `BL-D-032`。
- Stable Scene identity locked as `SCENE_CASTLE_ENTRANCE` and `SCENE_FIRST_HALL`。
- Legacy/source aliases retained for traceability: `CASTLE_ENTRANCE_OPEN_DOOR_DAY` and `FIRST_HALL_FIREPLACE`。
- Controlled State dimensions include DAY/NIGHT, door OPEN/CLOSED and fireplace EXTINGUISHED/BURNING; State change does not create a new Scene identity。
- Scene Master locks Scene Facts, not Shot Photography; camera / shot size / focal length / blocking / occlusion / depth of field / local exposure / composition remain shot-variable。
- Costume / Prop executable model follows Entity / Asset / Variant / State; missing required eligible formal asset remains `REFERENCE_GAP`, not fabricated completion。
- AO-03 requires Runtime / Resolver + machine-verifiable tests; documentation-only closeout is prohibited。
- Formal design evidence: `docs/project_control/gates/P0_2_visual_assets/ao03_scene_executable_spec_design_v0_1.md`。
- 本节为历史设计阶段记录；AO-03 最终完成状态见 2026-09-17 Closeout。

## CLOUD-DRILL-001｜Codex Cloud native PR workflow｜2026-09-15

Status: `PASS / REMOTE VERIFIED / PR MERGED`

Execution route: `OPERATIONS WORKFLOW DRILL / NO D-NUMBER`

- Purpose: verify the temporary no-Mac path without touching Project Control, production, AO-03 engineering, scripts/tests or workflows.
- Canonical source baseline at drill start: `a6db067927e26d19d5566d64fe04d3cb72a24961`。
- A first shell-level direct `git fetch/push` path failed because the Cloud shell had no GitHub credential; this was treated as diagnostic evidence, not as proof that native Cloud publication was unavailable.
- Cloud checkout retained a drill-only commit/work reference; preflight confirmed exactly one committed file: `docs/drills/CODEX_CLOUD_BRANCH_PR_DRILL_2026-09-15.md`。
- Codex Cloud native PR / `make_pr` request was accepted; although the task UI did not return PR number/URL, independent GitHub remote verification found actual PR `#5`。
- Actual PR head: `codex/-codex-cloud-pr`; base: `main`。
- PR scope audit: exactly one changed file, 12 additions, 0 deletions; no Project Control / production / AO-03 change.
- Traceability text was corrected before merge so drill metadata matched the actual PR head and remote publication outcome.
- Product Owner approved merge after independent review.
- Merge SHA: `774a6abed34b81e5558dbfeba3846380fb1ff26e`。
- Completion evidence: `docs/project_control/gates/P0_2_visual_assets/cloud_pr_workflow_drill_2026-09-15.md`。
- Resulting rule supplement: `RC-019` — Codex Cloud native PR publication is the verified remote publication path for TEMP_CLOUD_ONLY_MODE; shell-level direct push credential is not a baseline requirement.

## End-of-Day Project Control Closeout｜2026-09-15

- `project_state.json` advanced to `R036`。
- P0.2 remains `ACTIVE / APPROVED-OPEN CLOSEOUT BEFORE P1 WAVE 2`。
- AO-03 historical state at this checkpoint = `IN PROGRESS / AO-03A+B APPROVED / ENGINEERING IMPLEMENTATION`。
- AO-04 / AO-05 / AO-06 remained pending; P1 Wave 2 remained HOLD。
- `TEMP_CLOUD_ONLY_MODE_V1` was approved but pre-effective on 2026-09-15; it became effective at 2026-09-16 00:00。
- Codex Cloud native PR publication was verified for the 09/16–09/20 cloud-only window。
- Current blocker at that checkpoint: NONE。
- Current live Character coverage remained `42 / 63 = 66.7%`; P1 remained `2 / 10`。
- D-### baseline at that checkpoint: last actual Codex engineering task `D-066`; next formal Codex engineering task when needed = `D-067`。
- Historical next step at that checkpoint: `AO-03B｜Two Scene Master Structured Facts Definition`。


## D-069｜A04 Binary Delivery Deferral｜2026-09-19

Status: `DEFERRED BY PRODUCT OWNER / RESUME SAME D-069`

- Product Owner chose to pause the A04 binary-delivery step until GitHub/local access is available.
- Source attachment `A04_REBOOT_approved_v001.png` was successfully read in Work as the original PNG bytes: 2,486,659 bytes, 941 × 1672.
- Computed SHA-256 matched the expected approved identity exactly: `8111a2d80bb68efe99bc723d197a580b5bfed3d64a1ffeb3848db9260bb50398`.
- Transport branch `work/d069-a04-binary-intake` exists remotely, but no A04 staging binary has been committed; branch still points at the current main baseline.
- Multiple Work attempts to encode/upload the 2.49 MB PNG were interrupted by streaming failures before the GitHub commit completed.
- No Asset Registry, Entity Registry, Asset Relations, Audit Event Log, Shot Spec, Costume Asset, Prop Asset, or live USES_REFERENCE mutation occurred.
- Do not retry the Work direct-upload loop for now.
- Resume gate: when access is available, deliver the byte-exact original to `staging/d069_a04_intake/A04_REBOOT_approved_v001.png`, re-read from GitHub, verify the same SHA-256, then resume the same D-069 formalization path.
- AO-06 remains IN PROGRESS.
- D-070 remains NOT ALLOCATED.


## D-069｜A04 Binary Deferral Scope Correction｜2026-09-19

Status: `D-069 ACTIVE / ONLY A04 BINARY SUBSTEP DEFERRED UNTIL MACBOOK ACCESS`

- Product Owner clarified the previous deferral scope.
- The deferred item is only retrieval of the formal `A04_REBOOT_approved_v001.png` from the MacBook and its byte-exact delivery/formalization path.
- This is **not** a GitHub-access deferral and **not** a pause of the whole D-069.
- GitHub Web/App, ChatGPT, Codex Cloud, Project Control work, model review, resolver/package engineering, cross-checks, and any other work that does not require the local A04 binary may continue normally.
- When MacBook access returns, retrieve the formal A04 source, verify SHA-256 against `8111a2d80bb68efe99bc723d197a580b5bfed3d64a1ffeb3848db9260bb50398`, then continue the binary-dependent formalization/real-validation substep.
- D-070 remains NOT ALLOCATED.


## P0.2 P1 Character Production Resume｜2026-09-19

Status: `ACTIVE / PRODUCT OWNER REPRIORITIZATION`

- Product Owner explicitly chose to resume the remaining P1 Character production before AO-06 is fully closed.
- This supersedes only the sequencing HOLD created by BL-D-026 / BL-D-027 / BL-D-031; AO-06 remains mandatory before P0.2 final closeout / READY_FOR_APPROVAL.
- P1 live state at resume: `2 / 10 complete`, Core Coverage `42 / 63 = 66.7%`.
- Remaining P1 targets (8):
  1. `CHAR_JUN_LUYUAN / PROFILE_LEFT`
  2. `CHAR_JUN_LUYUAN / REAR_3Q_LEFT`
  3. `CHAR_NEIL / PROFILE_RIGHT`
  4. `CHAR_NEIL / REAR_3Q_RIGHT`
  5. `CHAR_SU_XIAOXIAO / PROFILE_LEFT`
  6. `CHAR_SU_XIAOXIAO / REAR_3Q_LEFT`
  7. `CHAR_LIAO_JIAN / PROFILE_LEFT`
  8. `CHAR_LIAO_JIAN / REAR_3Q_LEFT`
- Next production target: `CHAR_JUN_LUYUAN PROFILE_LEFT`.
- Existing production rules remain: 9:16 target, Fixed Standard Review, Product Owner approval before formal Registry entry, Automatic Ingest after approval.
- D-069 remains open as a parallel AO-06 closeout track; its byte-exact A04 binary substep waits for MacBook access.
- D-070 remains NOT ALLOCATED.
- P0.3 remains QUEUED / DO NOT START EARLY.


## P1｜Jun Luyuan PROFILE_LEFT Delivery Bundle｜2026-09-19

Status: `READY / WORK GENERATION NEXT`

- Initial Work generation attempt correctly returned `BLOCKED_ON_REQUIRED_REFERENCE_BINARIES`: Registry metadata resolved, but the four required Atomic PNG bodies were empty through the direct Work GitHub file/blob transport path.
- This reproduces the already-known AO-05 transport limitation and does not invalidate the Character Resolver or canonical assets.
- Required exact inputs:
  - `AST_IMG_000017 / FACE_FRONT / V001 / 7bf1f211743fb9f071d427c1404ea04dfd71c3804b5b526c2dca8b258ed4b96f`
  - `AST_IMG_000018 / PROFILE_RIGHT / V001 / 7a04169daed3034ed9d37a508670dce995d2dc2cb75a11148006f9e821321c92`
  - `AST_IMG_000016 / FACE_3Q_RIGHT / V001 / f9ddbb18d4b548bf4887d09d1e0a9eba8be2dde7d61275a8c09a1a5d639f9929`
  - `AST_IMG_000015 / BODY_FRONT / V001 / f9960466266f08d79fde32435f542bd47ed0f8ab26af99bbb2928bd8d3957e92`
- Chat created a temporary GitHub Actions transport workflow:
  `.github/workflows/p1-jun-luyuan-profile-left-delivery-bundle.yml`
- Workflow run `35422665719`: `SUCCESS`.
- Runner log: `PASS: 4/4 exact canonical reference binaries verified`.
- Artifact: `P1_JUN_LUYUAN_PROFILE_LEFT_DELIVERY_BUNDLE_V001`.
- Artifact ID: `10577930931`.
- Artifact size: `11,348,718 bytes`.
- Artifact ZIP digest: `sha256:a4cd646a66f7925089be869178efe255ce1e0612e36633358e883bf86a290075`.
- Source commit: `ebd22de616ebbae5be5b822575020a4fe4892b8c`.
- Expires: `2026-09-26T04:57:51Z`.
- This is a transport artifact only; it is not a formal Asset and causes no Registry / Audit mutation.
- Next: Work automatically downloads the artifact, independently validates manifest + 4 file SHA/bytes, then generates the `PROFILE_LEFT` candidate and performs Fixed Standard Review.
- Product Owner manual reference upload count remains `0`.
- D-070 remains NOT ALLOCATED.


## P1｜Jun Luyuan PROFILE_LEFT V001 Product Owner Approval｜2026-09-19

Status: `PO APPROVED / FORMAL INGEST PENDING`

- Final candidate visually reviewed in main Chat: `PASS`.
- Product Owner explicitly approved the candidate as Jun Luyuan `PROFILE_LEFT V001`.
- Canonical target filename: `CHAR_JUN_LUYUAN_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`.
- Exact uploaded approved source identity:
  - format: `PNG`
  - dimensions: `941 × 1672`
  - byte size: `1,933,426`
  - SHA-256: `00915474a52a29df753542b916503998c450b056d2ef59d98279841fdc9ad9be`
- Important audit boundary: Work's final report did not include the candidate PNG SHA, so there is no prior candidate SHA against which to cryptographically compare this upload. The current uploaded PNG is therefore locked as the PO-approved source identity for formalization.
- Do not re-encode, resize, screenshot, or substitute this source during formal publication.
- Core Coverage / P1 completion remain unchanged until exact-byte canonical publication + Automatic Ingest + Registry/Audit verification succeeds.
- After ingest: continue `CHAR_JUN_LUYUAN REAR_3Q_LEFT`.
- D-069 remains open in parallel; D-070 remains NOT ALLOCATED.


## P1｜Jun Luyuan PROFILE_LEFT V002 Visual Candidate｜2026-09-19

Status: `V001 APPROVAL WITHDRAWN PRE-INGEST / V002 VISUAL CANDIDATE / FORMAL REVALIDATION PENDING`

- Product Owner re-reviewed V001 before formal ingest and identified the neck as proportionally too long.
- A revised Chat-generated image with a shorter, more natural neck/shoulder relationship was selected as the preferred visual direction.
- V001 had not entered canonical storage/Registry, so its earlier approval is withdrawn without formal supersession.
- Do **not** publish or ingest V001.
- The revised image is designated only as `CHAR_JUN_LUYUAN_PROFILE_LEFT_DEFAULT_DEFAULT_V002 / VISUAL CANDIDATE`.
- It is not yet a formal Asset because it was generated outside the locked 4-reference Delivery Bundle execution path.
- Formal next step: rerun with the same verified canonical four-reference set; use the V002 candidate only as target appearance/neck-proportion guidance; then Fixed Standard Review → Product Owner final approval → exact-byte publication → Automatic Ingest.
- D-069 remains parallel; D-070 remains NOT ALLOCATED.


## P1｜Jun Luyuan PROFILE_LEFT V002 Work Revalidation Rejected｜2026-09-19

Status: `REJECTED BY PRODUCT OWNER / WRONG IMAGE / RERUN REQUIRED`

- Work successfully revalidated the Delivery Bundle and canonical 4-reference input set.
- Work nevertheless returned the wrong image for the intended V002 target.
- Product Owner explicitly rejected the image.
- Therefore Work's internal `INTERNAL APPROVED FINAL CANDIDATE` label is overridden by Product Owner authority and has no formal effect.
- Reference delivery evidence remains valid; the failure is at target-candidate selection/use or generation-result level.
- Correct visual target to use on rerun: the strict 90° left-profile image selected after V001 neck-length rejection, with shorter neck and more natural shoulder-neck proportion.
- Do not use the earlier REAR_3Q visual direction image as V002 target guidance.
- No ingest / Registry / Audit mutation occurred.


## P1｜Jun Luyuan PROFILE_LEFT V002 Work Rerun Internal Pass｜2026-09-19

Status: `WORK INTERNAL APPROVED FINAL CANDIDATE / MAIN CHAT VISUAL REVIEW PENDING`

- Work rerun explicitly confirmed it used the correct Product Owner-selected short-neck strict 90° left-profile visual target.
- The target candidate was used only as `NON-AUTHORITATIVE VISUAL TARGET GUIDANCE`.
- Identity authority remained the verified four canonical references.
- The previously rejected Work image was not used.
- Work reported PASS for Format, Identity, Role Accuracy, Continuity, Production Utility, Reference Type Purity, Problem Check, and Neck / Shoulder Proportion.
- No ingest / Registry / Audit / Project Control mutation was performed by Work.
- Formal status is still pending main-Chat visual review of the actual image and explicit Product Owner approval.


## P1｜Jun Luyuan PROFILE_LEFT V002 Product Owner Approval｜2026-09-19

Status: `PRODUCT OWNER APPROVED / FORMAL INGEST PENDING`

- Main Chat visually reviewed the actual Work rerun output and passed it.
- Product Owner explicitly approved `CHAR_JUN_LUYUAN_PROFILE_LEFT_DEFAULT_DEFAULT_V002.png`.
- Exact approved source:
  - format: PNG
  - dimensions: 941 × 1672
  - byte_size: 1,938,522
  - SHA-256: `8bc4ca3ab9f5f2b9e8603918c147211ad8234e80c0b527fa45c880879a8ee71c`
- This exact PNG is now the sole PO-approved source for formalization.
- Next: byte-for-byte canonical publication → remote SHA verification → Automatic Ingest → Registry/Audit verification.
- V001 remains `DO NOT INGEST`.
- No Registry/Audit mutation has occurred yet.


## P1｜Jun Luyuan PROFILE_LEFT V002 Transport Pending / REAR_3Q_LEFT Resume｜2026-09-19

Status: `PROFILE_LEFT V002 PO APPROVED / TRANSPORT-INGEST PENDING / REAR_3Q_LEFT PRODUCTION RESUMED`

- PROFILE_LEFT V002 remains the Product Owner-approved visual result.
- Exact source identity remains locked: 941×1672 / 1,938,522 bytes / SHA-256 `8bc4ca3ab9f5f2b9e8603918c147211ad8234e80c0b527fa45c880879a8ee71c`.
- GitHub binary upload repeatedly remained too slow/unreliable.
- Product Owner approved continuing P1 production without waiting for that transport/ingest.
- Formal P1 progress remains 2/10 until PROFILE_LEFT V002 exact-byte publication + Automatic Ingest completes.
- Next production target: `CHAR_JUN_LUYUAN_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001`.


## P1｜Jun Luyuan REAR_3Q_LEFT V001 Product Owner Approval｜2026-09-19

Status: `PRODUCT OWNER APPROVED / TRANSPORT-INGEST PENDING`

- Main Chat reviewed the actual Work output and passed it.
- Product Owner explicitly approved `CHAR_JUN_LUYUAN_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001.png`.
- Exact approved source:
  - format: PNG
  - dimensions: 941 × 1672
  - byte_size: 1,941,468
  - SHA-256: `97ad38c259274eced5be61035cda4c28df72babe084fc452fbbc927a2a6da21e`
- Geometry review: rear/back dominant; left face exposure approximately 1/4; no PROFILE or front-3Q drift; head/ear/neck/shoulder-back structures usable.
- Jun PROFILE_LEFT V002 and REAR_3Q_LEFT V001 both remain outside formal progress until exact-byte publication + Automatic Ingest succeeds.
- Formal P1 progress remains `2/10`.
- Next production target: `CHAR_NEIL_PROFILE_RIGHT_DEFAULT_DEFAULT_V001`.


## P1｜Neil PROFILE_RIGHT V001 + REAR_3Q_RIGHT V001 Product Owner Approval｜2026-09-19

Status: `BOTH PRODUCT OWNER APPROVED / TRANSPORT-INGEST PENDING`

- `CHAR_NEIL_PROFILE_RIGHT_DEFAULT_DEFAULT_V001.png`
  - PNG / 941×1672 / 1,693,697 bytes
  - SHA-256: `17dff7f50b7392915db6d74f1d04b506f2de884e9069ba11f9013bbe2fce8262`
- `CHAR_NEIL_REAR_3Q_RIGHT_DEFAULT_DEFAULT_V001.png`
  - PNG / 941×1672 / 1,656,490 bytes
  - SHA-256: `7f8cb635945e20035ba1b39dafecdf4caecc520d8e8794f67e39c2cfa1a6dad6`
- Both passed main-Chat visual review and explicit Product Owner approval.
- Both remain outside formal Registry/Core Coverage/P1 progress until exact-byte publication + Automatic Ingest succeeds.
- Jun Luyuan PROFILE_LEFT V002 and REAR_3Q_LEFT V001 remain in the same transport-ingest-pending state.
- Formal P1 progress therefore remains `2/10`.
- Next production target: `CHAR_SU_XIAOXIAO_PROFILE_LEFT_DEFAULT_DEFAULT_V001`.


## P1｜Su Xiaoxiao PROFILE_LEFT V001 Delivery Workflow｜2026-09-19

Status: `WORKFLOW CREATED / ARTIFACT BUILD PENDING`

- Target: `CHAR_SU_XIAOXIAO_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`.
- Dedicated workflow created: `.github/workflows/p1-su-xiaoxiao-profile-left-delivery-bundle.yml`.
- Source commit: `bcfe78f973f6221845ffbc80affb2cd99b5a09e6`.
- Canonical atomic set:
  - AST_IMG_000044 — FACE_FRONT / V001
  - AST_IMG_000043 — FACE_3Q_LEFT / V001
  - AST_IMG_000042 — BODY_FRONT / V001
  - AST_IMG_000041 — BODY_BACK / V001
- Su Xiaoxiao has no authoritative profile view. FACE_FRONT + FACE_3Q_LEFT are therefore the primary facial authorities; BODY_FRONT/BODY_BACK support body, neck and hair continuity.
- Next: successful artifact build → 4/4 exact-byte verification → Work generation → main-Chat review → Product Owner approval.


## Daily Closeout Cross-Check｜2026-09-19

Status: `COMPLETE / CROSS-CHECKED / EOD PAUSED`

Cross-checked and synchronized:

- `core/project_state.json`
- `core/acceptance_matrix.md`
- `gates/P0_2_visual_assets/README.md`
- `gates/P0_2_visual_assets/character_gap_live_progress_v1.md`
- `gates/P0_2_visual_assets/approved_open_tasks_v1.md`
- `logs/decision_log.md`
- `logs/execution_log.md`
- `logs/rules_change_log.md`
- `logs/risk_register.md`
- Dashboard
- four approved Jun/Neil canonical target paths on GitHub main

No new project-wide rule was added beyond existing RC-020. Risk Register statuses remain unchanged. Four approved PNGs are still not present at canonical GitHub paths; therefore no formal progress increment is recorded.

Resume point: Su Xiaoxiao PROFILE_LEFT delivery artifact verification / formal generation; exact-byte ingest of four approved Jun/Neil views when transport is stable; AO-06/D-069 remains parallel final-closeout work. D-070 remains NOT ALLOCATED.


## P1｜Su Xiaoxiao PROFILE_LEFT V001 Product Owner Approval｜2026-09-20

Status: `PRODUCT OWNER APPROVED / TRANSPORT-INGEST PENDING`

- Work generation used verified canonical reference delivery.
- Artifact ID: `10584448292`.
- Artifact actual SHA-256: `583294d5ac2acca71278a8d5cc02c1a628560623cdf9ec4fb2691604f06d42a0` / MATCH.
- Canonical references: AST_IMG_000044 FACE_FRONT, AST_IMG_000043 FACE_3Q_LEFT, AST_IMG_000042 BODY_FRONT, AST_IMG_000041 BODY_BACK; 4/4 MATCH.
- Main Chat Fixed Standard Review: PASS.
- Product Owner explicitly approved `CHAR_SU_XIAOXIAO_PROFILE_LEFT_DEFAULT_DEFAULT_V001.png`.
- Exact approved source:
  - format: PNG
  - dimensions: 941 × 1672
  - byte_size: 2,088,722
  - SHA-256: `3af763a5d96d043ccce061459b16af93114e0bcf59d44a98c9df17130c97868c`
- No ingest / Registry / Audit / Core Coverage mutation has occurred.
- Formal P1 progress remains `2/10`.
- Next production target: `CHAR_SU_XIAOXIAO_REAR_3Q_LEFT_DEFAULT_DEFAULT_V001`.
- Dedicated delivery workflow created at commit `2dcf38869f684add4a1424b1b60b6438229628a7`.


## Daily Closeout Cross-Check｜2026-09-20

Status: `COMPLETE / CROSS-CHECKED / EOD PAUSED / R070`

- P1 visual production = `10/10 PO APPROVED`; formal P1 remains `2/10`.
- P2 generated = `7/7`; explicit PO approvals = `6/7`.
- Castle Young Master `REAR_3Q_LEFT V001` = `PO REVIEW PENDING / DO NOT INGEST`.
- Total PO-approved Core-view binaries awaiting formal publication + ingest = `14`.
- Formal Core Coverage remains `42/63 = 66.7%`.
- No new Asset ID was allocated; Asset Registry / Audit were not mutated by visual approval alone.
- P3 Black Lady 6-view lateral rebuild remains NOT STARTED.
- AO-06 / D-069 remains open and mandatory before P0.2 final closeout.
- D-070 remains NOT ALLOCATED.
- TEMP_CLOUD_ONLY_MODE_V1 reaches its pre-approved time-box end at 2026-09-20 EOD; next local formal production requires GitHub→Local truth sync.
- Updated: project_state R070, acceptance matrix, P0.2 README/live progress/approved-open tasks, decision log BL-D-049..057, execution log, Dashboard V046, daily closeout.
- Reviewed unchanged: rules_change_log (no new rule); risk_register (RISK-001 CONTROLLED, RISK-002 ACCEPTED/NON-BLOCKING).

Resume: Castle Rear-3Q PO decision → exact-byte publication / remote SHA / Automatic Ingest for approved views → formal coverage refresh → GitHub→Local truth sync → AO-06/D-069 separate closeout.


## 2026-09-22｜D-070 Published Binary Adoption｜Rescue Publication

- Source baseline: `3d3aebba8ca458dcdb133c77e3611f037f2fc49a / R071`.
- Original Codex Cloud result was complete but not remotely published; rescue branch created directly on GitHub.
- Added fail-closed `--adopt-existing` controller mode and focused version-reservation safety.
- Formally admitted 21 previously published PO-approved Character Core binaries as `AST_IMG_000063–AST_IMG_000083`.
- Registry count advanced `62 → 83`.
- Audit count advanced `78 → 120`; D-070 contributes exactly 42 events.
- Formal Character Core Coverage advanced `42/63 → 63/63`; Single Current `63/63 PASS`.
- D-070 relation count = `0`; no existing CURRENT slot was replaced.
- Published PNGs were not changed by the rescue transaction.
- Existing Derived Reference Sheet PNGs remain unchanged; builder expected live coverage updated to complete Tier distribution.
- AO-06 / D-069 remains OPEN and mandatory before P0.2 final approval. P0.3 remains QUEUED.


## 2026-09-22｜D-070 PR #11 Formal Review

- PR #11 underwent code, Registry/Audit, binary-integrity and Project Control consistency review.
- Review Patch fixed post-commit invariant rollback ordering, scoped version reservation to adopt-existing only, and corrected rescue audit provenance/time semantics.
- First temporary validation run exposed a normal-supersession regression in the reservation logic; the regression was fixed before approval.
- Final GitHub Actions validation run `35678375411` passed:
  - targeted tests `15/15`;
  - full regression `86/86`;
  - all 21 D-070 canonical PNG SHA/byte/path checks;
  - Registry/Audit/Relations `83/120/44`;
  - D-070 `21 assets / 42 events / 0 relations`;
  - mandatory Character Core Single Current `63/63`;
  - Derived Reference Sheet live-coverage contract;
  - Project Control JSON and diff hygiene.
- Temporary review workflow removed after PASS; final PR changed-file scope = `13`, with no PNG, `production/audio/`, or ZIP change.
- Review conclusion: `PASS / READY_FOR_PRODUCT_OWNER_MERGE_APPROVAL`.
- Required merge method: `SQUASH` so rescue/review intermediate commits do not enter canonical main history.
- P0.2 remains ACTIVE; AO-06 / D-069 remains OPEN; P0.3 remains QUEUED.


## 2026-09-22｜D-070 PR #11 Merge Closeout

- Product Owner explicitly approved merge.
- PR #11 transitioned from Draft to Ready for Review and was squash-merged.
- Merge SHA: `6dc3171bba701c22a97580eadc06f62f391b5fe1`.
- Post-merge GitHub remote verification passed:
  - Registry `83`;
  - Audit `120`;
  - Relations `44`;
  - D-070 `21 assets / 42 events / 0 relations`;
  - Character Core `63/63`;
  - mandatory Single Current `63/63 PASS`;
  - AO-06 / D-069 still OPEN.
- Project Control advanced to R073 to remove the pre-merge waiting state and set AO-06 / D-069 as the current task.


## 2026-09-22｜Local Sync Deferral

- Product Owner decision: defer GitHub→Mac local sync until end of day.
- No intermediate local pull is required during the remaining cloud-side work.
- At end of day, perform one consolidated sync.
- Required sequence before the EOD pull:
  1. `git status`
  2. if clean, `git pull --ff-only origin main`
  3. if not clean, stop and resolve local changes before pulling.
- This deferral does not change GitHub `main` as SSOT.
- Current project task remains `AO-06 / D-069`.


## 2026-09-22｜D-069 Review Patch 02 Merge Closeout

Status: `MERGED / REMOTE VERIFIED / AO-06 ACTUAL USE + AUDIT NEXT`

- Product Owner explicitly approved the Review Patch 02 design boundary and subsequent PR #12 merge.
- Codex Cloud publication handshake failed because GitHub credentials were unavailable; no remote Codex branch was created, so the local Codex handshake commit was not treated as project fact.
- Chat/GitHub path executed the patch directly on `chatgpt/d069-review-patch-02`.
- Exact approved A04 evidence was materialized and verified:
  - path: `staging/d069_a04_intake/A04_REBOOT_approved_v001.png`
  - byte size: `2486659`
  - SHA-256: `8111a2d80bb68efe99bc723d197a580b5bfed3d64a1ffeb3848db9260bb50398`
  - Git blob SHA: `fd05cae8618d7daa16c16658b29d25ab65052fbb`
- Evidence-boundary correction:
  - `COSTUME_NEIL_DEFAULT` and `PROP_NEIL_CROSS` no longer block A04 as standalone formal visual Assets;
  - Neil black butler attire + visible chest cross are `CHAR_NEIL / DEFAULT` appearance-continuity constraints;
  - `WHITE_POCKET_HANDKERCHIEF_VISIBLE` removed as an A04 hard requirement;
  - no historical `USES_REFERENCE` was reconstructed.
- Validation workflow run `35703125845`:
  - exact A04 binary identity: PASS;
  - targeted D-069: `13/13 PASS`;
  - full regression: `86/86 PASS`.
- PR #12 changed-file scope after cleanup: 7 files; temporary validation workflow removed before merge.
- PR #12 moved Draft → Ready after PO approval and was squash-merged.
- Merge SHA: `fdc43a907cb799eef3c11553b34bab74374ddd5c`.
- Post-merge remote verification:
  - PR state = merged;
  - main HEAD = merge SHA;
  - squash-merge tree SHA exactly matches reviewed branch tree SHA `740a43aa62ed48948426a9da18bd488617f36bd5`;
  - A04 evidence on main retains byte size `2486659` and Git blob SHA `fd05cae8618d7daa16c16658b29d25ab65052fbb`, proving byte identity with the SHA-verified reviewed file.
- AO-06 is not complete. Remaining chain:
  `Reference Package → Actual Production Use → immutable use record → reverse audit`.
- P0.3 remains `QUEUED / DO NOT START EARLY`.
- Local GitHub→Mac sync remains intentionally deferred to EOD for one consolidated sync.


## 2026-09-22｜D-069 Final Audit PR #13 Merge Closeout

Status: `MERGED / REMOTE VERIFIED / AO-06 READY_FOR_APPROVAL`

- Product Owner authorized the next step, including PR #13 Ready-for-Review transition and squash merge.
- PR #13: `D-069 Final Audit: record A04 actual production use`.
- Merge SHA: `9ec2975059582bbd279d3a05d4af1284fac3f27a`.
- Post-merge main verification passed:
  - immutable use record `production/audit/shot_use_records/AO06_A04_USE_V001.json` exists on main;
  - use record references `A04_SPEC_V001` and `A04_REFERENCE_PACKAGE_V001`;
  - formal inputs are `AST_IMG_000060 / AST_IMG_000059 / AST_IMG_000052`;
  - Stage 4 actual-use proof remains `GitHub run 35705835709 / Artifact 10684566525 / imagegen exec-ae7fde3c-02a5-4106-beaa-69704b9164ea`.
- Final audit validation run `35709208035` had already passed:
  - immutable duplicate-write rejection;
  - Shot→inputs reverse trace;
  - Asset→use reverse trace 3/3;
  - targeted `13/13 PASS`;
  - full regression `86/86 PASS`.
- Controlled data counts remain unchanged after merge:
  - Asset Registry = `83`;
  - Asset Relations = `44`;
  - Audit Event Log = `120`.
- No live `USES_REFERENCE` was created; this is intentional because the validation output is NON_PRODUCTION and has no formal SHOT Asset ID.
- AO-06 engineering evidence chain is now complete:
  `Real Shot Spec → Resolver → Reference Package → Actual Production Use → immutable use record → reverse audit`.
- Governance result:
  - AO-06 = `READY_FOR_APPROVAL / WAITING PRODUCT OWNER APPROVAL`;
  - do not mark COMPLETE / APPROVED until explicit PO approval;
  - P0.2 remains ACTIVE pending that decision;
  - P0.3 remains QUEUED / DO NOT START EARLY.
- Project Control advanced to R076.
- Local GitHub→Mac sync remains deferred to EOD for one consolidated sync.


## 2026-09-22｜AO-06 Product Owner Approval + P0.2 Readiness

Status: `AO-06 COMPLETE / VERIFIED / PRODUCT OWNER APPROVED / P0.2 READY_FOR_APPROVAL`

- Product Owner explicitly approved AO-06 after reviewing its purpose and scope.
- AO-06 approval confirms the Visual Asset Management System can, on a real Shot:
  - resolve the correct formal references;
  - build a traceable Reference Package;
  - deliver that package into a real image-generation call;
  - record immutable actual-use evidence;
  - support Shot→Assets and Asset→Shot/use reverse trace.
- AO-06 does not validate final image quality, video generation, animation quality, edit quality, or the full P0.3 production pipeline.
- AO-06 closeout file:
  `docs/project_control/gates/P0_2_visual_assets/ao06_closeout_2026-09-22.md`.
- Decision record: `BL-D-065`.
- P0.2 final readiness review completed after AO-06 approval:
  - Character Core formal coverage `63/63`;
  - AO-01..AO-07 mandatory closeout set satisfied;
  - Automatic Ingest verified;
  - Scene/Character/Derived Registry and dependency model verified;
  - real A04 Resolver→Package→Actual Use→Audit chain verified;
  - RISK-002 remains accepted / non-blocking.
- Result: `P0.2 READY_FOR_APPROVAL / WAITING PRODUCT OWNER APPROVAL`.
- P0.2 is not yet PASS.
- P0.3 remains `QUEUED / DO NOT START EARLY`.
- Local GitHub→Mac sync remains deferred to EOD.


## 2026-09-22｜P0.2 Product Owner Approval + P0.3 Entry

Status: `P0.2 PASS / PRODUCT OWNER APPROVED / P0.3 READY_TO_START`

- Product Owner explicitly approved `P0.2｜人物锚定与 Scene Master 资产治理`.
- P0.2 closeout evidence:
  `docs/project_control/gates/P0_2_visual_assets/p0_2_closeout_2026-09-22.md`.
- Decision record: `BL-D-066`.
- Overall P0 Gate progress advanced from `1/3 PASS` to `2/3 PASS`.
- P0.2 approved-open task list closed; AO-01..AO-07 satisfied.
- P0.3 prerequisite is cleared.
- P0.3 is `READY_TO_START / NOT YET VALIDATED`; no video/animation quality conclusion is inherited from AO-06.
- Before formal local P0.3 execution, the deferred GitHub→Mac truth sync is required.
- Current next task:
  `P0.3｜ENTRY REVIEW + LOCAL TRUTH SYNC BEFORE FORMAL EXECUTION`.


## Local Truth Sync Complete｜2026-09-22

Status: `COMPLETE / LOCAL HEAD == ORIGIN/MAIN`

- Initial ordinary `git pull --ff-only origin main` failed with `Empty reply from server`.
- AO-07 verified recovery path was used via `$HOME/.local/bin/git-proxy-auto`.
- Sync then completed successfully.
- Final local truth:
  - branch: `main`
  - local HEAD: `d3a62f05c3c47c83d4b0583f591a9d61b308f4e8`
  - `origin/main`: `d3a62f05c3c47c83d4b0583f591a9d61b308f4e8`
- Known untracked local items remain preserved:
  - `black_lady_character_asset_migration_v1.zip`
  - `production/audio/`
- These untracked paths are not present on GitHub main and did not block the fast-forward sync.
- P0.3 local-entry prerequisite is satisfied.
- Next: `P0.3｜ENTRY REVIEW`.


## 2026-09-23｜P0.3 Representative Motion Validation Closeout

Status: `IN PROGRESS / TECHNICAL PROOFS RECORDED / P0.3 NOT YET VALIDATED`

- P0.3 moved from entry review into real project-material validation.
- A01→A02 Reference Delivery Bundle completed:
  - source commit `770635048a427ba1343f1bbee6cb5000f72429a9`;
  - workflow run `35838222340`;
  - artifact `BRIDGE_A01_A02_REFERENCE_DELIVERY_BUNDLE_V001`;
  - artifact ID `10740625723`;
  - 12/12 reference identity checks passed.
- Two bridge candidates retained as experimental staging inputs:
  - Wide SHA-256 `f60bf3289bb1eadcab770c9f51cc20afae725d282a3f46b78e401949983785ca`;
  - Tight SHA-256 `57f960184441c21ae3f881f8efe47ef858d3c87b13824ba689eeb6d3d282c316`.
- Initial A01→Wide→Tight→A02 hard-cut validation showed improved structural progression but remained visually jumpy / slideshow-like.
- Remotion camera-move V002:
  - branch `codex/p03-a01-a02-remotion-camera-v002`;
  - technical commit `01f248e182f4998121525b46eba54c58c28021cf`;
  - run `35857760082`;
  - artifact ID `10747314541`;
  - technical PASS;
  - Product Owner artistic result: not ideal / not approved as primary solution.
- A01 depth Gate A:
  - branch `codex/p03-a01-depthflow-proof-v001`;
  - run `35861220002`;
  - artifact `P03_A01_DEPTH_GATE_A_V001`, ID `10750093687`;
  - Depth Anything V2 Small depth map SHA-256 `fdcb7844cac2141a4a37f66b82a8c65a0978bd75d457b1302af21d8e24e14fe5`;
  - visual depth review usable for 2.5D proof.
- A01 DepthFlow Gate B:
  - two initial implementation attempts failed on unsupported `DepthState.quality`; source/depth identity and runtime initialization remained valid;
  - corrected commit `d6509c43c987646a04c7ac83329252af78f0741d`;
  - successful run `35867948575`;
  - artifact `P03_A01_DEPTH_GATE_B_V001`, ID `10753710981`;
  - output `A01_DEPTHFLOW_CAMERA_PROOF_V001.mp4`;
  - 720×1280 / 30fps / ~2.5s / H.264;
  - Product Owner result: `可以，值得继续尝试`.
- Execution-time finding:
  - successful run total ~3m37s;
  - actual 75-frame DepthFlow render ~40s;
  - most overhead came from repeated environment / Python / Torch / CUDA-related dependency setup.
- Product Owner next-direction instruction:
  - do not repeatedly download unchanged dependencies;
  - optimize caching / CPU-specific dependency path before repeated V002/V003 iterations.
- Current working method:
  - internal motion inside shots;
  - normal cuts between independently authored shots;
  - continue 2.5D validation;
  - Remotion remains compositor/editor/timing/audio/output;
  - AI video / FLF2V remains optional for selected shots only.
- No experimental motion branch was merged into production.
- No formal Asset Registry / Audit / P0.3 PASS update was made from experimental outputs.
- Detailed closeout:
  `docs/project_control/gates/P0_3_video_pipeline/p0_3_progress_closeout_2026-09-23.md`.


## 2026-09-28｜MANOR_GATE Scene Master Formalization + N15 Authority Correction

Status: `COMPLETE / PRODUCT OWNER APPROVED / REMOTE VERIFIED`

- Product Owner approved MANOR_GATE Scene Reference Candidate 02.
- Formalized Entity: `SCENE_MANOR_GATE`.
- Formalized Asset: `AST_IMG_000084` / `SCENE_MASTER / DEFAULT / DAY_CLOSED`.
- Canonical PNG: `production/image_library/scene_masters/manor_gate/SCENE_MANOR_GATE_SCENE_MASTER_DEFAULT_DAY_CLOSED_V001.png`.
- Exact binary: 941x1671 / 3279563 bytes / SHA-256 `95b3bebce1b2e9be72d5a2bc99665a4a99719eb0f4146e40a562210bd982e278` / Git blob `ac1dfb7be2069848917afb9749de6c8ebc54d3e5`.
- Formalization run `36370354050`: SUCCESS; formalization commit `6d7b7b9b5b65ac9adaf191aa5fd2a953c8927d6a`; evidence artifact `10948408214`.
- Scene profile locks `estate internal road → MANOR_GATE → external road` and explicitly separates the manor gate from `SCENE_CASTLE_ENTRANCE`.
- N15 old Neil-focused key-holder hypothesis is superseded after canonical story fact correction.
- N15 is now `Locked Gate Foreshadowing`: audience-only view of the true final exit before character discovery.
- N15 Scene Authority is formally bound to `AST_IMG_000084`; `AST_IMG_000052` cannot substitute for manor-gate geometry/identity.
- Project State advanced to `R117`.
- Next step: `N15 Reference Delivery Bundle Design`; Bundle build and generation are not yet authorized.

## 2026-09-28｜N15 Locked Gate Foreshadowing Formal Archival

Status: `COMPLETE / PRODUCT OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED`

- Final selected version: dense-fog N15 Candidate 01.
- Exact upload verification run `36374095043`: PASS.
- Final identity: 941x1672 / 2583010 bytes / SHA-256 `2712321ca6348cc39234f8ae65bcdb0fd2e6b2faf0b56dcc94a51235011d1191` / Git blob `4d9ca2dcd33df32294ff9b928bf3ab88d63c7487`.
- Canonical publication commit `deee18697dd79cd041d37c2725ee15028440dee5`; exact Git blob preserved, no re-encode.
- Canonical path: `production/image_library/approved/story_shots/N15_LOCKED_GATE_FORESHADOWING_APPROVED_V001.png`.
- Story Shot Index registration commit `a9fc6bb0eea41634777241d3dbbad83e3f867368`.
- Registration verification run `36374770242`: `SHA_MATCH=YES / BLOB_MATCH=YES / INDEX_MATCH=YES / DIMENSIONS_MATCH=YES / STAGING_CLEANUP_PASS / OVERALL_RESULT=PASS`.
- N15 is formally archived and no longer an active generation task.
- Project State advanced to `R118`.
- Next: continue S02-A from A05 reuse / sequence assembly planning under Product Owner direction.

## 2026-09-28｜S02-A Assembly V001 Formal Closeout

Status: `COMPLETE / PRODUCT OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED`

- Corrected S02-A audio boundary confirmed by Product Owner after Audio-Only QC: `00:33.020 → 01:18.750` / `45.730s`.
- Locked sequence: `N11 → N12 → A04 → N14 → N15 → A05`.
- Product Owner approved `S02_A_ASSEMBLY_PROOF_V002` after full-context review.
- Original V002 render was technically decodable but had low desktop compatibility (H.264 4:4:4 / 100fps / ALAC) and was not selected as canonical delivery binary.
- Compatibility master selected for canonical archival:
  - source name: `S02_A_ASSEMBLY_PROOF_V002_COMPAT.mp4`
  - 942×1672 / 30fps / H.264 yuv420p / AAC 48kHz stereo
  - duration: 45.730s
  - byte size: 6,822,004
  - SHA-256: `937008e11d20892ea0a17be64719a19cb131d174871930bc29004a678bb58ed1`
  - Git blob: `bcd3fef7a8d600c95cb4d7242d411cc0df41859c`
- Exact Binary Verification:
  - workflow run `36427746113`
  - job `108945798299`
  - result `SUCCESS / OVERALL_RESULT=PASS`
  - artifact `S02_A_APPROVED_UPLOAD_VERIFICATION_V001`
  - artifact ID `10972091936`
- Canonical Publication:
  - workflow run `36428710030`
  - job `108949038095`
  - canonical path `production/video/approved/s02_a/S02_A_ASSEMBLY_APPROVED_V001.mp4`
  - publication commit `e577cd09c5ba333b7659dc08bc0898a5596edbb5`
  - `EXACT_BLOB_PRESERVED=YES`
- Video Index Registration:
  - `production/video/video_index.jsonl`
  - registration commit `ed99eba7b780f6455323d035fdb4148f5c465dc1`
  - video ID `S02_A_ASSEMBLY_V001`
  - approval `PRODUCT_OWNER / APPROVED`
  - lifecycle `CURRENT`
- Registration Verification:
  - run `36430256742`
  - job `108954308923`
  - `SHA_MATCH=YES / BLOB_MATCH=YES / INDEX_MATCH=YES / BYTE_SIZE_MATCH=YES / MEDIA_METADATA_MATCH=YES / APPROVAL_LIFECYCLE_MATCH=YES / FULL_VIDEO_DECODE=PASS / FULL_AUDIO_DECODE=PASS / STAGING_CLEANUP_PASS / OVERALL_RESULT=PASS`.
- Formal closeout record:
  `docs/project_control/gates/P0_3_video_pipeline/s02_a_assembly_v001_formal_closeout_2026-09-28.md`.
- Final disposition:
  `S02_A_ASSEMBLY_V001 = PRODUCT_OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED / FORMALLY CLOSED`.
- P0.3 remains `IN PROGRESS`; this is a sequence-level closeout, not a Gate PASS.

## 2026-09-28｜P0.3 Daily Closeout / S02-A EOD

Status: `COMPLETE / CROSS-CHECKED / EOD CLOSEOUT / R120`

- S02-A formal asset chain was already completed before EOD closeout:
  - exact binary verification run `36427746113`: PASS;
  - canonical publication run `36428710030`: PASS;
  - publication commit `e577cd09c5ba333b7659dc08bc0898a5596edbb5`;
  - Video Index registration commit `ed99eba7b780f6455323d035fdb4148f5c465dc1`;
  - registration verification run `36430256742`: PASS.
- Final sequence: `N11 → N12 → A04 → N14 → N15 → A05`.
- Canonical audio: `00:33.020 → 01:18.750` / `45.730s`.
- Canonical video: `production/video/approved/s02_a/S02_A_ASSEMBLY_APPROVED_V001.mp4`.
- P0.3 README updated with S02-A formal closeout and resume point.
- Acceptance Matrix updated from Opening-proof wording to current S02-A-complete / P0.3-not-yet-validated state.
- Dashboard refreshed to `V090`, derived from `R120`.
- Dashboard current production segment corrected:
  - N13 cancelled / not registered;
  - N14 and N15 included;
  - Story Shot registered count = `21`;
  - next sequence not yet authorized.
- Rules Change Log cross-checked; no new RC rule required by this EOD closeout.
- Decision Log cross-checked; `BL-D-077` already contains the Product Owner S02-A approval decision, so no duplicate decision entry was added.
- Daily closeout record:
  `docs/project_control/gates/P0_3_video_pipeline/p0_3_daily_closeout_2026-09-28.md`.
- P0.3 remains `IN PROGRESS / NOT YET VALIDATED`.
- Resume next work from canonical audio immediately after `01:18.750`, only when Product Owner authorizes the next sequence.

## 2026-09-29｜S02-B Audio-Only Boundary QC

Status: `COMPLETE / PRODUCT OWNER AUDIO QC PASS / BOUNDARY LOCKED`

- S02-B resumes exactly after the formally closed S02-A endpoint at `01:18.750`.
- Boundary-analysis workflow `S02-B Audio Boundary Analysis V001` run `36505933111`: SUCCESS.
- Analysis artifact `S02_B_AUDIO_BOUNDARY_ANALYSIS_V001`, artifact ID `11006758193`, digest `sha256:0dc02d61ec623cd2ad2e1530e88a36b1d65d41696a0a21bfab00bff334b24f12`.
- Word-level alignment placed “各位，请随我来” ending at approximately `02:22.560`, with the next narrative sentence beginning approximately `02:23.420`.
- Formal Audio-Only QC proof workflow run `36506339712`: SUCCESS.
- QC artifact `S02_B_AUDIO_ONLY_QC_PROOF_V001`, artifact ID `11007655729`, digest `sha256:74525589b498b6a5f47952b451d2d93ba7e22a7a1dfbcc2b7f48cfa2137496e0`.
- QC WAV: `64.250s`, SHA-256 `90f40ed1eb1b708f200a2b030ffcdebeeb15375d38c88c37c8d682b199be4e27`; source SHA / byte size / duration / full decode all PASS.
- Product Owner listened to the delivered QC WAV and explicitly confirmed: `音频OK`.
- Locked S02-B canonical source-audio boundary: `01:18.750 → 02:23.000`.
- Formal approval record: `docs/project_control/gates/P0_3_video_pipeline/s02_b_audio_only_qc_v001_approval_2026-09-29.md`.
- No Story Shot design, generation, registration, video assembly, or P0.3 Gate approval was performed in this step.
- Next step: `S02-B Director Shot Design`.

## 2026-09-29｜S02-B Director Shot Design V0.1 Approval

Status: `COMPLETE / PRODUCT OWNER APPROVED / LOCKED`

- Product Owner approved the complete S02-B Director Shot Design arrangement.
- Locked source-audio authority remains `01:18.750 → 02:23.000` / `64.250s`.
- Locked visual sequence: `N16 → N17 → N18 → N19 → N20 → N21 → A06 → N22`.
- New Story Shots required: `N16–N22` (7).
- Existing approved Story Shot reuse: `A06｜门不关` (1).
- `A07｜大厅建立镜` is explicitly held for the following hall-introduction sequence.
- Exterior Neil speaking shots N02/N06/N07 are excluded from N22 reuse because they carry the wrong spatial-temporal state.
- N03 is excluded from N16/N17 reuse because it carries the exterior opening state.
- No Bundle was built, no Work image generation was started, no Story Shot was registered, and no video assembly was performed in this step.
- Next stage under the locked Story Shot workflow: `N16 Scene Reference Design`.

## 2026-09-29｜N16 Scene Reference Approval + Bundle Design V0.1

Status: `SCENE REFERENCE APPROVED + LOCKED / BUNDLE DESIGN READY FOR PRODUCT OWNER REVIEW`

- Product Owner approved N16 Scene Reference Design V0.1.
- Locked six-reference set:
  - AST_IMG_000057 Jun Character Reference Sheet;
  - AST_IMG_000072 Jun FACE_3Q_LEFT;
  - AST_IMG_000060 Ning Character Reference Sheet;
  - AST_IMG_000033 Ning FACE_3Q_RIGHT;
  - AST_IMG_000052 Castle Entrance Scene Master / DAY_DOOR_OPEN;
  - A03 approved Story Shot / interior reverse continuity.
- N16 Reference Delivery Bundle Design V0.1 created.
- Target bundle: `N16_REFERENCE_DELIVERY_BUNDLE_V001`.
- Planned transport: GitHub Actions → short-lived Artifact → Work automatic acquisition.
- Product Owner manual reference upload target: 0.
- Build contract: fail closed unless 6/6 exact canonical binaries verify.
- Story Shot ID remains globally unique as `N16`; sequence ownership is separate as `S02-B`.
- No Bundle Artifact was built and no image generation was started in this step.

## 2026-09-29｜Generic Story Shot Bundle Builder + N16 First Production Pass

Status: `IMPLEMENTED / VERIFIED / N16 BUNDLE BUILT / READY FOR WORK`

- Product Owner approved the permanent Generic Story Shot Reference Bundle Builder approach.
- Fixed workflow: `.github/workflows/story-shot-reference-bundle-builder.yml`.
- Fixed builder: `scripts/story_shot_reference_bundle_builder_v1.py`.
- Per-shot control plane: `production/bundle_specs/*.json`.
- N16 first production spec: `production/bundle_specs/N16_REFERENCE_DELIVERY_BUNDLE_V001.json`.
- N16 source commit: `4a9df630c36e2fc92ada929fcd80403ab57c74e3`.
- Generic Builder run: `36514238747`; job: `109232868440`; result: SUCCESS.
- Artifact: `N16_REFERENCE_DELIVERY_BUNDLE_V001`; ID `11010505345`.
- Artifact digest: `sha256:e44c4fc8e9b8d1499af8866ac601137dd315ac1f386a544eec19b709ac5cd0ff`.
- Artifact size: `11932780` bytes; expires `2026-10-06T02:47:42Z`.
- Builder exact verification: `6/6 PASS`.
- A03 build-computed SHA-256: `5dc075a6f917fb7fdc05cf299315675bfdd5db4a0d737518ef4aafeacc78ee1e`.
- Chat downloaded the Artifact and independently revalidated all six delivered PNG SHA-256 / byte sizes: PASS.
- Downloaded ZIP SHA-256 matches the GitHub Artifact digest exactly.
- `GENERATION_ALLOWED=TRUE`.
- Product Owner manual reference upload: 0.
- No Work image generation was executed in this step.
- From N17 onward, create/update Bundle Spec JSON and reuse the fixed Builder instead of creating another per-shot workflow.

## 2026-09-29｜N16 Candidate 01 Product Owner Approval + Exact Binary Verification

Status: `PRODUCT OWNER APPROVED / EXACT BINARY VERIFIED / CANONICAL PUBLICATION PENDING`

- Product Owner approved `N16 Candidate 01`.
- Candidate 02 remains a non-selected revision attempt only.
- Approved source dimensions: `941x1672`.
- Approved source byte size: `1942422`.
- Approved source SHA-256: `b26fb7d64a60fbd28d39b0ae22f7c85df18d4f947f31a3591c847dd5e1acf406`.
- Approved source Git blob: `44971dd53e37cd1b582bcf5094b0f09cb8e0647d`.
- PNG signature: PASS.
- Bundle provenance remains `N16_REFERENCE_DELIVERY_BUNDLE_V001`, run `36514238747`, Artifact `11010505345`, 6/6 exact references PASS.
- Approval checkpoint: `docs/project_control/gates/P0_3_video_pipeline/s02_b_n16_approval_checkpoint_2026-09-29.md`.
- No canonical publication, Story Shot registration or registration verification has been performed yet.
- Next step: N16 Canonical Publication using the exact approved binary identity only.

## 2026-09-29｜CHAT_TO_GITHUB_BINARY_BRIDGE_V1｜N16 Real Test

Status: `SOURCE BINARY VERIFIED / CHAT-NATIVE GITHUB BINARY DELIVERY BLOCKED`

- Product Owner authorized a real N16 Candidate 01 test using Chat as GitHub delivery/control plane.
- Chat re-read the approved original PNG from the conversation attachment.
- Exact identity PASS: 941x1672 / 1942422 bytes / SHA-256 `b26fb7d64a60fbd28d39b0ae22f7c85df18d4f947f31a3591c847dd5e1acf406` / Git blob `44971dd53e37cd1b582bcf5094b0f09cb8e0647d`.
- Current GitHub connector capabilities were inspected.
- Connector can write UTF-8 files and Git objects from supplied text/base64 content, but exposes no supported action that accepts the existing Chat conversation attachment / local container path / file ID / file URI as a raw binary upload source.
- GitHub app permission currently follows the ChatGPT default `Allow low-risk actions`; sensitive local-file upload operations may be denied under that mode.
- Changing GitHub app permission alone would not create the missing Chat file-handle upload action.
- No binary was uploaded, no candidate intake workflow was triggered, no canonical publication or Story Shot registration occurred.
- Evidence path: `docs/project_control/gates/P0_3_video_pipeline/chat_to_github_binary_bridge_v1.md`.

## 2026-09-29｜N16 Exact Binary Verification + Canonical Publication

Status: `COMPLETE / EXACT BLOB PRESERVED / REGISTRATION PENDING`

- Product Owner-approved source was uploaded to GitHub as `古堡门内的低声交谈.png`.
- GitHub blob matched the locked approved source exactly: `44971dd53e37cd1b582bcf5094b0f09cb8e0647d`.
- Formal exact-binary verification workflow run `36521093516`, job `109253896090`: SUCCESS.
- Verification result: 941x1672 / 1942422 bytes / SHA-256 `b26fb7d64a60fbd28d39b0ae22f7c85df18d4f947f31a3591c847dd5e1acf406` / Git blob `44971dd53e37cd1b582bcf5094b0f09cb8e0647d` / OVERALL_RESULT=PASS.
- Canonical exact-blob publication workflow run `36521143839`, job `109254056898`: SUCCESS.
- Publication commit: `c8fa5dc9f8b75ce7cb7c6f01899cbf45745558eb`.
- Canonical path: `production/image_library/approved/story_shots/N16_SISTER_QUESTION_APPROVED_V001.png`.
- Exact Git blob preserved: YES.
- Root upload source removed by exact rename.
- No Story Shot Registration or Registration Verification performed in this step.

## 2026-09-29｜N16 Story Shot Registration + Verification Closeout

Status: `COMPLETE / PRODUCT OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED / CLOSED`

- N16 Story Shot Index registration commit: `2de7c5eec0cf4223dbb04f12fb38f20dbe3860ca`.
- Registered canonical binary: `production/image_library/approved/story_shots/N16_SISTER_QUESTION_APPROVED_V001.png`.
- Exact identity retained: 941x1672 / 1942422 bytes / SHA-256 `b26fb7d64a60fbd28d39b0ae22f7c85df18d4f947f31a3591c847dd5e1acf406` / Git blob `44971dd53e37cd1b582bcf5094b0f09cb8e0647d`.
- Registration verification workflow run `36530978877`, job `109284366914`: SUCCESS.
- Verification result: `N16_PASS / SHA_MATCH=YES / BLOB_MATCH=YES / INDEX_MATCH=YES / DIMENSIONS_MATCH=YES / STAGING_CLEANUP_PASS / OVERALL_RESULT=PASS`.
- N16 formal closeout record: `docs/project_control/gates/P0_3_video_pipeline/s02_b_n16_story_shot_registration_closeout_2026-09-29.md`.
- Product Owner stopped the automatic final-candidate upload experiments for the current S02-B production cycle.
- `STORY_SHOT_CANDIDATE_DELIVERY_BRIDGE_V1` and `CHAT_TO_GITHUB_BINARY_BRIDGE_V1` are retained as `PAUSED / EXPERIMENTAL ONLY`.
- Current S02-B production path returns to: Work generation → PO review → one manual approved-PNG upload → Chat exact verification/publication/registration.
- N16 is closed. N17 has not started.

## 2026-09-29｜N17 Scene Reference Design V0.1

Status: `READY FOR PRODUCT OWNER REVIEW`

- Parent authority: `S02-B Director Shot Design V0.1 / PRODUCT OWNER APPROVED + LOCKED`.
- Shot: `N17｜Blood-Door Warning`.
- Source TC: `01:28.120→01:40.700`.
- Reference strategy intentionally differs from N16: use the formally closed N16 canonical Story Shot as immediate shot-to-shot continuity authority instead of A03.
- Proposed minimum set = 6 canonical references:
  1. AST_IMG_000060 — Ning Character Reference Sheet
  2. AST_IMG_000033 — Ning FACE_3Q_RIGHT
  3. AST_IMG_000057 — Jun Character Reference Sheet
  4. AST_IMG_000072 — Jun FACE_3Q_LEFT
  5. AST_IMG_000052 — Castle Entrance Scene Master / DAY_DOOR_OPEN
  6. N16 — immediate approved Story Shot continuity
- Visual progression locked for review: `Jun-speaking emphasis → Ning-speaking emphasis`.
- Ning remains screen-left / Jun screen-right; framing becomes slightly tighter and more Ning-weighted.
- Explicitly excluded: A03, N03, N14, A05, A07, all future N18–N22 imagery.
- No Bundle spec created, no Artifact built, no Work generation authorized.
- Design path: `docs/project_control/gates/P0_3_video_pipeline/n17_scene_reference_design_v0_1.md`.

## 2026-09-29｜N17 Scene Reference Design V0.2 — Close-up Revision

Status: `READY FOR PRODUCT OWNER REVIEW`

- Product Owner requested stronger visual differentiation from N16.
- N17 Scene Reference Design V0.1 is superseded.
- V0.2 changes framing from medium / medium-close two-shot to `Ning-dominant close-up / tight medium-close`.
- Jun remains only as a secondary listener at screen-right, preferably partial cheek/shoulder edge or soft foreground 3/4 presence.
- Immediate visual progression is now: `N16 balanced two-shot / Jun emphasis → N17 Ning close-up / survival-warning emphasis`.
- The same six canonical references remain sufficient; no new reference asset is required.
- No Bundle Spec created, no Artifact built, no Work generation authorized.
- V0.2 path: `docs/project_control/gates/P0_3_video_pipeline/n17_scene_reference_design_v0_2.md`.

## 2026-09-29｜N17 Reference Delivery Bundle Design V0.1

Status: `READY FOR PRODUCT OWNER REVIEW`

- Product Owner approved `N17 Scene Reference Design V0.2`; it is now `PRODUCT OWNER APPROVED / LOCKED`.
- Target Bundle: `N17_REFERENCE_DELIVERY_BUNDLE_V001`.
- Target generation: `N17 Candidate 01`.
- Locked reference count: `6`.
- References:
  1. AST_IMG_000060 — Ning Character Reference Sheet
  2. AST_IMG_000033 — Ning FACE_3Q_RIGHT
  3. AST_IMG_000057 — Jun Character Reference Sheet
  4. AST_IMG_000072 — Jun FACE_3Q_LEFT
  5. AST_IMG_000052 — Castle Entrance Scene Master / DAY_DOOR_OPEN
  6. N16 — immediate approved Story Shot continuity
- N16 direct exact identity is available and must be verified by locked SHA-256 / byte_size / Git blob; no computed-SHA fallback is needed.
- WORK_HANDOFF locks the N17 close-up strategy: Ning dominant, Jun secondary edge/soft foreground, visibly tighter than N16, shallow background.
- Fixed Generic Story Shot Reference Bundle Builder V1 remains mandatory.
- No new per-shot workflow is allowed.
- No Bundle Spec created, no GitHub Actions build triggered, no Artifact produced, no Work generation authorized.
- Design path: `docs/project_control/gates/P0_3_video_pipeline/n17_reference_delivery_bundle_design_v0_1.md`.


- 2026-09-29｜P0.3 S02-B｜N17/N18 formal archival closeout: exact verification PASS; exact-blob publication commit c211475b78a8a800ff55fbf76201707a5f1bf3f8; Story Shot registration commit 41e0a829419ff0f975e8bc6acce8e4f8c85ecb2e; registration verification PASS; archival run 36574163058.

## 2026-09-30｜N19 Story Shot Formal Archival Closeout

Status: `COMPLETE / PRODUCT OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED / CLOSED`

- Selected final: `N19 Candidate 04｜Localized Shoulder Gesture Edit`.
- Source upload commit: `a8c75f200b72ccf2a06b2e4d47b7b217005c1536`.
- Exact binary verification run `36651718484`, job `109687128829`: PASS.
- Exact identity: 941x1672 / 2052606 bytes / SHA-256 `5cc7e09716adf91a56b52f4714cc84945c73a4cbc5ed6162d90f2f3a9b351c7a` / Git blob `c842ad1a0b84b2d504b1e681dd327b01bb57c159`.
- Canonical exact-blob publication commit: `95d2bda461e74e0c3c5c6852684e5ca3d3bbb92a`.
- Canonical path: `production/image_library/approved/story_shots/N19_CONDITIONS_CAN_CHANGE_APPROVED_V001.png`.
- Story Shot registration commit: `4185a567341f29adcbb40f8d3d089e5db60b784c`.
- Registration verification run `36651939930`, job `109687829876`: SUCCESS / SHA_MATCH / BLOB_MATCH / INDEX_MATCH / DIMENSIONS_MATCH / STAGING_CLEANUP_PASS.
- N19 is formally closed.
- Next: `N20 Reference Delivery Bundle Design V0.1`.

## 2026-09-30｜N20 Reference Delivery Bundle Design V0.1

Status: `READY FOR PRODUCT OWNER REVIEW`

- Parent N20 Scene Reference Design V0.1 remains Product Owner approved / locked.
- Spatial execution clarified to `INTERIOR-SIDE REAR-3Q OBLIQUE FOLLOWING VIEW` so inward walking and receding doorway light can coexist without contradictory camera geometry.
- N19 was formally evaluated as a possible direct image reference after its closeout.
- Decision: do NOT include N19 in the N20 generation Bundle because its static shared-outward-gaze / shoulder-contact / doorway-pause composition creates a strong carryover risk precisely where N20 must introduce a new movement state.
- Proposed 5-reference set:
  1. AST_IMG_000060 — Ning Character Reference Sheet
  2. AST_IMG_000037 — Ning REAR_3Q_RIGHT V002
  3. AST_IMG_000057 — Jun Character Reference Sheet
  4. AST_IMG_000064 — Jun REAR_3Q_LEFT V001
  5. AST_IMG_000052 — Castle Entrance Scene Master / DAY_DOOR_OPEN
- N19 remains narrative continuity predecessor only.
- Hard performance lock: N19 shoulder contact ends before / as N20 movement begins; no camera-facing turn for facial visibility.
- No Bundle Spec created; no GitHub Actions build triggered; no Work generation authorized.
- Design path: `docs/project_control/gates/P0_3_video_pipeline/n20_reference_delivery_bundle_design_v0_1.md`.

## 2026-09-30｜N20 Reference Delivery Bundle V001 Build

Status: `PASS / READY FOR WORK GENERATION`

- Product Owner approved N20 Reference Delivery Bundle Design V0.1.
- Bundle Spec commit: `c3ac5d3d848a8823a13770636a033eb2636e68e9`.
- Generic Builder run `36654654071`, job `109696257939`: SUCCESS.
- Artifact: `N20_REFERENCE_DELIVERY_BUNDLE_V001` / ID `11072080675`.
- Artifact size: `8701679` bytes.
- Artifact digest: `sha256:203f866487808d99aeb7a408a91e5c599c919b889372444e78e1fbc3d11b3230`.
- Builder exact canonical verification: `5/5 PASS`.
- Chat independently downloaded and revalidated the Artifact ZIP: digest MATCH; all 5 PNG byte sizes / SHA-256 / Git blobs / PNG signatures MATCH.
- `GENERATION_ALLOWED=TRUE`.
- Product Owner manual reference upload: `0`.
- No N20 candidate was generated in this step.

## 2026-09-30｜N20 Candidate 03 Rejection + Bundle V002 Redesign

Status: `C01-C03 REJECTED / BUNDLE V002 DESIGN READY FOR PRODUCT OWNER REVIEW`

- Candidate 03 successfully improved slow同行 walking, gait separation, warm interior lighting and transition-zone scale.
- Product Owner rejected Candidate 03 because both characters had visibly changed and no longer matched approved Ning Qiushui / Jun Luyuan identities.
- Root corrective decision: stop further generation from Bundle V001.
- Proposed V002 reference set: AST_IMG_000060 / AST_IMG_000057 / N19 canonical / AST_IMG_000037 / AST_IMG_000064.
- Scene Master AST_IMG_000052 remains canonical scene authority in design, but is removed from the five-image generation input set.
- N19 is authorized only as actual on-screen appearance / wardrobe / body proportion / render-language continuity; N19 pose, shoulder contact, outward gaze and composition must not carry into N20.
- Candidate 04 remains NOT AUTHORIZED until V002 is Product Owner approved, built and verified.
- Design: `docs/project_control/gates/P0_3_video_pipeline/n20_reference_delivery_bundle_design_v0_2.md`.

## 2026-09-30｜N20 Reference Delivery Bundle V002 Build

Status: `PASS / READY FOR N20 CANDIDATE 04 WORK GENERATION`

- Product Owner approved N20 Reference Delivery Bundle Design V0.2.
- Bundle Spec commit: `67c316246fd76b5d039148d524c587ef67899617`.
- Generic Builder run `36658459273`, job `109707734342`: SUCCESS.
- Artifact: `N20_REFERENCE_DELIVERY_BUNDLE_V002` / ID `11073610356`.
- Artifact size: `8448179` bytes.
- Artifact digest: `sha256:ff3ab2ba9b22bad988cd201972a27236b2a9f7c2730d4109680664ebabcfd4bd`.
- GitHub exact verification: `5/5 PASS`.
- Chat independent Artifact verification: ZIP digest MATCH; all five PNG byte sizes / SHA-256 / Git blobs / PNG signatures MATCH.
- `GENERATION_ALLOWED=TRUE`.
- V002 supersedes V001 for subsequent N20 generation.
- Candidate 01–03 remain rejected and are not generation references.
- No Candidate 04 generated in this step.

## 2026-09-30｜N20 Story Shot Formal Archival Closeout

Status: `COMPLETE / PRODUCT OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED / CLOSED`

- Selected final: `N20 Candidate 04｜Clean Regeneration / Bundle V002`.
- Source upload commit: `390f8c837a66f166dc98c98ff88f2906aa160b14`.
- Exact binary verification run `36663290811`, job `109722497256`: PASS.
- Exact identity: 941x1672 / 2022630 bytes / SHA-256 `a61ab1310e86938b2a416516138981aafaf421add44c1a9d5a80d0ff9ec59a9e` / Git blob `58e145a51c3f993827e5e47964ad0e7f9dd9f0aa`.
- Canonical exact-blob publication commit: `230cdbd8e3e78e4211a287eaffe5073f5231485e`.
- Canonical path: `production/image_library/approved/story_shots/N20_DO_NOT_TOUCH_THINGS_APPROVED_V001.png`.
- Story Shot registration commit: `6381aa74cd7f959b65798d1eb21db5fa8ee99f96`.
- Registration verification run `36663515652`, job `109723183583`: SUCCESS.
- N20 is formally closed.
- Next: `N21｜Sixteen Guests Enter｜Scene Reference Design V0.1`.


## 2026-09-30｜S02-B V0.3 + N21 Responsibility Redesign

Status: `PRODUCT OWNER APPROVED / LOCKED`

- S02-B V0.3 + Review Patch 01 approved.
- N16–N20 remain locked / no rework.
- Revised downstream sequence: `N21 → N22 → N23 → N24 → A06 → N25 → N26 → N27`.
- Named-character seeding redistributed: N21 group-scale function first; N22 owns most named-character seeding.
- Eight high-level cinematic rules locked, including generation-stage color/look continuity and deferred exact composition.
- N21 Node-Level Director Shot Design V0.1 approved.
- N21 Scene Reference V0.3 approved.
- N21 Bundle V002 reduced generation inputs to exactly `AST_IMG_000052 + N20`.

## 2026-09-30｜N21 Reference Delivery Bundle V002 Build

Status: `PASS / TECHNICALLY VALID / FURTHER USE NOW PAUSED`

- Spec commit: `26aebca839ec5016762bed92bc9b52a5aa430b99`.
- Generic Builder run `36699004641`, job `109833744730`: SUCCESS.
- Artifact: `N21_REFERENCE_DELIVERY_BUNDLE_V002`, ID `11088797193`.
- Artifact digest: `sha256:e3ec3be6f1a75eae6507801a776bcf2a6e07312d2a26a91909466a73b805f4dc`.
- Exact canonical verification: `2/2 PASS`.
- Independent downloaded-artifact verification: `2/2 PASS`.
- Builder emitted `GENERATION_ALLOWED=TRUE`.
- Product Owner manual reference upload: `0`.
- After C01–C03 review, further use of V002 is paused pending N21 task-scope simplification.

## 2026-09-30｜N21 Candidate 01–03 Review + EOD Pause

Status: `NO CANDIDATE APPROVED / C04 NOT AUTHORIZED`

- Candidate 01: not accepted; frontal ensemble, hero-duo dominance, over-choreographed crowd, excessive face readability, over-bright entrance.
- Candidate 02: not accepted; entry-space geometry / adventure-threat read failed; crowd read too much like ordinary commuter flow.
- Candidate 03: not accepted; atmosphere improved, but Jun posture drifted, Ning identity drifted, protagonist weight remained too strong, residual orderly-flow feeling remained.
- Product Owner explicitly questioned further rule accumulation as a solution; current observed pattern is a multi-person generation tradeoff among crowd composition, atmosphere, character identity and body performance.
- Root cause is NOT proven as model degradation.
- Candidate 04 is NOT authorized.
- N22 is NOT started.
- Resume point: `N21 TASK-SCOPE SIMPLIFICATION / DIRECTOR STRATEGY REVIEW`.


## 2026-10-01｜N21 Scene Reference Design V0.4 Approval

Status: `PRODUCT OWNER APPROVED / LOCKED / BUNDLE V003 DESIGN NEXT`

- N21 single-frame responsibility was simplified from cohort-scale proof to `THRESHOLD TRANSITION + UNKNOWN-SPACE MOOD`.
- Canonical fact `16 participants total` remains unchanged, but exact single-frame counting is no longer required.
- Preferred visible complexity is approximately 4–6 readable people with crop / occlusion / silhouette / off-frame continuation allowed.
- Ning Qiushui / Jun Luyuan are no longer mandatory identity targets in N21 and must not dominate the frame.
- Character visual style continuity is now a hard Director gate; visible people must remain inside the established approved Story Shot human-rendering language.
- Formal reference strategy approved for next Bundle design:
  - `AST_IMG_000052` = space / architecture authority;
  - `N03_VISITOR_REACTION_APPROVED_V001.png` = character visual-style / multi-person rendering-language authority.
- `N20_DO_NOT_TOUCH_THINGS_APPROVED_V001.png` = Director continuity review only; not a proposed formal generation input.
- `N21_REFERENCE_DELIVERY_BUNDLE_V002` = technically valid / creative scope superseded.
- `RISK-003` remains ACTIVE; scope simplification alone does not prove generation stability.
- Candidate 04 remains NOT AUTHORIZED.
- N22 remains NOT STARTED.
- Next step: `N21_REFERENCE_DELIVERY_BUNDLE_V003 DESIGN` only.


## 2026-10-01｜N21 Reference Delivery Bundle V003 Build + Independent Verification

Status: `PASS / GENERATION_ALLOWED=TRUE / READY FOR WORK GENERATION`

- Spec commit: `6a03dc80fb7cf75ca5908d5ed364fed45fd988a8`.
- Workflow run: `36817339701`.
- Job: `110225166295`.
- Builder result: `PASS: 2/2 exact canonical reference binaries verified`.
- Artifact: `N21_REFERENCE_DELIVERY_BUNDLE_V003` / ID `11141917821`.
- Artifact size: `4606668` bytes.
- Artifact digest: `sha256:8be16a3538394046d1a875ff6a5e4802dd097bd52c44e8efd863af8807d9eaa0`.
- Independent ZIP digest: MATCH.
- `AST_IMG_000052`: 2305753 bytes / 941×1672 / SHA MATCH / PNG PASS.
- `N03`: 2321221 bytes / 941×1672 / SHA MATCH / PNG PASS.
- Product Owner manual reference upload: `0`.
- Candidate 04 may proceed as `CLEAN REGENERATION` through Work.
- RISK-003 remains ACTIVE until candidate evidence exists.
- N22 remains NOT STARTED.


## 2026-10-01｜N21 Candidate 04 Review

Status: `NOT APPROVED / REFERENCE CONTENT LEAKAGE`

- Candidate 04 was generated from verified `N21_REFERENCE_DELIVERY_BUNDLE_V003`.
- Bundle integrity remained `2/2 PASS`; no transport or exact-binary failure occurred.
- Human rendering style was broadly stable and body structure improved relative to Candidate 03.
- Main failure: the complete N03 Story Shot leaked concrete wardrobe / figure configuration into the generated result rather than acting as a style-only authority.
- Secondary issues: unknown/danger feeling remained weak; entrance daylight was strong; group flow retained some queue-like sequential movement.
- Product Owner rejected Candidate 04.
- Bundle V003 disposition: `TECHNICALLY VALID / CREATIVE REFERENCE STRATEGY FAILED`.
- N03 disposition for future N21 generation: `DO NOT REUSE AS FORMAL STYLE INPUT`.
- Product Owner approved next step: `Character Visual Style Reference V0.1｜Design`.
- Candidate 05 remains NOT AUTHORIZED.
- RISK-003 remains ACTIVE.


## 2026-10-01｜Character Visual Style Reference V0.1 Design

Status: `DIRECTOR DESIGN LOCK / PRODUCT OWNER REVIEW REQUIRED / NOT YET BUILT`

- New controlled reference proposed: `CHARACTER_VISUAL_STYLE_REFERENCE_V001`.
- Purpose: carry human visual language without carrying complete Story Shot composition, named-character showcase, scene background or reusable wardrobe/cast grouping.
- Design source set: six approved CURRENT Atomic Character assets from Guang Yong, Liao Jian, Su Xiaoxiao and Wen Qingya.
- Ning Qiushui / Jun Luyuan, all Story Shots and Character Reference Sheets are excluded.
- Build method: deterministic crop + resize + contact-sheet composition only; no AI generation, retouch, relight, recolor or generative fill.
- Proposed board: `1536x1024`, landscape, 3x2 equal-weight panels.
- Governance: proposed as P0.3 `CONTROLLED_PRODUCTION_REFERENCE`; do not mis-register as a single P0.2 Entity DERIVED_REFERENCE.
- Future Bundle integration will require an explicit `CONTROLLED_REFERENCE` source type rather than misusing `ASSET` or `STORY_SHOT`.
- Candidate 05 remains NOT AUTHORIZED.


## 2026-10-01｜Character Visual Style Reference V001 Exact Crop Plan + Build Prep

Status: `LOCKED / BUILD PREP READY / FORMAL BOARD NOT YET BUILT`

- Product Owner authorized progression from V0.1 design review.
- Source inspection successful on run `36820797772`; Artifact `11143985053`; 6/6 exact canonical Atomic PNG verification PASS.
- Exact six-panel crop plan written to `production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.crop_plan.json`.
- Final board geometry locked: 1536×1024 RGB / neutral RGB(144,144,144) / 48px outer margin / 24px gutters / 3×2 fixed slots.
- Four panels are single-side face/hair/skin fragments; two panels are clothing-material/upper-torso fragments; no complete person or complete outfit is permitted.
- No Ning Qiushui / Jun Luyuan source, no Story Shot, and no Character Reference Sheet is used.
- Build contract requires pinned Python + Pillow, fixed LANCZOS contain-fit, fixed rounding, no image generation or retouching, and two-run output SHA-256 equality before publication.
- During source inspection, the generic Bundle Builder exposed a shallow-checkout spec-selection bug. Final fix: checkout fetch-depth=2 and fail-closed HEAD^→HEAD single-spec selection. Successful verification occurred on run `36820797772`.
- Formal Style Board builder implementation / build / publication remain NOT AUTHORIZED.
- N21 Candidate 05 remains NOT AUTHORIZED; RISK-003 remains ACTIVE.


## 2026-10-01｜Character Visual Style Reference V001 Deterministic Builder + Two-Run Proof

Status: `TECHNICAL DETERMINISM PASS / DIRECTOR VISUAL PREFLIGHT PASS / PO VISUAL REVIEW REQUIRED`

- Product Owner authorized builder implementation + two-run proof.
- Workflow: `.github/workflows/character-visual-style-reference-v001-determinism.yml`.
- Builder: `scripts/build_character_visual_style_reference_v001.py`.
- Proof source commit: `a38a4471f521c3008dc32edb6cf6eaa069bf0f22`.
- Run: `36822615026`; Job: `110241244661`; conclusion SUCCESS.
- Environment: Python `3.12.14`; Pillow `11.3.0`.
- Run A SHA: `8d650483b6e082a80d41d93e14c7957595c451097aac63f3c84cbcc1ddc7ce41`; bytes `1301730`.
- Run B SHA: same; bytes `1301730`.
- SHA equality / byte-size equality / direct byte comparison: PASS.
- Artifact: `CHARACTER_VISUAL_STYLE_REFERENCE_V001_TWO_RUN_PROOF`; ID `11143724172`; digest `sha256:91d93bcccceafb5ef47eca5dd6d8f91054e84f87f755785ee2581638f4af55ef`.
- Independent Artifact ZIP digest verification: MATCH.
- Independent Run A / B PNG verification: `1536×1024 / RGB / PNG / byte-identical`.
- Director visual preflight: PASS / partial style fragments only / no full Story Shot, complete person, complete outfit, Ning/Jun, group composition or labels.
- Canonical publication is NOT AUTHORIZED.
- Candidate 05 remains NOT AUTHORIZED; RISK-003 remains ACTIVE.


## 2026-10-01｜Character Visual Style Reference V001 Product Owner Visual Approval

Status: `PRODUCT OWNER APPROVED / EXACT BINARY LOCKED / CANONICAL PUBLICATION NEXT`

- Product Owner visually approved the deterministic Style Board.
- Exact approved binary: `1536×1024 / RGB / PNG / 1301730 bytes`.
- SHA-256: `8d650483b6e082a80d41d93e14c7957595c451097aac63f3c84cbcc1ddc7ce41`.
- Approval source: run `36822615026` / job `110241244661` / Artifact `11143724172`.
- Authority scope: human visual-style language only; not named identity, full outfit, pose, group composition or scene.
- Canonical publication must preserve exact binary bytes; no image rewrite or re-encode is allowed.
- RISK-003 remains ACTIVE pending real N21 generation evidence.
- Candidate 05 remains NOT AUTHORIZED.


## 2026-10-01｜Character Visual Style Reference V001 Canonical Publication

Status: `PRODUCT OWNER APPROVED / CANONICAL PUBLISHED / REMOTE VERIFIED`

- Publication request commit: `abb3ac4d74ac670550bb1aea5228ff73b7aa55cd`.
- Publication run: `36823958149`; job: `110245367477`; SUCCESS.
- Publication commit: `36f146655fa9334d399fd3369f267dd406963ab2`.
- Canonical PNG: `production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.png`.
- Canonical manifest: `production/style_references/character_visual/CHARACTER_VISUAL_STYLE_REFERENCE_V001.manifest.json`.
- Exact binary: `1536×1024 / RGB / PNG / 1301730 bytes`.
- SHA-256: `8d650483b6e082a80d41d93e14c7957595c451097aac63f3c84cbcc1ddc7ce41`.
- Git blob: `216b1739db17cb3b183d613e4aefa6374d1088e2`.
- Post-publication remote SHA / bytes / Git blob / manifest verification: PASS.
- Publication proof Artifact: `11144775274`; digest `sha256:ceb87ff5a65d83bd2b0b4bacbccd657c4de987ccc5ce33ebdf0b53202ec18b43`.
- RISK-003 remains ACTIVE.
- N21 Candidate 05 remains NOT AUTHORIZED.
- Next design step: `CONTROLLED_REFERENCE delivery support + N21 Bundle V004 Design`.


## 2026-10-01｜CONTROLLED_REFERENCE + N21 Bundle V004 Design Lock

Status: `PRODUCT OWNER APPROVED / LOCKED / IMPLEMENTATION NOT YET AUTHORIZED`

- New P0.3 source type design: `CONTROLLED_REFERENCE`.
- N21 V004 formal input set locked to exactly two references:
  1. `AST_IMG_000052` — scene / architecture / open-door threshold facts only;
  2. `CHARACTER_VISUAL_STYLE_REFERENCE_V001` — character visual-style authority only.
- N03, N20, all named-character Character Sheets, A07, and N21 Candidate 01–04 are excluded.
- CONTROLLED_REFERENCE validation must fail closed on manifest / approval / lifecycle / authority / path / SHA / bytes / Git blob / PNG-readability / copied-binary mismatch.
- Product Owner manual reference upload remains `0`.
- Candidate 05 remains `NOT AUTHORIZED` pending V004 implementation/build/exact verification.
- RISK-003 remains ACTIVE.


## 2026-10-01｜CONTROLLED_REFERENCE Builder Support + N21 V004 Spec

Status: `COMPLETE / VALIDATION-ONLY 2 OF 2 PASS / FORMAL BUILD NOT AUTHORIZED`

- Product Owner authorization scope: Builder Support + V004 Spec only.
- Initial CONTROLLED_REFERENCE support commit: `2afef948bd396dd418a7d6289124c7811f616e09`.
- Builder validation/build gate hardening: `b636a2de2a63ddfb119c9c795b002e8a322650bd`.
- Workflow authorization gate: `4c124dad017cbc05ad6604098b7f28f35e1d0529`.
- V004 gated spec commit: `81d3ca4d80f745f6cf370f18567df2d9cb6460c5`.
- Current spec: `production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V004.json` / `build_authorized=false` / revision `V004-R2`.
- Validation-only run: `36826494510`; job: `110253232876`; conclusion SUCCESS.
- Result: `VALIDATION_PASS: 2/2 exact canonical references verified`.
- Gate result: `BUILD_AUTHORIZED=FALSE / GENERATION_ALLOWED=FALSE`.
- Bundle build step: SKIPPED; Artifact upload step: SKIPPED; Artifact count: 0.
- Historical pre-gate auto-trigger: run `36825856946` / Artifact `11144634603`; disposition `DO NOT USE / NOT FORMALLY AUTHORIZED`.
- Candidate 05 remains NOT AUTHORIZED.
- Next: separate Product Owner authorization for formal V004 Build + exact verification.


## 2026-10-01｜N21 Reference Delivery Bundle V004 Formal Build + Exact Verification

Status: `FORMAL BUILD PASS / 2 OF 2 EXACT VERIFIED / GENERATION_ALLOWED=TRUE / CANDIDATE 05 NOT YET AUTHORIZED`

- Product Owner authorized formal V004 Build + Exact Verification.
- Spec revision: `V004-R3`; build gate `true`; authorization commit `b0dd5dc00b70b953974e3580d6e4cb671c836848`.
- Workflow run: `36826967264`; job: `110254694293`; conclusion SUCCESS.
- Builder result: `PASS: 2/2 exact canonical reference binaries verified` / `GENERATION_ALLOWED=TRUE`.
- Formal Artifact: `11145497260`; size `3596063`; digest `sha256:0b3227f30d8156ed7be3f421f5b43d9233aba4fc609dedd09d76f4f1dc0ea27d`.
- Independent downloaded ZIP SHA: exact digest MATCH.
- delivery_manifest: 2 refs / all_reference_checks_pass=true / generation_allowed=true / overall_result=PASS.
- AST_IMG_000052 copy: 941×1672 / 2305753 bytes / SHA d49af6a5...3961 / blob e4dafe09...08f9 / EXACT MATCH.
- Style Reference copy: 1536×1024 / 1301730 bytes / SHA 8d650483...7ce41 / blob 216b1739...88e2 / EXACT MATCH.
- Historical pre-gate Artifact `11144634603`: DO NOT USE.
- Candidate 05 remains NOT YET AUTHORIZED; RISK-003 remains ACTIVE.


## 2026-10-01｜N21 Candidate 05 Work Generation Authorization

Status: `PRODUCT OWNER AUTHORIZED / ONE PNG ONLY / REVIEW REQUIRED`

- Candidate: `N21 Candidate 05｜Clean Regeneration`.
- Formal Bundle: `N21_REFERENCE_DELIVERY_BUNDLE_V004`.
- Formal Artifact: `11145497260` / digest `sha256:0b3227f30d8156ed7be3f421f5b43d9233aba4fc609dedd09d76f4f1dc0ea27d`.
- Historical Artifact `11144634603`: DO NOT USE.
- Work must auto-download and revalidate 2/2 references before generation.
- Generation limit: exactly 1 PNG, then stop for Product Owner review.
- Core visual read: threshold transition + unknown-space mood; approximately 4–6 readable people is sufficient.
- Style Reference authority is visual-language only; copying specific panel identity/outfit/grouping is a hard FAIL.
- Candidate 06 remains NOT AUTHORIZED; N22 NOT STARTED; RISK-003 ACTIVE.


## 2026-10-01｜N21 Candidate 05 / 06 Review

Status: `C05 NOT APPROVED / C06 NOT APPROVED / C07 NOT AUTHORIZED`

- Candidate 05: Style Reference mitigation improved human rendering stability and avoided obvious content leakage, but queue / expedition-team feel and body-performance issues remained.
- Candidate 06: entrance scale increased and bags were removed, but the frame shifted to an over-monumental cathedral-like entrance; daylight flooded the threshold; color / light continuity remained off; crowd still read sequentially.
- Product Owner rejected Candidate 06.
- V004 remains technically valid; no new Bundle build is authorized by this review.
- RISK-003 remains ACTIVE.
- Next: Director Strategy Review before any Candidate 07.


## 2026-10-01｜N21 Director Strategy Review before Candidate 07

Status: `DIRECTOR RECOMMENDATION LOCK / PRODUCT OWNER REVIEW REQUIRED / C07 NOT AUTHORIZED`

- Director inspection Artifact: `N21_DIRECTOR_STRATEGY_REFERENCE_INSPECTION_V001`; run `36831561991`; Artifact `11147044821`; inspection only / not a generation input.
- Inspected approved N01 / N08 / N19 / N20 plus formal Scene Master AST_IMG_000052.
- N08 proves entrance scale but is architecture-hero / monumental and unsuitable as the next direct shot language.
- AST_IMG_000052 remains valid scene authority, but its centered full doorway + large bright sky is not recommended as a direct C07 generation input.
- N20 is the strongest tonal / lighting continuity authority: dim warm interior / no dominant direct exterior sunlight.
- Recommended mitigation: deterministic `N21_ENVIRONMENT_CONTINUITY_REFERENCE_V001` using environment-only crops from Scene Master + N20.
- Future C07 composition: interior-side oblique / partial off-axis doorway / staggered threshold cluster / upright bodies / no bags.
- V004 remains technically valid but is not recommended for direct Candidate 07 reuse.
- Candidate 07 remains NOT AUTHORIZED; N22 NOT STARTED; RISK-003 ACTIVE.


## 2026-10-01｜N21 Threshold Transition Environment Reference V001 Formal Closeout

Status: `PRODUCT OWNER APPROVED / CANONICAL / EXACT VERIFIED / CONTROLLED REFERENCE REGISTERED / CLOSED`

- Approved staging upload commit: `5ecc61e112180fa55b5b8b7a15f093b17e075b08`.
- Canonical publication commit: `7108530b3bbed4bf01aac73c164978210545e4a9`.
- Canonical PNG: `production/environment_references/n21_threshold_transition/N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001.png`.
- Manifest: `production/environment_references/n21_threshold_transition/N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001.manifest.json`.
- Exact identity: `941x1672 / RGBA / 3394494 bytes / SHA-256 dd1b2dc6b831b2e22d8dc249859af1b4f65da6a20437cd8821627144e89a4f13 / blob 358057948ec222bbe63a47a07022de4453e20fc8`.
- Post-publication verification: run `36857195935` / job `110352417813` / all 10 checks PASS / `EXACT_BINARY_MATCH=YES`.
- Registration model: P0.3 controlled canonical binary + manifest; no P0.2 Registry schema extension.
- Staging + one-time verifier cleaned.
- Next: `N21_REFERENCE_DELIVERY_BUNDLE_V005 DESIGN`.
- Candidate 07 remains NOT GENERATED; N22 NOT STARTED; RISK-003 ACTIVE.


## 2026-10-01｜N21 Reference Delivery Bundle V005 Design V0.1

Status: `DIRECTOR DESIGN COMPLETE / PRODUCT OWNER REVIEW REQUIRED / BUILD NOT AUTHORIZED / C07 NOT AUTHORIZED`

- Proposed formal reference count: 2.
- REF-01: `N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001` / environment authority only.
- REF-02: `CHARACTER_VISUAL_STYLE_REFERENCE_V001` / character visual-style authority only.
- Direct `AST_IMG_000052`, N20, all complete Story Shots and all complete Scene Masters are excluded from V005 generation input.
- Future C07 mode: Clean Regeneration only.
- Crowd lock: staggered threshold cluster / upright bodies / no bags / no single-file queue.
- No V005 spec created; no Actions build; no Artifact; no Work generation.
- RISK-003 remains ACTIVE.


## 2026-10-01｜N21 Reference Delivery Bundle V005 Spec + Validation-Only

Status: `APPROVED / SPEC CREATED / 2 OF 2 PASS / NO ARTIFACT / FORMAL BUILD NOT AUTHORIZED`

- Spec: `production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V005.json`.
- Spec commit: `e05b5cefb1be29b5724c4bf782f149a99d2c040c`.
- Validation run: `36859052785` / job `110358458769`.
- Result: `VALIDATION_PASS: 2/2 exact canonical references verified`.
- `BUILD_AUTHORIZED=FALSE`.
- `GENERATION_ALLOWED=FALSE`.
- Artifact count: `0`.
- Next: Product Owner authorization for formal V005 build + exact verification.


## 2026-10-01｜N21 Reference Delivery Bundle V005 Formal Build + Exact Verification

Status: `FORMAL BUILD PASS / 2 OF 2 EXACT VERIFIED / INDEPENDENT ARTIFACT VERIFIED / C07 NOT AUTHORIZED`

- Spec revision: `V005-R2`.
- Authorization commit: `5dcb51deb9f00b01ee36a1e9290a23dbb60c6e8f`.
- Formal run: `36859705482` / job `110360617971` / SUCCESS.
- Builder: `PASS: 2/2 exact canonical reference binaries verified`.
- Bundle-level: `GENERATION_ALLOWED=TRUE`.
- Artifact: `11161920411` / `4697710 bytes` / `sha256:358ea894249d88e93047eabbfeb760196a34c29afdfa2a82277fc875560ecb58`.
- Independent Artifact ZIP digest: MATCH.
- Artifact file count: 4; image-input count: 2.
- Both image inputs independently exact-match canonical binaries.
- Candidate 07 remains NOT AUTHORIZED; N22 NOT STARTED.


## 2026-10-01｜N21 Candidate 07 Work Generation Authorization

Status: `PRODUCT OWNER AUTHORIZED / ONE PNG ONLY / WAITING WORK OUTPUT`

- Candidate: `N21 Candidate 07｜Clean Regeneration`.
- Formal Bundle: `N21_REFERENCE_DELIVERY_BUNDLE_V005`.
- Artifact: `11161920411`.
- Work must auto-acquire Artifact and verify `2/2 exact` before generation.
- Generation limit: exactly `1 PNG`.
- After generation: STOP for Product Owner review.
- Candidate 08: NOT AUTHORIZED.
- N22: NOT STARTED.
- Publication / registration / Project Control closeout: NOT AUTHORIZED.


## 2026-10-01｜N21 Human-Only Crowd Body/Wardrobe Reference Route

Status: `INPUT SPEC CREATED / VALIDATION 4 OF 4 PASS / FORMAL BUILD NOT AUTHORIZED`

- Target: `N21_CROWD_BODY_WARDROBE_REFERENCE_V001 Candidate 01`.
- Inputs: `AST_IMG_000051 / 000064 / 000068 / 000075`.
- No environment image, Story Shot or Style Board in this bundle.
- Validation run: `36865944026` / job `110381336287`.
- Result: `4/4 exact PASS`.
- `BUILD_AUTHORIZED=FALSE` / `GENERATION_ALLOWED=FALSE`.
- Artifact count: `0`.
- N21 Candidate 07: NOT APPROVED / review closed.
- Next: Product Owner authorization for formal input Bundle build.


## 2026-10-01｜N21 Human-Only Input Bundle Formal Build + Exact Verification

Status: `FORMAL BUILD PASS / 4 OF 4 EXACT VERIFIED / INDEPENDENT ARTIFACT VERIFIED / WORK GENERATION NOT AUTHORIZED`

- Bundle: `N21_CROWD_BODY_WARDROBE_REFERENCE_INPUT_BUNDLE_V001`.
- Spec revision: `V001-R2`.
- Authorization commit: `2dae9404d33730d332853923f3c995e538dd5c72`.
- Run: `36866387094` / job `110382804693` / SUCCESS.
- Artifact: `11163447680` / `7404683 bytes`.
- Digest: `sha256:79c150bc3caf4648b4935a411585d155228fea4b0c2e85959c83a51c4d7a69e1`.
- Independent ZIP digest: MATCH.
- Four canonical input PNGs: 4/4 EXACT MATCH.
- Bundle-level `GENERATION_ALLOWED=TRUE`.
- Human-only Candidate 01: NOT AUTHORIZED.
- N21 Candidate 08 / N22: NOT STARTED.


## 2026-10-01｜N21 Crowd Body/Wardrobe Reference V001 Candidate 01 Work Authorization

Status: `PRODUCT OWNER AUTHORIZED / ONE PNG ONLY / WAITING WORK OUTPUT`

- Target: `N21_CROWD_BODY_WARDROBE_REFERENCE_V001 Candidate 01`.
- Formal Artifact: `11163447680`.
- Pre-generation exact verification: `4/4 required`.
- Output limit: exactly `1 PNG`.
- No environment image.
- No Candidate 02.
- No N21 Candidate 08.
- No N22.
- No publication / controlled-reference closeout yet.


## 2026-10-01｜N21 Crowd Body/Wardrobe Reference V001 Candidate 03 Approval

Status: `PRODUCT OWNER APPROVED / EXACT BINARY INTAKE PENDING`

- approved candidate: `Candidate 03`
- source binary: `1536×1024 RGBA PNG`
- byte size: `1418940`
- SHA-256: `73bb645e5a22cccb53faf8eb2d4b8fc0b876980e7520a2bc54daab1207439dc6`
- staging intake prepared.
- no re-encode / resize / export allowed.
- N21 Candidate 08 / N22 not started.


## 2026-10-01｜N21 Crowd Body/Wardrobe Reference V001 Closeout

Status: `PRODUCT OWNER APPROVED / CANONICAL / EXACT VERIFIED / MANIFESTED / CLOSED`

- approved candidate: `Candidate 03`.
- canonical: `production/human_references/n21_crowd_body_wardrobe/N21_CROWD_BODY_WARDROBE_REFERENCE_V001.png`.
- exact identity: `1536×1024 RGBA / 1418940 bytes / SHA-256 73bb645e5a22cccb53faf8eb2d4b8fc0b876980e7520a2bc54daab1207439dc6 / blob 2b86ab207ee60ba0cd2de277bb55900b8854099c`.
- intake exact verification: run `36873981603` / job `110408581874` / PASS.
- canonical publication: exact Git blob reuse at `e1d3a82da4b96eb0f20f2a629ef1140d4668b650`.
- canonical verification: run `36874219371` / job `110409384685` / PASS.
- manifest finalized.
- staging and one-time verifier workflows removed.
- next design target: `N21_REFERENCE_DELIVERY_BUNDLE_V006` using Environment Reference + Crowd Body/Wardrobe Reference only, pending Product Owner approval.

## 2026-10-01｜N21 Candidate 08 Review + EOD Hold

Status: `NOT APPROVED / REVIEW CLOSED / HUMAN BODY-WARDROBE-DIRECTION IMPROVED / BLOCKING + ENVIRONMENT COMPOSITION FAIL / EOD HOLD`

- V006 Design V0.2 approved / locked.
- Validation-only run: `36878776156` / job `110424919156` / 2 of 2 exact / no Artifact.
- Formal V006 build: run `36879153275` / job `110426184563` / SUCCESS.
- Artifact: `11171365040` / `4813649 bytes` / `sha256:e9e718893de20d86e90352ba7bf2ece0c7fa4f242a3b22f436bf727e9760a0c0`.
- Independent Artifact ZIP + both PNG exact identities: PASS.
- Candidate 08 authorized for exactly one Clean Regeneration.
- Observed output: `941×1672 RGBA PNG`.
- Positive evidence: natural adult proportions improved; ordinary contemporary wardrobe; no obvious prohibited bags/luggage; movement direction correctly reads threshold → deeper castle interior; no obvious forced four-person cast; no hero-pair staging.
- Failure evidence: crowd still too organized / central-axis; environment drifts to monumental symmetrical Gothic portal / architectural showcase; route ahead is too legible; unknown / threat / partial-concealment read remains insufficient.
- Candidate 08: `NOT APPROVED`.
- RISK-003 remains ACTIVE / hard creative blocker, but body/wardrobe/direction are now partially mitigated in real candidate evidence.
- Candidate 09: `NOT AUTHORIZED`.
- N22: `NOT STARTED`.
- Resume point: narrow Candidate 09 strategy review only; preserve C08 gains and target blocking + environment composition.


## 2026-10-02｜N21 Hold / Downstream S02-B Resume

- Product Owner directive: pause N21 and complete downstream Story Shot production before revisiting N21.
- N21 Candidate 08: NOT APPROVED / retained as evidence only.
- N21 Candidate 09: NOT AUTHORIZED.
- RISK-003: ACTIVE but N21-scoped / deferred / NON-BLOCKING for N22–N27.
- Downstream authoritative sequence preserved: N22 → N23 → N24 → A06 → N25 → N26 → N27.
- Current active task: N22 Node-Level Director Shot Design.
- Project State target: R184; Dashboard target: V119.


## 2026-10-02｜N22 Director Shot Design V0.1 Approval

Status: `PRODUCT OWNER APPROVED / LOCKED`

- Shot: `N22｜People in the Flow — Ning Observational POV`.
- Function: `POV + INFORMATION UPGRADE + NAMED CHARACTER SEEDING`.
- Tier 1 seeds: Su Xiaoxiao + Liao Jian.
- Tier 2 seeds: Wen Qingya + Guang Yong.
- N22 does not prove all sixteen bodies or exact 8-men / 8-women arithmetic.
- Blocking locked to asynchronous / non-lineup / non-queue behavior.
- Architecture subordinate / off-axis; no monumental symmetric Gothic portal.
- Look continuity: N20 dim warm low-key entrance-to-interior world.
- Neil emphasis excluded; N23 retains direction-change ownership.
- Critical assumption remains unverified; first later generation proof is exactly one candidate.
- If four named seeds destabilize identity/composition, reduce complexity rather than blind regenerate.
- Next authorized step: N22 Scene Reference Design only.
- Project State target: R185; Dashboard target: V120.


## 2026-10-02｜N22 Scene Reference Design V0.1 Approval

Status: `PRODUCT OWNER APPROVED / LOCKED`

- Initial reference count: 5.
- Tier 1: AST_IMG_000061 Su Xiaoxiao + AST_IMG_000058 Liao Jian.
- Tier 2: AST_IMG_000062 Wen Qingya + AST_IMG_000056 Guang Yong.
- Scene: AST_IMG_000052 SCENE_CASTLE_ENTRANCE / DAY_DOOR_OPEN.
- N20: Director-level look / continuity authority only; excluded from initial generation input.
- Excluded initially: CHARACTER_VISUAL_STYLE_REFERENCE_V001, N21 environment reference, N21 crowd body/wardrobe reference, Ning, Jun, Neil.
- Design principle: minimum authority / avoid reference-content leakage / avoid cast-lineup pressure.
- Critical assumption remains unverified until one-candidate proof.
- Next authorized step: N22 Reference Delivery Bundle Design V0.1 only.
- Project State target: R186; Dashboard target: V121.


## 2026-10-02｜N22 Reference Delivery Bundle Design V0.1 Approval

Status: `PRODUCT OWNER APPROVED / LOCKED`

- Bundle: `N22_REFERENCE_DELIVERY_BUNDLE_V001`.
- Reference count: 5.
- Inputs: AST_IMG_000061 / AST_IMG_000058 / AST_IMG_000062 / AST_IMG_000056 / AST_IMG_000052.
- Exact canonical path / SHA-256 / byte size / Git blob locked in the design.
- Reference order is not screen position, left-right order, blocking order or prominence.
- N20 remains written look/continuity authority only; not a Bundle image input.
- Builder: existing `.github/workflows/story-shot-reference-bundle-builder.yml` only.
- No N22-specific workflow.
- Next authorized step: create Bundle Spec with `build_authorized=false` and prepare validation-only execution.
- Formal Artifact build: NOT AUTHORIZED.
- Candidate 01: NOT AUTHORIZED.
- Project State target: R187; Dashboard target: V122.


## 2026-10-02｜N22 Bundle V001 Validation-Only Pass

Status: `PASS / 5 OF 5 EXACT / NO ARTIFACT / GENERATION_ALLOWED=FALSE`

- Spec: `production/bundle_specs/N22_REFERENCE_DELIVERY_BUNDLE_V001.json`.
- Spec commit: `a3975de9e8e781b103936654676647d8db588a44`.
- `build_authorized=false`.
- Workflow run: `36962064841`.
- Job: `110697691495`.
- Builder output: `VALIDATION_PASS: 5/5 exact canonical references verified`.
- `BUILD_AUTHORIZED=FALSE`.
- `GENERATION_ALLOWED=FALSE`.
- Formal bundle build: SKIPPED.
- Bundle ID read: SKIPPED.
- Artifact upload: SKIPPED.
- Run artifacts: NONE.
- Next authority required: Product Owner formal Bundle build authorization.
- Candidate 01 remains NOT AUTHORIZED.


## 2026-10-02｜N22 Bundle V001 Formal Build + Independent Verification

Status: `FORMAL BUILD PASS / 5 OF 5 EXACT / INDEPENDENT ARTIFACT VERIFIED / GENERATION_ALLOWED=TRUE / CANDIDATE 01 NOT AUTHORIZED`

- PO formal-build authorization received.
- Spec authorization commit: `8cc4a9dbc959c8fa9f49d5e6a2b36649a53d58d3`.
- Spec revision: `V001-R2`; `build_authorized=true`.
- Run: `36962281468` / job `110698343917` / SUCCESS.
- Builder: `PASS: 5/5 exact canonical reference binaries verified`.
- `GENERATION_ALLOWED=TRUE`.
- Artifact: `11208576712` / `4752815 bytes`.
- Artifact digest: `sha256:301a127df57e197580c0b87aa0beb7d59c2687d3edd16686c10caa8f841f5c58`.
- Artifact expiry: `2026-10-09T03:55:37Z`.
- Independent downloaded ZIP SHA-256: MATCH.
- Independent 5-reference size / SHA-256 / Git blob / PNG signature verification: `5/5 PASS`.
- Product Owner manual reference upload: `0`.
- Candidate 01 generation: `NOT AUTHORIZED`.
- Next: Product Owner authorization for N22 Candidate 01 Work generation.


## 2026-10-02｜N22 Candidate 01 Work Generation Authorization

Status: `PRODUCT OWNER AUTHORIZED / EXACTLY ONE PNG`

- Target: `N22 Candidate 01｜Clean Regeneration`.
- Bundle: `N22_REFERENCE_DELIVERY_BUNDLE_V001`.
- Artifact: `11208576712`.
- Artifact digest: `sha256:301a127df57e197580c0b87aa0beb7d59c2687d3edd16686c10caa8f841f5c58`.
- Work automatic acquisition: REQUIRED.
- Pre-generation exact verification: REQUIRED 5/5.
- Generation count: exactly 1 PNG.
- After generation: STOP for Product Owner review.
- Candidate 02 / N23 / publication / registration / closeout: NOT AUTHORIZED.


## 2026-10-02｜N22 Candidate 01 Review Close + Bundle V002 Design

- Candidate 01: `NOT APPROVED / REVIEW CLOSED / VALID DIAGNOSTIC EVIDENCE`.
- Review PNG identity: `941×1672 / RGB / 1,968,418 bytes / SHA-256 3c8f81341967dce94e6fb5286cd38a3c53d8507371de9d81f1d6acb281336400`.
- Preserve: Su/Liao/Wen/Guang identity stability, body/wardrobe stability, Castle Entrance scene identity.
- Correct: four-character ensemble overexposure, Su-Liao hero-pair pressure, doorway brightness, floor daylight reflection.
- Candidate 02 Correction Strategy V0.1: `PRODUCT OWNER APPROVED / LOCKED`.
- Bundle V002 Design draft: 4 refs = AST_IMG_000061 / AST_IMG_000058 / AST_IMG_000056 / AST_IMG_000052.
- AST_IMG_000062 Wen Qingya: deferred from Candidate 02 generation reference set.
- Bundle V002 spec / validation / formal build / Candidate 02: NOT AUTHORIZED.
- Project State target: R191 / Dashboard V126.


## 2026-10-02｜N22 Bundle V002 Design Approval

Status: `PRODUCT OWNER APPROVED / LOCKED`

- Target Bundle: `N22_REFERENCE_DELIVERY_BUNDLE_V002`.
- Reference count: 4.
- Inputs: AST_IMG_000061 / AST_IMG_000058 / AST_IMG_000056 / AST_IMG_000052.
- Wen Qingya AST_IMG_000062: intentionally deferred.
- Candidate 01 pixels: excluded / diagnostic evidence only.
- Builder: existing Generic Story Shot Reference Bundle Builder V1.
- Next authorized step: Bundle V002 Spec + validation-only preparation with `build_authorized=false`.
- Formal Bundle V002 build: NOT AUTHORIZED.
- Candidate 02 generation: NOT AUTHORIZED.
- Project State target: R192 / Dashboard V127.


## 2026-10-02｜N22 Bundle V002 Validation-Only Pass

Status: `PASS / 4 OF 4 EXACT / NO ARTIFACT / GENERATION_ALLOWED=FALSE`

- Spec: `production/bundle_specs/N22_REFERENCE_DELIVERY_BUNDLE_V002.json`.
- Spec commit: `3f7d6c573807f139a646c46e7f0eab1a444cd123`.
- `build_authorized=false`.
- Workflow run: `36965661777`.
- Job: `110708748486`.
- Result: `VALIDATION_PASS: 4/4 exact canonical references verified`.
- `BUILD_AUTHORIZED=FALSE`.
- `GENERATION_ALLOWED=FALSE`.
- Artifacts: NONE.
- Next: Product Owner formal Bundle V002 build authorization.
- Candidate 02 remains NOT AUTHORIZED.


## 2026-10-02｜N22 Bundle V002 Formal Build + Independent Verification

Status: `FORMAL BUILD PASS / 4 OF 4 EXACT / INDEPENDENT ARTIFACT VERIFIED / GENERATION_ALLOWED=TRUE / CANDIDATE 02 NOT AUTHORIZED`

- PO formal-build authorization received.
- Spec authorization commit: `42d48adf8841d19da51a64dadcb2e2b6e85dee7f`.
- Spec revision: `V002-R2`; `build_authorized=true`.
- Run: `36982776916` / job `110760847742` / SUCCESS.
- Builder: `PASS: 4/4 exact canonical reference binaries verified`.
- `GENERATION_ALLOWED=TRUE`.
- Artifact: `11216560996` / `4,115,447 bytes`.
- Artifact digest: `sha256:28190d5b103b8c39409630d244aeb767d1c87930b31d24046325bd0b985e33c2`.
- Artifact expiry: `2026-10-09T08:13:08Z`.
- Independent downloaded ZIP SHA-256: MATCH.
- Independent 4-reference size / SHA-256 / Git blob / PNG signature verification: `4/4 PASS`.
- Product Owner manual reference upload: `0`.
- Candidate 02 generation: `NOT AUTHORIZED`.
- Next: Product Owner authorization for N22 Candidate 02 Work generation.


## 2026-10-02｜N22 Candidate 02 Work Generation Authorization

Status: `PRODUCT OWNER AUTHORIZED / EXACTLY ONE PNG`

- Target: `N22 Candidate 02｜Clean Regeneration`.
- Bundle: `N22_REFERENCE_DELIVERY_BUNDLE_V002`.
- Artifact: `11216560996`.
- Artifact digest: `sha256:28190d5b103b8c39409630d244aeb767d1c87930b31d24046325bd0b985e33c2`.
- Work automatic acquisition: REQUIRED.
- Pre-generation exact verification: REQUIRED 4/4.
- Wen Qingya: intentionally deferred from Candidate 02 input.
- Generation count: exactly 1 PNG.
- After generation: STOP for Product Owner review.
- Candidate 03 / N23 / publication / registration / closeout: NOT AUTHORIZED.


## 2026-10-02｜N22 Candidate 02 Review Close + Candidate 03 Strategy

- Candidate 02: `NOT APPROVED / REVIEW CLOSED`.
- Review PNG identity: `941×1672 / RGB / 1,782,593 bytes / SHA-256 56768b17ea6e9f1b818109c646662bbdc54403c5a16f340d4738ec1249cf0246`.
- Lighting correction: PASS / preserve.
- Larger-group foreground obstruction: improved / preserve.
- Remaining failure: Su + Liao dual-subject staging, Guang too readable, near-synchronized named-character gaze.
- Candidate 03 strategy draft: references proposed = AST_IMG_000061 / AST_IMG_000058 / AST_IMG_000052.
- AST_IMG_000056 Guang Yong: proposed removal from Candidate 03 formal generation reference set.
- New hard rule: Su/Liao must not share gaze direction; Su first-glance, Liao second-glance/partial.
- Bundle V003 / validation / formal build / Candidate 03: NOT AUTHORIZED.
- Project State target: R196 / Dashboard V131.


## 2026-10-02｜N22 Candidate 03 Correction Strategy Approval

Status: `PRODUCT OWNER APPROVED / LOCKED`

- Candidate 03 route: Su Xiaoxiao + Liao Jian + Castle Entrance only.
- Remove Guang Yong from Candidate 03 proposed generation reference set.
- Preserve Candidate 02 lighting gains; no new look reference by default.
- Su Xiaoxiao: only first-glance readable named face.
- Liao Jian: second-glance / partial identity.
- Hard rule: Su and Liao must not share gaze direction.
- Next authorized step: N22 Reference Delivery Bundle V003 Design only.
- Bundle V003 Spec / validation / formal build / Candidate 03: NOT AUTHORIZED.
- Project State target: R197 / Dashboard V132.


## 2026-10-02｜N22 Bundle V003 Design Draft

Status: `DRAFT / WAITING PRODUCT OWNER APPROVAL`

- Proposed Bundle: `N22_REFERENCE_DELIVERY_BUNDLE_V003`.
- Reference count: 3.
- Inputs: AST_IMG_000061 Su Xiaoxiao / AST_IMG_000058 Liao Jian / AST_IMG_000052 Castle Entrance.
- Guang Yong: removed from V003.
- Wen Qingya: remains deferred.
- Candidate 02 lighting gains: preserved unchanged.
- Su Xiaoxiao: only first-glance named face.
- Liao Jian: second-glance / partial identity.
- Hard rule: no shared Su/Liao gaze and no duo composition.
- Bundle V003 Spec / validation / formal build / Candidate 03: NOT AUTHORIZED.
- Project State target: R198 / Dashboard V133.


## 2026-10-02｜N22 Bundle V003 Design Approval

Status: `PRODUCT OWNER APPROVED / LOCKED`

- Target Bundle: `N22_REFERENCE_DELIVERY_BUNDLE_V003`.
- Reference count: 3.
- Inputs: AST_IMG_000061 / AST_IMG_000058 / AST_IMG_000052.
- Guang Yong AST_IMG_000056: removed from Candidate 03 input.
- Candidate 02 lighting gains: preserved unchanged.
- Su Xiaoxiao: only first-glance named face.
- Liao Jian: second-glance / partial identity.
- Hard rules: no shared Su/Liao gaze; no duo composition.
- Next authorized step: Bundle V003 Spec + validation-only preparation with `build_authorized=false`.
- Formal Bundle V003 build: NOT AUTHORIZED.
- Candidate 03 generation: NOT AUTHORIZED.
- Project State target: R199 / Dashboard V134.


## 2026-10-02｜N22 Bundle V003 Validation-Only Pass

- Spec: `production/bundle_specs/N22_REFERENCE_DELIVERY_BUNDLE_V003.json`
- Spec commit: `edb596f588d4a12f4b83186fc8e156844ffa3ac6`
- Run: `36985475173` / Job: `110769400351`
- Result: `VALIDATION_PASS: 3/3 exact canonical references verified`
- `BUILD_AUTHORIZED=FALSE` / `GENERATION_ALLOWED=FALSE`
- Artifacts: NONE
- Candidate 03: NOT AUTHORIZED


## 2026-10-02｜N22 Bundle V003 Formal Build + Independent Verification

Status: `FORMAL BUILD PASS / 3 OF 3 EXACT / INDEPENDENT ARTIFACT VERIFIED / GENERATION_ALLOWED=TRUE / CANDIDATE 03 NOT AUTHORIZED`

- Spec authorization commit: `42a52a515373954d8d0794bff29de236fe0eed78`.
- Spec revision: `V003-R2`; `build_authorized=true`.
- Run: `36985709195` / job `110770136859` / SUCCESS.
- Builder: `PASS: 3/3 exact canonical reference binaries verified`.
- `GENERATION_ALLOWED=TRUE`.
- Artifact: `11217127728` / `3,640,093 bytes`.
- Artifact digest: `sha256:e1171f901c167bd628934558ac02bb16091400a13a550c77e8aa96737c7852f2`.
- Artifact expiry: `2026-10-09T08:44:07Z`.
- Independent ZIP SHA-256: MATCH.
- Independent 3-reference size / SHA-256 / Git blob / PNG signature verification: `3/3 PASS`.
- Candidate 03 generation: `NOT AUTHORIZED`.
- Next: Product Owner authorization for N22 Candidate 03 Work generation.


## 2026-10-02｜N22 Candidate 03 Work Generation Authorization

Status: `PRODUCT OWNER AUTHORIZED / EXACTLY ONE PNG`

- Target: `N22 Candidate 03｜Clean Regeneration`.
- Bundle: `N22_REFERENCE_DELIVERY_BUNDLE_V003`.
- Artifact: `11217127728`.
- Artifact digest: `sha256:e1171f901c167bd628934558ac02bb16091400a13a550c77e8aa96737c7852f2`.
- Work automatic acquisition: REQUIRED.
- Pre-generation exact verification: REQUIRED 3/3.
- Su = only first-glance named face.
- Liao = second-glance / partial identity.
- No shared Su/Liao gaze; no duo composition.
- Candidate 02 lighting gains remain binding.
- Generation count: exactly 1 PNG.
- After generation: STOP for Product Owner review.
- Candidate 04 / N23 / publication / registration / closeout: NOT AUTHORIZED.


## 2026-10-02｜N22 Final Approval + Archival Preparation

Status: `PRODUCT OWNER APPROVED / FINAL BINARY LOCKED / WAITING ORIGINAL PNG GITHUB PUBLICATION`

- Shot: `N22｜People in the Flow — Ning Observational POV`.
- Selected result: `N22 Candidate 04｜Clarity-Clean Final Binary`.
- Exact approved binary: `941×1672 / RGB PNG / 1,834,637 bytes`.
- SHA-256: `6d1ed04106bb35943d752113e17d5f36fd2d55b29f4234e13177c7f8b6496f3a`.
- Git blob: `a0f38041c10e4eb13a5a915a5d2f7bf22f85a2cf`.
- Temporary approved-source path: `production/image_library/approved/story_shots/N22_Candidate_04_APPROVED_SOURCE.png`.
- Planned canonical path: `production/image_library/approved/story_shots/N22_PEOPLE_IN_THE_FLOW_APPROVED_V001.png`.
- Exact-binary verification workflow prepared: `.github/workflows/p03-n22-approved-upload-verification-v001.yml`.
- Canonical Publication / Story Shot Registration / Registration Verification: WAITING ON GITHUB SOURCE BINARY.
- Project State target: R203 / Dashboard V138.


## 2026-10-02｜N22 Story Shot Formal Closeout

Status: `COMPLETE / PRODUCT OWNER APPROVED / CANONICAL / REGISTERED / VERIFIED / CLOSED`

- Exact approved binary: `941×1672 RGB PNG / 1,834,637 bytes`.
- SHA-256: `6d1ed04106bb35943d752113e17d5f36fd2d55b29f4234e13177c7f8b6496f3a`.
- Git blob: `a0f38041c10e4eb13a5a915a5d2f7bf22f85a2cf`.
- Exact verification: run `36998121036` / job `110809408442` / PASS.
- Canonical publication: run `36998203149` / job `110809649430` / commit `984b708ff69104adc172f330c8a27791656749f0` / exact blob preserved.
- Canonical path: `production/image_library/approved/story_shots/N22_PEOPLE_IN_THE_FLOW_APPROVED_V001.png`.
- Story Shot registration commit: `474fe2cb478c2d9a4ce2be7a77838890fb1c38ad`.
- Registration verification: run `36998327975` / job `110810040324` / OVERALL_RESULT=PASS.
- N22 formal closeout record: `docs/project_control/gates/P0_3_video_pipeline/s02_b_n22_story_shot_registration_closeout_2026-10-02.md`.
- N21 remains HOLD.
- N23 remains NOT STARTED.
- Project State target: R204 / Dashboard V139.


## 2026-10-02｜N23 Node-Level Director Shot Design Draft

Status: `DRAFT / WAITING PRODUCT OWNER APPROVAL`

- Shot: `N23｜Neil Turns — Group Direction Changes`.
- Parent scope: `02:04.300 → 02:11.640`.
- Function: `PRIMARY ACTION + SPATIAL TRANSITION`.
- Core proof: Neil initiates a readable group direction change.
- Camera: medium-wide rear / rear-3Q, laterally offset.
- Group movement: asynchronous propagation; no synchronized turn / queue / procession.
- Neil: action anchor, not hero portrait.
- N24 boundary: do not consume Ning spatial POV or full destination reveal.
- Scene Reference / Bundle / Candidate 01: NOT AUTHORIZED.
- Project State target: R205 / Dashboard V140.


## 2026-10-02｜N23 Director Shot Design V0.2 Approval

Status: `PRODUCT OWNER APPROVED / LOCKED`

- V0.1 superseded after continuity review against A06.
- N23 primary frame: Neil stands beside the open castle door and side-glances at the cohort finishing entry.
- Neil does not close/touch the door and does not walk away yet.
- Crowd continuity: reuse the same N22 cohort from another real camera angle; do not mirror or literally duplicate N22.
- Guang Yong may retain low-weight backward attention as a visual bridge into his later A06 open-door question.
- Hierarchy: Neil + open door primary; group entry secondary; Guang Yong cue tertiary.
- A06 retains Neil leaving the open door behind / explicit question payoff.
- Next authorized step: N23 Scene Reference Design only.
- Bundle / Work / Candidate 01: NOT AUTHORIZED.
- Project State target: R206 / Dashboard V141.


## 2026-10-02｜N23 Scene Reference Design V0.1 Approval

Status: `PRODUCT OWNER APPROVED / LOCKED`

- Format: 9:16 vertical / target 941×1672.
- Camera: inside castle, deeper than threshold, side-offset, diagonally looking back toward open entrance.
- Group direction: doorway → castle interior. Any outward-exit read = automatic FAIL.
- Neil: beside open door / side glance / no door contact / not yet walking away.
- N22 canonical Story Shot: crowd-continuity authority only; not composition template.
- Guang Yong: optional low-weight backward-attention continuity cue for A06.
- Previous horizontal N23 explanatory diagram: INVALID FOR FORMAL EXECUTION / EXCLUDED FROM BUNDLE.
- Next authorized step: N23 Reference Delivery Bundle Design V0.1 only.
- Bundle Spec / build / Work / Candidate 01: NOT AUTHORIZED.
- Project State target: R207 / Dashboard V142.


## 2026-10-02｜N23 Reference Delivery Bundle Design V0.1 Draft

Status: `DRAFT / WAITING PRODUCT OWNER APPROVAL`

- Proposed Bundle: `N23_REFERENCE_DELIVERY_BUNDLE_V001`.
- Reference count: 4.
- N22 canonical Story Shot → crowd continuity only; not composition authority.
- AST_IMG_000052 → Castle Entrance / DAY_DOOR_OPEN scene authority.
- AST_IMG_000059 → Neil primary identity authority.
- AST_IMG_000056 → Guang Yong tertiary continuity identity authority.
- Camera / movement direction remains controlled by N23 Scene Reference Design V0.1 text authority.
- Hard fail: frame reads as people leaving the castle.
- Horizontal explanatory diagram and all generated camera sketches excluded.
- Bundle Spec / validation / formal build / Work / Candidate 01: NOT AUTHORIZED.
- Project State target: R208 / Dashboard V143.


## 2026-10-02｜N23 Bundle V001 Validation-Only Pass

Status: `4/4 EXACT / NO ARTIFACT / GENERATION NOT ALLOWED`

- Bundle Spec: `production/bundle_specs/N23_REFERENCE_DELIVERY_BUNDLE_V001.json`.
- Spec commit: `cc23ec059204e8cdcd361df90b9df47fcb277c0d`.
- Spec revision: `V001-R1` / `build_authorized=false`.
- Run: `37005584714` / Job: `110832961471`.
- Result: `VALIDATION_PASS: 4/4 exact canonical references verified`.
- `BUILD_AUTHORIZED=FALSE` / `GENERATION_ALLOWED=FALSE`.
- Artifacts: NONE.
- Candidate 01: NOT AUTHORIZED.
- Next: Product Owner formal Bundle V001 build authorization.
- Project State target: R209 / Dashboard V144.


## 2026-10-02｜N23 Bundle V001 Formal Build

Status: `FORMAL BUILD PASS / 4 OF 4 EXACT / ARTIFACT VERIFIED`

- Authorized Spec commit: `d88a9b882ebc1ddf78ed3701754ccb0e6791ebe2`.
- Spec: `V001-R2 / build_authorized=true`.
- Run: `37006373075` / Job: `110835506338`.
- Builder: `PASS: 4/4 exact canonical reference binaries verified`.
- Bundle-level: `GENERATION_ALLOWED=TRUE`.
- Artifact: `11225912126` / 5,426,263 bytes.
- Digest: `sha256:ffb6ceb327fc405fb000639921188a4ec333d8082d4ec526dc1ecd1e5533b88d`.
- Independent ZIP digest: MATCH.
- Independent delivered PNG bytes / SHA-256 / Git blob / dimensions: `4/4 MATCH`.
- Candidate 01 Work generation: NOT AUTHORIZED.
- Next: Product Owner Candidate 01 authorization.
- Project State target: R210 / Dashboard V145.


## 2026-10-02｜N23 Candidate 01 Work Generation Authorization

Status: `PRODUCT OWNER AUTHORIZED / EXACTLY ONE PNG / WAITING WORK OUTPUT`

- Mode: Clean Regeneration.
- Bundle: `N23_REFERENCE_DELIVERY_BUNDLE_V001`.
- Run: `37006373075`; Artifact: `11225912126`.
- Pre-generation verification: `4/4 exact required`.
- Camera: inside castle / deeper than threshold / side-offset / diagonally looking back to open entrance.
- Group motion: doorway → castle interior; outward-exit read = automatic FAIL.
- Neil: beside open door / side glance / no door contact / not walking away yet.
- N22: same-cohort continuity only; no mirror/copy.
- Guang Yong: tertiary backward-attention continuity cue only.
- Output: exactly one 941×1672 PNG, then stop for Product Owner review.
- Candidate 02 / N24 / publication / registration: NOT AUTHORIZED.
- Project State target: R211 / Dashboard V146.


## 2026-10-02｜N23 Candidate 01 Review + Scene Reference V0.2

Status: `C01 NOT APPROVED / DIAGNOSTIC ONLY / V0.2 CAMERA APPROVED`

- Candidate 01 preserved valid facts: inward movement and Neil beside open door.
- Failures: N22-like camera family, named-character ensemble over-read, Guang Yong over-weight, excessive exterior/floor light, ambiguous bag-like foreground element.
- V0.1 camera family is superseded.
- V0.2: door + controlled exterior light on LEFT; crowd travels LEFT → RIGHT into castle.
- Camera: side / broadside threshold view, mildly elevated.
- Neil: beside open door, near-frontal to camera, head/eyes slightly LEFT toward entering guests.
- Structural difference from N22 is mandatory.
- Candidate 02 / Bundle V002: NOT AUTHORIZED pending correction strategy / reference-architecture review.
- Project State target: R212 / Dashboard V147.


## 2026-10-02｜N23 Scene Reference V0.2.1 Gaze Correction

Status: `PRODUCT OWNER APPROVED / LOCKED`

- V0.2 camera geometry retained: door/light LEFT; crowd LEFT → RIGHT; side/broadside threshold view.
- Story moment clarified: the group is at the tail end of entry and almost fully inside.
- Most visible crowd mass should sit middle-right / right of Neil.
- Neil remains beside the open door and near-frontal to camera.
- Neil head / eyes corrected from LEFT to slight RIGHT, watching the group tail already inside.
- Neil must not primarily look toward the doorway / exterior.
- Candidate 02 remains NOT AUTHORIZED pending correction strategy / reference architecture review.
- Project State target: R213 / Dashboard V148.


## 2026-10-02｜N23 Candidate 02 Correction Strategy V0.1 Draft

Status: `DRAFT / WAITING PRODUCT OWNER APPROVAL`

- Scene Reference V0.2.1 remains unchanged.
- Proposed V002 direct inputs: AST_IMG_000052 + AST_IMG_000059 + AST_IMG_000013.
- N22 Story Shot direct pixels removed; N22 becomes Director-level continuity check only.
- Guang Yong Character Sheet AST_IMG_000056 removed; replace with single REAR_3Q_RIGHT atomic reference AST_IMG_000013.
- Other crowd members intentionally unseeded / anonymous.
- N21_CROWD_BODY_WARDROBE_REFERENCE_V001 not reused because canonical authority scope is N21-only.
- Candidate 02 remains NOT AUTHORIZED.
- Project State target: R214 / Dashboard V149.


## 2026-10-02｜Generic Guest Crowd Core Set V001 Asset Design Approval

Status: `PRODUCT OWNER APPROVED / LOCKED`

- New project-level reusable asset track: BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001.
- 10 fixed anonymous Guests A–J.
- Four full-body orientation boards: FRONT / LEFT PROFILE / RIGHT PROFILE / BACK.
- 40 controlled views total.
- Main-character visual language may be used as style source, but named-character identity / complete outfit copying is prohibited.
- Bags / shoulder bags / crossbody bags / luggage permanently prohibited.
- Authority scope is project-wide crowd identity/body/wardrobe continuity; not N21-only / N23-only.
- N23 Candidate 02 paused; N21 may be retested only after asset completion and remains HOLD.
- No generation or Bundle work authorized yet.
- Next: Style / Identity Reference Design V0.1.
- Project State target: R215 / Dashboard V150.


## 2026-10-02｜Generic Guest Crowd Gender Distribution Lock

Status: `PRODUCT OWNER APPROVED / LOCKED`

- BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001 remains 10 fixed anonymous Guests A–J.
- Gender distribution hard-locked: 6 female + 4 male.
- Four-board / 40-view structure unchanged.
- No Bundle or Work generation authorized.
- Next remains Style / Identity Reference Design V0.1.
- Project State target: R216 / Dashboard V151.


## 2026-10-02｜Generic Guest Crowd Style / Identity Design V0.1 Draft

Status: `DRAFT / WAITING PRODUCT OWNER APPROVAL`

- Guest A–F = female; Guest G–J = male.
- Ten low-detail anonymous identity archetypes drafted.
- Proposed style parents: AST_IMG_000042 / 000046 / 000022 / 000009.
- Production strategy: FRONT master first, then LEFT / RIGHT / BACK derived as same identities.
- Proposed board layout: 1536×1024, 2×5 fixed slots.
- Named-character identity / outfit copying prohibited.
- No bags / luggage across any view.
- No Bundle or Work generation authorized yet.
- Project State target: R217 / Dashboard V152.


## 2026-10-02｜Generic Guest Crowd Style / Identity Design V0.1 Approval

Status: `PRODUCT OWNER APPROVED / LOCKED`

- Guest A–F female / G–J male locked.
- Ten anonymous identity archetypes approved.
- FRONT Board locked as identity master before LEFT / RIGHT / BACK expansion.
- Style-parent assets locked: AST_IMG_000042 / 000046 / 000022 / 000009.
- Board target locked: 1536×1024 landscape / 2×5 fixed slots.
- Named-character identity / complete outfit copying prohibited.
- No Bundle Spec/build or Work generation authorized.
- Next: FRONT Board Reference Delivery Bundle Design V0.1.
- Project State target: R218 / Dashboard V153.

## 2026-10-02｜Generic Guest Crowd FRONT Board Bundle Design V0.1 Approval

Status: `PRODUCT OWNER APPROVED / LOCKED`

- Bundle Design locked for `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_FRONT_BOARD_REFERENCE_DELIVERY_BUNDLE_V001`.
- Reference count locked: 4.
- Style parents: AST_IMG_000042 / AST_IMG_000046 / AST_IMG_000022 / AST_IMG_000009.
- Initial test excludes Character Reference Sheets, Story Shots, Scene Masters and external images.
- Board contract retained: 1536×1024 landscape / 2×5 / Guest A–J fixed slots / 6F4M.
- Minimum proof: exactly one FRONT Board candidate after later gates.
- build_authorized remains false; formal Artifact build and Work generation are NOT authorized.
- Next: create Bundle Spec V001 + validation-only execution.
- Project State target: R219 / Dashboard V154.

## 2026-10-02｜Generic Guest Crowd FRONT Board Bundle V001 Validation-Only

Status: `PASS / 4 OF 4 EXACT / NO ARTIFACT`

- Spec commit: `00678ec24380eb8fad9dd7f8c350a93eb4080e8a`.
- Spec revision: `V001-R1` / `build_authorized=false`.
- Workflow run: `37019842679`.
- Job: `110879793932`.
- Validation step: SUCCESS.
- Four declared BODY_FRONT style-parent canonical references therefore all passed the fail-closed validation path.
- Formal build step: SKIPPED.
- Artifact upload step: SKIPPED.
- Artifact query: NONE.
- Work generation remains NOT AUTHORIZED.
- Next: Product Owner formal Bundle V001 build authorization.
- Project State target: R220 / Dashboard V155.

## 2026-10-02｜Generic Guest Crowd FRONT Board Bundle V001 Formal Build

Status: `FORMAL BUILD PASS / 4 OF 4 EXACT / INDEPENDENT ARTIFACT VERIFIED`

- Product Owner authorized formal Bundle build only.
- Authorization/spec commit: `8e5c51ac841992a319921ce2db959a9eae7d5fe3`.
- Spec revision: `V001-R2` / `build_authorized=true`.
- Workflow run: `37020135208`.
- Job: `110880801633`.
- Artifact ID: `11231259655`.
- Artifact size: `11,200,536 bytes`.
- GitHub Artifact digest: `sha256:336340a61feb7808006b4dd0c9d067a03c6ba8a4d3e4124ba08e039bc06efd07`.
- Independently downloaded ZIP SHA-256: exact MATCH.
- Manifest: `reference_count=4 / all_reference_checks_pass=true / overall_result=PASS`.
- Independent delivered PNG verification: `4/4 PASS` for byte size, SHA-256, dimensions and manifest identity.
- Bundle-level `generation_allowed=true` is technical readiness only; Work generation remains NOT AUTHORIZED.
- FRONT Candidate 01: NOT AUTHORIZED.
- Next: Product Owner FRONT Candidate 01 Work-generation authorization.
- Project State target: R221 / Dashboard V156.

## 2026-10-02｜Generic Guest Crowd FRONT Board Candidate 01 Work Authorization

Status: `PRODUCT OWNER AUTHORIZED / ONE PNG ONLY / WAITING WORK OUTPUT`

- Generation mode: Clean Regeneration.
- Verified Bundle: `BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_FRONT_BOARD_REFERENCE_DELIVERY_BUNDLE_V001`.
- Artifact: `11231259655`.
- Pre-generation exact verification: `4/4 required`.
- Output: exactly one `1536×1024` PNG.
- Fixed board: 2×5 / Guests A–J / A–F female / G–J male.
- Four delivered references are style parents only; named-character identity copying is prohibited.
- Candidate 02 / LEFT / RIGHT / BACK remain NOT AUTHORIZED.
- N21 remains HOLD; N23 Candidate 02 remains PAUSED.
- After generation: stop for Product Owner review.
- Project State target: R222 / Dashboard V157.

## 2026-10-02｜Generic Guest Crowd FRONT Board Candidate 02 Approval / Exact Intake Preparation

Status: `PRODUCT OWNER APPROVED / EXACT BINARY LOCKED / WAITING WORK BINARY DELIVERY`

- Candidate 01: NOT APPROVED / diagnostic only.
- Candidate 02: Product Owner APPROVED as formal FRONT identity authority for Guest A–J.
- Approved binary: 1536×1024 / RGBA / 8-bit PNG.
- Byte size: `2,335,288`.
- SHA-256: `ef6c1b65c8d2f41db70b77b8621ec5d9ade41ad43811d2ddda88a2c14c357a23`.
- Git blob: `d8ff2d789a352475daa945d22a0a65112c72a682`.
- Approved pixels supersede earlier text-only archetypes where they differ.
- Guest I muscular build / sleeveless black top / visible tattoos are identity-defining approved traits.
- Exact-intake staging target: `staging/generic_guest_crowd_core_set_v001_front_intake/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_FRONT_CANDIDATE_02_APPROVED.png`.
- Temporary intake verifier installed: `.github/workflows/black-lady-generic-guest-front-v001-intake-verify.yml`.
- Verifier now triggers only when the approved staging PNG is delivered.
- Bootstrap run `37026278280` failed before staging delivery because the first workflow-definition commit self-triggered; it is not an intake result and has no authority over the candidate. Trigger was immediately corrected in commit `dbabc7031cff62a23c4df1689ea2d80646e3fd68`.
- Canonical publication remains pending exact intake PASS.
- LEFT / RIGHT / BACK remain NOT AUTHORIZED.
- Project State target: R223 / Dashboard V158.

## 2026-10-02｜Generic Guest Crowd FRONT Authority Formal Closeout

Status: `PRODUCT OWNER APPROVED / CANONICAL / EXACT VERIFIED / MANIFESTED / CLOSED`

- Approved candidate: `FRONT BOARD Candidate 02`.
- Candidate 01: diagnostic only / not approved.
- Canonical PNG: `production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_FRONT.png`.
- Exact binary: 1536×1024 / RGBA / 8-bit / 2,335,288 bytes.
- SHA-256: `ef6c1b65c8d2f41db70b77b8621ec5d9ade41ad43811d2ddda88a2c14c357a23`.
- Git blob: `d8ff2d789a352475daa945d22a0a65112c72a682`.
- Intake verification: run `37027704229` / job `110906445923` / exact PASS.
- Canonical publication commit: `222a204000641edfa30ff42a7324ce52afc61e2c` / exact Git-blob reuse / no re-encode.
- Canonical verification: run `37027994620` / job `110907415764` / exact PASS.
- FRONT Authority manifest commit: `76a4eecd87161b2ad1f4c7995b45bd6b706c7db4`.
- Approved pixels supersede earlier text-only archetypes where different.
- Guest I muscular build / sleeveless black top / visible tattoos remain locked identity traits.
- Temporary staging and verifier files cleaned.
- LEFT / RIGHT / BACK generation remains NOT AUTHORIZED.
- Next: `LEFT PROFILE Design V0.1`.
- Project State target: R224 / Dashboard V159.

## 2026-10-02｜P0.3 End-of-Day Closeout

Status: `COMPLETE / PROJECT CONTROL SYNCHRONIZED / NO FURTHER GENERATION AUTHORIZED TONIGHT`

- N22 remains formally closed: Product Owner approved / canonical / registered / verified.
- N23 Candidate 01 remains not approved / diagnostic only.
- N23 Scene Reference V0.2.1 remains approved / locked.
- N23 Candidate 02 remains paused pending Generic Guest Crowd Core Set progress.
- N21 remains HOLD / unresolved.
- Generic Guest Crowd Core Set FRONT Authority is formally closed.
- FRONT canonical PNG: `production/human_references/generic_guest_crowd_core_set_v001/BLACK_LADY_GENERIC_GUEST_CROWD_CORE_SET_V001_FRONT.png`.
- FRONT exact identity: 1536×1024 / RGBA / 8-bit / 2,335,288 bytes.
- FRONT SHA-256: `ef6c1b65c8d2f41db70b77b8621ec5d9ade41ad43811d2ddda88a2c14c357a23`.
- FRONT Git blob: `d8ff2d789a352475daa945d22a0a65112c72a682`.
- FRONT intake verification: `37027704229 / 110906445923 / PASS`.
- FRONT canonical publication: `222a204000641edfa30ff42a7324ce52afc61e2c` / exact blob reuse / no re-encode.
- FRONT canonical verification: `37027994620 / 110907415764 / PASS`.
- FRONT manifest present and current.
- Temporary staging / verifier resources cleaned.
- Project State stale fields reconciled: Generic Guest Candidate 02 intake-pending state removed; FRONT Bundle next-step closed; stale N22 Candidate 03 active wording superseded by N22 final closure; active S02-B boundary updated.
- Project State advanced to `R225`.
- Dashboard target advanced to `V160`.
- Next session resume point: local main sync first → `LEFT PROFILE Design V0.1`.
- LEFT / RIGHT / BACK generation remains NOT AUTHORIZED.

## 2026-10-03｜Generic Guest Crowd LEFT PROFILE Authority Formal Closeout

Status: `PRODUCT OWNER APPROVED / CANONICAL / EXACT VERIFIED / MANIFESTED / CLOSED`

- Design V0.1: Product Owner approved / locked.
- Bundle Design V0.1.1: Product Owner approved / locked.
- Bundle validation-only: run `37085242066` / `1/1 exact PASS`.
- Formal Bundle Build: run `37085478707` / job `111094752923`.
- Artifact: `11260528188` / 2,338,717 bytes / digest `sha256:66f870b5e215b648909bcff7a9670f19631c8a386cec75e42c2417731cecafaa`.
- Candidate 01: only generated candidate / Product Owner approved as-is / no Candidate 02 required.
- Approved binary: 1536×1024 / RGB / 8-bit / 1,686,189 bytes.
- SHA-256: `15cc28a4cc54dd32ba9fdf7825be6a9402f22b1be19d59e74d1ad1656d238ba1`.
- Git blob: `67d07640938163d53af347c4cd4988c2554ffe91`.
- Guest I muscular-build reduction and tattoo-pattern variation are accepted as LEFT PROFILE tolerance only; FRONT remains primary global identity authority.
- User upload preserved exact approved blob even though initial filename remained `十人左侧全身参考板.png`; standardized staging filename was created by exact Git-blob reuse.
- Intake verification: run `37087159946` / job `111099737004` / exact PASS.
- Publication request commit: `acd7422ce6fb8b0cbc94cf7f7e6eb0491d116467`.
- Canonical publication: `f2120c4a39691b63619ceb26e724789e2aa66e85` / exact Git-blob reuse / no re-encode.
- Canonical verification: run `37087230188` / job `111099938256` / exact PASS.
- Manifest commit: `f4b2bbd21837545cf8607c884160a3efad9bb657`.
- Temporary staging binaries and temporary intake/canonical verifiers removed.
- Closeout path: `docs/project_control/gates/P0_3_video_pipeline/black_lady_generic_guest_crowd_core_set_v001_left_profile_authority_closeout_2026-10-03.md`.
- Project State advanced to `R226`.
- Dashboard advanced to `V161`.
- Next: `RIGHT PROFILE Design V0.1`.
- RIGHT PROFILE / BACK generation remains NOT AUTHORIZED.
- N21 remains HOLD / unresolved.
- N23 Candidate 02 remains PAUSED / NOT AUTHORIZED.

