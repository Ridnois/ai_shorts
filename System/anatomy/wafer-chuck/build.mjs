// Wafer chuck: a plasma-etch pedestal where helium under the wafer carries the heat away (schematic, not to scale).
// node build.mjs [--preview]  ->  wafer-chuck.svg  .json  .css  .pose.js  (+ preview.html with --preview)
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../../../.claude/skills/anatomy/kit/iso-kit.mjs";
import { kitScript } from "../../../.claude/skills/anatomy/scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const NAME = "wafer-chuck";
const WIDTH = 600, HEIGHT = 470;

// ---- world (x, y floor; z up). About 2 mm a unit: the wafer is 70 units in radius.
const PLATE = { x: -140, y: -290, w: 280, d: 480, r: 10 };
const PLATE_H = 10, FOOT_H = 5;
const WAFER_R = 70, WAFER_H = 1.8;
const CHUCK_R = 76, CHUCK_Z = 58, CHUCK_H = 10, CHUCK_TOP = CHUCK_Z + CHUCK_H;     // 68
const RAISE = 22, SLIDE = 172;                           // lift 0..0.3 raises the wafer on its pins, then it slides out along -y
const SHOWER_Z = 168, SHOWER_H = 10;
const POSTS = [[-112, -112], [112, -112], [-112, 112], [112, 112]];
const FRAME_Z = 150;
const MFC = { x: 76, y: 124, w: 46, d: 40, r: 4 }, MFC_H = 36;
const TANK = [-92, 150], TANK_R = 17, TANK_TOP = 100;
const DUCT_Z = 30;
// the helium line, as a 3D route: tank valve -> over -> down into the controller -> out along the floor into the pedestal
const ROUTE = [[TANK[0], TANK[1], 126], [TANK[0], 144, 126], [MFC.x + 14, 144, 126], [MFC.x + 14, 144, MFC_H], [MFC.x + 14, 144, MFC_H],
  [MFC.x + 14, 100, DUCT_Z], [30, 100, DUCT_Z], [30, 0, DUCT_Z]];
// simplified: the controller outlet is on its back face at z = DUCT_Z, so the last legs run along the floor
const ROUTE2 = [[MFC.x + 14, 144, MFC_H], [MFC.x + 14, 144, DUCT_Z]];

const P = k.fitProjection(
  [...k.boxCorners(PLATE, -PLATE_H - FOOT_H, 0), [0, 0, SHOWER_Z + SHOWER_H + 60], [TANK[0], TANK[1], 130], [0, -SLIDE, CHUCK_TOP + RAISE + 6], [0, -SLIDE - WAFER_R, CHUCK_TOP], [0, 0, CHUCK_TOP + RAISE + 6]],
  WIDTH, HEIGHT, { pad: 14, azimuth: 40, elevation: 30 });

const at = (p) => k.iso(p, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (pts, style) => k.dotsSvg(pts, style);
const byDepth = (pts) => [...pts].sort((a, b) => k.depthOf([a[0], a[1], 0], P) - k.depthOf([b[0], b[1], 0], P));
const bar = (x0, y0, x1, y1, z, t = 5, h = 5) => ({ x: Math.min(x0, x1) - (x0 === x1 ? t / 2 : 0), y: Math.min(y0, y1) - (y0 === y1 ? t / 2 : 0),
  w: Math.abs(x1 - x0) + (x0 === x1 ? t : 0), d: Math.abs(y1 - y0) + (y0 === y1 ? t : 0), r: 1.2, z, h });

// ---- parts, back to front
function floor() {
  const o = [`<path class="iso-halo" d="${k.haloOf(PLATE, -PLATE_H - FOOT_H, PLATE_H, P)}"/>`];
  for (const [x, y] of byDepth(k.corners(PLATE, 22))) {
    o.push(S(k.cylinder(x, y, 7, -PLATE_H - FOOT_H, 1.6, P, 24), { tone: "lo" }));
    o.push(S(k.cylinder(x, y, 5.4, -PLATE_H - FOOT_H + 1.6, FOOT_H - 1.6, P, 24), { tone: "mid" }));
  }
  o.push(S(k.slabOf(PLATE, -PLATE_H, PLATE_H, P, 8, 1.6), { tone: "mid" }));
  o.push(L(k.planOutline(k.insetPlan(PLATE, 5), 0, P), { tone: "lo" }));
  const screws = k.corners(PLATE, 11);
  o.push(L(screws.map(([x, y]) => k.ring(x, y, 2.2, 0, P, 16)).join(""), { tone: "lo" }));
  o.push(D(screws.map(([x, y]) => at([x, y, 0])), { size: 1.1 }));
  const strip = { x: -118, y: PLATE.y + 10, w: 236, d: 7, r: 1 };               // ruler strip along the back edge
  o.push(S(k.slabOf(strip, 0, 0.6, P, 3), { tone: "lo", crease: "none" }));
  const t = k.topTicks(strip.x + 4, strip.x + strip.w - 4, 4, 5, strip.y + 0.8, 0.6, [2, 3.6], P);
  o.push(L(t.minor, { tone: "lo" }), L(t.major, { tone: "mid" }));
  const plate = { x: -118, y: PLATE.y + PLATE.d - 24, w: 62, d: 14, r: 2 };    // label plate with three rule lines
  o.push(S(k.slabOf(plate, 0, 0.8, P, 3), { tone: "lo", crease: "none" }));
  for (const dy of [3.5, 7, 10.5]) o.push(L(k.lineOnTop([plate.x + 5, plate.y + dy], [plate.x + plate.w - (dy === 10.5 ? 24 : 6), plate.y + dy], 0.8, P), { tone: "faint", free: true }));
  return o.join("");
}

function post(x, y) {
  const o = [S(k.cylinder(x, y, 9, 0, 6, P, 24), { tone: "lo" }), S(k.cylinder(x, y, 4.6, 6, FRAME_Z - 6, P, 22), { tone: "mid", crease: "none" })];
  o.push(L([30, 72, 112].map((z) => k.sideArc(x, y, 4.6, z, P, 12)).join(""), { tone: "faint" }));
  o.push(S(k.cylinder(x, y, 7, FRAME_Z - 2, 8, P, 24), { tone: "mid" }));
  o.push(D([at([x, y, FRAME_Z + 6])], { size: 0.9, tone: "hi" }));
  return o.join("");
}
const frameBar = (a, b) => S(k.slabOf(bar(a[0], a[1], b[0], b[1], FRAME_Z, 7, 6), FRAME_Z, 6, P, 3, 0.5), { tone: "mid" });

function pedestal() {
  const o = [];
  o.push(S(k.cylinder(0, 0, 86, 0, 8, P, 72, 0.8), { tone: "lo" }));                        // base flange
  o.push(L(k.ring(0, 0, 80, 8, P, 64), { tone: "lo" }));
  o.push(D(Array.from({ length: 8 }, (_, i) => { const a = i * Math.PI / 4 + 0.39; return at([Math.cos(a) * 82, Math.sin(a) * 82, 8]); }), { size: 1 }));
  o.push(S(k.cylinder(0, 0, 64, 8, CHUCK_Z - 8, P, 64), { tone: "mid" }));                   // column
  o.push(L([20, 38].map((z) => k.sideArc(0, 0, 64, z, P, 40)).join(""), { tone: "faint" }));
  o.push(S(k.cylinder(0, 0, 69, 24, 8, P, 64, 0.5), { tone: "hi" }));                        // coolant manifold ring
  o.push(L(k.knurl(0, 0, 69, 24, 32, 56, P, 0.3), { tone: "lo" }));
  // coolant ports: two short stubs on the manifold, drawn as slabs along x
  for (const [y, tone] of [[-18, "blue"], [18, "mid"]]) {
    const stub = { x: -80, y: y - 4, w: 14, d: 8, r: 2, tone };
    o.push(S(k.slabOf(stub, 25, 6, P, 3, 0.4), { tone: "mid" }));
    o.push(L(k.ring(-80 + 0.2, y, 2.6, 28, P, 12), { tone: "lo" }));
  }
  o.push(S(k.cylinder(0, 0, 80, CHUCK_Z - 4, 4, P, 64), { tone: "lo" }));                    // edge ring under the wafer
  o.push(S(k.cylinder(0, 0, CHUCK_R, CHUCK_Z, CHUCK_H, P, 64, 0.8), { tone: "hi", crease: "lo" }));   // ceramic chuck
  // helium channels on the chuck face: three rings and eight spokes; the dots of the gas travel in them
  o.push(L([22, 44, 66].map((r) => k.ring(0, 0, r, CHUCK_TOP, P, 64)).join(""), { tone: "mid" }));
  o.push(L(Array.from({ length: 8 }, (_, i) => { const a = i * Math.PI / 4; return k.lineOnTop([Math.cos(a) * 6, Math.sin(a) * 6], [Math.cos(a) * 66, Math.sin(a) * 66], CHUCK_TOP, P); }).join(""), { tone: "mid" }));
  o.push(L(k.ring(0, 0, CHUCK_R - 3, CHUCK_TOP, P, 64), { tone: "faint" }));
  o.push(L(k.ring(0, 0, 4, CHUCK_TOP, P, 20), { tone: "hi" }));                              // the helium inlet
  // pins around the rim (lift pins parked in their holes)
  o.push(D([0, 1, 2].map((i) => { const a = Math.PI * 0.55 + i * 2.094; return at([Math.cos(a) * 52, Math.sin(a) * 52, CHUCK_TOP]); }), { size: 1.1, tone: "hi" }));
  return o.join("");
}

function wafer() {
  const o = [`<path class="iso-halo" d="${k.haloOf({ x: -WAFER_R, y: -WAFER_R, w: WAFER_R * 2, d: WAFER_R * 2, r: WAFER_R }, 0, 1, P)}" style="filter:blur(5px)"/>`];
  o.push(S(k.cylinder(0, 0, WAFER_R, 0, WAFER_H, P, 72, 0.4), { tone: "hi" }));
  o.push(`<path data-part="heat" class="an-heat" d="${k.ring(0, 0, WAFER_R - 0.4, WAFER_H, P, 72)}Z" style="fill-opacity:0"/>`);
  o.push(L(k.ring(0, 0, WAFER_R - 4, WAFER_H, P, 72), { tone: "faint" }));
  o.push(L(k.lineOnTop([-WAFER_R, 0], [-WAFER_R + 5, 0], WAFER_H, P), { tone: "hi" }));      // the notch
  const die = [];                                                                         // a grid of dies
  for (let i = -4; i <= 4; i++) { const e = Math.sqrt(66 * 66 - (i * 13) ** 2); die.push(k.lineOnTop([i * 13, -e], [i * 13, e], WAFER_H, P)); die.push(k.lineOnTop([-e, i * 13], [e, i * 13], WAFER_H, P)); }
  o.push(`<g data-part="dies">${L(die.join(""), { tone: "faint" })}</g>`);
  return o.join("");
}

function showerhead() {
  const o = [];
  o.push(S(k.cylinder(0, 0, 82, SHOWER_Z, SHOWER_H, P, 72, 0.8), { tone: "mid" }));
  o.push(L(k.ring(0, 0, 76, SHOWER_Z + SHOWER_H, P, 64), { tone: "lo" }));
  const holes = [];
  for (let r = 18; r <= 66; r += 16) for (let i = 0; i < Math.round(r / 5); i++) { const a = (i / Math.round(r / 5)) * Math.PI * 2; holes.push(at([Math.cos(a) * r, Math.sin(a) * r, SHOWER_Z + SHOWER_H])); }
  o.push(D(holes, { size: 0.9, tone: "hi" }));
  o.push(S(k.cylinder(0, 0, 16, SHOWER_Z + SHOWER_H, 40, P, 32), { tone: "mid" }));            // RF stem
  o.push(L([SHOWER_Z + 24, SHOWER_Z + 38].map((z) => k.sideArc(0, 0, 16, z, P, 20)).join(""), { tone: "faint" }));
  o.push(S(k.cylinder(0, 0, 10, SHOWER_Z + SHOWER_H + 40, 14, P, 24), { tone: "hi" }));
  o.push(L(k.knurl(0, 0, 10, SHOWER_Z + SHOWER_H + 40, SHOWER_Z + SHOWER_H + 54, 24, P, 0.3), { tone: "lo" }));
  o.push(D([at([0, 0, SHOWER_Z + SHOWER_H + 54])], { size: 1.2, tone: "hi" }));
  return o.join("");
}

function tank() {
  const [x, y] = TANK, o = [];
  o.push(`<path class="iso-halo" d="${k.haloOf({ x: x - TANK_R, y: y - TANK_R, w: TANK_R * 2, d: TANK_R * 2, r: TANK_R }, 0, 1, P)}"/>`);
  o.push(S(k.cylinder(x, y, TANK_R + 2, 0, 6, P, 32), { tone: "lo" }));
  o.push(S(k.cylinder(x, y, TANK_R, 6, TANK_TOP - 6, P, 40, 0.6), { tone: "hi" }));
  o.push(L([14, 24, 88].map((z) => k.sideArc(x, y, TANK_R, z, P, 24)).join(""), { tone: "faint" }));
  o.push(k.faceTextSvg(k.sideMatrix([x, y], 58, P, "right"), "He", { size: 12, tone: "lo", anchor: "middle" }));
  o.push(S(k.cylinder(x, y, 10, TANK_TOP, 12, P, 28), { tone: "mid" }));
  o.push(S(k.cylinder(x, y, 5, TANK_TOP + 12, 14, P, 20), { tone: "mid", crease: "none" }));
  o.push(S(k.slabOf({ x: x - 8, y: y - 8, w: 16, d: 16, r: 3 }, TANK_TOP + 24, 12, P, 3, 0.4), { tone: "mid" }));      // regulator block
  o.push(S(k.cylinder(x + 12, y, 5, TANK_TOP + 24, 4, P, 20), { tone: "hi" }));                                       // its small dial plug
  o.push(D([at([x - 5, y - 5, TANK_TOP + 36]), at([x + 5, y + 5, TANK_TOP + 36])], { size: 0.8 }));
  return o.join("");
}

function mfc() {
  const o = [`<path class="iso-halo" d="${k.haloOf(MFC, 0, 2, P)}"/>`];
  o.push(S(k.slabOf(MFC, 0, MFC_H, P, 5, 0.8), { tone: "mid" }));
  o.push(S(k.slabOf(k.insetPlan(MFC, 4), MFC_H, 4, P, 4, 0.5), { tone: "hi" }));
  o.push(L(k.planOutline(k.insetPlan(MFC, 8), MFC_H + 4, P, 3), { tone: "faint" }));
  // the pressure gauge lying on top: a dial with a needle that the pose moves
  const gx = MFC.x + 24, gy = MFC.y + 22, gz = MFC_H + 4;
  o.push(S(k.cylinder(gx, gy, 13, gz, 5, P, 40, 0.5), { tone: "hi", crease: "lo" }));
  o.push(L(k.ring(gx, gy, 10.6, gz + 5, P, 40), { tone: "lo" }));
  const t = k.radialTicks(gx, gy, 10.2, 40, 5, gz + 5, [1, 2.2], P, -2.2, 4.4);
  o.push(L(t.minor, { tone: "lo" }), L(t.major, { tone: "mid" }));
  o.push(`<path data-part="needle" class="iso-line" data-tone="lit" data-free="start" d="" style="stroke-width:1.2"/>`);
  o.push(L(k.ring(gx, gy, 1.5, gz + 5.2, P, 12), { tone: "mid" }));
  const knob = [MFC.x + 8, MFC.y + 31];
  o.push(S(k.cylinder(knob[0], knob[1], 5, gz, 5, P, 24), { tone: "mid" }));
  o.push(L(k.knurl(knob[0], knob[1], 5, gz, gz + 5, 24, P, 0.3), { tone: "lo" }));
  o.push(L(k.lineOnTop([knob[0], knob[1]], [knob[0] + 5, knob[1]], gz + 5, P), { tone: "hi" }));
  o.push(D([at([MFC.x + 5, MFC.y + 5, gz]), at([MFC.x + MFC.w - 5, MFC.y + MFC.d - 5, gz])], { size: 0.8 }));
  return { svg: o.join(""), gauge: [gx, gy, gz + 5.2] };
}

// helium line: square ducts along the route (the dots in them are drawn by the pose)
function duct(a, b) {
  const [x0, y0, z0] = a, [x1, y1, z1] = b;
  if (z0 !== z1) return S(k.cylinder(x0, y0, 2.6, Math.min(z0, z1), Math.abs(z1 - z0), P, 14), { tone: "mid", crease: "none" });
  const t = 5.2;
  return S(k.slabOf(bar(x0, y0, x1, y1, z0 - t / 2, t), z0 - t / 2, t, P, 2, 0.3), { tone: "mid", crease: "none" });
}
const LINE_PTS = [[TANK[0], TANK[1], TANK_TOP + 30], [TANK[0], 144 - 0, TANK_TOP + 30], [MFC.x + 14, 144, TANK_TOP + 30], [MFC.x + 14, 144, MFC_H + 4]];
const OUT_PTS = [[MFC.x + 14, MFC.y + 4, DUCT_Z], [30, MFC.y + 4, DUCT_Z], [30, 0, DUCT_Z], [0, 0, DUCT_Z]];
// the lengths the helium dots follow (ducts then the gap): used by the pose
function route(points) { const segs = []; let len = 0; for (let i = 0; i + 1 < points.length; i++) { const a = points[i], b = points[i + 1], d = Math.hypot(b[0] - a[0], b[1] - a[1], b[2] - a[2]); segs.push({ a, b, d, from: len }); len += d; } return { segs, len }; }

function ducts(m) {
  const o = [];
  // in: tank regulator -> over -> down into the controller top ; out: controller back -> floor -> into the column
  for (let i = 0; i + 1 < LINE_PTS.length; i++) o.push(duct(LINE_PTS[i], LINE_PTS[i + 1]));
  for (let i = 0; i + 1 < OUT_PTS.length; i++) o.push(duct(OUT_PTS[i], OUT_PTS[i + 1]));
  o.push(D([...LINE_PTS, ...OUT_PTS].map((p) => at(p)), { size: 1.3, tone: "hi" }));
  return o.join("");
}

// ---- assemble (painter's order: back posts and bars, floor gear, pedestal, wafer, gas, front bars and posts)
const m = mfc();
const sortedPosts = POSTS.map((p) => p).sort((a, b) => k.depthOf([a[0], a[1], 0], P) - k.depthOf([b[0], b[1], 0], P));
const backPosts = sortedPosts.slice(0, 3), frontPost = sortedPosts[3];
const bars = {
  back: [[[-112, -112], [112, -112]], [[-112, -112], [-112, 112]]],
  mid: [[[112, -112], [112, 112]]],
  front: [[[-112, 112], [112, 112]]],
};
const gasGap = `<g data-part="gap-dots" class="an-he"></g>`;
const body = [
  floor(),
  pedestal(),
  gasGap,
  `<path data-part="rim" class="an-rim" d="${k.ring(0, 0, CHUCK_R + 1, CHUCK_TOP, P, 72)}" style="opacity:0"/>`,
  `<g data-part="wafer">${wafer()}</g>`,
  backPosts.map(([x, y]) => post(x, y)).join(""),
  bars.back.map(([a, b]) => frameBar(a, b)).join(""),
  `<g data-part="plasma" class="an-plasma" style="opacity:0"></g>`,
  showerhead(),
  bars.mid.map(([a, b]) => frameBar(a, b)).join(""),
  tank(),
  mfc === undefined ? "" : m.svg,
  ducts(m),
  `<g data-part="duct-dots" class="an-he"></g>`,
  bars.front.map(([a, b]) => frameBar(a, b)).join(""),
  post(frontPost[0], frontPost[1]),
].join("");

const svg = k.figureSvg({
  width: WIDTH, height: HEIGHT,
  label: "A plasma-etch wafer pedestal, drawn as a machine. A wafer rests on a ceramic chuck cut with helium channels. Above it a showerhead holds the plasma. A helium tank feeds a controller whose line runs into the pedestal.",
  body: [body],
});

const css = k.ISO_CSS + `
.an-he circle{fill:var(--anatomy-blue);stroke:none;opacity:1}
.an-rim{fill:none;stroke:var(--anatomy-blue);stroke-width:3px;stroke-linecap:round}
.an-heat{fill:var(--anatomy-lit);stroke:none}
.an-plasma path{fill:var(--anatomy-lit);stroke:none}
.an-plasma .ion{fill:var(--anatomy-lit);stroke:none}
`;

const pose = (kitScript() + `
const P = ${JSON.stringify(P)};
const RAISE = ${RAISE}, SLIDE = ${SLIDE}, CHUCK_TOP = ${CHUCK_TOP}, WAFER_R = ${WAFER_R}, WAFER_H = ${WAFER_H}, SHOWER_Z = ${SHOWER_Z};
const GAUGE = ${JSON.stringify(m.gauge)};
const LINE_PTS = ${JSON.stringify(LINE_PTS)}, OUT_PTS = ${JSON.stringify(OUT_PTS)};
const route = ${route.toString()};
const IN = route(LINE_PTS), OUT = route(OUT_PTS);
const along = (R, d) => { for (const s of R.segs) if (d <= s.from + s.d + 1e-9) { const u = (d - s.from) / s.d; return [0, 1, 2].map((i) => s.a[i] + (s.b[i] - s.a[i]) * u); } const s = R.segs[R.segs.length - 1]; return s.b; };
const frac = (x) => x - Math.floor(x);
const q = {};
const part = (svg, n) => (q[n] = q[n] && svg.contains(q[n]) ? q[n] : svg.querySelector('[data-part="' + n + '"]'));
window.__ANP[${JSON.stringify(NAME)}] = {
  init: { lift: 0, plasma: 0, he: 0, die: 0 },
  apply(svg, s, t) {
    const sm = (u) => { u = Math.min(1, Math.max(0, u)); return u * u * (3 - 2 * u); };
    const wz = CHUCK_TOP + RAISE * sm(s.lift / 0.3), wy = -SLIDE * sm((s.lift - 0.3) / 0.7);
    part(svg, "wafer").setAttribute("transform", translateAlong(P, [0, wy, wz]));
    // helium in the ducts and in the channels of the chuck (positions are a pure function of the page clock)
    const he = s.he, dots = [];
    const nIn = 9, nOut = 9;
    for (let i = 0; i < nIn; i++) dots.push(iso(along(IN, frac(i / nIn + t * 0.22) * IN.len), P));
    for (let i = 0; i < nOut; i++) dots.push(iso(along(OUT, frac(i / nOut + t * 0.3) * OUT.len), P));
    part(svg, "duct-dots").innerHTML = he > 0.02 ? dotsSvg(dots.map(([x, y]) => [x, y, Math.min(1, he * 1.6)]), { size: 2.6 }) : "";
    const ch = [];
    for (let a = 0; a < 8; a++) for (let j = 0; j < 4; j++) {
      const r = 6 + frac(j / 4 + t * 0.35 + a * 0.071) * 60, ang = a * Math.PI / 4;
      ch.push(iso([Math.cos(ang) * r, Math.sin(ang) * r, CHUCK_TOP + 0.4], P));
    }
    for (let i = 0; i < 24; i++) {                                   // ring channels fill after the spokes
      const ang = (i / 24) * Math.PI * 2, r = [22, 44, 66][i % 3];
      ch.push(iso([Math.cos(ang) * r, Math.sin(ang) * r, CHUCK_TOP + 0.4], P));
    }
    part(svg, "gap-dots").innerHTML = he > 0.02 ? dotsSvg(ch.map(([x, y]) => [x, y, Math.min(1, he * 1.6)]), { size: 2.8 }) : "";
    // plasma between the showerhead and the wafer, with ions falling onto it
    const pl = part(svg, "plasma"), pz = CHUCK_TOP + WAFER_H, top = SHOWER_Z - 2;
    pl.style.opacity = s.plasma > 0.01 ? "1" : "0";
    if (s.plasma > 0.01) {
      let h = "";
      for (let i = 0; i < 5; i++) { const z = pz + 4 + (top - pz - 8) * (i / 4); h += '<path fill-opacity="' + (s.plasma * (0.07 + 0.05 * Math.sin(t * 7 + i))).toFixed(3) + '" d="' + ring(0, 0, 60 + 4 * Math.sin(i), z, P, 48) + 'Z"/>'; }
      for (let i = 0; i < 16; i++) { const a = i * 2.4, r = 14 + (i * 37) % 44, u = frac(i * 0.173 + t * 0.9), [x, y] = iso([Math.cos(a) * r, Math.sin(a) * r, top - u * (top - pz)], P); h += '<circle class="ion" cx="' + x.toFixed(1) + '" cy="' + y.toFixed(1) + '" r="1.5" fill-opacity="' + (s.plasma * (u > 0.85 ? 1 - (u - 0.85) / 0.15 : 0.9)).toFixed(2) + '"/>'; }
      pl.innerHTML = h;
    } else pl.innerHTML = "";
    // the wafer's heat: plasma power heats it, helium under it takes the heat to the water-cooled chuck
    const clamped = 1 - sm(s.lift / 0.15);
    const heat = Math.min(1, s.plasma * (1 - 0.88 * he * clamped));
    part(svg, "rim").style.opacity = (clamped * he).toFixed(2);
    part(svg, "heat").style.fillOpacity = (heat * 0.85).toFixed(3);
    // pressure gauge needle
    part(svg, "needle").setAttribute("d", (() => { const a = (-2.2 + he * 4.4) , [x, y, z] = GAUGE; return lineOnTop([x - Math.sin(a) * 2.5, y + Math.cos(a) * 2.5], [x + Math.sin(a) * 8.6, y - Math.cos(a) * 8.6], z, P); })());
  },
};
`).replaceAll("</script", "<\\/script");        // the kit holds the text "</script>" in a string: keep it from ending an inline script

writeFileSync(join(HERE, `${NAME}.svg`), svg);
writeFileSync(join(HERE, `${NAME}.css`), css);
writeFileSync(join(HERE, `${NAME}.pose.js`), pose);
writeFileSync(join(HERE, `${NAME}.json`), JSON.stringify({ width: WIDTH, height: HEIGHT, params: { lift: "wafer height, 0 clamped to 1 lifted", plasma: "0..1", he: "0..1 helium flow", die: "unused" } }, null, 1));
console.log("wrote", NAME, svg.length, "bytes");

if (process.argv.includes("--preview")) {
  const t = Number(process.argv[process.argv.indexOf("--preview") + 1]) || 0;
  const st = { lift: 0, plasma: 0, he: 0, die: 0 };
  const args = process.argv.find((a) => a.startsWith("--state="));
  if (args) Object.assign(st, JSON.parse(args.slice(8)));
  const page = `<!doctype html><html><head><meta charset="utf-8"><style>${css}body{margin:0;background:#0B0D17}.an{width:900px;margin:20px auto;--anatomy-paper:#151A2B;--anatomy-face:#1B2136;--anatomy-top:#232B47;--anatomy-shade-0:#0E111E;--anatomy-shade-1:#121626;--anatomy-shade-2:#171C2F;--anatomy-shade-3:#1C2238;--anatomy-hi:#D9D3C7;--anatomy-mid:#6B7590;--anatomy-lo:#3B4460;--anatomy-faint:#262D42;--anatomy-lit:#FF9A5C;--anatomy-lit-top:#6B3A1F;--anatomy-lit-shade:#4A2A18;--anatomy-weight:2.2px;--anatomy-blue:#8EC2F2}</style></head><body><div class="an iso" data-theme="dark" id="f">${svg}</div><script>window.__ANP={};${pose};window.__ANP["${NAME}"].apply(document.querySelector("svg"),${JSON.stringify(st)},${t});</script></body></html>`;
  writeFileSync(join(HERE, "preview.html"), page);
  console.log("preview.html");
}
