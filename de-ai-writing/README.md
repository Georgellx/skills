# 双语去 AI 味写作 Skill

一个面向 Codex/AI agent 的写作 skill，用来审读和改写中英文草稿里的 AI 腔、机翻腔和过度模板化表达。

它的目标不是绕过检测器，也不是给文字随机加口语词，而是帮助 agent 找到文本里真正让人觉得“像模型输出”的地方：过度工整的结构、空泛判断、意义拔高、机械连接词、英文 AI vocabulary clusters、中文公文腔和事实边界被抹平等。

## What It Does

- 审读中文、英文或中英混排文本里的 AI 味信号。
- 按需做轻度润色、深度重写、平台语气适配或作者样本拟合。
- 保留事实边界，不编造数据、案例、引用、经历或信源。
- 对学术、商务、博客、邮件、演讲稿、社媒文案等场景做不同程度的克制处理。
- 明确拒绝“规避检测器”“掩盖代写”“伪装学术原创”这类用途。

## Install

Clone this repository into your Codex skills directory:

```bash
git clone https://github.com/fu1fan/de-ai-writing-skill.git ~/.codex/skills/de-ai-writing
```

Then restart Codex or reload skills if your environment supports it.

## Usage

In a Codex chat, refer to the skill by name:

```text
Use $de-ai-writing to review this draft and make it sound less like AI.
```

中文也可以直接说：

```text
用双语去 AI 味写作 skill 帮我审读这篇稿子，把 AI 腔降下来。
```

## Repository Layout

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── README.md
├── LICENSE
└── .gitignore
```

## Inspiration

This skill was developed with inspiration from [daizhouchen/wechat-mp-writer](https://github.com/daizhouchen/wechat-mp-writer), especially its practical focus on publication-oriented writing workflows.

本 SKILL 的开发受到 [daizhouchen/wechat-mp-writer](https://github.com/daizhouchen/wechat-mp-writer) 的启发，尤其是它面向真实发布场景整理写作流程的思路。

## License

MIT License.
