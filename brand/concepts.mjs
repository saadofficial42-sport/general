// Renders three logo concepts for RS Links Consultants into brand/concepts/.
//   npm i playwright && node brand/concepts.mjs
import { chromium } from 'playwright';
import fs from 'fs';

const DIR = new URL('./', import.meta.url).pathname;
const OUT = DIR + 'concepts/';
fs.mkdirSync(OUT, { recursive: true });
const fonts = '<style>' + fs.readFileSync(DIR + 'fonts-inline.css', 'utf8') + '</style>';

/* ---------- 1. THE LINK: interlocking chain links in a hex nut ---------- */
const markLink = fs.readFileSync(DIR + '../website/assets/img/logo-mark.svg', 'utf8');

/* ---------- 2. THE SEAL: RS monogram in a consultancy seal ---------- */
const markSeal = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <defs><path id="ring" d="M50 50 m-38 0 a38 38 0 1 1 76 0 a38 38 0 1 1 -76 0"/></defs>
  <circle cx="50" cy="50" r="49" fill="#0A1B25"/>
  <circle cx="50" cy="50" r="46" fill="none" stroke="#F0B545" stroke-width="1.6"/>
  <circle cx="50" cy="50" r="30.5" fill="none" stroke="#3DBB8A" stroke-width="1.2" stroke-opacity=".7"/>
  <text font-family="IBM Plex Mono" font-weight="500" font-size="7.4" letter-spacing="2.15" fill="#C9D6D3">
    <textPath href="#ring" startOffset="0">RS LINKS CONSULTANTS ✦ RAWALPINDI ✦ PAKISTAN ✦</textPath>
  </text>
  <text x="50" y="61" text-anchor="middle" font-family="Bricolage Grotesque" font-weight="800" font-size="31" letter-spacing="-1.5"><tspan fill="#E8EFEC">R</tspan><tspan fill="#F0B545">S</tspan></text>
  <path d="M38 67.5h24" stroke="#3DBB8A" stroke-width="2.2" stroke-linecap="round"/>
</svg>`;

/* ---------- 3. THE ROUTE: an S-shaped route linking two points ---------- */
const markRoute = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect x="2" y="2" width="60" height="60" rx="17" fill="#12704F"/>
  <path d="M17 45H33A7 7 0 0 0 33 31H31A7 7 0 0 1 31 17H47" fill="none" stroke="#fff" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="16" cy="45" r="5.5" fill="#F0B545"/>
  <circle cx="48" cy="17" r="5" fill="#12704F" stroke="#fff" stroke-width="3"/>
</svg>`;

const css = `*{margin:0;box-sizing:border-box}html,body{background:transparent}
.lock{display:inline-flex;align-items:center;gap:34px;padding:44px 60px}
.lock svg{width:170px;height:170px;flex:none}
.on-dark{background:#0A1B25}
/* 1 */
.c1 .name{font:800 108px/.95 "Bricolage Grotesque";letter-spacing:-.025em;color:#0F2330}
.c1 .name i{font-style:normal;color:#12704F}
.c1 .tag{font:500 27px/1 "IBM Plex Mono";letter-spacing:.2em;text-transform:uppercase;margin-top:18px;color:#12704F}
.on-dark.c1 .name{color:#E8EFEC}.on-dark.c1 .name i{color:#3DBB8A}.on-dark.c1 .tag{color:#93A9A7}
/* 2 */
.c2 .name{font:600 92px/1 "Bricolage Grotesque";letter-spacing:.14em;color:#0A1B25;text-transform:uppercase}
.c2 .rule{height:3px;width:120px;background:#F0B545;margin:20px 0 18px}
.c2 .tag{font:500 28px/1 "Figtree";letter-spacing:.32em;text-transform:uppercase;color:#52656E}
.on-dark.c2 .name{color:#F2EBDD}.on-dark.c2 .tag{color:#B9C6C3}
/* 3 */
.c3 .name{font:800 116px/.9 "Figtree";letter-spacing:-.045em;color:#0F2330}
.c3 .name b{font-weight:800;color:#12704F}
.c3 .tag{font:500 30px/1 "Figtree";letter-spacing:.02em;color:#52656E;margin-top:16px}
.c3 .tag span{color:#C98A12}
.on-dark.c3 .name{color:#FFFFFF}.on-dark.c3 .name b{color:#3DBB8A}.on-dark.c3 .tag{color:#B9C6C3}.on-dark.c3 .tag span{color:#F0B545}
.markonly svg{width:512px;height:512px;display:block}
/* comparison sheet */
.sheet{width:2000px;background:#EEF2EF;padding:70px;display:grid;gap:44px;font-family:Figtree}
.sheet h1{font:800 64px/1 "Bricolage Grotesque";color:#0F2330;letter-spacing:-.02em}
.sheet h1 small{display:block;font:500 24px/1.4 Figtree;color:#52656E;letter-spacing:0;margin-top:12px}
.opt{display:grid;grid-template-columns:300px 1fr 1fr;gap:0;background:#fff;border-radius:28px;overflow:hidden;box-shadow:0 20px 50px -30px rgba(15,35,48,.4)}
.opt .meta{padding:44px;display:grid;align-content:center;gap:14px;border-right:1px solid #DCE4E0}
.opt .num{font:500 20px/1 "IBM Plex Mono";letter-spacing:.14em;color:#C98A12}
.opt h2{font:800 46px/1 "Bricolage Grotesque";color:#0F2330;letter-spacing:-.02em}
.opt p{font:400 21px/1.45 Figtree;color:#52656E}
.opt .light,.opt .dark{display:grid;place-items:center;padding:30px}
.opt .dark{background:#0A1B25}
.opt .lock{padding:10px;gap:26px}
.opt .lock svg{width:130px;height:130px}
.opt .c1 .name{font-size:76px}.opt .c1 .tag{font-size:19px}
.opt .c2 .name{font-size:62px}.opt .c2 .tag{font-size:19px}.opt .c2 .rule{width:80px;margin:14px 0 12px}
.opt .c3 .name{font-size:82px}.opt .c3 .tag{font-size:22px}
.sizes{display:flex;gap:18px;align-items:end;margin-top:6px}
.sizes svg{display:block}`;

const C = [
  { id: 1, title: 'The Link', mark: markLink,
    why: 'Two interlocking chain links, worker and employer, held in an industrial hex nut. Bold and literal: it says "Links" at a glance.',
    lock: d => `<div class="lock c1 ${d}">${markLink}<div><div class="name"><i>RS</i> Links</div><div class="tag">Consultants Pvt. Ltd.</div></div></div>` },
  { id: 2, title: 'The Seal', mark: markSeal,
    why: 'An RS monogram inside a corporate seal with the company name and city around the ring. Formal and established: it suits contracts, letterheads and stamps.',
    lock: d => `<div class="lock c2 ${d}">${markSeal}<div><div class="name">RS Links</div><div class="rule"></div><div class="tag">Consultants Pvt. Ltd.</div></div></div>` },
  { id: 3, title: 'The Route', mark: markRoute,
    why: 'A map-style route in the shape of an S, joining Pakistan (amber) to an employer abroad. Modern and friendly: it works well as an app icon and on social media.',
    lock: d => `<div class="lock c3 ${d}">${markRoute}<div><div class="name"><b>rs</b>links</div><div class="tag">consultants <span>pvt. ltd.</span></div></div></div>` }
];

const pages = {};
for (const c of C) {
  pages[`concept-${c.id}-light.png`] = c.lock('');
  pages[`concept-${c.id}-dark.png`] = c.lock('on-dark');
  pages[`concept-${c.id}-mark.png`] = `<div class="markonly">${c.mark}</div>`;
}
pages['concepts-sheet.png'] = `<div class="sheet"><h1>RS Links Consultants: logo options<small>Each shown on light and dark backgrounds, with the symbol at app-icon, favicon and tiny sizes.</small></h1>` +
  C.map(c => `<div class="opt"><div class="meta"><span class="num">OPTION ${c.id}</span><h2>${c.title}</h2><p>${c.why}</p>
    <div class="sizes">${[72, 40, 22].map(s => c.mark.replace('<svg ', `<svg width="${s}" height="${s}" `)).join('')}</div></div>
    <div class="light">${c.lock('')}</div><div class="dark">${c.lock('on-dark')}</div></div>`).join('') + `</div>`;

const b = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
const ctx = await b.newContext({ deviceScaleFactor: 2 });
for (const [file, body] of Object.entries(pages)) {
  const p = await ctx.newPage();
  await p.setContent(`<!doctype html><html><head>${fonts}<style>${css}</style></head><body>${body}</body></html>`);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(150);
  await (await p.$('body > *')).screenshot({ path: OUT + file, omitBackground: !file.includes('sheet') });
  await p.close();
  console.log('wrote', file);
}
await b.close();
