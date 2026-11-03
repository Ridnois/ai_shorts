---
type: status
updated: 2026-11-03
---

# AI attention explained: Status

**Ask once (user, 3 Nov 2026, verbatim):** angle "It resolves 'it' by weighing every word (Recommended)" · medium "Real attention weights + new Anatomy figure (Recommended)". Request: *"how AI attention works"*. After the probe showed no clean flip: turn "Keep the trophy case, turn = weights aren't the explanation (Recommended)".

| Stage | State |
| --- | --- |
| **Idea** | How AI works (last video Agent at work). Real thing: BERT (`bert-base-uncased`, 2018) attention on a trophy/suitcase pair, run 3 Nov 2026; Vaswani et al. 2017; Jain and Wallace 2019. Claim: a model scores every word against every other, and those scores barely move when the answer flips, so attention shows where it looked, not why. Demand (`youtube_search.py`, 3 Nov 2026): "How AI knows what 'it' means" 1,094 (20.8x), "Attention Mechanism Explained in 2 Minutes" 3,581 (27.1x), "Self-Attention Explained: How Does an LLM Know What 'It' Means?" 449 (3.1x). Hooks in [[Script - AI attention explained]]. |
| **Script** | 163 words, 7 scenes, turn at about 60 %; sources checked 3 Nov 2026 (arXiv abstracts fetched). |
| **Spend** | take `0xfg9mkvbhrmw0d1mce84wf7ec` (1,008 chars, about $0.025); incredibly-fast-whisper `8sm4tnfy05rmt0d1mcea4ss0rr` (about $0.01). Total about $0.035, cap $0.50. BERT run local, $0. |
| **Build** | new Anatomy `attention-desk` (15 channel strips, sliders at the real weights, bus bar; params `levels`, `mix`, `swap`, `tint`, `tints`, `lit`, `sink`; line check `line ends: 0`) in w1 to w5 and w7; crops of the arXiv page of Jain and Wallace (w6); recorded BERT weights (`Media/…/run/attention.json`). Transitions push, whip, cut, dip, blur, cut (2 of 6); shot sizes wide, medium, close (zooms on trophy, end marker, bus). Lint 0 errors; `check3d` OVERLAPS 0 (one 0.4 s nudge of the w6 line into the right strip, accepted); frame audit 3 rounds; the first render lost the w6 sheet (a `flash` hid it), fixed in r3. Render `att-50s-9x16-r3.mp4` 50.3 s; `MIX` −14.0 LUFS, −1.3 dBTP; `LISTEN` PASS; `PACE` PASS (r1 failed on two w6 stills, fixed with events); masters `-yt` 2160x3840 19.0 Mb/s, `-tt` 1080x1920; thumbnail; pack `upload/att-publish-pack.md`. |
| **Review** | waiting for the user's verdict (ship, fix or drop) |

## Not verified

BERT is an encoder, ChatGPT a decoder; no ChatGPT weights are public. One sentence pair, one model, weights averaged over 144 heads. Whether BERT resolves "it" was not tested. Whisper heard "BERT" as "bird": the caption word was fixed by hand, and how the voice says BERT was not heard. Quality score against [[Format]] §4 (0 good, 2 bad): frame 0 0 (claim + desk), empty frame 1 (the lower stage under the desk stays plain paper at wide shots), slideshow 0, text doing the picture's job 0, no real thing 0 (real run, real paper), static 0 (`PACE` PASS), same as last video 0 (new figure); total 1. Stake beat is thin (the question carries it). Not checked: how the voice and effects sound, the pace in motion, the zooms in motion.

## Feedback
