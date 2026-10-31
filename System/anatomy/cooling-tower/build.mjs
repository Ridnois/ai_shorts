// Cooling tower: how a data centre turns chip heat into steam. A server block on the left carries a finned heat sink that
// glows red when it works. Warm water (red beads) runs along a channel to a cooling tower on the right; there the fan pulls
// air through louvers, part of the water evaporates (yellow puffs rise from the stack, the heat leaves with them) and the
// cooled water (blue beads) runs back along the second channel. A rail of five lamps in front counts the drops one answer
// costs; a dial on the left reads the electricity the cooling takes. Schematic, not to scale.
// node build.mjs [--preview [t]] [--state='{"heat":1}']  ->  cooling-tower.svg  .json  .css  .pose.js  (+ preview.html)
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../../../.claude/skills/anatomy/kit/iso-kit.mjs";
import * as G from "../../../.claude/skills/anatomy/kit/lathe.mjs";
import { kitScript } from "../../../.claude/skills/anatomy/scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const NAME = "cooling-tower";
const WIDTH = 600;

// ---- world (x, y floor; z up)
const BASE = { x: -230, y: -130, w: 460, d: 250, r: 8 }, BASE_H = 12;
const Z0 = BASE_H;
// the server block and its heat sink
const CHIP = { x: -205, y: -70, w: 84, d: 84, r: 3 }, CHIP_H = 52, CZ = Z0 + CHIP_H;
const SINK = { x: -193, y: -58, w: 60, d: 60 }, SINK_BASE = 6, FIN_N = 7, FIN_W = 4.5, FIN_H = 26;
const finX = (i) => SINK.x + 3 + i * ((SINK.w - 6 - FIN_W) / (FIN_N - 1));
// the two channels on the floor: warm out (y = HOT_Y), cool back (y = COOL_Y), from the server to the tower
const CH_X0 = -121, CH_X1 = 88, HOT_Y = -48, COOL_Y = -8, CH_W = 16, CH_H = 3;
const BEADS = 5, CH_L = CH_X1 - CH_X0 - 20;
// the tower: basin, body, deck, fan stack
const BASIN = { x: 85, y: -80, w: 124, d: 124, r: 4 }, BASIN_H = 10, BZ = Z0 + BASIN_H;
const BODY = { x: 96, y: -69, w: 102, d: 102, r: 2 }, BODY_H = 88, TZ = BZ + BODY_H;
const DECK = { x: 90, y: -75, w: 114, d: 114, r: 3 }, DECK_H = 5, DZ = TZ + DECK_H;
const CX = 147, CY = -18, STACK_R = 38, STACK_H = 18, SZ = DZ + STACK_H;      // stack centre and rim height
// the drop rail in front: five lamps
const RAIL = { x: 24, y: 70, w: 164, d: 34, r: 3 }, RAIL_H = 3, RZ = Z0 + RAIL_H, LAMP_X = (i) => RAIL.x + 22 + i * 30, LAMP_Y = RAIL.y + 17;
// the power dial on the left front
const DIAL = { x: -150, y: 72, r: 30 }, DIAL_H = 8, DLZ = Z0 + DIAL_H;
const RISE = 120;                                                              // how high a puff travels

const EXTREMES = [...k.boxCorners(BASE, 0, BASE_H), ...k.boxCorners({ x: 96, y: -69, w: 102, d: 102 }, 0, SZ + RISE + 30)];
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
const disc = (x, y, r, z, h, style = {}) => S(k.cylinder(x, y, r, z, h, P, 28), { tone: "hi", crease: "none", ...style });
const screw = (x, y, z) => S(G.lathe([[0, 0], [0, 3], [1.2, 3], [1.2, 0]], G.frameAlong([x, y, z], [0, 0, 1]), P, { steps: 16 }), { tone: "hi", crease: "none" });
const bar = (x0, x1, y, z, h = 2.2) => poly([[x0, y - h, z], [x1, y - h, z], [x1, y + h, z], [x0, y + h, z]], "ct-ink");
const circle = (cx, cy, r, z, cls, n = 28) => poly(Array.from({ length: n }, (_, i) => [cx + r * Math.cos((i / n) * 2 * Math.PI), cy + r * Math.sin((i / n) * 2 * Math.PI), z]), cls);
const dome = (x, y, z, r, cls) => {
  const mer = [[0, 0], [0, r]]; for (let i = 1; i < 8; i++) { const b = (i / 8) * Math.PI / 2; mer.push([r * Math.sin(b), r * Math.cos(b), 1]); } mer.push([r, 0]);
  return S(G.lathe(mer, G.frameAlong([x, y, z], [0, 0, 1]), P, { steps: 36 }), { tone: "hi", crease: "none", ...(cls ? { className: cls } : {}) });
};

function base() {
  const o = [slab(BASE, 0, BASE_H, { crease: "none" })];
  for (const [x, y] of [[BASE.x + 12, BASE.y + 12], [BASE.x + BASE.w - 12, BASE.y + 12], [BASE.x + 12, BASE.y + BASE.d - 12], [BASE.x + BASE.w - 12, BASE.y + BASE.d - 12]])
    o.push(screw(x, y, Z0));
  // a ruler strip along the back edge
  const y0 = BASE.y + 10, x0 = BASE.x + 40;
  o.push(slab({ x: x0, y: y0, w: 150, d: 14, r: 2 }, Z0, 1.6, { crease: "none" }));
  for (let i = 0; i <= 14; i++) o.push(poly([[x0 + 6 + i * 9.4, y0 + 2, Z0 + 1.6], [x0 + 7.2 + i * 9.4, y0 + 2, Z0 + 1.6], [x0 + 7.2 + i * 9.4, y0 + (i % 5 ? 6 : 10), Z0 + 1.6], [x0 + 6 + i * 9.4, y0 + (i % 5 ? 6 : 10), Z0 + 1.6]], "ct-ink"));
  return o.join("");
}
function server() {
  const C = CHIP, o = [slab(C, Z0, CHIP_H)];
  // vents on the two front faces, a label plate and a lamp
  const Yf = C.y + C.d, Xf = C.x + C.w;
  for (let i = 0; i < 4; i++) {
    const z = Z0 + 10 + i * 6;
    o.push(poly([[C.x + 8, Yf, z], [C.x + C.w - 24, Yf, z], [C.x + C.w - 24, Yf, z + 2.4], [C.x + 8, Yf, z + 2.4]], "ct-ink"));
    o.push(poly([[Xf, C.y + 8, z], [Xf, C.y + C.d - 8, z], [Xf, C.y + C.d - 8, z + 2.4], [Xf, C.y + 8, z + 2.4]], "ct-ink"));
  }
  o.push(poly([[C.x + C.w - 18, Yf, Z0 + 28], [C.x + C.w - 6, Yf, Z0 + 28], [C.x + C.w - 6, Yf, Z0 + 44], [C.x + C.w - 18, Yf, Z0 + 44]], "ct-plate"));
  o.push(slab({ x: C.x - 3, y: C.y - 3, w: C.w + 6, d: C.d + 6, r: 3 }, CZ - 3, 3));
  for (const [x, y] of [[C.x + 6, C.y + 6], [C.x + C.w - 6, C.y + 6], [C.x + 6, C.y + C.d - 6], [C.x + C.w - 6, C.y + C.d - 6]]) o.push(screw(x, y, CZ));
  // the heat sink: a plate and seven fins
  o.push(slab({ x: SINK.x, y: SINK.y, w: SINK.w, d: SINK.d, r: 2 }, CZ, SINK_BASE));
  return o.join("");
}
const finsAt = (cls) => Array.from({ length: FIN_N }, (_, i) => slab({ x: finX(i), y: SINK.y + 2, w: FIN_W, d: SINK.d - 4, r: 1 }, CZ + SINK_BASE, FIN_H, cls ? { className: cls } : {})).join("");
function channel(y, cool) {
  const o = [slab({ x: CH_X0, y: y - CH_W / 2, w: CH_X1 - CH_X0, d: CH_W, r: 2 }, Z0, CH_H, { crease: "none" })];
  o.push(poly([[CH_X0 + 4, y - 4.5, Z0 + CH_H], [CH_X1 - 4, y - 4.5, Z0 + CH_H], [CH_X1 - 4, y + 4.5, Z0 + CH_H], [CH_X0 + 4, y + 4.5, Z0 + CH_H]], "ct-hatch"));
  // chevrons point the way the water goes: to the tower on the warm channel, back on the cool one
  for (let i = 0; i < 4; i++) {
    const x = CH_X0 + 36 + i * 44, d = cool ? -1 : 1;
    o.push(poly([[x - d * 5, y - 3.4, Z0 + CH_H], [x + d * 1, y, Z0 + CH_H], [x - d * 5, y + 3.4, Z0 + CH_H], [x - d * 3, y, Z0 + CH_H]], "ct-ink"));
  }
  return o.join("");
}
function bead(i, cool) {
  const y = cool ? COOL_Y : HOT_Y;
  return `<g data-part="${cool ? "cb" : "hb"}${i}" style="opacity:0">${disc(CH_X0 + 10, y, 4.6, Z0 + CH_H, 6, { className: cool ? "ct-b" : "ct-r" })}</g>`;
}
function tower() {
  const o = [slab(BASIN, Z0, BASIN_H)];
  // the water in the basin: a blue inlay, with a rim of four screws
  o.push(`<g data-part="water">${poly([[BASIN.x + 5, BASIN.y + 5, BZ + 0.2], [BASIN.x + BASIN.w - 5, BASIN.y + 5, BZ + 0.2], [BASIN.x + BASIN.w - 5, BASIN.y + BASIN.d - 5, BZ + 0.2], [BASIN.x + 5, BASIN.y + BASIN.d - 5, BZ + 0.2]], "ct-water")}</g>`);
  o.push(slab(BODY, BZ, BODY_H));
  // louvers on the two front faces: rows of slats
  const Yf = BODY.y + BODY.d, Xf = BODY.x + BODY.w;
  for (let i = 0; i < 7; i++) {
    const z = BZ + 10 + i * 11;
    o.push(poly([[BODY.x + 8, Yf, z], [BODY.x + BODY.w - 8, Yf, z], [BODY.x + BODY.w - 8, Yf, z + 3.2], [BODY.x + 8, Yf, z + 3.2]], "ct-ink"));
    o.push(poly([[Xf, BODY.y + 8, z], [Xf, BODY.y + BODY.d - 8, z], [Xf, BODY.y + BODY.d - 8, z + 3.2], [Xf, BODY.y + 8, z + 3.2]], "ct-ink"));
  }
  // the inlet where the warm channel meets the body
  o.push(poly([[BODY.x, HOT_Y - 8, BZ + 1], [BODY.x, HOT_Y + 8, BZ + 1], [BODY.x, HOT_Y + 8, BZ + 9], [BODY.x, HOT_Y - 8, BZ + 9]], "ct-plate"));
  o.push(poly([[BODY.x, COOL_Y - 8, BZ + 1], [BODY.x, COOL_Y + 8, BZ + 1], [BODY.x, COOL_Y + 8, BZ + 9], [BODY.x, COOL_Y - 8, BZ + 9]], "ct-plate"));
  o.push(slab(DECK, TZ, DECK_H));
  for (const [x, y] of [[DECK.x + 6, DECK.y + 6], [DECK.x + DECK.w - 6, DECK.y + 6], [DECK.x + 6, DECK.y + DECK.d - 6], [DECK.x + DECK.w - 6, DECK.y + DECK.d - 6]]) o.push(screw(x, y, DZ));
  // the fan stack: a ring, the dark throat, a hub and two guard bars
  o.push(disc(CX, CY, STACK_R, DZ, STACK_H));
  o.push(circle(CX, CY, STACK_R - 5, SZ + 0.2, "ct-hole"));
  o.push(`<path data-part="blades" class="ct-blade" d=""/>`);
  o.push(disc(CX, CY, 6, SZ - 4, 8));
  o.push(bar(CX - STACK_R + 3, CX + STACK_R - 3, CY, SZ + 0.4, 1.4), poly([[CX - 1.4, CY - STACK_R + 3, SZ + 0.4], [CX + 1.4, CY - STACK_R + 3, SZ + 0.4], [CX + 1.4, CY + STACK_R - 3, SZ + 0.4], [CX - 1.4, CY + STACK_R - 3, SZ + 0.4]], "ct-ink"));
  return o.join("");
}
const PUFFS = [[0, 0, 12], [-9, 6, 15], [8, -7, 13], [-4, -2, 16]];
function puff(i) {
  const [dx, dy, r] = PUFFS[i];
  return `<g data-part="puff${i}" style="opacity:0">${dome(CX + dx, CY + dy, SZ + 6, r, "ct-y")}</g>`;
}
function rail() {
  const o = [slab(RAIL, Z0, RAIL_H, { crease: "none" })];
  for (let i = 0; i < 5; i++) {
    o.push(disc(LAMP_X(i), LAMP_Y, 11, RZ, 3, {}));
    o.push(circle(LAMP_X(i), LAMP_Y, 7, RZ + 3.2, "ct-hole", 20));
    o.push(`<g data-part="drop${i}" style="opacity:0">${dome(LAMP_X(i), LAMP_Y, RZ + 3, 8, "ct-y")}</g>`);
  }
  // a rule strip behind the lamps: the five sit on a ruler with a tick between each pair
  for (let i = 0; i < 4; i++) o.push(poly([[LAMP_X(i) + 14, RAIL.y + 2, RZ], [LAMP_X(i) + 16, RAIL.y + 2, RZ], [LAMP_X(i) + 16, RAIL.y + 8, RZ], [LAMP_X(i) + 14, RAIL.y + 8, RZ]], "ct-ink"));
  return o.join("");
}
function dial() {
  const { x, y, r } = DIAL, o = [disc(x, y, r + 5, Z0, DIAL_H - 4), disc(x, y, r, Z0 + DIAL_H - 4, 4)];
  o.push(circle(x, y, r - 4, DLZ + 0.2, "ct-face", 36));
  // ticks along a 250 degree sweep, a major tick every fifth
  for (let i = 0; i <= 10; i++) {
    const a = (-125 + 25 * i - 90) * Math.PI / 180, r0 = r - 5, r1_ = r - (i % 5 ? 8 : 11), w = 0.05;
    o.push(poly([[x + r0 * Math.cos(a - w), y + r0 * Math.sin(a - w), DLZ + 0.3], [x + r0 * Math.cos(a + w), y + r0 * Math.sin(a + w), DLZ + 0.3],
      [x + r1_ * Math.cos(a + w), y + r1_ * Math.sin(a + w), DLZ + 0.3], [x + r1_ * Math.cos(a - w), y + r1_ * Math.sin(a - w), DLZ + 0.3]], "ct-ink"));
  }
  o.push(`<path data-part="needle" class="ct-needle" d=""/>`);
  o.push(disc(x, y, 3.2, DLZ + 0.4, 2.4));
  return o.join("");
}

const body = [
  base(),
  channel(HOT_Y, false), channel(COOL_Y, true),
  server(),
  finsAt(),
  `<g data-part="hot" style="opacity:0">${finsAt("ct-r")}</g>`,
  ...Array.from({ length: BEADS }, (_, i) => bead(i, false)), ...Array.from({ length: BEADS }, (_, i) => bead(i, true)),
  rail(),
  dial(),
  tower(),
  ...PUFFS.map((_, i) => puff(i)),
].join("");

const svg = k.figureSvg({
  width: WIDTH, height: HEIGHT,
  label: "Cooling tower: a server block with a finned heat sink that glows red when it works. Warm water (red beads) runs along a channel to a cooling tower; its fan pulls air through louvers, part of the water evaporates (yellow puffs rise from the stack) and the cooled water (blue beads) runs back. A rail of five lamps counts drops of water; a dial reads the electricity the cooling takes.",
  body: [body],
});

const tint = (cls, c, shade = 80) => {
  const mix = (p, w) => `color-mix(in srgb, ${c} ${p}%, ${w})`;
  const tones = [mix(62, "#000"), mix(shade, "#000"), c, c];
  const sel = `.iso .iso-solid.${cls}`;
  return `${sel}>.iso-fill,${sel}>.iso-top{fill:${c};stroke:var(--anatomy-hi)}\n` + tones.map((t, i) => `${sel}>.iso-shade[data-shade="${i}"]{fill:${t};stroke:${t}}`).join("\n") + "\n";
};
const flat = (cls, fill) => `.${cls}{fill:${fill};stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}\n`;
const css = k.ISO_CSS + tint("ct-r", "var(--anatomy-red)") + tint("ct-b", "var(--anatomy-blue)") + `
.iso .iso-solid.ct-y>.iso-fill,.iso .iso-solid.ct-y>.iso-top{fill:var(--anatomy-lit-top);stroke:var(--anatomy-hi)}
.iso .iso-solid.ct-y>.iso-shade{fill:var(--anatomy-lit-shade);stroke:var(--anatomy-lit-shade)}
.ct-ink{fill:var(--anatomy-hi);stroke:none}
.ct-blade{fill:var(--anatomy-mid);stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}
.ct-needle{fill:var(--anatomy-red);stroke:var(--anatomy-hi);stroke-width:2px;stroke-linejoin:round;vector-effect:non-scaling-stroke}
` + flat("ct-plate", "var(--anatomy-shade-3)") + flat("ct-hatch", "var(--anatomy-shade-2)") + flat("ct-hole", "var(--anatomy-mid)") + flat("ct-face", "var(--anatomy-shade-3)")
  + flat("ct-water", "color-mix(in srgb, var(--anatomy-blue) 45%, #fff)");

const pose = (kitScript() + `
const P = ${JSON.stringify(P)};
const C = { cx: ${CX}, cy: ${CY}, fanZ: ${SZ - 0.6}, r: ${STACK_R - 8}, dial: [${DIAL.x}, ${DIAL.y}, ${DLZ + 0.8}], dr: ${DIAL.r - 6} };
const GEO = { x0: ${CH_X0 + 10}, L: ${CH_L}, beads: ${BEADS}, rise: ${RISE} };
const q = {};
const part = (svg, n) => (q[n] = q[n] && svg.contains(q[n]) ? q[n] : svg.querySelector('[data-part="' + n + '"]'));
const cl = (u) => Math.min(1, Math.max(0, u));
const sm = (u) => { u = cl(u); return u * u * (3 - 2 * u); };
const frac = (u) => u - Math.floor(u);
const op = (el, v) => { el.style.opacity = v <= 0.001 ? "0" : v >= 0.999 ? "1" : v.toFixed(3); };
const path = (pts) => pts.map((p, i) => { const [x, y] = iso(p, P); return (i ? "L" : "M") + x.toFixed(1) + " " + y.toFixed(1); }).join("") + "Z";
window.__ANP[${JSON.stringify(NAME)}] = {
  init: { heat: 0, flow: 0, evap: 0, rise: 0, fan: 0, drops: 0, power: 0.18 },
  apply(svg, s, t) {
    // the machine runs on the page clock: fan, puffs and beads keep moving between the pose keys (a key adds an offset)
    const T = t || 0;
    s = { ...s, flow: s.flow + 0.42 * T, rise: s.rise + 0.5 * T, fan: s.fan + 1.6 * T };
    // heat: the heat sink fins glow red
    op(part(svg, "hot"), cl(s.heat));
    // flow: beads ride the channels, warm out to the tower, cool back; they fade in and out at the ends
    for (let i = 0; i < GEO.beads; i++) {
      const u = frac(s.flow + i / GEO.beads), env = Math.sin(Math.PI * u), a = cl(s.heat * 4) * Math.pow(env, 0.5);
      part(svg, "hb" + i).setAttribute("transform", translateAlong(P, [GEO.L * u, 0, 0]));
      op(part(svg, "hb" + i), a);
      part(svg, "cb" + i).setAttribute("transform", translateAlong(P, [GEO.L * (1 - u), 0, 0]));
      op(part(svg, "cb" + i), a * cl(s.evap * 3));
    }
    // evap: puffs of vapour rise out of the stack and fade; the heat leaves with them
    for (let i = 0; i < 4; i++) {
      const u = frac(s.rise + i / 4), env = Math.pow(Math.sin(Math.PI * u), 0.7);
      part(svg, "puff" + i).setAttribute("transform", translateAlong(P, [u * 18, 0, u * GEO.rise]));
      op(part(svg, "puff" + i), cl(s.evap) * env);
    }
    // the basin water dims a little as it evaporates
    op(part(svg, "water"), 1 - 0.35 * cl(s.evap));
    // fan: four blades turn on the stack, drawn flat on its throat
    const f = s.fan * 2 * Math.PI, blades = [];
    for (let j = 0; j < 4; j++) {
      const a = f + (j * Math.PI) / 2, dx = Math.cos(a), dy = Math.sin(a), px = -dy, py = dx;
      const pts = [[C.cx + 6 * dx + 2.6 * px, C.cy + 6 * dy + 2.6 * py], [C.cx + C.r * dx + 8 * px, C.cy + C.r * dy + 8 * py], [C.cx + C.r * dx + 1 * px, C.cy + C.r * dy + 1 * py], [C.cx + 6 * dx - 2.6 * px, C.cy + 6 * dy - 2.6 * py]];
      blades.push(path(pts.map(([x, y]) => [x, y, C.fanZ])));
    }
    part(svg, "blades").setAttribute("d", blades.join(""));
    // drops: the lamps on the rail light one by one
    for (let i = 0; i < 5; i++) op(part(svg, "drop" + i), cl(s.drops - i));
    // power: the dial needle sweeps 250 degrees
    const a = ((-125 + 250 * cl(s.power) - 90) * Math.PI) / 180, [dx, dy] = [Math.cos(a), Math.sin(a)], [px, py] = [-dy, dx], [ox, oy, oz] = C.dial;
    part(svg, "needle").setAttribute("d", path([[ox + 3 * px, oy + 3 * py, oz], [ox + C.dr * dx + 0.8 * px, oy + C.dr * dy + 0.8 * py, oz], [ox + C.dr * dx - 0.8 * px, oy + C.dr * dy - 0.8 * py, oz], [ox - 3 * px, oy - 3 * py, oz]]));
  },
};
`).replaceAll("<script", "<\\u0073cript").replaceAll("</script", "<\\/script");

writeFileSync(join(HERE, `${NAME}.svg`), svg);
writeFileSync(join(HERE, `${NAME}.css`), css);
writeFileSync(join(HERE, `${NAME}.pose.js`), pose);
const anchors = {
  chip: [CHIP.x + CHIP.w / 2, CHIP.y + CHIP.d / 2, CZ + SINK_BASE + FIN_H],
  hot: [-40, HOT_Y, Z0 + CH_H],
  cool: [-40, COOL_Y, Z0 + CH_H],
  tower: [BODY.x + BODY.w, BODY.y + BODY.d / 2, BZ + BODY_H / 2],
  stack: [CX, CY, SZ],
  vapour: [CX, CY, SZ + RISE * 0.6],
  drops: [LAMP_X(2), LAMP_Y, RZ + 6],
  dial: [DIAL.x, DIAL.y, DLZ],
  basin: [BASIN.x + BASIN.w, BASIN.y + BASIN.d / 2, BZ],
};
writeFileSync(join(HERE, `${NAME}.json`), JSON.stringify({ width: WIDTH, height: HEIGHT,
  params: {
    heat: "0..1 the heat sink fins glow red and warm beads start to ride the first channel",
    flow: "phase offset (the clock already runs it at 0.42 laps a second): beads ride the channels, warm out to the tower, cool back",
    evap: "0..1 vapour puffs rise out of the fan stack; cool beads return; the basin water dims",
    rise: "phase offset (the clock runs it at 0.5 a second): how far the puffs have travelled; shown only while evap is above 0",
    fan: "phase offset (the clock turns it 1.6 turns a second): the fan blades",
    drops: "0..5 the lamps on the rail light one by one (drops of water)",
    power: "0..1 the dial needle sweeps (electricity the cooling takes); rest 0.18",
  },
  anchors: Object.fromEntries(Object.entries(anchors).map(([n, p]) => [n, at(p).map(r1)])) }, null, 1));
console.log("wrote", NAME, svg.length, "bytes", WIDTH, "x", HEIGHT, "scale", P.scale.toFixed(3));

if (process.argv.includes("--preview")) {
  const t = Number(process.argv[process.argv.indexOf("--preview") + 1]) || 0;
  const st = { heat: 0, flow: 0, evap: 0, rise: 0, fan: 0, drops: 0, power: 0.18 };
  const args = process.argv.find((a) => a.startsWith("--state="));
  if (args) Object.assign(st, JSON.parse(args.slice(8)));
  const vars = "--anatomy-paper:#FFFFFF;--anatomy-face:#FFFFFF;--anatomy-top:#FFFFFF;--anatomy-shade-0:#C4BAA6;--anatomy-shade-1:#D4CBB9;--anatomy-shade-2:#E3DCCD;--anatomy-shade-3:#F1ECE2;--anatomy-hi:#121212;--anatomy-mid:#3D3932;--anatomy-lo:#5A554B;--anatomy-faint:#B3AA98;--anatomy-lit:#121212;--anatomy-lit-top:#FFD23F;--anatomy-lit-shade:#F0B90F;--anatomy-halo:#6F6552;--anatomy-halo-opacity:.30;--anatomy-dot:#121212;--anatomy-weight:3.2px;--anatomy-red:#D7392B;--anatomy-green:#13965A;--anatomy-blue:#2C5BEA";
  const page = `<!doctype html><html><head><meta charset="utf-8"><style>${css}body{margin:0;background:#F4EFE4}.an{width:860px;margin:20px auto;${vars}}</style></head><body><div class="an iso" data-theme="dark" id="f">${svg}</div><script>window.__ANP={};${pose};window.__ANP["${NAME}"].apply(document.querySelector("svg"),${JSON.stringify(st)},${t});</script></body></html>`;
  writeFileSync(join(HERE, "preview.html"), page);
  console.log("preview.html");
}
