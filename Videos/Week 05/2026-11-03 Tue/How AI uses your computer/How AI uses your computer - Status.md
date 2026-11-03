---
type: status
updated: 2026-11-03
---

# How AI uses your computer: Status

**Ask once (user, 3 Nov 2026, verbatim):** angle "It sees a photo (Recommended)" · medium "Real recorded run (Recommended)". Request: *"choose a short topic and build a video so you display the changes"*.

| Stage | State |
| --- | --- |
| **Idea** | Agent at work (last video How AI works). Pattern `surprising-result`. Real thing: our recorded runs of Claude Opus 5.5 on mobile Wikipedia (3 Nov 2026), Anthropic computer-use docs. Claim: an agent never sees a button, only a screenshot and two numbers. Demand: NAauIR6JFps 5.99 M (92x), zK38VMVV_Fs 437 k (618x), 9DxXDLhXnwU 876 k (3.8x). Score: demand 5 · own fit 4 (Agent at work 680 median engaged, above our 368) · showable 5 (a real run shows the whole loop) · real thing 4 = 18/20 |
| **Pre-flight** | (1) `surprising-result`, radar above. (2) Field titles promise the result; ours shows the mechanism in a real run. (3) 0 s: the screenshot with the crosshair and IT CAN'T SEE BUTTONS; 3 s: "It sees a photo"; 6 s: "a wrong guess clicks the wrong thing", no citation (4 to 7 s rule). (4) Weakest beat: scene 5 (typing, a connective beat). (5) Prediction at 7 d: **above** our median (368 engaged). |
| **Script** | 167 words, 8 scenes; sources checked 3 Nov 2026 ([[Script - How AI uses your computer]]) |
| **Spend** | take `zqepjb86ddrmw0d1me9bse64s8` (964 chars, about $0.024); incredibly-fast-whisper `2htg8sa8dxrmt0d1me9bze6n8c` (about $0.01). Recorded runs via `claude -p` on the user's Claude plan (8 calls, no Replicate). Total about $0.035, cap $2.00. |
| **Build** | main medium `capture` (two real runs, `run/agent.mjs`, `run/log.json`, `run/run1/`), spine = `loop` primitive (w2, w5, w8), `tokens` primitive for the model's real replies (w4, w5), frame 0 on the end state (screenshot + crosshair at 469, 27). r3 (50.5 s): `qa.py` kit, build, lint, layout (OVERLAPS 0), frames PASS; pace PASS (2 stills of 2.3 and 2.7 s, WARN); composition WARN (6 stretches of 6 to 8 s over the 5 s tier); LISTEN PASS −14.0 LUFS, −1.5 dBTP; MASTER yt 2160x3840 bt709, tt 1080x1920. One accepted WARN: the hook's 8 % push moves the camera under callout `o1` (check3d: nothing cropped). Transitions push, whip, push, cut, dip, blur, push. Frames audited twice; fixed: empty 3.6 to 4.5 s, a blank typing screenshot, hidden terminal rows, an unreadable height crop, a clipped counter, a still hook. Pack: `upload/cu-publish-pack.md` (dry run). |
| **Review** | **ship** (user, 3 Nov 2026: *"ship it, build the upload pack"*); r3, no revisions |
| **Publish** | **public** 3 Nov 2026, [`FFAD92aUjFg`](https://youtu.be/FFAD92aUjFg) (user: *"ship it as public, hide likes and add tagged comment"*); 4K master, thumbnail confirmed. Hide likes and pin the comment: by hand in Studio (no API for either). TikTok: by hand. |

## Not verified

Not heard: the voice and effect levels; whether the motion reads well at speed. The Tip row (330 m) sits at the bottom edge of the model's screenshot, half cut: shown as the model saw it. The composition tier warns 6 times (calibrated on one older render only). The runs use our own harness (`claude -p` reading a screenshot), built on the documented loop, not Anthropic's hosted computer-use tool.

## Feedback
