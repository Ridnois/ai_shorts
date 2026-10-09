# Agent guide: Redtail Shorts vault (`~/Documents/youtube`)

English-language, AI-assisted technology-explainer channel (IT, engineering, human progress, resources, programming, civil engineering): vertical Shorts for YouTube and TikTok, five a week at a fixed time, never two on one day. The vault is the single source of knowledge: you do not rely on past chats, you read the notes and follow them; **feedback becomes an edit of the owning note** ([[Feedback loop]]). Everything is written in English.

## Read order (every task)

1. This file. 2. `System/Playbook.md` (every content rule; read it whole before writing). 3. `System/Workflow.md` (stages, gates, budget, models, files, commands). 4. `Analytics/Report.md` before choosing an idea, hook or length. 5. The video's `<Topic> - Status` and script (`Videos/Week NN/<Topic>/`).
On demand: `System/Audience.md` (niche, deep-first search, package, opening) when choosing an idea and writing the script's Package; `System/Style.md` (on-screen text, design tokens, brand, persona) when writing text or cards; `System/Publish.md` at P8 and for metrics; `Pipeline/Pipeline.md` for the idea queue.

## Hard rules

- **No media before P4** (prompts and budget approved, in dollars). If the user delegates, record it in Status and continue within the cap (base × 1.2); **stop at the render (P7)**. Replicate calls in series, one retry per image, prediction id logged at once.
- **The idea is a gate** (Y outcome and X mechanism named, deep-first search done, [[Audience]]): facts bank ≥ 15, scores, street-lamp and expert tests ("borderline" = fail), a demand check, five hooks of different types. **Length is planned in words** (130 to 190, aim 130 to 160; every third video a compact 80 to 115).
- **First 2 seconds = a need-to-know claim (the twist is the first words, no preamble) a stranger understands at once (plain, a reason to care, opens a question the next scene answers; judged by the hook test, never by word count; no story opener);** one theme line every scene bridges back to, ≤ 5 facts, concrete ending; explain, do not narrate.
- **Every visual shows the verb, not the noun** (usefulness and swap tests, [[Playbook]] §3): footage of real things doing it, animated schematics (`motion.py`) for hidden processes, numbers as comparisons that build; plates cut on the word (`at`), a visual event every 2 to 3 s (nothing unchanged over 3.5 s, a still ≤ 4 s), ≥ 60 % of the runtime moving, 3 to 5 visual worlds with one anchor that returns; ≤ 3 generated media (no custom style; AI video only as gentle motion on a real photo, disclosed); schematics are scientifically faithful; no card or callout on a bare gradient.
- **Word-by-word captions on every video; no branding inside the video.** Text passes the specificity test.
- **Package at the script phase:** title, thumbnail and promise are written in the Script note and scene 1 pays the promise (promise, proof, plan).
- **Voice:** `elevenlabs/turbo-v2.5`, per scene with `previous_text` and `next_text`.
- **Sound:** synthesized by the builder by default; any recording or music is opt-in, licensed, credited, approved.
- **Publish:** upload private by default and only after the user confirms title, description, thumbnail, visibility; **P8 is `python3 System/scripts/publish.py <publish.json>`** ([[Publish]]); pasteable text in plain ASCII ```` ```text ```` blocks; **every video has `upload/<prefix>-publish-pack.md` (thumbnail, title, description, pinned comment, TikTok caption in text blocks) before the user is asked to approve** ([[Publish]]); fill `Analytics/videos.csv` at P8; pull numbers at about 24 h, 7 d, 28 d; under about 100 views read counts only.
- **Rigor and honesty:** every figure has source and date; say what you could not check (you cannot hear audio or watch a whole video); P7 is the user's.
- **Notes live in the vault** (Markdown), never as artifacts or docs elsewhere; keep them short (size ceilings per note type in [[Workflow]], enforced by `check_vault.py`); delete obsolete notes instead of archiving; one Status note per video.
- **Done = `python3 System/scripts/check_vault.py` passes.**

## Gotchas that already cost time

Replicate 429 under bursts (the helper retries, nothing is charged); Wikimedia thumbnails throttle (fetch originals from `upload.wikimedia.org`); system Python has no numpy (Blender's does); `.blend` needs absolute paths; Blender background mixdown is silent; Obsidian re-pads tables; never `pkill -f` a pattern in your own command; a hung download is recovered, never regenerated; `Media/` is local and gitignored; motion plates need the `SOLO_PROYECTO=1` build first (it writes `render/_timeline.json`); clips must be at the plan's 24 fps (`stock_videos.py cut` does it); you cannot watch a clip, so look at `look` and `--sheet` frames.

## Map

```
CLAUDE.md · YouTube Channel.md (index, video table)
System/  Playbook · Workflow · Style · Publish · Feedback loop · Brand/Redtail (logo, banner) · scripts/ (youtube_search, build_video, motion, stock_photos, stock_videos, replicate_helper, word_timings, youtube_upload, youtube_analytics, analytics, make_thumbnail, check_vault)
Pipeline/ idea queue (runner: ~/Documents/youtube-pipeline/pipeline.py)    Analytics/ csvs · Report.md (generated) · Reports/
Videos/Week NN/<YYYY-MM-DD Day>/<Topic>/ Status · Script · Upload      Media/Week NN/<YYYY-MM-DD Day>/<Video>/ local media
```
