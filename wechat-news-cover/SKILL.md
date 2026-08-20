---
name: wechat-news-cover
description: Creates Chinese 16:9 editorial covers from a supplied source photo and user-provided information, using only news published and events occurring within the latest 48 hours, current-news fact checking, and restrained British public-broadcast visual language. Use for 热点新闻封面, BBC风格封面, 原图修图, 微信贴图, 微信图文封面, 横版新闻头图, or explicit 3:4 platform adaptations.
---

# 48-Hour Hot News Cover

Turn a supplied photo and information into a factual, legible 16:9 editorial cover. Use only a verified news angle from the latest 48 hours and preserve the source image.

## Core rules

1. Use the `imagegen` skill and the built-in image generation tool for every raster edit.
2. Require two inputs: a source photo and user-provided information such as a person, event, keyword, fact, caption, or URL. Use the information as the search seed; do not silently treat it as verified fact.
3. Treat the supplied photo as the edit target, not merely a loose reference. Inspect a local image with `view_image` before editing it.
4. Default every generated cover to landscape 16:9. Change the aspect ratio only when the user explicitly requests another format.
5. Use only news whose publication time is within the preceding 48 hours. When the event time is known, require the event itself to fall within the same 48-hour window.
6. Reject a newly published article that merely recaps an event older than 48 hours.
7. Prefer primary or authoritative reporting and corroborate material claims with a second independent source when available.
8. Never invent events, quotes, dates, cards, scores, identities, statistics, or reactions.
9. Preserve people’s identities, faces, uniforms, gestures, objects, and photographic realism unless the user explicitly requests a change.
10. Use restrained British public-broadcast visual grammar: deep red, white, charcoal, clean sans-serif type, compact category bars, strong hierarchy, and ample negative space.
11. Do not reproduce the BBC name, logo, three-block mark, or any fake network logo.
12. Keep the edit surgical. Do not add decorative effects, sensational icons, fake badges, or unrelated elements.

## Workflow

### 1. Establish the inputs and deliverable

Confirm that the request supplies both an image and enough information to identify a topic. Ask one concise question only when the topic cannot be identified safely.

- Generate **landscape 16:9** by default, including when the user says 微信贴图 or 微信图文 without specifying dimensions.
- Use **portrait 3:4** only when the user explicitly asks for 3:4/竖版, provides a 3:4 target specification, or explicitly asks to fix a known 3:4 crop.
- If a generated 16:9 cover is cropped by a confirmed 3:4 placement, rebuild it as portrait 3:4. Do not merely shrink the landscape image inside empty borders.
- If the user supplies both an original photo and an approved cover, label the original as the edit target and the approved cover as the style/copy reference.

Do not infer portrait output merely from the word “微信”.

### 2. Apply the 48-hour freshness gate

1. Record the current date, time, and user timezone before searching.
2. Search using the user-provided person/event/keywords plus recency terms.
3. Open candidate reports and capture both the publication timestamp and the described event timestamp when available.
4. Keep a candidate only when it was published no more than 48 hours ago and does not describe an event older than 48 hours.
5. Prefer one primary or authoritative source plus one independent corroborating source. Syndicated copies of the same report count as one source.
6. If no report passes the gate, stop before image generation. State that no eligible 48-hour news was verified and ask the user for a source or permission to widen the time window.

Do not use search-result snippets alone for material facts when the underlying report can be opened. Do not fill a missing timestamp by guessing.

### 3. Choose the cover angle and copy

From eligible reporting, extract only:

- one headline-worthy fact or reaction,
- one supporting fact,
- the event date,
- the source context needed to avoid exaggeration.

Keep cover copy compact:

- category: 4–10 Chinese characters,
- headline: no more than two short lines,
- subheadline: one line when possible,
- date: `YYYY.MM.DD`.

When the conversation already contains another cover about the same person or event, choose a materially different angle. Do not repeat the previous main headline, statistic, or framing. Examples of distinct angles include match facts, referee performance, external reaction, historical significance, and team impact. Do not claim that a reaction is “foreign media praise” when the evidence only shows social-media comments; use “海外球迷评价” instead.

If live verification fails, do not call the angle “latest” or “hot”. Stop before generation unless the user supplies a timestamped source that passes the 48-hour gate.

Before generating, tell the user the selected angle and that it passed the 48-hour gate. Keep this preflight update brief.

### 4. Define image invariants

Before calling the image tool, explicitly state what must remain unchanged:

- subject identity and facial features,
- clothing and official badges already present,
- pose and gesture,
- cards, ball, equipment, and other news-relevant objects,
- important secondary subjects,
- match setting and photographic realism.

Also state what may change:

- crop and canvas aspect ratio,
- natural background extension,
- subtle dark gradient for legibility,
- text and simple broadcast-news graphic bars.

Never ask the model to “recreate” a person when a precise edit is required.

### 5. Compose for the surface

#### Default: landscape 16:9

- Explicitly request a 16:9 landscape cover in the prompt.
- Keep the main subject fully visible and away from headline text.
- Place text in existing negative space or over a subtle dark gradient.
- Use one compact red category strip, a two-line white headline, one supporting line, and a small date.
- Keep all text at least 5% away from every edge.

#### Explicit exception: portrait 3:4

- Request a portrait 3:4 composition, ideally described as 1080×1440.
- Place the main subject in the upper-middle area.
- Preserve the face, head, torso, raised arms, hands, and news-relevant objects with generous clearance.
- Keep all critical subjects and text inside the central 82% width and central 84% height.
- Leave at least 8% padding from each edge.
- Put the headline in a compact lower-third or upper negative-space block; do not let it cross a face or body.
- Reduce type size and shorten line lengths rather than pushing text to an edge.
- Allow peripheral players or background details to crop before cropping the main subject.
- Extend the stadium or background naturally when the original landscape frame lacks vertical coverage.

### 6. Build the image prompt

Use this compact structure and include only applicable lines:

```text
Use case: precise-object-edit
Asset type: <landscape 16:9 editorial cover by default | explicit portrait 3:4 adaptation>
Input images: <identify edit target and optional style reference>
Primary request: <verified news angle that passed the 48-hour gate>
Preserve exactly: <identity, pose, clothing, relevant objects, secondary subjects>
Composition: <subject placement, text region, safe zone, crop permissions>
Text (verbatim):
Category: “<category>”
Headline: “<line 1>” / “<line 2>”
Subheadline: “<supporting fact>”
Date: “<YYYY.MM.DD>”
Typography: clean broadcast-news sans-serif, crisp Chinese, strong hierarchy
Palette: deep red, white, charcoal; preserve the source photo’s natural colors
Constraints: no network logo, no watermark, no invented objects, no facial changes,
no duplicated limbs or people, no text outside the safe zone
```

Quote every required string and require it to appear verbatim. Keep Chinese copy short enough for reliable rendering.

### 7. Validate the output

Check the generated image against these acceptance criteria:

- correct aspect ratio for the target surface,
- 16:9 output unless the user explicitly requested another ratio,
- main subject and relevant gesture/object fully visible,
- headline and subheadline fully readable,
- all copy inside the safe zone,
- factual angle matches the verified reporting,
- source publication and event fall within the 48-hour window,
- no repeated headline angle when the user requested a distinct version,
- no fake logo or trademark imitation,
- no altered identity, extra card, duplicated limb, or invented person.

For a WeChat crop complaint, the task is successful only when the cover remains understandable from a centered 3:4 preview.

## Output behavior

Render the generated image directly. Follow the image tool’s rule not to add commentary after generation. Keep the source file intact and save edits non-destructively.
