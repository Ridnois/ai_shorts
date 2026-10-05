---
type: research
created: 2026-10-03
updated: 2026-10-04
status: v2 · English states and properties; the runner follows the idea-quality and illustration rules
tags: [research, youtube, pipeline, hub]
---

# 🏭 Video pipeline

← [[YouTube Channel]] · [[Workflow]] · [[Workflow]]

One **note per idea** in `Pipeline/Ideas/`; its `status` property is the table column. Changing `status` in the table is the command; the runner does the work and leaves the next status.

![[Pipeline table.base]]

## States

```
idea ──▶ build-script ──▶ building-script ──▶ script-ready
              ▲ you             ▲ runner            │ you review P1–P4a and P4
                                                    ▼
render-ready ◀── (editing, by hand) ◀── illustrations-ready ◀── generating-assets ◀── generate-assets
                                              ▲ runner                ▲ runner            ▲ you
                                                                              (requires an approved budget)
```

| Status | Set by | Meaning |
| --- | --- | --- |
| `idea` | you | Just the note; nothing happens |
| `build-script` | **you** (trigger) | Asks for research, script, direction, prompts and budget (stages 0–4, text only) |
| `building-script` | runner | In progress |
| `script-ready` | runner | Text and estimated budget ready. **You review P1–P4 here** |
| `generate-assets` | **you** (trigger) | Asks for voice and images. Only runs if `approved_budget_usd` > 0 |
| `generating-assets` | runner | Spending on Replicate |
| `illustrations-ready` | runner | Voice and images in `Media/`. **You review P6 here** |
| `render-ready` | you | Editing in Blender done ([[Playbook]]); P7 approved |
| `error` | runner | Something failed; the reason is in the *Error* column. Fix it and set the trigger again |

## How to use it (all from Obsidian)

The runner runs by itself as a user service (`youtube-pipeline.service`, checks the table every 15 s). There is no need to open a terminal.

1. In the table (**This week** view), **New** button: type the title. Within ≈ 15 s the note gets its properties. Fill in `publish` (date) and the topic in the body. **Write the idea in English.**
2. Change `status` to `build-script` → it becomes `building-script` → `script-ready`. Review.
3. If you approve the budget, write the figure in `approved_budget_usd` and set `generate-assets`.
4. Review plates and voice (`illustrations-ready`); edit; set `render-ready`.

Service: `systemctl --user status youtube-pipeline` · log: `journalctl --user -u youtube-pipeline -f` · stop: `systemctl --user stop youtube-pipeline`.

## Rules

- **The controller lives outside the vault**, in `~/Documents/youtube-pipeline` (its own repo). The vault only has notes and the table.
- **Nothing is spent without an approved budget** (master rule of [[Workflow]]). The hard cap is ×1.2 of `approved_budget_usd`.
- The script runner **cannot call Replicate** (it only reads and writes notes); the assets runner can.
- The cap is applied by instruction to the model and checked **afterwards** with `actual_cost_usd`; it is not a technical cutoff.
- An idea in `building-*` or `generating-*` (in progress) after a runner crash stays stuck: set the trigger again in the table.
- **Language:** scripts, research and descriptions are written in English ([[YouTube Channel]]).
