---
type: video-idea
status: published
series: How AI works
score: 16
publish: 2026-10-31
video: "[[Lottery ticket - Status]]"
hook_type: number
case: "Frankle and Carbin, The Lottery Ticket Hypothesis, ICLR 2019 (arXiv 1803.03635 v5)"
created: 2026-10-31
updated: 2026-10-31
tags: [youtube, pipeline]
---

# Lottery ticket

← [[Pipeline]] · [[Strategy]] §The idea passes

**Claim:** you can delete 90 % of a neural network and it still works, because a small winning ticket inside does the learning, but only from its original starting numbers.

**Real thing:** Frankle and Carbin (MIT CSAIL), ICLR 2019, arXiv 1803.03635: over 90 % pruning, tickets under 10 to 20 % of the size, 38 % earlier at 21.1 % kept, 2.51x faster than the reinitialized copy.

**Y · X:** to understand why big networks can be shrunk · the starting numbers, not the shape, make the ticket win.

**Demand:** 255,073 (17.8x), 1,357 (6.6x), 985 (6.4x), 316 (7.5x), 612 (4.9x), `youtube_search.py` 31 Oct 2026.

**Showable:** the `ticket-board` Anatomy figure (36 tickets, prune, rewind, new random numbers) and crops of the paper.

**Hooks:** 1. "Delete ninety percent of a neural network. It still works." 2. "The same weights, reshuffled, and the network falls apart." 3. "A network holds a smaller network that wins by luck of its start."
