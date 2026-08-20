# Routing Rules

## Vault Root

The active vault root is `D:\personkonw\Pskonw`.

Before routing any asset, read `D:\personkonw\Pskonw\AGENTS.md` and inspect the current top-level folders. The destination must be chosen by topic fit and the active vault rules, not by a hard-coded `知识资产` map from another vault.

Current known top-level areas include:

| Area | Use |
|---|---|
| `Claude` | Claude-related notes or official snapshots when the topic clearly belongs there. |
| `codex` | Codex, local agent, automation, or skill/workflow notes when the topic clearly belongs there. |
| `prompt` | Reusable prompt-bank entries and prompt modules. |
| `Templates` | Templates only. Do not store ordinary notes here. |
| `Clippings` | Temporary captured source material when the source needs to be preserved separately. |
| Existing topic folders | Prefer these for article notes, methods, book notes, personal insights, retrospectives, and product ideas when the topic fits. |

Do not treat this table as exhaustive. If the filesystem contains a more specific existing topic folder, prefer that folder when it matches `AGENTS.md`.

## Classification Dimensions

For every ingest, decide these before writing:

- `asset_type`: article note, method, prompt, product idea, retrospective, book note, self-understanding, official snapshot, or skip.
- `source_kind`: conversation, pasted text, web article, Clippings file, book/course, official doc, personal experience.
- `durable_value`: high, medium, low, or skip.
- `reuse_mode`: copy/use directly, guide future work, support a decision, preserve evidence, or personal reflection.
- `evidence_strength`: first-hand, sourced, inferred, anecdotal, or unverified.
- `source_retention`: none, citation only, key excerpts, or original asset.
- `maturity`: raw capture, cleaned note, reusable method, tested workflow, archived.

Only write fields that are useful for the note type. Do not add empty frontmatter placeholders.

## Asset Routing

| If the material is... | Route by default | Type | Notes |
|---|---|---|---|
| External article, newsletter, transcript, or long pasted source | Existing topic folder under `D:\personkonw\Pskonw`; use `Templates\Temp.md` for article notes | `文章笔记` | Use A/B/C value triage. For A/high-value sources, preserve the original asset or enough original text for evidence. Extract prompts or product ideas only when they will be reused independently. |
| A reusable framework, SOP, checklist, operating method, or decision rule | Existing topic folder that matches the domain | `方法论` | Distill into reusable steps. Do not bury durable methods inside article notes only when the method will be reused independently. |
| A reusable prompt or prompt module | `D:\personkonw\Pskonw\prompt` or an existing prompt category inside it | `提示词` | Store the prompt once. The source note should link to the prompt note instead of duplicating the full prompt. |
| A business/product idea, automation idea, monetization angle, or "以后可以做" thought | Existing topic or product-related folder if one exists; otherwise ask before creating a new category | `产品想法` | Capture evidence or mark `待验证`. Do not create a product index unless the vault already has one or the user asks. |
| A finished project lesson, debugging lesson, experiment result, or workflow after-action | Existing project/topic folder | `复盘` | Separate facts, decisions, what worked, what failed, and next rules. |
| A book/course summary or reading note | Existing topic folder or a book/course folder if the vault already has one | `书籍` | Preserve source identity, keep the original file/text when high-value and user-provided, and extract only durable concepts into the note. |
| A personal values, strengths, direction, identity, or life-design insight | Existing personal/reflection topic folder if present; otherwise ask before creating one | `自我认知` | Keep private/person-centered. Link sparingly. |
| Claude/OpenAI/vendor documentation snapshot | `Claude` only when the source or topic clearly belongs there; otherwise route by topic | `官方快照` or `文章笔记` | Time-sensitive claims need dates and source URLs. |
| Temporary source material | `Clippings` if source preservation is useful and the folder exists | `原始资料` | Preserve source information. Do not delete after extraction unless the user confirms. |
| Rejected low-value source | `D:\personkonw\Pskonw\拒收资料记录.md` | `拒收记录` | Record why it failed the quality gate from `AGENTS.md`. |
| Temporary execution notes, command logs, or scaffolding | Skip | none | Mention if it should not be saved. |

## Article Value Triage

- **A high value**: original practice, dense information, unique data, a complete method, or an example the user can reuse. Keep the original source asset or necessary original text plus interpretation.
- **B medium value**: useful but verbose, salesy, scattered, or AI-flavored. Keep source plus a clean rewrite or distilled version.
- **C low value**: mostly marketing, trend-chasing, obvious, or reducible to one paragraph. Save only the extraction, source, and useful quote if the user still wants it.

Also apply the `AGENTS.md` quality gate before putting a source into a topic library: it must fit the topic and cover at least two of `原理`, `案例`, and `应用`. If it fails, record it in `D:\personkonw\Pskonw\拒收资料记录.md` instead of scattering rejection notes across topic folders.

For any high-value source, do not let summarization destroy evidence. If the user supplied a local file or text and it is useful as a future reference, save or link that original alongside the distilled note. If full preservation is not appropriate, record why and keep the strongest excerpts or source pointer.

Ask: "What remains after removing packaging?" and "Can the user reuse this later?"

## Tags

- Use 3-6 tags.
- Prefer stable concept tags over one-off source tags.
- Reuse existing tag language where obvious.
- Use nested tags only when they represent a real hierarchy in this vault.
- Do not add both broad and narrow duplicates unless both help retrieval.

## Wikilinks

- Use `[[真实文件名]]` only after checking the file exists.
- Prefer links by concept, method dependency, source lineage, or workflow relationship.
- Do not link merely because two notes share an author, platform, or broad topic.
- Keep the selected template's related field to 0-3 items. If no credible link exists, leave the related field blank and write `暂无` in the body if an association section is needed.

## New Category Policy

Default to no new top-level folder and no new prompt category.

Create a new category only when all are true:

1. The material does not fit an existing destination without distortion.
2. Similar material is likely to recur.
3. The new category has a clear boundary and a useful retrieval purpose.
4. The reason, boundary, and long-term reuse value satisfy `D:\personkonw\Pskonw\AGENTS.md`.

If uncertain, stop and give the user 2-3 numbered destination options with reasons. When creating a new category, explain the reason in the final report.
