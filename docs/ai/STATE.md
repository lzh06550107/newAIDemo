# STATE.md — 当前项目状态

记录日期：2026-10-12  
事实源：GitHub 仓库 lzh06550107/newAIDemo

## Current branch / 当前分支

`main`。

## Current commit / 当前 Commit

以每次读取时 GitHub `main` 的 HEAD SHA 为准。**最近在写入本文件之前已核实的 Commit** 为 `9ad3d47f1e0e984e3fc22ba6cb6fb5fb24f7106b`（AGENTS.md 初始提交）。

注意：本文件与其他文档将在后续 Commit 中创建，不能在 Git 文件内容中预先自引用其所属 Commit SHA。接手时必须实时查询 HEAD；不得把上述历史 SHA 视为永远最新的 HEAD。

## Current task / 当前任务

建立文档事实源和 AI 协作基线；后续应用方向和技术栈待确认。

## Completed / 已完成事项

- 已通过 GitHub API 确认仓库身份与默认分支 main。
- 已提交用户提供的 AGENTS.md，初始提交 SHA 如上。
- 本次文档初始化提交包含 README.md 和 docs/ai 下五份基线文档；需在推送后核验仓库读取结果。

## Pending / 未完成事项

- 核验本次文档初始化 Commit、HEAD 和各文件可读取性。
- 确认产品目标、平台与技术栈。
- 实现业务源码与真实构建配置。
- 建立 scripts/ci 下可执行的测试和统一验证入口。
- 建立 .github/workflows 下的正式 CI。
- 确认并验证部署/真机/浏览器环境。
- 形成真实功能验收标准与测试证据。

## Known issues / 已知问题

尚无应用源码，无法判断功能缺陷；目前缺少 CI 和真实环境验证能力。这是待建基础设施，不应误报为 CI 失败。

## CI status / CI 状态

未配置，未运行，不能标记 CI_VERIFIED。

## Local verification / 本地验证

尚无统一 verify 入口，未执行本地项目验证，不能标记 LOCAL_VERIFIED。

## Deployment status / 部署状态

未部署；目标环境待确认。

## Runtime verification / 运行环境验证

未执行；验证方式待技术栈和目标环境确定。

## Task status / 任务状态

`IMPLEMENTED`（针对文档写入阶段；仅在文件实际提交成功后成立）。不代表 LOCAL_VERIFIED、CI_VERIFIED 或 DONE。

## Next step / 下一步

核验 main 最新 HEAD 与文档存在性，之后确认业务/技术栈并建立真实应用与统一验证入口。每轮开发前重新读取 AGENTS.md、这五份文档及当前仓库事实。
