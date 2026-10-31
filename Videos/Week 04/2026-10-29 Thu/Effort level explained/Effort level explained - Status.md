---
type: status
updated: 2026-10-30
---

# Effort level explained: Status

**Verdict (user, 30 Oct 2026):** *"mark them as shipped so you stop asking but do nothing else"* → **shipped**, not uploaded; the upload is a separate step.

**Ask once (user, 29 Oct 2026, verbatim):** angle "Same task, low vs max (Recommended)" · medium "Run + Anatomy figure + captures" · runs spend "Yes, run them (Recommended)". Request: *"new short: Effort level explained, is it higher better?"*.

| Stage | State |
| --- | --- |
| **Idea** | Agent at work (last video How AI works). Real thing: Claude Opus 5.5 (`claude-opus-5-5`) run with `claude -p --effort low` and `--effort max`, no tools, 29 Oct 2026, 21 recorded runs (`Media/…/run/`). Claim: effort sets how many tokens Claude spends, not how clever it is; on easy questions low and max agree, max pays more; on a hard one low can stop short, max finishes at 7x the tokens of low's good try. Demand: not measured (no YouTube key in `.env`). Hooks in [[Script - Effort level explained]]. |
| **Script** | 167 words, 7 scenes, turn at 56 %; 16 runs, Anthropic effort docs captured. |
| **Spend** | take `1sfv6ejsghrmy0d1h93v768xc8` (1,029 chars, about $0.026); incredibly-fast-whisper `kgzv4tdac5rmr0d1h93rsm4c7g` canceled in `starting`; WhisperX `agye6j19phrna0d1h98tsjfyb8` (about $0.005). Total about $0.03, cap $0.50. Runs: 21 on the user's Claude plan (notional API cost in the JSONs, about $1.0, mostly cached system prompt and the max run's $0.46). |
| **Build** | Anatomy `effort-meter` (new: `effort`, `think`, `out`, `ok`, `bad`) in w1, w3, w5, w6, w7; recorded runs as terminal panels (real JSON values, trimmed) in w2, w4, w5; Anthropic docs captures (header, levels table) in w2, w3, w7. Transitions whip, push, cut, dip, blur (1 cut of 6); shot sizes wide, medium (cage, card), close (knob). `hfkit` fix: anatomy SVG ids scoped per mount (a shared clip id hid the answer card in every world after w1). Lint 0 errors; `check3d` OVERLAPS 0; frame audit 3 rounds plus the master sheet. Render `eff-54s-9x16-r1.mp4` 54.3 s; `MIX` −14.0 LUFS, −1.2 dBTP; `LISTEN` PASS; masters `-yt` 2160x3840 8.2 Mb/s (last video 7.2: the flat look), `-tt` 1080x1920; thumbnail; pack `upload/eff-publish-pack.md`. |
| **Review** | ship (user, 30 Oct 2026, asked-once round of the ETH Short: "Ship both (Recommended)") |
| **Publish** | not uploaded |
| **Numbers** | |

## Not verified

A handful of runs, one max try on the hard question: an illustration, not a benchmark (said in the caveats). The low failures were tool calls written with tools off under Claude Code's system prompt; via the bare API low may behave differently. Opus 5.5's medium default is from the API docs; Claude Code's own default for it was not checked. Whisper heard "seating" as "seeding" and added a stray "The" at 0.03 s: fixed in the words file. Quality score against [[Format]] §4 (0 good, 2 bad): frame 0 0 (claim + full meter), empty frame 1 (w4 panel half empty for 2 s before its rows land; w7 lower third after the prompt), slideshow 0, text doing the picture's job 1 (w4 is a terminal + big lines), no real thing 0, static 0, same as last video 0 (new figure, new medium mix); total 2. Not checked: how the voice and effects sound, the pace in motion.

## Feedback
