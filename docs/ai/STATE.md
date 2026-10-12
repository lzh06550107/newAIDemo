# STATE.md — 当前项目状态

记录日期：2026-10-12  
事实源：https://github.com/lzh06550107/newAIDemo

## Current branch / 当前分支

`main`（每轮都要重新核对）。

## Current commit / 当前 Commit

最近已确认的文档基线提交为 `9a3cb8933e329f13fe7f7449c859e8e13625bdf9`。本文件被修改即产生新 Commit，因此**当前 HEAD 必须实时从 GitHub 获取**，不能把此处的历史 SHA 当作最新状态。

## Current task / 当前任务

建立文档检查器、测试、统一验证入口和 GitHub Actions 工作流；尚未开始任何业务应用实现。

## Completed / 已完成事项

- 已提交并核验上传的 AGENTS.md、README.md 及五份 docs/ai 事实源文档。
- 文档基础设施脚本、回归测试和工作流已加入本阶段目标提交；对应的本地文件 SHA 与 GitHub 待提交 blob SHA 一致，提交后仍须核验 main。

## Pending / 未完成事项

- 核验新增代码与工作流在 main 上存在、可读取。
- 查看当前 Commit 的 GitHub Actions 运行结果；尚不能预设 CI PASS。
- 确认产品需求、应用平台及技术栈。
- 实施应用源码、真实构建/功能测试、部署及目标环境验收。

## Known issues / 已知问题

尚无产品代码和应用验证入口；文档检查器不能证明应用行为。此项为明确的测试覆盖范围限制，并非应用 CI 已失败的证据。

## CI status / CI 状态

文档专用 GitHub Actions 工作流在本次阶段配置；正式 CI 验证结果待 GitHub 运行记录确认。未获证据前不得标记 CI_VERIFIED。

## Local verification / 本地验证

已于 2026-10-12 在工作树执行 `bash scripts/ci/verify.sh`：5/5 回归测试通过，文档检查 PASS，退出码 0。通过 `git hash-object` 核对本地 10 个新增/更新文件的 Git blob SHA 与 GitHub 待提交 blob SHA 一致。本结果仅适用于文档检查，不代表应用本地测试通过。

## Deployment status / 部署状态

未部署；目标环境未确定。

## Runtime verification / 运行环境验证

未执行；应用类型和验收方式未确定。

## Task status / 任务状态

`LOCAL_VERIFIED`（仅文档 CI 基础设施；等待核验最新目标 Commit 的 GitHub CI）。该标签不代表应用开发任务已经 DONE。

## Next step / 下一步

确认文档验证在对应 GitHub Commit 上的 CI 结果；随后确定业务目标和应用技术栈，再扩充真正的应用测试及部署流程。
