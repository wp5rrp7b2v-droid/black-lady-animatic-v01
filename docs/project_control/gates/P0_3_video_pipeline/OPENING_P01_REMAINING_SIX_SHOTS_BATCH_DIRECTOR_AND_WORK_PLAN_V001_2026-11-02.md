# 《诡舍·黑衣夫人》｜P01 后续六镜整批制图｜Director + Reference + Work Plan V001

日期：2026-11-02
PO本轮指令：直接一次性P01后续的全部制图流程。
状态：整批制作意图已授权；Work候选审图和后续Canonical登记仍须PO逐张批准。

## 1. 唯一事实基线

- 已批准192.257秒Opening原声，P01从绝对00:00.000开始，P01段时长约63.2秒，不改音轨、不同步额外新旁白，逐句切点仍需声音编辑复核。
- P01首镜 OPENING_P01_OPEN_01：PO Approved / Current，正式JPEG 864×1536、336546字节，SHA-256 4ccebb6a903b9cbeac1dfdc2e8b05c7f5dafa05e31cff53e775dfa2f37945452，Git Blob 9c5fc2d1d5bcc711a0be129fcc3e3229f039bf3a。音频绝对00:00.000开始。
- 同图受控 Scene Anchor：OPENING_P01_OPEN_01_BAI_RESIDENCE_SCENE_ANCHOR_V001。白潇潇左侧红色睡裙、君鹭远右前蓝灰上衣、宁秋水后侧黑色服装，房屋窗、家具与光照在全批保持连续。
- 仅把上述首镜JPEG作为住宅空间/服装/站位参考；人物的脸必须分别受已批准Atomic/Sheet控制。不把首镜当成新的所有人脸Master。
- P01第132–133章背景：白潇潇在迷迭香私人住所告知风险；君鹭远病弱但自愿；宁秋水直到约00:32才表态同行。不能让宁秋水在前段先以语言/动作宣告决定。

## 2. 六镜分镜、候选命名与音画

| 镜头 | 约略声时 | 文件名（每镜仅1张候选） | 视觉叙事 |
|---|---|---|---|
| P01-OPEN-02 | 00:04–00:19 | OPENING_P01_OPEN_02_JUN_RESOLVE_CANDIDATE_01.png | 由已批P01首镜君鹭远的右前位置沿轴线自然切近：病弱仍坚决，目光对向白潇潇位置。避免健康后的英雄姿态。 |
| P01-OPEN-03 | 00:19–00:32 | OPENING_P01_OPEN_03_BAI_CAUTION_CANDIDATE_01.png | 从白潇潇左侧座位的3/4侧前机位，担忧而清醒地解释危险，画面另一侧保留君鹭远部分肩影，不能变成白潇潇写真。 |
| P01-OPEN-04 | 00:32–00:40 | OPENING_P01_OPEN_04_NING_VOLUNTEERS_CANDIDATE_01.png | 宁秋水从首镜后方自然进入对话主位，中景平静表示自愿陪同，前景保留君鹭远肩影。不是举拳、誓言式英雄镜。 |
| P01-OPEN-05 | 00:40–00:48 | OPENING_P01_OPEN_05_JUN_GRATEFUL_CANDIDATE_01.png | 君鹭远面对宁秋水的方向，短暂克制略苦的感激笑，区别于前段面对白潇潇的坚定态度。 |
| P01-OPEN-06 | 00:48–00:58 | OPENING_P01_OPEN_06_JUN_BURDEN_CANDIDATE_01.png | 安静侧向关系镜：君鹭远不愿牵连对方，笑意消退，双手自然在膝前；宁秋水位于较远的真实空间层次。不是05的同机位重画表情。 |
| P01-OPEN-07 | 00:58–01:03 | OPENING_P01_OPEN_07_DECISION_CLOSE_CANDIDATE_01.png | 三人关系自然收束的更宽侧向构图，现实客厅不变，决定回诡舍签契约；下个场景才转换地点。不可提前给出血门/诡舍图。 |

这些时间来自已记录的源录屏高亮辅助定位，不是锁定秒级EDL。静帧数6仅为本轮批准制作候选数，画面不代表每句必须切一次。

## 3. 关键技术验证与批准边界

- 先对同一ZIP做混合JPG/PNG的3/3校验。2026-11-02 GitHub Actions **Run 41388931182 SUCCESS**，VALIDATION_PASS 3/3，验证已批准原始JPEG Scene Anchor + 君鹭远及白潇潇Approved PNG Identity Inputs。仅校验源，不改文件、不冒充JPEG为PNG。
- 此项只能证明建包器接受并核实字节格式和正式引用，不能证明Work模型对所有人物和空间必然准确。
- 每个镜头最多5张正向直接参考，包括1张已批准住宅JPEG和不同角色必要身份Anchor。不要把温倾雅/苏小小正脸加入白潇潇的正向输入。
- 对每个镜头新建独立的正式 Reference Delivery Bundle Spec；先基于真实GitHub资产和已批准首镜测试精确二进制与Artifact，再允许Work执行。
- 六张一批由Work按序出图，建议输出941×1672、9:16 PNG，每张1个Candidate，不自主多生备选，不制作动图/视频，不反复进行整图微动作重生成。
- Work若因身份、住宅几何、座位/服装不一致而判断某镜失败，只记录该镜FAIL；不得使用失败图继续派生其他镜。其他镜仍使用首镜Canonical场景参考。
- 六张完成后一次性提交六张独立原图+可阅览的顺序图集，等待PO审图后再决定调整与Canonical发布。PO本轮的整批执行授权**不等于**预批准未来未看到的6个输出。
- Original Opening V001、192.257秒原音、P03A/P03B/P04C与36个已批准Story Shots不变；当前P0.3仍未PASS。

## 4. 最小证明结论

已通过：JPEG+PNG混合参考格式检查；首镜已批准并独立登记。
尚未通过：六个新的正式Bundle均已生成并且artifact通过独立复核；六张Work图实际生成；PO逐张视觉审查；P01音画成片审查。
PASS（技术）：六个正式Bundle各自有真实Run SUCCESS、Artifact存在、ref hashes和数量与约束一致。
FAIL：JPEG被转码冒充原件、角色身份碰撞、首镜住宅结构错乱、某镜Bundle失败、或Work并未实际产生6张PNG。
PO视觉PASS待审：角色分别一致、感情转折与声音顺序一致、六个构图确实承担不同叙事责任而非重复人物写真。
