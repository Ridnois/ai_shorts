/**
 * Splitter: one word lies on a board as a bar already scored into four pieces of unequal length, the way a model reads
 * a word as tokens. The pointer picks the nearest seam; a blade drops into it and the pieces part outwards from it, the
 * nearer first. At rest the blade hovers over the bar and is the bright mark. The read-out names the seam; the slider
 * is how wide the pieces part.
 *
 * The pattern: one of many. Tweens for the blade and the gap (a choice, rule 08), a stagger by distance from the seam
 * (rule 02), and a hit test on the seams' rest screen x, which never moves (rule 01).
 */
const { Cam, facing, fit, prism, proj, rrect, seg, tween, tset, tval, tdone, disposer, mk, put, solid, pointer, reflect, register } = HL;

const LEN = [16, 27, 12, 22], BH = 12, BD = 16, SEAM = 0.9, LIFT = BH + 14, CUT = 2, BLADE = 22, REST_K = 2;
const D = [Math.cos(Math.PI / 6), -Math.sin(Math.PI / 6)], E = [Math.sin(Math.PI / 6), Math.cos(Math.PI / 6)];   // 15° off level
const at = (t, e) => [t * D[0] + e * E[0], t * D[1] + e * E[1]];
function along(t0, e0, t1, e1, r, n = 6) {
  return rrect(t0, e0, t1, e1, r, n).map((q) => { const [u, v] = at(q.u, q.v), [nu, nv] = at(q.nu, q.nv); return { ...q, u, v, nu, nv }; });
}

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let gap = value;
  const W = LEN.reduce((a, b) => a + b, 0) + SEAM * (LEN.length - 1), T0 = -W / 2;
  const start = LEN.map((_, i) => T0 + LEN.slice(0, i).reduce((a, b) => a + b, 0) + SEAM * i);
  const seamT = start.slice(1).map((s) => s - SEAM / 2);              // seam k (1..3) sits before piece k

  const C = Cam(45, 0.5, 2.6);
  fit(C, [[...at(T0 - 16, -BD), -4], [...at(-T0 + 16, BD), -4], [...at(T0 - 16, BD), -4], [...at(-T0 + 16, -BD), LIFT + BLADE + 6], [...at(T0, -BD), LIFT + BLADE + 6]], 200, 166);
  const P = proj(C), front = facing(C);
  const q = (t, e, z) => P(...at(t, e), z);

  const g = mk("g", {}, svg);
  const board = along(T0 - 16, -BD, -T0 + 16, BD, 6), boardIn = along(T0 - 14.5, -BD + 1.5, -T0 + 14.5, BD - 1.5, 4.5);
  reflect(svg, g, P, front, board, -4, 12);
  put(solid(g), prism(P, front, board, boardIn, -4, 0));

  const pieces = LEN.map((len, i) => {
    const grp = mk("g", {}, g), s = solid(grp), mark = mk("path", { class: "nf lo" }, grp);
    return { len, t0: start[i], grp, s, mark, dx: tween(0), last: NaN };
  });
  const blade = { grp: mk("g", {}, g), t: tween(seamT[REST_K - 1]), z: tween(LIFT), last: "" };
  blade.s = solid(blade.grp); blade.h = solid(blade.grp);           // the blade, and its handle along the top
  blade.s.sil.classList.add("hi");                                    // the blade is the one bright thing (rule 04)

  function drawPiece(p, dx) {
    const t0 = p.t0 + dx, t1 = t0 + p.len;
    put(p.s, prism(P, front, along(t0, -BD / 2, t1, BD / 2, 2.2), along(t0 + 1, -BD / 2 + 1, t1 - 1, BD / 2 - 1, 1.2), 0, BH));
    p.mark.setAttribute("d", seg(q(t0 + 3, 0, BH), q(t1 - 3, 0, BH)));   // the printed run on the piece's top: its one mark
  }

  const B = register(stage, (_dt, now) => {
    let moving = false;
    for (const p of pieces) {
      const dx = tval(p.dx, now);
      if (dx !== p.last) { drawPiece(p, dx); p.last = dx; }
      if (!tdone(p.dx, now)) moving = true;
    }
    const bt = tval(blade.t, now), bz = tval(blade.z, now), key = bt + "," + bz;
    if (key !== blade.last) {
      put(blade.s, prism(P, front, along(bt - 0.7, -BD / 2 - 6, bt + 0.7, BD / 2 + 6, 0.6, 3), along(bt - 0.3, -BD / 2 - 5.6, bt + 0.3, BD / 2 + 5.6, 0.25, 3), bz, bz + BLADE));
      put(blade.h, prism(P, front, along(bt - 2.2, -7, bt + 2.2, 7, 2), along(bt - 1.2, -6, bt + 1.2, 6, 1.1), bz + BLADE, bz + BLADE + 5));
      blade.last = key;
    }
    if (!tdone(blade.t, now) || !tdone(blade.z, now)) moving = true;
    return moving;
  });
  bag.add(B.unregister);

  let act = -2;
  const sx = seamT.map((t) => q(t, 0, BH)[0]), ends = [q(T0, 0, BH)[0] - 10, q(-T0, 0, BH)[0] + 10];
  function hit(x) {
    if (x < ends[0] || x > ends[1]) return -1;
    let best = 0;
    sx.forEach((s, k) => { if (Math.abs(s - x) < Math.abs(sx[best] - x)) best = k; });
    return best + 1;
  }
  function choose(k) {
    if (k === act) return;
    act = k;
    const now = performance.now(), from = k > 0 ? k : REST_K;
    pieces.forEach((p, i) => tset(p.dx, k < 0 ? 0 : i < k ? -gap / 2 : gap / 2, now, Math.abs(i + 0.5 - from) * 45));
    tset(blade.t, seamT[from - 1], now, 0);
    tset(blade.z, k < 0 ? LIFT : CUT, now, 0);
    // the blade is painted just behind the piece after its seam while it cuts, above every piece while it hovers (rule 06)
    if (k > 0) pieces[k - 1].grp.after(blade.grp); else pieces[pieces.length - 1].grp.after(blade.grp);
    read.textContent = k < 0 ? "rest" : "seam " + k;
    B.wake();
  }
  choose(-1);
  bag.add(pointer(stage, { move: ([x]) => choose(hit(x)), leave: () => choose(-1) }));
  bag.add(() => svg.replaceChildren());

  return { set: (v) => { gap = v; const k = act; act = -2; choose(k); }, destroy: bag.dispose };
}

hairline({
  name: "splitter",
  means: "A word as a bar scored into token pieces: point at a seam and a blade drops in as the pieces part.",
  rules: [1, 2, 6, 8],
  range: [3, 6, 10],
  tour: [[150, 170], [235, 150], [275, 140], null],
  mount,
});
