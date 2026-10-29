---
type: process
updated: 2026-10-29
status: v1 · 29 Oct 2026: lean run (one question round, then the agent runs to the audited render), the YouTube 4K master and the TikTok master. Replaces Workflow
---

# Production: stages, budget, commands, checks

What to make: [[Format]]. How it looks: [[Look]]. Upload and numbers: [[Growth]]. The skills in `.claude/skills/` run these stages: `/short` (end to end), `/short-idea`, `/short-script`, `/short-qa`, `/short-publish`.

## The run (one session per video)

1. **Ask once** (`AskUserQuestion`, 1 to 4 questions, the recommendation first): angle and series, the real thing, the visual medium, anything unclear. The answers go verbatim into Status. A fix or rerun skips it.
2. **Idea** ([[Format]] §2) → **script** with sources ([[Format]] §3) → **beat sheet** (one row per beat: word, what the viewer sees happen, camera, transition, text, sound).
3. **Spend:** voice and word timings (about $0.03). The default cap is $0.50 a video, written in Status; anything above it (generated stills or clips) is asked first.
4. **Build** `hf/build.py` → checks → render → mix → **master** → thumbnail → publish pack.
5. **Stop at review.** The user says ship, fix or drop ([[Format]] §6). Upload only after the user confirms the pack ([[Growth]] §Publish).

## Budget

| Item | Tool | Price |
| --- | --- | --- |
| Voice, one take | `inworld/realtime-tts-2`, voice `Dennis`, rate 1.1 (`voice.py`) | about $0.025 per 1,000 characters |
| Word timings | `incredibly-fast-whisper` on Replicate (`word_timings.py`); if it sits in `starting` for minutes, cancel it and use WhisperX | about $0.01 |
| Stills, opt-in | `openai/gpt-image-2` | about $0.25 |
| Clips, opt-in, on a real photo | `lightricks/ltx-2.5-fast` | about $0.12 |
| Captures, Hairline, Anatomy, 3D, render, mix, master | local | $0 |

Replicate calls run in series, one retry per image, each prediction id logged in Status at once; a hung download is recovered (`replicate_helper.py recover`), never regenerated.

## Voice

One continuous take for the whole script (`voice.py`): scenes are paragraphs of one request, never stitched or cut. `temperature` 0, 48 kHz WAV, one bracketed direction at the top, 2 breaks or fewer. Check the take: whisper's words equal the script; no silence over 0.9 s; a mispronounced word is fixed by rewording and one retake.

## Checks (the agent runs them all; [[Format]] §4 is the bar)

| Check | Command | Pass |
| --- | --- | --- |
| Design system | `python3 System/scripts/hfkit.py` | `hfkit OK` |
| Builder warnings | `python3 hf/build.py` | no `WARN` left unexplained (frame 0, transitions, callouts, card fit) |
| Page lint | `HYPERFRAMES_NO_TELEMETRY=1 npx --yes hyperframes@0.8.209 check --json` (in `hf/`) | no errors (nested-structure and dense-track warnings accepted) |
| Layout | `node System/scripts/check3d.mjs hf/index.html` | `OVERLAPS 0`, no `CLIPPED`, `OVERFLOW`, `TEXT OVER PICTURE` |
| Frames | `npx --yes hyperframes@0.8.209 snapshot --at "$(cat ../render/_beats.txt)"` (in `hf/`) | every contact sheet read; a fault found once is searched for on all frames |
| Sound | `python3 System/scripts/listen.py <mixed mp4>` | `LISTEN PASS`: −14 LUFS ±1, true peak −1 dBTP or lower, no silence over 0.9 s |
| Master | `python3 System/scripts/master.py <mixed mp4>` | `MASTER yt` 2160x3840 bt709 and `MASTER tt` 1080x1920 |
| Vault | `python3 System/scripts/check_vault.py` | passes |

**Say what was not checked:** how the voice and effects sound and the pace in motion (the agent reads frames and numbers, it cannot watch or listen).

## Master (why YouTube looked soft)

YouTube re-encodes every upload. A 1080x1920 upload on a small channel is usually served as H.264 at a low bitrate; an upload at 2160x3840 is processed into the VP9/AV1 ladder, whose 1080p rung is cleaner. `master.py` makes:

- `upload/<v>-yt.mp4`: lanczos upscale to 2160x3840, x264 CRF 14 (about 35 to 60 Mb/s), BT.709 tags, closed GOP of 15, `aq-mode 3` (bits for flat areas), a light unsharp, AAC 384 kb/s 48 kHz, faststart.
- `upload/<v>-tt.mp4`: 1080x1920 CRF 16 for TikTok (which downsizes anything larger). Upload from the web, or turn on "Upload HD" in the app.

**Verify once per look change:** upload privately, open "Stats for nerds" in the player; the 1080p rung should read `vp09` or `av01`, not `avc1`. Write the result in [[Growth]] §Publish.

## Commands

| Need | Command |
| --- | --- |
| Voice | `python3 System/scripts/voice.py "Media/…/<Video>" --dry` ($0), then without `--dry` |
| Word timings | `python3 System/scripts/word_timings.py "Media/…/<Video>"` |
| Stock | `stock_photos.py search "<q>" --source openverse\|nasa\|commons`, `get …`; `stock_videos.py search … --vertical`, `get`, `cut` |
| Replicate | `System/scripts/replicate_helper.py` (`run`, `download`, `recover`) |
| New project | copy `hf/hyperframes.json`, `meta.json`, `package.json` from the last video's `hf/`, then write `hf/build.py`; a template: `python3 System/scripts/hfkit.py --demo <scratch dir>` |
| Render | `npx --yes hyperframes@0.8.209 render . -o ../render/<v>-<s>s-9x16-r<n>.mp4 -q delivery --crf 14` (in `hf/`, background, 3 to 5 min) |
| Mix | `python3 System/scripts/mix_audio.py "Media/…/<Video>"` |
| Contact sheet | `ffmpeg -i <mp4> -vf "fps=1/2,scale=270:-1,tile=8x4" -frames:v 1 render/_sheet.jpg` |
| Anatomy figure | `/anatomy <the machine>`, kept in `System/anatomy/<name>/` with the pose contract; line check `node .claude/skills/anatomy/scripts/lines.mjs <preview.html>` prints `line ends: 0` |
| Hairline figure | `/hairline-create <idea>` → `System/scripts/vendor/hairline/custom/` |
| Brand assets | `python3 "System/Brand/Next Token/brand.py"` |
| Upload | `python3 System/scripts/publish.py "Media/…/upload/publish.json"` (`--dry-run` builds the pack only) |

Never `pkill -f` a pattern that appears in your own command. In zsh never name a variable `path`.

## Files

```
Videos/Week NN/<YYYY-MM-DD Day>/<Topic>/   <Topic> - Status · Script - <Topic> · Upload - <Topic>
Media/Week NN/<YYYY-MM-DD Day>/<Topic>/    local, gitignored: plan.json · voice/ · hf/ · stock/ · render/ · upload/ (thumb.jpg, -yt.mp4, -tt.mp4, publish.json, pack)
```

Week 01 = 5 to 11 Oct 2026, Monday to Sunday. Media files carry the video prefix: `<v>-take-v<n>.wav`, renders `<v>-<seconds>s-9x16-r<n>.mp4`. Note ceilings (words, `check_vault.py`): Script 2,700 · Status 1,500 · Upload 2,300.

## Status note (one per video)

First line: the user's answers, verbatim. Then a table: **Idea** (series, real thing, claim, demand evidence, 3 hooks) · **Script** (words, sources checked) · **Spend** (prediction ids, total, cap) · **Build** (check results, transitions, shot sizes) · **Review** (verdict) · **Publish** (video id, date) · **Numbers** (24 h, 7 d, 28 d). Then *Not verified* and *Feedback* (the user's words).
