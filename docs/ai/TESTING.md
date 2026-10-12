# TESTING.md — 测试策略与入口

记录日期：2026-10-12

## 当前真实入口（仅文档基线）

前置：Bash、Python 3.10+；仅使用 Python 标准库。仓库根目录执行：

```bash
bash scripts/ci/verify.sh
```

该入口顺序执行 Bash 语法检查、Python unittest 文档检查器回归测试，以及 `scripts/ci/check_docs.py` 对项目实际文档/CI 文件的校验。错误会导致非零退出。也可独立运行：

```bash
python3 -B scripts/ci/check_docs.py
python3 -B -m unittest discover -s scripts/ci/tests -p 'test_*.py' -v
```

## GitHub CI

工作流：`.github/workflows/ci.yml`。触发方式：push 到 main、pull_request、workflow_dispatch。在 GitHub-hosted Runner 上 checkout，并运行与本地相同的 `bash scripts/ci/verify.sh`。

**CI 状态以 GitHub 当前目标 Commit 的实际运行记录为准**，不能根据该文件或脚本存在推断 PASS。

## 尚未配置的测试层

| 层级 | 状态 |
| --- | --- |
| 应用 lint | 未配置，应用技术栈未确定 |
| 应用单元/集成测试 | 未配置，无业务源码 |
| 应用构建测试 | 未配置，无构建工程 |
| 部署/安装 | 未配置 |
| 浏览器/真机运行验收 | 未配置 |

未来新增应用代码时，在同一统一入口中加入真正的应用验证，并同步脚本、GitHub Actions、PROJECT.md、STATE.md、ACCEPTANCE.md 和本文件。
