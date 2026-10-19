# 业务事件（后续写入适配器使用）

一事件一 JSON：event_id、operation_id、actor、occurred_at、kind、file_id、source_version、affected_ids、summary。放入 events 子目录。摘要权限不得比原文件更宽。

当前 reader 使用本地文件清单比较，未生成本目录事件，也未实现 Changes API。读、轮询、已读确认不产生团队事件。
