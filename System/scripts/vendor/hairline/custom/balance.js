/**
 * Balance: a beam balance with an answer slip standing in each pan, the picture of people choosing between two answers
 * (RLHF). The pointer leans to a side of the post; the beam tips so that pan rises, and its slip takes the bright edge.
 * At rest the beam leans a little and the pivot cap is the bright mark. The read-out names the choice; the slider is
 * how far the beam tips, in degrees.
 *
 * The pattern: one of two. A tween for the tip (a choice, rule 08); the choice is read from the post's rest screen x,
 * which never moves (rule 01).
 */
const { Cam, circ, facing, fillet, fit, poly, prism, proj, rad, rings, seg, tween, tset, tval, tdone, disposer, mk, put, solid, pointer, reflect, register } = HL;

const L = 62, ZB = 66, DROP = 28, PR = 19, BH = 3, SW = 15, SH = 21, POST = 4.5, REST = -4;
const shift = (ring, cx, cy) => ring.map((q) => ({ ...q, u: q.u + cx, v: q.v + cy }));
const D = [Math.SQRT1_2, -Math.SQRT1_2], E = [Math.SQRT1_2, Math.SQRT1_2];   // the beam runs along x − y: level on screen, so its tip reads

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let tip = value;

  const C = Cam(45, 0.5, 2.0);
  const hiZ = ZB + L * Math.sin(rad(24));
  const at = (t, e, z) => [t * D[0] + e * E[0], t * D[1] + e * E[1], z];
  fit(C, [at(-L - PR, 0, 0), at(L + PR, 0, 0), at(0, -30, 0), at(0, 30, 0), at(-L, 0, hiZ + 4), at(L, 0, hiZ + 4), at(-L, 0, ZB - L * Math.sin(rad(24)) - DROP)], 200, 166);
  const P = proj(C), front = facing(C);

  const g = mk("g", {}, svg);
  const [br, bi] = rings(-26, -26, 26, 26, 8, 1.5);
  reflect(svg, g, P, front, br, 0, 12);
  put(solid(g), prism(P, front, br, bi, 0, 5));

  /** A pan with its slip and its two rods; side -1 is the far (left) one, painted before the post. */
  function panParts(side) {
    const grp = mk("g", {}, g);
    const rods = mk("path", { class: "nf" }, grp), pan = solid(grp), slip = mk("path", { class: "sil" }, grp), rule = mk("path", { class: "nf lo" }, grp);
    return { side, grp, rods, pan, slip, rule };
  }
  const [pr, pi] = rings(-POST, -POST, POST, POST, 3, 1);
  put(solid(g), prism(P, front, pr, pi, 5, ZB - 2));
  const left = panParts(-1), right = panParts(1);
  const beamTop = mk("path", { class: "sil" }, g), beamFace = mk("path", { class: "sil" }, g);
  const cap = solid(g);
  put(cap, prism(P, front, circ(5, 24), circ(3.8, 24), ZB - 2, ZB + 3));

  const tw = tween(REST);
  const SLIP = fillet([[-SW / 2, 0], [SW / 2, 0], [SW / 2, SH], [-SW / 2, SH]], [1, 1, 2.5, 2.5]);

  function draw(th) {
    const c = Math.cos(rad(th)), s = Math.sin(rad(th));
    const end = (side) => [side * L * c, ZB - side * L * s];        // th > 0 lifts the left pan
    const [tl, zl] = end(-1), [tr, zr] = end(1);
    const q = (t, e, z) => P(...at(t, e, z));
    beamTop.setAttribute("d", poly([q(tl, -1.6, zl), q(tr, -1.6, zr), q(tr, 1.6, zr), q(tl, 1.6, zl)]));
    beamFace.setAttribute("d", poly([q(tl, 1.6, zl), q(tr, 1.6, zr), q(tr, 1.6, zr - 2.6), q(tl, 1.6, zl - 2.6)]));
    for (const p of [left, right]) {
      const [t, z] = end(p.side), zp = z - DROP, [cx, cy] = at(t, 0, 0);
      p.rods.setAttribute("d", seg(q(t - PR * 0.8, 0, zp + BH), q(t, 0, z)) + seg(q(t + PR * 0.8, 0, zp + BH), q(t, 0, z)));
      put(p.pan, prism(P, front, shift(circ(PR, 32), cx, cy), shift(circ(PR - 1.4, 32), cx, cy), zp, zp + BH));
      p.slip.setAttribute("d", poly(SLIP.map(([u, v]) => q(t + u, 0, zp + BH + v))));
      p.rule.setAttribute("d", [7, 11, 15].map((v) => seg(q(t - SW / 2 + 3, 0, zp + BH + v), q(t + SW / 2 - 3, 0, zp + BH + v))).join(""));
    }
  }

  let last = NaN;
  const B = register(stage, (_dt, now) => {
    const th = tval(tw, now);
    if (th !== last) { draw(th); last = th; }
    return !tdone(tw, now);
  });
  bag.add(B.unregister);

  let act = -2;
  const px = P(0, 0, ZB)[0];
  function choose(a) {
    if (a === act) return;
    act = a;
    tset(tw, a < 0 ? REST : a === 0 ? tip : -tip, performance.now(), 0);
    left.slip.classList.toggle("hi", a === 0); right.slip.classList.toggle("hi", a === 1);
    cap.sil.classList.toggle("hi", a < 0);
    read.textContent = a < 0 ? "rest" : a === 0 ? "A preferred" : "B preferred";
    B.wake();
  }
  choose(-1);
  bag.add(pointer(stage, { move: ([sx]) => choose(sx < px - 8 ? 0 : sx > px + 8 ? 1 : -1), leave: () => choose(-1) }));
  bag.add(() => svg.replaceChildren());

  return { set: (v) => { tip = v; const a = act; act = -2; choose(a); }, destroy: bag.dispose };
}

hairline({
  name: "balance",
  means: "Two answers on a beam balance: lean to one and its pan rises, the way people pick the better answer.",
  rules: [1, 4, 5, 8],
  range: [8, 14, 22],
  tour: [[120, 150], [290, 170], [200, 120], null],
  mount,
});
