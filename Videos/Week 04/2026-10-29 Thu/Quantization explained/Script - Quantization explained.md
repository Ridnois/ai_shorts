---
type: script
updated: 2026-10-29
series: Agent at work
words: 174
---

# Script: Quantization explained

Status: [[Quantization explained - Status]] · rules: [[Format]] §3 · idea: [[Quantization explained]]

## Research (29 Oct 2026)

1. **Recorded run** on this laptop, 29 Oct 2026 16:08 (-03): `free -h` 10 GiB total, 3.0 GiB available; `ollama show qwen3:8b`: 8.2B parameters, quantization Q4_K_M; `ollama list`: 5.2 GB; `ollama run qwen3:8b --verbose`: answered after 13 min 11 s, 602 tokens at **0.78 tokens/s** (RAM full, swap full: a browser and other apps open; the model ignored `/no_think` and reasoned at length). Its own answer said "4 bits per parameter instead of 32 or 64" (the usual baseline is 16; not shown). Log: `Media/…/run/run1.txt`.
2. Memory arithmetic: 8.2B weights x 2 bytes = 16.4 GB at 16 bits; 5.2 GB x 8 / 8.2B = about 5.1 bits per weight for the file (Q4_K_M keeps some tensors at 6 bits).
3. llama.cpp PR #1684 *k-quants* (ikawrakow, opened 3 Jun 2023, merged 5 Jun 2023): Q4_K = "super-blocks containing 8 blocks, each block having 32 weights", scales and mins in 6 bits, 4.5 bpw; Q4_K_M uses Q6_K for half of some tensors. 7B (LLaMA) wikitext perplexity: F16 5.9066, Q4_K_M 5.9601 (+0.9 %), Q2_K 6.7764 (+14.7 %). (captured)
4. Ollama library, qwen3, read 29 Oct 2026: qwen3:8b 5.2 GB. (captured)

**Not verified:** how fast the same run is with free RAM (not re-run: the user's apps stay open); the perplexity numbers are LLaMA 7B, not Qwen3 8B.

## Package

- **Promise:** how an 8B model fits a 10 GB laptop, and what the rounding costs.
- **Titles:** **Quantization Explained: How an 8B AI Model Fits on a Laptop** ← · What Q4_K_M Means (Before You Download a Model) · 4-Bit AI Models Explained in 50 Seconds
- **Frame 0:** 8B MODEL / 10 GB LAPTOP over the real `ollama show` output. **Thumbnail:** the RAM stick, 16 GB → 5 GB.
- **Hooks:** contradiction ← "This laptop has ten gigabytes of memory, and it just ran an eight billion parameter AI model." · number "Sixteen gigabytes of model in a five gigabyte file." · fact "Every weight in this model can only be one of sixteen values."

## Scenes

| # | Beat | Voice (as read) | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | hook | This laptop has ten gigabytes of memory, and it just ran an eight billion parameter AI model. | 17 | real terminal: `free -h` 10Gi, `ollama show` 8.2B | run |
| 2 | stake | At sixteen bits a weight, that model needs about sixteen gigabytes. It shouldn't fit. The trick is quantization. | 18 | Anatomy `ram-stick`: 16-bit blocks overflow, red | arithmetic |
| 3 | mechanism | Every weight is a number. Quantization rounds it to four bits, so it can only land on one of sixteen levels. | 21 | Hairline `quantize`: pins snap to 16 rails | k-quants |
| 4 | mechanism 2 | Each block of thirty-two weights keeps its own scale, so the levels sit where those weights are. The file's tag, Q four K M, works out to about five bits per weight. | 32 | close on a block and its scale; the real tag in `ollama show` | k-quants, run |
| 5 | run | So Qwen three, with eight billion weights, is a five point two gigabyte file, and it answered. With a browser open, it ran under one token a second, but it ran. | 31 | the stick at 4-bit: fits, green; real Ollama size table; real `--verbose` stats 0.78 tokens/s | run, Ollama |
| 6 | turn (67 %) | But rounding has a price. On a seven billion model, llama dot c p p measured how well it predicts text. Four bits cost about one percent. Two bits cost fifteen. | 29 | real PR table; `quantize` at 2-bit, gaps visible; +1 % / +15 % | k-quants |
| 7 | payoff, loop | So read the tag before you download. Q four K M is the sweet spot. It's the only reason this laptop can do it. | 22 | the tag; frame 0's terminal; comment prompt | |

Words: 174 (51.3 s take; the count includes the spelled tag). Turn at 67 %. Loop: "...this laptop can do it. This laptop has ten gigabytes..." In `plan.json`, `texts` carry digits and tags as whisper heard them; `spoken` holds the text read.
