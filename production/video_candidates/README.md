# Video Candidate Registry｜审核视频候选登记区

本目录存放**非正式母版的视频候选**，与正式 `production/video/video_index.jsonl` 分离。

- `video_candidate_index.jsonl`：审核候选索引；状态 `PO_REVIEW_PENDING` 不等于 `APPROVED`。
- `assets/`：审核候选原始 MP4 备份，保留 SHA-256 与字节数，不允许重编码覆盖。
- 正式视频母版、正式 Video Index、Storyboard Approved PNG、音轨及 `main` 均不得因登记候选而修改。
- 候选如获 PO 批准，须经过独立审批、Exact Verification 和正式视频发布登记，不能直接改变现有母版。
- 本目录中 V006 的源片来自 Github Actions Run `38569617657`，因完整 V005 审核源未取得，确切标签必须为 `RECONSTRUCTED_ROUGH_REVIEW`，禁止标记为 V005 exact visual continuation。
