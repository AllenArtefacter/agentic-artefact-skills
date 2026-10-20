# 项目 Calendar

Google Calendar 是会议时间、参会人、重复会议和提醒的主记录，不是任务状态库。

manifest.calendar.id 填实际 Calendar ID（不是 Drive folder ID）。Calendar 权限与 Drive 权限分别配置；当前 Drive reader 不读取 Calendar。

事件描述链接会议纪要 MEET-ID 或里程碑 MS-ID；纪要保存 calendar_id + event_id，重复会议按具体 instance 关联。确认会议改期时先更新 Calendar，会议纪要记实际发生时间。任务 deadline 的主记录在 Control.Timeline；Calendar 提醒如启用，由 steward 单向映射，避免双向循环修改。

常见节奏可选：内部 weekly、客户 weekly、sprint planning / review、ad hoc catchup。不要为模板自动创建会议或邀请他人。
