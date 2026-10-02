# N22｜Scene Reference Design V0.1

Status: `PRODUCT OWNER APPROVED / LOCKED / BUNDLE DESIGN NEXT`

Date: 2026-10-02

Shot:

`N22｜People in the Flow — Ning Observational POV`

Director authority:

`N22 Node-Level Director Shot Design V0.1 / PRODUCT OWNER APPROVED + LOCKED`

Project state at design start:

`R185`

---

## 1. GOAL

Define the smallest authoritative visual-reference set that can support N22's approved function:

`POV + INFORMATION UPGRADE + NAMED CHARACTER SEEDING`

without reintroducing the N21 failure pattern of:

- crowd lineup;
- central-axis composition;
- over-organized blocking;
- monumental architecture;
- unnecessary main-character dominance;
- reference-content leakage.

N22 must preserve four named identities while remaining an observed fragment of a larger group.

---

## 2. SUCCESS

Scene Reference Design succeeds if it gives Work enough visual authority to establish:

1. Su Xiaoxiao identity;
2. Liao Jian identity;
3. Wen Qingya identity;
4. Guang Yong identity;
5. Castle Entrance / interior-transition scene identity;

while NOT forcing:

- exact character placement;
- exact four-person ensemble;
- exact pose;
- exact body direction;
- exact camera;
- exact N20 composition;
- exact N21 crowd composition;
- exact sixteen-person count.

---

## 3. EVIDENCE CLASS

### FACT

All four named characters have formal:

`APPROVED / CURRENT / resolver-eligible`

visual assets in the Asset Registry.

Each also has a formal Derived Character Reference Sheet:

- Su Xiaoxiao:
  - `AST_IMG_000061`
  - `CHAR_SU_XIAOXIAO_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
  - authority: `DERIVED`
  - resolver usage: `DEFAULT`
  - provenance: `COMPLETE`

- Liao Jian:
  - `AST_IMG_000058`
  - `CHAR_LIAO_JIAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
  - authority: `DERIVED`
  - resolver usage: `DEFAULT`
  - provenance: `COMPLETE`

- Wen Qingya:
  - `AST_IMG_000062`
  - `CHAR_WEN_QINGYA_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
  - authority: `DERIVED`
  - resolver usage: `DEFAULT`
  - provenance: `COMPLETE`

- Guang Yong:
  - `AST_IMG_000056`
  - `CHAR_GUANG_YONG_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
  - authority: `DERIVED`
  - resolver usage: `DEFAULT`
  - provenance: `COMPLETE`

Formal scene authority exists:

- `AST_IMG_000052`
- entity: `SCENE_CASTLE_ENTRANCE`
- role: `SCENE_MASTER`
- state: `DAY_DOOR_OPEN`
- approval / lifecycle: `APPROVED / CURRENT`
- provenance: `COMPLETE`

N20 is a canonical registered Story Shot and establishes:

- dim warm interior practical lighting;
- limited entrance-to-interior transition;
- no direct exterior sunlight flooding the characters;
- no full hall reveal.

N21 evidence shows that using visually rich continuity/group references can create:

- subject leakage;
- protagonist over-weighting;
- organized crowd flow;
- composition overconstraint.

### INFERENCE

The four Derived Character Reference Sheets are more appropriate than expanding into multiple Atomic views per character because:

- they already encode approved identity information;
- one sheet per named character reduces formal reference count;
- adding front/profile/rear assets individually would create unnecessary competing visual instructions.

### WORKING HYPOTHESIS

A five-reference Bundle consisting of four Character Reference Sheets plus the Castle Entrance Scene Master can preserve enough character identity and scene truth while leaving composition free enough to avoid a staged ensemble.

### UNKNOWN

- Whether four named identities remain sufficiently stable in one actual generation.
- Whether AST_IMG_000052 alone, combined with textual lighting constraints, is sufficient to reproduce the N20 warm low-key visual world.
- Whether a later targeted look-continuity reference will be needed after Candidate 01 evidence.

---

## 4. FORMAL GENERATION REFERENCE SET

Proposed formal reference count:

`5`

This is the maximum initial reference set for Candidate 01.

Do not add further references before real Candidate evidence.

---

### REF-01｜Su Xiaoxiao Character Reference Sheet

Reference ID:

`AST_IMG_000061`

Entity:

`CHAR_SU_XIAOXIAO`

Role:

`CHARACTER_REFERENCE_SHEET`

Canonical path:

`production/image_library/derived_reference_sheets/su_xiaoxiao/CHAR_SU_XIAOXIAO_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Expected SHA-256:

`e869d118e22e50cfe6e6280632da4534e660dc74ec96cf3871099b87cf42701a`

Expected byte size:

`700794`

Authority purpose:

- named-character identity;
- face / hair / overall approved normal-state appearance;
- feminine-presenting visual read;
- approved default clothing language.

Must NOT control:

- exact pose;
- exact shot angle;
- exact location;
- exact proximity to Liao Jian;
- glamour staging;
- future reveal information.

Priority:

`TIER 1 IDENTITY AUTHORITY`

---

### REF-02｜Liao Jian Character Reference Sheet

Reference ID:

`AST_IMG_000058`

Entity:

`CHAR_LIAO_JIAN`

Role:

`CHARACTER_REFERENCE_SHEET`

Canonical path:

`production/image_library/derived_reference_sheets/liao_jian/CHAR_LIAO_JIAN_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Expected SHA-256:

`3f2f01fea63401a3726abdf5053e75361d5d43091830ce8e1636883bd1cd6817`

Expected byte size:

`650562`

Authority purpose:

- named-character identity;
- face / hair / approved default appearance;
- fit young-man read;
- ordinary athletic body language.

Must NOT control:

- bodybuilding exaggeration;
- hero pose;
- exact proximity to Su Xiaoxiao;
- exact camera-facing angle.

Priority:

`TIER 1 IDENTITY AUTHORITY`

---

### REF-03｜Wen Qingya Character Reference Sheet

Reference ID:

`AST_IMG_000062`

Entity:

`CHAR_WEN_QINGYA`

Role:

`CHARACTER_REFERENCE_SHEET`

Canonical path:

`production/image_library/derived_reference_sheets/wen_qingya/CHAR_WEN_QINGYA_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Expected SHA-256:

`09551f02ad9cd4d3ae8e4483d017c230877165c4b88346ff9762527246569f0c`

Expected byte size:

`641800`

Authority purpose:

- named-character identity;
- approved normal-state appearance;
- round-frame-glasses / cultured read where naturally visible.

Must NOT force:

- full clean frontal face;
- equal prominence with Su / Liao;
- formal introduction staging.

Priority:

`TIER 2 IDENTITY AUTHORITY`

---

### REF-04｜Guang Yong Character Reference Sheet

Reference ID:

`AST_IMG_000056`

Entity:

`CHAR_GUANG_YONG`

Role:

`CHARACTER_REFERENCE_SHEET`

Canonical path:

`production/image_library/derived_reference_sheets/guang_yong/CHAR_GUANG_YONG_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`

Expected SHA-256:

`2a98e74ddba60a259758643b56ffddafd5a7cb30de040880f991fb47216b45fb`

Expected byte size:

`475761`

Authority purpose:

- named-character identity;
- shorter / slightly chubby human silhouette;
- approved normal-state appearance.

Must NOT force:

- clear frontal hero face;
- equal prominence with Tier 1 seeds;
- isolated introduction frame.

Priority:

`TIER 2 IDENTITY AUTHORITY`

---

### REF-05｜Castle Entrance Scene Master

Reference ID:

`AST_IMG_000052`

Entity:

`SCENE_CASTLE_ENTRANCE`

Role:

`SCENE_MASTER`

State:

`DAY_DOOR_OPEN`

Canonical path:

`production/image_library/scene_masters/castle_entrance/SCENE_CASTLE_ENTRANCE_SCENE_MASTER_DEFAULT_DAY_DOOR_OPEN_V001.png`

Expected SHA-256:

`d49af6a5e42d0867f2ffe4883e6af82f4d3777da3e96d788924cee2a9c743961`

Expected byte size:

`2305753`

Authority purpose:

- Castle Entrance identity;
- stone / entrance material facts;
- open-door state;
- entrance-to-interior world continuity.

Must NOT control:

- exact camera position;
- empty-scene composition;
- centered architecture;
- exterior-dominant daylight;
- full-hall reveal;
- monumental scale.

Priority:

`SCENE FACT AUTHORITY`

---

## 5. EXCLUDED FROM FORMAL GENERATION INPUT

### N20 Canonical Story Shot

Canonical:

`N20_DO_NOT_TOUCH_THINGS_APPROVED_V001.png`

Disposition:

`DIRECTOR CONTINUITY / LOOK REVIEW ONLY`

Do NOT include it in the first N22 Bundle.

Reason:

N20 is the correct immediate look-continuity evidence, but it contains Ning Qiushui + Jun Luyuan as dominant visible subjects.

N21 already supplied real evidence that using N20 directly as a generation reference can create:

- protagonist content leakage;
- over-weighted Ning / Jun presence;
- private-pair composition pressure.

For N22, that risk is unnecessary because Ning is only an optional edge POV cue and Jun is not required.

N20 therefore controls the written continuity standard:

- dim warm low-key interior;
- limited transition-zone scale;
- no direct daylight flooding;
- no full hall reveal;

but does not become a Candidate 01 image input.

---

### CHARACTER_VISUAL_STYLE_REFERENCE_V001

Disposition:

`NOT REQUIRED FOR N22 CANDIDATE 01`

Reason:

The four named Character Reference Sheets already carry approved named-character rendering.

Adding a generic style board creates another visual authority layer without solving a proven N22 problem.

Do not add pre-emptively.

Possible future use:

Only if Candidate 01 shows a clearly isolated general human-rendering style drift while named identity and composition otherwise succeed.

---

### N21_THRESHOLD_TRANSITION_ENVIRONMENT_REFERENCE_V001

Disposition:

`EXCLUDED / N21-SCOPED CONTROLLED REFERENCE`

Reason:

- formal authority scope is N21 threshold-transition environment;
- N22 must not silently broaden that authority;
- Candidate 08 evidence still showed monumental / central-axis environment drift despite the N21 controlled route;
- N22 has formal Scene Master authority already.

Do not reuse it as a positive N22 generation input.

---

### N21_CROWD_BODY_WARDROBE_REFERENCE_V001

Disposition:

`EXCLUDED`

Reason:

N22 is no longer an anonymous-body/wardrobe problem.

It is a named-character identity seeding shot.

The Human Body/Wardrobe Reference would introduce unnecessary generic-human pressure and could compete with the four named Character Reference Sheets.

---

### Ning Qiushui Character Reference

Disposition:

`NOT REQUIRED IN INITIAL BUNDLE`

Reason:

Ning's visible body is optional and limited to a cropped / soft edge POV cue.

If generated without Ning, the shot still satisfies the approved Director function through edit attribution.

Do not spend a formal identity reference on an optional edge element.

---

### Jun Luyuan / Neil references

Disposition:

`EXCLUDED`

Jun is not required.

Neil is specifically excluded from subject emphasis because N23 owns his directional action.

---

## 6. WHY FIVE REFERENCES, NOT MORE

Initial reference architecture:

`4 CHARACTER SHEETS + 1 SCENE MASTER`

This is deliberately minimal.

Do NOT add:

- Atomic front faces;
- Atomic profiles;
- rear 3/4 assets;
- N20;
- N21 group references;
- style board;
- additional scene screenshots;

before Candidate 01.

Reason:

The highest-risk assumption in N22 is not missing identity data.

It is whether the generation system can combine four named identities without turning the image into a posed ensemble or identity-collapse frame.

Increasing reference count before the first test would make that assumption harder—not easier—to diagnose.

---

## 7. LOOK CONTINUITY CONTRACT

Although N20 is not a formal image input, its approved look remains binding at Director / Work instruction level.

Candidate 01 must match:

- dim warm amber / tungsten interior practical lighting;
- low-key exposure;
- natural skin tones;
- restrained saturation;
- moderate cinematic contrast;
- textured blacks;
- no strong outdoor sunlight on bodies / floor;
- limited entrance-to-interior transition scale.

The Scene Master may establish architecture and open-door state but must not override this lighting contract.

Authority priority:

1. N22 Director Design → composition / narrative function;
2. Character Reference Sheets → named identities;
3. Scene Master → stable scene facts;
4. N20 approved look statement → continuity / lighting constraint.

---

## 8. CHARACTER REFERENCE USAGE CONTRACT

The four Character Reference Sheets are:

`IDENTITY AUTHORITIES`

They are NOT:

`CAST MEMBERS TO COPY INTO FIXED POSITIONS`

Work must explicitly decouple:

- reference panel position;
- panel pose;
- panel facing direction;
- body stance;
- spacing;
- left-right order;

from Candidate composition.

The Candidate must not reproduce a four-person board-like arrangement.

---

## 9. BLOCKING / COMPOSITION CONTRACT

N22 visual structure remains:

`OBSERVED GROUP FRAGMENT / NOT FOUR-PERSON CAST SHOT`

Target visibility:

- Su Xiaoxiao: comparatively readable;
- Liao Jian: comparatively readable;
- Wen Qingya: secondary / partial;
- Guang Yong: secondary / partial;
- additional unnamed guests: allowed as partial bodies / silhouettes / depth figures.

No fixed visible-person count.

No requirement that all four named faces be simultaneously fully visible.

Priority is:

`IDENTITY PRESERVATION + NATURAL GROUP FRAGMENT`

not:

`MAXIMUM FACE EXPOSURE`

---

## 10. CRITICAL ASSUMPTION

Unverified assumption remains:

`FOUR NAMED REFERENCE SHEETS CAN BE COMBINED WITHOUT ENSEMBLE STAGING OR IDENTITY COLLAPSE`

This Scene Reference Design does not claim that assumption is proven.

The first generation is the minimum proof.

---

## 11. MINIMUM PROOF / SCALE GATE

After later Bundle approval:

`1 × N22 Candidate 01`

Only one.

### PASS conditions

Reference strategy passes if Candidate 01 demonstrates:

1. Su Xiaoxiao identity materially preserved;
2. Liao Jian identity materially preserved;
3. Wen Qingya remains usable as secondary seed;
4. Guang Yong remains usable as secondary seed;
5. no four-person lineup / poster;
6. group fragment feels larger than the named four;
7. scene remains Castle Entrance transition;
8. N20 warm-low-key continuity is broadly maintained;
9. architecture remains subordinate;
10. Neil / Jun do not leak into the shot as unintended subjects.

### FAIL / DIAGNOSTIC branches

#### FAIL-A｜Identity collapse

If Tier 1 identity fails:

- do not add more characters;
- inspect whether Character Sheet needs targeted Atomic augmentation for that one character only.

#### FAIL-B｜Four-person poster / lineup

If identities are correct but staging becomes promotional / posed:

- reduce named-character count;
- preserve Su + Liao;
- keep only one Tier 2 readable seed;
- defer the other.

Do not solve by adding more references.

#### FAIL-C｜Look continuity fails

If identities and blocking pass but image becomes too bright / cold / tonally inconsistent:

- then consider one targeted look-continuity control derived from already approved evidence;
- do not immediately add N20 raw Story Shot without a separate authority/risk review.

#### FAIL-D｜Scene identity fails

If architecture no longer reads as Castle Entrance / transition:

- review Scene Master usage;
- do not introduce N21 environment reference automatically.

---

## 12. PROPOSED BUNDLE INPUT ORDER

If this Scene Reference Design is approved, N22 Bundle Design should preserve semantic grouping:

1. `identity_primary/AST_IMG_000061`
2. `identity_primary/AST_IMG_000058`
3. `identity_secondary/AST_IMG_000062`
4. `identity_secondary/AST_IMG_000056`
5. `scene_authority/AST_IMG_000052`

Reference order must not imply screen position.

Work handoff must explicitly say:

`REFERENCE ORDER ≠ CHARACTER LEFT/RIGHT ORDER ≠ BLOCKING ORDER`

---

## 13. CURRENT BOUNDARY

Current status:

`PRODUCT OWNER APPROVED / LOCKED`

Authorized next step:

- N22 Reference Delivery Bundle Design V0.1.

Still not authorized:

- Bundle Spec finalization / build execution;
- GitHub Actions build;
- Artifact;
- Work generation;
- Candidate 01;
- N23.

Approval authority:

`PRODUCT OWNER EXPLICIT APPROVAL IN CHAT / 2026-10-02`

Scene Reference approval does not authorize image generation.
