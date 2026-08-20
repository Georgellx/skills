# Note Templates

Use the active vault templates first. The active vault root is `D:\personkonw\Pskonw`, and `D:\personkonw\Pskonw\AGENTS.md` is the source of truth for template selection and frontmatter expectations.

Before writing a note:

1. Read `D:\personkonw\Pskonw\AGENTS.md`.
2. Inspect `D:\personkonw\Pskonw\Templates`.
3. Select the closest existing template.
4. Use a minimal custom structure only when no template fits.

Do not silently invent a new template. If a note type repeatedly needs a new structure, suggest a new template to the user instead.

## Shared Frontmatter Rules

- Keep frontmatter aligned with the selected vault template.
- For article notes, use the current template fields from `D:\personkonw\Pskonw\Templates\Temp.md`: `title`, `original title`, `author`, `source`, `source url`, `date`, `type`, `tags`, and `related notes`.
- Do not rename template fields such as `source url` or `related notes` unless the user explicitly asks to update templates or field naming.
- Fill only useful fields. If a template placeholder is unknown, leave it blank only when the template already expects a blank value.
- Tags should be useful for retrieval, not decorative.
- Wikilinks in `related notes` must point to real notes.
- For non-article notes without a matching template, follow the `AGENTS.md` general fields as a minimal default: `title`, `type`, `status`, `tags`, `source`, `created`, `updated`, and `related`, removing fields that do not apply.

## Article Note

Default source template:

```markdown
---
title: <% tp.file.title %>
original title: 
author: 
source: <来源>
source url: <URL>
date: <% tp.date.now("YYYY/MM/DD") %>
type: 文章笔记
tags: 
related notes: 
---
```

After applying the template frontmatter, use this body shape unless the user asks for a different output:

```markdown

# 入库判断
> 价值档位：<A/B/C>。<一句理由>

# 文章摘要
<紧凑摘要>

# 核心观点
- <观点>

# 可复用内容
- <句子、框架、步骤或案例>

# 方法解读与验证
<当文章包含方法论或可验证论断时写。区分事实、经验、推断和营销话术。>

# 关联笔记
- [[真实文件名]]：<为什么关联>

# 原文与来源保存
<A 档/高价值资料保留原文资产路径或必要原文；B 档保留关键原文和干净改写；C 档只保留来源、关键引用和提炼。>
```

## Method Or SOP Note

```markdown
---
title: <方法名>
type: 方法论
status: 提炼完成
tags:
  - 方法论
  - <领域>
source: <对话成果/文章/项目>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
evidence_strength: <first-hand/sourced/inferred/anecdotal/unverified>
related:
  - "[[真实文件名]]"
---

# <方法名>

> 适用场景：<什么时候用>
> 核心判断：<一句话讲清这套方法解决什么>

## 使用步骤
1. <步骤>

## 判断标准
- <何时适用>
- <何时不适用>

## 示例
<一个短例子，足够以后复用>

## 来源与边界
<来自哪里；哪些是已验证，哪些还只是推断>
```

## Prompt Bank Entry

Append to the best matching file in `D:\personkonw\Pskonw\prompt` or an existing prompt subfolder. Do not duplicate a prompt in the source article.

````markdown
## <提示词名>

用途：<一句话说明场景和用法>。来源 [[<来源笔记名>]]。

```text
<提示词正文>
```
````

If a new prompt category page is truly needed, use:

```markdown
---
title: <分类名>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
type: 提示词
status: 可复用
tags:
  - 提示词
  - <用途>
---

# <分类名>
```

## Product Idea

```markdown
---
title: <想法名>
author: george
source: <来源>
idea_source: <复刻/原创>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
type: 产品想法
status: 待孵化
tags:
  - 产品想法
  - <主题>
related:
  - "[[真实文件名]]"
---

# <想法名>

**一句话**：<这是什么>

## 已验证样本 / 复刻证据
- **谁的打法 / 来源**：<来源>
- **成了没有（真实数据）**：<有数据写数据，没有写待验证>
- **这是想法还是真实需求**：<判断>

## 解决什么 / 为什么有意思
- <痛点、人群、价值>

## 怎么做
- <最小实现路径>

## 商业化想象
- <怎么赚钱或积累>

## 风险与难点
- <最大风险>

## 下一步
- <最小验证动作>
```

After creating or updating a product idea, update an existing product index only if the vault already has one. Do not create a new index page unless the user asks.

## Retrospective

```markdown
---
title: <复盘标题>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
type: 复盘
status: 提炼完成
tags:
  - 复盘
  - <项目/主题>
related:
  - "[[真实文件名]]"
---

# <复盘标题>

## 背景
<发生了什么>

## 结果
<最后产出了什么，成功与否>

## 做对了什么
- <可复用经验>

## 问题与原因
- <问题 -> 原因>

## 下次规则
- <以后遇到类似情况怎么做>
```

## Book Or Course Note

```markdown
---
title: <书/课程名>
author: <作者>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
type: 书籍
status: 提炼完成
tags:
  - 书籍
  - <主题>
related:
  - "[[真实文件名]]"
---

# <书/课程名>

## 核心问题
<这本书/课程主要解决什么>

## 可带走的观点
- <观点>

## 可实践的方法
- <方法>

## 原文与来源保存
<如果原书/课程资料很有价值，记录原始文件路径、摘录范围或保留策略；否则只记录来源身份。>

## 我的判断
<哪些值得用，哪些保留怀疑>
```

## Self-Understanding Note

```markdown
---
title: <主题>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
type: 自我认知
status: 提炼完成
tags:
  - 自我认知
  - <主题>
related:
  - "[[真实文件名]]"
---

# <主题>

## 触发
<这个洞察从哪里来>

## 观察
- <事实和感受分开写>

## 可能的模式
<反复出现的行为、偏好、价值观或边界>

## 下一步
- <一个温和可执行动作>
```
