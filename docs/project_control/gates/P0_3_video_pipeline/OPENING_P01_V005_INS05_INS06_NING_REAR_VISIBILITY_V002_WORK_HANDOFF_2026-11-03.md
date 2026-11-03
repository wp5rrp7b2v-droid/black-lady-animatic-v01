# 《诡舍·黑衣夫人》｜P01 V005 INS-05 / INS-06｜宁秋水后景保留｜Work V002 两张修正制图正式交接

Date: 2026-11-03
State: **TWO BUNDLES VERIFIED EXACT 10/10 PASS / EACH ONE CANDIDATE_02 AUTHORIZED / PO VISUAL REVIEW PENDING / NO PUBLICATION OR REGISTRATION**

## 1. PO feedback → why V001 failed

PO reviewed Work-created V001 Bai Xiaoxiao action images and reported **宁秋水在原沙发后方的位置不见了**. GitHub audit confirms neither INS-05 V001 nor INS-06 V001 Bundle contained Ning character identity as a direct positive reference, and the initial handoff let INS05 crop Ning off-screen. These are input-constraint errors; no V001 output is PO-approved. V001 generation authorization was disabled for both old specifications.

Active corrected director, mandatory read:
`docs/project_control/gates/P0_3_video_pipeline/OPENING_P01_V005_INS05_INS06_NING_REAR_VISIBILITY_DIRECTOR_V002_2026-11-03.md`.

Repo: `wp5rrp7b2v-droid/black-lady-animatic-v01`.

## 2. Verified GitHub Actions delivery — V002 only

| Order | New target (exact filename) | Bundle ID | Actions run | Artifact ID | Original reference verification |
|---|---|---|---|---|---|
| 1 INS05 | `OPENING_P01_INS_05_BAI_RESTRAINING_GESTURE_CANDIDATE_02.png` | `OPENING_P01_INS_05_BAI_RESTRAINING_GESTURE_REFERENCE_DELIVERY_BUNDLE_V002` | [41589534914](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41589534914) | **13209272925** | **PASS 5/5** |
| 2 INS06 | `OPENING_P01_INS_06_BAI_FORWARD_WARNING_EXPLAIN_CANDIDATE_02.png` | `OPENING_P01_INS_06_BAI_FORWARD_WARNING_EXPLAIN_REFERENCE_DELIVERY_BUNDLE_V002` | [41589540027](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41589540027) | **13209297938** | **PASS 5/5** |

Both Actions concluded SUCCESS, log `PASS: 5/5 exact canonical reference binaries verified` and `GENERATION_ALLOWED=TRUE`.

Independently downloaded and inspected actual ZIP artifacts locally:
- INS05 original artifact ZIP: 9,038,547 bytes, SHA256 `be7c2dd36203af4ec172e6d5c7e61a6ee3180643baeeb8e20ad5da5a65f989df`.
- INS06 original artifact ZIP: 9,038,599 bytes, SHA256 `61ddf4c9ae49f05abb5d5951913684ce9f54bdfd48f948f8a67a56ba8350b795`.

Both ZIP CRC PASS and include `WORK_HANDOFF.md`, `delivery_manifest.json`, exactly FIVE original images each. Independent SHA256, Git Blob SHA-1, exact byte counts and PNG dimensions/JPEG signature all **5/5 PASS per artifact**.

### Five approved image sources in EACH Bundle

1. `OPENING_P01_OPEN_01_BAI_RESIDENCE_SCENE_ANCHOR_V001`: original Approved JPEG 864×1536; exact approved room/sofa/furniture/character blocking and natural lighting, not Bai face identity master.
2. `AST_IMG_000109`: Bai Xiaoxiao C06 FACE_FRONT, Approved independent identity.
3. `AST_IMG_000110`: Bai Xiaoxiao FACE_3Q_LEFT, Approved independent identity.
4. `AST_IMG_000060`: **NING QIUSHUI APPROVED CHARACTER_REFERENCE_SHEET** in black clothes; mandatory visible rear sofa character.
5. `OPENING_P01_OPEN_07_P01_ACTION_SPATIAL_AUX_V001`: approved three-person relationship, **Bai left, Ning center/back behind sofa, Jun front/right**.

Reference cap is FIVE. The removed Jun character sheet may NOT be substituted without rebuilding a new Bundle. Jun's blue-gray clothing and partly visible front-right foreground blocking derive from approved OPEN01 and OPEN07, not an invented close-up identity. **No recognizable new Jun close-up**. No old OPEN03 or rejected INS05/06 V001 candidate as direct positive input.

## 3. Hard spatial pass — not negotiable

The scene is the original Bai Xiaoxiao private living room: Bai **LEFT foreground** on red-nightdress sofa speaking, Jun **RIGHT foreground** in blue-gray clothes sitting (may be only blurred shoulder), Ning Qiushui **CENTER/REAR, physically BEHIND THE SAME SOFA BACKREST** in black.

**Ning MUST BE VISIBLE** in the generated final image: his independent head and shoulders and part of upper torso must be discernible above the sofa backrest, not fully cropped away, not a vague black blob, not completely hidden by Bai/hair/lamp, and NOT teleported forward to the side or Bai's seat. He's a listener in the back, not the dominant speaker or a posed group portrait.

Camera: choose a naturally wider, slightly diagonal medium-wide composition with foreground Bai and BACKGROUND Ning. Preserve original left/right camera axis, bookshelves, warm interior lamp, coffee table and sofa backrest from approved OPEN01 / OPEN07.

If retaining Ning proves physically impossible within a chosen tight framing, **widen/recompose while respecting approved scene**; do not silently omit Ning. Report `SPATIAL_CONTINUITY_FAILED` if an honest visible result is impossible, not an invented or wrong-side geometry.

## 4. The TWO different Bai performance beats

**INS05 C02**: Bai remains seated left. Lightly raises ONE hand, palm subtly outward/down, clear but restrained warning gesture. Her other hand on armrest/knee. Facial expression concerned, slight brow furrow, naturally parted lips. Jun partly at right as listening target, Ning visible center-rear listening. Audio intention approximately 0–4s of P01 (unverified exact words). Medium-wide 3/4 with sofa armrest in view.

**INS06 C02**: same left seat and C06 face, Bai noticeably LEANS FORWARD, one hand remains on knee as support, other opens palm UP toward Jun explaining danger/accompaniment. More composed and serious than INS05; visibly different pose AND hand orientation. Ning stays in **the SAME visible rear-center spatial position**. Audio intention about 19–31s, not a locked EDL. Don't turn this into just another solo face crop.

Visual style: 941×1672 PNG portrait 9:16, grounded 2.5D semi-realistic cinematic animated drama, warm subdued palette, realistic body proportions, fingers and wrist anatomy. No text in image, no extra prop, no new room, no castle or blood door.

## 5. Production and delivery

1. Work first reads corrective V002 director and this exact handoff, then downloads each respective GitHub Actions artifact.
2. Independently verifies manifest and five actual unmodified original JPEG/PNG binary sources including SHA256/Git blobs; STOP on mismatch.
3. Generates only **one INS05 C02** from its own V002 Bundle; then only **one INS06 C02** from the second V002 Bundle; no repeated per-step PO confirmation, no unbounded auto-variants. Do NOT use a candidate from step 3 as a reference for step 4.
4. Visual QA requires visible rear-center Ning, unchanged identities and furniture and distinct Bai hand gestures. If FAIL, return specific defects rather than claim the PO approved image.
5. Deliver two exact original 941×1672 PNG download links, sizes and reference provenance, one ordered comparison for PO to review.
6. STOP without independent publishing, exact-binary Story Shot registration, audio/video assembly, changes to current P01 seven Approved original images, 42-Story Shot index, Video Index 3, approved 192.257s source audio or P0.3 project Gate.

PO-approved INS00 empty residence entrance + INS04 gently resting hand on shoulder are still **APPROVED IMAGE / REGISTRATION HELD FOR JOINT BATCH**. Previous INS01/INS02/old INS04 standing and these V001 Bai outputs are PO FAIL, NEVER automatically include in later approved batch.

A V002 GitHub Actions PASS is proof of **reference input validity only**, NOT that newly generated artwork has fixed Ning's visibility. **Next independent proof is Product Owner actual review of two C02 images**.
