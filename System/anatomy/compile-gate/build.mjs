// Compile gate: the compiler as an inspection station on a production line. A press on the left (the model) stamps a
// code block (a yellow part with three engraved rule lines) onto a belt. The belt carries it under a gate (the compiler):
// a feeler on the crossbar drops onto the part. A pass lights the green lamp and the part rides on into the done tray; a
// fail lights the red lamp, a kicker on the front pushes the part off the belt onto a return chute behind it, and the
// chute runs it back to the press (the error message fed back to the model for another try).
// Schematic, not to scale.
// node build.mjs [--preview [t]] [--state='{"feed":1}']  ->  compile-gate.svg  .json  .css  .pose.js  (+ preview.html)
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../../../.claude/skills/anatomy/kit/iso-kit.mjs";
import * as G from "../../../.claude/skills/anatomy/kit/lathe.mjs";
import { kitScript } from "../../../.claude/skills/anatomy/scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const NAME = "compile-gate";
const WIDTH = 600;

// ---- world (x, y floor; z up). The line runs along +x; fronts face +y.
const BASE = { x: -300, y: -128, w: 600, d: 236, r: 8 }, BASE_H = 12;
const Z0 = BASE_H;
const PRESS = { x: -290, y: -66, w: 82, d: 86, r: 3 }, PRESS_H = 104;
const BELT = { x: -206, y: -42, w: 380, d: 44 }, BELT_Z = Z0 + 34;          // belt top
const RAIL_D = 6;
const CHUTE = { x: -206, y: -104, w: 270, d: 40 }, CHUTE_Z = Z0 + 10;       // the return trough behind the belt
const GATE_X = 4, POST = 12, GB = -118, GF = 14, BAR_Z = Z0 + 132;           // one gate post at y GB (behind the chute); the bar reaches over the belt
const PART = { w: 44, d: 32, h: 14 };
const PY = BELT.y + (BELT.d - PART.d) / 2;                                   // part y on the belt
const RY = CHUTE.y + (CHUTE.d - PART.d) / 2;                                 // part y on the chute
const X0 = BELT.x + 6, XG = GATE_X + POST / 2 - PART.w / 2;                  // part x at the press, under the gate
const TRAY = { x: 196, y: -54, w: 86, d: 68 }, TRAY_H = 22, TRAY_Z = Z0;
const XT = TRAY.x + (TRAY.w - PART.w) / 2, YT = TRAY.y + (TRAY.d - PART.d) / 2;
const KICK = { x: GATE_X + 26, w: 30 };                                      // the kicker beside the belt's front, past the gate

const EXTREMES = [...k.boxCorners(BASE, 0, BASE_H), ...k.boxCorners(PRESS, 0, Z0 + PRESS_H + 8),
  ...k.boxCorners({ x: GATE_X, y: GB, w: POST, d: GF + POST - GB }, 0, BAR_Z + 34)];
const VIEW = { azimuth: 50, elevation: 42 };
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
const bar = (x0, x1, y, z, h = 2.2) => poly([[x0, y - h, z], [x1, y - h, z], [x1, y + h, z], [x0, y + h, z]], "cg-ink");
const face = (X, y0, y1, z0, z1, cls) => poly([[X, y0, z0], [X, y1, z0], [X, y1, z1], [X, y0, z1]], cls);

// ---- parts
function base() {
  const o = [slab(BASE, 0, BASE_H, { crease: "none" })];
  for (const [x, y] of [[BASE.x + 12, BASE.y + 12], [BASE.x + BASE.w - 12, BASE.y + 12], [BASE.x + 12, BASE.y + BASE.d - 12], [BASE.x + BASE.w - 12, BASE.y + BASE.d - 12]])
    o.push(screw(x, y, Z0));
  const y0 = BASE.y + BASE.d - 40, x0 = BASE.x + 30;
  o.push(slab({ x: x0, y: y0, w: 96, d: 28, r: 2 }, Z0, 1.6, { crease: "none" }));
  for (const [i, e] of [[0, 0], [1, 20], [2, 36]]) o.push(bar(x0 + 10, x0 + 86 - e, y0 + 7 + i * 7, Z0 + 1.6, 1.4));
  return o.join("");
}
function postSvg(y) {
  return slab({ x: GATE_X - 5, y: y - 5, w: POST + 10, d: POST + 10, r: 2 }, Z0, 6) + slab({ x: GATE_X, y, w: POST, d: POST, r: 1 }, Z0 + 6, BAR_Z - Z0 - 6);
}
function press() {
  const o = [], X = PRESS.x + PRESS.w;
  o.push(slab({ x: PRESS.x - 4, y: PRESS.y - 4, w: PRESS.w + 8, d: PRESS.d + 8, r: 3 }, Z0, 8));
  o.push(slab(PRESS, Z0 + 8, PRESS_H - 8, { crease: "none" }));
  o.push(slab({ x: PRESS.x - 3, y: PRESS.y - 3, w: PRESS.w + 6, d: PRESS.d + 6, r: 2 }, Z0 + PRESS_H, 6));
  // a hopper on top, a ram column and its head over the slot
  o.push(slab({ x: PRESS.x + 14, y: PRESS.y + 16, w: 40, d: 40, r: 3 }, Z0 + PRESS_H + 6, 22));
  o.push(slab({ x: PRESS.x + 10, y: PRESS.y + 12, w: 48, d: 48, r: 3 }, Z0 + PRESS_H + 28, 5));
  // the output slot on the +x face at belt height, and a vent row above it
  o.push(face(X, PY - 3, PY + PART.d + 3, BELT_Z - 1, BELT_Z + PART.h + 4, "cg-slot"));
  for (let i = 0; i < 4; i++) { const y0 = PRESS.y + 12 + i * 16; o.push(face(X, y0, y0 + 6, Z0 + 70, Z0 + 92, "cg-slot")); }
  // a label plate on the front face
  const Y = PRESS.y + PRESS.d;
  o.push(poly([[PRESS.x + 12, Y, Z0 + 30], [PRESS.x + PRESS.w - 12, Y, Z0 + 30], [PRESS.x + PRESS.w - 12, Y, Z0 + 56], [PRESS.x + 12, Y, Z0 + 56]], "cg-plate"));
  for (const [z, e] of [[Z0 + 38, 0], [Z0 + 47, 18]]) o.push(poly([[PRESS.x + 18, Y, z - 1.5], [PRESS.x + PRESS.w - 18 - e, Y, z - 1.5], [PRESS.x + PRESS.w - 18 - e, Y, z + 1.5], [PRESS.x + 18, Y, z + 1.5]], "cg-ink"));
  return o.join("");
}
function chute() {
  const o = [], C = CHUTE;
  o.push(slab({ x: C.x, y: C.y, w: C.w, d: C.d, r: 2 }, CHUTE_Z, 4, { crease: "none", className: "cg-k" }));
  o.push(slab({ x: C.x, y: C.y - 4, w: C.w, d: 4, r: 1 }, CHUTE_Z, 12));
  for (const x of [C.x + 30, C.x + C.w - 30]) o.push(slab({ x: x - 4, y: C.y + 4, w: 8, d: C.d - 8, r: 1 }, Z0, CHUTE_Z - Z0));
  // arrows engraved on the floor, pointing back to the press
  for (const x0 of [C.x + 60, C.x + 140, C.x + 220]) {
    const yc = C.y + C.d / 2, z = CHUTE_Z + 4;
    o.push(poly([[x0, yc, z], [x0 + 14, yc - 7, z], [x0 + 14, yc - 2.5, z], [x0 + 26, yc - 2.5, z], [x0 + 26, yc + 2.5, z], [x0 + 14, yc + 2.5, z], [x0 + 14, yc + 7, z]], "cg-red"));
  }
  return o.join("");
}
function chuteFront() {
  const C = CHUTE;
  return slab({ x: C.x, y: C.y + C.d, w: C.w, d: 4, r: 1 }, CHUTE_Z, 12);
}
function belt() {
  const o = [], B = BELT, zb = BELT_Z - 10;
  for (const x of [B.x + 16, B.x + B.w - 24]) for (const y of [B.y - RAIL_D, B.y + B.d]) o.push(slab({ x, y, w: 8, d: RAIL_D, r: 1 }, Z0, zb - Z0));
  o.push(slab({ x: B.x, y: B.y - RAIL_D, w: B.w, d: RAIL_D, r: 1 }, zb, 14));
  o.push(slab({ x: B.x, y: B.y, w: B.w, d: B.d, r: 3 }, zb + 4, 6, { crease: "none", className: "cg-k" }));
  // belt slats
  for (let x = B.x + 12; x < B.x + B.w - 8; x += 16) o.push(bar(x, x + 2.4, B.y + B.d / 2, BELT_Z, B.d / 2 - 3));
  return o.join("");
}
function beltFront() {
  const B = BELT, zb = BELT_Z - 10, o = [slab({ x: B.x, y: B.y + B.d, w: B.w, d: RAIL_D, r: 1 }, zb, 14)];
  for (let x = B.x + 30; x < B.x + B.w - 20; x += 60) o.push(screw(x, B.y + B.d + RAIL_D / 2, zb + 14));
  return o.join("");
}
function tray() {
  const T = TRAY, o = [];
  o.push(slab({ x: T.x, y: T.y, w: T.w, d: T.d, r: 3 }, TRAY_Z, 4, { crease: "none", className: "cg-g2" }));
  o.push(slab({ x: T.x, y: T.y, w: T.w, d: 5, r: 1 }, TRAY_Z + 4, TRAY_H - 4));
  o.push(slab({ x: T.x, y: T.y, w: 5, d: T.d, r: 1 }, TRAY_Z + 4, TRAY_H - 4));
  return o.join("");
}
function trayFront() {
  const T = TRAY;
  return slab({ x: T.x + T.w - 5, y: T.y, w: 5, d: T.d, r: 1 }, TRAY_Z + 4, TRAY_H - 4) + slab({ x: T.x, y: T.y + T.d - 5, w: T.w, d: 5, r: 1 }, TRAY_Z + 4, TRAY_H - 4);
}
// a code block: a part with three engraved rule lines; cls tints it (yellow: fresh, green: passed, red: rejected)
function partSvg(x, y, z, cls) {
  const t = z + PART.h, o = [S(k.slabOf({ x, y, w: PART.w, d: PART.d, r: 2 }, z, PART.h, P, 3), { tone: "hi", crease: "none", className: cls })];
  for (const [dy, e] of [[6, 0], [12, 8], [18, 4]]) o.push(poly([[x + 5, y + dy, t], [x + PART.w - 5 - e, y + dy, t], [x + PART.w - 5 - e, y + dy + 2.6, t], [x + 5, y + dy + 2.6, t]], "cg-ink"));
  return o.join("");
}
const tinted = (x, y, z, id) => `<g data-part="${id}">${partSvg(x, y, z, "cg-y")}<g data-part="${id}-ok" style="opacity:0">${partSvg(x, y, z, "cg-g")}</g><g data-part="${id}-bad" style="opacity:0">${partSvg(x, y, z, "cg-r")}</g></g>`;
function stack() {
  const o = [];
  for (let i = 0; i < 3; i++) o.push(`<g data-part="done-${i}" style="opacity:0">${partSvg(XT, YT, TRAY_Z + 4 + i * (PART.h + 1), "cg-g")}</g>`);
  return o.join("");
}
function kicker() {
  const o = [], y = BELT.y + BELT.d + RAIL_D;
  o.push(slab({ x: KICK.x - 4, y, w: KICK.w + 8, d: 22, r: 2 }, Z0, BELT_Z + 8 - Z0));
  return o.join("");
}
// the kicker's paddle, built retracted (flush with the front rail) and pushed along -y by the pose
const paddleSvg = () => slab({ x: KICK.x, y: BELT.y + BELT.d - 2, w: KICK.w, d: 6, r: 1 }, BELT_Z + 1, PART.h + 4);
function crossbar() {
  const o = [];
  o.push(slab({ x: GATE_X - 4, y: GB - 4, w: POST + 8, d: BELT.y + BELT.d - GB + 4, r: 2 }, BAR_Z, 14));
  o.push(slab({ x: GATE_X - 6, y: GB - 6, w: POST + 12, d: 26, r: 2 }, BAR_Z - 22, 22));
  // two lamps on the bar: green over the belt's back, red behind it
  for (const [y, id] of [[-62, "lamp-ok"], [-92, "lamp-bad"]]) {
    const cx = GATE_X + POST / 2, F = G.frameAlong([cx, y, BAR_Z + 14], [0, 0, 1]);
    o.push(S(k.cylinder(cx, y, 9, BAR_Z + 14, 4, P, 28), { tone: "hi", crease: "none" }));
    const mer = [[0, 0], [0, 8]]; for (let i = 1; i < 8; i++) { const b = (i / 8) * Math.PI / 2; mer.push([8 * Math.sin(b), 8 * Math.cos(b), 1]); } mer.push([8, 0]);
    const dome = (cls) => S(G.lathe(mer, G.frameAlong([cx, y, BAR_Z + 18], [0, 0, 1]), P, { steps: 40 }), { tone: "hi", crease: "none", ...(cls ? { className: cls } : {}) });
    o.push(dome(), `<g data-part="${id}" style="opacity:0">${dome(id === "lamp-ok" ? "cg-g" : "cg-r")}</g>`);
  }
  return o.join("");
}
// the feeler: a guide block on the bar and a plunger with a foot, built up (z offset 0) and lowered by the pose
const FEEL_Y = PY + PART.d / 2;
function feelerSvg() {
  const cx = GATE_X + POST / 2, o = [];
  o.push(S(k.cylinder(cx, FEEL_Y, 3.4, BELT_Z + PART.h + 34, BAR_Z - (BELT_Z + PART.h + 34), P, 20), { tone: "hi", crease: "none" }));
  o.push(slab({ x: cx - 12, y: FEEL_Y - 10, w: 24, d: 20, r: 2 }, BELT_Z + PART.h + 28, 6));
  o.push(`<g data-part="probe" style="opacity:0">${slab({ x: cx - 12, y: FEEL_Y - 10, w: 24, d: 20, r: 2 }, BELT_Z + PART.h + 28, 6, { className: "cg-y" })}</g>`);
  return o.join("");
}
const guide = () => slab({ x: GATE_X - 6, y: FEEL_Y - 9, w: POST + 12, d: 18, r: 2 }, BAR_Z - 16, 16);

const body = [
  base(),
  postSvg(GB),
  press(),
  chute(),
  `<g data-part="ret">${tinted(XG, RY, CHUTE_Z + 4, "rp")}</g>`,
  chuteFront(),
  belt(),
  tray(),
  stack(),
  `<g data-part="mv">${tinted(X0, PY, BELT_Z, "mp")}</g>`,
  `<g data-part="paddle">${paddleSvg()}</g>`,
  beltFront(),
  trayFront(),
  kicker(),
  `<g data-part="feeler">${feelerSvg()}</g>`,
  guide(),
  crossbar(),
].join("");

const svg = k.figureSvg({
  width: WIDTH, height: HEIGHT,
  label: "A compile gate: a press on the left stamps a yellow code block onto a belt. The belt carries it under a gate whose feeler drops onto the part. A pass lights a green lamp and the part rides on into a done tray; a fail lights a red lamp and a kicker pushes the part onto a return chute behind the belt, back to the press.",
  body: [body],
});

const tint = (cls, c, shade = 80) => {
  const mix = (p, w) => `color-mix(in srgb, ${c} ${p}%, ${w})`;
  const tones = [mix(62, "#000"), mix(shade, "#000"), c, c];
  const sel = `.iso .iso-solid.${cls}`;
  return `${sel}>.iso-fill,${sel}>.iso-top{fill:${c};stroke:var(--anatomy-hi)}\n` + tones.map((t, i) => `${sel}>.iso-shade[data-shade="${i}"]{fill:${t};stroke:${t}}`).join("\n") + "\n";
};
const flat = (cls, fill) => `.${cls}{fill:${fill};stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}\n`;
const css = k.ISO_CSS + tint("cg-r", "var(--anatomy-red)") + tint("cg-g", "var(--anatomy-green)") + tint("cg-k", "var(--anatomy-shade-2)", 90)
  + tint("cg-g2", "#CFEBDD", 90) + `
.iso .iso-solid.cg-y>.iso-fill,.iso .iso-solid.cg-y>.iso-top{fill:var(--anatomy-lit-top);stroke:var(--anatomy-hi)}
.iso .iso-solid.cg-y>.iso-shade{fill:var(--anatomy-lit-shade);stroke:var(--anatomy-lit-shade)}
.cg-ink{fill:var(--anatomy-hi);stroke:none}
.cg-red{fill:var(--anatomy-red);stroke:none}
` + flat("cg-slot", "var(--anatomy-mid)") + flat("cg-plate", "var(--anatomy-shade-3)");

const pose = (kitScript() + `
const P = ${JSON.stringify(P)};
const X0 = ${X0}, XG = ${XG}, XT = ${XT}, YT = ${YT}, PY = ${PY}, RY = ${RY}, BZ = ${BELT_Z}, CZ = ${CHUTE_Z + 4}, TZ = ${TRAY_Z + 4}, H = ${PART.h};
const DROP = ${BELT_Z + PART.h + 28 - (BELT_Z + PART.h + 2)}, KICK_Y = ${PY - RY};
const q = {};
const part = (svg, n) => (q[n] = q[n] && svg.contains(q[n]) ? q[n] : svg.querySelector('[data-part="' + n + '"]'));
const cl = (u) => Math.min(1, Math.max(0, u));
const sm = (u) => { u = cl(u); return u * u * (3 - 2 * u); };
const op = (el, v) => { el.style.opacity = v <= 0.001 ? "0" : v >= 0.999 ? "1" : v.toFixed(3); };
window.__ANP[${JSON.stringify(NAME)}] = {
  init: { feed: 0, check: 0, ok: 0, bad: 0, count: 0, part: 1 },
  apply(svg, s, t) {
    // feed: the part leaves the press and rides the belt to the gate; ok: it rides on and drops into the tray
    const f = sm(s.feed), g = sm(s.ok), b = cl(s.bad);
    let x = X0 + (XG - X0) * f, dz = 0;
    if (g > 0) { const u = sm(g / 0.75), w = sm((g - 0.75) / 0.25); x = XG + (XT - XG) * u; dz = (TZ + s.count * (H + 1) - BZ) * w; }
    // bad: the kicker pushes it off the back of the belt (first 35 %), then the chute carries it back to the press
    const k1 = sm(b / 0.35), k2 = sm((b - 0.35) / 0.65), onChute = b > 0.35;
    part(svg, "mv").setAttribute("transform", translateAlong(P, [x - X0, -KICK_Y * k1, (CZ - BZ) * k1 * 0.6 + dz]));
    op(part(svg, "mv"), (onChute ? 0 : 1) * cl(s.part));
    part(svg, "ret").setAttribute("transform", translateAlong(P, [(X0 - XG) * k2, 0, 0]));
    op(part(svg, "ret"), onChute ? cl(s.part) * (1 - sm((b - 0.92) / 0.08)) : 0);
    part(svg, "paddle").setAttribute("transform", translateAlong(P, [0, -KICK_Y * (b > 0 && b < 0.6 ? Math.sin(Math.PI * cl(b / 0.5)) : 0), 0]));
    // check: the feeler drops onto the part and lights; the lamps and the part's tint follow the verdict
    part(svg, "feeler").setAttribute("transform", translateAlong(P, [0, 0, -DROP * Math.sin(Math.PI * cl(s.check))]));
    op(part(svg, "probe"), Math.sin(Math.PI * cl(s.check)));
    const okL = sm(s.ok / 0.15), badL = sm(s.bad / 0.12);
    op(part(svg, "lamp-ok"), okL * (1 - badL)); op(part(svg, "lamp-bad"), badL);
    for (const id of ["mp", "rp"]) { op(part(svg, id + "-ok"), okL * (1 - badL)); op(part(svg, id + "-bad"), badL); }
    for (let i = 0; i < 3; i++) op(part(svg, "done-" + i), cl(s.count - i));
  },
};
`).replaceAll("<script", "<\\u0073cript").replaceAll("</script", "<\\/script");

writeFileSync(join(HERE, `${NAME}.svg`), svg);
writeFileSync(join(HERE, `${NAME}.css`), css);
writeFileSync(join(HERE, `${NAME}.pose.js`), pose);
const anchors = {
  press: [PRESS.x + PRESS.w, PRESS.y + PRESS.d / 2, Z0 + 60],
  gate: [GATE_X + POST / 2, FEEL_Y, BELT_Z + PART.h],
  part0: [X0 + PART.w / 2, PY + PART.d, BELT_Z + PART.h],
  lamps: [GATE_X + POST / 2, -77, BAR_Z + 26],
  chute: [CHUTE.x + CHUTE.w / 2, CHUTE.y, CHUTE_Z + 8],
  tray: [TRAY.x + TRAY.w / 2, TRAY.y + TRAY.d, TRAY_Z + TRAY_H],
  belt: [0, BELT.y + BELT.d / 2, BELT_Z],
};
writeFileSync(join(HERE, `${NAME}.json`), JSON.stringify({ width: WIDTH, height: HEIGHT,
  params: {
    feed: "0..1 the code block leaves the press and rides the belt to the gate",
    check: "0..1 the feeler drops onto the part and lifts again (lit while down)",
    ok: "0..1 green lamp, the part turns green and rides on into the tray (lands on top of `count` parts)",
    bad: "0..1 red lamp, the part turns red; the kicker pushes it onto the return chute (to 0.35) and the chute carries it back to the press",
    count: "0..3 green parts already in the done tray",
    part: "0..1 the moving part shows (0 hides it: an empty line)",
  },
  anchors: Object.fromEntries(Object.entries(anchors).map(([n, p]) => [n, at(p).map(r1)])) }, null, 1));
console.log("wrote", NAME, svg.length, "bytes", WIDTH, "x", HEIGHT, "scale", P.scale.toFixed(3));

if (process.argv.includes("--preview")) {
  const t = Number(process.argv[process.argv.indexOf("--preview") + 1]) || 0;
  const st = { feed: 0, check: 0, ok: 0, bad: 0, count: 0, part: 1 };
  const args = process.argv.find((a) => a.startsWith("--state="));
  if (args) Object.assign(st, JSON.parse(args.slice(8)));
  const vars = "--anatomy-paper:#FFFFFF;--anatomy-face:#FFFFFF;--anatomy-top:#FFFFFF;--anatomy-shade-0:#C4BAA6;--anatomy-shade-1:#D4CBB9;--anatomy-shade-2:#E3DCCD;--anatomy-shade-3:#F1ECE2;--anatomy-hi:#121212;--anatomy-mid:#3D3932;--anatomy-lo:#5A554B;--anatomy-faint:#B3AA98;--anatomy-lit:#121212;--anatomy-lit-top:#FFD23F;--anatomy-lit-shade:#F0B90F;--anatomy-halo:#6F6552;--anatomy-halo-opacity:.30;--anatomy-dot:#121212;--anatomy-weight:3.2px;--anatomy-red:#D7392B;--anatomy-green:#13965A;--anatomy-blue:#2C5BEA";
  const page = `<!doctype html><html><head><meta charset="utf-8"><style>${css}body{margin:0;background:#F4EFE4}.an{width:860px;margin:20px auto;${vars}}</style></head><body><div class="an iso" data-theme="dark" id="f">${svg}</div><script>window.__ANP={};${pose};window.__ANP["${NAME}"].apply(document.querySelector("svg"),${JSON.stringify(st)},${t});</script></body></html>`;
  writeFileSync(join(HERE, "preview.html"), page);
  console.log("preview.html");
}
