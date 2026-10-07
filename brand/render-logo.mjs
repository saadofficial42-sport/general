// Renders the final RS Links Consultants logo files into website/assets/img/.
//   npm i playwright && node brand/render-logo.mjs
import { chromium } from 'playwright';
import fs from 'fs';

const DIR = new URL('./', import.meta.url).pathname;
const OUT = DIR + '../website/assets/img/';
const seal = fs.readFileSync(OUT + 'logo-seal.svg', 'utf8');
const icon = fs.readFileSync(OUT + 'logo-mark.svg', 'utf8');
const fonts = '<style>' + fs.readFileSync(DIR + 'fonts-inline.css', 'utf8') + '</style>';

const css = `*{margin:0;box-sizing:border-box}html,body{background:transparent}
.lock{display:inline-flex;align-items:center;gap:38px;padding:44px 60px}
.lock svg{width:200px;height:200px;flex:none}
.name{font:800 112px/.95 "Bricolage Grotesque";letter-spacing:-.025em;color:#0F2330}
.name i{font-style:normal;color:#0B4A34}
.tag{font:500 28px/1 "IBM Plex Mono";letter-spacing:.2em;text-transform:uppercase;margin-top:20px;color:#12704F}
.dark{background:#0A1B25}.dark .name{color:#E8EFEC}.dark .name i{color:#2FAE78}.dark .tag{color:#93A9A7}
.white .name,.white .name i{color:#fff}.white .tag{color:#E3EFEA}
.stack{display:inline-flex;flex-direction:column;align-items:center;gap:30px;padding:50px 70px;text-align:center}
.stack svg{width:300px;height:300px}
.app{width:512px;height:512px;display:grid;place-items:center;background:#0A1B25;border-radius:112px}
.app svg{width:430px;height:430px}
.solo{display:inline-block}.solo svg{width:800px;height:800px;display:block}
.fav{display:inline-block}.fav svg{width:256px;height:256px;display:block}
.og{width:1200px;height:630px;background:radial-gradient(800px 500px at 80% 30%,#123444,#0A1B25 65%);position:relative;overflow:hidden;display:flex;align-items:center;padding:0 90px;font-family:Figtree}
.og .grid{position:absolute;inset:0;background-image:radial-gradient(rgba(200,225,218,.12) 1.2px,transparent 1.4px);background-size:26px 26px}
.og .in{position:relative;display:grid;gap:36px}
.og .lock{padding:0}.og .lock svg{width:170px;height:170px}.og .name{font-size:88px;color:#E8EFEC}.og .name i{color:#2FAE78}.og .tag{font-size:22px;color:#93A9A7}
.og p{font:500 30px/1.35 Figtree;color:#C9D6D3;max-width:820px}.og p b{color:#3DBB8A;font-weight:500}
.og .ghost{position:absolute;right:-120px;bottom:-140px;width:560px;opacity:.12}`;

const lock = cls => `<div class="lock ${cls}">${seal}<div><div class="name"><i>RS</i> Links</div><div class="tag">Consultants Pvt. Ltd.</div></div></div>`;
const pages = {
  'logo-horizontal.png': lock(''),
  'logo-horizontal-dark.png': lock('dark'),
  'logo-horizontal-white.png': lock('white'),
  'logo-stacked.png': `<div class="stack">${seal}<div><div class="name"><i>RS</i> Links</div><div class="tag">Consultants Pvt. Ltd.</div></div></div>`,
  'logo-seal.png': `<div class="solo">${seal}</div>`,
  'logo-mark-512.png': `<div class="app">${seal}</div>`,
  'logo-icon.png': `<div class="fav">${icon}</div>`,
  // solid white backgrounds (for documents, printing, WhatsApp/DP uploads)
  'logo-seal-white-bg.png': `<div style="background:#fff;padding:120px;display:inline-block;line-height:0"><div class="solo">${seal}</div></div>`,
  'logo-horizontal-white-bg.png': `<div style="background:#fff;padding:40px 30px;display:inline-block">${lock('')}</div>`,
  'og-image.png': `<div class="og"><div class="grid"></div><div class="ghost">${icon}</div><div class="in">${lock('')}<p>Manpower recruitment &amp; consultancy. Linking Pakistan's workforce with employers in <b>the Gulf, Europe and Central Asia</b>.</p></div></div>`
};

const b = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
const ctx = await b.newContext({ deviceScaleFactor: 2 });
for (const [file, body] of Object.entries(pages)) {
  const p = await ctx.newPage();
  await p.setContent(`<!doctype html><html><head>${fonts}<style>${css}</style></head><body>${body}</body></html>`);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(150);
  await (await p.$('body > *')).screenshot({ path: OUT + file, omitBackground: true });
  await p.close();
  console.log('wrote', file);
}
await b.close();
