# AGENTS.md

# 项目 AI 开发宪法

> 本文件是本项目中所有 AI Agent、ChatGPT Web 会话、自动化开发流程和人工协作时必须遵守的最高级开发规则。
>
> 本文件的目标是：
>
> - 防止长对话上下文腐化；
> - 防止模型记忆、旧聊天和旧方案污染当前项目状态；
> - 防止“未执行、未验证，却宣称已经完成”的幻觉；
> - 保证项目架构、测试、CI、部署和真实环境验收都有明确事实源；
> - 让任何新的 ChatGPT / Agent 会话都可以仅依靠仓库重新恢复正确的项目上下文。
>
> **任何 Agent 在修改本项目之前，都必须先读取并遵守本文件。**

---

# 1. 最高原则：仓库事实高于聊天记忆

项目真实状态的优先级必须遵循：

```text
真实运行环境结果
    >
CI / 自动化测试结果
    >
GitHub 当前代码
    >
当前 Branch / Commit
    >
DECISIONS.md
    >
STATE.md
    >
ACCEPTANCE.md
    >
PROJECT.md
    >
TESTING.md
    >
当前聊天内容
    >
历史聊天
    >
模型 Memory
```

如果多个来源发生冲突：

1. 先以可重复验证的真实结果为准；
2. 再以 GitHub 当前代码和当前 Commit 为准；
3. 再以最新明确的项目决策文件为准；
4. 不得用历史聊天或模型记忆覆盖当前代码。

---

# 2. GitHub 是唯一正式项目事实源

以下信息不得只存在于聊天中：

- 当前分支；
- 当前 Commit；
- 当前任务；
- 已完成事项；
- 未完成事项；
- 已知问题；
- 架构说明；
- 测试方式；
- 测试命令；
- 构建方式；
- 部署方式；
- 关键技术决策；
- 已废弃方案；
- 验收条件；
- 真机验证要求。

ChatGPT Memory、Project Memory、历史 Chat、交接摘要都只能作为辅助信息。

> **项目动态状态必须最终落到仓库。**

---

# 3. 推荐仓库结构

项目推荐至少存在以下文件：

```text
repo/
├── AGENTS.md
├── README.md
│
├── docs/
│   └── ai/
│       ├── PROJECT.md
│       ├── STATE.md
│       ├── DECISIONS.md
│       ├── ACCEPTANCE.md
│       └── TESTING.md
│
├── scripts/
│   ├── ci/
│   │   ├── lint.sh
│   │   ├── test.sh
│   │   ├── build.sh
│   │   └── verify.sh
│   └── deploy/
│       └── deploy-staging.sh
│
└── .github/
    └── workflows/
        ├── ci.yml
        └── deploy.yml
```

不同语言或框架可以调整目录，但职责必须保持清晰。

---

# 4. 各文件职责

## 4.1 AGENTS.md

作用：

```text
定义所有 Agent 必须遵守的规则
```

包括：

- 事实源优先级；
- 开发流程；
- 测试规则；
- CI 规则；
- 验收规则；
- 禁止事项；
- 状态机；
- 交接规则；
- 防幻觉规则。

`AGENTS.md` 不应该承载大量具体业务逻辑或频繁变化的项目状态。

---

## 4.2 PROJECT.md

作用：

```text
描述“这个项目是什么、怎么组成”
```

应包含：

- 技术栈；
- 项目架构；
- 模块职责；
- 目录结构；
- 外部依赖；
- 运行环境；
- 构建环境；
- 数据库；
- 服务依赖；
- 网络依赖；
- 特殊硬件要求；
- 部署拓扑；
- 关键约束。

示例：

```text
Android
├── Kotlin / Java
├── Gradle
├── Android SDK
├── Camera
├── Wi-Fi
├── SQLite
└── Backend API
```

或：

```text
Web
├── Nginx
├── PHP-FPM
├── ThinkPHP / FastAdmin
├── MySQL
├── Redis
└── Frontend Assets
```

---

## 4.3 STATE.md

作用：

```text
描述“项目现在处于什么状态”
```

至少应包含：

```text
Current branch:
当前分支

Current commit:
当前 Commit SHA

Current task:
当前任务

Completed:
已完成事项

Pending:
未完成事项

Known issues:
已知问题

CI status:
当前 CI 状态

Deployment status:
当前部署状态

Runtime verification:
当前运行时验证状态

Next step:
下一步
```

Agent 不得仅凭聊天历史推断当前状态。

---

## 4.4 DECISIONS.md

作用：

```text
记录已经确认的重要技术和业务决策
```

目标：

- 防止旧方案死灰复燃；
- 防止不同聊天重复讨论同一问题；
- 防止 Agent 因上下文丢失重新做出已被否决的选择。

推荐格式：

```text
## ADR-017

日期：
2026-09-21

决定：
/clock/upload 保留原接口，
新增 client_record_id。

禁止：
不要再次删除 client_record_id。

原因：
用于客户端请求唯一性和问题追踪。

状态：
ACTIVE
```

如果历史聊天与 `DECISIONS.md` 冲突：

> **以最新且状态为 ACTIVE 的决策为准。**

---

## 4.5 ACCEPTANCE.md

作用：

```text
定义“什么条件下任务才算真正完成”
```

禁止 Agent 根据“代码看起来正确”自行判断完成。

### Web 示例

```text
首页 Banner
[ ] CI PASS
[ ] 已部署 Staging
[ ] Chrome 1920×1080 验证
[ ] Chrome 2048×1536 验证
[ ] 4K 验证
[ ] Mobile 验证
[ ] 无关键 Console Error
[ ] 无关键 404
```

### Android 示例

```text
Wi-Fi 功能
[ ] CI Build PASS
[ ] APK 构建成功
[ ] Android 12 安装成功
[ ] Runtime Permission 正常
[ ] Wi-Fi 扫描成功
[ ] Logcat 无阻断异常
```

---

## 4.6 TESTING.md

作用：

```text
描述“项目应该测试什么、测试分几层、各层入口是什么”
```

`TESTING.md` 负责说明，不应成为唯一可执行事实源。

它应包含：

- 快速检查；
- 单元测试；
- 集成测试；
- 构建测试；
- 完整验证；
- 真机测试；
- 浏览器验收；
- 各测试层的前置条件；
- 各命令的用途。

示例：

```text
快速检查：
./scripts/ci/lint.sh

单元测试：
./scripts/ci/test.sh

完整 CI 验证：
./scripts/ci/verify.sh

Android Release 构建：
./gradlew assembleRelease
```

---

# 5. 测试命令不得只存在于 Markdown

真正的测试逻辑应尽量封装成仓库中的可执行入口。

推荐：

```text
scripts/ci/
```

例如：

```bash
./scripts/ci/lint.sh
./scripts/ci/test.sh
./scripts/ci/build.sh
./scripts/ci/verify.sh
```

或者项目统一使用：

```text
make verify
```

或：

```text
npm run verify
```

或：

```text
./gradlew verify
```

---

# 6. 单一验证入口原则

项目应尽量提供一个统一完整验证入口：

```text
./scripts/ci/verify.sh
```

或者：

```text
make verify
```

所有环境优先执行同一入口：

```text
开发人员
      │
      ├── verify
      │
ChatGPT / Agent
      ├── verify
      │
GitHub Actions
      └── verify
```

目标：

> 避免本地、ChatGPT、README、GitHub Actions 四处执行不同测试逻辑。

---

# 7. 测试命令事实源优先级

Agent 不得自行猜测或发明测试命令。

测试和构建命令的事实源优先级为：

```text
1. scripts/ci/
2. Makefile / Taskfile / package scripts / Gradle tasks
3. .github/workflows/
4. docs/ai/TESTING.md
5. README.md
6. 当前聊天说明
7. 历史聊天
8. 模型记忆
```

如果存在统一验证入口：

```text
./scripts/ci/verify.sh
```

则 Agent、开发人员和 CI 都应优先使用该入口。

---

# 8. 修改测试流程时必须同步

如果修改：

- 测试命令；
- 构建命令；
- 依赖安装；
- CI 流程；
- 测试前置条件；

必须检查并同步：

```text
scripts/ci/
.github/workflows/
docs/ai/TESTING.md
```

必要时同时更新：

```text
PROJECT.md
ACCEPTANCE.md
```

禁止只改文档不改 CI，或只改 CI 不更新测试说明。

---

# 9. Agent 每轮开始前必须重新建立事实状态

每个新的 ChatGPT / Agent 会话在修改代码前必须先读取：

```text
1. AGENTS.md
2. PROJECT.md
3. STATE.md
4. DECISIONS.md
5. ACCEPTANCE.md
6. TESTING.md
7. 当前 GitHub Branch
8. 当前 Commit
9. 相关源代码
10. scripts/ci/
11. .github/workflows/
```

之后才能开始分析或修改。

禁止：

```text
“根据我们前面几百轮聊天继续改”
```

正确方式：

```text
先重新读取仓库当前事实，
建立当前项目状态，
再继续执行任务。
```

---

# 10. 新项目首次初始化流程

首次进入新项目时：

```text
AGENTS.md
    ↓
PROJECT.md
    ↓
STATE.md
    ↓
DECISIONS.md
    ↓
ACCEPTANCE.md
    ↓
TESTING.md
    ↓
GitHub Branch / Commit
    ↓
项目目录和源码
    ↓
scripts/ci/
    ↓
.github/workflows/
```

初始化完成后，Agent 应先输出：

```text
当前项目架构
当前 Branch
当前 Commit
当前任务
当前 CI 入口
当前本地验证入口
真实环境验证方式
已完成事项
未完成事项
关键决策
当前验收标准
下一步
```

首次初始化阶段默认不修改代码，除非用户明确要求直接实施。

---

# 11. 强制任务状态机

所有开发任务必须使用明确状态：

```text
PLANNED
↓
IMPLEMENTED
↓
LOCAL_VERIFIED
↓
CI_VERIFIED
↓
DEPLOYED
↓
RUNTIME_VERIFIED
↓
DONE
```

---

## 11.1 PLANNED

需求已经确认，但尚未修改代码。

---

## 11.2 IMPLEMENTED

代码已经修改，但尚未完成验证。

---

## 11.3 LOCAL_VERIFIED

已经在当前开发环境执行项目定义的快速或完整验证入口。

例如：

```text
./scripts/ci/verify.sh
```

注意：

> LOCAL_VERIFIED 不能代替 CI_VERIFIED。

---

## 11.4 CI_VERIFIED

GitHub Actions / GitHub-hosted Runner 已经对当前 Commit 验证通过。

只有 CI 对应的 Commit 与当前目标 Commit 一致时才能进入该状态。

---

## 11.5 DEPLOYED

已经部署或安装到目标运行环境。

Web：

```text
已部署到 Staging / Production
```

Android：

```text
APK 已安装到目标真机
```

---

## 11.6 RUNTIME_VERIFIED

已经在真实运行环境完成验证。

Web：

```text
浏览器实际访问与交互验收完成
```

Android：

```text
目标 Android 真机实际功能验证完成
```

---

## 11.7 DONE

只有满足 `ACCEPTANCE.md` 中全部必要条件，才能进入 DONE。

---

# 12. 禁止“无证据完成”

Agent 不得仅凭代码修改结果说：

```text
已经解决
已经修复
已经完成
确认正常
肯定没有问题
```

除非有对应证据。

---

## 12.1 正确表达示例

如果只修改代码：

```text
代码修改已完成。

当前状态：
IMPLEMENTED

尚未完成：
- 本地验证
- CI
- 运行时验收
```

如果本地测试通过：

```text
当前状态：
LOCAL_VERIFIED

本地验证通过，但 GitHub CI 尚未确认。
```

如果 CI 通过：

```text
当前状态：
CI_VERIFIED

CI 已通过，但真实运行环境尚未验收。
```

只有真实环境也验证通过后，才可以进入：

```text
RUNTIME_VERIFIED
```

满足全部验收项后：

```text
DONE
```

---

# 13. 必须区分事实、推断、未验证和建议

Bug 分析时使用以下分类：

```text
[已确认]
从代码、CI、日志、接口、数据库、页面或真机获得直接证据。

[推断]
根据当前证据形成的原因判断。

[未验证]尚未通过真实环境或直接证据确认。

[建议]
推荐的修改方案。
```

示例：

```text
[已确认]
Manifest 声明 ACCESS_FINE_LOCATION。

[已确认]
Logcat 出现 Wi-Fi 权限失败。

[推断]
问题更可能发生在 Runtime Permission 阶段。

[未验证]
Android 12 实际授权状态尚未确认。

[建议]
增加启动时权限状态检查后重新真机验证。
```

禁止把推断表述成事实。

---

# 14. 最小变更原则

每次修改应尽量只处理当前任务所需范围。

禁止：

- 顺手重构无关代码；
- 顺手修改无关页面；
- 顺手改变接口；
- 顺手改变数据库结构；
- 顺手替换技术方案；
- 顺手升级大量依赖。

除非这些修改是解决当前问题的必要条件。

如果需要架构级调整：

1. 先说明原因；
2. 更新 `DECISIONS.md`；
3. 再实施。

---

# 15. Bug 修复标准流程

```text
复现问题
    ↓
收集证据
    ↓
确认当前 Branch / Commit
    ↓
读取相关代码
    ↓
形成假设
    ↓
最小修改
    ↓
本地验证
    ↓
提交 GitHub
    ↓
CI
    ↓
真实环境验证
    ↓
更新 STATE.md
```

如果真实环境验证失败：

> 不得标记 DONE。

---

# 16. CI 是正式事实校验层

CI 不只是构建工具。

它还是：

```text
防止模型“以为正确”的自动事实校验层
```

Agent 的：

```text
“应该没问题”
```

不能代替：

```text
CI PASS
```

---

# 17. Web 项目标准开发流程

```text
ChatGPT Web
    ↓
读取仓库事实
    ↓
分析需求
    ↓
修改代码
    ↓
本地 verify
    ↓
提交 GitHub
    ↓
GitHub Actions
    ↓
GitHub-hosted Runner
    │
    ├─ checkout
    ├─ 安装依赖
    ├─ lint
    ├─ unit test
    ├─ build
    └─ verify
    ↓
CI PASS
    ↓
SSH / rsync / scp
    ↓
Linux Staging Server
    ↓
Nginx / PHP-FPM / Node / Java / DB
    ↓
浏览器验收
    ↓
满足 ACCEPTANCE.md
    ↓
DONE
```

---

# 18. Web 项目测试分层

## 第一层：开发环境

执行：

```text
快速检查
单元测试
统一 verify
```

作用：

```text
尽早发现明显错误
```

---

## 第二层：GitHub-hosted Runner

执行正式 CI：

```text
GitHub Actions
→ verify
```

只有该层通过才可进入：

```text
CI_VERIFIED
```

---

## 第三层：真实 Web 环境

部署：

```text
Staging
```

验证：

- HTTP 状态；
- 页面结构；
- JavaScript；
- Console；
- 404；
- 登录；
- 后台功能；
- API；
- 响应式；
- 用户指定浏览器；
- 用户指定分辨率。

Build PASS 不等于页面验收 PASS。

---

# 19. Android App 标准开发流程

```text
ChatGPT Web
    ↓
读取仓库事实
    ↓
修改 Android 代码
    ↓
本地可执行验证
    ↓
提交 GitHub
    ↓
GitHub Actions
    ↓
GitHub-hosted Runner
    │
    ├─ Gradle 编译
    ├─ lint
    ├─ unit test
    ├─ Manifest 检查
    ├─ dependency 检查
    └─ build
    ↓
CI PASS
    ↓
本地 Android Studio
    ↓
git pull
    ↓
确认 Commit 与 CI 一致
    ↓
Build APK
    ↓
ADB 安装
    ↓
Android 真机
    ↓
真实功能验证
    ↓
满足 ACCEPTANCE.md
    ↓
DONE
```

---

# 20. Android 测试分层

## 第一层：开发环境

可执行：

```text
Gradle 编译
Lint
Unit Test
静态检查
```

---

## 第二层：GitHub-hosted Runner

正式 CI：

```text
Gradle
Lint
Unit Test
Build
Manifest
Dependency
```

CI PASS 说明：

```text
工程和代码层基本正常
```

但不说明真机功能正常。

---

## 第三层：Android 真机

必须用于验证真实能力：

- Wi-Fi；
- Camera；
- Face Recognition；
- Runtime Permission；
- Platform Signature；
- Device Owner；
- Kiosk；
- Bluetooth；
- USB；
- NFC；
- 局域网；
- 真机性能；
- 厂商定制系统行为。

Gradle PASS 不等于 Android 真机 PASS。

---

# 21. Android Commit 一致性

真机验收前必须确认本地代码与 CI 验证的 Commit 一致。

例如：

```bash
git rev-parse HEAD
```

如果本地 Commit 与 CI Commit 不一致：

> 不得说真机测试验证的是 CI 对应版本。

---

# 22. GitHub-hosted Runner 的定位

GitHub-hosted Runner 是：

```text
临时 CI / Build / Test / Deploy 命令执行环境
```

不是：

```text
生产服务器
永久运行环境
Android 真机
```

Web：

```text
GitHub-hosted Runner
→ CI
→ SSH / rsync
→ Linux Server
```

Android：

```text
GitHub-hosted Runner
→ CI
→ Android Studio 拉取同 Commit
→ Build APK
→ ADB
→ Android 真机
```

---

# 23. 不默认使用 self-hosted Runner

除非项目明确需要：

- 内网资源；
- 特殊硬件；
- GPU；
- USB 真机；
- 固定网络；
- 私有依赖；
- 特殊操作系统；
- 无法由 GitHub-hosted Runner 访问的环境。

否则默认优先：

```text
GitHub-hosted Runner
```

---

# 24. 普通 Chat 不得假装会自动持续监控

普通 ChatGPT Web 对话结束后，不会因为 CI 失败自动重新唤醒。

因此不得声称：

```text
“我会一直自动监控 CI，失败后自动修复直到成功。”
```

除非当前项目确实配置了明确、可验证的外部自动触发机制。

默认流程：

```text
ChatGPT 修改
→ GitHub
→ CI
→ 用户再次触发
→ ChatGPT 检查 CI
→ 继续修复
```

---

# 25. 一个项目一个上下文边界

推荐：

```text
Project: jinya-website
Project: faceapk
Project: nocobase-plugin
```

不推荐：

```text
Project: 所有开发项目
```

不同项目的动态状态不得混用。

---

# 26. 一个阶段一个 Chat

不要无限延长一个开发 Chat。

出现以下情况时应开启新 Chat：

- 一个阶段已经完成；
- Branch 发生切换；
- 架构发生重大调整；
- 同一问题反复修复 3 次以上；
- 已多次出现“前面不是已经说过了吗”；
- Agent 开始重新引入旧方案；
- 当前 Chat 中已经存在多个相互冲突的旧状态；
- 已难以确认哪一个结论是最新状态。

---

# 27. 新 Chat 恢复规则

新的 Chat 不依赖旧 Chat 全量历史。

必须通过以下内容恢复上下文：

```text
AGENTS.md
PROJECT.md
STATE.md
DECISIONS.md
ACCEPTANCE.md
TESTING.md
GitHub 当前代码
Branch
Commit
scripts/ci/
.github/workflows/
```

---

# 28. 阶段结束交接规则

阶段结束时必须更新：

```text
STATE.md
```

必要时更新：

```text
DECISIONS.md
ACCEPTANCE.md
TESTING.md
PROJECT.md
```

交接内容至少包含：

```text
当前 Branch
当前 Commit
本轮修改内容
本地验证状态
CI 状态
部署状态
运行时验证状态
已完成事项
未完成事项
已知问题
下一步
```

---

# 29. 禁止事项

所有 Agent 禁止：

## 29.1 根据记忆猜当前代码

必须先读仓库。

---

## 29.2 假装执行过操作

没有实际执行时不得说：

```text
已经提交
已经测试
已经部署
已经通过 CI
已经验证
```

---

## 29.3 发明测试命令

必须依据仓库中的真实入口。

---

## 29.4 用旧聊天覆盖当前实现

当前 GitHub 代码与有效决策优先。

---

## 29.5 编译通过就宣称功能完成

```text
Build PASS ≠ Runtime PASS
```

---

## 29.6 绕过 CI 判定完成

除非用户明确要求跳过，否则正常流程必须经过 CI。

---

## 29.7 修改无关范围

遵循最小变更原则。

---

# 30. 证据优先原则

Agent 在得出结论前，应优先寻找：

```text
源代码
Git diff
CI
测试日志
应用日志
数据库
API 响应
浏览器结果
截图
Android 真机结果
```

不要优先依赖：

```text
猜测
旧聊天
Memory
“通常应该是”
```

---

# 31. 文档与脚本职责分离

统一遵循：

```text
AGENTS.md
= RULES

PROJECT.md
= ARCHITECTURE / CONTEXT

STATE.md
= CURRENT STATE

DECISIONS.md
= DECISIONS

ACCEPTANCE.md
= DEFINITION OF DONE

TESTING.md
= TESTING GUIDE

scripts/ci/
= EXECUTABLE TEST LOGIC

.github/workflows/
= CI TRIGGER + EXECUTION ENVIRONMENT
```

也可以概括为：

```text
文档描述 WHAT / WHY

脚本描述 HOW

GitHub Actions 决定 WHEN / WHERE
```

---

# 32. 最终抗腐化架构

```text
               ┌───────────────────────┐
               │      GitHub Repo      │
               │                       │
               │ AGENTS.md             │
               │ PROJECT.md            │
               │ STATE.md              │
               │ DECISIONS.md          │
               │ ACCEPTANCE.md         │
               │ TESTING.md            │
               │ scripts/ci/           │
               │ source code           │
               └──────────┬────────────┘
                          │
                          ▼
                    ChatGPT Web
                          │
                    读取当前事实
                          │
                          ▼
                      修改代码
                          │
                          ▼
                    本地 verify
                          │
                          ▼
                       GitHub
                          │
                          ▼
                    GitHub Actions
                          │
                          ▼
                GitHub-hosted Runner
                          │
                        CI
                          │
                 ┌────────┴────────┐
                 │                 │
                Web             Android
                 │                 │
             Staging          Android Studio
                 │                 │
             Browser             ADB
                 │                 │
                 │           Android 真机
                 │                 │
                 └────────┬────────┘
                          │
                    Runtime Verify
                          │
                          ▼
                    更新 STATE.md
```

---

# 33. 十条最高优先级规则

如果只读取本文件的一部分，至少必须遵守以下十条：

1. **GitHub 当前代码和真实验证结果高于聊天记忆。**
2. **每轮开发前先读取 AGENTS、PROJECT、STATE、DECISIONS、ACCEPTANCE、TESTING。**
3. **必须确认当前 Branch 和 Commit。**
4. **不得自行发明测试命令。**
5. **优先执行仓库中的统一验证入口。**
6. **本地测试通过不能代替 GitHub CI。**
7. **CI 通过不能代替真实运行环境验收。**
8. **没有证据不得声称“已经解决”。**
9. **阶段结束必须更新 STATE.md。**
10. **不要让一个 Chat 无限增长；阶段结束后用仓库状态开启新的干净 Chat。**

---

# 34. 最终目标

本项目不要求 AI：

```text
永远记住整个项目
```

而要求 AI：

```text
无论何时进入一个新的 Chat，
都能通过仓库中的事实重新建立正确上下文。
```

最终目标是：

> **把“项目记忆”从 LLM 内部迁移到版本化、可验证、可执行、可审计、可恢复的仓库中。**

任何新的 Agent，只要能够读取：

```text
AGENTS.md
PROJECT.md
STATE.md
DECISIONS.md
ACCEPTANCE.md
TESTING.md
scripts/ci/
.github/workflows/
GitHub 当前代码
```

就应该能够在不依赖漫长历史聊天的情况下，重新建立一个干净、可信、可继续执行的项目状态。