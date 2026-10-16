# 可选 CLI 接入（非默认）

仅在宿主集成不可用、能力不足且用户选择 CLI 备用路线时执行。以下“默认”仅指已选 CLI 路线内部优先使用 gws，不适用于整个 skill。

# 接入依赖检查与安装

本流程供仓库 INSTALL.md 和已安装 skill 的 initialize / work 共用。遵守 SKILL.md 的全局限制；安装或修改本机依赖前列出具体方案并取得确认。用户已明确确认同一安装方案时不重复询问。

## 选择工具

- 默认使用 gws（Google Workspace CLI）。先检查可执行文件及 `gws --version`、`gws --help`；已有可用版本则复用，不自动升级。
- gog 是另一个独立 CLI，不是 gws 的依赖。已有 gog 或其他已授权连接器时，按其实际帮助与文档确认是否支持本次 Drive / Docs / Sheets / Slides 操作。支持则可复用；不把 gws 命令直接套给 gog，不假定二者共享凭据。
- 无可用接入工具时，默认准备 gws 安装方案。不要同时安装 gws 和 gog，也不要仅因机器上存在 gog 就认为已能读取项目。
- Python 3.10+ 仅在执行本 skill 的 Python 脚本时需要。Node/npm 仅是 gws 的一种安装途径，不是使用预编译 gws 二进制的强制前置。

## 由 agent 执行安装

1. 检查操作系统、架构、现有工具与包管理器，不输出凭据。
2. 查阅 [gws 上游安装说明](https://github.com/googleworkspace/cli#installation)，选择适合当前机器的方式。已有 Homebrew 时可用 `brew install googleworkspace-cli`；已有符合上游要求的 Node/npm 时可用 `npm install -g @googleworkspace/cli`；也可从上游 Releases 下载匹配系统和架构的预编译二进制到用户可写位置。具体以当前上游文档为准。
3. 展示所选命令、组件、目标位置及是否需要 PATH 调整，询问用户确认。不要同时执行多个安装方案，不自动 sudo 或覆盖现有配置。
4. 确认后由 agent 执行，检查退出状态，再运行 `gws --version` / `gws --help` 验证。若 PATH 尚未生效，使用实际安装绝对路径核验，报告所需后续步骤。
5. 失败时报告具体错误。仅当当前宿主确实不能执行安装时，才将最小手动步骤交给用户。

用户明确选择 gog 时使用 [gog 上游安装说明](https://github.com/openclaw/gogcli)，确认后执行对应安装；不将 gog 包装成必需依赖。

## 接入验收

工具就绪后进入 [authentication.md](authentication.md)。gws 的 OAuth 命令仅适用于 gws；其他接入工具遵循其自身登录流程，同时保留相同项目范围和写入确认限制。

OAuth client 缺失时，向团队接入维护者获取正确配置途径；不要求每位同事新建 GCP 项目，也不把 client secret、token 收集到聊天。API 未启用和公司策略限制不能靠安装另一个 CLI 解决。

分别报告：skill 安装状态、CLI/连接器状态、OAuth 状态、指定项目只读探测结果。未给项目链接时，可完成安装和工具检查，但不能声称项目 context 已加载。安装不启动后台服务。
