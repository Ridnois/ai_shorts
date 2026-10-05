---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v2 · redesigned from the first video's feedback; English since 3 Oct 2026
tags: [research, youtube, process, production]
---

# Video production process

← [[YouTube Channel]] · [[Narration guide]] · [[Illustration pipeline]] · [[Prompt - per-scene generation guide]] · [[Media convention]] · [[Feedback loop]]

> **Daily operation: [[Fast workflow]]** (review in 5 packages, fast models, image cap and a budget in dollars). This note stays as the reference for stages and gates.

> **Master rule:** no media (voice, image, sound, video) is generated until the user approves the prompts and the generation budget (gate 4). Everything before that is done as text, in the vault.

> **Language:** everything is written in English: research, script, narration, on-screen text, prompts, status notes and the video description ([[YouTube Channel]]).

It comes from the first video's feedback ([[Script - Magnets and geopolitics (38 seconds)]], section *Final user feedback*): the process was improvised on the fly and media was generated without defined steps or approvals. They are fixed here.

## The stages and their gates

Each stage ends in a **gate 🚦**: the user reviews and approves before moving to the next. A gate that is not approved sends the work back to its stage; a change in an approved stage reopens the later ones.

| # | Stage | What is produced (note in the vault) | Gate 🚦: the user approves |
| --- | --- | --- | --- |
| 0 | **Idea** | Topic, central question, for whom and why now, **plus the ranked angles and five hook candidates** ([[Idea and hook quality]]) | **P1** · the chosen angle, its alternatives and the hook |
| 1 | **Research** | **Facts bank (≥ 15 remarkable facts) and scoring table first**, then the claims sheet for the chosen facts: every figure with source and date; what is unverified is marked | **P2** · that the facts are remarkable and supported |
| 2 | **Script** | Narration per scene, written for the ear, per [[Narration guide]], **sized in words (130 to 190, aim 130 to 160), not in seconds**; theme line written, facts ≤ 5, cut test done, plain-words opener, concrete ending ([[Guidelines for new scripts]] §0.8 to 0.9, §1.10 to 1.11) | **P3** · the text, read aloud |
| 3 | **Direction: the visual plan** | One row per plate: **type** (stock photo, generated explainer, cutout, photo edit, number plate), **source**, the **usefulness sentence** ("this plate lets the viewer see ___ so they understand ___"), callouts and the card, per [[Illustration pipeline]] and [[On-screen text style]]; sound only if the script needs it, as a plan row with a free licensed source and credits ([[Guidelines for new scripts]] §3) | **P4a** · the visual plan |
| 4 | **Prompts, stock photos and budget** | Stock photos chosen and downloaded (free, credits logged), one content-first prompt per generated plate, voice prompts, `plan.json`, and the list of *predictions* with model and quantity ([[Prompt - per-scene generation guide]]) | **P4** · prompts and budget. **Generation can start from here** |
| 5 | **Tests** | Fixed references and a single scene of each category | **P5** · the look and the voice |
| 6 | **Generation** | The rest, by category (voice → image; sound only if the script requires it, taken from a free library), in small batches | **P6** · each category, separately |
| 7 | **Editing** | Cut in Blender ([[Blender editing]]) | **P7** · the cut |
| 8 | **Publishing** | Title, thumbnail, description with sources and AI disclosure | **P8** · before publishing |

## When a new video is requested

A short request ("a script about the power moves around helium") starts the process and **ends at gate P4**, not at the media:

1. Create the video's folder in `Videos/Week NN/` (the current week) with its `<Topic> - Status` note; a new week = a new `Videos/Week NN/` and `Media/Week NN/` pair.
2. Do stages 0 to 4 **as text only**: idea and question, research with sources and dates, script per [[Narration guide]], the visual plan per [[Illustration pipeline]], and the voice and image prompts, ready to paste, with the *predictions* budget per category.
3. Everything is marked as a **draft awaiting approval**; gates P1 to P4 are approved by the user, not by Claude.
4. Deliver a summary and **stop**. Replicate is not called, nothing is created in `Media/` and nothing is edited until the user approves P4 and asks for it.

## Gate rules

- **The user decides.** Claude proposes, measures and recommends; it does not approve on the user's behalf or advance a stage out of inertia.
- **Show before spending, in dollars.** At P4 the budget is delivered: how many *predictions* per category, with which model, **their price** (see [[Channel models]]) and an estimate of attempts. Input reference images are also charged.
- **A cap per category.** If the real cost exceeds the budget, say so and ask for approval before continuing.
- **Retries with judgement.** Fix the prompt before retrying and review every result before launching the next batch; requests go in series.
- **Small batches.** First the minimum that tests the idea (P5); the rest only afterwards. An image or voice that failed the test is not replicated ×40.
- **What is not generated without a gate:** no file in `Media/`, no Replicate call. Exceptions are requested explicitly.
- **Every approval is written down** in the video's status note (date and what was approved), so the process can be resumed without context.
- **Discards are not deleted** until P8; they live in `_descartes/` ([[Media convention]]).

## Where everything lives

```
(vault root)  ← text, versioned in git
├── YouTube Channel.md               channel index
├── System/                          rules that apply to every video
└── Videos/
    ├── Week NN/<Topic>/             one folder per video, grouped by publishing week (Week 01 = the first video under the process)
    │   ├── <Topic> - Status.md      current stage and approvals log
    │   ├── Research - <Topic>.md
    │   ├── Scripts/                 script versions
    │   └── Upload - <Topic>.md      the upload package (title, description, hashtags, thumbnail, checklist)
    └── Legacy/<Topic>/              everything made before Week 01 (kept as a record)

Media/              ← media, only on this machine (ignored by git)
├── _canal/                          shared: style, references, music, brand drafts
├── Week NN/<Video>/                 voice · plates · stock · render (the same week as the note in Videos/)
└── Legacy/<Video> - <N seconds>/    older videos, with their Spanish inner names
```

## Status template per video

Each video has a `<Topic> - Status` note with this table, updated at every gate:

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ⏳ / ✅ | date | chosen angle + 5 hooks + ranked alternatives |
| 1 Research | | | |
| 2 Script | | | |
| 3 Visual plan | | | |
| 4 Prompts, stock photos and budget | | | |
| 5 Tests | | | |
| 6 Generation | | | per category |
| 7 Editing | | | |
| 8 Publishing | | | |
