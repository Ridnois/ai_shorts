// Rater: the thumbs-up tuner. Two reply cards wait in a tray: A (blue strip, the reply that agrees) and B (ink strip, the
// reply that pushes back). A thumb lever on a column rates the card under it; a tally drum on the column top counts the
// thumbs-up. An up-rated card feeds into the model box, whose dial needle swings toward AGREE; a down-rated card drops into
// the reject bin. A green clamp (the clinician-set gate) can hold the needle at centre; a lamp says green or red.
// Schematic, not to scale: preference tuning (RLHF from ratings) as a machine.
// node build.mjs [--preview [t]] [--state='{"feed":1}']  ->  rater.svg  .json  .css  .pose.js  (+ preview.html with --preview)
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../../../.claude/skills/anatomy/kit/iso-kit.mjs";
import * as G from "../../../.claude/skills/anatomy/kit/lathe.mjs";
import { kitScript } from "../../../.claude/skills/anatomy/scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const NAME = "rater";
const WIDTH = 600;

// ---- world (x, y floor; z up). Cards run along +x (screen left to right); the column stands behind the path (-y).
const BASE = { x: -214, y: -96, w: 432, d: 210, r: 8 }, BASE_H = 12;
const Z0 = BASE_H;
const DECK = { x: -206, y: -16, w: 278, d: 56, r: 2 }, DECK_H = 10;          // the card path, from the tray to the model
const CARD = { w: 54, d: 40, t: 3.5 }, CARD_Y = -8, CARD_Z = Z0 + DECK_H;    // card bottom on the deck
const X_TRAY = -196, X_RATE = -79, X_IN = 128;                                 // card left edge: tray, under the lever, fully inside the model
// column with the thumb lever on its front face (+y) and the tally drum on top
const COL = { x: -74, y: -86, w: 44, d: 40, r: 3 }, COL_H = 112;
const CX = COL.x + COL.w / 2, COL_FRONT = COL.y + COL.d, COL_TOP = Z0 + COL_H;
const PIV = [CX, COL_FRONT + 4, Z0 + 80];                                      // lever pivot (axis along y)
const ARM = 34, FIST = { s: 46, along: 13, across: 15, deep: 9 }, THUMB = { s: 66, off: 7, along: 9, across: 5.5, deep: 6.5 };
const DRUM = { cx: COL.x + COL.w + 7 + 15, cy: COL.y + COL.d / 2, z: Z0 + 94, r: 13, L: 30 };  // drum axis along x, on an axle out of the column's +x side
// model box with the dial on its front face
const MOD = { x: 72, y: -62, w: 106, d: 106, r: 3 }, MOD_H = 124;
const MFRONT = MOD.y + MOD.d, DIAL = { cx: MOD.x + MOD.w / 2, cz: Z0 + 70, R: 36, span: 60 };
const FACE_Y = MFRONT + 3;                                                     // dial face plane, 3 in front of the box
// reject bin in front of the rating spot, its back wall is the deck's front face
const BIN = { x: -96, y: DECK.y + DECK.d, w: 80, d: 58 }, BIN_H = 16;
const LAMP = { x: 196, y: 84 }, LAMP_Z = Z0 + 46;

const EXTREMES = [...k.boxCorners(BASE, 0, BASE_H), ...k.boxCorners(MOD, 0, Z0 + MOD_H + 8), ...k.boxCorners(COL, 0, COL_TOP + 5),
  [PIV[0], PIV[1], PIV[2] + THUMB.s + 8], [LAMP.x, LAMP.y, LAMP_Z + 22]];
const VIEW = { azimuth: 55, elevation: 40 };
const pre = k.fitProjection(EXTREMES, 1000, 1000, { pad: 0, ...VIEW });
const sx = EXTREMES.map((p) => k.iso(p, pre)), bw = Math.max(...sx.map((p) => p[0])) - Math.min(...sx.map((p) => p[0])), bh = Math.max(...sx.map((p) => p[1])) - Math.min(...sx.map((p) => p[1]));
const HEIGHT = Math.round(WIDTH * bh / bw);
const P = k.fitProjection(EXTREMES, WIDTH, HEIGHT, { pad: 14, ...VIEW });

const at = (p) => k.iso(p, P);
const S = (paths, style) => k.solidSvg(paths, style);
const r1 = (v) => Math.round(v * 10) / 10;
const poly = (pts, cls, extra = "") => `<path class="${cls}"${extra} d="${pts.map((p, i) => `${i ? "L" : "M"}${r1(at(p)[0])} ${r1(at(p)[1])}`).join("")}Z"/>`;
const slab = (plan, z, h, style = {}) => S(k.slabOf({ r: 1.5, ...plan }, z, h, P, 4), { tone: "hi", ...style });

// an oriented box (centre, three half-axes) as kit solid paths; the same source runs in the pose module
function obox(c, axes, P, isoF, camF) {
  const { sinA, cosA, sinE, cosE } = camF(P);
  const V = [cosA * cosE, sinA * cosE, sinE];
  const f = (v) => (Math.round(v * 10) / 10).toFixed(1).replace(/\.0$/, "");
  const pt = (sa, sb, sc) => isoF([0, 1, 2].map((i) => c[i] + sa * axes[0][i] + sb * axes[1][i] + sc * axes[2][i]), P);
  const S = [-1, 1], C = [];
  for (const a of S) for (const b of S) for (const cc of S) C.push({ s: [a, b, cc], p: pt(a, b, cc) });
  const key = (s) => s.join(",");
  const byKey = Object.fromEntries(C.map((q) => [key(q.s), q.p]));
  const path = (pts) => pts.map((p, i) => (i ? "L" : "M") + f(p[0]) + " " + f(p[1])).join("") + "Z";
  const shades = ["", "", "", ""], edges = {};
  let top = "";
  for (let i = 0; i < 3; i++) for (const s of S) {
    const len = Math.hypot(...axes[i]), n = axes[i].map((v) => (v * s) / len);
    if (n[0] * V[0] + n[1] * V[1] + n[2] * V[2] <= 1e-6) continue;
    const j = (i + 1) % 3, kk = (i + 2) % 3, ring = [[-1, -1], [1, -1], [1, 1], [-1, 1]].map(([u, v]) => { const q = [0, 0, 0]; q[i] = s; q[j] = u; q[kk] = v; return q; });
    const d = path(ring.map((q) => byKey[key(q)]));
    if (n[2] > 0.55) top += d;
    else { const h = Math.hypot(n[0], n[1]) || 1, lit = ((n[0] / h) * -sinA + (n[1] / h) * cosA + 1) / 2; shades[Math.min(3, Math.max(0, Math.floor(lit * 4)))] += d; }
    ring.forEach((q, m) => { const e = [key(q), key(ring[(m + 1) % 4])].sort().join("|"); edges[e] = (edges[e] || 0) + 1; });
  }
  const pts = C.map((q) => q.p).sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  const cr = (o, a, b) => (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
  const lo = [], hi = [];
  for (const p of pts) { while (lo.length >= 2 && cr(lo[lo.length - 2], lo[lo.length - 1], p) <= 0) lo.pop(); lo.push(p); }
  for (const p of pts.slice().reverse()) { while (hi.length >= 2 && cr(hi[hi.length - 2], hi[hi.length - 1], p) <= 0) hi.pop(); hi.push(p); }
  const hull = path(lo.slice(0, -1).concat(hi.slice(0, -1)));
  const crease = Object.entries(edges).filter(([, n]) => n === 2).map(([e]) => { const [a, b] = e.split("|").map((t) => byKey[t]); return "M" + f(a[0]) + " " + f(a[1]) + "L" + f(b[0]) + " " + f(b[1]); }).join("");
  return { fill: hull, shades, top: top || "", crease, outline: hull };
}

// the thumb lever at angle th (degrees from straight up, toward +x): arm, fist, thumb. Axis along y through PIV.
function thumbLever(th) {
  const a = (th * Math.PI) / 180, u = [Math.sin(a), 0, Math.cos(a)], w = [Math.cos(a), 0, -Math.sin(a)];
  const along = (s, off, dy) => [0, 1, 2].map((i) => PIV[i] + u[i] * s + w[i] * off + (i === 1 ? dy : 0));
  const m = (v, s) => v.map((x) => x * s);
  return [
    { c: along(ARM / 2, 0, 6), ax: [m(u, ARM / 2 + 4), m(w, 5.5), [0, 4.5, 0]] },
    { c: along(FIST.s, 0, 9), ax: [m(u, FIST.along), m(w, FIST.across), [0, FIST.deep, 0]] },
    { c: along(THUMB.s, THUMB.off, 9), ax: [m(u, THUMB.along), m(w, THUMB.across), [0, THUMB.deep, 0]] },
  ];
}
// the crank on the drum's +x end at angle ph (degrees), turning about x
function crank(ph) {
  const a = (ph * Math.PI) / 180, u = [0, Math.sin(a), Math.cos(a)], w = [0, Math.cos(a), -Math.sin(a)];
  const X = DRUM.cx + DRUM.L / 2 + 9;
  const p = (s, dx) => [X + dx, DRUM.cy + u[1] * s, DRUM.z + u[2] * s];
  return [
    { c: p(7, 0), ax: [[2, 0, 0], u.map((v) => v * 9), w.map((v) => v * 3)] },
    { c: p(15, 4), ax: [[5, 0, 0], u.map((v) => v * 2.5), w.map((v) => v * 2.5)] },
  ];
}
// a needle in the dial face plane at angle a (degrees from up, toward +x), as a polygon
function needlePts(a, D) {
  const r = (a * Math.PI) / 180, s = Math.sin(r), c = Math.cos(r);
  const pt = (along, across) => [D.cx + s * along + c * across, D.y, D.cz + c * along - s * across];
  return [pt(-7, -2.6), pt(D.R - 6, -1.6), pt(D.R - 2, 0), pt(D.R - 6, 1.6), pt(-7, 2.6)];
}
const OB = (c, axes, style) => S(obox(c, axes, P, k.iso, k.cameraOf), { tone: "hi", crease: "none", ...style });
const leverSvg = (th, cls) => thumbLever(th).map((b) => OB(b.c, b.ax, cls ? { className: cls } : {})).join("");
const crankSvg = (ph) => crank(ph).map((b) => OB(b.c, b.ax)).join("");
const TH_REST = -90;

// ---- parts, back to front
function base() {
  const o = [slab(BASE, 0, BASE_H, { crease: "none" })];
  for (const [x, y] of [[BASE.x + 10, BASE.y + 10], [BASE.x + BASE.w - 10, BASE.y + 10], [BASE.x + 10, BASE.y + BASE.d - 10], [BASE.x + BASE.w - 10, BASE.y + BASE.d - 10]])
    o.push(S(k.cylinder(x, y, 3.2, Z0, 1.6, P, 20), { tone: "hi", crease: "none" }));
  return o.join("");
}

function column() {
  const o = [];
  o.push(slab({ x: COL.x - 6, y: COL.y - 6, w: COL.w + 12, d: COL.d + 12, r: 4 }, Z0, 8));
  o.push(slab(COL, Z0 + 8, COL_H - 8, { crease: "none" }));
  o.push(slab({ x: COL.x - 3, y: COL.y - 3, w: COL.w + 6, d: COL.d + 6, r: 2 }, COL_TOP, 5));
  // a label plate on the +x side with three rule bars
  const X = COL.x + COL.w, z0 = Z0 + 22, z1 = z0 + 30, y0 = COL.y + 7, y1 = COL_FRONT - 7;
  o.push(poly([[X, y0, z0], [X, y1, z0], [X, y1, z1], [X, y0, z1]], "rt-plate"));
  for (const [z, e] of [[z0 + 8, 5], [z0 + 15, 5], [z0 + 22, 12]]) o.push(poly([[X, y0 + 5, z - 1.5], [X, y1 - e, z - 1.5], [X, y1 - e, z + 1.5], [X, y0 + 5, z + 1.5]], "rt-ink"));
  // the pivot boss on the front face
  o.push(S(G.lathe([[0, 0], [0, 10], [4, 10], [4, 0]], G.frameAlong([PIV[0], COL_FRONT, PIV[2]], [0, 1, 0]), P, { steps: 36 }), { tone: "hi", crease: "none" }));
  return o.join("");
}

function drum() {
  // the axle boss on the column's +x side
  return S(G.lathe([[0, 0], [0, 7], [5, 7], [7, 4.5], [7, 0]], G.frameAlong([COL.x + COL.w, DRUM.cy, DRUM.z], [1, 0, 0]), P, { steps: 28 }), { tone: "hi", crease: "none" });
}
function drumBody(cls) {
  const F = G.frameAlong([DRUM.cx - DRUM.L / 2, DRUM.cy, DRUM.z], [1, 0, 0]);
  const m = [[0, 0], [0, DRUM.r - 1.5], [1.5, DRUM.r], [DRUM.L - 1.5, DRUM.r], [DRUM.L, DRUM.r - 1.5], [DRUM.L, 0]];
  return S(G.lathe(m, F, P, { steps: 40 }), { tone: "hi", crease: "none", ...(cls ? { className: cls } : {}) });
}
function axleCap() {
  return S(G.lathe([[0, 0], [0, 3.5], [7, 3.5], [7, 0]], G.frameAlong([DRUM.cx + DRUM.L / 2 + 1, DRUM.cy, DRUM.z], [1, 0, 0]), P, { steps: 24 }), { tone: "hi", crease: "none" });
}

function deck() {
  const o = [slab(DECK, Z0, DECK_H, { crease: "none" })];
  // tray: a back lip and an end stop hold the stack
  o.push(slab({ x: X_TRAY - 8, y: DECK.y, w: CARD.w + 14, d: 6 }, CARD_Z, 12));
  o.push(slab({ x: X_TRAY - 8, y: DECK.y + 6, w: 6, d: DECK.d - 6 }, CARD_Z, 12));
  // two guide rails along the path, between the tray and the model
  for (const y of [DECK.y + 2]) o.push(slab({ x: X_TRAY + CARD.w + 8, y, w: MOD.x - (X_TRAY + CARD.w + 8), d: 4, r: 1 }, CARD_Z, 3));
  // rating spot: a yellow inlay under the lever
  o.push(slab({ x: X_RATE + 4, y: CARD_Y + 4, w: CARD.w - 8, d: CARD.d - 8, r: 1 }, CARD_Z, 0.6, { flat: true, crease: "none", className: "rt-pl" }));
  return o.join("");
}

function binBack() {
  const o = [slab({ x: BIN.x, y: BIN.y, w: BIN.w, d: BIN.d, r: 1 }, Z0, 1.5, { crease: "none", flat: true })];
  o.push(slab({ x: BIN.x, y: BIN.y, w: 5, d: BIN.d, r: 1 }, Z0, BIN_H));
  return o.join("");
}
function binFront() {
  const o = [slab({ x: BIN.x + BIN.w - 5, y: BIN.y, w: 5, d: BIN.d, r: 1 }, Z0, BIN_H)];
  o.push(slab({ x: BIN.x, y: BIN.y + BIN.d - 5, w: BIN.w, d: 5, r: 1 }, Z0, BIN_H, { crease: "none" }));
  // a red tab on the front wall: the reject bin
  const Y = BIN.y + BIN.d, x0 = BIN.x + 24, x1 = BIN.x + BIN.w - 24;
  o.push(poly([[x0, Y, Z0 + 4], [x1, Y, Z0 + 4], [x1, Y, Z0 + 11], [x0, Y, Z0 + 11]], "rt-red"));
  return o.join("");
}

// a reply card: base slab, a coloured strip (blue for A, ink for B) and three rule bars
function cardSvg(strip) {
  const x = X_TRAY, y = CARD_Y, z = CARD_Z + CARD.t;
  const o = [S(k.slabOf({ x, y, w: CARD.w, d: CARD.d, r: 1.5 }, CARD_Z, CARD.t, P, 3), { tone: "hi", crease: "none" })];
  o.push(S(k.slabOf({ x: x + 5, y: y + 4, w: CARD.w - 10, d: 8, r: 1 }, z, 1.4, P, 2), { tone: "hi", crease: "none", className: strip }));
  const bar = (x0, x1, yy) => poly([[x0, yy - 2, z], [x1, yy - 2, z], [x1, yy + 2, z], [x0, yy + 2, z]], "rt-ink");
  o.push(bar(x + 6, x + CARD.w - 6, y + 19), bar(x + 6, x + CARD.w - 14, y + 26), bar(x + 6, x + CARD.w - 22, y + 33));
  return o.join("");
}

function model() {
  const o = [];
  o.push(slab({ x: MOD.x - 5, y: MOD.y - 5, w: MOD.w + 10, d: MOD.d + 10, r: 4 }, Z0, 8));
  o.push(slab(MOD, Z0 + 8, MOD_H - 8, { crease: "none" }));
  o.push(slab({ x: MOD.x - 3, y: MOD.y - 3, w: MOD.w + 6, d: MOD.d + 6, r: 2 }, Z0 + MOD_H, 6));
  o.push(slab({ x: MOD.x + 20, y: MOD.y + 24, w: MOD.w - 40, d: MOD.d - 48, r: 3 }, Z0 + MOD_H + 6, 5));
  // vents on the +x side: closed slots
  const X = MOD.x + MOD.w;
  for (let i = 0; i < 5; i++) { const y0 = MOD.y + 18 + i * 15; o.push(poly([[X, y0, Z0 + 86], [X, y0 + 7, Z0 + 86], [X, y0 + 7, Z0 + 114], [X, y0, Z0 + 114]], "rt-slot")); }
  // a label plate on the +x side under the vents
  o.push(poly([[X, MOD.y + 18, Z0 + 26], [X, MOD.y + 85, Z0 + 26], [X, MOD.y + 85, Z0 + 52], [X, MOD.y + 18, Z0 + 52]], "rt-plate"));
  for (const [z, e] of [[Z0 + 34, 6], [Z0 + 43, 22]]) o.push(poly([[X, MOD.y + 24, z - 1.5], [X, MOD.y + 85 - e, z - 1.5], [X, MOD.y + 85 - e, z + 1.5], [X, MOD.y + 24, z + 1.5]], "rt-ink"));
  // screws at the front face corners
  const Y = MFRONT;
  for (const [x, z] of [[MOD.x + 9, Z0 + 18], [MOD.x + MOD.w - 9, Z0 + 18], [MOD.x + 9, Z0 + MOD_H - 9], [MOD.x + MOD.w - 9, Z0 + MOD_H - 9]])
    o.push(S(G.lathe([[0, 0], [0, 3], [1.4, 3], [1.4, 0]], G.frameAlong([x, Y, z], [0, 1, 0]), P, { steps: 16 }), { tone: "hi", crease: "none" }));
  // the dial: bezel, face, sectors, ticks
  const D = DIAL, FY = FACE_Y;
  o.push(S(G.lathe([[0, 0], [0, D.R + 6], [3, D.R + 6], [3, 0]], G.frameAlong([D.cx, Y, D.cz], [0, 1, 0]), P, { steps: 64 }), { tone: "hi", crease: "none" }));
  const arc = (r0, r1, a0, a1, n = 24) => {
    const pts = [];
    for (let i = 0; i <= n; i++) { const a = ((a0 + ((a1 - a0) * i) / n) * Math.PI) / 180; pts.push([D.cx + r1 * Math.sin(a), FY, D.cz + r1 * Math.cos(a)]); }
    for (let i = n; i >= 0; i--) { const a = ((a0 + ((a1 - a0) * i) / n) * Math.PI) / 180; pts.push([D.cx + r0 * Math.sin(a), FY, D.cz + r0 * Math.cos(a)]); }
    return pts;
  };
  const disc = [];
  for (let i = 0; i < 64; i++) { const a = (i / 64) * Math.PI * 2; disc.push([D.cx + D.R * Math.sin(a), FY, D.cz + D.R * Math.cos(a)]); }
  o.push(poly(disc, "rt-face"));
  o.push(poly(arc(D.R - 15, D.R - 5, -D.span, -4), "rt-blue"));
  o.push(poly(arc(D.R - 15, D.R - 5, 4, D.span), "rt-sector"));
  o.push(poly(arc(D.R - 15, D.R - 5, 4, D.span), "rt-yel", ' data-part="agree" style="opacity:0"'));
  o.push(poly(arc(D.R - 15, D.R - 5, 4, D.span), "rt-red", ' data-part="agree-bad" style="opacity:0"'));
  for (let i = 0; i <= 12; i++) {
    const a = -D.span + (i * 2 * D.span) / 12, big = i % 3 === 0;
    o.push(poly(arc(D.R - 5, D.R - (big ? -1 : 1), a - (big ? 1.6 : 1), a + (big ? 1.6 : 1), 2), "rt-ink"));
  }
  // the clamp bracket above the dial (the clamp pins slide out of it)
  o.push(slab({ x: D.cx - 13, y: Y, w: 26, d: 9, r: 1.5 }, D.cz + D.R + 8, 12));
  return o.join("");
}
function hub() {
  return S(G.lathe([[0, 0], [0, 5], [3, 5], [4, 3], [4, 0]], G.frameAlong([DIAL.cx, FACE_Y, DIAL.cz], [0, 1, 0]), P, { steps: 28 }), { tone: "hi", crease: "none" });
}
// the clamp: two green pins either side of the needle at centre, sliding down along z in front of the face
const PIN = { half: 2.6, gap: 5.5, len: DIAL.R + 6, y: FACE_Y + 3.5, up: 30 };
function clamp() {
  const top = DIAL.cz + DIAL.R + 8;
  const o = [];
  for (const sgn of [-1, 1]) o.push(slab({ x: DIAL.cx + sgn * PIN.gap - PIN.half, y: PIN.y, w: 2 * PIN.half, d: 5, r: 1 }, top - PIN.len, PIN.len, { crease: "none", className: "rt-g" }));
  return o.join("");
}
// the clamp's clip: only below the bracket's bottom (the pins hide inside it when raised)
const clampTop = DIAL.cz + DIAL.R + 8;

function lamp() {
  const o = [];
  o.push(S(k.cylinder(LAMP.x, LAMP.y, 14, Z0, 5, P, 40), { tone: "hi", crease: "none" }));
  o.push(S(k.cylinder(LAMP.x, LAMP.y, 5, Z0 + 5, LAMP_Z - Z0 - 5, P, 28), { tone: "hi", crease: "none" }));
  o.push(S(k.cylinder(LAMP.x, LAMP.y, 15, LAMP_Z, 5, P, 40), { tone: "hi", crease: "none" }));
  const F = G.frameAlong([LAMP.x, LAMP.y, LAMP_Z + 5], [0, 0, 1]);
  const mer = [[0, 0], [0, 14]];
  for (let i = 1; i < 8; i++) { const b = (i / 8) * Math.PI / 2; mer.push([14 * Math.sin(b), 14 * Math.cos(b), 1]); }
  mer.push([14, 0]);
  const dome = (cls) => S(G.lathe(mer, F, P, { steps: 48 }), { tone: "hi", crease: "none", ...(cls ? { className: cls } : {}) });
  o.push(dome(), `<g data-part="lamp-ok" style="opacity:0">${dome("rt-g")}</g>`, `<g data-part="lamp-bad" style="opacity:0">${dome("rt-r")}</g>`);
  return o.join("");
}

// clips: card A disappears into the model's -x face; the clamp pins show only below the bracket
const scr = (pts) => pts.map((p, i) => `${i ? "L" : "M"}${r1(at(p)[0])} ${r1(at(p)[1])}`).join("") + "Z";
const clipPin = `<clipPath id="rater-pin"><path d="${scr([[DIAL.cx - 60, PIN.y, clampTop], [DIAL.cx + 60, PIN.y, clampTop], [DIAL.cx + 60, PIN.y, -200], [DIAL.cx - 60, PIN.y, -200]])}"/></clipPath>`;
// the clip of card A must cover the whole card plane left of the model at any screen height: use a tall band
const clipA2 = (() => {
  const a = at([MOD.x, -400, CARD_Z]), b = at([MOD.x, 400, CARD_Z]);
  // everything on the left of the line through a and b (screen), extended far
  const dx = b[0] - a[0], dy = b[1] - a[1], L = 4000 / Math.hypot(dx, dy);
  const A = [a[0] - dx * L, a[1] - dy * L], B = [a[0] + dx * L, a[1] + dy * L];
  const nx = dy, ny = -dx, M = 4000 / Math.hypot(nx, ny);              // normal pointing to -x side
  const s = (nx * (at([MOD.x - 50, 0, CARD_Z])[0] - a[0]) + ny * (at([MOD.x - 50, 0, CARD_Z])[1] - a[1])) > 0 ? 1 : -1;
  const C = [B[0] + s * nx * M, B[1] + s * ny * M], D = [A[0] + s * nx * M, A[1] + s * ny * M];
  return `<clipPath id="rater-in"><path d="M${r1(A[0])} ${r1(A[1])}L${r1(B[0])} ${r1(B[1])}L${r1(C[0])} ${r1(C[1])}L${r1(D[0])} ${r1(D[1])}Z"/></clipPath>`;
})();

const body = [
  `<defs>${clipA2}${clipPin}</defs>`,
  base(),
  column(),
  drum(),
  `<g data-part="drum">${drumBody()}</g>`,
  `<g data-part="drum-lit" style="opacity:0">${drumBody("rt-y")}</g>`,
  axleCap(),
  `<g data-part="crank">${crankSvg(0)}</g>`,
  `<g data-part="lever">${leverSvg(TH_REST)}</g>`,
  `<g data-part="lever-up" style="opacity:0"></g>`,
  `<g data-part="lever-down" style="opacity:0"></g>`,
  deck(),
  binBack(),
  `<g data-part="card-b">${cardSvg("rt-k")}</g>`,
  `<g clip-path="url(#rater-in)"><g data-part="card-a" transform="${k.translateAlong(P, [0, 0, CARD.t])}">${cardSvg("rt-b")}</g></g>`,
  binFront(),
  model(),
  `<g data-part="needle">${poly(needlePts(0, { ...DIAL, y: FACE_Y + 1 }), "rt-needle")}</g>`,
  hub(),
  `<g clip-path="url(#rater-pin)"><g data-part="clamp" transform="${k.translateAlong(P, [0, 0, PIN.up + PIN.len - 20])}">${clamp()}</g></g>`,
  lamp(),
].join("");

const svg = k.figureSvg({
  width: WIDTH, height: HEIGHT,
  label: "A rating machine: two reply cards wait in a tray, one with a blue strip that agrees and one with a dark strip that pushes back. A thumb lever on a column rates the card under it and a drum on top counts the thumbs-up. Up-rated cards feed into a model box whose dial needle swings toward agree; down-rated cards drop into a reject bin. A green clamp can hold the needle at centre, and a lamp on a post lights green or red.",
  body: [body],
});

const tint = (cls, c) => {
  const mix = (p, w) => `color-mix(in srgb, ${c} ${p}%, ${w})`;
  const tones = [mix(62, "#000"), mix(80, "#000"), c, c];
  const sel = `.iso .iso-solid.${cls}`;
  return `${sel}>.iso-fill,${sel}>.iso-top{fill:${c};stroke:${c}}\n` + tones.map((t, i) => `${sel}>.iso-shade[data-shade="${i}"]{fill:${t};stroke:${t}}`).join("\n") + "\n";
};
const flat = (cls, fill) => `.${cls}{fill:${fill};stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}\n`;
const css = k.ISO_CSS + tint("rt-g", "var(--anatomy-green)") + tint("rt-r", "var(--anatomy-red)") + tint("rt-b", "var(--anatomy-blue)") + tint("rt-k", "var(--anatomy-mid)")
  + tint("rt-pl", "var(--anatomy-shade-2)") + `
.iso .iso-solid.rt-y>.iso-fill,.iso .iso-solid.rt-y>.iso-top{fill:var(--anatomy-lit-top);stroke:var(--anatomy-lit-top)}
.iso .iso-solid.rt-y>.iso-shade{fill:var(--anatomy-lit-shade);stroke:var(--anatomy-lit-shade)}
.iso .iso-solid.rt-y>.iso-shade[data-shade="2"],.iso .iso-solid.rt-y>.iso-shade[data-shade="3"]{fill:var(--anatomy-lit-top);stroke:var(--anatomy-lit-top)}
.rt-ink{fill:var(--anatomy-hi);stroke:none}
.rt-needle{fill:var(--anatomy-hi);stroke:var(--anatomy-hi);stroke-width:1px;stroke-linejoin:round;vector-effect:non-scaling-stroke}
` + flat("rt-plate", "var(--anatomy-shade-3)") + flat("rt-slot", "var(--anatomy-mid)") + flat("rt-face", "var(--anatomy-face)")
  + flat("rt-sector", "var(--anatomy-shade-2)") + flat("rt-blue", "color-mix(in srgb, var(--anatomy-blue) 30%, #fff)")
  + flat("rt-yel", "var(--anatomy-lit-top)") + flat("rt-red", "var(--anatomy-red)");

const pose = (kitScript() + `
const P = ${JSON.stringify(P)};
${obox.toString()}
const PIV = ${JSON.stringify(PIV)}, ARM = ${ARM}, FIST = ${JSON.stringify(FIST)}, THUMB = ${JSON.stringify(THUMB)}, DRUM = ${JSON.stringify(DRUM)}, DIAL = ${JSON.stringify(DIAL)};
${thumbLever.toString()}
${crank.toString()}
${needlePts.toString()}
const X_TRAY = ${X_TRAY}, X_RATE = ${X_RATE}, X_IN = ${X_IN}, CARD = ${JSON.stringify(CARD)}, BIN = ${JSON.stringify(BIN)}, CARD_Y = ${CARD_Y}, CARD_Z = ${CARD_Z}, Z0 = ${Z0};
const FACE_Y = ${FACE_Y}, PIN = ${JSON.stringify(PIN)}, TH_REST = ${TH_REST};
const q = {};
const part = (svg, n) => (q[n] = q[n] && svg.contains(q[n]) ? q[n] : svg.querySelector('[data-part="' + n + '"]'));
const sm = (u) => { u = Math.min(1, Math.max(0, u)); return u * u * (3 - 2 * u); };
const op = (el, v) => { el.style.opacity = v <= 0.001 ? "0" : v >= 0.999 ? "1" : v.toFixed(3); };
const OB = (c, axes, cls) => solidSvg(obox(c, axes, P, iso, cameraOf), cls ? { tone: "hi", crease: "none", className: cls } : { tone: "hi", crease: "none" });
const r1 = (v) => (Math.round(v * 10) / 10);
const last = new WeakMap();
const setHtml = (el, key, html) => { if (last.get(el) !== key) { last.set(el, key); el.innerHTML = html(); } };
window.__ANP[${JSON.stringify(NAME)}] = {
  init: { feed: 0, up: 0, down: 0, tune: 0, ok: 0, bad: 0 },
  apply(svg, s, t) {
    // feed: card A (top of the stack) slides to the rating spot (0.5) and on into the model (1)
    const fa = sm(s.feed / 0.5), fb = sm((s.feed - 0.5) / 0.5);
    const xa = (X_RATE - X_TRAY) * fa + (X_IN - X_RATE) * fb;
    const za = CARD.t * (1 - sm((s.feed - 0.24) / 0.1));                // clear of B, it steps down off the stack onto the deck
    part(svg, "card-a").setAttribute("transform", translateAlong(P, [xa, 0, za]));
    op(part(svg, "card-a"), s.feed > 0.98 ? 0 : 1);
    // down: card B (on the deck under A) slides to the rating spot, then off the deck into the bin
    const da = sm(s.down / 0.4), db = sm((s.down - 0.6) / 0.4);
    const bx = (X_RATE - X_TRAY) * da + (BIN.x + 13 - X_RATE) * db;
    const by = (BIN.y + 9 - CARD_Y) * db;
    const fall = (CARD_Z - (Z0 + 1.5)) * sm((s.down - 0.75) / 0.25);
    const bz = -fall;
    part(svg, "card-b").setAttribute("transform", translateAlong(P, [bx, by, bz]));
    // the lever: up swings to thumb-up (yellow), down to thumb-down (red); otherwise it rests pointing at the tray
    const u = sm((s.up - 0.1) / 0.5), d = sm((s.down - 0.35) / 0.3);
    const th = Math.round((TH_REST + 90 * u - 90 * d) * 10) / 10;
    const lv = (cls) => () => thumbLever(th).map((b) => OB(b.c, b.ax, cls)).join("");
    setHtml(part(svg, "lever"), th, lv());
    setHtml(part(svg, "lever-up"), th, lv("rt-y"));
    setHtml(part(svg, "lever-down"), th, lv("rt-r"));
    op(part(svg, "lever-up"), u);
    op(part(svg, "lever-down"), d * (1 - u));
    // the tally drum: lights and its crank turns one and a half turns on a thumb-up
    op(part(svg, "drum-lit"), sm((s.up - 0.4) / 0.3));
    const ph = Math.round(540 * sm((s.up - 0.3) / 0.7));
    setHtml(part(svg, "crank"), ph, () => crank(ph).map((b) => OB(b.c, b.ax)).join(""));
    // the dial: tune swings the needle to full agree; the clamp (ok) holds it at centre
    const clamp = sm(s.ok / 0.5);
    const a = Math.round(DIAL.span * sm(s.tune) * (1 - clamp) * 10) / 10;
    setHtml(part(svg, "needle"), a, () => { const pts = needlePts(a, { ...DIAL, y: FACE_Y + 1 }); return '<path class="rt-needle" d="' + pts.map((p, i) => (i ? "L" : "M") + iso(p, P).map(r1).join(" ")).join("") + 'Z"/>'; });
    part(svg, "clamp").setAttribute("transform", translateAlong(P, [0, 0, (PIN.up + PIN.len - 20) * (1 - clamp)]));
    op(part(svg, "agree"), sm(s.tune / 0.6) * (1 - clamp) * (1 - sm(s.bad / 0.3)));
    op(part(svg, "agree-bad"), sm(s.bad / 0.3));
    op(part(svg, "lamp-ok"), sm(s.ok / 0.3) * (1 - sm(s.bad / 0.3)));
    op(part(svg, "lamp-bad"), sm(s.bad / 0.3));
  },
};
`).replaceAll("<script", "<\\u0073cript").replaceAll("</script", "<\\/script");

writeFileSync(join(HERE, `${NAME}.svg`), svg);
writeFileSync(join(HERE, `${NAME}.css`), css);
writeFileSync(join(HERE, `${NAME}.pose.js`), pose);
const anchors = {
  tray: [X_TRAY + CARD.w / 2, CARD_Y + CARD.d / 2, CARD_Z + 2 * CARD.t],
  lever: [PIV[0], PIV[1], PIV[2]],
  counter: [DRUM.cx, DRUM.cy, DRUM.z],
  dial: [DIAL.cx, FACE_Y, DIAL.cz],
  needle: [DIAL.cx, FACE_Y, DIAL.cz + DIAL.R - 4],
  reject: [BIN.x + BIN.w / 2, BIN.y + BIN.d / 2, Z0 + 2],
  lamp: [LAMP.x, LAMP.y, LAMP_Z + 14],
  slot: [MOD.x, CARD_Y + CARD.d / 2, CARD_Z + CARD.t],
};
writeFileSync(join(HERE, `${NAME}.json`), JSON.stringify({ width: WIDTH, height: HEIGHT,
  params: {
    feed: "0..1 card A (blue strip, agrees) slides from the tray to the rating spot under the lever (0.5) and into the model (1, gone)",
    up: "0..1 the thumb lever swings to thumb-up and lights yellow; the tally drum lights and its crank turns",
    down: "0..1 card B (ink strip, pushes back) slides to the rating spot, the lever swings to thumb-down (red), B drops into the reject bin",
    tune: "0..1 the dial needle swings from centre to full AGREE (right); the agree sector fills yellow",
    ok: "0..1 lamp green; the green clamp pins drop in front of the dial and hold the needle at centre (even with tune 1)",
    bad: "0..1 lamp red; the agree sector turns red",
  },
  anchors: Object.fromEntries(Object.entries(anchors).map(([n, p]) => [n, at(p).map(r1)])) }, null, 1));
console.log("wrote", NAME, svg.length, "bytes", WIDTH, "x", HEIGHT, "scale", P.scale.toFixed(3));

if (process.argv.includes("--preview")) {
  const t = Number(process.argv[process.argv.indexOf("--preview") + 1]) || 0;
  const st = { feed: 0, up: 0, down: 0, tune: 0, ok: 0, bad: 0 };
  const args = process.argv.find((a) => a.startsWith("--state="));
  if (args) Object.assign(st, JSON.parse(args.slice(8)));
  const vars = "--anatomy-paper:#FFFFFF;--anatomy-face:#FFFFFF;--anatomy-top:#FFFFFF;--anatomy-shade-0:#C4BAA6;--anatomy-shade-1:#D4CBB9;--anatomy-shade-2:#E3DCCD;--anatomy-shade-3:#F1ECE2;--anatomy-hi:#121212;--anatomy-mid:#3D3932;--anatomy-lo:#5A554B;--anatomy-faint:#B3AA98;--anatomy-lit:#121212;--anatomy-lit-top:#FFD23F;--anatomy-lit-shade:#F0B90F;--anatomy-halo:#6F6552;--anatomy-halo-opacity:.30;--anatomy-dot:#121212;--anatomy-weight:3.2px;--anatomy-red:#D7392B;--anatomy-green:#13965A;--anatomy-blue:#2C5BEA";
  const page = `<!doctype html><html><head><meta charset="utf-8"><style>${css}body{margin:0;background:#F4EFE4}.an{width:860px;margin:20px auto;${vars}}</style></head><body><div class="an iso" data-theme="dark" id="f">${svg}</div><script>window.__ANP={};${pose};window.__ANP["${NAME}"].apply(document.querySelector("svg"),${JSON.stringify(st)},${t});</script></body></html>`;
  writeFileSync(join(HERE, "preview.html"), page);
  console.log("preview.html");
}
