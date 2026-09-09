# 《金刚般若波罗蜜经》全文学习

**v0.1.0-preview** · 姚秦鸠摩罗什译通行三十二分本 · 私人学习项目

这是一套可以离线阅读、搜索和复习的《金刚经》全文学习材料。它沿用已验收的《滕王阁序》和《心经》项目模板，把全文拆成三十二个导航分、句群翻译、读音、语境、术语名句、问答和背诵卡。分段服务于学习，不冒充古本唯一章次或宗派科判。

## 开始学习

下载仓库 ZIP，解压后用本机浏览器打开 [学习入口](preview/index.html)。预览不需要安装依赖、登录或联网；GitHub 文件页面不会自动运行 HTML。本项目没有公开部署网站。

先从一个分读开始：看原文，听自己的朗读，说出句群意思，遮盖后回忆，再记录一个错点。卡片支持搜索、分类、字号、已学标记和“今天睡得不好，只复习已学卡”的轻量模式。学习记录保存在当前浏览器，使用独立的 `diamond-sutra-learned-v1` 存储键，不覆盖前两个项目。

- [完整经文](content/full-text.md) · [全文注解长图](assets/cards/classic.png) · [全文注解 HTML](assets/cards/classic.html)
- [注音与诵读](content/pronunciation.md) · [句群翻译](content/translations.md) · [人物、出处与语境](content/allusions.md)
- [术语与名句](content/idioms-and-lines.md) · [背诵方法](content/memorization.md)
- [结构伴读](content/reading-map.md) · [问答链](content/questions.md) · [白话解读](content/interpretation.md)
- [伴读与概念页面](preview/guide.html) · [全部卡片 JSON](data/cards.json)

## 内容清单

| 内容 | 数量 |
| --- | ---: |
| 三十二分原文卡 | 32 |
| 独立全文卡 | 1 |
| 句群翻译卡 | 32 |
| 注音卡 | 42 |
| 人物、出处与语境卡 | 23 |
| 经文术语与名句卡 | 22 |
| 背诵方法卡 | 8 |
| 学习卡合计 | 160 |
| 全文注解长图 | 1 |
| 无字记忆配图 | 6 |

正文共 5,179 个汉字（题署、分名、标点不计），末尾“应作如是观”偈和“信受奉行”结尾均保留。每张卡都有 Markdown、HTML、PNG 和 JSON 记录；全文注解长图由官方 `ljg-classic` 工具生成，85 张重叠切片用于视觉检查。42 个注音、23 个出处语境、22 个术语名句和 8 张记忆卡分别有独立源文件。

三十二分的导航名为：法会因由、善现启请、大乘正宗、妙行无住、如理实见、正信希有、无得无说、依法出生、一相无相、庄严净土、无为福胜、尊重正教、如法受持、离相寂灭、持经功德、能净业障、究竟无我、一体同观、法界通化、离色离相、非说所说、无法可得、净心行善、福智无比、化无所化、法身非相、无断无灭、不受不贪、威仪寂静、一合理相、知见不生、应化非真。它们是常见的学习导航名，原经没有现代卡片式标题层级。

## 底本、版本差异与校对原则

本项目选择公有领域、便于现代读者诵读的简体通行三十二分本，题署为“姚秦三藏法师鸠摩罗什译”。正文初始取自 [维基文库《金刚般若波罗蜜经（鸠摩罗什）》](https://zh.wikisource.org/zh-hans/%E9%87%91%E5%89%9B%E8%88%AC%E8%8B%A5%E6%B3%A2%E7%BE%85%E8%9C%9C%E7%B6%93%EF%BC%88%E9%B3%A9%E6%91%A9%E7%BE%85%E4%BB%80%EF%BC%89)，逐段整理为 `data/section-source.json` 和 `data/source-text.txt`。网页版本的繁体字、全形标点和版面标题不直接当作本项目正文。

参校 [CBETA T0235](https://cbetaonline.dila.edu.tw/zh/T0235) 及其 [公开 XML](https://github.com/cbeta-org/xml-p5/blob/master/T/T08/T08n0235.xml)，只取经文正文，排除藏经卷首信息、题署、校勘标记和页面导航。对照纯文字保存在 [cbeta-comparison.txt](data/cbeta-comparison.txt)，机器可读差异保存在 [version-comparison.json](verification/version-comparison.json)。

本项目采用简体和现代中文标点，统一了不影响句义的排版差异（如 `无餘`→`无余`），固定通行写法“波罗蜜”，并保留经文的“须菩提”“如是我闻”“信受奉行”等关键文字。不同传本在“无余涅槃”“波罗蜜/波罗密”、分段、引号和句读上可能有异；这里不把多个底本静默拼接。版本对照文件记录所选底本、参校对象、规范化规则和仍需人工复核的差异。卡片的三十二分标题是导航标签，不宣称是鸠摩罗什译本原有标题。

## 注释边界与学习方式

“空”“无住”“无我”“无所得”“如梦幻泡影”等解释以入门可用为目标，帮助读者观察“不要把一个概念、功德或身份抓成固定实体”的推理方向。白话稿、句群翻译和概念卡是本项目重写，不能替代不同传承的讲解、梵汉文献研究或个人宗教实践。典故与出处卡只解释经文中的譬喻、人物和论证作用，不把后世传说写成经文史实。

背诵计划按 D0/1/3/7/14/30 做间隔重复：每次三到十分钟，先朗读，再遮盖回忆，最后只修一个错点。睡眠很差时切换“只复习”模式，不强行学习新分；这是一份低压力学习建议，不是医疗方案，也不承诺改善失眠。

## LJG 技能与模板来源

本项目实际使用官方 [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills/tree/0f16badf701f8c8a788ed5942ce7b670f742f1e7) 固定 commit：`0f16badf701f8c8a788ed5942ce7b670f742f1e7`。前项目模板为已验收的 [tengwang-pavilion-preface-study](https://github.com/0xAAcodeislaw/tengwang-pavilion-preface-study) 和 [heart-sutra-study](https://github.com/0xAAcodeislaw/heart-sutra-study)。模板内容未被修改。

| 技能 | 本次实际产物 |
| --- | --- |
| `ljg-classic` | 全经原文、逐词注音/释义、句群解释、无字配图和结构解读，官方 RenderClassic / ValidateClassic 长图与切片 |
| `ljg-card` | 160 张完整卡片，官方 full template；每张先 `verify-full-text` 再 `capture`，并保留源文本与 ledger |
| `ljg-plain` | 各分句群自然白话、`content/interpretation.md` 全文白话解读 |
| `ljg-read` | 32 分结构地图、八条阅读路线、每分的执著观察和读后留白 |
| `ljg-qa` | 从法会因由到应化非真的递进问答链，回答含结论、论证步和边界 |
| `ljg-learn` | 无住布施、四相与无我、即非与是名、无所得与成就四组多维概念拆解 |

这些是工具的实际产物，不声称李继刚本人撰写、审定或宗教背书本项目。卡片模板中的署名只表示模板来源。官方工具的固定版本、输入、输出和校验记录见 `verification/`。

## 图片与记忆作用

`assets/images/` 内有六幅低干扰、无文字、无水印的水彩/水墨类比图：法会与乞食、无住布施、诸相如影、三世心不可得、庄严净土、筏喻与渡行。它们服务于记忆入口，不是佛陀或经文人物肖像、寺院复原，也不为任何教义作视觉证明。尺寸、SHA-256、提示词约束和用途见 [图片清单](assets/images/manifest.json)。

## 文件结构

```text
content/              全文、注音、翻译、出处、术语名句、记忆、伴读、问答、概念
cards/                sections / pronunciation / translations / allusions / idioms / memory
data/                 JSON、分段源文、锁定全文、CBETA 对照文字
assets/images/        六幅无字记忆类比图及 manifest
assets/cards/         160 张普通卡 + 1 张 classic 长图及对应 HTML
preview/              离线学习入口、伴读页面、样式和交互脚本
notes/                七份 Org 伴读/技能笔记
scripts/              内容生成、预览重建、渲染导出和完整性检查
verification/         文本锁定、版本比较、渲染结果、视觉报告
README.md / STATUS.md / CHANGELOG.md / LICENSE / LJG-LICENSE
```

## 检查与继续修订

```bash
python3 scripts/generate_content.py
python3 scripts/build_image_manifest.py
python3 scripts/build-preview.py
python3 scripts/check.py
```

官方渲染命令、160 张卡片的 ledger/capture 结果、全文注解长图的 85 个切片和浏览器检查记录见 [验收报告](verification/REPORT.md)。`scripts/check.py` 会检查全文字符数、分段拼接、源文 hash、JSON 字段、卡片账本、PNG/HTML、图片 hash、classic manifest、预览链接和独立存储键。

修订时从 `data/section-source.json`、`data/cards.json` 和 Markdown 源开始，并重新生成预览、卡片账本和校验结果；不要只改 PNG 或只改预览。外部出处链接需要联网，离线预览不需要。

## 许可证

代码与本项目编写的学习材料按 [MIT](LICENSE) 发布；原始佛经属于公有领域。LJG 工具和模板的来源及许可证说明见 [LJG-LICENSE](LJG-LICENSE)。各外部站点的版权、版本和使用条件以其页面为准。
