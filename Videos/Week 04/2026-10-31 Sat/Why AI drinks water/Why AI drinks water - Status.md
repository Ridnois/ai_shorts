---
type: status
updated: 2026-10-31
---

# Why AI drinks water: Status

**Verdict (user, 31 Oct 2026):** *"Perfect,ship it"* → **shipped** (r1). Upload by hand from the pack (not uploaded by the agent).

**Ask once (user, 31 Oct 2026, verbatim):** angle "Heat becomes steam (Recommended)" · medium "Anatomy cooling tower + report captures (Recommended)". Request: `/short Why AI drinks water` (idea picked from the 5 listed that day).

| Stage | State |
| --- | --- |
| **Idea** | What's coming (last video Agent at work). Real thing: Google, *Measuring the environmental impact of AI inference* (21 Aug 2025: median Gemini Apps text prompt 0.26 mL, about five drops) and the Google 2025 Environmental Report (2024 data: about 8.1 billion gallons consumed across its data centers and offices, 54 golf courses; evaporation counts as consumed; air cooling planned in Mesa, Arizona). Claim: one answer costs five drops because cooling towers turn chip heat into vapor, and Google chooses water on purpose because it saves electricity. Demand (`youtube_search.py`, 31 Oct 2026): Captured Secrets 409,934 (302.9x), Qube 57,366 (903.4x), Really No Really Podcast 36,562 (11.0x), CarterPCs 23,966,881 (7.9x). Hooks in [[Script - Why AI drinks water]]. |
| **Script** | 149 words, 6 scenes, turn at 63 %; the blog post and the 120-page report PDF read and captured 31 Oct 2026. The first search disagreed with the report (7.2, 10.5, 10.9 B gallons): the video uses only figures read at the source. |
| **Spend** | take `x0aehammm1rmr0d1jer9vra5jw` (931 chars, about $0.023), WhisperX `4hx1177dfdrnc0d1jets0564xm` (about $0.005); `incredibly-fast-whisper` `mf2263qjynrmt0d1jerbqg9xtg` sat in `starting` for 5 min and was cancelled (nothing charged). Total about $0.03, cap $0.50. |
| **Build** | **r1** (31 Oct 2026): new Anatomy figure `cooling-tower` (server block with a heat sink, warm and cool channels with beads, tower with fan and vapor puffs, five drop lamps, a power dial; params `heat`, `flow`, `evap`, `rise`, `fan`, `drops`, `power`; its fan, puffs and beads run on the page clock) in every world; phrase crops of Google's post, the report PDF and Google's data-centers page in w2, w4, w5; 54 counted golf tiles (w2). `line ends: 0` and a clean console on the figure. Transitions whip, push, blur, dip, whip (no cuts); shot sizes wide, medium, close (zooms shifted down so the drawing stays under the headline). Lint 0 errors; `check3d` OVERLAPS 0 except two single-sample interface-strip notes (w5 and w6 headlines arriving, accepted as in the Rust video); frame audit 6 rounds. Render `wtr-50s-9x16-r1.mp4` 49.8 s; `MIX` −14.0 LUFS, −1.6 dBTP; `LISTEN` PASS; `PACE` PASS (no still of 1.5 s or more); masters `-yt` 2160x3840 16.2 Mb/s, `-tt` 1080x1920 4.9 Mb/s; thumbnail; pack `upload/wtr-publish-pack.md` (`publish.py --dry-run`, private). |
| **Review** | ship (user, 31 Oct 2026: "Perfect,ship it") |
| **Publish** | pack ready; the user uploads by hand |
| **Numbers** | |

## Not verified

The five drops are Google's estimate for Gemini Apps (one product, Aug 2025) from a fleet-average water figure, not a measurement and not ChatGPT's. The 8.1 billion gallons is all of Google's own data centers and offices in 2024, not only AI (the voice says so); the freshwater part is 7.2 B. "Vapor never comes back, so Google counts it as consumed" applies the report's definition (withdrawal minus discharge); the report does not say it in those words. The dial's rise under air cooling is a schematic of Google's statement that water cooling saves energy compared with air, not a measurement. The 2026 environmental report (2025 data) was not read. The first search results for the water numbers were wrong or mixed (news summaries); only the report PDF figures are used. Quality score against [[Format]] §4 (0 good, 2 bad): frame 0 0, empty frame 1 (the w2 capture beat at 4 to 5.5 s leaves the lower third bare), slideshow 0, text doing the picture's job 1 (w2 and w4 are captures and headlines), no real thing 0, static 0, same as last video 0 (new figure, new series); total 2. Not checked: how the voice and effects sound (WhisperX heard the script exactly), the pace in motion (`pace.py` measures that the picture moves, not why), how the 4K master looks on YouTube.

## Feedback
