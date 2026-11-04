---
type: video-idea
status: review
series: Agent at work
hook_pattern: surprising-result
medium: capture
score: 19
publish: 
video: "[[AI websites look the same - Status]]"
created: 2026-11-03
updated: 2026-11-03
tags: [youtube, pipeline]
---

# Why every AI website looks the same

← [[Pipeline]] · [[Strategy]] §The idea passes

**Claim** (one line a stranger would say "wait, why?" to): ask any coding agent for a landing page and you get the same purple gradient and the same font, and two of GitHub's biggest repos this week exist only to stop it.

**Real thing** (named product, company, person or incident, dated, with its source): `pbakaus/impeccable` (Paul Bakaus, Apache 2.0, about 101.6 k stars, read 3 Nov 2026; started from Anthropic's frontend-design skill) names the defaults: "Inter for everything", "purple-to-blue gradients", "cards nested in cards". `Nutlope/hallmark` (Together AI, MIT, 47.0 k stars, read 3 Nov 2026) lists more ("an eyebrow above every heading", "one coloured word in a headline"). Neither cites a study: the evidence must be our own recorded run. Verify at P1: the Tailwind `bg-indigo-500` default as the likely origin of the purple (Adam Wathan's public remark, find the primary post and date, or drop it).

**Y · X** (the result the viewer wants · the mechanism in the way): a site that does not look AI-made · a model writes the most likely next token, so with no direction it returns the most common design in what it learned; a skill or a named constraint moves it off the average.

**Hook pattern** (an id from [[Strategy]] §Hooks) and why people click it: `surprising-result`; an unfair-advantage feeling (spot AI sites, make yours not look like one) and a thing every vibe-coder has seen.

**Demand** (rows from [[Radar]] or `youtube_search.py`: link, views, ratio; or the autocomplete): [[Radar]] 3 Nov 2026: Coding with Lewis "Every AI Startup Website Looks the Same" youtu.be/HRaGvoRa-IU 458,642 (9.3x). Autocomplete (YouTube, 3 Nov 2026): "ai website design", "ai website design workflow". Signals: impeccable 11,754 and hallmark 10,517 trending scores on GitHub. `youtube_search.py "why ai websites look the same" --short --min-ratio 3` (4 Nov 2026): x33pfxMChsM 877 (12.4x); WcxGicjgcK4 510 (8.0x); JwrYd6PMOYU 4,338 (8.2x); 7gsg0ef-8Cc 1,035 (5.3x); JYSitj3nimY 654 (3.5x).

**Own fit** (how our videos of this series and pattern did, from [[Report]]): Agent at work 680 engaged (n=4), surprising-result 702.5 (n=4), both above our 585.5 median.

**Showable** (the medium of the mechanism, [[Picture]] §Medium, the one real run or model output, and the spine): capture. Same prompt ("landing page for a note-taking app"), same model (name and version at P1), recorded twice: bare, then with impeccable installed. Count the defaults on screen (font, gradient, nested cards) against the repo's list. Spine: the bare page, a tile of N bare runs that all match, the "most likely token" figure (a probability bar landing on purple), the skill run.

**Score** demand 5 · own fit 5 · showable 5 · real thing 4 = 19 / 20 (demand rescored 4 Nov 2026)

**Hooks** (3, different patterns):

1. surprising-result: I asked AI for five different websites. I got the same one five times.
2. name-it: There's a name for this purple. Developers call it AI slop.
3. news-why: Why 100,000 developers just installed a file that tells AI what not to design.
