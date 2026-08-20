# Subtitle contract

## Derive from the final edit

Generate caption timing from aligned words after the EDL is locked. Convert source word times to output times with the segment's cumulative output offset. Keep a structured `caption-plan.json` and derive `master.srt` or the composition's caption data from it.

## Group by spoken meaning

Build each cue from one continuous semantic unit. Prefer this boundary order:

1. sentence-ending punctuation and completed propositions;
2. aligned natural pauses;
3. complete subject-predicate, verb-object, modifier-head, or enumerated phrase units;
4. rendered-width limits.

Keep a dependent fragment with the phrase it modifies. Keep references such as “这个阶段”“这件事”“所以” with the clause that supplies their meaning. Split a long sentence at a natural spoken boundary rather than fixed character counts.

Ordinary captions should remain verbatim except for approved punctuation and normalization. Treat kinetic headlines as a separate editorial track; they may condense only the idea active at that moment.

## Time each cue

- Start from the first spoken word in the cue and end after its last spoken word with only a small readability tail.
- Clear the prior cue before the next semantic unit begins.
- Keep cues non-overlapping unless the approved design explicitly supports multiple speakers.
- Preserve short silent gaps instead of stretching unrelated text across them.
- Review the rendered output at normal speed; waveform alignment alone is insufficient.

## Fit the vertical frame

- Prefer one line for short-form vertical talking-head captions.
- Measure rendered width; reduce font size within the approved scale before wrapping.
- Place ordinary captions inside the lower safe area and outside platform interaction controls.
- Keep captions independent from portrait and information regions.
- Use high-contrast text, outline, or shadow appropriate to the background; use a plate only when the approved visual system calls for one.
- Apply captions as the final compositing layer or the highest intentional layer in an all-in-one composition.

## Validate twice

Run `validate_subtitles.py` for timing, overlap, embedded sentence breaks, display width, and reading-speed warnings. Then perform a human semantic review using the transcript, audio, and rendered video together.

Record intentional exceptions in `caption-plan.json` with a brief reason rather than weakening the validator globally.
