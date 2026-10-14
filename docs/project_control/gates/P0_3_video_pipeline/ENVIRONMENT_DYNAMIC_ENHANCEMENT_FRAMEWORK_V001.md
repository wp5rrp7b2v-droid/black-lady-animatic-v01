# 《诡舍·黑衣夫人》｜环境动态增强框架 V001

Date: 2026-10-14
Authority: PO 已同意建立可复用环境动态方案，以 NEW-02 为第二个测试镜头。仅授权审核测试和受控落档；不授权修改已批准 Story Shot、V006 候选视频、正式 Video Index 或合并 main。

**状态：FRAMEWORK ACTIVE FOR CONTROLLED PILOTS；NOT AUTHORITY FOR AUTOMATIC BATCH APPLICATION。**

## 1. 目的

用已具备的 GitHub Actions / FFmpeg / Python Pillow+NumPy（必要时 Blender）在**不购买 AI 视频生成额度**的情况下，对已批准静态镜头进行受控、低幅度、局部环境动态增强。批准的 PNG 只读；独立渲染为候选审核 MP4。不要把静态人物加上灯光/浮尘误称人物在走动。

## 2. 模块登记

| ID | Module | 职责 | 当前状态 |
| --- | --- | --- | --- |
| M01 | CANDLELIGHT_BASELINE_V001 | 局部烛台与邻近墙面非同步轻微光变化，保持整体低调曝光 | **N23 技术 PASS + PO 视觉认可该效果**；迁移到别的镜头需重新审核 |
| M02 | SHADOW_BREATH_BASELINE_V001 | 局部阴影边缘细微渐变，严格限制在建筑区域 | 仅 DESIGN，未生成、未验证 |
| M03 | DUST_BASELINE_V001 | 少量靠近局部受光区域的慢速浮尘，不覆盖人物、不过密 | **NEW-02 待实验**；不是已批准的 baseline |
| M04 | HAZE_BASELINE_V001 | 建筑深处极弱空气层，保持清晰且不发灰 | 仅 DESIGN，未生成、未验证 |
| M05 | AMBIENCE_SOUND_BASELINE_V001 | 石质空间 room tone、轻微脚步/烛火等独立 SFX 通道 | 仅 DESIGN，未混入任何原声 |

登记机读配置：`production/environment_dynamic/module_registry_v001.json`。参数如 11/255 或某组遮罩坐标只是 **N23 基准测试的事实**，不是跨镜头直接套用的绝对通用阈值。

## 3. 统一工程接口

- `shot_id`, `source_canonical_path`, `source_sha256`, `source_git_blob`, `source_bytes`, `source_dimensions`：测试输入唯一身份。
- `enabled_modules`：逐镜头决定，不默认全选。
- `duration_seconds`, `fps`, `width`, `height`：输出规格。
- `effect_masks`：归一化的**建筑及光源白名单**、排除人物的遮罩；绝不简单整幅调亮。
- `intensity_cap`, `temporal_profile`, `seed`, `particle_budget`：效果强度、时间曲线与可复现随机源。
- `forbidden_zones`：人物、脸部、服装、门扇、主楼梯等局部动态保护区。
- `po_visual_status`, `technical_gate_status`, `source_immutability`：独立记录机器验证与 PO 感知评审，不把 MACHINE PASS 当成视觉批准。
- `render_script_version`, `artifact_sha256`, `output_git_blob`：复现与落档证据。

单镜头参数位于 `production/environment_dynamic/shot_profiles/`；通用渲染代码为 `scripts/environment_dynamic_render_v001.py`。

## 4. Stage A N23 烛光基准（历史事实）

- 原图：`production/image_library/approved/story_shots/N23_NEIL_AT_OPEN_DOOR_APPROVED_V001.png`，941×1672，2,697,400 bytes，SHA `2d94488e36d878ccb6ae7c3f9f3bf2a122eebca5ae01ad0e5b3105de4d535973`。
- 3 秒 / 90 帧 / 720×1280，无声，摄影机与人物不动。
- 原始渲染控制：非授权灯光区 RAW RGB 差异为 **0**，最大单通道变化 **11/255**；MP4 压缩并不意味着逐像素二进制无差异。
- GitHub 复现样片：`production/motion_tests/n23_candlelight_control_v001/N23_CANDLELIGHT_MOTION_CONTROL_TEST_V001.mp4`；SHA `6e8f7411cf40f957bd87c3b69a4304004501a1a6dd103900f574c047a6e830a4`。
- 源代码：`scripts/n23_candlelight_motion_control_test_v001.py`。
- GitHub Actions 构建 Run `38577595269` SUCCESS，独立精确核验 Run `38578211199` SUCCESS。
- PO 评价：「这个烛光的效果我觉得挺好的，满自然的」；`n23_stage_a_candlelight_motion_control_po_visual_approval_2026-10-14.md`。
- 该评价针对观看样片的自然度；不要伪称云端复现的每一个压缩字节由 PO 直接看过，也不要视作其他镜头的自动视觉通过。

## 5. NEW-02 第二次测试（本轮新授权）

- Shot：`S02B_V006_CROWD_INTERIOR_SIDE_DEPTH_TEST_01`，使用正式已批准原图 `production/image_library/approved/story_shots/S02B_V006_NEW02_CROWD_INTERIOR_SIDE_DEPTH_APPROVED_V001.png`，941×1672；1,963,410 bytes；SHA `d1866a667d7a24b8c5ae5b7670486b8b312e6f4a8fbce457763668e84d843bd4`，Git blob `d8feba3692ebe25afd0e51f5e3ab32358ea19ded`。
- 输出 **仅 1 × 4 秒、720×1280、30 FPS、120 帧、无音轨**的 M01 烛光 + M03 极轻浮尘审核 MP4。
- 烛台位置应独立根据 NEW-02 实景确认；只作用于受光建筑区域，人物和衣料的原始 RAW RGB 纹理必须不动；浮尘不得“飘雪”或占满画面，不叠加整片雾/曝光/镜头运动。
- 以受控配置将 candlelight / dust 两类贡献分别限定在不同遮罩，验证未经授权区域 RAW RGB 修改=0；单通道动态偏移受控并写入验证 JSON。
- 光变化从 0 起并回到 0，允许极弱不规则不同步起伏；浮尘运动可出现微小粒子穿行，但局限在无人物的建筑受光区域。
- 出片后**立即停止**，交 PO 判断 M01 迁移效果、M03 是否自然。未获得 PO 审批前不得批量实施 N24/A06 等镜头。

## 6. 验收门槛与禁止项

**技术门槛：** 原批准 PNG SHA/bytes/Git blob/尺寸匹配；唯一候选 MP4；90/120 帧准确、fps 与尺寸准确、完整解码通过；无人物/建筑形变；时域平缓；输出哈希、Git blob、证据 JSON 登记并独立复核。源 PNG 与正式视频 index 哈希不变。

**视觉门槛：** 阴暗压抑、无全局闪烁、不模糊发灰、烛光不过亮、浮尘极少且只在空间光内、没有机械或模板感；由 PO 观看完整镜头逐次决定。

**禁止：** 重编码/改写已批准 Story Shot PNG；整体提亮；全图随机噪点；同帧推拉、人工人物走路/变形；统一机械叠化；覆盖 V006 候选或正式视频；修改对白原声；自动升级 Module 状态到 PO APPROVED；未经授权 main merge。

## 7. 生命周期

Director/Framework Design → 单镜头参数校准 → GitHub Actions 仅 1 个试验 MP4 → 原图身份+渲染机器验收 → GitHub 审核分支备份 → 独立 Exact Verification → PO 视觉审批 → 锁定局部模块风格基线 → 待后续明确授权才集成到新一版视频。

**现阶段 M01（N23）视觉样式通过；M03（NEW-02）仍待视觉审核。V006 候选状态不改变。**
