/**
 * Window: a tape of sixteen word blocks on a plinth, and a frame of four thin rails floating over a span of them. The
 * pointer's place along the tape slides the frame (a spring); the blocks under it stand tall, the rest lie low, each at
 * its own height like words of different lengths. The read-out names the span; the slider is the frame's length in blocks.
 *
 * The pattern: a field along one axis. The pointer is read on the ground plane, which never moves (rule 01); one spring
 * for the frame and one per block, so the blocks follow the frame as it glides.
 */
const { Cam, clamp, facing, fit, proj, prism, rings, seg, unproj, spring, stepS, disposer, mk, put, solid, pointer, reflect, register } = HL;

const N = 16, BW = 9, GAP = 3, BD = 14, STEP = BW + GAP, L = N * STEP - GAP;
const LOW = [3, 5, 2, 4, 6, 3, 2, 5, 4, 3, 6, 2, 4, 5, 3, 2];   // word lengths: rest is uneven, never a flat row (rule 05)
const RISE = 16, ZF = 6 + RISE + 6, RAIL = 2.2, PAD = 3;
const REST_C = 4.6 * STEP;                                         // at rest the window sits over the first third

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let span = value;

  const C = Cam(45, 0.5, 1.78);
  fit(C, [[-6, -6, -4], [L + 6, BD + 6, -4], [-6, BD + 6, -4], [L + 6, -6, ZF + RAIL], [-6, -6, ZF + RAIL]], 200, 170);
  const P = proj(C), front = facing(C);

  const g = mk("g", {}, svg);
  const [pr, pi] = rings(-6, -6, L + 6, BD + 6, 5, 1.5);
  reflect(svg, g, P, front, pr, -4, 12);
  put(solid(g), prism(P, front, pr, pi, -4, 0));

  const blocks = [];
  for (let i = 0; i < N; i++) {
    const [r, inn] = rings(i * STEP, 0, i * STEP + BW, BD, 2.2, 1);
    const s = solid(g);
    blocks.push({ r, inn, s, line: mk("path", { class: "nf lo" }, s.g), x: i * STEP, h: spring(LOW[i]), last: -1 });
  }
  // the frame: back rail, the two ends, front rail, painted back to front above every block
  const rails = [0, 1, 2, 3].map(() => solid(g));

  const frame = spring(REST_C);
  const lo = () => (span * STEP) / 2;
  const inside = (i, c) => Math.abs(i * STEP + BW / 2 - c) < lo();

  function drawFrame(c) {
    const x0 = c - lo() - PAD, x1 = c + lo() + PAD - GAP, y0 = -PAD - 1, y1 = BD + PAD + 1;
    const parts = [[x0, y0, x1, y0 + RAIL], [x0, y0, x0 + RAIL, y1], [x1 - RAIL, y0, x1, y1], [x0, y1 - RAIL, x1, y1]];
    parts.forEach(([a, b, cc, d], k) => { const [r, inn] = rings(a, b, cc, d, 1, 0.5); put(rails[k], prism(P, front, r, inn, ZF, ZF + RAIL)); });
  }
  rails.forEach((s) => s.sil.classList.add("hi"));                 // the frame is the one bright thing, at rest and moving (rule 04)

  let lastC = -1;
  function caption(c) {
    const lit = blocks.map((_, i) => i).filter((i) => inside(i, c));
    return lit.length ? `${String(lit[0] + 1).padStart(2, "0")}–${String(lit[lit.length - 1] + 1).padStart(2, "0")}` : "rest";
  }

  const B = register(stage, (dt) => {
    let moving = stepS(frame, dt);
    const c = frame.x;
    blocks.forEach((b, i) => {
      b.h.t = LOW[i] + (inside(i, frame.t) ? RISE : 0);            // targets come from the frame's target, not its pose (rule 01)
      if (stepS(b.h, dt)) moving = true;
      if (Math.abs(b.h.x - b.last) > 0.01) {
        put(b.s, prism(P, front, b.r, b.inn, 0, b.h.x));
        b.line.setAttribute("d", seg(P(b.x + 2.5, BD / 2, b.h.x), P(b.x + BW - 2.5, BD / 2, b.h.x)));   // the tile's printed run, its one mark
        b.last = b.h.x;
      }
    });
    if (Math.abs(c - lastC) > 0.01) { drawFrame(c); lastC = c; }
    return moving;
  });
  bag.add(B.unregister);

  let touched = false;
  function slide(c) {
    frame.t = clamp(c, lo() - BW / 2, L - lo() + BW / 2);
    read.textContent = touched ? caption(frame.t) : "rest";
    B.wake();
  }
  bag.add(pointer(stage, {
    move: ([sx, sy]) => { touched = true; slide(unproj(C, sx, sy, 0)[0]); },
    leave: () => { touched = false; slide(REST_C); },
  }));
  read.textContent = "rest";
  bag.add(() => svg.replaceChildren());

  return {
    set: (v) => { span = v; lastC = -1; slide(frame.t); },
    destroy: bag.dispose,
  };
}

hairline({
  name: "window",
  means: "A frame slides over a tape of word blocks: only the blocks inside it stand up; the rest lie flat.",
  rules: [1, 3, 5, 8],
  range: [4, 6, 9],
  tour: [[150, 150], [215, 182], [275, 212], null],
  mount,
});
