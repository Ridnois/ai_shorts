// Effort meter: the effort knob of a model as a machine. A control box carries a rotary knob with five detents (LOW at the
// left, MAX at the right); a yellow arc on the box face lights from LOW up to the pointer. A feed pipe runs to a glass-less
// cage where thinking tokens (yellow tiles) stack up, one tile per step: the tokens the model spends before it answers. A
// printer at the right pushes out the answer card; its strip turns green (the right number) or red (no number: it stopped
// short). A lamp on a post says green or red.
// Schematic, not to scale: effort sets how many tokens may be spent, not how clever the model is.
// node build.mjs [--preview [t]] [--state='{"effort":1}']  ->  effort-meter.svg  .json  .css  .pose.js  (+ preview.html)
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../../../.claude/skills/anatomy/kit/iso-kit.mjs";
import * as G from "../../../.claude/skills/anatomy/kit/lathe.mjs";
import { kitScript } from "../../../.claude/skills/anatomy/scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const NAME = "effort-meter";
const WIDTH = 600;

// ---- world (x, y floor; z up). Parts run along +x (screen left to right); fronts face +y.
const BASE = { x: -214, y: -86, w: 430, d: 196, r: 8 }, BASE_H = 12;
const Z0 = BASE_H;
const CTRL = { x: -198, y: -40, w: 96, d: 76, r: 3 }, CTRL_H = 96;            // the control box
const CFRONT = CTRL.y + CTRL.d;
const KNOB = { cx: CTRL.x + CTRL.w / 2, cz: Z0 + 52, R: 22, deep: 9, span: 120 }; // pointer from -span (LOW) to +span (MAX), degrees from up
const CAGE = { x: -64, y: -56, w: 80, d: 66 }, CAGE_H = 206;                    // the token cage
const POST = 9;
const N = 14, TOK = { h: 9, gap: 4.4, z0: Z0 + 8 };                              // token tiles
const TOKP = { x: CAGE.x + POST + 2, y: CAGE.y + 6, w: CAGE.w - 2 * POST - 4, d: CAGE.d - 12, r: 2 };
const PRN = { x: 58, y: -56, w: 122, d: 96, r: 3 }, PRN_H = 74;                // the printer
const PFRONT = PRN.y + PRN.d;
const CARD = { x: PRN.x + 22, w: 78, d: 62, t: 3 }, CARD_Z = Z0 + 24, CARD_OUT = 58;
const LAMP = { x: 196, y: 80 }, LAMP_Z = Z0 + 46;

const EXTREMES = [...k.boxCorners(BASE, 0, BASE_H), ...k.boxCorners(CTRL, 0, Z0 + CTRL_H + 6), ...k.boxCorners(CAGE, 0, Z0 + CAGE_H + 8),
  ...k.boxCorners(PRN, 0, Z0 + PRN_H + 10), [LAMP.x, LAMP.y, LAMP_Z + 22], [CARD.x, PFRONT + CARD_OUT, CARD_Z]];
const VIEW = { azimuth: 55, elevation: 34 };
const pre = k.fitProjection(EXTREMES, 1000, 1000, { pad: 0, ...VIEW });
const sx = EXTREMES.map((p) => k.iso(p, pre)), bw = Math.max(...sx.map((p) => p[0])) - Math.min(...sx.map((p) => p[0])), bh = Math.max(...sx.map((p) => p[1])) - Math.min(...sx.map((p) => p[1]));
const HEIGHT = Math.round(WIDTH * bh / bw);
const P = k.fitProjection(EXTREMES, WIDTH, HEIGHT, { pad: 14, ...VIEW });

const at = (p) => k.iso(p, P);
const S = (paths, style) => k.solidSvg(paths, style);
const r1 = (v) => Math.round(v * 10) / 10;
const poly = (pts, cls, extra = "") => `<path class="${cls}"${extra} d="${pts.map((p, i) => `${i ? "L" : "M"}${r1(at(p)[0])} ${r1(at(p)[1])}`).join("")}Z"/>`;
const slab = (plan, z, h, style = {}) => S(k.slabOf({ r: 1.5, ...plan }, z, h, P, 4), { tone: "hi", ...style });

// an annulus sector on a face plane y = Y around (cx, cz), angles in degrees from up toward +x
function arcPts(cx, cz, Y, r0, r1_, a0, a1, n = 24) {
  const pts = [];
  for (let i = 0; i <= n; i++) { const a = ((a0 + ((a1 - a0) * i) / n) * Math.PI) / 180; pts.push([cx + r1_ * Math.sin(a), Y, cz + r1_ * Math.cos(a)]); }
  for (let i = n; i >= 0; i--) { const a = ((a0 + ((a1 - a0) * i) / n) * Math.PI) / 180; pts.push([cx + r0 * Math.sin(a), Y, cz + r0 * Math.cos(a)]); }
  return pts;
}
// the knob pointer on the knob's front face at angle a
function pointerPts(a, K, Y) {
  const r = (a * Math.PI) / 180, s = Math.sin(r), c = Math.cos(r);
  const pt = (along, across) => [K.cx + s * along + c * across, Y, K.cz + c * along - s * across];
  return [pt(-4, -3.4), pt(K.R - 5, -3.4), pt(K.R - 2, 0), pt(K.R - 5, 3.4), pt(-4, 3.4)];
}
const ARC = { r0: KNOB.R + 5, r1: KNOB.R + 12 };

// ---- parts, back to front
function base() {
  const o = [slab(BASE, 0, BASE_H, { crease: "none" })];
  for (const [x, y] of [[BASE.x + 10, BASE.y + 10], [BASE.x + BASE.w - 10, BASE.y + 10], [BASE.x + 10, BASE.y + BASE.d - 10], [BASE.x + BASE.w - 10, BASE.y + BASE.d - 10]])
    o.push(S(k.cylinder(x, y, 3.2, Z0, 1.6, P, 20), { tone: "hi", crease: "none" }));
  return o.join("");
}

function control() {
  const o = [];
  o.push(slab({ x: CTRL.x - 5, y: CTRL.y - 5, w: CTRL.w + 10, d: CTRL.d + 10, r: 4 }, Z0, 8));
  o.push(slab(CTRL, Z0 + 8, CTRL_H - 8, { crease: "none" }));
  o.push(slab({ x: CTRL.x - 3, y: CTRL.y - 3, w: CTRL.w + 6, d: CTRL.d + 6, r: 2 }, Z0 + CTRL_H, 6));
  // a label plate on the +x side with two rule bars
  const X = CTRL.x + CTRL.w, y0 = CTRL.y + 10, y1 = CFRONT - 10;
  o.push(poly([[X, y0, Z0 + 20], [X, y1, Z0 + 20], [X, y1, Z0 + 46], [X, y0, Z0 + 46]], "em-plate"));
  for (const [z, e] of [[Z0 + 29, 6], [Z0 + 37, 20]]) o.push(poly([[X, y0 + 5, z - 1.5], [X, y1 - e, z - 1.5], [X, y1 - e, z + 1.5], [X, y0 + 5, z + 1.5]], "em-ink"));
  // the dial ring on the front face: a plain track, five detent ticks
  const K = KNOB, Y = CFRONT;
  o.push(poly(arcPts(K.cx, K.cz, Y, ARC.r0, ARC.r1, -K.span, K.span, 40), "em-track"));
  for (let i = 0; i < 5; i++) {
    const a = -K.span + (i * 2 * K.span) / 4, big = i === 0 || i === 4;
    o.push(poly(arcPts(K.cx, K.cz, Y, ARC.r1 + 1.5, ARC.r1 + (big ? 9 : 6), a - 3.2, a + 3.2, 2), "em-ink"));
  }
  return o.join("");
}
function knob() {
  const K = KNOB, F = G.frameAlong([K.cx, CFRONT, K.cz], [0, 1, 0]);
  const m = [[0, 0], [0, K.R], [K.deep - 1.5, K.R], [K.deep, K.R - 1.5], [K.deep, 0]];
  const o = [S(G.lathe([[0, 0], [0, K.R + 3], [2, K.R + 3], [2, 0]], F, P, { steps: 56 }), { tone: "hi", crease: "none" })];
  o.push(S(G.lathe(m, F, P, { steps: 56 }), { tone: "hi", crease: "none" }));
  return o.join("");
}

function pipe() {
  // a square feed pipe from the control box's +x side into the cage's -x post, with two collars
  const y = -16, d = 18, z = Z0 + 58, h = 16;
  const o = [slab({ x: CTRL.x + CTRL.w, y, w: CAGE.x - (CTRL.x + CTRL.w), d, r: 2 }, z, h)];
  for (const x of [CTRL.x + CTRL.w + 4, CAGE.x - 14]) o.push(slab({ x, y: y - 3, w: 8, d: d + 4, r: 1.5 }, z - 3, h + 6));
  return o.join("");
}

function cageBack() {
  const o = [];
  o.push(slab({ x: CAGE.x - 6, y: CAGE.y - 6, w: CAGE.w + 12, d: CAGE.d + 12, r: 3 }, Z0, 7));
  // back wall and the two back posts
  o.push(slab({ x: CAGE.x, y: CAGE.y, w: CAGE.w, d: 6, r: 1 }, Z0 + 7, CAGE_H - 7, { crease: "none" }));
  for (const x of [CAGE.x, CAGE.x + CAGE.w - POST]) o.push(slab({ x, y: CAGE.y, w: POST, d: POST, r: 1 }, Z0 + 7, CAGE_H - 7));
  // scale marks on the back wall's front face, one per two tokens
  const Y = CAGE.y + 6;
  for (let i = 1; i <= N / 2; i++) {
    const z = TOK.z0 + i * 2 * (TOK.h + TOK.gap) - TOK.gap / 2;
    o.push(poly([[CAGE.x + POST + 2, Y, z - 1.4], [CAGE.x + POST + 10, Y, z - 1.4], [CAGE.x + POST + 10, Y, z + 1.4], [CAGE.x + POST + 2, Y, z + 1.4]], "em-ink"));
  }
  return o.join("");
}
const tokenSvg = (i, cls) => S(k.slabOf(TOKP, TOK.z0 + i * (TOK.h + TOK.gap), TOK.h, P, 3), { tone: "hi", crease: "none", className: cls });
function tokens() {
  const o = [];
  for (let i = 0; i < N; i++) o.push(`<g data-part="tok-${i}" style="opacity:0">${tokenSvg(i, "em-y")}</g>`);
  return o.join("");
}
function cageFront() {
  const o = [];
  const Yf = CAGE.y + CAGE.d - POST;
  for (const x of [CAGE.x, CAGE.x + CAGE.w - POST]) o.push(slab({ x, y: Yf, w: POST, d: POST, r: 1 }, Z0 + 7, CAGE_H - 7));
  // two cross bars hold the front posts; the cap closes the top
  for (const z of [Z0 + 7, Z0 + CAGE_H - 12]) o.push(slab({ x: CAGE.x, y: Yf + 1, w: CAGE.w, d: POST - 2, r: 1 }, z, 5));
  o.push(slab({ x: CAGE.x - 4, y: CAGE.y - 4, w: CAGE.w + 8, d: CAGE.d + 8, r: 2 }, Z0 + CAGE_H, 8));
  return o.join("");
}

function printer() {
  const o = [];
  o.push(slab({ x: PRN.x - 5, y: PRN.y - 5, w: PRN.w + 10, d: PRN.d + 10, r: 4 }, Z0, 8));
  o.push(slab(PRN, Z0 + 8, PRN_H - 8, { crease: "none" }));
  o.push(slab({ x: PRN.x - 3, y: PRN.y - 3, w: PRN.w + 6, d: PRN.d + 6, r: 2 }, Z0 + PRN_H, 6));
  o.push(slab({ x: PRN.x + 18, y: PRN.y + 16, w: PRN.w - 36, d: 30, r: 3 }, Z0 + PRN_H + 6, 4));
  // vents on the +x side
  const X = PRN.x + PRN.w;
  for (let i = 0; i < 5; i++) { const y0 = PRN.y + 16 + i * 14; o.push(poly([[X, y0, Z0 + 40], [X, y0 + 6, Z0 + 40], [X, y0 + 6, Z0 + 64], [X, y0, Z0 + 64]], "em-slot")); }
  // the card slot on the front face
  const Y = PFRONT;
  o.push(poly([[CARD.x - 4, Y, CARD_Z - 2], [CARD.x + CARD.w + 4, Y, CARD_Z - 2], [CARD.x + CARD.w + 4, Y, CARD_Z + CARD.t + 3], [CARD.x - 4, Y, CARD_Z + CARD.t + 3]], "em-slot"));
  // two screws on the front face
  for (const x of [PRN.x + 9, PRN.x + PRN.w - 9])
    o.push(S(G.lathe([[0, 0], [0, 3], [1.4, 3], [1.4, 0]], G.frameAlong([x, Y, Z0 + PRN_H - 10], [0, 1, 0]), P, { steps: 16 }), { tone: "hi", crease: "none" }));
  return o.join("");
}
// the answer card, drawn inside the printer (y from PFRONT - CARD.d to PFRONT) and slid out along +y
function cardSvg() {
  const x = CARD.x, y = PFRONT - CARD.d, z = CARD_Z + CARD.t;
  const o = [S(k.slabOf({ x, y, w: CARD.w, d: CARD.d, r: 1.5 }, CARD_Z, CARD.t, P, 3), { tone: "hi", crease: "none" })];
  const strip = (cls, part) => `<g data-part="${part}" style="opacity:0">${S(k.slabOf({ x: x + 6, y: y + CARD.d - 14, w: CARD.w - 12, d: 9, r: 1 }, z, 1.4, P, 2), { tone: "hi", crease: "none", className: cls })}</g>`;
  o.push(S(k.slabOf({ x: x + 6, y: y + CARD.d - 14, w: CARD.w - 12, d: 9, r: 1 }, z, 1.4, P, 2), { tone: "hi", crease: "none", className: "em-k" }));
  o.push(strip("em-g", "strip-ok"), strip("em-r", "strip-bad"));
  // the number: three heavy bars near the out edge
  const bar = (x0, x1, yy) => poly([[x0, yy - 2.4, z], [x1, yy - 2.4, z], [x1, yy + 2.4, z], [x0, yy + 2.4, z]], "em-ink");
  o.push(`<g data-part="digits">${bar(x + 8, x + 30, y + CARD.d - 26)}${bar(x + 36, x + 52, y + CARD.d - 26)}${bar(x + 58, x + 70, y + CARD.d - 26)}</g>`);
  return o.join("");
}

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
  o.push(dome(), `<g data-part="lamp-ok" style="opacity:0">${dome("em-g")}</g>`, `<g data-part="lamp-bad" style="opacity:0">${dome("em-r")}</g>`);
  return o.join("");
}

// the card shows only in front of the printer's front face: a screen half-plane along the face line at card height
const clipOut = (() => {
  const a = at([-400, PFRONT, CARD_Z]), b = at([400, PFRONT, CARD_Z]);
  const dx = b[0] - a[0], dy = b[1] - a[1], L = 4000 / Math.hypot(dx, dy);
  const A = [a[0] - dx * L, a[1] - dy * L], B = [a[0] + dx * L, a[1] + dy * L];
  const nx = dy, ny = -dx, M = 4000 / Math.hypot(nx, ny);
  const q = at([CARD.x, PFRONT + 40, CARD_Z]);
  const s = (nx * (q[0] - a[0]) + ny * (q[1] - a[1])) > 0 ? 1 : -1;
  const C = [B[0] + s * nx * M, B[1] + s * ny * M], D = [A[0] + s * nx * M, A[1] + s * ny * M];
  return `<clipPath id="em-out"><path d="M${r1(A[0])} ${r1(A[1])}L${r1(B[0])} ${r1(B[1])}L${r1(C[0])} ${r1(C[1])}L${r1(D[0])} ${r1(D[1])}Z"/></clipPath>`;
})();

const body = [
  `<defs>${clipOut}</defs>`,
  base(),
  control(),
  `<g data-part="arc"></g>`,
  knob(),
  `<g data-part="pointer"></g>`,
  cageBack(),
  pipe(),
  tokens(),
  cageFront(),
  printer(),
  `<g clip-path="url(#em-out)"><g data-part="card">${cardSvg()}</g></g>`,
  lamp(),
].join("");

const svg = k.figureSvg({
  width: WIDTH, height: HEIGHT,
  label: "An effort meter: a control box with a rotary knob running from low to max, a yellow arc lighting up to the pointer. A pipe feeds a tall cage where yellow token tiles stack up, one per step of thinking. A printer on the right pushes out an answer card whose strip turns green for a right answer or red for none, and a lamp on a post lights green or red.",
  body: [body],
});

const tint = (cls, c) => {
  const mix = (p, w) => `color-mix(in srgb, ${c} ${p}%, ${w})`;
  const tones = [mix(62, "#000"), mix(80, "#000"), c, c];
  const sel = `.iso .iso-solid.${cls}`;
  return `${sel}>.iso-fill,${sel}>.iso-top{fill:${c};stroke:${c}}\n` + tones.map((t, i) => `${sel}>.iso-shade[data-shade="${i}"]{fill:${t};stroke:${t}}`).join("\n") + "\n";
};
const flat = (cls, fill) => `.${cls}{fill:${fill};stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}\n`;
const css = k.ISO_CSS + tint("em-g", "var(--anatomy-green)") + tint("em-r", "var(--anatomy-red)") + tint("em-k", "var(--anatomy-mid)") + `
.iso .iso-solid.em-y>.iso-fill,.iso .iso-solid.em-y>.iso-top{fill:var(--anatomy-lit-top);stroke:var(--anatomy-lit-top)}
.iso .iso-solid.em-y>.iso-shade{fill:var(--anatomy-lit-shade);stroke:var(--anatomy-lit-shade)}
.iso .iso-solid.em-y>.iso-shade[data-shade="2"],.iso .iso-solid.em-y>.iso-shade[data-shade="3"]{fill:var(--anatomy-lit-top);stroke:var(--anatomy-lit-top)}
.em-ink{fill:var(--anatomy-hi);stroke:none}
.em-pointer{fill:var(--anatomy-hi);stroke:var(--anatomy-hi);stroke-width:1px;stroke-linejoin:round;vector-effect:non-scaling-stroke}
` + flat("em-plate", "var(--anatomy-shade-3)") + flat("em-slot", "var(--anatomy-mid)") + flat("em-track", "var(--anatomy-shade-2)")
  + flat("em-yel", "var(--anatomy-lit-top)");

const pose = (kitScript() + `
const P = ${JSON.stringify(P)};
${arcPts.toString()}
${pointerPts.toString()}
const KNOB = ${JSON.stringify(KNOB)}, ARC = ${JSON.stringify(ARC)}, CFRONT = ${CFRONT}, N = ${N}, CARD_OUT = ${CARD_OUT}, CARD = ${JSON.stringify(CARD)};
const q = {};
const part = (svg, n) => (q[n] = q[n] && svg.contains(q[n]) ? q[n] : svg.querySelector('[data-part="' + n + '"]'));
const sm = (u) => { u = Math.min(1, Math.max(0, u)); return u * u * (3 - 2 * u); };
const op = (el, v) => { el.style.opacity = v <= 0.001 ? "0" : v >= 0.999 ? "1" : v.toFixed(3); };
const r1 = (v) => (Math.round(v * 10) / 10);
const d = (pts) => pts.map((p, i) => (i ? "L" : "M") + iso(p, P).map(r1).join(" ")).join("") + "Z";
const last = new WeakMap();
const setHtml = (el, key, html) => { if (last.get(el) !== key) { last.set(el, key); el.innerHTML = html(); } };
window.__ANP[${JSON.stringify(NAME)}] = {
  init: { effort: 0, think: 0, out: 0, ok: 0, bad: 0 },
  apply(svg, s, t) {
    // effort: the pointer turns from LOW (-span) to MAX (+span); the yellow arc lights from LOW up to the pointer
    const a = Math.round((-KNOB.span + 2 * KNOB.span * Math.min(1, Math.max(0, s.effort))) * 10) / 10;
    setHtml(part(svg, "pointer"), a, () => '<path class="em-pointer" d="' + d(pointerPts(a, KNOB, CFRONT + KNOB.deep + 0.5)) + '"/>');
    setHtml(part(svg, "arc"), a, () => a <= -KNOB.span + 0.5 ? "" : '<path class="em-yel" d="' + d(arcPts(KNOB.cx, KNOB.cz, CFRONT, ARC.r0, ARC.r1, -KNOB.span, a, 32)) + '"/>');
    // think: token tiles stack up from the bottom, each fading in over its own step
    for (let i = 0; i < N; i++) op(part(svg, "tok-" + i), Math.min(1, Math.max(0, s.think * N - i)));
    // out: the answer card slides out of the slot toward the viewer
    part(svg, "card").setAttribute("transform", translateAlong(P, [0, CARD_OUT * sm(s.out), 0]));
    op(part(svg, "strip-ok"), sm(s.ok / 0.4) * (1 - sm(s.bad / 0.4)));
    op(part(svg, "strip-bad"), sm(s.bad / 0.4));
    op(part(svg, "digits"), 1 - sm(s.bad / 0.4));
    op(part(svg, "lamp-ok"), sm(s.ok / 0.3) * (1 - sm(s.bad / 0.3)));
    op(part(svg, "lamp-bad"), sm(s.bad / 0.3));
  },
};
`).replaceAll("<script", "<\\u0073cript").replaceAll("</script", "<\\/script");

writeFileSync(join(HERE, `${NAME}.svg`), svg);
writeFileSync(join(HERE, `${NAME}.css`), css);
writeFileSync(join(HERE, `${NAME}.pose.js`), pose);
const tz = (i) => TOK.z0 + i * (TOK.h + TOK.gap) + TOK.h;
const anchors = {
  knob: [KNOB.cx, CFRONT + KNOB.deep, KNOB.cz],
  low: [KNOB.cx + (ARC.r1 + 10) * Math.sin(-KNOB.span * Math.PI / 180), CFRONT, KNOB.cz + (ARC.r1 + 10) * Math.cos(-KNOB.span * Math.PI / 180)],
  max: [KNOB.cx + (ARC.r1 + 10) * Math.sin(KNOB.span * Math.PI / 180), CFRONT, KNOB.cz + (ARC.r1 + 10) * Math.cos(KNOB.span * Math.PI / 180)],
  cage: [CAGE.x + CAGE.w / 2, CAGE.y + CAGE.d, Z0 + CAGE_H / 2],
  tok2: [CAGE.x + CAGE.w, CAGE.y + CAGE.d / 2, tz(1)],
  tok14: [CAGE.x + CAGE.w, CAGE.y + CAGE.d / 2, tz(N - 1)],
  card: [CARD.x + CARD.w / 2, PFRONT + CARD_OUT - CARD.d / 2 + 10, CARD_Z + CARD.t],
  printer: [PRN.x + PRN.w / 2, PFRONT, Z0 + PRN_H / 2],
  lamp: [LAMP.x, LAMP.y, LAMP_Z + 14],
};
writeFileSync(join(HERE, `${NAME}.json`), JSON.stringify({ width: WIDTH, height: HEIGHT,
  params: {
    effort: "0..1 the knob pointer turns from LOW (0) to MAX (1); five detents at 0, .25, .5, .75, 1; the yellow arc lights up to the pointer",
    think: "0..1 token tiles stack up in the cage, 14 at 1 (one tile is 1/14); 1/7 = 2 tiles",
    out: "0..1 the answer card slides out of the printer slot",
    ok: "0..1 the card strip and the lamp turn green",
    bad: "0..1 the card strip and the lamp turn red and the card's number bars vanish (no answer)",
  },
  anchors: Object.fromEntries(Object.entries(anchors).map(([n, p]) => [n, at(p).map(r1)])) }, null, 1));
console.log("wrote", NAME, svg.length, "bytes", WIDTH, "x", HEIGHT, "scale", P.scale.toFixed(3));

if (process.argv.includes("--preview")) {
  const t = Number(process.argv[process.argv.indexOf("--preview") + 1]) || 0;
  const st = { effort: 0, think: 0, out: 0, ok: 0, bad: 0 };
  const args = process.argv.find((a) => a.startsWith("--state="));
  if (args) Object.assign(st, JSON.parse(args.slice(8)));
  const vars = "--anatomy-paper:#FFFFFF;--anatomy-face:#FFFFFF;--anatomy-top:#FFFFFF;--anatomy-shade-0:#C4BAA6;--anatomy-shade-1:#D4CBB9;--anatomy-shade-2:#E3DCCD;--anatomy-shade-3:#F1ECE2;--anatomy-hi:#121212;--anatomy-mid:#3D3932;--anatomy-lo:#5A554B;--anatomy-faint:#B3AA98;--anatomy-lit:#121212;--anatomy-lit-top:#FFD23F;--anatomy-lit-shade:#F0B90F;--anatomy-halo:#6F6552;--anatomy-halo-opacity:.30;--anatomy-dot:#121212;--anatomy-weight:3.2px;--anatomy-red:#D7392B;--anatomy-green:#13965A;--anatomy-blue:#2C5BEA";
  const page = `<!doctype html><html><head><meta charset="utf-8"><style>${css}body{margin:0;background:#F4EFE4}.an{width:860px;margin:20px auto;${vars}}</style></head><body><div class="an iso" data-theme="dark" id="f">${svg}</div><script>window.__ANP={};${pose};window.__ANP["${NAME}"].apply(document.querySelector("svg"),${JSON.stringify(st)},${t});</script></body></html>`;
  writeFileSync(join(HERE, "preview.html"), page);
  console.log("preview.html");
}
