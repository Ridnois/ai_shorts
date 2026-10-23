---
type: research
created: 2026-10-23
updated: 2026-10-23
status: v1 · P1 to P4a done by delegation; compact
tags: [research, youtube, script, ai, week-03]
---

# Script · AI removes TV ads (Week 03, Fri 23 Oct)

← [[AI removes TV ads - Status]] · [[YouTube Channel]] · [[Playbook]] · [[Audience]]

User (23 Oct 2026): *"Chose a trending ai topic and generate a new video"*. Series: **Agent at work** (the last two were How it works). **Compact** (third video).

**Y:** a smart TV without the ads and tracking. **X:** Android TVs hide a developer interface (ADB) that an agent can drive over Wi-Fi to switch apps off, and it is unencrypted. **Theme line:** *the developer door.* **One question:** how does an agent clean a TV?

## 0. Facts bank (**read** = opened 23 Oct 2026)

| # | Fact | Source |
| --- | --- | --- |
| 1 | Developer Gathin T. gave Claude Code the model number of his parents' Xiaomi TV (a sponsored ad played before Netflix); the agent found the TV on the home Wi-Fi, disabled 25 Xiaomi packages and wrote a new home screen; posted on X 17 Oct 2026 | Decrypt, J. A. Lanz, 20 Oct 2026 (**read**) |
| 2 | Android TV exposes ADB once developer mode is on: Settings, About, press Build seven times, then USB debugging (and network debugging) | Decrypt (**read**); cleanyourtv README (**read**) |
| 3 | Packages are disabled with `pm disable-user`, not uninstalled; no root; a restore script undoes every step | cleanyourtv README (**read**) |
| 4 | "Network ADB is plaintext on port 5555, and on firmware with `ro.adb.secure=0` any device on the LAN gets a shell"; turn debugging off afterwards | cleanyourtv README (**read**, quoted) |
| 5 | cleanyourtv: 27.0k stars, 3.0k forks on 23 Oct 2026 (10.7k on 20 Oct); 252 models, 74 brands | GitHub (**read**); Decrypt |
| 6 | Not for Samsung (Tizen) or LG (webOS); Fire TV only the cleanup half | README, Decrypt (**read**) |
| 7 | One user bricked a TV when the agent rebooted it and uninstalled the OS; another got stuck mid-way | Decrypt (**read**; not used) |
| 8 | Other users: a 192 MB launcher replaced by 83 MB; free memory up about 90 % on an old TV | Decrypt (**read**; not used) |
| 9 | ACR fingerprints whatever is on screen for ad targeting; Texas sued Sony, Samsung, LG, Hisense, TCL in Dec 2025 alleging screenshots about every 500 ms | Decrypt (**read**; not used, compact) |
| 10 | Vizio paid $2.2 million to the FTC in 2017 over viewing data from 11 million TVs | Decrypt (**read**; not used) |
| 11 | dumbtv for Fire TV disables about 65 packages and installs a 41 KB launcher without internet permission | Decrypt (**read**; not used) |
| 12 | Microsoft found hidden instructions could push Claude Code into exposing credentials; Anthropic patched it in May | Decrypt (**read**; not used) |
| 13 | "Vibe coding": Andrej Karpathy, 2025 | Decrypt (**read**; not used) |
| 14 | Router port forwarding of ADB is warned against ("Never by opening the ADB port on their router") | README (**read**; not used) |
| 15 | A phone-only community app does the same cleanup | README (**read**; not used) |

## 1. Idea gate

**Scores:** surprise 4 (a hidden door in your TV) · scale 4 (27k stars in days) · depth 4 · evidence 5 (primary README) · showable 5 · plain 5. **Street-lamp:** pass: the headline "AI removes TV ads" does not say how; the video adds ADB, disable-not-delete and the unencrypted door. **Expert test:** `pm disable-user` without root, plaintext port 5555. **Coffee test:** *"An AI agent can open your TV's developer door and switch the ad apps off, but close the door after."* **Against:** (1) "not my TV" → Android and Google TV only, said on screen; (2) "dangerous" → the catch scene; (3) "just news" → the video teaches the mechanism and a safety habit. **Demand check: not run** (YouTube token HTTP 400). Indirect: the repo went from 10.7k to 27k stars in three days, Decrypt coverage, the X trend of 19 Oct. **Compact:** 114 words.
**Five hooks:** stakes "People are using AI agents to remove the ads from their smart TVs. Here is how." (**used**: Named, stake, promise) · surprising fact "Your smart TV has a hidden developer door." · number "An AI agent switched off twenty-five ad apps on one TV." · contradiction "The ads on your TV are apps, and apps can be switched off." · consequence "One prompt and your TV stops showing ads."
**Hook test (used):** named (AI agents, smart TV ads) · stake (ads everyone hates) · curiosity before explanation, promise "Here is how" · sound-off (caption ADS over the TV with ad tiles) · honest · matches the package.

## 2. Package

- **Promise:** people use AI agents to remove smart TV ads; the video shows how (the developer door) and the one safety step.
- **Titles:** *People Are Using AI to Remove Smart TV Ads. Here's How* (recommended) · *How an AI Agent Switched Off 25 Ad Apps on a TV* · *Your Smart TV Has a Hidden Developer Door*.
- **Thumbnail (at P8):** the 3D TV with its rose ad tiles popping off, the ember agent link; words "NO MORE TV ADS".
- **Opening map:** scene 1 promise · scene 2 definition (the door) · scene 3 the run (proof).

## 3. Script: 114 words, 5 scenes

| Sc | Question it answers | Voice text | Delivery |
| --- | --- | --- | --- |
| 1 | (hook) | People are using AI agents to remove the ads from their smart TVs. Here is how. | plain, intrigued |
| 2 | how can an agent reach a TV? | Many smart TVs run Android, which hides a developer door called A D B. Tap the build number seven times, and it opens. | steady |
| 3 | then what does the agent do? | One developer gave Claude Code his parents' TV model. The agent found the TV on the Wi-Fi, switched off twenty-five apps that served ads or tracking, and wrote a cleaner home screen. | brisk, step by step |
| 4 | is that safe? | The catch: that door is not encrypted. On some TVs, anyone on your Wi-Fi can walk in, so close it after. | a little grave |
| 5 | so what? | So here is the point: agents can now reshape the devices you own. Would you let one into your TV? Tell me. | slower on the point; `break` 0.2 after "own" |

**Honesty:** "Many smart TVs run Android": Android TV and Google TV sets (Sony, TCL, Hisense, Philips, Xiaomi), not Samsung or LG: on screen. "Switched off": `pm disable-user`, reversible. "Anyone on your Wi-Fi": only on firmware with `ro.adb.secure=0` ("on some TVs"). Facts used: 3 (the door, the run, the catch). The ADB address and package names on screen are illustrative.

## 4. Beat sheet, prefix `tv` (one running example: the parents' TV)

1 3D at start: a TV with app tiles, three rose ad tiles; on "remove" the ad tiles pop off · 2 2D at "Many": the TV's settings list in mono, "Build" pressed 7 times (counter), "Developer mode ON" in mint, the ADB door (port 5555) opens in ember · 3 2D at "One": laptop terminal in mono, the Wi-Fi link to the same TV draws on "found", `pm disable-user` rows on "switched", 25 rose units turn off · 4 2D at "wrote": the same TV, now a clean home screen in mint · 5 2D at "The": the door open, other devices on the Wi-Fi reach it in rose on "anyone", it shuts on "close" (debugging OFF) · 6 3D at "So": the clean TV, camera pulls back, conclusion card · 7 2D at "Would": the TV and an ember agent link, margin note.

## 5. Not verified

The X posts themselves (read through Decrypt); the trend's size beyond stars; which Xiaomi packages; demand; how the voice sounds. P7 is the user's.
