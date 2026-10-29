---
type: status
updated: 2026-10-28
---

# Helium and AI chips: Status

**Clarify (user, 28 Oct 2026, verbatim answers):** angle "How it works: why a chip can't be made without it (Recommended)" · delegation "Delegated to the render, stop at P7 (Recommended)" · ship rule "Yes, a one-off test exception (Recommended)" · visuals "Anatomy Figure of the wafer chuck, plus real captures (Recommended)". Request: *"modify the vault to use the anatomy skill https://cellcog.ai/blog/anatomy-claude-skill/ and test it on a new short: why helium is important on the ai race"*.

**Delegation:** P1 to P7 by the agent, base about $0.04 (take about $0.02, timing about $0.01), cap $0.10; stop at the render. Exception to the two-renders-waiting rule, for this test only (about eleven renders wait). First video on the Anatomy medium.

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Beat sheet | done | 28 Oct 2026 (delegation) | How it works; real case Qatar helium offline 2 Mar 2026; hook type surprising fact; theme line "AI chips are made on helium they never show"; street-lamp pass; demand check not run; facts bank 18 (see Script); figure set Anatomy `wafer-chuck`, bars, counters, USGS capture |
| 4 Captures, budget | done | 28 Oct 2026 (delegation) | real capture: USGS *Mineral Commodity Summaries 2026*, helium, page 2 (Qatar 63 of 190), cropped from the published PDF; budget base about $0.04, cap $0.10 |
| 5 Generation | done | 28 Oct 2026 | take v1 `8h2dr22dndrmw0d1gmkre1aba0` (782 characters, about $0.02, 39.2 s); word timings: `incredibly-fast-whisper` stayed in `starting` for 11 min (cancelled, nothing run), WhisperX `w2f1hbp0nhrn80d1gmrvf2nez8` answered at once, 125 words; total about $0.03 of the $0.10 cap |
| 6 Build | done | 28 Oct 2026 | Anatomy `wafer-chuck` (Figure tier, about 60 parts, schematic: 2 mm a unit, no true gap size; the cooling shown is a qualitative model); skill line check `line ends: 0 of 385`; `hyperframes check` no errors (accepted structure warnings); `check3d` OVERLAPS 1 sample (the 19.5 s caption of the bars board touches x 950 for one frame on its entrance); transitions push, whip, dip, blur, cut (1 hard cut of 5); shot sizes wide, medium, close (camera moves in w1, w2, w3, w5, w6); slideshow-risk score 1 (repetition 1: the chuck is on 4 of 6 worlds, kept as the anchor); render `he-41s-9x16-r1.mp4` (40.6 s, re-rendered once before P7 after the user's fitting note), CRF 14, about 4.0 Mbps; `MIX` -13.9 LUFS, true peak -1.5 dBTP; `LISTEN` PASS (9 silences 0.34 to 0.44 s); thumbnail built |
| 7 Verdict · 8 Publish · 9 Measure | P7 open | | waiting for the user: ship, fix or drop |

## Not verified

How the voice and effects sound; caption timing against speech; pace in motion. I read contact sheets, not the whole video. Claims taken at second hand: Korea 64.7 % (KITA via Korea Herald), Reuters stock of 4 to 6 months (one unnamed supplier source), IDTechEx "no viable alternatives" (via a summary). The Qatar shutdown date is 2 Mar (28 Feb is the war). No source says helium is the reason an AI chip, HBM or GPU package was delayed: the script does not claim it; the video's honest limit is that it shows the mechanism and the supply exposure, not an output cut. The wafer in the figure is a schematic: no real heat model, and the dies, pins and ducts are illustrative. The Anatomy skill's audit (`--audit`) was not run: the figure has no pipes or round bodies built with its tube and lathe kit. Not tested: the figure in a light theme or at 4x zoom beyond the video's camera.

## Feedback

User, 28 Oct 2026, on the last frame: *"check this mistake and improve overall fitting"* (the comment prompt's third chip, "suppliers", ran past the panel's border and the panel covered the bottom of the chuck). Fixed before P7: chips shortened to fabs, states, suppliers; every figure host moved inside x 20 to 960 and, in the closing world, above the deck (y 190 to 863). Rule edit: [[Design system]] *Anatomy figures* (placement) and `hfkit.ask` (warns when chips are wider than the panel).
