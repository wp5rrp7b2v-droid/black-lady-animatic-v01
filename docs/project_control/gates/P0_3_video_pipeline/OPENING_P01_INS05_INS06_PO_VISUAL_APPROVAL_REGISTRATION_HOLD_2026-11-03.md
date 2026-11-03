# 《诡舍·黑衣夫人》｜Opening P01 INS-05 / INS-06｜Product Owner 视觉审批与登记暂缓记录

日期：2026-11-03

状态：**PO VISUAL APPROVED / EXACT ORIGINALS IDENTIFIED IN CHAT / NOT CANONICAL / REGISTRATION HELD / NO AUDIOVISUAL MASTER APPROVAL**

## 1. 审批对象与证据等级

Product Owner 在收到根据宁秋水后景连续性 V002 整改生成的两张白潇潇动作图后，上传两份实际文件并明确指令：「这两张通过批准」。

已对上传的 **原始文件二进制** 进行本地读取、PIL文件格式/尺寸读取和 SHA-256 计算；按画面动作对应：

| 镜头 | 叙事目的 | Product Owner 实际批准的文件名 | 文件格式 | 原始尺寸（px） | 原始字节数 | SHA-256 |
|---|---|---|---|---|---:|---|
| INS-05 | 白潇潇担忧地单手向外抬起劝阻，宁秋水在沙发后方 | `红裙女子旁的沙发修复(1).jpeg` | JPEG | 938×1536 | 331,211 | `4a3e1da7bc4187434efd62083a61bfa7178dda085bc4a55856926b5f53d83bb2` |
| INS-06 | 白潇潇前倾并掌心向上解释风险，宁秋水在沙发后方 | `沙发后的中央黑衣男子(1).png` | PNG | 980×1605 | 2,034,228 | `1a93f9167781155c5706b26b5bc12ea2a29775a67ba1323eb3a99a4d24cdf1c0` |

**FACT（本次人工可见审图）**：两张均有白潇潇左侧红裙，宁秋水中后方黑衣、头肩可见，君鹭远在右前方蓝灰衣；两种手势/上身倾斜方向不同。Product Owner 的视觉批准是最终艺术审批依据。

**FACT（尚未证明）**：上述二进制文件本次通过用户消息上传并由Chat本地读取，**本次没有上传到GitHub Staging、不能声称 Git Blob / Repo Exact Binary PASS，更没有Canonical发布**。待后续统一登记时须再次获得/上传这两个**完全相同的原始二进制**并执行严格核验，不可按预期文件名虚构文件内容。

## 2. 特别说明：视觉审批与输出技术要求不等价

V002 Reference Bundle Work 指令的输出目标原为 **941×1672 PNG**；此次 PO 明确批准的源文件尺寸/格式分别是 **938×1536 JPEG** 与 **980×1605 PNG**，与原目标不同。

- **视觉审核：PASS（Product Owner 明确批准）**。
- **原指定输出格式和尺寸 Gate：尚不符合**。不能把源文件改名为PNG来宣称转换过，也不能悄悄重采样后当作被批准的原件。
- 后续**视频粗剪**可按画布制作派生画面，保留这两个精确二进制不变；若以后 Canonical Story Shot 登记要求941×1672 PNG，必须单独明确如何处理尺寸/格式例外，先取得相应技术标准或PO的接受决定，不得无声替换。
- 本条不主动重新设计图片；仅记录事实和避免未来错误登记。

## 3. 已验证参考链（仅证明输入有效）

- INS-05 V002 Bundle: Actions [41589534914](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41589534914)，Artifact `13209272925`，5/5 Approved 原始参考 PASS。
- INS-06 V002 Bundle: Actions [41589540027](https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/41589540027)，Artifact `13209297938`，5/5 Approved 原始参考 PASS。
- 这些 PASS 不是两张最终上传图片的 GitHub Exact Binary Verification。

## 4. 待统一登记的当前获批插镜

- INS-00：已批准的无人住宅入口，仍待联合登记，原文件保持不变；
- INS-04：已批准的「暖光下轻搭肩膀」图，仍待联合登记，旧站立候选不是通过版；
- **INS-05：此次视觉 APPROVED，精确文件标识如上，注册 HOLD；**
- **INS-06：此次视觉 APPROVED，精确文件标识如上，注册 HOLD。**

INS-01/INS-02、错误空间位置的INS-04站立方案、INS-05/06旧版没有后景宁秋水的候选仍属 FAIL，不列入注册批次。

**Current Canonical 不变：** Story Shot Index 42，formal Video Index 3，P0.3 IN PROGRESS。V002多景别/轻推镜是以后声画剪辑的节奏基线；PO尚未批准加入这两张后的全段正式视频。下一步若继续声画测试，须从0–约10秒及19–31秒先做局部A/B，保持已批准原音、已批准原件二进制、人物空间/时间连续性。
