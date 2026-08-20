# Editorial cutting contract

## Work audio-first

Use word-level verbatim ASR as the timing authority. Read packed phrases for narrative reasoning, then inspect raw word timing only around chosen edges. Cache transcripts while source files remain unchanged.

Build the narrative from complete beats rather than source order. For each kept range, retain:

- source ID and exact source path mapping;
- padded source start and end;
- narrative beat;
- verbatim quote;
- concise editorial reason.

## Protect meaning

Remove false starts, recoverable slips, duplicated explanations, empty transitions, and excessive silence only when the remaining speech preserves the speaker's intended claim and tone. Retain human breaths, reactions, hesitations, or gestures when they carry emotion or make a cut feel natural.

Do not assemble words into a claim the speaker did not make. When a tighter target requires dropping a substantive beat, present that tradeoff for approval.

## Place cut edges

- Place the first kept edge before the first retained word and the last edge after the last retained word.
- Use 30–200ms as the normal padding range; inspect waveform and mouth motion when tighter or looser padding is needed.
- Apply a short audio fade at every extracted segment boundary.
- Prefer phrase boundaries with useful silence; inspect any boundary inside continuous delivery.
- Review both picture and waveform around every final cut.

## Maintain EDL integrity

Use ordered `ranges` as the output narrative order. Compute output offsets from cumulative kept durations. Derive captions and overlay timing from the output timeline, never from original source time alone.

Minimum schema:

```json
{
  "version": 1,
  "sources": {"source-id": "absolute-source-path.mp4"},
  "ranges": [
    {
      "source": "source-id",
      "start": 1.16,
      "end": 3.77,
      "beat": "HOOK",
      "quote": "保留的原话",
      "reason": "叙事作用"
    }
  ],
  "total_duration_s": 84.8
}
```

Run `validate_edl.py` against cached transcripts. Resolve errors before rendering. Review warnings at the stated source times and record intentional exceptions.

## Review the rough cut

Render speech and picture without final packaging first when the edit changes materially. Listen with the screen hidden once, then watch without sound once. Confirm:

- the argument remains coherent;
- pronouns and connective words retain their referents;
- cuts preserve plausible breath and mouth continuity;
- the opening reaches the premise quickly;
- the ending lands and holds long enough for comprehension.
