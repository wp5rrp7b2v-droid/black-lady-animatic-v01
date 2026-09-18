# AO-06｜Stage 1｜A01–A07 Real Shot Selection + Fact Boundary Audit V0.1

Status: `READY_FOR_PRODUCT_OWNER_REVIEW`

Date: `2026-09-18`

Task: `AO-06｜Real Shot Spec Resolver + Shot-level Audit Reverse Trace`

## 1. Stage 1 purpose

选择一个真实、已批准的 A-Series Shot，作为 AO-06 后续：

`Shot Spec → Resolver → traceable Reference Package → generation/use record → USES_REFERENCE → reverse audit`

的唯一验证对象。

Stage 1 只做 Shot 选择与事实边界审核，不创建 Shot Asset、不创建 Costume/Prop Asset、不写 USES_REFERENCE、不执行 generation。

## 2. Candidate comparison

| Shot | AO-06 suitability | Reason |
|---|---|---|
| A01 | LOW | 16 人到达 + Entrance 建立，Character 规模过大，会把 Resolver/Audit 测试混入群体人物覆盖问题。 |
| A02 | MEDIUM | Neil 单人 + Castle Entrance + cross / white handkerchief 明确，适合 Costume/Prop，但对 multi-character Shot composition 覆盖不足。 |
| A03 | MEDIUM | Character + Castle Entrance state 明确，但关键 Costume/Prop 不是镜头核心。 |
| A04 | **RECOMMENDED** | 两个 Character + Castle Entrance + Neil costume/prop continuity；Schema V0.3 已以 A04 做过 Shot-bound Walkthrough；复杂度足够但仍可控。 |
| A05 | MEDIUM | 腰间/钥匙信息强，但属于 detail insert，Scene 与 Character identity 承载较弱；容易把“缺少钥匙”误建模成一个视觉 Prop Asset。 |
| A06 | LOW-MEDIUM | Door / stair continuity 强，主要验证 Scene State，不足以覆盖关键 Costume/Prop。 |
| A07 | MEDIUM | First Hall Scene Master 价值高，但 Costume/Prop 要求弱，接近重复 AO-03 Scene Resolver 验证。 |

## 3. Recommended canonical validation Shot

`shot_id = A04`

Legacy alias/history such as `A04_REBOOT` remains migration history only.

Schema V0.3 already locks the canonical Shot identity rule:

`A04_REBOOT → A04`

and uses A04 as the real Shot-bound walkthrough example.

## 4. Current formal runtime truth

Independent check against current Formal Asset Registry:

- total Formal Asset records: `62`;
- formal `SHOT` assets: `0`;
- formal `PROP_*` assets: `0`;
- formal `COSTUME_*` assets: `0`.

Therefore Stage 1 must not claim that A04 Shot Master, Neil costume, cross, or handkerchief already exist as formal runtime Asset records.

### Formal anchors already available

#### Character

- `AST_IMG_000060`
  - `CHAR_NING_QIUSHUI`
  - `CHARACTER_REFERENCE_SHEET`
  - `APPROVED / CURRENT / DEFAULT`

- `AST_IMG_000059`
  - `CHAR_NEIL`
  - `CHARACTER_REFERENCE_SHEET`
  - `APPROVED / CURRENT / DEFAULT`

#### Scene

- `AST_IMG_000052`
  - `SCENE_CASTLE_ENTRANCE`
  - `SCENE_MASTER`
  - state profile `DAY_DOOR_OPEN`
  - `APPROVED / CURRENT`

The existing Scene Resolver already proves:

`SCENE_CASTLE_ENTRANCE + {time_of_day=DAY, main_door=OPEN} → AST_IMG_000052`.

## 5. A04 proposed Shot fact boundary

### 5.1 Allowed narrative / continuity facts

The Stage 2 Shot Spec may encode:

- canonical Shot identity = `A04`;
- Characters present:
  - `CHAR_NING_QIUSHUI`
  - `CHAR_NEIL`;
- Scene identity:
  - `SCENE_CASTLE_ENTRANCE`;
- required Scene state:
  - `time_of_day = DAY`
  - `main_door = OPEN`;
- narrative action:
  - Ning Qiushui observes / directs attention toward Neil's waist area;
- Neil appearance continuity must preserve the already approved but not-yet-formalized costume/prop facts selected for this Shot, subject to explicit Stage 2 Entity/Asset handling.

### 5.2 Costume / Prop facts proposed for Stage 2

Proposed executable objects:

- `COSTUME_NEIL_DEFAULT`
  - Neil's default butler costume identity;
  - may carry required component `WHITE_POCKET_HANDKERCHIEF`.

- `PROP_NEIL_CROSS`
  - Neil's visible chest cross;
  - owner/context = Neil / default castle-host appearance.

These IDs are proposals for the Shot Spec model only at Stage 1.

They are **not formal Entities or Assets yet**.

Current resolver behavior for any `PROP_*` / `COSTUME_*` without eligible formal assets is correctly:

`REFERENCE_GAP`.

Stage 2 must decide whether AO-06 needs a minimal formal Costume/Prop representation or an explicitly approved safe evidence-carrier rule. It may not silently treat Character assets as Prop/Costume Masters.

### 5.3 Keys / absence boundary

Do **not** encode `PROP_NEIL_KEYS` or `KEYS_ABSENT` as a positive A04 reference requirement.

Reason:

- A04 narrative function is the observation toward Neil's waist;
- the empty key-position insert is the following A05 information beat;
- “absence of keys” is a negative continuity/narrative constraint, not a positive visual Prop Asset to resolve;
- if AO-06 later needs this fact, it belongs in a controlled `forbidden_presence / negative_continuity_fact` field, not as a fabricated Prop Master.

This prevents A04 from inheriting A05 facts or turning absence into a fake asset.

## 6. Scene Fact vs Shot Photography boundary

A04 must inherit the Scene identity/state but not the Scene Master's photography.

### Scene facts

May be inherited from `SCENE_CASTLE_ENTRANCE`:

- entrance spatial identity;
- main door / threshold / exterior-step topology where visible;
- current state `DAY_DOOR_OPEN`;
- stone entrance material identity.

### Shot photography

The following remain Shot-level variables and must not be inferred from Scene Master:

- camera position;
- exact shot size;
- focal length;
- exact Ning/Neil blocking coordinates;
- screen-left / screen-right placement;
- occlusion;
- depth of field;
- local exposure;
- composition.

If the approved A04 image is needed to lock these fields, Stage 2/3 must use the actual approved A04 source/evidence. Chat memory must not be converted into fabricated numerical camera metadata.

## 7. Why A04 is preferred

A04 is the smallest real Shot that simultaneously stresses the AO-06 system requirements without introducing unnecessary crowd complexity:

`2 Characters + 1 state-aware Scene + Neil Costume/Prop continuity + Shot-level use audit`.

It also exercises the exact Schema V0.3 rule that a multi-character Shot remains Shot-bound and its composition belongs in the Shot Spec rather than the filename or a single Character Entity.

## 8. Stage 1 acceptance questions

Product Owner approval should explicitly confirm:

1. `A04` is the canonical AO-06 validation Shot.
2. Scene requirement is `SCENE_CASTLE_ENTRANCE / DAY_DOOR_OPEN`.
3. Required Characters are `CHAR_NING_QIUSHUI + CHAR_NEIL`.
4. Neil default costume + cross / white handkerchief are valid AO-06 Costume/Prop continuity requirements, but currently remain formal runtime gaps.
5. A04 does not claim the A05 “keys absent” insert fact.
6. Shot photography is not inferred from Scene Master or chat memory; exact A04 photography must come from approved A04 evidence if required.

## 9. Stage 2 boundary

Only after Stage 1 approval should AO-06 proceed to:

`Stage 2｜A04 Real Shot Spec V0.1 + Resolver Contract`

Stage 2 must define:

- Shot Spec schema;
- required vs optional references;
- exact REFERENCE_GAP behavior;
- how Costume/Prop gaps are handled without fabricating assets;
- expected Reference Package;
- generation/use record schema;
- `USES_REFERENCE` direction;
- reverse-audit queries.

No D-069 is allocated by Stage 1.
