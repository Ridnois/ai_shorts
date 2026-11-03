// Scripted browser capture for proof footage (Build: Kit, Captures). Called by capture.py; writes numbered JPEG frames (Chrome screencast)
// and frames.json ([[file, seconds since start], ...]) into an output folder while a list of steps runs.
// Usage: node capture.mjs <script.json> <out dir>
// script.json: {"url": "https://...", "viewport": [540, 960], "scale": 2, "steps": [
//   {"wait": 2}, {"waitFor": "css selector"}, {"click": "css selector"}, {"type": ["css selector", "text", 60]},
//   {"press": "Enter"}, {"scroll": 400}, {"eval": "js expression"}, {"hold": 1.5}]}
// A 540x960 viewport at scale 2 gives 1080x1920 frames with phone-sized text. puppeteer-core and Chrome are borrowed
// from the hyperframes npx cache, as check3d.mjs does.
import { createRequire } from "module";
import { execSync } from "child_process";
import fs from "fs";
import path from "path";

const npx = execSync("ls -d $HOME/.npm/_npx/*/node_modules/puppeteer-core | head -1").toString().trim();
const chrome = execSync("ls $HOME/.cache/hyperframes/chrome/chrome-headless-shell/*/chrome-headless-shell-linux64/chrome-headless-shell | head -1").toString().trim();
const puppeteer = createRequire(import.meta.url)(npx);
const [scriptFile, out] = process.argv.slice(2);
const S = JSON.parse(fs.readFileSync(scriptFile, "utf8"));
fs.mkdirSync(out, { recursive: true });
const [vw, vh] = S.viewport || [540, 960];
const browser = await puppeteer.launch({ executablePath: chrome, headless: true,
  args: ["--no-sandbox", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--hide-scrollbars"] });
const page = await browser.newPage();
await page.setViewport({ width: vw, height: vh, deviceScaleFactor: S.scale || 2 });
await page.goto(S.url, { waitUntil: "networkidle2", timeout: 90000 });

const frames = [];                 // Chrome's own screencast: a frame each time the page paints (smooth, not polled)
let n = 0, t0 = null;
const cdp = await page.createCDPSession();
cdp.on("Page.screencastFrame", async f => {
  const t = f.metadata.timestamp; if (t0 === null) t0 = t;
  const name = `f${String(n++).padStart(5, "0")}.jpg`;
  fs.writeFileSync(path.join(out, name), Buffer.from(f.data, "base64"));
  frames.push([name, t - t0]);
  await cdp.send("Page.screencastFrameAck", { sessionId: f.sessionId }).catch(() => {});
});
await cdp.send("Page.startScreencast", { format: "jpeg", quality: 92, maxWidth: vw * (S.scale || 2), maxHeight: vh * (S.scale || 2), everyNthFrame: 1 });
const tStart = Date.now();
const sleep = s => new Promise(r => setTimeout(r, s * 1000));
for (const st of S.steps || []) {
  if (st.wait !== undefined) await sleep(st.wait);
  else if (st.hold !== undefined) await sleep(st.hold);
  else if (st.waitFor) await page.waitForSelector(st.waitFor, { timeout: 60000 });
  else if (st.click) await page.click(st.click);
  else if (st.type) await page.type(st.type[0], st.type[1], { delay: st.type[2] || 60 });
  else if (st.press) await page.keyboard.press(st.press);
  else if (st.scroll !== undefined) await page.evaluate(y => window.scrollBy({ top: y, behavior: "smooth" }), st.scroll);
  else if (st.eval) await page.evaluate(st.eval);
}
await cdp.send("Page.stopScreencast");
frames.push(["end", (Date.now() - tStart) / 1000]);          // the last frame holds until the steps ended
fs.writeFileSync(path.join(out, "frames.json"), JSON.stringify(frames));
await browser.close();
console.log(`CAPTURE ${frames.length - 1} frames over ${frames.at(-1)[1].toFixed(1)} s`);
