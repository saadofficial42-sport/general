// Brand banner with the catch line → brand/banner/*.png
//   npm i playwright && node brand/banner.mjs
import { chromium } from 'playwright';
import fs from 'fs';

const DIR = new URL('./', import.meta.url).pathname;
const IMG = DIR + '../website/assets/img/';
const FLAGS = DIR + '../website/assets/flags/';
const OUT = DIR + 'banner/';
fs.mkdirSync(OUT, { recursive: true });
const fonts = '<style>' + fs.readFileSync(DIR + 'fonts-inline.css', 'utf8') + '</style>';
const seal = fs.readFileSync(IMG + 'logo-seal.svg', 'utf8');
const flag = c => 'data:image/svg+xml;base64,' + fs.readFileSync(FLAGS + c + '.svg').toString('base64');
const countries = ['sa', 'ae', 'qa', 'om', 'tr', 'ro', 'pt', 'pl', 'rs', 'by', 'kg', 'uz'];
const ic = {
  phone: '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
  mail: '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
  web: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>'
};
const svgI = n => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">${ic[n]}</svg>`;

// decorative flight arcs radiating from a point behind the seal
function arcs(w, h, ox, oy){
  const dests = [[.62,.12],[.78,.08],[.93,.2],[.98,.42],[.88,.62],[.72,.9],[.97,.82],[.55,.05]];
  let s = '';
  dests.forEach(([dx, dy], i) => {
    const x = dx * w, y = dy * h, mx = (ox + x) / 2, my = Math.min(oy, y) - 120 - i * 10;
    s += `<path d="M${ox} ${oy} Q${mx} ${my} ${x} ${y}" fill="none" stroke="rgba(61,187,138,.22)" stroke-width="2" stroke-dasharray="4 9"/>`;
    s += `<circle cx="${x}" cy="${y}" r="5" fill="rgba(61,187,138,.55)"/><circle cx="${x}" cy="${y}" r="13" fill="none" stroke="rgba(61,187,138,.2)" stroke-width="2"/>`;
  });
  return `<svg class="arcs" viewBox="0 0 ${w} ${h}" width="${w}" height="${h}">${s}</svg>`;
}

const css = `*{margin:0;box-sizing:border-box}
.banner{position:relative;overflow:hidden;font-family:Figtree;color:#E8EFEC;
  background:radial-gradient(900px 600px at 18% 50%,#164257 0%,rgba(22,66,87,0) 60%),radial-gradient(700px 500px at 95% 0%,rgba(240,181,69,.14),rgba(0,0,0,0) 60%),linear-gradient(120deg,#0A1B25 0%,#0D2430 55%,#0A3A2A 100%)}
.banner::before{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(200,225,218,.13) 1.6px,transparent 1.9px);background-size:30px 30px;-webkit-mask-image:linear-gradient(90deg,rgba(0,0,0,.9),rgba(0,0,0,.35))}
.arcs{position:absolute;left:0;top:0}
.ring{position:absolute;border-radius:50%;border:2px solid rgba(61,187,138,.18)}
.inner{position:relative;z-index:2;height:100%;display:grid;align-items:center}
.seal-wrap{position:relative;display:grid;place-items:center}
.seal-wrap svg{filter:drop-shadow(0 30px 60px rgba(0,0,0,.55))}
.eyebrow{font:500 22px/1 "IBM Plex Mono";letter-spacing:.28em;text-transform:uppercase;color:#F0B545;display:flex;align-items:center;gap:18px}
.eyebrow::before{content:"";width:60px;height:3px;background:#F0B545;border-radius:3px}
h1{font-family:"Bricolage Grotesque";font-weight:800;letter-spacing:-.035em;line-height:.95}
h1 span{display:block}
h1 .g{background:linear-gradient(90deg,#3CCB8F,#2FAE78 45%,#F0B545);-webkit-background-clip:text;background-clip:text;color:transparent}
.sub{color:#C9D6D3;font-weight:500}
.sub b{color:#fff;font-weight:600}
.flags{display:flex;gap:10px;align-items:center}
.flags img{border-radius:5px;box-shadow:0 0 0 1.5px rgba(255,255,255,.22);object-fit:cover}
.bar{position:absolute;left:0;right:0;bottom:0;z-index:3;display:flex;justify-content:space-between;align-items:center;background:rgba(5,15,21,.72);border-top:3px solid transparent;border-image:linear-gradient(90deg,#14855A,#3CCB8F 60%,#F0B545) 1}
.bar .c{display:flex;align-items:center;gap:12px;color:#E8EFEC;font-weight:600}
.bar svg{color:#3DBB8A}
.bar .r{font:500 16px/1 "IBM Plex Mono";letter-spacing:.18em;text-transform:uppercase;color:#93A9A7}`;

function banner(W, H, o){
  return `<div class="banner" style="width:${W}px;height:${H}px">
    ${arcs(W, H, o.ox, o.oy)}
    <div class="ring" style="width:${o.seal * 1.5}px;height:${o.seal * 1.5}px;left:${o.ox - o.seal * .75}px;top:${o.oy - o.seal * .75}px"></div>
    <div class="ring" style="width:${o.seal * 2.1}px;height:${o.seal * 2.1}px;left:${o.ox - o.seal * 1.05}px;top:${o.oy - o.seal * 1.05}px;border-style:dashed;border-color:rgba(240,181,69,.16)"></div>
    <div class="inner" style="grid-template-columns:${o.col}px 1fr;padding:0 ${o.pad}px ${o.barH}px;gap:${o.gap}px">
      <div class="seal-wrap">${seal.replace('<svg ', `<svg width="${o.seal}" height="${o.seal}" `)}</div>
      <div style="display:grid;gap:${o.vgap}px">
        <div class="eyebrow" style="font-size:${o.eyebrow}px">RS Links Consultants Pvt. Ltd.</div>
        <h1 style="font-size:${o.h1}px"><span>Linking Talent.</span><span class="g">Building Futures.</span></h1>
        <p class="sub" style="font-size:${o.sub}px"><b>Manpower Recruitment</b> · HR Consultancy · Visas &amp; Study Abroad</p>
        <div class="flags">${countries.map(c => `<img src="${flag(c)}" style="width:${o.flag}px;height:${o.flag * .75}px" alt="">`).join('')}</div>
      </div>
    </div>
    <div class="bar" style="height:${o.barH}px;padding:0 ${o.pad}px;font-size:${o.bar}px">
      <div style="display:flex;gap:${o.pad * .6}px">
        <span class="c">${svgI('phone').replace('<svg ', `<svg width="${o.bar + 4}" height="${o.bar + 4}" `)}+92 371 9051589</span>
        <span class="c">${svgI('mail').replace('<svg ', `<svg width="${o.bar + 4}" height="${o.bar + 4}" `)}hr@rslinksconsultants.com</span>
        <span class="c">${svgI('web').replace('<svg ', `<svg width="${o.bar + 4}" height="${o.bar + 4}" `)}rslinksconsultants.com</span>
      </div>
      <span class="r">Rawalpindi · Pakistan</span>
    </div>
  </div>`;
}

const pages = {
  // general wide banner (website, presentations, print)
  'RS-Links-Banner.png': banner(1920, 720, { ox: 430, oy: 320, seal: 440, col: 560, pad: 110, gap: 40, vgap: 26, eyebrow: 22, h1: 118, sub: 30, flag: 44, barH: 92, bar: 22 }),
  // Facebook page cover (upload size 1640 × 624)
  'RS-Links-Facebook-Cover.png': banner(1640, 624, { ox: 360, oy: 270, seal: 360, col: 460, pad: 90, gap: 34, vgap: 20, eyebrow: 18, h1: 100, sub: 25, flag: 36, barH: 80, bar: 19 })
};

const b = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
const ctx = await b.newContext({ deviceScaleFactor: 2 });
for (const [file, body] of Object.entries(pages)) {
  const p = await ctx.newPage();
  await p.setContent(`<!doctype html><html><head>${fonts}<style>${css}</style></head><body style="margin:0">${body}</body></html>`);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(200);
  await (await p.$('.banner')).screenshot({ path: OUT + file });
  await p.close();
  console.log('wrote', file);
}
await b.close();
