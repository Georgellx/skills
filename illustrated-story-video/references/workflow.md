# Workflow and gates

## 1. Intake

Collect only decisions that affect production:

| Field | Default when appropriate |
| --- | --- |
| Source | User article, topic, script, or reference video |
| Platform | User-specified; otherwise infer from delivery request |
| Aspect ratio | 9:16 for Douyin/Xiaohongshu vertical video |
| Scene count | 4-8; default 6 |
| Target duration | 30-50 seconds |
| Subtitle language | Chinese or Chinese-English |
| Audio | Manual in Jianying/CapCut |
| Output | Silent MP4 plus SRT |
| Visual identity | Route with the table below |

Ask one concise question at a time only when the answer materially changes the result. Prefer a recommended default.

## 2. Visual identity router

| Situation | Mode | Action |
| --- | --- | --- |
| Stable owned character references exist | `existing-ip` | Audit references and lock immutable traits |
| User wants a recurring account character | `series-ip` | Create a minimal reusable character sheet |
| User needs only this video | `project-character` | Create one project-level anchor image |
| User does not want characters | `characterless` | Lock objects, spaces, silhouettes, color, and light |
| User supplies all final stills | `supplied-images` | Validate crop, size, continuity, and safe zones |

Do not confuse a long-term brand IP with a project-level visual anchor. Every multi-scene video needs continuity anchors, but not every user needs a full mascot brand.

## 3. Reference-video analysis

When a reference video is supplied, extract:

- canvas and content aspect ratios
- scene count and cut points
- empty-space and subtitle zones
- image reveal order and timing
- grayscale/color relationship
- crop, zoom, and per-scene positioning
- typography placement without copying wording
- audio structure and whether it remains in editing

Separate form from content. Reuse mechanics only.

## 4. Content development

1. Extract the source's core proposition, audience tension, concrete incident, change, and takeaway.
2. Offer up to three routes when the idea is not already locked: story, teaching/example, or visual metaphor.
3. Expand only the approved route.
4. Complete the scene table defined in `content-gates.md`.
5. Approve all subtitle content before generating visuals.

## 5. Visual development

1. Select the visual-identity mode.
2. Create or audit the anchor.
3. Generate one first-scene still.
4. Confirm style, identity, composition, safe zones, and image cleanliness.
5. Render the first-scene animation preview.
6. Generate remaining images one at a time only after approval.

## 6. Deterministic production

1. Initialize the project with `scripts/init-project.mjs`.
2. Make `project.json` match the approved scene plan.
3. Put scene images in `remotion/public/images/`.
4. Validate configuration and images.
5. Generate SRT from `project.json`.
6. Install the pinned Remotion dependencies in the project.
7. Render preview, then full video.
8. Strip audio and inspect the final MP4.

## 7. Final handoff

Deliver:

- source and reference material
- approved content/scene table
- visual-identity anchor
- scene images
- `project.json`
- silent MP4
- importable SRT
- short editor note: add voice, title styling, BGM, and final timing adjustments without recropping the video
