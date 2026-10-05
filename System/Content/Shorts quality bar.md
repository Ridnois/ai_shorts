---
type: research
created: 2026-10-04
updated: 2026-10-04
status: v2 · plain-words hook, engaging through-line, smaller captions, faster images (Superconductors feedback, 4 Oct 2026); v1 from the Magnetar feedback ("create top tier quality youtube shorts") · craft rules are working hypotheses until the channel has Analytics data
tags: [research, youtube, shorts, retention, captions, quality]
---

# Shorts quality bar

← [[YouTube Channel]] · [[Guidelines for new scripts]] · [[Narration guide]] · [[On-screen text style]] · [[Channel strategy]] · [[Channel playbook]]

> **User feedback (Magnetar, 4 Oct 2026):** *"narrative oriented too much on storytelling, this could be something you need to know after 3 seconds"*, *"add transcriptions… word by word so users can follow the narrative with the audio off"*, *"the style of the added text is good and appealing, keep improving the render guidelines"*, *"create top tier quality youtube shorts."* This note is the bar a Short must clear before P7. Status of the evidence: the platform facts are sourced (§7); the craft rules below are **working hypotheses from common Shorts practice and this channel's feedback, not measured here**. The first Analytics data replaces them ([[Channel strategy]] §6).

## 1. The first 3 seconds

1. **A need-to-know claim, in plain words, not a story.** The first sentence needs **no defined term** ("Some wires waste no electricity. Almost nobody can use them.", not "zero resistance": rated 2 of 5). Scene 1 is ≤ 10 words; its first clause (≈ 7 words) is spoken inside 3 s. A specific, true statement that makes the next sentence necessary ("Some wires carry electricity with zero resistance. Not low. Zero."). Banned openers: a date and a scene ("In May 2025, a line stopped…"), "Imagine…", "Have you ever…", any greeting.
2. **Speech starts at once.** Intro silence ≤ 0.2 s (`start` in `plan.json`); no logo, no title card before the voice.
3. **The strongest real image is on screen from frame 1**, and the **caption of the first word is on screen with it**.
4. **The hook is a claim you can check.** If it cannot be sourced it cannot open the video ([[Idea and hook quality]] §3).

## 2. Explain, do not narrate

- The voice teaches: one mechanism per scene, cause then effect ("because", "so"). **No storyteller register** (scene-setting, suspense, dramatic pauses). The channel voice is the curious specialist ([[Channel identity]]), who *tells you what you need to know*.
- Every scene answers a question the previous one opened. A scene that only decorates is cut.
- The close hands the viewer one idea to finish alone; if it can echo the hook, the last plate is the first plate again (the video then loops without a seam).

**Make it engaging (Superconductors feedback, 3 scores of 2 out of 5 on idea, script and hook; *"I got lost on the facts and forgot the theme"*).** Explaining is not listing:

- **One theme line** in plain words, stated early; **every scene opens with a bridge** back to it ("so", "that is why", "and here is the catch"); the close answers it with **a concrete payoff** ([[Guidelines for new scripts]] §0.9, §1.10).
- **Fact budget:** ≤ 5 facts, ≤ 3 spoken figures; each fact followed by what it changes.
- **Cut test and compaction:** delete each sentence in turn; whatever the video does not miss stays deleted (§1.11).
- **Passion is stakes and specificity, not volume:** a delivery note per scene, varied sentence length, ≤ 1 rhetorical question.

## 3. Captions (word by word)

| Element | Rule |
| --- | --- |
| What | **One word at a time**, centred, in the order spoken; the word changes on the voice, not on a fixed beat. The script's own spelling is shown ("1,232" stays a figure) |
| Look | Noto Sans Display Bold, **88 px** (was 104; feedback: *"font could be a little bit smaller"*; layout otherwise rated 5 of 5), capitals, white with a dark outline and a soft shadow; **words that contain a digit are copper** (the channel accent), and so are up to six key terms listed in `plan.json` `keywords` |
| Place | centred at **the middle of the frame, 50 % of the height** (`CAP_Y` in the builder). User feedback, 5 Oct 2026: *"the youtube shorts ui overlaps the captions, redesign the layout… captions should go more on the center"*: the old position (16.5 % from the bottom) sat under the channel name, title and sound ticker. Cards sit below them (66 % from the top), callout labels above; cards and callouts never enter the caption zone |
| Timing | from `voice/<take>.words.json` (whisper word timestamps, `System/scripts/word_timings.py`); estimated by characters and punctuation when the file is missing (a reasonable fallback, not exact) |
| Hold | a word stays until the next one starts, but never across a pause longer than 0.55 s |
| Check | read the word list in the render log, and look at stills at the start of three scenes; **timing against the real voice is not verified by the agent** (it cannot hear) |

## 4. Visual rhythm

- **A new image every ≈ 3 to 4 s; any plate over 5 s is a defect** (the builder prints `LONG PLATE`). User: *"add more reference images, so it changes faster"* and editing rated 3: *"could be a little more dynamic"*. Pushes alternate in and out at 8 %, cross-fades are 0.2 s. The same photo may return with a different crop. Callouts and cards add change inside a plate but do not replace new images.
- **Real photos for real things, faithful schematics for hidden things** ([[Illustration pipeline]] §1, rule 2.13); **never an empty gradient with text** (rule 2.14).
- One card per plate, one number per video, ≤ 2 margin notes ([[On-screen text style]]).
- The text style (copper bar card, callouts) is the channel's recognisable look; keep it identical across videos, vary only the gradient palette of the topic.

## 5. Sound

Every Short has the **synthesized sound design** (whoosh on scene cuts, ticks on plates and callouts, a ping on cards, an opening thump, a very quiet drone; [[Blender editing]] §Sound design): each cue marks a change the eye is about to see, nothing else. Any extra recording or music comes from **free licensed libraries** (YouTube Audio Library, Sonniss, Pixabay, Incompetech; BigSoundBank and Freesound deferred), as a row of the visual plan, with approval and credits ([[Guidelines for new scripts]] §3). Never sound effects "because Shorts have them"; each one has a purpose.

## 6. Checklist before P7 (the agent runs it and says what it could not check)

- [ ] Scene 1 ≤ 10 words, first clause inside 3 s, no scene-setting; speech starts ≤ 0.2 s after frame 1.
- [ ] Captions on from the first word; `CAPTIONS n words` printed; stills show no overlap with cards or callouts.
- [ ] Every plate has a usefulness sentence; every generated plate was checked element by element against the research note.
- [ ] No plate is a bare gradient; no callout or card sits in the caption zone.
- [ ] A new image every ≈ 3 to 4 s, none over 5 s (the build prints the durations and `LONG PLATE`).
- [ ] First sentence in plain words; theme line stated and bridged by every scene; facts ≤ 5; concrete ending.
- [ ] Every figure on screen has a source on a card or in the description.
- [ ] **No branding inside the video** (no progress bar, no mark, no series tag).
- [ ] Description: sources, date, AI disclosure ([[Channel strategy]] §3).
- [ ] **Not verified by the agent, said out loud:** how the voice sounds, whether the captions land on the spoken words, pace and transitions in motion.

## 7. Platform facts this note relies on (fetched 4 Oct 2026)

| Fact | Source |
| --- | --- |
| Since 31 March 2025 a Shorts view counts every start or replay with no minimum watch time; **engaged views** is the measure monetization uses | YouTube Help, Shorts views (fetched 4 Oct 2026) |
| Shorts can be up to 3 minutes (announced Sept 2024) | Wikipedia, *YouTube Shorts* |
| Shorts reached over 100 billion views a day (Nov 2025) | Wikipedia, *YouTube Shorts* |
| Shorts creators receive 45 % of the Shorts ad revenue pool (regular videos 55 %) | Wikipedia, *YouTube Shorts* |
| Education content tends to do better in regular videos than in Shorts | Wikipedia, *YouTube Shorts* (a summary of reports; weak): a reason for [[Channel strategy]] §4 to pair Shorts with long videos |
