# Stage 1 — Deep Research & Viral Intelligence

> Send the Stage 1 banner FIRST, then execute. All internal steps run silently — no tool
> names, no search-query enumeration, no UUID talk. Read `references/capability.md` before
> Step 0 and `references/rubric.md` before Step 4.

**Output of this stage:** `[brand]-research-dossier.md` saved to outputs, plus the Viral
Content Brief presented in chat. Update the state file (`progress.stage_1`, `higgsfield.*`,
`artifacts.dossier`) when done.

---

## EVIDENCE LABELS (HARD RULE for everything in this stage)

Web search cannot see inside TikTok or Instagram. Search results about social content are
mostly secondhand (articles, SEO posts) and the model's instinct is to fill gaps with
plausible inventions. That destroys the dossier's value. Therefore every finding — every
hook, trend, and competitor observation — carries one of three labels:

- **VERIFIED** — you fetched the actual page and saw the content/claim yourself
- **REPORTED** — a search snippet or article states it, but you couldn't open the source
- **INFERRED** — your pattern-recognition guess, clearly labeled as a hypothesis

Rules:
1. NEVER state engagement numbers (views, likes) unless VERIFIED.
2. NEVER attribute a specific hook to a specific competitor unless VERIFIED or REPORTED
   with the source named.
3. INFERRED items are allowed — good hypotheses matter — but they must say INFERRED.
4. The Proven Hooks Library must contain at least 5 VERIFIED-or-REPORTED entries. If
   research comes up thin, say so honestly in the brief ("competitor content was hard to
   verify this run — these 4 hooks are confirmed, the rest are informed hypotheses") rather
   than padding with fabrications.
5. If a Brand Pack was uploaded, its hooks library entries keep their original labels and
   any performance notes — those are the most trustworthy entries you have. Merge new
   findings into it; never overwrite it.

---

## Step 0 — Probe Higgsfield capability (internal, silent)

1. `show_marketing_studio(action='presets')`
2. `show_marketing_studio(action='list', type='hook', size=100)`
3. `show_marketing_studio(action='list', type='setting', size=100)`

Write ALL returned names + UUIDs into `higgsfield.hooks`, `higgsfield.settings`,
`higgsfield.presets_snapshot` in the state file NOW — Stage 3 reads them from the file,
not from this conversation.

## Step 0.5 — Fetch the PDP (internal, silent)

If a PDP URL exists: `web_fetch` it. Extract product name + description, key claims and
differentiators, 5–10 review excerpts (recurring language, complaints, praised results),
price positioning, audience cues. Also fetch linked review/testimonial pages. All of this
is VERIFIED evidence. No URL → skip silently.

## Step 1 — Auto-detect product and niche (silent — never ask the user to confirm)

From the product image: category, variants/SKUs visible, packaging style + palette, target
demographic cues. From the URL/PDP: name, official category, brand voice, regional cues.
Derive: niche keyword (plain English), target market (default "Global / English-speaking"),
primary goal (default "Mixed awareness + conversion"), active presets (from the relevance
map in capability.md). Write all of it to `brand.*` in the state file.

User-facing output — one status line, phrased as a marketer's read, NOT a question:
> "Got it — looks like a [niche descriptor] with [variants]. I'll target a [market] audience
> and lean into what's actually moving in this category right now — challenge-style clips,
> sidewalk interviews, premium unboxing reveals, honest reviews, and audio-first ASMR."

## Step 2A — Market research (internal, silent; short status line OK)

Run in parallel, substituting `[niche]`, `[brand]`, `[current month year]`:

Trends: 1. `[niche] TikTok trending videos this week …` 2. `viral [niche] content Instagram
Reels …` 3. `[niche] YouTube Shorts trending …` 4. `[niche] brand content going viral …`
5. `top [niche] ads performing Meta …` 6. `[niche] UGC content trend …` 7. `[niche] hooks
that stop the scroll …` 8. `[niche] competitor brands social media strategy …`

Customer voice: 9. `[niche] honest reviews site:reddit.com …` 10. `[niche] what actually
works reddit complaints …` 11. `[product type] reviews site:amazon.com best sellers`
12. `[brand or product name] amazon customer reviews [year]`

Extract per result (with evidence label): format, hook patterns, visual style, brands
mentioned, engagement signals, customer language, pain points, praised results.

## Step 2B — Competitor + own-brand research (internal; only if competitor list non-empty)

Per competitor, in parallel: `[competitor] TikTok viral videos …` · `[competitor] Instagram
Reels top performing …` · `site:tiktok.com [competitor handle]`. If own handles provided:
`site:tiktok.com [own handle]` and `site:instagram.com [own handle]`.

Extract per competitor (labeled): top hook formats, opening lines, visual style, themes,
comment-section signals.

## Step 3 — Fetch source pages (internal)

`web_fetch` the 2–4 most promising URLs from 2A/2B. Anything successfully opened upgrades
to VERIFIED. Prioritize fetches that can verify REPORTED hook attributions.

## Step 2C — VOC synthesis (internal; surfaces in the dossier + brief)

From Reddit + Amazon + PDP reviews, extract: pain points (the problem before buying),
results language (exact customer phrases — quote them), objection language (doubts, negative
reviews), category language register (clinical / casual / dramatic), emotional hook triggers
(which results get the strongest reactions). Compress to a 5–8 bullet VOC Summary. Quote
real phrases in quotation marks with their source. These bullets are the copy DNA for every
hook and scene prompt.

## Step 2D — Proven Hooks Library (internal; surfaces in the dossier + brief)

Build 10–15 hooks observed to perform in this category. Per hook: hook line (first-3-seconds
verbal or visual opening) · hook type (problem/pain · transformation · curiosity gap ·
controversy · challenge · social proof · ingredient reveal · comparison · POV) · source WITH
EVIDENCE LABEL · why it works (1 sentence tied to a VOC bullet) · format fit (which of the
5 formats executes it best). If a Brand Pack library exists, merge into it.

## WRITE THE DOSSIER (before building the brief)

Save `[brand]-research-dossier.md` to outputs with sections: Product summary (from PDP) ·
VOC Summary · Proven Hooks Library (with labels) · Trend clusters · Competitor findings ·
Evidence notes (what couldn't be verified this run). Record the path in
`artifacts.dossier`. Stage 2 and 3 read VOC and hooks FROM THIS FILE.

## Step 4 — Synthesize the Viral Content Brief

Read `references/formats.md` (format definitions + gold-standard examples) and
`references/rubric.md` now.

- 15+ seed ideas, ~75% UGC-family, distributed across the 5 formats
- Every idea uses the REQUIRED card fields exactly as shown in the formats.md examples —
  match their specificity, not just their structure
- Every idea references a Proven Hooks Library entry and quotes VOC language
- Run every idea through the producibility self-check (below), then the rubric. Regenerate
  failures silently; only survivors enter the brief.

Producibility self-check: duration ≤15s? · preset routing matches idea strength (recipe →
tutorial, talking head → product_review, box reveal → ugc_unboxing, lifestyle/ASMR → ugc,
kinetic hero → hyper_motion, cinematic → tv_spot, surreal → wild_card, try-on →
virtual_try_on)? · picklist-legal hook and setting? · no forbidden patterns (lip-sync,
multi-character dialogue, split-screen)?

Brief structure: Product summary → VOC Summary → Proven Hooks Library → Trends table →
Competitor table → Hook patterns (verbal) → Format momentum → **Recommended Content Mix**
(present the per-format counts as a consequence of the research — "based on what's winning,
here's the mix" — never as a config rule; get counts from `allocate.py`) → seed ideas →
methodology footer (rubric line + evidence-label legend).

## Step 5 — Approval (button-driven)

> "Brief is built from your real competitor data, customer language, and proven hooks. What next?"
> - "Looks good — proceed to Stage 2 (Recommended)"
> - "Add more UGC ideas first"
> - "Swap some ideas"
> - "Adjust the mix ratios"

Only on click does the pipeline proceed. Update state file, then read
`references/stage-2-plan.md`.
