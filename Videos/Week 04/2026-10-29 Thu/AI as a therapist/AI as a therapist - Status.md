---
type: status
updated: 2026-10-30
---

# AI as a therapist: Status

**Verdict (user, 30 Oct 2026):** *"mark them as shipped so you stop asking but do nothing else"* → **shipped**, not uploaded; the upload is a separate step.

**Ask once (user, 29 Oct 2026, verbatim):** angle "Works, but a yes-man (Recommended)" · medium "Captures + Anatomy figure". Request: *"new short: AI as psychologist, does it really work? is it a yesman? where do we draw the line?"*.

| Stage | State |
| --- | --- |
| **Idea** | How AI works (last video Agent at work). Real things: Dartmouth's Therabot trial (NEJM AI, 27 Mar 2025, −51 % depression symptoms); Stanford's bridge test (Moore et al., 25 Apr 2025; models inappropriate ≥ 20 % of the time, therapists 93 % right); OpenAI's GPT-4o rollback (29 Apr 2025). Claim: an AI therapist can work when built and watched by clinicians; a general chatbot tuned on ratings drifts into a yes-man. Demand: not measured (no YouTube key in `.env`). Hooks in [[Script - AI as a therapist]]. |
| **Script** | 169 words as read, 9 scenes, turn at 51 %; 5 sources, 4 captured. |
| **Spend** | take `ktj6jgafk1rmr0d1h699qka30g` (1,118 chars, about $0.028); incredibly-fast-whisper `c55gp0xcfhrmy0d1h699bz8rvg` sat in `starting` 10 min, cancelled (no charge expected); WhisperX `ka6b639hnhrnc0d1h6easkd1x0` (about $0.005). Total about $0.03, cap $0.50. |
| **Build** | Anatomy `rater` (new, `System/anatomy/rater/`: `feed`, `up`, `down`, `tune`, `ok`, `bad`; built by a sub-agent, previews read) in w2, w3, w4, w9; real captures in w1, w2, w5, w6, w7, w9 (Dartmouth news, OpenAI post, the Stanford paper's Fig. 3 and Fig. 4). Transitions push, whip, cut, dip, blur (2 cuts of 8); shot sizes wide, medium (the figure), close (the dial, the 51 % line, the stimulus line). `hyperframes check` 0 errors; craft flag on `NEJM AI` label is false (on screen 4.3 to 7.6 s, read on frame 5.77). `check3d`: only 1 sample in the push transition at 54.38 s. Frame audit: 3 rounds plus the render sheet; fixed the figure not popping in (w3, w4, w9), the empty prompt panel, misplaced boxes, the caption GPT-4-0 (now GPT-4O). Render `therapy-60s-9x16-r1.mp4` 59.6 s; `MIX` −14.1 LUFS, −1.4 dBTP; `LISTEN` PASS; masters `-yt` 2160x3840 (8.1 Mb/s), `-tt` 1080x1920; thumbnail; pack `upload/therapy-publish-pack.md`. |
| **Review** | ship (user, 30 Oct 2026, asked-once round of the ETH Short: "Ship both (Recommended)") |
| **Publish** | not uploaded |
| **Numbers** | |

## Not verified

The NEJM AI paper itself (403 to scripted fetch); Therabot's training data is described from secondary coverage (Psychiatric News, ScienceDaily). The voice paraphrases nothing from the Stanford prompt: it reads the paper's stimulus verbatim. Topic touches suicide: the description carries a crisis line (988 in the US) and the video names no method beyond the paper's own published example.

Quality score against [[Format]] §4: frame 0 pass (claim and the real page); real over drawn pass; mechanism drawn (the rater dial); weakest: the captures are small text; w8 is tags only (no picture); 59.6 s sits at the 60 s ceiling; the YouTube master came out at 8.1 Mb/s, under the 35 to 60 the note expects (flat frames). Not checked: how the voice and effects sound, the pace in motion.

## Feedback
