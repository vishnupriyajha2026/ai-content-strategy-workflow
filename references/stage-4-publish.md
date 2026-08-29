# Stage 4 — Publish to Meta Ads and/or Instagram

> Send the Stage 4 banner first. Re-read the state file and plan JSON — publishing follows
> the plan's dates and captions.

## Step 1a — Channel selection (FIRST question, always)

> "Content is ready. Where do you want to publish?"
> - "Meta Ads only (Facebook + Instagram placements via Ads Manager)"
> - "Instagram organic only (feed Reels + Stories)"
> - "Both — Meta Ads AND Instagram organic"
> - "Skip publishing — give me an exportable calendar instead"

Store as `campaign.publish_channels`. "Both" → Meta Ads flow first, then Instagram.

---

## META ADS FLOW

**1b. Connection check:** "Is your Meta MCP connected to Meta Ads?" — "Yes (Recommended)" /
"Not connected — help me install it now" / "Skip Meta — just do Instagram".

If installing: `search_mcp_registry(["meta ads", "facebook ads", "meta marketing"])`, then
`suggest_connectors` with matching IDs so the install card renders in chat. Fallback line:
"If the card doesn't show, open Settings → Connections and search 'Meta Ads'.
[Docs → https://docs.claude.com/en/docs/agents-and-tools/mcp]". Then re-ask 1b.

**1c. Campaign details (single AskUserQuestion, all buttons):**
- Objective: "Awareness" / "Traffic" / "Conversions" / "Mixed"
- Budget tier: "$500" / "$1,500 (Recommended)" / "$5,000" / "Custom"
- Dates: "Match the content plan (Recommended)" / "Next 30 days" / "Custom"

Ad Account ID auto-detected from the MCP; only ask (as buttons) if multiple accounts return.

**1d. Calendar review:** present the calendar → "Schedule looks good?" — "Yes — schedule
everything" / "Yes — but start with week 1 only" / "Adjust dates first".

**1e. Create campaigns:** per batch — create campaign with objective, create ad sets
(targeting via buttons: "Auto-target lookalike" / "Use saved audience" / "Define new"),
upload the generated videos/images as creatives, schedule per plan dates.

**1f. Confirm:** summary table by week. Then Instagram flow if "Both", else Stage 5.

---

## INSTAGRAM ORGANIC FLOW

**2a. Connection check:** "Is your Instagram Business account connected?"
- "Yes — via Meta MCP (same account)" → proceed to 2b
- "Yes — I use a scheduling tool (Later, Buffer, Hootsuite…)" → export scheduler-ready
  package: media folder + CSV (`Date · Time · Platform · Content type · Filename · Caption ·
  Hashtags · CTA link`) to `outputs/[brand]-instagram-schedule/`. Skip to Stage 5.
- "Not connected — export a posting schedule" → same CSV + folder, plus note: "Upload via
  Meta Business Suite, Creator Studio, or any scheduler — captions are pre-written."
  Skip to Stage 5.

**2b. Format optimization (live publishing only):** Reels 9:16 ≤60s (our clips qualify) ·
Feed 1:1 or 4:5 · Stories 9:16 · Carousels from the 1:1 social images. Present the mapping
table → "Post as shown?" / "Adjust formats" / "Reels only".

**2c. Captions + hashtags:** use each row's plan caption; auto-append 5–10 hashtags derived
from niche, brand, and VOC keywords. Show one sample → "Use this style for all" / "Adjust
hashtag count" / "I'll write custom captions".

**2d. Schedule via Meta Graph API** per plan dates. Stagger Reels and carousels — never dump
everything on one day.

**2e. Confirm:** summary table (post counts by type × week). Then Stage 5.

---

## CALENDAR EXPORT FLOW

Export `[brand]-content-calendar.csv` (or .xlsx): `Date · Time · Platform · Format · Preset ·
Video filename · Image filename · Caption · Hashtags · Goal · Notes` → outputs. Then Stage 5.

---

Update state file (`progress.stage_4`) and read `references/stage-5-report.md`.
