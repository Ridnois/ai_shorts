/**
 * Temperature: seven candidate next words stand as bars on a tray, each as tall as its chance. The pointer's height is
 * the sampling temperature: near the bottom (cold) one bar towers and the rest shrink to stubs; near the top (hot) they
 * level out, so any of them could be picked. The likeliest bar keeps the bright edge. The read-out names the
 * temperature; the slider is how hot the top of the stage runs.
 *
 * The pattern: a field driven by one number. Heights are a softmax of fixed scores at the pointer's temperature, one
 * spring per bar (rule 08); the temperature comes from the pointer's screen height, which no drawing moves (rule 01).
 */
const { Cam, clamp, facing, fit, lerp, prism, proj, rrect, disposer, mk, put, solid, spring, stepS, pointer, reflect, register } = HL;

const N = 7, BW = 13, STEP = 19, HMAX = 74, HMIN = 3, COLD = 0.15, REST_T = 0.55;
const SCORE = [1.0, 2.6, 1.5, 0.3, 1.9, 0.6, 0.1];
const TOP = SCORE.indexOf(Math.max(...SCORE));
const D = [Math.cos(Math.PI / 6), -Math.sin(Math.PI / 6)], E = [Math.sin(Math.PI / 6), Math.cos(Math.PI / 6)];   // the row runs 15° off level: depth shows
const at = (t, e) => [t * D[0] + e * E[0], t * D[1] + e * E[1]];
/** A rounded rectangle laid along the row: t across it, e into the page. */
function along(t0, e0, t1, e1, r, n = 6) {
  return rrect(t0, e0, t1, e1, r, n).map((q) => {
    const [u, v] = at(q.u, q.v), [nu, nv] = at(q.nu, q.nv);
    return { ...q, u, v, nu, nv };
  });
}
const heights = (T) => {
  const p = SCORE.map((s) => Math.exp(s / T)), m = Math.max(...p);
  return p.map((x) => HMIN + (HMAX - HMIN) * (x / m));
};

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let hot = value;
  const W = (N - 1) * STEP + BW, T0 = -W / 2;

  const C = Cam(45, 0.5, 2.05);
  fit(C, [[...at(T0 - 9, -12), -4], [...at(-T0 + 9, 12), -4], [...at(T0 - 9, 12), -4], [...at(-T0 + 9, -12), HMAX], [...at(T0, -12), HMAX]], 200, 168);
  const P = proj(C), front = facing(C);

  const g = mk("g", {}, svg);
  const tray = along(T0 - 9, -12, -T0 + 9, 12, 7), trayIn = along(T0 - 7.5, -10.5, -T0 + 7.5, 10.5, 5.5);
  reflect(svg, g, P, front, tray, -4, 12);
  put(solid(g), prism(P, front, tray, trayIn, -4, 0));

  const h0 = heights(REST_T);
  const bars = SCORE.map((_, i) => {
    const t = T0 + i * STEP, r = along(t, -BW / 2, t + BW, BW / 2, 2.4), inn = along(t + 1, -BW / 2 + 1, t + BW - 1, BW / 2 - 1, 1.4);
    const s = solid(g);
    if (i === TOP) s.sil.classList.add("hi");                        // the likeliest word: the one bright edge (rule 04)
    return { r, inn, s, h: spring(h0[i]), last: -1 };
  });

  const B = register(stage, (dt) => {
    let moving = false;
    for (const b of bars) {
      if (stepS(b.h, dt)) moving = true;
      if (Math.abs(b.h.x - b.last) > 0.02) { put(b.s, prism(P, front, b.r, b.inn, 0, b.h.x)); b.last = b.h.x; }
    }
    return moving;
  });
  bag.add(B.unregister);

  let T = REST_T, touched = false;
  function heat(t) {
    T = t;
    heights(T).forEach((h, i) => { bars[i].h.t = h; });
    read.textContent = touched ? `temp ${T.toFixed(1)}` : "rest";
    B.wake();
  }
  read.textContent = "rest";
  bag.add(pointer(stage, {
    move: ([, sy]) => { touched = true; heat(lerp(hot, COLD, clamp((sy - 60) / 200, 0, 1))); },
    leave: () => { touched = false; heat(REST_T); },
  }));
  bag.add(() => svg.replaceChildren());

  return { set: (v) => { hot = v; }, destroy: bag.dispose };
}

hairline({
  name: "temperature",
  means: "Next-word chances as bars: cold, one word towers; hot, they level out and any could be picked.",
  rules: [1, 3, 5, 8],
  range: [1.2, 2, 3],
  tour: [[200, 270], [200, 160], [200, 60], null],
  mount,
});
