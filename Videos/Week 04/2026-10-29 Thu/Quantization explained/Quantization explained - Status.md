---
type: status
updated: 2026-10-30
---

# Quantization explained: Status

**Verdict (user, 30 Oct 2026):** *"mark them as shipped so you stop asking but do nothing else"* → **shipped**, not uploaded; the upload is a separate step.

**Ask once (user, 29 Oct 2026, verbatim):** angle "Agent at work: 8B on a laptop (Recommended)" · medium "Run + hairline + anatomy + captures". Request: *"New short: Quantization explained"*.

| Stage | State |
| --- | --- |
| **Idea** | Agent at work (last video How AI works). Real thing: Qwen3 8B (Q4_K_M, 5.2 GB) run with Ollama on this 10 GB laptop, 29 Oct 2026. Claim: rounding each weight to about 4 bits makes a 16 GB model a 5 GB file; one scale per block keeps it close; the cost is small at 4 bits and large at 2. Demand: not measured (no YouTube key in `.env`). Hooks in [[Script - Quantization explained]]. |
| **Script** | 174 words, 7 scenes, turn at 67 %; 1 recorded run, 2 sources captured. |
| **Spend** | take `5cawz1esa9rmr0d1h4e9d8k9t0` (1,005 chars, about $0.025); WhisperX `azwgemj3m1rnc0d1h4es51r1v4` (about $0.005). Total about $0.03, cap $0.50. The local run costs nothing. |
| **Build** | Recorded run (real terminal lines, trimmed) in w1, w4, w5, w7; Anatomy `ram-stick` (new: `load`, `bits`, `bad`, `ok`) in w2, w5; Hairline `quantize` (new custom: pointer height = bits; 16, 4, 2-bit) in w3, w4, w6; captures Ollama sizes (w5), llama.cpp PR #1684 table (w6). Transitions push, whip, cut, blur, dip (2 cuts of 6); shot sizes wide, medium, close (the scale block). `check3d`: left are TEXT OVER PICTURE against the Hairline host box (frames read clear). Frame audit: 3 rounds plus the render sheet. Render `qnt-53s-9x16-r1.mp4` 52.7 s; `MIX` −14.0 LUFS, −1.5 dBTP; `LISTEN` PASS; masters `-yt` 2160x3840, `-tt` 1080x1920; thumbnail; pack `upload/qnt-publish-pack.md`. |
| **Review** | ship (user, 29 Oct 2026, asked-once round of the AI-therapist Short: "Ship") |
| **Publish** | not uploaded |
| **Numbers** | |

## Not verified

The run's speed (0.78 tokens/s) was measured with RAM and swap full; a free machine would be faster, not re-run. Whisper heard "Qwen3" as "QN3" and "Q four K M" as "Q4KM": fixed by hand in the words file. Quality score against [[Format]] §4: frame 0 pass (claim and the real terminal); real over drawn pass (a real run on this machine); weakest: the 16 to 4-bit change in w3 is subtle (the 2-bit snap in w6 is the clear one), and the terminal beats (w4, w5) hold a panel for about 3 s with one highlight. Not checked: how the voice and effects sound, the pace in motion.

## Feedback
