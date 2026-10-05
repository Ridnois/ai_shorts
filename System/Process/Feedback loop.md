---
type: research
created: 2026-10-04
updated: 2026-10-04
status: v1 · from the Twisted carbon feedback on vault management (4 Oct 2026)
tags: [research, youtube, process, feedback, vault]
---

# Feedback loop

← [[YouTube Channel]] · [[Production process]] · [[Guidelines for new scripts]]

> **The user's requirement (4 Oct 2026):** *"All suggestions and requirements always end in improvements to the knowledge in this vault. Our focus is to edit the content based on my feedback; you can show me what you changed, but see the whole vault as a single source of knowledge and keep it coherent with the general ideas and feedback across all documents. Make sure the agent that works on this vault gets their guide."*

**Feedback is not finished when the chat answer is sent. It is finished when the vault says it, on every layer, and still agrees with itself.**

## 1. Procedure (every time the user gives feedback, on a video or on the process)

1. **Record it verbatim** (the user fills [[Post-render feedback template]], copied to the video's folder when a render is ready; free text is fine) in the video's feedback note (`Videos/<Topic>/Scripts/Post-render feedback - <Topic>.md`), or in a dated quote if it is about the process. The user's words stay; they are the evidence.
2. **Classify each point by layer** (table below) and list the notes it touches.
3. **Apply it on every layer**, not only one: the rule note, the checklists, the templates, the tooling (scripts, `plan.json`, the pipeline runner prompts), the index and the agent guide. A rule that exists in one note and contradicts another is a defect.
4. **Retire what it replaces:** delete obsolete notes (git keeps the history; do not archive), redirect links, and note the supersession in the surviving note (e.g. [[Illustration pipeline]] §8).
5. **Run the check:** `python3 System/scripts/check_vault.py` must report no problems (broken links, missing front matter, notes missing from the index, encoded-feedback invariants, scripts that compile).
6. **Answer briefly:** a table of *what changed where*, appended as a **Response** section to the feedback note and shown to the user; plus what was **not** verified or not done.
7. **Update the agent's memory** with the lesson in one line, pointing at the note that now holds it.

## 2. Where each kind of feedback goes

| The feedback is about… | It lands in… |
| --- | --- |
| The idea, the facts, the hook | [[Idea and hook quality]], [[Guidelines for new scripts]] §0, [[Narration guide]], the idea template, the runner prompt |
| Script structure, length, rigor | [[Narration guide]], [[Guidelines for new scripts]] §1 |
| Illustrations, prompts, stock photos | [[Illustration pipeline]], [[Prompt - per-scene generation guide]], [[Guidelines for new scripts]] §2, [[Fast workflow]] §3 to §7, [[Channel models]] |
| On-screen text and added content, personality | [[On-screen text style]], [[Channel identity]], [[Guidelines for new scripts]] (T rules) |
| Voice, audio, editing, technical defects | [[Blender editing]], `System/scripts/build_video.py`, [[Guidelines for new scripts]] §3 and §4, [[Channel voice]] |
| Gates, costs, delegation | [[Production process]], [[Fast workflow]], [[Guidelines for new scripts]] §5 |
| **Data from the channel** (retention, viewed vs swiped away, shares, subscribers) | [[Analytics]] (record), then the layer of the cause: hook → [[Idea and hook quality]] and [[Narration guide]]; pace and length → [[Guidelines for new scripts]]; visuals → [[Illustration pipeline]] |
| How the agent should work | `CLAUDE.md` (vault root), this note |

## 3. Conflicts and supersession

- **The newest explicit feedback wins**, and the older rule is edited or deleted in the same pass, never left beside it.
- If two instructions truly conflict, say so to the user and propose which one to keep; do not silently pick.
- Decisions that replaced an earlier one (so nobody re-introduces them):

| Date | Replaced | By | Where |
| --- | --- | --- | --- |
| 3 Oct 2026 | Spanish as the working language | English everywhere | [[YouTube Channel]] |
| 4 Oct 2026 | Time ranges for script length | Word ranges (130 to 190 for a Short) | [[Guidelines for new scripts]] |
| 4 Oct 2026 | Plasticine miniatures via Kontext + one reference per plate | Visual plan with stock photos, generated explainers and cutouts, no custom style | [[Illustration pipeline]] |
| 4 Oct 2026 | Generic label/title/detail cards on every plate | Callouts, number cards, margin notes and specific context cards | [[On-screen text style]] |
| 4 Oct 2026 | One builder script per video | `build_video.py` + `plan.json`, padded and checked voices | [[Blender editing]] |
| 4 Oct 2026 | A scene-setting, story-style hook of 12 to 20 words | A need-to-know claim of ≤ 10 words inside 3 s; explain, do not narrate | [[Narration guide]], [[Shorts quality bar]] |
| 4 Oct 2026 | Creative explainers and number cards on bare gradients | Scientifically faithful schematics; cards only on real photos or explainers | [[Illustration pipeline]] |
| 4 Oct 2026 | Generated sound effects (`audiogen`, 16 kHz) as the only sound route | Opt-in sound from free licensed libraries, credited; BigSoundBank and Freesound deferred | [[Guidelines for new scripts]] §3 |
| 4 Oct 2026 | Cards and callouts only | Cards, callouts and word-by-word captions on every video | [[Blender editing]], [[On-screen text style]] |
| 4 Oct 2026 | Sound off by default (and, in a parallel edit the same day, opt-in from licensed libraries only) | The builder's synthesized sound design on by default; recordings and music stay opt-in and licensed | [[Guidelines for new scripts]] §3, [[Blender editing]] |
| 4 Oct 2026 | In-video branding (progress bar, ring-and-dot mark, series tag) | **None inside the video**; the brand lives on the channel page and in the recurring look of cards and captions | [[Channel playbook]] §3.4 and §4, [[Blender editing]] |
| 4 Oct 2026 | A scene-setting list of facts that "explains" | One theme line, bridges, ≤ 5 facts, a concrete payoff ending, a cut test | [[Guidelines for new scripts]] §0.8 to 0.9, §1.10 to 1.12, [[Narration guide]] |
| 4 Oct 2026 | One image every 4 to 6 s (12 to 14 plates) | One image every 3 to 4 s (16 to 20 plates), half real photos, 2 to 3 candidates per scene | [[Illustration pipeline]], [[Shorts quality bar]] §4 |
| 4 Oct 2026 | Captions at 104 px | 88 px | [[On-screen text style]] |
| 4 Oct 2026 | A proposed channel name and avatar "to decide" | **Cutaway**, "How it works. With sources.", the ring-and-dot avatar | [[Channel playbook]] §4 |
| 4 Oct 2026 | *"redesign for the brand, add an animal into it and science as the topic"* | copper fox mascot, tagline "Science, cut open. With sources.", science-wide audience | [[Channel playbook]] §4 |
| 5 Oct 2026 | Positioning and slogans around "science media with sources" (*"Dont focus on 'science media with sources' make it more like 'science entertainment'"*) | **Science entertainment** as the brand promise; sourcing stays a rigor rule in descriptions; slogans like "Follow the tail.", "Science at full speed.", "Science with teeth." | [[Channel playbook]] §4, [[Brand options]] |
| 5 Oct 2026 | Names, logos and banners explored in one session (*"Redtail it is"*, *"Banner b is the winner"*) | Name **Redtail**, NFL-style fox logo, slogan **"Science at full speed."**, banner B; the rest archived as text | [[Brand options]], [[Channel playbook]] §4 |
| 5 Oct 2026 | Videos in one flat list; no upload step (*"Its perfect, now i want it to prepare for upload… organize the videos by week, this one is week 1 and the rest is legacy… description, hashtags, and thumbnail… research how to build all of this in order to be captivating and improve metrics"*) | **Week NN / Legacy** folders in `Videos/` and `Media/`; an **Upload note** per video (title options, description, hashtags, thumbnail, checklist, metrics table); thumbnails are allowed on Shorts (YouTube, 24 July 2026) | [[Media convention]], [[Guidelines for new scripts]] §5, [[Fast workflow]] §4, [[Upload - Battery and lithium]] |
| 5 Oct 2026 | Captions at 16.5 % from the bottom, under the Shorts interface; a generated-image default of ≈ $0.05 with ≤ 5 plates (*"the youtube shorts ui overlaps the captions, redesign the layout of the videos captions should go more on the center… given that we are using less generated images and more stock, you can use a very good model"*) | **Captions centred (50 % of the height), cards at 66 %, callout labels above the captions**; **`gpt-image-2` for the ≤ 3 generated plates** (stock first); the copper video in Week 01 (a week is a calendar week: user, 5 Oct 2026, *"Why copper and ai race should be week 2? it was made today, which is week one"*) | [[On-screen text style]], [[Shorts quality bar]] §3, [[Channel playbook]] §3.3, [[Fast workflow]] §3, [[Channel models]] |

## 4. The coherence check

`System/scripts/check_vault.py` guards the vault: it fails on broken wikilinks, notes without front matter, System notes missing from the [[YouTube Channel]] index, scripts that do not compile, and **missing encoded feedback** (a list of phrases that must stay in the notes that carry each rule, so a later edit cannot silently drop a rule) and **missing guards in the builder** (code that enforces a rule, such as refusing bare backdrops). When feedback adds a rule, **add its invariant to the script** in the same pass.
