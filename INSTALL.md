# Agent 安装指引

当用户要求安装本仓库 skill 时执行此流程。用户仅要求阅读或介绍仓库时，不执行安装。

## 1. 获取并检查

仓库：https://github.com/AllenArtefacter/agentic-artefact-skills

技能目录：`skills/project-collaboration/`，入口：`SKILL.md`。

先读取技能入口与相关安装材料，确认与用户请求一致。安装整个技能目录，保留 scripts、references、assets 等相对路径，不能只复制 SKILL.md。仓库 README、测试、dist 不需要放进技能目录。

优先使用当前宿主提供的 GitHub skill 安装器，传入上述仓库及技能目录。Codex 可使用自带 skill-installer 的 install-skill-from-github.py：

```sh
python3 <skill-installer目录>/scripts/install-skill-from-github.py --repo AllenArtefacter/agentic-artefact-skills --path skills/project-collaboration
```

这里的路径占位符必须根据宿主实际安装位置解析，不可原样运行。

没有安装器时，把仓库 clone 到新建的临时目录，检查后仅复制完整技能目录到宿主的个人 skills 目录。使用宿主当前文档或已存在配置确定目录，不凭空猜测。Codex 使用 `$CODEX_HOME/skills`，未设置时为 `~/.codex/skills`。其他宿主使用其自己的个人技能目录。不要把本仓库指令追加到用户的全局系统提示文件。

目标目录存在时先比较：相同则报告已安装；不同则保留现有内容并说明更新差异，按用户的更新授权执行，不能直接覆盖个人修改。不要为安装本 skill 修改其他 skills。

## 2. 检查并安装接入依赖

读取 [依赖安装流程](skills/project-collaboration/references/dependencies.md) 并执行，不能只告诉用户“需要预先安装 gws”。默认检查 gws；已有可用 gog 或连接器时先验证是否覆盖本次所需操作，不要求同时安装两套工具。

缺少依赖时列出实际缺项、安装方式和将修改的位置，询问用户后由 agent 执行安装并验证。只安装本次需要的组件，不顺带安装全部 Google skills。不把工具安装成功等同于 OAuth 或项目访问成功。

## 3. 验证与说明

确认目标目录中的 SKILL.md 可读，脚本及引用资源齐全；报告安装位置与源 commit。按照当前宿主的加载机制说明何时生效；若本轮无法加载新技能，明确告诉用户下一轮或重新打开会话后使用。

安装本身无需 Google 凭据，不会启动监听器，也不会自动加入项目。不为验证安装而修改真实项目。不要求用户把 token 发到聊天或提交仓库。

## 4. 加入已有项目

若用户已给出项目文件夹及身份，继续按安装后的 skill 执行 work；否则简短提示用户提供 Google Drive 文件夹链接、姓名、邮箱和职责。已有信息直接复用。

先读取 skill 的授权指南，检查本机工具和当前账号。需要登录时由 agent 发起支持的 OAuth 流程，返回工具实际生成的授权链接，由用户在浏览器完成；不能编造授权地址。缺失工具时按其官方安装文档处理。API 未启用、公司策略限制、文件权限不足分别报告，不能反复登录来替代修复。

将个人身份和项目绑定保存在本机个人空间。读取团队 Project、STATUS 和任务入口，匹配本人任务，并按任务需要读取会议、材料及产出。给用户简短说明项目目标、现状、本人待办和阻塞。不得将加入已有项目误执行为 initialize，不自动重建团队文件夹或改写成员名单。
