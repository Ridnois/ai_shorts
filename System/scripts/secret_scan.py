#!/usr/bin/env python3
"""Keeps keys out of the repo (stdlib only). The vault auto-commits to a PUBLIC GitHub repo, so this runs twice:
  python3 System/scripts/secret_scan.py           # every file git would commit (tracked + untracked not ignored); check_vault runs it
  python3 System/scripts/secret_scan.py --staged  # the pre-commit hook (System/scripts/githooks): blocks the commit
Fails on: a key-shaped string, any value from .env, a credential file name, .env not gitignored, the hook not installed."""
import os, re, subprocess, sys

PATTERNS = {
    "Google OAuth client secret": r"GOCSPX-[A-Za-z0-9_-]{10,}",
    "Google refresh token": r"\b1//0[0-9A-Za-z_-]{30,}",
    "Google access token": r"\bya29\.[0-9A-Za-z_-]{20,}",
    "Google API key": r"\bAIza[0-9A-Za-z_-]{35}",
    "Replicate token": r"\br8_[A-Za-z0-9]{20,}",
    "OpenAI-style key": r"\bsk-[A-Za-z0-9_-]{20,}",
    "private key": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    "client secret JSON": r'"client_secret"\s*:\s*"',
}
NAMES = re.compile(r"(^|/)(\.env(\..*)?|client_secret[^/]*\.json|.*\.pem|.*\.p12|credentials\.json|token\.json)$")
HOOKS = "System/scripts/githooks"


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True).stdout


def env_values():
    vals = []
    for l in open(".env") if os.path.exists(".env") else []:
        k, _, v = l.strip().partition("=")
        if k and not k.startswith("#") and len(v) >= 12 and not v.endswith(".apps.googleusercontent.com"):  # a client id is public
            vals.append((k, v))
    return vals


def scan(staged=False):
    problems = []
    files = (git("diff", "--cached", "--name-only", "--diff-filter=ACMR") if staged else git("ls-files", "-co", "--exclude-standard")).splitlines()
    vals = env_values()
    for f in files:
        if NAMES.search(f) and not f.endswith(".env.example"):
            problems.append(f"credential file would be committed: {f}")
            continue
        try:
            data = subprocess.run(["git", "show", ":" + f], capture_output=True).stdout if staged else open(f, "rb").read()
        except OSError:
            continue
        if b"\0" in data[:8192] or len(data) > 5_000_000:
            continue  # binary or media
        t = data.decode("utf-8", "replace")
        for what, rx in PATTERNS.items():
            if re.search(rx, t):
                problems.append(f"{what} in {f}")
        for k, v in vals:
            if v in t:
                problems.append(f"the value of {k} (.env) in {f}")
    if not git("check-ignore", ".env").strip():
        problems.append(".env is not gitignored")
    if git("config", "--get", "core.hooksPath").strip() != HOOKS:
        problems.append(f"pre-commit secret hook not installed: git config core.hooksPath {HOOKS}")
    return problems


if __name__ == "__main__":
    p = scan("--staged" in sys.argv)
    for x in p: print("SECRET CHECK:", x, file=sys.stderr)
    if p: sys.exit("Commit blocked: remove the key, move it to .env, or gitignore the file." if "--staged" in sys.argv else 1)
    print("ok: no keys in what git would commit")
