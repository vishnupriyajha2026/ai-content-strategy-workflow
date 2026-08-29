# The 5 UGC Formats — campaign mix + gold-standard examples

Every campaign distributes across these 5 formats (counts come from `scripts/allocate.py`).
Each format maps to a specific preset. When generating idea cards, vary the concept seed
within each format — no two videos in the same format should be the same concept.

> Generation note: Formats 1, 2, 5 all share `ugc` preset / `"UGC"` mode at the API level.
> What differentiates them is the system hook, the setting, the audio flag, and the prompt.
> Format 3 uses `ugc_unboxing` / `"Unboxing"`. Format 4 uses `product_review` / `"Product Review"`.

## Format 1 — UGC Entertainment
- **Vibe:** challenge / dare / entertainment-first. The product is the punchline, not the subject.
- **Preset:** `ugc` · **Mode:** `"UGC"` · **Audio:** on
- **Recommended system hooks:** Product Hit · Product Dodge · Product Crash · Random Object Mic · Epic Fail · Camera Bump
- **Concept seeds:** blind taste "guess which one is [brand]" · "$100 if you try it" street
  challenge · "will it pour?" absurd pour · product-flying-into-frame deadpan reaction ·
  failed dare → recover → review pivot · epic-fail backflip → unflappable product hold

## Format 2 — Street Interview
- **Vibe:** Erewhon-style sidewalk stranger interviews where the product appears in
  conversation. High-trust, "real people."
- **Preset:** `ugc` · **Mode:** `"UGC"` · **Audio:** on
- **System hook:** Interview (specifically) · **Setting:** Street (always)
- **Concept seeds:** "what's your favorite [niche] right now?" → stranger pulls product from
  bag · sing for the product · "rate this out of 10" sip-then-score · hot-day first-sip from
  a real stranger · "trade me your coffee for this" · two strangers blind opinion → brand reveal

## Format 3 — Unboxing
- **Vibe:** premium reveal energy. Hands, packaging, the moment of discovery.
- **Preset:** `ugc_unboxing` · **Mode:** `"Unboxing"` · **Audio:** on (often ASMR-leaning)
- **No system hook** — the unboxing IS the hook
- **Concept seeds:** trio reveal in pastel paper · solo drop with slow ribbon-pull ·
  subscription box with brand note · premium gift-set unbox · hangtag macro series ·
  crate / "picked today" reveal

## Format 4 — Product Review
- **Vibe:** honest talking-head. Product in hand, ingredients read aloud, rankings, comparisons.
- **Preset:** `product_review` · **Mode:** `"Product Review"` · **Audio:** on
- **Recommended system hooks:** none / Camera Bump / Spicy / Product Crash / Product Hit
- **Concept seeds:** two-ingredient label test · fridge ranking "always [flavor], don't @ me" ·
  side-by-side vs generic competitor · "I tried this for 7 days" diary with empties ·
  beauty-editor mirror review (Bathroom + Spicy) · final variant ranking on camera

## Format 5 — ASMR
- **Vibe:** sound-led close-ups. No music, audible product handling, caption-only.
- **Preset:** `ugc` · **Mode:** `"UGC"` · `generate_audio: true`
- **Settings:** Kitchen / Bathroom / Bedroom only · **Hook:** none
- **Concept seeds:** macro cap-unscrew + glug pour over ice · condensation-bead slide then
  open · spoon-clink + ice-drop pour · bottle-on-marble tap-and-rotate · ribbon-pull /
  paper rustle (crossed with Unboxing) · two bottles clinking, no soundtrack

---

# GOLD-STANDARD IDEA CARDS (calibration examples)

These use a fictional brand ("Vola" sparkling yuzu water) purely to show the quality bar.
NEVER reuse Vola content for a real brand — match the STRUCTURE, specificity, and
VOC-traceability, with the real brand's own research data.

Notice what makes these good: the scene prompt is concrete and shootable in one take, the
hook line is traceable to a source, the VOC language is quoted (not paraphrased), and the
"why viral now" names a specific observed pattern — not "this format is popular."

## Example — Format 1 (UGC Entertainment)

```
7. **The Fridge Heist**
- Preset: ugc
- Model: marketing_studio_video
- Duration: 9 seconds
- Aspect ratio: 9:16
- Setting: Kitchen
- System hook: Camera Bump
- Audio: true
- Avatar/persona: mid-20s roommate type, hoodie, caught-in-the-act energy
- Scene prompt: Late-night kitchen, fridge door open casting light. Person freezes mid-reach
  with the last can of Vola, looks dead into camera, slowly closes the fridge while
  maintaining eye contact and backing out of frame.
- Hook line: "POV: you bought it but your roommate 'tried it once'" (source: Poppi comment
  section pattern — REPORTED)
- VOC language used: "my husband keeps stealing mine" — recurring phrase in Amazon reviews
- Social post caption: Buy two. Trust us. 🍋 #sparklingwater #roommatelife
- Inspired by: fridge-caught format trending across beverage TikTok (Step 2A, trend cluster 3)
- Why viral now: low-effort relatable theft-of-product bit is outperforming polished ads in
  beverage feeds this month; the freeze-frame eye contact is the retention device.
```

## Example — Format 2 (Street Interview)

```
12. **Trade You My Coffee**
- Preset: ugc
- Model: marketing_studio_video
- Duration: 12 seconds
- Aspect ratio: 9:16
- Setting: Street
- System hook: Interview
- Audio: true
- Avatar/persona: interviewer + late-20s commuter holding iced coffee
- Scene prompt: Busy sidewalk morning. Interviewer offers a chilled can of Vola in exchange
  for the stranger's iced coffee. Stranger hesitates, sips, eyebrows up, hands over the
  coffee without a word.
- Hook line: "I traded strangers their morning coffee for this" (source: Ghost Energy street
  series — VERIFIED, fetched TikTok page)
- VOC language used: "replaced my 3pm coffee and I don't miss it" — Reddit r/HydroHomies
- Social post caption: The coffee trade-in program is going well ☕→🍋
- Inspired by: Ghost Energy's barter-format series, 3 of their top 10 videos this quarter
- Why viral now: barter formats give a built-in mini-arc (offer → hesitation → verdict) in
  under 15s, and the stranger's unscripted face is the proof moment.
```

## Example — Format 3 (Unboxing)

```
18. **The Citrus Trio**
- Preset: ugc_unboxing
- Model: marketing_studio_video
- Duration: 10 seconds
- Aspect ratio: 9:16
- Setting: n/a
- System hook: none
- Audio: true
- Avatar/persona: hands-only, neutral manicure, soft daylight
- Scene prompt: Matte kraft box on a linen surface. Hands lift the lid, peel back pale
  yellow tissue paper to reveal three Vola cans (yuzu, grapefruit, lime) nestled in a row,
  then lift the yuzu can slowly toward camera.
- Hook line: "the prettiest thing my mailman has ever handed me" (source: own IG top Reel — VERIFIED)
- VOC language used: "the packaging alone is gift-worthy" — PDP review excerpt
- Social post caption: Summer trio just landed. Which one first? 🍊
- Inspired by: pastel-tissue trio reveals across premium beverage unboxings (Step 2A)
- Why viral now: save-and-send-to-a-friend behavior on gift-worthy packaging reveals; the
  slow tissue peel is the watch-time device.
```

## Example — Format 4 (Product Review)

```
23. **The Two-Ingredient Test**
- Preset: product_review
- Model: marketing_studio_video
- Duration: 13 seconds
- Aspect ratio: 9:16
- Setting: Kitchen
- System hook: none
- Audio: true
- Avatar/persona: early-30s skeptical reviewer, no-makeup look, direct to camera
- Scene prompt: Reviewer holds the Vola can at label height, reads the ingredient list out
  loud with a raised eyebrow, turns the can to camera, cracks it open and sips, gives one
  slow approving nod.
- Hook line: "I only buy drinks where I can read every ingredient" (source: Proven Hooks
  Library #4 — competitor Olipop, REPORTED)
- VOC language used: "finally something without the fake sweetener aftertaste" — Amazon,
  17 similar mentions
- Social post caption: Two ingredients. That's the whole list. 🧾
- Inspired by: label-read skeptic reviews outperforming enthusiastic reviews in this niche
- Why viral now: ingredient-transparency content is the dominant trust format in beverage
  right now; the eyebrow raise front-loads skepticism so the nod lands as a verdict.
```

## Example — Format 5 (ASMR)

```
29. **First Crack Over Ice**
- Preset: ugc
- Model: marketing_studio_video
- Duration: 8 seconds
- Aspect ratio: 9:16
- Setting: Kitchen
- System hook: none
- Audio: true
- Avatar/persona: hands-only
- Scene prompt: Macro shot. Chilled Vola can beaded with condensation on a stone counter.
  Fingers tap the lid twice, crack it open, slow pour over a glass of clear ice — audible
  fizz, ice shifting, no music, no voice.
- Hook line: none — the crack-and-pour audio is the hook
- VOC language used: "that first sip fizz is genuinely addictive" — PDP review
- Social post caption: Sound on. You know why. 🔊
- Inspired by: pour-audio loops with high save rates in beverage ASMR (Step 2A)
- Why viral now: sound-led loops replay 2–3x when the ending visually matches the start;
  the loop point here is the untouched glass returning to frame.
```
