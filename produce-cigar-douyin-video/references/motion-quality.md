# True-Motion Contract

## What counts as video

A production shot must include semantic physical motion in the generated or captured frames. Valid examples include:

- hands opening packaging, inspecting a wrapper, rotating a cigar, placing cigars, closing a humidor, or adjusting a hygrometer;
- leaves moving during sorting, rolling, pressing, drying, or inspection;
- a drawer, cabinet, tool, gauge, cloth, vapor, practical light, or background worker changing over time;
- an intentional camera push, orbit, track, tilt, rack focus, or handheld drift combined with subject or environmental action.

Every shot must contain:

1. one primary semantic action; and
2. one independent secondary movement from camera, environment, another person, light, focus, or prop.

Across every opening 15-second window, include at least one human action, one prop action, and one environmental or camera movement.

## What does not count

Reject:

- cartoons, illustrations, flat/vector graphics, schematic cutaways, infographics, or explanatory motion-graphic pages in place of live-action-style footage;
- a still image with only scale, crop, pan, parallax, simulated depth, grain, smoke, or lighting overlays;
- animated text over a static image;
- a short motion loop repeated to fill a longer scene;
- the same source action replayed in another scene, including after re-encoding, cropping, retiming, or crossing the preview boundary;
- a newly generated clip that copies another scene's first frame and preserves substantially the same composition and action;
- breathing-only or blinking-only portrait animation;
- a locked scene whose only change is compression noise;
- a dissolve between two still images presented as cinematic movement.

Storyboard and character images may be shown for content approval, but may not be placed directly on the preview or final timeline.

## Prompt contract for generated clips

Write each visual prompt with explicit fields:

- `subject_action`: what the hand, person, cigar, leaf, tool, or cabinet physically does;
- `secondary_motion`: independent background, light, focus, or prop movement;
- `camera_motion`: direction, speed, and endpoint;
- `continuity_start`: the first-frame state;
- `continuity_end`: the state needed for the next cut;
- `stability`: shape, hand, label, cabinet, gauge, and cigar constraints;
- `prohibited`: face visibility by default, smoking, lit cigar, brands, text generation, warping, teleportation, or duplicate limbs.

Prefer one clear action arc per clip. Avoid prompts containing several unrelated actions that a short generation cannot complete cleanly.

## Automated thresholds

Run `scripts/check_motion.py` on every preview and final video.

Default thresholds:

- longest frozen interval: at most 0.75 seconds;
- sampled moving-frame ratio: at least 0.90;
- black interval longer than 0.25 seconds: fail unless explicitly designed and approved;
- missing video/audio stream, decode error, zero duration, or duration mismatch: fail.

The checker reports evidence; it cannot distinguish real semantic action from a digital zoom. Perform manual review after it passes.

## Full-timeline uniqueness checks

Motion in every file is insufficient: compare shots across the complete composed timeline. Persist root source lineage and normalized source ranges so derived clips remain traceable to the same underlying footage. Fail automatically when:

- source ranges overlap or move backward between adjacent intervals declared as one continuous shot;
- a scene crossing the preview boundary restarts before the exact source cursor consumed by the preview;
- different scenes have the same rendered-start-frame checksum;
- non-adjacent scenes reuse the same source lineage without a reviewed, materially different action and composition;
- contact-sheet or perceptual comparison identifies a repeated action sequence despite different filenames or encodes.

Write the result to a visual-reuse audit artifact. Replacements and local edits invalidate the previous audit and require a whole-timeline rerun.

Use `scripts/check_visual_reuse.py work/visual-reuse-audit.json` during planning and add `--require-manual-pass` for final approval. Each interval in the JSON records `scene_id`, timeline start/end, root `source_lineage_id`, normalized source start/end, `rendered_start_frame_sha256`, `shot_signature`, and an optional `continuation_group_id`. The final `manual_review` records a reviewer plus evidence for normal-speed full-video review, a scene-boundary contact sheet, and non-adjacent scene comparison.

## Manual review

Review the first 15 seconds frame by frame and the full video at normal speed. Reject when any of these appear:

- any current production interval is visibly cartoon, illustrated, diagrammatic, or otherwise non-photorealistic without an explicit user-approved exception;
- slideshow feeling despite numerical motion;
- repeated or reversed loops;
- an earlier shot or action returning later in the video, even when it has a new filename, crop, speed, prompt, or provider task ID;
- hands, fingers, cigars, leaves, gauges, or cabinets changing shape;
- people or props teleporting between frames;
- labels or numerals crawling or mutating;
- generated pseudo-text, logos, labels, or numerals hidden by an opaque caption card, blur, or patch instead of rejecting the source shot;
- camera motion without subject purpose;
- an action cut before its motion reads clearly;
- several consecutive shots with the same angle, speed, or movement direction;
- central headline and lower subtitle duplicating the same sentence;
- subtitles outside the vertical safe area.
- ordinary subtitles on a solid background, auto-wrapped to multiple lines, paraphrased instead of spoken, or timed from an estimate;
- a visual action whose semantic purpose does not match the active spoken phrase and subtitle.

Record both the automated report and the human decision, including scene-boundary contact sheets and non-adjacent comparisons. A command-line manual-pass switch without review evidence is not a decision. Do not mark a failed clip as approved by lowering thresholds without explaining and obtaining approval.
