// Ownership: Rust's memory rules as a bench machine. A yellow crate (a value) sits on a pad in the middle. One blue key
// (its owner) hangs on post a at the left; a move carries the key over the crate to post b at the right, and post a's lamp
// turns red if a is touched afterwards (the compiler's "use of moved value"). Three reader lenses stand in front (shared
// borrows: any number may light at once); a writer stamp hangs over the crate from the back (an exclusive borrow: it lowers
// alone, and the lenses go dark). When the owner is done, a hatch opens and the crate sinks through the pad: freed on the
// spot, no collector. Schematic, not to scale.
// node build.mjs [--preview [t]] [--state='{"move":1}']  ->  ownership.svg  .json  .css  .pose.js  (+ preview.html)
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../../../.claude/skills/anatomy/kit/iso-kit.mjs";
import * as G from "../../../.claude/skills/anatomy/kit/lathe.mjs";
import { kitScript } from "../../../.claude/skills/anatomy/scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const NAME = "ownership";
const WIDTH = 600;

// ---- world (x, y floor; z up)
const BASE = { x: -220, y: -150, w: 440, d: 260, r: 8 }, BASE_H = 12;
const Z0 = BASE_H;
const PAD = { x: -62, y: -72, w: 124, d: 124 }, PAD_H = 10, PZ = Z0 + PAD_H;
const CRATE = { x: -40, y: -50, w: 80, d: 80 }, CRATE_H = 64;
const POSTX = [-168, 168], POSTY = -24, POST_H = 150, POST_W = 14;
const HOOK_Z = Z0 + POST_H - 24, HOOK_L = 26;                                // hook arm toward +y... toward the crate in x
const READX = [-70, 0, 70], READY = 86, READ_H = 44;
const WRITER = { x: -8, y: -138, w: 16, d: 16 }, WR_Z = Z0 + 172;           // the writer's post at the back and its arm height
const STAMP = { w: 44, d: 44, h: 18 }, STAMP_UP = 52;                        // stamp gap above the crate at rest

const EXTREMES = [...k.boxCorners(BASE, 0, BASE_H), ...k.boxCorners({ x: POSTX[0], y: POSTY, w: POSTX[1] - POSTX[0] + POST_W, d: POST_W }, 0, Z0 + POST_H + 20),
  ...k.boxCorners({ x: WRITER.x, y: WRITER.y, w: 16, d: 160 }, 0, WR_Z + 16)];
const VIEW = { azimuth: 50, elevation: 34 };
const pre = k.fitProjection(EXTREMES, 1000, 1000, { pad: 0, ...VIEW });
const sx = EXTREMES.map((p) => k.iso(p, pre)), bw = Math.max(...sx.map((p) => p[0])) - Math.min(...sx.map((p) => p[0])), bh = Math.max(...sx.map((p) => p[1])) - Math.min(...sx.map((p) => p[1]));
const HEIGHT = Math.round(WIDTH * bh / bw);
const P = k.fitProjection(EXTREMES, WIDTH, HEIGHT, { pad: 14, ...VIEW });

const at = (p) => k.iso(p, P);
const S = (paths, style) => k.solidSvg(paths, style);
const r1 = (v) => Math.round(v * 10) / 10;
const poly = (pts, cls) => `<path class="${cls}" d="${pts.map((p, i) => `${i ? "L" : "M"}${r1(at(p)[0])} ${r1(at(p)[1])}`).join("")}Z"/>`;
const slab = (plan, z, h, style = {}) => S(k.slabOf({ r: 1.5, ...plan }, z, h, P, 4), { tone: "hi", ...style });
const screw = (x, y, z) => S(G.lathe([[0, 0], [0, 3], [1.2, 3], [1.2, 0]], G.frameAlong([x, y, z], [0, 0, 1]), P, { steps: 16 }), { tone: "hi", crease: "none" });
const bar = (x0, x1, y, z, h = 2.2) => poly([[x0, y - h, z], [x1, y - h, z], [x1, y + h, z], [x0, y + h, z]], "ow-ink");
const dome = (x, y, z, r, cls) => {
  const mer = [[0, 0], [0, r]]; for (let i = 1; i < 8; i++) { const b = (i / 8) * Math.PI / 2; mer.push([r * Math.sin(b), r * Math.cos(b), 1]); } mer.push([r, 0]);
  return S(G.lathe(mer, G.frameAlong([x, y, z], [0, 0, 1]), P, { steps: 36 }), { tone: "hi", crease: "none", ...(cls ? { className: cls } : {}) });
};

function base() {
  const o = [slab(BASE, 0, BASE_H, { crease: "none" })];
  for (const [x, y] of [[BASE.x + 12, BASE.y + 12], [BASE.x + BASE.w - 12, BASE.y + 12], [BASE.x + 12, BASE.y + BASE.d - 12], [BASE.x + BASE.w - 12, BASE.y + BASE.d - 12]])
    o.push(screw(x, y, Z0));
  const y0 = BASE.y + BASE.d - 34, x0 = BASE.x + BASE.w - 126;
  o.push(slab({ x: x0, y: y0, w: 96, d: 24, r: 2 }, Z0, 1.6, { crease: "none" }));
  for (const [i, e] of [[0, 0], [1, 22]]) o.push(bar(x0 + 10, x0 + 86 - e, y0 + 8 + i * 8, Z0 + 1.6, 1.4));
  return o.join("");
}
function writerPost() {
  const W = WRITER, o = [];
  o.push(slab({ x: W.x - 6, y: W.y - 6, w: W.w + 12, d: W.d + 12, r: 2 }, Z0, 6));
  o.push(slab(W, Z0 + 6, WR_Z - Z0 - 6));
  o.push(slab({ x: W.x - 2, y: W.y, w: W.w + 4, d: (CRATE.y + CRATE.d / 2) - W.y + 10, r: 2 }, WR_Z, 14));
  return o.join("");
}
// the stamp: a rod down from the arm and a head, built at rest and lowered by the pose
const SZ = PZ + CRATE_H + STAMP_UP;
function stampSvg() {
  const cy = CRATE.y + CRATE.d / 2, o = [];
  o.push(S(k.cylinder(0, cy, 4, SZ + STAMP.h, WR_Z - SZ - STAMP.h, P, 20), { tone: "hi", crease: "none" }));
  o.push(slab({ x: -STAMP.w / 2, y: cy - STAMP.d / 2, w: STAMP.w, d: STAMP.d, r: 3 }, SZ, STAMP.h));
  o.push(`<g data-part="stamp-on" style="opacity:0">${slab({ x: -STAMP.w / 2, y: cy - STAMP.d / 2, w: STAMP.w, d: STAMP.d, r: 3 }, SZ, STAMP.h, { className: "ow-g" })}</g>`);
  return o.join("");
}
function post(i) {
  const x = POSTX[i] - POST_W / 2, o = [];
  o.push(slab({ x: x - 6, y: POSTY - 6, w: POST_W + 12, d: POST_W + 12, r: 2 }, Z0, 6));
  o.push(slab({ x, y: POSTY, w: POST_W, d: POST_W, r: 1 }, Z0 + 6, POST_H - 6));
  // the hook arm reaches toward the crate
  const dir = i === 0 ? 1 : -1, hx = i === 0 ? x + POST_W : x - HOOK_L;
  o.push(slab({ x: hx, y: POSTY + 3, w: HOOK_L, d: 8, r: 1 }, HOOK_Z, 6));
  o.push(slab({ x: i === 0 ? hx + HOOK_L - 6 : hx, y: POSTY + 3, w: 6, d: 8, r: 1 }, HOOK_Z + 6, 8));
  // the name plate on the post's front: one rule bar for a, two for b
  const Y = POSTY + POST_W;
  o.push(poly([[x + 2, Y, Z0 + 60], [x + POST_W - 2, Y, Z0 + 60], [x + POST_W - 2, Y, Z0 + 90], [x + 2, Y, Z0 + 90]], "ow-plate"));
  // the lamp on top: white, red (touched after the move) or green (holds the key)
  const lx = POSTX[i], lz = Z0 + POST_H;
  o.push(S(k.cylinder(lx, POSTY + POST_W / 2, 14, lz, 4, P, 28), { tone: "hi", crease: "none" }));
  o.push(dome(lx, POSTY + POST_W / 2, lz + 4, 13), `<g data-part="lamp${i}-ok" style="opacity:0">${dome(lx, POSTY + POST_W / 2, lz + 4, 13, "ow-g")}</g>`,
    `<g data-part="lamp${i}-bad" style="opacity:0">${dome(lx, POSTY + POST_W / 2, lz + 4, 13, "ow-r")}</g>`);
  return o.join("");
}
function pad() {
  const o = [slab({ ...PAD, r: 3 }, Z0, PAD_H, { crease: "none" })];
  for (const [x, y] of [[PAD.x + 8, PAD.y + 8], [PAD.x + PAD.w - 8, PAD.y + 8], [PAD.x + 8, PAD.y + PAD.d - 8], [PAD.x + PAD.w - 8, PAD.y + PAD.d - 8]]) o.push(screw(x, y, PZ));
  // the hatch outline under the crate, and the open hatch (dark) shown by the pose
  o.push(poly([[CRATE.x - 4, CRATE.y - 4, PZ], [CRATE.x + CRATE.w + 4, CRATE.y - 4, PZ], [CRATE.x + CRATE.w + 4, CRATE.y + CRATE.d + 4, PZ], [CRATE.x - 4, CRATE.y + CRATE.d + 4, PZ]], "ow-hatch"));
  o.push(`<g data-part="hole" style="opacity:0">${poly([[CRATE.x - 2, CRATE.y - 2, PZ + 0.2], [CRATE.x + CRATE.w + 2, CRATE.y - 2, PZ + 0.2], [CRATE.x + CRATE.w + 2, CRATE.y + CRATE.d + 2, PZ + 0.2], [CRATE.x - 2, CRATE.y + CRATE.d + 2, PZ + 0.2]], "ow-hole")}</g>`);
  return o.join("");
}
function crateSvg() {
  const C = CRATE, o = [S(k.slabOf({ ...C, r: 3 }, PZ, CRATE_H, P, 4), { tone: "hi", crease: "none", className: "ow-y" })];
  // slats on the two front faces and a lid rim
  const Yf = C.y + C.d, Xf = C.x + C.w;
  for (const z of [PZ + 20, PZ + 42]) {
    o.push(poly([[C.x + 4, Yf, z - 1.6], [Xf - 4, Yf, z - 1.6], [Xf - 4, Yf, z + 1.6], [C.x + 4, Yf, z + 1.6]], "ow-ink"));
    o.push(poly([[Xf, C.y + 4, z - 1.6], [Xf, Yf - 4, z - 1.6], [Xf, Yf - 4, z + 1.6], [Xf, C.y + 4, z + 1.6]], "ow-ink"));
  }
  o.push(slab({ x: C.x - 3, y: C.y - 3, w: C.w + 6, d: C.d + 6, r: 3 }, PZ + CRATE_H, 4, { className: "ow-y" }));
  return o.join("");
}
function reader(i) {
  const x = READX[i], o = [];
  o.push(S(k.cylinder(x, READY, 10, Z0, 4, P, 24), { tone: "hi", crease: "none" }));
  o.push(S(k.cylinder(x, READY, 3, Z0 + 4, READ_H - 4, P, 16), { tone: "hi", crease: "none" }));
  // the lens: a ring facing the crate (in the plane y = READY), lit blue when reading
  const F = G.frameAlong([x, READY, Z0 + READ_H + 14], [0, -1, 0]);
  const ring = (cls) => S(G.lathe([[0, 0], [0, 16], [5, 16], [5, 0]], F, P, { steps: 36 }), { tone: "hi", crease: "none", ...(cls ? { className: cls } : {}) });
  o.push(ring(), `<g data-part="lens${i}" style="opacity:0">${ring("ow-b")}</g>`);
  return o.join("");
}
// the key: a bow (ring) and a bit, hanging from post a's hook; moved by the pose along an arc to post b's hook
const KX0 = POSTX[0] - POST_W / 2 + POST_W + HOOK_L - 3, KX1 = POSTX[1] - POST_W / 2 - HOOK_L + 3, KZ = HOOK_Z - 4;
function keySvg() {
  const x = KX0, y = POSTY + 7, o = [];
  const F = G.frameAlong([x, y, KZ - 18], [0, 1, 0]);
  o.push(S(G.lathe([[0, 0], [0, 18], [6, 18], [6, 0]], F, P, { steps: 40 }), { tone: "hi", crease: "none", className: "ow-b" }));
  o.push(slab({ x: x - 4, y: y - 3, w: 8, d: 6, r: 1 }, KZ - 84, 48, { className: "ow-b" }));
  o.push(slab({ x: x + 4, y: y - 3, w: 14, d: 6, r: 1 }, KZ - 82, 8, { className: "ow-b" }));
  o.push(slab({ x: x + 4, y: y - 3, w: 10, d: 6, r: 1 }, KZ - 68, 7, { className: "ow-b" }));
  return o.join("");
}

const body = [
  base(),
  writerPost(),
  post(0), post(1),
  pad(),
  `<g data-part="crate">${crateSvg()}</g>`,
  `<g data-part="stamp">${stampSvg()}</g>`,
  reader(0), reader(1), reader(2),
  `<g data-part="key">${keySvg()}</g>`,
].join("");

const svg = k.figureSvg({
  width: WIDTH, height: HEIGHT,
  label: "Ownership: a yellow crate (a value) on a pad. One blue key (its owner) hangs on post a and can move to post b; post a's lamp turns red if it is used after the move. Three reader lenses in front can light together; a writer stamp over the crate lowers alone. When the owner is done, a hatch opens and the crate sinks: freed on the spot.",
  body: [body],
});

const tint = (cls, c, shade = 80) => {
  const mix = (p, w) => `color-mix(in srgb, ${c} ${p}%, ${w})`;
  const tones = [mix(62, "#000"), mix(shade, "#000"), c, c];
  const sel = `.iso .iso-solid.${cls}`;
  return `${sel}>.iso-fill,${sel}>.iso-top{fill:${c};stroke:var(--anatomy-hi)}\n` + tones.map((t, i) => `${sel}>.iso-shade[data-shade="${i}"]{fill:${t};stroke:${t}}`).join("\n") + "\n";
};
const flat = (cls, fill) => `.${cls}{fill:${fill};stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}\n`;
const css = k.ISO_CSS + tint("ow-r", "var(--anatomy-red)") + tint("ow-g", "var(--anatomy-green)") + tint("ow-b", "var(--anatomy-blue)") + `
.iso .iso-solid.ow-y>.iso-fill,.iso .iso-solid.ow-y>.iso-top{fill:var(--anatomy-lit-top);stroke:var(--anatomy-hi)}
.iso .iso-solid.ow-y>.iso-shade{fill:var(--anatomy-lit-shade);stroke:var(--anatomy-lit-shade)}
.ow-ink{fill:var(--anatomy-hi);stroke:none}
` + flat("ow-plate", "var(--anatomy-shade-3)") + flat("ow-hatch", "var(--anatomy-shade-2)") + flat("ow-hole", "var(--anatomy-mid)");

const pose = (kitScript() + `
const P = ${JSON.stringify(P)};
const DX = ${KX1 - KX0}, ARC = 70, SINK = ${CRATE_H + 10}, DROP = ${STAMP_UP - 2};
const q = {};
const part = (svg, n) => (q[n] = q[n] && svg.contains(q[n]) ? q[n] : svg.querySelector('[data-part="' + n + '"]'));
const cl = (u) => Math.min(1, Math.max(0, u));
const sm = (u) => { u = cl(u); return u * u * (3 - 2 * u); };
const op = (el, v) => { el.style.opacity = v <= 0.001 ? "0" : v >= 0.999 ? "1" : v.toFixed(3); };
window.__ANP[${JSON.stringify(NAME)}] = {
  init: { move: 0, bad: 0, read: 0, write: 0, free: 0 },
  apply(svg, s, t) {
    // move: the key lifts off a's hook, arcs over the crate and hangs on b's hook; the holder's lamp shows green
    const m = sm(s.move);
    part(svg, "key").setAttribute("transform", translateAlong(P, [DX * m, 0, ARC * Math.sin(Math.PI * m)]));
    op(part(svg, "key"), 1 - sm(s.free / 0.4));
    op(part(svg, "lamp0-ok"), (1 - m) * (1 - sm(s.free / 0.4)));
    op(part(svg, "lamp1-ok"), m * (1 - sm(s.free / 0.4)));
    op(part(svg, "lamp0-bad"), sm(s.bad / 0.3));
    // read: lenses light one by one (any number); write: the stamp lowers and lights, and the lenses go dark
    const w = sm(s.write);
    for (let i = 0; i < 3; i++) op(part(svg, "lens" + i), cl(s.read - i) * (1 - w));
    part(svg, "stamp").setAttribute("transform", translateAlong(P, [0, 0, -DROP * w]));
    op(part(svg, "stamp-on"), w);
    // free: the hatch opens and the crate sinks through the pad, fading as it goes
    const f = sm(s.free);
    op(part(svg, "hole"), sm(s.free / 0.25));
    part(svg, "crate").setAttribute("transform", translateAlong(P, [0, 0, -SINK * f]));
    op(part(svg, "crate"), 1 - sm((s.free - 0.1) / 0.45));
  },
};
`).replaceAll("<script", "<\\u0073cript").replaceAll("</script", "<\\/script");

writeFileSync(join(HERE, `${NAME}.svg`), svg);
writeFileSync(join(HERE, `${NAME}.css`), css);
writeFileSync(join(HERE, `${NAME}.pose.js`), pose);
const anchors = {
  crate: [CRATE.x + CRATE.w, CRATE.y + CRATE.d, PZ + CRATE_H / 2],
  a: [POSTX[0], POSTY + POST_W, Z0 + POST_H],
  b: [POSTX[1], POSTY + POST_W, Z0 + POST_H],
  key: [KX0, POSTY + 7, KZ - 20],
  readers: [0, READY, Z0 + READ_H + 10],
  stamp: [0, CRATE.y + CRATE.d / 2, SZ + STAMP.h],
  pad: [0, PAD.y + PAD.d, PZ],
};
writeFileSync(join(HERE, `${NAME}.json`), JSON.stringify({ width: WIDTH, height: HEIGHT,
  params: {
    move: "0..1 the owner key arcs from post a (left) to post b (right); the holder's lamp is green",
    bad: "0..1 post a's lamp turns red (a used after the move: the compiler's error)",
    read: "0..3 reader lenses light one by one (shared borrows)",
    write: "0..1 the writer stamp lowers onto the crate and turns green; the lenses go dark (exclusive borrow)",
    free: "0..1 the hatch opens and the crate sinks through the pad and fades; the key and lamps go too (freed)",
  },
  anchors: Object.fromEntries(Object.entries(anchors).map(([n, p]) => [n, at(p).map(r1)])) }, null, 1));
console.log("wrote", NAME, svg.length, "bytes", WIDTH, "x", HEIGHT, "scale", P.scale.toFixed(3));

if (process.argv.includes("--preview")) {
  const t = Number(process.argv[process.argv.indexOf("--preview") + 1]) || 0;
  const st = { move: 0, bad: 0, read: 0, write: 0, free: 0 };
  const args = process.argv.find((a) => a.startsWith("--state="));
  if (args) Object.assign(st, JSON.parse(args.slice(8)));
  const vars = "--anatomy-paper:#FFFFFF;--anatomy-face:#FFFFFF;--anatomy-top:#FFFFFF;--anatomy-shade-0:#C4BAA6;--anatomy-shade-1:#D4CBB9;--anatomy-shade-2:#E3DCCD;--anatomy-shade-3:#F1ECE2;--anatomy-hi:#121212;--anatomy-mid:#3D3932;--anatomy-lo:#5A554B;--anatomy-faint:#B3AA98;--anatomy-lit:#121212;--anatomy-lit-top:#FFD23F;--anatomy-lit-shade:#F0B90F;--anatomy-halo:#6F6552;--anatomy-halo-opacity:.30;--anatomy-dot:#121212;--anatomy-weight:3.2px;--anatomy-red:#D7392B;--anatomy-green:#13965A;--anatomy-blue:#2C5BEA";
  const page = `<!doctype html><html><head><meta charset="utf-8"><style>${css}body{margin:0;background:#F4EFE4}.an{width:860px;margin:20px auto;${vars}}</style></head><body><div class="an iso" data-theme="dark" id="f">${svg}</div><script>window.__ANP={};${pose};window.__ANP["${NAME}"].apply(document.querySelector("svg"),${JSON.stringify(st)},${t});</script></body></html>`;
  writeFileSync(join(HERE, "preview.html"), page);
  console.log("preview.html");
}
