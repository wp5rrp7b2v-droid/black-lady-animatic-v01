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
