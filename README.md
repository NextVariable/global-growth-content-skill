# 产品定位与增长内容 / Global Positioning & Growth Content

技能标识 `global-growth-content`，是五个海外增长 Skill 中的第二个。它把第一部分已选客户、真实工作流、价值与证据转成定位和信息主线、客户语言材料、页面与产品介绍、开发者 README、搜索内容、社媒/UGC brief 和多语言改写。每次只生成本次需要的产物，不执行发布、外联、销售或实验。

独立安装单元在 [skills/global-growth-content](skills/global-growth-content/)，入口是 [SKILL.md](skills/global-growth-content/SKILL.md)。只复制这个目录到所用客户端的技能目录，不复制整个第二部分或第一部分。当前项目内的实现没有写入全局技能目录，也不会自动覆盖已安装 Skill。调用示例：`使用 $global-growth-content，根据授权产品背景和已有 GTM 判断改写首页首屏，目标是让首次了解的客户看懂工作流。`

承接第一部分的普通交接文字或已有证据账本，沿用客户/产品/项目身份、来源 ID、证据状态、决策版本及禁止宣称项；不强制重做 GTM、不默认更换客户。第一部分的[交接模板](https://github.com/NextVariable/global-gtm-strategy-skill/blob/main/skills/global-gtm-strategy-skill/templates/handoff.md)与[证据约定](https://github.com/NextVariable/global-gtm-strategy-skill/blob/main/skills/global-gtm-strategy-skill/references/evidence-and-state.md)用于开发兼容性核对；安装单元内包含独立所需说明，不依赖这些相邻文件。

业务资料放在技能目录外的授权项目，例如根目录中已忽略的 `growth-workspaces/<client>/<product>/<project>/`。通用安装单元不含业务数据或测试产物；本模块的 `tests/fixtures/` 与 `validation/` 全部为明确标记的合成测试资料，不是用户产品事实。

在本仓库执行 `python3 scripts/validate.py`，可检查安装独立性、引用和实际测试来源一致性。可选 `--output <日志目录>` 保存检查报告。这不是文案质量评分，不检查关键词或字数来判优；语义审阅与未验证范围见 [validation/README.md](validation/README.md)。任务和条件变化输入见 [cases.json](tests/fixtures/cases.json)。

第三部分接收素材及人群/阶段/目的/CTA/渠道条件，第四部分接收价值/证明/疑虑与购买角色，第五部分接收信息假设、版本差异、预期行为与评价口径。内容完成、具备发布条件、实际发布和效果验证是不同状态。

本地实现及验证不代表客户端已安装、远端已发布或真实客户理解度已验证。许可见安装单元的 [LICENSE](skills/global-growth-content/LICENSE)。
