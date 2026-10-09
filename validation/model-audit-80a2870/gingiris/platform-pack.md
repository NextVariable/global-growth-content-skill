# Public drafts — synthetic FormRelay demonstration

## LinkedIn short post — English, event operators

Before your next event, trace one website registration all the way to the CSV your team will use.

FormRelay saves website-form submissions to CSV. In our synthetic demonstration, an administrator authorises the first connection, then we submit “Demo Guest” for “Workshop A” and check that record after the next sync.

Each workspace retains the most recent 30 days. Sync runs are at most 15 minutes apart; that is not a promise that every submission reaches the CSV within 15 minutes. Telephone and chat registrations are outside this workflow.

See the data workflow before deciding how it fits your event operations.

## X thread — English, technical integrators, five posts

### Post 1
Trace the handoff, not just the form: FormRelay saves website-form submissions to CSV. This synthetic demo follows one record through connection authorisation, submission and the next sync. See the data workflow.

### Post 2
The first form connection requires administrator authorisation. For the demo, use only two fields: name and session. Submit name = Demo Guest and session = Workshop A. These are synthetic records, not attendee data.

### Post 3
After the next sync, check the CSV for Demo Guest / Workshop A. The maximum interval between sync runs is 15 minutes. That interval is not a guaranteed delivery deadline for each submission, and the workflow is not real-time.

### Post 4
Check the workspace's retention information too: it keeps the most recent 30 days. Build your review around that window. FormRelay supports website forms; telephone and chat registrations are not covered.

### Post 5
A useful first check is whether the authorised form's test fields appear in the CSV after sync. This demo makes no promise about conversion or faster event operations. See the data workflow, including authorisation, sync and retention.

## 四页中文轮播 — 逐页正文与画面

### 第1页

页面完整文字：“报名提交以后，记录去哪了？用一条合成报名，看 FormRelay 的网页表单到 CSV 流程。了解数据流程。”

画面：左侧绘制仅含 name、session 两字段的测试报名表，右侧绘制 CSV 表格轮廓，中间用“下一次同步”箭头连接。底部注明“合成演示记录”。不添加真人头像或未确认按钮。

### 第2页

页面完整文字：“先连接，再提交。首次连接需要管理员授权。本次测试只填 name：Demo Guest；session：Workshop A。这里只演示网页表单，不包含电话或聊天报名。”

画面：管理员授权节点 → 两字段测试表。字段值完整可读；授权节点是说明图，不模拟未知的权限弹窗或按钮名称。

### 第3页

页面完整文字：“下一次同步后，去 CSV 核对这条记录。两次同步运行的最大间隔为15分钟。这不是每条提交15分钟内送达的保证，也不是实时同步。”

画面：CSV 展示 name、session 两列及 Demo Guest / Workshop A 一行；旁边用“提交 → 下一次同步 → CSV核对”流程图。无15分钟倒计时、即时到达动画或送达保证。

### 第4页

页面完整文字：“核对记录，也核对保留窗口。每个工作区保留最近30天的数据。把管理员授权、同步节奏和保留说明一起看，再判断是否适合你的活动流程。了解数据流程。”

画面：工作区保留说明特写与30天窗口示意；页脚重复“合成演示，无真人报名资料”。不添加下载、预约或转化承诺。

## 可拍25秒视频 — 分镜、口播、字幕

### 0–3秒

操作/画面：显示测试报名表，name 与 session 两字段可见，画面角落全程显示“Synthetic demo”。

旁白：“Where does a website sign-up go?”

字幕：“FormRelay: form → CSV”

### 3–7秒

操作/画面：使用经授权的测试环境录制管理员完成首次表单连接授权；不命名未提供的按钮。若尚无真实授权界面素材，拍说明卡“Administrator authorisation required”并标注流程说明，不伪装成实际点击。

旁白：“An administrator authorises the first connection.”

字幕：“First connection: administrator authorisation”

### 7–11秒

操作/画面：填入 Demo Guest / Workshop A，提交测试报名表。

旁白：“Submit Demo Guest for Workshop A.”

字幕：“name: Demo Guest | session: Workshop A”

### 11–16秒

操作/画面：剪切到下一次同步后的 CSV，框出同一行。剪切处明确显示“After the next sync — waiting omitted”。不显示固定等待秒数。

旁白：“After the next sync, check the CSV.”

字幕：“Sync runs: maximum 15 minutes apart. No per-submission delivery guarantee.”

### 16–21秒

操作/画面：工作区30天保留说明特写；素材未取得时使用清楚标为说明的文字卡，不冒充界面。

旁白：“The workspace retains the most recent thirty days.”

字幕：“Retention: most recent 30 days | Not real-time”

### 21–25秒

操作/画面：回到表单 → 同步 → CSV → 保留窗口的四节点流程卡。

旁白：“Website forms only. See the data workflow.”

字幕：“Website forms only — no phone or chat | See the data workflow”

拍摄素材条件：仅使用D1合成记录、测试表单、获授权的演示工作区和屏幕录制；检查画面不出现真实报名者或其他工作区信息。获得授权完成与下一次同步后的真实片段后才可拼接成操作演示。当前交付的是25秒脚本，未拍成片、未执行同步；25秒是剪辑时长，不是端到端等待耗时。无需真人肖像、第三方音乐或生成假用户体验。

## LinkedIn short post — French adaptation

Avant votre prochain événement, suivez une inscription sur votre site jusqu’au fichier CSV que votre équipe utilisera.

FormRelay enregistre les soumissions de formulaires web dans un CSV. Dans notre démonstration avec des données fictives, un administrateur autorise la connexion initiale. Nous inscrivons ensuite « Demo Guest » à « Workshop A », puis vérifions cette ligne après la synchronisation suivante.

Chaque espace de travail conserve les données des 30 derniers jours. Les synchronisations sont espacées de 15 minutes au maximum ; cela ne garantit pas que chaque soumission arrive dans le CSV sous 15 minutes. Les inscriptions par téléphone et par chat ne sont pas prises en charge.

Découvrez le parcours des données avant de décider comment l’intégrer à l’organisation de vos événements.

# Internal sources and handoff

F1 supplies capability, administrator authorisation, 30-day retention and maximum 15-minute interval between sync runs. D1 supplies only the name/session synthetic demo and its sequence. No existing published blog, precise UI buttons, delivery SLA, effect figures, wait time or real URL exists in this case. gr-social-distill's blog-repurposing entry therefore only partly fits; its platform differentiation is used without inventing a blog. The user's five X posts and four carousel pages override the longer templates. gingiris-ugc-matrix and full-sop supply hook → demo → CTA structure; recruitment, account expansion, US-first market changes and publishing are outside the task.

第三部分交接：接收这些完整文案与D1/F1来源标记，准备合成演示素材，核实实际授权界面、CSV结果与保留说明；不得从脚本推断已录制或真实用户效果。第五部分交接：如后续另获实验授权，可检查活动运营者能否复述数据去向、技术接入者能否识别授权/间隔/保留边界；当前没有实验、发布、投放或效果验证。英文、法文、中文页面与视频口播/字幕均采用同一能力口径。
