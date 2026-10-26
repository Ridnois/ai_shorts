---
type: rules
updated: 2026-10-26
status: v10 · condensed to the rules that change a video (user, 26 Oct 2026: "optimize the playbook"); short test block (90 to 140 words) and phrase captions (user, 26 Oct 2026); v9 · the bar is the feed (named real case, named tool shown running, frame fill, slideshow-risk score); v8 · named-subject hook, series arcs, connection test, running example, bridge visuals; v7 · AI channel; v6 · one-take voice, mix to −14 LUFS, show the verb
---

# Playbook: every rule for a Short

Read it whole before writing. **[H]** marks a hypothesis not yet tested on channel data; the 10-video review in [[Publish]] §Analytics loop keeps, changes or deletes it. Model to imitate: [[Model script]]. When feedback changes a rule, **edit the rule here** ([[Feedback loop]]); the dated user quotes behind each rule live in git history. Process and prices: [[Workflow]]. Publishing and numbers: [[Publish]]. Look: [[Style]].

**Product:** vertical Shorts (9:16) for YouTube and TikTok, English, **five a week at a fixed time, never two on one day** (YouTube diagnostic, 9 Oct 2026). Goal: **teach people AI** (how it works, agents at work, what's coming) as narrated learning worth watching even knowing it is made with AI. Same master on both platforms.

## 0. The bar is the feed, not our last video

A Short competes in one swipe against the outliers in `Pipeline/Niche map.md` §Reference formats. The agent's review of its own renders (26 Oct 2026) found five gaps; each has a rule:

| Gap (26 Oct 2026) | Ours | What wins in the feed | Rule |
| --- | --- | --- | --- |
| Subject | a concept drawn as a diagram ("chatbot vs agent") | a named real thing with an outcome ("The Pepsi Contest That Killed 5 People") | §1 item 9 |
| Proof | tools named, never shown running | the real thing on screen | §3 *A named tool is shown running* |
| Frame | small hero, lower half empty (16 of 71 s sparse) | the subject fills the frame | §3 *Fill the frame* |
| Look | the same ground, pill and card on every tile | a new picture for each step | §7 slideshow-risk score |
| Shipping | 9 renders, 0 uploads | a channel learns from its own median | [[Workflow]] *Ship before you build* |

## 1. Idea (gate P1; read `Analytics/Report.md` first)

1. **Facts bank:** ≥ 15 remarkable true facts (mechanism, strange behaviour, scale, connections, expert details; news last), each with source and date. A fact about what a model or product can do is ≤ 12 months old or dated on screen.
2. **Score** each angle 1 to 5 on surprise, scale, depth, evidence, showable, plain; the thread needs ≥ 4 on surprise, scale and plain. Show the chosen row and one line per rejected candidate. **Argue against it:** list the three strongest reasons a viewer would scroll past; any left unanswered lowers the score. Report data, once it exists, gives a bonus to a hook type or topic that held `viewed_pct`, `shares`, `subs_gained` (under 10 videos it guides, it does not decide).
3. **Street-lamp test:** if a headline or product spec answers the central question, go back to 1. **"Borderline" is a fail:** change the angle, or write the one mechanism the video adds beyond the headline and get the user's yes before P2. **Expert test:** a specialist would call it "the interesting part". **Coffee test:** the thread in one plain sentence; "so what?" means surprise ≤ 3.
4. **Five candidate hooks of different types** (surprising fact, surprising number, question, contradiction, stakes); pick with the **Hook test** (§2). The type goes in Status and `Analytics/videos.csv`.
5. **Original synthesis:** one derived comparison or number per video (no template content: [[Publish]] Inauthentic content).
6. **Demand check:** one line per finalist: search autocomplete for the plain question and the views of 3 comparable Shorts (`youtube_search.py`, [[Audience]]). No demand for the mechanism: bridge it to an outcome people want. Recorded in Status.
7. **Outcome and mechanism** ([[Audience]]): Y (the result the viewer wants) and X (the mechanism they did not know blocked it), one of the three series, after a deep-first search (`Pipeline/Niche map.md`).
8. **Topic spread and mini-series [H]:** every video is **How it works**, **Agent at work** or **What's coming** (`series` in `videos.csv`); two consecutive videos never share a series. The description ends with the next two titles of the series; the pinned comment links the previous one.
9. **A named real case carries the concept [H]** (26 Oct 2026; breakout titles in the feed are named things with an outcome, "Toyota's $2,300,000,000 Mistake"): the concept enters through one real, dated case with a named product, company or person and a consequence. It becomes the running example (§2) and the thumbnail's focal image, and is verified at P1 like any fact. No real case: reject the idea or bridge it to one.

## 2. Script (gate P3)

- **Length in words, never seconds. Short test block [H]** (user, 26 Oct 2026: *"Lets test with shorter videos"*; YouTube diagnostic, 9 Oct 2026: 6 in 10 viewers swipe away, *"test 30 to 45 seconds"*): **the next 10 videos are 90 to 140 words, aim 110 to 130 (about 35 to 45 s at rate 1.1), 4 to 6 scenes, ≤ 3 facts. Compact test:** every third of them is 60 to 85 words (about 25 s), 3 to 4 scenes. Never pad; if the cut test leaves 95 words, ship 95. After 10 uploads, `analytics.py report` compares them by length with the earlier 180 to 235-word cuts (≈ 60 to 70 s) and the rule is kept or reverted. Report the duration only after the voice exists.
- **One question, one theme line** (plain words, stated in scene 1 or 2). Every scene opens with a bridge back to it ("so", "that is why", "the catch") only where the logic turns; the close answers it. ≤ 2 spoken figures. One new idea per scene.
- **Answer a real viewer's question:** when a video compares or advises, open with the objection a real person says ("I use top chatbots for free. Why pay?"); every scene answers it, the rest is cut [H].
- **Scene 1 is the hook: a need-to-know claim a stranger understands at once.** The first words are the twist itself, with no setup, greeting or context; the first clause is spoken inside 2 s (check the take). **Hook test**, all must hold:
  1. **Plain:** no term a later scene defines ("A chatbot never looks anything up. It guesses.").
  2. **Reason to care:** a consequence for the viewer, a broken expectation or a stake; a big number alone is not a hook.
  3. **Open question:** a friend would ask "why?" or "how?", and the next scene answers.
  4. **Sound-off:** the first caption plus the first image raise that question.
  5. **Honest:** the video delivers exactly the promise.
  6. **Matches the package** (§2b): it restates the title and thumbnail promise; scene 2 gives proof and plan ([[Audience]]).
  7. **Named:** after the first sentence the viewer knows what the video is about, in words they know, never "the idea", "the trick", "the math".
  8. **Curiosity before explanation:** no mechanism, definition or history before the promise. Default How it works shape: *subject + why it matters + "and here is how it works"*.
  No date opener, "Imagine", "did you know", or a question as the first words; no story opener.
- **Low-attention-proof:** written for a half-listening viewer. First sentence ≤ 12 words, no technical term except the glossed subject; the stake follows. No jargon in the voice (parameter counts, benchmark names, version strings go on screen or out). One idea per sentence. **The conclusion is spoken as a conclusion** and shown on a card before the social question. Repeat the thread word in hook, middle and close.
- **Explain, do not narrate:** cause and effect joined by "because / so / but", never "and then". Cut side detail, never the why.
- **Structure by series [H]** (short block in brackets): **How it works:** hook · **definition** (one plain sentence a stranger knows) · origin (only when it is part of the twist) · "Here is how", on one running example (2 to 3 scenes) · the catch · close. **Agent at work:** hook (the result) · the task · the run, step by step · what to copy · close. **What's coming:** hook (the change) · the evidence · the mechanism · the counter-view · close.
- **Connection test:** every sentence answers the question the previous one raised; the script table writes that question per scene. A sentence answering no open question, or opening one the next ignores, is rewritten or cut.
- **One running example carries the mechanism:** the explanation stays on one concrete case the viewer knows (the real case of §1 item 9, or "The cat sat on the ___": guess *moon*, the score says how wrong, the numbers are nudged, it guesses *mat*), and the loop closes on it. An abstraction enters only as a mapping from that example, said and shown ("those numbers are a position; the score is the height").
- **Close = concrete payoff:** one plain sentence that answers the question and says what it means for something the viewer knows. No aphorism or summary. **Then one social question** the viewer can answer in the comments ("Would you let an agent send email in your name? Tell me what you think."), on screen as a margin note; never "like and subscribe". If it fits, the last plate is the first (loop).
- **Cut test:** delete each sentence in turn; if the video still answers its question, it stays deleted.
- **For the ear:** sentences of 6 to 16 words, active verbs, ≤ 1 rhetorical question, no exclamation marks; the voice is **calm and unhurried, human enough to fall asleep to**. Figures and dates go on screen; numbers and acronyms are written as spoken ("G P U"). A delivery note per scene.
- **AI rigor:** every capability claim names model, version and date ("GPT-5 in August 2025", never "AI can"); benchmarks carry source and caveat; forecasts are labelled with who made them; models are described by mechanism ("it predicts the likely next word", not "it wants"); no hype or doom; a demo is a real run (§3).
- **Rigor:** every figure has source and date; weak facts attributed or cut; convicted ≠ accused ≠ investigated; conflicting sources said; the research note lists what was not verified.
- **Pause plan [H]:** pauses follow the sentence's intention and emotion and are **written into the one take** (§5), never cut into the audio:

  | Where | How it is written | Silence (Inworld TTS-2, measured 9 Oct 2026) |
  | --- | --- | --- |
  | Next scene continues the thought ("and", "so", "but") | a new paragraph, no mark | about 0.35 s |
  | A new idea | a full stop; a new scene is a new paragraph | 0.35 to 0.6 s |
  | Before the payoff or central question (1 or 2 per video) | `beat` 0.2 to 0.3, or `pauses` `[["word", 0.3]]` (adds to the natural pause) | 0.7 to 0.9 s, never over 0.9 |
  | After a short setup ("Simple, but slow.") | its own sentence | natural |
  | **Never** | between subject and verb, after "the", "a", "of", "and", before a unit | |

  The agent writes each pause's intention in the table, checks the take's silences (`silencedetect`), and fixes a pause inside a clause by rewording and a retake, never by cutting.
- **Script table columns:** scene · question it answers · voice text · words · delivery · pause intention and beat · visual beat (what the viewer sees happen, medium) · on-screen text · source.

## 2b. Package (written inside the Script note, gate P3)

A **Package** section before the scene table: **Y** and **X** · **promise** (one sentence the video must pay) · **3 titles** (≤ 100 characters, one marked) · **thumbnail**: one focal image (the real case or the anchor in its surprising state) and 3 to 4 words that complement the title ([[Workflow]] §Thumbnail), plus one line on why it beats 3 neighbours in search · **opening map**: scene 1 = promise, scene 2 = proof and plan. `publish.json` copies these fields; a changed hook re-checks the package. Rules: [[Audience]].

**Checklist before P3:** package matches scene 1 · facts bank, scores, street-lamp, expert and against-the-idea passes · demand check · named real case · five hooks · words in range · Hook test · series arc · connection test · one running example, loop closed · theme line · cut test · concrete ending · understandable without images · every claim sourced.

## 3. Visuals (gate P4a: beat sheet, one row per plate)

- **Show the verb, not the noun.** Each sentence gets a visual beat: what the viewer must *see happen* to understand it with the sound off. **Usefulness test:** "the viewer sees ___ happen, so they understand ___". Showing a thing only because the voice names it is allowed once, as the first look at a part the mechanism needs.
- **Swap test:** if any other picture of the same noun would do, cut it. A push on a generic photo is decoration, not motion.
- **Medium by what the sentence does** (first row that fits):

  | The sentence... | Medium |
  | --- | --- |
  | shows an AI or agent doing a task | a **recorded run** of the real tool (`video`, cut to 9:16 on the action) |
  | shows a real thing, place or scale | **footage** of it doing the verb; a photo with a `move` only when no footage exists |
  | explains a process inside a model with depth or many parts | **3D plate** (`scene3d.py` or three.js in HyperFrames): the exception, only where depth explains ([[Style]]) |
  | explains a flat hidden process (a loop, a pipeline) | **motion** plate (`motion.py` or HyperFrames): a faithful moving schematic |
  | gives a number | a **comparison that builds** (a bar grows, a counter runs), never a figure alone on a card |
  | change over time · a place · a trade-off | a chart that draws itself · an animated map · both in one frame |

- **A named tool is shown running:** a script that names a product (ChatGPT, Claude Code, Codex) shows a recorded run of it in at least one scene, whatever the series; logos and drawn mock-ups do not count.
- **Fill the frame:** the subject spans 60 to 80 % of the frame width ([[Style]] Composition); the stage (y 10 to 75 %) is never three-quarters empty for over 3 s. `check3d.mjs` prints `WARN SPARSE` and `WARN SMALL TEXT`: fix both or write why in Status.
- **Comparisons live on one board** (user, 26 Oct 2026: comparisons got lost between fast topic changes): one table (logos as column heads) stays on screen across the comparing scenes; each reason adds a row on the word that names it, earlier rows dimmed [H].
- **3 to 5 visual worlds and one anchor** that returns at the close in a changed state. One source on more than 2 plates without a new state is a repeat (`REPEAT`).
- **Cut for a new step, move within it.** A plate starts **on the word** that opens a step (`at`, 0.15 s early). A visual event every 2 to 3 s; nothing unchanged over 3.5 s; a still ≤ 4 s. ≥ 60 % of the runtime moves (`MOTION SHARE`).
- **Bridge visuals:** moving from the example to a model of it, the plate shows the mapping while the example stays visible; never a cut from the example to an unrelated abstraction. The loop closes on screen: the same example improves.
- **Parts build in the order they are named;** nothing labelled appears before it is spoken. **One focal point:** the subject in ember or moving, the rest grey or still; on screen at once: subject, ≤ 1 label or figure, caption.
- **Real first for real things, drawn for hidden ones.** Footage licences: PD, CC0, CC BY, CC BY-SA, Pexels or Pixabay (`stock_videos.py` logs credits); `look` at frames before choosing; cut 3 to 5 s on the action (`cut --focus`); no landscape source for text or fine detail; no visible brand, burned-in text or identifiable person unless they are the subject.
- **Recorded runs:** the real tool, large font, tall window, prompt visible before the result; speed-ups marked ("4x"); nothing staged or retyped; no key, email, path or personal data (blur or re-run); a product's interface shown as itself, never imitated.
- **AI clichés are banned:** glowing brains, robots at keyboards, circuit faces, binary rain, "AI" chip renders, human-robot handshakes. Show the text the model wrote, the tokens, the run, the data centre.
- **Plates** (specs in [[Style]]): ink ground, ≤ 3 colours plus grey, text ≥ 40 px, nothing in the caption band or interface zones; look at every `--sheet` before the build. 3D: ≤ 30 s per Short, `--preview` first; text never moves in 3D.
- **Generated media: opt-in, ≤ 3 per Short.** Stills: `openai/gpt-image-2`, **no custom style**, content-first prompts (subject · structure · view · what must be readable · what each reference supplies · "plain background, no letters"). AI image-to-video only as gentle motion on a checked real photo, never for a mechanism, an event or a person; disclosed ([[Publish]]).
- **Scientific fidelity beats creativity:** a schematic shows the established model and only what the research note supports; "schematic" marked when simplified; unsourced elements removed; real diagrams are references, never redrawn by an image model.
- **No bare backdrops (Immersive plates):** a figure or card sits on what it is about, never on an empty gradient (the builder refuses `blank`); legacy `contain` stills need `"bg": "blur"` or an inset.
- **Lanes (9:16)** and **mute test**: subject upper, captions at 50 %, one support element lower, bottom 25 % and right 12 % left to the interface ([[Style]]); every beat reads with the sound off.
- **Beat sheet (P4a), one row per plate:** scene · `at` word · medium and source · what the viewer sees happen · events on which words · text on screen.

## 4. On-screen text

- **Purpose of each text:** a label names a part and lands on its word (1 to 4 words, ≤ 2 at once) · a figure is a comparison with unit and source · a context card frames and sources (title a statement ≤ 26 characters, detail ≤ 40) · a margin note gives a voice (≤ 2 per video). Cards are rare: the conclusion, the closing question, a claim no picture carries.
- **Specificity test:** could this text appear unchanged in a video about another topic? Rewrite it with a name, number, place or mechanism. Banned: "The takeaway", "Key point", "Fun fact", "Why it matters", "In summary" and the words in [[Style]]. Only captions repeat the narration.
- **Symbols:** never write ≈ ≥ ≤ → in a card or callout (the font shows boxes): "about", "or more", "to", "·".
- **Phrase captions on every video [H]** (user, 26 Oct 2026: *"lets test more than one word captions"*; they replace Word-by-word captions for the short test block): 1 to 3 words per caption, ≤ 16 characters, a new caption at punctuation or a silence over 0.3 s; the spoken word is full colour and the others dimmed, so the timing stays word-exact. `System/scripts/captions.py` groups them for both builders. Spelling for the eye in `captions`.
- **No branding inside the video** (no progress bar, mark, series tag, logo).

## 5. Voice and sound

- **Voice:** `inworld/realtime-tts-2`, voice `Dennis`, **one continuous take for the whole script** (`voice.py`): scenes are paragraphs of one request, so prosody never resets and nothing is stitched. `speaking_rate` 1.1 (user, 26 Oct 2026: 1.25 was too fast), `temperature` 0, 48 kHz WAV, one direction at the top: *"[say calmly and warmly, like a curious specialist explaining something to a friend]"*; scene directions only where the tone must change. About 195 to 210 wpm. **Breaks:** ≤ 2, each ≤ 0.3 s. A word the model mispronounces, clips, or that whisper hears as another word, is fixed by rewording and one retake (more needs a reason in Status). **Check the take:** whisper's words equal the script, every silence 0.3 to 0.9 s, none inside a clause. The agent cannot hear: it says so at P7.
- **Sound:** voice first. The builder adds only **the opening bell** the user likes and a soft whoosh in the pause between scenes; nothing under speech (ticks and pings are opt-in, `"events": "full"`). **Music is opt-in** (plan row with source, licence, purpose, approved at P4a): instrumental, calm, 85 to 110 BPM, `lu` 15 LU under the voice and ducked about 9 dB under speech. Sources: **Pixabay by hand, shield-free only** (API has no audio) → Mixkit → YouTube Audio Library → Incompetech (CC BY) → ccMixter (CC BY); credits in `sound/_credits.jsonl`. **Never** BBC/RemArc, CC BY-NC, game rips, unread licences. **BigSoundBank and Freesound are deferred**; no ML-generated sound without approval.
- **Mix and master** (`mix_audio.py` after every render): phone-speaker voice chain, music ducked, then **−14 LUFS integrated, true peak ≤ −1 dBTP**; prints `MIX`.

## 6. Edit (`build_video.py` + `plan.json`, or HyperFrames `hf/build.py`)

- The take is never cut: the builder pads the take (0.30 s before, 0.40 s after, short fades), places it once and ends each scene halfway through the silence before the next; `CHECK=1` verifies lead-in, tail and overlaps. Caption and cue times start where speech starts.
- Speech starts at once (≤ 0.2 s); the hook's visual claim and first caption on frame 1, no title slide; the opening bell and voice-first start stay. 1.2 s tail. Plates start on their `at` word. Fix `LONG PLATE`, `REPEAT` and `MOTION SHARE` before rendering. Motion plates: `SOLO_PROYECTO=1` build first (writes `render/_timeline.json`), `motion.py --sheet`, look, then render.
- Field and builder details: header of `build_video.py`; HyperFrames commands and `check3d.mjs` in [[Workflow]]. Captions timed by `word_timings.py`; `render/<prefix>.srt` written for upload; then `mix_audio.py`.

## 7. Checklist before P7 (the agent runs it and says what it could not check)

- [ ] Hook test passes; first clause inside 2 s on the take; speech ≤ 0.2 s after frame 1; captions from the first word
- [ ] Every beat shows its verb (usefulness, swap); named tool shown running; bridge visuals; no AI cliché; every sheet and `look` was looked at; no key or personal data
- [ ] **Slideshow-risk score** (adapted from OpenMontage's pre-render check, github.com/calesthio/OpenMontage): on the contact sheet ([[Workflow]] Commands) score 0 to 2 each: repetition (same layout on 4 or more tiles in a row), decoration, weak motion, text doing the picture's job, no real thing on screen, a world that never changes state. Any 2, or a total ≥ 4, means rework the plates before P7; the score goes in Status
- [ ] No bare gradient plate; `MOTION SHARE` ≥ 60 %; no `REPEAT`, `WARN` or `OVERLAP`, or each explained in Status
- [ ] Theme line, ≤ 3 facts, concrete ending; every figure sourced; every AI claim with model, version, date; no in-video branding
- [ ] Audio: one take; whisper heard the script; no silence over 0.9 s or inside a clause; `MIX` at −14 LUFS (±1), true peak ≤ −1 dBTP
- [ ] **Not verified, said out loud:** how the voice sounds, caption timing against speech, sound levels, pace in motion. P7 belongs to the user.
