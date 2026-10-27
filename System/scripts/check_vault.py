#!/usr/bin/env python3
"""Coherence check for the YouTube vault. Run from the vault root:  python3 System/scripts/check_vault.py

Fails (exit 1) on:
  * broken wikilinks and embeds (a target that is neither a note nor a file in the vault or in Media/)
  * notes without front matter (type, updated)
  * System/ notes that the index (YouTube Channel.md) does not mention
  * Python scripts that do not compile
  * `[[Note]] §Heading` references whose heading does not exist (numbered §N must match "## N." in that note)
  * per-video notes over their size ceiling; index missing a video's YouTube id; Script scene 1 differing from the hook in Analytics/videos.csv
  * missing INVARIANTS: phrases that encode user feedback and must stay in the notes that carry them
When feedback adds a rule, add its invariant below in the same pass (see System/Feedback loop.md).
"""
import os
import re
import sys

ROOT = os.getcwd()
SKIP = (".git", ".obsidian", ".claude", "Media", "__pycache__")       # .claude: agent skills, not notes

INVARIANTS = [
    # (file, phrase, rule it protects)
    ("System/Playbook.md", "Street-lamp test", "idea gate"),
    ("System/Playbook.md", "Five candidate hooks", "hook earns its reaction"),
    ("System/Playbook.md", "Facts bank", "idea gate"),
    ("System/Playbook.md", "never seconds", "length is planned in words"),
    ("System/Playbook.md", "need-to-know claim", "first 3 seconds"),
    ("System/Playbook.md", "Explain, do not narrate", "no storytelling"),
    ("System/Playbook.md", "theme line", "one thread"),
    ("System/Playbook.md", "concrete payoff", "ending"),
    ("System/Playbook.md", "Cut test", "compact script"),
    ("System/Playbook.md", "Usefulness test", "every plate earns its place"),
    ("System/Playbook.md", "no custom style", "model's own style"),
    ("System/Playbook.md", "Scientific fidelity beats creativity", "faithful explainers"),
    ("System/Playbook.md", "No bare backdrops", "numbers sit on real images"),
    ("System/Playbook.md", "Specificity test", "text with a point of view"),
    ("System/Playbook.md", "Phrase captions on every video", "captions on every video, 1 to 3 words (user, 26 Oct 2026)"),
    ("System/Playbook.md", "No branding inside the video", "no in-video branding"),
    ("System/Playbook.md", "never write ≈ ≥ ≤ →", "font lacks those symbols"),
    ("System/Playbook.md", "BigSoundBank and Freesound are deferred", "sound sources"),
    ("System/Playbook.md", "RemArc", "BBC effects are non-commercial"),
    ("System/Playbook.md", "pads the take", "voice start fix"),
    ("System/Playbook.md", "Not verified, said out loud", "honesty about what the agent cannot check"),
    ("System/Workflow.md", "no Replicate call", "no media before P4"),
    ("System/Workflow.md", "gpt-image-2", "generated plate model"),
    ("System/Workflow.md", "cap = base", "budget cap"),
    ("System/Workflow.md", "Week NN", "week folders"),
    ("System/Workflow.md", "Day folder", "videos are grouped by the day they were made (user, 6 Oct 2026)"),
    ("System/Design system.md", "50 % of the height", "captions centred"),
    ("System/Style.md", "Redtail", "brand"),
    ("System/Playbook.md", "`Dennis`", "channel voice (user chose Inworld TTS-2, 9 Oct 2026)"),
    ("System/Publish.md", "Inauthentic content", "monetization policy"),
    ("System/Publish.md", "Default private", "uploads are private by default"),
    ("System/Publish.md", "```text", "copy-paste blocks"),
    ("System/Publish.md", "Sample rule", "under 100 views read counts only"),
    ("System/Publish.md", "youtube_upload.py thumb", "thumbnails are re-set after processing and checked"),
    ("System/Publish.md", "publish.py", "P8 is one command (token-cheap)"),
    ("System/Workflow.md", "One focal image", "thumbnail v2: one drawn focal image, 3 to 4 words, no chips or logo (user, 9 Oct 2026: research-led redesign)"),
    ("System/Publish.md", "one change per video", "analytics attribution"),
    ("System/Feedback loop.md", "single source of knowledge", "feedback ends in the vault"),
    ("CLAUDE.md", "need-to-know", "agent guide carries the hook rule"),
    ("CLAUDE.md", "No media before P4", "agent guide carries the gate"),
    ("CLAUDE.md", "Analytics/Report.md", "report read before choosing"),
    ("Pipeline/Idea template.md", "hook_type", "idea notes carry the hook type"),
    ("System/Playbook.md", "inworld/realtime-tts-2", "voice model (user, 9 Oct 2026: \"go for a higher tier model\")"),
    ("System/Playbook.md", "one continuous take", "no stitched scenes: the voice felt broken (user, 9 Oct 2026)"),
    ("System/Playbook.md", "never by cutting", "pauses are written into the take, never cut into the audio"),
    ("System/Playbook.md", "−14 LUFS", "master loudness (audio research, 9 Oct 2026)"),
    ("System/Playbook.md", "shield-free", "Pixabay music only without a Content ID shield"),
    ("System/Workflow.md", "mix_audio.py", "every render is mixed and mastered"),
    ("CLAUDE.md", "one continuous take", "agent guide carries the voice rule"),
    ("CLAUDE.md", "mix_audio.py", "agent guide carries the master rule"),
    ("System/Playbook.md", "2b. Package", "title and thumbnail are written at the script phase (user, 6 Oct 2026)"),
    ("System/Audience.md", "Deep-first search", "niche research method (user insights, 6 Oct 2026)"),
    ("System/Playbook.md", "Then one social question", "the close ends with a question that invites comments (user, 6 Oct 2026)"),
    ("System/Audience.md", "youtube_search.py", "deep-first search runs on the YouTube Data API (user, 6 Oct 2026)"),
    ("System/Audience.md", "promise, proof, plan", "opening reaffirms the click"),
    ("System/Workflow.md", "inworld/realtime-tts-2", "voice model in the budget"),
    ("CLAUDE.md", "Package at the script phase", "agent guide carries the package rule"),
    ("System/Playbook.md", "Hook test", "hook is judged by a test, not by word count"),
    ("System/Playbook.md", "\"Borderline\" is a fail", "street-lamp test has a fail state"),
    ("System/Playbook.md", "Demand check", "ideas get outside evidence"),
    ("System/Playbook.md", "Topic spread", "no two videos in a row on one topic family"),
    ("System/Publish.md", "publish-pack.md", "every video has a copy-ready publish pack in upload/ (user, 9 Oct 2026)"),
    ("CLAUDE.md", "publish-pack.md", "agent guide carries the publish pack rule"),
    ("System/Style.md", "Motion plates and engagement rules", "plates are built to engage (user, 9 Oct 2026)"),
    ("System/Playbook.md", "Show the verb, not the noun", "visuals show what happens, not the thing named (user, 9 Oct 2026)"),
    ("System/Playbook.md", "Swap test", "decorative pictures are cut (user, 9 Oct 2026)"),
    ("System/Playbook.md", "on the word", "cuts and labels land on the word they illustrate (temporal contiguity)"),
    ("System/Playbook.md", "MOTION SHARE", "most of the runtime moves: no slideshows (user, 9 Oct 2026; YPP policy)"),
    ("System/Playbook.md", "one anchor", "a few visual worlds and an anchor that returns"),
    ("System/Style.md", "Ink ground", "motion and 3D plates share one ground (look v2, 23 Oct 2026)"),
    ("System/Workflow.md", "stock_videos.py", "footage has a tool and a license filter"),
    ("System/Workflow.md", "ltx-2.5-fast", "AI video is opt-in and priced"),
    ("System/Workflow.md", "did any picture fail to show what was being said", "listening rubric asks about visual sync"),
    ("CLAUDE.md", "verb, not the noun", "agent guide carries the visual rule"),
    ("System/Playbook.md", "Compact test", "every third video is compact (YouTube diagnostic, 9 Oct 2026)"),
    ("System/Playbook.md", "Illustrate, do not typeset", "every step has a picture, not a text box (user, 26 Oct 2026)"),
    ("System/Style.md", "Fluent Emoji 3D", "illustration library for everyday objects (user, 26 Oct 2026)"),
    ("System/Audience.md", "Case sources", "AI cases come from incidents, lab disclosures, measurements, real runs (user, 26 Oct 2026)"),
    ("System/Audience.md", "Plain-words map", "AI jargon has fixed plain words and pictures (user, 26 Oct 2026)"),
    ("System/Audience.md", "News is the case, never the video", "evergreen mechanism, timely case (user, 26 Oct 2026)"),
    ("System/Publish.md", "AI shelf life", "AI claims are re-checked before upload (user, 26 Oct 2026)"),
    ("System/Design system.md", "Comment prompt", "the closing question is a reply box with answer chips (user, 27 Oct 2026)"),
    ("System/Playbook.md", "Short test block", "shorter videos are tested, 90 to 140 words (user, 26 Oct 2026)"),
    ("System/Playbook.md", "Comparisons live on one board", "a comparison stays on one table (user, 26 Oct 2026)"),
    ("System/Playbook.md", "mini-series", "strong families become series (YouTube diagnostic, 9 Oct 2026)"),
    ("System/Playbook.md", "never two on one day", "steady cadence (YouTube diagnostic, 9 Oct 2026)"),
    ("System/Playbook.md", "[H]", "untested rules are marked as hypotheses"),
    ("System/Playbook.md", "Pause plan", "pauses follow intention and emotion (user, 5 Oct 2026)"),
    ("System/Playbook.md", "opening bell", "the opening bell is liked and kept"),
    ("System/Playbook.md", "Immersive plates", "no empty screens (user, 5 Oct 2026)"),
    ("System/Style.md", "Immersive plates", "blur background, inset, split layout"),
    ("System/Workflow.md", "do the pauses feel human", "listening rubric asks about pauses"),
    ("System/Workflow.md", "Listening rubric", "the user's ear is the only audio evidence"),
    ("System/Workflow.md", "Note size ceilings", "per-video notes stay short"),
    ("System/Model script.md", "Hook rewrites", "a model to imitate"),
    ("CLAUDE.md", "teaches AI", "the channel teaches AI (user, 23 Oct 2026)"),
    ("System/Audience.md", "Agent at work", "three AI series: How it works, Agent at work, What's coming"),
    ("System/Playbook.md", "AI rigor", "capability claims carry model, version and date; forecasts labelled"),
    ("System/Playbook.md", "AI clichés are banned", "no glowing brains, robots at keyboards or binary rain"),
    ("System/Playbook.md", "Recorded runs", "agent demos are real runs, not mock-ups"),
    ("System/Playbook.md", "scene3d.py", "3D plates for mechanisms with depth (user, 23 Oct 2026)"),
    ("System/Style.md", "3D plates", "3D look shares the motion plates' world"),
    ("System/Workflow.md", "scene3d.py", "3D plates have a tool, a cost and a command"),
    ("System/Playbook.md", "**Named:**", "the hook names the subject, never 'the idea' (user, 23 Oct 2026)"),
    ("System/Playbook.md", "Curiosity before explanation", "the hook promises the how before explaining (user, 23 Oct 2026)"),
    ("System/Playbook.md", "definition** (one plain sentence", "How it works arc: definition, origin, explanation (user, 23 Oct 2026)"),
    ("System/Playbook.md", "Connection test", "each sentence answers the previous one's question (user, 23 Oct 2026)"),
    ("System/Playbook.md", "One running example", "the mechanism stays on one concrete example (user, 23 Oct 2026)"),
    ("System/Playbook.md", "Bridge visuals", "abstractions are mapped from the example on screen (user, 23 Oct 2026)"),
    ("System/Style.md", "Semantic colours", "one meaning per colour, validated (user, 23 Oct 2026)"),
    ("System/Style.md", "Line style", "line style is designed, not default (user, 23 Oct 2026)"),
    ("System/Design system.md", "one dominant element per moment", "one dominant element, layout rules (user, 23 Oct 2026)"),
    ("System/Design system.md", "hfkit.py", "the design system is code every HyperFrames builder imports (user, 27 Oct 2026)"),
    ("System/Design system.md", "colx(k, n)", "elements sit on a column grid, never placed by eye (user, 27 Oct 2026)"),
    ("System/Design system.md", "Blender glb", "Blender scenes reach HyperFrames as glb or alpha webm (user, 27 Oct 2026)"),
    ("System/Workflow.md", "validate_palette.js", "new colours are validated, not eyeballed"),
    ("System/Workflow.md", "did you know what the video is about", "rubric asks about hook clarity"),
]
FORBIDDEN = [
    # (file, phrase, why): rules the user removed; must not come back
    ("System/Playbook.md", "≤ 10 words", "hook quality is not measured in words (feedback, 5 Oct 2026)"),
    ("CLAUDE.md", "≤ 10 words", "hook quality is not measured in words (feedback, 5 Oct 2026)"),
    ("CLAUDE.md", "16 to 20 plates", "a plate count produced filler pictures (user, 9 Oct 2026)"),
    ("CLAUDE.md", "previous_text", "per-scene takes with text context were retired (user, 9 Oct 2026)"),
    ("System/Playbook.md", "16 to 20 plates", "a plate count produced filler pictures (user, 9 Oct 2026)"),
    ("System/Audience.md", "civil engineering", "the old technology niche was replaced by AI (user, 23 Oct 2026)"),
    ("CLAUDE.md", "civil engineering", "the old technology niche was replaced by AI (user, 23 Oct 2026)"),
    ("System/Style.md", "drafting grid: designed", "the drafting grid read as generic (user, 23 Oct 2026)"),
]
CEILING = {"Script - ": 2700, "Upload - ": 2300, " - Status": 1500}

problems = []
notes, names = {}, set()
for r, d, f in os.walk(ROOT):
    d[:] = [x for x in d if x not in SKIP]
    for x in f:
        p = os.path.join(r, x)
        rel = os.path.relpath(p, ROOT)
        names.add(x)
        names.add(os.path.splitext(x)[0])
        if x.endswith(".md"):
            notes[rel] = open(p, encoding="utf-8").read()
media = set()
for r, d, f in os.walk(os.path.join(ROOT, "Media")):
    for x in f:
        media.add(x)
        media.add(os.path.splitext(x)[0])

LINK = re.compile(r"!?\[\[([^\]|#]+)((?:#[^\]|]*)?)(?:\|[^\]]*)?\]\]")
for rel, t in notes.items():
    body = re.sub(r"```.*?```", "", t, flags=re.S)           # ignore code blocks
    body = re.sub(r"`[^`]*`", "", body)                      # and inline code
    for m in LINK.finditer(body):
        tgt = m.group(1).strip()
        if (m.group(1) + m.group(2)).strip() in names:      # a note whose own name contains "#" (e.g. "Youtube idea #2")
            continue
        if tgt in names or os.path.basename(tgt) in names or tgt in media or os.path.basename(tgt) in media:
            continue
        problems.append(f"broken link in {rel}: [[{tgt}]]")
    if rel in ("CLAUDE.md",):
        continue
    fm = re.match(r"---\n(.*?)\n---\n", t, re.S)
    if not fm:
        problems.append(f"no front matter: {rel}")
    else:
        keys = {l.split(":")[0].strip() for l in fm.group(1).splitlines() if ":" in l and not l.startswith((" ", "-"))}
        need = {"type", "status"} if rel.startswith("Pipeline/Idea") else {"type", "updated"}
        miss = need - keys
        if miss:
            problems.append(f"front matter of {rel} lacks {sorted(miss)}")

index = notes.get("YouTube Channel.md", "")
for rel in notes:
    if rel.startswith("System/") and os.path.splitext(os.path.basename(rel))[0] not in index:
        problems.append(f"not in the index (YouTube Channel.md): {rel}")

# builder guards that encode feedback (code, not notes)
_b = open(os.path.join(ROOT, "System", "scripts", "build_video.py"), encoding="utf-8").read()
if "def add_brand" in _b:
    problems.append("build_video.py still has the brand layer the user asked to remove (feedback, 4 Oct 2026)")
for _needle, _why in (("bare backdrop refused", "no bare backdrops"), ("add_captions()", "word-by-word captions"), ("write_srt(", "caption track export"), ("LONG PLATE", "long plates are reported"), ("add_sound()", "sound design"), ("plan.captions needs one string", "display captions"), ("CAP_CH = 40", "captions are the top layer, above cards and callouts"), ("def pause_cuts", "inner pauses are set per word"), ("def blur_bg", "immersive blurred backgrounds"), ("EMPTY PLATE", "empty plates are reported")):
    if _needle not in _b:
        problems.append(f"build_video.py lost its guard: {_needle} ({_why})")

for r, d, f in os.walk(os.path.join(ROOT, "System", "scripts")):
    for x in f:
        if x.endswith(".py"):
            try:
                compile(open(os.path.join(r, x), encoding="utf-8").read(), x, "exec")      # syntax only
            except SyntaxError as e:
                problems.append(f"does not compile: {x}: {str(e)[:80]}")

for rel, phrase, why in FORBIDDEN:
    if phrase.lower() in notes.get(rel, "").lower():
        problems.append(f"{rel} contains \"{phrase}\": {why}")

# section references: [[Note]] §N or §Heading must point at a real heading
SEC = re.compile(r"\[\[([^\]|#]+)\]\] §([0-9]+|[A-Za-z][A-Za-z ]*[A-Za-z])")
by_name = {os.path.splitext(os.path.basename(r))[0]: t for r, t in notes.items()}
for rel, t in notes.items():
    if rel.startswith("Analytics/Reports/"):
        continue          # dated reports are history
    for m in SEC.finditer(t):
        tgt, ref = m.group(1).strip(), m.group(2).strip()
        body = by_name.get(tgt)
        if body is None:
            continue
        heads = re.findall(r"(?m)^#+ (.*)$", body)
        ok = any(h.startswith(ref + ".") for h in heads) if ref.isdigit() else any(ref.lower().startswith(h.lower()) or h.lower().startswith(ref.lower()) for h in heads)
        if not ok:
            problems.append(f"dead section reference in {rel}: [[{tgt}]] §{ref}")

# per-video note size ceilings (words)
for rel, t in notes.items():
    if rel.startswith("Videos/"):
        n = len(t.split())
        for key, cap in CEILING.items():
            if key in os.path.basename(rel) and n > cap:
                problems.append(f"{rel} has {n} words, ceiling {cap} (Workflow: Note size ceilings)")

# the index knows every published video; Script scene 1 equals the hook in videos.csv
import csv
norm = lambda s: re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()
with open(os.path.join(ROOT, "Analytics", "videos.csv"), encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        if row["youtube_id"] and row["youtube_id"] not in index:
            problems.append(f"YouTube Channel.md lacks the id of {row['video']} ({row['youtube_id']})")
        sc = next((t for r, t in notes.items() if os.path.basename(r) == f"Script - {row['video']}.md"), "")
        m = re.search(r"(?m)^\|\s*1\s*\|\s*([^|]+?)\s*\|", sc[sc.find("Voice (exact text)"):]) if "Voice (exact text)" in sc else None
        if m and norm(m.group(1)) != norm(row["hook"]):
            problems.append(f"hook in videos.csv differs from scene 1 of the script: {row['video']}")

for rel, phrase, why in INVARIANTS:
    t = notes.get(rel, "")
    if phrase.lower() not in t.lower():
        problems.append(f"missing in {rel}: \"{phrase}\" ({why})")

print(f"{len(notes)} notes checked, {len(INVARIANTS)} invariants.")
if problems:
    print(f"{len(problems)} problem(s):")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("OK: the vault is coherent.")
