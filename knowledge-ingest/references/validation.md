# Validation Checklist

Run this before reporting completion.

## File And Encoding

- The file is in the intended destination.
- The destination is under `D:\personkonw\Pskonw`.
- The destination choice follows `D:\personkonw\Pskonw\AGENTS.md`: existing topic folders first; new category folders only when the reason, boundary, and long-term reuse value are clear.
- Chinese text opens correctly as UTF-8.
- The filename is searchable, specific, and not a noisy full sentence unless the source title is important.
- No unrelated files were moved, rewritten, or cleaned up.

## Frontmatter

- YAML starts and ends with `---`.
- The note uses the closest template from `D:\personkonw\Pskonw\Templates` when one fits.
- Article notes use `D:\personkonw\Pskonw\Templates\Temp.md` unless `AGENTS.md` points to a better template.
- For article notes, preserve the template field names: `title`, `original title`, `author`, `source`, `source url`, `date`, `type`, `tags`, and `related notes`.
- For non-article notes without a matching template, use the minimal `AGENTS.md` fields where useful: `title`, `type`, `status`, `tags`, `source`, `created`, `updated`, and `related`.
- `tags` follows the selected template shape. If expanded into a YAML list, use:

```yaml
tags:
  - 方法论
  - 内容创作
```

- Related-note fields follow the selected template. If expanded into a YAML list, quote wikilinks:

```yaml
related:
  - "[[真实文件名]]"
```

- Empty fields are removed, not left as `""`, `null`, or `待补` unless `待补` is meaningful content.
- URL values are quoted.

## Content Quality

- The note has a clear reason to exist.
- For topic-library inclusion, the source passes the `AGENTS.md` quality gate: it fits the topic and covers at least two of `原理`, `案例`, and `应用`.
- If a source fails the quality gate, record it in `D:\personkonw\Pskonw\拒收资料记录.md` instead of creating a topic note.
- It is not merely a transcript of the conversation unless the raw record is the asset.
- Durable knowledge is distilled into future-usable form.
- If the source is high-value, the note preserves the original asset, necessary original text, or an explicit reason for not preserving it.
- Claims are labeled as fact, source claim, inference, or unverified when ambiguity matters.
- External articles keep enough original source context to preserve evidence.
- Prompt text is stored in the prompt directory when it is meant to be copied and reused.
- Product ideas include evidence or explicitly say `待验证`.

## Links And Tags

- Every wikilink in the related field points to a real note name.
- There are no more than 3 related links unless the user explicitly asked for a map.
- Tags are retrieval-friendly and not just decorative.
- New categories were created only under the new category policy.

## Index Updates

- Update an existing index page only when the vault already has one and the change clearly belongs there.
- Do not create new index pages unless explicitly requested.

## Source Cleanup

- Do not delete any source file unless the user explicitly confirms deletion.
- If source material came from `D:\personkonw\Pskonw\Clippings`, keep it after extraction unless the user explicitly asks for cleanup.

## Final Report

Report:

- `入库判断`: saved, skipped, or updated, with one short reason.
- `位置`: created/updated file paths.
- `分类`: asset type, tags, and value level if relevant.
- `双链`: links added, or `暂无`.
- `清理`: any Clippings deletion, or `无`.
