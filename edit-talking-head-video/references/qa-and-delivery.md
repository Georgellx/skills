# QA and delivery contract

## Review every approval artifact

Apply the same minimum checks to a style prototype, full preview, and final render. A shorter artifact reduces the number of samples, not the quality standard.

## Run structural checks

- Validate EDL structure and word-boundary proximity.
- Validate caption timing, overlap, display width, and reading speed.
- Run the selected animation engine's lint, runtime, layout, motion, and contrast checks.
- Verify output duration, resolution, display aspect, frame rate, codecs, audio streams, and pixel format.
- Measure integrated loudness and true peak after final encoding.
- Detect black intervals and inspect intentional fades separately.

Store machine-readable results in `edit/qa/report.json`.

## Build visual evidence

Generate:

- a representative whole-video contact sheet;
- frames immediately before and after every scene transition;
- cut-boundary filmstrips with waveform for each EDL edge;
- first two seconds, last two seconds, and all high-intensity motion moments;
- safe-area frames for portrait-window and dense-information scenes.

Use `make_qa_contact_sheet.py` for the overview and the Video Use timeline helper for close boundary review.

## Review at normal speed

Watch the complete output with sound and captions. Confirm:

- the narrative remains coherent and natural;
- every caption expresses only the active spoken meaning;
- portrait, information, captions, and platform-safe regions remain independent;
- face, hands, and topic objects remain readable when relevant;
- motion lands on its spoken cue and resolves long enough to understand;
- transitions preserve visual continuity without flashes or duplicate layers;
- audio has consistent speech level and clean cut boundaries.

Also listen once without looking at the image and scan once without sound.

## Use measurable delivery defaults

For a standard Chinese vertical short-video deliverable, use 1080×1920, square pixels, 30fps, H.264 video, AAC 48kHz audio, and the workspace's approved duration. Target speech near -14 LUFS while keeping true peak at or below -1 dBTP unless the platform or user specifies otherwise.

Treat these as project defaults, not permission to override an explicit delivery specification.

## Limit internal iteration

Fix, rerender, and recheck for at most three internal QA rounds. If a material issue remains, describe the exact timestamp, evidence, impact, and available options to the user.

Deliver only the latest approved files. Preserve diagnostics under `edit/verify/`, append the final outcome to `edit/project.md`, and report the final path, media parameters, measured audio, and known limitations.
