# Agentic Artefact Skills

面向 Artefact 团队/客户项目的 Google Drive 协作 skill，支持 Codex、Claude Code 等 agent。仅在明确点名 skill 或明确指定 Artefact 团队项目时使用，不适用于员工的私人项目。当前版本：**0.8.0**。

## 给 agent 一个链接即可安装

把下面这句话发给 Codex / Claude Code 等支持本地 skills 的 agent：

> 请安装 https://github.com/AllenArtefacter/agentic-artefact-skills 中的 agentic-artefact-project-collaboration skill，先读取仓库 INSTALL.md 并按指引执行。

安装后加入已有项目：

> 使用 agentic-artefact-project-collaboration 的 work 模式，项目是【Google Drive 文件夹链接】。我是【姓名】，邮箱【邮箱】，职责【职责】。

也可以将两句话合并发送。安装 skill 与 Google 授权是两个步骤；不需要用户手动 clone 或复制文件。执行 agent 需要联网和本地文件写入能力，私有仓库还需要 GitHub 访问权限。

## 安装与连接

[INSTALL.md](INSTALL.md) 是 agent 的统一安装入口。用户不需要手动下载 ZIP。

1. Agent 安装 skill，检查当前宿主已有的 Google Drive / Workspace MCP 或连接器。
2. 已连接则直接验证；未连接时，agent 提供安装/连接入口，并执行宿主允许且用户确认的配置。
3. 用户完成必要的安装确认和 Google 浏览器授权，agent 验证指定项目访问后继续 work。

**默认不需要 gws/gog、团队 OAuth JSON 或自行配置 GCP。** MCP/连接器的具体能力和认证方式以所选实现为准；没有合适集成时才询问是否使用 CLI 或浏览器备用路线。

接入问题联系 [allen.liang@artefact.com](mailto:allen.liang@artefact.com)。自带 OAuth 的 CLI 备用方案仍保留在 [团队配置指南](skills/agentic-artefact-project-collaboration/references/team-google-setup.md)，不再作为新人默认步骤。

## 两个入口

### initialize

> 使用 agentic-artefact-project-collaboration 初始化这个项目 folder。项目背景是……，成员和职责是……。

Agent 检查身份和目录，准备项目上下文、人员、状态、计划及任务入口，发布后回读验证。已有项目采用补齐流程，不覆盖重建。生成本地草稿不代表已发布。

### work

> 我是……，邮箱是……。使用 agentic-artefact-project-collaboration 对这个项目执行 work，告诉我目前需要做什么。

Agent 读取个人 ME.md、团队 Project 和 STATUS，定位本人负责/参与/审核任务，只读取本轮需要的资料。完成授权的工作后更新产出和状态，回读核验。

## 默认资料布局

团队正文使用原生 **Google Docs**；结构化任务表优先 **Google Sheets**；汇报使用 **Google Slides**。Sheets 不可用时允许 Docs 任务表并说明限制。Project 和 STATUS 是逻辑名称，不要求 `.md` 后缀。

```text
Project                 Google Doc：背景、范围、成员与职责
STATUS                  Google Doc：当前进展、阻塞、下一步
00_Start_Here/          项目索引及入口
01_Management/          工作计划、任务和决策
02_Meetings/            内部、客户、catchup 纪要
04_Deliverables/        报告及正式产出
05_Materials/           输入与参考资料
90_Archive/             旧版和归档
```

尊重已有项目实际结构，不自动补回被删目录。通用说明、流程和空白模板只放在 skill 内。离线空间全部属于个人；个人草稿不会自动上传。

项目索引是低频维护的导航。文件版本、修改时间由 Drive 管理；当前用户、读取进度、同步游标和机器映射保存在各自本机。

## 全局限制

- 仅访问指定项目文件夹及其子目录，不得访问父目录、同级目录或整个 Drive。
- 所有删除 / 更改先展示具体方案并询问用户，确认后执行；包含新建、上传、重命名、移动、归档与状态更新。
- 这是 skill 的行为规范，不替代 Drive 权限隔离。

## 能力与限制

- 优先通过宿主 Google MCP/连接器执行已确认操作；按实际工具验证 Drive / Docs / Sheets / Slides 能力。gws/gog 仅为可选备用。
- 本地 scaffold / initialize 脚本仅生成 Markdown / JSON 草稿，发布时转换或填充为原生 Google 文件。
- 独立 Python reader 支持项目范围清单、内容读取、全量清单差异和本地确认，不执行云端写入；它与 gws 使用独立凭据入口和同步状态。
- 浏览器是 API 受阻时的备用入口，不能绕过文件权限。
- 不含通用的一键云端部署器、事务化写入协调器、Changes API 增量 worker 或后台通知服务。任务分工不等于访问权限。
- 单账号 Drive 读写、文件移动和原生 Docs 转换已在项目试点验证；不代表任意公司策略或多账号场景已通过。单元测试使用模拟 API。

## 本地草稿与测试

```sh
python3 skills/agentic-artefact-project-collaboration/scripts/scaffold.py --space team --output /absolute/path/new-draft --name "Example project" --folder GOOGLE_FOLDER_URL
python3 skills/agentic-artefact-project-collaboration/scripts/initialize.py --brief /absolute/path/brief.json --output /absolute/path/filled-draft
python3 -m unittest discover -s tests -p 'test_project_collaboration.py'
```

brief 结构见 `skills/agentic-artefact-project-collaboration/assets/initialize-brief.json`。输出目录必须不存在。

[Skill 入口](skills/agentic-artefact-project-collaboration/SKILL.md) · [授权](skills/agentic-artefact-project-collaboration/references/authentication.md) · [空间模型](skills/agentic-artefact-project-collaboration/references/workspace-model.md) · [读取器](skills/agentic-artefact-project-collaboration/references/google-reader.md)

## 发布内容

只包含可复用 skill、空白模板、脚本、测试和说明；不包含客户资料、项目成员名单、客户项目文件夹 ID、个人 ME.md 或任何登录凭据。包含经维护者指定公开的团队 GCP project ID 和接入联系邮箱。原仓库许可证见 LICENSE。
