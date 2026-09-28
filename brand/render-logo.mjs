import { chromium } from 'playwright';
import fs from 'fs';

const NAME = process.env.BRAND_NAME || 'Margalla Global';
const TAG = process.env.BRAND_TAG || 'Recruitment & Consultancy';
const OUT = new URL('../website/assets/img/', import.meta.url).pathname;
const mark = fs.readFileSync(OUT + 'logo-mark.svg', 'utf8');

const fonts = '<style>' + fs.readFileSync(new URL('./fonts-inline.css', import.meta.url), 'utf8') + '</style>';
const css = `*{margin:0;box-sizing:border-box}html,body{background:transparent}
.lock{display:inline-flex;align-items:center;gap:34px;padding:40px 56px}
.lock svg{width:170px;height:170px;flex:none}
.name{font:800 108px/0.95 "Bricolage Grotesque";letter-spacing:-.025em}
.tag{font:500 27px/1 "IBM Plex Mono";letter-spacing:.2em;text-transform:uppercase;margin-top:18px}
.dark{background:#0A1B25}.dark .name{color:#E8EFEC}.dark .tag{color:#93A9A7}
.light .name{color:#0F2330}.light .tag{color:#12704F}
.stack{display:inline-flex;flex-direction:column;align-items:center;gap:26px;padding:50px 60px;text-align:center}
.stack svg{width:220px;height:220px}
.markbox{width:512px;height:512px;display:grid;place-items:center;background:#0A1B25;border-radius:110px}
.markbox svg{width:380px;height:380px}
.markonly svg{width:512px;height:512px;display:block}
.og{width:1200px;height:630px;background:radial-gradient(800px 500px at 80% 30%,#123444,#0A1B25 65%);position:relative;overflow:hidden;display:flex;align-items:center;padding:0 90px;color:#E8EFEC;font-family:Figtree}
.og .grid{position:absolute;inset:0;background-image:radial-gradient(rgba(200,225,218,.12) 1.2px,transparent 1.4px);background-size:26px 26px}
.og .in{position:relative;display:grid;gap:34px}
.og .lock{padding:0}
.og .lock svg{width:130px;height:130px}.og .name{font-size:84px}.og .tag{font-size:22px;color:#93A9A7}
.og p{font:500 30px/1.35 Figtree;color:#C9D6D3;max-width:820px}
.og p b{color:#3DBB8A;font-weight:500}
.og .hex{position:absolute;right:-80px;bottom:-90px;width:520px;opacity:.18}`;

const lockup = (cls) => `<div class="lock ${cls}">${mark}<div><div class="name">${NAME}</div><div class="tag">${TAG}</div></div></div>`;
const pages = {
  'logo-horizontal-dark.png': lockup('dark'),
  'logo-horizontal.png': lockup('light'),
  'logo-horizontal-white.png': `<div class="lock" style="--x:0">${mark}<div><div class="name" style="color:#fff">${NAME}</div><div class="tag" style="color:#CFE3DC">${TAG}</div></div></div>`,
  'logo-stacked.png': `<div class="stack light">${mark}<div><div class="name">${NAME}</div><div class="tag">${TAG}</div></div></div>`,
  'logo-mark-512.png': `<div class="markbox">${mark}</div>`,
  'logo-mark-transparent.png': `<div class="markonly">${mark}</div>`,
  'og-image.png': `<div class="og"><div class="grid"></div><div class="hex">${mark}</div><div class="in">${lockup('')}<p>Blue-collar manpower for employers in <b>Pakistan, the Gulf, Europe and Central Asia</b>.</p></div></div>`
};

const b = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
const ctx = await b.newContext({ deviceScaleFactor: 2 });
for (const [file, body] of Object.entries(pages)) {
  const p = await ctx.newPage();
  await p.setContent(`<!doctype html><html><head>${fonts}<style>${css}</style></head><body>${body}</body></html>`, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const ok = await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family).join(','));
  const el = await p.$('body > *:not(link)');
  await el.screenshot({ path: OUT + file, omitBackground: true });
  console.log(file, 'font loaded:', ok);
  await p.close();
}
await b.close();
