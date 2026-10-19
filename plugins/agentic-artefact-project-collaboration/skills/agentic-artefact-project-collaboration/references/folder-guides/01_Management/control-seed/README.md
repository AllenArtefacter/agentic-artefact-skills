# Project Control 初始化表头

每个 CSV 导入同一个 Google Sheet 的同名 tab，保留 ID 列；它们是初始化种子，非运行中的独立台账。CSV 导入时作为纯文本处理输入，避免把客户文本当公式。项目数据主要由 agent 读取原生 Sheet。

时间用 ISO 8601，含时区；日期用 YYYY-MM-DD。多 ID 字段用分号分隔。ID 由类型前缀加 UUID 生成，展示时可用短名称。不得让两个人同时用“最大编号 + 1”生成 ID。

Tasks 是任务责任、deadline、状态的唯一主记录；Tasks.detail_url 是可选的详细工作说明。Deliverables 的状态在此，文档内容在主文件。需要状态变更时用 record ID 定位，先读最新值；steward 串行维护，禁止按旧行号覆写整张表。当前工具只读，不实现表格写入。

People 不记录 token 或个人 Drive 私密路径。sprint_id 可空。无交付物的内部任务允许 deliverable_ids 为空，但保留原因。模板数据为空，不推断项目已开始。

成员身份和职责以根 Project.md 为准；People 是可选派生视图，不手工维护第二套成员名单。Tasks.owner、contributors、reviewer 使用 Project.md 的 person_id；多成员字段用分号分隔。迁移旧表中邮箱时按 Project.md 已确认的完整邮箱/别名精确匹配，不按姓名推断。
