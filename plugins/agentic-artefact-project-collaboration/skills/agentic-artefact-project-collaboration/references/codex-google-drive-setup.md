# Codex: connect Google Drive

Use this guide when Codex Google Drive is missing, disconnected, or connected but unable to access the specified project. Reuse a verified working connection; an enabled plugin alone is not proof of the correct account.

Tell the user:

> 在 Codex 中打开：设置 → 插件 → 搜索 `google` → 点开 **Google Drive** → 在认证页面选择能访问团队项目的 Google 账号并完成授权。完成后告诉我，我会验证项目文件夹访问并继续。

English equivalent:

> In Codex, open Settings → Plugins → search `google` → open **Google Drive** → complete Google sign-in and authorization. Use the account that can access the team project. Tell me when finished; I will verify access and continue.

![Codex Settings → Plugins → search google → Google Drive](../assets/onboarding/codex-google-drive-setup.png)

The screenshot was supplied by the project maintainer on 19 Oct 2026. It shows the plugin list, not the authorization page. A blue enabled toggle does not by itself prove authentication or project access. Do not tell users to install Gmail, Calendar or Contacts for this skill.

Display the screenshot directly in the same reply as the connection steps whenever onboarding is required. Do not merely mention its location or output a path in backticks. Resolve `assets/onboarding/codex-google-drive-setup.png` from the installed skill root.

- If the host supports user-visible local images, use its native image attachment/display method or a Markdown image with the absolute local path. Reading an image with an inspection tool alone does not ensure the user sees it.
- If the host supports remote Markdown images, use:

![Codex Google Drive connection guide](https://raw.githubusercontent.com/AllenArtefacter/agentic-artefact-skills/main/skills/agentic-artefact-project-collaboration/assets/onboarding/codex-google-drive-setup.png)

- If neither image mode is available, explain that the client cannot display the image inline and include this clickable fallback along with the steps:

[Open the illustrated connection guide](https://github.com/AllenArtefacter/agentic-artefact-skills/blob/main/skills/agentic-artefact-project-collaboration/assets/onboarding/codex-google-drive-setup.png)

Never give only a container-local path such as `/root/...` that the user may be unable to open. Never claim the image was displayed if the interface only returned a path. Do not change account permissions or authentication behavior to work around rendering limitations.

If the UI differs or Google Drive is absent, inspect the host plugin catalog and offer its actual install/connect entry. Do not invent buttons or auth URLs. The user completes account selection and consent. Afterward, check tool availability and read only the supplied project folder; do not inspect its parent or the entire Drive. If the new connection is not visible to the current session, explain that a new session may be needed. Report success only after the scoped read succeeds.

## Enabled plugin, different connected account

When Google Drive is already enabled but another Google account is connected, do not ask the user to reinstall or toggle the plugin. Use this maintainer-confirmed Codex path:

> 在 Codex 中打开 **设置 → 插件 → Google Drive → 下拉菜单 → 已链接用户 → 添加**，选择**你自己有项目访问权限的 Google 账号**并完成授权。如果该账号已在列表中，先核对它是否为本次使用的连接，按界面提供的选择入口操作。完成后告诉我，我会重新读取你提供的项目文件夹。

English: **Settings → Plugins → Google Drive → dropdown → Linked users → Add**, then authorize your own Google account with access to the project. Preserve other existing connections; do not disconnect them automatically.

If the plugin responds but the target folder returns not found/empty, provide this concrete next step when an account mismatch is possible. A 404 or empty result alone does not prove the wrong account: the link, file availability or permissions may also be responsible. When the tool cannot reveal the active account, say so and ask the user to check Linked users instead of asserting an identity.

After account selection/authorization, retry the exact folder ID read and scoped listing. If access still fails, have the user verify the same URL with that account and request access from the project owner if needed. Do not scan parent folders, broaden Google scopes or use a different tool to bypass missing access. If tool discovery remains stale, explain that a new session may be needed.

The bundled screenshot illustrates the plugin entry only; it does not show the Linked users dropdown. Give the full textual path above and do not claim the screenshot demonstrates the account-add step. This branch is Codex-specific: the Claude screenshot or a ~/.claude path does not establish the current host. Route by the actual client, and do not give Codex settings steps to a Claude user.
