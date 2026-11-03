---
type: script
updated: 2026-11-03
---

# Script: How AI uses your computer

← [[How AI uses your computer - Status]] · [[Story]] · [[Picture]] §Medium

**Promise:** you will see what an AI agent actually gets from your screen (a photo) and what it sends back (two numbers).
**Pattern:** `surprising-result` (an agent can't see buttons) · **Series:** Agent at work · **Main medium:** capture (a real recorded run).

## Package

| | |
| --- | --- |
| Title | How AI Uses Your Computer: It Only Sees a Photo |
| Alternatives | Claude Can't See Your Buttons. Here's How It Clicks · How AI Agents Click: Screenshot, Guess, Repeat |
| Frame-0 text | IT CAN'T SEE BUTTONS |
| Thumbnail | the Wikipedia screenshot with a yellow crosshair at 469, 27 · "IT SEES A PHOTO" |
| Field (nearest [[Radar]] / Niche outliers) | "Put Claude to work on your computer" (NAauIR6JFps, 5.99 M, 92x); "How OpenClaw takes over your computer" (9DxXDLhXnwU, 876 k, 3.8x): both promise the result; ours promises the mechanism with a real run, which neither shows |

## Voice (exact text)

| Scene | Beat | Voice | Words | Viewer sees happen | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | Hook | The AI clicking around your screen can't see a single button. | 11 | the real screenshot with the crosshair landing on 469, 27 | run 2, step 1 |
| 2 | Stake | It sees a photo, and every click is a guess in pixels. A wrong guess clicks the wrong thing. | 19 | the screenshot turns into a pixel grid; the loop spine LOOK, THINK, CLICK appears | Anthropic docs (below) |
| 3 | Mechanism | So I gave Claude one goal: find how tall the Eiffel Tower is. | 12 | the goal typed as a tag; the phone with Wikipedia; tag "Claude Opus 5.5 · 3 Nov 2026" | run 2 |
| 4 | Mechanism | It gets a screenshot, and it answers with two numbers. Click at four sixty-nine, twenty-seven. That's the search icon. | 19 | the reply as token chips `{"click", 469, 27}`; the camera pushes to the icon | run 2, step 1 log |
| 5 | Mechanism | It types Eiffel Tower, then it looks again. Every look is a new photo, and about five seconds of thinking. | 19 | step 2 and 3 screenshots; the spine lights LOOK again; a counter to 5 s | run 2 latencies 4.2 to 7.3 s |
| 6 | Turn | But in my first run, a banner pushed the page down. Same icon, new photo, and Claude clicked at two seventy-seven. It never knew the button. It found it in the picture. | 32 | run 1 and run 2 side by side: the same icon, crosshairs at y 27 and y 277 | run 1, step 1 log |
| 7 | Mechanism 2 | Then the height sat below the edge of the screen, and it told me it couldn't see it. Give it a scroll, and it read the answer: three hundred thirty metres to the tip. | 33 | run 1's real reply in a terminal; then the scroll steps; the infobox crop "330 m (1,083 ft)" | run 1 step 3, run 2 step 5 |
| 8 | Payoff | So close what you don't want it to read, because to an agent, your whole screen is one photo. | 19 | the spine complete; back to the frame-0 screenshot | Anthropic docs (prompt injection) |

167 words. Turn at about 48 % of the words (scene 6), a second reversal at 70 % (scene 7).

## Sources (checked 3 Nov 2026)

- **Our runs** (`Media/…/How AI uses your computer/run/`, `agent.mjs`, 3 Nov 2026): Claude Opus 5.5 (`claude-opus-5-5`) through `claude -p` with the Read tool only, one 540×960 screenshot per step, one JSON action in screenshot pixels, puppeteer clicking; mobile English Wikipedia. Run 1: click 469,277 (an app banner on top), type, then "the height row in the infobox is below the fold, and I have no scroll action to reach it" (it answered 330 m from memory, flagged as such). Run 2 (scroll allowed): click 469,27; type; scroll 600; scroll 700; done "300 m (984 ft) architectural; 330 m (1,083 ft) to the tip, per the Wikipedia infobox". Think times 4.2, 4.3, 4.2, 5.9, 7.3 s (median 4.3 s; "about five seconds" is the rounded run mean, 5.2 s).
- **Anthropic computer use docs** (platform.claude.com/docs/en/docs/agents-and-tools/tool-use/computer-use-tool, read 3 Nov 2026): `screenshot` "Capture the full display and return it as an image"; "Coordinates are in screenshot pixels … with the origin at the top left"; "instructions on webpages or contained in images might override your instructions".
- **Anthropic, 22 Oct 2024** (anthropic.com/news/3-5-models-and-computer-use): computer use launched with Claude 3.5 Sonnet, "by looking at a screen, moving a cursor, clicking buttons, and typing text". Not used in the voice.

*Not verified:* how the production computer-use tool (not `claude -p` with screenshots) scales or crops; our harness is our own, built on the documented mechanism.

## Beat sheet (spine: the `loop` primitive LOOK · THINK · CLICK; moves borrowed from [[Shots]])

Borrowed: **open on the finished picture** ([[Welch Labs - The efficient compute frontier]]): frame 0 is the screenshot with the crosshair already on the icon. **A running scorecard / spine** ([[Jeff Su - AI Agents explained in 3 steps]]): the loop returns in scenes 2, 5 and 8 with the current step lit.

| Cue | Imp. | Medium | Picture event | Camera | Trans. | Text | Sound |
| --- | --- | --- | --- | --- | --- | --- | --- |
| frame 0 | 3 | capture | screenshot, crosshair on icon, "469, 27" | medium | – | IT CAN'T SEE BUTTONS | hit |
| photo | 2 | primitive | loop spine lands, LOOK lit | wide | push | – | pop |
| pixels | 2 | capture | the screenshot zooms to the icon, pixel blocks | close | – | – | whoosh |
| goal | 1 | capture | phone with the main page, goal tag | medium | whip | Claude Opus 5.5 · 3 Nov 2026 | – |
| numbers | 3 | primitive | token chips of the real reply | close | – | – | pops |
| icon | 2 | capture | callout on the icon | push | – | search icon | click |
| looks | 2 | primitive | spine returns, LOOK lit; counter 5 s | wide | cut | – | – |
| banner | 3 | capture | run 1 beside run 2, crosshairs at 277 and 27 | wide | dip | – | – |
| picture | 2 | capture | "found it in the picture" highlighted | – | – | – | – |
| couldn't | 2 | capture | run 1 reply in terminal | medium | blur | – | – |
| answer | 3 | capture | infobox crop, "330 m" marked | close | – | – | riser, hit |
| photo | 2 | capture | the frame-0 screenshot returns, the spine complete | wide | push | – | – |
