---
type: video-idea
status: idea
series: How AI works
hook_pattern: surprising-result
medium: primitive
score: 16
publish: 
video: 
created: 2026-11-04
updated: 2026-11-04
tags: [youtube, pipeline]
---

# AI fixed another AI's brain

← [[Pipeline]] · [[Strategy]] §The idea passes

**Claim** (one line a stranger would say "wait, why?" to): an AI read another AI's raw numbers, found the one direction that made it loop forever, deleted it, and its maths score went from 8 % to 48 %.

**Real thing** (named product, company, person or incident, dated, with its source): Takehi, Teoh, Zhang and Khattab (MIT CSAIL), "Weight-space programming" (rikiyat.github.io/blog/weight-space-programming, 2 Nov 2026, read 4 Nov 2026; HN 2,934 points). Astra traced Qwen3.5-0.8B's looping to one direction written by the MLPs in layers 15 and 19 and removed it from 131,072 weights (0.016 %): MATH-500 7.9 % → 48.1 %, hitting the token limit 93.0 % → 33.1 % (50 passes). Turn: on Gemma 3 270M, which does not loop, nothing improved: "Editing weights could remove an obstacle that hid an ability, but it could not add an ability the model lacked." Also: it named the game a network played (4 of 4) from weights alone. Check at P1 which Astra (the post's model name and maker) and that the HN reading of "steering/ablation, a known technique" is fair.

**Y · X** (the result the viewer wants · the mechanism in the way): to understand what "weights" are · a model is numbers; a behaviour can be one direction in those numbers, and removing it is subtraction, not training.

**Hook pattern** (an id from [[Strategy]] §Hooks) and why people click it: `surprising-result`; AI repairing AI, with a before/after number.

**Demand** (rows from [[Radar]] or `youtube_search.py`: link, views, ratio; or the autocomplete): `youtube_search.py "can ai read neural network weights" --short --min-ratio 3` (4 Nov 2026): htHNuhdZX28 870 (3.6x); wkZRSQmaPnc 148 (9.2x, tiny channel). Signal: HN 2,934 points, the week's top AI thread. Demand is thin: a lead.

**Own fit** (how our videos of this series and pattern did, from [[Report]]): How AI works 631 (n=7) and surprising-result 702.5 (n=4), above our median.

**Showable** (the medium of the mechanism, [[Picture]] §Medium, the one real run or model output, and the spine): `matrix` of weights with one direction lit and subtracted; `tokens` looping ("so so so…") then stopping; the post's real table as a marked crop. A local run of Qwen3.5-0.8B looping is possible (check size and licence).

**Score** demand 2 · own fit 5 · showable 4 · real thing 5 = 16 / 20

**Hooks** (3, different patterns):

1. surprising-result: An AI deleted 0.016 % of another AI. Its maths score went up six times.
2. limit-mystery: The fix only worked on the model that was broken.
3. name-it: This is weight-space programming: AI editing AI by hand.
