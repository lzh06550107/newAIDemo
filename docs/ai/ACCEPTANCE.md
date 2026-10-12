# ACCEPTANCE.md — 验收标准

## 阶段 1：仓库文档事实源（已通过 GitHub 文件核验）

- [x] main 有 Commit，AGENTS.md 与用户上传的原文一致。
- [x] README.md 与 docs/ai 五份文档在 main 可读取。
- [x] STATE.md 能区分已完成、待办、CI、部署、运行时验证。

记录：2026-10-12；此前文档基线提交 `c847b83b2fd0505a640ea29e873e2ffd7886e58a` 完成 GitHub API 核验。

## 阶段 2：文档自动检查基础设施

- [x] `scripts/ci/verify.sh` 有可执行的真实检查逻辑，不是无条件通过。
- [x] 检查器能检查缺失文件、STATE 必需栏目和失效相对链接。
- [x] 回归测试覆盖正常样例与失败样例，实际执行通过。
- [x] GitHub Actions 工作流引用同一验证入口。
- [x] 仓库 main 上的脚本、工作流、相关文档可读取。
- [ ] 当前目标 Commit 的 GitHub Actions 检查实际 PASS（才可称 CI_VERIFIED）。

以上项目应按实际核验结果勾选，不得把工作流文件存在等同于 CI PASS。

## 未来：应用功能验收（待定义）

待确认业务目标后，逐项定义应用期望行为、边界情况、实际构建/测试入口、对应 Commit CI、部署/安装、浏览器或真机验收。文档 CI PASS 不构成应用任务 DONE。
