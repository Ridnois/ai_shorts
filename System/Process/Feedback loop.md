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

1. **Record it verbatim** in the video's feedback note (`Videos/<Topic>/Scripts/Post-render feedback - <Topic>.md`), or in a dated quote if it is about the process. The user's words stay; they are the evidence.
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

## 4. The coherence check

`System/scripts/check_vault.py` guards the vault: it fails on broken wikilinks, notes without front matter, System notes missing from the [[YouTube Channel]] index, scripts that do not compile, and **missing encoded feedback** (a list of phrases that must stay in the notes that carry each rule, so a later edit cannot silently drop a rule). When feedback adds a rule, **add its invariant to the script** in the same pass.
