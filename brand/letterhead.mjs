// A4 letterhead for RS Links Consultants → brand/letterhead/RS-Links-Letterhead.pdf (+ PNG preview)
//   npm i playwright && node brand/letterhead.mjs
import { chromium } from 'playwright';
import fs from 'fs';

const DIR = new URL('./', import.meta.url).pathname;
const IMG = DIR + '../website/assets/img/';
const FLAGS = DIR + '../website/assets/flags/';
const OUT = DIR + 'letterhead/';
fs.mkdirSync(OUT, { recursive: true });

// Contact details: leave a value empty to leave that line off the letterhead.
const CONTACT = {
  address1: 'Office No. 20, 3rd Floor, Satellite Shopping Centre',
  address2: 'Sixth Road, Rawalpindi, Pakistan',
  phone: '+92 371 9051589  (Phone / WhatsApp)',
  whatsapp: '',       // e.g. '+92 300 0000000'
  email: '',          // e.g. 'info@rslinks.com.pk'
  web: ''             // e.g. 'www.rslinks.com.pk'
};

const fonts = '<style>' + fs.readFileSync(DIR + 'fonts-inline.css', 'utf8') + '</style>';
const seal = fs.readFileSync(IMG + 'logo-seal.svg', 'utf8');
const icon = fs.readFileSync(IMG + 'logo-mark.svg', 'utf8').replace(/rsl-m/g, 'rsl-w');
const flag = c => 'data:image/svg+xml;base64,' + fs.readFileSync(FLAGS + c + '.svg').toString('base64');
const countries = ['sa', 'ae', 'qa', 'om', 'tr', 'ro', 'pt', 'pl', 'by', 'kg'];
const ic = {
  pin: '<path d="M12 21s-7-5.6-7-11a7 7 0 0 1 14 0c0 5.4-7 11-7 11z"/><circle cx="12" cy="10" r="2.6"/>',
  phone: '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
  wa: '<path d="M3 21l1.6-4.7A8.5 8.5 0 1 1 7.7 19.4z"/>',
  mail: '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
  web: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>'
};
const row = (i, t) => t ? `<div class="c"><span>${t}</span><svg viewBox="0 0 24 24">${ic[i]}</svg></div>` : '';

const html = `<!doctype html><html><head>${fonts}<style>
@page{size:A4;margin:0}
*{margin:0;box-sizing:border-box}
html,body{width:210mm;height:297mm}
body{font-family:Figtree,sans-serif;color:#0F2330;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;background:#fff}
/* corner accents */
.corner{position:absolute;right:-30mm;top:-30mm;width:82mm;height:82mm;border-radius:50%;background:radial-gradient(circle at 30% 70%,rgba(20,133,90,.10),rgba(20,133,90,0) 70%)}
.corner2{position:absolute;right:14mm;top:-16mm;width:46mm;height:46mm;border-radius:50%;border:.5mm dashed rgba(201,138,18,.28)}
header{position:relative;display:flex;justify-content:space-between;align-items:center;padding:13mm 16mm 7mm}
.brand{display:flex;align-items:center;gap:5mm}
.brand svg{width:27mm;height:27mm;flex:none}
.name{font:800 27pt/.95 "Bricolage Grotesque";letter-spacing:-.02em;color:#0F2330}
.name i{font-style:normal;color:#0B4A34}
.tag{font:500 8.2pt/1 "IBM Plex Mono";letter-spacing:.22em;text-transform:uppercase;color:#14855A;margin-top:2.6mm}
.sub{font:500 8pt/1 Figtree;color:#52656E;margin-top:2.4mm;letter-spacing:.02em}
.contact{display:grid;gap:1.6mm;text-align:right;font-size:8.4pt;line-height:1.35;color:#2A3D47}
.c{display:flex;justify-content:flex-end;align-items:flex-start;gap:2mm}
.c svg{width:3.6mm;height:3.6mm;flex:none;fill:none;stroke:#14855A;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;margin-top:.3mm}
.bar{height:1.3mm;margin:0 16mm;border-radius:1mm;background:linear-gradient(90deg,#0A4632,#14855A 45%,#3CCB8F 70%,#F0B545)}
.meta{display:flex;justify-content:space-between;padding:6mm 16mm 0;font:500 8pt/1 "IBM Plex Mono";letter-spacing:.08em;color:#7A8B92;text-transform:uppercase}
.meta span{display:inline-block;min-width:46mm;border-bottom:.25mm solid #CFD9D4;margin-left:2mm;height:3.4mm}
.water{position:absolute;left:50%;top:52%;width:120mm;height:120mm;transform:translate(-50%,-50%);opacity:.05}
.water svg{width:100%;height:100%}
footer{position:absolute;left:0;right:0;bottom:0}
.slogan{display:flex;align-items:center;gap:4mm;padding:0 16mm 3.5mm;font:600 8.6pt/1 "Bricolage Grotesque";color:#14855A;letter-spacing:.01em}
.slogan::after{content:"";flex:1;height:.3mm;background:linear-gradient(90deg,#CFD9D4,transparent)}
.band{position:relative;background:linear-gradient(100deg,#0A1B25 0%,#0F2A36 60%,#0A4632 100%);color:#C9D6D3;padding:4.6mm 16mm;display:flex;justify-content:space-between;align-items:center;gap:6mm;font-size:7.6pt}
.band::before{content:"";position:absolute;left:0;right:0;top:0;height:.9mm;background:linear-gradient(90deg,#14855A,#3CCB8F 60%,#F0B545)}
.band b{color:#fff;font:700 8pt/1.2 Figtree;display:block}
.flags{display:flex;gap:1.5mm;align-items:center}
.flags img{width:5.6mm;height:4.2mm;border-radius:.6mm;object-fit:cover;box-shadow:0 0 0 .2mm rgba(255,255,255,.25)}
.band .r{text-align:right;font:500 7pt/1.4 "IBM Plex Mono";letter-spacing:.12em;text-transform:uppercase;color:#93A9A7}
</style></head><body><div class="page">
  <div class="corner"></div><div class="corner2"></div>
  <header>
    <div class="brand">${seal}<div><div class="name"><i>RS</i> Links</div><div class="tag">Consultants Pvt. Ltd.</div><div class="sub">Manpower Recruitment · HR &amp; Business Consultancy</div></div></div>
    <div class="contact">
      ${row('pin', CONTACT.address1 + '<br>' + CONTACT.address2)}
      ${row('phone', CONTACT.phone)}${row('wa', CONTACT.whatsapp)}${row('mail', CONTACT.email)}${row('web', CONTACT.web)}
    </div>
  </header>
  <div class="bar"></div>
  <div class="meta"><div>Ref:<span></span></div><div>Date:<span></span></div></div>
  <div class="water">${icon}</div>
  <footer>
    <div class="slogan">Linking skilled hands with the world's employers</div>
    <div class="band">
      <div><b>RS Links Consultants Pvt. Ltd.</b>${CONTACT.address1}, ${CONTACT.address2}</div>
      <div class="flags">${countries.map(c => `<img src="${flag(c)}" alt="">`).join('')}</div>
      <div class="r">Recruitment<br>Consultancy</div>
    </div>
  </footer>
</div></body></html>`;

const b = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
await p.setContent(html);
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(300);
await p.pdf({ path: OUT + 'RS-Links-Letterhead.pdf', format: 'A4', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
await p.screenshot({ path: OUT + 'RS-Links-Letterhead-preview.png', fullPage: true });
await b.close();
console.log('wrote letterhead');
