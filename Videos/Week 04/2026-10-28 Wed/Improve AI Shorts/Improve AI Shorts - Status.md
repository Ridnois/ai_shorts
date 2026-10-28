---
type: status
updated: 2026-10-28
---

# Improve AI Shorts: Status

**Clarify (user, 28 Oct 2026, verbatim answers):** queue "Proceed, queue is your call (Recommended)" · angle "Toolchain tour" · delegation "Delegate A to D, stop at P7 (Recommended)" · visuals "Real runs + Hairline callouts (Recommended)". Request: *"improve the vault and generate a new short: How to improve your ai youtube shorts, skills and tools to make delightful videos"*, earshot named as an example tool.

**Delegation:** P1 to P7 by the agent, cap $0.06 (base $0.05); stop at the render.

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Beat sheet | done | 28 Oct 2026 (delegation) | Agent at work; hook type contradiction; theme line "an agent improves only what it can measure"; street-lamp pass; demand check not run |
| 4 Captures, budget | done | 28 Oct 2026 (delegation) | `.env` copied from `../youtube_vault` (gitignored); budget $0.03, cap $0.06; `Media/Week 04/2026-10-28 Wed/Improve AI Shorts/` created from scratch (no earlier `hf/` on this machine) |
| 5 Generation | blocked at word timings | | voice take v1 `wr1hb00anhrmt0d1ghzvhysq9c` (744 characters, about $0.02, 36.8 s). `listen.py` on the raw take: −23.9 LUFS, true peak −5.4 dBTP, 13 silences of 0.31 to 0.58 s, FAIL on loudness (the real fail for scene 5). Whisper on Replicate stayed in `starting`: `gdhzr2tw05rmw0d1ghzs3h3r1w` (about 20 min, cancelled) and the one retry `gz58kwg3bhrmw0d1gj8ak5zvrr` (10+ min, still starting). HyperFrames' local `transcribe` needs a Whisper or Parakeet install the user has not approved |
| 6 to 9 | not started | | needs `ias-take-v1.words.json`; then `hf/build.py` (written from scratch with hfkit), check, render, `mix_audio.py`, `listen.py` |

## Vault changes

`System/scripts/listen.py` (ears: LUFS, true peak, silences, clipping, exit 1 on a miss; tested on a synthetic clip with known gaps), Playbook §5 and §7, Workflow §Commands, one invariant. earshot is recorded as optional: its install was refused by the permission classifier, so the user installs it.

## Not verified

How the voice and effects sound; earshot's behaviour (never run here; its numbers are the author's); `listen.py` on a real render.
