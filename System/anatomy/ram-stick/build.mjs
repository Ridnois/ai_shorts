// RAM stick: a laptop memory module lying flat on a bench plate, eight chips in a row, and the model's weights as blocks
// stacked on the chips under a height bar (the laptop's 10 GB). At 16 bits a weight block is tall: three fill a chip to the
// bar and the rest spill onto a red overflow pile. At about 4.5 bits every block is under a third as tall, the pile flies
// back onto the chips and every stack fits with room left (schematic, not to scale).
//   8.2 B params x 16 bit = 16.4 GB > 10 GB;  ~4.5 bits per weight (Q4_K_M with its scales) = 5.2 GB < 10 GB.
// node build.mjs [--preview [t]] [--state='{"load":1}']  ->  ram-stick.svg  .json  .css  .pose.js  (+ preview.html with --preview)
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../../../.claude/skills/anatomy/kit/iso-kit.mjs";
import * as G from "../../../.claude/skills/anatomy/kit/lathe.mjs";
import { kitScript } from "../../../.claude/skills/anatomy/scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const NAME = "ram-stick";
const WIDTH = 600;

// ---- the model behind the picture: 40 blocks of 0.41 GB at 16 bits = 16.4 GB; 8 chips x 3 blocks = 24 x 0.41 = 9.8 GB ~ 10 GB
const N_CHIP = 8, PER = 5, FIT = 3;                                // 5 blocks per chip, 3 fit at 16 bits
const R4 = 5.2 / 16.4;                                             // block height at ~4.5 bits over its height at 16 bits (0.317)

// ---- world (x, y floor; z up). The stick runs along +x; its gold edge faces the viewer (+y).
const BASE = { x: -246, y: -14, w: 560, d: 170, r: 8 }, BASE_H = 10, Z0 = BASE_H;
const PCB = { x: -170, y: 0, w: 340, d: 130 }, PCB_T = 5, ZP = Z0 + PCB_T;    // PCB top
const NOTCH = { x: 28, w: 8, d: 11 };                              // the key notch in the contact edge (off centre)
const CHIP = { w: 32, d: 52, h: 6 }, CHIP_Y = 24, PITCH = 40;
const chipX = (c) => PCB.x + 14 + c * PITCH;                        // left edge of chip c
const ZC = ZP + CHIP.h;                                            // chip top
const BLK = { w: 26, d: 44, h: 22 };                               // a weight block at 16 bits
const CAP = ZC + FIT * BLK.h;                                      // the height bar: what the laptop holds
const BAR = { y: 15, d: 8, h: 7 }, POST = { w: 10, d: 10 }, POST_X = [PCB.x - 18, PCB.x + PCB.w + 8];
// the overflow tray beyond the +x end, with a back lip and an end lip
const TRAY = { x: 196, y: 26, w: 112, d: 114 }, TRAY_H = 3, ZT = Z0 + TRAY_H;
// the status sign at the -x end: a stand and a plate facing +x
const SIGN = { x: -228, y: 70, w: 30, d: 82 }, SIGN_H = 8, PLATE = { x: -216, y: 78, w: 6, d: 66, h: 58 };

// pile slots (x, y of the block's corner, layer), filled in spill order; constant offsets make it look tipped out, not stacked
const PILE = [];
{
  const cx = (i) => TRAY.x + 8 + i * 33, cy = (j) => TRAY.y + 14 + j * 49;
  const off = [[0, 0], [2, -1], [-1, 2], [1, 1], [-2, 0], [0, 2]];
  let n = 0;
  for (const [layer, cols, rows, sx, sy] of [[0, 3, 2, 0, 0], [1, 3, 2, 3, 2], [2, 2, 2, 17, 3]])
    for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) { const o = off[n++ % off.length]; PILE.push([cx(i) + sx + o[0], cy(j) + sy + o[1], layer]); }
  // spill order: nearest the stick first, bottom layer first
}

const EXTREMES = [...k.boxCorners(BASE, 0, BASE_H), [POST_X[0], BAR.y, CAP + BAR.h + 4], [POST_X[1] + POST.w, BAR.y + BAR.d, CAP + BAR.h + 4],
  [PLATE.x, PLATE.y, ZC + PLATE.h + 6], [PLATE.x, PLATE.y + PLATE.d, ZC + PLATE.h + 6]];
const VIEW = { azimuth: 36, elevation: 40 };
const pre = k.fitProjection(EXTREMES, 1000, 1000, { pad: 0, ...VIEW });
const sx = EXTREMES.map((p) => k.iso(p, pre)), bw = Math.max(...sx.map((p) => p[0])) - Math.min(...sx.map((p) => p[0])), bh = Math.max(...sx.map((p) => p[1])) - Math.min(...sx.map((p) => p[1]));
const HEIGHT = Math.round(WIDTH * bh / bw);
const P = k.fitProjection(EXTREMES, WIDTH, HEIGHT, { pad: 14, ...VIEW });

const at = (p) => k.iso(p, P);
const S = (paths, style) => k.solidSvg(paths, style);
const r1 = (v) => Math.round(v * 10) / 10;
const poly = (pts, cls, extra = "") => `<path class="${cls}"${extra} d="${pts.map((p, i) => `${i ? "L" : "M"}${r1(at(p)[0])} ${r1(at(p)[1])}`).join("")}Z"/>`;
const slab = (plan, z, h, style = {}) => S(k.slabOf({ r: 1.5, ...plan }, z, h, P, 4), { tone: "hi", ...style });

// ---- the blocks: one pure map from the state to every block's box and colour, run by the build and by the pose
function blocksOf(s, C) {
  const cl = (u) => Math.min(1, Math.max(0, u)), sm = (u) => { u = cl(u); return u * u * (3 - 2 * u); };
  const N = C.N_CHIP * C.PER, D = 2.2, DF = 2;
  const b = sm(s.bits), h = C.BLK.h * (1 - (1 - C.R4) * b);
  const out = [];
  for (let c = 0; c < C.N_CHIP; c++) for (let l = 0; l < C.PER; l++) {
    const g = c * C.PER + l;
    const u = cl((s.load * (N - 1 + D) - g) / D);
    if (u <= 0) continue;
    const bx = C.chipX[c] + (C.CHIP.w - C.BLK.w) / 2, by = C.CHIP_Y + (C.CHIP.d - C.BLK.d) / 2;
    let tx = bx, ty = by, tz = C.ZC + l * h, red = 0;
    if (l >= C.FIT) {
      // a block that does not fit at 16 bits: on the pile until the bits drop, then it flies back to its chip
      const k = (l - C.FIT) * C.N_CHIP + c, [px, py, layer] = C.PILE[k];
      const f = sm((s.bits * (C.N_CHIP * (C.PER - C.FIT) - 1 + DF) - k) / DF);
      const pz = C.ZT + layer * h;
      tx = px + (bx - px) * f; ty = py + (by - py) * f; tz = pz + (tz - pz) * f + (30 + 6 * (c % 3)) * Math.sin(Math.PI * f);
      red = 1 - f;
    }
    // the drop: from above its chip, over the bar, falling faster as it goes
    const z0 = C.CAP + 34 + l * 4, e = u * u;
    const x = bx + (tx - bx) * u, y = by + (ty - by) * u, z = z0 + (tz - z0) * e + (l >= C.FIT ? 20 * Math.sin(Math.PI * u) * (1 - b) : 0);
    out.push({ x: Math.round(x * 10) / 10, y: Math.round(y * 10) / 10, z: Math.round(z * 10) / 10, h: Math.round(h * 100) / 100,
      o: Math.round(sm(u / 0.35) * 1000) / 1000, r: Math.round(red * 1000) / 1000, yl: Math.round(b * 1000) / 1000 });
  }
  return out;
}
function blocksSvg(list, C, P, slabOf, solidSvg, depthOf) {
  return list.map((q) => ({ q, d: depthOf([q.x + C.BLK.w / 2, q.y + C.BLK.d / 2, q.z + q.h / 2], P) }))
    .sort((a, b) => a.d - b.d)
    .map(({ q }) => `<g style="--r:${q.r};--y:${q.yl}${q.o < 1 ? ";opacity:" + q.o : ""}">${solidSvg(slabOf({ x: q.x, y: q.y, w: C.BLK.w, d: C.BLK.d, r: 1.5 }, q.z, q.h, P, 4), { tone: "hi", crease: "none", className: "rs-b" })}</g>`)
    .join("");
}

// ---- parts, back to front
function base() {
  const o = [slab(BASE, 0, BASE_H, { crease: "none" })];
  for (const [x, y] of [[BASE.x + 10, BASE.y + BASE.d - 10], [BASE.x + BASE.w - 10, BASE.y + BASE.d - 10], [BASE.x + BASE.w - 10, BASE.y + 10], [BASE.x + 10, BASE.y + 10]])
    o.push(S(k.cylinder(x, y, 3.6, Z0, 1.6, P, 20), { tone: "hi", crease: "none" }));
  // a label plate on the bench, front left, with two rule bars
  const lp = { x: -150, y: 138, w: 60, d: 12, r: 1 };
  o.push(slab(lp, Z0, 1.6, { crease: "none" }));
  o.push(poly([[lp.x + 5, lp.y + 4, Z0 + 1.7], [lp.x + 40, lp.y + 4, Z0 + 1.7], [lp.x + 40, lp.y + 7, Z0 + 1.7], [lp.x + 5, lp.y + 7, Z0 + 1.7]], "rs-ink"));
  o.push(poly([[lp.x + 44, lp.y + 4, Z0 + 1.7], [lp.x + 55, lp.y + 4, Z0 + 1.7], [lp.x + 55, lp.y + 7, Z0 + 1.7], [lp.x + 44, lp.y + 7, Z0 + 1.7]], "rs-ink"));
  return o.join("");
}

// the sign: a stand with a slot; the red X plate and the green check plate rise out of it
function signPlate(kind) {
  const X = PLATE.x + PLATE.w, z0 = Z0 + SIGN_H, cy = PLATE.y + PLATE.d / 2, cz = z0 + PLATE.h / 2;
  const o = [S(k.slabOf({ ...PLATE, r: 1.5 }, z0, PLATE.h, P, 4), { tone: "hi", crease: "none", className: kind === "ok" ? "rs-g" : "rs-r" })];
  const face = (pts) => pts.map(([u, v]) => [X + 0.2, cy + u, cz + v]);
  if (kind === "bad") {
    const t = 6, L = 19;
    o.push(poly(face([[t, 0], [L, L - t], [L - t, L], [0, t], [-(L - t), L], [-L, L - t], [-t, 0], [-L, -(L - t)], [-(L - t), -L], [0, -t], [L - t, -L], [L, -(L - t)]]), "rs-mark"));
  } else {
    o.push(poly(face([[-21, 2], [-8, -11], [20, 17], [12, 24], [-8, 5], [-14, 10]].map(([u, v]) => [u * 1.15, v * 1.15 - 4])), "rs-mark"));
  }
  return `<g data-part="sign-${kind}" style="opacity:0">${o.join("")}</g>`;
}
function sign() {
  const o = [slab({ ...SIGN, r: 3 }, Z0, SIGN_H)];
  // the slot the plates stand in, on the stand's top
  o.push(poly([[PLATE.x - 1, PLATE.y - 1, Z0 + SIGN_H + 0.1], [PLATE.x + PLATE.w + 1, PLATE.y - 1, Z0 + SIGN_H + 0.1], [PLATE.x + PLATE.w + 1, PLATE.y + PLATE.d + 1, Z0 + SIGN_H + 0.1], [PLATE.x - 1, PLATE.y + PLATE.d + 1, Z0 + SIGN_H + 0.1]], "rs-ink"));
  for (const y of [SIGN.y + 6, SIGN.y + SIGN.d - 6]) o.push(S(k.cylinder(SIGN.x + SIGN.w - 7, y, 2.4, Z0 + SIGN_H, 1.2, P, 16), { tone: "hi", crease: "none" }));
  o.push(signPlate("bad"), signPlate("ok"));
  return o.join("");
}

function post(x) {
  const o = [slab({ x: x - 3, y: BAR.y - 4, w: POST.w + 6, d: POST.d + 6, r: 2 }, Z0, 5)];
  o.push(slab({ x, y: BAR.y - 1, w: POST.w, d: POST.d }, Z0 + 5, CAP - Z0 - 5, { crease: "none" }));
  return o.join("");
}
function bar() {
  const o = [slab({ x: POST_X[0] - 2, y: BAR.y, w: POST_X[1] + POST.w + 2 - POST_X[0] + 2, d: BAR.d }, CAP, BAR.h, { crease: "none" })];
  for (const x of POST_X) o.push(S(k.cylinder(x + POST.w / 2, BAR.y + BAR.d / 2, 3, CAP + BAR.h, 2, P, 20), { tone: "hi", crease: "none" }));
  return o.join("");
}

// the module: a PCB with the key notch cut in its contact edge, gold-finger pads, passives, the SPD chip and eight chips
function pcb() {
  const { x, y, w, d } = PCB, n0 = NOTCH.x - NOTCH.w / 2, n1 = NOTCH.x + NOTCH.w / 2, Y = y + d;
  const ring = [[x + 3, y], [x + w - 3, y], [x + w, y + 3], [x + w, Y], [n1, Y], [n1, Y - NOTCH.d], [n0, Y - NOTCH.d], [n0, Y], [x, Y], [x, y + 3]];
  const o = [S(k.extrude(ring, Z0, PCB_T, P, { convex: false }), { tone: "hi", crease: "none" })];
  // gold fingers: a row of pads on the contact edge, broken by the notch
  for (let i = 0; i < 19; i++) {
    const px = x + 8 + i * 17.4;
    if (px + 11 > n0 - 3 && px < n1 + 3) continue;
    o.push(S(k.slabOf({ x: px, y: Y - 15, w: 11, d: 13, r: 1 }, ZP, 0.8, P, 2), { tone: "hi", crease: "none", flat: true, className: "rs-pad" }));
  }
  // passives between the chips and the fingers: a pair of small caps under each chip
  for (let c = 0; c < N_CHIP; c++) for (const dx of [5, 18])
    o.push(slab({ x: chipX(c) + dx, y: CHIP_Y + CHIP.d + 6, w: 9, d: 5, r: 0.6 }, ZP, 2.4, { crease: "none" }));
  // the SPD chip and a row of resistors behind the chips
  o.push(slab({ x: x + w - 34, y: 6, w: 18, d: 12, r: 1 }, ZP, 2.6, { crease: "none" }));
  for (let i = 0; i < 6; i++) o.push(slab({ x: x + 30 + i * 46, y: 8, w: 8, d: 5, r: 0.6 }, ZP, 2, { crease: "none" }));
  return o.join("");
}
function chip(c) {
  const x = chipX(c), o = [slab({ x, y: CHIP_Y, w: CHIP.w, d: CHIP.d, r: 1 }, ZP, CHIP.h, { crease: "none" })];
  // pin-1 dot at the front left corner of the package
  o.push(S(k.cylinder(x + 6, CHIP_Y + CHIP.d - 5, 2.2, ZC, 0.4, P, 14), { tone: "hi", crease: "none", flat: true, className: "rs-dot" }));
  return o.join("");
}

function tray() {
  const o = [slab({ ...TRAY, r: 3 }, Z0, TRAY_H)];
  o.push(slab({ x: TRAY.x, y: TRAY.y, w: TRAY.w, d: 6, r: 1 }, ZT, 6));
  o.push(slab({ x: TRAY.x + TRAY.w - 6, y: TRAY.y + 6, w: 6, d: TRAY.d - 6, r: 1 }, ZT, 6));
  return o.join("");
}

const C = { N_CHIP, PER, FIT, R4, BLK, CHIP, CHIP_Y, ZC, ZT, CAP, chipX: Array.from({ length: N_CHIP }, (_, c) => chipX(c)), PILE };
const INIT = { load: 0, bits: 0, bad: 0, ok: 0 };

const body = [
  base(),
  sign(),
  post(POST_X[0]),
  pcb(),
  ...Array.from({ length: N_CHIP }, (_, c) => chip(c)),
  post(POST_X[1]),
  bar(),
  tray(),
  `<g data-part="blocks">${blocksSvg(blocksOf(INIT, C), C, P, k.slabOf, k.solidSvg, k.depthOf)}</g>`,
].join("");

const svg = k.figureSvg({
  width: WIDTH, height: HEIGHT,
  label: "A laptop memory stick lies on a bench under a height bar, with eight chips in a row. Blocks standing for a model's weights stack on the chips; at 16 bits they reach the bar and the rest spill onto a red pile beside the stick; at 4 bits they shrink and all fit with room left. A sign at the end shows a red X or a green check.",
  body: [body],
});

const tint = (cls, c) => {
  const mix = (p, w) => `color-mix(in srgb, ${c} ${p}%, ${w})`;
  const tones = [mix(62, "#000"), mix(80, "#000"), c, c];
  const sel = `.iso .iso-solid.${cls}`;
  return `${sel}>.iso-fill,${sel}>.iso-top{fill:${c};stroke:${c}}\n` + tones.map((t, i) => `${sel}>.iso-shade[data-shade="${i}"]{fill:${t};stroke:${t}}`).join("\n") + "\n";
};
// weight blocks: paper at 16 bits, red while on the overflow pile (--r), lit yellow as the bits drop (--y); one continuous mix
const RED = (p) => `color-mix(in srgb, var(--anatomy-red) ${p}%, #000)`;
const blockTone = (paper, red, lit) => `color-mix(in srgb, ${lit} calc(var(--y, 0) * 100%), color-mix(in srgb, ${red} calc(var(--r, 0) * 100%), ${paper}))`;
const BT = [
  ["top", "var(--anatomy-top)", "var(--anatomy-red)", "var(--anatomy-lit-top)"],
  ['shade[data-shade="0"]', "var(--anatomy-shade-0)", RED(62), "var(--anatomy-lit-shade)"],
  ['shade[data-shade="1"]', "var(--anatomy-shade-1)", RED(80), "var(--anatomy-lit-shade)"],
  ['shade[data-shade="2"]', "var(--anatomy-shade-2)", "var(--anatomy-red)", "var(--anatomy-lit-top)"],
  ['shade[data-shade="3"]', "var(--anatomy-shade-3)", "var(--anatomy-red)", "var(--anatomy-lit-top)"],
];
const css = k.ISO_CSS + tint("rs-r", "var(--anatomy-red)") + tint("rs-g", "var(--anatomy-green)") +
  BT.map(([part, a, b, c]) => { const t = blockTone(a, b, c); return `.iso .iso-solid.rs-b>.iso-${part}{fill:${t};stroke:${t};stroke-width:.4}`; }).join("\n") + `
.iso .iso-solid.rs-b>.iso-fill{fill:${blockTone("var(--anatomy-top)", "var(--anatomy-red)", "var(--anatomy-lit-top)")}}
.iso .iso-solid.rs-pad>.iso-fill{fill:var(--anatomy-shade-1)}
.iso .iso-solid.rs-dot>.iso-fill{fill:var(--anatomy-hi)}
.rs-ink{fill:var(--anatomy-hi);stroke:none}
.rs-mark{fill:var(--anatomy-paper);stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}
`;

const pose = (kitScript() + `
const P = ${JSON.stringify(P)};
const C = ${JSON.stringify(C)};
${blocksOf.toString()}
${blocksSvg.toString()}
const q = {};
const part = (svg, n) => (q[n] = q[n] && svg.contains(q[n]) ? q[n] : svg.querySelector('[data-part="' + n + '"]'));
const sm = (u) => { u = Math.min(1, Math.max(0, u)); return u * u * (3 - 2 * u); };
const op = (el, v) => { el.style.opacity = v <= 0.001 ? "0" : v >= 0.999 ? "1" : v.toFixed(3); };
const last = new WeakMap();
const setHtml = (el, key, html) => { if (last.get(el) !== key) { last.set(el, key); el.innerHTML = html(); } };
const RISE = ${PLATE.h * 0.35};
window.__ANP[${JSON.stringify(NAME)}] = {
  init: ${JSON.stringify(INIT)},
  apply(svg, s, t) {
    // load: blocks drop chip by chip; bits: 16 -> ~4.5 bits per weight (blocks shrink, the pile flies back, paper -> yellow)
    const list = blocksOf(s, C);
    setHtml(part(svg, "blocks"), JSON.stringify(list), () => blocksSvg(list, C, P, slabOf, solidSvg, depthOf));
    // bad / ok: the sign plate rises out of its stand; ok wins over bad when both are up
    const vb = sm(s.bad / 0.6) * (1 - sm(s.ok / 0.4)), vo = sm(s.ok / 0.6);
    for (const [n, v] of [["sign-bad", vb], ["sign-ok", vo]]) {
      const el = part(svg, n);
      op(el, sm(v / 0.5));
      const dz = Math.round(-RISE * (1 - v) * 10) / 10;
      el.setAttribute("transform", dz ? translateAlong(P, [0, 0, dz]) : "");
    }
  },
};
`).replaceAll("<script", "<\\u0073cript").replaceAll("</script", "<\\/script");

writeFileSync(join(HERE, `${NAME}.svg`), svg);
writeFileSync(join(HERE, `${NAME}.css`), css);
writeFileSync(join(HERE, `${NAME}.pose.js`), pose);
const anchors = {
  stick: [PCB.x + PCB.w / 2, PCB.y + PCB.d / 2, ZP],
  chips: [0, CHIP_Y + CHIP.d / 2, ZC],
  chip0: [chipX(0) + CHIP.w / 2, CHIP_Y + CHIP.d / 2, ZC],
  chip7: [chipX(7) + CHIP.w / 2, CHIP_Y + CHIP.d / 2, ZC],
  overflow: [TRAY.x + TRAY.w / 2, TRAY.y + TRAY.d / 2, ZT + BLK.h],
  mark: [PLATE.x + PLATE.w, PLATE.y + PLATE.d / 2, Z0 + SIGN_H + PLATE.h / 2],
};
writeFileSync(join(HERE, `${NAME}.json`), JSON.stringify({ width: WIDTH, height: HEIGHT,
  params: { load: "0..1 the 40 weight blocks drop onto the chips, chip by chip (5 per chip); at 16 bits 3 fit under the bar and 2 spill onto the red overflow pile",
    bits: "0..1 0 = 16 bits per weight (16.4 GB: tall blocks, 24 on the chips, 16 on the pile); 1 = ~4.5 bits (5.2 GB: blocks 0.32 as tall, the pile flies back, all 40 fit to half the bar, lit yellow)",
    bad: "0..1 a red plate with an X rises at the -x end of the stick (does not fit)",
    ok: "0..1 a green plate with a check rises at the -x end (fits); hides the red plate" },
  anchors: Object.fromEntries(Object.entries(anchors).map(([n, p]) => [n, at(p).map(r1)])) }, null, 1));
console.log("wrote", NAME, svg.length, "bytes", WIDTH, "x", HEIGHT, "scale", P.scale.toFixed(3));

if (process.argv.includes("--preview")) {
  const t = Number(process.argv[process.argv.indexOf("--preview") + 1]) || 0;
  const st = { ...INIT };
  const args = process.argv.find((a) => a.startsWith("--state="));
  if (args) Object.assign(st, JSON.parse(args.slice(8)));
  // the video's paper look (System/scripts/hfkit.py, .an.iso)
  const vars = "--anatomy-paper:#FFFFFF;--anatomy-face:#FFFFFF;--anatomy-top:#FFFFFF;--anatomy-shade-0:#C4BAA6;--anatomy-shade-1:#D4CBB9;--anatomy-shade-2:#E3DCCD;--anatomy-shade-3:#F1ECE2;--anatomy-hi:#121212;--anatomy-mid:#3D3932;--anatomy-lo:#5A554B;--anatomy-faint:#B3AA98;--anatomy-lit:#121212;--anatomy-lit-top:#FFD23F;--anatomy-lit-shade:#F0B90F;--anatomy-halo:#6F6552;--anatomy-halo-opacity:.30;--anatomy-dot:#121212;--anatomy-weight:3.2px;--anatomy-red:#D7392B;--anatomy-green:#13965A;--anatomy-blue:#2C5BEA";
  const page = `<!doctype html><html><head><meta charset="utf-8"><style>${css}body{margin:0;background:#F4EFE4}.an{width:860px;margin:20px auto;${vars}}</style></head><body><div class="an iso" data-theme="dark" id="f">${svg}</div><script>window.__ANP={};${pose};window.__ANP["${NAME}"].apply(document.querySelector("svg"),${JSON.stringify(st)},${t});</script></body></html>`;
  writeFileSync(join(HERE, "preview.html"), page);
  console.log("preview.html");
}
