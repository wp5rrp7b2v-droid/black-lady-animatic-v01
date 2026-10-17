# M01 Candle Engine V002 | Repeatable One-Click Readiness Design

Date: 2026-10-17
Status: DESIGN_ONLY / NOT IMPLEMENTED / NOT PRODUCT_OWNER_APPROVED
Branch: review/s02b-jun-nod-insert-20261014

## 1. Problem and evidence

The V007 full-length rough review reports 15/17 segments M01-enabled (1433/1927 frames; 74.364% timeline) but PO cannot readily perceive differences against V006. The metric reports **frame eligibility**, not flame motion, correct flame alignment, or perceptibility. Average authorized mask area across the full timeline is approximately 4.2%; maximum raw RGB delta only 12/255. V007 uses manually estimated ellipse anchors and one shared harmonic signal for all lights in a shot.

The earlier renderer `scripts/environment_dynamic_render_v001.py` already contains per-spot `phase` and `strength`; this capability was not propagated to the full V007 renderer. Its existence does not prove registration, flame-core movement, or visual quality.

## 2. Required outcome

A standard reusable M01 driver that turns registered, evidence-grounded candle sources into temporally natural micro-motion and local architectural illumination, with protected source imagery and soundtrack.

- **Known scene, approved light profile:** one-click render (no manual per-video coordinates).
- **Unregistered scene or new camera:** automatic light candidate detection and confidence assessment; missing or low-confidence source requires calibration and review. **Never silently guess or claim full automation.**
- Output per video: review MP4, optional synchronized A/B, source identity and profile hashes, flame-to-mask alignment evidence, per-light response metrics, protected pixel/scene QC, audio packet/time checks.
- Story Shot PNGs and official master files remain read-only; neither official index nor main can be mutated by preview workflow.

## 3. Mandatory components

**A. Scene Light Atlas**
Versioned scene/camera asset:
`scene_reference_sha256`, `scene_id`, `coordinate_space`, `source_id`, `source_type`, `flame_core_bbox_or_mask`, `practical_light_region`, `wall_receiving_light_polygon`, `protected_human_and_skin_masks`, `visibility`, `confidence`, `approval`. Preserve each independently verified source across shots; register transforms when crop/camera changes.

**B. Source discovery and registration**
Use existing atlas and frame matching/registration if known. Unknown scenes: propose candidate flame/wall sconces based on local image analysis, retain source evidence and confidence. Export visual overlays of *actual* frame + core, halo, wall and forbidden masks. For ambiguous light sources, STOP_FOR_CALIBRATION. Pure manually guessed ellipse coordinates are prohibited in automated production.

**C. Per-light animation engine**
For each registered source `i`, a deterministic independent temporal signal `f_i(t;phase_i,seed_i)` drives three linked layers: (1) minute flame-core shape/edge motion confined to original flame segmentation; (2) intensity and halo modulation; (3) architecture receiving-light changes obeying existing scene shading, distance and occlusion. Respect separate light phases. Do not move people, candles, camera, or repaint scenery. Restrict flame-core modifications to flames; other original pixels remain unchanged before encoding.

**D. QC gates**
- `SOURCE_IDENTITY_PASS`: approved input PNG/MP4 hash and identity unchanged.
- `LIGHT_REGISTRATION_PASS`: each effect source has traceable flame/sconce evidence and a visually inspectable mask overlay on the exact video frame, with unique `source_id`. Registration failures stop auto-render.
- `PER_SOURCE_MOTION_PASS`: flame-core area, edge or position must show a bounded, temporally coherent measurable change for visible flames; a zero flame-core motion signal is a failure for shots with visible flame.
- `ILLUMINATION_LINK_PASS`: associated wall halo varies in sync with *its own* flame source, not one universal signal. No ungrounded whole-frame modulation.
- `PROTECTION_PASS`: pre-encode pixels outside authorized visual effect masks unchanged; human/face/wardrobe exclusions enforced; no unnatural brightness uplift.
- `VISIBILITY_REVIEW`: A/B at normal speed **must be perceptible and natural to the PO**; a bitwise pixel delta or number of eligible shots is never sufficient.
- `DELIVERY_PASS`: exact frame count, fps, duration; original AAC payload and timestamps preserved when required; complete decode, artifact SHA.
- `PUBLICATION_GATE`: visual approval does NOT imply official publication; each lifecycle has a separate PO-controlled promotion.

Exact visibility/geometry acceptance tolerances must be empirically established from N23 and NEW-02 tests, not invented as a universal 12/255 threshold.

**E. One-click GitHub Actions entrypoint**
`workflow_dispatch` parameters: `scene_or_video_id`, `light_profile_version` (or `auto` with fail-closed confidence), `test_mode` (`alignment_only`, `pilot`, `review_full`), `ab_comparison`. The workflow resolves approved profiles and builds from immutable assets. It never auto-approves or merges. Automatic scripts cannot claim supported light coverage where none exists.

## 4. Implementation milestones (strict order)

1. **Gate 0: alignment truth.** For current V007 17 frames, generate source-frame overlays containing detected/registered flame cores, luminous halo, architectural receiving-light masks and protected people. Audit wrong/unsupported coordinates, and record `PASS/NEEDS_CALIBRATION/NO_PRACTICAL` for every shot. No full length replacement render.
2. **Gate 1: registered pilot.** Select N23 plus NEW-02 (known favorable references) and one previously unverified shot. Build per-source atlas and actual flame animation. Confirm exact visual core/halo alignment with evidence.
3. **Gate 2: perceptibility pilot.** Short A/B at normal speed, approved style baseline, technical QC and Product Owner visual review. Adjust strength based on observed lighting, not arbitrary universal gains.
4. **Gate 3: batch regression.** Run all eligible S02-B shots with per-shot confidence, skip daylit/no practical shots honestly; full V008 A/B review.
5. **Gate 4: reusable product.** Generalize to other S02 scenes with versioned asset atlas, simple one-click dispatch and fail-closed unseen-scene calibration.

## 5. Do not treat existing approval as blanket approval

The N23 and NEW-02 V003 candlelight samples were accepted as visual style references. They are **not** approvals of inaccurate mask placement, the V007 implementation or any new flame-shape algorithm. All changes remain review-only pending PO.

---

## 6. 2026-10-17 Product Owner correction: reusable ENGINE is the deliverable, not merely S02-B success

**PO decision:** The purpose of M01 is a **reusable, cross-shot and cross-scene candlefire engine** for many future films and scenes. Passing S02-B is a **necessary prerequisite** and first acceptance gate, **not proof the engine is reusable nor sufficient to close the project**.

### Two distinct approval milestones

- **G-S02B / Pilot validation:** Calibrated M01 locates real candle cores and nearby light-receiving geometry in S02-B, protects people in all frames, creates independent natural flame + reflected-light motion, and passes PO-reviewed A/B at normal speed. Passing this gate allows **S02-B pilot use only**, not general batch production.
- **G-REUSE / Product acceptance:** A *frozen* M01 engine, without per-shot manual recoding or source coordinate guessing, runs on **independent never-used-for-tuning scenes**. It must automatically recover known approved Scene Light Atlas profiles, propose well-grounded sources in unregistered scenes, flag ambiguous/missing sources for calibration instead of rendering, protect human pixels, and deliver visual and binary QA. Only this gate supports the designation **REUSABLE M01 CANDLE ENGINE**.

Do not promote an engine because the workflow ran successfully, because all S02-B clips were covered, or because a fixed set of S02-B source coordinates passed. S02-B-only scripts are test fixtures and must not become the permanent engine API.

### Cross-scene release test matrix (preserve independent holdouts)

Test scenes must be selected from the repository's available approved/registered environments and have verifiable source imagery, without assuming every environment contains candles.

1. **Same scene, changed framing:** wide shot, close-up, crop, scale, or shifted camera. Light locations follow the actual image/camera transform, not a copied fixed pixel coordinate.
2. **Different castle interiors:** at least two visually distinct sets such as an entrance lobby, corridor, guest room, gallery or hall **where a visible or evidenced practical light is actually present**. Do not choose/test an invented fixture.
3. **Adverse cases:** candelabra with multiple flames; partial candle occlusion; candle behind a foreground moving/person mask; overexposed or pale flame; person wearing dark clothes; a flickering reflection near a face.
4. **Negative cases:** daylight or no reliable candle source, another bright object imitating a flame. Must return `NO_PRACTICAL` or `CALIBRATION_REQUIRED`, not manufacture flicker.
5. **Repeatability and regression:** same input identity + profile + seed yields deterministic output; changing input or source profile invalidates cached locations as appropriate. Accepted scene profiles are reused without additional manual XY tuning.
6. **Visual product acceptance:** review short natural-speed A/B clips from S02-B and independent unseen scenes. PO approves perceptibility, realism, continuity and subject protection, not a single pixel-based PASS.

### Release deliverables

- Independently versioned engine code and CLI/Action interface: `input`, `output`, `scene_profile=auto|approved:<version>`, `mode=diagnostic|pilot|review_full`, `ab=true|false`; no S02-B-specific constants in common engine.
- Versioned `Scene Light Atlas` with stable fixture IDs, reference frame/transform, per-flame segmentation and receiving-light regions, person exclusion, confidence and review status. Reuse from approved atlas where reliable; unfamiliar sets require initial profile calibration, then become repeatable.
- Per-input machine-readable localization and human-protection assessment, source masks/overlays, visible-flame-movement/illuminance evidence, error/uncertainty and source/model version provenance.
- Cloud GitHub Actions single-run invocation for batch *eligible* inputs, deterministic versioning, independent verification and downloadable video or explicit fail-closed report. No PO bypass, main merge or canonical publication.
- Release dashboard / acceptance matrix that differentiates **S02-B PILOT PASS** from **CROSS-SCENE REUSABLE ENGINE PASS**.

### Change to milestone order

The earlier Gate 4 is not an optional later enhancement. Following S02-B pilot validation (G-S02B), cross-scene holdout tests, fail-closed automation and approval (G-REUSE) are **required** before M01 can be considered complete or offered as a reliable one-click effect across future video batches.

**Current measured status:** V007 Gate0 position failed; human protection unverified on all frames; N24 and NEW-01 localization unresolved in subsequent Gate1C diagnostics. `G-S02B=BLOCKED`, `G-REUSE=NOT_STARTED`, batch rendering `HOLD`. Existing completed diagnostic Actions do **not** alter this status.
