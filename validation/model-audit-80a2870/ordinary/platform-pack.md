# English LinkedIn post — event operations

When registrations come through a website form, your event team needs to understand where those submissions go and how long they remain available.

FormRelay saves website-form submissions to CSV for small event organisers in the UK and France. An administrator authorises the first connection. Sync runs are at most 15 minutes apart, and each workspace retains the most recent 30 days of submissions. That sync interval is not a guarantee that every submission arrives within 15 minutes.

A simple way to understand the flow: connect a test form, submit “Demo Guest” for “Workshop A”, and check for that record in the CSV after the next sync. Then check the workspace's 30-day retention explanation.

It supports website forms; telephone and chat registrations are outside this workflow.

Understand the form-to-CSV data flow before using it for your next event.

# English X thread — technical integration

**1/5** Before connecting an event-registration form, map the data path. FormRelay supports website forms and saves submissions to CSV. It does not support telephone or chat submissions, and it is not a real-time sync service. Understand the data flow first.

**2/5** The first connection needs administrator authorisation. For the demo, use a test form with only `name` and `session`. Authorise that form connection, then submit `Demo Guest` and `Workshop A`. Use synthetic data throughout.

**3/5** Check the CSV after the next sync for that test record. Sync runs have a maximum interval of 15 minutes. This describes the spacing between runs; it does not guarantee that each submission is delivered within 15 minutes. Avoid treating the demo as a latency benchmark.

**4/5** Each workspace retains the most recent 30 days. Check that retention explanation as part of the demo and assess whether the window fits your workflow. The supplied capability does not establish an archival process beyond that window.

**5/5** The demo shows one authorised website form, one synthetic submission and its appearance in CSV after a sync. Exact UI labels and fixed wait times are not specified. Understand the complete form-to-CSV data flow before planning your integration.

# 中文四页轮播 — 逐页文字与画面

## 第1页

**完整文字：** 报名提交之后，数据去了哪里？FormRelay 面向英国与法国小型活动组织者，将网页表单提交保存到 CSV。先看清从表单到文件的数据流程，再判断是否适合自己的活动。

**画面：** 简单的数据流图，左侧为“网页报名表”，右侧为“CSV”，箭头写“同步后保存”。只使用绘制的示意图，不展示真实报名者。

## 第2页

**完整文字：** 首次连接，需要管理员授权。演示只用两个字段：name 与 session。提交一条合成报名：Demo Guest / Workshop A。电话、聊天报名不在这个流程内。

**画面：** 测试表单画面，显示两个字段及合成值；旁边写“管理员授权一次连接”。不画未经确认的具体按钮名或权限细节。

## 第3页

**完整文字：** 下一次同步后，到 CSV 中查找测试记录。两次同步运行的最大间隔为 15 分钟；这不等于每一条提交都保证在 15 分钟内送达，也不等于实时同步。

**画面：** 先显示“提交测试记录”，再显示标注“下一次同步后”的 CSV，表头为 name、session，测试行是 Demo Guest、Workshop A。用时间跳转标识，不展示假倒计时。

## 第4页

**完整文字：** 每个工作区保留最近 30 天的提交。查看保留说明，确认这个窗口是否符合你的报名管理流程。了解网页表单 → 同步 → CSV 的数据流程。

**画面：** 工作区保留说明的真实演示素材，突出“最近30天”；如尚无可拍画面，使用明确标注“示意”的文字卡。底部为了解数据流程的文字 CTA，不提供虚构链接。

# 25-second video — shootable script

**0–4 seconds.** Show a synthetic two-field website registration form. Voiceover: “Where does a website registration go?” Subtitle: “Website form → CSV”. Use the demo form only; no real attendee data.

**4–8 seconds.** Show the administrator authorising the first test-form connection, using the actual interface available during filming. Voiceover: “An administrator authorises the first connection.” Subtitle: “First connection: administrator authorisation”. Do not invent a button name or display account secrets.

**8–12 seconds.** Enter and submit `Demo Guest` in `name` and `Workshop A` in `session`. Voiceover: “Submit a synthetic test registration.” Subtitle: “Demo Guest / Workshop A”. Show the actual test submission operation; use no real names.

**12–17 seconds.** Cut to the CSV captured after the next sync and point to the matching test row. Mark the cut “After the next sync”. Voiceover: “Check the CSV after the next sync.” Subtitle: “Sync runs: at most 15 minutes apart. Per-submission delivery time is not guaranteed.” Use a previously recorded completed sync to fit the film; the edit must not imply an instant arrival or a five-second sync.

**17–21 seconds.** Show the workspace's retention explanation, or a plainly labelled illustrative card if that footage is unavailable. Voiceover: “Workspaces retain the most recent thirty days.” Subtitle: “Retention: most recent 30 days”. Do not claim a longer archive.

**21–25 seconds.** Show a flow card “Website form → sync → CSV”. Voiceover: “Understand the data flow. Website forms only.” Subtitle: “Understand the data flow • No telephone, chat or real-time sync”. No URL is supplied.

Record the actual authorised test workflow and post-sync CSV before editing. The 25 seconds are the film duration, not the workflow's elapsed time. Keep the long timing qualification readable during its shot, and verify subtitle placement does not obscure the sample row. This is a script, not a claim that footage has been filmed or published.

# French LinkedIn adaptation — event operations

Après une inscription via un formulaire web, votre équipe événementielle a besoin de savoir où vont les données et combien de temps elles restent disponibles.

FormRelay enregistre les soumissions de formulaires web dans un CSV pour les petits organisateurs d’événements au Royaume-Uni et en France. Un administrateur autorise la première connexion. Les exécutions de synchronisation sont espacées de 15 minutes au maximum, et chaque espace de travail conserve les soumissions des 30 derniers jours. Cet intervalle ne garantit pas que chaque soumission arrive en moins de 15 minutes.

Pour comprendre le parcours, connectez un formulaire de test, envoyez « Demo Guest » pour « Workshop A », puis recherchez cette ligne dans le CSV après la prochaine synchronisation. Consultez ensuite l’explication de la conservation sur 30 jours dans l’espace de travail.

Ce parcours concerne les formulaires web ; les inscriptions par téléphone ou par chat ne sont pas prises en charge.

Découvrez le parcours des données du formulaire au CSV avant de l’utiliser pour votre prochain événement.

# Internal sources and handoff

F1 supplies supported website forms, CSV saving, the 30-day retention window, the maximum 15-minute interval between sync runs and first-connection administrator authorisation. D1 supplies the two demo fields, synthetic values and post-sync observation. No conversion, productivity or per-submission latency result is claimed. All channels retain those limits; French adapts the operations message without adding capabilities.

For the third Skill handoff, provide these finished assets, F1 and D1 for channel selection and distribution planning, preserving the different operations and technical tasks. For the fifth Skill handoff, provide the shot timings, synthetic-data requirement, actual-interface capture requirement and time-jump qualification for production and creative verification. The third and fifth Skill names or contracts are not supplied here; these are bounded handoff notes, not claims that those Skills were loaded or executed. No external publication, advertising or experiment is authorised or performed.
