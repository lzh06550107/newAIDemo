# ACCEPTANCE.md — 验收标准

## 本阶段：文档基线初始化

本阶段仅验收仓库文件与 GitHub 事实，不将其等同于应用功能完成。执行者必须根据证据实际核对下面项目，未核对不得将其标记通过：

- [x] main 分支存在，能读取最新 HEAD Commit SHA。
- [x] AGENTS.md 与用户上传的原文一致。
- [x] README.md 与 docs/ai/PROJECT.md、STATE.md、DECISIONS.md、ACCEPTANCE.md、TESTING.md 均可在 main 读取。
- [x] STATE.md 准确区分已完成、待办、CI、部署与运行时验证状态。
- [x] 未虚构应用源码、测试结果、部署结果或技术选型。

**完成边界**：这些条件全部满足，仅表示“文档基线初始化得到仓库层面验证”；项目开发任务不能因此进入 AGENTS.md 定义的 DONE。

验收记录：2026-10-12，GitHub API 复核 `main` 文档基线 Commit `c847b83b2fd0505a640ea29e873e2ffd7886e58a`；AGENTS.md 与用户原文内容对照一致。该核验仅覆盖仓库文档。

## 后续实际开发验收（待业务和技术栈确认）

每个功能应在实施前补充可检查的验收项，通常包括：

1. 预期行为、范围和异常情况。
2. 当前 Commit 的本地验证证据。
3. 对应 Commit 的 GitHub CI 结果。
4. 目标环境部署/安装结果。
5. 浏览器/真机/接口的真实运行验证。

上述各项目前都没有针对业务功能的可执行入口或证据，不能预先勾选。
