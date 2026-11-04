#!/usr/bin/env python3
"""Put one key into .env without it ever appearing on screen or in a chat log (Build §Upload).
    python3 System/scripts/set_key.py APIFY_TOKEN        # asks for the value with hidden input
    python3 System/scripts/set_key.py GEMINI_API_KEY
Run it in your own terminal (not through the agent): the value is read with getpass and written to .env (0600).
Prints only the key name and the value's length."""
import getpass, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))   # .env lives at the vault root
from youtube_auth import set_env

if len(sys.argv) != 2 or not re.fullmatch(r"[A-Z][A-Z0-9_]+", sys.argv[1]):
    sys.exit(__doc__)
v = getpass.getpass(f"{sys.argv[1]} (input hidden): ").strip()
if not v:
    sys.exit("nothing entered; .env unchanged")
set_env(sys.argv[1], v)
print(f"saved {sys.argv[1]} to .env ({len(v)} characters)")
