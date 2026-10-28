/**
 * Loop: an oval track with three stations beside it, plan, act and check, marked by one, two and three dots, and a
 * carriage on the rail: the agent's loop. The pointer picks a station; the carriage rides there, always forwards round
 * the loop, and the station rises and takes the bright edge. At rest the carriage waits between check and plan and is
 * the bright mark. The read-out names the station; the slider is how far a chosen station rises.
 *
 * The pattern: one of a few, on a path. A tween on the carriage's place along the loop and on each station's lift (a
 * choice, rule 08); stations are picked by their rest screen position (rule 01); stations and carriage are re-ordered
 * by depth as the carriage goes round (rule 06).
 */
const { Cam, facing, fit, flatDot, place, prism, proj, rrect, rings, tween, tset, tval, tdone, disposer, mk, put, solid, pointer, reflect, register } = HL;

const RX = 58, RY = 28, HALF = 9, CW = 15, CD = 9, CH = 8, SW = 13, OFF = 22, REST_S = 0.92;
const STATIONS = [{ s: 0.1, h: 10, name: "plan" }, { s: 0.43, h: 17, name: "act" }, { s: 0.76, h: 13, name: "check" }];

/** The rail's centre line: an even ring of points with outward normals, and a lookup by place s in [0, 1). */
function path() {
  const ring = rrect(-RX, -RY, RX, RY, RY, 24), pts = ring.map((q) => [q.u, q.v, q.nu, q.nv]);
  const cum = [0];
  for (let i = 1; i <= pts.length; i++) { const a = pts[i - 1], b = pts[i % pts.length]; cum.push(cum[i - 1] + Math.hypot(b[0] - a[0], b[1] - a[1])); }
  const total = cum[cum.length - 1];
  return (s) => {
    const d = (((s % 1) + 1) % 1) * total;
    let i = 1;
    while (cum[i] < d) i++;
    const a = pts[i - 1], b = pts[i % pts.length], span = cum[i] - cum[i - 1], f = span > 0 ? (d - cum[i - 1]) / span : 0;   // the corner samples meet: a step may be empty
    return { x: a[0] + (b[0] - a[0]) * f, y: a[1] + (b[1] - a[1]) * f, nx: a[2] + (b[2] - a[2]) * f, ny: a[3] + (b[3] - a[3]) * f };
  };
}
/** A rounded box footprint turned to angle a about (cx, cy). */
function turned(cx, cy, w, d, r, a) {
  const c = Math.cos(a), s = Math.sin(a);
  return rrect(-w / 2, -d / 2, w / 2, d / 2, r, 5).map((q) => ({ ...q, u: cx + q.u * c - q.v * s, v: cy + q.u * s + q.v * c, nu: q.nu * c - q.nv * s, nv: q.nu * s + q.nv * c }));
}

function mount({ stage, svg, read }, value) {
  const bag = disposer();
  let lift = value;
  const at = path();

  const C = Cam(45, 0.5, 2.45);
  fit(C, [[-RX - HALF - OFF, -RY - HALF - OFF, -3], [RX + HALF + OFF, RY + HALF + OFF, -3], [-RX - OFF, RY + OFF, 0], [RX + OFF, -RY - OFF, 30]], 200, 162);
  const P = proj(C), front = facing(C);

  const g = mk("g", {}, svg);
  const outer = rrect(-RX - HALF, -RY - HALF, RX + HALF, RY + HALF, RY + HALF, 10), outerIn = rrect(-RX - HALF + 1.5, -RY - HALF + 1.5, RX + HALF - 1.5, RY + HALF - 1.5, RY + HALF - 1.5, 10);
  reflect(svg, g, P, front, outer, -3, 10);
  put(solid(g), prism(P, front, outer, outerIn, -3, 0));
  const hole = rrect(-RX + HALF, -RY + HALF, RX - HALF, RY - HALF, RY - HALF, 10);
  mk("path", { d: "M" + hole.map((q) => P(q.u, q.v, 0).join(",")).join("L") + "Z", class: "nf" }, g);   // the infield's edge
  mk("path", { d: "M" + rrect(-RX, -RY, RX, RY, RY, 10).map((q) => P(q.u, q.v, 0).join(",")).join("L") + "Z", class: "nf lo dash" }, g);   // the rail

  const layer = mk("g", {}, g);
  const stations = STATIONS.map((st, k) => {
    const p = at(st.s), cx = p.x + p.nx * OFF, cy = p.y + p.ny * OFF;
    const grp = mk("g", {}, layer), body = solid(grp);
    const dots = [];
    for (let i = 0; i <= k; i++) dots.push(flatDot(grp, C, 1.3, "dot m"));
    return { ...st, cx, cy, grp, body, dots, z: tween(0), last: NaN, key: cx + cy };
  });
  const car = { grp: mk("g", {}, layer), s: tween(REST_S), last: NaN };
  car.solid = solid(car.grp);

  function drawStation(st, z) {
    const [r, inn] = rings(st.cx - SW / 2, st.cy - SW / 2, st.cx + SW / 2, st.cy + SW / 2, 3, 1);
    put(st.body, prism(P, front, r, inn, z, z + st.h));
    st.dots.forEach((d, i) => place(d, P(st.cx + (i - (st.dots.length - 1) / 2) * 3.4, st.cy, z + st.h)));
  }
  function drawCar(s) {
    const p = at(s), q = at(s + 0.004), a = Math.atan2(q.y - p.y, q.x - p.x);
    const r = turned(p.x, p.y, CW, CD, 2.4, a), inn = turned(p.x, p.y, CW - 2, CD - 2, 1.4, a);
    put(car.solid, prism(P, front, r, inn, 0.5, 0.5 + CH));
    return p.x + p.y;
  }
  let order = "";
  function sortBy(carKey) {               // back to front by x + y, the carriage among the stations
    const items = [...stations.map((st) => [st.key, st.grp]), [carKey, car.grp]].sort((a, b) => a[0] - b[0]);
    const sig = items.map((i) => (i[1] === car.grp ? "c" : "s")).join("");
    if (sig !== order) { items.forEach((i) => layer.appendChild(i[1])); order = sig; }
  }

  const B = register(stage, (_dt, now) => {
    let moving = false;
    for (const st of stations) {
      const z = tval(st.z, now);
      if (z !== st.last) { drawStation(st, z); st.last = z; }
      if (!tdone(st.z, now)) moving = true;
    }
    const s = tval(car.s, now);
    if (s !== car.last) { sortBy(drawCar(s)); car.last = s; }
    if (!tdone(car.s, now)) moving = true;
    return moving;
  });
  bag.add(B.unregister);

  let act = -2;
  const spot = stations.map((st) => P(st.cx, st.cy, st.h));
  function hit([x, y]) {
    let best = -1, bd = 60;
    spot.forEach(([sx, sy], k) => { const d = Math.hypot(sx - x, sy - y); if (d < bd) { bd = d; best = k; } });
    return best;
  }
  function choose(k) {
    if (k === act) return;
    act = k;
    const now = performance.now(), cur = tval(car.s, now), want = k < 0 ? REST_S : stations[k].s;
    let to = Math.floor(cur) + want;
    if (to < cur - 0.001) to += 1;                                         // always forwards round the loop
    tset(car.s, to, now, 0);
    stations.forEach((st, i) => { tset(st.z, i === k ? lift : 0, now, 0); st.body.sil.classList.toggle("hi", i === k); });
    car.solid.sil.classList.toggle("hi", k < 0);
    read.textContent = k < 0 ? "rest" : stations[k].name;
    B.wake();
  }
  choose(-1);
  bag.add(pointer(stage, { move: (p) => choose(hit(p)), leave: () => choose(-1) }));
  bag.add(() => svg.replaceChildren());

  return { set: (v) => { lift = v; const k = act; act = -2; choose(k); }, destroy: bag.dispose };
}

hairline({
  name: "loop",
  means: "An agent's loop as a track: point at plan, act or check and the carriage rides round to it.",
  rules: [1, 4, 6, 8],
  range: [10, 16, 22],
  tour: [[220, 214], [30, 94], [305, 88], null],
  mount,
});
