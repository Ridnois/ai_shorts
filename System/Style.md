---
type: rules
updated: 2026-10-05
status: v1 · channel identity, on-screen design system and brand in one note
---

# Style: voice persona, on-screen design, brand

Captions are always the top layer (see Layers below). Approved by the user ("good and appealing, keep improving"): **keep the layout exactly**; improve specificity, placement over real images and captions, not the design. Rules for what text says: [[Playbook]] §4.

## Brand

- **Redtail**, science entertainment. Slogan **"Science at full speed."** (second line "Strange, fast and true."). Logo: NFL-style snarling orange fox head; banner B; assets in `System/Brand/Redtail/` (`redtail-logo.png` transparent, **`redtail-logo-dark.png` and `-dark-small.png` on a dark navy `#101824` rounded square**, for thumbnails and dark surfaces; user, 7 Oct 2026). TikTok **@redtail_media**; YouTube channel `UCCZX7-YPNPntwPKI1hdv2hQ`.
- Niche: technology and the systems under it (see [[Audience]]). Mission: make how the world is built and run entertaining, the strange machinery behind it in a minute you will want to watch again. Pillars: precise (figures sourced), surprising (≥ 4 on surprise and scale), calm (no hype), honest about machines (AI voice and schematics disclosed), real over decorative.
- The sign-off is an idea, never "like and subscribe". Brand lives on the channel page, **never inside the video**.
- Does not do: clickbait, fake experts, photoreal fakes of real events or people, copied scripts, template videos where only the topic word changes.

## Persona: the curious specialist

Spent years next to the machines and papers behind the news; precise, quietly confident, dry. Specific beats general ("Jarillo-Herrero's group at MIT, 2018", not "researchers"). **Banned words** in narration, cards and descriptions: *did you know, game-changing, revolutionary, incredible, unlock, journey, the takeaway, fun fact, key point, in this video*, plus memes and exclamation marks. Recurring devices: the copper accent, one number, the margin note, part-name callouts, source tags, the last line.

## Design system (1080×1920, from `build_video.py`)

| Token | Value |
| --- | --- |
| Paper | `#F9F6EE` at 94 % (cards, callout boxes) |
| Ink | `#1C1A17`, soft `#4D4741` |
| **Copper** | `#C76B38`: callout dots and lines, card bar, big figures, copper words in captions. One emphasis colour; never highlight more than one word in three |
| Caption | white `#FFFFFF`, outline `#0A0907` |
| Fonts | Noto Sans Display Bold (titles, numbers, captions), Noto Sans Regular (labels, details, callouts) |
| Gradients | one family per topic (cold blue cryogenics, warm copper energy, deep green materials), dark enough for paper boxes; behind `contain` photos and cutouts only |

| Component | Spec |
| --- | --- |
| **Caption** | one word at a time, centred at **the middle of the frame (50 % of the height, `CAP_Y`)**, 88 px bold capitals, white, dark outline and soft shadow; words with a digit and up to 6 `keywords` in copper; word holds until the next, never across a pause > 0.55 s; long words shrink |
| **Context card** | 894 × 280 px, 16 px corners, 1 px graphite border at 25 %, 8 px copper bar left, centred at **66 % from the top** (x 56 to 950); label 32 px spaced capitals copper, title 56 px bold, detail 34 px |
| **Number card** | same box; figure 124 px bold copper, caption 44 px bold, source 30 px |
| **Margin note** | same box, label "Margin note", two lines ≤ 30 characters, 46 px bold |
| **Callout** | copper dot 13 px with ring, 2 px leader, paper label with copper bar, 34 px; enters 1 s after the plate, 0.6 s apart; labels clamped above the caption zone |
| **Layers** | **Captions are the top layer**: cards, callouts and their text always sit under the captions (user, 5 Oct 2026: *"added text and pointers are covering the captions, that should be below the captions"*; builder `CAP_CH`) |
| **Immersive plates** | no empty screens (user, 5 Oct 2026). `"bg": "blur"`: the plate's own photo (or `"bg_photo"`) cover-fitted, blurred and darkened to 38 % plus a dark tint, behind a `contain` plate. `"inset": {"file", "pos", "width"}`: a second picture, rounded 22 px with the soft shadow, enters 0.7 s after the plate, leaves 0.15 s before it; **split layout**: diagram on top (pos y about 0.27, width 0.78), inset of the real object under the captions (pos [0.5, 0.67], width ≤ 0.62), never in the last 25 % of the frame |
| **Motion** | cards fade in 0.25 s with a 24 px rise, out 0.2 s, card enters 0.45 s after its plate; no shakes, flashes or zoom punches |

Layout from the top: top 10 % free (Shorts title bar) · callout labels · captions at 50 % · cards at 66 % · last ≈ 25 % and the right edge ≈ 12 % belong to the platform interface. TikTok covers more of the bottom 15 to 20 %: unverified, test once with a private upload and, if needed, raise `CAP_Y` for a TikTok export (`plan.json`) without touching the YouTube master.
