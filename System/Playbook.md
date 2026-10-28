---
type: rules
updated: 2026-10-27
status: v11 · rewritten 27 Oct 2026 for professional-level Shorts: one owner per rule, each a principle plus its test (the dated user quotes behind them live in git); craft standard (camera, transitions with a cause, designed sound), ship discipline, variety guard
---

# Playbook: every rule for a Short

Read it whole before writing. Process and commands: [[Workflow]]. Look, layout, camera, motion and sound kit: [[Design system]]. Brand, persona and words on screen: [[Style]]. Before the click: [[Audience]]. Upload and numbers: [[Publish]]. **[H]** marks a hypothesis the analytics loop keeps or deletes ([[Publish]] §Hypotheses). Target to imitate: [[Model script]].

**Product:** vertical Shorts (1080 × 1920), English, the same master on YouTube and TikTok, **five a week at a fixed time, never two on one day**. Goal: **teach people AI** in three series (How it works, Agent at work, What's coming) as narrated learning worth watching even knowing it is made with AI.

## 0. The bar is the feed

A Short competes in one swipe with the best of the feed, not with our last video. Professional means all five at once:

| Bar | Test |
| --- | --- |
| A named real case carries the concept | the title can name a product, company or person and an outcome |
| The real thing is on screen | a named tool is shown running; real pages, frames and numbers are shown, not drawn |
| The subject fills the frame | it spans 60 to 85 % of the stage width; the stage is never three-quarters empty for over 3 s |
| It moves like film, not slides | the camera moves inside worlds, 3 or more shot sizes, transitions with a cause, an event every 1.5 to 2 s |
| It sounds designed | one continuous take, an effect on every visible action of weight, one payoff hit, −14 LUFS |

## 1. Idea (gate P1; read `Analytics/Report.md` first)

1. **Outcome and mechanism:** Y (the result the viewer wants) and X (the mechanism they did not know blocked it), one line each, one of the three series, after a deep-first search ([[Audience]]).
2. **A named real case carries the concept [H]:** one real, dated case with a named product, company or person and a consequence. It becomes the running example (§2) and the thumbnail's focal image. No real case: reject the idea or bridge it to one ([[Audience]] *Case sources*).
3. **Facts bank:** 15 or more remarkable true facts, each with source and date; a fact about what a model or product can do is 12 months old or less, or dated on screen.
4. **Score** each angle 1 to 5 on surprise, scale, depth, evidence, showable, plain; the thread needs 4 or more on surprise, scale and plain. **Argue against it:** the three strongest reasons a viewer would scroll past; an unanswered one lowers the score.
5. **Street-lamp test:** if a headline answers the central question, go back. **"Borderline" is a fail.** **Expert test:** a specialist would call it "the interesting part". **Coffee test:** the thread in one plain sentence.
6. **Demand check:** search autocomplete for the plain question and the views of 3 comparable Shorts (`youtube_search.py`); no demand for X alone means bridging it to a Y people want.
7. **Five candidate hooks of different types** (surprising fact, surprising number, question, contradiction, stakes); pick with the Hook test (§2).
8. **Original synthesis:** one derived comparison or number per video.
9. **Spread and variety:** two consecutive videos never share a series, a hook picture or a figure set (the inauthentic-content policy punishes interchangeable videos, [[Publish]]). Status records the figure set.

## 2. Script (gate P3)

- **Length in words, never seconds. Short test block [H]:** the next 10 videos are 90 to 140 words (aim 110 to 130, about 35 to 45 s at rate 1.1), 4 to 6 scenes, 3 facts or fewer; every third is a compact 60 to 85 words, 3 to 4 scenes. Never pad. After 10 uploads `analytics.py report` compares them with the old 180 to 235-word cuts.
- **Scene 1 is the hook: a need-to-know claim a stranger understands at once.** The first words are the twist itself, spoken inside 2 s. **Hook test**, all must hold: (1) plain, no term a later scene defines; (2) a reason to care: a consequence, a broken expectation or a stake; (3) an open question the next scene answers; (4) sound-off: the first caption and image raise it; (5) honest; (6) it restates the package's promise; (7) named: the subject in words the viewer knows, never "the idea"; (8) curiosity before explanation: no mechanism or history before the promise. No date opener, "Imagine", "did you know", question opener or story opener.
- **Structure by series [H]:** **How it works:** hook · definition (one plain sentence) · origin (only when it is part of the twist) · "here is how", on one running example (2 to 3 scenes) · the catch · close. **Agent at work:** hook (the result) · the task · the run, step by step · what to copy · close. **What's coming:** hook (the change) · the evidence · the mechanism · the counter-view · close.
- **One running example carries the mechanism:** the real case of §1, worked through start to finish; an abstraction enters only as a mapping from it, said and shown, and the loop closes on it.
- **Theme line:** one plain line stated in scene 1 or 2; scenes bridge back to it only where the logic turns; the close answers it.
- **Connection test:** every sentence answers the question the previous one raised; the script table writes that question per scene. Scenes open on a turn word that says how they connect ("so", "now", "then", "but"), and each sentence names its concrete thing ("each timestamp", "the web page"), never a bare "it" or "each one" whose referent sits in the previous scene.
- **A comparison is a story, never a table:** one learner's task fails; each thing compared fixes one failure of that task, in order; the close hands the viewer a question to diagnose their own case.
- **Explain, do not narrate:** cause and effect joined by "because", "so", "but", never "and then".
- **Low-attention-proof and for the ear:** first sentence 12 words or fewer; sentences of 6 to 16 words, one idea each, active verbs, one rhetorical question at most, no exclamation marks; jargon, version strings and figures go on screen; numbers and acronyms written as spoken ("G P U"). Calm and unhurried.
- **Close = concrete payoff:** one plain sentence that answers the question for something the viewer knows, shown as a card, then **one social question** the viewer can answer, on screen as the comment prompt with two or three answer chips. Never "like and subscribe".
- **Cut test:** delete each sentence in turn; if the video still answers its question, it stays deleted.
- **Rigor:** every figure has source and date; every AI capability claim names model, version and date; forecasts name who made them; models are described by mechanism ("it predicts the likely next word"), never by wants; no hype or doom; the research note lists what was not verified.
- **Pause plan:** pauses follow the sentence's intention and are written into the one take: a new paragraph for a continuing scene (about 0.35 s), a full stop for a new idea (0.35 to 0.6 s), a `beat` or `pauses` of 0.2 to 0.3 s before the payoff (1 or 2 per video, never over 0.9 s in all); never between subject and verb or after "the", "a", "of", "and".
- **Script table columns:** scene · question it answers · voice text · words · delivery · pause · visual beat (what the viewer sees happen) · camera · on-screen text · source.

## 2b. Package (inside the Script note, gate P3)

A **Package** section before the scene table: Y and X · **promise** (one sentence the video must pay) · **3 titles** (100 characters or fewer, one marked) · **thumbnail** (one focal image and 3 to 4 words that complement the title, plus why it beats 3 neighbours in search) · **opening map** (scene 1 = promise, scene 2 = proof and plan). `publish.json` copies these fields; a changed hook re-checks the package ([[Audience]]).

## 3. Visuals (gate P4a: the beat sheet)

- **Show the verb, not the noun.** **Usefulness test:** "the viewer sees ___ happen, so they understand ___". **Swap test:** if any other picture of the same noun would do, cut it.
- **Medium by what the sentence does** (first row that fits):

  | The sentence… | Medium |
  | --- | --- |
  | shows an AI or agent doing a task | a **recorded run** of the real tool, cut on the action |
  | shows a real thing, page or number | the **real capture** (screenshot, frame, footage), a camera move onto the detail |
  | explains a flat hidden process | a **Hairline figure** acting on the word, parts named by callouts, the pipeline rail ([[Design system]]) |
  | gives a number | a **comparison that builds** (a counter runs, a bar grows), never a figure alone |
  | explains depth itself (layers, a space) | **3D**, the exception ([[Design system]] *3D routes*) |

- **Worlds and camera:** 3 to 5 visual worlds and one anchor that returns at the close in a changed state. Each world is a canvas: open wide, push to the part the voice names (on its word), pull back to show the relation. **Three or more shot sizes** per video; the scale change happens through the camera, not a new slide.
- **Transitions with a cause:** worlds change by whip, push, dip, cut or blur, **3 to 5 kinds per video, at most a third hard cuts**, never a crossfade between worlds; the best one enters the next world through an object on screen. `hfkit` warns when this fails.
- **Motion:** arrivals land on a long tail, exits are shorter and accelerate; landed text holds still; no breathing, floating or idle wobble; words stagger 60 to 120 ms; a line the viewer must read holds 0.5 s plus 0.3 s a word.
- **Rhythm:** a visual event every 1.5 to 2 s; nothing unchanged over 3.5 s; 60 % or more of the runtime moving; hold 0.3 to 0.75 s before the payoff, which plays at normal speed.
- **Frame 1 carries the claim:** the hook's picture and first caption are on screen at 0 s (social players show frame 0 as the thumbnail).
- **Illustrate, do not typeset:** every step has a picture that carries it; text names parts (callouts) or frames a claim (one card), never replaces the picture.
- **Parts build in the order they are named;** nothing labelled appears before it is spoken. One focal point: the hero in ember or moving, the rest grey or still; at most 2 callouts at once.
- **Comparisons live on one board:** one table or row of pictures stays on screen across the comparing scenes; each reason adds a row on its word.
- **Recorded runs:** the real tool, large font, tall window, prompt visible before the result, speed-ups marked ("4x"), nothing staged or retyped, no key, email, path or personal data; a product's interface is shown as itself, never imitated.
- **Footage and photos:** PD, CC0, CC BY, CC BY-SA, Pexels or Pixabay, credits logged by `stock_*.py`; no visible brand, burned-in text or identifiable person unless they are the subject.
- **AI clichés are banned:** glowing brains, robots at keyboards, circuit faces, binary rain, chip renders, human-robot handshakes.
- **Generated media: opt-in, 3 or fewer per Short**, content-first prompts, no custom style; AI video only as gentle motion on a checked real photo, disclosed.
- **Scientific fidelity beats creativity:** a schematic shows the established model and only what the research supports, "schematic" noted in Status when simplified.
- **Mute test:** every beat reads with the sound off.
- **Beat sheet, one row per beat:** scene · `at` word · medium and source · what the viewer sees happen · camera (wide, medium, close, move) · transition in · text on screen · sound.

## 4. On-screen text

- **Jobs:** a callout names a part on its word (1 to 4 words, 2 at once at most) · a figure is a comparison with unit and source · a card frames and sources (title 26 characters or fewer, detail 40) · the comment prompt carries the closing question. Cards are rare.
- **Specificity test:** could this text appear unchanged in a video about another topic? Rewrite it with a name, number, place or mechanism. Banned words: [[Style]].
- **Phrase captions on every video [H]:** 1 to 3 words, 16 characters or fewer, spoken word lit, in the caption band (`captions.py`).
- **No branding inside the video** (no logo, mark, series tag or progress bar).

## 5. Voice and sound

- **Voice:** `inworld/realtime-tts-2`, voice `Dennis`, **one continuous take for the whole script** (`voice.py`): scenes are paragraphs of one request, nothing is stitched or cut. `speaking_rate` 1.1, `temperature` 0, 48 kHz WAV, one direction at the top; breaks 2 or fewer, each 0.3 s or less. **Check the take:** whisper's words equal the script; every silence 0.3 to 0.9 s, none inside a clause; a mispronounced word is fixed by rewording and one retake.
- **Effects with a cause** (kit in [[Design system]] *Sound*): a whoosh on a whip, push or fast camera move (rotated takes), a soft click on a callout, a pop on chips, an opening hit, and once per video a riser into the payoff word with a hit on it. Effects sit well under the voice; nothing loud lands on a word.
- **Music is opt-in:** instrumental, calm, licensed (Pixabay by hand, shield-free), credited, approved at P4a; ducked under speech.
- **Mix and master:** `mix_audio.py` after every render: phone-speaker voice chain, **−14 LUFS integrated, true peak −1 dBTP or lower**.

## 6. Build (HyperFrames + `hfkit.py`)

- The take is never cut: `hfkit.Short` places it once (0.15 s lead), cues every event on a heard word and ends each world 0.2 s before the next scene's first word.
- Speech starts within 0.2 s; no title slide; 1.2 s tail.
- Before rendering: `npx hyperframes check` (no errors; read the craft warnings), `check3d.mjs` (`OVERLAPS 0`, every WARN fixed or explained), snapshots at the cue moments looked at.

## 7. Checklist before P7 (the agent runs it and says what it could not check)

- [ ] Hook test passes; first clause inside 2 s; the claim's picture and caption on frame 1
- [ ] Every beat shows its verb; named tool shown running; real captures where real things exist; no AI cliché; no personal data
- [ ] **Slideshow-risk score** on the contact sheet, 0 to 2 each: repetition (the same layout on 4 tiles in a row) · decoration · weak motion · text doing the picture's job · no real thing on screen · a world that never changes state · **one shot size throughout**. Any 2, or a total of 4 or more, means rework before P7; the score goes in Status
- [ ] 3 to 5 transition kinds, at most a third hard cuts; 3 or more shot sizes; no `WARN` left unexplained
- [ ] Theme line, 3 facts or fewer, concrete ending; every figure sourced; every AI claim with model, version and date
- [ ] Audio: one take; whisper heard the script; `MIX` at −14 LUFS (±1), true peak −1 dBTP or lower; effects stem under −1 dBFS
- [ ] Render at CRF 14 or better (`--crf 14`); bitrate printed
- [ ] **Not verified, said out loud:** how the voice and effects sound, caption timing against speech, pace in motion. P7 belongs to the user.

## 8. Ship discipline (P7 and after)

- **The user's verdict is one of three:** *ship* (to P8), *fix* (one list of changes, applied in one revision), *drop* (the lesson goes into the owning rule). A video gets **at most two revisions after r1**; then it ships or drops.
- **Feedback edits the owning rule once** ([[Feedback loop]]) and applies forward: renders already waiting still ship unless the feedback names a defect in them.
- **At most two renders wait at P7 or P8** before a new video starts; a new request while two wait first asks the user to ship, fix or drop them.
