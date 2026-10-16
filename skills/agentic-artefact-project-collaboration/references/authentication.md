# Agent 执行 Google 授权

**团队配置入口：** 先读取 [team-google-setup.md](team-google-setup.md)。本团队 OAuth 应用所属 GCP project 为 `gen-lang-client-0444403763`；配置缺失或接入失败时指引用户联系 allen.liang@artefact.com。不得仅凭 project ID 发起登录，也不得自动给普通成员新建 GCP project。

initialize 和 work 共用这个前置步骤。已有本机 gws 配置时优先复用；需要重新登录时由 agent 执行命令，用户只负责在浏览器选择账号并确认 Google 授权。不要把终端操作清单交回用户，也不要请求用户粘贴 access token、refresh token 或授权回调 code。

## 没有管理员支持时

若用户明确没有 Cloud/IT 权限，且当前问题需要项目级配置，改用 [浏览器接入](browser-access.md) 验证已有网页访问。普通 Google 网页登录不依赖本项目启用 Drive API；仍受实际文件权限约束。不要继续把 IAM/API 启用清单交给普通成员。以下是选择 API 接入时的流程。

## 0. 工具依赖

先执行 [dependencies.md](dependencies.md)：检查实际可用工具，缺少工具时由 agent 提出安装方案、取得确认并执行，不直接把安装任务交给用户。以下命令针对 gws；gog 或其他连接器按其自身文档认证，不能混用命令或凭据。

## 1. 检查

Agent 执行 `gws auth status`，必要时查看 `gws auth login --help`。不要只因配置文件存在就判断已授权。有效登录且具有本次所需权限时直接复用，并用后续只读探测核验实际账号和 folder。

本项目的默认权限需求为 Drive + Sheets（读取资料、创建项目文件和管理表）。只在确实是纯只读任务且已有相应授权时沿用只读能力；不要给 initialize 加 --readonly 后又尝试创建文件。不要使用 --full 扩大到无关服务。

## 2. 启动登录并返回真实链接

需要重登、补齐所需授权或用户明确要求重登时，agent 执行：

```sh
gws auth login --services drive,sheets
```

使用可持续运行的交互终端/PTY，短时间返回输出并保留 session ID，不能把登录子进程结束掉再交给用户一个失效链接。若本机版本出现 scope picker，按工具显示选择本任务需要的 Drive/Sheets；不要假定此 flag 会跳过全部交互。已有 OAuth client 配置时不重新执行 auth setup，也不要求重新创建 GCP 项目。

从该次进程输出提取实际 Google authorization URL，原样作为可点击 Markdown 链接交给用户，保留该次 state/redirect 等参数，不手工拼装或复用旧链接。仅展示 consent URL，绝不展示带 code/token 的回调地址或凭据。

先以可点击 Markdown 链接展示工具实际返回的授权 URL，再发送以下提示：

> 已启动 Google 授权。请打开上方授权链接，选择能访问项目文件夹的 Google 账号，并确认 Drive 和 Sheets 权限。完成后我会检查登录状态并继续。

这是一项真实浏览器操作，允许且应直接在对话中请求用户完成；不能用普通文本选择框代替 Google consent。gws 可能同时自动打开本机浏览器，仍优先给出可用的工具返回链接。若本版本只打开浏览器而没有输出 URL，明确说明已打开页面，不编造链接或未经验证的 CLI 参数。

保持回调监听进程存活，分段等候/轮询，每次不长时间阻塞沟通。等待期间可整理项目 brief 和本地模板；依赖 Google 授权的操作必须等真实成功。用户还未点击不等于取消；超时或用户拒绝时如实说明，旧链接过期后重新启动登录再给新链接，不无限重试。

## 3. 认证后验证并继续

登录进程成功返回后，agent 执行：

```sh
gws auth status
gws drive about get --params '{"fields":"user(emailAddress,displayName,permissionId)"}'
```

然后用实际 folder ID 检查可访问性和所需能力（参数由 agent 结构化构造，不能把用户字符串直接拼进 shell）：

```sh
gws drive files get --params '{"fileId":"ACTUAL_FOLDER_ID","supportsAllDrives":true,"fields":"id,name,mimeType,driveId,capabilities(canAddChildren,canEdit)"}'
```

上面的 ACTUAL_FOLDER_ID 必须替换后执行。核对返回账号与 ME.md/项目成员；新项目可先与 PM 提供的身份核对。用户说“已完成”或浏览器显示成功还不够，必须检查进程结果及 API 实际访问。

登录成功不等于文件夹具备写权限。缺权限时区分：OAuth scope、未启用 API、文件 ACL、账号不匹配、网络错误；不要对所有 403 反复要求登录。只读探测能确认当前账号和 folder，但不能声称已验证所有 Sheets 写入；执行实际授权操作时再验证结果。

## 4. 授权后直接使用 gws

gws 自行管理本机凭据。后续读写优先直接调用已登录的 gws；按安装版本的 --help / gws schema 检查具体 API 参数，然后继续 initialize 或 work。不要为适配 Python reader 而导出未掩码凭据、读取 keychain 密钥或让用户重新提供 token。

`drive_reader.py` 是独立的只读备选工具，当前不自动读取 gws 加密凭据。其 token-env/credentials-file 流程只用于用户已选择该接入方式的环境，不能在 gws 登录成功后当作第二次必需授权。使用 gws 时也要执行项目范围过滤、分页、读取新版本和写后验证；Python reader 的本地 inbox/ack 不会自动覆盖直接 gws 调用，不得声称它已经记录了本次同步。

如果 gws 未安装，先按 dependencies.md 处理安装；若 OAuth client 缺失或执行宿主不支持维持本机 OAuth 回调，报告具体缺项并给最小解决办法。只有 agent 确实无法执行时才请用户手动运行命令。已有可用连接器和授权可沿用，不创建多套重复凭据。

参考：[gws authentication](https://github.com/googleworkspace/cli#authentication)。本机已核对 login 支持 --services 和 status 子命令；本次技能修改未发起真实重新登录。

## 普通成员与管理员的职责边界

大部分项目成员不是 Google Cloud 管理员。正常成员接入仅包括个人 OAuth 浏览器授权和已授予的项目文件访问，不应要求每个人进入 IAM 设置。OAuth 配置、API 启用及确实需要的 consumer/quota project 权限由组织指定的接入维护者预先配置。

遇到 403 时，agent 先查看原始错误的 reason、permission 和 consumer/project 标识，并核对当前身份与非敏感的接入/配额项目配置。不能仅凭 403 就断言缺少 Service Usage Consumer，也不能把 OAuth client project、quota/consumer project、Shared Drive folder 当成同一个东西。若是错误选择了项目，确认目标后修正配置；不得为了绕过检查切换到未授权项目或身份。

只有错误明确指向 serviceusage.services.use 等项目使用权限，且已确认该 consumer project 是团队预期配置时，才说明需要接入维护者处理。不要向普通成员发送“打开 IAM 给自己加角色，完成后回复已配置”的要求；也不应把这当作重新 OAuth 登录能解决的问题。

向普通成员说明：个人登录是否已完成、哪个只读调用被什么错误阻塞、是否修改过团队文件。生成可转交给接入维护者的短说明，包含受影响工作邮箱、确切项目标识、调用服务、错误 reason/permission 及所需检查；不附 token、client secret 或授权回调 code。只有用户需要转交入口时才提供管理员控制台链接，并注明它不是成员操作步骤。未经明确授权不替用户发送邮件或消息。

等待团队接入配置修复期间，继续完成不依赖云端的 brief 整理、模板填充和 initialize 草稿；明确云端部署/读取尚未完成。修复后由 agent 重试原来的只读探测，验证真实可用性，再恢复 initialize/work，不要求用户做重复登录。

面向产品部署：先由接入维护者用一个非管理员成员账号完成登录、读取及所需写入试点。只有通过此验证，才能宣称“同事只需登录并选择项目 folder”。当前 skill 不能自动保证任意本机 OAuth 配置都满足这一体验。

## gws 0.22.5 的 consumer-project 403：已验证诊断路径

该版本存在额外 x-goog-user-project 请求头问题：[上游 issue #729](https://github.com/googleworkspace/cli/issues/729)。不要把这种错误直接解释为所有同事都需要 Cloud IAM 角色。

本机已做真实对照：同一已登录用户、同一加密 OAuth 凭据，原 gws 请求返回 serviceusage.services.use 403；用临时隔离配置，不继承 client_secret.json 的 project_id，也不继承环境 ADC quota project 后，Google 返回 Drive 与 Sheets API 未启用。数字项目编号替换测试也未解决原错误。此结果确认登录有效，并揭示两项问题：gws 自动显式配额项目，以及 OAuth 项目未启用所需 API。后续仍需针对实际目标验证读取；不要把本地兼容性测试视为任意账户的访问证明。

可使用已加入技能包的兼容入口进行后续 Workspace 调用：

```sh
python3 scripts/gws_workspace.py drive about get --params '{"fields":"user(emailAddress,displayName,permissionId)"}'
```

它仅在当前用户已有加密 gws OAuth 凭据时可用：临时目录引用现有加密凭据，不导出 token、不复制明文密钥、不改原配置、不修改 IAM；退出清理临时配置。Google 仍校验 OAuth scopes、API 启用、用户身份与文件 ACL。它不适用于需要显式配额项目的 Cloud API/ADC 场景，仅支持 Drive/Sheets/Docs/Slides，不代理 auth 命令。原生 gws 登录仍使用原配置。

如果返回 API 未启用，指向实际错误确认的 OAuth 项目，请组织接入维护者一次性启用 Drive 和 Sheets API，或提供已经正确配置的组织 OAuth 客户端。不是每位成员都要当管理员，也不是在浏览器重复授权能解决。不能只根据项目名称/编号外观断言是两个不同项目。

诊断调用只读取 Drive about 或使用不存在的 Sheet ID 判断 API 启用错误；Sheets 404 只能说明探测到相应处理阶段，不代表任何真实工作簿可读。管理员配置完成后，agent 必须用实际目标 folder/Sheet 回读验收，再声称接入可用。
