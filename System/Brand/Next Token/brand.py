#!/usr/bin/env python3
"""Next Token: avatar (800x800), banner (2560x1440) and the mascot sheet, drawn as pages in the paper look
(System/Look.md) and shot with the HyperFrames headless Chrome.
Mascot, "Tok": a yellow token tile with a thick ink outline and two eyes; the next token a model is about to say.
    python3 "System/Brand/Next Token/brand.py"     (writes nt-avatar.png, nt-avatar-small.png, nt-banner.png, nt-mascot.png here)"""
import glob, os, subprocess, sys

OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT, "..", "..", "scripts"))
import hfkit as K

FONTS = os.path.join(OUT, "..", "..", "scripts", "vendor", "fonts")
CSS = K.FACES.replace("assets/fonts/", f"file://{os.path.abspath(FONTS)}/") + f"""
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:{K.PAPER}; font-family:Inter; color:{K.INK}; overflow:hidden; }}
.ground {{ position:absolute; inset:0; background:{K.PAPER};
  background-image: radial-gradient(circle at 4px 4px, rgba(18,18,18,0.10) 3px, transparent 3.6px); background-size:64px 64px; }}
.tile {{ position:absolute; display:flex; align-items:center; justify-content:center; border:10px solid {K.INK}; border-radius:44px;
  background:{K.WHITE}; box-shadow:16px 16px 0 {K.INK}; font-family:"Inter Display"; font-weight:900; letter-spacing:-0.03em; }}
.big {{ font-family:"Inter Display"; font-weight:900; letter-spacing:-0.04em; line-height:0.92; }}
.hot {{ background:{K.YELLOW}; padding:0 0.08em; border-radius:0.1em; box-shadow:0 0 0 0.05em {K.INK} inset; }}
"""


def tok(x, y, s, look=(0, 0), blink=False):
    """The mascot at (x, y), s px wide: a yellow tile, two eyes (pupils shifted by look), a small smile."""
    lx, ly = look
    eye = lambda cx: (f'<ellipse cx="{cx}" cy="92" rx="17" ry="{4 if blink else 23}" fill="{K.WHITE}" stroke="{K.INK}" stroke-width="7"/>'
                      + ("" if blink else f'<circle cx="{cx + 5 + lx}" cy="{96 + ly}" r="9" fill="{K.INK}"/>'))
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px" width="{s}" height="{s}" viewBox="0 0 200 200">'
            f'<rect x="22" y="26" width="164" height="164" rx="34" fill="{K.INK}"/>'
            f'<rect x="10" y="12" width="164" height="164" rx="34" fill="{K.YELLOW}" stroke="{K.INK}" stroke-width="9"/>'
            + eye(68) + eye(118) +
            f'<path d="M76 132 Q93 146 110 132" fill="none" stroke="{K.INK}" stroke-width="8" stroke-linecap="round"/>'
            f'<rect x="146" y="40" width="9" height="34" rx="4" fill="{K.INK}"/></svg>')


def page(w, h, inner):
    return f'<!doctype html><html><head><meta charset="UTF-8"/><style>{CSS}</style></head><body style="width:{w}px;height:{h}px"><div class="ground"></div>{inner}</body></html>'


def shoot(html_, w, h, out):
    chrome = sorted(glob.glob(os.path.expanduser("~/.cache/hyperframes/chrome/chrome-headless-shell/*/chrome-headless-shell-linux64/chrome-headless-shell")))
    if not chrome:
        sys.exit("no headless Chrome: run any `npx hyperframes snapshot` once to install it")
    src = f"{OUT}/_page.html"
    open(src, "w").write(html_)
    subprocess.run([chrome[-1], "--no-sandbox", "--hide-scrollbars", "--allow-file-access-from-files", f"--window-size={w},{h}",
                    "--virtual-time-budget=3000", f"--screenshot={out}", f"file://{src}"], capture_output=True, check=True)
    os.remove(src)
    print("wrote", os.path.basename(out))


def avatar():
    inner = tok(97, 92, 660, look=(3, 2))
    shoot(page(800, 800, inner), 800, 800, f"{OUT}/nt-avatar.png")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f"{OUT}/nt-avatar.png", "-vf", "scale=98:98:flags=lanczos", f"{OUT}/nt-avatar-small.png"], check=True)


def banner():
    # safe area for every device: 1546 x 423 centred (x 507..2053, y 508..931)
    words = [("how", 240), ("AI", 170), ("really", 300)]
    x, tiles = 560, ""
    for t, w in words:
        tiles += f'<div class="tile" style="left:{x}px;top:515px;width:{w}px;height:150px;font-size:92px">{t}</div>'
        x += w + 40
    tiles += tok(x - 18, 473, 228, look=(-4, 4))
    inner = (tiles +
             f'<div class="big" style="position:absolute;left:560px;top:700px;font-size:140px">Next <span class="hot">Token</span></div>'
             f'<div style="position:absolute;left:1325px;top:722px;width:740px;font-size:42px;font-weight:800;line-height:1.3">'
             f'How AI works · Agents at work<br>What\'s coming · <span style="color:{K.MUTED}">Mon to Fri</span></div>')
    shoot(page(2560, 1440, inner), 2560, 1440, f"{OUT}/nt-banner.png")


def mascot():
    inner = "".join(tok(40 + k * 330, 60, 280, look=lk, blink=b) for k, (lk, b) in enumerate([((0, 0), False), ((-8, 0), False), ((8, 6), False), ((0, 0), True)]))
    shoot(page(1400, 400, inner), 1400, 400, f"{OUT}/nt-mascot.png")


if __name__ == "__main__":
    avatar(); banner(); mascot()
