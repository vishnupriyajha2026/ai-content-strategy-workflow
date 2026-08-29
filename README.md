# AI Content Strategy Workflow

An AI workflow that turns a brand or product brief into research, customer insights, campaign ideas, a production plan, and an execution-ready content calendar.

It guides an AI agent through five connected stages:

1. Research the category, customer language, competitors, and proven hooks
2. Build a dated video plan with a consistent mix of formats
3. Generate videos and image assets in controlled batches when a compatible creative tool is connected
4. Prepare or schedule publishing
5. Compare generation spend with a transparent traditional-production estimate

The workflow is brand-agnostic. Brand names, products, competitors, campaign files, and generated media stay outside the reusable workflow and are created only during a user's own run.

## Why this exists

Generating one AI video is easy. Keeping 50 or 100 outputs consistent is harder. Research disappears from long chats, prompts drift, faces change, ideas repeat, and unsupported trend claims creep in.

The workflow uses files as campaign memory, adds approval gates before paid generation or publishing, and requires every idea to pass a quality rubric before it reaches the plan.

## What is included

```text
ai-content-strategy-workflow/
|-- SKILL.md
|-- references/
|   |-- capability.md
|   |-- formats.md
|   |-- rubric.md
|   |-- stage-1-research.md
|   |-- stage-2-plan.md
|   |-- stage-3-generate.md
|   |-- stage-4-publish.md
|   `-- stage-5-report.md
|-- scripts/
|   `-- allocate.py
`-- tests/
    `-- test_allocate.py
```

`allocate.py` handles format splits, posting dates, and image-pack counts deterministically so the agent does not improvise campaign math.

## Requirements

- Claude Code or another tool that supports the Agent Skills format
- Python 3.9 or newer
- Optional: a connected Higgsfield account for asset generation
- Optional: an active Higgsfield plan and enough credits for the batches you approve
- Optional publishing connections if you want the workflow to schedule content

Research and planning can still run without generating paid assets.

## Install

Clone or download this repository, then copy the folder into your personal Claude Code skills directory:

```bash
mkdir -p ~/.claude/skills
cp -R ai-content-strategy-workflow ~/.claude/skills/ai-content-strategy-workflow
```

Claude Code discovers reusable workflows from `~/.claude/skills/<name>/SKILL.md`. You can also place it inside a project at `.claude/skills/ai-content-strategy-workflow/`.

## Use

Start Claude Code and ask for a campaign in plain language:

```text
Use the AI Content Strategy Workflow to build a 50-video campaign for this product.
```

Attach a product image or share the product-page URL. The workflow will collect the brand context it cannot safely infer, then begin with research. It pauses before each paid generation batch and before any publishing action.

You can also start from a later stage if you already have a research brief, content plan, or finished assets.

## Privacy and safety

- Do not commit campaign state files, product images, generated media, API keys, customer data, or unpublished brand research.
- The included `.gitignore` excludes the normal campaign-output paths and common credential files.
- Treat publishing and paid generation as approval-gated actions.
- Only use faces, product assets, and brand materials you own or have permission to use.

## Validation

Run the local planning tests:

```bash
python3 -m unittest discover -s tests -v
```

The deterministic allocation helper is tested locally. Higgsfield generation, spend reporting, and publishing depend on the live tools and account connections available in your environment, so verify those integrations with a small three-asset quality-check batch before scaling.

## Important limitation

Higgsfield's available models, templates, modes, limits, and command schemas can change. The workflow requires live capability discovery before generation, and live values take precedence over the reference snapshot in `references/capability.md`.

## License

MIT
