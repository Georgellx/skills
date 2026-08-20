---
name: edit-talking-head-video
description: Plan, prototype, edit, package, subtitle, and verify Chinese 9:16真人原声口播视频 from local footage and reference videos. Use when Codex needs to remove slips or repetition, build a word-boundary EDL, imitate an approved reference's visual grammar without copying its identity, design portrait-safe layouts and motion graphics, repair semantic subtitle grouping, create a real short style prototype, or deliver a quality-checked vertical talking-head MP4. This skill is for footage-led editing, not script-to-faceless-video or synthetic-host production.
---

# Edit Talking-Head Video

Build a Chinese vertical talking-head video through explicit editorial approvals, word-accurate cutting, reference-led design, semantic captions, and evidence-backed QA.

## Load the working contracts

Read the active workspace's `AGENTS.md` and `<workspace>/edit/project.md` first when present. Treat explicit user instructions as higher priority than project defaults.

Locate and read the installed `video-use` skill before transcription or rendering. Reuse its helpers and production-correctness rules instead of copying its renderer. Load the relevant HyperFrames or Remotion skill completely before using that engine.

Read these references only when their stage applies:

- `references/intake-and-approval.md` before asking questions, proposing a plan, or interpreting approval.
- `references/editorial-cutting.md` before generating or changing an EDL.
- `references/subtitle-contract.md` before grouping, timing, styling, or reviewing captions.
- `references/reference-style-and-layout.md` before analyzing a reference, writing `DESIGN.md`, making an ASCII layout, or building motion.
- `references/assets-and-rights.md` before downloading, generating, or licensing external visuals, fonts, or music.
- `references/qa-and-delivery.md` before showing a prototype, preview, or final render.

## Preserve the project boundary

Keep source footage immutable. Store transcripts, decisions, intermediate media, verification artifacts, previews, and final output under `<workspace>/edit/`. Cache transcription by source checksum or unchanged source identity.

Use these artifacts as sources of truth:

```text
edit/
├── project.md
├── takes_packed.md
├── transcripts/
├── edl.json
├── DESIGN.md
├── layout-ascii.md
├── caption-plan.json
├── master.srt
├── animations/
├── verify/
├── qa/report.json
├── preview.mp4
└── final.mp4
```

Initialize missing directories with `scripts/init_project.py`. Copy the bundled white-editorial template only when the project selects it.

## Follow the approval state machine

Record the current state and the exact approved artifacts in `edit/project.md`:

```text
analysis
  → waiting_for_strategy_approval
  → waiting_for_style_approval        (new or changed visual direction)
  → building_preview
  → waiting_for_preview_approval
  → building_final
  → complete
```

Treat a user's explicit approval of a named plan, layout, prototype, or preview as approval for that artifact only. Preserve prior approvals when later feedback does not invalidate them. Return to the affected approval state when narrative meaning, reference priority, visual system, music, rights, or output format changes.

## Execute the production workflow

1. **Inspect without editing.** Inventory sources with `ffprobe`, reuse or create word-level transcripts, read the packed transcript, and inspect representative frames plus waveform windows.
2. **Clarify material decisions.** Resolve only choices that materially change meaning, duration, style, rights, cost, or delivery. Ask focused questions; continue read-only analysis while waiting.
3. **Propose the strategy.** Describe narrative shape, removals, preserved moments, expected duration, portrait treatment, visual beats, caption treatment, audio policy, and deliverables in plain language. Stop at strategy approval.
4. **Lock the edit.** Create `edl.json` from transcript word boundaries. Preserve source quotes and reasons. Validate it with `scripts/validate_edl.py` before rendering.
5. **Lock the visual system.** Deconstruct the approved reference, write `DESIGN.md`, and show an ASCII layout for each distinct scene family. Separate portrait, information, captions, and platform-safe regions. Stop at style approval when the direction is new or changed.
6. **Build a real prototype when required.** Render about 10 seconds with final source footage, crop behavior, captions, audio treatment, layout, and motion. Run the same checks required for a final render. Stop at prototype approval.
7. **Build the full preview.** Compose the approved EDL and deterministic motion system. Align every reveal to the active spoken idea. Apply captions last unless the complete composition intentionally renders captions as its final top layer.
8. **Self-review.** Validate captions, generate contact sheets, inspect cut and transition boundaries, review at normal speed, and verify media parameters. Fix and repeat for at most three internal rounds.
9. **Deliver deliberately.** Show `preview.mp4` only after QA passes. Build `final.mp4` after preview approval, normalize audio, rerun final QA, and append decisions, outputs, measured results, and remaining limitations to `project.md`.

## Ask when the answer changes the work

Pause and ask before deciding among competing references, changing the speaker's intended meaning, selecting a new visual direction, using unverified external assets, adding music, starting paid generation, accepting a crop that loses an essential subject, or changing the approved output format.

Resolve discoverable facts through read-only inspection. Do not ask the user for metadata, timing, file properties, or local state that tools can determine.

## Enforce the editorial invariants

- Keep every cut outside spoken-word interiors and preserve suitable edge padding and audio fades.
- Keep captions aligned to the final output timeline and grouped by complete spoken meaning.
- Keep the active portrait, information, captions, and platform interaction zones spatially independent.
- Use full-screen portrait for human emphasis and a proportionate portrait window for information-heavy scenes.
- Keep face, hands, and the topic-defining object visible when they carry meaning.
- Reproduce reference grammar through hierarchy, spacing, palette, typography, motion, and rhythm; create project-owned text and identity.
- Make animation deterministic, frame-seekable, and readable at normal playback speed.
- Use current, documented licenses for external assets and preserve provenance.
- Support every quality claim with a command result, contact sheet, or normal-speed review record.

## Use the bundled utilities

```powershell
py -3 scripts/init_project.py --workspace <workspace> --style white-editorial-v2
py -3 scripts/validate_edl.py <workspace>/edit/edl.json --transcripts-dir <workspace>/edit/transcripts
py -3 scripts/validate_subtitles.py <workspace>/edit/master.srt
py -3 scripts/make_qa_contact_sheet.py <workspace>/edit/preview.mp4 --edl <workspace>/edit/edl.json --output <workspace>/edit/verify/contact-sheet.jpg
py -3 scripts/verify_output.py <workspace>/edit/final.mp4 --output <workspace>/edit/qa/report.json
```

Run scripts from the skill directory or use their absolute paths. Treat structural validators as evidence, not substitutes for editorial judgment.
