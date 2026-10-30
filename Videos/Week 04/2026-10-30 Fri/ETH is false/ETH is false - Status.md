---
type: status
updated: 2026-10-30
---

# ETH is false: Status

**Ask once (user, 30 Oct 2026, verbatim):** pending "Ship both (Recommended)" · angle "claim + review, but be sure people not familiarized with the problem can understand it" · medium "Hairline + captures but make sure captures are readable on the short speed and format. also consider anatomy". Request: *"new short: read this and explain it to the world https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf"*.

| Stage | State |
| --- | --- |
| **Idea** | What's coming (last video Agent at work). Real thing: OpenAI, *The Exponential Time Hypothesis is False*, 67-page preprint dated 25 Oct 2026 (17 Oct, revised 25 Oct), openai/math, by "an unnamed internal OpenAI model"; Lean statement `exact_count_and_sat`. Claim: the paper claims k-SAT can be counted in subexponential time, which would refute ETH; it is unverified, and ETH's authors are reviewing it. Demand: not measured (no YouTube key in `.env`); wide press coverage 26 to 28 Oct 2026. Hooks in [[Script - ETH is false]]. |
| **Script** | 170 words, 9 scenes, turn at 62 %; paper, README, Lean statement and reference captured; review via press (1 outlet quotes the letter). |
| **Spend** | total about $0.03; take `k8f75x6rnnrmy0d1hvvv69r3mm` (1,104 chars, about $0.028); WhisperX `v3rcjda5m1rne0d1hvwanp73ag` (about $0.005); cap $0.50. |
| **Build** | Anatomy `switchboard` (new: `s0`..`s7`, `more`, `r0`..`r2`) in w2, w3; Hairline `doubling` (new custom: doubling columns, value 1 adds the claim row, shape only) in w4, w6, w7; real captures cropped two or three words a row from the paper (title, abstract, p. 2 limit, [IP01]) and the README, on `K.sheet` (new in `hfkit`: warns under 80 px a row); the Lean statement as a code panel. Transitions push, cut, whip, blur, dip (2 cuts of 8). Lint 0 errors; `check3d` OVERLAPS 0; frame audit 4 rounds (first pass: captures too small, two figures never shown, a sheet pushed off by a zoom; all fixed) plus the master sheet. Render `eth-58s-9x16-r1.mp4` 58.1 s; `MIX` −14.0 LUFS, −1.3 dBTP; `LISTEN` PASS; masters `-yt` 2160x3840 7.8 Mb/s, `-tt` 1080x1920; thumbnail; pack `upload/eth-publish-pack.md`. |
| **Review** | review |
| **Publish** | not uploaded |
| **Numbers** | |

## Not verified

The proof itself (not checked; nobody outside OpenAI has confirmed it as of 30 Oct 2026, per press). The reviewers' open letter is seen only through press (XenoSpectrum quotes it; others report the group). The doubling and claim rows are a drawing of the shape, labelled not to scale. Whisper split "OpenAI" and misspelled the names: fixed in the words file. Quality score against [[Format]] §4 (0 good, 2 bad): frame 0 0 (claim + the real title), empty frame 1 (about 1 s at 32 s while the claim row starts as stubs; the lower stage under the title sheets), slideshow 0, text doing the picture's job 1 (w5, w8 are sheets and lines), no real thing 0, static 0, same as last video 0 (new figures, What's coming); total 2. Not checked: how the voice and effects sound, the pace in motion.

## Feedback

- 30 Oct 2026: "make sure captures are readable on the short speed and format" → [[Look]] §Components, *Readable capture*.
