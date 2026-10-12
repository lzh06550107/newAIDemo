# newAIDemo

本仓库目前处于 **AI 协作基础设施初始化阶段**。已提供项目事实源文档和文档专用自动验证；业务需求、应用技术栈与产品源码仍待确定。

## 文档事实源

- [AGENTS.md](AGENTS.md)：所有 Agent 必须遵守的规则。
- [PROJECT.md](docs/ai/PROJECT.md)：项目定位、架构与技术选型状态。
- [STATE.md](docs/ai/STATE.md)：当前任务与事实状态。
- [DECISIONS.md](docs/ai/DECISIONS.md)：有效技术决策。
- [ACCEPTANCE.md](docs/ai/ACCEPTANCE.md)：阶段验收标准。
- [TESTING.md](docs/ai/TESTING.md)：真实可执行的测试入口及作用范围。

## 目前可执行的验证

在具备 Bash 和 Python 3.10+ 的环境中：

```bash
bash scripts/ci/verify.sh
```

该入口执行文档结构/链接检查及检查器的回归测试；GitHub Actions 通过 [.github/workflows/ci.yml](.github/workflows/ci.yml) 调用相同入口。**这不是应用 lint、单测、构建、部署或真机/浏览器运行验收。**

首次进入或继续开发前，读取 AGENTS.md 和上述文档，核对 GitHub main HEAD。下一阶段在确认业务目标和技术栈后扩展验证入口。
