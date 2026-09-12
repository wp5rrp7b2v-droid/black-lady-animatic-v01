# P0.2-02｜Asset Naming Rules V1

Status: `LOCKED DESIGN RULE / IMPLEMENTATION NOT YET VALIDATED`

本文件定义《诡舍·黑衣夫人》Visual Asset Management System V1 的正式资产命名与永久 ID 规则。该命名规则已由 Product Owner 在 2026-09-12 当前 Chat 明确确认。

本规则不代表 P0.2 Gate 已通过；后续仍需完成 Entity / Asset Registry Schema、Automatic Ingest、Storage 与真实资产迁移验证。

## 1. 核心原则

资产永久 ID、Entity ID 与文件名承担不同职责，三者不得混用：

- `asset_id`：只负责永久唯一识别，不承担人物、角色、角度、版本等业务语义；
- `entity_id`：负责说明资产属于哪个稳定叙事对象；
- `filename`：负责提供人类可读的业务含义，并由系统根据 Registry metadata 自动生成。

文件改名、移动位置或切换 Storage 不得改变 `asset_id`。

## 2. Asset ID

统一格式：

`AST_<MEDIA_CODE>_<6-digit sequence>`

当前媒体代码：

- `IMG`｜Image / 静态图片
- `VID`｜Video / 视频
- `AUD`｜Audio / 音频
- `MDL`｜3D Model / 三维模型（未来如启用）
- `TEX`｜Texture / 材质纹理（未来如启用）

示例：

- `AST_IMG_000128`
- `AST_VID_000037`
- `AST_AUD_000012`

Reference Sheet 如果文件实体本身是图片，仍使用 `AST_IMG_*`；其业务职责由 `asset_class = REFERENCE_SHEET` 等 Registry 字段表达，不在 Asset ID 中重复编码。

Asset ID 由 Automatic Ingest 分配；Product Owner 不手工编号。

## 3. Entity ID

Entity ID 使用稳定、可读的业务前缀：

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

Entity ID 代表对象本身，不代表某张图片或某个版本。

## 4. Human-readable Filename

默认格式：

`<ENTITY_ID>_<ROLE>_<VARIANT>_V###.<ext>`

示例：

`CHAR_NING_QIUSHUI_PROFILE_RIGHT_DEFAULT_V003.png`

文件名中的：

- `ENTITY_ID` 来自 Entity Registry；
- `ROLE` 来自标准 Role vocabulary；
- `VARIANT` 来自受控 Variant vocabulary；
- `V###` 来自该 Entity + Role + Variant 下的版本序列。

文件名不得承担 Asset ID、审批状态、Lifecycle 状态或 Storage 地址的唯一事实源职责。

## 5. 禁止事项

正式资产不得：

- 使用 UUID、下载名、模型默认输出名作为正式生产文件名；
- 在文件名中依赖 `final`、`new`、`latest`、`good` 等非确定性词语；
- 把 `CURRENT / SUPERSEDED / DEPRECATED / ARCHIVED` 写死进文件名；
- 因移动目录或改变 Storage 而重新生成 Asset ID；
- 让 Product Owner 手工决定流水号、改文件名或登记 Asset ID。

## 6. Automatic Ingest 要求

Product Owner 批准资产后，系统应自动：

1. 判断 media type；
2. 分配 `AST_<MEDIA_CODE>_<sequence>`；
3. 读取 Entity / Role / Variant / Version metadata；
4. 生成标准文件名；
5. 写入正式 Storage；
6. 计算 hash；
7. 写入 Asset Registry；
8. 写入 Audit Trail。

命名错误应作为 Ingest 异常处理，而不是交给 Product Owner 手工修复。
