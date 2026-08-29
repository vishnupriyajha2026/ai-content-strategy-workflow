# Stage 2 — Video Content Plan

> Send the Stage 2 banner first. Re-read the state file and the research dossier before
> starting — the plan is built FROM the dossier, not from conversation memory.

**Outputs of this stage:**
1. `[brand]-video-plan.json` — machine-readable, the single source of truth Stage 3 executes
2. `[brand]-video-plan.html` — human-readable document rendered FROM the JSON

Update state file (`progress.stage_2`, `artifacts.plan_json`, `artifacts.plan_html`) when done.

## Step 1 — Confirm campaign details (single AskUserQuestion, all buttons, smart defaults)

- Campaign name → "Use auto: [Brand] [Season] Campaign [month year]" / "Different name"
- Date range → "Next 30 days (Recommended)" / "Next 60 days" / "Next 90 days" / "Custom"
- Variants → multi-select buttons listing every variant detected on the product

Do NOT ask about the format breakdown — it was already revealed naturally in the brief.
If the user wants to override the split they'll say so; otherwise the computed values stand.
Goal and brand colors are auto-derived; don't ask unless the user raises them.

## Step 2 — Run the allocation script (deterministic — never do this math in-head)

```
python3 scripts/allocate.py --videos [VIDEO_COUNT] --start [YYYY-MM-DD] --end [YYYY-MM-DD] \
  --formats [comma-separated active format numbers, e.g. 1,2,3,4,5]
```

The script returns JSON: per-format counts (floor split, remainder from format 1), an
interleaved date schedule (formats mixed day-to-day so the feed never dumps 20 reviews
back-to-back), and the image-pack allocation. Use its output verbatim.

**Fallback if code execution is unavailable** (do not freehand beyond these tables):
per-format count = floor(N/5), remainder +1 starting at format 1. For 50: 10 each.
For 100: 20 each. For 150: 30 each. For 200: 40 each. Dates: cycle formats 1→2→3→4→5
repeating, spacing videos evenly across the window.

## Step 3 — Build the plan JSON

Every row:

```json
{"id": 1, "date": "YYYY-MM-DD", "format": 1, "format_name": "UGC Entertainment",
 "preset": "ugc", "mode": "UGC", "duration_s": 9, "aspect_ratio": "9:16",
 "setting": "Kitchen", "system_hook": "Camera Bump", "audio": true,
 "persona": "mid-20s roommate type", "scene_prompt": "...", "hook_line": "... (source)",
 "voc_language": "\"...\"", "caption": "...", "goal": "awareness",
 "variant": "yuzu", "status": "pending"}
```

Rules:
- Concepts come from the approved brief ideas first; extend with unused concept seeds from
  `references/formats.md` until every row is filled. No two rows in the same format share
  a concept. New concepts (not from the approved brief) must pass the rubric before entering
  the plan.
- `caption` is upload metadata ONLY — never rendered in the video (Stage 3 enforces).
- Multi-clip sequences: two rows labeled "(1/2)" and "(2/2)" in the scene title.
- Distribute variants evenly within each format.
- `system_hook` and `setting` must be names present in the state file's picklists.

Save the JSON to outputs.

## Step 4 — Render the HTML plan from the JSON

One polished HTML document: campaign header (name, dates, volume, mix), then rows grouped
by format bucket in order 1→5 (this grouping powers Stage 3's per-batch gates), showing
every field except internal ones (`status`). Brand-color header treatment derived from the
product palette. Save to outputs.

## Step 5 — Present and gate

Show the HTML plan. AskUserQuestion:
> "Plan is ready — [N] videos across [k] formats, [date range]. What next?"
> - "Approved — start generating (Stage 3)"
> - "Adjust some rows first"
> - "Change the date spread"
> - "Pause here"

On approval: update state, read `references/stage-3-generate.md`.
