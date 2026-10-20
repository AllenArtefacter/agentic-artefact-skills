---
schema_version: 1
identity_source: online_personal
identity_source_ref: null
name: null
primary_email: null
email_aliases: []
timezone: null
updated_at: null
project_membership:
  team_root_id_or_url: "{{PROJECT_FOLDER}}"
  project_id: null
  person_id: null
  declared_roles: []
  declared_workstream_ids: []
  responsibilities: []
---

# 我是谁

请由本人填写真实信息。project_id/person_id 从团队 manifest 和 Project.md 获取，不在个人空间另造同一个项目的成员 ID。角色和职责可以多项。

## 我的身份与本项目职责

上方 name / primary_email 用于身份确认；email_aliases 只写已确认别名。responsibilities 说明我负责什么，例如分析交付、模型评估或数据管道；以真实项目约定填写。

## 身份来源

默认本地 ME.md 是个人入口。若决定以线上个人 ME.md 为主档，将 identity_source 改为 online_personal，identity_source_ref 填明确 file ID/URL。本地保留指针，不把两份资料当成独立主档。线上模板未发布前同样只是个人本地草稿。

## 如何找到我的任务

1. 用 person_id 对应 Project.md 成员，交叉核对完整邮箱与已登记别名。
2. person_id 尚未填写时，用完整邮箱匹配唯一成员，再使用其 person_id；重名或多个匹配请本人确认。
3. 读取 Project Timeline 的 Timeline 页，以已确认的本人邮箱匹配 Owner 芯片；Backlog 中的候选任务单独列出。旧版 Control 表按实际 schema 读取。
4. 未完成优先；blocked、到期/逾期和等待我 review 的事项分别标注。done/cancelled 按用户需求查历史。
5. roles/workstream_ids 用于发现相关事项，不构成自动分配；相关但未分配的任务单独列出。
6. owner/邮箱冲突、账号使用他人身份或职责变化未确认时明确说明，不能静默改身份或认领任务。

时间判断使用明确的当前日期和时区；缺少截止日期不能推断成逾期。

## 我的当前关注（可选）

可记录本人的工作重点与 TASK-ID，但不复制团队任务状态。开始工作时先读本文件，再读团队 Project.md / STATUS.md 并同步任务来源。个人关注不等于已分配任务。
