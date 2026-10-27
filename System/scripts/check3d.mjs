// Overlap check for HyperFrames pages with a three.js canvas: samples the timeline every 0.25 s and reports
//   3D vs text   (projected object boxes, window.__boxes3d, against every visible .ov element)
//   3D vs band   (objects inside the caption band)
//   text vs text (visible .ov elements that are not nested in each other)
// and warns (exit code unchanged) for Style.md rules the eye misses on a sheet:
//   SMALL TEXT   visible text under 40 px outside captions and cards (Style: legible at phone size)
//   SPARSE       everything but the captions (text, 3D and .art illustrations) covers under a quarter of the stage (y 192 to 1440) for over 3 s in a row
// Usage: node check3d.mjs [index.html]     exit code 1 when anything overlaps. Shared copy: System/scripts/check3d.mjs
// ponytail: puppeteer-core and Chrome are borrowed from the hyperframes npx cache; pin them if this becomes a tool.
import { createRequire } from "module";
import { execSync } from "child_process";
import path from "path";

const npx = execSync("ls -d $HOME/.npm/_npx/*/node_modules/puppeteer-core | head -1").toString().trim();
const chrome = execSync("ls $HOME/.cache/hyperframes/chrome/chrome-headless-shell/*/chrome-headless-shell-linux64/chrome-headless-shell | head -1").toString().trim();
const puppeteer = createRequire(import.meta.url)(npx);
const file = path.resolve(process.argv[2] || "index.html");

const browser = await puppeteer.launch({ executablePath: chrome, headless: true, args: ["--no-sandbox", "--allow-file-access-from-files", "--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
const page = await browser.newPage();
await page.setViewport({ width: 1080, height: 1920 });
page.on("pageerror", e => console.log("PAGE ERROR", e.message));
await page.goto("file://" + file, { waitUntil: "networkidle0" });
for (let k = 0; ; k++) {                              // waitForFunction stalls here; a plain evaluate loop does not
  if (await page.evaluate(() => !!(window.__ready3d && window.__timelines && window.__timelines.main))) break;
  if (k > 120) throw new Error("page never became ready (window.__ready3d)");
  await new Promise(r => setTimeout(r, 500));
}
await page.evaluate(() => document.fonts.ready);

const res = await page.evaluate(() => {
  const tl = window.__timelines.main, dur = tl.duration(), band = [0, 880, 1080, 1040];
  const hit = (a, b, m = 4) => a[0] < b[2] - m && a[2] > b[0] + m && a[1] < b[3] - m && a[3] > b[1] + m;
  const clipOn = (el, t) => { for (let e = el; e && e.dataset; e = e.parentElement) if (e.classList.contains("clip")) {
      const s = +e.dataset.start, d = +e.dataset.duration; if (t < s || t >= s + d) return false; } return true; };
  const alpha = el => { let a = 1; for (let e = el; e && e !== document.body; e = e.parentElement) a *= +getComputedStyle(e).opacity; return a; };
  const found = {}, warn = {}, stage = 1080 * (1440 - 192);
  const warnAt = (t, k) => { (warn[k] = warn[k] || []).push(+t.toFixed(2)); };
  const note = (t, k) => { (found[k] = found[k] || []).push(+t.toFixed(2)); };
  for (let t = 0; t < dur; t += 0.25) {
    tl.seek(t, false); window.__render3d && window.__render3d(t);
    const els = [...document.querySelectorAll(".ov")].filter(e => clipOn(e, t) && alpha(e) > 0.05)
      .map(e => { const r = e.getBoundingClientRect(); return { id: e.id || e.className, el: e, r: [r.left, r.top, r.right, r.bottom] }; });
    const gl = document.getElementById("gl"), glOn = gl && clipOn(gl, t) && alpha(gl) > 0.05;
    const b3 = glOn ? (window.__boxes3d || []) : [];
    for (const b of b3) { if (hit(b, band)) note(t, "3D in caption band"); for (const e of els) if (hit(b, e.r)) note(t, `3D vs ${e.id}`); }
    for (let i = 0; i < els.length; i++) for (let j = i + 1; j < els.length; j++) {
      const a = els[i], b = els[j]; if (a.el.contains(b.el) || b.el.contains(a.el)) continue;
      const inside = (x, y) => x.r[0] >= y.r[0] && x.r[1] >= y.r[1] && x.r[2] <= y.r[2] && x.r[3] <= y.r[3];
      if ((b.el.classList.contains("box") && inside(a, b)) || (a.el.classList.contains("box") && inside(b, a))) continue;   // held fully by a frame
      if ((a.el.classList.contains("box") && b.el.classList.contains("mover")) || (b.el.classList.contains("box") && a.el.classList.contains("mover"))) continue;   // a mover crosses frames by design
      if (hit(a.r, b.r)) note(t, `${a.id} vs ${b.id}`); }
    for (const e of els) if (hit(e.r, band, 0) && !e.el.closest("#caps")) note(t, `${e.id} in caption band`);
    for (const e of els) for (const n of [e.el, ...e.el.querySelectorAll("*")])
      if ([...n.childNodes].some(c => c.nodeType === 3 && c.textContent.trim()) && !n.closest("#caps, [id*=card]")   // cards keep the approved Style sizes
          && parseFloat(getComputedStyle(n).fontSize) < 40) warnAt(t, `SMALL TEXT ${parseFloat(getComputedStyle(n).fontSize)} px in ${e.id}`);
    const art = [...document.querySelectorAll(".art")].filter(e => clipOn(e, t) && alpha(e) > 0.05)    // illustrations fill the frame too
      .map(e => { const r = e.getBoundingClientRect(); return [r.left, r.top, r.right, r.bottom]; });
    const boxes = [...els.filter(e => !e.el.closest("#caps")).map(e => e.r), ...b3, ...art];
    if (boxes.length) {                                // bounding box of the picture, not its ink: generous on purpose
      const x0 = Math.min(...boxes.map(b => b[0])), y0 = Math.max(192, Math.min(...boxes.map(b => b[1])));
      const x1 = Math.max(...boxes.map(b => b[2])), y1 = Math.min(1440, Math.max(...boxes.map(b => b[3])));
      if ((x1 - x0) * Math.max(0, y1 - y0) < stage / 4) warnAt(t, "SPARSE frame");
    } else warnAt(t, "SPARSE frame");
    for (const e of els) { if (e.r[2] > 952) note(t, `${e.id} in the right interface strip (x > 950)`);      // Style.md lanes: the app's buttons
                           if (e.r[3] > 1442) note(t, `${e.id} in the bottom interface zone (y > 1440)`); }
  }
  return { found, warn };
});
await browser.close();
const { found, warn } = res, keys = Object.keys(found);
for (const k of keys) console.log(`OVERLAP ${k}: ${found[k].length} samples, ${found[k][0]} to ${found[k][found[k].length - 1]} s`);
const longest = ts => { let best = [0, ts[0], ts[0]], a = ts[0];            // longest unbroken run of 0.25 s samples
  for (let i = 1; i <= ts.length; i++) if (i === ts.length || ts[i] - ts[i - 1] > 0.26) {
    if (ts[i - 1] - a + 0.25 > best[0]) best = [ts[i - 1] - a + 0.25, a, ts[i - 1]]; a = ts[i]; } return best; };
for (const [k, ts] of Object.entries(warn)) {
  const [run, a, b] = longest(ts);
  if (!k.startsWith("SPARSE") || run > 3)
    console.log(`WARN ${k}: ${(ts.length * 0.25).toFixed(1)} s in all, longest ${run.toFixed(2)} s (${a} to ${b} s)`); }
console.log(keys.length ? `${keys.length} overlap kinds` : "OVERLAPS 0");
process.exit(keys.length ? 1 : 0);
