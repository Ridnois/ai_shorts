# Guide for the agent working in this vault

This vault (`~/Documents/youtube`) is the **single source of knowledge** of an English-language, AI-assisted explainer channel (vertical Shorts today). You do not rely on memory of past chats: you read the notes, you follow them, and when the user gives feedback you **change the notes** so the next run does it right by default. Everything in the vault is written in **English**.

## 1. Read order (every task)

1. `YouTube Channel.md`: the index and the list of videos.
2. `System/Guidelines for new scripts.md`: every quality rule, compressed (idea → script → illustrations → text → voice → editing → process). **Read it whole before writing anything.**
3. `System/Process/Fast workflow.md`: how a video is produced (packages, models, prices, budget).
4. For a new video also: `System/Content/Shorts quality bar.md` (the bar every Short must clear), `System/Content/Idea and hook quality.md`, `System/Visual/Illustration pipeline.md`, `System/Content/Narration guide.md`, `System/Content/Channel identity.md`, `System/Visual/On-screen text style.md`.
5. On demand: `System/Content/Channel strategy.md` (monetization, policies, multi-platform plan), `System/Content/Channel playbook.md` (engagement, on-screen design system, brand and mission), `System/Process/Production process.md` (stages and gates), `System/Process/Media convention.md`, `System/Process/YouTube upload.md` (when uploading), `System/Editing/Blender editing.md`, `System/Content/Channel voice.md`, `System/Models/Channel models.md`, and the video's `<Topic> - Status` note.

## 2. Hard rules (never skip)

- **No media is generated before gate P4** (prompts and budget approved, in dollars). If the user delegates ("follow all the steps until the render"), record it in the Status note and continue **within the cap**; stop at the render (P7). Replicate calls go **in series**, one retry per image, and the prediction id is logged at once.
- **The idea is a gate:** facts bank of ≥ 15 remarkable facts, scoring, street-lamp and expert tests, five hooks. **Length is planned in words** (130 to 190 for a Short, aim 130 to 160), never in seconds.
- **Every plate passes the usefulness test** and sits in a **visual plan** (stock photo, generated explainer, cutout, photo edit, number plate). Stock photos are free and credited; generated plates are **content-first prompts** with references and **no custom style**; style is applied in Blender.
- **The first 3 seconds are a need-to-know claim in plain words** (≤ 10 words, no jargon, no story opener); **one theme line that every scene bridges back to, ≤ 5 facts, a concrete ending**; **a new image every ≈ 3 to 4 s (none over 5 s, 16 to 20 plates)**; **no branding inside the video** (no progress bar, mark or series tag); the script **explains, it does not narrate**; **explainers are scientifically faithful schematics** (nothing invented); **no number card or callout on a bare gradient**; **every video has word-by-word captions** (`System/Content/Shorts quality bar.md`).
- **Text and added content** pass the specificity test ([[Channel identity]] voice): callouts name parts, a number card carries the figure, margin notes give a voice, context cards cite a source. No generic labels.
- **Sound:** the builder synthesizes the channel's sound design by default (`sound` in `plan.json`, user request 4 Oct 2026); any recording or music track is opt-in from a free licensed library with credits and approval; no ML-generated sound; BigSoundBank and Freesound are deferred (`System/Guidelines for new scripts.md` §3).
- **Rigor:** every figure has a source and a date; weak facts are attributed or left out; the research note says what was not verified.
- **Be honest about what you could not check** (you cannot hear audio or watch a whole video): say it, and leave P7 to the user.
- **Notes live in the vault** (Markdown, Obsidian), never as artifacts or documents elsewhere. Keep them short; **delete obsolete notes** instead of archiving (git keeps history); keep one note per video for the status.
- **Money:** show a dollar budget with a cap (base × 1.2) before spending; going over the cap needs approval; model research is not video cost.

## 3. Feedback protocol (the vault must always get better)

When the user gives feedback (after a render, or about the process), follow **`System/Process/Feedback loop.md`**: record it verbatim, classify it by layer, **apply it to every layer** (rule notes, checklists, templates, scripts, `plan.json`, runner prompts, index), retire what it replaces, add an invariant to `System/scripts/check_vault.py`, run the check, then answer with a short table of *what changed where* and what remains unverified. **You are not done until `python3 System/scripts/check_vault.py` passes and the vault agrees with itself.** Update your own memory with a one-line pointer to the note that now holds the lesson.

## 4. Tooling, in one place

| Need | Use |
| --- | --- |
| Stock photos (free, credited) | `python3 System/scripts/stock_photos.py search "<query>" --source openverse\|nasa\|commons` and `get …` |
| Replicate calls | `System/scripts/replicate_helper.py` (`run`, `download` with retries, `recover(id, dest)`) with `REPLICATE_API_TOKEN` from `.env` |
| Sound or music (opt-in, free licensed libraries, credited; BigSoundBank and Freesound deferred) | `System/Guidelines for new scripts.md` §3, manual download with the license recorded in `Media/Week NN/<Video>/sound/_credits.jsonl` |
| Word timings for the captions | `python3 System/scripts/word_timings.py "Media/Week NN/<Video>"` (needs `REPLICATE_API_TOKEN`; the builder estimates if skipped) |
| Assemble and render | `VIDEO="Media/Week NN/<Video>" SOLO_PROYECTO=1 CHECK=1 blender -b --factory-startup --python System/scripts/build_video.py`, then without `SOLO_PROYECTO` in the background |
| Upload to YouTube (API, private by default; one-time setup by the user) | `python3 System/scripts/youtube_upload.py upload …`; guide `System/Process/YouTube upload.md` (confirm title, description, thumbnail and visibility with the user first) |
| Pipeline runner | `~/Documents/youtube-pipeline/pipeline.py` (a user service; its prompts follow these notes) |
| Vault coherence | `python3 System/scripts/check_vault.py` |

**Gotchas that already cost time:** Replicate answers HTTP 429 under bursts (the helper now waits and retries; nothing is charged); the Wikimedia thumbnail API throttles (fetch originals from `upload.wikimedia.org` directly); the system Python has no `numpy` (Blender's does); `.blend` files need absolute paths; Blender's background mixdown is silent (the builder checks the strips instead); Obsidian re-pads Markdown tables on save (parse tolerantly); never `pkill -f` a pattern that appears in your own command; if a download hangs, recover the prediction, never regenerate.

## 5. Where things live

```
YouTube Channel.md            index · videos table
System/Guidelines…            all rules, compressed          System/Process/   workflow · process · media · feedback loop
System/Content/               idea quality · identity · narration · voice · Shorts quality bar · channel strategy · channel playbook · quality guide
System/Visual/                illustration pipeline · prompts · on-screen text
System/Editing/               Blender editing · transitions   System/Models/    models and prices
System/scripts/               build_video.py · stock_photos.py · replicate_helper.py · check_vault.py · legacy build_*.py
Pipeline/                     idea queue, template and table   Research/         general model research
Videos/Week NN/<Topic>/       Status · Research · Scripts · feedback · Upload (a Week NN is a calendar week, Mon to Sun; Week 01 = 5 to 11 Oct 2026; Videos/Legacy/ holds everything made before it)
Media/Week NN/<Video>/        generated media, same week as the note (local, gitignored); Media/Legacy/, Media/_canal/ (shared, brand)
```
