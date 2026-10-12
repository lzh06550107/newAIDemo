# TESTING.md — 测试策略与入口

## 已确认的当前情况（2026-10-12）

仓库处于文档基线阶段，暂无实际应用工程、依赖配置、可执行测试脚本、构建入口或 GitHub Actions 工作流。

| 层级 | 当前入口 | 状态 |
| --- | --- | --- |
| 快速静态检查 | 未定义 | 未配置 |
| 单元测试 | 未定义 | 未配置 |
| 集成测试 | 未定义 | 未配置 |
| 构建测试 | 未定义 | 未配置 |
| 统一验证（verify） | 未定义 | 未配置 |
| GitHub CI | 未定义 | 未配置 |
| 浏览器 / 真机运行验收 | 未定义 | 未配置 |

## 本阶段可执行的事实核验

本阶段可以通过 GitHub 查看实际 main HEAD，以及读取 AGENTS.md、README.md 和 docs/ai 下文档，逐项对照 ACCEPTANCE.md。该操作属于**仓库文件核验**，不能标记 LOCAL_VERIFIED、CI_VERIFIED 或 RUNTIME_VERIFIED。

## 确立技术栈之后

- 根据实际工程建立脚本或等价统一入口（优先 scripts/ci/verify.sh，但不得创建仅返回成功的假验证脚本）。
- 配置 GitHub Actions 调用相同实际验证入口。
- 明确依赖安装、前置条件、运行环境、单元/集成/构建测试及命令。
- 补充浏览器或真机验收方式，并将结果与目标 Commit 关联。
- 测试逻辑变动时同步更新 scripts/ci、.github/workflows、本文件及必要的 ACCEPTANCE.md、PROJECT.md。

禁止直接执行 AGENTS.md 中作为示例出现、但目前尚不存在的测试命令。
