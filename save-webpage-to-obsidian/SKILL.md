---
name: save-webpage-to-obsidian
description: Save a public or authenticated webpage, article, documentation page, or course lesson as a local Obsidian Markdown note with ordered text, headings, formatting, links, tables, code blocks, and locally downloaded content images. Use when the user asks to archive, clip, export, download, or save a URL/webpage to Obsidian or Markdown while preserving both text and images, including pages that require an existing browser login.
---

# Save Webpage to Obsidian

Create a self-contained Obsidian note whose local image embeds remain usable after the source page changes or signed asset URLs expire.

## Define the output

1. Use the user-specified vault, folder, and filename when provided.
2. Otherwise, look for a single `.obsidian` directory in the workspace and use its parent as the vault root.
3. If no vault is present, save under the current workspace and tell the user the exact location. If several vaults are equally plausible, ask which one to use.
4. Derive a filesystem-safe note name from the article heading or page title.
5. Store attachments in an adjacent `assets/` directory unless the vault already has an established attachment convention.

## Acquire the page

1. Follow any URL-reading or browser-control skills available in the session before using their tools.
2. Try an authorized semantic reader or public page fetch first when it preserves the required content and image URLs.
3. Use the browser selected by the browser-control skill when public extraction fails, the page is client-rendered, or existing login state is required.
4. If authentication is missing, ask the user to sign in in the selected browser. Do not inspect cookies, local storage, passwords, or session files.
5. Do not bypass paywalls, access controls, CAPTCHA, anti-bot protections, or DRM. Ask the user to handle CAPTCHA when encountered.

## Identify canonical content

Treat the article, lesson, or document body as the default scope. Preserve its DOM order and include:

- title and heading hierarchy;
- paragraphs and inline emphasis;
- ordered and unordered lists;
- quotes and callouts;
- tables and code blocks;
- meaningful inline links;
- images belonging to the canonical body.

Exclude site chrome, menus, sidebars, ads, recommendation cards, avatars, reaction icons, footers, comments, and publisher copyright notices unless the user explicitly asks for the whole page.

For an iframe-hosted document, inspect the relevant frame. Scroll the page or its content container enough to load lazy content, then re-check the canonical body. Do not assume the top-level asset inventory includes iframe images.

## Extract text and structure

Prefer semantic HTML inside the narrowest reliable content root. Convert structure deliberately instead of flattening all visible text:

- page title to `#`;
- major sections to `##` and subsections to `###` or deeper;
- bold, italic, strike, links, lists, quotes, tables, and fenced code to their Markdown equivalents;
- repeated empty blocks to nothing.

When a custom editor renders generic `div` blocks, infer block type from stable classes and contained elements. Keep the first and last meaningful paragraphs as completeness anchors.

## Download body images

1. Inventory images only inside the canonical content root and retain their document order.
2. Prefer a browser asset-bundling capability when it covers the relevant frame. Otherwise use the rendered image element's `currentSrc` or `src` from the authorized page.
3. Download public or signed image URLs directly when permitted. Do not copy authentication secrets into shell commands or output.
4. Detect the real format from response MIME type or file signature; use the correct extension even when the URL has none.
5. Name files deterministically, for example `chapter-name-01.webp`, `chapter-name-02.png`.
6. Inspect representative images and verify every downloaded file is non-empty. If an image failed because a signed URL expired, refresh the page and obtain a fresh rendered URL.
7. Embed local attachments with Obsidian syntax such as `![[assets/chapter-name-01.webp]]`.

Do not include logos, profile photos, favicons, UI icons, or decorative backgrounds unless they are part of the requested content.

## Write the note

Use UTF-8 and add YAML frontmatter:

```yaml
---
title: "Page title"
source: "https://example.com/page"
captured: YYYY-MM-DD
updated: YYYY-MM-DDTHH:MM:SS+TZ
tags:
  - web-archive
---
```

Omit `updated` when the page does not expose it; never invent a publication or update time. Keep the source URL only in YAML frontmatter for traceability. Do not add a visible source callout or source section below the title, and do not append a copyright notice or copyright callout.

Use external Markdown links for web URLs and Obsidian embeds for local attachments. Do not leave expiring remote image URLs in the final note.

## Verify before completion

1. Compare the saved title, heading count, first paragraph, and last paragraph with the rendered source.
2. Confirm the Markdown image reference count matches the downloaded body-image count.
3. Run:

```bash
python scripts/validate_note.py "/absolute/path/to/note.md"
```

4. Require `missing_count: 0`, valid YAML frontmatter, and a `source` property.
5. Inspect at least the first and last downloaded images when visual tools are available.
6. Report the clickable note path, attachment directory, image count, and any deliberately excluded page regions.

Keep the archive for the user's personal/local use. Do not redistribute protected course content or claim that local saving grants publication rights.
