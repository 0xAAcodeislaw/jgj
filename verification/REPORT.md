# `v0.1.0-preview` 验收记录

## 内容与来源

- 正文：5,179 个汉字，32 个导航分，首尾与 `data/source-text.txt` 锁定一致。
- 底本：简体通行三十二分本；参校 CBETA T0235 XML。繁简、句读、`无余` 和“波罗蜜”等规范化规则见 `verification/version-comparison.json`。
- 卡片：160 张，分为 32 原文、32 翻译、42 注音、23 出处语境、22 术语名句、8 背诵方法和 1 张独立全文卡。
- 技能笔记：7 份 Org 文件，覆盖 `ljg-classic`、`ljg-card`、`ljg-plain`、`ljg-read`、`ljg-qa`、`ljg-learn` 与伴读流程。

## 官方 LJG 渲染

固定技能版本：`0f16badf701f8c8a788ed5942ce7b670f742f1e7`。

`ljg-classic` 输入 `data/classic.json`，输出 `assets/cards/classic.html` 与 `assets/cards/classic.png`。官方 `ValidateClassic.ts` 结果：`status=valid`，PNG `1080 × 113147`，`tokenCount=2041`，`annotationCount=1524`，`annotationCoverage=1`，`interpretationParagraphs=8`，`heroPresent=true`，`qaSlices=85`。85 张切片保存在 `verification/classic-slices/`。

`ljg-card` 使用官方 full template。160 张普通卡均先通过 `verify-full-text.ts`，再由 `capture.ts` 生成 PNG；每张卡的源文本和 block ledger 在 `verification/card-sources/`、`verification/card-ledgers/`。普通卡与 classic 长图合计 161 个 1080 像素宽 PNG/HTML 文件。

## 图片与预览

`assets/images/manifest.json` 记录 6 幅 1536 × 1024 的无字、无水印、低干扰类比图及 SHA-256。用途分别对应法会乞食、无住布施、诸相如影、三世心不可得、庄严净土和筏喻渡行。

`preview/index.html` 与 `preview/guide.html` 为静态离线入口；`app.js` 提供搜索、分类筛选、字号、已学标记、低压力复习和 hash 导航。已学记录使用 `diamond-sutra-learned-v1`，与前两个项目隔离。

## 可重复检查

```bash
python3 scripts/generate_content.py
python3 scripts/build_image_manifest.py
python3 scripts/build-preview.py
python3 scripts/check.py
```

最终检查应输出 `status: pass`，并报告 `cards=160`、`sections=32`、`annotations=1524`、`rendered_cards=161`、`illustrations=6`、`chars=5179`。官方工具需要在拥有 Chromium 权限的本机环境运行；普通结构检查和预览不需要联网。

视觉抽查覆盖 classic 首部、中部和尾部切片，以及普通卡的原文、翻译、术语和记忆类别。图片作为学习锚点，不被当作经文正文、历史肖像或教义证明。
