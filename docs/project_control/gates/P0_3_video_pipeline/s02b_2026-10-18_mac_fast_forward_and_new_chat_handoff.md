# S02-B｜2026-10-18 本地同步与新对话交接

## 正式代码源和版本

`wp5rrp7b2v-droid/black-lady-animatic-v01`。

- GitHub `main`：本轮正式收尾与已批准成果的事实源；V006 是保留的基础剪辑参考（未明确独立视频 PO 批准），V018 是新视觉批准迭代；此前 V001 保留。**不覆盖历史视频，亦不把 V018 视为必须替换的唯一母片。**
- 研发分支：`feature/m01-v002-engine-stage-a-20261017`，保留 M01 统一引擎源码、N17/N23/NEW02 样例、V016/V017 技术中间版及 V018 研发历史。**不能删除该分支。**
- 本次 Project Control：`docs/project_control/core/project_state.json` 最新 R360；收尾事实总账：`docs/project_control/gates/P0_3_video_pipeline/p0_3_s02b_m01_2026-10-17_to_2026-10-18_full_closeout.md`。
- 历史版本：`production/video/iteration_history/S02_B_ITERATIONS_V001.json`。
- 视觉批准 V018：SHA-256 `6897b1ac246e4c30d84aca3b80003a58d7bae86eb7631272fe28253b23a01427`；**不能重新编码然后沿用此 SHA。**

## Mac 本地同步｜仅 GitHub 拉取，不产生 ZIP

项目历史保存的本机路径：`/Users/caroline/诡舍/黑衣夫人/black_lady_short_01`。若该本机目录搬迁，以实际 Git worktree 路径为准。**仅用户 Mac 可执行，云端 Actions/Chat 无法伪造 Mac HEAD。**

在 Mac Terminal 逐段执行：

```bash
cd "/Users/caroline/诡舍/黑衣夫人/black_lady_short_01" || exit 1
git status --short --branch
# 如上一步存在受 Git 跟踪文件的本地修改，停止，先处理，不 stash/reset/clean。
if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "STOP: tracked local modifications; do not pull."
else
  git switch main || exit 1
  git-proxy-auto pull --ff-only origin main || exit 1
  git fetch origin feature/m01-v002-engine-stage-a-20261017 || exit 1
  echo "LOCAL_HEAD=$(git rev-parse HEAD)"
  echo "ORIGIN_MAIN=$(git rev-parse origin/main)"
  echo "REMOTE_FEATURE=$(git rev-parse origin/feature/m01-v002-engine-stage-a-20261017)"
  git status --short --branch
fi
```

**失败时停止并保存输出；不要自行强推、重置或清理。** 未跟踪的 `BlackLadyLocalConsole/` / `BlackLadyLocalConsolePrivate/` 原样保留。用户将 Terminal 输出贴到当前对话，Chat 与 GitHub 实时 `main` commit SHA 比对后才可以写 `LOCAL_SYNC_VERIFIED`。

仅拉取 `origin/feature/...` 远端分支引用，不切换当前工作树、不把研发分支的未批准文件误合入 `main`；未来新会话可按需从远端读取研发进度。

## 新对话框启动语句

> 请先读取《诡舍·黑衣夫人》GitHub 仓库 `main/docs/project_control/core/project_state.json`、`docs/project_control/gates/P0_3_video_pipeline/p0_3_s02b_m01_2026-10-17_to_2026-10-18_full_closeout.md`、`production/video/iteration_history/S02_B_ITERATIONS_V001.json`，核对 M01 研发分支 `feature/m01-v002-engine-stage-a-20261017`。前次截止 2026-10-18，V018 全片烛火视觉获批，V006 是不能丢的基础剪辑参考，V001/V006/V018 均作为独立版本保留，今后审批迭代只增不覆。请汇报当前 P0.3 Gate、下一制作方向与待审批项；不要重做已批准 V018、不要用 V018 直接覆盖母版，Story Shot 正式制图仍交 Work。本地同步仅在用户提供 Mac 命令输出后标记完成。
