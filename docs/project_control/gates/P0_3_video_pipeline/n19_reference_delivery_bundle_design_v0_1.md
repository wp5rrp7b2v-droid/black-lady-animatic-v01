# N19｜Reference Delivery Bundle Design V0.1

Status: `PRODUCT OWNER APPROVED / LOCKED / BUNDLE BUILD AUTHORIZED`

Date: 2026-09-29

Target bundle:

`N19_REFERENCE_DELIVERY_BUNDLE_V001`

Target generation:

`N19 Candidate 01`

Parent authorities:

- `S02-B Director Shot Design V0.2 / PRODUCT OWNER APPROVED + LOCKED`
- `N19 Scene Reference Design V0.2 / PRODUCT OWNER APPROVED + LOCKED`

## 1. N19 Director lock

N19 = `Conditions Can Change — Entrance Response`.

Owned dialogue:

`这里面瞬息万变，等你多来几次就知道了。`

Parent source scope:

`01:46.720 → 01:54.700`

Exact N19→N20 audio micro-cut remains deferred to later audio-aligned assembly.

Locked visual progression:

`N18 Jun looks outside alone → N19 Ning joins Jun's outward look and responds → N20 both turn away and move inward`

Locked composition:

- 9:16 vertical cinematic audio-comic still;
- medium two-shot;
- camera remains on the interior side of the castle entrance;
- Jun Luyuan remains closer to the doorway / exterior side of the pair;
- Ning Qiushui stands immediately beside or slightly behind / inside Jun;
- both look toward the same bright exterior direction;
- Ning is in a restrained speaking state;
- Ning may lightly rest one hand on Jun's upper shoulder;
- shoulder contact is optional-but-preferred, never mandatory if hand anatomy or character identity degrades;
- neither character has begun walking inward yet;
- main door remains OPEN;
- exterior remains bright / clear / apparently stable;
- no rain / storm / supernatural weather cue;
- no full hall establishment;
- no Neil as visible subject.

Narrative tone:

`shared outward gaze / experienced response / calm warning without alarm`

## 2. Canonical reference set

Reference count:

`5`

This count intentionally fits the current image-generation interface ceiling.

### REF-01｜Ning Qiushui Character Reference Sheet

- reference_id: `AST_IMG_000060`
- source_type: `ASSET`
- entity_id: `CHAR_NING_QIUSHUI`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- provenance: `COMPLETE`
- canonical_path: `production/image_library/derived_reference_sheets/ning_qiushui/CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- SHA-256: `15ec6c2682da0fe2502267bde21e9bc0bd7104bbf3e6041521121cc69a0e77be`
- byte_size: `1123635`
- Git blob: `b674733242ab5d603dc42c53b8f7582003064499`
- destination_group: `character_authority`
- authority_purpose: `NING_PRIMARY_IDENTITY_WARDROBE_CONTINUITY`

Responsibility:

- primary Ning identity;
- hairstyle;
- current wardrobe;
- facial / body proportion continuity.

---

### REF-02｜Jun Luyuan Character Reference Sheet

- reference_id: `AST_IMG_000057`
- source_type: `ASSET`
- entity_id: `CHAR_JUN_LUYUAN`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- provenance: `COMPLETE`
- canonical_path: `production/image_library/derived_reference_sheets/jun_luyuan/CHAR_JUN_LUYUAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- SHA-256: `e8a0410cfc176ec9d6446b84f89b2c12d0683ec32b927c90353e850c416d909e`
- byte_size: `969995`
- Git blob: `d11db79f4ceab2bb52139bfb8805f7c8f09b0cfc`
- destination_group: `character_authority`
- authority_purpose: `JUN_PRIMARY_IDENTITY_WARDROBE_CONTINUITY`

Responsibility:

- primary Jun identity;
- hairstyle;
- current wardrobe;
- facial / body proportion continuity.

---

### REF-03｜N17 Canonical Story Shot

- reference_id: `N17`
- source_type: `STORY_SHOT`
- shot_id: `N17`
- title: `Blood-Door Warning`
- approval / lifecycle: `APPROVED / CURRENT`
- canonical_path: `production/image_library/approved/story_shots/N17_BLOOD_DOOR_WARNING_APPROVED_V001.png`
- SHA-256: `bd31599978d927cbd3748dc77073503c78cf87ccc68b21458de08625ebbfa3a3`
- byte_size: `1671344`
- dimensions: `941x1672`
- Git blob: `c5020af8fa61225f0e4a88104990c1663fddcec9`
- destination_group: `continuity_refs`
- authority_purpose: `NING_JUN_TWO_PERSON_SCALE_SPEAKING_RELATIONSHIP_CONTINUITY`

Responsibility:

- established Ning / Jun relative scale;
- immediate current wardrobe and entrance-side lighting;
- Ning restrained speaking-state continuity;
- two-character relational continuity.

Restriction:

- N19 must NOT copy N17's tighter warning composition;
- N17 does not control N19 gaze direction;
- N17 does not require a static face-to-face conversation pose.

---

### REF-04｜N18 Canonical Story Shot

- reference_id: `N18`
- source_type: `STORY_SHOT`
- shot_id: `N18`
- title: `Clear-Sky Doubt`
- approval / lifecycle: `APPROVED / CURRENT`
- canonical_path: `production/image_library/approved/story_shots/N18_CLEAR_SKY_DOUBT_APPROVED_V001.png`
- SHA-256: `18746fdde8a3b7699061fd6f4a8a6b666d50001250a2df902bb3b5995e7e2613`
- byte_size: `2158626`
- dimensions: `941x1672`
- Git blob: `039471efd721fa5f822c4fb8ec933b4893f91641`
- destination_group: `continuity_refs`
- authority_purpose: `DIRECT_PRECEDING_SHOT_OUTWARD_GAZE_CLEAR_WEATHER_DOOR_CONTINUITY`

Responsibility:

- direct preceding-shot continuity;
- Jun's outward gaze direction;
- clear-weather visual state;
- open-door placement;
- current threshold lighting and exterior read.

Restriction:

- N19 must add Ning as a clear speaking partner;
- N19 must not become a near-duplicate Jun solo shot;
- N18's raised-hand gesture must NOT be repeated.

---

### REF-05｜Castle Entrance Scene Master / DAY_DOOR_OPEN

- reference_id: `AST_IMG_000052`
- source_type: `ASSET`
- entity_id: `SCENE_CASTLE_ENTRANCE`
- role: `SCENE_MASTER`
- asset_class: `ATOMIC`
- authority_class: `MASTER`
- approval / lifecycle / resolver: `APPROVED / CURRENT / CONDITIONAL`
- provenance: `COMPLETE`
- canonical_path: `production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- byte_size: `2305753`
- Git blob: `e4dafe096f5c5c8782257030a5a659aeec7808f9`
- destination_group: `scene_authority`
- authority_purpose: `CASTLE_ENTRANCE_DAY_DOOR_OPEN_SPATIAL_AUTHORITY`

Responsibility:

- castle entrance architectural identity;
- DAY state;
- OPEN main-door state;
- exterior / threshold spatial authority;
- bright exterior remains visually plausible and readable.

## 3. Why this five-reference set is preferred

N19 has three simultaneous continuity problems:

1. two separate character identities must remain stable;
2. it must continue directly from N18's outward-looking weather beat;
3. it must preserve the castle-entrance spatial state while changing the two-person body relationship.

The selected five-reference set covers these without exceeding the current generation interface ceiling:

- REF-01 + REF-02 = both identities;
- REF-03 = established Ning/Jun relationship and Ning speaking continuity;
- REF-04 = direct N18 outward-gaze / weather continuity;
- REF-05 = architectural / DAY / DOOR_OPEN scene truth.

No additional profile anchor is included because doing so would require dropping a more important continuity authority.

## 4. Shoulder-contact design rule

The shoulder touch is a `DIRECTORIAL PERFORMANCE OPTION`, not an anatomical hard requirement.

Preferred interpretation:

`Ning lightly rests one hand on Jun's upper shoulder while both look outside.`

Priority hierarchy:

1. preserve Ning identity;
2. preserve Jun identity;
3. preserve correct hand / arm anatomy and natural contact;
4. preserve shared outward gaze;
5. preserve open-door / clear-weather continuity;
6. only then preserve shoulder contact.

If the shoulder touch causes:

- distorted fingers;
- oversized hand;
- merged bodies;
- unnatural arm reach;
- excessive intimacy;
- staged friendship-pose reading;

then Work must omit the shoulder contact and keep both characters naturally standing side-by-side looking outward.

A clean no-contact version is preferable to a bad-contact version.

## 5. Authority precedence

1. `S02-B Director Shot Design V0.2`
2. `N19 Scene Reference Design V0.2`
3. `AST_IMG_000060` — Ning identity
4. `AST_IMG_000057` — Jun identity
5. `AST_IMG_000052` — entrance / DAY / DOOR_OPEN scene facts
6. `N18` — direct preceding-shot direction / weather / threshold continuity
7. `N17` — two-person scale / speaking relationship continuity

Conflict rules:

- Character Reference Sheets win identity / wardrobe conflicts.
- Scene Master wins architecture / door-state / DAY-state conflicts.
- N18 wins immediate outward-gaze continuity unless it conflicts with the Scene Master.
- N17 supports two-person relationship only and cannot force its tighter composition.
- Director / Scene Reference locks control framing, action and narrative emphasis.
- Shoulder contact never overrides anatomy or identity integrity.

## 6. Explicit exclusions

Do not include in `N19_REFERENCE_DELIVERY_BUNDLE_V001`:

- rejected N18 Candidates 01–03;
- N18 working / pre-approval images;
- superseded Ning / Jun character anchors;
- Neil references;
- A03;
- A05;
- A06;
- A07;
- First Hall Scene Master;
- mural corridor assets;
- MANOR_GATE Scene Master;
- N20–N23;
- rain / storm / ominous-weather references;
- internet / non-canonical imagery.

## 7. WORK_HANDOFF locks

`WORK_HANDOFF.md` must instruct Work to generate exactly:

`N19 Candidate 01`

Generation requirements:

- generate exactly one N19 Candidate 01;
- 9:16 vertical cinematic audio-comic still;
- medium two-shot;
- camera on the interior side of the castle entrance;
- Ning Qiushui and Jun Luyuan both remain at the entrance threshold;
- both look toward the same bright exterior direction;
- Jun remains closer to the doorway / exterior side;
- Ning stands immediately beside or slightly behind / inside Jun;
- Ning is the speaking emphasis;
- Ning mouth state = restrained natural speech;
- Ning expression = calm, experienced, slightly serious;
- Jun expression = attentive / still considering the weather question;
- preserve canonical Ning identity / hairstyle / wardrobe;
- preserve canonical Jun identity / hairstyle / wardrobe;
- preserve CASTLE_ENTRANCE / DAY / DOOR_OPEN state;
- preserve N18 clear-weather exterior continuity;
- preserve N17 two-person relative scale and local wardrobe/light continuity;
- shoulder contact is optional-but-preferred;
- if used, Ning's hand rests lightly and naturally on Jun's upper shoulder with correct scale and relaxed fingers;
- if shoulder contact cannot be rendered cleanly, omit it rather than force it;
- both characters remain standing; no inward walking yet;
- no direct camera gaze.

Explicit exclusions:

- arm-around-shoulder embrace;
- forceful shoulder grip;
- comforting / consoling pose;
- staged friendship portrait;
- oversized or malformed hand;
- merged arms / shoulders;
- repeated N18 outward-presenting hand gesture;
- hands in pockets;
- clothing-adjustment model pose;
- both characters facing camera;
- both characters walking inward;
- Neil;
- crowd / sixteen-guest group;
- rain;
- dark storm cloud;
- lightning;
- wet clothing;
- supernatural weather cue;
- closed door;
- hall establishment;
- mural corridor;
- rule text / warning symbols.

Narrative tone:

`the weather looks fine, but Ning calmly tells Jun that conditions here can change rapidly`

## 8. Planned artifact layout

`N19_REFERENCE_DELIVERY_BUNDLE_V001/`

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- `character_authority/AST_IMG_000060__CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `character_authority/AST_IMG_000057__CHAR_JUN_LUYUAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `continuity_refs/N17__N17_BLOOD_DOOR_WARNING_APPROVED_V001.png`
- `continuity_refs/N18__N18_CLEAR_SKY_DOUBT_APPROVED_V001.png`
- `scene_authority/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`

Retention target:

`7 days`

Product Owner manual reference upload:

`0`

Transport:

`GitHub Actions → short-lived Artifact → Work automatic acquisition`

Codex:

`NOT PART OF THIS STORY SHOT BUNDLE PATH`

## 9. Planned Bundle Spec contract

Future spec path after Product Owner approval:

`production/bundle_specs/N19_REFERENCE_DELIVERY_BUNDLE_V001.json`

Required fields:

- schema_version: `1.0`
- bundle_id: `N19_REFERENCE_DELIVERY_BUNDLE_V001`
- target_shot_id: `N19`
- sequence_id: `S02-B`
- target_candidate: `N19 Candidate 01`
- retention_days: `7`
- manual_product_owner_reference_upload: `0`
- builder_version: `STORY_SHOT_REFERENCE_BUNDLE_BUILDER_V1`

No N19-specific Bundle workflow may be created.

Use only:

`.github/workflows/story-shot-reference-bundle-builder.yml`

## 10. Build validation contract

Bundle construction must fail closed unless all `5/5` references pass:

1. exact reference count = 5;
2. unique Registry / Story Shot Index lookup;
3. entity / role / authority identity matches where applicable;
4. approval_status = APPROVED;
5. lifecycle = CURRENT;
6. resolver_usage allowed where applicable;
7. canonical path exact match;
8. regular non-symlink file;
9. exact byte_size match;
10. exact SHA-256 match;
11. exact Git blob match;
12. PNG signature valid;
13. dimensions readable;
14. artifact copy byte-identical;
15. post-assembly revalidation PASS.

Required result:

`PASS: 5/5 exact canonical reference binaries verified`

Only then:

`GENERATION_ALLOWED=TRUE`

Any mismatch:

`GENERATION_ALLOWED=FALSE`

and Work must not generate N19.

## 11. Current boundary

Current disposition:

`N19 REFERENCE DELIVERY BUNDLE DESIGN V0.1 = PRODUCT OWNER APPROVED / LOCKED / BUNDLE BUILD AUTHORIZED`

Not authorized yet:

- Bundle Spec creation;
- GitHub Actions Bundle build;
- Artifact production;
- Work acquisition;
- N19 Candidate 01 generation;
- N20 production;
- Story Shot publication / registration.

## 12. Product Owner approval

On 2026-09-29, the Product Owner explicitly approved this Bundle Design V0.1 and authorized the Bundle build.

Authorized next steps:

1. create `production/bundle_specs/N19_REFERENCE_DELIVERY_BUNDLE_V001.json`;
2. run the existing Generic Story Shot Reference Bundle Builder V1;
3. verify the resulting Artifact and exact `5/5` canonical inputs.

Image generation remains blocked until Bundle verification returns:

`GENERATION_ALLOWED=TRUE`
