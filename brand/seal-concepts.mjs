// Two seal logos combining the chain-link symbol with a round name ring.
//   npm i playwright && node brand/seal-concepts.mjs   → brand/concepts/seal-*.png
import { chromium } from 'playwright';
import fs from 'fs';

const DIR = new URL('./', import.meta.url).pathname;
const OUT = DIR + 'concepts/';
fs.mkdirSync(OUT, { recursive: true });
const fonts = '<style>' + fs.readFileSync(DIR + 'fonts-inline.css', 'utf8') + '</style>';

// chain links drawn in a 64-unit box centred on 32,32 (same geometry as the site logo)
const chain = (id, a, b, sw = 5.6) => `
  <defs><clipPath id="${id}"><rect x="22" y="32" width="20" height="14"/></clipPath></defs>
  <g transform="rotate(-45 32 32)" fill="none" stroke-width="${sw}">
    <rect x="11" y="24.5" width="26" height="15" rx="7.5" stroke="${a}"/>
    <rect x="27" y="24.5" width="26" height="15" rx="7.5" stroke="${b}"/>
    <rect x="11" y="24.5" width="26" height="15" rx="7.5" stroke="${a}" clip-path="url(#${id})"/>
  </g>`;
// ring text: top arc reads left→right over the top, bottom arc reads upright along the bottom
const rings = (id, top, bottom, fill, size = 6.5, ls = .55) => `
  <defs>
    <path id="${id}-t" d="M15 50A35 35 0 0 1 85 50"/>
    <path id="${id}-b" d="M9.5 50A40.5 40.5 0 0 0 90.5 50"/>
  </defs>
  <text font-family="Bricolage Grotesque" font-weight="800" font-size="${size}" letter-spacing="${ls}" fill="${fill}" text-anchor="middle">
    <textPath href="#${id}-t" startOffset="50%">${top}</textPath>
  </text>
  <text font-family="Bricolage Grotesque" font-weight="600" font-size="${size - 1}" letter-spacing="${ls + .6}" fill="${fill}" text-anchor="middle">
    <textPath href="#${id}-b" startOffset="50%">${bottom}</textPath>
  </text>`;
const star = (x, y, c) => `<path d="M${x} ${y - 2.6}l.9 1.7 1.7.9-1.7.9-.9 1.7-.9-1.7-1.7-.9 1.7-.9z" fill="${c}"/>`;

/* A: navy seal, amber rim, chain inside the hex nut */
const sealA = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="49" fill="#0A1B25"/>
  <circle cx="50" cy="50" r="46.5" fill="none" stroke="#F0B545" stroke-width="1.8"/>
  <circle cx="50" cy="50" r="31" fill="none" stroke="#3DBB8A" stroke-width="1.2"/>
  ${rings('sa', 'RS LINKS CONSULTANTS', 'PVT. LTD. · RAWALPINDI', '#EDE6D6')}
  ${star(12.2, 50, '#F0B545')}${star(87.8, 50, '#F0B545')}
  <g transform="translate(50 50) scale(.78) translate(-32 -32)">
    <path d="M32 3 57.1 17.5v29L32 61 6.9 46.5v-29Z" fill="#123444" stroke="#3DBB8A" stroke-width="3" stroke-linejoin="round"/>
    ${chain('sa-clip', '#3DBB8A', '#F0B545')}
  </g>
</svg>`;

/* B: light stamp-style seal, navy rings and text, large chain on its own */
const sealB = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="49" fill="#FBFAF6"/>
  <circle cx="50" cy="50" r="47.5" fill="none" stroke="#0F2330" stroke-width="2.6"/>
  <circle cx="50" cy="50" r="44.6" fill="none" stroke="#0F2330" stroke-width=".7"/>
  <circle cx="50" cy="50" r="30.5" fill="#12704F"/>
  <circle cx="50" cy="50" r="30.5" fill="none" stroke="#0F2330" stroke-width=".7" stroke-dasharray="1.2 1.6"/>
  ${rings('sb', 'RS LINKS CONSULTANTS', '★ PVT. LTD. ★', '#0F2330')}
  ${star(12.2, 50, '#C98A12')}${star(87.8, 50, '#C98A12')}
  <g transform="translate(50 50) scale(.9) translate(-32 -32)">${chain('sb-clip', '#FFFFFF', '#F0B545', 6)}</g>
</svg>`;

const css = `*{margin:0;box-sizing:border-box}html,body{background:transparent}
.lock{display:inline-flex;align-items:center;gap:38px;padding:44px 60px}
.lock svg{width:190px;height:190px;flex:none}
.on-dark{background:#0A1B25}
.a .name{font:600 92px/1 "Bricolage Grotesque";letter-spacing:.14em;color:#0A1B25;text-transform:uppercase}
.a .rule{height:3px;width:120px;background:#F0B545;margin:20px 0 18px}
.a .tag{font:500 28px/1 "Figtree";letter-spacing:.32em;text-transform:uppercase;color:#52656E}
.on-dark.a .name{color:#F2EBDD}.on-dark.a .tag{color:#B9C6C3}
.b .name{font:800 108px/.95 "Bricolage Grotesque";letter-spacing:-.025em;color:#0F2330}
.b .name i{font-style:normal;color:#12704F}
.b .tag{font:500 27px/1 "IBM Plex Mono";letter-spacing:.2em;text-transform:uppercase;margin-top:18px;color:#12704F}
.on-dark.b .name{color:#E8EFEC}.on-dark.b .name i{color:#3DBB8A}.on-dark.b .tag{color:#93A9A7}
.markonly{display:inline-block}.markonly svg{width:600px;height:600px;display:block}
.sheet{width:2000px;background:#EEF2EF;padding:70px;display:grid;gap:44px;font-family:Figtree}
.sheet h1{font:800 64px/1 "Bricolage Grotesque";color:#0F2330;letter-spacing:-.02em}
.sheet h1 small{display:block;font:500 24px/1.4 Figtree;color:#52656E;letter-spacing:0;margin-top:12px}
.opt{display:grid;grid-template-columns:420px 1fr 1fr;background:#fff;border-radius:28px;overflow:hidden;box-shadow:0 20px 50px -30px rgba(15,35,48,.4)}
.opt .big{display:grid;place-items:center;padding:36px;border-right:1px solid #DCE4E0;gap:20px;align-content:center}
.opt .big svg{width:300px;height:300px}
.opt .num{font:500 20px/1 "IBM Plex Mono";letter-spacing:.14em;color:#C98A12}
.opt h2{font:800 40px/1 "Bricolage Grotesque";color:#0F2330;text-align:center}
.opt p{font:400 20px/1.45 Figtree;color:#52656E;text-align:center;max-width:32ch}
.opt .light,.opt .dark{display:grid;place-items:center;padding:30px}
.opt .dark{background:#0A1B25}
.opt .lock{padding:10px;gap:26px}
.opt .lock svg{width:140px;height:140px}
.opt .a .name{font-size:58px}.opt .a .tag{font-size:17px}.opt .a .rule{width:80px;margin:14px 0 12px}
.opt .b .name{font-size:70px}.opt .b .tag{font-size:17px}
.sizes{display:flex;gap:16px;align-items:end;justify-content:center}`;

const C = [
  { id: 'a', title: 'Navy Seal', mark: sealA,
    why: 'The hex-nut chain symbol at the centre of a navy seal with an amber rim. Rich and premium, made for screens, signage and visiting cards.',
    lock: d => `<div class="lock a ${d}">${sealA}<div><div class="name">RS Links</div><div class="rule"></div><div class="tag">Consultants Pvt. Ltd.</div></div></div>` },
  { id: 'b', title: 'Classic Stamp', mark: sealB,
    why: 'A traditional double-ring stamp with a large chain on a green centre. Clean and official, it also prints well in one colour as a rubber stamp.',
    lock: d => `<div class="lock b ${d}">${sealB}<div><div class="name"><i>RS</i> Links</div><div class="tag">Consultants Pvt. Ltd.</div></div></div>` }
];
const pages = {};
for (const c of C) {
  pages[`seal-${c.id}-light.png`] = c.lock('');
  pages[`seal-${c.id}-dark.png`] = c.lock('on-dark');
  pages[`seal-${c.id}-mark.png`] = `<div class="markonly">${c.mark}</div>`;
}
pages['seal-sheet.png'] = `<div class="sheet"><h1>RS Links Consultants: seal logo options<small>The chain-link symbol inside a round seal with the company name around the ring.</small></h1>` +
  C.map((c, i) => `<div class="opt"><div class="big"><span class="num">OPTION ${String.fromCharCode(65 + i)}</span>${c.mark}<h2>${c.title}</h2><p>${c.why}</p>
    <div class="sizes">${[64, 36, 20].map(s => c.mark.replace('<svg ', `<svg width="${s}" height="${s}" style="width:${s}px;height:${s}px" `)).join('')}</div></div>
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
