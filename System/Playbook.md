---
type: rules
updated: 2026-10-05
status: v3 · pause plan (human rhythm); immersive plates (no empty screens); hook test; fail states; [H] marks untested rules
---

# Playbook: every rule for a Short

Read it whole before writing anything. **[H] marks a hypothesis** (a number or habit not yet tested on channel data); the 10-video review in [[Publish]] §Analytics loop turns each into a kept, changed or deleted rule. Model to imitate: [[Model script]]. One note, no history: when feedback changes a rule, **edit the rule here** ([[Feedback loop]]). Process, models and prices: [[Workflow]]. Publishing and numbers: [[Publish]]. Look and brand: [[Style]].

**Product:** vertical Shorts (9:16) for YouTube and TikTok, English, one a day. Goal: narrated learning you enjoy even knowing it is AI. Same master on both platforms.

## 1. Idea (gate P1; read `Analytics/Report.md` first)

1. **Facts bank:** ≥ 15 remarkable true facts (origin and scale, strange behaviour, extremes, connections, expert details; uses and news last), each with source and date.
2. **Score** each angle 1 to 5 on surprise, scale, depth, evidence, showable, plain. **The thread must score ≥ 4 on surprise, scale and plain.** Show only the chosen row and one line per rejected candidate. **Argue against it:** a second pass lists the three strongest reasons a viewer would scroll past; if any is not answered by the thread, rescore it lower. Scores are the agent's guess until Report data exists. Report data: a hook type or topic that held `viewed_pct`, `shares`, `subs_gained` earns a bonus; one that fell is not repeated without a new angle (under 10 videos with data it guides, it does not decide).
3. **Street-lamp test (it has a fail state):** if a headline or product spec answers the central question, go back to 1. **"Borderline" is a fail:** either change the angle, or write one sentence saying which mechanism beyond the headline the video adds and get the user's yes before P2. Never record "borderline" and proceed. **Expert test:** a specialist would call it "the interesting part"; each scene has one detail a generic explainer skips. **Coffee test:** the thread in one plain sentence; a friend saying "so what?" means surprise ≤ 3.
4. **Five candidate hooks of different types;** pick with the **hook test** in §2 (not by length). The hook type (surprising fact, surprising number, question, contradiction, stakes) goes in the Status note and `Analytics/videos.csv`.
5. **Original synthesis:** one derived comparison or number per video (monetization policy: no template content).
6. **Demand check (outside evidence):** one line per finalist: is the subject searched or shared? Search autocomplete for the plain question, and the views of 3 comparable Shorts or videos. No demand and a strong thread = write why it still earns a slot. Record it in the Status note.
7. **Topic spread [H]:** two consecutive videos never share a topic family (batteries, metals, space, medicine, machines...); use `series` in `videos.csv` only for a recurring format with at least 5 videos.

## 2. Script (gate P3)

- **Length in words, never seconds:** 130 to 190, aim 130 to 160, 6 to 8 scenes [H]. Austin runs ≈ 170 wpm (≈ 187 speaking), so 160 words ≈ 60 s; report duration only after the voice exists.
- **One question, one theme line** (plain words, stated in scene 1 or 2). **Every scene opens with a bridge** back to it ("so", "that is why", "the catch"); the close answers it. **≤ 5 facts, ≤ 3 spoken figures.** One new idea per scene.
- **Scene 1 = the hook: a need-to-know claim a stranger understands at once.** Length is whatever lets the first clause be spoken inside 3 s (check it on the voice take, not by counting). **Hook test, all five must hold:** (1) **Plain:** no term that a later scene defines ("Some wires waste no electricity. Almost nobody can use them.", not "zero resistance"). (2) **Reason to care before the reaction:** it names a consequence for the viewer, a broken expectation, or a stake; a big number alone is not a hook. (3) **Open question:** a curious friend would ask "why?" or "how?", and the next scene answers it. (4) **Sound-off:** the first caption word plus the first image already raise that question. (5) **Honest:** the video delivers exactly what it promises (no malicious clickbait). No date opener, "Imagine", greeting, "did you know", or question as the first words. Resolved within its scene or the next.
- **Explain, do not narrate:** mechanism, cause → effect joined by "because / so / but", never "and then". Cut side detail, never the why. Concrete beats abstract. Facts answer "so what changes?" in at least two scenes.
- **Structure:** 1 hook · 2 minimal context (16 to 26) · 3 to 5 causal chain (20 to 30 each) · 6 turn (20 to 30) · 7 close (15 to 25).
- **Close = concrete payoff:** one plain sentence that answers the question and says what it means for something the viewer knows; repeatable to a friend. No aphorism, moral, summary or call to action. If it fits, the last plate is the first (loop).
- **Cut test:** delete each sentence in turn; if the video still answers its question, it stays deleted.
- **For the ear:** sentences of 6 to 16 words, active verbs, varied length, ≤ 1 rhetorical question, no exclamation marks, **the voice should be calm and unhurried, human enough to fall asleep to** (user, 5 Oct 2026). **Pause plan:** every boundary and every inner pause is planned from the sentence's intention and emotion, never left to the model's defaults; see the table below. A **delivery note per scene** (calm, rising, amused, grave). Figures and dates go on screen, not in the voice. Numbers and acronyms are written as spoken if the model misreads them ("A S M L").
- **Rigor:** every figure has source and date; weak facts attributed or cut ("could"); convicted ≠ accused ≠ investigated; if sources conflict, say "a base recipe from several sources"; respect the focus the user fixed; the research note says what was not verified.
- **Pause plan [H]** (user, 5 Oct 2026: *"pauses should be paired with intention and emotionality of the phrase... the narrative rhythm so human that you could fall asleep listening"*). Each scene gets a **pause after** (the `gaps` entry; the audible silence is the gap plus about 0.42 s of kept lead and tail) and, where the thought needs it, **inner pauses** (`pauses` in `plan.json`):

  | Where | Pause | Why |
  | --- | --- | --- |
  | The next scene continues the same thought (starts with "and", "so", "but") | 0.15 to 0.25 s | no gap that breaks a sentence in two |
  | A new idea | 0.45 s | the default breath |
  | After a turn or the catch, before the payoff, before the central question | 0.9 to 1.2 s | the listener's time to think |
  | Inner: after a short setup ("Simple, but slow.") | 0.5 to 0.9 s | lets the claim land |
  | Inner: after a list item or a clause end | 0.25 to 0.4 s | breath |
  | **Never** | between subject and verb, after "the", "a", "of", "and", before a number's unit | the uncanny pause the user heard |

  The agent cannot hear: it writes the pause plan in the **Pause after (s) and inner pauses** columns of the script table (intention in words: "gentle", "let it land", "breath"), builds with them, and the user's listening rubric at P7 decides ([[Workflow]]). Pauses the voice model made on its own (a long gap mid-clause) are shortened with an inner pause of 0.25 s on the word before it.
- **Script table columns:** scene · exact voice text · words · delivery note · **pause after (s) and inner pauses (word, seconds)** · visual plan (plate type, source, usefulness sentence) · on-screen text · source.

**Checklist before P3:** facts bank and scores · street-lamp (not borderline), expert and against-the-idea tests · demand check · five hooks of different types · words in range · scene 1 passes the hook test · theme line and bridges · facts ≤ 5 · cut test · concrete ending · understandable without the images · read aloud, no drag · every claim sourced.

## 3. Visuals (gate P4a: the visual plan, one row per plate)

- **Usefulness test per plate:** "this plate lets the viewer see ___ so they understand ___". If it cannot be written, cut or replace it.
- **Types:** S stock photo (free, credited) · G generated explainer · C cutout · E photo edit · D drawn diagram (Pillow, exact geometry) · N number plate. **Real things are photographed, hidden things (insides, processes, scales) are explained.** Photo plus callouts beats a generated schematic.
- **Rhythm:** a new image every ≈ 3 to 4 s, none over 5 s: **16 to 20 plates for 160 words** [H]. At least half real photos or figures, ≥ a third explainers or cutouts, no two consecutive plates of the same type unless treatment and subject both differ. The same photo may return with a different crop (`focus`, `zoom`). Order plates by the sentence they illustrate.
- **Find 2 to 3 candidate photos per scene** before the plan (Openverse, NASA, Commons; real diagrams as `contain` plates). Pick relevance first, then ≥ 1,080 px, sharp, no watermark or brand, then license. Credits go to `stock/_credits.jsonl` as downloaded; CC BY and CC BY-SA are credited in the description. No identifiable people unless they are the subject.
- **Generated plates: ≤ 3 per Short, `openai/gpt-image-2`, content-first prompts, no custom style** (no clay, sketch, "cinematic", mood, props). Prompt order: subject (exact name) · structure (parts, count, arrangement, from the research note) · view (cutaway, exploded, top-down) · what must be readable (paraphrase, never the narration sentence) · what each reference supplies · output ("plain background, no letters, numbers or labels"; `background: transparent` for cutouts). Use 1 to 4 real references; do not paste narration into a prompt; check every reference for text and brands.
- **Scientific fidelity beats creativity:** an explainer is a textbook schematic of the established model, only what the research note supports; prompt what must not appear ("no glow, no light rays, no decorative particles"); check every element against the note; mark "schematic" in Status when simplified. Unsourced element → regenerate once without it or use a photo. Image models restyle diagrams: use diagrams as references or `contain` plates, not as sources to redraw.
- **No bare backdrops:** a number card, quote or callout sits on a real photo or faithful explainer, never an empty gradient (the builder refuses `blank` plates).
- **Immersive plates, no empty screens** (user, 5 Oct 2026: *"sometimes the screen feels empty, only with a picture and a note"*). **No plate is one picture and one label on a flat gradient.** Three layouts: (1) **full-bleed** photo with callouts and/or a card; (2) **framed photo** (`contain`) with `"bg": "blur"` (the same photo, blurred and darkened, fills the frame) and a card or an `inset`; (3) **split**: an explainer or diagram on top with `"bg": "blur"` + `"bg_photo"` (a related real photo) and an **inset** of the real thing below the captions. A flat gradient is allowed only behind a cutout. The build prints `EMPTY PLATE`: fix before rendering. Specs: [[Style]] (Immersive plates).
- **Safe zone (9:16):** subject within 15 to 60 % of the height; caption zone (50 %), card (66 %) and callout labels never collide ([[Style]]).
- **Plates must make sense without the voice.**

## 4. On-screen text (specificity test)

- **Purpose of each text:** callout names a part (1 to 4 words, ≥ 1 per photo or explainer, ≤ 3 per plate) · number card quantifies (the figure with unit, what it measures, source) · context card frames and sources (label = place/date/person/mechanism, title = a statement with a verb ≤ 26 characters, detail = source, scale or caveat ≤ 40) · margin note gives a voice (≤ 2 per video, ≤ 60 characters).
- **Specificity test:** could this text appear unchanged in a video about another topic? Then rewrite it with a name, number, place or mechanism. Banned: "The takeaway", "Key point", "Fun fact", "Same material", "Why it matters", "In summary" and the banned words in [[Style]]. Do not repeat the narration. One card per plate; not every plate needs one.
- **Symbols:** never write ≈ ≥ ≤ → in a card or callout (the font shows boxes): use "about", "or more", "to", "·". Figures like `180 °C`, `72.5 %`, `1,000`. Card captions ≤ 40 characters.
- **Word-by-word captions on every video**, from the voiced words (spelling for the eye in `captions`).
- **No branding inside the video** (no progress bar, mark, series tag, logo).

## 5. Voice and sound

- **Voice:** `elevenlabs/v3`, `Austin`, `language_code: en`, `speed` 1.0, `previous_text` / `next_text`, one take per scene with the exact script text. Optional expressive variant (`stability` 0.35, `style` 0.35, one `[tag]` per scene in the voice prompt only, never in captions) is an A/B in a test run on scene 1; the user's ear decides. The agent cannot hear: declare it at P7.
- **Sound:** the builder synthesizes the sound design by default (`sound` in `plan.json`: **the opening bell/thump the user likes**, scene whooshes, plate ticks, card pings, callout clicks, A-minor drone; levels voice ≈ −22, effects ≈ −31, bed ≈ −37 dBFS [H]; dials `sfx_gain`, `bed_gain`). Any recording or music is **opt-in**: a plan row with source, license and purpose, approved at P4a, from YouTube Audio Library → Sonniss → Pixabay (per track) → Incompetech (CC BY, credit); credits in `sound/_credits.jsonl`; volume under voice 0.18 to 0.22, bed ≤ 0.12. **Never:** BBC/RemArc (non-commercial), CC BY-NC, game rips, unread licenses (NCS, BenSound, FMA). **BigSoundBank and Freesound are deferred**; no ML-generated sound.

## 6. Edit (Blender 5.2, `build_video.py` + `plan.json`)

- A voice sentence is never cut or abrupt: the builder pads every take (0.30 s before, 0.40 s after, 20 ms fade-in, 50 ms fade-out) and `CHECK=1` verifies lead-in, tail and overlaps.
- Speech starts at once (`start` ≤ 0.2 s), strongest real image and first caption word on frame 1 (**the opening bell and the voice-first start are liked by the user: keep them**); gaps between scenes follow the **pause plan** (§2; `gaps`, default 0.45 s), inner pauses are set with `pauses` (`[["word", seconds, nth]]` per scene: the silence after that heard word becomes exactly that long, captions follow), 1.2 s tail; page turn between scenes, 0.2 s cross-fade within, 8 % push alternating in and out. The build prints `PLATES` and `LONG PLATE` (> 5 s): fix before rendering.
- `plan.json` fields and builder details: header of `System/scripts/build_video.py`. Captions timed by `word_timings.py` (whisper, ≈ $0.01 per take), estimated if skipped; `render/<prefix>.srt` is written for upload.
- Blender 5.2 gotchas: `image_settings.media_type = "VIDEO"` before `FFMPEG`; `sequence_editor.strips`; `new_effect(length=...)`; `keyframe_new_interpolation_type = "LINEAR"`; `view_transform = "Standard"`; absolute paths in the `.blend`; TEXT default font is monospaced (load Noto Sans); system Python has no numpy (Blender's does); background mixdown is silent (the builder checks strips).

## 7. Checklist before P7 (the agent runs it and says what it could not check)

- [ ] Scene 1 passes the five-part hook test; first clause spoken inside 3 s on the real take; speech ≤ 0.2 s after frame 1
- [ ] Captions on from the first word (`CAPTIONS n words` printed), stills show no overlap with cards or callouts
- [ ] Every plate has a usefulness sentence; every generated plate checked against the research note
- [ ] No bare gradient plate; a new image every ≈ 3 to 4 s, none over 5 s
- [ ] Theme line bridged by every scene, facts ≤ 5, concrete ending
- [ ] Every on-screen figure sourced (card or description); no in-video branding
- [ ] **Not verified, said out loud:** how the voice sounds, caption timing against speech, sound levels, pace in motion. P7 belongs to the user.
