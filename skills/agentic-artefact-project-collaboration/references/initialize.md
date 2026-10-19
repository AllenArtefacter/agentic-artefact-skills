# initialize — 项目经理建立团队项目

**全局限制：** 遵守 SKILL.md 的 Global restrictions：不得访问项目父目录或其他范围外目录；任何删除 / 更改先展示具体方案并询问用户。以下创建、发布、更新、归档步骤均受此限制。

先按 [dependencies.md](dependencies.md) 检查宿主 Google MCP/连接器；已有连接直接复用，否则指引安装与授权。验证指定项目的只读访问后继续。gws/gog 与团队 OAuth JSON 仅在用户选择 CLI 备用路线时使用。

这是一次项目级启动流程。已有项目的新同事加入属于 work。项目经理是通常执行者，实际以用户授权的项目设置负责人为准。

## 输入

优先读取用户提供的 brief、SOW、会议记录和客户资料，再补充缺项：

- 项目名称、客户/业务背景、问题 context。
- 愿景 vision：希望最终改变什么业务结果；与交付清单区分。
- 范围/非范围、可检验的成功标准。
- 目标 Shared Drive/新 folder 或现有空 folder；个人本地准备目录。
- 项目经理姓名/邮箱，成员姓名、邮箱、角色和具体职责；未知人员不虚构。
- 已确认的工作线、计划、日期、交付物、输入资料；未确定项明确列出。

团队侧管理员已配置的 OAuth/API 不需每个项目重做。用户凭据只在本地安全渠道配置。人员名单不构成发邀请或修改访问权限的授权。

## 执行步骤

1. **检查目标。** 验证当前 Google 身份和根目录访问；确认这是待初始化的项目。目标已有 Project.md/manifest 时，读取并采用补齐或恢复流程，不能覆盖重建。没有云端工具时只准备本地草稿。
2. **建立目录。** 默认使用用户确认的六个目录：00_Start_Here、01_Management、02_Meetings、04_Deliverables、05_Materials、90_Archive。现有项目尊重实际布局，不自动补回删去的目录。 在新的本地目录生成项目专属文件和所需工作目录；通用 README、空白模板、CSV 表头及操作指南留在 skill 中。云端有已授权写入器时在指定位置新建项目根目录或使用指定空目录，登记创建返回的 ID；避免靠同名文件判断唯一性。重试复用已创建 ID，不能生成重复套件。
3. **写 Project.md。** 将 context、vision、范围、成功标准、成员邮箱/职责、PM、协作约定和入口写成项目特定内容。为新成员分配稳定 person_id；不另建 AGENTS.md / TEAM.md / SOUL.md。
4. **写 STATUS.md。** 根据实际事实给出项目阶段、已完成的设置、未确定事项、初始阻塞和下一步；填 as_of、来源和汇总者。初始化不是交付已完成；准备完本地草稿也不是云端已发布。
5. **准备工作资料。** 填工作计划；创建/登记 Project Control 和已有输入材料。只添加已确认任务、里程碑、交付物；可选 Calendar、sprint 未配置就明示。从 skill 的 assets/control-seed 导入 CSV 表头 为同一 Sheet 的 tabs，不长期维护 CSV 副本。
6. **发布和登记。** 用真实云端 file IDs 更新 manifest；记录 Project.md、STATUS.md、工作计划、Control 和各入口。团队 Project、STATUS、计划和纪要默认发布为原生 Google Docs，不使用 .md 后缀；任务表优先 Sheets，接口不可用时可用 Docs 表格并注明。本地 Markdown 仅为草稿。团队项目索引可为原生 Docs，机器 JSON 映射保存在本机；按实际 ID 找文件。没有云端 writer 时产出本地 draft_ready，不模拟发布。
7. **回读验收。** 从实际目标根目录重新列出并读取关键文件，核对成员、链接、内容和权限内可读性。成功后才能将 initialization_status 设为 ready。初始状态摘要对应的是上线设置结果，不代表业务验收。

## 本地填充工具

`assets/initialize-brief.json` 是空白输入结构，没有虚构成员。

```sh
python3 scripts/initialize.py --brief /absolute/path/filled-brief.json --output /absolute/path/new-project-draft
```

脚本复制模板并填充两份核心 MD、人员 ID 和 manifest，返回本地 draft_ready。项目 folder URL 是输入引用，不会创建云端目录。若要创建全新云端根目录，可先由 agent 的授权写入工具创建，再把实际 ID 写入 brief；没有写入工具则将链接留为待部署的明确说明，并保持本地草稿状态。

如果目前信息不足以满足脚本必填项，agent 可先 scaffold 并生成带待确认项的草稿；不可绕过缺项，把它称为已完成初始化。

## 完成条件

**draft_ready：** 本地模板已复制，项目背景/愿景/名单已填，待配置云端事项明确。可交给 PM 审阅和后续部署。

**ready：** 目标团队文件夹实际存在；两份核心 MD 可回读；真实成员及职责已配置；Control、工作计划及必需 canonical IDs 有效；未启用的可选功能标明；用成员实际权限验证后才能声称该成员可用。未做双账号验证只报告 PM 身份下验证通过。

返回项目入口、核心文件、维护者、初始资料、尚待确认事项，以及新人使用 work 的示例。写入部分成功时列出已创建 ID 与缺失步骤，恢复时只补未完成部分。

Project 必须按 [project-metadata.md](project-metadata.md) 填写六项统一 metadata；缺失项写 TBD，Google Docs 人员使用经邮箱核实的原生 @person chip。
