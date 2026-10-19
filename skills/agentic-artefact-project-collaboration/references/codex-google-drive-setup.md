# Codex: connect Google Drive

Use this guide when a Codex user installs this skill and Google Drive is not yet connected. Reuse a working connection; do not require another login.

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
