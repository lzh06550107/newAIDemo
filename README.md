# newAIDemo

本仓库已建立 AI 协作与项目事实源文档基线，业务目标、技术栈和应用源码尚未确定。本 README 不代表应用已实现或已通过测试。

## 文档索引

- [AGENTS.md](AGENTS.md)：AI/开发协作最高规则。
- [PROJECT.md](docs/ai/PROJECT.md)：项目架构与环境信息。
- [STATE.md](docs/ai/STATE.md)：当前事实、任务与下一步。
- [DECISIONS.md](docs/ai/DECISIONS.md)：已确认的关键决策。
- [ACCEPTANCE.md](docs/ai/ACCEPTANCE.md)：验收条件。
- [TESTING.md](docs/ai/TESTING.md)：测试分层与实际入口。

## 当前状态（2026-10-12）

目前只有文档基线，没有应用源码、构建入口、可运行测试或 GitHub Actions 工作流。项目类型和技术栈未确定。请先阅读 [STATE.md](docs/ai/STATE.md)，并实时核对 GitHub main 的 HEAD；以仓库实际状态而非本段静态文字为准。

## 开始开发前

1. 阅读 AGENTS.md 与 docs/ai 下五份文档。
2. 核对实际 Branch / Commit、源码、scripts/ci 和 .github/workflows。
3. 确定业务范围与技术栈，在 PROJECT.md 记录。
4. 根据真实工程配置统一验证入口和 GitHub Actions；同步更新 TESTING.md、ACCEPTANCE.md 和 STATE.md。

**注意**：本仓库尚无可执行的 `verify` 命令；不要把文档示例命令当作已存在的测试入口。
