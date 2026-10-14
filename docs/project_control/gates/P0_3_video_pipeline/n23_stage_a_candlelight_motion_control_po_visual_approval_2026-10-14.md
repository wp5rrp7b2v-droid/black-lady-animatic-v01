# 《诡舍·黑衣夫人》｜N23 Stage A 烛光微动态｜Product Owner 视觉审批

日期：2026-10-14
状态：**STAGE A CONTROL EFFECT PO VISUAL APPROVED / TECHNICAL EXACT PASS / NO N23 REPLACEMENT / NO V006 VIDEO CHANGE**

## PO 明确反馈
Product Owner 在观看 3 秒 N23 烛光动态样片后表示：

> “这个烛光的效果我觉得挺好的，满自然的”

该评价确认为：**Stage A 的“局部烛光微弱动态表现”在当前 N23 镜头下视觉通过，作为后续环境动态试验可复用的风格与幅度基准**。

本次不代表：
- PO 已批准 Stage B 尼尔或诡客真实人物动画；
- PO 已批准 N23 动态视频替换现有正式 Story Shot PNG；
- PO 已批准将微动态插入 V006 候选视频；
- PO 已批准修改既有音频、视频母版、正式 Video Index 或合并 main；
- 参数已在其他场景/光源得到验证。

## 锁定样片身份

- N23 批准原图：`production/image_library/approved/story_shots/N23_NEIL_AT_OPEN_DOOR_APPROVED_V001.png`
- 原图 SHA-256：`2d94488e36d878ccb6ae7c3f9f3bf2a122eebca5ae01ad0e5b3105de4d535973`
- 原图 Git blob：`649ed97addf97f126a05e12d43325720a624ea19`
- 经 PO 视觉认可的 Stage A 样片（GitHub 云端复现版本）：`production/motion_tests/n23_candlelight_control_v001/N23_CANDLELIGHT_MOTION_CONTROL_TEST_V001.mp4`
- GitHub 云端 MP4 SHA-256：`6e8f7411cf40f957bd87c3b69a4304004501a1a6dd103900f574c047a6e830a4`
- Git blob：`accb833152ee68e687c67558dae8f21c8d7f72f3`
- 3.000 秒 / 30 FPS / 90 帧 / 720×1280 / 无声音。
- 技术证据：`production/motion_tests/n23_candlelight_control_v001/N23_CANDLELIGHT_MOTION_CONTROL_TEST_V001_EVIDENCE.json`
- 渲染脚本：`scripts/n23_candlelight_motion_control_test_v001.py`
- 生产运行：GitHub Actions `38577595269` SUCCESS。
- 独立确证运行：GitHub Actions `38578211199` SUCCESS。
- 源 N23 和 V006 视频候选二进制均未被更改。

注：此前对话中提供的本地 MP4 预览与 GitHub 云端复现版由同一技术方法产生，但可能因编码环境不同而具有不同的文件 SHA。PO 的自然度评价来源于对话中播放的样片；本记录对云端版本标示为**同设计复现的已核验文件**，而非宣称 PO 已逐字节审阅云端 MP4。

## 已通过的可复用视觉标准

1. **局部而非全画面闪烁**：暖光只在烛台与邻近墙面形成微弱的明暗起伏，不提高整幅曝光。
2. **变化平缓、非机械规律闪烁**：不同小区域不同步，持续变化、没有明显亮度跳变。
3. **保留 N23 阴暗压抑氛围**：石墙、人物和门的结构、位置保持不变；不因动态化将古堡变亮。
4. **技术参数仅作为 N23 基准**：本版编码前 RAW RGB 最大单通道亮度变化 `11/255`，指定灯光区外变化像素数 `0`；如迁移到其他镜头，须重新依据烛光与人物遮挡设计局部范围，不可机械复制遮罩坐标。
5. **烛光动态不等于人物动态**：Stage B 的真实步态、尼尔自然轻微头部/视线运动尚未实现，不得以视觉通过的 Stage A 冒充全片动画技术通过。

## 下一步

优先利用既定 `n23_people_and_neil_micro_motion_stage_b_work_test_handoff_v0_1_2026-10-14.md` 进入真实人物动作单镜头试验。每轮最多一条独立 MP4，严格禁止改变已批准的 N23 原 PNG、身份、门的位置、阴暗光线、V006 候选母版。当前连接的 Runway 工作空间没有可用视频生成模型，Stage B 尚未制作，必须先确认独立可执行的视频生成路径。

**Gate disposition: N23 STAGE A VISUAL EFFECT APPROVED / RECORD CLOSED; N23 FULL MOTION NOT YET APPROVED.**
