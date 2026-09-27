# P0.2-02｜Asset Naming Rules V1

Status: `LOCKED / IMPLEMENTED + VALIDATED / P0.2 PRODUCT OWNER APPROVED 2026-09-22`

本文件定义《诡舍·黑衣夫人》Visual Asset Management System V1 的正式资产命名与永久 ID 规则。基础规则由 Product Owner 于 2026-09-12 批准；2026-09-13 随 Entity / Asset Registry Schema V0.3 正式修订并再次纳入锁定基线。

本规则最初在 P0.2 Gate 内锁定；Automatic Ingest、Storage / canonical publication 与真实资产迁移随后已完成验证，P0.2 已于 2026-09-22由 Product Owner 明确批准。

## 0. Scope Clarification｜RC-025

本命名规则适用于 **Entity / Asset Registry 管理的 ATOMIC / DERIVED_REFERENCE / SHOT assets**。

P0.3 的 `STORY_SHOT` operational layer 是独立的叙事 / 剪辑索引层，当前由 RC-024 SOP 管理。已批准 N01–N10 的 Story Shot canonical filenames 不做追溯性重命名，也不因为包含 `APPROVED` 等 Story Shot 业务标记而被判定违反本文件。

边界：

- Asset Registry `SHOT`：继续使用 `<SHOT_ID>_<ROLE>_<VARIANT>_<STATE>_V###.<ext>`，不得包含 `approved / final / current / lock` 等状态词；
- P0.3 `STORY_SHOT`：当前 filename / canonical path 由 Story Shot SOP + Story Shot Index 管理；
- 两者不得静默互相转换。未来如把 Story Shot 迁入 Asset Registry，必须显式分配 Asset ID、生成本规则合规 filename，并记录 source mapping / SHA / provenance。
## 1. 核心原则

资产永久 ID、Entity / Shot ID 与文件名承担不同职责，不得混用：

- `asset_id`：永久唯一识别，不承担人物、角度、版本、审批或生命周期业务语义；
- `entity_id`：说明 Entity-bound Asset 属于哪个稳定叙事对象；
- `shot_id`：说明 Shot-bound Asset 属于哪个 canonical Shot；
- `filename`：提供人类可读业务含义，由系统根据 Registry metadata 自动生成。

文件改名、移动位置或切换 Storage 不得改变 `asset_id`。

## 2. Asset ID

统一格式：

`AST_<MEDIA_CODE>_<6-digit sequence>`

媒体代码：

- `IMG`｜Image / 静态图片
- `VID`｜Video / 视频
- `AUD`｜Audio / 音频
- `MDL`｜3D Model / 三维模型（保留）
- `TEX`｜Texture / 材质纹理（保留）

示例：

- `AST_IMG_000128`
- `AST_VID_000037`
- `AST_AUD_000012`

Derived Reference Sheet 如果文件实体本身是图片，仍使用 `AST_IMG_*`；其职责由 `asset_class = DERIVED_REFERENCE` 与 `role` 表达。

Asset ID 由 Automatic Ingest 分配；Product Owner 不手工编号。

## 3. Entity ID 与 Shot ID

Entity ID 使用稳定业务前缀：

- `CHAR_*`｜Character
- `SCENE_*`｜Scene
- `PROP_*`｜Prop
- `COSTUME_*`｜Costume

示例：

- `CHAR_NING_QIUSHUI`
- `CHAR_NEIL`
- `SCENE_FIRST_HALL`
- `PROP_NEIL_CROSS`
- `COSTUME_NEIL_DEFAULT`

Entity ID 代表对象本身，不代表某张文件或某个版本。

Shot-bound Asset 使用 canonical `shot_id`，例如 `A01 / A04 / A07`。历史 `A01_REBOOT / A04_REBOOT` 等仅保留在 Migration Mapping Manifest，不进入新的 canonical Shot ID。

## 4. Human-readable Filename

### 4.1 Entity-bound Asset

格式：

`<ENTITY_ID>_<ROLE>_<VARIANT>_<STATE>_V###.<ext>`

示例：

`CHAR_NING_QIUSHUI_PROFILE_RIGHT_DEFAULT_DEFAULT_V003.png`

### 4.2 Shot-bound Asset

格式：

`<SHOT_ID>_<ROLE>_<VARIANT>_<STATE>_V###.<ext>`

示例：

`A04_SHOT_MASTER_DEFAULT_DEFAULT_V001.png`

文件名中的：

- `ENTITY_ID / SHOT_ID` 来自正式 Registry / Shot Register；
- `ROLE` 来自按 `asset_class` 分组的受控 Role vocabulary；
- `VARIANT` 来自受控 Variant vocabulary；
- `STATE` 来自受控 State vocabulary；
- `V###` 来自同一 Entity/Shot + Role + Variant + State 下的版本序列。

把 `STATE` 纳入文件名是 Schema V0.3 的正式修订，用于避免不同 State 下同版本资产产生人类可读文件名冲突。

## 5. 多人物 Shot

Shot 文件名不写人物名称。

即使一个 Shot 中存在多个 Character，文件名仍只使用 canonical Shot ID，例如：

`A04_SHOT_MASTER_DEFAULT_DEFAULT_V001.png`

人物、Scene、Prop 等组成由 Shot Register / Shot Spec 表达；具体生成时实际使用的 Reference Asset IDs 通过 `USES_REFERENCE` 关系和 Audit Trail 记录。

## 6. 禁止事项

正式资产不得：

- 使用 UUID、下载名、模型默认输出名作为正式生产文件名；
- 在文件名中依赖 `final / new / latest / good / approved / current / lock / reboot` 等状态或历史流程词；
- 把 `CURRENT / SUPERSEDED / DEPRECATED / ARCHIVED` 写进文件名；
- 把多人物名单写进 Shot filename；
- 因移动目录或改变 Storage 而重新生成 Asset ID；
- 让 Product Owner 手工决定流水号、改文件名或登记 Asset ID。

## 7. Legacy Migration

旧文件名与旧 Shot ID 不直接覆盖新 canonical identity。

例如：

- legacy shot id：`A04_REBOOT`
- legacy filename：`A04_REBOOT_approved_v001.png`
- canonical shot id：`A04`
- canonical filename：`A04_SHOT_MASTER_DEFAULT_DEFAULT_V001.png`

Legacy identifier、legacy filename 与映射依据保留在 Migration Mapping Manifest，用于追溯。

## 8. Automatic Ingest 要求

Product Owner 批准资产后，系统应自动：

1. 判断 media type；
2. 分配 `AST_<MEDIA_CODE>_<sequence>`；
3. 读取 Entity / Shot / Role / Variant / State / Version metadata；
4. 生成标准文件名；
5. 写入正式 Storage；
6. 计算 hash；
7. 写入 Asset Registry；
8. 写入 Relations / Audit Trail。

命名错误应作为 Ingest 异常处理，而不是交给 Product Owner 手工修复。
