---
type: research
created: 2026-10-04
updated: 2026-10-04
status: feedback received · applied to the vault 4 Oct 2026
tags: [research, youtube, feedback, superconductors]
---

# Post-render feedback - Superconductors

← [[YouTube Channel]] · [[Superconductors - Status]] · [[Feedback loop]]

**Render watched:** `Media/Legacy/Superconductors/render/sc-72s-9x16-r2.mp4` · **Watched with sound?** yes · **Device:**: desktop

## 1. Verdict

**Would you publish it as it is?** yes after small fixes
**In one sentence, the best thing:** the general layout, visual text, visual explanation
**In one sentence, the worst thing:** the illustrations and the boring narrative

## 2. By layer (rating 1 to 5, then your words)

| Layer                                                                                                                                               | Rating | What you saw or heard, and what you want instead                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ----------------------------------------------------------------- |
| **Hook** (first 3 s: is it a claim you need to hear? does it stop you?) — *"Some wires carry electricity with zero resistance. Not low. Zero."*     | 2      | It vague, i may dont know what zero resistance means              |
| **Idea and content** (is it surprising, clear, scientifically right?)                                                                               | 2      | not surprising nor clear enough, well researched                  |
| **Script and pace** (explains or narrates? drags anywhere? too dense?)                                                                              | 2      | boring, feels unconnected, could be more compacted                |
| **Illustrations and photos** (useful, faithful, one per idea?) — the levitation, LHC and diamond-anvil plates are held longest (9 to 12 s)          | 3      | getting better, could improve, be more realistic and related with |
| **Text boxes, callouts, highlight** (readable, specific, in the right place?)                                                                       | 5      | Good, structured                                                  |
| **Captions** (on the spoken word? readable on every image?)                                                                                         | 5      | Font could be a little bit smaller                                |
| **Brand layer** (progress bar, mark, series tag, avatar, name)                                                                                      | 0      | unnecesary, should be removed                                     |
| **Voice** (timbre, speed, intonation, mispronounced words)                                                                                          | 3      | needs improvement, rithm could be more controlled and passionate  |
| **Sound design** (thump, whooshes, ticks, pings, drone: too loud, missing, annoying?) — first time it exists; synthesized, never heard by the agent | 5      | good for now                                                      |
| **Editing** (cuts, cross-fades, how long an image stays, transitions)                                                                               | 3      | could improve making it a little more dinamic                     |
| **Ending** (does it leave an idea? does it loop?)                                                                                                   | 1      | vague ending as the rest of the script                            |

## 3. Moments (use the time in the video)

| Time (s) | What happens | What is wrong or great | What to do |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |

## 4. Checks only you can do (the agent cannot hear or watch the video)

- [x] The voice sounds natural and the pace feels right
	 the pace could improve
- [x] Each caption word lands on the spoken word
- [x] The sound design is at a comfortable level (adjust `sfx_gain`, `bed_gain`)
- [x] Transitions and the progress bar look right in motion
- [x] The facts you know are correct; list any doubt here (the agent's own doubts: pair size in the pairing drawing, the "grids could recover part of the five percent" line, the 28-year gravimeter figure from a secondary source):

## 5. After publishing (fill 48 hours and 7 days later; see [[Channel strategy]] §6)

| Metric | 48 h | 7 days |
| --- | --- | --- |
| Views / **engaged views** | | |
| Share who stay past the first seconds (Studio: viewed vs swiped away, if shown) | | |
| Average percentage viewed | | |
| Subscribers gained | | |
| Comments worth reading (paste the best two) | | |

## 6. Process and anything else

Rules you want changed, things the agent should always or never do, ideas for the channel:

- make the content more engaging and interesting, i feel like i got lost on the facts and forgot the theme of the video, it is good on a non self-concious way
- Add more reference images, so it changes faster

## 7. Keep and change (for the agent to turn into rules)

**Keep exactly:** text distribution, and notes
**Change from now on:** no progress bar nor branding, more reference images and better written scripts

## Response (4 Oct 2026)

| Feedback (verbatim in the sections above) | Layer | What changed where |
| --- | --- | --- |
| Hook 2/5: *"it vague, I may not know what zero resistance means"* | Idea, script | New rule 0.8 *Plain-words test* ([[Guidelines for new scripts]]); [[Idea and hook quality]] (Plain criterion, coffee test); [[Narration guide]] (opener in plain words; the failed hook and its rewrite *"Some wires waste no electricity. Almost nobody can use them."*); [[Shorts quality bar]] §1 |
| Idea 2/5, script 2/5: *"not surprising nor clear"*, *"boring, unconnected, could be more compacted"*, *"I got lost on the facts and forgot the theme"*; engaging; ending 1/5 *"vague"* | Script | Rules 0.9 *One thread, a fact budget* (theme line, a bridge in every scene, ≤ 5 facts, ≤ 3 spoken figures), 1.10 *Concrete ending*, 1.11 *Cut test*, 1.12 *Engaging is stakes plus specificity*: [[Guidelines for new scripts]]; [[Narration guide]] §2 (through-line example, new close definition, aim 130 to 160 words); [[Shorts quality bar]] §2; [[Production process]] stage 2; [[Fast workflow]] §6 |
| Illustrations 3/5: *"be more realistic and related with…"* (the sentence stops there) | Illustrations | Rule 2.15 and [[Illustration pipeline]]: photo plus callouts beats a generated schematic when a photo exists; generated plates are realistic renders from a real reference, labelled "schematic" when simplified |
| *"Add more reference images, so it changes faster"*; editing 3/5 *"a little more dynamic"* | Illustrations, editing, builder | A new image every ≈ 3 to 4 s, 16 to 20 plates, none over 5 s, half real photos, 2 to 3 candidates per scene, the same photo with a new crop allowed ([[Guidelines for new scripts]] 2.2 and 2.15, [[Illustration pipeline]], [[Fast workflow]], [[Shorts quality bar]] §4). `build_video.py`: pushes 8 % and alternating, cross-fades 0.2 s, `LONG PLATE` warning |
| Text boxes 5/5, captions 5/5 but *"font a little smaller"*; keep *"text distribution, and notes"* | Text | Captions 104 to 88 px ([[On-screen text style]], [[Shorts quality bar]] §3, [[Channel playbook]]); the card, callout, margin-note and caption layout is **frozen** (*Keep exactly* in [[On-screen text style]]) |
| Brand layer 0/5 *"unnecessary, should be removed"*; *"no progress bar nor branding"* | Builder, brand | Progress bar, mark and series tag removed from `build_video.py` and `plan.json`; `mark.png` deleted; [[Channel playbook]] §3.4 and §4, [[Blender editing]]; a guard in `check_vault.py` fails if the builder regrows `add_brand` |
| Voice 3/5: *"rhythm could be more controlled and passionate"*; *"the pace could improve"* | Voice | [[Channel voice]] *Expressiveness*: rhythm from the script, a delivery note per scene, an expressive variant (`stability` 0.35, `style` 0.35, audio tags in the voice prompt only) as a **P5 A/B test** of scene 1 (≈ $0.02, [[Fast workflow]]); the default stands until you listen |
| Sound design 5/5 *"good for now"* | Sound | unchanged (synthesized sound design stays on by default) |
| Checks: captions land on the words, transitions and sound fine | Verified by the user | recorded; the agent's own doubts (pair size, grid 5 %, 28 years) were not commented on: they stay open in [[Superconductors - Status]] |
| Process | Guards | `check_vault.py`: 10 new invariants and two builder guards; supersession rows in [[Feedback loop]]; `CLAUDE.md`, the runner prompt (`youtube-pipeline/pipeline.py`), the feedback template and the index agree |

**Not done:** the Superconductors video was not reworked (see its *Rework list*). **Not verified:** the voice variant (not heard), whether 88 px reads better, whether a new image every 3 to 4 s feels right (the agent has no way to watch it). **Open question:** the feedback row called *Brand layer* named avatar and name too; the agent read it as the video only and kept the channel's name, avatar and banner ([[Channel playbook]] §4).
