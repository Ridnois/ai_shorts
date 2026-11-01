---
type: status
updated: 2026-10-31
---

# Lottery ticket: Status

**Verdict (user, 31 Oct 2026):** *"ship it publicly"* → **shipped** (r1), public.

**Ask once (user, 31 Oct 2026, verbatim):** angle "Delete 90% and it still works (Recommended)" · medium "New Anatomy 'ticket drum' + paper crops". Request: *"Upload the video, and go for 5"* (idea 5 of the five How AI works suggestions: *Can you delete 90% of a neural network?*).

| Stage | State |
| --- | --- |
| **Idea** | How AI works (last video What's coming). Real thing: Frankle and Carbin (MIT CSAIL), *The Lottery Ticket Hypothesis*, ICLR 2019, arXiv 1803.03635 v5 (4 Mar 2019). Claim: a trained network can lose over 90 % of its weights and keep its accuracy, because a small winning ticket inside does the learning, but only from its original starting numbers. Demand (`youtube_search.py`, 31 Oct 2026): calculusphile 255,073 (17.8x), The ml guy 1,357 (6.6x), The Junior Engineer 985 (6.4x), Cyril Imhof 316 (7.5x), Habesha AI 612 (4.9x). Hooks in [[Script - Lottery ticket]]. |
| **Script** | 147 words, 6 scenes, turn at 61 %; the paper's PDF read and captured 31 Oct 2026 (abstract, method, 38 % earlier, 2.51x faster, 266K weights). |
| **Spend** | take `e7g876jym1rmr0d1jfy80n1ss0` (1,019 chars, about $0.025), WhisperX `cpdvat5bzsrna0d1jfyb3fp50c` (about $0.005). Total about $0.03, cap $0.50. WhisperX heard "Frankle" and "Carbin" wrongly; the two words are corrected in the timings file. |
| **Build** | **r1** (31 Oct 2026): new Anatomy figure `ticket-board` (36 tickets in a pegboard with a chip for each number; the weakest drop through the board; a tape reel rewinds the survivors to their starting colour; red chips for new random numbers; yellow rims for the winning ticket; an accuracy dial; params `train`, `prune`, `rewind`, `again`, `fresh`, `lit`, `acc`) in every world; phrase crops of the paper (title block, "test accuracy comparable", "Reset the remaining", "38% earlier", "2.51x faster"); a 10 by 10 tile grid with 21 lit (21 % of every 100 weights); two bar pictures for 38 % sooner and 2.5x faster. `line ends: 0` and a clean console on the figure; one bug found and fixed on the way (a clamp applied before a divide kept the pruned tickets on the board). Transitions whip, push, blur, dip, whip; shot sizes wide, medium, close. Lint 0 errors; `check3d` OVERLAPS 0 except one single-sample interface-strip note (the w2 headline arriving); frame audit 7 rounds. Render `lth-51s-9x16-r1.mp4` 50.6 s; `MIX` −14.0 LUFS, −1.6 dBTP; `LISTEN` PASS; `PACE` PASS; masters `-yt` 2160x3840 15.7 Mb/s, `-tt` 1080x1920 4.7 Mb/s; thumbnail; pack `upload/lth-publish-pack.md` (`publish.py --dry-run`, private). |
| **Review** | ship (user, 31 Oct 2026: "ship it publicly") |
| **Publish** | uploaded public 31 Oct 2026 ([`TH-zkTN8HR0`](https://youtu.be/TH-zkTN8HR0)), thumbnail confirmed; row in `Analytics/videos.csv`; one `check_vault` fix on the way: the csv hook now reads as the script's scene 1 ("ninety percent") |
| **Numbers** | |

## Not verified

All results are the paper's, on small networks (Lenet-300-100 on MNIST, small convolutional networks on CIFAR10), not language models; I did not run the method myself. The 36-ticket board and the dial are a schematic of the method, not a measurement; four of 36 is 89 % removed, drawn as the paper's "over 90 %"; the dial's sag under new random numbers is a schematic of "no longer match the performance". "Finished learning 38 % sooner" is the paper's early-stopping iteration (its proxy for learning speed), for iterative pruning at Pm = 21.1 %. The 2.51x is also at Pm = 21 %. The ticket is found by training the full network first. Later research on the hypothesis was not read. Quality score against [[Format]] §4 (0 good, 2 bad): frame 0 0, empty frame 1 (the lower third of the w3 to w6 frames under the board is bare paper), slideshow 0, text doing the picture's job 1 (w2 and w5 lean on captures and bars), no real thing 0, static 0, same as last video 0 (new figure, new series); total 2. Not checked: how the voice and effects sound, the pace in motion (`pace.py` measures that the picture moves, not why), how the 4K master looks on YouTube.

## Feedback
