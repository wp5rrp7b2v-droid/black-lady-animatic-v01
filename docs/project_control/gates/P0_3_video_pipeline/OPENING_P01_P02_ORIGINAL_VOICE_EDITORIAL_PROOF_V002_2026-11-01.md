# Opening P01/P02 原声试听纠偏 V002｜2026-11-01

**正式裁定：V001 叙事听审 FAIL（PO 提出两处可定位缺陷）；V002 AUDIO TECHNICAL PASS / DRIVE EXACT MATCH；V002 PO LISTENING PENDING。**

## 用户反馈 / V001 实际问题

1. “露出感激的笑容”和下一段衔接割裂：V001 使用新录音 171.500–212.000s，跳到旧原音 115.000s，省略了君鹭远感激后的心理与担忧，以及宁秋水提出回诡舍签约的自然过门。
2. 最后部分被掐断：V001 旧原音结束 204.000s，未保留该处完整叙述和句后余量。

用户反馈属于 **新获得的实测反证**，原先“技术文件 PASS”仍有效，但不应推导为音频剪辑的艺术 PASS。保留 V001 供历史比对，不入正式 Opening。

## V002 修正内容（只做声音剪辑最小修正）

- P01 新原声 `CH133_EARLIER_SOURCE_EXACT_AAC_V001.m4a`：171.500–236.950s。延续“感激的笑容”后原音，包含他担忧给人带来麻烦、两人已经作出决定、回诡舍签订血门契约和“试炼应该会立即开始”的完整交代；结束于下一句“宁秋水点头”之前的相对低音区。
- P02 旧原声 `CH133_AUDIO_SOURCE_UNTRIMMED_V001.m4a`：61.500–208.500s。保留诡舍人物/场景过门和血门契约危险事件，结尾延长至“眼前也恢复了清明”之后的相对静音区，且在随后插播广告前结束。
- 两段之间只使用 0.18s 音频淡叠接，不再插入 V001 的 0.65s 人工静音。该跳接是编辑性的“回诡舍→到诡舍”，**并非声源天然连续**；声学参数不能代替 PO 听感认可。
- 原始有声小说声音来自授权用户提供的既有录音；未克隆、未改写台词。为混音制作了 AAC 192kbps 派生文件，母源二进制未动。
- 完整 V002：`OPENING_P01_P02_ORIGINAL_VOICE_EDITORIAL_PROOF_V002.m4a`，212.270s、5,136,712 bytes，SHA-256 `34ce36b682ba7e62e06e0395ac49b0e9b1f3041e245eb6aae65d356426ee18d3`；私有 Google Drive `https://drive.google.com/file/d/14x6RXJQVLjeeCin1JtLwQPzF37Bgk3Js/view`。
- 衔接 35 秒检查段：`OPENING_P01_P02_V002_JOINT_REVIEW_35S.m4a`（V002 第49秒起连续35秒），850,191 bytes，SHA-256 `57842b4bd23ef3fc2922272825fa280e79406cf5ba5fecd7b81dd597988f832b`；私有 Google Drive `https://drive.google.com/file/d/16sr9EC6zymt-uWZqTG8j1opz9o7KBbxx/view`。为临时审听派生物，**待审核完成、不再需要时删除**；不误删源音。
- 完整与35s文件均已 FFmpeg 解码 PASS，并自 Drive 下载二进制与本地输出 `cmp` 逐位一致（SHA-256一致）；Drive 路径为 `Black Lady Project/06_Audio`，根目录未留下临时文件。

## Gate / 审批边界

- **FACT：** 用户指出 V001 两处剪辑问题；V002 文件已制作及二进制核验；V001 技术 PASS 没有被推翻，但叙事剪辑 FAIL。
- **WORKING HYPOTHESIS：** 延长 P01 至完整决定、延长 P02 至叙述句尾，能改善割裂与截尾；仅靠视觉字幕/静音检测不能证明最终人耳观感通过。
- **PO LISTENING PENDING：** A/B 节拍及 0.18s 编辑跳接是否自然，尾部是否完整，整体 212s 是否过长及后续最短可用时长。
- **PASS：** PO 实际试听认可叙事与句尾完整性；此后才决定下一轮浓缩长度、声画 Proof 和 Work 制图授权。
- **FAIL：** 仍有明显断句或突兀；继续编辑声轨最低必要位置，不扩到视频/图像生产。
- 正式 `OPENING_V001`、已批 P03A/P03B/P04C、已批 40.260s P03/P04→Neil 声桥、Story Shot Index 35、Video Index 3 及 P0.3 IN PROGRESS 全部保持不变。

## 2026-11-01 Product Owner 听审裁定（追加，不覆盖原 V002 技术记录）

- PO 对上述 **完整 V002 原声试听稿** 回复：「这版可以」。
- 裁定：**P01→P02 叙事连续性与尾部完整性 LISTENING PASS / PRODUCT OWNER APPROVED AS EDITORIAL AUDIO BASELINE V002**。
- V001 曾经被指出的「感激的笑容」后割裂及末尾截断两处问题，已由 V002 修正并经 PO 听审接受。此前音频二进制与解码 TECHNICAL PASS 继续有效。
- 审批仅针对 **212.270s 的 P01/P02 独立原声剪辑叙事听感**；不意味着它的长时长已经被指定为最终 Opening，也不包含最终 P02→P03/P04→Neil 连贯全片审片、视觉新镜头、配音授权扩张、Video Index 或母版替换。
- **保留已批准的 V002 完整音频原件和 SHA-256**；压缩版本仅能以独立候选方式探索，不反向修改这一已听审通过的 baseline。
- 下一最小 Gate：先依据 V002 既有剪辑和获批 P03/P04→Neil 音桥设计一个范围更紧凑、断句完整的低成本音频衔接候选。PASS = 观众仍能理解人物选择、契约后果、任务提示，且自然接入尼尔欢迎；FAIL = 删除必要因果、截句、转场突兀或整体节奏不自然。V002 保持有效 baseline 直到新版本获得独立 PO 审核。
