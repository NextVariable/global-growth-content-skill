![Growth Content — five independent growth skills](docs/assets/cover.svg)

# Growth Content

**产品定位与增长内容 · 把已确认的产品价值，写成客户看得懂、信得过、知道下一步怎么做的内容。**

[![Validate](https://github.com/NextVariable/global-growth-content-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/NextVariable/global-growth-content-skill/actions/workflows/validate.yml) [![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Agent Skills](https://img.shields.io/badge/Agent_Skills-compatible-6e56cf.svg)](https://agentskills.io/specification)

[快速开始](#quick-start) · [任务示例](examples/first-task.md) · [方法](#method) · [验证](#validation) · [五个 Skill 合集](https://github.com/NextVariable/global-growth-skills)

输入 **目标读者、真实能力与限制、证明材料、内容类型、下一步入口**，得到 **定位、官网与落地页、文章、开发者 README、社媒与视频脚本**。可以独立使用；已有项目资料或其他 Skill 的交接都能直接接入。指令以中文编写，对客产物按目标受众选择语言。

## In practice

> Choose which return reasons to investigate first.
>
> 机制说明保留手动 CSV 导入、原因与 SKU 汇总、手动 PDF 导出；用已获授权的匿名引语，不增加省时、营收或退款改善数字。

以上是合成任务的结果节选。[查看输入和完整任务说明 →](examples/first-task.md)

## Quick start

在你的项目目录运行，选择要安装到的客户端：

```sh
npx skills add NextVariable/global-growth-content-skill --skill global-growth-content
```

需要跨项目使用时加 `-g`。此安装方式需要 Node.js 22.20+；也可以直接复制技能目录。

<details>
<summary>手动安装到 Codex（Git；已有目录时停止）</summary>

```sh
git clone https://github.com/NextVariable/global-growth-content-skill.git
cd global-growth-content-skill
mkdir -p "$HOME/.agents/skills"
target="$HOME/.agents/skills/global-growth-content"
if [ -e "$target" ] || [ -L "$target" ]; then
  echo "Already exists: $target"
else
  cp -R skills/global-growth-content "$target"
fi
```

完整保留 `skills/global-growth-content/` 内的方法、模板和许可。已有同名目录时先保存旧版及个人修改，再比较版本；不要把两份目录直接合并。其他客户端使用其配置的 Skill 目录。

</details>

重新加载客户端后调用 `$global-growth-content`。纯 Markdown 方法，无需 Python、服务或专用密钥。

```text
使用 $global-growth-content。
产品与当前阶段：……
这次要解决：……
已确认的能力、材料和限制：……
可投入的时间、预算与人员：……
请完成我需要的产物；未知的关键条件明确说明。
```

项目资料保存在你自己的工作目录，安装包只放通用方法。实际外发、发布、支出或客户系统操作依赖相应工具和授权。

## Method

入口只保留任务判断和必要边界，按需加载相关方法，不要求每次读完或跑完整个流程。

| 方法 | 解决什么 |
|---|---|
| [定位与客户语言](skills/global-growth-content/references/positioning-and-language.md) | 从工作任务、机制与购买差异组织主张 |
| [页面与对比](skills/global-growth-content/references/pages-and-comparisons.md) | 首屏、场景、功能、比较与迁移条件 |
| [开发者采用](skills/global-growth-content/references/developer-adoption.md) | 可运行的快速开始、输入输出和失败恢复 |
| [搜索内容](skills/global-growth-content/references/search-content.md) | 选题、内容 brief、教程、对比与证据 |
| [改写与本地化](skills/global-growth-content/references/adaptation.md) | 完整社媒成稿、镜头动作和多语言表达 |
| [版本与交接](skills/global-growth-content/references/provenance-and-handoff.md) | 追踪事实变化，修订受影响资产并交接 |

## Validation

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate.py
```

[验证说明](validation/README.md)区分结构与记录检查、计算测试、模型任务和真实业务结果。自动检查不替代语义审阅；合成试用不能证明获客、收入或留存提升。客户端实际加载、目标用户理解和业务效果应在自己的环境验证。

## Ecosystem

[01 市场战略](https://github.com/NextVariable/global-gtm-strategy-skill) → [02 定位内容](https://github.com/NextVariable/global-growth-content-skill) → [03 发布获客](https://github.com/NextVariable/global-launch-acquisition-skill) → [04 客户增长](https://github.com/NextVariable/global-sales-retention-skill) → [05 实验复盘](https://github.com/NextVariable/global-growth-experiments-skill)

五个独立仓库，按当前问题选用。共享产品背景、证据与版本，结果可以回到前面的决策；其他四个不是安装依赖。

## Contributing

改进建议请带一个具体任务、期望结果和实际问题。开发、检查与提交方式见 [CONTRIBUTING.md](CONTRIBUTING.md)；功能问题可提交 [Issue](https://github.com/NextVariable/global-growth-content-skill/issues/new/choose)。

## English

Turn product facts and customer context into positioning, pages, developer READMEs, articles, social posts and video scripts. Content stays specific to the audience, mechanism and available proof. Install the complete skill directory and invoke `$global-growth-content`. Instructions are Chinese-first; deliverables follow the target audience. Model and external tools are supplied by your client.

[MIT](LICENSE). 安装和再分发时保留随包许可文件。
