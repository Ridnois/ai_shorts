---
type: research
created: 2026-10-04
updated: 2026-10-04
status: v3 · in-video branding removed (progress bar, mark, series tag: Superconductors feedback, 4 Oct 2026); v2 name, avatar, banner and sound design; v1 requested by the user (4 Oct 2026); YouTube statements fetched from YouTube Help that day, everything marked "hypothesis" is untested on this channel
tags: [research, youtube, engagement, design, branding, mission, guidelines]
---

# Channel playbook: engagement, on-screen design, brand and mission

← [[YouTube Channel]] · [[Channel strategy]] · [[Shorts quality bar]] · [[On-screen text style]] · [[Channel identity]]

> **User request (4 Oct 2026):** *"go deeper on youtube guidelines, show me on a note the strategy for good engagement, the design of the text boxes, highlight and any support on the video, the channel branding and mission of the channel."* [[Channel strategy]] holds money and policy; this note holds what makes people stay, how the screen looks, and who the channel is.

## 1. What YouTube itself says (verified 4 Oct 2026, YouTube Help and How YouTube Works)

| Statement                                                                                                                                                                                                                        | Source                                     | What it means for us                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Recommendations use *"viewing behavior, likes, dislikes, subscriptions, and feedback, including from satisfaction surveys"*, and *"the reputation and the quality of a channel"*                                                 | How YouTube recommends videos              | There is no trick: viewers staying and being satisfied, and a channel with a clean, consistent reputation. Every rule below serves those two                |
| Since **31 March 2025** a Shorts view is *"the number of times a Short starts to play or replay, with no minimum watch time"*; **"Engaged views"** is the separate measure and monetization is based on **Engaged Shorts views** | YouTube Help, Shorts views                 | A raw view count says little; **engaged views and the share who stay** are the numbers to read ([[Channel strategy]] §6)                                    |
| The retention graph: flat = watched, gradual slope = normal, **spikes = rewatched or shared**, **dips = stopped watching**; it needs ≥ 60 s and 100 views and **does not document Shorts**                                       | YouTube Help, audience retention           | Read it on the long videos; for Shorts use engaged views and compare Shorts to each other                                                                   |
| Titles: *accurate, succinct, key words first, limit ALL CAPS and emoji*; two kinds work, **searchable** and **intriguing**; *90 % of the best-performing videos have custom thumbnails* (general videos, not Shorts)             | YouTube Help, thumbnail and title tips     | Shorts titles are searchable statements; long videos get a custom thumbnail                                                                                 |
| **Malicious clickbait** (titles, descriptions or imagery that do not deliver what they promise) and technical tricks to evade detection are spam, punished with strikes, loss of monetization or termination                     | YouTube Help, spam and deceptive practices | A hook promises only what the video then shows; never a tease the video does not pay                                                                        |
| Content with a clear **educational, documentary, scientific or artistic (EDSA) context** can be an exception under community rules                                                                                               | How YouTube Works, Community Guidelines    | Sources on screen and in the description *are* the EDSA context                                                                                             |
| Captions let a video reach *"a larger audience, including deaf or hard-of-hearing viewers and viewers who speak another language"*; a caption **file can be uploaded**, with position and style                                  | YouTube Help, subtitles                    | Burned-in captions serve the silent viewer; **also upload the `.srt`** the builder writes (`render/<prefix>.srt`) for search, translation and accessibility |
| Realistic synthetic content must be disclosed ([[Channel strategy]] §3)                                                                                                                                                          | How YouTube Works                          | no photoreal fakes                                                                                                                                          |

**Not found in the official pages (so not claimed):** any Shorts-specific ranking weights, an ideal length, a posting time, or a hashtag effect. Those circulate as folklore; test them with our own data.

## 2. Engagement strategy

**Principle:** engagement is a *result of the viewer's time being well spent*, not a request. The channel never asks for likes, never says "subscribe", never ends on a call to action ([[Narration guide]]). It earns them with the sequence below. Rules marked **(H)** are hypotheses to test; the others follow from §1.

| Moment            | Goal                                                  | What we do                                                                                                                                                                                                                  |
| ----------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0 to 3 s**      | the viewer does not swipe                             | need-to-know claim ≤ 10 words, the strongest real image, first word captioned at once ([[Shorts quality bar]] §1)                                                                                                           |
| **3 to 20 s**     | the viewer sees the question is answered step by step | one idea per scene, cause then effect; a new image every ≈ 3 to 4 s, with callouts and cards on top                                                                                                                                        |
| **Middle**        | a reason to keep watching                             | a **number the viewer wants to check** (rewatch spike, H), a surprise that reverses an assumption ("the record needs 1.5 million atmospheres")                                                                              |
| **Close**         | the idea sticks and the video **loops**               | one idea to finish alone; the last plate is the first plate again (H: a seamless loop raises replays, which count as views)                                                                                                 |
| **After**         | comments, trust, subscribers                          | **pinned comment with the sources and one corrections line**; answer every serious comment within a day, in the specialist's voice; a question in the description that has a checkable answer, not "what do you think?" (H) |
| **Across videos** | a reason to subscribe                                 | series with fixed formats ([[Channel strategy]] §4), playlists per series, each description links the next video of the series, the long video links back to its Shorts                                                     |

**Loop of improvement:** after 48 hours and 7 days write into the Status note engaged views, share who stay (Studio), subscribers gained, comments; after every 10 Shorts run [[Feedback loop]] on the data. **Never** buy views, use engagement groups or mislead in titles (§1).

**Titles for Shorts (H, from YouTube's title advice):** a statement with the subject first: "Superconductors carry current with zero resistance", not "You won't believe…". ≤ 60 characters; no all caps; no emoji; the claim is in the video within 10 seconds.

## 3. On-screen design system (what the viewer sees besides the picture)

The style is approved (*"good and appealing"*, Magnetar feedback). This section writes it down as a system so every video matches. Numbers are those of `build_video.py` for 1080×1920.

### 3.1 Tokens

| Token              | Value                                                                                                              | Use                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| Paper              | `#F9F6EE` at 94 %                                                                                                  | the card and callout boxes                                                             |
| Ink                | `#1C1A17` / soft `#4D4741`                                                                                         | text on paper                                                                          |
| **Copper**         | `#C76B38`                                                                                                          | the signature: callout dots and lines, card bar, big figures, copper words in captions |
| Caption white      | `#FFFFFF`, outline `#0A0907`                                                                                       | captions only                                                                          |
| Titles and figures | Noto Sans Display Bold                                                                                             | cards, captions                                                                        |
| Labels and details | Noto Sans Regular                                                                                                  | callouts, card details                                                                 |
| Gradients          | one family per topic (cold blue cryogenics, warm copper energy, deep green materials), dark enough for paper boxes | behind `contain` photos and cutouts only, **never bare**                               |

### 3.2 Components

| Component          | Spec                                                                                                                                                               | Used for                                                        | Limits                                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Context card**   | 894 × 280 px, 16 px corners, 8 px copper bar on the left, centred at 28.5 % from the bottom; label 32 px spaced capitals in copper, title 56 px bold, detail 34 px | frame and source a fact (place and date, the claim, the source) | title ≤ 26 characters; detail ≤ 40; one card per plate                                                         |
| **Number card**    | same box; **figure 124 px bold copper**, caption 44 px bold, source 30 px                                                                                          | the one figure the argument rests on                            | one per video as the main number; others only if each carries a scene (Superconductors uses four, all sourced) |
| **Margin note**    | same box, label "Margin note", two lines ≤ 30 characters, 46 px bold                                                                                               | the specialist's dry aside                                      | ≤ 2 per video                                                                                                  |
| **Callout**        | copper dot (13 px) with a ring, 2 px leader line, paper label with a copper bar, 34 px text; enters 1 s after the plate, 0.6 s apart                               | **name a real part** of the photo or schematic                  | 1 to 3 per plate; 1 to 4 words; the dot sits on the part; labels never cover the card or the caption zone      |
| **Caption**        | one word at a time, 88 px bold capitals, white, dark outline and shadow, centred at 16.5 % from the bottom; long words shrink                                     | the silent viewer follows the whole script                      | figures copper; **key terms copper** (`keywords` in `plan.json`, ≤ 6 per video); a word holds until the next   |
| **Highlight rule** | copper means "this is the thing to remember": a figure, a key term, a dot                                                                                          | the eye learns one signal                                       | never highlight more than one word in three; never two colours of emphasis                                     |
| **Motion**         | cards and texts fade in 0.25 s with a 24 px rise, out 0.2 s; plates push 5 %; cross-fade 0.3 s within a scene, short dip between scenes                            | calm, readable motion                                           | no shakes, no flashes, no zoom punches                                                                         |

### 3.3 Safe zones (Shorts interface)

Top 10 %: free (the title bar). Subject between 15 % and 60 % of the height. **Card zone 21 % to 36 % from the bottom. Caption zone ≈ 16.5 % from the bottom (centre).** The last ≈ 15 % and the right edge carry YouTube's own text and buttons: nothing essential there. **TikTok and Reels cover more of the bottom; test one video and move `CAP_Y` per platform** ([[Channel strategy]] §5).

### 3.4 Other supports on the video

| Support                                                                         | Status                                                                             |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Word-by-word captions                                                           | built ([[Blender editing]])                                                        |
| `.srt` caption track for upload                                                 | built (`render/<prefix>.srt`, 5 words per cue)                                     |
| Source tags on cards                                                            | built                                                                              |
| **Progress bar, brand mark, series tag** | **removed** (Superconductors feedback, 4 Oct 2026: brand layer rated 0, *"unnecessary, should be removed"*; *"no progress bar nor branding"*). The video carries no branding; the brand lives in the channel page, the name and the recurring look of the cards |
| **Quiet drone bed**                                                             | built, synthesized (A minor, ≈ −37 dBFS), user request 4 Oct 2026; a licensed music track stays opt-in ([[Guidelines for new scripts]] §3)   |
| **Sound design** (whoosh, ticks, pings, opening thump)                          | built, synthesized, on by default; **not heard by the agent** ([[Blender editing]] §Sound design)         |

## 4. Mission, brand and identity (proposal; the user decides)

**Mission (one sentence):** *Make the machinery behind the headlines understandable in a minute, with the sources on screen.*

**Promise to the viewer:** you will leave knowing *how* something works and *why* it is hard, and you can check every number.

**Audience:** curious adults who like physics, engineering and materials; they do not want hype and they notice mistakes.

**Brand pillars (each is a rule the vault already enforces):**

| Pillar                    | Meaning                                                               | Where it is enforced                                |
| ------------------------- | --------------------------------------------------------------------- | --------------------------------------------------- |
| **Precise**               | every figure sourced and dated; weak facts attributed                 | [[Guidelines for new scripts]] Rigor                |
| **Surprising**            | the chosen angle scores ≥ 4 on surprise and scale                     | [[Idea and hook quality]]                           |
| **Calm**                  | no hype words, no shouting, no false urgency                          | [[Channel identity]] banned words                   |
| **Honest about machines** | says when the voice and the schematics are AI, and what is simplified | description template, Status "known simplification" |
| **Real over decorative**  | real photos for real things, faithful schematics for hidden things    | [[Illustration pipeline]]                           |

**Voice:** the curious specialist ([[Channel identity]]): tells you what you need to know, never narrates a story.

**Visual identity:** copper accent on paper-white boxes over real images, Noto Sans Display Bold, one gradient family per topic, the **callout dot with its ring as the logo mark** (a copper dot inside a thin ring on a dark ground: it is already the channel's recurring device). Avatar: that mark. Banner: the mark, the one-line mission, a photo-and-callout crop.

**Name: Cutaway.** Tagline: **"How it works. With sources."** (user, 4 Oct 2026: *"the mission is good, invent something catchy and well positioned for channel name"*.) Why it fits: a *cutaway* is the diagram that cuts the outside away to show the inside, which is exactly what the channel does with a mechanism (the schematics and the callouts that name the parts); it is one word, easy to say and spell, and it says nothing about physics only, so it survives the move to materials, biology or software. Wordmark: "Cutaway" in Noto Sans Display Bold, paper-white on ink, with the copper ring-and-dot to its left.

**Handle (not verified):** the fetch tool cannot read YouTube channel pages, so **availability on YouTube, TikTok and Instagram is unchecked**. Try in this order in YouTube Studio: `@cutaway`, `@cutawayhq`, `@watchcutaway`, `@cutaway.science`; use the first free one on all three platforms. YouTube handles are unique and the name or handle can be changed twice per 14 days (verified, YouTube Help). Fallback names if "Cutaway" is taken or too crowded: **Part Names**, **Show the Part**, **Teardown Minute**. **Trademark and search crowding are not researched**: search "Cutaway" on YouTube before committing.

**Brand assets** (channel page only; drawn by `System/scripts/make_brand.py`, kept in `System/Brand/`):

| File | Use | Design |
| --- | --- | --- |
| `avatar.png` (800 px) and `avatar.svg` | profile picture | an annotation: a copper ring with a dot, a leader line, a paper label with two text lines, on a dark ground that fades from ink to the cryogenic navy; centred inside the circular crop |
| `banner.png` (2560 × 1440) | channel banner | ring-and-dot, "Cutaway" and the tagline, centred in the middle safe area (**YouTube's 1546 × 423 safe-area size is from memory, not verified**: check the Studio preview) |

**The Short itself carries no branding** (no progress bar, mark or series tag; removed on the user's feedback). It stays recognisable through the cards, callouts, copper highlight and captions (§3.1). Series names (The mechanism, The number, The catch) are content formats for playlists and descriptions only. *Interpretation to confirm:* the feedback row called "Brand layer" listed avatar and name too; the agent read the verdict as **about the video**, and kept the channel's name, avatar and banner (the channel page needs them).

**Channel description template (about 3 lines, searchable words first):** *[Mission sentence]. New Short every [cadence]: [series names]. Every figure is sourced in the description; voices and schematics are AI-generated.*

**Recurring devices** (what makes a clip recognisable even without the logo): the copper dot, the number card, the margin note, the part-name callouts, the closing idea ([[Channel identity]] §2).

**What the channel does not do:** clickbait, fake experts or AI personas giving advice, photoreal fakes of real events or people, copied scripts, template videos where only the topic word changes ([[Channel strategy]] §2).

## 5. Open decisions for the user

- Approve or change the mission sentence and the five pillars.
- Confirm the name **Cutaway** and the tagline, then check the handle (above); look at `System/Brand/avatar.png` and `banner.png`.
- The three series names (The mechanism, The number, The catch), used only as playlist names.
- Whether Shorts titles follow §2, and whether long videos get custom thumbnails ([[Channel strategy]] §4).
- Listen to the first Short's sound design (the agent cannot): too loud, too busy, or fine? The levels are plan parameters.

## 6. Not verified

YouTube pages gave signals and definitions, **not tactics**: every engagement tactic marked (H), the ideal pacing, the loop effect, the title length, the pinned-comment effect and the safe-zone numbers of other platforms are hypotheses. The retention-graph page does not cover Shorts. Test one change at a time and write the result in the Status notes.
