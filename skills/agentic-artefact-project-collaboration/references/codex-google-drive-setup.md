# Codex: connect Google Drive

Use this guide when a Codex user installs this skill and Google Drive is not yet connected. Reuse a working connection; do not require another login.

Tell the user:

> 在 Codex 中打开：设置 → 插件 → 搜索 `google` → 点开 **Google Drive** → 在认证页面选择能访问团队项目的 Google 账号并完成授权。完成后告诉我，我会验证项目文件夹访问并继续。

English equivalent:

> In Codex, open Settings → Plugins → search `google` → open **Google Drive** → complete Google sign-in and authorization. Use the account that can access the team project. Tell me when finished; I will verify access and continue.

![Codex Settings → Plugins → search google → Google Drive](../assets/onboarding/codex-google-drive-setup.png)

The screenshot was supplied by the project maintainer on 19 Oct 2026. It shows the plugin list, not the authorization page. A blue enabled toggle does not by itself prove authentication or project access. Do not tell users to install Gmail, Calendar or Contacts for this skill.

Show the bundled screenshot when it helps the user find the entry. Resolve its path relative to the installed skill directory; use an absolute local image path if the host supports local image display. Otherwise provide the repository image link below. Do not rely on the maintainer's original clipboard path.

Repository image: https://github.com/AllenArtefacter/agentic-artefact-skills/blob/main/skills/agentic-artefact-project-collaboration/assets/onboarding/codex-google-drive-setup.png

If the UI differs or Google Drive is absent, inspect the host plugin catalog and offer its actual install/connect entry. Do not invent buttons or auth URLs. The user completes account selection and consent. Afterward, check tool availability and read only the supplied project folder; do not inspect its parent or the entire Drive. If the new connection is not visible to the current session, explain that a new session may be needed. Report success only after the scoped read succeeds.
