# 项目状态

目标：以已验收的滕王阁与心经项目为模板，完成《金刚般若波罗蜜经》全文 `v0.1.2-preview` 修订版，并发布到 `0xAAcodeislaw` 的私有仓库。

- [x] 锁定通行简体三十二分本，保留全文与“信受奉行”结尾。
- [x] 参校 CBETA T0235 XML，记录版本差异、规范化规则和源文 hash。
- [x] 完成 32 分原文卡、32 句群翻译卡、42 注音卡、23 出处语境卡、22 术语名句卡、8 背诵方法卡。
- [x] 完成全文白话、结构地图、递进问答、四组概念拆解和七份 Org 技能笔记。
- [x] 生成六幅无字、无水印、低干扰记忆配图并写入图片 manifest。
- [x] 修复全文注解长图：按 32 分句群翻译原经文，移除占位注释；官方 `ljg-classic` 验证为 1080 × 72341，54 张重叠切片，注释覆盖率 100%。
- [x] 将主 PNG 做 256 色表压缩，保持原尺寸与文字布局，文件约 4.7 MB，适合手机和 GitHub 图片查看器；原始渲染 hash 已写入 manifest。
- [x] 使用官方 `ljg-card` 模板完成 160 张卡片的 ledger 校验和 PNG capture。
- [x] 完成离线 `preview/index.html`、`preview/guide.html`、样式、搜索/筛选/字号/已学及低压力复习模式。
- [x] 运行本地完整性检查、代表性卡片视觉检查和离线预览交互检查。
- [x] 创建 `0xAAcodeislaw/diamond-sutra-study` 私有仓库。
- [x] 推送 `main` 分支和 `v0.1.0-preview` 标签。
- [x] 远端复验可见性为 `PRIVATE`、默认分支为 `main`，且远端 tag 与 main 可读取。

本次修订另保留 `verification/translation-sources.md`，记录 CBETA T0235、通行白话译文与历代注疏的交叉复核来源。旧的 `v0.1.0-preview`、`v0.1.1-preview` 标签均保留为历史版本；本次移动端修订使用新的 `v0.1.2-preview` 标签。

当前工作区没有凭证阻塞；GitHub 发布步骤沿用 Codex 当前已认证身份，不使用云浏览器，也不输出密码、Token 或验证码。

远端：<https://github.com/0xAAcodeislaw/diamond-sutra-study>。发布完成后若继续修改正文、卡片或图片，应创建新的版本标签，不要覆盖本标签。
