#!/usr/bin/env python3
"""Coherence check for the YouTube vault. Run from the vault root:  python3 System/scripts/check_vault.py

Fails (exit 1) on:
  * broken wikilinks and embeds (a target that is neither a note nor a file in the vault or in Media/)
  * notes without front matter (type, updated)
  * System/ notes that the index (YouTube Channel.md) does not mention
  * Python scripts that do not compile
  * missing INVARIANTS: phrases that encode user feedback and must stay in the notes that carry them
When feedback adds a rule, add its invariant below in the same pass (see System/Feedback loop.md).
"""
import os
import re
import sys

ROOT = os.getcwd()
SKIP = (".git", ".obsidian", "Media", "__pycache__")

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
    ("System/Playbook.md", "Word-by-word captions", "captions on every video"),
    ("System/Playbook.md", "No branding inside the video", "no in-video branding"),
    ("System/Playbook.md", "never write ≈ ≥ ≤ →", "font lacks those symbols"),
    ("System/Playbook.md", "BigSoundBank and Freesound are deferred", "sound sources"),
    ("System/Playbook.md", "RemArc", "BBC effects are non-commercial"),
    ("System/Playbook.md", "pads every take", "voice start fix"),
    ("System/Playbook.md", "Not verified, said out loud", "honesty about what the agent cannot check"),
    ("System/Workflow.md", "no Replicate call", "no media before P4"),
    ("System/Workflow.md", "gpt-image-2", "generated plate model"),
    ("System/Workflow.md", "cap = base", "budget cap"),
    ("System/Workflow.md", "Week NN", "week folders"),
    ("System/Style.md", "50 % of the height", "captions centred"),
    ("System/Style.md", "Redtail", "brand"),
    ("System/Playbook.md", "`Austin`", "channel voice"),
    ("System/Publish.md", "Inauthentic content", "monetization policy"),
    ("System/Publish.md", "Default private", "uploads are private by default"),
    ("System/Publish.md", "```text", "copy-paste blocks"),
    ("System/Publish.md", "Sample rule", "under 100 views read counts only"),
    ("System/Publish.md", "one change per video", "analytics attribution"),
    ("System/Feedback loop.md", "single source of knowledge", "feedback ends in the vault"),
    ("CLAUDE.md", "need-to-know", "agent guide carries the hook rule"),
    ("CLAUDE.md", "No media before P4", "agent guide carries the gate"),
    ("CLAUDE.md", "Analytics/Report.md", "report read before choosing"),
    ("Pipeline/Idea template.md", "hook_type", "idea notes carry the hook type"),
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
