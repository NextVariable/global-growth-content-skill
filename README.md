# 产品定位与增长内容 / Global Positioning & Growth Content

把已有目标客户、产品能力与证据转成定位、官网首屏、文章、开发者 README 和社媒内容。适合已经知道产品服务谁、需要讲清价值与使用方式的团队；每次只完成你需要的产物。

## 获取与安装

```sh
git clone https://github.com/NextVariable/global-growth-content-skill.git
cd global-growth-content-skill
```

将完整的 [skills/global-growth-content](skills/global-growth-content/) 目录复制到客户端已配置的 Skill 目录，保留里面所有文件。已有同名目录时先核对版本，不直接覆盖。重新加载后确认客户端能识别 `$global-growth-content`；不同客户端的目录和加载方式以其实际配置为准，目前没有验证所有客户端自动发现。

使用这份 Markdown Skill 不需要安装 Python 包或独立服务，模型及工具由客户端提供。Python 和 Git 仅用于仓库的开发检查。

## 第一次任务

最少提供目标读者、已确认能力、读者现有做法、所需产物及真实下一步。没有访谈、数据或购买证明可以直接说明，Skill仍可生成基于能力的初稿。

下面是合成示例，不是真实客户资料：

```text
使用 $global-growth-content，为我们的CSV对账工具写英文官网首屏。
目标读者：每月核对订单表的财务人员。
现有做法：人工对照两份CSV。
已确认能力：按订单编号匹配，列出状态差异和单侧缺失记录。
限制：不回写原表，不判断是否漏款，结果需要人工核验。
证据：只有上述已确认能力，没有客户效果数据。
下一步：查看随附流程说明，目前没有公开URL。
```

应得到完整标题、副标题和下一步文案，能解释工具如何帮助复核；没有URL时给待配置入口，不编链接。待确认资料与来源说明放在独立内部注释，不用它们取代正文。生成初稿不等于内容已发布或效果已验证。

## 范围与交接

这是五个海外增长 Skill 中的第二个，标识为 `global-growth-content`。它承接已有市场和客户判断，不重新选择市场；处理定位、产品营销页面、采用内容和改写，不执行实际发布、外联、投放、销售或增长实验。

第一部分交接可以是普通文字，也可使用现有证据账本；本Skill独立安装，不需要第一部分脚本或相邻文件。开发兼容资料见第一部分的[交接模板](https://github.com/NextVariable/global-gtm-strategy-skill/blob/main/skills/global-gtm-strategy-skill/templates/handoff.md)。后续发布、成交和实验分别交第三、第四、第五部分。项目资料保存到用户授权的位置，不放进通用安装单元。

## 检查与当前限制

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

检查覆盖安装单元、部分历史运行记录、公开副本完整性及当前候选文件；不评价文案效果，不检测全部Git历史。具体范围见[验证说明](validation/README.md)。独立复制和结构检查已经执行；最新一轮对75fb824方法重新运行三组合成任务、连续更新，并按实际问题定向修订复测，见[最新审查](validation/model-audit-75fb824/report.md)；[f7e9d15审查](validation/model-audit-f7e9d15/report.md)保留为历史。精确后端模型设置不可见，不能据此宣称公平胜出；客户端首次内容任务及真实用户反馈仍未验收。旧隔离记录冲突的对照不用于公平比较；历史隐私清理仍待单独处理。仓库是公开可用原型，不宣称成熟、全面领先或增长效果已验证。

完整开发档案和未完成对照在本地私有保存，已知失败修复及必要复现记录暂保留公开。记录精简不代表清除了旧提交中的资料。项目采用 [MIT](LICENSE)，安装单元含自己的 [LICENSE](skills/global-growth-content/LICENSE)。
