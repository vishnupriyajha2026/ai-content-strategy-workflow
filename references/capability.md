# Marketing Studio Capability Ground Truth

Always honor these constraints. The lists below are reference snapshots that may drift —
Stage 1 Step 0 probes Higgsfield for live values and writes them to the state file. When
the live probe and this file disagree, THE LIVE PROBE WINS.

## Hard limits (Marketing Studio video model)

- **Duration:** 4–15 seconds per single clip. PERIOD. Longer narratives must be designed as
  a 15s cut OR explicitly as a 2-clip sequence (clip A + clip B, edited externally).
- **Aspect ratios:** auto · 21:9 · 16:9 · 4:3 · 1:1 · 3:4 · 9:16
- **Resolution:** 480p · 720p · 1080p
- **Audio:** optional via `generate_audio` — set `true` for ASMR-style UGC.
- **Reference media:** product image (always pass), avatar image (UGC family).

## The 9 presets

| Preset (slug) | Built for | Hook + Setting picklist? | Best for ideas like… |
|---|---|---|---|
| `ugc` — UGC | Realistic single-take social videos, person + product | ✅ | First-sip POV, fridge-caught, day-in-life, ASMR close-ups |
| `tutorial` — Tutorial | Step-by-step how-to / recipe | ✅ | "Make a mocktail in 60s", "How to enjoy X" |
| `ugc_unboxing` — Unboxing | High-quality unboxing reveal | ✅ | Box reveal, hangtag-pull, first-look |
| `hyper_motion` — Hyper Motion | Kinetic product hero shots | ❌ | The pour, droplet impact, cap-pop reveal |
| `product_review` — Product Review | Authentic talking-head review, product in hand | ✅ | Honest review, ingredient reveal, "I tried this for X days" |
| `tv_spot` — TV Spot | Cinematic commercial narrative | ❌ | Brunch scene, first-summer-day (≤15s) |
| `wild_card` — Wild Card | Surreal one-shot concepts | ❌ | FOOH stunts, giant bottles, dreamlike |
| `ugc_virtual_try_on` — UGC Virtual Try On | Casual try-before-buy | ✅ | Apparel, eyewear, accessories |
| `virtual_try_on` — Pro Virtual Try On | Studio-quality try-on | ✅ | Premium try-on, hero campaign |

**UGC family (picklist hook + setting + audio):** `ugc` · `tutorial` · `ugc_unboxing` ·
`product_review` · `ugc_virtual_try_on` · `virtual_try_on`. These are the workhorses.

## CRITICAL — `mode` on every generate_video call (never narrate this to the user)

Without an explicit `mode`, `marketing_studio_video` defaults to UGC and rewrites the prompt
as a UGC scene — even when the prompt says "no people, kinetic product hero shot." This is
the most common failure mode of the whole pipeline.

The `slug` from `show_marketing_studio(action='presets')` does NOT always match what
`generate_video.mode` accepts. Always pass the **title-case `mode` value** from
`presets[].mode` — the server normalizes it.

| Pass this as `mode` | Slug equivalent | Slug matches presets[].slug? |
|---|---|---|
| "UGC" | `ugc` | ✓ |
| "Tutorial" | `ugc_how_to` | ✗ (slug says `tutorial`) |
| "Unboxing" | `ugc_unboxing` | ✓ |
| "Hyper Motion" | `product_showcase` | ✗ (slug says `hyper_motion`) |
| "Product Review" | `product_review` | ✓ |
| "TV Spot" | `tv_spot` | ✓ |
| "Wild Card" | `wild_card` | ✓ |
| "UGC Virtual Try On" | `ugc_virtual_try_on` | ✓ |
| "Pro Virtual Try On" | `virtual_try_on` | ✓ |

## Preset relevance map — auto-filter by product category

Not every preset fits every product. Auto-decide scope from the category; the user can
override via button.

| Product category | Relevant presets |
|---|---|
| Single-SKU beverage (juice, soda, kombucha, water, energy) | `ugc` · `product_review` · `hyper_motion` · `tv_spot` · `wild_card` |
| Beverage with mixology/recipe angle | + `tutorial` |
| Beverage subscription / gift box / multi-SKU trio | + `ugc_unboxing` |
| Food (snack, bar, jar, sauce, instant, cereal) | `ugc` · `product_review` · `tutorial` · `hyper_motion` · `tv_spot` · `wild_card` |
| Skincare / beauty / haircare | `ugc` · `product_review` · `tutorial` · `ugc_unboxing` · `hyper_motion` · `tv_spot` · `wild_card` |
| Wellness supplement / vitamin / gummy | `ugc` · `product_review` · `tutorial` · `ugc_unboxing` · `hyper_motion` · `tv_spot` · `wild_card` |
| Apparel / accessories / footwear | `ugc` · `product_review` · `ugc_virtual_try_on` · `virtual_try_on` · `hyper_motion` · `tv_spot` · `wild_card` |
| Eyewear / jewelry / watches | + `ugc_unboxing` |
| Premium / gift / luxury (perfume, candle) | `ugc` · `product_review` · `ugc_unboxing` · `hyper_motion` · `tv_spot` · `wild_card` |
| Electronics / gadget / appliance | `ugc` · `product_review` · `tutorial` · `ugc_unboxing` · `hyper_motion` · `tv_spot` · `wild_card` |
| Software / SaaS / app | `ugc` · `product_review` · `tutorial` · `tv_spot` · `wild_card` (no Hyper Motion — no physical hero) |
| Service / subscription / fitness app | same as software |
| Home / kitchen / housewares | `ugc` · `product_review` · `tutorial` · `ugc_unboxing` · `hyper_motion` · `tv_spot` · `wild_card` |

When in doubt: universal core = `ugc` · `product_review` · `hyper_motion` · `tv_spot` ·
`wild_card`. Redistribution rule: when presets are excluded, their share flows back into the
UGC family first (heaviest into `ugc`, then `product_review`).

## Hooks and Settings picklists

**Hooks (UGC family)** are visual scene templates, NOT verbal copy. Seen live: Product Hit,
Spicy, Interview, Random Object Mic, Product Crash, Blizzard, Camera Bump, Product Dodge,
Epic Fail. UUIDs resolve at runtime via the Stage 1 probe (stored in state file).

**Settings (UGC family).** Realistic: Bedroom, Bathroom, Kitchen, Office, In Car, Street,
Gym, Nature. Unrealistic: Airplane Wing, Roofing, Volcano Rim, Tiny Reviewer, Car Roof,
Train Surf.

A "hook line" written for the plan is VO/caption copy. The system `hook_id` is a structured
visual template from the picklist. These are different things — never conflate them.

## ASMR routing (content style, not a preset)

- Preset: `ugc` (or `ugc_unboxing` for crinkle/wrap-pull ASMR)
- `generate_audio: true`
- Setting: Kitchen / Bathroom / Bedroom (intimate, low-noise) — never Street, In Car, Gym
- Hook: usually `none` — the close-up carries attention
- Prompt focus: close-up handling, cap unscrewing, pour, clinks, condensation. No talking.

## What Marketing Studio CANNOT do (never propose ideas needing these)

- ❌ Single clips longer than 15 seconds
- ❌ Reliable lip-synced dialogue from non-human characters
- ❌ Multi-character coordinated dialogue with consistent identities across cuts
- ❌ Split-screen / multiple settings / day-X-vs-day-Y diary in a single output
- ❌ Free-form `hook_id` or `setting_id` outside the picklist

## Escape hatch (use sparingly — UGC-first means most ideas stay inside Marketing Studio)

Ideas genuinely needing lip-sync, longer narrative, or multi-shot continuity get labeled
**"Outside Marketing Studio"** and route to: Wan 2.7 (synced audio + character consistency),
Veo 3.1 (ultra-realistic cinematic), Cinema Studio Video 3.0 (cinema-grade), Seedance 2.0
(reference-driven, multi-SKU identity), Kling 3.0 (multi-shot, audio sync, motion transfer).
