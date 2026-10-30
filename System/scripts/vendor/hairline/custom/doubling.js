/**
 * Doubling: ten columns stand in a row on a tray, one per switch added to a puzzle. Each back column is twice as tall as
 * the one before it: the settings to try double with every switch, so the first few are stubs and the last ones tower
 * (the exponential wall). With the claim shown (value 1), a front row stands before it whose heights grow on a slower
 * curve, 2^(n / sqrt(log2(n + 2))): a drawing of the shape of a subexponential bound, not to scale (the paper's bound
 * hides constants). The pointer's x is the puzzle size: columns left of it stand, the rest wait as flat stubs. The
 * tallest standing back column takes the bright edge; with the claim shown, the front row takes it instead.
 *
 * The pattern: a field driven by one choice. The size is picked from the pointer's screen x, which no drawing moves
 * (rule 01); each column rides a spring to its height (a choice lands on a spring, rule 08).
 */
const { Cam, clamp, facing, fit, prism, proj, rrect, disposer, mk, put, solid, spring, stepS, pointer, reflect, register } = HL;

const N = 10, STEP = 14, BW = 8.5, UNIT = 0.3, STUB = 0.8;
const BACK = Array.from({ length: N }, (_, i) => UNIT * 2 ** i);                           // 0.3 .. 154
const CLAIM = Array.from({ length: N }, (_, i) => UNIT * 2 ** (i / Math.sqrt(Math.log2(i + 2))));   // 0.3 .. about 9
const D = [Math.cos(Math.PI / 6), -Math.sin(Math.PI / 6)], E = [Math.sin(Math.PI / 6), Math.cos(Math.PI / 6)];
const at = (t, e) => [t * D[0] + e * E[0], t * D[1] + e * E[1]];
function along(t0, e0, t1, e1, r, n = 6) {
  return rrect(t0, e0, t1, e1, r, n).map((q) => {
    const [u, v] = at(q.u, q.v), [nu, nv] = at(q.nu, q.nv);
    return { ...q, u, v, nu, nv };
  });
}

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  const claim = Math.round(value) >= 1;
  const W = (N - 1) * STEP + BW, T0 = -W / 2, T1 = T0 + W;
  const EB = -7, EF = 8;                                                       // the back row and the front row, into the page

  const C = Cam(45, 0.5, 1.7);
  fit(C, [[...at(T0 - 8, -16), -4], [...at(T1 + 8, 18), -4], [...at(T1, EB), BACK[N - 1]], [...at(T0 - 8, 18), -4]], 200, 160);
  const P = proj(C), front = facing(C);

  const g = mk("g", {}, svg);
  const tray = along(T0 - 8, -16, T1 + 8, 18, 6), trayIn = along(T0 - 6.5, -14.5, T1 + 6.5, 16.5, 4.6);
  reflect(svg, g, P, front, tray, -4, 10);
  put(solid(g), prism(P, front, tray, trayIn, -4, 0));

  const col = (i, e) => {
    const t = T0 + i * STEP;
    return { r: along(t, e - BW / 2, t + BW, e + BW / 2, 1.8), inn: along(t + 0.9, e - BW / 2 + 0.9, t + BW - 0.9, e + BW / 2 - 0.9, 1) };
  };
  // painted back to front: the back row first, then the front row
  const back = BACK.map((h, i) => ({ h, ...col(i, EB), s: solid(g), z: spring(STUB), last: -1 }));
  const fore = claim ? CLAIM.map((h, i) => ({ h, ...col(i, EF), s: solid(g), z: spring(STUB), last: -1 })) : [];

  let n = 0, touched = false;
  const B = register(stage, (dt) => {
    let moving = false;
    for (const c of [...back, ...fore]) {
      if (stepS(c.z, dt)) moving = true;
      if (Math.abs(c.z.x - c.last) > 0.02) { put(c.s, prism(P, front, c.r, c.inn, 0, Math.max(STUB, c.z.x))); c.last = c.z.x; }
    }
    return moving;
  });
  bag.add(B.unregister);

  function size(k) {
    k = clamp(k, 0, N);
    if (k === n) return;
    n = k;
    back.forEach((c, i) => { c.z.t = i < n ? c.h : STUB; c.s.sil.classList.toggle("hi", !claim && i === n - 1); });
    fore.forEach((c, i) => { c.z.t = i < n ? c.h : STUB; c.s.sil.classList.toggle("hi", i < n); });   // the claim row: the bright edge
    B.wake();
  }
  function show() { read.textContent = touched ? `${n} switches` : "rest"; }
  size(0); show();
  // the size from the pointer's x: the tray spans about x 60 to 340 of the viewBox
  bag.add(pointer(stage, {
    move: ([sx]) => { touched = true; size(Math.round(clamp((sx - 60) / 280, 0, 1) * N)); show(); },
    leave: () => { touched = false; size(0); show(); },
  }));
  bag.add(() => svg.replaceChildren());

  return { set: () => {}, destroy: bag.dispose };
}

hairline({
  name: "doubling",
  means: "Columns that double with every switch added (the exponential wall); with the claim, a front row on a slower curve.",
  rules: [1, 4, 8],
  range: [0, 0, 1],
  tour: [[80, 160], [200, 160], [340, 160], null],
  mount,
});
