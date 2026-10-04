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
