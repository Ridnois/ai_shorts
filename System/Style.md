---
type: rules
updated: 2026-10-27
status: v5 · layout, components and motion moved to Design system (27 Oct 2026); v4 · Redtail look v2 (ink ground, four validated semantic colours, line style, type, composition), user feedback 23 Oct 2026; v3 · AI channel identity and 3D plates (23 Oct 2026); v2 · motion plates (navy ground, lanes, word cues) added 9 Oct 2026; channel identity, design system and brand in one note
---

# Style: voice persona, on-screen design, brand

Captions are always the top layer ([[Design system]] Layers). Approved by the user ("good and appealing, keep improving"): **keep the caption and card layout exactly**; improve specificity and placement. What fills the frame behind them was redesigned on 9 Oct 2026 at the user's request ([[Playbook]] §3, Motion plates below). Rules for what text says: [[Playbook]] §4.

## Brand

- **Inside the Model** (user, 27 Oct 2026: *"I like 3: inside the model. make a new handle, avatar and banner. forget the fox but be original"*; replaces Redtail and its fox). Handle **@insidethemodelai** (`@insidethemodel` is taken; `@insidethemodelai` returned 404 on 27 Oct 2026, so likely free, claimed by the user in Studio). Banner line "How AI works · Agents at work · What's coming" and "NEW SHORTS MON TO FRI". **Mascot: the peeker** (user, 27 Oct 2026: *"Avatar is quite boring, no soul"*, replacing a ring mark the same day): the model is a dark box with its lid open; a round ember creature with big eyes and two small hands on the rim peeks out at you; two signal tokens float up out of the box; drawn in the look tokens below by `System/Brand/Inside the Model/brand.py` (`itm-avatar.png` 800 px, `itm-banner.png` 2560×1440, text inside the 1546×423 safe area). `System/Brand/Redtail/` stays only for legacy `make_thumbnail.compose`. TikTok still **@redtail_media** until the user renames it; YouTube channel `UCCZX7-YPNPntwPKI1hdv2hQ`.
- Niche: artificial intelligence, in three series (see [[Audience]]). Mission: teach people AI, how it works, how to make agents do real work, and what it changes, in a minute they will want to watch again and repeat to a friend. Pillars: precise (model, version and date on every claim), useful (the viewer can do or explain something new after one minute), calm (no hype, no doom), honest about machines (AI voice, schematics and speed-ups disclosed), real over decorative (real runs, real hardware, no AI clichés).
- The sign-off is an idea, never "like and subscribe". Brand lives on the channel page, **never inside the video**.
- Does not do: clickbait, fake experts, staged or retyped demos, drawn mock-ups of real products, photoreal fakes of real events or people, copied scripts, template videos where only the topic word changes, launch-day news recaps.

## Persona: the engineer who uses it every day

Builds with models and agents daily and reads the papers behind the headlines; precise, quietly confident, dry, neither a booster nor a doomer. Specific beats general ("Vaswani and colleagues at Google, 2017", not "researchers"; "Claude Opus 5.5 in October 2026", not "AI"). **Banned words** in narration, cards and descriptions: *did you know, game-changing, revolutionary, incredible, mind-blowing, insane, unlock, supercharge, journey, the takeaway, fun fact, key point, in this video, this changes everything, AGI is here*, plus memes and exclamation marks. Recurring devices: the copper accent, one number, the comment prompt, part-name callouts, source tags, the last line.

## Look tokens (1080×1920)

Redtail look v2 (23 Oct 2026; user: *"color, background and line style feel too generic, you could research more for the style of the videos too"*). Sources read 23 Oct 2026: fan guides to the 3Blue1Brown style (a few semantic colours, each tied to one role, on a dark ground), GitLab motion guidelines and motion-design notes (layered soft radial gradients plus grain instead of flat fills), vertical-composition research (Nakhon Phanom Univ. journal: a centred subject and negative space read best in 9:16) and explainer-hierarchy notes (one dominant element at a time; motion only where the viewer needs it). The palette passed the dataviz skill's validator on the ink ground (lightness band, chroma, colour-blind and normal-vision separation, 3:1 contrast). [H] until the analytics loop compares it.

| Token | Value |
| --- | --- |
| **Ink ground** | `ink` `#0B0D17` to `ink2` `#151A2B`, two soft light pools (ember low left at 10 %, signal high right at 9 %), vignette and fixed fine grain; no drafting grid (it read as generic). `motion.py` `ground()` draws it; `scene3d.py` composites the same image behind every 3D plate, so 2D and 3D cut together |
| **Semantic colours** (one meaning each, the same in every video) | **ember** `#E36927` the hero, the one thing the voice is explaining (light `ember2` `#FF9A5C` for glow cores) · **signal** `#418AD1` data and inputs: numbers, tokens fed in, the landscape (light `signal2` `#8EC2F2`) · **mint** `#00AE7B` right, better, the target · **rose** `#B83255` wrong, error, loss. Text in mint or rose uses `mint2` `#5FD6A8` and `rose2` `#E8708F` |
| Neutrals | `cream` `#F3EDE2` text and labels · `slate` `#6B7590` structure, axes, secondary lines · `haze` `#262D42` inactive parts, tracks, boxes |
| **Solution scenes** (user, 26 Oct 2026: *"when presenting solution, make it more attractive and colorful"*) | from the scene that gives the fix to the close: **mint is the hero** (`mint`, `mint2`), the ground pools turn mint and signal (a colour flood of about 0.6 s on the scene's first word), and up to three semantic colours share the frame (mint, `signal2`, `ember2`) with springy entrances (`back.out`); still no new hex without the validator, still no gradient on cards. **Meaningful, not only green** (user on the prompt-injection r3, 26 Oct 2026: *"solution could be more colorful and meaingful"*): the picture shows *why* the fix works (the attack visibly hits the limit and fails, step by step on the words), never just a mint end state. The problem scenes keep the sober ink look, so the switch itself tells the viewer "here is the fix" [H] |
| Rules of colour | the hero is the only ember thing on screen; colour never decorates (a blue box is data, a rose word is wrong); never highlight more than one word in three; any new colour runs the dataviz validator first ([[Workflow]] §Commands) |
| **Line style** | rounded caps and joins, two weights: structure 4 to 6 px slate, the hero 8 to 12 px ember with `glow`; dashed only for something predicted, hypothetical or removed; arrows only where direction is the point |
| **Type** | Inter Display Bold (titles, numbers, figures), Inter (labels), **JetBrains Mono for anything a model reads or writes** (tokens, prompts, outputs, code: `mono`); captions and cards keep the approved builder fonts |
| Caption | white `#FFFFFF`, outline `#0A0907` |
| Paper | `#F9F6EE` at 94 % (cards, callout boxes) |
| Gradients | only the ink ground; legacy `contain` photos and cutouts keep their blur backgrounds |

**Layout, components and motion** (zones, column grid, arrangements, every component's spec, motion verbs, 3D routes) live in [[Design system]] and its code `System/scripts/hfkit.py`; this note keeps the look they are drawn in.

| Legacy Blender builder (`build_video.py`, `motion.py`) and the library | Spec |
| --- | --- |
| **Illustrations** (since 26 Oct 2026, [[Playbook]] §3 *Illustrate, do not typeset*) | **Fluent Emoji 3D** (Microsoft, MIT, `github.com/microsoft/fluentui-emoji`, 256 px PNG): everyday objects that carry a step, shown at ≤ 280 px (they blur above that), soft drop shadow, class `art`; enter on their word with a small grow and turn (`back.out`), no idle wobble; never the robot, brain or chip emoji (AI clichés). Real things are photos ([[Playbook]] §3 footage rules); interfaces are drawn devices (a phone frame around the chat). Credit line in `stock/_credits.jsonl`. **Concept pictures are fixed** (the Picture column of [[Audience]] *Plain-words map*): the same object stands for the same AI idea in every video |
| **Callout** | ember dot 13 px with ring, leader, paper label with ember bar, 40 px; enters on the word that names the part (`at`), else 1 s after the plate; labels clamped above the caption zone. Motion plates draw the same callout (`label`) and chip (`chip`) |
| **Motion plate** | 1080×1920 clip from `motion.py`: ink ground, subject in the upper lane, one supporting element in the lower lane, events on word cues, fades 0.25 s with an 18 px rise for text; specs below |
| **Immersive plates** | legacy stills; no empty screens (user, 5 Oct 2026). `"bg": "blur"`: the plate's own photo (or `"bg_photo"`) cover-fitted, blurred and darkened to 38 % plus a dark tint, behind a `contain` plate. `"inset": {"file", "pos", "width"}`: a second picture, rounded 22 px with the soft shadow, enters 0.7 s after the plate, leaves 0.15 s before it; **split layout**: diagram on top (pos y about 0.27, width 0.78), inset of the real object under the captions (pos [0.5, 0.67], width ≤ 0.62), never in the last 25 % of the frame |

## Motion plates and engagement rules (9 Oct 2026)

From the user's *"make more engaging videos"* and the 9 Oct redesign; each rule is [H] until the comparison in [[Publish]] §Analytics loop.

1. **First frame carries the claim.** The hook plate shows the anchor already doing the surprising thing (the counter racing, the bar dropping) from frame 1, with at most one key-term label; the voice and captions carry the sentence.
2. **Things build, they do not appear.** Parts enter on the word that names them; lines draw themselves (`draw`, `to_x`); particles travel (`stream`); numbers count (`value`). Nothing labelled is on screen before it is spoken.
3. **Legible at phone size.** Text ≥ 40 px (captions and cards keep their approved sizes above) (labels 40, figures 56 to 112), ≤ 25 words per plate, one ember subject. `motion.py` warns below 40 px and in the caption band (y 880 to 1040), the bottom interface (y > 1440) and the right action strip (x > 950).
4. **Scale changes inside a world:** a zoom from the object to its inside (the chat window opens into the row of tokens), a camera move to the detail named; a new world only for a new step.
5. **An event every 2 to 3 s.** `motion.py` warns when nothing changes for over 3.5 s.
6. **Conclusion card and question.** The last scene returns to the anchor with the conclusion card (≤ 26 characters); the closing question has its own plate with the comment prompt ([[Playbook]] §2).
7. **Colour:** the semantic colours above, never more than three of them on one plate plus the neutrals.
8. **Footage under a drawing:** a motion plate may use a clip or photo as its ground (`bg` `video` or `photo`, dimmed) so labels and arrows land on the real thing.

## 3D plates (23 Oct 2026)

**3D is the exception, not the look** (user, 26 Oct 2026, on *Free or paid* r2: *"Horrible, unnecesary 3d models. unclear diferentiation. go simpler"*): default to clean, large 2D diagrams; use 3D only when depth itself is the point a 2D drawing cannot show, and never to decorate a comparison. One difference per video, drawn as simply as possible beats many vivid scenes [H].

Rendered by `scene3d.py` (Blender EEVEE) for mechanisms with depth: tokens flowing through layers, an embedding space, attention links, a rack of GPUs as a model. Same world as the motion plates so they cut together without a jump.

- **Ground and light:** the ink ground composited behind the scene (transparent film), one soft key and one rim light, gentle bloom on emissive parts (`bloom` 0.4 to 0.8). No fog, no lens flares, no chrome.
- **Palette in 3D:** the semantic colours above. Surfaces are shaded by height in one hue (`ramp` ink, haze, signal: valleys dark, only rims lit), so a landscape reads as data and the hero pops; **the hero glows ember** (`emit` 2 to 4); `cream` for words on tiles; a thin slate grid at low emission. The thing the voice names pulses (`pulse`, `fire`) on its word.
- **Camera:** one slow move per plate (a dolly in or a quarter orbit, lens 35 to 50), always toward the part being named; never a spin for its own sake, never a cut inside a plate.
- **Text never moves in 3D** (user, 26 Oct 2026, on the CSS-3D prompt-injection cut: *"Theres no point on using the tiles that way, no 3d movement on text element"*): captions, cards, labels, emails and buttons stay flat and face the camera; a label may follow a 3D object only by sliding in 2D (projected position). Words are not shown as tiles flowing in depth: a word in a 3D world is an object (a capsule) whose meaning comes from its colour and a flat label. The depth, orbit and rhythm belong to objects (three.js in HyperFrames, or `scene3d.py`). `scene3d.py` warns for text in the caption band and interface zones.
- **Faithful:** a 3D network or embedding cloud is marked "schematic" in Status; counts are illustrative unless the research note gives them (a real model has billions of weights, the plate shows a dozen nodes).

**Lanes** are the [[Design system]] zones (STAGE, BAND, DECK, interface). TikTok covers more of the bottom 15 to 20 %: unverified, test once with a private upload and, if needed, raise `CAP_Y` for a TikTok export (`plan.json`) without touching the YouTube master.
