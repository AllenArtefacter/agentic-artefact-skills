# Google 接入：优先宿主 MCP / 连接器

本 skill 的默认接入方式是宿主提供的 Google Drive / Google Workspace 插件、连接器或 MCP，不默认安装 Google CLI 工具，也不默认要求团队 OAuth JSON 或 GCP 配置。MCP 是协议，不是唯一产品；不同实现的认证要求和能力不同。

## 1. 检查已有连接

识别当前宿主，检查实际可调用的 Google 工具及连接状态。已安装不等于已连接，已连接不等于支持所需操作。若已连接，复用，不启动第二套登录。

按本轮任务检查：指定文件夹元数据和范围内列举、原生文档读取，以及需要时的 Docs/Sheets/Slides 编辑能力。只读探测限制在用户指定项目及其子目录内；无 folder 链接时先索取，不通过整个 Drive 搜索来验证连接。不用试写验证权限。

## 2. 没有连接时由 agent 引导

- **Codex**：安装时若尚未连接，必须按 [Codex 图文接入指引](codex-google-drive-setup.md) 告知用户：设置 → 插件 → 搜索 google → 点开 Google Drive → 认证页面完成授权，并在同一回复直接展示随 skill 打包的截图。使用宿主插件发现/管理能力查找 Google Drive；读取返回的插件身份与状态，提供宿主支持的安装/连接入口或建议卡片。已安装则引导连接而不是重复安装。插件支持统一 Drive/Docs/Sheets/Slides 时不额外要求分别安装。不得把建议卡片已显示说成已安装。
- **Claude / Claude Code**：未连接的 Claude 用户按 [Claude 图文接入指引](claude-google-drive-setup.md) 操作 Settings → Connectors → Google Drive → Connect → 完成认证；在同一回复直接展示截图。截图中的勾选为已连接示例，先验证再决定是否需认证。先检查当前会话可见的连接器/MCP。优先使用该宿主现有 Google Workspace/Drive 集成；参照当前官方文档及实际 UI 引导启用。不要假设所有 Claude 客户端共享连接、权限和能力。
- **其他宿主或自定义 MCP**：查阅宿主和选定提供方的官方文档，确定准确包名、服务器 URL、安装方法和认证方式。不凭“Google MCP”名称安装未知第三方服务器，不编造 MCP URL。

能调用安装/配置工具时，先展示具体方案并询问用户，确认后由 agent 执行；宿主仅提供安装卡片或 UI 时，请用户点击对应按钮。Google 账号选择、同意授权，以及宿主要求的安装/信任确认由用户完成，不代替用户同意权限。

只给当前所需的最短步骤，说明下一步完成后 agent 会继续；不让用户手动下载 JSON 或配置 GCP，除非选定集成确实要求自带 OAuth 客户端，并已说明用户选择。不要承诺所有 MCP 都免客户端配置。

已授权工具返回真实登录 URL 时可直接提供；宿主只提供连接按钮时引导该按钮，不编造链接。连接成功后重新检查工具可用性及指定项目只读访问；需要新会话才能加载时明确说明。

## 3. 验证后继续

分别报告 skill 安装、Google 连接、当前账号（工具能够核验时）和项目可访问性。账号不可查询时如实说明，不以本地 ME.md 代替实际登录证据。完成后继续 initialize/work，所有修改仍先询问用户。

能力不足时说明缺少哪项，保留已可用的只读工作；不要立即要求换工具或扩大权限。无合适宿主集成时，说明能力缺口；经用户选择可使用 [浏览器接入](browser-access.md)。本 skill 不再分发 CLI/OAuth 自建接入路线。

Python 仅在运行本 skill 的本地脚本时需要，不是使用远程 Google 连接器的前置。安装 skill 不会启动监听器。

参考：[Claude Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)、[Claude Code MCP](https://code.claude.com/docs/en/mcp)。具体入口以当前宿主实际界面和官方文档为准。

## Required visual onboarding response

When the user needs to connect Google, send the relevant host screenshot together with the shortest click path in the same response. A code-formatted filesystem path or the sentence “the skill contains a guide” is not visual delivery. Follow the host setup guide's image-delivery rules. If images cannot render, say so briefly and provide a clickable public repository image link plus the full text steps. Do not require a separate request for the guide. Keep installation diagnostics (file counts, comparison details) secondary to the user's next action. Ask users to choose their own authorized account; do not default coworkers to the maintainer's email.

After installation, include the short capability welcome in [welcome.md](welcome.md), alongside any necessary connection steps.

## Connected but project inaccessible

Do not stop at “not found” or a list of possible causes. Provide an actionable host-specific account check. In Codex, if another account may be connected, follow [the linked-user branch](codex-google-drive-setup.md#enabled-plugin-different-connected-account): 设置 → 插件 → Google Drive → 下拉菜单 → 已链接用户 → 添加. Use the user’s own project-authorized account, preserve other connections, then retry the exact project root. Treat account mismatch as unverified unless the tool or user confirms it. Identify the actual host before choosing UI instructions.
