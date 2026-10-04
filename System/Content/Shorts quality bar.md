---
type: research
created: 2026-10-04
updated: 2026-10-04
status: v1 · from the Magnetar feedback ("create top tier quality youtube shorts") · craft rules are working hypotheses until the channel has Analytics data
tags: [research, youtube, shorts, retention, captions, quality]
---

# Shorts quality bar

← [[YouTube Channel]] · [[Guidelines for new scripts]] · [[Narration guide]] · [[On-screen text style]] · [[Channel strategy]] · [[Channel playbook]]

> **User feedback (Magnetar, 4 Oct 2026):** *"narrative oriented too much on storytelling, this could be something you need to know after 3 seconds"*, *"add transcriptions… word by word so users can follow the narrative with the audio off"*, *"the style of the added text is good and appealing, keep improving the render guidelines"*, *"create top tier quality youtube shorts."* This note is the bar a Short must clear before P7. Status of the evidence: the platform facts are sourced (§7); the craft rules below are **working hypotheses from common Shorts practice and this channel's feedback, not measured here**. The first Analytics data replaces them ([[Channel strategy]] §6).

## 1. The first 3 seconds

1. **A need-to-know claim, not a story.** Scene 1 is ≤ 10 words; its first clause (≈ 7 words) is spoken inside 3 s. A specific, true statement that makes the next sentence necessary ("Some wires carry electricity with zero resistance. Not low. Zero."). Banned openers: a date and a scene ("In May 2025, a line stopped…"), "Imagine…", "Have you ever…", any greeting.
2. **Speech starts at once.** Intro silence ≤ 0.2 s (`start` in `plan.json`); no logo, no title card before the voice.
3. **The strongest real image is on screen from frame 1**, and the **caption of the first word is on screen with it**.
4. **The hook is a claim you can check.** If it cannot be sourced it cannot open the video ([[Idea and hook quality]] §3).

## 2. Explain, do not narrate

- The voice teaches: one mechanism per scene, cause then effect ("because", "so"). **No storyteller register** (scene-setting, suspense, dramatic pauses). The channel voice is the curious specialist ([[Channel identity]]), who *tells you what you need to know*.
- Every scene answers a question the previous one opened. A scene that only decorates is cut.
- The close hands the viewer one idea to finish alone; if it can echo the hook, the last plate is the first plate again (the video then loops without a seam).

## 3. Captions (word by word)

| Element | Rule |
| --- | --- |
| What | **One word at a time**, centred, in the order spoken; the word changes on the voice, not on a fixed beat. The script's own spelling is shown ("1,232" stays a figure) |
| Look | Noto Sans Display Bold, 104 px, capitals, white with a dark outline and a soft shadow; **words that contain a digit are copper** (the channel accent), and so are up to six key terms listed in `plan.json` `keywords` |
| Place | centred at **16.5 % from the bottom** (`CAP_Y` in the builder): above the Shorts interface, below the card zone; cards and callouts never enter it |
| Timing | from `voice/<take>.words.json` (whisper word timestamps, `System/scripts/word_timings.py`); estimated by characters and punctuation when the file is missing (a reasonable fallback, not exact) |
| Hold | a word stays until the next one starts, but never across a pause longer than 0.55 s |
| Check | read the word list in the render log, and look at stills at the start of three scenes; **timing against the real voice is not verified by the agent** (it cannot hear) |

## 4. Visual rhythm

- A new image, card or callout at least every **≈ 4 to 6 s**; with fewer than that, a scene must carry callouts that arrive one after another. A held photo with nothing changing for more than 8 s is a defect.
- **Real photos for real things, faithful schematics for hidden things** ([[Illustration pipeline]] §1, rule 2.13); **never an empty gradient with text** (rule 2.14).
- One card per plate, one number per video, ≤ 2 margin notes ([[On-screen text style]]).
- The text style (copper bar card, callouts) is the channel's recognisable look; keep it identical across videos, vary only the gradient palette of the topic.

## 5. Sound

Voice only today. **Open item:** a quiet music bed and tasteful transitions could add dynamism (user, Brazil feedback); test one source with approval at P4 ([[Guidelines for new scripts]] §6). Never sound effects "because Shorts have them".

## 6. Checklist before P7 (the agent runs it and says what it could not check)

- [ ] Scene 1 ≤ 10 words, first clause inside 3 s, no scene-setting; speech starts ≤ 0.2 s after frame 1.
- [ ] Captions on from the first word; `CAPTIONS n words` printed; stills show no overlap with cards or callouts.
- [ ] Every plate has a usefulness sentence; every generated plate was checked element by element against the research note.
- [ ] No plate is a bare gradient; no callout or card sits in the caption zone.
- [ ] A visual change at least every ≈ 6 s (list the plate durations).
- [ ] Every figure on screen has a source on a card or in the description.
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
