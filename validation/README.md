# 验证范围与复现

公开记录中的本机定位信息已脱敏；原始文件保留在本地忽略目录，未覆盖。输入和输出的原始 SHA 保持不变，公开副本的 SHA 与转换范围另记在 [public-export.json](public-export.json)。校验同时核对原始哈希身份和公开副本字节，不能将脱敏副本称为逐字原稿，也不能把位置脱敏当成新的模型执行。`snapshot://`、`local-comparator://`、`local-tool://` 与 `runtime://` 仅为记录中的逻辑定位符，不是安装依赖或可执行命令。

对提交80a2870新增方法的后续实际运行审查见 [model-audit-80a2870/report.md](model-audit-80a2870/report.md)：三组同输入原稿、逐任务加载记录、匿名语义审查、连续变更、修订与独立上下文复测均另存。该记录补充原有合成案例测试，不覆盖旧稿，不以原稿完整性检查宣称内容质量合格。

输入在 [cases.json](../tests/fixtures/cases.json)。全部为合成产品、合成访谈/付款与冻结竞品材料；真实任务类型执行不等于真实客户研究。覆盖无客户 B2B、已有付费但表达混乱、消费 App、开发者工具、硬件订阅、多语言多平台，以及客户改变、角色差异、无效果证据、迁移、竞品更新、局部改写、了解 CTA、交接冲突和搜索内容。

相同输入分别由普通提示执行者与 Skill 执行者完成，原始产物按 case ID 保存在 `baseline/` 和 `skill-v1/`；输入/输出 SHA256 保存在各组 `manifest.json`。普通提示执行者使用不继承编写历史的新上下文，只获得任务输入与开发者源码；先前可能继承编写历史的普通提示执行已中止，未作为对照。Skill 执行者获得入口与按需方法，不获得预期答案或普通提示结果。一次执行不构成统计性模型比较。

语义评价关注产品/任务是否可理解、差异是否与购买有关、证明是否支持主张、角色与迁移条件、CTA 和后续交接可用性。开发验证脚本只检查可移植安装单元、链接、案例覆盖及哈希一致性，不把标题/关键词/长度转换成质量评分。原输出保留不覆盖，修复后另存版本及修订依据。

结构复现：仓库根目录 `python3 scripts/validate.py --output .validation-output`。开发者例子：进入 `tests/fixtures/devtool/` 后运行 `python3 csvpeek.py sample.csv`，期望输出 JSON 的表头 `order_id,total` 和行数 2。此工具只证明该 README 示例可运行，不验证任意真实开源产品。

仍未验证真实客户理解度、转化/留存改善、搜索排名/AI 引用、母语市场认知与平台发布、真实硬件部署或集成。持续集成已接入第二部分入口，但本地成功不能称远端多系统运行已成功；当前也未全局安装或对外发布。

完整对照见 [comparison.md](comparison.md)，盲审原结果见 [blind-review.md](blind-review.md)，修复记录见 [review-notes.md](review-notes.md)。初版14对原稿均保留；修复后另存4个重新执行产物 `skill-v2/`，两项上游来源/授权追加任务保存在 `followup/`，均有输入输出哈希。例子实际复跑日志在 [devtool-execution.json](devtool-execution.json)，安装隔离检查在 [package-checks.json](package-checks.json)。

单组14项共享测试上下文；Skill初轮为整个套件读取了六份方法，再按任务使用，并没有逐任务模型上下文隔离。修复复跑使用新的无历史上下文，但四项仍在同一执行者中处理。首轮入口字节哈希未捕获，期间修过状态条款；这些限制已经记录，不能称完整冻结、可重复的模型性能实验。哈希只防无意改写，不证明内容质量或来源真实。

四项复跑独立复审见 [retest-review.md](retest-review.md)。其中多语言v2仍将“最大同步间隔”写成有最大频率歧义的英法措辞，追加修正方法并单独复跑为 `skill-v3/multilingual.md`；v2不是最终可采用稿。原始输出和失败均不覆盖，最终使用哪版以审阅记录为准。

最终采用稿：B2B、冲突交接、硬件场景使用 `skill-v2/` 对应文件；多语言使用 [skill-v3/multilingual.md](skill-v3/multilingual.md)；其余10项保留 `skill-v1/` 原稿。独立复审已确认已发现问题在这些修复稿中消失，没有把该结论升级成真实客户或增长验证。原始普通提示和所有失败稿仍可查，禁止用最终选稿覆盖历史。

本地验证汇总见 [check-results.json](check-results.json)，原始输出哈希改写检测见 [provenance-tamper-check.json](provenance-tamper-check.json)。检测通过意味着确实能识别原稿被改写，不意味着语义自动判优。[implementation-manifest.json](implementation-manifest.json) 是2026-10-09早期实现的历史快照；后续方法修订快照见 [model-audit-80a2870/revised-snapshot.json](model-audit-80a2870/revised-snapshot.json)，不能用历史快照当当前版本验收。
