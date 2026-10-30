// Switchboard: the 3-SAT puzzle as a machine. A console carries eight toggle switches in a row (1 to 8, left to right);
// a lever leans toward the viewer when the switch is on (lit yellow) and away when it is off. An upright rule board behind
// the console carries three lamps, one per rule ("switch 3 on, or switch 7 off"): grey when not checked, green when the
// rule holds, red when it fails. Switches 4 to 8 can fade in, so the row grows on a word.
// Schematic: a k-SAT formula with n variables and m clauses, n = switches, m = lamps.
// node build.mjs [--preview [t]] [--state='{"s2":1}']  ->  switchboard.svg  .json  .css  .pose.js  (+ preview.html)
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../../../.claude/skills/anatomy/kit/iso-kit.mjs";
import * as G from "../../../.claude/skills/anatomy/kit/lathe.mjs";
import { kitScript } from "../../../.claude/skills/anatomy/scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const NAME = "switchboard";
const WIDTH = 600;

// ---- world (x, y floor; z up). The row runs along +x; the console's front faces +y.
const BASE = { x: -222, y: -104, w: 444, d: 214, r: 8 }, BASE_H = 12;
const Z0 = BASE_H;
const CON = { x: -206, y: -22, w: 412, d: 92, r: 3 }, CON_H = 34;           // the console
const TOP = Z0 + CON_H;
const N = 8, PITCH = 48, SX0 = CON.x + 38;                                   // switch centres along x
const SY = CON.y + CON.d / 2 + 6;                                            // switch centres along y
const PLATE = { w: 30, d: 38, h: 4 };
const PIV_Z = TOP + PLATE.h + 3;
const LEV = { len: 34, half: 4.6, deep: 4.6, tip: 7.5 };                     // lever: a bar and a knob
const ON = 28, OFF = -28;                                                    // lever tilt from vertical, toward +y when on
const BOARD = { x: -206, y: -90, w: 412, d: 16, r: 2 }, BOARD_H = 150;      // the rule board
const BFRONT = BOARD.y + BOARD.d;
const LAMPS = [-136, 0, 136].map((x) => ({ x, z: Z0 + 112 }));

const EXTREMES = [...k.boxCorners(BASE, 0, BASE_H), ...k.boxCorners(BOARD, 0, Z0 + BOARD_H + 8), ...k.boxCorners(CON, 0, TOP + 50)];
const VIEW = { azimuth: 40, elevation: 34 };
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
// the lever of switch i at tilt th (degrees from vertical, + toward the viewer): a bar and a knob, pivot on the axis along x
function lever(i, th, X0, PITCH_, SY_, PZ, L) {
  const a = (th * Math.PI) / 180, u = [0, Math.sin(a), Math.cos(a)], w = [0, Math.cos(a), -Math.sin(a)];
  const x = X0 + i * PITCH_, c = (s) => [x, SY_ + u[1] * s, PZ + u[2] * s];
  const m = (v, s) => v.map((q) => q * s);
  return [
    { c: c(L.len / 2), ax: [[L.half, 0, 0], m(u, L.len / 2), m(w, L.deep)] },
    { c: c(L.len + L.tip * 0.6), ax: [[L.tip, 0, 0], m(u, L.tip), m(w, L.tip)] },
  ];
}
const OB = (c, axes, style) => S(obox(c, axes, P, k.iso, k.cameraOf), { tone: "hi", crease: "none", ...style });
const leverSvg = (i, th, cls) => lever(i, th, SX0, PITCH, SY, PIV_Z, LEV).map((b) => OB(b.c, b.ax, cls ? { className: cls } : {})).join("");

// ---- parts, back to front
function base() {
  const o = [slab(BASE, 0, BASE_H, { crease: "none" })];
  for (const [x, y] of [[BASE.x + 10, BASE.y + 10], [BASE.x + BASE.w - 10, BASE.y + 10], [BASE.x + 10, BASE.y + BASE.d - 10], [BASE.x + BASE.w - 10, BASE.y + BASE.d - 10]])
    o.push(S(k.cylinder(x, y, 3.2, Z0, 1.6, P, 20), { tone: "hi", crease: "none" }));
  return o.join("");
}
function board() {
  const o = [];
  o.push(slab({ x: BOARD.x - 5, y: BOARD.y - 5, w: BOARD.w + 10, d: BOARD.d + 10, r: 3 }, Z0, 7));
  o.push(slab(BOARD, Z0 + 7, BOARD_H - 7, { crease: "none" }));
  o.push(slab({ x: BOARD.x - 3, y: BOARD.y - 3, w: BOARD.w + 6, d: BOARD.d + 6, r: 2 }, Z0 + BOARD_H, 6));
  // under each lamp, a rule plate with three bars: the rule's three switches
  for (const L of LAMPS) {
    const z0 = L.z - 62, z1 = L.z - 28, x0 = L.x - 44, x1 = L.x + 44;
    o.push(poly([[x0, BFRONT, z0], [x1, BFRONT, z0], [x1, BFRONT, z1], [x0, BFRONT, z1]], "sb-plate"));
    for (const [z, e] of [[z0 + 8, 10], [z0 + 17, 22], [z0 + 26, 34]]) o.push(poly([[x0 + 8, BFRONT, z - 2], [x1 - e, BFRONT, z - 2], [x1 - e, BFRONT, z + 2], [x0 + 8, BFRONT, z + 2]], "sb-ink"));
  }
  return o.join("");
}
function lamp(L, i) {
  const F = G.frameAlong([L.x, BFRONT, L.z], [0, 1, 0]);
  const o = [S(G.lathe([[0, 0], [0, 22], [5, 22], [5, 0]], F, P, { steps: 48 }), { tone: "hi", crease: "none" })];
  const F2 = G.frameAlong([L.x, BFRONT + 5, L.z], [0, 1, 0]);
  const mer = [[0, 0], [0, 16]];
  for (let s = 1; s < 8; s++) { const b = (s / 8) * Math.PI / 2; mer.push([12 * Math.sin(b), 16 * Math.cos(b), 1]); }
  mer.push([12, 0]);
  const dome = (cls) => S(G.lathe(mer, F2, P, { steps: 48 }), { tone: "hi", crease: "none", ...(cls ? { className: cls } : {}) });
  o.push(dome(), `<g data-part="ok-${i}" style="opacity:0">${dome("sb-g")}</g>`, `<g data-part="bad-${i}" style="opacity:0">${dome("sb-r")}</g>`);
  return o.join("");
}
function console_() {
  const o = [];
  o.push(slab({ x: CON.x - 5, y: CON.y - 5, w: CON.w + 10, d: CON.d + 10, r: 4 }, Z0, 6));
  o.push(slab(CON, Z0 + 6, CON_H - 6, { crease: "none" }));
  // a label strip along the front face with a tick under each switch
  const Y = CON.y + CON.d;
  o.push(poly([[CON.x + 12, Y, Z0 + 12], [CON.x + CON.w - 12, Y, Z0 + 12], [CON.x + CON.w - 12, Y, Z0 + 26], [CON.x + 12, Y, Z0 + 26]], "sb-plate"));
  for (let i = 0; i < N; i++) { const x = SX0 + i * PITCH; o.push(poly([[x - 2, Y, Z0 + 15], [x + 2, Y, Z0 + 15], [x + 2, Y, Z0 + 23], [x - 2, Y, Z0 + 23]], "sb-ink")); }
  return o.join("");
}
function plate(i) {
  const x = SX0 + i * PITCH;
  const o = [slab({ x: x - PLATE.w / 2, y: SY - PLATE.d / 2, w: PLATE.w, d: PLATE.d, r: 2 }, TOP, PLATE.h)];
  o.push(S(G.lathe([[0, 0], [0, 7], [6, 7], [6, 0]], G.frameAlong([x - 10, SY, PIV_Z], [1, 0, 0]), P, { steps: 24 }), { tone: "hi", crease: "none" }));
  return o.join("");
}
function axleCap(i) {
  const x = SX0 + i * PITCH;
  return S(G.lathe([[0, 0], [0, 7], [5, 7], [5, 0]], G.frameAlong([x + 5, SY, PIV_Z], [1, 0, 0]), P, { steps: 24 }), { tone: "hi", crease: "none" });
}

const sw = [];
for (let i = 0; i < N; i++)
  sw.push(`<g data-part="sw-${i}">${plate(i)}<g data-part="lv-${i}">${leverSvg(i, OFF)}</g><g data-part="lvon-${i}" style="opacity:0"></g>${axleCap(i)}</g>`);

const body = [base(), board(), ...LAMPS.map(lamp), console_(), ...sw].join("");

const svg = k.figureSvg({
  width: WIDTH, height: HEIGHT,
  label: "A switchboard: a console with a row of eight toggle switches, each lever leaning toward the viewer and lit yellow when on, away when off. Behind it an upright board carries three lamps, one per rule, each with a small plate of three bars below it; a lamp lights green when its rule holds and red when it fails.",
  body: [body],
});

const tint = (cls, c) => {
  const mix = (p, w) => `color-mix(in srgb, ${c} ${p}%, ${w})`;
  const tones = [mix(62, "#000"), mix(80, "#000"), c, c];
  const sel = `.iso .iso-solid.${cls}`;
  return `${sel}>.iso-fill,${sel}>.iso-top{fill:${c};stroke:${c}}\n` + tones.map((t, i) => `${sel}>.iso-shade[data-shade="${i}"]{fill:${t};stroke:${t}}`).join("\n") + "\n";
};
const flat = (cls, fill) => `.${cls}{fill:${fill};stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}\n`;
const css = k.ISO_CSS + tint("sb-g", "var(--anatomy-green)") + tint("sb-r", "var(--anatomy-red)") + `
.iso .iso-solid.sb-y>.iso-fill,.iso .iso-solid.sb-y>.iso-top{fill:var(--anatomy-lit-top);stroke:var(--anatomy-lit-top)}
.iso .iso-solid.sb-y>.iso-shade{fill:var(--anatomy-lit-shade);stroke:var(--anatomy-lit-shade)}
.iso .iso-solid.sb-y>.iso-shade[data-shade="2"],.iso .iso-solid.sb-y>.iso-shade[data-shade="3"]{fill:var(--anatomy-lit-top);stroke:var(--anatomy-lit-top)}
.sb-ink{fill:var(--anatomy-hi);stroke:none}
` + flat("sb-plate", "var(--anatomy-shade-3)");

const pose = (kitScript() + `
const P = ${JSON.stringify(P)};
${obox.toString()}
${lever.toString()}
const N = ${N}, SX0 = ${SX0}, PITCH = ${PITCH}, SY = ${SY}, PIV_Z = ${PIV_Z}, LEV = ${JSON.stringify(LEV)}, ON = ${ON}, OFF = ${OFF};
const q = {};
const part = (svg, n) => (q[n] = q[n] && svg.contains(q[n]) ? q[n] : svg.querySelector('[data-part="' + n + '"]'));
const sm = (u) => { u = Math.min(1, Math.max(0, u)); return u * u * (3 - 2 * u); };
const op = (el, v) => { el.style.opacity = v <= 0.001 ? "0" : v >= 0.999 ? "1" : v.toFixed(3); };
const OB = (c, axes, cls) => solidSvg(obox(c, axes, P, iso, cameraOf), cls ? { tone: "hi", crease: "none", className: cls } : { tone: "hi", crease: "none" });
const last = new WeakMap();
const setHtml = (el, key, html) => { if (last.get(el) !== key) { last.set(el, key); el.innerHTML = html(); } };
const init = { more: 1, r0: 0, r1: 0, r2: 0 };
for (let i = 0; i < N; i++) init["s" + i] = 0;
window.__ANP[${JSON.stringify(NAME)}] = {
  init,
  apply(svg, s, t) {
    // more: switches 4 to 8 fade in one after another (0: only 1 to 3 shown)
    for (let i = 3; i < N; i++) op(part(svg, "sw-" + i), sm(s.more * (N - 3) - (i - 3)));
    for (let i = 0; i < N; i++) {
      const v = Math.min(1, Math.max(0, s["s" + i])), th = Math.round((OFF + (ON - OFF) * sm(v)) * 10) / 10;
      const lv = (cls) => () => lever(i, th, SX0, PITCH, SY, PIV_Z, LEV).map((b) => OB(b.c, b.ax, cls)).join("");
      setHtml(part(svg, "lv-" + i), th, lv());
      setHtml(part(svg, "lvon-" + i), th, lv("sb-y"));
      op(part(svg, "lvon-" + i), sm((v - 0.5) / 0.3));
    }
    // r: -1 red (the rule fails), 0 grey (not checked), 1 green (the rule holds)
    for (let i = 0; i < 3; i++) { const r = s["r" + i]; op(part(svg, "ok-" + i), sm(r)); op(part(svg, "bad-" + i), sm(-r)); }
  },
};
`).replaceAll("<script", "<\\u0073cript").replaceAll("</script", "<\\/script");

writeFileSync(join(HERE, `${NAME}.svg`), svg);
writeFileSync(join(HERE, `${NAME}.css`), css);
writeFileSync(join(HERE, `${NAME}.pose.js`), pose);
const anchors = { board: [0, BFRONT, Z0 + BOARD_H / 2], console: [0, CON.y + CON.d, Z0 + CON_H / 2] };
for (let i = 0; i < N; i++) anchors["sw" + (i + 1)] = [SX0 + i * PITCH, SY, PIV_Z + LEV.len];
LAMPS.forEach((L, i) => (anchors["lamp" + (i + 1)] = [L.x, BFRONT + 10, L.z]));
writeFileSync(join(HERE, `${NAME}.json`), JSON.stringify({ width: WIDTH, height: HEIGHT,
  params: {
    s0: "0..1 switch 1 off (lever away) to on (lever toward the viewer, lit yellow); s1 .. s7 the same for switches 2 to 8",
    more: "0..1 switches 4 to 8 fade in one after another (init 1: all eight shown)",
    r0: "-1..1 lamp 1: -1 red (the rule fails), 0 grey, 1 green (the rule holds); r1, r2 lamps 2 and 3",
  },
  anchors: Object.fromEntries(Object.entries(anchors).map(([n, p]) => [n, at(p).map(r1)])) }, null, 1));
console.log("wrote", NAME, svg.length, "bytes", WIDTH, "x", HEIGHT, "scale", P.scale.toFixed(3));

if (process.argv.includes("--preview")) {
  const t = Number(process.argv[process.argv.indexOf("--preview") + 1]) || 0;
  const st = { more: 1, r0: 0, r1: 0, r2: 0 };
  for (let i = 0; i < N; i++) st["s" + i] = 0;
  const args = process.argv.find((a) => a.startsWith("--state="));
  if (args) Object.assign(st, JSON.parse(args.slice(8)));
  const vars = "--anatomy-paper:#FFFFFF;--anatomy-face:#FFFFFF;--anatomy-top:#FFFFFF;--anatomy-shade-0:#C4BAA6;--anatomy-shade-1:#D4CBB9;--anatomy-shade-2:#E3DCCD;--anatomy-shade-3:#F1ECE2;--anatomy-hi:#121212;--anatomy-mid:#3D3932;--anatomy-lo:#5A554B;--anatomy-faint:#B3AA98;--anatomy-lit:#121212;--anatomy-lit-top:#FFD23F;--anatomy-lit-shade:#F0B90F;--anatomy-halo:#6F6552;--anatomy-halo-opacity:.30;--anatomy-dot:#121212;--anatomy-weight:3.2px;--anatomy-red:#D7392B;--anatomy-green:#13965A;--anatomy-blue:#2C5BEA";
  const page = `<!doctype html><html><head><meta charset="utf-8"><style>${css}body{margin:0;background:#F4EFE4}.an{width:860px;margin:20px auto;${vars}}</style></head><body><div class="an iso" data-theme="dark" id="f">${svg}</div><script>window.__ANP={};${pose};window.__ANP["${NAME}"].apply(document.querySelector("svg"),${JSON.stringify(st)},${t});</script></body></html>`;
  writeFileSync(join(HERE, "preview.html"), page);
  console.log("preview.html");
}
