# Artefact 团队 Google OAuth 接入

- 团队接入使用的 GCP project ID：`gen-lang-client-0444403763`。
- 接入维护者：Allen Liang，联系 [allen.liang@artefact.com](mailto:allen.liang@artefact.com)。遇到配置、测试用户、API 或权限问题时联系 Allen；agent 不自动发送邮件。
- 这是 OAuth 应用所属的技术项目，不是客户项目文件夹。知道 project ID 不等于已配置登录；登录必须使用此项目下的团队 Desktop app OAuth 客户端。
- 本仓库不包含 OAuth 客户端 JSON、client secret、任何个人 token 或已登录凭据。当前没有自动分发客户端配置的地址；不能编造下载链接。

## 普通同事：由 agent 引导

1. Agent 检查 gws 和现有授权，按 authentication.md 处理。已有有效团队配置和正确账号时直接复用。
2. 缺少客户端配置时，向用户说明：请联系 Allen 获取团队 OAuth Desktop app 客户端 JSON，通过团队内部渠道保存到本机，并提供本地文件路径。不要要求用户把 JSON 内容、secret 或 token 粘贴到聊天。同事不需要创建 GCP project 或进入 IAM 给自己加权限。
3. Agent 检查提供文件的类型及非敏感项目标识，确认是 `installed` 类型，且 project_id 匹配 `gen-lang-client-0444403763`。缺字段或不匹配时先向 Allen 核实，不猜测或改写字段来伪装匹配。不要把文件内容输出到日志。
4. Agent 展示配置目标，询问确认后将该客户端文件配置到 gws 的实际配置目录；默认位置为 `~/.config/gws/client_secret.json`，如有自定义配置目录则按本机实际设置处理。已有其他应用配置时不直接覆盖；说明影响并确认隔离或迁移方案。仅分发客户端配置，不复制 Allen 的 credentials.enc、token 或密钥环。
5. Agent 按 authentication.md 启动 `gws auth login --services drive,sheets`，保持登录进程存活，返回该次真实授权链接。用户用自己的公司 Google 账号在浏览器授权。若本次操作需要 Docs / Slides 的额外 scope，应先说明并按工具实际支持的参数申请，不默认申请无关服务。
6. Agent 核验登录结果、当前账号以及用户指定项目文件夹的只读访问，然后继续 work 或 initialize。工具安装、OAuth 成功、文件夹访问分别验证；不越过项目根目录，不以试写来验证权限。

未获得团队客户端配置时，agent 可以完成 skill/工具安装，但必须明确报告认证待配置，给出 Allen 联系方式；不能声称“只需点击登录即可完成”。

## Allen / 接入维护者的一次性准备

1. 在上述 GCP project 中确认需要的 Workspace API 已启用，例如 Drive、Sheets，以及使用原生编辑 API 时需要的 Docs / Slides。
2. 配置 OAuth consent screen / audience，创建或复用 **Desktop app** 客户端，并下载客户端 JSON，通过团队内部渠道提供给成员。
3. 如果应用处于 Testing，将需要登录的同事邮箱加入 Test users。公司 Workspace 策略可能另有限制，不能保证添加测试用户就一定可登录。
4. 用普通成员账号完成登录和指定项目的只读访问试点。不要要求每位同事都拥有 GCP 管理权限。

维护者入口：[OAuth 客户端](https://console.cloud.google.com/apis/credentials?project=gen-lang-client-0444403763)、[OAuth 配置](https://console.cloud.google.com/apis/credentials/consent?project=gen-lang-client-0444403763)。普通成员无需操作这些控制台页面。

## 失败时

区分客户端配置缺失、测试用户未加入、OAuth scope、API 未启用、账号错误、Drive 文件权限与 quota/consumer project 错误。不要为了“指定项目”强行设置 quota project 或 x-goog-user-project；它不是选择 OAuth 应用的替代方式。按 authentication.md 的诊断流程处理具体错误。

给用户说明哪个步骤失败，并提供 Allen 的联系地址及可转交的错误摘要，不附 secret/token，不自动向 Allen 发消息。

参考：[gws OAuth 配置说明](https://github.com/googleworkspace/cli#manual-oauth-setup-google-cloud-console)。
