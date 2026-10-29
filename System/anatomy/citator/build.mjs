// Citator: a citation card goes through a reader that looks it up in a cabinet of case reporters; a lamp and a stamp say
// found or not found (schematic, not to scale). An AI writes a likely-looking citation; this machine checks it is real.
// node build.mjs [--preview [t]] [--state='{"feed":1}']  ->  citator.svg  .json  .css  .pose.js  (+ preview.html with --preview)
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../../../.claude/skills/anatomy/kit/iso-kit.mjs";
import * as G from "../../../.claude/skills/anatomy/kit/lathe.mjs";
import { tubePieces, tubeSvg } from "../../../.claude/skills/anatomy/kit/tube.mjs";
import { kitScript } from "../../../.claude/skills/anatomy/scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const NAME = "citator";
const WIDTH = 600;

// ---- world (x, y floor; z up). The card runs along +x (screen left to right); the cabinet stands behind (-y).
const BASE = { x: -162, y: -152, w: 334, d: 216, r: 8 }, BASE_H = 12;
const Z0 = BASE_H;
// cabinet of drawers: 3 x 3 volumes of case reporters, faces looking +y
const CELL = { w: 54, h: 38, gap: 7 };
const CAB = { x: -80, y: -144, w: 3 * CELL.w + 4 * CELL.gap, d: 58 };
const CAB_FRONT = CAB.y + CAB.d;                                  // y of the carcass front
const PLINTH_H = 12, CAB_Z1 = Z0 + PLINTH_H + 3 * CELL.h + 4 * CELL.gap;
const FACE_T = 4;                                                 // drawer face thickness
const cellOf = (row, col) => ({ x: CAB.x + CELL.gap + col * (CELL.w + CELL.gap), z: Z0 + PLINTH_H + CELL.gap + (2 - row) * (CELL.h + CELL.gap) });
const MATCH = { row: 1, col: 2 };
const POP = 7, PULL = 44;                                         // a passing scan pops a drawer out 7; the match pulls out 44
// the card: lies flat, travels along x at one height through the reader
const CARD = { w: 62, d: 44, t: 3 }, CARD_Y = -4, CARD_Z = Z0 + 8;   // card bottom
const X_TRAY = -144, X_SLOT = -44, X_LAND = 52;                   // card left edge at each stop
const TRAY = { x: -152, y: -10, w: 84, d: 58, r: 4 };
const SLOT = { x: -56, y: -18, w: 86, d: 70, r: 4 }, SLOT_H = 50;   // reader box; the card fits inside it whole
const LAND = { x: 42, y: -10, w: 90, d: 58, r: 4 };
// stamp: a lever on a fork post behind the landing spot, swinging about an axis along x
const ARM_X = X_LAND + CARD.w / 2, ARM_Y = -38, HEAD = { h: 22, half: 14 };
const PIVOT = [ARM_X, ARM_Y, CARD_Z + CARD.t + HEAD.h + 5.5];
const REACH = CARD_Y + CARD.d / 2 - ARM_Y;                        // pivot to the head's axis
const ARM_UP = 30;                                                // degrees raised at rest
// lamp
const LAMP = { x: 148, y: -44 }, LAMP_Z = Z0 + 50;

const EXTREMES = [...k.boxCorners(BASE, 0, BASE_H), ...k.boxCorners({ x: CAB.x - 3, y: CAB.y - 3, w: CAB.w + 6, d: CAB.d + 6 }, 0, CAB_Z1 + 8), [LAMP.x, LAMP.y, LAMP_Z + 22]];
const VIEW = { azimuth: 58, elevation: 36 };
const pre = k.fitProjection(EXTREMES, 1000, 1000, { pad: 0, ...VIEW });
const sx = EXTREMES.map((p) => k.iso(p, pre)), bw = Math.max(...sx.map((p) => p[0])) - Math.min(...sx.map((p) => p[0])), bh = Math.max(...sx.map((p) => p[1])) - Math.min(...sx.map((p) => p[1]));
const HEIGHT = Math.round(WIDTH * bh / bw);
const P = k.fitProjection(EXTREMES, WIDTH, HEIGHT, { pad: 14, ...VIEW });

const at = (p) => k.iso(p, P);
const S = (paths, style) => k.solidSvg(paths, style);
const depth = (p) => k.depthOf(p, P);
const r1 = (v) => Math.round(v * 10) / 10;
const poly = (pts, cls, extra = "") => `<path class="${cls}"${extra} d="${pts.map((p, i) => `${i ? "L" : "M"}${r1(at(p)[0])} ${r1(at(p)[1])}`).join("")}Z"/>`;
const slab = (plan, z, h, style = {}) => S(k.slabOf({ r: 1.5, ...plan }, z, h, P, 4), { tone: "hi", ...style });

// an oriented box (centre, three half-axes) as kit solid paths: used for the stamp lever, which turns about x.
// The same source runs in the pose module, so the drawing at any angle is the build's drawing.
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
const OB = (c, axes, style) => S(obox(c, axes, P, k.iso, k.cameraOf), { tone: "hi", ...style });

// the stamp lever at angle th (degrees, up positive): arm, grip, head
function lever(th) {
  const a = (th * Math.PI) / 180, u = [0, Math.cos(a), Math.sin(a)], w = [0, -Math.sin(a), Math.cos(a)];
  const along = (s, up) => [0, 1, 2].map((i) => PIVOT[i] + u[i] * s + w[i] * up);
  const m = (v, s) => v.map((x) => x * s);
  const arm = { c: along((REACH + 12 - 12) / 2, 0), ax: [[6, 0, 0], m(u, (REACH + 12 + 12) / 2), m(w, 5)] };
  const head = { c: along(REACH, -5 - HEAD.h / 2), ax: [[HEAD.half, 0, 0], m(u, HEAD.half), m(w, HEAD.h / 2)] };
  const knob = { c: along(REACH, 5 + 6), ax: [[5, 0, 0], m(u, 5), m(w, 6)] };
  const tail = { c: along(-14, 0), ax: [[8, 0, 0], m(u, 7), m(w, 8)] };
  return { arm, head, knob, tail };
}

// ---- parts, back to front
function base() {
  const o = [slab(BASE, 0, BASE_H, { crease: "none" })];
  // corner screws on the plate
  for (const [x, y] of [[BASE.x + 10, BASE.y + BASE.d - 10], [BASE.x + BASE.w - 10, BASE.y + BASE.d - 10], [BASE.x + BASE.w - 10, BASE.y + 10]])
    o.push(S(k.cylinder(x, y, 3.2, Z0, 1.6, P, 20), { tone: "hi", crease: "none" }));
  return o.join("");
}

function cabinet() {
  const o = [];
  o.push(slab({ x: CAB.x + 4, y: CAB.y + 4, w: CAB.w - 8, d: CAB.d - 6 }, Z0, PLINTH_H));
  o.push(slab({ x: CAB.x, y: CAB.y, w: CAB.w, d: CAB.d }, Z0 + PLINTH_H, CAB_Z1 - Z0 - PLINTH_H, { crease: "none" }));
  o.push(slab({ x: CAB.x - 3, y: CAB.y - 3, w: CAB.w + 6, d: CAB.d + 6, r: 2 }, CAB_Z1, 6, { crease: "none" }));
  // a label frame on the side (+x) of the carcass
  const X = CAB.x + CAB.w, z0 = Z0 + PLINTH_H + 40, z1 = z0 + 26, y0 = CAB.y + 14, y1 = CAB_FRONT - 14;
  o.push(poly([[X, y0, z0], [X, y1, z0], [X, y1, z1], [X, y0, z1]], "ct-plate"));
  for (const z of [z0 + 9, z0 + 17]) o.push(poly([[X, y0 + 6, z - 1.6], [X, z === z0 + 9 ? y1 - 6 : y1 - 16, z - 1.6], [X, z === z0 + 9 ? y1 - 6 : y1 - 16, z + 1.6], [X, y0 + 6, z + 1.6]], "ct-ink"));
  return o.join("");
}

// a drawer: a body rebuilt by the pose as it pulls out, then the face, handle and label plate that move together
const DRAWERS = [];
for (let row = 2; row >= 0; row--) for (let col = 0; col < 3; col++) DRAWERS.push({ row, col, ...cellOf(row, col), match: row === MATCH.row && col === MATCH.col });
// scan order: reading order, top row first
DRAWERS.forEach((d) => (d.order = d.row * 3 + d.col));
const MCARD = { inset: 9, back: 22, t: 3, h: 18 };          // the case card standing in the match drawer
function drawer(d) {
  const y = CAB_FRONT, cx = d.x + CELL.w / 2, mid = d.z + CELL.h / 2;
  const mv = [];
  if (d.match) {
    const cy = y - MCARD.back, zt = d.z + CELL.h, cz = zt + MCARD.h;
    const card = { x: d.x + MCARD.inset, y: cy, w: CELL.w - 2 * MCARD.inset, d: MCARD.t, r: 0.5 };
    const fy = cy + MCARD.t;
    const bar = (x0, x1, z) => poly([[x0, fy, z - 1.8], [x1, fy, z - 1.8], [x1, fy, z + 1.8], [x0, fy, z + 1.8]], "ct-ink");
    mv.push(`<g data-part="mcard" style="opacity:0">${S(k.slabOf(card, zt, MCARD.h, P, 2), { tone: "hi", crease: "none", className: "ct-y" })}${bar(card.x + 5, card.x + card.w - 5, cz - 5)}${bar(card.x + 5, card.x + card.w - 12, cz - 11)}</g>`);
  }
  mv.push(slab({ x: d.x, y, w: CELL.w, d: FACE_T, r: 2 }, d.z, CELL.h, { crease: "none" }));
  // label plate (white, with a yellow copy the scan lights) and a handle
  const lp = { x: cx - 12, y: y + FACE_T, w: 24, d: 1.6, r: 0.5 };
  mv.push(slab(lp, mid + 4, 10, { crease: "none" }));
  mv.push(`<g data-part="lab-${d.order}" style="opacity:0">${slab(lp, mid + 4, 10, { crease: "none", className: "ct-y" })}</g>`);
  mv.push(slab({ x: cx - 10, y: y + FACE_T, w: 20, d: 5, r: 2 }, mid - 9, 6, { crease: "none" }));
  return `<g data-part="drawer-${d.order}"><g data-part="body-${d.order}"></g><g data-part="mv-${d.order}">${mv.join("")}</g></g>`;
}

function tray() {
  const o = [slab(TRAY, Z0, 7)];
  // the tray floor sits at CARD_Z; a back lip and an end stop hold the card
  o.push(slab({ x: TRAY.x, y: TRAY.y, w: TRAY.w, d: 6 }, Z0 + 7, 9));
  o.push(slab({ x: TRAY.x, y: TRAY.y + 6, w: 6, d: TRAY.d - 6 }, Z0 + 7, 9));
  o.push(slab({ x: TRAY.x + 6, y: TRAY.y + 6, w: TRAY.w - 6, d: TRAY.d - 6, r: 1 }, Z0 + 7, 1, { flat: true, crease: "none" }));
  return o.join("");
}

// the card: base solid, a red copy (bad), the yellow header strip, ink bars and, on the landed copy, the stamp marks
function cardSvg(copy) {
  const x = X_TRAY, y = CARD_Y, z = CARD_Z + CARD.t;
  const o = [S(k.slabOf({ x, y, w: CARD.w, d: CARD.d, r: 1.5 }, CARD_Z, CARD.t, P, 3), { tone: "hi", crease: "none" })];
  if (copy === "b") o.push(`<g data-part="card-red" style="opacity:0">${S(k.slabOf({ x, y, w: CARD.w, d: CARD.d, r: 1.5 }, CARD_Z, CARD.t, P, 3), { tone: "hi", crease: "none", className: "ct-r" })}</g>`);
  o.push(S(k.slabOf({ x: x + 5, y: y + 4, w: CARD.w - 10, d: 8, r: 1 }, z, 1.4, P, 2), { tone: "hi", crease: "none", lit: true }));
  const bar = (x0, x1, yy) => poly([[x0, yy - 2, z], [x1, yy - 2, z], [x1, yy + 2, z], [x0, yy + 2, z]], "ct-ink");
  o.push(bar(x + 6, x + CARD.w - 6, y + 19), bar(x + 6, x + CARD.w - 14, y + 26), bar(x + 6, x + CARD.w - 22, y + 33));
  if (copy === "b") {
    const zm = z + 0.2, cx = x + CARD.w / 2, cy = y + CARD.d / 2 + 2;
    // a check: two thick strokes as one polygon
    const ck = [[-17, -3], [-6, 7], [15, -15], [17, -6], [-6, 17], [-17, 5]].map(([u, v]) => [cx + u, cy + v - 2, zm]);
    // an X: two crossed bars as one polygon (12 corners)
    const t = 4.6, L = 15;
    const xs = [[t, 0], [L, L - t], [L - t, L], [0, t], [-(L - t), L], [-L, L - t], [-t, 0], [-L, -(L - t)], [-(L - t), -L], [0, -t], [L - t, -L], [L, -(L - t)]].map(([u, v]) => [cx + u, cy + v, zm]);
    o.push(poly(ck, "ct-ok", ' data-part="mark-ok" style="opacity:0"'), poly(xs, "ct-bad", ' data-part="mark-bad" style="opacity:0"'));
  }
  return o.join("");
}

function slot() {
  const o = [];
  o.push(slab({ x: SLOT.x - 4, y: SLOT.y - 4, w: SLOT.w + 8, d: SLOT.d + 8, r: 5 }, Z0, 5));
  o.push(slab(SLOT, Z0 + 5, SLOT_H - 5, { crease: "none" }));
  o.push(slab({ x: SLOT.x + 8, y: SLOT.y + 8, w: SLOT.w - 16, d: SLOT.d - 16, r: 3 }, Z0 + SLOT_H, 5));
  // the mouth on the out face (+x): a dark slit the card leaves through
  const X = SLOT.x + SLOT.w, y0 = CARD_Y - 5, y1 = CARD_Y + CARD.d + 5, z0 = CARD_Z - 2, z1 = CARD_Z + CARD.t + 3;
  o.push(poly([[X, y0, z0], [X, y1, z0], [X, y1, z1], [X, y0, z1]], "ct-ink"));
  // a reading window on the front face (+y): yellow while the reader searches
  const Y = SLOT.y + SLOT.d, x0 = SLOT.x + 14, x1 = SLOT.x + SLOT.w - 14, wz0 = Z0 + 24, wz1 = Z0 + 36;
  o.push(poly([[x0, Y, wz0], [x1, Y, wz0], [x1, Y, wz1], [x0, Y, wz1]], "ct-plate"));
  o.push(poly([[x0, Y, wz0], [x1, Y, wz0], [x1, Y, wz1], [x0, Y, wz1]], "ct-win", ' data-part="window" style="opacity:0"'));
  return o.join("");
}

function landing() {
  return [slab(LAND, Z0, 8), slab({ x: LAND.x + LAND.w - 8, y: LAND.y, w: 8, d: LAND.d }, Z0 + 8, 6)].join("");
}

// the fork post: block, back cheek, [lever], front cheek with the pin cap
function postBack() {
  return [slab({ x: ARM_X - 14, y: ARM_Y - 10, w: 28, d: 20, r: 3 }, Z0, 10), slab({ x: ARM_X - 12, y: ARM_Y - 6, w: 5, d: 12, r: 1 }, Z0 + 10, PIVOT[2] + 7 - Z0 - 10)].join("");
}
function postFront() {
  const o = [slab({ x: ARM_X + 7, y: ARM_Y - 6, w: 5, d: 12, r: 1 }, Z0 + 10, PIVOT[2] + 7 - Z0 - 10)];
  o.push(S(G.lathe([[0, 0], [0, 4], [3, 4], [3, 0]], G.frameAlong([ARM_X + 12, ARM_Y, PIVOT[2]], [1, 0, 0]), P, { steps: 28 }), { tone: "hi", crease: "none" }));
  return o.join("");
}
function leverSvg(th) {
  const L = lever(th);
  return [OB(L.tail.c, L.tail.ax), OB(L.arm.c, L.arm.ax), OB(L.head.c, L.head.ax), OB(L.knob.c, L.knob.ax)].join("");
}

function lamp() {
  const o = [];
  o.push(S(k.cylinder(LAMP.x, LAMP.y, 15, Z0, 5, P, 40), { tone: "hi", crease: "none" }));
  o.push(S(k.cylinder(LAMP.x, LAMP.y, 6, Z0 + 5, LAMP_Z - Z0 - 5, P, 28), { tone: "hi", crease: "none" }));
  o.push(S(k.cylinder(LAMP.x, LAMP.y, 16, LAMP_Z, 5, P, 40), { tone: "hi", crease: "none" }));
  const F = G.frameAlong([LAMP.x, LAMP.y, LAMP_Z + 5], [0, 0, 1]);
  const mer = [[0, 0], [0, 14]];
  for (let i = 1; i < 8; i++) { const b = (i / 8) * Math.PI / 2; mer.push([15 * Math.sin(b), 14 * Math.cos(b), 1]); }
  mer.push([15, 0]);
  const dome = (cls) => S(G.lathe(mer, F, P, { steps: 48 }), { tone: "hi", crease: "none", className: cls });
  o.push(dome(), `<g data-part="lamp-ok" style="opacity:0">${dome("ct-g")}</g>`, `<g data-part="lamp-bad" style="opacity:0">${dome("ct-r")}</g>`);
  return o.join("");
}

// the landed copy is clipped to the out side of the reader's mouth (x beyond the box), so it seems to come out of it
const XOUT = SLOT.x + SLOT.w;
const clip = `<clipPath id="ct-out"><path d="${[[XOUT, -900, CARD_Z + 1.5], [XOUT, 900, CARD_Z + 1.5], [900, 900, CARD_Z + 1.5], [900, -900, CARD_Z + 1.5]].map((p, i) => `${i ? "L" : "M"}${r1(at(p)[0])} ${r1(at(p)[1])}`).join("")}Z"/></clipPath>`;

const body = [
  `<defs>${clip}</defs>`,
  base(),
  cabinet(),
  ...DRAWERS.map(drawer),
  tray(),
  `<g data-part="card-a">${cardSvg("a")}</g>`,
  slot(),
  postBack(),
  `<g data-part="lever">${leverSvg(ARM_UP)}</g>`,
  postFront(),
  landing(),
  `<g clip-path="url(#ct-out)"><g data-part="card-b" style="opacity:0">${cardSvg("b")}</g></g>`,
  lamp(),
].join("");

const svg = k.figureSvg({
  width: WIDTH, height: HEIGHT,
  label: "A citation checker: a card with a citation waits in a tray, passes through a reader box and comes out on a landing pad. Behind it a cabinet of nine drawers holds the volumes of real cases. A lamp on a post and a stamp lever mark the card found or not found.",
  body: [body],
});

const tint = (cls, c) => {
  const mix = (p, w) => `color-mix(in srgb, ${c} ${p}%, ${w})`;
  const tones = [mix(62, "#000"), mix(80, "#000"), c, c];
  const sel = `.iso .iso-solid.${cls}`;
  return `${sel}>.iso-fill,${sel}>.iso-top{fill:${c};stroke:${c}}\n` + tones.map((t, i) => `${sel}>.iso-shade[data-shade="${i}"]{fill:${t};stroke:${t}}`).join("\n") + "\n";
};
const css = k.ISO_CSS + tint("ct-g", "var(--anatomy-green)") + tint("ct-r", "var(--anatomy-red)") + `
.iso .iso-solid.ct-y>.iso-fill,.iso .iso-solid.ct-y>.iso-top{fill:var(--anatomy-lit-top);stroke:var(--anatomy-lit-top)}
.iso .iso-solid.ct-y>.iso-shade{fill:var(--anatomy-lit-shade);stroke:var(--anatomy-lit-shade)}
.iso .iso-solid.ct-y>.iso-shade[data-shade="2"],.iso .iso-solid.ct-y>.iso-shade[data-shade="3"]{fill:var(--anatomy-lit-top);stroke:var(--anatomy-lit-top)}
.ct-ink{fill:var(--anatomy-hi);stroke:none}
.ct-plate{fill:var(--anatomy-shade-3);stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}
.ct-win{fill:var(--anatomy-lit-top);stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}
.ct-ok{fill:var(--anatomy-green);stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}
.ct-bad{fill:var(--anatomy-red);stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}
`;

const DR = DRAWERS.map((d) => ({ o: d.order, x: d.x, z: d.z, m: d.match ? 1 : 0 }));
const pose = (kitScript() + `
const P = ${JSON.stringify(P)};
${obox.toString()}
const PIVOT = ${JSON.stringify(PIVOT)}, REACH = ${REACH}, HEAD = ${JSON.stringify(HEAD)}, ARM_UP = ${ARM_UP};
${lever.toString()}
const DR = ${JSON.stringify(DR)}, CELL = ${JSON.stringify(CELL)}, CAB_FRONT = ${CAB_FRONT}, POP = ${POP}, PULL = ${PULL};
const X_TRAY = ${X_TRAY}, X_SLOT = ${X_SLOT}, X_LAND = ${X_LAND};
const q = {};
const part = (svg, n) => (q[n] = q[n] && svg.contains(q[n]) ? q[n] : svg.querySelector('[data-part="' + n + '"]'));
const sm = (u) => { u = Math.min(1, Math.max(0, u)); return u * u * (3 - 2 * u); };
const op = (el, v) => { el.style.opacity = v <= 0.001 ? "0" : v >= 0.999 ? "1" : v.toFixed(3); };
const OB = (c, axes) => solidSvg(obox(c, axes, P, iso, cameraOf), { tone: "hi" });
const last = new WeakMap();
const setHtml = (el, key, html) => { if (last.get(el) !== key) { last.set(el, key); el.innerHTML = html(); } };
window.__ANP[${JSON.stringify(NAME)}] = {
  init: { feed: 0, search: 0, found: 0, ok: 0, bad: 0 },
  apply(svg, s, t) {
    // feed: tray -> inside the reader (0.5) -> out on the landing pad (1)
    const fa = sm(s.feed / 0.5), fb = sm((s.feed - 0.5) / 0.5);
    part(svg, "card-a").setAttribute("transform", translateAlong(P, [(X_SLOT - X_TRAY) * fa, 0, 0]));
    part(svg, "card-b").setAttribute("transform", translateAlong(P, [X_SLOT - X_TRAY + (X_LAND - X_SLOT) * fb, 0, 0]));
    op(part(svg, "card-a"), s.feed < 0.5 ? 1 : 0);
    op(part(svg, "card-b"), s.feed > 0.5 ? 1 : 0);
    // search: a yellow marker steps through the drawers in reading order; each pops out as it passes
    const p = s.search * 9.4 - 0.2;
    op(part(svg, "window"), sm(s.search / 0.04) * (1 - sm((s.search - 0.96) / 0.04)));
    for (const d of DR) {
      const w = sm((p - d.o) / 0.18) * (1 - sm((p - d.o - 1) / 0.18));
      const out = POP * Math.sin(Math.PI * Math.min(1, Math.max(0, p - d.o))) * (w > 0 ? 1 : 0) + (d.m ? (PULL - 0) * sm(s.found / 0.7) : 0);
      const lit = d.m ? Math.max(w, sm(s.found / 0.3)) : w;
      op(part(svg, "lab-" + d.o), lit);
      const o = Math.round(out * 10) / 10;
      part(svg, "mv-" + d.o).setAttribute("transform", o ? translateAlong(P, [0, o, 0]) : "");
      setHtml(part(svg, "body-" + d.o), o, () => o > 0.05 ? solidSvg(slabOf({ x: d.x + 1.5, y: CAB_FRONT, w: CELL.w - 3, d: o, r: 0.5 }, d.z + 1.5, CELL.h - 3, P, 2), { tone: "hi", crease: "none" }) : "");
    }
    op(part(svg, "mcard"), sm((s.found - 0.45) / 0.3));
    // ok / bad: the lamp lights; the lever comes down onto the card and lifts again, leaving its mark
    const bump = (v) => Math.sin(Math.PI * Math.min(1, Math.max(0, (v - 0.15) / 0.7)));
    const down = Math.max(bump(s.ok), bump(s.bad));
    const th = Math.round(ARM_UP * (1 - sm(down / 0.6)) * 10) / 10;
    setHtml(part(svg, "lever"), th, () => { const L = lever(th); return [OB(L.tail.c, L.tail.ax), OB(L.arm.c, L.arm.ax), OB(L.head.c, L.head.ax), OB(L.knob.c, L.knob.ax)].join(""); });
    op(part(svg, "lamp-ok"), sm(s.ok / 0.25) * (1 - sm(s.bad / 0.25)));
    op(part(svg, "lamp-bad"), sm(s.bad / 0.25));
    op(part(svg, "mark-ok"), sm((s.ok - 0.5) / 0.05) * (1 - sm((s.bad - 0.5) / 0.05)));
    op(part(svg, "mark-bad"), sm((s.bad - 0.5) / 0.05));
    op(part(svg, "card-red"), sm((s.bad - 0.5) / 0.3));
  },
};
`).replaceAll("<script", "<\\u0073cript").replaceAll("</script", "<\\/script");

writeFileSync(join(HERE, `${NAME}.svg`), svg);
writeFileSync(join(HERE, `${NAME}.css`), css);
writeFileSync(join(HERE, `${NAME}.pose.js`), pose);
const M = cellOf(MATCH.row, MATCH.col);
const anchors = {
  card: [X_TRAY + CARD.w / 2, CARD_Y + CARD.d / 2, CARD_Z + CARD.t],
  slot: [SLOT.x + SLOT.w, CARD_Y + CARD.d / 2, CARD_Z + CARD.t],
  drawers: [CAB.x + CAB.w / 2, CAB_FRONT, (Z0 + PLINTH_H + CAB_Z1) / 2],
  match: [M.x + CELL.w / 2, CAB_FRONT + FACE_T, M.z + CELL.h / 2],
  lamp: [LAMP.x, LAMP.y, LAMP_Z + 15],
  stamp: [X_LAND + CARD.w / 2, CARD_Y + CARD.d / 2, CARD_Z + CARD.t],
};
writeFileSync(join(HERE, `${NAME}.json`), JSON.stringify({ width: WIDTH, height: HEIGHT,
  params: { feed: "0..1 card slides tray -> inside the reader (0.5) -> out on the landing spot (1)", search: "0..1 a yellow marker steps through the 9 drawers in reading order; each pops out as it passes",
    found: "0..1 the match drawer (middle row, right) pulls out and shows a yellow case card", ok: "0..1 lamp lights green; the stamp comes down and leaves a green check",
    bad: "0..1 lamp lights red; the stamp comes down and leaves a red X; the card turns red" },
  anchors: Object.fromEntries(Object.entries(anchors).map(([n, p]) => [n, at(p).map(r1)])) }, null, 1));
console.log("wrote", NAME, svg.length, "bytes", WIDTH, "x", HEIGHT, "scale", P.scale.toFixed(3));

if (process.argv.includes("--preview")) {
  const t = Number(process.argv[process.argv.indexOf("--preview") + 1]) || 0;
  const st = { feed: 0, search: 0, found: 0, ok: 0, bad: 0 };
  const args = process.argv.find((a) => a.startsWith("--state="));
  if (args) Object.assign(st, JSON.parse(args.slice(8)));
  // the video's paper look (System/scripts/hfkit.py, .an.iso)
  const vars = "--anatomy-paper:#FFFFFF;--anatomy-face:#FFFFFF;--anatomy-top:#FFFFFF;--anatomy-shade-0:#C4BAA6;--anatomy-shade-1:#D4CBB9;--anatomy-shade-2:#E3DCCD;--anatomy-shade-3:#F1ECE2;--anatomy-hi:#121212;--anatomy-mid:#3D3932;--anatomy-lo:#5A554B;--anatomy-faint:#B3AA98;--anatomy-lit:#121212;--anatomy-lit-top:#FFD23F;--anatomy-lit-shade:#F0B90F;--anatomy-halo:#6F6552;--anatomy-halo-opacity:.30;--anatomy-dot:#121212;--anatomy-weight:3.2px;--anatomy-red:#D7392B;--anatomy-green:#13965A;--anatomy-blue:#2C5BEA";
  const page = `<!doctype html><html><head><meta charset="utf-8"><style>${css}body{margin:0;background:#F4EFE4}.an{width:860px;margin:20px auto;${vars}}</style></head><body><div class="an iso" data-theme="dark" id="f">${svg}</div><script>window.__ANP={};${pose};window.__ANP["${NAME}"].apply(document.querySelector("svg"),${JSON.stringify(st)},${t});</script></body></html>`;
  writeFileSync(join(HERE, "preview.html"), page);
  console.log("preview.html");
}
