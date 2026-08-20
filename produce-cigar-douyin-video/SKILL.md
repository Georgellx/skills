---
name: produce-cigar-douyin-video
description: Turn Chinese cigar-knowledge topics, text, screenshots, or user images into a fact-checked, conversational, cinematic, true-motion Douyin video workflow. Use when Codex must research and improve a cigar topic, draft the spoken script and scene plan, reproduce the locked local reference-video style and subtitles, resolve an authorized cloned voice or MiniMax junlang_nanyou fallback, create a real first-15-second preview for approval, or resume the approved arbitrary-duration production without slideshow footage.
---

# Produce Cigar Douyin Video

Create or resume one isolated project under `projects/<project-id>/`. Treat project files, approvals, provider IDs, costs, and checksums as the source of truth.

## Load the contracts

Read these resources before planning:

- `references/workflow-contract.md` for intake, research, approvals, voice, music, and state transitions.
- `references/reference-style.md` before writing scenes, typography, transitions, or composition.
- `references/sync-and-subtitles.md` before aligning narration, timing scenes, or rendering text.
- `references/motion-quality.md` before acquiring visuals, generating video, or reviewing a render.
- `references/content-and-safety.md` before researching or approving the script.

Also read the active workspace's `AGENTS.md`, product/technical decisions, asset policy, project state, and active `work/job-state.json` when present. Never override a stricter workspace rule.

## Initialize safely

Run `scripts/init_cigar_project.py` for a new project. It copies the approved reference-style lock and project `AGENTS.md` template without overwriting existing work.

```powershell
python scripts/init_cigar_project.py --workspace <workspace> --project-id <project-id>
```

Keep user inputs immutable under `input/`, resumable state and intermediate media under `work/`, and approved deliverables under `output/`.

## Follow the production sequence

1. Accept text, images, screenshots, or a topic. Record source and rights declarations.
2. Ask for optional background music and its usage authorization. If no music file is supplied, set `music.mode=none`; do not source or generate music automatically.
3. Prefer the channel owner's stable authorized clone. If no usable local sample and authorization exist, use MiniMax system voice `junlang_nanyou`. Never clone an unverified sample.
4. Audit the topic for factual, health, platform, advertising, and originality risk. Browse current authoritative sources when facts, regulations, or trends may have changed. Save URLs, dates, and claim mappings.
5. Rewrite into natural spoken Chinese. Remove AI-style framing, inflated claims, textbook transitions, and repetitive summaries.
6. Produce the complete editorial review package: hook, spoken script, fact notes, scene/action plan, full-timeline shot-reuse map, character policy, scene reference images, subtitle beats, provider-call plan, and cost ceiling.
7. Stop at `waiting_for_content_approval`. Do not treat silence or general encouragement as approval.
8. After approval, generate the complete final narration, align its words or spoken-caption phrases, then split the aligned audio into semantic shots of arbitrary total duration. Duration-weighted or equal-interval estimates cannot pass as alignment.
9. Acquire or generate true-motion clips under the motion contract. Storyboard stills are review artifacts only.
10. Audit the complete planned timeline for repeated sources, overlapping source ranges, duplicate rendered first frames, and near-identical shot designs before rendering the actual first `min(15 seconds, full duration)` with final voice, moving footage, locked typography, subtitles, transitions, and supplied music when present.
11. Run `scripts/check_motion.py`, `scripts/check_visual_reuse.py`, and the workspace media checks. Stop at `waiting_for_preview_approval`.
12. Generate the remaining paid visuals only when `preview.approved` is exactly `true`. Reuse persisted provider jobs; never submit a blind paid retry. Within one project, execute paid creates, status queries, downloads, and their state-file mutations serially unless one transaction lock covers the provider-job store, job state, manifest, and scene plan; never launch separate scene executors concurrently against unlocked project files.
13. Re-run the visual-reuse audit over the composed full timeline, verify the final MP4 with `ffprobe`, write quality/provenance reports, and keep release blocked when rights remain unresolved.

## Enforce the visual identity

Reproduce the approved reference's visual grammar as closely as possible: live-action documentary realism, warm brown/black palette, macro cigar detail, active hands and environments, rapid opening cuts, semantic-chunk kinetic headlines, colored emphasis, restrained lower subtitles, and the persistent health notice.

Every production visual must be photorealistic live-action-style video. Reject cartoons, illustrations, flat or vector graphics, schematic cutaways, infographics, icon animation, and explanatory motion-graphic pages unless the user explicitly requests a non-realistic exception. Express abstract ideas with realistic macro footage, hands, instruments, environmental changes, focus, light, and camera movement instead.

Do not directly crop the 16:9 reference into 9:16. Rebuild every shot natively for vertical composition while preserving the locked rhythm, hierarchy, color, movement, and transition behavior. Do not copy the reference's footage, people, words, logos, or audio unless their reuse rights are documented.

Default to a faceless host: hands, arms, back, silhouette, point-of-view, or off-camera narration. If the user explicitly asks for a visible virtual character, pause for a capability and policy review. Only proceed when the active project rules allow it; use a consistent photorealistic AI character, never impersonate a real person, and do not add lip sync unless separately approved.

## Enforce the anti-slideshow gate

Reject still-image zooms, pans, parallax, animated smoke overlays, cartoons, diagrams, or moving captions over a static base as substitutes for realistic video. Every production shot must contain semantic physical action plus a second independent motion layer. The first 15 seconds must collectively show human action, prop action, and environmental or camera movement.

Automated motion checks supplement, but never replace, frame-by-frame review. Reject frozen intervals, repeated loops, deformed hands or cigars, object teleportation, unstable labels, action discontinuity, generated pseudo-text, and any audio-caption-visual semantic mismatch. Do not hide a failed generated shot behind an opaque text card and mark it passed.

## Enforce full-timeline shot uniqueness

Treat shot reuse as a full-video property, not a per-file or per-stage check. Before preview rendering, record every timeline interval's root source lineage, source time range, rendered-start-frame checksum, shot signature, and any continuation group. Audit the preview and planned remainder together; repeat the audit after every replacement, regeneration, or edit.

Default to failure when a later interval replays an earlier source range, uses the same rendered first frame, or reproduces the same subject/action/angle closely enough to look like the same shot. A different filename, re-encode, crop, speed change, or regenerated clip from the same first frame does not make a shot unique. The same location may return only with a materially different composition and action.

An exact source may span adjacent semantic scenes only as one declared continuous shot: the intervals must share a continuation ID, use contiguous non-reversing source ranges, and preserve an uninterrupted action. When a shot crosses the 15-second preview boundary, persist the consumed source cursor and resume from that exact point in the full render; never restart the clip or switch back to an earlier source offset. If the source is too short, plan a distinct shot rather than replaying it.

Final approval requires both machine evidence and normal-speed human review: compare scene lineage/ranges, inspect a scene-boundary contact sheet, and compare non-adjacent scenes for perceptual near-duplicates. A boolean `manual_pass` flag without recorded evidence cannot satisfy this gate.

## Enforce subtitle and sync integrity

Render ordinary narration subtitles from the final audio-alignment artifact, never from project-specific hardcoded strings. Default them to a transparent background, one line, and the lower safe area with only stroke and soft shadow. Split long captions at aligned natural pauses; never auto-wrap them.

Treat kinetic headlines as a separate track. They may condense the phrase currently being spoken, but may not introduce an earlier or later idea. Every timed visual interval must support the narration and subtitle active in that interval. If the alignment backend is unavailable, the timing artifact is estimated, or normal-speed review finds a mismatch, stop before preview approval.

## Preserve approval and cost boundaries

Show exact provider calls, models, bounded call counts, and the maximum cost before the first paid call. Persist request fingerprints and provider task IDs immediately. Resume completed stages rather than regenerating them.

Advance only one paid provider state transition at a time per project. Wait until its provider record and local output state are durably reconciled before advancing another scene. If a local write conflict or process interruption occurs, inspect the persisted fingerprint, provider ID, output checksum, and current cost before doing anything else; do not infer failure from the caller error or create a replacement until the prior outcome is classified.

Do not infer or hardcode a persistent project-wide budget from an estimated production total. Keep a user-declared total budget separate from the bounded ceiling for the current provider-call plan. When the user has not declared a total budget, or explicitly requests no project-wide cap, do not invent one; still calculate, disclose, and bind every paid batch to an exact maximum call count and maximum cost so provider errors cannot create unbounded charges.

Content approval authorizes narration and preview production only. Preview approval authorizes remaining full-length generation. A changed approved script, voice, style lock, or supplied music invalidates the affected approval.
