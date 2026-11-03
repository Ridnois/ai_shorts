// Attention desk: the attention of one word as a mixing desk. Fifteen channel strips stand in a row, one per piece of the
// sentence "The trophy doesn't fit in the suitcase because it is too big." (the tokens of bert-base-uncased, "doesn't" is
// three pieces summed); each strip's slider cap rides a post to a height set by the real attention weight the word "it"
// gave that piece, averaged over the model's 144 heads (run 3 Nov 2026, Media/…/run/attention.json). In front, a bus bar
// shows the blend: one segment per channel, as wide as its weight, the 100 % that "it" is mixed from. `swap` moves the
// caps from the "too big" weights to the "too small" weights: they barely move. Schematic of a real measurement.
// node build.mjs [--preview [t]] [--state='{"levels":1}']  ->  attention-desk.svg .json .css .pose.js (+ preview.html)
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../../../.claude/skills/anatomy/kit/iso-kit.mjs";
import * as G from "../../../.claude/skills/anatomy/kit/lathe.mjs";
import { kitScript } from "../../../.claude/skills/anatomy/scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const NAME = "attention-desk";
const WIDTH = 600;

// the real numbers: attention from "it", mean over 12 layers x 12 heads, bert-base-uncased, 3 Nov 2026
// pieces: [CLS] the trophy doesn't(3 pieces) fit in the suitcase because it is too big|small . [SEP]
const WB = [0.0892, 0.0371, 0.0601, 0.1223, 0.0243, 0.0215, 0.0336, 0.0427, 0.0784, 0.0323, 0.0733, 0.0367, 0.0553, 0.0625, 0.2307];
const WS = [0.0891, 0.0377, 0.0607, 0.1195, 0.027, 0.0223, 0.0344, 0.0438, 0.0777, 0.0315, 0.0708, 0.036, 0.0558, 0.0664, 0.2272];
const N = WB.length, WMAX = 0.2307, TROPHY = 2, SUIT = 7, IT = 9, BIG = 12, SEP = 14;

const BASE = { x: -290, y: -118, w: 580, d: 232, r: 8 }, BASE_H = 12, Z0 = BASE_H;
const PITCH = 35, CX0 = -245, cx = (i) => CX0 + i * PITCH;                // channel centres along x
const STRIP = { w: 31, d: 118, y: -104 }, STRIP_H = 5;                    // each strip's plate
const POST = { w: 8, d: 8, y: -62 }, TR = 104, POST_H = TR + 18, CAPZ = Z0 + STRIP_H + 4;
const CAP = { w: 25, d: 22, h: 11 };
const BUS = { y: 40, d: 30, h: 9, x0: -250, span: 500 };
const bx = (i) => BUS.x0 + BUS.span * WB.slice(0, i).reduce((a, b) => a + b, 0);

const TOP = CAPZ + TR + CAP.h + 6;
const EXTREMES = [...k.boxCorners(BASE, 0, BASE_H), ...k.boxCorners({ x: cx(0) - 20, y: STRIP.y, w: cx(N - 1) - cx(0) + 40, d: BUS.y + BUS.d - STRIP.y }, 0, TOP)];
const VIEW = { azimuth: 52, elevation: 36 };
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

function base() {
  const o = [slab(BASE, 0, BASE_H, { crease: "none" })];
  for (const [x, y] of [[BASE.x + 12, BASE.y + 12], [BASE.x + BASE.w - 12, BASE.y + 12], [BASE.x + 12, BASE.y + BASE.d - 12], [BASE.x + BASE.w - 12, BASE.y + BASE.d - 12]])
    o.push(screw(x, y, Z0));
  // label plate on the front strip, three rule lines
  const y0 = BUS.y + BUS.d + 12, x0 = BASE.x + 26;
  o.push(slab({ x: x0, y: y0, w: 92, d: 26, r: 2 }, Z0, 1.6, { crease: "none" }));
  for (const [i, e] of [[0, 0], [1, 18], [2, 34]]) o.push(poly([[x0 + 10, y0 + 6 + i * 6.4, Z0 + 1.6], [x0 + 82 - e, y0 + 6 + i * 6.4, Z0 + 1.6], [x0 + 82 - e, y0 + 8.6 + i * 6.4, Z0 + 1.6], [x0 + 10, y0 + 8.6 + i * 6.4, Z0 + 1.6]], "ad-ink"));
  return o.join("");
}

// one strip: plate, post with a tick every 13, a groove behind the post, two screws
function channel(i) {
  const x = cx(i), o = [];
  o.push(slab({ x: x - STRIP.w / 2, y: STRIP.y, w: STRIP.w, d: STRIP.d, r: 2 }, Z0, STRIP_H, { crease: "none" }));
  o.push(slab({ x: x - 5, y: POST.y - 14, w: 10, d: 44, r: 3 }, Z0 + STRIP_H, 1.2, { crease: "none", className: "ad-k" }));   // the slot the cap rides in
  o.push(slab({ x: x - POST.w / 2, y: POST.y, w: POST.w, d: POST.d, r: 1 }, Z0 + STRIP_H, POST_H));
  const Y = POST.y + POST.d;
  for (let t = 0; t <= 8; t++) { const z = CAPZ + 6 + t * 13, w = t % 4 === 0 ? 3.2 : 1.8; o.push(poly([[x - w, Y, z], [x + w, Y, z], [x + w, Y, z + 1.6], [x - w, Y, z + 1.6]], "ad-ink")); }
  o.push(screw(x, STRIP.y + 8, Z0 + STRIP_H), screw(x, STRIP.y + STRIP.d - 8, Z0 + STRIP_H));
  return `<g data-part="ch-${i}">${o.join("")}</g>`;
}

// the slider cap, built at its rest height (level 0) and lifted by the pose; overlays: tint (own colour), lit/sink (yellow), swap (red)
function cap(i) {
  const x = cx(i), y = POST.y + POST.d / 2 - CAP.d / 2, plan = { x: x - CAP.w / 2, y, w: CAP.w, d: CAP.d, r: 3 };
  const body = (cls) => S(k.slabOf({ r: 3, ...plan }, CAPZ, CAP.h, P, 4), { tone: "hi", crease: "none", className: cls });
  const o = [body()];
  if (i === TROPHY) o.push(`<g data-part="tint-t" style="opacity:0">${body("ad-b")}</g>`);
  if (i === SUIT) o.push(`<g data-part="tint-s" style="opacity:0">${body("ad-k2")}</g>`);
  if (i === IT) o.push(`<g data-part="lit" style="opacity:0">${body("ad-y")}</g>`);
  if (i === SEP) o.push(`<g data-part="sink" style="opacity:0">${body("ad-y")}</g>`);
  if (i === BIG) o.push(`<g data-part="swap" style="opacity:0">${body("ad-r")}</g>`);
  // a grip line across the cap's front face and a pointer notch on its top
  const Y = y + CAP.d;
  o.push(poly([[x - CAP.w / 2 + 4, Y, CAPZ + 4.6], [x + CAP.w / 2 - 4, Y, CAPZ + 4.6], [x + CAP.w / 2 - 4, Y, CAPZ + 6.2], [x - CAP.w / 2 + 4, Y, CAPZ + 6.2]], "ad-ink"));
  o.push(poly([[x - 1, y + 5, CAPZ + CAP.h], [x + 1, y + 5, CAPZ + CAP.h], [x + 1, y + CAP.d - 5, CAPZ + CAP.h], [x - 1, y + CAP.d - 5, CAPZ + CAP.h]], "ad-ink"));
  return `<g data-part="cap-${i}">${o.join("")}</g>`;
}

// the bus: a long trough with one segment per channel, as wide as its weight
function bus() {
  const o = [slab({ x: BUS.x0 - 8, y: BUS.y - 6, w: BUS.span + 16, d: BUS.d + 12, r: 3 }, Z0, 3, { crease: "none", className: "ad-k" })];
  const segs = [];
  for (let i = 0; i < N; i++) {
    const x = bx(i), w = Math.max(2, BUS.span * WB[i] - 1.4);
    const cls = i === TROPHY ? "ad-b" : i === SUIT ? "ad-k2" : undefined;
    let g = S(k.slabOf({ x, y: BUS.y, w, d: BUS.d, r: 0.8 }, Z0 + 3, BUS.h, P, 3), { tone: "hi", crease: "none", className: cls });
    if (i === SEP) g += `<g data-part="bus-sink" style="opacity:0">${S(k.slabOf({ x, y: BUS.y, w, d: BUS.d, r: 0.8 }, Z0 + 3, BUS.h, P, 3), { tone: "hi", crease: "none", className: "ad-y" })}</g>`;
    segs.push(`<g data-part="seg-${i}" style="opacity:0">${g}</g>`);
  }
  // end stops of the trough
  const stops = [BUS.x0 - 8, BUS.x0 + BUS.span + 2].map((x) => slab({ x, y: BUS.y - 6, w: 6, d: BUS.d + 12, r: 1 }, Z0 + 3, BUS.h + 4));
  return o.join("") + segs.join("") + stops.join("");
}

const body = [base(), ...Array.from({ length: N }, (_, i) => channel(i)), ...Array.from({ length: N }, (_, i) => cap(i)), bus()].join("");

const svg = k.figureSvg({
  width: WIDTH, height: HEIGHT,
  label: "An attention desk: fifteen channel strips on a base, one per piece of the sentence about a trophy and a suitcase. Each slider cap rides a post to the height of the attention the word it gave that piece. A bus bar in front shows the blend as fifteen segments as wide as their weights.",
  body: [body],
});

const tint = (cls, c, shade = 80) => {
  const mix = (p, w) => `color-mix(in srgb, ${c} ${p}%, ${w})`;
  const tones = [mix(62, "#000"), mix(shade, "#000"), c, c];
  const sel = `.iso .iso-solid.${cls}`;
  return `${sel}>.iso-fill,${sel}>.iso-top{fill:${c};stroke:var(--anatomy-hi)}\n` + tones.map((t, i) => `${sel}>.iso-shade[data-shade="${i}"]{fill:${t};stroke:${t}}`).join("\n") + "\n";
};
const css = k.ISO_CSS + tint("ad-b", "var(--anatomy-blue)") + tint("ad-r", "var(--anatomy-red)") + tint("ad-k2", "#3D3932", 88) + tint("ad-k", "var(--anatomy-shade-2)", 90) + `
.iso .iso-solid.ad-y>.iso-fill,.iso .iso-solid.ad-y>.iso-top{fill:var(--anatomy-lit-top);stroke:var(--anatomy-hi)}
.iso .iso-solid.ad-y>.iso-shade{fill:var(--anatomy-lit-shade);stroke:var(--anatomy-lit-shade)}
.ad-ink{fill:var(--anatomy-hi);stroke:none}
`;

const pose = (kitScript() + `
const P = ${JSON.stringify(P)};
const N = ${N}, WB = ${JSON.stringify(WB)}, WS = ${JSON.stringify(WS)}, WMAX = ${WMAX}, TR = ${TR};
const q = {};
const part = (svg, n) => (q[n] = q[n] && svg.contains(q[n]) ? q[n] : svg.querySelector('[data-part="' + n + '"]'));
const cl = (u) => Math.min(1, Math.max(0, u));
const sm = (u) => { u = cl(u); return u * u * (3 - 2 * u); };
const op = (el, v) => { if (el) el.style.opacity = v <= 0.001 ? "0" : v >= 0.999 ? "1" : v.toFixed(3); };
window.__ANP[${JSON.stringify(NAME)}] = {
  init: { levels: 0, mix: 0, swap: 0, tint: 0, tints: 0, lit: 0, sink: 0 },
  apply(svg, s, t) {
    // levels: the caps rise to the real weights (staggered left to right); swap blends the big weights into the small ones
    for (let i = 0; i < N; i++) {
      const w = WB[i] + (WS[i] - WB[i]) * cl(s.swap), u = sm(s.levels * 1.6 - i * 0.04 * 1.6);
      part(svg, "cap-" + i).setAttribute("transform", translateAlong(P, [0, 0, TR * (w / WMAX) * u]));
      op(part(svg, "seg-" + i), sm(s.mix * (N + 3) - i));
    }
    op(part(svg, "tint-t"), sm(s.tint)); op(part(svg, "tint-s"), sm(s.tints));
    op(part(svg, "lit"), sm(s.lit)); op(part(svg, "sink"), sm(s.sink)); op(part(svg, "bus-sink"), sm(s.sink));
    op(part(svg, "swap"), sm(s.swap * 2));
  },
};
`).replaceAll("<script", "<\\u0073cript").replaceAll("</script", "<\\/script");

writeFileSync(join(HERE, `${NAME}.svg`), svg);
writeFileSync(join(HERE, `${NAME}.css`), css);
writeFileSync(join(HERE, `${NAME}.pose.js`), pose);
const capTop = (i) => [cx(i), POST.y + POST.d / 2, CAPZ + CAP.h + TR * WB[i] / WMAX];
const anchors = { trophy: capTop(TROPHY), suitcase: capTop(SUIT), it: capTop(IT), big: capTop(BIG), sep: capTop(SEP), doesnt: capTop(3),
  bus: [0, BUS.y + BUS.d, Z0 + 3 + BUS.h], busTrophy: [bx(TROPHY) + BUS.span * WB[TROPHY] / 2, BUS.y + BUS.d, Z0 + 3 + BUS.h],
  busSuitcase: [bx(SUIT) + BUS.span * WB[SUIT] / 2, BUS.y + BUS.d, Z0 + 3 + BUS.h], busSep: [bx(SEP) + BUS.span * WB[SEP] / 2, BUS.y + BUS.d, Z0 + 3 + BUS.h], desk: [0, -20, Z0 + 40] };
writeFileSync(join(HERE, `${NAME}.json`), JSON.stringify({ width: WIDTH, height: HEIGHT,
  params: {
    levels: "0..1 the 15 slider caps rise from the strip plates to the real attention weights from 'it' (bert-base-uncased, mean of 144 heads, 3 Nov 2026), staggered left to right",
    mix: "0..1 the bus bar fills left to right: one segment per channel, as wide as its weight (they add to 100 %)",
    swap: "0..1 the weights move from the 'too big' run to the 'too small' run (caps shift by under 0.4 points) and the 'big' cap turns red",
    tint: "0..1 the trophy cap takes its colour (blue); its bus segment is always blue",
    tints: "0..1 the suitcase cap takes its colour (dark); its bus segment is always dark",
    lit: "0..1 the cap of the word 'it' turns yellow",
    sink: "0..1 the end-marker cap and its bus segment turn yellow (23 % of the attention)",
  },
  data: { source: "Media/Week 05/…/AI attention explained/run/attention.json", model: "bert-base-uncased", date: "2026-11-03", pieces: ["[CLS]", "the", "trophy", "doesn't", "fit", "in", "the", "suitcase", "because", "it", "is", "too", "big|small", ".", "[SEP]"], big: WB, small: WS },
  anchors: Object.fromEntries(Object.entries(anchors).map(([n, p]) => [n, at(p).map(r1)])) }, null, 1));
console.log("wrote", NAME, svg.length, "bytes", WIDTH, "x", HEIGHT, "scale", P.scale.toFixed(3));

if (process.argv.includes("--preview")) {
  const t = Number(process.argv[process.argv.indexOf("--preview") + 1]) || 0;
  const st = { levels: 0, mix: 0, swap: 0, tint: 0, tints: 0, lit: 0, sink: 0 };
  const args = process.argv.find((a) => a.startsWith("--state="));
  if (args) Object.assign(st, JSON.parse(args.slice(8)));
  const vars = "--anatomy-paper:#FFFFFF;--anatomy-face:#FFFFFF;--anatomy-top:#FFFFFF;--anatomy-shade-0:#C4BAA6;--anatomy-shade-1:#D4CBB9;--anatomy-shade-2:#E3DCCD;--anatomy-shade-3:#F1ECE2;--anatomy-hi:#121212;--anatomy-mid:#3D3932;--anatomy-lo:#5A554B;--anatomy-faint:#B3AA98;--anatomy-lit:#121212;--anatomy-lit-top:#FFD23F;--anatomy-lit-shade:#F0B90F;--anatomy-halo:#6F6552;--anatomy-halo-opacity:.30;--anatomy-dot:#121212;--anatomy-weight:3.2px;--anatomy-red:#D7392B;--anatomy-green:#13965A;--anatomy-blue:#2C5BEA";
  const page = `<!doctype html><html><head><meta charset="utf-8"><style>${css}body{margin:0;background:#F4EFE4}.an{width:860px;margin:20px auto;${vars}}</style></head><body><div class="an iso" data-theme="dark" id="f">${svg}</div><script>window.__ANP={};${pose};window.__ANP["${NAME}"].apply(document.querySelector("svg"),${JSON.stringify(st)},${t});</script></body></html>`;
  writeFileSync(join(HERE, "preview.html"), page);
  console.log("preview.html");
}
