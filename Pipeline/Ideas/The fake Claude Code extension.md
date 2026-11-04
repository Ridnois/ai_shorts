---
type: video-idea
status: next
series: Agent at work
hook_pattern: incident
medium: capture
score: 15
publish: 
video: 
created: 2026-11-03
updated: 2026-11-03
tags: [youtube, pipeline]
---

# The fake Claude Code extension

← [[Pipeline]] · [[Strategy]] §The idea passes

**Claim** (one line a stranger would say "wait, why?" to): for 11 hours, installing Claude Code in Cursor gave a stranger a key to your computer, and Anthropic never wrote that version.

**Real thing** (named product, company, person or incident, dated, with its source): Cursor security notice (cursor.com/blog/claude-code-extension-security-notice, read 3 Nov 2026): tampered `Anthropic.claude-code` 2.1.312 and 2.1.313 on the Cursor marketplace, 29 Oct 2026, about 2:27 to 1:35 PT; `extension.js` adds an SSH key labelled `svc-telemetry` to `authorized_keys`, opens a reverse SSH tunnel, sets persistence (LaunchAgent or scheduled task). "Up to 5,000 users" (Reuters via several outlets, an upper bound; Reuters page itself not read). Analysis: Phorion (phorion.io/blog/offical-claude-code-vsx-compromise). Fixed version 2.1.314.

**Y · X** (the result the viewer wants · the mechanism in the way): to install AI tools without handing over your machine · an editor extension runs with your user's rights the moment it loads; the name on the listing is not proof of who published it.

**Hook pattern** (an id from [[Strategy]] §Hooks) and why people click it: `incident`; a named tool many viewers have installed, and a check they can run in 10 seconds.

**Demand** (rows from [[Radar]] or `youtube_search.py`: link, views, ratio; or the autocomplete): autocomplete only (YouTube, 3 Nov 2026: "claude code extension in cursor"). Signals: three HN threads (1,009, 662, 399 points). IBM "When Security Patches Leak" 9.6x is `early` and a neighbour, not the same question. Needs `youtube_search.py` at P1.

**Own fit** (how our videos of this series and pattern did, from [[Report]]): incident 721 (n=3), Agent at work 680 (n=4), both above our 585.5 median.

**Showable** (the medium of the mechanism, [[Picture]] §Medium, the one real run or model output, and the spine): capture of the safe check (`grep svc-telemetry ~/.ssh/authorized_keys`, empty on our machine) plus a figure: the extension loads, one line lands in a key file, a tunnel opens. Never show the attacker IP or a working payload.

**Score** demand 1 · own fit 5 · showable 4 · real thing 5 = 15 / 20

**Hooks** (3, different patterns):

1. incident: For 11 hours, installing Claude Code gave a stranger a key to your laptop.
2. stakes: Your editor's extensions can do anything you can. One just did.
3. surprising-result: Anthropic never wrote version 2.1.313. Up to 5,000 people installed it.
