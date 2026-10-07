---
type: research
created: 2026-10-06
updated: 2026-10-06
status: P1 to P3 done (delegated run after the user's rewrite request); r1 render next; P7 is the user's
tags: [research, youtube, script, drm, streaming, week-01]
---

# Script · Netflix screenshot (Week 01, Tuesday 6 Oct)

← [[Netflix screenshot - Status]] · [[YouTube Channel]] · [[Playbook]] · [[Audience]] · [[Why you cannot screenshot Netflix]] · [[Niche map]]

User choice (6 Oct 2026): *"Lets go with idea #1"*. **Y:** copy a frame of what I pay for (and, bridged, watch it sharp). **X:** the black frame is the operating system refusing to copy protected video; "knowing" is a different feature that fires after the fact. **Theme line (proposed):** *Netflix does not catch your screenshot: your device is built not to copy the picture.* **One question:** why is a screenshot of a streamed film black, and does Netflix know?

## 0. Facts bank (**read** = page opened 6 Oct 2026; **not read** = search snippet only, not for the voice)

| # | Fact | Source |
| --- | --- | --- |
| 1 | Apple: `UIScreen.isCaptured` is YES when the system is "actively recording, mirroring, or using AirPlay" | Apple developer docs (**read**) |
| 2 | Apple: the system "doesn't include video content encrypted using FairPlay Streaming" when recording, mirroring or AirPlaying; it "blacks out" that video | Apple docs (**read**) |
| 3 | Apple: FairPlay-encrypted **audio is still included**; apps must watch `isCaptured` to stop it | Apple docs (**read**) |
| 4 | Apple: `userDidTakeScreenshotNotification` "posts after the screenshot is taken", with no extra data | Apple docs (**read**) |
| 5 | Android: `FLAG_SECURE` "tells Android not to allow screenshots or to display the window view on a non-secure display"; "the resulting image is blank" | Android developers, Secure sensitive activities (**read**) |
| 6 | Android 14 (API 34): `Activity.ScreenCaptureCallback` lets an app be notified when a screenshot or screen recording is initiated (permission detail not confirmed) | Android reference (**read**, partial) |
| 7 | Windows: `SetWindowDisplayAffinity` with `WDA_MONITOR`: the window is shown only on a monitor, "everywhere else, the window appears with no content" | Microsoft Learn (**read**) |
| 8 | Microsoft says it is **not** a DRM or security guarantee: it works only while the Desktop Window Manager is composing, and a photo of the screen defeats it | Microsoft Learn (**read**) |
| 9 | Widevine L1: decryption and processing "entirely in a TEE", original resolution; L2 and L3: software or dedicated video hardware, or no TEE, **fixed (lower) resolution** | Wikipedia, Widevine (**read**; secondary) |
| 10 | Widevine is Google's content-protection system used by partners such as Netflix, Disney+ and Amazon Prime Video; licences are issued through the partner's proxy | Google Widevine overview (**read**) |
| 11 | Netflix 4K on Windows needs an HDCP 2.2-compatible connection, HEVC, 15 Mbps or more, a listed GPU | Netflix Help (**read**) |
| 12 | Netflix Help page says nothing about screenshots or black screens | Netflix Help (**read**) |
| 13 | HDCP: Intel's copy protection that authenticates devices and encrypts video over HDMI and DisplayPort; 2.2 (2012) addresses weaknesses of earlier versions | Wikipedia, HDCP (**read**; secondary) |
| 14 | Common web explanations say "DRM recognises the capture and blanks it"; the platform docs above describe the **operating system leaving protected content out of the copy**, and a separate callback that tells the app *after* | agent's reading of facts 1 to 8 |
| 15 | YouTube: "How does Netflix know when you take a screenshot?" 5.8M views (Tech.Explain); other videos on the black screenshot: 400 to 8.7k | youtube_search, 6 Oct 2026 |
| 16 | Not found: any Netflix statement of which API its apps use; so the voice says "streaming apps" and "protected video", never "Netflix uses FLAG_SECURE" | agent |

## 1. Idea gate

**Street-lamp test: pass, with a limit.** "Black because of DRM" is the headline that the 5.8M video and a dozen small ones already give. What the headline lacks, and the platform docs give: **two separate mechanisms** that people merge into "Netflix knows": (a) **blocking**: the OS leaves protected video out of the copy (facts 2, 5, 7, 9); (b) **knowing**: an app can be told *after* a screenshot (fact 4) or when a recording starts (facts 1, 6). One-sentence mechanism: *the black frame is the system refusing to copy; the "it knows" part is a notification that arrives afterwards.* Honesty check: Microsoft itself says the Windows version is not DRM (fact 8), and Apple's blackout covers recording and mirroring too.
**Scores:** surprise 4 · scale **3** · depth 4 · evidence 4 (three OS vendors, primary pages) · showable 4 · plain 5. **Scale is 3, below the required 4** (the parked Decimal video had the same weakness). **Proposed fix (the user's yes needed): bridge to the outcome people also want, a sharp picture.** The same protected path decides resolution: L1 gives original resolution, L2 and L3 a fixed lower one (fact 9), and 4K needs HDCP 2.2 (fact 11). Title and thumbnail sell *the black screenshot*, the close pays *why your laptop may get a softer picture than your TV*. If the user declines the bridge, the idea stays scale 3 and drops to the end of the queue.
Rejected, one line each: **"how to bypass it"** (not explained, not taught); **Netflix's own system design** (no source); **a piracy angle** (policy).
**Coffee test:** *"A black screenshot of Netflix is your phone refusing to copy protected video, not Netflix spying on you."* "Oh, so it does not know?" surprise 4.
**Expert test:** a platform engineer would say the interesting part is protected buffers and the secure decode path, and that detection is a separate callback. Pass if fact 9's hardware path is read in a primary source (open item).
**Against the idea (three reasons to scroll past):** (1) "I know it is DRM": answered by the blocking vs knowing split; (2) "who cares about screenshots": answered by the resolution bridge; (3) "a 5.8M video already did it": its answer is "it knows"; ours says it mostly does not. If the split reads as a technicality, surprise drops to 3.
**Demand check:** one proven outlier (5.8M, 47x), the rest of the question 400 to 8.7k ([[Niche map]]); quality-fix videos around the resolution bridge 20k to 143k from tiny channels. **Risk:** one outlier can be luck, so the resolution bridge is what makes demand robust. **Topic family:** software and networks; previous video Decimal error (software, parked): spread ok because that video was not published.
**Five hooks (different types, voice-take check pending):** contradiction (leading) "Netflix does not know you took a screenshot, and it does not need to." · surprising fact "A screenshot of Netflix is black because the film never enters the picture your phone copies." · stakes "The same trick that blacks out your screenshot also decides how sharp your picture is." · question-as-claim "The black screen is not a bug: it is the protection working." · consequence "Your laptop may stream a softer picture than your TV because of a security rule." (verify before use; facts 9 and 11 support the direction, not the claim for every device).

## 2. Rewrite after the user's feedback (6 Oct 2026, P2 and P3, delegated)

*"make it more like an interesting fact, keep the information about os blocking the screen recording on netflix. and end on a way to fidelize the user, make him think, ask him something, make it social."* The street-lamp and scale worries of §1 were set aside by the user: the video is an **interesting-fact explainer** that keeps the OS blocking (facts 1 to 8) and closes on a **question to the viewer**; no resolution bridge, Widevine, HDCP or Android 14 callback in the voice (cut test).

**Package.** Y: copy a frame of what I pay for. X: the operating system refuses to copy protected video. **Promise:** a Netflix screenshot is black because your own device refuses to copy it. **Titles:** *Why Your Phone Won't Screenshot Netflix* (recommended) · *The Black Screenshot: What Your Phone Is Really Doing* · *Netflix Doesn't Block Your Screenshot. Your Phone Does.* (check wording: Netflix's app may set the flag; use only if a source says so). **Thumbnail:** hero `ns-phone-hand.jpg` (CC0) with the black-screen contrast; kicker **STREAMING**; lines **SCREENSHOT** / **COMES OUT BLACK** (second line orange); chips **3 SYSTEMS · 1 RULE** · **SOUND STILL GETS THROUGH** · **A CAMERA STILL WORKS**. Beats its neighbours (search 6 Oct 2026: face-on thumbnails and "Real Reason" text) by naming the surprise in two plain lines plus facts. **Opening map:** scene 1 promise; scene 2 proof (apps mark video protected, three systems) and plan.

## 3. Script (P2): 168 words, 924 characters, 7 scenes

Bridges: 2 "and the operating system obeys" · 3 "On Android" · 4 "An iPhone" · 5 "Windows" · 6 "The app can be told" · 7 "So". **Facts (5):** the OS leaves protected video out (all three); Android's secure setting; iPhone blacks out video but not sound; Windows marks a window empty and Microsoft says no guarantee; notifications come after. **Spoken figures:** none; everything is on screen as words. **Original synthesis:** one rule shown across three vendors side by side. **Cut test:** Widevine levels, HDCP, resolution, Android 14 callback, Netflix's own implementation (fact 16). **Honesty:** "apps can mark their video as protected" (generic, not "Netflix uses ..."); Microsoft's caveat is voiced. **Close:** payoff ("your own device following a rule the app set") then the question and the invitation ([[Playbook]] §2).

| Scene | Voice text | Words | Delivery | Pause after (s) |
| --- | --- | --- | --- | --- |
| 1 | A screenshot of a Netflix movie comes out black, and Netflix does not have to notice a thing. | 18 | curious, matter-of-fact | 0.60 |
| 2 | Apps can mark their video as protected, and the operating system obeys. Android, iPhone and Windows each do it their own way. | 22 | clear, explaining | 0.40 |
| 3 | On Android, one setting called secure makes the screenshot blank, and keeps the window off non-secure screens, like a projector. | 20 | light, one fact at a time | 0.30 |
| 4 | An iPhone blacks out protected video in screen recordings, mirroring and AirPlay. The sound still gets through, so the app has to pause it. | 24 | steady, a little surprised at the sound | 0.30 |
| 5 | Windows can mark a window so it looks empty everywhere except the monitor. Microsoft says it is no guarantee: a camera pointed at the screen still copies it. | 28 | dry, amused at the camera | 0.40 |
| 6 | The app can be told about a screenshot, but only afterwards. It is a notification, not a lock. | 18 | calm, short | 0.80 (before the close) |
| 7 | So the black square is not Netflix watching you. It is your own device following a rule the app set. Should a device be allowed to refuse to copy what it shows you? Tell me what you think. | 38 | warm, open: speaking to the viewer | (tail) |

`gaps` = [0.60, 0.40, 0.30, 0.30, 0.40, 0.80]; inner pauses after "black," "obeys." "blank" "monitor." "you." "set.". **Voice:** `elevenlabs/turbo-v2.5`, Austin, per scene with previous and next text. Scene 6 was retaken (v2) because speech-to-text heard "after it has taken"; it now reads "only afterwards".

## 4. Visual plan (P3): 17 plates, prefix `ns`, folder `Media/Week 01/2026-10-06 Tue/Netflix-screenshot/`

Photos (credits in `stock/_credits.jsonl`): `ns-phone-hand` (CC0, NeONBRAND), `ns-phone-use` (CC0), `ns-android` (CC BY-SA 4.0), `ns-laptop` (CC BY-SA 4.0, Ajsm712), `ns-projector` (public domain). Generated (`gpt-image-2`, `high`): layers (plate 4) and camera against screenshot (plate 13). Drawn (Pillow): 6.

| # | Sc | Type · layout | This plate lets the viewer see ___ so they understand ___ |
| --- | --- | --- | --- |
| 1 | 1 | S full + callout | a phone playing video, so the hook is about an everyday action |
| 2 | 1 | D split | the same moment as a picture and as a black screenshot |
| 3 | 2 | S full + callout | a laptop, so "the operating system" is a real thing |
| 4 | 2 | G split | the screen built from layers, with the video layer left out of the copy |
| 5 | 2 | D split | three systems, one rule |
| 6 | 3 | S full + callout | an Android phone and its secure setting |
| 7 | 3 | D split + inset | a secure window: shown on the phone, blank in a screenshot, not shown on a projector (inset: projector) |
| 8 | 4 | S full + callout | a phone and the blacked-out video |
| 9 | 4 | D split | recording, mirroring and AirPlay: video out, sound passes |
| 10 | 5 | S full + callout | a laptop and a window marked monitor-only |
| 11 | 5 | D split | on the monitor against everywhere else (Microsoft) |
| 12 | 5 | G split | a screenshot tool gets black, a camera still gets the picture |
| 13 | 6 | D split | the notification arrives after the screenshot |
| 14 | 6 | S full + callout | the phone, told afterwards |
| 15 | 7 | S full | an Android phone, the question coming |
| 16 | 7 | S contain blur + margin note | the closing question on screen |
| 17 | 7 | S full | the first phone again (loop) |

**Mix:** 8 S, 6 D, 2 G (17 plates; scene durations decide the rest). **Weak points known now:** the "film" in plate 2 is a drawn gradient, not a real frame; the schematic plates simplify layers; no photo shows a Netflix screen (not used: copyright and brand); generic phone photos stand for iPhone, Android and Windows. **On-screen text:** callouts and one margin note only.

## 3. Not verified

Facts 9 and 13 are Wikipedia; fact 6 permission detail; how Netflix's own apps implement protection (fact 16); behaviour differs by device and app version. The agent cannot hear or watch: P7 is the user's.
