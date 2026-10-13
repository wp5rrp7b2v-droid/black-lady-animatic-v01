# S02-B｜宁秋水「夫人的要求」反应插镜｜Reference Delivery Bundle V001 Design V0.1

日期：2026-10-13

状态：**PRODUCT OWNER APPROVED / LOCKED 2026-10-13 / VALIDATION-ONLY 3/3 PASS / FORMAL BUILD NOT AUTHORIZED / NO WORK GENERATION**

## 0｜权限和来源

已批准的上级依据：
- Director Concept：`docs/project_control/gates/P0_3_video_pipeline/s02_b_ning_rule_reaction_editorial_insert_concept_2026-10-13.md`
- Scene Reference Design V0.1：`docs/project_control/gates/P0_3_video_pipeline/s02_b_ning_rule_reaction_scene_reference_design_v001_2026-10-13.md`

本文件仅把已批准 Scene Reference 转成可核验、可交接的 Bundle **设计**。Product Owner 的“开始下一步”授权推进设计审核，不默示允许 GitHub Actions 正式构建、Work 制图或发布注册。

## 1｜目标

- Bundle ID（拟定）：`TAIL_NING_REACTION_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001`
- Test-only target shot ID：`TAIL_NING_REACTION_TEST_01`（非 Story Shot 正式登记 ID）
- Sequence：`S02-B`
- Target Candidate：`TAIL_NING_REACTION_TEST_01 Candidate 01 / CLEAN GENERATION`
- 未来候选输出：**Exactly 1 × PNG**，941×1672，纵向影院风格静帧。
- 画面职责：在尼尔讲“这是夫人的要求”时，让宁秋水以独立的 3/4 中近景呈现细微的信息接收反应；下一切回已批准 N26 领队画面。
- 这不是 N26 改图、同图裁切、镜头替换或原音频修改。

## 2｜直接参考｜EXACTLY 3 / MAX 5

### 01｜宁秋水整体身份
- Reference ID：`AST_IMG_000060`
- source_type：`ASSET`
- entity_id：`CHAR_NING_QIUSHUI`
- role：`CHARACTER_REFERENCE_SHEET`
- asset_class：`DERIVED_REFERENCE`
- authority_class：`DERIVED`
- approval_status：`APPROVED`
- lifecycle：`CURRENT`
- resolver_usage：`DEFAULT`
- canonical_path：`production/image_library/derived_reference_sheets/ning_qiushui/CHAR_NING_QIUSHUI_CHARACTER_REFERENCE_SHEET_DEFAULT_DEFAULT_V001.png`
- expected_sha256：`15ec6c2682da0fe2502267bde21e9bc0bd7104bbf3e6041521121cc69a0e77be`
- expected_byte_size：`1123635`
- expected_git_blob：`b674733242ab5d603dc42c53b8f7582003064499`
- destination_group：`ning_global_identity`
- authority_purpose：面容家族、发型、年龄、身型与服装。参考板中的多图排列/站姿不作为构图参考。

### 02｜宁秋水左侧 3/4 脸
- Reference ID：`AST_IMG_000071`
- source_type：`ASSET`
- entity_id：`CHAR_NING_QIUSHUI`
- role：`FACE_3Q_LEFT`
- asset_class：`ATOMIC`
- authority_class：`AUXILIARY`
- approval_status：`APPROVED`
- lifecycle：`CURRENT`
- resolver_usage：`DEFAULT`
- canonical_path：`production/image_library/character_references/ning_qiushui/CHAR_NING_QIUSHUI_FACE_3Q_LEFT_DEFAULT_DEFAULT_V001.png`
- expected_sha256：`8d92bcc601220654499f7be57fc83411c57dedccc44e8f764cc65ce1b840334e`
- expected_byte_size：`1761408`
- expected_git_blob：`31cfa62e27233b2a955e3201d5a88f96ad1dc6c3`
- destination_group：`ning_face_identity`
- authority_purpose：脸部近景五官连续、自然 3/4 左侧表情；禁止变为对镜头正面摆拍或完全侧背。

### 03｜古堡入口内部内门厅
- Reference ID：`AST_IMG_000108`
- source_type：`ASSET`
- entity_id：`SCENE_CASTLE_ENTRANCE_INNER_LOBBY`
- role：`SCENE_MASTER`
- asset_class：`ATOMIC`
- authority_class：`MASTER`
- approval_status：`APPROVED`
- lifecycle：`CURRENT`
- resolver_usage：`CONDITIONAL`
- canonical_path：`production/image_library/scene_masters/castle_entrance_inner_lobby/SCENE_CASTLE_ENTRANCE_INNER_LOBBY_SCENE_MASTER_DEFAULT_DEFAULT_V001.png`
- expected_sha256：`f16d98a977eb73c75249cd3692ebfce9e3cd12cfbcbdb171d5b652149cb7c1a3`
- expected_byte_size：`2541370`
- expected_git_blob：`91471e32dab1c7b51b7e718ffd539305d81daf85`
- destination_group：`scene_inner_lobby`
- authority_purpose：内门厅建筑材料、局部纵深和低调暖光；不得将 4:3 空景直接作为 9:16 对称构图复刻。

**三张原图 Git blob 核对：2026-10-13 GitHub main 3/3 MATCH。** expected_sha256 / expected_byte_size 为已批准资产登记值；当前只核验 Git blob，尚未完成新的 PNG 二进制字节/SHA-256 运算；将由正式 Builder 在有授权的验证环节计算。

## 3｜邻接镜头核对边界｜N25 与 N26

- N25：`production/image_library/approved/story_shots/N25_RAIN_DAY_RULE_NEIL_ANSWERS_WITHOUT_TURNING_APPROVED_V001.png`，Git blob `8e523285a832496f1e316fd20737293668cf18db`。
- N26：`production/image_library/approved/story_shots/N26_LADYS_RULE_AND_FORWARD_MOTION_APPROVED_V001.png`，Git blob `a5ce429689a99437773385e25b9813745e380f74`。

2026-10-13：两张相邻正式资产通过 Git blob 复核；**并未直接读取其 PNG 像素进行独立视觉比较**，因此左右行进轴、机位侧别、宁秋水脸部当时朝向、背景相邻结构与曝光匹配均保持 **VISUAL REVIEW PENDING**。不可把“文件相同”写成“电影空间连续性已验证”。

本 Bundle 仅传递三张批准的身份/场景参考；相邻 N25/N26 不占 Work 直接参考名额，但必须在构建后、真正生成前由 Chat/Work 的实际画面核对流程审核。若三参考结构不足以保障正确机位，先提出 Scene Reference 修订并重新取得 PO 批准，而不是偷加第四张、第五张或自动生成。

## 4｜未来 WORK_HANDOFF 核心指令（设计稿）

1. 仅在 PO 明确授权且正式 Bundle manifest 3/3 字节/SHA/Git blob 全部通过时生成；读取 `delivery_manifest.json` 和 `WORK_HANDOFF.md`。
2. 一次仅生成 **Exactly 1 × PNG**，然后停止。Target size 941×1672。
3. 唯一第一视觉主体为宁秋水，使用 `AST_IMG_000060` + `AST_IMG_000071` 保证面容、衣着、比例与 3/4 左侧脸可读。
4. 以自然移动中的独立近景/中近景取代 N26 原有群像机位，不可把 N26 裁切/放大成新镜头。
5. 听到尼尔说“这是夫人的要求”时的短暂关注：眼神自然轻停、克制思索；不能演成惊恐、突然顿足、已猜透危险、瞪眼或夸张皱眉。
6. 身体保持自然、同一空间光照，宁秋水双手不得插袋；无背包、挎包、行李、背带等。
7. `AST_IMG_000108` 控制内门厅材料、空间深度、局部暖灯方向；暗调、低饱和、自然肤色、清晰无脏噪，不因人物近景而整体提亮。
8. 拍摄轴与背景建筑必须服从 N25→N26 实际画面视觉复核；如原图像素尚未核验或方向冲突，**STOP / DO NOT GENERATE**，不得自行推断一个“安全方向”。
9. 画面不出现古堡外、蓝天、雨、正在关闭的门、First Hall、壁炉、大楼梯、摄影棚灯光、抠图感。
10. 尼尔和君鹭远都不是必选入镜对象；不因为补人数而破坏宁秋水独立观察镜头的主语。
11. 原音频不裁切、不拉伸、不重复；精确插镜点通过后续局部 A/B 试剪对齐；当前静帧不声称具有嘴形动作。
12. 未经 PO 静帧批准不得追加第 2 张候选或进入剪辑母版修改。

## 5｜构建技术方案及授权边界

- 固定 Builder：`.github/workflows/story-shot-reference-bundle-builder.yml`（原有复用入口）。
- 脚本：`scripts/story_shot_reference_bundle_builder_v1.py`。
- 未来 Spec 路径（**尚未创建**）：`production/bundle_specs/TAIL_NING_REACTION_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001.json`。
- 未来必备 schema：`schema_version`, `bundle_id`, `target_shot_id`, `sequence_id`, `target_candidate`, `references`, `work_handoff`；含 `manual_product_owner_reference_upload: 0`, `max_direct_referenced_images: 5`, `build_authorized: false`。
- 技术注意：该 Builder 的 `push` 触发规则覆盖 `production/bundle_specs/*.json`。一旦创建 Spec（即使 `build_authorized:false`），也将自动开始 **validation-only Actions**。本轮尚无单独 Spec / Actions 授权，故**仅存设计文档，不创建 Spec，不触发 Actions**。
- 后续授权顺序：PO 审核 Bundle Design → 单独授权建立 validate-only Spec / 跑 3/3 校验（0 Artifact）→ 单独批准正式 Build / Artifact 完全一致性核验 → 在实际 N25/N26 空间与人物镜头视觉核对 PASS 后，单独授权 Work 生成唯一候选。
- 验证失败：有 SHA/size/blob 不一致，或实际镜头跨轴/风格连续性不成立时 STOP，查明原因；不可自动变更批准资产、增加参考图或生成。

## 6｜测试 Gate

**最关键工作假设：** 新机位的宁秋水克制反应提供实质新叙事信息，能使“夫人的要求”成为观看注意点，且不破坏已批准镜头的群体行进。

最小端到端证明：3/3 exact bundle → 1 PNG 视觉审核 → 一次 N25/反应/N26 局部原声 A/B → PO 对照判断。

- **PASS（技术参考）**：Builder 3/3 PNG SHA、bytes、Git blob、manifest 一致，并且 N25/N26 实际运动轴/背景连贯复核 PASS。
- **PASS（艺术/叙事）**：宁秋水身份不漂移、并非摆拍或同图裁切；PO 确认局部 A/B 相对现有 S02-B 对应片段更清晰、更自然、更有吸引力。
- **FAIL**：任一参考核验失败、图像身份/空间/光色/动作错误、跨轴、原音频语义错位或 PO 认为效果不优于现有。FAIL 不扩产。

## 7｜保持锁定

- `N25` / `N26` Approved Binary：UNCHANGED
- `N27` ABSORBED INTO `N26`：UNCHANGED
- `S02_B_ASSEMBLY_V001` 64.250 秒：APPROVED / CANONICAL / UNCHANGED
- `N16–N17 V004` 21.95 秒局部处理：APPROVED / UNCHANGED
- Tail V001 / V002：NOT APPROVED / ON HOLD
- `Video Index` / `Story Shot Index`：UNCHANGED
- P0.3：IN PROGRESS
- 本设计文件：**PRODUCT OWNER APPROVED / LOCKED 2026-10-13**

## 8｜2026-10-13 PO Approval & Validation-only Result

Product Owner explicitly approved this Bundle Design V0.1 and authorized ONLY creation of `build_authorized=false` Spec plus exact 3/3 validation. The previously prospective statements “尚未创建 Spec / 不触发 Actions” in section 5 describe the **pre-authorization design state** and are superseded by the recorded run below; they do not imply permission to build formally.

- Created Spec: `production/bundle_specs/TAIL_NING_REACTION_TEST_01_REFERENCE_DELIVERY_BUNDLE_V001.json` (flag remains `false`).
- Spec commit: `cd233e47d9af03b7464b9cebe67efee76162fd3a`.
- GitHub Actions Run: `38328900831` — completed / SUCCESS.
- Job: `115073876666` — `VALIDATION_PASS: 3/3 exact canonical references verified`.
- Job confirms `BUILD_AUTHORIZED=FALSE`, `GENERATION_ALLOWED=FALSE`.
- Bundle build/upload steps SKIPPED; Workflow Artifact count exactly **0**.
- Verification record: `docs/project_control/gates/P0_3_video_pipeline/s02_b_ning_rule_reaction_bundle_v001_validation_only_record_2026-10-13.md`.
- **Next Gate = PO FORMAL BUILD AUTHORIZATION ONLY; PO WORK IMAGE GENERATION NOT AUTHORIZED; N25/N26 image-pixel visual continuity remains unverified and must PASS before candidate generation.**
