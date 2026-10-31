---
type: status
updated: 2026-10-30
---

# Can AI replace lawyers: Status

**Verdict (user, 30 Oct 2026):** *"mark them as shipped so you stop asking but do nothing else"* → **shipped**, not uploaded; the upload is a separate step.

**Ask once (user, 29 Oct 2026, verbatim):** angle "theme 1 focused on how to solve this issues, we want to discuss the possibility of use ai agents as legal orientation" · medium "use anatomy + hairline + captures, but not that much focus on the example case, if there's something about this topic on the vault, just forget it and write the script unbiased". Request: *"new short: can ai replace lawyers? the complexity of citing the law the right way"*.

| Stage | State |
| --- | --- |
| **Idea** | How AI works (last video What's coming). Real things: Charlotin's database (2,231 decisions, 28 Oct 2026); Free Law Project's citation lookup API (16 Apr 2024); Stanford/Yale study (17 to 33 %, 2024); SRA's Garfield.Law approval (6 May 2025). Claim: a citation is a pattern, so a model can write a perfect fake; an AI legal guide is safe only when every citation is looked up and a person answers for it. Demand: not measured (no YouTube key in `.env`). Hooks in [[Script - Can AI replace lawyers]]. Written fresh, without the vault's earlier video on invented sources (the user's instruction). |
| **Script** | 168 words, 7 scenes, turn at 55 %; 4 sources captured. |
| **Spend** | take `ap70eb36v5rmt0d1gstt6463y0` (1,021 chars, about $0.026); WhisperX `503wczya5srnc0d1gstvz6n88w` (about $0.005). Total about $0.03, cap $0.50. |
| **Build** | Anatomy `citator` (new, `System/anatomy/citator/`: `feed`, `search`, `found`, `ok`, `bad`) in w4, w5, w7; Hairline `loop` (w2) and `temperature` (w3; `riffle` did not answer the pointer, swapped); real captures in w1, w2, w4, w5, w6, w7 (Charlotin, Free Law Project, arXiv, SRA). Transitions push, whip, cut, dip, blur (2 cuts of 6); shot sizes wide, medium, close (stamp, the 17 to 33 % line). `hyperframes check` 0 errors. `check3d`: left are TEXT OVER PICTURE against figure host boxes during zooms (frames read clear). Frame audit: 3 rounds of snapshots plus the render sheet. Render `law-53s-9x16-r1.mp4` 53.1 s; `MIX` −14.0 LUFS, −1.5 dBTP; `LISTEN` PASS; masters `-yt` 2160x3840, `-tt` 1080x1920; thumbnail; pack `upload/law-publish-pack.md`. |
| **Review** | ship (user, 29 Oct 2026, asked-once round of the AI-therapist Short: "Ship") |
| **Publish** | not uploaded |
| **Numbers** | |

## Not verified

Whisper added "Thank you." in the silence after the last word (51.39 s to the end); removed from the words file. The SRA page was captured from its HTML with the cookie banner hidden (its web font did not load; the text is the page's own). Quality score against [[Format]] §4: frame 0 pass (claim and the real database); real over drawn pass; the mechanism is drawn (code panel, `temperature`, `citator`); weakest: the w1 and w2 captures are small text, and the lower stage is empty for about 3 s in w1 and in the SRA beat; the dip into w5 darkens the citator for 0.1 s. Not checked: how the voice and effects sound, the pace in motion.

## Feedback
