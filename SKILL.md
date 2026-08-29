---
name: ai-content-strategy-workflow
description: >
  Turn a brand or product brief into customer and competitor research, a source-grounded
  content strategy, campaign ideas, a production plan, and an execution-ready calendar.
  Works for any brand or category. Use for requests such as 'research this brand', 'create
  a campaign', 'build a content strategy', 'make a content plan', 'generate the assets',
  'schedule to Meta', 'upload to Instagram', or 'run the content workflow'.
---

# AI Content Strategy Workflow

A 5-stage workflow: Deep Research → Plan → Generate → Publish → Report.

The strategy and planning stages work independently. When a compatible Higgsfield
connection is available, the generation stage can execute the approved production plan.

This file is the ROUTER. It holds onboarding, global rules, and state management.
Each stage's detailed instructions live in a reference file. When a stage begins,
READ that stage's file and follow it exactly. Do not run a stage from memory of
having read the file earlier in a long conversation — re-read it at stage start.

| Stage | Read this file first |
|---|---|
| 1 — Deep Research | `references/stage-1-research.md` |
| 2 — Content Plan | `references/stage-2-plan.md` |
| 3 — Generate | `references/stage-3-generate.md` |
| 4 — Publish | `references/stage-4-publish.md` |
| 5 — Cost Report | `references/stage-5-report.md` |

Supporting files (read when instructed by a stage file):
- `references/capability.md` — Marketing Studio ground truth: presets, limits, mode mapping
- `references/formats.md` — the 5 UGC format definitions + gold-standard idea card examples
- `references/rubric.md` — the quality rubric every idea must pass before the user sees it
- `scripts/allocate.py` — deterministic math for splits, dates, and image-pack allocation

---

## STATE MANAGEMENT (the consistency backbone — HARD RULES)

The #1 failure mode of pipelines like this is state living in conversation memory:
long chats compact, sessions break, and cached UUIDs / research / plans silently
vanish or mutate. This skill therefore keeps ALL state in files.

**The state file:** `[brand]-campaign-state.json` in the outputs directory
(`/mnt/user-data/outputs/` on claude.ai; `./outputs/` if that path doesn't exist).

Schema (create at end of onboarding, update at every stage boundary):

```json
{
  "skill_version": "2.0",
  "brand": {"name": "", "pdp_url": "", "handles": {"tiktok": "", "instagram": ""},
             "competitors": [], "category": "", "niche_keyword": "",
             "variants": [], "palette": "", "positioning": ""},
  "campaign": {"name": "", "video_count": 0, "date_start": "", "date_end": "",
                "active_formats": [], "publish_channels": []},
  "higgsfield": {"product_uuid": "", "hooks": [{"name": "", "uuid": ""}],
                  "settings": [{"name": "", "uuid": ""}],
                  "avatars": [{"name": "", "uuid": "", "descriptor": ""}],
                  "presets_snapshot": []},
  "progress": {"stage_1": "pending|done", "stage_2": "pending|done",
                "stage_3": {"format_1": "pending|partial|done", "...": "",
                             "image_pack": "pending|done"},
                "stage_4": "pending|done", "stage_5": "pending|done",
                "failed_rows": []},
  "artifacts": {"dossier": "", "plan_json": "", "plan_html": "", "brand_pack": ""}
}
```

**Rules:**
1. **Write at every stage boundary.** The moment a stage completes (or a Stage 3 batch
   completes), update and re-save the state file. Never defer.
2. **Read, don't remember.** At the start of every stage — and after any long gap in the
   conversation — re-read the state file. If a value in your working memory disagrees with
   the file, THE FILE WINS.
3. **UUIDs live in the file only.** Hook, setting, avatar, and product UUIDs are written to
   `higgsfield.*` when probed in Stage 1 and read back in Stage 3. Never re-quote them from
   conversation memory.
4. **Resume behavior.** If the skill triggers and a `*-campaign-state.json` exists in outputs
   or is attached by the user, offer via AskUserQuestion: "Resume [campaign name] at
   [next incomplete stage]?" / "Start a fresh campaign". On resume, skip onboarding entirely.
5. **Missing state mid-pipeline.** If a stage needs state that isn't in the file (e.g. the
   plan JSON is gone), say so plainly and offer to regenerate that artifact — never silently
   improvise replacement values.

**Other artifacts (all saved to outputs, paths recorded in `artifacts`):**
- `[brand]-research-dossier.md` — Stage 1 output (VOC, hooks library, trends, competitor findings)
- `[brand]-video-plan.json` — Stage 2 machine-readable plan (source of truth for Stage 3)
- `[brand]-video-plan.html` — Stage 2 human-readable plan (rendered FROM the JSON)
- `[brand]-brand-pack.md` — the portable brand file (see below)

## THE BRAND PACK (cross-campaign persistence)

Chats don't share files, so anything learned in one campaign is lost unless exported.
The Brand Pack is a single portable markdown file the user re-uploads next campaign.

Contents: brand context (everything in `brand.*`), the curated Proven Hooks Library
(with evidence labels and any performance notes), VOC summary, what was generated last
campaign, and user preferences observed (e.g. "always skips with-people shots").

- **Generate/refresh it** at the end of Stage 3 (or whenever the user says "export my brand pack").
- **At onboarding Round 1**, if the user attached a Brand Pack: skip Round 2 entirely,
  seed the hooks library and VOC from the pack, and confirm with one button question:
  "Using your saved brand profile for [brand] — anything changed?"
  ("Nothing changed — go" / "Update competitors" / "Update product/PDP" / "Start from scratch")
- Tell the user at the end of every campaign: "Save this Brand Pack file — upload it next
  time and onboarding takes one click."

---

## GLOBAL HARD RULES (apply to every stage)

1. **Button-driven UX.** Every clarifying question is an AskUserQuestion call with 2–4
   concrete option buttons. Free-form typing is reserved ONLY for content the user must
   originate (product URL, competitor names, handles) — and even then offer a smart default
   accepted with one click. Bundle related questions into a single AskUserQuestion call.
2. **User-facing language.** The user is not a developer. Never narrate tool names, UUIDs,
   slug mappings, parallel-search mechanics, or file plumbing. One friendly stage banner at
   each stage start (exact banners below), one "Stage N done — [deliverable]" line at each
   stage end. If the user asks how it works under the hood, then explain.
3. **Deterministic math is done by the script, never in-head.** Format splits, date
   distribution, and image-pack allocation come from running `scripts/allocate.py`
   (see stage files for the exact invocation). If code execution is unavailable, use the
   lookup tables in the stage files — never freehand the arithmetic.
4. **Brand-agnostic.** Never hardcode any brand, product, or competitor into ideas, hooks,
   or copy. Everything specific derives from onboarding inputs and this run's research.
5. **No rendered text in any video.** Captions in the plan are upload metadata only. Every
   video prompt carries the no-text negative block (Stage 3 file has the template).
6. **Per-batch permission gates in Stage 3.** Never auto-run the full plan.
7. **Evidence honesty.** Research findings must carry evidence labels (VERIFIED / REPORTED /
   INFERRED — defined in Stage 1 file). Never invent engagement numbers or attribute a hook
   to a competitor without a source.
8. **Quality gate.** No idea card reaches the user before passing the rubric in
   `references/rubric.md`. Score silently; regenerate failures; show only survivors.
9. **5-format split.** Campaigns distribute across the 5 UGC formats (see `formats.md`)
   via `allocate.py`. Cinematic presets (Hyper Motion / TV Spot / Wild Card) are OFF by
   default, activated only on explicit user request.
10. **Failure handling.** Log failed generation rows to `progress.failed_rows` in the state
    file and offer "Retry / Skip / Pause" buttons. Never silently skip.

## STAGE BANNERS (use exactly; adapt only if the user sets custom phrasing)

| Stage | Banner |
|---|---|
| 1 | **🔍 Stage 1: Deep Research — starting now.** I'm pulling Reddit discussions, Amazon reviews, competitor TikTok and Instagram content, your own product page, and trending niche content — then synthesizing it into a proven hook library and Viral Content Brief built specifically for your brand. |
| 2 | **🗂️ Stage 2: Content plan — starting now.** I'm building your full video content plan as a polished HTML document, with every video mapped, dated, and ready to generate. |
| 3 | **🎬 Stage 3: Generating videos — starting now.** I'm producing your videos in Higgsfield Marketing Studio, one batch at a time. I'll ask before each batch fires, so you stay in control. |
| 3 (images) | **🖼️ Image asset pack — starting now.** I'm generating your social posts, hero banners, and product stills. |
| 4 | **📅 Stage 4: Publishing — starting now.** I'm setting up your campaigns and scheduling everything across the calendar you approved. |
| 5 | **💰 Stage 5: Cost report — starting now.** I'm compiling what you actually spent versus what this volume would cost the traditional way. |

---

## ONBOARDING — always runs first (TWO ROUNDS, NO PAUSES)

> Exception: if a Brand Pack or campaign-state file is present, use the resume / brand-pack
> flows from the State Management section instead.

Round 1 fires immediately on trigger. Round 2 fires the instant Round 1 is answered.
Both complete before any research begins. Never ask onboarding questions outside these
two rounds; once Round 2 is answered, proceed straight to the chosen stage with no extra
confirmation.

### Round 1 — stage, volume, product (SINGLE AskUserQuestion call)

**A — Higgsfield MCP connected?** "Yes — connected" / "Not yet — I'll connect now" / "Skip — research only"

**B — Starting stage:**
- "Stage 1 — Full pipeline (needs a product image)"
- "Stage 2 — Build content plan (I have a brief)"
- "Stage 3 — Generate now (I have a plan)"
- "Stage 4 — Publish (content is ready)"

Product image with no other context → default Stage 1.

**C — Video volume:** "50 videos" / "100 videos (Recommended)" / "150 videos" / "200 videos"
/ Other (any number). Store as `campaign.video_count`. Do NOT announce the per-format split
here — it surfaces naturally inside the Viral Content Brief.

**D — In the same message:** "Attach your product image OR drop a URL — that's all I need
to start." Skip D if the product is already attached. If Stage 3/4 chosen, swap D for
"Drop your existing content plan file."

### Round 2 — brand context + competitors (fires immediately; still onboarding, no banner)

**E — Brand context (text input, one message):**
> "One quick round before the deep research — things I can't infer from the image alone:
> 1. **Your product page URL** — I'll pull claims, ingredients, and customer reviews from it
> 2. **Your brand name** as you want it in the plan
> 3. **Your TikTok / Instagram handles** *(optional — I'll include your own best content in the research)*"

**F — Competitors (smart multi-select MCQ, same message):** auto-detect the niche from the
product image, then offer 5–8 known competitors in that category as multi-select buttons,
plus "None of these — I'll type them" and "All of the above + I'll add more".

Category → suggested competitors:
- Wellness supplements / adaptogens / sleep → Ritual, AG1, Olly, Thorne, Garden of Life, Care/of, HUM
- Energy / functional beverages → Prime, Ghost, Celsius, Bang, Reign, ZOA, C4
- Skincare / beauty / haircare → CeraVe, The Ordinary, Paula's Choice, Drunk Elephant, Tatcha, La Roche-Posay
- Food / snacks / bars → Kind, RXBAR, Larabar, Perfect Bar, That's It, Nature Valley
- Protein / fitness nutrition → Optimum Nutrition, Dymatize, Quest, Orgain, Gainful
- Apparel / footwear → Allbirds, Hoka, On, Lululemon, Gymshark
- Electronics / gadgets → Anker, Belkin, + sub-niche natives
- Home / kitchen → Vitamix, Instant Pot, Our Place, GreenPan
- No match → single text-input option: "I'll type the competitors I want researched"

Store answers into `brand.*` in the state file. Blank E or F → skip those research sub-steps
silently; do not re-prompt.

**End of onboarding:** create `[brand]-campaign-state.json`, then send the Stage 1 banner
and READ `references/stage-1-research.md`.
