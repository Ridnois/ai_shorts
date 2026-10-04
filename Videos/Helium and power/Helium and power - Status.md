---
type: research
created: 2026-10-03
updated: 2026-10-03
status: render r1 done (71.9 s) · awaiting your review (P7) · narrated in Spanish
tags: [research, youtube, status, helium]
---

# Helium and power · status

← [[YouTube Channel]] · [[Production process]]

Second video of the channel, the first to follow the full [[Production process]]. It reached gate P4 with text only. After the user's approval **only the stage 5 test** was generated (3 predictions). The rest awaited P5. **Narration and on-screen text are in Spanish** (made before the English-only decision of 3 Oct 2026); this note was translated afterwards.

## Stage log

| Stage | Status | Approved | Note |
| --- | --- | --- | --- |
| 0 Idea | ✅ | 3 Oct 2026 · implicit | Request: "a script on the tensions around helium". The user answered "lets do it" to the full package from P1 to P4 |
| 1 Research | ✅ | 3 Oct 2026 · implicit | [[Research - Helium]]: 24 claims: 4 with a single source or doubtful dates (not used or qualified) and 1 discarded. **Re-check Hormuz and Ras Laffan before recording** |
| 2 Script | 🔁 reopened | ⏳ P3 | The user asked for **70 s** (3 Oct 2026): [[Script - Helium (70 seconds)]], 176 words, ≈ 70 s. The 2-minute text was approved; the cut needs new approval. The P3 read-aloud is still unconfirmed |
| 3 Direction | ✅ | 3 Oct 2026 · implicit | Shots in the technical-sketch visual style (withdrawn) |
| 4 Prompts and budget | ✅ | **3 Oct 2026** | Decisions: voice B (younger and brisker), cross-faded images with no video model; the length went from 258 words to 176 (70 s). Budget: 26 base prompts, unchanged |
| 5 Tests | ✅ | **3 Oct 2026** · "images and audio ok, proceed" | Scene 1 voice (profile B) and image shot 1 approved |
| 6 Generation | ✅ | 3 Oct 2026 · **implicit** on asking for the editing | 6 voices (67.8 s of useful voice), 3 sounds, 8 shots × 2 frames and a thumbnail. 32 predictions (23 of image, for 6 retries). Approval was not requested category by category; if any does not convince you, it is redone |
| 7 Editing | ✅ render r1 · ⏳ awaiting P7 | ⏳ | `render/helio-70s-r1.mp4`, **71.9 s**. Detail in [[Script - Helium (70 seconds)]] (*Editing*) and design in [[Transitions and effects]] |
| 8 Publishing | ⏳ not started | — | Thumbnail with title, description with sources and AI disclosure are missing |

## What awaits your decision (P7)

1. **Watch and listen** to `Media/Helio y poder - 70 segundos/render/helio-70s-r1.mp4`. It lasts 71.9 s; to land at 70, "In March its price doubled" (scene 4) is cut.
2. Judge what I could not check: the **balance between the voice and the background sounds**, the timbre of the six voices and the pace.
3. Image deviations worth looking at: 3a (tanks of equal height), 5a (the seal is missing), 5b (a single hand at the end) and 6 (repeated icons).
4. Before publishing: re-check Hormuz and Ras Laffan, add figures on screen and the thumbnail with title.

## Resolved incidents

- **Images from another video appeared in this script.** Obsidian resolves embeds by file name and the two videos shared names (`e1-final-v1.png`…). All of this video's files now carry the `helio-` prefix; the rule is recorded in [[Media convention]].
- **`_canal/` was at the vault root.** It was moved back to `Media/_canal/`, where Git ignores it. **It is still in GitHub's history** (the automatic commit at 05:18 pushed it): removing it from history requires rewriting it and a `push --force`, which I did not do without your permission.
- **Replicate's rate limit:** parallel requests got a 429; they are sent in series.

## Notes

- [[Script - Helium (70 seconds)]]
- [[Research - Helium]]
- Media in `Media/Helio y poder - 70 segundos/` (only on this machine, [[Media convention]]).
