# Stage 3 — Generate in Higgsfield Marketing Studio

> Send the Stage 3 banner first. Re-read the state file AND the plan JSON — every
> generation call is driven by plan rows and state-file UUIDs, never by memory.
> Read `references/capability.md` for the mode mapping before the first call.

⚠️ Ask permission before EACH format batch. Never auto-run the full plan.

**Stage outputs:** rendered videos, the image asset pack, an updated Brand Pack, and
per-row `status` updates written back to the plan JSON as batches complete.

## Step 1 — Register the product (internal, silent)

`media_upload` → curl PUT → `media_confirm` → write `higgsfield.product_uuid` to the state
file. Pass as reference image in ALL generations. User sees at most "Getting your product
ready…" — never tool names.

## Step 2 — Resolve picklist UUIDs (internal, silent)

For each UGC-family plan row, resolve `system_hook` and `setting` names → UUIDs using the
lists in the state file (probed in Stage 1). If a name is missing from the state file's
picklists, re-probe live, update the state file, and if still missing, set it to none and
flag the row — never guess a UUID.

## Step 2a — Preset avatars (REQUIRED on every video)

⚠️ Never leave `avatars: []` empty — Higgsfield casts a fresh random face per render,
killing campaign consistency.

1. `show_marketing_studio(action='list', type='avatar', size=100)` → cache to state file
   with demographic descriptors. Filter to `source: "preset"` (user-trained Souls only on
   explicit opt-in).
2. Assign by format: UGC Entertainment → energetic Gen-Z casual · Street Interview →
   interviewer + stranger (rotate 2 per scene) · Unboxing → hands-only or lifestyle ·
   Product Review → authentic mid-20s–30s reviewer · ASMR → hands-only preferred.
3. Rotate 2–4 avatars within each batch so one face doesn't front all 20 videos.
4. Pass as `avatars: [{ id: "<uuid>", type: "preset" }]`.

If no preset avatars exist for this account, fall back to empty AND warn once: "Heads up —
no preset avatars found for your account. Faces in this batch will vary per video."

## Step 3 — Per-batch permission gates

Process format buckets in order: 1 UGC Entertainment → 2 Street Interview → 3 Unboxing →
4 Product Review → 5 ASMR. Before each batch, AskUserQuestion:

> "Ready to generate the **[N] [format name]** videos? ([resolution], 9:16, audio [on/off])"
> - "Yes — generate all [N]"
> - "Start with 3 for a quality check first (Recommended)"
> - "Skip this batch for now"
> - "Change settings before generating"

Only on click, call `generate_video` for the batch. After each batch: `job_display` the
results, mark rows `done` in the plan JSON, update `progress.stage_3` in the state file,
then auto-prompt: "Generate next batch" / "Re-do this one" / "Pause here".

**Quality-check path:** if the user picks "Start with 3", generate 3, display, then ask
"Continue with the remaining [N-3]?" / "Adjust the prompt style first" / "Skip the rest".

## Step 3a — `mode` on every call (internal — the mapping lives in capability.md)

Always pass the title-case `mode` (e.g. `mode: "Hyper Motion"`, `mode: "Product Review"`).
Omitting it silently rewrites everything as UGC — the most common failure of this pipeline.

## Step 4 — Prompt construction (NO on-screen text, EVER)

⚠️ The plan's `caption` field is social-post metadata. It must NEVER appear in a generation
prompt as overlay text.

```
[scene_prompt from plan row].
Product: [product name], [key visual detail — color, packaging, label].
Style cues: [preset-specific — "authentic, handheld feel, natural daylight" for UGC;
"intimate ASMR close-up, no music, audible product handling" for ASMR;
"polished cinematic, golden hour" for TV Spot].
Negative: no text overlay, no captions, no subtitles, no on-screen text, no watermarks,
no lower-third, no graphic typography, no brand callout banners. Clean image only.
```

UGC family: also pass `hook_id`, `setting_id`, and a preset avatar.

## Step 5 — Image asset pack (after all video batches)

Count and breakdown come from `allocate.py` (image pack total = floor(videos/5); split 40%
social / 20% hero / 20% with-people / 20% without-people, remainder → without-people).
Fallback table: 50→10 (4/2/2/2) · 100→20 (8/4/4/4) · 150→30 (12/6/6/6) · 200→40 (16/8/8/8).

Single gate: "Videos done. Ready to generate the image asset pack — [N] images?"
- "Yes — generate all [N] (Recommended)" / "Yes — skip with-people shots" /
  "Yes — skip without-people shots" / "Skip image pack entirely"

Generate via `generate_image`, `model: "gpt_image_2"`, product UUID in `medias[]` role
`image`, `quality: "high"`, `resolution: "2k"`:
1. **Social posts** — 1:1, lifestyle stills derived from the most-shareable video scenes
2. **Hero banners** — 16:9: studio-clean, lifestyle, moody low-light, spread evenly
3. **With-people** — diverse demographics, hands holding, using, sharing
4. **Without-people** — product on wood / stone / brand-color background, no humans

Save to `outputs/[brand]-asset-pack/` with descriptive names
(`social-01-lifestyle-kitchen.png`, `hero-02-lifestyle.png`, …).

Final gate: "All set — proceed to Stage 4 (Publish)" / "Re-do specific assets" / "Pause here".

## Step 6 — Refresh the Brand Pack (always, before leaving Stage 3)

Write/update `[brand]-brand-pack.md`: brand context, the current Proven Hooks Library with
evidence labels, VOC summary, what was generated this campaign (counts per format), and any
user preferences observed. Tell the user: "Save this Brand Pack — upload it next campaign
and onboarding takes one click."

## Standalone image-pack mode

Trigger phrases: "generate the image pack", "just the static visuals", "image assets only".
Bypass Stages 1–2 and video batches:
1. Product registered? Use cached UUID from state file if present; else register from the
   attached image (`show_marketing_studio(action='create', type='product', medias=[…])`) or
   URL (`action='fetch'`); if neither, ask once for an image or URL.
2. Auto-detect product details silently (Stage 1 Step 1 routine).
3. One AskUserQuestion for pack size: "10 (Light)" / "20 (Recommended)" / "30" / "40".
4. Same generation, breakdown, and filenames as Step 5. End after showing files.

## Failure handling

If `generate_video` fails (rate limit, MCP error): write the row IDs to
`progress.failed_rows` in the state file and offer "Retry failed rows" / "Skip them" /
"Pause". Never silently skip.
