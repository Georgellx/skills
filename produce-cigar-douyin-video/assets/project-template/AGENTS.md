# Cigar Douyin Video Project Rules

## Outcome

Turn approved Chinese cigar-knowledge content into an arbitrary-duration, native 9:16, narrated Douyin video that reproduces the locked reference style with original true-motion visuals.

## Sources of truth

Read before acting:

1. the parent workspace `AGENTS.md` and durable decisions;
2. `input/brief.json` and immutable user inputs;
3. `input/reference-style-lock.json`;
4. `work/job-state.json`;
5. `work/research-sources.json`, `work/scene-plan.json`, and `work/asset-manifest.json` when present.

The stricter applicable rule wins.

## Editorial rules

- Audit user text and images before writing.
- Verify changing or uncertain facts with current authoritative sources and retain claim mappings.
- Write conversational Chinese without AI-style filler or inflated certainty.
- Keep content educational and adult-oriented; do not add sales, prices, purchase links, smoking action, lit cigars, brands, minors, or unsupported health/status claims.
- Keep the health notice visible as required by the style lock.

## Character rules

- The channel host does not show a face by default. Use hands, arms, point-of-view, back, silhouette, or off-camera narration.
- A visible virtual character is considered only after an explicit user request.
- Before that branch, confirm the parent workspace allows digital characters, approve a consistent photorealistic character sheet, and record the decision.
- Never imitate a real person or add lip sync without separate approval.

## Voice and music

- Reuse the channel owner's stable authorized clone when available.
- If no valid local sample and authorization exist, use MiniMax `junlang_nanyou`.
- Generate the complete narration before timing scenes.
- Ask the user to supply optional background music and usage authorization. If absent, use no background music and do not source or generate one automatically.

## Motion and style

- Reproduce `input/reference-style-lock.json` as closely as possible in native 9:16.
- Do not crop or reuse the reference footage; create original footage with the same production grammar.
- Storyboard stills are never production footage.
- Reject still pans, zooms, parallax, overlays, or captions over a static base as video.
- Every shot requires semantic physical action plus a second independent movement layer.
- Build a full-timeline shot-reuse map with root source lineage, normalized source range, rendered-start-frame checksum, shot signature, and continuation group.
- Do not replay source ranges or reuse the same rendered first frame across scenes. A clip crossing the 15-second preview boundary must resume from the exact consumed source cursor.
- Run the motion checker and the full-timeline visual-reuse audit, then perform normal-speed and scene-boundary frame review before approval.

## Approval and paid calls

- Stop for explicit content-package approval before narration and preview production.
- Show provider calls and a numeric cost ceiling before the first paid call.
- Produce the actual first `min(15 seconds, full duration)` for preview.
- Do not start remaining full-length paid generation until `preview.approved` is exactly `true`.
- Persist and reuse provider job IDs. Never retry a paid generation blindly.

## Provenance and delivery

- Record every asset with origin, authorization or license evidence, provider job ID when generated, checksum, and consuming scenes.
- Unknown or restricted rights block production; unresolved review status blocks public release.
- Verify final media with `ffprobe`; file size alone is not proof of completion.
- Preserve completed stages and resume from recorded state.
