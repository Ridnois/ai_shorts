---
type: script
updated: 2026-10-31
series: How AI works
words: 147
---

# Script: Lottery ticket

Status: [[Lottery ticket - Status]] · rules: [[Story]] §Beats

## Research (31 Oct 2026)

Every number below is read in the paper itself (arXiv 1803.03635 v5, PDF captured), not in a video or a summary.

1. **Paper:** Jonathan Frankle and Michael Carbin (both MIT CSAIL), *The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks*, ICLR 2019 (arXiv v1 9 Mar 2018, v5 4 Mar 2019).
2. **Abstract:** "Neural network pruning techniques can reduce the parameter counts of trained networks by over 90% ... without compromising accuracy." The hypothesis: "dense, randomly-initialized, feed-forward networks contain subnetworks (winning tickets) that, when trained in isolation, reach test accuracy comparable to the original network in a similar number of iterations"; "winning tickets that are less than 10-20% of the size of several fully-connected and convolutional feed-forward architectures for MNIST and CIFAR10".
3. **Method (the video's three steps):** train the network; prune the smallest-magnitude weights ("we identify a winning ticket by training a network and pruning its smallest-magnitude weights"); "Reset the remaining parameters to their values in θ0". Iterative pruning repeats this over rounds, each pruning a fraction of the survivors (20 % per round in the Lenet runs).
4. **Lenet-300-100 on MNIST** (handwritten digits): 266 K weights (Figure 2). A winning ticket keeping 21.1 % of the weights stops early "38% earlier than for the original network"; accuracy improves by more than 0.3 points at 13.5 % and "return[s] to the level of the original network when Pm = 3.6%" (so about 96 % of the weights can go).
5. **Random reinitialization** (same mask, new random starting values): "initialization is crucial"; the reinitialized copies "learn progressively slower"; at Pm = 21 % "the winning ticket reaches minimum validation loss 2.51x faster than when reinitialized and is half a percentage point more accurate".

**Not verified / limits:** all results are on small networks (Lenet on MNIST, small convolutional networks on CIFAR10), not language models; I did not run the method myself. "Learned 38 % sooner" is the paper's early-stopping iteration (its proxy for how fast a network learns). The ticket is found by training the full network first, which the voice implies ("training, then pruning, finds the lucky one") but does not dwell on. The 36-ticket board and the dial are a schematic of the method, not a measurement; the video says so on screen ("drawn with 36 tickets") and in the voice ("drawn as a tiny network of thirty-six weights"). Four survivors of 36 is 89 % removed, drawn as the paper's "over 90 %".

## Package

- **Promise:** a network can lose 90 % of its weights and keep working, because a small winning ticket inside does the learning, and only if it keeps its original starting numbers.
- **Titles:** **Delete 90% of a Neural Network? The Lottery Ticket Hypothesis** ← (60 chars) · How Pruning Works: Why a Neural Network Needs Only 10% · The Lottery Ticket Hypothesis in 50 Seconds
- **Frame 0:** DELETE 90% over the full board of trained tickets. **Thumbnail:** the board with four lit survivors, "DELETE 90%".
- **Hooks (3, different types):** number ← "Delete ninety percent of a neural network. It still works." · contradiction "The same weights, reshuffled, and the network falls apart." · mechanism "A network holds a smaller network that wins by luck of its start."

## Scenes

| # | Beat | Voice (as read) | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | hook | Delete ninety percent of a neural network. It still works. | 10 | `ticket-board`: 36 trained tickets; 32 drop through the board; four lit survivors; the dial stays high | 2 |
| 2 | stake | In a 2019 paper, Frankle and Carbin tried it on a network with 266,000 weights, reading handwritten digits. Keep just 21%. And it finished learning 38% sooner. | 27 | the paper's title block; FRANKLE + CARBIN; the board; 21 of 100 tiles lit; two bars (100 vs 62) with the paper's "38% earlier" | 1, 4 |
| 3 | mechanism | Here's their method, drawn as a tiny network of 36 weights. First, train it. Second, delete the weakest, a little at a time. Third, rewind the survivors to the exact numbers they started with, and train again. | 38 | chips deepen; tickets fall one by one; the reel spins and the survivors' chips go back to light blue (the paper's "Reset the remaining"); they deepen again | 3 |
| 4 | result | The few left, a winning ticket. Learn as well as the whole network. | 13 | the lit survivors, the dial high; the paper's "test accuracy comparable" | 2 |
| 5 | turn (61 %) | But give those same survivors brand new random starting numbers, and it falls apart. At 21%, the real ticket learned two and a half times faster than its reshuffled copy. | 32 | the same four turn red, the needle sags; two bars, 40 vs 100, with the paper's "2.51x faster" | 5 |
| 6 | payoff, loop | So the shape doesn't win. The starting numbers do. A big network holds many small ones. And training, then pruning, finds the lucky one. That's why you can delete the rest. | 31 | the full board returns with four lit; it trains, then the rest drop away; ends on DELETE 90% | 2, 3 |

Words: 147 (48.8 s take, 50.6 s video). Turn ("But") at 61 %. Loop: "…That's why you can delete the rest. Delete 90% of a neural network. It still works."

## Self-test

- [x] 147 words (130 to 170); counted from `plan.json`.
- [x] Hook 10 words, says "neural network", no banned opener; frame-0 text (DELETE 90%) and picture (the board, then its tickets dropping) say the same thing.
- [x] Stake by 10 s: 266,000 weights at 7.5 s, 21 % and 38 % by 14 s (the hook already carries "ninety percent").
- [x] Worked case first: a 36-ticket board is trained, pruned and rewound on screen before the paper's numbers return (the 2.5x and the 21 %).
- [x] Turn ("But") at 61 %; re-hooks at 3.5 s (the paper), 15 s (their method), 19 s (train), 23 s (rewind), 27.6 s (winning ticket), 31 s (but), 40 s (the start wins).
- [x] Payoff the viewer can repeat; the last sentence read into the first plays as one.
- [x] Ear: sentences of 4 to 17 words; numbers as spoken; no exclamation marks; no banned words.
- [x] Cut test, sentences deleted while drafting: "Pruning is not new" (the abstract's baseline, not needed), the Conv-6 / CIFAR10 numbers, "the ticket needs the big network to be found" (kept only as "training, then pruning").
- [x] Every number has a picture (90 → tiles dropping, 21 → 21 of 100 tiles, 38 → a 62 % bar, 36 → 36 tickets, 2.5x → a 40 % bar against 100 %); the "but" is the dip and the red chips; one word acted out: "delete" (the tickets fall).
- [x] Sources: rows 1 to 5; the voice says "Frankle and Carbin", the screen shows their names and MIT CSAIL.
