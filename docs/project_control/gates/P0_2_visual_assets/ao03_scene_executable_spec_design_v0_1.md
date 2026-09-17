# AO-03A｜Fact Boundary + Executable Spec Design V0.1

Status: `APPROVED / PRODUCT OWNER APPROVED 2026-09-15`

Project: `BLACK-LADY-001｜诡舍·黑衣夫人`

Gate: `P0.2｜人物锚定与 Scene Master 资产治理`

Task: `AO-03｜Scene Master Structured Facts + Scene/Costume/Prop/Variant Executable Spec`

## 1. Purpose

AO-03 的目标不是只登记两张 Scene Master 图片，而是建立 Scene / Costume / Prop / Variant / State 的可执行生产模型，使后续 Shot / Task Spec 与 Reference Resolver 可以稳定读取并校验场景状态，避免依赖人工记忆或在镜头中静默漂移。

## 2. Core boundary

Scene Master 锁定 `Scene Facts`，不锁死单个 Shot 的摄影表现。

### 2.1 Scene Facts｜必须继承

至少包括：

- 空间拓扑 / 房间结构；
- 固定建筑元素；
- 固定关键物件及其位置关系；
- 已锁定连续性状态；
- 核心材质与建筑身份。

### 2.2 Shot Photography｜允许变化

至少包括：

- camera position；
- shot size；
- focal length；
- character blocking；
- occlusion；
- depth of field；
- local exposure；
- composition。

不得把 Scene Master 当前图片的摄影机位置、景别或构图误登记为稳定 Scene Fact。

## 3. Scene identity and state separation

历史工作名称将 Scene identity 与当前状态混在同一标签中。新体系必须分离 Stable Scene Entity 与受控 State Profile。

### 3.1 Castle Entrance

- Stable Scene Entity: `SCENE_CASTLE_ENTRANCE`
- Asset Role: `SCENE_MASTER`
- Variant: `DEFAULT`
- Current State Profile: `DAY_DOOR_OPEN`
- Confirmed state dimensions:
  - `time_of_day = DAY`
  - `main_door = OPEN`
- Legacy/source alias retained for traceability: `CASTLE_ENTRANCE_OPEN_DOOR_DAY`

### 3.2 First Hall

- Stable Scene Entity: `SCENE_FIRST_HALL`
- Asset Role: `SCENE_MASTER`
- Variant: `DEFAULT`
- Current State Profile: `FIREPLACE_EXTINGUISHED`
- Confirmed state dimensions:
  - `fireplace = EXTINGUISHED / NOT_BURNING`
- Legacy/source alias retained for traceability: `FIRST_HALL_FIREPLACE`

State change does not create a new Scene identity. Example: `SCENE_CASTLE_ENTRANCE + NIGHT + DOOR_OPEN` or `SCENE_FIRST_HALL + FIREPLACE_BURNING` remains the same Scene Entity with a different controlled State Profile.

If the requested controlled state has no eligible formal asset, Resolver must return `REFERENCE_GAP`; it must not silently reuse a mismatched Scene Master.

## 4. Executable Scene Spec structure

AO-03 adopts a `State Profile + multidimensional facts` model rather than storing one opaque state string only.

Minimum structure:

```text
scene_id
scene_name

stable_facts
├─ spatial_topology
├─ fixed_architecture
├─ key_objects
├─ object_relationships
└─ core_materials

state_profile
├─ profile_id
├─ time_of_day
├─ weather
├─ door_state
├─ fireplace_state
└─ other_continuity_states

shot_variable_fields
├─ camera_position
├─ shot_size
├─ focal_length
├─ character_blocking
├─ occlusion
├─ depth_of_field
├─ local_exposure
└─ composition

source_master_asset_id
evidence
status
```

The implementation may use JSON / Registry records, but the semantic boundary above is authoritative.

## 5. Variant vs State

`variant` and `state` remain separate as required by Registry Schema V0.3.

- Variant = relatively stable design difference.
- State = temporary / continuity-sensitive production condition.

DAY/NIGHT, door OPEN/CLOSED, fireplace EXTINGUISHED/BURNING and similar continuity facts must be controlled State dimensions. They may not drift silently inside Shot generation.

## 6. Costume / Prop executable rule

AO-03 establishes executable rules for Costume and Prop, but must not fabricate formal assets merely to fill Registry fields.

### Costume

```text
COSTUME Entity
→ Costume Master
→ variant
→ state
→ placement / required_components
```

### Prop

```text
PROP Entity
→ Prop Master
→ scale
→ state
→ placement / owner / context
```

If a Shot Spec requires a Costume / Prop reference that has no eligible formal asset, Resolver returns `REFERENCE_GAP` unless an explicitly approved rule permits a safe alternative. Missing assets must not be represented as completed assets.

## 7. AO-03B｜Two Scene Master Structured Facts Definition

Status: `APPROVED / PRODUCT OWNER APPROVED 2026-09-17`

### 7.1 SCENE_CASTLE_ENTRANCE

```text
scene_id       = SCENE_CASTLE_ENTRANCE
scene_name     = 古堡主入口
asset_role     = SCENE_MASTER
variant        = DEFAULT
state_profile  = DAY_DOOR_OPEN
time_of_day    = DAY
main_door      = OPEN
legacy_alias   = CASTLE_ENTRANCE_OPEN_DOOR_DAY
```

#### Stable facts

- `spatial_topology`
  - 古堡内部入口空间通过主门与外部连接；
  - 门槛之外立即进入向下延伸的石质台阶；
  - 台阶进一步连接外部庭院 / 道路；
  - 更远处为树林环境。
- `fixed_architecture`
  - 古堡主入口；
  - 大型双开主门；
  - 门槛；
  - 外部石质台阶。
- `key_objects`
  - 当前无必须独立建模的可移动关键物件。
- `object_relationships`
  - 主门位于内外空间交界；
  - 石阶从门槛外开始向下；
  - 石阶之后连接庭院 / 道路；
  - 树林位于更远外部环境。
- `core_materials`
  - 石质入口建筑体系；
  - 石质门槛 / 台阶。

Visual evidence may record no visible precipitation, but AO-03B does not invent a new weather enum. Weather remains unspecified until implementation vocabulary is explicitly defined.

### 7.2 SCENE_FIRST_HALL

```text
scene_id         = SCENE_FIRST_HALL
scene_name       = 古堡第一大厅
asset_role       = SCENE_MASTER
variant          = DEFAULT
state_profile    = FIREPLACE_EXTINGUISHED
fireplace_state  = EXTINGUISHED
fire_visible     = FALSE
legacy_alias     = FIRST_HALL_FIREPLACE
```

#### Stable facts

- `spatial_topology`
  - 一个完整的古堡室内生活大厅；
  - 大厅存在主要生活 / 停留区域；
  - 通过一个拱形通道继续连接更深的古堡内部空间。
- `fixed_architecture`
  - 大型石质壁炉；
  - 石质墙体；
  - 深色木质天花；
  - 通往更深内部空间的拱形通道。
- `key_objects`
  - 扶手椅；
  - 小边桌；
  - 书柜及书籍；
  - 地毯。
- `object_relationships`
  - 扶手椅与壁炉形成相邻生活区；
  - 小边桌属于该座椅区域；
  - 书柜 / 书籍位于大厅内部；
  - 地毯定义主要生活空间；
  - 拱形通道连接大厅与更深古堡内部空间。
- `core_materials`
  - 石材为主要墙体及壁炉材质；
  - 深色木材构成主要天花体系。

Fireplace continuity is strict: no burning flame and no visual interpretation of an actively burning fireplace is allowed under the current `FIREPLACE_EXTINGUISHED` State Profile.

### 7.3 Coordinate and photography exclusion rule

The following are not Scene Facts even when visible in a Scene Master:

- current image left / right position;
- camera position or viewing direction;
- shot size;
- focal length;
- character presence or blocking;
- foreground occlusion;
- depth of field;
- local exposure;
- composition.

Relationships must be stored semantically, e.g. `armchair adjacent_to fireplace` and `arched_passage connects first_hall to deeper_castle_interior`, not as screen-coordinate statements such as `fireplace = left` or `archway = right`.

## 8. AO-03 Definition of Done

AO-03 is COMPLETE only when all of the following are verified:

1. `SCENE_CASTLE_ENTRANCE` and `SCENE_FIRST_HALL` stable Scene Entities exist in the executable model.
2. The two approved Scene Masters are formally mapped to the new Scene Entities while preserving legacy/source aliases for traceability.
3. Both Scene Masters have structured separation of `Scene Fact / State Fact / Shot Photography`.
4. Executable Scene / Costume / Prop / Variant / State Profile specification is implemented.
5. Resolver can read `scene_id + required_state`; mismatched or absent controlled state returns `REFERENCE_GAP`.
6. At minimum the following machine-verifiable cases pass:
   - Castle Entrance + DAY + OPEN → current eligible Scene Master.
   - Castle Entrance + CLOSED → `REFERENCE_GAP`.
   - First Hall + FIREPLACE_EXTINGUISHED → current eligible Scene Master.
   - First Hall + FIREPLACE_BURNING → `REFERENCE_GAP`.

## 9. Runtime implication

Current runtime implementation is Character-only. Existing resolver source validation is fixed to `CHAR_*` and `production/image_library/character_references`.

Therefore AO-03 cannot close by documentation-only registration. Runtime support must be extended so Scene assets and required state matching can participate in resolver decisions without weakening existing Character behavior.

## 10. Execution split

- `AO-03A` = Fact Boundary + Executable Spec Design V0.1 — **APPROVED 2026-09-15**.
- `AO-03B` = Two Scene Master Structured Facts Definition — **APPROVED 2026-09-17**.
- Following implementation step = create / extend Registry + resolver runtime + validation tests based on approved AO-03A/B contract.

No P1 Wave 2 production resumes until AO-03 through AO-06 closeout conditions are satisfied.
