---
name: knowledge-ingest
description: Classifies, evaluates, and saves conversation outputs, external articles, prompts, methods, SOPs, product ideas, retrospectives, book notes, and personal insights into the local Obsidian vault at D:\personkonw\Pskonw. Use when the user asks to 存入知识库, 入库, 沉淀, 整理这篇, 分析这篇值不值得存, 记下来, 收进提示词目录, 做成方法论, 做复盘, 加双链, 打标签, or otherwise wants a source turned into a durable knowledge asset.
---

# Knowledge Ingest

Use this skill to turn a useful conversation result or external source into a correctly routed Obsidian knowledge asset in `D:\personkonw\Pskonw`.

## Core Rule

Work on the content layer. Do not create vault home pages, index pages, dashboards, or folder reorganizations unless the user explicitly asks for those. The default job is: decide whether the material is worth saving, choose the right existing place, write the note or append the asset, add conservative tags and wikilinks, then verify.

If the original source is high-value, preserve it as well. A distilled note should not replace the source when the original contains reusable evidence, examples, wording, data, or structure. Save the user-provided original file/text alongside the note when appropriate, or keep enough original context and a clear source pointer when full preservation is not appropriate.

Before choosing a destination or template, read `D:\personkonw\Pskonw\AGENTS.md`. Treat it as the active vault contract for classification, directory growth, templates, frontmatter, tags, source retention, duplicate handling, and deletion rules.

## Required References

- Read `D:\personkonw\Pskonw\AGENTS.md` before classifying, choosing a destination, or deciding whether a new category folder is allowed.
- Read [references/routing.md](references/routing.md) before classifying or choosing a destination.
- Read [references/templates.md](references/templates.md) and the selected file under `D:\personkonw\Pskonw\Templates` before writing or appending any vault file.
- Read [references/validation.md](references/validation.md) before reporting completion.

## Workflow

1. **Identify the source and intent**
   - Conversation result: a decision, plan, prompt, workflow, method, code lesson, product idea, or personal insight from the current chat.
   - External source: article, link, transcript, Clippings file, book/course excerpt, or official material.
   - If unclear, ask one short question: "这是要消化外部资料，还是把我们这段对话的成果入库？"

2. **Make a keep/drop judgment**
   - Save if it is reusable, decision-shaping, evidence-bearing, personally important, or likely to be searched later.
   - Do not save trivial chat, temporary scaffolding, duplicated summaries, or vague inspiration unless the user explicitly says to remember it.
   - For external articles, assign `A/B/C` value level using `routing.md`.
   - For high-value sources, decide both the distilled note and the original-source retention plan before writing.

3. **Route to the smallest fitting asset type**
   - Prefer existing topic folders under `D:\personkonw\Pskonw`.
   - Use `AGENTS.md` to decide whether the asset belongs in an existing category folder or whether a new category folder is justified.
   - Do not create a new category folder unless `AGENTS.md`'s directory-growth standard is met: explain why existing folders do not fit, define the new category boundary, and confirm it has long-term reuse value. If uncertain, stop and give the user 2-3 numbered options.
   - Split mixed material into separate assets only when the parts will be reused independently, such as an article note plus a prompt-bank entry plus a product idea.
   - Keep a single source of truth: prompts live under `D:\personkonw\Pskonw\prompt`; product ideas, reusable methods, and retrospectives live in the existing topic folder that best matches them unless `AGENTS.md` justifies asking the user about a new category.

4. **Check duplicates and related notes**
   - Search existing file names and nearby folders before writing.
   - Use 0-3 conservative links in the selected template's related field; link only real existing note names by concept or workflow relationship, not by loose topic similarity.
   - If a likely duplicate exists, update or ask before creating a second copy.

5. **Write, append, or update**
   - Use UTF-8. On Windows paths, use literal paths and avoid wildcard path assumptions.
   - For article notes, start from `D:\personkonw\Pskonw\Templates\Temp.md` unless `AGENTS.md` points to a better template.
   - Preserve the template's frontmatter shape unless the user explicitly asks to update templates or field names.
   - Obsidian wikilinks should use note names only, not filesystem paths.
   - Never delete source files unless the user explicitly confirms deletion.

6. **Validate and report**
   - Run the checklist in `validation.md`.
   - Report created/updated files, classification, tags, wikilinks, and any source cleanup. Keep the report short and actionable.
