---
type: status
updated: 2026-10-28
---

# Vault pipeline: Status

**Clarify (user, 27 Oct 2026, verbatim answers):** toolchain "HyperFrames only (Recommended)" · old videos "Prune superseded (Recommended)" · upgrades "Camera on one canvas, Official HyperFrames skills, Render quality + type, Sound design kit" · demo Short "Delegated to render (Recommended)". Request: *"redesign this vault and show me the results on a new short explaining how this vault generate youtube shorts"*.

**Delegation:** P1 to P7 by the agent, cap $0.10 (base about $0.04: one take about $0.02, one timing call about $0.01); stop at the render.

| Stage | Status | Approved (date) | Note |
| --- | --- | --- | --- |
| 0 Idea · 1 Research · 2 Script · 3 Beat sheet | done | 28 Oct 2026 (delegation) | Agent at work; real case: this channel; hook type contradiction; theme line "fix the note, not the video"; demand check not run (token expired); street-lamp pass; figure set `slow`, `format` |
| 4 Captures, budget | done | 28 Oct 2026 (delegation) | real captures only (listing, frames of earlier renders, code, check output); budget $0.04, cap $0.10 |
| 5 Generation | done | 28 Oct 2026 | take v1 `4b9snthh31rmt0d1g1wax7j3d0` (762 characters, about $0.02); timings `n7qzzzwqb1rmy0d1g1wacq5zx0` (about $0.01); total about $0.03 of the $0.10 cap. Whisper heard all 125 words (homophones "queues" and "and" took the script's spelling); silences 0.25 to 0.93 s, the 0.93 s one at the hook-to-scene-2 boundary |
| 6 Build | done | 28 Oct 2026 | hfkit v2; `hyperframes check` ok (accepted: nested structure, dense track; one warning at 32.1 s: the terminal close-up passes under the rail's backing band); `check3d` OVERLAPS 0, no WARN; transitions cut, dip, whip, whip, push, blur (1 hard cut of 6); shot sizes wide, medium, close (W1, W3, W5, W6 camera); slideshow-risk score 2 (text doing the picture's job 1: the terminal world; decoration 1: small frames in the strips); render `vp-43s-9x16-r1.mp4` at CRF 14, about 2.9 Mbps; `MIX` −14.1 LUFS, true peak −1.2 dBTP; thumbnail and publish pack built (dry run) |
| 7 Verdict | fix (r1) | 28 Oct 2026 | r2: caption word gaps, one hero per beat, tightened script; take v2 `fws3ag1ke1rmt0d1g2ea0vbrbc` (820 characters, about $0.02) and timings (about $0.01): total about $0.06 of the $0.10 cap |
| 7 Verdict (r2) | fix | 28 Oct 2026 | r3: technical script, one running word; take v3 `vfj1kcqf8hrmw0d1g2tbp4cnf0` (841 characters) and timings: total about $0.09 of the $0.10 cap |
| 7 Verdict (r3) | ship | 28 Oct 2026 | user: *"like it, go for the upload package"* |
| 8 Publish · 9 Measure | pack built; the user uploads by hand | 28 Oct 2026 | `upload/vp-publish-pack.md`, render `vp-47s-9x16-r3.mp4` |

## Not verified

How the voice and effects sound; caption timing against speech; pace in motion. No screen recording of Claude Code: the named tool is shown through its real output (terminal panels), labelled as such.

## Feedback

- r2 (user, 28 Oct 2026): *"Dont like the script, forget about not uploaded videos, describe how this works on the technical aspect. not the history of videos generated."* Rule changed: [[Playbook]] §2 *Mechanism, not history*. r3 follows one word through the pipeline.

- r1 (user, 28 Oct 2026): *"i think you can improve the spacing of words (missing spaces on captions) the distribution of elements and scripting. improve that and redo last short. ask me stuff to know how i visualize it"*. Answers: look "Mix by beat", layout "One hero, full width", script "Keep and tighten", captions "Low band, fixed". Rules changed: [[Design system]] (caption gaps, one hero per beat, worlds clipped above the band), [[Playbook]] §2 (turn words, concrete nouns).
