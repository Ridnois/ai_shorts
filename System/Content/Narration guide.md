---
type: research
created: 2026-10-03
updated: 2026-10-03
status: v3 · short-story narration craft + feedback rules from 4 videos; English-only since 3 Oct 2026
tags: [research, youtube, script, narration]
---

# Narration guide

← [[YouTube Channel]] · [[Guidelines for new scripts]] · [[Production process]] · [[Channel voice]] · [[Illustration pipeline]] · [[YouTube with AI - quality content guide]]

Applied at stage 2 (script) and 3 (direction) of the [[Production process]], and checked before P3. **It is the source of truth for writing a script**; the other notes link to it. **Scripts are written directly in English** (not translated from Spanish): idioms, rhythm and sentence length are English ones, read aloud with the English voice ([[Channel voice]]).

Basis: short-film direction and writing craft (a hook in the first seconds, a single idea, setup → conflict → resolution structure, image before exposition) ([source](https://glcoverage.com/2024/12/25/tips-for-writing-short-film/), [source](https://subscribr.ai/youtube-strategy/scripting-youtube-shorts-engagement)), plus the feedback from the channel's videos. **The call-to-action ending** recommended by Shorts guides is discarded: here the video closes with an idea.

## 0. First, is the idea worth it?

Before structure and craft: pass the **idea gates** in [[Idea and hook quality]] (facts bank of ≥ 15, scoring, street-lamp and expert tests, five hooks). A well-crafted script about a street lamp is still a street lamp.

## 1. One story, one question

The video answers **one question**, written in one sentence before writing ("why did a factory stop because of a magnet?"). Anything that does not help answer it, out. If the topic needs two questions, they are two videos.

## 2. Structure of a Short (130 to 190 words, 6 to 8 scenes)

| Scene | Function | Words |
| --- | --- | --- |
| 1 · **Hook** | **The most astonishing true thing about the subject, stated plainly, with its meaning attached** (a reason before a reaction; never a bare big number). A concrete, specific fact or moment. No greeting, no "in this video", no "did you know…?" See [[Idea and hook quality]] §3 | 12 to 20 |
| 2 · **Minimal context** | What it is and why it matters, just what is needed to understand the next sentence | 20 to 30 |
| 3 to 5 · **Causal chain** | Three links. Each is born from the previous one with **"because" or "so"**, never "and then" | 20 to 30 each |
| 6 · **Turn** | What changes how everything is understood (around 60 to 70 % of the video) | 20 to 30 |
| 7 · **Close** | Answers the question and leaves **one idea the viewer closes alone**; one or two sentences; no moral, no summary, no call to action | 15 to 25 |

**Words are the budget; time is only a result.** Write inside the word ranges above, never to a target duration. The length appears after the voice is generated (measured English pace ≈ 144 words per minute with `elevenlabs/v3` at `speed` 0.95, see [[Channel voice]]); report it as derived. **One voice take per scene.**

## 3. Craft rules

1. **The hook is a headline, not a greeting, and it earns its reaction.** A concrete fact that shows what is at stake **and why it is remarkable** ("In May 2025, an assembly line in Chicago stopped moving") beats a generic question. Context gives the tension; waiting does not.
2. **Every hook is resolved in its scene or the next**, and answers all three: **what it is**, **why it happened**, **what it means**. A question is not left open just to sustain curiosity.
3. **Cause → effect, not a list.** Each link carries its why in the same sentence. "Because / so / but" joins; "and then" enumerates. If you must cut, sacrifice the side detail (dates, names, secondary figures), **never the why**.
4. **The concrete beats the abstract.** One object, one place, one figure per idea. A 3 cm screw says more than "a critical dependency". Data are few and go at the end of the sentence, where the voice stresses them.
5. **A thread that returns.** An object or character that reappears (the magnet, the glass dish) organizes the story and allows a close that echoes the hook. That object is also the **stock photo or reference** of its plate ([[Illustration pipeline]]).
6. **Every scene raises the stakes or changes the reading.** If a scene only informs, merge it with another or cut it. **One new idea per scene.**
7. **Make them think.** The ending delivers an idea, not a fact ("a case that falls on procedure never gets to judge the facts"; "if it goes wrong, it is not the recipe: it is a step"), without reproach or sermon.
8. **Write for the ear and read it aloud.** Sentences of 8 to 16 words, one idea each, active and concrete verbs; no parentheses or chained subordinate clauses. A single tense across the whole video (historical present: "In 1973, a ship arrives…"). If it sounds forced or dramatic when spoken, rewrite it. Use contractions as a spoken narrator would ("it's", "doesn't") when they sound natural.
9. **Rhythm.** Short, full sentences of varied length. **Silence is used once, on purpose** (≈ 1.2 s before the central question); not as a style.
10. **The voice names what the image cannot; the image shows what the voice names.** The voice does not describe the image. **Figures and dates go on screen**, not in the voice ([[On-screen text style]]).
11. **Rigor.** Every figure with source and date; what is weak, attributed ("according to…") or with "could". Use the exact words of the ruling or the fact and the same treatment for all characters: nobody gets adjectives. Check the request's premise. Detail in [[Guidelines for new scripts]] §1.
12. **Spoken numbers and acronyms.** Write numbers the way they are said ("twenty twenty-four" if the model reads "2024" oddly) and spell out acronyms the voice mispronounces ("A S M L"); note the change.

## 4. Script format (input to stages 3 and 4)

Each scene is a row; that way the script feeds the prompts of [[Prompt - per-scene generation guide]] directly:

| Scene | Voice (exact text) | Words | Visual plan: plate type, source and what it lets the viewer see | On-screen text (callouts, number, card) | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | … | | S/G/C/E/N · source (stock page or generated) · "lets the viewer see ___ so they understand ___" | callout names, number card, or context card ([[On-screen text style]]) | |

- **Two plates per scene** by default (about one plate per 5 s of voice), each with its usefulness sentence; each plate cites the script second where it is used.
- The **visual-plan cell cannot be filled** if the scene has nothing to show or explain: a sign that the scene is abstract and must be rewritten around a real thing or a process.
- If the user fixes a focus ("candidates, their crimes and how the election is sabotaged"), respect it; do not widen it.

## 5. Check before P3

- [ ] Does the video answer **one** question, written in one sentence?
- [ ] Is the hook a concrete fact in ≤ 20 words, no greeting?
- [ ] Does every hook answer what it is, why and what it means?
- [ ] Is each scene born from the previous one with a why, and does it bring **one** idea?
- [ ] Does someone who knows nothing understand the chain **without seeing the images**?
- [ ] Is there a pause or sentence that exists only to create suspense?
- [ ] Does the close leave an idea, with no moral or call to action?
- [ ] Does each scene have a concrete object with a reference photo?
- [ ] Is every claim supported or attributed?
- [ ] Read aloud, where does it drag? With the real voice, does the duration fit without speeding up?

## 6. Example: rewriting a hook

Before (waiting): "A magnet was missing." → does not say what it is, why or what it means.
After (context): "In May 2025, an assembly line in Chicago stopped: China had demanded licenses to export the rare-earth magnets that drive car motors." → what it is, why and what is at stake, in one sentence.
