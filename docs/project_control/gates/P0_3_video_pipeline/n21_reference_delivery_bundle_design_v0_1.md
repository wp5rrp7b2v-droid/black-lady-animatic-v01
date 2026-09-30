# N21｜Reference Delivery Bundle Design V0.1

Status: `PRODUCT OWNER APPROVED / LOCKED / BUILT / 6 OF 6 PASS / WORK GENERATION SUSPENDED PENDING S02-B V0.3`

Date: 2026-09-30

Target shot:

`N21｜Sixteen Guests Enter`

Target candidate after later build authorization:

`N21 Candidate 01`

Target bundle:

`N21_REFERENCE_DELIVERY_BUNDLE_V001`

Scene authority:

`N21 Scene Reference Design V0.2｜Named Character Seeding / PRODUCT OWNER APPROVED + LOCKED`

## 1. Design objective

Build the smallest practical formal reference set that can support all four N21 priorities without turning the shot into a cast lineup:

1. established castle entrance / open-door spatial continuity;
2. immediate visual continuity from N20;
3. reliable identity seeding for Su Xiaoxiao / Liao Jian / Wen Qingya / Guang Yong;
4. preservation of full sixteen-person group scale.

Bundle design principle:

`GROUP FIRST / NAMED CHARACTER SEEDS SECOND / REFERENCE LOAD CONTROLLED`

Formal generation reference count:

`6`

## 2. Reference set

### REF-01｜Castle Entrance Scene Master

- reference_id: `AST_IMG_000052`
- source_type: `ASSET`
- entity_id: `SCENE_CASTLE_ENTRANCE`
- role: `SCENE_MASTER`
- state: `DAY_DOOR_OPEN`
- authority_class: `MASTER`
- approval / lifecycle: `APPROVED / CURRENT`
- canonical_path: `production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- expected SHA-256: `d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`
- expected byte_size: `2305753`
- expected Git blob: `e4dafe096f5c5c8782257030a5a659aeec7808f9`
- destination_group: `scene_authority`

Authority purpose:

- castle entrance architecture;
- main-door geometry;
- `DAY_DOOR_OPEN` fact;
- entrance material / stone architecture continuity.

Must NOT force:

- exterior-dominant lighting;
- empty-scene composition;
- exact Scene Master camera angle.

N21 lighting instruction overrides any tendency to spill hard daylight deep into the interior.

### REF-02｜N20 Canonical Story Shot

- reference_id: `N20`
- source_type: `STORY_SHOT`
- title: `Do Not Touch Things — Start Moving Inward`
- approval / lifecycle: `APPROVED / CURRENT`
- canonical_path: `production/image_library/approved/story_shots/N20_DO_NOT_TOUCH_THINGS_APPROVED_V001.png`
- expected SHA-256: `a61ab1310e86938b2a416516138981aafaf421add44c1a9d5a80d0ff9ec59a9e`
- expected byte_size: `2022630`
- expected Git blob: `58e145a51c3f993827e5e47964ad0e7f9dd9f0aa`
- dimensions: `941x1672`
- destination_group: `immediate_story_continuity`

Authority purpose:

- immediate visual continuity from N20;
- dim / warm interior render language;
- entrance-to-interior transition depth;
- current Ning Qiushui + Jun Luyuan production appearance;
- current wardrobe and body-proportion continuity.

Must NOT control:

- N20 two-person dominance;
- N20 exact pose;
- private conversational framing;
- exact gait phase;
- N20 character prominence.

Hard rule:

`PRESERVE APPEARANCE / LIGHTING CONTINUITY; EXPAND COMPOSITION TO GROUP SCALE`

### REF-03｜Su Xiaoxiao Character Reference Sheet

- reference_id: `AST_IMG_000061`
- source_type: `ASSET`
- entity_id: `CHAR_SU_XIAOXIAO`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- canonical_path: `production/image_library/derived_reference_sheets/su_xiaoxiao/CHAR_SU_XIAOXIAO_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- expected SHA-256: `e869d118e22e50cfe6e6280632da4534e660dc74ec96cf3871099b87cf42701a`
- expected byte_size: `700794`
- expected Git blob: `2b584d4172484216478319025440b16ba7c2859a`
- destination_group: `named_character_seeds`

Authority purpose:

- Su Xiaoxiao identity;
- hairstyle;
- wardrobe;
- body proportions;
- feminine-presenting visual appearance.

Hard restriction:

`NO VISUAL FORESHADOWING OF THE LATER GENDER REVEAL`

At this story point Su must visually read exactly as the other characters perceive Su.

### REF-04｜Liao Jian Character Reference Sheet

- reference_id: `AST_IMG_000058`
- source_type: `ASSET`
- entity_id: `CHAR_LIAO_JIAN`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- canonical_path: `production/image_library/derived_reference_sheets/liao_jian/CHAR_LIAO_JIAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- expected SHA-256: `3f2f01fea63401a3726abdf5053e75361d5d43091830ce8e1636883bd1cd6817`
- expected byte_size: `650562`
- expected Git blob: `f8b600e49c0bd40177c723d9c0abd474678f41c2`
- destination_group: `named_character_seeds`

Authority purpose:

- Liao Jian identity;
- hairstyle / wardrobe;
- fit young-adult body proportion.

Do not exaggerate into a bodybuilder or hero silhouette.

### REF-05｜Wen Qingya Character Reference Sheet

- reference_id: `AST_IMG_000062`
- source_type: `ASSET`
- entity_id: `CHAR_WEN_QINGYA`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- canonical_path: `production/image_library/derived_reference_sheets/wen_qingya/CHAR_WEN_QINGYA_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- expected SHA-256: `09551f02ad9cd4d3ae8e4483d017c230877165c4b88346ff9762527246569f0c`
- expected byte_size: `641800`
- expected Git blob: `e391622643034485dc4e9a862ba29cde72cdeefd`
- destination_group: `named_character_seeds`

Authority purpose:

- Wen Qingya identity;
- hairstyle / wardrobe;
- round-frame-glasses continuity;
- cultured / literary visual impression.

Do not pre-stage her later argumentative / analytical interaction with Ning.

### REF-06｜Guang Yong Character Reference Sheet

- reference_id: `AST_IMG_000056`
- source_type: `ASSET`
- entity_id: `CHAR_GUANG_YONG`
- role: `CHARACTER_REFERENCE_SHEET`
- asset_class: `DERIVED_REFERENCE`
- authority_class: `DERIVED`
- approval / lifecycle / resolver: `APPROVED / CURRENT / DEFAULT`
- canonical_path: `production/image_library/derived_reference_sheets/guang_yong/CHAR_GUANG_YONG_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- expected SHA-256: `2a98e74ddba60a259758643b56ffddafd5a7cb30de040880f991fb47216b45fb`
- expected byte_size: `475761`
- expected Git blob: `e37ad60d933c3fdc434768bb449019146eb9333e`
- destination_group: `named_character_seeds`

Authority purpose:

- Guang Yong identity;
- short / slightly chubby silhouette;
- hairstyle / wardrobe.

Do not stage him already asking Neil a question.

## 3. Why Ning / Jun Character Sheets are excluded

Ning Qiushui and Jun Luyuan remain visible continuity characters, but they are intentionally not given separate Character Reference Sheets in V001.

Reason:

- N20 canonical is the immediately preceding approved Story Shot;
- N20 already carries their exact current production appearance together in the correct lighting / scene state;
- N21 deliberately lowers their prominence;
- two extra sheets would increase reference count from 6 to 8 and raise the risk that the generator turns the shot back into a named-character ensemble.

Therefore:

`N20 = NING/JUN CONTINUITY AUTHORITY FOR N21 V001`

If Candidate 01 later shows identity drift specifically in Ning or Jun, a Bundle V002 may add targeted character sheets. Do not pre-emptively overload V001.

## 4. Why A03 is excluded from the formal Bundle

`A03｜门内反拍` remains a valid approved spatial precedent.

However it is excluded from V001 generation inputs because:

- AST_IMG_000052 already supplies canonical entrance architecture;
- N20 supplies current interior transition / lighting state;
- A03 would become a third scene/composition image and could overconstrain the generator;
- its value is primarily director review, not identity generation.

Therefore:

`A03 = REVIEW AUTHORITY ONLY / NOT BUNDLE INPUT`

## 5. Sixteen-person group rule

The Bundle does not attempt to provide reference sheets for all sixteen people.

Generation instruction must create:

`16 TOTAL PARTICIPANTS`

with:

`BALANCED MALE/FEMALE PRESENTATION AT THIS STORY POINT`

and ten unnamed participants designed as distinct secondary adults.

If all figures are countable:

`EXACTLY 16`

If natural overlap / cropping prevents exact counting:

- image must still plausibly represent the full cohort;
- visible scale must not contradict sixteen;
- no 20+ crowd;
- no small 6–8 person group.

Su Xiaoxiao must remain female-presenting in this shot.

## 6. Named-character blocking authority

Formal placement intent:

- Ning + Jun: near-mid continuity layer, secondary;
- Su + Liao: mid-layer loose teammate cluster;
- Wen: separate mid-side placement, optionally with one unnamed companion;
- Guang: rear-mid / threshold cluster;
- remaining ten: distributed through depth layers.

Do not arrange the six named characters together.

Do not rotate named characters toward camera merely to prove identity.

Identity visibility can come from:

- silhouette;
- hair;
- wardrobe;
- partial side / rear-3Q face;
- body proportion.

## 7. Group / composition hard locks for Work handoff

Candidate 01 must read first as:

`A FULL COHORT ENTERING THE CASTLE`

not:

`A PROMOTIONAL MAIN-CAST GROUP`

Required:

- wide interior oblique entrance shot;
- camera inside castle, laterally offset;
- still-open main doors visible behind group;
- layered depth;
- natural teammate sub-clusters;
- mixed gait phases;
- natural occlusion;
- no one facing camera intentionally;
- Neil absent;
- group traveling inward.

## 8. Lighting hard locks

- open entrance may be brighter;
- daylight remains localized near doorway;
- no hard sunlight flooding foreground;
- no direct exterior sunlight dominating participant bodies deeper inside;
- warm / dim interior architectural lighting dominates mid / foreground;
- no rain;
- no storm foreshadowing.

## 9. Character-seeding hard locks

### Su Xiaoxiao

- recognizable;
- feminine-presenting;
- visually attractive / petite;
- no reveal clue;
- no comedy pose.

### Liao Jian

- recognizable;
- fit young adult;
- no exaggerated hero build;
- naturally near Su but not interacting theatrically.

### Wen Qingya

- recognizable;
- round-frame glasses if feasible;
- observant / cultured visual read;
- no confrontation.

### Guang Yong

- recognizable;
- short / slightly chubby;
- rear-mid;
- no question gesture / Neil interaction.

## 10. Unnamed-participant generation locks

The ten unnamed participants:

- must not look cloned;
- must not repeat named-character faces;
- should vary hairstyle, clothing, height and body type;
- remain grounded contemporary adults;
- no supernatural ghost styling;
- no transparent / glowing bodies.

## 11. Authority precedence

1. `S02-B Director Shot Design V0.2`
2. `N21 Scene Reference Design V0.2`
3. `AST_IMG_000052` — entrance architecture / door-state authority
4. `N20 canonical` — immediate production / Ning-Jun / lighting continuity
5. `AST_IMG_000061` — Su identity
6. `AST_IMG_000058` — Liao identity
7. `AST_IMG_000062` — Wen identity
8. `AST_IMG_000056` — Guang identity
9. `A03` — director review precedent only, not generation input

No image reference overrides:

- sixteen-person story fact;
- group-first composition;
- Neil exclusion;
- no formal character introduction.

## 12. Planned artifact structure

`N21_REFERENCE_DELIVERY_BUNDLE_V001/`

- `delivery_manifest.json`
- `WORK_HANDOFF.md`
- `scene_authority/AST_IMG_000052__SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`
- `immediate_story_continuity/N20__N20_DO_NOT_TOUCH_THINGS_APPROVED_V001.png`
- `named_character_seeds/AST_IMG_000061__CHAR_SU_XIAOXIAO_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `named_character_seeds/AST_IMG_000058__CHAR_LIAO_JIAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `named_character_seeds/AST_IMG_000062__CHAR_WEN_QINGYA_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- `named_character_seeds/AST_IMG_000056__CHAR_GUANG_YONG_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Retention target:

`7 days`

Product Owner manual reference upload:

`0`

Transport:

`GitHub Actions → Artifact → Work automatic acquisition`

## 13. Builder contract

After Product Owner approval, create:

`production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V001.json`

Use existing fixed workflow only:

`.github/workflows/story-shot-reference-bundle-builder.yml`

Do NOT create an N21-specific Bundle builder workflow.

Build must fail closed unless all 6 references pass:

- canonical path;
- approval / lifecycle where applicable;
- byte size;
- SHA-256;
- Git blob;
- PNG signature;
- readable dimensions;
- byte-identical artifact copy;
- post-assembly revalidation.

Required output:

`PASS: 6/6 exact canonical reference binaries verified`

then:

`GENERATION_ALLOWED=TRUE`

## 14. Explicit exclusions

Do not include in V001:

- Ning Character Sheet;
- Jun Character Sheet;
- A03 binary;
- Neil Character Sheet;
- N19;
- N18;
- A07;
- mural-corridor references;
- any rejected N20 candidate;
- internet / non-canonical imagery;
- character sheets for the ten unnamed participants.

## 15. Current boundary

Current disposition:

`N21 REFERENCE DELIVERY BUNDLE DESIGN V0.1 = PRODUCT OWNER APPROVED / LOCKED / BUNDLE BUILD AUTHORIZED`

Authorized next:

- Bundle Spec creation;
- Generic Story Shot Reference Bundle Builder execution;
- 6/6 exact reference verification.

Still not authorized:

- Work generation before `GENERATION_ALLOWED=TRUE`;
- Candidate 02;
- N22;
- Story Shot publication / registration before Product Owner candidate approval.

## 16. Product Owner approval

On 2026-09-30, the Product Owner explicitly approved N21 Reference Delivery Bundle Design V0.1.

Authorized next:

1. create `production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V001.json`;
2. run `.github/workflows/story-shot-reference-bundle-builder.yml`;
3. independently verify the generated Artifact.

Work generation remains blocked until:

`GENERATION_ALLOWED=TRUE`


## 17. Build result

Bundle:

`N21_REFERENCE_DELIVERY_BUNDLE_V001`

Spec:

`production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V001.json`

Spec commit:

`a3058fe38b2fca462094fbe4df38b41e9ecf5b7b`

Generic builder:

`.github/workflows/story-shot-reference-bundle-builder.yml`

Workflow run:

`36669436051`

Job:

`109741045220`

Result:

`SUCCESS`

Builder verification:

`PASS: 6/6 exact canonical reference binaries verified`

Generation gate:

`GENERATION_ALLOWED=TRUE`

Artifact:

- name: `N21_REFERENCE_DELIVERY_BUNDLE_V001`
- Artifact ID: `11076819801`
- ZIP size: `6762818 bytes`
- digest: `sha256:a141ad98c50538c470901ef40ff7a9baa9e0ae8586703c6e82b617ad346308c1`
- expires: `2026-10-07T04:34:26Z`

Independent Chat verification:

- downloaded Artifact ZIP SHA-256 = GitHub Artifact digest: `MATCH`
- bundle_id: `MATCH`
- reference_count: `6`
- generation_allowed: `true`
- overall_result: `PASS`
- all six PNGs independently checked for byte size / SHA-256 / Git blob / PNG signature: `6/6 PASS`

Formal disposition:

`READY FOR WORK GENERATION / N21 CANDIDATE 01`


## 18. V0.3 suspension note

On 2026-09-30, before Work generation began, Product Owner required an Audience-Retention revision of S02-B from N21 onward.

The Artifact remains technically valid:

- `N21_REFERENCE_DELIVERY_BUNDLE_V001`
- 6/6 exact reference verification PASS
- Artifact ID `11076819801`

However, its existing Work handoff was authored for the pre-V0.3 single-shot N21 concept.

Disposition:

`VERIFIED ARTIFACT RETAINED / WORK GENERATION SUSPENDED`

Do NOT generate N21 Candidate 01 from this handoff until S02-B Director Shot Design V0.3 is Product Owner approved and the N21/N22 reference responsibilities are reassessed.
