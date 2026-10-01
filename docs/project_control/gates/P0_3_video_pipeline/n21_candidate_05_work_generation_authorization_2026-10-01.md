# N21 Candidate 05｜Work Generation Authorization

Date: 2026-10-01

Status:

`PRODUCT OWNER AUTHORIZED / WORK GENERATION ALLOWED / ONE PNG ONLY / REVIEW REQUIRED`

Shot:

`N21｜Cohort Enters — Into the Unknown`

Candidate:

`N21 Candidate 05｜Clean Regeneration`

## 1. Product Owner authorization

Product Owner explicitly authorized:

`START N21 CANDIDATE 05`

This authorizes Work to generate exactly one Candidate 05 PNG from the verified V004 Bundle.

It does not authorize:

- Candidate 06;
- N22;
- canonical publication;
- Story Shot registration;
- Asset Registry modification;
- Project Control modification by Work;
- merge.

## 2. Formal Bundle

Repository:

`wp5rrp7b2v-droid/black-lady-animatic-v01`

Bundle:

`N21_REFERENCE_DELIVERY_BUNDLE_V004`

Workflow Run:

`36826967264`

Job:

`110254694293`

Artifact ID:

`11145497260`

Artifact size:

`3596063 bytes`

Artifact digest:

`sha256:0b3227f30d8156ed7be3f421f5b43d9233aba4fc609dedd09d76f4f1dc0ea27d`

Spec:

`production/bundle_specs/N21_REFERENCE_DELIVERY_BUNDLE_V004.json`

Spec revision:

`V004-R3`

Formal Build result:

`2/2 EXACT VERIFIED / GENERATION_ALLOWED=TRUE`

Manual Product Owner reference upload:

`0`

Historical Artifact `11144634603` is explicitly forbidden:

`DO NOT USE`

## 3. Required Work preflight

Work must automatically acquire Artifact `11145497260`.

Before generation, independently verify:

- ZIP digest matches the formal Artifact digest;
- `delivery_manifest.json` exists;
- `reference_count = 2`;
- `all_reference_checks_pass = true`;
- `generation_allowed = true`;
- both PNGs exact-match manifest SHA / bytes / Git blob / dimensions.

Any mismatch:

`STOP / DO NOT GENERATE`

## 4. Two formal image inputs only

### REF-01｜Scene authority

`AST_IMG_000052`

Use only for:

- castle entrance architecture;
- stone material;
- open-door threshold fact;
- entrance-to-interior spatial continuity.

Do not copy exact camera, crowd placement or shot composition.

### REF-02｜Character visual-style authority

`CHARACTER_VISUAL_STYLE_REFERENCE_V001`

Use only for:

- realistic adult human rendering;
- skin treatment;
- hair realism;
- believable adult proportions;
- restrained clothing / fabric material rendering.

Do not copy:

- any panel as a specific character;
- a complete outfit;
- panel layout;
- pose;
- group arrangement;
- scene composition.

## 5. Candidate 05 image task

Generation mode:

`CLEAN REGENERATION`

Do not edit or use Candidate 01–04 as an image input.

Output:

`1 × PNG / 9:16 vertical`

Core visual statement:

`一群参与者正在从古堡入口跨入一个更黑暗、更未知、具有潜在危险感的内部空间。`

First read must be:

`进入未知`

not:

- showing all 16 people;
- showing named protagonists;
- a group portrait.

Approximately 4–6 relatively readable people are sufficient. The remaining cohort may be implied through crop, occlusion, partial bodies, silhouettes, deeper figures and off-frame continuation.

Movement should feel naturally distributed rather than queued or synchronized.

The interior must remain an entrance / transition zone. Do not reveal a complete First Hall.

Unknown / danger feeling should come from:

- reduced visibility deeper inside;
- architectural occlusion;
- light falloff;
- spatial compression;
- incomplete information.

Do not rely on fantasy fog, monsters, blue game-horror lighting or exaggerated supernatural effects.

## 6. Hard visual gate

Visible people must remain inside the established Black Lady human-rendering language.

Hard FAIL if there is obvious:

- generic AI crowd-face look;
- game-NPC rendering;
- plastic skin;
- fashion-advertising polish;
- body / posture error;
- direct copying of a Style Board person or clothing configuration.

Ning Qiushui and Jun Luyuan are not mandatory identity targets in this shot and must not be intentionally centered as a hero pair.

## 7. Stop condition

After generating the single PNG, Work must report:

- actual dimensions;
- Bundle verification result;
- visible-person estimate;
- whether the first read is “进入未知”;
- character visual-style stability;
- whether any Style Board content appears copied;
- crowd movement naturalness;
- whether full First Hall was avoided;
- `Ready for Product Owner review: YES / NO`.

Then stop.

Do not generate another candidate automatically.

## 8. Current governance

`N21 Candidate 05 = AUTHORIZED FOR ONE WORK GENERATION ONLY`

RISK-003 remains ACTIVE until Product Owner reviews the actual generated image.

N22 remains:

`NOT STARTED`
