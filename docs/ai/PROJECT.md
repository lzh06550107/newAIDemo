# PROJECT.md — 项目架构与上下文

记录日期：2026-10-12  
仓库：https://github.com/lzh06550107/newAIDemo

## 项目定位

[已确认] 仓库目前用于建立 AI 协作、仓库事实源和文档自动验证基线。产品目标、业务边界尚未确认。

## 架构与环境

| 项目 | 当前事实 |
| --- | --- |
| 应用类型 / 平台 | 待确认 |
| 应用编程语言与框架 | 待确认 |
| 应用源码 / 模块 | 暂无；待设计 |
| 数据库、网络与外部依赖 | 待确认 |
| 应用构建、部署及真实运行环境 | 待确认 |
| 文档验证工具 | Bash + Python 3.10+ 标准库（不代表应用技术栈） |
| CI 执行环境 | GitHub-hosted ubuntu-latest；Python 3.12；由 .github/workflows/ci.yml 定义 |

## 已建立的基础设施

```text
AGENTS.md
README.md
docs/ai/{PROJECT,STATE,DECISIONS,ACCEPTANCE,TESTING}.md
scripts/ci/verify.sh
scripts/ci/check_docs.py
scripts/ci/tests/test_check_docs.py
.github/workflows/ci.yml
```

## 技术约束

- 项目开发规则参照 AGENTS.md，动态状态在 STATE.md。
- 统一验证入口为 `bash scripts/ci/verify.sh`，目前仅覆盖文档基线。
- 改变测试方式须同步验证脚本、CI 工作流和 TESTING.md。
- 未经业务决策，不创建应用框架、数据库、部署配置或假成功的应用构建测试。
