// Gut carrier: an oral antibiotic floods the whole body and breeds resistant bacteria in the gut; a nanocarrier rides the
// blood sealed and opens only at the infection site (schematic, not to scale).
// node build.mjs [--preview [t]] [--state='{"pill":1}']  ->  gut-carrier.svg  .json  .css  .pose.js  (+ preview.html with --preview)
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../../../.claude/skills/anatomy/kit/iso-kit.mjs";
import * as G from "../../../.claude/skills/anatomy/kit/lathe.mjs";
import { tubePieces, tubeSvg } from "../../../.claude/skills/anatomy/kit/tube.mjs";
import { kitScript } from "../../../.claude/skills/anatomy/scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const NAME = "gut-carrier";
const WIDTH = 600;

// ---- world (x, y floor; z up). The gut block sits at the back, the infection site at the front, a vessel joins them along +x.
const GUT = { x: -204, y: -164, w: 120, d: 236, r: 3 }, GUT_H = 16;              // tissue floor of the gut block
const CH = { x0: -188, x1: -102, y0: GUT.y, y1: GUT.y + GUT.d };                 // the open channel (lumen), along y
const BACK_WALL = { x: GUT.x, y: GUT.y, w: CH.x0 - GUT.x, d: GUT.d, r: 2 }, BACK_H = 34;
const FRONT_WALL = { x: CH.x1, y: GUT.y, w: GUT.x + GUT.w - CH.x1, d: GUT.d, r: 2 }, FRONT_H = 9;   // cut away low to show the lumen
const FOLDS = [-110, -54, 2];                                                     // ridges across the channel floor (y)
const FOLD_D = 8, FOLD_H = 4;
const ROD_R = 5.5, ROD_L = 30;                                                   // bacteria: rods 30 long, 11 thick
const VES_Y = -50, VES_R = 8, VES_Z = VES_R + 0.5;                               // the blood vessel lies on the plinth
const SITE = { x: 70, y: -100, w: 112, d: 112, r: 6 }, SITE_H = 16;
const DOME = { c: [SITE.x + SITE.w / 2, SITE.y + SITE.d / 2], R: 42, H: 36 };
const DOME_Z = SITE_H;
const GX = GUT.x + GUT.w;                                                         // front face of the gut block

const EXTREMES = [...k.boxCorners(SITE, 0, SITE_H), ...k.boxCorners(GUT, 0, GUT_H + BACK_H), [DOME.c[0], DOME.c[1], DOME_Z + DOME.H + 4]];
const VIEW = { azimuth: 30, elevation: 40 };                                      // high enough to look down into the lumen
const pre = k.fitProjection(EXTREMES, 1000, 1000, { pad: 0, ...VIEW });
const sx = EXTREMES.map((p) => k.iso(p, pre)), bw = Math.max(...sx.map((p) => p[0])) - Math.min(...sx.map((p) => p[0])), bh = Math.max(...sx.map((p) => p[1])) - Math.min(...sx.map((p) => p[1]));
const HEIGHT = Math.round(WIDTH * bh / bw);
const P = k.fitProjection(EXTREMES, WIDTH, HEIGHT, { pad: 14, ...VIEW });

const at = (p) => k.iso(p, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (pts, style) => k.dotsSvg(pts, style);
const depth = (p) => k.depthOf(p, P);
const r1 = (v) => Math.round(v * 10) / 10;

// a seeded layout, baked at build: nothing random at runtime
function rng(seed) { return () => { seed |= 0; seed = (seed + 0x6D2B79F5) | 0; let t = Math.imul(seed ^ (seed >>> 15), 1 | seed); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
const rand = rng(20261029);

// ---- shapes
// a rod (bacterium or capsule half): a lathe body along any axis with round ends
function capsule(h, r, round = [true, true]) {
  const m = [];
  const N = 5;
  if (round[0]) { m.push([-h, 0]); for (let i = 1; i < N; i++) { const a = (i / N) * Math.PI / 2; m.push([-h + r - r * Math.cos(a), r * Math.sin(a), 1]); } m.push([-h + r, r, 1]); }
  else m.push([-h, 0], [-h, r]);
  if (round[1]) { m.push([h - r, r, 1]); for (let i = N - 1; i >= 1; i--) { const a = (i / N) * Math.PI / 2; m.push([h - r + r * Math.cos(a), r * Math.sin(a), 1]); } m.push([h, 0]); }
  else m.push([h, r], [h, 0]);
  return m;
}
const rodSvg = (c, dir, h, r, cls, round) => S(G.lathe(capsule(h, r, round), G.frameAlong(c, dir), P, { steps: 28 }), { tone: "hi", crease: "none", className: cls });
const ballSvg = (c, r, style) => S(G.sphereOf(c, r, P, { steps: 32 }), { tone: "hi", crease: "none", ...style });
const blob = (p, r, cls, extra = "") => { const [x, y] = at(p); return `<circle class="${cls}" cx="${r1(x)}" cy="${r1(y)}" r="${r}"${extra}/>`; };

// ---- the gut: bacteria laid out in the gaps between the folds
const GAPS = [];
{ const edges = [CH.y0, ...FOLDS.flatMap((y) => [y - FOLD_D / 2, y + FOLD_D / 2]), CH.y1]; for (let i = 0; i < edges.length; i += 2) GAPS.push([edges[i], edges[i + 1]]); }
// gap 0 holds the pill; the rods go in gaps 1..3
const segDist = (a0, a1, b0, b1) => { let best = Infinity; for (let i = 0; i <= 12; i++) { const t = i / 12; const p = [a0[0] + (a1[0] - a0[0]) * t, a0[1] + (a1[1] - a0[1]) * t]; for (let j = 0; j <= 12; j++) { const u = j / 12; best = Math.min(best, Math.hypot(p[0] - b0[0] - (b1[0] - b0[0]) * u, p[1] - b0[1] - (b1[1] - b0[1]) * u)); } } return best; };
const RODS = [];
const PER_GAP = [1, 5, 5, 6];
const PILL = { c: [-160, (GAPS[0][0] + GAPS[0][1]) / 2 - 2], dir: [0.94, 0.34], h: 22, r: 8.5 };
for (let g = 0; g < GAPS.length; g++) {
  const [y0, y1] = GAPS[g];
  let mine = [];
  for (let restart = 0; restart < 400 && mine.length < PER_GAP[g]; restart++) { mine = [];
  for (let tries = 0; mine.length < PER_GAP[g] && tries < 600; tries++) {
    const ang = (rand() - 0.5) * Math.PI * 1.1, dx = Math.cos(ang), dy = Math.sin(ang), hh = ROD_L / 2 - ROD_R;
    const cx = CH.x0 + 4 + rand() * (CH.x1 - CH.x0 - 8), cy = y0 + 2 + rand() * (y1 - y0 - 4);
    const a = [cx - dx * hh, cy - dy * hh], b = [cx + dx * hh, cy + dy * hh];
    const m = ROD_R + 1.5;
    if (Math.min(a[0], b[0]) < CH.x0 + m || Math.max(a[0], b[0]) > CH.x1 - m - 3 || Math.min(a[1], b[1]) < y0 + m || Math.max(a[1], b[1]) > y1 - m) continue;
    if (mine.some((o) => segDist(a, b, o.a, o.b) < ROD_R * 2 + 3.5)) continue;
    if (g === 0 && segDist(a, b, [PILL.c[0] - PILL.dir[0] * PILL.h, PILL.c[1] - PILL.dir[1] * PILL.h], [PILL.c[0] + PILL.dir[0] * PILL.h, PILL.c[1] + PILL.dir[1] * PILL.h]) < ROD_R + PILL.r + 8) continue;
    mine.push({ c: [cx, cy], a, b, dir: [dx, dy], gap: g });
  }
  }
  RODS.push(...mine);
}
// kinds: 8 helpful (green), 2 resistant (red), 7 hidden resistant that appear with `resist`
{
  // dealt in layout order (gap by gap), so each kind is spread over the lumen
  const kinds = ["g", "x", "g", "x", "g", "r", "x", "g", "x", "g", "x", "r", "g", "x", "g", "x", "g"];
  RODS.forEach((r, n) => (r.kind = kinds[n]));
}
const GREEN = RODS.filter((r) => r.kind === "g"), REDV = RODS.filter((r) => r.kind === "r"), HIDDEN = RODS.filter((r) => r.kind === "x");
GREEN.forEach((r, i) => (r.id = `bug-g-${i}`)); REDV.forEach((r, i) => (r.id = `bug-r-${i}`)); HIDDEN.forEach((r, i) => (r.id = `bug-x-${i}`));
const ROD_Z = GUT_H + ROD_R;

// drug dots on the channel floor, away from rods, folds and the pill
const GUT_DOTS = [];
for (let tries = 0; GUT_DOTS.length < 18 && tries < 20000; tries++) {
  const x = CH.x0 + 6 + rand() * (CH.x1 - CH.x0 - 14), y = CH.y0 + 6 + rand() * (CH.y1 - CH.y0 - 12);
  const g = GAPS.findIndex(([a, b]) => y > a + 4 && y < b - 4);
  if (g < 0) continue;
  if (RODS.some((r) => segDist([x, y], [x, y], r.a, r.b) < ROD_R + 6)) continue;
  if (g === 0 && Math.hypot(x - PILL.c[0], y - PILL.c[1]) < 34) continue;
  if (GUT_DOTS.some((d) => Math.hypot(d.p[0] - x, d.p[1] - y) < 13)) continue;
  GUT_DOTS.push({ p: [x, y, GUT_H + 4], gap: g, th: 0 });
}
GUT_DOTS.forEach((d) => (d.th = Math.hypot(d.p[0] - PILL.c[0], d.p[1] - PILL.c[1]) / 200));   // they spread out from the pill

// ---- the vessel and the site
const VES_A = [GX, VES_Y, VES_Z], VES_B = [SITE.x, VES_Y, VES_Z];
const VES_DOTS = Array.from({ length: 12 }, (_, i) => { const u = (i + 0.5) / 12; return { p: [VES_A[0] + (VES_B[0] - VES_A[0]) * u + (rand() - 0.5) * 5, VES_Y + (rand() - 0.5) * 4, VES_Z + 1], u }; });
const domeAt = (phi, beta, lift = 0) => { const n = [DOME.H * Math.cos(beta) * Math.cos(phi), DOME.H * Math.cos(beta) * Math.sin(phi), DOME.R * Math.sin(beta)]; const l = Math.hypot(...n);
  return [DOME.c[0] + DOME.R * Math.cos(beta) * Math.cos(phi) + lift * n[0] / l, DOME.c[1] + DOME.R * Math.cos(beta) * Math.sin(phi) + lift * n[1] / l, DOME_Z + DOME.H * Math.sin(beta) + lift * n[2] / l]; };
const deg = Math.PI / 180;
// red bacteria on the dome: lower ring, facing the viewer
const SITE_BUGS = [[-12, 26, 70], [22, 22, 20], [52, 30, 100], [80, 20, 40], [8, 52, 150]].map(([phi, beta, tw], i) => {
  const c = domeAt(phi * deg, beta * deg, ROD_R + 0.3), n = G.unit3(G.sub3(c, domeAt(phi * deg, beta * deg, 0)));
  const t1 = G.unit3(G.cross3([0, 0, 1], n)), t2 = G.cross3(n, t1);
  const dir = G.unit3(G.add3(G.mul3(t1, Math.cos(tw * deg)), G.mul3(t2, Math.sin(tw * deg))));
  return { c, dir, id: `site-bug-${i}` };
});
// drug that reaches the site with the flood: dots on the dome and the site top
const SITE_DOTS = [[-40, 12], [-5, 8], [35, 6], [65, 10], [100, 12], [-25, 40], [40, 46], [70, 50], [12, 70]].map(([phi, beta], i) => ({ p: domeAt(phi * deg, beta * deg, 4.2), th: i / 9 }))
  .concat([[SITE.x + 12, SITE.y + SITE.d - 14], [SITE.x + SITE.w - 12, SITE.y + 18], [SITE.x + SITE.w - 16, SITE.y + SITE.d - 12], [SITE.x + 20, SITE.y + 14]].map(([x, y], i) => ({ p: [x, y, SITE_H + 4], th: 0.3 + i * 0.15 })));
// nanocarrier parking spots on the upper dome
const CAR_R = 8.5;
const SPOTS = [[-45, 50], [-8, 46], [30, 44], [68, 48], [105, 54], [25, 76]].map(([phi, beta]) => domeAt(phi * deg, beta * deg, CAR_R + 0.4));
const CAR_N = SPOTS.length, LAG = 0.07;
// the shared route: from the pill along the lumen, over the front wall, through the vessel to the back of the site
const CH_ROUTE = [[PILL.c[0] + 6, PILL.c[1] + 18, GUT_H + 22], [-136, VES_Y, GUT_H + 22], [GX - 4, VES_Y, GUT_H + FRONT_H + 6], [GX + 10, VES_Y, VES_Z]];
const U_A = 0.3, U_B = 0.92;   // u < U_A in the gut, U_A..U_B in the vessel, then it surfaces at its spot on the dome
// release dots: three per carrier, thrown out from the spot over the dome
const REL = SPOTS.flatMap((s, i) => [0, 1, 2].map((j) => { const a = (i * 2.1 + j * 2.09); return { from: s, to: [s[0] + Math.cos(a) * 16, s[1] + Math.sin(a) * 16, s[2] - 3 + j * 2], car: i, j }; }));

// ---- parts, back to front
function gutBack() {
  const o = [];
  o.push(S(k.slabOf(GUT, 0, GUT_H, P, 4), { tone: "hi" }));
  o.push(S(k.slabOf(BACK_WALL, GUT_H, BACK_H, P, 4), { tone: "hi" }));
  // villi: a row of rounded nubs on the back wall's top
  const vil = [];
  for (let i = 0; i < 9; i++) { const y = GUT.y + 12 + i * ((GUT.d - 24) / 8); vil.push([BACK_WALL.x + BACK_WALL.w / 2, y]); }
  vil.sort((a, b) => depth([a[0], a[1], 0]) - depth([b[0], b[1], 0]));
  for (const [x, y] of vil) o.push(S(G.lathe([[0, 0], [0, 5], [4, 5, 1], [7, 3, 1], [8.5, 0]], G.frameAlong([x, y, GUT_H + BACK_H], [0, 0, 1]), P, { steps: 24 }), { tone: "hi", crease: "none" }));
  return o.join("");
}

function channel() {
  // painter's order: gap by gap (each fold is a full-width barrier), inside a gap by depth
  const items = [];
  FOLDS.forEach((y, i) => items.push({ key: [i + 0.5, 0], svg: S(k.slabOf({ x: CH.x0, y: y - FOLD_D / 2, w: CH.x1 - CH.x0, d: FOLD_D, r: FOLD_D / 2 }, GUT_H, FOLD_H, P, 6), { tone: "hi", crease: "none" }) }));
  for (const r of RODS) {
    const svg = rodSvg([r.c[0], r.c[1], ROD_Z], [r.dir[0], r.dir[1], 0], ROD_L / 2, ROD_R, r.kind === "g" ? "gc-g" : "gc-r", [true, true]);
    const [cx, cy] = at([r.c[0], r.c[1], ROD_Z]);
    items.push({ key: [r.gap, depth([r.c[0], r.c[1], ROD_Z])], svg: `<g data-part="${r.id}" data-c="${r1(cx)} ${r1(cy)}"${r.kind === "x" ? ' style="opacity:0"' : ""}>${svg}</g>` });
  }
  GUT_DOTS.forEach((d, i) => items.push({ key: [d.gap, depth(d.p) - 2], svg: blob(d.p, 4.5, "gc-drug", ` data-part="dg-${i}" style="opacity:0"`) }));
  // the pill: two halves along its axis, the far one first
  const pz = GUT_H + PILL.r, ax = [PILL.dir[0], PILL.dir[1], 0], c = [PILL.c[0], PILL.c[1], pz];
  const halves = [
    { id: "pill-a", c: G.add3(c, G.mul3(ax, -PILL.h / 2)), cls: "gc-cap-a" },
    { id: "pill-b", c: G.add3(c, G.mul3(ax, PILL.h / 2)), cls: "gc-cap-b" },
  ].sort((a, b) => depth(a.c) - depth(b.c));
  for (const hf of halves) {
    const round = hf.id === "pill-a" ? [true, false] : [false, true];
    items.push({ key: [0, depth(hf.c)], svg: `<g data-part="${hf.id}">${rodSvg(hf.c, ax, PILL.h / 2, PILL.r, hf.cls, round)}</g>` });
  }
  items.sort((a, b) => a.key[0] - b.key[0] || a.key[1] - b.key[1]);
  return items.map((i) => i.svg).join("");
}

function gutFront() {
  const o = [S(k.slabOf(FRONT_WALL, GUT_H, FRONT_H, P, 4), { tone: "hi" })];
  // the vessel's port on the front face: a collar
  const F = G.frameAlong([GX, VES_Y, VES_Z], [1, 0, 0]);
  o.push(S(G.lathe([[0, 0], [0, VES_R + 4], [5, VES_R + 4], [5, 0]], F, P, { steps: 36 }), { tone: "hi", crease: "none" }));
  return o.join("");
}

function vessel() {
  const pieces = tubePieces([[GX + 5, VES_Y, VES_Z], [SITE.x - 5, VES_Y, VES_Z]], VES_R, P, { maxLength: 400, caps: [false, false] });
  const o = pieces.map((p) => tubeSvg(p, { tone: "hi" }));
  // a collar at the site end (behind the block, mostly hidden) and clamps that hold the vessel to the plinth
  for (const x of [-40, 10]) {
    const F = G.frameAlong([x, VES_Y, VES_Z], [1, 0, 0]);
    o.push(S(G.lathe([[0, 0], [0, VES_R + 2.5], [6, VES_R + 2.5], [6, 0]], F, P, { steps: 36 }), { tone: "hi", crease: "none" }));
  }
  return o.join("");
}

function site() {
  const o = [];
  o.push(S(k.slabOf(SITE, 0, SITE_H, P, 6), { tone: "hi" }));
  const F = G.frameAlong([DOME.c[0], DOME.c[1], DOME_Z], [0, 0, 1]);
  o.push(S(G.lathe([[0, 0], [0, DOME.R + 5], [3, DOME.R + 5], [3, 0]], F, P, { steps: 64 }), { tone: "hi", crease: "none" }));   // rim at the dome's foot
  const mer = [[3, 0], [3, DOME.R]];
  for (let i = 1; i < 8; i++) { const b = (i / 8) * Math.PI / 2; mer.push([3 + DOME.H * Math.sin(b), DOME.R * Math.cos(b), 1]); }
  mer.push([3 + DOME.H, 0]);
  o.push(S(G.lathe(mer, F, P, { steps: 64 }), { tone: "hi", crease: "none" }));
  return o.join("");
}

function siteItems() {
  const items = [];
  for (const b of SITE_BUGS) items.push({ d: depth(b.c), svg: `<g data-part="${b.id}">${rodSvg(b.c, b.dir, ROD_L / 2, ROD_R, "gc-r", [true, true])}</g>` });
  SITE_DOTS.forEach((d, i) => items.push({ d: depth(d.p) - 1, svg: blob(d.p, 4.5, "gc-drug", ` data-part="ds-${i}" style="opacity:0"`) }));
  SPOTS.forEach((s, i) => {
    const [x, y] = at(s), r = CAR_R * G.scaleOf(P);
    // sealed carrier (site copy) and its two opened halves, cut on a slant
    const a = -0.6 + i * 0.35, ux = Math.cos(a), uy = Math.sin(a);
    const half = (sgn) => { const sa = [x - ux * r, y - uy * r], sb = [x + ux * r, y + uy * r];
      return `<path class="gc-shell" data-part="sh-${i}-${sgn > 0 ? "b" : "a"}" data-n="${r1(-uy * sgn)} ${r1(ux * sgn)} ${sgn}" data-h="${r1(sb[0])} ${r1(sb[1])}" style="opacity:0" d="M${r1(sa[0])} ${r1(sa[1])}A${r1(r)} ${r1(r)} 0 0 ${sgn > 0 ? 1 : 0} ${r1(sb[0])} ${r1(sb[1])}Z"/>`; };
    items.push({ d: depth(s), svg: `<g data-part="car-s-${i}" style="opacity:0">${ballSvg(s, CAR_R, { lit: true, className: "gc-car" })}</g>${half(-1)}${half(1)}` });
  });
  REL.forEach((d, n) => items.push({ d: depth(d.to) + 0.5, svg: blob(d.to, 4.5, "gc-drug", ` data-part="dr-${n}" style="opacity:0"`) }));
  items.sort((a, b) => a.d - b.d);
  return items.map((i) => i.svg).join("");
}

// the travelling carriers: built at the route start and moved by the pose; one copy in the lumen, one on the vessel
const CAR0 = CH_ROUTE[0];
const carCopies = (layer) => Array.from({ length: CAR_N }, (_, i) => `<g data-part="car-${layer}-${i}" style="opacity:0">${ballSvg(CAR0, CAR_R, { lit: true, className: "gc-car" })}</g>`).join("");

const body = [
  gutBack(),
  channel(),
  carCopies("c"),
  gutFront(),
  vessel(),
  `<g data-part="dv">${VES_DOTS.map((d, i) => blob(d.p, 4.5, "gc-drug", ` data-part="dv-${i}" style="opacity:0"`)).join("")}</g>`,
  carCopies("v"),
  site(),
  siteItems(),
].join("");

const svg = k.figureSvg({
  width: WIDTH, height: HEIGHT,
  label: "A cut-away block of gut with bacteria in its open channel and a pill at one end. A blood vessel runs from the gut to a small tissue block with a dome, the infection site, where red bacteria sit. Drug dots and nanocarriers travel the same route.",
  body: [body],
});

const tint = (cls, c) => {
  const mix = (p, w) => `color-mix(in srgb, ${c} ${p}%, ${w})`;
  const tones = [mix(62, "#000"), mix(80, "#000"), c, c];
  const sel = `.iso .iso-solid.${cls}`;
  return `${sel}>.iso-fill,${sel}>.iso-top{fill:${c};stroke:${c}}\n` + tones.map((t, i) => `${sel}>.iso-shade[data-shade="${i}"]{fill:${t};stroke:${t}}`).join("\n") + "\n";
};
const css = k.ISO_CSS + tint("gc-g", "var(--anatomy-green)") + tint("gc-r", "var(--anatomy-red)") + tint("gc-cap-a", "var(--anatomy-blue)") + `
.gc-cap-b>.iso-fill{fill:var(--anatomy-paper)}
.iso .iso-solid.gc-car>.iso-shade[data-shade="0"]{fill:var(--anatomy-lit-shade);stroke:var(--anatomy-lit-shade)}
.iso .iso-solid.gc-car>.iso-shade[data-shade="1"],.iso .iso-solid.gc-car>.iso-shade[data-shade="2"]{fill:var(--anatomy-lit-top);stroke:var(--anatomy-lit-top)}
.iso .iso-solid.gc-car>.iso-shade[data-shade="3"]{fill:color-mix(in srgb, var(--anatomy-lit-top) 55%, #fff);stroke:color-mix(in srgb, var(--anatomy-lit-top) 55%, #fff)}
.gc-drug{fill:var(--anatomy-blue);stroke:none}
.gc-shell{fill:var(--anatomy-lit-top);stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}
`;

const pose = (kitScript() + `
const P = ${JSON.stringify(P)};
const CH_ROUTE = ${JSON.stringify(CH_ROUTE)}, VES_A = ${JSON.stringify([GX + 10, VES_Y, VES_Z])}, VES_B = ${JSON.stringify(VES_B)};
const SPOTS = ${JSON.stringify(SPOTS.map((s) => s.map(r1)))}, CAR0 = ${JSON.stringify(CAR0)};
const REL = ${JSON.stringify(REL.map((d) => ({ s: at(d.from).map(r1), t: at(d.to).map(r1), car: d.car, j: d.j })))};
const GUT_TH = ${JSON.stringify(GUT_DOTS.map((d) => Math.round(d.th * 100) / 100))};
const VES_U = ${JSON.stringify(VES_DOTS.map((d) => Math.round(d.u * 100) / 100))};
const SITE_TH = ${JSON.stringify(SITE_DOTS.map((d) => Math.round(d.th * 100) / 100))};
const N = { g: ${GREEN.length}, r: ${REDV.length}, x: ${HIDDEN.length}, site: ${SITE_BUGS.length}, car: ${CAR_N} };
const U_A = ${U_A}, U_B = ${U_B}, LAG = ${LAG};
const lerp = (a, b, u) => a.map((v, i) => v + (b[i] - v) * u);
const routeLen = (pts) => { let l = 0; for (let i = 1; i < pts.length; i++) l += Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1], pts[i][2] - pts[i - 1][2]); return l; };
const along = (pts, u) => { let d = u * routeLen(pts); for (let i = 1; i < pts.length; i++) { const s = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1], pts[i][2] - pts[i - 1][2]); if (d <= s || i === pts.length - 1) return lerp(pts[i - 1], pts[i], Math.min(1, d / s)); d -= s; } return pts[pts.length - 1]; };
const C0 = iso(CAR0, P);
const q = {};
const part = (svg, n) => (q[n] = q[n] && svg.contains(q[n]) ? q[n] : svg.querySelector('[data-part="' + n + '"]'));
const sm = (u) => { u = Math.min(1, Math.max(0, u)); return u * u * (3 - 2 * u); };
const op = (el, v) => { el.style.opacity = v <= 0.001 ? "0" : v >= 0.999 ? "1" : v.toFixed(3); };
const scaleAbout = (el, s) => { const [cx, cy] = el.getAttribute("data-c").split(" ").map(Number); el.setAttribute("transform", s === 1 ? "" : "translate(" + cx + " " + cy + ") scale(" + s.toFixed(3) + ") translate(" + (-cx) + " " + (-cy) + ")"); };
const moveTo = (el, p) => { const [x, y] = iso(p, P); el.setAttribute("transform", "translate(" + (x - C0[0]).toFixed(2) + " " + (y - C0[1]).toFixed(2) + ")"); };
window.__ANP[${JSON.stringify(NAME)}] = {
  init: { pill: 0, spread: 0, kill: 0, resist: 0, carrier: 0, open: 0 },
  apply(svg, s, t) {
    // pill: the halves slide apart and fade, the drug fans out from it along the lumen
    const pl = sm(s.pill), sep = 12 * pl;
    for (const [n, sg] of [["pill-a", -1], ["pill-b", 1]]) {
      const el = part(svg, n); el.setAttribute("transform", translateAlong(P, [${PILL.dir[0]} * sep * sg, ${PILL.dir[1]} * sep * sg, 0]));
      op(el, 1 - sm((s.pill - 0.35) / 0.55));
    }
    GUT_TH.forEach((th, i) => op(part(svg, "dg-" + i), sm((s.pill - 0.1 - th * 0.6) / 0.2)));
    // spread: the drug rides the vessel and reaches the site (the whole body gets it)
    VES_U.forEach((u, i) => op(part(svg, "dv-" + i), sm((s.spread - u * 0.6) / 0.15)));
    SITE_TH.forEach((th, i) => op(part(svg, "ds-" + i), sm((s.spread - 0.62 - th * 0.25) / 0.12)));
    // kill: the helpful bacteria shrink and go
    for (let i = 0; i < N.g; i++) { const v = sm((s.kill - i * 0.05) / 0.6), el = part(svg, "bug-g-" + i); scaleAbout(el, 1 - 0.6 * v); op(el, 1 - v); }
    // resist: the resistant ones multiply, one by one
    for (let i = 0; i < N.x; i++) { const v = sm((s.resist - i * 0.11) / 0.25), el = part(svg, "bug-x-" + i); scaleAbout(el, 0.4 + 0.6 * v); op(el, v); }
    // carrier: sealed nanocarriers travel lumen -> vessel -> site, in a short convoy
    const arr = [];
    for (let i = 0; i < N.car; i++) {
      const u = Math.min(1, Math.max(0, (s.carrier - i * LAG) / (1 - (N.car - 1) * LAG)));
      const on = sm(s.carrier / 0.06) * (u > 0 || s.carrier > i * LAG ? 1 : 0);
      const ce = part(svg, "car-c-" + i), ve = part(svg, "car-v-" + i), se = part(svg, "car-s-" + i);
      moveTo(ce, along(CH_ROUTE, Math.min(1, u / U_A)));
      moveTo(ve, lerp(VES_A, VES_B, Math.min(1, Math.max(0, (u - U_A) / (U_B - U_A)))));
      op(ce, u < U_A ? on : 0);
      op(ve, u >= U_A && u < U_B ? on * (1 - sm((u - U_B + 0.04) / 0.04)) : 0);
      const a = sm((u - U_B) / (1 - U_B));
      arr.push(a);
      // open: at the site the carrier splits and lets the drug out there only
      const o = sm(s.open / 0.45) * a;
      op(se, a * (1 - o));
      for (const h of ["a", "b"]) {
        const el = part(svg, "sh-" + i + "-" + h), [nx, ny, sg] = el.getAttribute("data-n").split(" ").map(Number), [hx, hy] = el.getAttribute("data-h").split(" ").map(Number);
        // the shell splits like a clam: each half swings out about the hinge at one end of the cut
        el.setAttribute("transform", "translate(" + (nx * 3 * o).toFixed(2) + " " + (ny * 3 * o).toFixed(2) + ") rotate(" + (sg * 32 * o).toFixed(1) + " " + hx + " " + hy + ")");
        op(el, o);
      }
    }
    REL.forEach((d, n) => { const v = sm((s.open - 0.2 - d.j * 0.08) / 0.4) * arr[d.car], el = part(svg, "dr-" + n);
      el.setAttribute("transform", "translate(" + ((d.s[0] - d.t[0]) * (1 - v)).toFixed(2) + " " + ((d.s[1] - d.t[1]) * (1 - v)).toFixed(2) + ")"); op(el, v); });
    const cleared = sm((s.open - 0.3) / 0.6) * (arr.reduce((a, b) => a + b, 0) / N.car);
    for (let i = 0; i < N.site; i++) op(part(svg, "site-bug-" + i), 1 - sm((cleared - i * 0.06) / 0.7));
  },
};
`).replaceAll("<script", "<\\u0073cript").replaceAll("</script", "<\\/script");

writeFileSync(join(HERE, `${NAME}.svg`), svg);
writeFileSync(join(HERE, `${NAME}.css`), css);
writeFileSync(join(HERE, `${NAME}.pose.js`), pose);
const anchors = { gut: [(CH.x0 + CH.x1) / 2, (CH.y0 + CH.y1) / 2, GUT_H], pill: [PILL.c[0], PILL.c[1], GUT_H + PILL.r], vessel: [(VES_A[0] + VES_B[0]) / 2, VES_Y, VES_Z],
  site: [DOME.c[0], DOME.c[1], DOME_Z + 3 + DOME.H], bugs: [0, 1, 2].map((j) => j === 2 ? ROD_Z : RODS.reduce((a, r) => a + r.c[j], 0) / RODS.length) };
writeFileSync(join(HERE, `${NAME}.json`), JSON.stringify({ width: WIDTH, height: HEIGHT,
  params: { pill: "0..1 capsule opens, drug fills the gut", spread: "0..1 drug rides the vessel to the site (whole body)", kill: "0..1 helpful green bacteria shrink and go",
    resist: "0..1 hidden resistant red bacteria appear one by one", carrier: "0..1 sealed nanocarriers travel gut -> vessel -> site", open: "0..1 carriers at the site split, release drug there, site bacteria fade" },
  anchors: Object.fromEntries(Object.entries(anchors).map(([n, p]) => [n, at(p).map(r1)])) }, null, 1));
console.log("wrote", NAME, svg.length, "bytes", WIDTH, "x", HEIGHT, "rods", RODS.length, "scale", P.scale.toFixed(3), "rod px", r1(ROD_L * G.scaleOf(P)));

if (process.argv.includes("--preview")) {
  const t = Number(process.argv[process.argv.indexOf("--preview") + 1]) || 0;
  const st = { pill: 0, spread: 0, kill: 0, resist: 0, carrier: 0, open: 0 };
  const args = process.argv.find((a) => a.startsWith("--state="));
  if (args) Object.assign(st, JSON.parse(args.slice(8)));
  // the video's paper look (System/scripts/hfkit.py, .an.iso)
  const vars = "--anatomy-paper:#FFFFFF;--anatomy-face:#FFFFFF;--anatomy-top:#FFFFFF;--anatomy-shade-0:#C4BAA6;--anatomy-shade-1:#D4CBB9;--anatomy-shade-2:#E3DCCD;--anatomy-shade-3:#F1ECE2;--anatomy-hi:#121212;--anatomy-mid:#3D3932;--anatomy-lo:#5A554B;--anatomy-faint:#B3AA98;--anatomy-lit:#121212;--anatomy-lit-top:#FFD23F;--anatomy-lit-shade:#F0B90F;--anatomy-halo:#6F6552;--anatomy-halo-opacity:.30;--anatomy-dot:#121212;--anatomy-weight:3.2px;--anatomy-red:#D7392B;--anatomy-green:#13965A;--anatomy-blue:#2C5BEA";
  const page = `<!doctype html><html><head><meta charset="utf-8"><style>${css}body{margin:0;background:#F4EFE4}.an{width:860px;margin:20px auto;${vars}}</style></head><body><div class="an iso" data-theme="dark" id="f">${svg}</div><script>window.__ANP={};${pose};window.__ANP["${NAME}"].apply(document.querySelector("svg"),${JSON.stringify(st)},${t});</script></body></html>`;
  writeFileSync(join(HERE, "preview.html"), page);
  console.log("preview.html");
}
