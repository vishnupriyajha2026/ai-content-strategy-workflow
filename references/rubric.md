# Quality Rubric — every idea card passes this before the user sees it

This is the pipeline's quality gate. Score SILENTLY. The user never sees scores, failed
drafts, or the regeneration loop — only ideas that survived. If asked how ideas were
selected, then explain.

## When to apply

1. **Stage 1, Step 4** — score every seed idea before it enters the Viral Content Brief.
2. **Stage 2** — score every plan row that introduces a NEW concept (rows reusing an
   approved brief idea inherit its score).
3. **Stage 3** — before firing each batch, spot-check the batch's scene prompts against
   criteria 3 and 5 only (producibility + prompt quality), since concepts were already gated.

## The 6 criteria (score each 1–5)

**1. Hook strength** — Does the first visual/verbal beat interrupt a scroll?
- 5: names a specific tension or pattern-break in the first beat (an unexpected offer, a
  freeze, a skeptical read)
- 3: competent but generic opening ("person holds product, smiles")
- 1: no identifiable hook; the video starts with the product pitch

**2. VOC traceability** — Does the idea use real customer language from the dossier?
- 5: quotes an exact phrase from reviews/Reddit, and the phrase drives the concept
- 3: paraphrases a real pain point
- 1: generic marketing language with no dossier source ("refreshing and delicious")

**3. Producibility** — Can Marketing Studio actually render this?
- 5: single take, one setting, ≤15s, picklist-legal hook/setting, correct preset routing
- 3: renderable but strained (crowded scene, precise-timing gag, complex hand choreography)
- 1: violates a hard limit (lip-sync dialogue, split-screen, >15s, off-picklist) — AUTO-FAIL

**4. Brand fit** — Does it match the positioning and palette in the state file?
- 5: tone, setting, and persona all consistent with the brand's register
- 3: neutral; wouldn't embarrass the brand but wasn't built for it
- 1: clashes with positioning (slapstick dare for a premium sleep brand)

**5. Concept distinctness** — Is it different from every other idea in the same format?
- 5: unique concept seed AND unique retention device within its format
- 3: same seed as another idea but meaningfully different execution
- 1: near-duplicate of another card — AUTO-FAIL (regenerate from an unused seed)

**6. Evidence honesty** — Are the "source" and "why viral now" claims properly labeled?
- 5: cites a VERIFIED or REPORTED source from the dossier by name
- 3: INFERRED and labeled as such
- 1: asserts a trend or competitor attribution that appears nowhere in the dossier — AUTO-FAIL

## Pass / fail

- **Pass:** total ≥ 22 of 30, AND no criterion at 1.
- **Fail → regenerate:** rewrite the idea targeting its lowest criterion. Maximum 2
  regeneration attempts per idea; if still failing, discard and draw a fresh concept seed.
- **Batch floor:** if more than a third of a format's ideas fail on VOC traceability
  (criterion 2), the problem is the dossier, not the ideas — go back and deepen the VOC
  extraction for that pain point before regenerating.

## Reporting

After gating, include ONE line in the brief's methodology footer:
"Every idea passed a 6-point quality screen (hook, customer-language fit, producibility,
brand fit, distinctness, source honesty) before making this brief."
