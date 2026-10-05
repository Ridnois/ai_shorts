---
type: research
created: 2026-10-05
updated: 2026-10-05
status: decided (name, logo, slogan, banner); channel description options waiting for the user's pick; open: avatar, handle, trademark
tags: [brand, youtube, redtail]
---

# Brand register: Redtail (decided 5 Oct 2026) and archive

Context: the channel's brand was designed in one session from the user's [[Logo references]] (NFL animal logos, round club crests). The decision lives in [[Channel playbook]] §4; this note is the register of the final assets and of what was rejected.

## Decided

| Item | Decision | Source of the decision |
| --- | --- | --- |
| Name | **Redtail** | *"Redtail it is"* |
| Slogan | **SCIENCE AT FULL SPEED.** / second line **STRANGE, FAST AND TRUE.** | *"Banner b is the winner"* |
| Positioning | **science entertainment**; sourcing is a rigor rule in descriptions, not a slogan | *"Dont focus on 'science media with sources' make it more like 'science entertainment'"* |
| Logo | NFL-style snarling profile fox head in a ring, slanted italic block wordmark, bushy cream-tipped tail curling behind it | *"I like 2"* (style) |
| Palette | oranges, cream white, navy | *"i like orange"* |
| Use | channel page only (logo, banner, avatar); never inside a Short ([[Channel playbook]] §4) | |

![[System/Brand/Redtail/redtail-logo.png|300]] ![[System/Brand/Redtail/redtail-banner.png|520]]

| File | What | Made by |
| --- | --- | --- |
| `System/Brand/Redtail/redtail-logo.png` | 1024², transparent | `System/scripts/gen_redtail_logo.py` (`gpt-image-1.5`, ≈ $0.05, prompt inside) from `redtail-style-reference.png` (the winning logo style, the only image fed back) |
| `System/Brand/Redtail/redtail-banner.png` | 2560 × 1440, crest left, slogan right, navy yard-line field, orange base stripe | `System/scripts/make_redtail_banner.py` (local PIL, free) |
| `System/Brand/Redtail/redtail-style-reference.png` | the winning style-2 logo, kept as the reference for any redraw | |

## Open

- **Avatar:** not made. The wordmark does not survive a small circular crop; it needs a head-only version (about 800 px, plain background). Free if drawn locally from the logo, ≈ $0.05 if regenerated.
- **Handle, existing channels, trademark:** unverified (the fetch tool cannot read YouTube; a web search found no science channel named Redtail, which is not proof). Try `@redtail`, `@redtailscience`, `@watchredtail`, `@redtail.science`.
- **Colour:** the generated art leans red rather than orange; a regeneration with "warm orange, not red" would fix it (≈ $0.05, over the logo cap).
- **Banner safe area:** 1546 × 423 is from memory; check Studio's preview on TV, desktop and phone. Legibility at 48 px is unchecked.
- **Cost:** ≈ $0.05 per generated image is OpenAI's rate; Replicate's `metrics` carry no cost, so check the dashboard. The brand work in total ran about 17 `gpt-image-1.5` predictions (≈ $0.85, unmeasured).

## Archive (rejected candidates, text only)

The images, the generator scripts of the rejected rounds and the old avatar and banner were deleted; **they were not committed to git, so they cannot be recovered** (the prompts survive only in the idea lines below).

- **Names round 1:** Cutaway (first brand: copper geometric fox, "Science, cut open. With sources."; dropped, *"cutaway is not making it"*), Foxplained, Kitfox Science, Fennec Lab, Copper Fox. Pet-name mascots (Cutter, Rusty, Kit, Fenn, Coppa) and the football-jersey mascot brief were dropped: the user wanted a logo, *"now pet name"*.
- **Names round 2:** Vulpine (many channels named Vulpine…, one in biotech), **Fox Theory** (a YouTube channel "Fox Theory" exists, an indie-punk band; echoes MatPat's "Game Theory"), Foxfield, Redshift (crowded with software), Atomic Foxes. Also rejected on search: Gridfox (an agency making explainer videos), Foxglove (a science-explainer channel and a robotics company).
- **Names round 3:** Reynard, Brushfire, **Redtail (chosen)**.
- **Logo options** (all five had "CUTAWAY"): 1 round crest with a front fox and stars (friendly, closest to club crests); **2 snarling NFL profile in a ring with a slanted wordmark (winner)**; 3 shield with the fox half solid, half blueprint (carries the cutaway idea, busy); 4 Bears-style C with the fox inside (clean silhouette); 5 leaping fox in swoosh style (dynamic, a banner mark). An earlier round of five local vector drawings (crest, profile, shield, monogram, orbit) and a first Replicate round (grey glow instead of the asked navy background) were discarded. Lesson: **ask `gpt-image-1.5` for `background: transparent`** to avoid the glow.
- **Banners:** a first set (A crest + tagline; B fox head + wordmark + tail underline on orange; C fox leap on speed lines) was replaced by three with one design and different slogans. Rejected slogans: FOLLOW THE TAIL. / SCIENCE THAT'S FUN TO WATCH.; SCIENCE WITH TEETH. / ONE WEIRD MECHANISM PER SHORT. Retired sourcing-led slogans: FOLLOW THE TAIL. / SCIENCE, EXPLAINED WITH SOURCES.; NO HYPE. JUST THE MECHANISM.; CHECK THE NUMBERS.

## Channel description options (5 Oct 2026, waiting for the user's pick)

User: *"Write 3 options for the channel description, same procedure, register and cleanup after i decide"*, then: *"I like the \"New shorts every week\" but instead of listing examples, you should generalize the style of the content on one phrase, consider the last 4 only, thats the real context"*. The last four videos in [[YouTube Channel]] are Magnetar, Moon, Superconductors and Asteroid mining: all English Shorts of about a minute on the extremes of space and physics, with real NASA or Commons photos and faithful schematics. **One phrase for the content: "the strangest things in space and physics and how they actually work"**; no example list (the first draft's topic list is gone). **"New Shorts every week" is the chosen cadence.** Rules applied: **science entertainment** first, sourcing only as a plain line ([[Channel playbook]] §4); the AI-voice and AI-schematics disclosure stays ("Honest about machines"); YouTube allows 1,000 characters; none of the banned words ([[Channel identity]]).

**Option 1 · punchy (259 characters)**

> Science at full speed.
>
> Redtail explains the strangest things in space and physics and how they actually work, one mechanism per Short, in about a minute.
>
> New Shorts every week. Figures are sourced in each description; voices and schematics are AI-generated.

**Option 2 · the fox's voice (346 characters)**

> Follow the tail.
>
> Redtail is a fox with a thing for the strangest things in space and physics. Every Short follows one idea from the first question to the last surprise, with real photos and clean schematics.
>
> Strange, fast and true. New Shorts every week. Voices and schematics are AI-generated; every figure is sourced in the video description.

**Option 3 · search first (361 characters)**

> Short science explainers on the strangest things in space and physics and how they actually work, in about a minute.
>
> Redtail follows one surprising mechanism per video with real photos and faithful schematics. Science at full speed. Strange, fast and true.
>
> New Shorts every week. Sources are listed in each description. Voices and schematics are AI-generated.

Agent's view: **1** is the shortest and the closest to the banner; **2** has the most personality but personifies the fox (a mascot, not a fake expert); **3** opens with the plain-words topic, the best for search. Caveat: the phrase narrows the channel to space and physics, while the playbook's audience still lists materials, biology and the body (and older videos cover chips, helium and a lemon cake): if the channel will widen again, the phrase must widen too. Nothing is applied to the channel; the playbook's "Channel description template" is updated after the pick.
