// Ticket board: the lottery ticket hypothesis as a bench machine. Thirty-six tickets (weights) sit in a pegboard, each with a
// blue chip for its number: light blue at the start, deep blue once trained. `train` darkens the chips and the dial reads the
// accuracy; `prune` lets the weakest tickets drop through the board one by one until four survive; `rewind` spins the tape reel
// and sets the survivors back to the numbers they started with; `fresh` gives the same four brand-new random numbers (red);
// `lit` turns the survivors yellow (the winning ticket). Schematic: 36 weights stand for a network of 266 thousand.
// node build.mjs [--preview [t]] [--state='{"train":1}']  ->  ticket-board.svg  .json  .css  .pose.js  (+ preview.html)
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../../../.claude/skills/anatomy/kit/iso-kit.mjs";
import * as G from "../../../.claude/skills/anatomy/kit/lathe.mjs";
import { kitScript } from "../../../.claude/skills/anatomy/scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const NAME = "ticket-board";
const WIDTH = 600;

// ---- world (x, y floor; z up)
const BASE = { x: -235, y: -135, w: 470, d: 285, r: 8 }, BASE_H = 12, Z0 = BASE_H;
const N = 6, PITCH = 34, BOARD = { x: -215, y: -118, w: N * PITCH + 28, d: N * PITCH + 28, r: 4 }, BOARD_H = 14, BZ = Z0 + BOARD_H;
const cellX = (c) => BOARD.x + 14 + PITCH / 2 + c * PITCH, cellY = (r) => BOARD.y + 14 + PITCH / 2 + r * PITCH;
const TK = 24, TK_H = 6, CHIP = 14;
const SURVIVORS = [2, 16, 19, 33];                                               // cell indices (row * 6 + col) of the four survivors
const ORDER = [20, 7, 28, 13, 1, 31, 10, 24, 5, 35, 17, 22, 0, 29, 14, 8, 26, 3, 32, 11, 21, 6, 30, 15, 9, 25, 4, 34, 12, 23, 18, 27];
const RANK = Object.fromEntries(ORDER.map((c, r) => [c, r]));                  // the weakest first
const DIAL = { x: 130, y: -70, r: 38 }, DIAL_H = 8, DLZ = Z0 + DIAL_H;
const REEL = { x: 130, y: 70, r: 36 }, REEL_H = 8, RLZ = Z0 + REEL_H;
const TRAY = { x: BOARD.x, y: BOARD.y + BOARD.d + 8, w: BOARD.w, d: 26, r: 3 };

const EXTREMES = [...k.boxCorners(BASE, 0, BASE_H), ...k.boxCorners(BOARD, 0, BZ + 40)];
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
const circle = (cx, cy, r, z, cls, n = 28) => poly(Array.from({ length: n }, (_, i) => [cx + r * Math.cos((i / n) * 2 * Math.PI), cy + r * Math.sin((i / n) * 2 * Math.PI), z]), cls);
const sq = (cx, cy, h, z, cls) => poly([[cx - h, cy - h, z], [cx + h, cy - h, z], [cx + h, cy + h, z], [cx - h, cy + h, z]], cls);

function base() {
  const o = [slab(BASE, 0, BASE_H, { crease: "none" })];
  for (const [x, y] of [[BASE.x + 12, BASE.y + 12], [BASE.x + BASE.w - 12, BASE.y + 12], [BASE.x + 12, BASE.y + BASE.d - 12], [BASE.x + BASE.w - 12, BASE.y + BASE.d - 12]]) o.push(screw(x, y, Z0));
  // a ruler strip along the back edge
  const x0 = 30, y0 = BASE.y + 10;
  o.push(slab({ x: x0, y: y0, w: 180, d: 14, r: 2 }, Z0, 1.6, { crease: "none" }));
  for (let i = 0; i <= 16; i++) o.push(poly([[x0 + 6 + i * 10.2, y0 + 2, Z0 + 1.6], [x0 + 7.2 + i * 10.2, y0 + 2, Z0 + 1.6], [x0 + 7.2 + i * 10.2, y0 + (i % 4 ? 6 : 10), Z0 + 1.6], [x0 + 6 + i * 10.2, y0 + (i % 4 ? 6 : 10), Z0 + 1.6]], "tb-ink"));
  return o.join("");
}
function board() {
  const o = [slab(BOARD, Z0, BOARD_H)];
  for (let r = 0; r < N; r++) for (let c = 0; c < N; c++) o.push(sq(cellX(c), cellY(r), 15, BZ + 0.2, "tb-slot"));
  for (const [x, y] of [[BOARD.x + 7, BOARD.y + 7], [BOARD.x + BOARD.w - 7, BOARD.y + 7], [BOARD.x + 7, BOARD.y + BOARD.d - 7], [BOARD.x + BOARD.w - 7, BOARD.y + BOARD.d - 7]]) o.push(screw(x, y, BZ));
  // the catch tray in front: where the pruned tickets land
  o.push(slab(TRAY, Z0, 5), poly([[TRAY.x + 6, TRAY.y + 6, Z0 + 5.2], [TRAY.x + TRAY.w - 6, TRAY.y + 6, Z0 + 5.2], [TRAY.x + TRAY.w - 6, TRAY.y + TRAY.d - 6, Z0 + 5.2], [TRAY.x + 6, TRAY.y + TRAY.d - 6, Z0 + 5.2]], "tb-slot"));
  return o.join("");
}
// a ticket: a paper body and a chip for its number. Survivors carry all four chip states and a yellow overlay; the rest need two.
function ticket(i, survivor) {
  const r = Math.floor(i / N), c = i % N, x = cellX(c), y = cellY(r), z = BZ;
  const o = [slab({ x: x - TK / 2, y: y - TK / 2, w: TK, d: TK, r: 2 }, z, TK_H)];
  const chip = (cls, show) => `<g data-part="${survivor ? "sv" + SURVIVORS.indexOf(i) : "tk" + i}-${show}" ${show === "start" ? "" : 'style="opacity:0"'}>${sq(x, y, CHIP / 2, z + TK_H + 0.2, cls)}</g>`;
  o.push(chip("tb-start", "start"));
  if (survivor) o.push(chip("tb-fresh", "fresh"));
  o.push(chip("tb-trained", "trained"));
  if (survivor) o.push(chip("tb-trained-red", "trainedred"));
  // two rule bars on the ticket's front edge, like a tear-off stub
  o.push(poly([[x - 8, y + TK / 2, z + 2], [x + 8, y + TK / 2, z + 2], [x + 8, y + TK / 2, z + 3.4], [x - 8, y + TK / 2, z + 3.4]], "tb-ink"));
  const g = `<g data-part="${survivor ? "sv" + SURVIVORS.indexOf(i) : "tk" + i}">${o.join("")}</g>`;
  if (!survivor) return g;
  const lit = `<g data-part="lit${SURVIVORS.indexOf(i)}" style="opacity:0">${slab({ x: x - TK / 2 - 6, y: y - TK / 2 - 6, w: TK + 12, d: TK + 12, r: 3 }, z + 0.3, 3.2, { className: "tb-y" })}</g>`;
  return lit + g;
}
function dial() {
  const { x, y, r } = DIAL, o = [disc(x, y, r + 5, Z0, DIAL_H - 4), disc(x, y, r, Z0 + DIAL_H - 4, 4)];
  o.push(circle(x, y, r - 4, DLZ + 0.2, "tb-face", 36));
  for (let i = 0; i <= 10; i++) {
    const a = (-125 + 25 * i - 90) * Math.PI / 180, r0 = r - 5, r1_ = r - (i % 5 ? 8 : 11), w = 0.05;
    o.push(poly([[x + r0 * Math.cos(a - w), y + r0 * Math.sin(a - w), DLZ + 0.3], [x + r0 * Math.cos(a + w), y + r0 * Math.sin(a + w), DLZ + 0.3],
      [x + r1_ * Math.cos(a + w), y + r1_ * Math.sin(a + w), DLZ + 0.3], [x + r1_ * Math.cos(a - w), y + r1_ * Math.sin(a - w), DLZ + 0.3]], "tb-ink"));
  }
  o.push(`<path data-part="needle" class="tb-needle" d=""/>`);
  o.push(disc(x, y, 3.4, DLZ + 0.4, 2.4));
  return o.join("");
}
function reel() {
  const { x, y, r } = REEL, o = [disc(x, y, r + 5, Z0, REEL_H - 3), disc(x, y, r, Z0 + REEL_H - 3, 3)];
  o.push(circle(x, y, r - 5, RLZ + 0.2, "tb-face", 36), circle(x, y, 8, RLZ + 0.3, "tb-slot", 20));
  o.push(`<path data-part="spokes" class="tb-spoke" d=""/>`);
  o.push(disc(x, y, 5, RLZ + 0.4, 5));
  // a label plate: three rule bars (the START mark)
  for (let i = 0; i < 3; i++) o.push(poly([[x - 22, y + r + 12 + i * 5, Z0 + 0.4], [x + 22 - i * 6, y + r + 12 + i * 5, Z0 + 0.4], [x + 22 - i * 6, y + r + 14.2 + i * 5, Z0 + 0.4], [x - 22, y + r + 14.2 + i * 5, Z0 + 0.4]], "tb-ink"));
  return o.join("");
}

const tickets = Array.from({ length: N * N }, (_, i) => ticket(i, SURVIVORS.includes(i))).join("");
const body = [base(), board(), tickets, dial(), reel()].join("");

const svg = k.figureSvg({
  width: WIDTH, height: HEIGHT,
  label: "Ticket board: thirty-six tickets in a pegboard, each with a blue chip for its number (light at the start, deep once trained). The weakest tickets drop through the board until four survive; a tape reel rewinds the survivors to their starting numbers; the same four with new random numbers turn red. A dial reads accuracy. Schematic.",
  body: [body],
});

const tint = (cls, c, shade = 80) => {
  const mix = (p, w) => `color-mix(in srgb, ${c} ${p}%, ${w})`;
  const tones = [mix(62, "#000"), mix(shade, "#000"), c, c];
  const sel = `.iso .iso-solid.${cls}`;
  return `${sel}>.iso-fill,${sel}>.iso-top{fill:${c};stroke:var(--anatomy-hi)}\n` + tones.map((t, i) => `${sel}>.iso-shade[data-shade="${i}"]{fill:${t};stroke:${t}}`).join("\n") + "\n";
};
const flat = (cls, fill) => `.${cls}{fill:${fill};stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}\n`;
const css = k.ISO_CSS + `
.iso .iso-solid.tb-y>.iso-fill,.iso .iso-solid.tb-y>.iso-top{fill:var(--anatomy-lit-top);stroke:var(--anatomy-hi)}
.iso .iso-solid.tb-y>.iso-shade{fill:var(--anatomy-lit-shade);stroke:var(--anatomy-lit-shade)}
.tb-ink{fill:var(--anatomy-hi);stroke:none}
.tb-needle{fill:var(--anatomy-red);stroke:var(--anatomy-hi);stroke-width:2px;stroke-linejoin:round;vector-effect:non-scaling-stroke}
.tb-spoke{fill:var(--anatomy-mid);stroke:var(--anatomy-hi);stroke-width:var(--anatomy-weight);stroke-linejoin:round;vector-effect:non-scaling-stroke}
` + flat("tb-slot", "var(--anatomy-mid)") + flat("tb-face", "var(--anatomy-shade-3)")
  + flat("tb-start", "color-mix(in srgb, var(--anatomy-blue) 28%, #fff)") + flat("tb-fresh", "color-mix(in srgb, var(--anatomy-red) 45%, #fff)")
  + flat("tb-trained", "var(--anatomy-blue)") + flat("tb-trained-red", "color-mix(in srgb, var(--anatomy-red) 85%, #000)");

const pose = (kitScript() + `
const P = ${JSON.stringify(P)};
const C = { dial: [${DIAL.x}, ${DIAL.y}, ${DLZ + 0.8}], dr: ${DIAL.r - 7}, reel: [${REEL.x}, ${REEL.y}, ${RLZ + 0.6}], rr: ${REEL.r - 9} };
const SURV = ${JSON.stringify(SURVIVORS)}, RANK = ${JSON.stringify(RANK)}, N = ${N * N}, DROP = 26;
const q = {};
const part = (svg, n) => (q[n] = q[n] && svg.contains(q[n]) ? q[n] : svg.querySelector('[data-part="' + n + '"]'));
const cl = (u) => Math.min(1, Math.max(0, u));
const sm = (u) => { u = cl(u); return u * u * (3 - 2 * u); };
const op = (el, v) => { el.style.opacity = v <= 0.001 ? "0" : v >= 0.999 ? "1" : v.toFixed(3); };
const path = (pts) => pts.map((p, i) => { const [x, y] = iso(p, P); return (i ? "L" : "M") + x.toFixed(1) + " " + y.toFixed(1); }).join("") + "Z";
window.__ANP[${JSON.stringify(NAME)}] = {
  init: { train: 0, prune: 0, rewind: 0, again: 0, fresh: 0, lit: 0, acc: 0.12 },
  apply(svg, s, t) {
    // train: every chip deepens from its light start colour to deep blue (red for the survivors' fresh numbers)
    for (let i = 0; i < N; i++) {
      const sv = SURV.indexOf(i);
      if (sv < 0) {
        op(part(svg, "tk" + i + "-trained"), s.train);
        // prune: the weakest drop through the board in turn, then fade
        const f = cl((s.prune * 34 - RANK[i]) / 2), g = part(svg, "tk" + i), u = sm(f);
        g.setAttribute("transform", translateAlong(P, [0, 0, -DROP * u]));
        op(g, 1 - sm(f * 1.4 - 0.4));
      } else {
        // survivors: rewind sets the trained look back to the start numbers; fresh swaps them for new random ones
        const tr = Math.max(s.train * (1 - s.rewind), s.again);
        op(part(svg, "sv" + sv + "-fresh"), s.fresh);
        op(part(svg, "sv" + sv + "-trained"), tr * (1 - s.fresh));
        op(part(svg, "sv" + sv + "-trainedred"), tr * s.fresh);
        op(part(svg, "lit" + sv), s.lit);
      }
    }
    // rewind: the reel turns two full turns backwards
    const a = -s.rewind * 4 * Math.PI, sp = [];
    for (let j = 0; j < 3; j++) {
      const b = a + (j * 2 * Math.PI) / 3, dx = Math.cos(b), dy = Math.sin(b), px = -dy, py = dx, [rx, ry, rz] = C.reel;
      sp.push(path([[rx + 6 * dx + 3 * px, ry + 6 * dy + 3 * py, rz], [rx + C.rr * dx + 3.4 * px, ry + C.rr * dy + 3.4 * py, rz], [rx + C.rr * dx - 3.4 * px, ry + C.rr * dy - 3.4 * py, rz], [rx + 6 * dx - 3 * px, ry + 6 * dy - 3 * py, rz]]));
    }
    part(svg, "spokes").setAttribute("d", sp.join(""));
    // acc: the dial needle sweeps 250 degrees
    const d = ((-125 + 250 * cl(s.acc) - 90) * Math.PI) / 180, [dx, dy] = [Math.cos(d), Math.sin(d)], [px, py] = [-dy, dx], [ox, oy, oz] = C.dial;
    part(svg, "needle").setAttribute("d", path([[ox + 3 * px, oy + 3 * py, oz], [ox + C.dr * dx + 0.8 * px, oy + C.dr * dy + 0.8 * py, oz], [ox + C.dr * dx - 0.8 * px, oy + C.dr * dy - 0.8 * py, oz], [ox - 3 * px, oy - 3 * py, oz]]));
  },
};
`).replaceAll("<script", "<\\u0073cript").replaceAll("</script", "<\\/script");

writeFileSync(join(HERE, `${NAME}.svg`), svg);
writeFileSync(join(HERE, `${NAME}.css`), css);
writeFileSync(join(HERE, `${NAME}.pose.js`), pose);
const anchors = {
  board: [BOARD.x + BOARD.w / 2, BOARD.y + BOARD.d / 2, BZ + TK_H],
  ticket: [cellX(SURVIVORS[1] % N), cellY(Math.floor(SURVIVORS[1] / N)), BZ + TK_H + 4],
  tray: [TRAY.x + TRAY.w / 2, TRAY.y + TRAY.d, Z0 + 5],
  dial: [DIAL.x, DIAL.y, DLZ],
  reel: [REEL.x, REEL.y, RLZ],
  front: [BOARD.x + BOARD.w, BOARD.y + BOARD.d / 2, BZ],
};
writeFileSync(join(HERE, `${NAME}.json`), JSON.stringify({ width: WIDTH, height: HEIGHT,
  params: {
    train: "0..1 every chip deepens from light blue (its starting number) to deep blue (trained); survivors' chips follow",
    prune: "0..1 the weakest 32 tickets drop through the board in turn, leaving four",
    rewind: "0..1 the reel turns two turns back and the survivors' chips return to their light starting colour",
    again: "0..1 the survivors train again from where the rewind left them (chips deepen; with fresh they deepen to dark red)",
    fresh: "0..1 the survivors swap their starting numbers for new random ones (red); with train they deepen to dark red",
    lit: "0..1 the four survivors turn yellow: the winning ticket",
    acc: "0..1 the dial needle (accuracy); rest 0.12",
  },
  anchors: Object.fromEntries(Object.entries(anchors).map(([n, p]) => [n, at(p).map(r1)])) }, null, 1));
console.log("wrote", NAME, svg.length, "bytes", WIDTH, "x", HEIGHT, "scale", P.scale.toFixed(3));

if (process.argv.includes("--preview")) {
  const t = Number(process.argv[process.argv.indexOf("--preview") + 1]) || 0;
  const st = { train: 0, prune: 0, rewind: 0, again: 0, fresh: 0, lit: 0, acc: 0.12 };
  const args = process.argv.find((a) => a.startsWith("--state="));
  if (args) Object.assign(st, JSON.parse(args.slice(8)));
  const vars = "--anatomy-paper:#FFFFFF;--anatomy-face:#FFFFFF;--anatomy-top:#FFFFFF;--anatomy-shade-0:#C4BAA6;--anatomy-shade-1:#D4CBB9;--anatomy-shade-2:#E3DCCD;--anatomy-shade-3:#F1ECE2;--anatomy-hi:#121212;--anatomy-mid:#3D3932;--anatomy-lo:#5A554B;--anatomy-faint:#B3AA98;--anatomy-lit:#121212;--anatomy-lit-top:#FFD23F;--anatomy-lit-shade:#F0B90F;--anatomy-halo:#6F6552;--anatomy-halo-opacity:.30;--anatomy-dot:#121212;--anatomy-weight:3.2px;--anatomy-red:#D7392B;--anatomy-green:#13965A;--anatomy-blue:#2C5BEA";
  const page = `<!doctype html><html><head><meta charset="utf-8"><style>${css}body{margin:0;background:#F4EFE4}.an{width:860px;margin:20px auto;${vars}}</style></head><body><div class="an iso" data-theme="dark" id="f">${svg}</div><script>window.__ANP={};${pose};window.__ANP["${NAME}"].apply(document.querySelector("svg"),${JSON.stringify(st)},${t});</script></body></html>`;
  writeFileSync(join(HERE, "preview.html"), page);
  console.log("preview.html");
}
