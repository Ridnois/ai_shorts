---
type: process
updated: 2026-11-03
status: v2 · 3 Nov 2026 vault rebuild. Owns how a Short is made and shipped: the run, budget, brand, look tokens, layout, the kit (components, ML primitives, figures, captures, Manim), sound kit, voice, checks, master, upload, schedule, files. Replaces Production and Look. Code: System/scripts/hfkit.py
---

# Build: make it, check it, ship it

What to make: [[Strategy]]. Words: [[Story]]. Picture rules: [[Picture]]. Numbers: [[Data]]. The skills run these stages: `/short` (end to end), `/short-idea`, `/short-script`, `/short-qa`, `/short-publish`.

## The run (one session per video)

1. **Ask once** (`AskUserQuestion`, 1 to 4 questions, the recommendation first): angle and series, the real thing, the medium of the mechanism ([[Picture]] §Medium), anything unclear. The answers go verbatim into Status. A fix or rerun skips it.
2. **Idea** ([[Strategy]]) → **script** ([[Story]]) → **pre-flight card** ([[Data]]) → **beat sheet** (one row per beat: cue word, medium, what the viewer sees happen, camera, transition, text, sound; 2 borrowed moves from [[Shots]]).
3. **Spend:** voice and timings (about $0.03), then anything else up to the cap, logged in Status.
4. **Build** `hf/beats.json` (`beats.py`) → `qa.py` → render → mix → `qa.py --render` → master → thumbnail → publish pack.
5. **Stop at review.** The user says **ship**, **fix** (one list, one revision) or **drop**; at most two revisions. A Short that waits more than 7 days is shipped or dropped: only uploads produce data. Upload only after the user confirms the pack.

## Budget (cap $2.00 a video, the user's decision of 3 Nov 2026; written in Status)

| Item | Tool | Price |
| --- | --- | --- |
| Voice, one take | `inworld/realtime-tts-2`, voice `Dennis`, rate 1.1 (`voice.py`) | about $0.025 per 1,000 characters |
| Word timings | `incredibly-fast-whisper` on Replicate (`word_timings.py`); if it sits in `starting` for minutes, cancel it and use WhisperX | about $0.01 |
| Still in our style | an image model on Replicate (check the model id exists first; Flux 2 Pro or Nano Banana 2 class, about $0.02 to $0.07) | per image |
| Clip from that still | image-to-video on Replicate (Hailuo 2.3 or Veo 3.1 Lite class, about $0.05 a second; 5 s is about $0.25) | per clip |
| Captures, primitives, figures, Manim, 3D, render, mix, master | local | $0 |

Replicate calls run in series, one retry each, every prediction id logged in Status at once; a hung download is recovered (`replicate_helper.py recover`), never regenerated. Prices are from third-party roundups (3 Nov 2026): read the model page before the first call.

## Brand

- **Next Token** (renamed 29 Oct 2026). Line: "How AI works · Agents at work · What's coming". Kit: `System/Brand/Next Token/` (`brand.py` writes avatar, banner, mascot).
- **Mascot, Tok:** a yellow token tile with a thick ink outline, two eyes and a cursor. It lives on the channel page, the banner and thumbnails, **not inside the video**: the look is the brand inside the video.
- Persona and banned words: [[Story]] §Persona.

## Look: flat paper

Why: flat colour and still texture compress cleanly; a bright frame stands out in a dark feed; thick ink survives the 1080p rung. **Never:** full-frame gradients, animated grain or noise, glows, thin lines, small text.

| Token | Value | Job |
| --- | --- | --- |
| `PAPER` | `#F4EFE4` with a still dot grid | the ground |
| `INK` | `#121212` | lines (6 px), text, hard shadows |
| `YELLOW` | `#FFD23F` | **the hero**: the one thing being explained, as a fill or a marker under ink text; never a text colour |
| `BLUE` | `#2C5BEA` (`BLUE2` `#D3DEFF`) | data, inputs, a figure's lit stroke |
| `RED` | `#D7392B` (`RED2`) | wrong, the error |
| `GREEN` | `#13965A` (`GREEN2`) | right, the fix; `flood=` turns the ground `GREEN2` from the fix on |
| `MUTED`, `PAPER2`, `WHITE` | `#6B665C`, `#E7E0D1`, `#FFFFFF` | secondary text · inactive · panels |

- Text takes only `INK`, `MUTED`, `BLUE`, `RED`, `GREEN` (`hfkit.TEXT_SAFE`); a "hot" word sits on a yellow marker.
- **Type:** Inter Display Black for display lines and numbers (tracking −0.03 em), Inter Black for captions and labels, JetBrains Mono for anything a model reads or writes. Scale `T`: 44 · 60 · 84 · 128 · 190 px; nothing read is under 44 px.
- **Panels:** white, 6 px ink border, a hard 12 to 14 px ink offset shadow. Terminal and code panels are the one dark block (`#171717`).
- Generated stills and Manim clips use these tokens too (the style prompt and `manim.py`'s palette), so a medium change never changes the look.

## Layout (1080 × 1920)

| Zone | Area (px) | Holds |
| --- | --- | --- |
| Top bar | y < 180 | nothing (platform) |
| **STAGE** | x 56 to 950, y 180 to 860 (to 1150 when the deck is empty) | pictures; `HERO` x 73 to 933, y 330 to 1150 is one hero filling about 80 % of the width |
| **DECK** | x 56 to 950, y 880 to 1150 | one card or the comment prompt |
| **BAND** | y 1180 to 1320 | captions only; worlds are clipped above it |
| Interface | y > 1440, x > 950 | nothing (title, buttons) |

- **Instagram fits this layout** (third-party safe-zone guides, 3 Nov 2026; no Meta spec found): its top bar reaches about y 220, its buttons x > 960, its caption about the last 250 to 440 px. Captions and anything read already sit inside. The profile grid shows the cover's middle 1080 × 1440 (y 240 to 1680).
- **One hero per beat**, centred on x 503 (the right strip belongs to the buttons).
- **Two layers:** pictures live in the camera; everything read on the glass (a claim, a number, a card, the prompt) goes through `K.screen(...)`, so a zoom never crops it. A callout stays in the camera, shows only while the camera is still and for 0.8 s or more, its label in free space.
- **Captions:** 1 to 3 words, Inter Black capitals up to 96 px, ink on paper, the spoken word on a yellow marker and 6 % larger; in the band (`captions.py`).

## Kit (`hfkit.py`; a video's `hf/beats.json` only places and times it)

Change a rule here and in `hfkit.py` together; never fork a component inside a video's builder. What `beats.json` cannot say goes in `hf/extra.py`.

| Component | Function |
| --- | --- |
| Display line | `big(id, text, x, y, w, size, hot=k)` with `v.reveal` |
| Real frame, phone | `frame(...)`, `phone(...)`: screenshots, captures and recorded runs, ink border and hard shadow |
| Readable capture | `sheet(id, rows, x, y)`: real crops of two or three words each, every row 80 px tall or more; a whole page appears only as a brief establishing shot under a big line |
| Terminal | `code(id, lines, x, y, w, title=)`: `<s>` strings, `<b>` numbers, `<u>` prompt |
| Counter, callout, tag, card, prompt | `counter` + `v.count` · `callout(...)` + `v.callout` · `tag`, `card(...)`, `ask(...)` |
| Pipeline rail | `v.rail(steps, t)`, `v.step(k, t, "on"/"done"/"bad"/"good")` |
| Hairline figure | `hairline(id, x, y, w)` + `v.hairline(id, name)` + `v.point` |
| Anatomy figure | `anatomy(id, name, x, y, w)` + `v.anatomy(id, name)` + `v.pose` |
| Clip | `clip(id, src, x, y, w)` + `v.play`: a captured, Manim or generated webm/mp4 from `hf/assets/` in an ink frame |
| 3D | `blender3d(spec, out, dur)` then `v.model3d` or `v.plate3d` (only where depth explains) |
| Thumbnail | `v.thumb(inner)` → `upload/thumb.jpg` |

**ML primitives** (3 Nov 2026; each has a `beats.py` item type and is shown in `System/scripts/primitives-example.json`):

| Primitive | Shows | Verbs |
| --- | --- | --- |
| `tokens(id, pieces, x, y, w)` | text split into token chips (pass the real split from the model's tokenizer) | `chips` (arrive in order), `light` (one chip) |
| `probs(id, rows, x, y, w)` | next-token odds as ink bars, highest first | `grow` (bars fill to their value), `light` (the pick) |
| `heatmap(id, labels, weights, x, y, w)` | an attention grid, cell ink by weight | `reveal` (cells fill by row), `light` (one row) |
| `vecgrid(id, vectors, x, y, w)` | arrows on a dot grid (embeddings, a vector sum) | `grow` (arrows draw from the origin) |
| `scatter(id, points, x, y, w)` | an embedding map: labelled dots, clusters by colour | `chips` (dots land), `light` (one cluster) |
| `net(id, sizes, x, y, w, h)` | a small network: columns of nodes and thick links | `reveal` (activations flow left to right) |
| `matrix(id, rows, x, y, w)` | a grid of numbers (weights, a product) | `chips` (cells land), `light` (one cell) |
| `loop(id, steps, x, y, w)` | the agent ring: plan, act, check around a centre | `step` per node (`on`, `done`, `bad`, `good`) |

Verbs fire on a heard word (`v.cue(scene, "word")`): `pop`, `grow`, `reveal`, `blurin`, `hide`, `rise`, `chips`, `count`, `light`, `strike`, `flash`, `slide`, `nudge`, `pose`, `point`, `cam`, `focus`, `wide`, `play`. Words stagger 60 to 120 ms.

**Figures:** Hairline (isometric line figures, MIT): `riffle`, `terrain`, `drawer`, `window`, `balance`, `temperature`, `splitter`, `loop`, `doubling`, `quantize`; the 33 packaged ones are in `vendor/hairline/README.upstream`; new ones with `/hairline-create` into `vendor/hairline/custom/`. Anatomy (isometric machines, `System/anatomy/<name>/`, pose contract: parameters in, part transforms out): `wafer-chuck`, `gut-carrier`, `citator`, `ram-stick`, `rater`, `switchboard`, `ownership`, `compile-gate`, `context-reader`, `effort-meter`, `attention-desk`, `cooling-tower` (heat, flow, evaporation, drops: AI water use), `ticket-board` (train, prune, rewind: the lottery ticket). Their parameters are in each `<name>.json`. One figure is the anchor of one video; the next video needs a different main picture.

**Captures** (`capture.py`): records a scripted browser session at 1080×1920 into `hf/assets/<name>.webm` (a page, a list of clicks and waits, typed text). Our own runs (a terminal, Claude Code) are recorded from the real session. Licence and credit of every recorded tool go in the Script note.

**Manim** (`manim.py`): renders one Manim CE scene with the paper palette and 6 px ink to a transparent `hf/assets/<name>.webm`, placed with `clip`. Manim lives in `System/.venv` (system Python has no numpy).

## Sound kit (`System/assets/sfx/`, credits in its `CREDITS.md`)

`whoosh-air`, `whoosh-swipe`, `whoosh-stick`, `whoosh` (rotated on whips, pushes, fast moves) · `click` (callouts) · `pop` (chips) · `impact-bass-2` (opening and payoff hit) · `riser` (into the payoff) · `ping`, `key-press`, `typing` (on demand, `v.sfx`). `v.payoff(t)` once per video; the 0.6 s before its hit is kept free of other effects. New sounds: CC0 (Openverse) or the `media-use` skill, credited.

## Voice

One continuous take for the whole script (`voice.py`): scenes are paragraphs of one request, never stitched or cut. `temperature` 0, 48 kHz WAV, one bracketed direction at the top, 2 breaks or fewer. Check the take: whisper's words equal the script; no silence over 0.9 s; a mispronounced word is fixed by rewording and one retake.

## Checks: one command

`python3 System/scripts/qa.py "Media/…/<Video>"` runs, in order, and prints one table with PASS or FAIL per row:

| Row | What | Pass |
| --- | --- | --- |
| kit | `hfkit.py` self-test | `hfkit OK` |
| build | `beats.py` warnings | no `WARN` left unexplained |
| lint | `hyperframes@0.8.209 check` | no errors (nested-structure and dense-track warnings accepted) |
| layout | `check3d.mjs` | `OVERLAPS 0`, no `CLIPPED`, `OVERFLOW`, `TEXT OVER PICTURE` |
| frames | `hyperframes snapshot` at `render/_beats.txt` | contact sheets written; the agent reads each once ([[Picture]] §Bar) |

With `--render <mixed mp4>` it adds **pace** (`pace.py`: motion and composition tiers), **sound** (`listen.py`: −14 LUFS ±1, true peak −1 dBTP or lower, no silence over 0.9 s) and **master** (`master.py`: `MASTER yt` 2160x3840 bt709 and `MASTER tt` 1080x1920). **Say what was not checked:** how the voice and effects sound, and whether the motion means something.

## Master (why YouTube looked soft)

YouTube re-encodes every upload. An upload at 2160x3840 is processed into the VP9/AV1 ladder, whose 1080p rung is cleaner than the H.264 a 1080p upload gets. `master.py` makes `upload/<v>-yt.mp4` (lanczos to 2160x3840, x264 CRF 14, BT.709, closed GOP 15, `aq-mode 3`, light unsharp, AAC 384 kb/s) and `upload/<v>-tt.mp4` (1080x1920 CRF 16). **Every upload uses the master.** Open: compare "Stats for nerds" on a private 4K upload; write the codec seen here.

## Upload

- `python3 System/scripts/publish.py "Media/…/upload/publish.json"` (keys in its header, including `series`, `hook_pattern`, `medium`): builds the 4K master when missing, uploads it with language `en`, category 28, tags and the synthetic flag, sets the thumbnail, writes the `videos.csv` row, the Upload note and the Status line. `--dry-run` builds the pack only; `--resume <id>` after a crash. Default private; scheduled with `publish_at`.
- **Instagram and TikTok** are posted by hand from `upload/*-tt.mp4` with the pack's captions ([[Strategy]] §Package); no upload script.
- **Auth:** one OAuth token (upload, read-only channel and analytics) from the Desktop client "Redtail Uploader" in Google Cloud project `redtail-upload`. `youtube_auth.py` checks every token against the NextToken channel (`UCCZX7-YPNPntwPKI1hdv2hQ`, @yournexttoken) and stops on any other. The token expires every 7 days: on HTTP 400 the user runs `python3 System/scripts/youtube_auth.py` and picks **REDTAIL** at "Choose your account or a brand account". The YouTube scripts use this OAuth token, not an API key. Quota: 10,000 units a day; an upload is about 1,600, a radar pull about 100.
- **Studio only** (no Data API field, checked 3 Nov 2026): hiding the like count (Details › Show more › "Show how many viewers like this video") and pinning a comment. The token holds `youtube.force-ssl` since 3 Nov 2026, so `comments.py` can post replies, and the pinned comment can be posted by it, but pinning it stays a Studio step.
- **The repo is public:** keys live only in `.env` (gitignored, 0600); `.env.example` lists every key the vault reads and where each comes from, with no values. `secret_scan.py` runs in `check_vault.py` and as the pre-commit hook.

## Schedule

A daily job at 16:00 UTC, set from Claude Code (`CronCreate`), runs from the vault root: `python3 System/scripts/daily.py`. It runs the analytics pull and report, the comments pull (`comments.py pull`), a Monday radar pull and report, and signals. When the weekly token has expired, it writes a one-line "re-auth needed" banner at the top of `Analytics/Report.md` instead of failing silently.

## Commands

| Need | Command |
| --- | --- |
| Voice | `python3 System/scripts/voice.py "Media/…/<Video>" --dry` ($0), then without `--dry` |
| Word timings | `python3 System/scripts/word_timings.py "Media/…/<Video>"` |
| Stock | `stock_photos.py search "<q>" --source openverse\|nasa\|commons`; `stock_videos.py search … --vertical`, `get`, `cut` |
| Capture | `python3 System/scripts/capture.py "Media/…/<Video>" <name> <script.json>` |
| Manim clip | `System/.venv/bin/python System/scripts/manim.py "Media/…/<Video>" <scene.py> <Scene>` |
| Replicate | `System/scripts/replicate_helper.py` (`run`, `download`, `recover`) |
| New build | `python3 System/scripts/beats.py "Media/…/<Video>" --new` writes `hf/beats.json`; format in `beats.py`'s docstring; examples in `beats-example.json` and `primitives-example.json` |
| Build | `python3 System/scripts/beats.py "Media/…/<Video>" [--rev N]` → `hf/index.html`, the sound timeline, `upload/thumb.jpg` |
| Render | `npx --yes hyperframes@0.8.209 render . -o ../render/<v>-<s>s-9x16-r<n>.mp4 -q delivery --crf 14` (in `hf/`, background, 3 to 5 min) |
| Mix | `python3 System/scripts/mix_audio.py "Media/…/<Video>"` |
| Checks | `python3 System/scripts/qa.py "Media/…/<Video>" [--render <mixed mp4>]` |
| Anatomy figure | `/anatomy <the machine>`, kept in `System/anatomy/<name>/`; line check `node .claude/skills/anatomy/scripts/lines.mjs <preview.html>` prints `line ends: 0` |
| Hairline figure | `/hairline-create <idea>` → `System/scripts/vendor/hairline/custom/` |
| Comments | `comments.py pull`, `draft`, `check`, `post` (post only what the user approved; [[Strategy]] §Comments) |
| Ideas and numbers | `radar.py`, `signals.py`, `youtube_analytics.py pull`, `analytics.py report`/`beats` ([[Strategy]] §Ideas, [[Data]]) |

## Files

```
Videos/Week NN/<YYYY-MM-DD Day>/<Topic>/   <Topic> - Status · Script - <Topic> · Upload - <Topic>
Media/Week NN/<YYYY-MM-DD Day>/<Topic>/    local, gitignored: plan.json · voice/ · hf/ · stock/ · render/ · upload/
Research/                                  Channels (watchlist) · Radar, Signals (generated) · Shots/ (reference shots)
```

Week 01 = 5 to 11 Oct 2026, Monday to Sunday. Media files carry the video prefix: `<v>-take-v<n>.wav`, renders `<v>-<seconds>s-9x16-r<n>.mp4`. Note ceilings (words, `check_vault.py`): Script 2,700 · Status 1,500 · Upload 2,300.

**Status note** (one per video): first line, the user's answers verbatim. Then a table: **Idea** (series, hook pattern, real thing, claim, demand evidence) · **Pre-flight** ([[Data]]) · **Script** (words, sources checked) · **Spend** (prediction ids, total, cap) · **Build** (main medium, `qa.py` result) · **Review** (verdict) · **Publish** (video id, date) · **Numbers** (24 h, 7 d, 28 d, with the prediction checked). Then *Not verified* and *Feedback* (the user's words). Build detail stays in the Media folder, not in Status.

Never `pkill -f` a pattern that appears in your own command. In zsh never name a variable `path`.
