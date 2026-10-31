// Context reader: a chat's context window as a bench machine. A long tray on a base plate holds the conversation as
// message slips laid in order, left to right (blue: what you typed, white: the reply). A reading head rides a rail on two
// posts behind the tray, on a cantilever arm over the slips: each turn it sweeps the whole tray from the first slip to the
// last, because the model keeps nothing between turns; it reads what is in the tray. A holder at the head of the tray
// takes a yellow memory note: "memory" is a note laid in first. A token ruler runs along the front lip, and a red stop at
// the far end marks the window's limit. Middle slips can fade: a long context is read worst in the middle.
// Schematic, not to scale.
// node build.mjs [--preview [t]] [--state='{"msgs":4}']  ->  context-reader.svg  .json  .css  .pose.js  (+ preview.html)
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../../../.claude/skills/anatomy/kit/iso-kit.mjs";
import * as G from "../../../.claude/skills/anatomy/kit/lathe.mjs";
import { kitScript } from "../../../.claude/skills/anatomy/scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const NAME = "context-reader";
const WIDTH = 600;

// ---- world (x, y floor; z up). The tray runs along +x (screen left to right); fronts face +y.
const BASE = { x: -290, y: -128, w: 580, d: 236, r: 8 }, BASE_H = 12;
const Z0 = BASE_H;
const TRAY = { x: -268, y: -46, w: 536, d: 104, r: 4 }, TRAY_H = 14, LIP = 6;
const TZ = Z0 + 4;                                                        // the tray floor's top
const N = 8, SL = { w: 48, d: 76, t: 2.4, gap: 7 }, SX0 = -194, SY = TRAY.y + (TRAY.d - 76) / 2;
const slipX = (i) => SX0 + i * (SL.w + SL.gap);
const NOTE = { x: -258, y: SY + 4, w: 48, d: 68 };                         // the memory-note holder at the head of the tray
const POST = { w: 14, d: 14 }, RAIL_Z = Z0 + 84, RAIL = { y: -112, d: 14, h: 12 };
const POSTS = [-262, 248];
const CARR = { w: 34, d: 30, h: 26 };                                     // the carriage on the rail
const ARM = { w: 16, h: 10 }, ARM_Y1 = SY + 38;                          // the arm reaches to the slips' centre line
const HEAD = { w: 30, d: 30, h: 34 };                                     // the reading head under the arm's tip
const HX0 = NOTE.x + NOTE.w / 2, HX1 = slipX(N - 1) + SL.w / 2;          // the head's sweep: the note, then the last slip
const STOP = { x: TRAY.x + TRAY.w - 22, y: TRAY.y + 8, w: 12, d: TRAY.d - 16 };

const EXTREMES = [...k.boxCorners(BASE, 0, BASE_H), ...k.boxCorners({ x: POSTS[0], y: RAIL.y, w: POSTS[1] - POSTS[0] + POST.w, d: RAIL.d }, 0, RAIL_Z + RAIL.h + CARR.h),
  ...k.boxCorners(TRAY, 0, Z0 + TRAY_H)];
const VIEW = { azimuth: 52, elevation: 38 };
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
const bar = (x0, x1, y, z, h = 2.2) => poly([[x0, y - h, z], [x1, y - h, z], [x1, y + h, z], [x0, y + h, z]], "cr-ink");

// ---- parts, back to front
function base() {
  const o = [slab(BASE, 0, BASE_H, { crease: "none" })];
  for (const [x, y] of [[BASE.x + 12, BASE.y + 12], [BASE.x + BASE.w - 12, BASE.y + 12], [BASE.x + 12, BASE.y + BASE.d - 12], [BASE.x + BASE.w - 12, BASE.y + BASE.d - 12]])
    o.push(screw(x, y, Z0));
  // a label plate on the base's front strip, three rule lines
  const y0 = TRAY.y + TRAY.d + 16, x0 = BASE.x + 26;
  o.push(slab({ x: x0, y: y0, w: 92, d: 30, r: 2 }, Z0, 1.6, { crease: "none" }));
  for (const [i, e] of [[0, 0], [1, 18], [2, 34]]) o.push(bar(x0 + 10, x0 + 82 - e, y0 + 8 + i * 7, Z0 + 1.6, 1.4));
  return o.join("");
}

function rail() {
  const o = [];
  for (const x of POSTS) {
    o.push(slab({ x: x - 6, y: RAIL.y - 6, w: POST.w + 12, d: POST.d + 12, r: 2 }, Z0, 6));
    o.push(slab({ x, y: RAIL.y, w: POST.w, d: POST.d, r: 1 }, Z0 + 6, RAIL_Z - Z0 - 6));
  }
  o.push(slab({ x: POSTS[0] - 4, y: RAIL.y, w: POSTS[1] - POSTS[0] + POST.w + 8, d: RAIL.d, r: 1.5 }, RAIL_Z, RAIL.h));
  for (const x of [POSTS[0] - 8, POSTS[1] + POST.w + 2]) o.push(slab({ x, y: RAIL.y - 3, w: 6, d: RAIL.d + 6, r: 1 }, RAIL_Z - 3, RAIL.h + 6));
  // ticks on the rail's front face, one per slip
  const Y = RAIL.y + RAIL.d;
  for (let i = 0; i < N; i++) { const x = slipX(i) + SL.w / 2; o.push(poly([[x - 1.4, Y, RAIL_Z + 3], [x + 1.4, Y, RAIL_Z + 3], [x + 1.4, Y, RAIL_Z + RAIL.h - 3], [x - 1.4, Y, RAIL_Z + RAIL.h - 3]], "cr-ink")); }
  return o.join("");
}

function tray() {
  const o = [];
  o.push(slab(TRAY, Z0, 4, { crease: "none" }));                          // the floor
  const T = TRAY;
  o.push(slab({ x: T.x, y: T.y, w: T.w, d: LIP, r: 1 }, TZ, TRAY_H - 4));    // back lip
  o.push(slab({ x: T.x, y: T.y, w: LIP, d: T.d, r: 1 }, TZ, TRAY_H - 4));    // left lip
  o.push(slab({ x: T.x + T.w - LIP, y: T.y, w: LIP, d: T.d, r: 1 }, TZ, TRAY_H - 4));
  // the window's limit: a red stop block near the far end
  o.push(slab(STOP, TZ, 10, { crease: "none", className: "cr-r" }));
  // the note holder: a recessed plate with two corner clips
  o.push(slab({ x: NOTE.x - 3, y: NOTE.y - 3, w: NOTE.w + 6, d: NOTE.d + 6, r: 2 }, TZ, 1.2, { crease: "none", className: "cr-k" }));
  return o.join("");
}
function trayFront() {
  const T = TRAY, o = [];
  o.push(slab({ x: T.x, y: T.y + T.d - LIP, w: T.w, d: LIP, r: 1 }, TZ, TRAY_H - 4));
  // the token ruler on the front lip's top: a minor tick every 11, a major every 5th
  const tk = k.topTicks(T.x + 12, T.x + T.w - 12, 11, 5, T.y + T.d - LIP + 0.6, Z0 + TRAY_H, [2.4, 4.6], P, "x");
  o.push(k.lineSvg(tk.minor, { tone: "lo", free: true }), k.lineSvg(tk.major, { tone: "mid", free: true }));
  return o.join("");
}

// a slip: a thin card with three rule lines of "text"; user slips carry a blue band, the lit slip turns yellow
function slipSvg(i) {
  const x = slipX(i), z = TZ + SL.t, user = i % 2 === 0;
  const o = [S(k.slabOf({ x, y: SY, w: SL.w, d: SL.d, r: 1.5 }, TZ, SL.t, P, 3), { tone: "hi", crease: "none", className: user ? "cr-b2" : undefined })];
  if (i === 0) o.push(`<g data-part="lit" style="opacity:0">${S(k.slabOf({ x, y: SY, w: SL.w, d: SL.d, r: 1.5 }, TZ, SL.t, P, 3), { tone: "hi", crease: "none", className: "cr-y" })}</g>`);
  const rows = user ? [[10, 0], [22, 14]] : [[10, 0], [22, 8], [34, 18], [46, 26]];
  for (const [dy, e] of rows) o.push(poly([[x + 7, SY + dy, z], [x + SL.w - 7 - e * 0.5, SY + dy, z], [x + SL.w - 7 - e * 0.5, SY + dy + 4.4, z], [x + 7, SY + dy + 4.4, z]], "cr-ink"));
  return `<g data-part="slip-${i}" style="opacity:0">${o.join("")}</g>`;
}
function noteSvg() {
  const x = NOTE.x, y = NOTE.y, z = TZ + 1.2 + 3;
  const o = [S(k.slabOf({ x, y, w: NOTE.w, d: NOTE.d, r: 1.5 }, TZ + 1.2, 3, P, 3), { tone: "hi", crease: "none", className: "cr-y" })];
  for (const [dy, e] of [[12, 0], [24, 10], [36, 4]]) o.push(poly([[x + 7, y + dy, z], [x + NOTE.w - 7 - e, y + dy, z], [x + NOTE.w - 7 - e, y + dy + 4.4, z], [x + 7, y + dy + 4.4, z]], "cr-ink"));
  return `<g data-part="note" style="opacity:0">${o.join("")}</g>`;
}
// the two clips that hold the note, drawn over it
function clips() {
  return [NOTE.y - 4, NOTE.y + NOTE.d - 8].map((y) => slab({ x: NOTE.x + NOTE.w / 2 - 9, y, w: 18, d: 12, r: 2 }, TZ + 4.2, 3)).join("");
}

// the carriage, arm and head, built at x = 0 and moved along x by the pose
function headSvg() {
  const o = [], cy = ARM_Y1;
  const hz0 = RAIL_Z + RAIL.h + 8 - HEAD.h + ARM.h - 6, fz = TZ + SL.t + 0.4;
  o.push(`<g data-part="cone" style="opacity:0">${poly([[-9, cy, hz0], [9, cy, hz0], [SL.w / 2 - 3, cy + SL.d / 2 - 4, fz], [-SL.w / 2 + 3, cy + SL.d / 2 - 4, fz]], "cr-beam")}${poly([[-9, cy, hz0], [9, cy, hz0], [SL.w / 2 - 3, cy - SL.d / 2 + 4, fz], [-SL.w / 2 + 3, cy - SL.d / 2 + 4, fz]], "cr-beam")}</g>`);
  o.push(slab({ x: -CARR.w / 2, y: RAIL.y - 6, w: CARR.w, d: CARR.d, r: 2 }, RAIL_Z + RAIL.h, CARR.h));
  o.push(screw(-CARR.w / 2 + 7, RAIL.y + 2, RAIL_Z + RAIL.h + CARR.h), screw(CARR.w / 2 - 7, RAIL.y + 2, RAIL_Z + RAIL.h + CARR.h));
  o.push(slab({ x: -ARM.w / 2, y: RAIL.y + CARR.d - 6, w: ARM.w, d: ARM_Y1 - (RAIL.y + CARR.d - 6), r: 1 }, RAIL_Z + RAIL.h + 8, ARM.h));
  const hz = RAIL_Z + RAIL.h + 8 - HEAD.h + ARM.h;
  o.push(slab({ x: -HEAD.w / 2, y: cy - HEAD.d / 2, w: HEAD.w, d: HEAD.d, r: 3 }, hz, HEAD.h));
  // a vent row on the head's front face
  const Y = cy + HEAD.d / 2;
  for (let i = 0; i < 3; i++) { const x0 = -9 + i * 7; o.push(poly([[x0, Y, hz + 14], [x0 + 3.4, Y, hz + 14], [x0 + 3.4, Y, hz + 26], [x0, Y, hz + 26]], "cr-slot")); }
  // the lens under the head, and its lamp ring (lit while reading)
  o.push(S(k.cylinder(0, cy, 11, hz - 6, 6, P, 32), { tone: "hi", crease: "none" }));
  o.push(`<g data-part="lens" style="opacity:0">${S(k.cylinder(0, cy, 11, hz - 6, 6, P, 32), { tone: "hi", crease: "none", className: "cr-y" })}</g>`);
  return o.join("");
}
// the reading beam: a thin yellow footprint on the slip under the lens
function beamSvg() {
  const cy = ARM_Y1 - HEAD.d / 2;
  return `<g data-part="beam" style="opacity:0">${poly([[-SL.w / 2 + 2, SY + 3, TZ + SL.t + 0.4], [SL.w / 2 - 2, SY + 3, TZ + SL.t + 0.4], [SL.w / 2 - 2, SY + SL.d - 3, TZ + SL.t + 0.4], [-SL.w / 2 + 2, SY + SL.d - 3, TZ + SL.t + 0.4]], "cr-beam")}</g>`;
}

const body = [
  base(),
  rail(),
  tray(),
  noteSvg(),
  clips(),
  ...Array.from({ length: N }, (_, i) => slipSvg(i)),
  `<g data-part="beamg">${beamSvg()}</g>`,
  trayFront(),
  `<g data-part="head">${headSvg()}</g>`,
].join("");

const svg = k.figureSvg({
  width: WIDTH, height: HEIGHT,
  label: "A context reader: a long tray on a base plate holds a chat as message slips laid in order, blue for what you typed and white for the replies. A reading head on a rail behind the tray sweeps over every slip each turn. A holder at the head of the tray takes a yellow memory note; a red stop at the far end marks the window's limit.",
  body: [body],
});

const tint = (cls, c, shade = 80) => {
  const mix = (p, w) => `color-mix(in srgb, ${c} ${p}%, ${w})`;
  const tones = [mix(62, "#000"), mix(shade, "#000"), c, c];
  const sel = `.iso .iso-solid.${cls}`;
  return `${sel}>.iso-fill,${sel}>.iso-top{fill:${c};stroke:${c}}\n` + tones.map((t, i) => `${sel}>.iso-shade[data-shade="${i}"]{fill:${t};stroke:${t}}`).join("\n") + "\n";
};
const flat = (cls, fill) => `.${cls}{fill:${fill};stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}\n`;
const css = k.ISO_CSS + tint("cr-r", "var(--anatomy-red)") + tint("cr-k", "var(--anatomy-shade-2)", 90) + tint("cr-b2", "#D3DEFF", 88) + `
.iso .iso-solid.cr-b2>.iso-fill,.iso .iso-solid.cr-b2>.iso-top{stroke:var(--anatomy-hi)}
.iso .iso-solid.cr-y>.iso-fill,.iso .iso-solid.cr-y>.iso-top{fill:var(--anatomy-lit-top);stroke:var(--anatomy-hi)}
.iso .iso-solid.cr-y>.iso-shade{fill:var(--anatomy-lit-shade);stroke:var(--anatomy-lit-shade)}
.cr-ink{fill:var(--anatomy-hi);stroke:none}
.cr-beam{fill:var(--anatomy-lit-top);fill-opacity:.55;stroke:none}
` + flat("cr-slot", "var(--anatomy-mid)");

const pose = (kitScript() + `
const P = ${JSON.stringify(P)};
const N = ${N}, HX0 = ${HX0}, HX1 = ${HX1}, X = ${JSON.stringify(Array.from({ length: N }, (_, i) => slipX(i) + SL.w / 2))}, NX = ${HX0};
const q = {};
const part = (svg, n) => (q[n] = q[n] && svg.contains(q[n]) ? q[n] : svg.querySelector('[data-part="' + n + '"]'));
const cl = (u) => Math.min(1, Math.max(0, u));
const sm = (u) => { u = cl(u); return u * u * (3 - 2 * u); };
const op = (el, v) => { el.style.opacity = v <= 0.001 ? "0" : v >= 0.999 ? "1" : v.toFixed(3); };
window.__ANP[${JSON.stringify(NAME)}] = {
  init: { msgs: 0, scan: 0, read: 0, note: 0, lit: 0, mid: 0 },
  apply(svg, s, t) {
    // msgs: slips land one by one (each drops 18 units onto the tray over its own step); mid fades slips 2..5
    for (let i = 0; i < N; i++) {
      const u = cl(s.msgs - i), el = part(svg, "slip-" + i), m = i >= 2 && i <= 5 ? 1 - 0.8 * sm(s.mid) : 1;
      op(el, sm(u / 0.5) * m);
      el.setAttribute("transform", translateAlong(P, [0, 0, 18 * (1 - sm(u))]));
    }
    // note: the memory note drops into its holder
    const nu = sm(s.note);
    op(part(svg, "note"), sm(s.note / 0.4));
    part(svg, "note").setAttribute("transform", translateAlong(P, [0, 0, 26 * (1 - nu)]));
    op(part(svg, "lit"), sm(s.lit));
    // scan: the head sweeps from the note holder (0) to the last slip (1); read lights the lens and the beam
    const hx = HX0 + (HX1 - HX0) * cl(s.scan);
    part(svg, "head").setAttribute("transform", translateAlong(P, [hx, 0, 0]));
    // the beam shows only over a slip that is there (or the note), nearest slot to the head
    let best = NX, have = s.note > 0.5, dmin = Math.abs(hx - NX);
    for (let i = 0; i < N; i++) { const dd = Math.abs(hx - X[i]); if (dd < dmin) { dmin = dd; best = X[i]; have = s.msgs - i > 0.5; } }
    part(svg, "beamg").setAttribute("transform", translateAlong(P, [best, 0, 0]));
    op(part(svg, "beam"), have ? sm(s.read) : 0);
    op(part(svg, "lens"), sm(s.read));
    op(part(svg, "cone"), have ? sm(s.read) * 0.8 : 0);
  },
};
`).replaceAll("<script", "<\\u0073cript").replaceAll("</script", "<\\/script");

writeFileSync(join(HERE, `${NAME}.svg`), svg);
writeFileSync(join(HERE, `${NAME}.css`), css);
writeFileSync(join(HERE, `${NAME}.pose.js`), pose);
const anchors = {
  note: [NOTE.x + NOTE.w / 2, NOTE.y + NOTE.d, TZ + 4],
  slip0: [slipX(0) + SL.w / 2, SY + SL.d, TZ + SL.t],
  slip3: [slipX(3) + SL.w / 2, SY + SL.d, TZ + SL.t],
  slip7: [slipX(7) + SL.w / 2, SY + SL.d, TZ + SL.t],
  mid: [(slipX(2) + slipX(5) + SL.w) / 2, SY + SL.d / 2, TZ + SL.t],
  head0: [HX0, ARM_Y1, RAIL_Z],
  stop: [STOP.x + STOP.w / 2, STOP.y + STOP.d, TZ + 10],
  ruler: [0, TRAY.y + TRAY.d, Z0 + TRAY_H],
  tray: [0, TRAY.y + TRAY.d / 2, TZ],
};
writeFileSync(join(HERE, `${NAME}.json`), JSON.stringify({ width: WIDTH, height: HEIGHT,
  params: {
    msgs: "0..8 message slips land on the tray in order, left to right (slip i shows when msgs > i; 0, 2, 4, 6 are blue: the user)",
    scan: "0..1 the reading head sweeps from the note holder (0) to the last slip slot (1); slip i sits at (i + 1) / 8 of the sweep",
    read: "0..1 the lens lights yellow and a beam falls on the slip (or note) under the head",
    note: "0..1 the yellow memory note drops into the holder at the head of the tray",
    lit: "0..1 the first slip (the one that says the dog's name) turns yellow",
    mid: "0..1 slips 2..5 fade to 20 % (read worst in the middle)",
  },
  anchors: Object.fromEntries(Object.entries(anchors).map(([n, p]) => [n, at(p).map(r1)])) }, null, 1));
console.log("wrote", NAME, svg.length, "bytes", WIDTH, "x", HEIGHT, "scale", P.scale.toFixed(3));

if (process.argv.includes("--preview")) {
  const t = Number(process.argv[process.argv.indexOf("--preview") + 1]) || 0;
  const st = { msgs: 0, scan: 0, read: 0, note: 0, lit: 0, mid: 0 };
  const args = process.argv.find((a) => a.startsWith("--state="));
  if (args) Object.assign(st, JSON.parse(args.slice(8)));
  const vars = "--anatomy-paper:#FFFFFF;--anatomy-face:#FFFFFF;--anatomy-top:#FFFFFF;--anatomy-shade-0:#C4BAA6;--anatomy-shade-1:#D4CBB9;--anatomy-shade-2:#E3DCCD;--anatomy-shade-3:#F1ECE2;--anatomy-hi:#121212;--anatomy-mid:#3D3932;--anatomy-lo:#5A554B;--anatomy-faint:#B3AA98;--anatomy-lit:#121212;--anatomy-lit-top:#FFD23F;--anatomy-lit-shade:#F0B90F;--anatomy-halo:#6F6552;--anatomy-halo-opacity:.30;--anatomy-dot:#121212;--anatomy-weight:3.2px;--anatomy-red:#D7392B;--anatomy-green:#13965A;--anatomy-blue:#2C5BEA";
  const page = `<!doctype html><html><head><meta charset="utf-8"><style>${css}body{margin:0;background:#F4EFE4}.an{width:860px;margin:20px auto;${vars}}</style></head><body><div class="an iso" data-theme="dark" id="f">${svg}</div><script>window.__ANP={};${pose};window.__ANP["${NAME}"].apply(document.querySelector("svg"),${JSON.stringify(st)},${t});</script></body></html>`;
  writeFileSync(join(HERE, "preview.html"), page);
  console.log("preview.html");
}
