# Audio, Subtitle, and Visual Sync Contract

## Required artifacts

Generate the complete selected-voice narration first. Align that exact audio to the approved script with `faster-whisper` or another local compatible backend and store ordered word or spoken-caption timestamps. The artifact must record its backend, audio checksum, confidence or review evidence, and `estimated=false`.

Do not render a preview when alignment is based only on total duration, character weights, equal scene lengths, or silence detection. Do not pass an artifact with `human_alignment_review_required=true`.

## Ordinary subtitles

- Source every subtitle from the final alignment artifact; generic composers must not contain project-specific spoken strings.
- Preserve the words being spoken. Remove punctuation only when it improves reading without changing meaning.
- Use one line in the lower safe area, normally 78–83% of frame height.
- Use transparent background, white text, dark stroke, and soft shadow. No black rectangle, pill, or card by default.
- Split long text at an aligned pause. Never auto-wrap or shrink it into multiple lines.
- Start and end each subtitle on its aligned spoken span; do not display the next sentence early or retain the previous sentence over a new idea.

## Kinetic headlines

Keep headlines on a separate timed track. They may shorten only the phrase currently being spoken. They may not replace ordinary subtitles after the opening headline window, introduce later facts early, or cover visual defects.

## Visual timing

Derive shot boundaries from aligned semantic spans. For every shot record the active spoken-caption IDs and the visual action that explains them. A shot may bridge adjacent phrases only when its action supports both.

Review the preview at normal speed with sound and frame samples at every subtitle and shot boundary. Fail when the spoken phrase, visible subtitle, and visual action are not mutually consistent.

Generated pseudo-text, unstable labels, or wrong props make the source shot unusable. Regenerate it or select an approved alternate; do not conceal it with a text background, blur, crop, or patch and then mark it passed.
