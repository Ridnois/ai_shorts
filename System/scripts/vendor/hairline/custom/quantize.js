/**
 * Quantize: a block of fourteen weights stands as thin pins on a tray, in front of a wall that carries the allowed
 * levels as rails. The pointer's height is the bit depth: near the top (16-bit) the rails are too fine to tell apart
 * and every pin stands at its true height; lower down the rails thin out to 16 (4-bit) and, at the bottom, 4 (2-bit),
 * and each pin snaps to its nearest rail. A dim ring stays at each pin's true height, so the rounding error is the gap
 * between ring and top; the pin that lost the most takes the bright edge. The block at the end of the row is the
 * shared scale: one step between rails, tall when the levels are coarse. The read-out names the bits; the slider is
 * the bit depth the bottom of the stage reaches.
 *
 * The pattern: a field driven by one choice. The bit depth is picked from the pointer's screen height, which no drawing
 * moves (rule 01); the rails' spacing is a tween (a choice, rule 08) and each pin and the scale ride a spring to their
 * snapped targets; levels span the block's own min and max (one scale and one offset per block).
 */
const { Cam, clamp, facing, fit, open, prism, proj, rrect, run, seg, disposer, mk, put, solid, spring, stepS, tween, tset, tval, tdone, pointer, reflect, register } = HL;

const TRUE = [34, 52, 21, 44, 61, 29, 39, 14, 48, 57, 26, 42, 18, 36];   // the weights, baked: their heights in world units
const N = TRUE.length, BW = 5.6, STEP = 10, CAP = 64, REST_B = 4;
const LO = Math.min(...TRUE), HI = Math.max(...TRUE), WALL = HI + 9;
/** Bands of the pointer's screen height, top to bottom: [below this sy, bits]. */
const BANDS = [[110, 16], [140, 5], [190, 4], [228, 3], [262, 2], [Infinity, 1]];
const D = [Math.cos(Math.PI / 6), -Math.sin(Math.PI / 6)], E = [Math.sin(Math.PI / 6), Math.cos(Math.PI / 6)];   // the row runs 15° off level: depth shows
const at = (t, e) => [t * D[0] + e * E[0], t * D[1] + e * E[1]];
/** A rounded rectangle laid along the row: t across it, e into the page. */
function along(t0, e0, t1, e1, r, n = 6) {
  return rrect(t0, e0, t1, e1, r, n).map((q) => {
    const [u, v] = at(q.u, q.v), [nu, nv] = at(q.nu, q.nv);
    return { ...q, u, v, nu, nv };
  });
}
/** Intervals between the levels of a bit depth; past CAP they are drawn as CAP, a stand-in for "too fine to see". */
const gaps = (b) => Math.min(2 ** b, CAP) - 1;
/** Round-to-nearest onto 2^b levels spanning the block's min and max. */
const snap = (h, b) => { const s = (HI - LO) / (2 ** b - 1); return LO + Math.round((h - LO) / s) * s; };

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let floor = Math.round(value);
  const W = (N - 1) * STEP + BW, T0 = -W / 2, T1 = T0 + W, ST0 = T1 + 7, ST1 = ST0 + 11;
  const EW = -BW / 2 - 0.6;                                                // the wall's front face, just behind the pins: a top meets its rail

  const C = Cam(45, 0.5, 1.72);
  fit(C, [[...at(T0 - 8, -20), -4], [...at(ST1 + 8, 12), -4], [...at(T0 - 8, 12), -4], [...at(T0 - 5, EW - 3), WALL], [...at(T1 + 5, EW - 3), WALL], [...at(ST1, -6), 26]], 200, 166);
  const P = proj(C), front = facing(C), back = (q) => !front(q);

  const g = mk("g", {}, svg);
  const tray = along(T0 - 8, -20, ST1 + 8, 12, 7), trayIn = along(T0 - 6.5, -18.5, ST1 + 6.5, 10.5, 5.5);
  reflect(svg, g, P, front, tray, -4, 12);
  put(solid(g), prism(P, front, tray, trayIn, -4, 0));
  const wall = along(T0 - 5, EW - 3, T1 + 5, EW, 1.4), wallIn = along(T0 - 4, EW - 2.2, T1 + 4, EW - 0.8, 0.6);
  put(solid(g), prism(P, front, wall, wallIn, 0, WALL));
  const rails = mk("path", { d: "", class: "nf lo" }, g);
  const railAt = (z) => seg(P(...at(T0 - 3, EW), z), P(...at(T1 + 3, EW), z));

  const pins = TRUE.map((h, i) => {
    const t = T0 + i * STEP, r = along(t, -BW / 2, t + BW, BW / 2, 1.6), inn = along(t + 0.8, -BW / 2 + 0.8, t + BW - 0.8, BW / 2 - 0.8, 0.9);
    const ring = along(t - 1.5, -BW / 2 - 1.5, t + BW + 1.5, BW / 2 + 1.5, 2.6);
    const behind = mk("path", { d: "", class: "nf lo" }, g), s = solid(g), ahead = mk("path", { d: "", class: "nf lo" }, g);
    return { h, r, inn, ring, behind, s, ahead, z: spring(snap(h, REST_B)), last: -1, ghost: "" };
  });
  /** The ghost ring at the pin's true height: wrapped round the pin when the top is above it, whole in the air when not. */
  function ghost(p, top) {
    const key = top >= p.h ? "wrap" : "air";
    if (key === p.ghost) return;
    p.ghost = key;
    const all = "M" + p.ring.map((q) => P(q.u, q.v, p.h).join(",")).join("L") + "Z";
    if (key === "air") { p.behind.setAttribute("d", ""); p.ahead.setAttribute("d", all); }
    else { p.behind.setAttribute("d", open(run(p.ring, back).map((q) => P(q.u, q.v, p.h)))); p.ahead.setAttribute("d", open(run(p.ring, front).map((q) => P(q.u, q.v, p.h)))); }
  }
  const scale = { s: solid(g), z: spring((HI - LO) / (2 ** REST_B - 1)), last: -1 };
  const [sr, si] = [along(ST0, -5.5, ST1, 5.5, 2.4), along(ST0 + 1, -4.5, ST1 - 1, 4.5, 1.4)];

  const dens = tween(Math.log2(gaps(REST_B)));
  let lastD = NaN;
  const B = register(stage, (dt, now) => {
    let moving = false;
    const d = tval(dens, now);
    if (d !== lastD) {
      const n = 2 ** d, step = (HI - LO) / n;
      let path = "";
      for (let k = 0; k <= Math.floor(n + 1e-6); k++) path += railAt(LO + k * step);
      if (n % 1 > 1e-6) path += railAt(HI);                                  // mid-tween, the top level stays where it is
      rails.setAttribute("d", path);
      lastD = d;
    }
    if (!tdone(dens, now)) moving = true;
    for (const p of pins) {
      if (stepS(p.z, dt)) moving = true;
      if (Math.abs(p.z.x - p.last) > 0.02) { put(p.s, prism(P, front, p.r, p.inn, 0, p.z.x)); ghost(p, p.z.x); p.last = p.z.x; }
    }
    if (stepS(scale.z, dt)) moving = true;
    if (Math.abs(scale.z.x - scale.last) > 0.02) { put(scale.s, prism(P, front, sr, si, 0, Math.max(2.2, scale.z.x))); scale.last = scale.z.x; }
    return moving;
  });
  bag.add(B.unregister);

  let bits = -1, touched = false, band = REST_B;
  function quantize(b) {
    b = Math.max(b, floor);
    if (b === bits) return;
    bits = b;
    tset(dens, Math.log2(gaps(b)), performance.now(), 0);
    let worst = 0, we = -1;
    pins.forEach((p, i) => { p.z.t = snap(p.h, b); const e = Math.abs(p.z.t - p.h); if (e > we + 1e-9) { we = e; worst = i; } });
    pins.forEach((p, i) => p.s.sil.classList.toggle("hi", i === worst));   // the pin that lost the most: the one bright edge (rule 04)
    scale.z.t = (HI - LO) / (2 ** b - 1);
    B.wake();
  }
  function show() { read.textContent = touched ? `${bits}-bit` : "rest"; }
  quantize(REST_B); show();
  bag.add(pointer(stage, {
    move: ([, sy]) => { touched = true; band = BANDS.find(([y]) => sy < y)[1]; quantize(band); show(); },
    leave: () => { touched = false; band = REST_B; quantize(REST_B); show(); },
  }));
  bag.add(() => svg.replaceChildren());

  return { set: (v) => { floor = Math.round(clamp(v, 1, 4)); bits = -1; quantize(band); show(); }, destroy: bag.dispose };
}

hairline({
  name: "quantize",
  means: "Weights as pins before rails of allowed levels: fewer bits, fewer rails, and each pin snaps to the nearest one.",
  rules: [1, 4, 5, 8],
  range: [4, 2, 1],
  tour: [[200, 70], [200, 165], [200, 245], null],
  mount,
});
