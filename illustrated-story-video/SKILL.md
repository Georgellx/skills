---
name: illustrated-story-video
description: Build a static illustrated short-video project from an article, topic, script, story idea, or reference video. Use when Codex needs to develop and approve the content, route users who have an existing IP character or no IP at all, generate consistent scene-image directions or images, render a grayscale-to-color reveal video with Remotion, create Chinese or bilingual SRT subtitles for CapCut/Jianying/Douyin, and verify a silent MP4 handoff.
---

# Illustrated Story Video

Create a 4-8 scene illustrated video, defaulting to six scenes. Deliver a silent MP4 plus importable SRT; leave voice, music, and final text styling to the editor unless the user explicitly expands the project scope.

## Core Scope

- Treat an article, topic, or reference video as source material, not as a finished script.
- Reproduce structural mechanics such as layout, pacing, grayscale reveal, and color sweep without copying another creator's characters or wording.
- Support existing IP, newly bootstrapped series IP, one-off project characters, characterless visual motifs, and user-supplied images.
- Use one still image per scene. Derive grayscale and color layers from that exact same image.
- Generate text-free scene images. Put readable subtitles in editing or SRT.
- Keep voice synthesis, music selection, posting, and platform operations out of the default workflow.

## Required References

Read only the references needed for the active stage:

- Read `references/workflow.md` before starting any project.
- Read `references/content-gates.md` before writing the content plan or subtitles.
- Read `references/visual-identity.md` before choosing or generating characters, scenes, or visual anchors.
- Read `references/project-schema.md` before creating or editing `project.json`.
- Read `references/qa.md` before rendering, generating SRT, or handing off the final files.

## Workflow

1. Inspect the source article/topic, reference video, existing images, and any project contract files.
2. Record platform, aspect ratio, target duration, subtitle languages, editor, and visual-identity mode. Use 9:16, six scenes, bilingual SRT, and silent MP4 only when the user has not specified alternatives and those defaults fit the platform.
3. Propose up to three genuinely different content routes. Recommend one, then stop for approval before expanding it.
4. Produce the approved scene plan with visible event, narrative function, emotional change, Chinese subtitle, optional English adaptation, and why each scene is indispensable.
5. Apply the content gate in `references/content-gates.md`. Do not generate images while critical failures remain or before the user approves the full scene plan and subtitle content.
6. Route visual identity:
   - `existing-ip`: audit supplied references and list immutable traits.
   - `series-ip`: create a minimal reusable character sheet before scene generation.
   - `project-character`: create one project-level character anchor for a one-off video.
   - `characterless`: use recurring objects, hands, silhouettes, rooms, color, or light as anchors.
   - `supplied-images`: validate and use user-owned stills.
7. Generate or specify only the visual anchor and first scene. Stop for approval of character consistency, composition, negative space, and style.
8. Initialize a production project with `scripts/init-project.mjs`, fill `project.json`, place images under `remotion/public/images/`, and render the first-scene preview.
9. After the preview is approved, generate the remaining scene images one at a time. Reject drift in character, wardrobe, room, crop, style, or subtitle safe zones.
10. Run `scripts/validate-project.mjs`, generate SRT with `scripts/generate-srt.mjs`, render the Remotion composition, strip audio, and verify the final MP4.
11. Deliver the silent MP4, SRT, approved scene plan, visual anchor, source images, and concise editor handoff.

## Confirmation Gates

Stop only at decisions that make later work expensive to redo:

1. Content route.
2. Complete scene plan and subtitle wording.
3. Visual-identity mode and anchor image.
4. First scene still.
5. First scene animation preview.
6. Final MP4 acceptance.

Do not stop for routine folder creation, deterministic script execution, validation, or formatting.

## Content Integrity Rules

- Never invent a user's personal experience and present it as true. Ask for real details or label the story as fictional.
- Prefer concrete incidents, relationships, objects, and actions over abstract explanations.
- Require each scene to change information, action, or emotional state.
- Do not let subtitles explain a story the images fail to show.
- Adapt English for natural spoken meaning; do not translate Chinese mechanically.
- End with a resolving image or action, not a slogan pasted onto an unresolved story.

## Visual Consistency Rules

- Do not use Perry's Kapi/Tuanzi characters or any other project-specific IP unless the user owns and supplies that IP for the active project.
- Reuse the same approved character and environment references in every relevant image-generation call.
- Lock immutable character traits, wardrobe, palette, and scene architecture before batch generation.
- Generate one scene per image and no in-image text, logos, or watermarks.
- Use the exact same image, crop, position, and scale for grayscale and color layers.
- Preserve user-specified subtitle and title safe zones; include per-scene `imagePosition` in `project.json`.

## Production Commands

Initialize a project:

```powershell
node scripts/init-project.mjs "D:\path\to\new-project"
```

From the skill directory, validate and generate subtitles:

```powershell
node scripts/validate-project.mjs "D:\path\to\new-project\project.json"
node scripts/generate-srt.mjs "D:\path\to\new-project\project.json"
```

From the generated project's `remotion` directory:

```powershell
npm install
npm run render:preview
npm run render
```

Validate the final video:

```powershell
node scripts/validate-project.mjs "D:\path\to\new-project\project.json" --video "D:\path\to\new-project\outputs\final\story-video-silent.mp4"
```

## Deliverables

- Approved human-readable scene plan.
- `project.json` as the single production timing/configuration source.
- Visual anchor references and one image per scene.
- Silent H.264 MP4.
- UTF-8 SRT containing subtitle content only.
- QA result and editor handoff noting that voice and music remain manual.

## Failure Handling

- If no image-generation tool is available, deliver the anchor and scene prompt pack, then wait for returned images.
- If the user has no IP and declines character creation, route to `characterless`; do not silently invent a mascot.
- If the first scene fails consistency, revise the anchor before producing later scenes.
- If recorded voice is longer than the scene, update `durationSeconds` in `project.json`, regenerate SRT, and rerender rather than stretching the finished video.
- If the final MP4 cannot be inspected because ffprobe is missing, report that QA is incomplete instead of claiming success.
