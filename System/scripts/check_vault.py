#!/usr/bin/env python3
"""Coherence check for the YouTube vault. Run from the vault root:  python3 System/scripts/check_vault.py

Fails (exit 1) on:
  * broken wikilinks and embeds (a target that is neither a note nor a file in the vault or in Media/)
  * notes without front matter (type, created, updated, status, tags)
  * System/ notes that the index (YouTube Channel.md) does not mention
  * Python scripts that do not compile
  * missing INVARIANTS: phrases that encode user feedback and must stay in the notes that carry them
When feedback adds a rule, add its invariant below in the same pass (see System/Process/Feedback loop.md).
"""
import os
import re
import sys

ROOT = os.getcwd()
SKIP = (".git", ".obsidian", "Media", "__pycache__")

INVARIANTS = [
    ("System/Editing/Blender editing.md", "spelling for the eye", "captions show the clean spelling, the voice the spoken one (Moltbook research)"),
    # Free sound sources research, 4 Oct 2026
    ("System/Guidelines for new scripts.md", "Sound and music are opt-in", "sound only from free licensed libraries, credited, approved"),
    ("System/Guidelines for new scripts.md", "BigSoundBank and Freesound are deferred", "user deferred those two sources"),
    ("System/Guidelines for new scripts.md", "RemArc", "BBC effects are non-commercial"),
    ("System/Content/Shorts quality bar.md", "free licensed libraries", "quality bar points at the sound rule"),
    ("System/Process/Fast workflow.md", "Free libraries", "workflow prices sound at $0 from libraries"),
    ("System/Process/Media convention.md", "sound/", "sound folder with credits"),
    # (file, phrase, which feedback it encodes)
    ("System/Content/Idea and hook quality.md", "street-lamp test", "idea quality gate (helium feedback, 4 Oct 2026)"),
    ("System/Content/Idea and hook quality.md", "five candidate hooks", "hook earns its reaction"),
    ("System/Guidelines for new scripts.md", "Words are the unit", "plan length in words"),
    ("System/Guidelines for new scripts.md", "usefulness test", "illustrations earn their place (Twisted carbon feedback)"),
    ("System/Guidelines for new scripts.md", "stock photos", "free stock photos in the mix"),
    ("System/Guidelines for new scripts.md", "No custom style", "model's own style"),
    ("System/Guidelines for new scripts.md", "pads every take", "voice start fix"),
    ("System/Visual/Illustration pipeline.md", "usefulness test", "illustration pipeline"),
    ("System/Visual/Illustration pipeline.md", "transparent", "cutouts with gradients in Blender"),
    ("System/Visual/Illustration pipeline.md", "Openverse", "free stock sources"),
    ("System/Visual/Prompt - per-scene generation guide.md", "specification, not a scene", "content-first prompts"),
    ("System/Visual/On-screen text style.md", "specificity test", "text with personality"),
    ("System/Content/Channel identity.md", "curious specialist", "channel personality"),
    ("System/Editing/Blender editing.md", "CHECK=1", "voices checked in the builder"),
    ("System/Process/Production process.md", "visual plan", "stage 3 is the visual plan"),
    ("System/Process/Fast workflow.md", "stock", "stock photos in the workflow"),
    ("System/Process/Feedback loop.md", "single source of knowledge", "the vault is one coherent source"),
    ("CLAUDE.md", "Feedback loop", "the agent guide points to the feedback procedure"),
    # Magnetar feedback, 4 Oct 2026
    ("System/Guidelines for new scripts.md", "need-to-know", "first 3 seconds are a claim, not a story"),
    ("System/Guidelines for new scripts.md", "Scientific fidelity beats creativity", "explainers are scientific"),
    ("System/Guidelines for new scripts.md", "No bare backdrops", "numbers sit on real images"),
    ("System/Guidelines for new scripts.md", "Word-by-word captions", "captions on every video"),
    ("System/Content/Narration guide.md", "explains a mechanism", "explain, do not narrate"),
    ("System/Content/Idea and hook quality.md", "need-to-know claim", "hook is a claim"),
    ("System/Visual/Illustration pipeline.md", "Scientific fidelity beats creativity", "illustration pipeline"),
    ("System/Visual/Illustration pipeline.md", "No bare backdrops", "illustration pipeline"),
    ("System/Visual/Prompt - per-scene generation guide.md", "No glow, no light rays", "scientific explainer prompts"),
    ("System/Visual/On-screen text style.md", "the middle of the frame (50 % of the height)", "caption zone is the centre of the frame (user, 5 Oct 2026)"),
    ("System/Editing/Blender editing.md", "word_timings.py", "captions pipeline"),
    ("System/Content/Shorts quality bar.md", "Checklist before P7", "the Short quality bar"),
    ("System/Content/Channel strategy.md", "inauthentic content", "monetization policy awareness"),
    ("System/Content/Channel strategy.md", "Not verified", "strategy says what was not verified"),
    ("CLAUDE.md", "need-to-know", "agent guide carries the new hard rule"),
    ("System/Process/Media convention.md", "Legacy", "videos are grouped by Week NN and the rest is Legacy (user, 5 Oct 2026)"),
    ("System/Content/Shorts quality bar.md", "middle of the frame, 50 % of the height", "captions sit in the middle of the frame, clear of the Shorts interface (user, 5 Oct 2026)"),
    ("System/Guidelines for new scripts.md", "Upload package", "every video gets an Upload note with title, description, hashtags, thumbnail (user, 5 Oct 2026)"),
    ("System/Guidelines for new scripts.md", "Never write ≈ ≥ ≤ → in a card", "symbols the card font lacks (Battery and lithium r1, 5 Oct 2026)"),
    # engagement, design and brand playbook (4 Oct 2026)
    ("System/Content/Channel playbook.md", "Engaged views", "engaged views, not raw views"),
    ("System/Content/Channel playbook.md", "On-screen design system", "text box and highlight design written down"),
    ("System/Content/Channel playbook.md", "Mission (one sentence)", "channel mission"),
    ("System/Content/Channel voice.md", "Austin it is", "channel voice (user, 5 Oct 2026)"),
    ("System/Content/Channel playbook.md", "Redtail it is", "channel name (user, 5 Oct 2026)"),
    ("System/Content/Channel playbook.md", "[[Brand options]]", "brand logo under review (user, 5 Oct 2026: old avatar and banner deleted as a bias)"),
    ("System/Content/Channel playbook.md", "Science at full speed", "Redtail slogan (user, 5 Oct 2026: banner B)"),
    ("System/Process/YouTube upload.md", "Unaudited API projects", "API uploads lock to private until audit (docs, 5 Oct 2026)"),
    ("CLAUDE.md", "youtube_upload.py", "agent guide points at the uploader"),
    # Superconductors feedback, 4 Oct 2026
    ("System/Guidelines for new scripts.md", "Plain-words test", "hook in plain words"),
    ("System/Guidelines for new scripts.md", "One thread, a fact budget", "theme line and fact budget"),
    ("System/Guidelines for new scripts.md", "concrete payoff", "concrete ending"),
    ("System/Guidelines for new scripts.md", "Cut test", "compact scripts"),
    ("System/Guidelines for new scripts.md", "Reference images are the main source of change", "more reference images"),
    ("System/Content/Narration guide.md", "theme line", "through-line"),
    ("System/Content/Shorts quality bar.md", "LONG PLATE", "a new image every 3 to 4 s"),
    ("System/Content/Shorts quality bar.md", "No branding inside the video", "no in-video branding"),
    ("System/Visual/On-screen text style.md", "Keep exactly", "text layout is frozen"),
    ("System/Content/Channel voice.md", "Expressiveness", "expressive voice A/B"),
    ("CLAUDE.md", "no branding inside the video", "agent guide carries it"),
    ("System/Process/Post-render feedback template.md", "Keep exactly", "feedback template has its keep/change section"),
    ("System/Process/Feedback loop.md", "Post-render feedback template", "the loop points at the template"),
    ("System/Editing/Blender editing.md", "Sound design", "synthesized sound design documented"),
    ("System/Guidelines for new scripts.md", "synthesized by the builder", "sound design on by default"),
    ("System/Content/Channel playbook.md", "Not verified", "playbook says what is hypothesis"),
]

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

LINK = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
for rel, t in notes.items():
    body = re.sub(r"```.*?```", "", t, flags=re.S)           # ignore code blocks
    body = re.sub(r"`[^`]*`", "", body)                      # and inline code
    for m in LINK.finditer(body):
        tgt = m.group(1).strip()
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
        need = {"type", "created", "updated"} if rel.startswith("Pipeline/Ideas") else {"type", "created", "updated", "status", "tags"}
        if rel.startswith(("Pipeline/Idea template", "Pipeline/Ideas")):
            need = {"type", "status"}
        miss = need - keys
        if miss and rel != "YouTube Channel.md":
            problems.append(f"front matter of {rel} lacks {sorted(miss)}")

index = notes.get("YouTube Channel.md", "")
for rel in notes:
    if rel.startswith("System/") and os.path.splitext(os.path.basename(rel))[0] not in index:
        problems.append(f"not in the index (YouTube Channel.md): {rel}")

# builder guards that encode feedback (code, not notes)
_b = open(os.path.join(ROOT, "System", "scripts", "build_video.py"), encoding="utf-8").read()
if "def add_brand" in _b:
    problems.append("build_video.py still has the brand layer the user asked to remove (feedback, 4 Oct 2026)")
for _needle, _why in (("bare backdrop refused", "no bare backdrops"), ("add_captions()", "word-by-word captions"), ("write_srt(", "caption track export"), ("LONG PLATE", "long plates are reported"), ("add_sound()", "sound design"), ("plan.captions needs one string", "display captions")):
    if _needle not in _b:
        problems.append(f"build_video.py lost its guard: {_needle} ({_why})")

for r, d, f in os.walk(os.path.join(ROOT, "System", "scripts")):
    for x in f:
        if x.endswith(".py"):
            try:
                compile(open(os.path.join(r, x), encoding="utf-8").read(), x, "exec")      # syntax only
            except SyntaxError as e:
                problems.append(f"does not compile: {x}: {str(e)[:80]}")

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
