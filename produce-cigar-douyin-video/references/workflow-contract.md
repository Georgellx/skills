# Workflow Contract

## Project state

Use this order and persist every transition in `work/job-state.json`:

```text
initialized
  -> intake_ready
  -> research_ready
  -> waiting_for_content_approval
  -> content_approved
  -> narration_ready
  -> scene_plan_ready
  -> preview_generating
  -> waiting_for_preview_approval
  -> full_generation
  -> rendering
  -> quality_review
  -> complete
```

Preserve the last successful state after failures. A timeout or missing download URL does not authorize a new provider job.

## Intake

Record:

- topic, user text, and immutable copies of supplied images or screenshots;
- intended audience and platform; default to adult Chinese Douyin viewers and `9:16`;
- user ownership or permission declaration for every supplied asset;
- channel voice profile and any stable cloned `voice_id`;
- optional background-music path and authorization;
- whether a visible virtual character was explicitly requested.

Ask for background music once during intake: “如需背景音乐，请上传音乐文件并说明使用授权；不提供则成片不加背景音乐。” Do not search for, generate, or extract music when none is supplied.

## Editorial research

Evaluate the user's premise before enriching it. Separate:

- stable cigar craft and storage knowledge;
- claims that require current verification;
- personal preference or experience;
- health, advertising, platform, or legal risk;
- unsupported precision, causal claims, and universal promises.

Browse when the content involves current rules, product information, trends, recent events, or a claim with meaningful uncertainty. Prefer primary and authoritative sources. Record each usable claim with its source URL, title, publisher, publication/update date, access date, and the exact script sentence it supports.

Trend research may improve the hook or framing, but may not copy another creator's wording, shot sequence, footage, title, or music.

## Editorial review package

Deliver one review package before paid preview production:

1. One recommended hook and up to two alternatives.
2. The complete natural spoken script.
3. Claim-by-claim fact notes and risk edits.
4. An audio-driven scene plan with actions, locations, props, camera movement, subtitle mode, and a full-timeline shot-reuse map.
5. Scene and optional character reference images for visual review only.
6. The reference-style mapping for the first 15 seconds.
7. The proposed voice route.
8. Background-music status: supplied or none.
9. Exact paid provider calls and maximum cost.

Set `state=waiting_for_content_approval` and stop. Record explicit approval text and a fingerprint of the approved script, style profile, voice route, music file, and scene plan.

Treat cost controls as two separate values: an optional total budget explicitly declared by the user, and a mandatory bounded ceiling for the current provider-call batch. Never turn an estimated production total into a persistent project-wide budget without the user's instruction. If the user requests no total cap, leave the project budget unset while retaining exact per-batch call counts, maximum cost, approval binding, and zero automatic create retries.

Serialize all paid provider state transitions within one project. Do not run separate scene creates, status queries, downloads, or manifest/state writers concurrently unless a single transaction lock protects `provider-jobs.json`, `job-state.json`, `asset-manifest.json`, and `scene-plan.json` together. After a local write conflict or interrupted caller, reconcile the persisted request fingerprint, provider ID, output checksum, and charged cost before classifying the outcome; a caller-side error does not prove that the provider call failed.

## Full-timeline visual reuse audit

Plan and review the opening preview and remaining timeline as one visual sequence. For every rendered interval, persist the root source lineage, normalized source start/end, rendered-start-frame checksum, shot signature, and continuation group when applicable. Fail the plan when a later interval restarts an already consumed source range, copies a rendered first frame, or repeats the same composition and action under a different filename, crop, speed, or generation job.

Adjacent semantic scenes may share one source only when they are an explicitly declared continuous shot with contiguous, forward-only source ranges. If the interval crosses the 15-second preview boundary, the final composer must resume at the exact source cursor consumed by the approved preview. Insufficient source duration requires a distinct replacement shot; it never authorizes replay.

Run the complete reuse audit before preview approval, after every asset replacement or regeneration, and again on the composed full video. The final audit must include machine-readable lineage/range results plus evidence of normal-speed full-video review, boundary contact sheets, and non-adjacent near-duplicate comparison. Do not accept a bare manual-pass flag as evidence.

## Voice

Prefer the channel owner's authorized stable clone:

1. Locate the saved channel voice identity and local authorized sample.
2. Verify the sample checksum and authorization record.
3. Reuse the existing stable clone `voice_id`; do not reclone per video.
4. Create a clone only when no stable identity exists, the sample is human, authorization is retained, and the paid plan is approved.

When no valid local sample and authorization exist, use the MiniMax official system voice `junlang_nanyou`. Do not send a missing or unauthorized sample to a clone endpoint.

Generate the complete final narration before timing scenes. Produce sentence- or word-level timestamps with a local compatible alignment backend and use that verified artifact as the timeline source of truth. Equal scene intervals, character-weighted timing, silence-only guesses, or a timing artifact marked as estimated or still requiring human alignment review cannot enter preview rendering.

## Character policy

Default to no visible host face. Use hands, arms, back, silhouette, point-of-view, shallow-focus background people, and off-camera narration.

If the user explicitly asks for a visible virtual person:

- stop and check the active workspace rules;
- collect the role, age band, appearance, clothing, scene function, and continuity requirements;
- require explicit approval of a photorealistic AI character sheet before generating shots;
- keep the identity consistent with approved reference images and provider reference controls;
- never imitate a real identifiable person, use a minor, or imply the virtual person is real;
- do not add talking-head lip sync unless separately requested and permitted.

If a parent `AGENTS.md` or durable decision prohibits digital humans or portraits, record the request as blocked pending a policy change. A Skill cannot silently override it.

## Preview and completion

Render the real first `min(15 seconds, total duration)` from final narration and production visuals. Include final typography, health notice, supplied music when present, natural ambience when authorized, and the production transition policy.

Show the complete remaining scene summary and cost together with the preview. Set `state=waiting_for_preview_approval` and stop.

Only `preview.approved=true` authorizes remaining full-length visual generation. Verify final streams, duration, sync, subtitles, movement, shot uniqueness, provenance, and rights before delivery. Preview quality must fail when ordinary subtitles are not sourced from the final alignment artifact, when the active visual, spoken phrase, and subtitle are not semantically consistent, when a source range or near-identical shot is repeated, or when any production interval is cartoon, illustrated, diagrammatic, or otherwise non-photorealistic without the user's explicit exception.
