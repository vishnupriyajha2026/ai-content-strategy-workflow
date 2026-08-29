# Stage 5 — Cost Comparison Report

> Send the Stage 5 banner first. Re-read the state file for actual generated volumes.

**Output:** `outputs/[brand]-cost-comparison.html` — actual Higgsfield spend vs the estimated
cost of producing the same volume traditionally.

## Step 1 — Pull live spend

`transactions(limit=200)` (highest available). Filter to jobs created during the Stage 3
window (campaign start → now). Sum credits per preset and per asset type, plus total.

Credits → USD at the user's plan rate. Common rates: Creator ≈ $0.02/credit · Team/Pro ≈
$0.01–$0.005/credit. If the rate isn't surfaced, present credits-only and note it's
plan-dependent. Never invent a rate.

## Step 2 — Traditional cost model (2026 industry-average midpoints; show low–mid–high)

| Asset type | Low | Mid | High | Why the range |
|---|---:|---:|---:|---|
| UGC creator video (TikTok/Reels) | 250 | 750 | 1,500 | Creator fee + light production |
| Product Review video | 300 | 900 | 2,000 | Talent + setting + edit |
| Tutorial / Recipe video | 400 | 1,200 | 2,500 | Recipe shoot + post |
| Unboxing video | 300 | 800 | 1,500 | Box creation + shoot + edit |
| Hyper Motion CGI hero ≤15s | 3,000 | 9,000 | 15,000 | CGI/VFX studio half-day to two-day |
| TV Spot 15s | 15,000 | 50,000 | 150,000 | Production + DOP + cast + post |
| Wild Card / FOOH stunt | 30,000 | 100,000 | 500,000+ | Real FOOH = full crew |
| UGC Virtual Try On | 200 | 600 | 1,000 | Quick try-on shoot |
| Pro Virtual Try On | 1,000 | 3,000 | 5,000 | Studio quality |
| Social post (1:1 still) | 100 | 250 | 500 | Photographer half-day |
| Hero banner (16:9) | 1,000 | 2,500 | 5,000 | Studio + retouch |
| Photoshoot WITH people | 500 | 1,500 | 3,000 | Half-day with talent |
| Photoshoot WITHOUT people | 200 | 700 | 1,500 | Studio product photographer |

Time-savings benchmarks: ~80 mixed videos = 1–3 hours render vs 4–12 weeks production ·
~20-image pack = 5–15 min vs 1–3 weeks · scheduling = minutes vs days of trafficking.

Cite as "Industry-average estimates, 2026"; let the user override with their own rate card.

## Step 3 — Compute (via allocate.py where possible; otherwise show the arithmetic)

- `traditional_[low|mid|high] = Σ (asset_count × rate)` per asset type
- `higgsfield_usd = total_credits × plan_rate` (rate disclosed)
- `savings_pct_mid = 1 − higgsfield_usd / traditional_mid` (cap 99.99%)
- time savings = traditional weeks − render hours

## Step 4 — Render the HTML report

Sections, in order:
1. **Hero number card** — "[Campaign]: delivered for **$X** instead of **$Y–$Z**. You saved
   **N%** and **W weeks**."
2. Volume summary (what was generated, per type)
3. Higgsfield spend breakdown (credits per preset/asset, USD at disclosed rate)
4. Traditional cost breakdown (low/mid/high per asset type with subtotals)
5. Side-by-side comparison with simple HTML/CSS horizontal bars (no external chart libs)
6. Time savings panel
7. Methodology footer — traditional costs are 2026 industry-average estimates (not quotes),
   Higgsfield USD based on plan rate at report time, prices vary by region/agency tier

Same brand-color header treatment as the plan documents.
Title: `[Campaign name] — Cost Comparison Report`.

## Step 5 — Present (button confirm)

Show the saved file. Final AskUserQuestion: "Cost report ready. What next?"
- "Done — close the pipeline (Recommended)"
- "Email this report to my team"
- "Adjust the traditional-cost rate card and re-render"
- "Run the pipeline again for another product"

Update state file (`progress.stage_5 = done`). Remind the user to save their Brand Pack.
