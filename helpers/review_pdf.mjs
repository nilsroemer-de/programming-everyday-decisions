// Review-PDFs der Folien: Druckansicht von RevealJS mit Sprechernotizen auf einer eigenen
// Seite nach jeder Folie (?print-pdf&showNotes=separate-page), gedruckt über das Chrome
// DevTools Protocol, weil der direkte --print-to-pdf das Layout der Druckansicht nicht abwartet.
// Voraussetzungen: _site/ gerendert, chrome-headless-shell (quarto install chrome-headless-shell),
// Node 22+ (globales WebSocket). Aufruf: zsh helpers/review_pdf.sh [deck ...]
import { spawn } from 'node:child_process';
import { writeFileSync, mkdirSync } from 'node:fs';
import { homedir } from 'node:os';

const [port, outDir, ...decks] = process.argv.slice(2);
const CHROME = `${homedir()}/Library/Application Support/quarto/chrome-headless-shell/chrome-headless-shell-mac-arm64/chrome-headless-shell`;
mkdirSync(outDir, { recursive: true });

const proc = spawn(CHROME, ['--headless', '--disable-gpu', '--no-sandbox', '--remote-debugging-port=0', 'about:blank'], { stdio: ['ignore', 'pipe', 'pipe'] });
const wsUrl = await new Promise((resolve, reject) => {
  let buf = '';
  proc.stderr.on('data', (d) => { buf += d.toString(); const m = buf.match(/DevTools listening on (ws:\/\/\S+)/); if (m) resolve(m[1]); });
  setTimeout(() => reject(new Error('chrome start timeout\n' + buf)), 15000);
});
const ws = new WebSocket(wsUrl);
await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
let id = 0;
const pending = new Map();
const listeners = new Set();
ws.onmessage = (ev) => {
  const msg = JSON.parse(ev.data);
  if (msg.id && pending.has(msg.id)) { const { res, rej } = pending.get(msg.id); pending.delete(msg.id); msg.error ? rej(new Error(JSON.stringify(msg.error))) : res(msg.result); }
  else if (msg.method) listeners.forEach((l) => l(msg));
};
const send = (method, params = {}, sessionId) => new Promise((res, rej) => { const i = ++id; pending.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method, params, sessionId })); });
const { targetId } = await send('Target.createTarget', { url: 'about:blank' });
const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
const s = (m, p) => send(m, p, sessionId);
await s('Page.enable');
await s('Runtime.enable');
await s('Emulation.setDeviceMetricsOverride', { width: 1200, height: 800, deviceScaleFactor: 1, mobile: false });
const evaluate = async (expression) => (await s('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true })).result.value;

for (const d of decks) {
  const loaded = new Promise((res) => { const l = (m) => { if (m.method === 'Page.loadEventFired' && m.sessionId === sessionId) { listeners.delete(l); res(); } }; listeners.add(l); });
  await s('Page.navigate', { url: `http://127.0.0.1:${port}/${d.startsWith('tut_') ? 'tutorials' : 'lectures'}/${d}_presentation.html?print-pdf&showNotes=separate-page` });
  await loaded;
  // wait until reveal has laid out the print pages and the fonts are ready
  await evaluate(`(async () => { for (let i = 0; i < 100; i++) { if (document.querySelectorAll('.pdf-page').length > 0 && document.fonts.status === 'loaded') break; await new Promise(r => setTimeout(r, 200)); } await new Promise(r => setTimeout(r, 1500)); })()`);
  const pages = await evaluate(`document.querySelectorAll('.pdf-page').length`);
  // reveal 5 inserts the notes of a slide as .speaker-notes-pdf[data-layout=separate-page] after its page
  const notes = await evaluate(`document.querySelectorAll('.speaker-notes-pdf[data-layout="separate-page"]').length`);
  const r = await s('Page.printToPDF', { printBackground: true, preferCSSPageSize: true, displayHeaderFooter: false });
  const file = `${outDir}/${d}-review.pdf`;
  writeFileSync(file, Buffer.from(r.data, 'base64'));
  console.log(`${file}: ${pages} pages (${notes} notes pages)`);
}
ws.close();
proc.kill();
