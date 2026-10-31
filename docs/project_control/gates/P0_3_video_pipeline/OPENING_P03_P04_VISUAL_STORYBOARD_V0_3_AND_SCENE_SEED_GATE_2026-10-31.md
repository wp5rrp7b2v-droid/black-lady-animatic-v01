# Opening P03–P04 V0.3｜三张候选授权与缺失场景的首张验证方案

日期：2026-10-31　状态：**V0.3 STORY STRUCTURE PO APPROVED / 3 PNG CANDIDATES AUTHORIZED / P03-A FIRST SCENE-SEED BUNDLE BUILD AUTHORIZED / P03-B/C STILL BLOCKED BY SCENE VISUAL GATE**

## 一、为什么不能直接将三张候选同时交给 Work

Work 基于 main `62a986e` 核查了 `SCENE_GHOST_HOUSE_THIRD_FLOOR_BLOOD_DOOR` 缺少 Approved 场景 PNG、规划的 `OPENING_P03_P04_BLOOD_DOOR_STORY_SHOT_REFERENCE_DELIVERY_BUNDLE_V001` 无正式验证 Artifact，依据最初指令 fail closed，**未出任何图**。此结果为符合治理的发现，不是 Work 的图像模型 FAIL。

PO 已批准 V0.3 三图：P03-A 建立、P03-B 任务、P04-C 两条提示，以及总数量 3×941×1672 PNG。新目标不是额外制作第四张场景图。

**调整为渐进式授权链：**第一张 `P03-A Candidate 01` 同时承担新诡舍血门场景的 Scene Seed，利用已验证的人物 Reference＋小说文字事实生成候选；PO 先审其门体、诡舍空间及人物一致性。只有 PO 认为该张足以担任连续性场景依据，Chat 才能 Exact Binary 核验其文件并把对应受控场景参考注册为 Approved，然后构建用于 P03-B/C 的正式 Bundle，二者才可以在同一门体基础上制作。这样仍为三张候选，没有额外场景图。

## 二、三个正式镜头的设计基线

| 镜头 | 主体 | 视觉职责 / 禁止事项 | 审核 Gate |
|---|---|---|---|
| P03-A | 诡舍三楼关闭的真实木质血门＋宁秋水与君鹭远后侧自然错位 | 先建立这是承载规则的真实木门，门体/木纹/门框几何清晰可见，血字存在但无须读全 | 第一个产生；PO 审其图像与作为共享场景种子的适用性 |
| P03-B | 同一门的任务区域近景 | 精确呈现“在莫妮卡夫人的庄园中活过五日并找到离开庄园的大门钥匙”，不能变成古堡大门钥匙 | 依赖 P03-A approved scene anchor / Bundle |
| P04-C | 同一门的两条提示近景 | 清楚呈现“提示1：不要淋雨”“提示2：不要长时间和它对视”，不能揭示‘它’ | 依赖同一 door scene anchor / Bundle |

T01 引用现有已批 Opening V001 前6.55秒尼尔欢迎（晴朗），40.260秒音轨已经 PO Approved，二者不需要重制。

## 三、P03-A 起步引用哪些 Approved 参考

**只传四张具有正确权限的身份图：**
- `AST_IMG_000060` 宁秋水完整人物参考（CHARACTER_REFERENCE_SHEET）
- `AST_IMG_000057` 君鹭远完整人物参考（CHARACTER_REFERENCE_SHEET）
- `AST_IMG_000071` 宁秋水 3/4 左脸方向辅助
- `AST_IMG_000072` 君鹭远 3/4 左脸方向辅助

均为 GitHub Asset Registry APPROVED/CURRENT；四张的具体 SHA、Git blob 与文件大小写入 `production/bundle_specs/OPENING_P03A_BLOOD_DOOR_SCENE_SEED_REFERENCE_DELIVERY_BUNDLE_V001.json`，由通用 GitHub Actions builder 做真正二进制检查。这里只能证明这四张既有图是正确引用，**不能把它称为血门场景图的 exact verification**。

诡舍三楼血门场景尚无 Approved 布景输入，这不是首张 Scene Seed 的循环前提：新场景本身是首次待审的 RECONSTRUCTED VISUAL DESIGN。PO 需凭真实出图决定是否接受材质、门扇结构、门框、锁具和环境。若不接受，P03-A 停止并返工，不得转入 P03-B/C。

**不使用** `AST_IMG_000105` 艾伦古堡入口、`AST_IMG_000107` 庄园大门、第三层肖像走廊等去冒充诡舍三楼的建筑几何；它们仅是区分地点的事实背景。

## 四、Bundle 步骤

1. Chat 创建 `production/bundle_specs/OPENING_P03A_BLOOD_DOOR_SCENE_SEED_REFERENCE_DELIVERY_BUNDLE_V001.json`，仅为 P03-A Scene Seed 的 4 张已批准人物 Reference；`build_authorized=true` 代表允许 GitHub Actions 做 P03-A 专用 Bundle 构建，不代表任何场景 Master 或候选获得 PO 批准。
2. 由既有 `.github/workflows/story-shot-reference-bundle-builder.yml` 触发，执行 registry/path/byte-size/SHA-256/Git blob/PNG dimensions 和最终复制 exact validation，保留 Actions run 与 artifact ID。**必须看到真 PASS** 才可交 Work。
3. Work 只生一张 `OPENING_P03A_BLOOD_DOOR_ESTABLISH_CANDIDATE_01.png`，完成后停止。它是三图中的第一张，不是额外 Scene Master。
4. PO 看实图，**同时**确认 P03-A 镜头感与血门场景连续性是否可作为后两图唯一 seed。无 PO PASS 则不得登记为 Approved Scene Reference。
5. PO PASS 后，Chat 执行 Exact Binary Verification / controlled reference publication，重新建立包含已批 P03-A/Scene Seed 的 P03-B/C Bundle 并调用 GitHub Actions 验证；Work 生成剩余两张，不得无视同门/同木纹连续性。

## 五、PASS / FAIL

第一轮 PASS：P03-A 是 941×1672 PNG，人物身份不漂移；木门完全关闭，结构真实、门体在镜头中清楚可定位、门上有自然血字痕迹；诡舍三楼而非庄园/古堡；PO 认可能作为后续共享门体/灯光/环境锚点；二进制来源有真实文件校验。
第一轮 FAIL：人物错误、门不完整/木纹不连贯、场景误用、血字悬浮/乱码过多影响场景判断、PO 否认场景种子一致性；停止扩展，不伪造 Approved scene。
后三图 Gate：P03-B/P04-C 不可在 P03-A 未真正 PO PASS 前开工。所有正式发布、音画合成、Story Shot 登记依旧需要分项 PO approval。

## 六、授权不变的边界

- 40.260 秒音频 PO Approved 持续有效，SHA `c47c11668ff2053d59131f3914bec14b6a223a67e79ad2ebd260212fc5411f6c`。
- 原 Opening V001 SHA `70d7922244161dd216a26446fd75531db20eea0ac7fc25f567f6ff14e2746e3a` 不更改。
- 旧独立血门木门 A 仍未 PO Approved、B 未授权、动画 HOLD；本任务不会解冻它。
- 不生成新视频、字幕卡、附加第4张图；不在 PO 审核前注册 P03-A 为正式 Story Shot 或 Scene Master。
- P03-A 的首包验证为 existing CHARACTERS PASS，不是 Ghost House Scene Master PASS；如果 Actions 失败不得交 Work 生成。
