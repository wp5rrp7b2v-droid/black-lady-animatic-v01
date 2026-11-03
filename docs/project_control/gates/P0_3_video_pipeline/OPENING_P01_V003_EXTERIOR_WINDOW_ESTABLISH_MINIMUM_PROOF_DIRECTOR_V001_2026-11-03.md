> **SUPERSEDED / PO VISUAL FAIL on 2026-11-03:** Product Owner rejected the through-window view with visible people as voyeuristic. This earlier window director is historical only and not valid for future generation. Active replacement director: `OPENING_P01_V004_RESIDENCE_GATE_NO_PEOPLE_DECISION_AUDIO_DIRECTOR_V001_2026-11-03.md`. Active Work handoff: `OPENING_P01_V004_RESIDENCE_GATE_WORK_SINGLE_CANDIDATE_HANDOFF_2026-11-03.md`. Old window Bundle spec has both authorizations set FALSE. No change to any existing approved seven P01 images.

# 《诡舍·黑衣夫人》｜Opening P01 V003｜住所窗外建立镜｜Minimum Proof Director V001

Date: 2026-11-03
Status: **DIRECTOR TEST APPROVED IN PRINCIPLE / ONE NEW CANDIDATE AUTHORIZED / ARTWORK NOT YET PO APPROVED / NOT CANONICAL**

## 1. Decision and factual basis

On 2026-11-03, Product Owner asked whether P01 needs some shots outside the conversation scene, then accepted the recommendation to **test a single short exterior-residence establishing shot** with “好”. Scope is one exploratory visual test, not a permission to create multiple exterior scenes, a formal external Scene Master, a new approved Story Shot, or to replace P01 Video V002.

PO previously reviewed P01 V001/V002 and found image repetition, monotonous visual coverage and a lag when Bai Xiaoxiao started speaking. V002 had 17 edit cuts but only seven independently approved images; that is why a genuinely new visual angle is being tested.

Current authoritative inputs:
- Approved 192.257s compact original-audio edit `OPENING_P01_P04_NEIL_COMPACT_AUDIO_PROOF_V001.m4a`, original source SHA256 `1701f3a8140775550a30ac788b9221486349c058278d1ef0c2c5163664d6c4ac`.
- P01 uses opening approx 00:00–01:03.38 of that track. Actual exact word boundaries not verified.
- Approved `OPENING_P01_OPEN_01` JPEG: `production/image_library/approved/story_shots/OPENING_P01_OPEN_01_THREE_PERSON_DECISION_ESTABLISH_APPROVED_V001.jpeg`, 864×1536, SHA256 `4ccebb6a903b9cbeac1dfdc2e8b05c7f5dafa05e31cff53e775dfa2f37945452` and Git blob `9c5fc2d1d5bcc711a0be129fcc3e3229f039bf3a`.
- Controlled apartment interior scene anchor `OPENING_P01_OPEN_01_BAI_RESIDENCE_SCENE_ANCHOR_V001` is approved only for **interior** spatial continuity, not for a definitive apartment-building exterior.
- Seven existing P01 story shots APPROVED/CURRENT; total approved Story Shots 42; formal videos 3; P0.3 still IN PROGRESS.

## 2. New single candidate

- ID: `OPENING_P01_INS_00_WINDOW_EXTERIOR_ESTABLISH`
- Candidate filename: `OPENING_P01_INS_00_WINDOW_EXTERIOR_ESTABLISH_CANDIDATE_01.png`
- Target: one 941×1672 9:16 PNG, 2.5D cinematic animated film style.
- Planned insertion: **0–about 2.5s** of Opening, just before using P01-OPEN-01 to establish three characters in the living room. Bai Xiaoxiao's already approved voice is heard as off-screen speech throughout, not removed or redubbed.
- Director's composition: restrained near-exterior window / threshold establishing angle, close enough that the established room's recognisable **interior window geometry, warm light and furniture relationship** can be seen inside. An oblique glimpse at the three-character conversation may be suggested by tiny indistinct silhouettes, but **no new close-ups or readable character faces**. Give the viewer a clear understanding that the conversation is taking place inside a private real-world residence; not a panoramic street or a fictional named building.
- Outdoor parts must be minimal / deliberately unidentifiable: only short generic frame or wall edge required to show camera sits immediately beyond the window. **Do not invent a recognizable facade, floors, address, skyline, street, neighborhood, building type, weather, rain, night/day time or season** not supported by the approved interior image. Any exterior architecture outside the image evidence is a working hypothesis, not an Approved Scene Master fact.
- No supernatural visuals, blood door, castle, manor exterior, mist-world imagery, visualized dangers or drama-closing new action.
- The original P01-OPEN-01 JPEG is used exclusively as approved interior space/light/window geometry reference; do **not** transfer its character faces as new Identity Masters. Source JPEG stays exact and unmodified.

## 3. Minimal A/B assembly test and gates

After actual Work candidate generation (and PO inspection of new image), compare two rough cuts using the identical already-approved original voice:
- **A**: V002 00:00–~00:08 existing opening, seven-images-only flow.
- **B**: New exterior-window insert 00:00–about 00:02.5 → existing P01-OPEN-01 apartment interior from ~00:02.5 → approved other shot sequence.
- Set the precise first shot cut only after listening to the real first sentence; rough 2.5s is not an exact EDL.
- **PASS**: Viewer perceives location/atmosphere more readily, Bai's first line remains clearly supported, entry to the three-character living room is coherent, no invented building/time facts or window mismatch, and PO prefers B on an actual played A/B proof.
- **FAIL**: Exterior makes the opening too distant from speakers, creates ungrounded architecture/weather/time, contradicts approved room window layout, fails character / style continuity, or PO sees no perceptual benefit. If FAIL, retire candidate rather than manufacture multiple related exteriors.

**Scale Gate**: Before opening further exterior setups, test this one real candidate. Only if A/B is PASS consider integrating it into a full P01 V003 and further selected indoor coverage shots (INS01 / INS02). Do not independently publish or register any new Story Shot prior to explicit PO visual approval.

## 4. Production route

Director design (this file) → exact existing reference spec → GitHub Actions validated Bundle → Work 1 PNG Candidate → PO visual review → local minimal audiovisual A/B → PO audiovisual review → on approval, Chat exact binary publication and Story Shot registration.

Work must **not** use screenshot mockups, fake reference images, cropped old P01 screenshot or other female cast faces to bypass the verified Bundle. Codex is not involved; no video or canonical source is changed at this phase.

## 5. Verified production bundle and one-shot Work handoff (2026-11-03)

**FACT: Builder PASS / Exact binary reference PASS; output picture not yet produced.**

- Approved single-shot Bundle Spec: `production/bundle_specs/OPENING_P01_INS_00_WINDOW_EXTERIOR_ESTABLISH_REFERENCE_DELIVERY_BUNDLE_V001.json`.
- GitHub Actions Run: [41555252819](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41555252819), `completed / success`.
- Artifact ID: `13193826977`, artifact name `OPENING_P01_INS_00_WINDOW_EXTERIOR_ESTABLISH_REFERENCE_DELIVERY_BUNDLE_V001`.
- Independent downloaded ZIP SHA-256: `a4773fddf4b92bfa4f5a8a6c5d3af847df6ed01f8f3bf4b2b0f37f521e2fb99c`; ZIP contains exactly three expected entries: `delivery_manifest.json`, `WORK_HANDOFF.md`, and the single P01 approved scene JPEG reference.
- Manifest `overall_result=PASS`, `generation_allowed=true`, one original reference. Independently recalculated source SHA-256 `4ccebb6a903b9cbeac1dfdc2e8b05c7f5dafa05e31cff53e775dfa2f37945452`, Git Blob `9c5fc2d1d5bcc711a0be129fcc3e3229f039bf3a`, 336546 bytes, 864×1536 JPEG; all match GitHub approved original.

**Work execution permission:** Product Owner's affirmative decision authorizes **one** exploratory candidate only, named `OPENING_P01_INS_00_WINDOW_EXTERIOR_ESTABLISH_CANDIDATE_01.png`. Work must download and independently verify this exact validated Artifact and follow embedded `WORK_HANDOFF.md`. If the approved interior JPEG cannot establish a convincing but noninvented near-window exterior-side composition, Work must report `SCENE_EXTERIOR_UNGROUNDED` rather than hallucinating a building facade, weather or time of day. Work returns candidate to PO for visual approval; no automatic second image or asset registration.

**Pending Gate:** No actual new image, no 0–8s A/B video, no PO review. Project State R411 / Story Shot Index 42 / Video Index 3 / P0.3 IN PROGRESS remain authoritative.
