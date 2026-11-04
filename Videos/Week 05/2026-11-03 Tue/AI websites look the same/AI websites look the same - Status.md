---
type: status
updated: 2026-11-03
---

# AI websites look the same: Status

**Ask once (user, 3 Nov 2026, verbatim):** angle "5 sites, 1 design (Recommended)" · real run "Claude Code headless (Recommended)". Request: *"1"* (pick 1 of the /short-idea table). After the key outage: *"updated .env test now"* (4 Nov 2026).

| Stage | State |
| --- | --- |
| **Idea** | Agent at work (last video How AI works). `surprising-result`. Real thing: our runs, Claude Opus 5.5 in Claude Code 2.1.318, 3 Nov 2026: five briefs, one page (5 of 5 "See how it works"); impeccable 4.8.0 on the same five prompts gives five different pages. Demand: Coding with Lewis "Every AI Startup Website Looks the Same" 458,642 (9.3x); autocomplete "ai website design". `youtube_search.py` (4 Nov 2026): 5 outliers on the exact question, best 12.4x. Idea note [[Why every AI website looks the same]], score 19. |
| **Pre-flight** | 1. `surprising-result`; Lewis 9.3x. 2. Field: Lewis "Every AI Startup Website Looks the Same", "The AI Model Iceberg", "3 GitHub repos with 150,000 stars…", "WTF is going on at GitHub?", "The End of Programming"; ours is the only one with a test, a reason and a measured fix. 3. Hook "Claude Code built me five websites. They're the same website."; stake "A notes app, a budget app, a fitness band…"; 0 s the five-hero grid, 3 s the notes hero full width, 6 s the budget hero. 4. Weakest beat: scene 3 (token talk after a visual hook; 16 words, chips must move fast). 5. Prediction: above median (650 engaged at 7 d against 585.5). |
| **Script** | 167 words, 7 scenes, turn at 52 %; sources checked 3 Nov 2026 ([[Script - AI websites look the same]]). |
| **Spend** | cap $2.00. Runs on the user's Claude plan (claude.ai auth), $0 billed. Voice take `f0fcrkcmh5rmw0d1mn1sper5j4` (1,028 chars, about $0.026); incredibly-fast-whisper `jd8r7v79cxrmy0d1mn1rf4hm2g` (about $0.01). Total about $0.04; r2 adds about $0.034 (total about $0.07). |
| **Build** | r2 (main medium capture): before/after full-width pairs (notes, budget, fitness), the grid swap, the bare grid and real button crops, `tokens`, `probs` (our run counts, labelled), README and GitHub crops, the swap again on the payoff. `hf/gen_beats.py` writes `hf/beats.json` (`rev` 2). `qa.py` 8 of 8 PASS on `render/aw-54s-9x16-r2.mp4` (54.4 s; −14.1 LUFS, −1.3 dBTP; PACE PASS, one composition warning, 5.7 s from 39.1 s). Masters `-yt` 2160x3840, `-tt` 1080x1920; thumbnail BEFORE / AFTER (notes page over its skill version); pack `upload/aw-publish-pack.md` (dry run). r1 kept: `render/aw-55s-9x16-r1.mp4`. Kit fix (r1): `qa.py` sound row read `LISTEN PASS`, which `listen.py` no longer prints; it now reads the exit code. |
| **Review** | r1: fix (user, 4 Nov 2026, see Feedback). r2 waiting for the verdict (revision 1 of 2). |

## Not verified

The bars are counts from five runs, not token odds. The skill pages were judged by eye and by computed styles, five a side. Scene 7's advice was not run. Whisper heard "Claude" as "cloud" once (caption fixed by hand). Quality against [[Picture]] §Bar (0 good, 2 bad): frame 0 0, empty frame 1 (scene 3 and the turn's end are text over plain paper for about 2 s each), slideshow 0, text doing the picture's job 1 ("the look changed, the sameness didn't" and "give it a direction" are type only), no real thing 0, static 0, same as last video 0; total 2 for r1; r2: empty frame 1 (the turn's opening line, 32.4 to 35.8 s, over plain paper), text doing the picture's job 0, the rest 0: total 1. Not checked: how the voice and effects sound, the motion in playback.

## Feedback

- **r1 (user, 4 Nov 2026, verbatim):** *"Start from the before/after of the issue, then go for the explanation and finally a generalm conclussion mentioning tools and the importance of taste. from 0:43 to 0:47 is the most beautiful part, you could add the before and after on full screen for each one at the start as you narrate. redo it from this angle"* → r2: script rewritten (152 words), take v2 `yvsz3kw2xxrmt0d1mwwsecyavr` (963 chars, about $0.024), whisper `s6ytpa7369rmt0d1mwwt9qjre4` (about $0.01).
