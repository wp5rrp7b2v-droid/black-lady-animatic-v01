# 《诡舍·黑衣夫人》｜Opening P01 V005｜四张已批准补镜声画装配技术验证

日期：2026-11-03
状态：**LOCAL VIDEO TECHNICAL PASS / PRODUCT OWNER AUDIOVISUAL REVIEW PENDING / NO CANONICAL VIDEO PUBLICATION / FOUR NEW INSERT STORY SHOTS STILL REGISTRATION HOLD**

## PO授权和与原方案的关系

PO在审片P01 V004后要求进一步缩短门外入口镜头，白潇潇增加动作与神态，保留V002多景别、短切换及轻微推镜风格；随后批准 INS-05 / INS-06 两张实际上传的新图，并说「开始剪辑」。

保持的Baseline：P01现有七张Canonical Story Shot及 Approved 192.257秒原始音轨不变；独立测试用 V002 完整视频 `P01_SEVEN_SHOTS_AUDIOVISUAL_PROOF_V002.mp4` 是唯一画面剪辑基线。INS-00无人住宅入口、INS-04宁秋水轻搭肩、INS-05白潇潇手势劝阻、INS-06白潇潇前倾解释，均为PO已通过视觉审批、**目前尚未统一登记**的精确原件；不重画原件、不使用被PO否决的INS01/INS02或错误站立INS04。

## 输入实际二进制核验

本次Chat执行前，读取当前挂载原始文件并重新计算源 SHA-256 与既有审批记录逐一对应，全部 PASS：

| 类型 | 原始文件 | 原生规格 | SHA-256 |
|---|---|---|---|
| 剪辑基线 | `P01_SEVEN_SHOTS_AUDIOVISUAL_PROOF_V002.mp4` | 942×1672 / 24fps / 63.375s | `e30d0604ef26ed95d4496e7996d18262c84c1827211cf554e879b9856079b7b3` |
| 已批准完整原声 | `OPENING_P01_P04_NEIL_COMPACT_AUDIO_PROOF_V001.m4a` | 192.257s | `1701f3a8140775550a30ac788b9221486349c058278d1ef0c2c5163664d6c4ac` |
| INS00 | `OPENING_P01_INS_00_RESIDENCE_GATE_ESTABLISH_CANDIDATE_01(1).png` | PNG 941×1672 | `9f5b55574e417c002aab20472277f6b413b50be06106c23e95bb520bb70b21e7` |
| INS05 | `红裙女子旁的沙发修复(1).jpeg` | JPEG 938×1536 | `4a3e1da7bc4187434efd62083a61bfa7178dda085bc4a55856926b5f53d83bb2` |
| INS06 | `沙发后的中央黑衣男子(1).png` | PNG 980×1605 | `1a93f9167781155c5706b26b5bc12ea2a29775a67ba1323eb3a99a4d24cdf1c0` |
| INS04 | `暖光下轻搭肩膀(1).png` | PNG 941×1672 | `a9ca228f99f70b0ebf38852002b408808a2d43aceb184fdc918732d3e4abd96d` |

**IMPORTANT** INS05/INS06原批准源尺寸/格式和预期941×1672 PNG不同；只在此次视频派生帧中填充/裁取942×1672画布。没有重采样或覆盖PO批准的原始二进制，也没有将JPEG改名为PNG后冒充Exact original。

## 试剪具体EDL（基于V002源片，非逐字音轨锁定）

所有时间均为整段P01获批准原声的绝对时标。V002中未被下表覆盖的部分保留原有帧、景别切换、推拉和音频顺序。

| 起始秒 | 终止秒 | 改动后的画面 | 持续 |
|---:|---:|---|---:|
| 0.000 | 1.500 | INS00 无人住宅入口，轻推镜 | 1.500s |
| 1.500 | 3.625 | INS05 白潇潇抬手劝阻（宁秋水仍在沙发后） | 2.125s |
| 3.625 | 19.500 | 原V002全部对应镜头，包括君鹭远单人近景与三人关系镜 | 保留 |
| 19.500 | 22.625 | INS06 白潇潇前倾解释（宁秋水仍在后景） | 3.125s |
| 22.625 | 33.000 | 原V002多景别镜头：三人关系、白潇潇警告等 | 保留 |
| 33.000 | 35.500 | INS04 宁秋水从原位置轻搭君鹭远肩 | 2.500s |
| 35.500 | 63.375 | 原V002宁秋水、君鹭远等后续反应镜 | 保留 |

**未锁定的事实**：原音尚无可靠的精确逐字中文对齐；1.500s/3.625s/19.500s/33.000s切点是依据旧Cue及既有V002声画节拍选择的审片试剪，不可声称已精确落在对白最后一个字。需PO复听，发现抢话则只修正失败切点。无任何原音语句被移动、增删或重配。

## 实际合成、验收与交付状态

完成实际新视频：`P01_V005_FOUR_APPROVED_INSERTS_V002_RHYTHM_REVIEW_FINAL.mp4`
- 时长 **63.375s**，**1521帧**，942×1672，24fps，H.264/yuv420p + 原V002 AAC 48kHz 双声道，faststart MP4。
- 原输出文件大小 **10,461,892 bytes**；SHA-256 `45293debbf9c49a4fd474019d8f41df45d5325085b5e1ef36def2fc761128d31`。
- **Full decode PASS**：`ffmpeg -v error -i ... -f null -` 无错误，ffprobe帧数、码率、时长与声画轨匹配。
- **Audio bit-exact stream identity PASS**：从V002与V005分别以copy解出ADTS AAC，比对字节 `cmp` 完全相同；ADTS SHA-256均为 `4c753973491c6f6b68e2de1bbefe8238daae74c2a8e3132d28f121c854326ba1`。这证明声音与**V002派生AAC**完全相同，而非与192.257秒M4A文件二进制相同（M4A与AAC封装/片段本就不同）。既有V002从原声起始63.375秒编辑，声音内容沿用，无额外处理。
- **Retained V002 visuals QC**：抽检14个没有插入替换的实际时点（4、6、8.5、12、17.75、23.5、26、29、32、35.75、40、47、56、62s），每点输出帧与原V002压缩后均值绝对像素误差0.783–1.476/255，均低于5/255。
- **Inserted frame change QC**：0.5、1.75、2.9、19.75、21、33.25、34.5s处相对于V002原帧的平均误差14.388–49.503/255，确认新素材确实替换画面；并生成22帧完整时序联系图可人工核查。
- **New scene visual verification（本地抽帧）**：INS05（t1.75/2.5）中宁秋水在沙发后保留；INS06（t19.7/21/22.5）宁在后景；INS04（t33.5/34.7）宁轻搭君肩且没有错误站立。此为技术画面定位核查，不等于本轮新视频PO艺术PASS。
- Review excerpts, all decode PASS: `P01_V005_OPENING_FIRST_10_5S_REVIEW.mp4`（10.5s，1,610,729 bytes；SHA256 `67c74aee7ea287fb6a09715ced162ec0b98ab27f72cdb444944686adf388372d`）；`P01_V005_BAI_NING_17_5_TO_37_5S_REVIEW.mp4`（20s，3,050,729 bytes；SHA256 `de1e6ad937aab3c30e775bf7046fe1b29923385a80b528880c6994c740121901`）。
- Storyboard contact sheet `P01_V005_EIGHT_KEY_MOMENTS.jpg` SHA256 `92701ba5289d8e7c0a1350b83a9ec72b657245def73df75e3be37c2b8855fcec`.

**Delivery scope**: MP4s + keyframe image are Chat-session artifacts only, **not uploaded to GitHub** (original voice rights / review-only). This Markdown report records evidence; it is NOT a new Canonical Video and should NOT appear in Video Index until PO review.

## Product Owner gates remaining

- **PO editor PASS/FAIL** must decide: whether doorway at 1.5s feels suitably short; at ~1.5–3.625s Bai face/action and early first spoken line naturally match; when Jun begins speaking (~3.625 onward), solo shot is timely; at 19.5–22.625s Bai actual speech reaches explanatory gesture; at 33.0–35.5s Ning's volunteering falls naturally over shoulder beat; overall V002 pacing stays intact.
- If PO points to an actual timing mismatch, correct only that range using original untouched voice; do not generate extra images or alter PO-approved originals to mask problems.
- **INS00, INS04, INS05, INS06 IMAGE approval is PO PASS, but GitHub Exact Binary Publication / Story Shot Registration remain HOLD** until PO says batch register. Existing Story Shot Index count **42**, formal Video Index **3**, P0.3 **IN PROGRESS**. The V005 sound-picture proof remains V005 **candidate** not final approved audiovisual master.
