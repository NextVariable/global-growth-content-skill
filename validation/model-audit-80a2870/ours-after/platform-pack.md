# 内部创作说明

LinkedIn 英文短帖面向英国、法国小型活动组织者中的运营人员，解释网站报名记录进入 CSV 的路径与保留条件；英文 X 五段长串面向技术接入者，提供最小演示动作与同步边界；中文四页轮播让运营读者按页理解记录去向；25 秒视频用屏幕动作呈现连接、提交、结果和保留说明。法文版本保留 LinkedIn 的业务情境和全部事实。各版本均服务了解阶段，CTA 为了解数据流程，没有真实 URL，也不包含销售承诺。

# LinkedIn — English short post

Where does a website registration go after someone submits it?

For a small event team, FormRelay provides a CSV path for website form submissions. An administrator authorises the first connection. A test registration can then show the flow: submit “Demo Guest” for “Workshop A”, and inspect the CSV after the next sync.

The gap between sync runs is no more than 15 minutes. That is not a guarantee that each submission arrives within 15 minutes, and the flow is not real time. Each workspace retains the most recent 30 days. Phone and chat registrations are outside this workflow.

The example uses synthetic records. Start by understanding how the data moves and how the retention window fits your event’s record-keeping.

**CTA: Explore the website-form-to-CSV workflow.**

# X — English five-part thread

**1/5**
Connecting an event website form to FormRelay? Here is a minimal test of the form-to-CSV path. Use synthetic data: name = Demo Guest; session = Workshop A. This workflow supports website forms, not phone or chat registrations.

**2/5**
Have an administrator authorise the first form connection. Complete that authorisation before testing a submission. Opening the authorisation screen alone does not complete the connection.

**3/5**
Enter Demo Guest and Workshop A in the test form, then submit the record. Filling in the fields alone is not a submission. After the next sync, inspect the CSV for that test record.

**4/5**
The gap between sync runs is no more than 15 minutes. That describes run spacing, not a per-submission delivery deadline. FormRelay does not provide real-time sync. Keep those distinctions in your integration notes.

**5/5**
Each workspace retains the most recent 30 days. Check that retention information as part of the demo; do not treat the workspace as a permanent archive. Explore the website-form-to-CSV workflow to understand the data path.

# 中文轮播 — 四页完整文案与画面

## 第 1 页

**标题：网站报名提交后，记录去哪了？**

**正文：**FormRelay 将网页表单提交保存到 CSV。我们用合成报名记录演示这条路径：Demo Guest 报名 Workshop A。电话和聊天报名不在这条流程里。

**画面：**左侧是演示网站报名表，两项字段 name、session 清晰可读；右侧是 CSV 图示，以虚线箭头连接。图示标注“流程示意”，页脚标注“合成测试记录”。不使用真人照片、真实名单或未经验证的界面截图。

## 第 2 页

**标题：先完成管理员授权，再提交测试报名**

**正文：**首次连接网页表单，需要管理员完成授权。连接完成后，在演示表单填入 name：Demo Guest、session：Workshop A，并提交这条测试记录。

**画面：**分成两个连续动作区：左侧“管理员完成连接授权”，右侧“填写并提交测试表单”。用操作目的说明动作，不画出虚构按钮；若采用实际录屏截帧，须覆盖授权完成与提交动作，不用打开授权页或填好表单替代完成状态。

## 第 3 页

**标题：下一次同步后，在 CSV 中查看测试记录**

**正文：**查看 CSV 中的 Demo Guest／Workshop A 记录。两次同步运行之间的间隔不超过 15 分钟；这个间隔不保证每条提交都在 15 分钟内送达。FormRelay 不提供实时同步。

**画面：**截取经实录核验的 CSV，只显示 name、session 与该合成记录。若尚未录制，使用标明“预期演示画面”的 CSV 示意。表单提交和 CSV 结果之间放置“下一次同步后”提示，避免瞬间箭头暗示实时出现。

## 第 4 页

**标题：理解流向，也要理解保留窗口**

**正文：**每个工作区保留最近 30 天的数据。查看工作区的保留说明，判断这段窗口是否适合你的活动记录需求。

**CTA：了解网站表单到 CSV 的数据流程。**

**画面：**用“最近 30 天”的窗口图解释滚动保留范围；配上真实工作区保留说明截帧的预留区域。素材未制作时保留为标注清楚的示意，不伪造界面。CTA 仅为文案，无链接或二维码。

# 25 秒短视频 — 可拍摄脚本

**素材条件：**准备仅有 name、session 两字段的测试报名表，可由管理员授权连接的演示工作区，以及 CSV 查看画面和真实保留说明。所有提交只使用 Demo Guest／Workshop A 合成记录。预先安排能完成授权的管理员；处理任何可识别人员、账号或敏感授权信息。具体控件名称以拍摄时的真实界面为准。全片为介绍与流程演示，不拍创作者付费体验见证。

**0–4 秒：首次连接授权。**画面标注“FormRelay · website form → CSV”和“Synthetic demo”。使用真实录屏的授权关键片段：管理员执行完成连接授权的动作，并保留完成状态的画面；较长授权过程可剪辑，但不能以仅打开授权页代替完成。旁白：“First, an administrator authorises the connection.” 字幕：“Administrator authorisation required for the first connection.”

**4–9 秒：填写演示表单。**画面依次输入 name 字段的 Demo Guest、session 字段的 Workshop A，保持两项内容可读。旁白：“Enter a synthetic name and session.” 字幕：“Demo Guest · Workshop A”。

**9–12 秒：提交。**录下实际提交该测试记录的操作，停留在真实提交后画面，不补造成功消息。旁白：“Submit the test registration.” 字幕：“Submit the test record”。

**12–17 秒：跳切到下一次同步后的 CSV。**先出现“After the next sync · time jump”提示，再展示 CSV 中的 Demo Guest／Workshop A 行。旁白：“After the next sync, inspect the CSV.” 字幕分两行：“Sync-run gap: ≤15 min”／“Not a per-record deadline; not real time”。不得用 15 分钟倒计时或固定等待时长连接这两段素材；保留时间跳切标注。

**17–21 秒：查看保留说明。**打开工作区实际保留说明，取可清楚读到 30 天信息的录屏片段。旁白：“Check the workspace’s 30-day retention window.” 字幕：“Each workspace retains the most recent 30 days”。

**21–25 秒：了解 CTA。**画面为简洁尾卡“FormRelay · Website forms only”，下方“Explore the form-to-CSV workflow”。旁白：“Explore the form-to-CSV workflow.” 字幕与 CTA 同文，不加网址、二维码或额外效果信息。

**制作核验范围：**上述时长为剪辑方案，不承诺真实授权或同步能在镜头时长内完成。口播约 45 个英文词，已按脚本逐镜头作文本负载检查；未实际朗读计时、录屏或操作 FormRelay。拍摄时需核验每个动作的完成状态、字幕可读性和总时长，授权与同步等待使用明确剪辑，不加速成即时同步承诺。

# LinkedIn — Version française

Où va une inscription envoyée depuis le site de votre événement ?

Pour une petite équipe événementielle, FormRelay permet d’enregistrer les envois d’un formulaire web dans un CSV. Un administrateur autorise la première connexion. Un test permet ensuite de suivre le parcours : envoyez l’inscription « Demo Guest » pour « Workshop A », puis consultez le CSV après la synchronisation suivante.

L’intervalle entre deux exécutions de synchronisation ne dépasse pas 15 minutes. Cela ne garantit pas que chaque inscription arrive en moins de 15 minutes ; le fonctionnement n’est pas en temps réel. Chaque espace de travail conserve les données des 30 derniers jours. Les inscriptions par téléphone ou par chat ne font pas partie de ce flux.

Cet exemple utilise des données fictives. Commencez par comprendre le parcours des données et vérifier si la durée de conservation convient au suivi de votre événement.

**CTA : Découvrez le parcours du formulaire web au CSV.**

# 内部来源、状态与交接

F1 是本输入的能力来源：网页表单提交保存 CSV；每工作区最近 30 天保留；两次同步运行最大间隔 15 分钟，不是逐条送达上限；首次连接需管理员授权；不支持电话、聊天、实时同步，没有效果数字。D1 是本输入可演示资料：两字段、合成值、一次授权、提交、下一次同步后的 CSV 记录与保留说明。以上正文、翻译、图示和字幕均仅使用这些材料，没有从其他 FormRelay 场景补入事实。英文和法文都明确写成同步运行间隔不超过 15 分钟，未改成每 15 分钟至多运行一次。

这些是完整素材初稿及拍摄方案，未制作实际截图或视频，未核验当前平台发布规则，未配置 CTA 入口，未发布、投放或执行接入演示。法文为本次改写，未完成母语审阅或当地客户验证。拍摄素材必须取自上述合成测试流程，不能替换为未经授权的真实报名者资料。

第三 Skill 接收本文各平台成稿与视频分镜，面向既定英国／法国小型活动组织者及技术接入者，目的为了解流程。由其安排素材实录、核验平台要求、配置真实了解入口与必要披露后再确认发布条件；本部分不执行发布、创作者招募、激励或洽谈。

第五 Skill 接收待验证信息假设：运营短帖能否使读者理解记录去向；技术长串能否使读者复述授权、提交、同步和查看步骤；轮播与视频能否避免“15 分钟内逐条送达”和“永久存储”的误读。各版本改变的是表达任务与载体，事实边界相同。可设计一次素材理解测试，分别记录每版完成阅读或观看的人数，以及正确解释运行间隔、保留窗口和动作链的人数，明确分母为该版本完成测试的受试者；误读应记录原话。没有已实施实验、业务成功阈值或转化结果；若误读集中出现，应回到对应表达修订，而不是声称某平台天然更有效。
