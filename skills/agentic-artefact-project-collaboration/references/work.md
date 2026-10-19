# work — 成员获取上下文、执行和更新

**全局限制：** 遵守 SKILL.md 的 Global restrictions：不得访问项目父目录或其他范围外目录；任何删除 / 更改先展示具体方案并询问用户。以下创建、发布、更新、归档步骤均受此限制。

先按 [dependencies.md](dependencies.md) 检查宿主 Google MCP/连接器；已有连接直接复用，否则指引安装与授权。验证指定项目的只读访问后继续。

既用于新同事第一次加入，也用于成员每天继续工作。已有团队项目不重复 initialize。

## 第一次加入（work 的准备阶段）

1. 指定团队 folder、个人本地 workspace 和本人 Google 连接（不收集 token）。
2. 必要时复制 local-personal 模板，创建 ME.md；先列出团队文件并读 Project.md，从正式成员表确认 person_id、邮箱和职责。姓名/邮箱缺失时补问本人，不新建一份团队成员身份。
3. 优先使用当前宿主的 Google MCP/连接器关联目标 folder 并核对可查询的连接账户。Google 账号、本人声明和团队成员信息冲突时先说明；可继续不依赖个人归属的一般阅读。
4. 个人端只保留 ME.md 作为必读身份入口；团队端只保留 Project.md / STATUS.md 两份必读上下文。

## 云端格式

Project 与 STATUS 默认是原生 Google Docs，名称不带 .md；下文 .md 名称也包括对应原生文档。优先读取项目索引和实际 file ID；本机模板不代表云端存在同名 Markdown。不得把已归档的迁移旧版当作主记录。

## 每轮 work

### 获取 context

- 用实际连接器检查文件变化，记录最后成功扫描时间；本地仅记录实际已读取文件的版本和时间。
- 读 ME.md → Project.md → STATUS.md；首次或布局变化时读 manifest 和 skill 中的目录指引。
- 按 [task-tracking.md](task-tracking.md) 读 Tasks Sheet，按经确认的 Owner 芯片邮箱匹配本人任务，Backlog 建议单列；再读相关任务依赖、材料和会议/决策来源。
- STATUS.md 是摘要，如果比源表旧就重读源表，不能把旧摘要当当前事实。
- 以当前用户请求确定本轮工作，不能看到一个变化就自动执行无关任务。

### 执行与产出

- 在个人 working 区进行分析、开发、整理和草稿。
- 需要共享时依据对象类型选择团队位置，参照 skill 的目录指引；项目确有专属说明时再读取。
- 保留 TASK / MAT / DEL / MEET / DEC 关联、输入版本及验证证据。复杂任务才需要独立说明文档。
- 写入前遵守 SKILL.md 的全局限制：列出具体更改并先询问用户；只有明确确认的变更才可执行。

### 更新团队资料

| 发生的事情 | 更新哪里 |
|---|---|
| 会议结束 | 会议纪要；人或 AI 记录的待确认行动进入 Backlog；人工确认后进入 Tasks；决策保留在纪要/Decisions 并互链 |
| 任务推进、阻塞或完成 | Tasks 的 Status、Description 依据和 Deliverables；不新增旧版 Control 专属列 |
| 新产出或评审结果 | 交付主内容 + Deliverables 目录索引 + 对应 Tasks 的 Deliverables 链接 |
| 新收到客户材料 | Materials 目录索引 + 原始输入目录 |
| 项目重要进展、阻塞、优先级变化 | STATUS.md 对应部分，刷新 as_of 和来源 |
| 确认的范围、愿景、成员或职责变化 | Project.md 对应部分，更新 updated_at 和依据 |
| 仅个人笔记/偏好变化 | ME.md 的个人关注或个人 working，不自动发布 |

更新前读取最新版本；按 ID 定位，不凭文件名或旧行号整份覆写。先验证内容写入，再更新对应状态。STATUS.md 只做有来源的局部汇总，由项目负责人/指定汇总者协调；每次读取、微小文字修正无需重新生成整个摘要。Project.md 不作为日常流水账。

### 结束与交接

- 回读验证实际共享结果，记录 file ID/URL、任务状态和证据。
- 内容成功、状态更新失败时明确部分成功，仅补缺失步骤。
- 无 cloud writer 时完成个人产出与 outbox 提案，列出目标 ID、修改内容和证据；不得称为共享已更新。
- 在个人 ME.md 的可选关注部分留下必要的下一步，避免复制团队任务全表。
- 记录已读取的版本；其他成员下次运行 work 时重新检查变化。未配置后台机制就不声称实时通知。

## 结束报告

本轮做了什么；写入的实际文件与状态；验证结果；仍在个人空间的待发布内容；依赖/阻塞与下一步。把“完成工作”“发布成功”“审核通过”“客户接受”分别报告。


## Meeting layout

Use 02_Meetings/raw and 02_Meetings/note. Follow [meeting-notes.md](meeting-notes.md) for source-linked notes and the single running Meeting Briefs document. Create the brief when there is real meeting content; do not publish blank templates.

材料和产出变更时，按 [folder-indexes.md](folder-indexes.md) 更新目录索引及关联任务。

## STATUS presentation

Use native Google Docs date chips for known status-as-of, edited and event dates; preserve any known time/timezone. Keep the status-as-of date distinct from the edit date. Do not append a PM field to the STATUS header. Unknown dates remain TBD; do not invent dates or use literal @date text as a chip. Verify dateElement readback.
