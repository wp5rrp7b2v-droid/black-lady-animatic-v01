# 《诡舍·黑衣夫人》｜Opening P01 V008 剪辑整改与技术验证

日期：2026-11-06
状态：**V007 PO EDITORIAL FAIL / V008 TECH PASS / V008 PO AUDIOVISUAL REVIEW PENDING / NOT CANONICAL**

## 输入事实与 V007 失败原因
- Product Owner 审片明确指出：“声画有点不够匹配，比如我带他去吧 就和手放在肩膀上没有同步；另外镜头还是切的太碎了”。
- V007 63.375s / 18段 / 17次切换；宁秋水表态 OPEN04 出现于 33.000–35.500s，但搭肩 INS04 在 35.500s 才切入。
- 用户反馈是编辑效果失败，不影响 2026-11-03 七张正式新增 Story Shot 7/7 Approved/Current/Exact Registration PASS。

## V008 执行修正
- 原声保留 P01 绝对起点 00:00.000–00:63.375，缩减为 **11段 / 10次切镜**（切换次数较 V007 减少 7次，约41.2%）。
- 在 32.500–38.750s 显示 `OPENING_P01_INS_04` 宁秋水搭肩，不再先用 OPEN04 再在35.5s晚切搭肩图。此选择覆盖正式 Cue Sheet 对宁秋水表态的**约32–35秒**粗时间窗。
- 原始台词起始字的**逐字真实时间 UNKNOWN**；没有独立音频文字对齐证明 32.500s 恰等于台词开始，因此此处只属工作假设与审片修正，不能称“精准同步PASS”。
- 其余连续节拍为：INS00 0–1.5 / INS05 1.5–3.75 / INS07 3.75–10.5 / OPEN02 10.5–17.5 / INS06 17.5–25.0 / OPEN03 25–32.5 / INS04 32.5–38.75 / OPEN05 38.75–44.5 / INS08 44.5–49.75 / INS09 49.75–57.5 / OPEN07 57.5–63.375。各段无时间空隙。
- 14/14 GitHub Approved 原始静帧 SHA256 和 bytes 从已验证 artifact 重新核验 PASS；V008 实际选用其中11张，未覆盖任何原始图片。静帧只有极轻量派生镜头推拉，不冒充手部真实位移动画。

## 技术验证
- 源原音 `OPENING_P01_P04_NEIL_COMPACT_AUDIO_PROOF_V001.m4a` SHA256 `1701f3a8140775550a30ac788b9221486349c058278d1ef0c2c5163664d6c4ac` MATCH。
- V008 review MP4 942×1672 / 24fps / **1521帧** / 视频轨63.375s；容器总时长63.381s（AAC封装采样尾差）；8,564,083 bytes；SHA256 **`0d29bfeae202ba1b143bda9cfd8d3efa6f6a67df5d19ad60dbdca4ed0f320296`**。
- FFmpeg 全程解码0错误；源音首63.375秒与视频提取 AAC→ADTS 经 `cmp` **bit-exact PASS**，共同 SHA256 `427f5993d7da774fc42cfda4d7fa97755ccbf0a12ec3f1a4f90d1ff0e1a48056`。
- 精确帧边界核查：第779帧（32.458s）仍为白潇潇说明；第780帧（32.500s）为宁秋水搭肩；第929帧（38.708s）仍搭肩，第930帧（38.750s）切为君鹭远感激。
- 视频、EDL JSON、Storyboard 作为本次 Chat 审片文件提供；版权原声**不上传公开 GitHub**。此文档仅记录可重现实测参数与哈希，不主张原始视频已在 GitHub canonical。
- **已证实：**技术可解码、画面入点改变、减少重复切镜、原音二进制不变。
- **未证实：**真实台词首字与搭肩精确同帧、V008叙事自然度达到 PO 艺术 PASS。

## 下一步与权限边界
PO审看本次V008完整63.375s。若仍有实际提前/滞后，按照PO指出的具体秒点调整 INS04 单段，不新增图片；若节奏仍异常，只调整必要编辑点，不恢复无意义反复反打。Formal Videos仍3，Story Shots仍49，Audit Events仍239，P0.3仍IN PROGRESS。Mac最新本地同步没有新增独立验证证据。

## 2026-11-06 追加：PO 对26–43秒专项审片结果（BL-D-196）

**Product Owner 原话：**“这段可以”。直接承接 `OPENING_P01_V008_SHOULDER_DIALOGUE_26_43S_REVIEW.mp4`（26–43秒）专项审片交付。

**结果：PO AUDIOVISUAL SCOPED SEGMENT PASS（26.000–43.000秒）**。INS04 搭肩32.500–38.750秒与该段现有剪辑节奏获得PO观感接受。此局部段落作为后续剪辑固定基线；未经新失败证据不主动推翻或重复修改。

**不扩大授权：**完整P01 V008 63.375秒**尚未批准**；开头00–26秒及43–63.375秒仍需审核，不能宣称词级同步、正式母版发布或索引登记完成。49 Story Shots、239 Audit Events、3 Formal Videos、P0.3 IN PROGRESS不变。
