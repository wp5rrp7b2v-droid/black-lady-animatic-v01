# 《诡舍·黑衣夫人》｜P02 C03/C05｜Work 正式双镜候选制图交接 V001
2026-11-18｜状态：BUNDLES 2/2 BUILT, EXACT REFERENCES 3/3 EACH PASS；WORK GENERATION AUTHORIZED；PO VISUAL APPROVAL PENDING。

## 范围
依据 PO “开始”指令，本工作单元连续生成两张、各仅一版、**941×1672 9:16 PNG**，然后统一交 PO 审核。禁止生成其余 C01–C09、自动发布、登记 Story Shot、视频或变更任何 Approved 母版。
正式流程：Chat → GitHub Actions → Work → PO → Chat，图像由 Work 执行，禁止冒称 Chat 制图为 Work 交付。

## GitHub Actions 验证事实
Repository: `wp5rrp7b2v-droid/black-lady-animatic-v01`
- C03 spec: `production/bundle_specs/OPENING_P02_C03_CONTRACT_CONTINUITY_REFERENCE_DELIVERY_BUNDLE_V001.json`
  - Run `44213797459` SUCCESS; Artifact `14387755828`; ZIP upload SHA256 `01c48d8c93419ec5c58e554cb09bb742c30b09e00f800d352679996b700c529a`
  - URL: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/44213797459/artifacts/14387755828
  - Output: `OPENING_P02_C03_BLOOD_PALM_CONTACT_CANDIDATE_01.png`
- C05 spec: `production/bundle_specs/OPENING_P02_C05_CONTRACT_CONTINUITY_REFERENCE_DELIVERY_BUNDLE_V001.json`
  - Run `44216903413` SUCCESS; Artifact `14387768775`; ZIP upload SHA256 `86ec956b5275c914e3baae8b200558c4aaed99d0003afb717a252479efba1aa3`
  - URL: https://github.com/wp5rrp7b2v-droid/black-lady-animatic-v01/actions/runs/44216903413/artifacts/14387768775
  - Output: `OPENING_P02_C05_DOOR_GAP_WRIST_GRIP_CANDIDATE_01.png`

两个 Actions job 的构建及上传步骤均 SUCCESS，日志均输出 `PASS: 3/3 exact canonical reference binaries verified` 和 `GENERATION_ALLOWED=TRUE`；不能把它当作候选图审核通过。

## 每个 Bundle 中的三个相同正式输入
1. `OPENING_P02_D03`，已批诡舍三楼旧血木门，941×1672，SHA256 `f1c706e7ed60accf169e75a8b1d131974489c438bf179b093847ec3860fd43c3`
2. `AST_IMG_000057` 君鹭远 approved 角色参考，SHA256 `e8a0410cfc176ec9d6446b84f89b2c12d0683ec32b927c90353e850c416d909e`
3. `AST_IMG_000072` 君鹭远 approved 左3/4脸部辅助，SHA256 `be9f1f39ae303a61a79746b25a0f9f8153797b179ef85d07a5c2fdf1ce02d01b`

Work 先下载两个 Artifact，逐项读取 `delivery_manifest.json` 和 `WORK_HANDOFF.md`，核实实际三张参考的字节、尺寸、身份。如无法读取或发现不符，停止并报告，不能自行换图。

## 连续场景硬约束
场景始终为**诡舍三楼**同一扇 D03 木门，不是艾伦古堡、莫妮卡庄园。保留 D03 门框、木纹、血色旧痕、光线、相机轴线。尚未签约，**不能提前出现试炼任务/提示血字**。不使用已有 P03A 带字门为正向输入，因其受控正向参考权限只覆盖 P03B/P04C。孟军正脸未有 Approved Master，本轮只允许画外动作，不得擅自创造正式正脸。

C03：从自然侧向中近景展示君鹭远**右手**掌心少量血液，手掌紧贴完全关闭的木门。要看清袖口与前臂连接、掌门位置及足够木门结构，以便后续动作衔接；没有门缝、腐手或任务文字。

C05：**同一右手/右腕、同一袖口、同一木门、同一触点和接近的摄影轴线**。木门仅开狭缝；**一只**腐烂的手臂从门**里面**伸出并准确抓住君鹭远右腕。右掌仍贴在门外侧。不得出现额外手/指、肢体融合、反转左右侧、门彻底打开、完整怪物/鬼脸或不必要的血浆。

右手是双状态空间一致性采用的 **WORKING HYPOTHESIS**，原著没有指定左右手，不能冒称为原著事实。

## 通过／失败条件
PASS（需要 PO 审核生成图）：D03 门体与君鹭远身份稳定，同一右腕空间连续，血掌贴门→门缝内腐手抓腕因果清楚，无畸形或提前血字。
FAIL：门换了、人物漂移、左右手互换、腐手从外面出现、抓握不成立、手臂畸形、凭空多出人物。失败时停止扩产，不自行无限重抽或自动修复原图。

## 不变基线
P01 V018、D V005、D01–D03、P03A/B/P04C 原件及索引全部保持不变；目前 52 Story Shots、248 Audit Events，P0.3 继续 IN PROGRESS。C03/C05 候选批准后才由 Chat 执行 Exact Binary → Canonical Publication → Story Shot Registration → Registration Verification → Project Control Closeout。

导演设计：`docs/project_control/gates/P0_3_video_pipeline/OPENING_P02_POST_D03_CONTRACT_DIRECTOR_DESIGN_V001_2026-11-18.md`
