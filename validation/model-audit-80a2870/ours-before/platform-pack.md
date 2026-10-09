# Public LinkedIn post — event operations, English

Before an event, it helps to know where a website registration goes after someone submits it.

FormRelay saves website-form submissions to CSV. In the demo, an administrator authorises the form connection, then a synthetic registration—Demo Guest, Workshop A—appears in the CSV after the next sync. Each workspace retains the latest 30 days.

The interval between sync runs is no more than 15 minutes; that is not a guaranteed delivery deadline for each submission. FormRelay does not cover phone or chat registrations, or provide real-time sync.

See the data workflow: form submission, sync, CSV and retention.

# Public LinkedIn post — event operations, French

Avant un événement, il est utile de savoir où va une inscription envoyée depuis votre formulaire web.

FormRelay enregistre les soumissions de formulaires web dans un fichier CSV. Dans la démonstration, un administrateur autorise la connexion du formulaire, puis une inscription fictive — Demo Guest, Workshop A — apparaît dans le CSV après la synchronisation suivante. Chaque espace de travail conserve les données des 30 derniers jours.

L’intervalle entre deux synchronisations ne dépasse pas 15 minutes ; cela ne garantit pas un délai de réception pour chaque soumission. FormRelay ne prend pas en charge les inscriptions par téléphone ou par messagerie, ni la synchronisation en temps réel.

Découvrez le parcours des données : envoi du formulaire, synchronisation, CSV et conservation.

# Public X thread — technical setup, English

**1/5** Connecting an event website form to FormRelay? Follow the data path first: website submission → sync → CSV. The demo uses synthetic data, so you can explain the flow without showing real attendee details.

**2/5** The first connection needs administrator authorisation. Use the demo form with just name and session fields. Authorise its connection once, then submit Demo Guest / Workshop A as a test record.

**3/5** After the next sync, check the CSV for Demo Guest / Workshop A. Sync runs are no more than 15 minutes apart. This describes the interval between runs, not a guaranteed delivery time for any individual submission.

**4/5** Check the workspace’s retention information: it keeps the latest 30 days. Plan how that window fits your process. FormRelay supports website forms, not phone or chat submissions, and does not provide real-time sync.

**5/5** A useful setup check traces one synthetic record from the authorised form to the CSV and checks the retention window. See the data workflow to understand what happens at each stage before connecting your event form.

# Public carousel — Chinese, four complete pages

## 第1页

**标题：网站报名提交后，记录去了哪里？**

**正文：FormRelay把网页表单提交保存为CSV。先用一条合成报名记录看懂数据路径：表单提交 → 同步 → CSV。电话和聊天报名不在这个流程里。**

**画面：展示三格数据路径示意图，分别标“网页表单”“同步”“CSV”；表单只显示 name 和 session 两个字段。配角标“合成演示，无真人报名资料”。这是一张流程示意，不冒充产品界面。**

## 第2页

**标题：第一次连接，需要管理员授权**

**正文：管理员先授权演示表单连接，再提交 name：Demo Guest、session：Workshop A。首次授权是连接条件；提交表单不等于记录已出现在CSV。**

**画面：使用实际演示连接授权界面及填写两字段的画面；只有完成真实授权后才使用完成状态截图。不得自造按钮名。数据仅限上述合成值，遮去无关账号信息。**

## 第3页

**标题：下一次同步后，核对CSV记录**

**正文：在CSV中检查Demo Guest / Workshop A。两次同步运行的间隔不超过15分钟，这不保证每条提交都在15分钟内送达，也不是实时同步。**

**画面：CSV中突出显示合成记录；表单提交与CSV结果之间用明显“下一次同步后”的转场。不要用秒表或即时闪现暗示实时送达。**

## 第4页

**标题：还要看工作区的数据保留窗口**

**正文：每个工作区保留最近30天的记录。了解这段窗口如何适配活动流程，再安排后续工作。了解数据流程：从网页表单、同步、CSV，到保留期限。**

**画面：展示实际工作区30天保留说明的截屏，突出“最近30天”；下方放文字CTA“了解数据流程”，不放虚构链接、二维码或未确认的归档按钮。**

# Public 25-second video — operations demonstration

**0–4 seconds.** Shot: a close view of the synthetic demo form with the name and session fields visible. No real attendee records. Voiceover: “Where does a website registration go?” Caption: “FormRelay: website form → sync → CSV.”

**4–9 seconds.** Shot: show the administrator authorising the first form connection, then show the form filled with Demo Guest / Workshop A. Voiceover: “An administrator authorises the connection. Submit a synthetic test.” Caption: “First connection: administrator authorisation. Test: Demo Guest / Workshop A.” Use the actual interface; do not label an invented button.

**9–14 seconds.** Shot: a clearly labelled transition to footage taken after the next actual sync, then the matching synthetic CSV record. Voiceover: “After the next sync, check the CSV.” Caption: “After the next sync — elapsed time omitted.” The cut must not imply the record arrived instantly.

**14–20 seconds.** Shot: hold the CSV and overlay the timing statement as a graphic rather than pretending it is an actual interface label. Voiceover: “Runs are at most fifteen minutes apart; individual delivery is not guaranteed.” Caption: “Sync-run interval ≤15 min. No per-submission delivery deadline. Not real-time.”

**20–25 seconds.** Shot: show the actual workspace retention explanation and end on the data-path graphic. Voiceover: “Thirty-day retention. See the data workflow.” Caption: “Latest 30 days per workspace. Website forms only; no phone or chat. See the data workflow.”

# Internal sources, conditions and handoff

F1 supports website-form-to-CSV storage, the latest 30-day workspace retention window, a maximum 15-minute interval between sync runs, administrator authorisation for first connection, and the exclusions. D1 supports the specific two-field synthetic demonstration, authorisation, submission, appearance after the next sync and viewing the retention explanation. All language versions preserve the distinction between run interval and individual delivery. French wording “ne dépasse pas 15 minutes” deliberately states the maximum interval directly.

LinkedIn addresses an operator’s need to understand where registrations go; X gives a technical setup trace; the carousel explains stages visually; the video demonstrates those stages with explicit elapsed-time omission. All serve the fixed UK/French event-organiser audience at the awareness stage and lead to understanding the data workflow. No real URL is supplied or claimed. These are finished copy and production instructions, not produced footage or published posts.

Production requires authorised actual UI captures, a working demonstration connection, synthetic-only form and CSV data, and an actual post-sync result. Retention screenshots must reflect F1. No administrator identity, real registration or unrelated workspace data may appear. The narrator describes a demonstration rather than giving a fabricated personal testimonial. The five-second final frame may need careful typography; current platform dimensions, posting limits and native-language audience reception were not externally verified under this frozen task. The script's 25 seconds is the edit duration, not sync duration.

For the third Skill, transfer the full assets, audience, awareness objective, data-workflow CTA, unconfigured destinations and unproduced footage conditions. Creator recruitment, incentives and publishing remain outside this task. For the fifth, the content hypothesis is that tracing one synthetic record helps readers distinguish submission, sync, CSV and retention. The expected observable behaviour is a reader accurately explaining administrator setup, the sync-interval boundary and the 30-day window. Any evaluation should measure correct answers per exposed reader within a specified session; no test, threshold validation or growth effect has been performed.
