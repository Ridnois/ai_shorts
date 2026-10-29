---
type: research
created: 2026-10-26
updated: 2026-10-26
status: v1 · P1 to P4a done by delegation; off-niche one-off (user's choice); first video built with HyperFrames
tags: [research, youtube, script, hardware, week-04]
---

# Script · ThinkPad TrackPoint (Week 04, Mon 26 Oct)

← [[ThinkPad TrackPoint - Status]] · [[YouTube Channel]] · [[Format]] · [[Growth]]

User (26 Oct 2026): *"Make a new short with hyperframes https://github.com/heygen-com/hyperframes topic: Why thinkpads are so special"*. At the idea gate the user chose **"One-off, mechanism angle"**: off the AI niche (no series; it is not counted in the series rotation) but built as **How it works** (hook, definition, origin, explanation on one running example, turn, close). Not compact (the last video was compact).

**Y:** know why people swear by ThinkPads. **X:** the red dot never tracks motion; it reads force, and IBM shaped force into speed in zones (dead band, one slow speed, a top speed capped at what the eye can follow). **Theme line:** *how hard you push.* **One question:** how does a dot that barely moves steer a cursor?

## 0. Facts bank (**read** = opened 26 Oct 2026)

| # | Fact | Source |
| --- | --- | --- |
| 1 | TrackPoint is isometric: it responds to sustained force, not movement; two pairs of resistive strain gauges sense it; more force, faster pointer | Wikipedia "Pointing stick" (**read**) |
| 2 | Ted Selker built a pointing-stick model at Xerox PARC in 1984 to cut keyboard-to-mouse switching; refined it at IBM about three years later | Wikipedia "Pointing stick" (**read**; the 0.75 s switching figure is "citation needed": not used) |
| 3 | First laptop with a pointing stick: ThinkPad 700 series, launched 5 Oct 1992 | Wikipedia "ThinkPad", "ThinkPad 700" (**read**) |
| 4 | Rutledge and Selker (IBM) patent US5764219 (priority 25 Sep 1992): velocity vs force curve with a dead band so "the cursor sit steady even though the user has fingers on the joystick" | Google Patents US5764219A (**read**) |
| 5 | Same patent: a low plateau gives "predictable slow motion for moving the cursor short distances under smooth control" | US5764219A (**read**) |
| 6 | Same patent: a high plateau "limits the cursor speed to a speed which can be tracked by the human eye"; above it, a fast dash (e.g. to a menu) | US5764219A (**read**) |
| 7 | Patent values: velocity scale 1,500 pixels/s, force scale 225 g, force sampled 100 times a second | US5764219A (**read**; not used) |
| 8 | TrackPoint II firmware: sigmoid transfer function with a dead zone, 8-bit force input, inputs 0 to 3 give no motion | US5570111A background (**read**; not used) |
| 9 | Negative inertia: "amplifies changes in applied force"; the cursor may "back up" slightly at the end of a motion; added in TrackPoint III | Barrett, Selker, Rutledge, Olyha, CHI '95, IBM Almaden (**read**) |
| 10 | Negative inertia improved pure pointing 7.8 ± 3.5 % (9 subjects, p < 0.005); 9.4 % on 3 mm targets; 10 of 16 preferred it | CHI '95 (**read**) |
| 11 | Users thought negative inertia had higher gain; "the gain was actually the same" | CHI '95 (**read**; not used) |
| 12 | Richard Sapper's 1990 design: a Japanese bento box (also compared to a black cigar box) | Wikipedia "ThinkPad" (**read**; not used) |
| 13 | IBM first told Sapper he could not use red: it was the colour of the mainframe emergency-off button | Time, "Lenovo ThinkPad 25" (search excerpt, not opened; not used) |
| 14 | NASA bought 500+ ThinkPad 750s; a 750 flew on the 1993 Hubble repair mission | Wikipedia "ThinkPad" (**read**; not used) |
| 15 | Over 200 million ThinkPads sold by 2022; Lenovo bought IBM's PC business in 2005 | Wikipedia "ThinkPad" (**read**; not used) |
| 16 | Most studies find touchpads slightly faster than pointing sticks (e.g. 1.7 s vs 2.2 s selection) | Wikipedia "Pointing stick", citing Sutter and Ziefle (**read**; not used, a counter-view for comments) |

## 1. Idea gate

**Scores:** surprise 4 (a dot that does not move steers by force) · scale 3 · depth 5 (patent zones, eye-speed cap) · evidence 5 (patents, CHI paper) · showable 5 · plain 4. **Street-lamp:** pass: "why ThinkPads are special" headlines answer with durability and keyboards; the video adds the force-to-speed zones and the eye-speed cap. **Expert test:** the high plateau set to what the eye can track; negative inertia making the cursor back up. **Coffee test:** *"The ThinkPad's red dot reads how hard you push and turns it into speed, capped at what your eyes can follow."* **Against:** (1) "I use a touchpad" → the closing question invites the debate; (2) "old tech" → it still ships on ThinkPads; (3) "not AI" → the user's one-off. **Demand check:** `youtube_search.py` failed (HTTP 400, as on 23 Oct); YouTube autocomplete on 26 Oct 2026 offers "why are thinkpads so good", "why are thinkpads so popular", "thinkpad trackpoint how to use", "thinkpad red dot": the bridge is Y (why ThinkPads) to X (the TrackPoint). **Original synthesis:** the patent curve redrawn as one chart the cursor rides, zone by zone.

**Five hooks:** contradiction "The red dot on a ThinkPad barely moves. It reads how hard you push, and here is how that steers your cursor." (**used**) · question "Why do ThinkPad owners refuse to give up the red dot?" · fact "A ThinkPad caps your cursor at the speed your eyes can follow." · stakes "Your hands never leave the keys on a ThinkPad, because of one red dot." · number "In 1992 IBM put a pointing stick in a laptop for the first time."
**Hook test (used):** plain · named (the red dot on a ThinkPad) · reason to care (it steers without moving) · open question (how?) with the promise "here is how" · sound-off (DOT caption over the laptop, push and speed bars moving) · honest · matches the package.

## 2. Package

- **Promise:** why the ThinkPad's red dot is special: it steers by force, shaped into speed zones.
- **Titles:** *The ThinkPad Red Dot Doesn't Move. Here's How It Steers* (recommended) · *Why ThinkPads Are So Special: the Red Dot Explained* · *Your ThinkPad Caps Your Cursor at Eye Speed*.
- **Thumbnail (at P8):** the drawn ThinkPad with the ember cap and the push-to-speed curve rising behind it; words "IT DOESN'T MOVE". Beats neighbours (keyboard and durability reviews) by showing a mechanism, not a laptop.
- **Opening map:** scene 1 promise · scene 2 definition and proof (strain gauges, real photo) · scene 4 plan ("Here is how").

## 3. Script: 170 words, 8 scenes (take v1: 60.6 s)

| Sc | Question it answers | Voice (exact text) | Delivery · pause |
| --- | --- | --- | --- |
| 1 | (hook) | The red dot on a ThinkPad barely moves. It reads how hard you push, and here is how that steers your cursor. | plain, intrigued |
| 2 | what is it? | It is called the TrackPoint. Under the cap, tiny strain gauges measure how hard, and which way, you press. | steady |
| 3 | where did it come from? | Ted Selker designed it so typists never leave the keys, and IBM shipped it on the first ThinkPads. | warm |
| 4 | how does it work? | Here is how. Say you spot a typo two lines up. A light touch does nothing, so a resting finger never nudges the cursor. | step by step |
| 5 | and a little more? | Push a little harder, and the cursor creeps at one slow, steady speed, slow enough to land on a single letter. | slow |
| 6 | and pushing hard? | Push hard, and it speeds up, but only to the fastest speed your eyes can follow, so you never lose it. | rising; break 0.2 after "follow" |
| 7 | is that all? (turn) | Later TrackPoints even overreact as you start and stop. In IBM's tests, that made pointing about eight percent faster. | amused |
| 8 | so what? | So here is the point: a ThinkPad steers by how hard you push, tuned to your eyes. Would you trade your touchpad for that? Tell me. | slower; break 0.2 after "eyes" |

**Honesty:** "barely moves": isometric, deflection is microscopic. "first ThinkPads": the 700 series of Oct 1992. The zones are from Rutledge and Selker's IBM patent; shipping firmware curves differ by generation (schematic, Status). "about eight percent": 7.8 ± 3.5 %, 9 users, pure pointing, on screen with source. Facts used: 5.

## 4. Beat sheet, prefix `tp` (one running example: the typo "teh")

1 drawn ThinkPad at frame 1, cursor already moving, push and speed bars live; rings on "reads", bars jump on "hard", stop on "here", glide to "teh" (turns rose) on "steers" · 2 photo of the stick module (cap off), label "TrackPoint" on "track point", zoom on "Under" · photo of the four sensing elements, rings land on "strain gauges", "4 strain gauges, 2 pairs"; arrow right on "which way" (right gauge bright), swings up on "press" · 3 photo of a ThinkPad 720C (1993) with slow push to the red dot; card "Ted Selker" on "Selker"; card "ThinkPad 700 ships · 5 Oct 1992" on "IBM" · 4 doc window with "teh" two lines up (rose underline on "typo", dashed path on "two"); chart axes; marker in the dead band on "light", label "dead band" · 5 low plateau draws on "Push", cursor creeps the path on "creeps", lands on the letter on "letter" · 6 rise and high plateau draw, cursor dashes to Edit with a signal trail, eye follows on "eyes", ring on "lose" · 7 speed trace (schematic): standard vs negative inertia spike and dip on "start"/"stop"; bars "time to hit a target", 7.8 % shorter on "eight" · 8 the ThinkPad again, "teh" fixed to "the" in mint; conclusion card "Pressure in, speed out"; margin note "TrackPoint or touchpad?" on "Would".

## 5. Not verified

The black elements in the sensor photo are read as the strain gauges from Wikipedia's "two pairs" and their layout, not from a datasheet. The 1984 PARC start is Wikipedia's (one secondary source). Demand beyond autocomplete. How the voice sounds. P7 is the user's.
