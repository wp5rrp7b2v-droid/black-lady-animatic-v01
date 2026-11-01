# Opening P01/P02｜原始有声素材恢复与最小听审验证 V001

日期：2026-11-01  
状态：**SOURCE INGEST / EXACT AUDIO TECHNICAL PASS / EDITORIAL PROOF CREATED / PO LISTENING PENDING / NOT CANONICAL VIDEO**

## 核验的原始素材

- 新增的 096 集录屏：`CH133_P01_EARLIER_RAW_SCREEN_RECORDING_20261101_SOURCE_V001.mp4`，241.158333 秒、132178716 字节，SHA-256 `16e79db3a197def8a93e1775cf6a6c31094d0a23eb35f74c81ff7971b3d9612d`；私有 Google Drive 06_Audio 保留原件 `1dhWufEc6rlm8OcJLWotMycY92Z6Fcs8n`。原用户根目录临时录屏已清除。
- 由其不重编码抽取的完整 AAC：`CH133_EARLIER_SOURCE_EXACT_AAC_V001.m4a`，241.158 秒、3302604 字节、44.1kHz 双声道，SHA-256 `2e9348c4639b8824493553ef41ae4d868de556804f2962414efda29ead1e794c`；Google Drive `1lbR_kIqBfxbgQpl4YC9U_4GmXRB2xDUW`，上传后独立重新下载核对通过。
- 既有第133章后半段来源：`CH133_AUDIO_SOURCE_UNTRIMMED_V001.m4a`，290.689002 秒、3994021 字节，SHA-256 `26d41ab241228f0de10531ceb6e67129f530a25589aa89a4c3417b884b7b9b20`；Drive `1hl9XNYZ5s0hk-VEjyKk7eyPrguY8zdEK`。仍是源档，不变更。

## 完整性和因果事实

- 新录屏的播放器同步文字覆盖君鹭远主动决定试炼 → 必须有诡舍老人同行 → 宁秋水主动应允。**新录屏实际字幕为「我来带他吧」；原著正式文本中的句子为「我带你吧……顺便也正好可以历练一下」。** 两者不应被混写成同一逐字台词。播放器高亮时码为可视近似，不等价于逐字专业听录。
- 基于 8000Hz 单声道解码音频做 FFT 波形互相关，既有音频 `t=0.000s` 匹配新录音 `t≈223.03675s`。2秒片段归一化相关约 0.98745；这证明两次录音中存在真实重叠音频，不能仅凭该值断言所有接缝听感自然。
- 提前的 P01 音源 **不再缺失**；但原声可用性不代表 P01/P02 叙事剪辑已由 PO 批准。

## 最小音频审听稿 V001（仅实验，不是正式 Opening）

- 文件：`OPENING_P01_P02_ORIGINAL_VOICE_EDITORIAL_PROOF_V001.m4a`
- Drive 私有链接：`https://drive.google.com/file/d/1mPC3rRdEHKL0EiUlm8i4pxyhySVqGpxY/view`，保存在 `Black Lady Project/06_Audio`。
- A 段：新增早期原声 `171.500–212.000s`，40.500s，围绕君鹭远决意与宁秋水应允。
- **编辑跳接**：0.650s 静音明确标示略去中途出行/抵达等剧情；这并非源录音原样无缝连续，也没有声称该跨场景跳接已被审核通过。
- B 段：旧第133章原声 `115.000–204.000s`，89.000s，进入孟军引导的血门契约/危险事件。此段不是完整 P02 终局，不含全部后续腕上黑印结尾；不得把它当作完整契约因果的最终证明。
- 试听总时长：**130.150s**；AAC 44.1kHz 双声道，编码 192kbps 生成实验派生文件（原声内容未克隆或改词，原两个母源保持不变）；输出字节 3141078，SHA-256 `b55c4ecbd55e76f8f29a1620b41aca7d3b6385cbb1f81acab1b09b08b0d909c8`。
- FFmpeg 全段解码 PASS，Drive 重新下载与原输出 SHA256 完全一致，`cmp` EXACT PASS。
- 试听稿中截取的 P01/P02 各4s音频与各自原声交叉相关分别约 **0.99978 / 0.99984**，证明没有改用其他说话者。切点 **未进行人工听感的逐句句首句尾确认**。

## Gate 裁定

- **FACT / TECHNICAL PASS：** 新增 P01 来源已到位；两次录音有高度一致的真实重叠；试听稿完成并私有云归档；文件、格式、哈希/全段解码均核验通过。
- **UNKNOWN / PO LISTENING PENDING：** 起止是否断句、两段跨越出行过程的跳接是否自然、新观众能否理解为何契约、P02 事件是否过长或内容是否缺尾。此实验不能宣称叙事 PASS。
- **FAIL 触发条件：** 试听认为仍从中间说话开始、人物选择难以理解、跳接突兀、叙述冗长或关键结果不完整，则只在声音剪辑级继续小范围调节，不扩大成视频或 Work 出图。
- **PASS 触发条件：** PO 试听明确认可叙事起点和声桥可读性，并对接入正式 P03/P04 音桥提出后续授权。只有此后才推进最小视觉设计/Scene Reference/Bundle/Work 单图候选的正式链路。

## 不修改已批准基线

- 不替换 Opening V001，不把实验样片纳入 Video Index；当前正式 Story Shots **35**、正式 Video Index **3**、P0.3 **IN PROGRESS**。
- 先前 PO 批准的前情提要**文案**仍然批准；此真实原音路线是另一个未通过审听的声音试验，未自动撤销原文。
- P03-A/B/C 已批准的原始 PNG 与 40.260s P03/P04→Neil 音桥不改；旧独立血门 A/B 项目暂停；不声称 P02 的完整叙事已完成。
- 有版权的录屏及音频均只存私有 Drive；GitHub 仅保留元数据与验证记录。
