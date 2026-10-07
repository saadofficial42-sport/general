// Website handover guide for the hosting provider → brand/handover/RS-Links-Website-Handover-Guide.pdf
//   npm i playwright && node brand/handover.mjs
import { chromium } from 'playwright';
import fs from 'fs';

const DIR = new URL('./', import.meta.url).pathname;
const IMG = DIR + '../website/assets/img/';
const OUT = DIR + 'handover/';
fs.mkdirSync(OUT, { recursive: true });
const fonts = '<style>' + fs.readFileSync(DIR + 'fonts-inline.css', 'utf8') + '</style>';
const seal = fs.readFileSync(IMG + 'logo-seal.svg', 'utf8');

const DOMAIN = 'rslinksconsultants.com';
const EMAIL = 'hr@rslinksconsultants.com';
const PHONE = '+92 371 9051589';

const step = (n, t, body) => `<div class="step"><b>${n}</b><div><h4>${t}</h4>${body}</div></div>`;
const check = items => `<ul class="check">${items.map(i => `<li>${i}</li>`).join('')}</ul>`;

const html = `<!doctype html><html><head>${fonts}<style>
@page{size:A4;margin:16mm 16mm 18mm}
*{box-sizing:border-box}
body{margin:0;font:400 10pt/1.55 Figtree,sans-serif;color:#0F2330;-webkit-print-color-adjust:exact;print-color-adjust:exact}
h1,h2,h3,h4{font-family:"Bricolage Grotesque",sans-serif;margin:0;letter-spacing:-.01em}
.cover{height:262mm;display:flex;flex-direction:column;justify-content:space-between;background:radial-gradient(120mm 90mm at 85% 15%,#123444,#0A1B25 70%);color:#E8EFEC;border-radius:6mm;padding:18mm 16mm;page-break-after:always;position:relative;overflow:hidden}
.cover::after{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(200,225,218,.12) .4mm,transparent .5mm);background-size:6mm 6mm}
.cover > *{position:relative;z-index:1}
.cover .brand{display:flex;align-items:center;gap:6mm}
.cover .brand svg{width:30mm;height:30mm}
.cover .name{font:800 28pt/.95 "Bricolage Grotesque"}.cover .name i{font-style:normal;color:#2FAE78}
.cover .tag{font:500 8pt/1 "IBM Plex Mono";letter-spacing:.22em;text-transform:uppercase;color:#93A9A7;margin-top:3mm}
.cover h1{font-size:34pt;line-height:1.02;font-weight:800;max-width:150mm}
.cover h1 em{font-style:normal;color:#3DBB8A}
.cover p.lead{font-size:12pt;color:#C9D6D3;max-width:140mm;margin-top:6mm}
.facts{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}
.facts div{border:.3mm solid rgba(255,255,255,.18);border-radius:3mm;padding:4mm;background:rgba(255,255,255,.04)}
.facts small{display:block;font:500 7pt/1.3 "IBM Plex Mono";letter-spacing:.12em;text-transform:uppercase;color:#93A9A7;margin-bottom:1.5mm}
.facts b{font-size:10.5pt;color:#fff;font-weight:600}
.eyebrow{font:500 7.5pt/1 "IBM Plex Mono";letter-spacing:.16em;text-transform:uppercase;color:#14855A}
h2{font-size:17pt;font-weight:800;margin:2mm 0 4mm}
h3{font-size:12pt;margin:6mm 0 2mm}
section{margin-bottom:8mm;page-break-inside:avoid}
section.breakable{page-break-inside:auto}
p{margin:0 0 2.5mm}
.box{background:linear-gradient(170deg,#F4F9F5,#E6F0EA);border:.3mm solid #CFDDD5;border-radius:3mm;padding:4mm 5mm;margin:3mm 0}
.warn{background:linear-gradient(170deg,#FFF8E8,#F8EBCB);border-color:#E9CF8C}
.step{display:grid;grid-template-columns:9mm 1fr;gap:3mm;margin:0 0 3.5mm;page-break-inside:avoid}
.step > b{width:8mm;height:8mm;border-radius:50%;background:#14855A;color:#fff;display:grid;place-items:center;font:600 9pt/1 "IBM Plex Mono"}
.step h4{font-size:10.5pt;margin:1mm 0 1mm}
code,.mono{font:500 8.8pt/1.4 "IBM Plex Mono";background:#E6EEE9;border-radius:1mm;padding:.2mm 1.2mm}
table{width:100%;border-collapse:collapse;font-size:9pt;margin:2mm 0}
th,td{text-align:left;padding:2mm 2.5mm;border-bottom:.25mm solid #D5E0DA;vertical-align:top}
th{font:500 7pt/1.3 "IBM Plex Mono";letter-spacing:.1em;text-transform:uppercase;color:#52656E;background:#EEF4F0}
ul{margin:1mm 0 2mm;padding-left:5mm}
ul.check{list-style:none;padding-left:0}
ul.check li{padding-left:6mm;position:relative;margin-bottom:1.4mm}
ul.check li::before{content:"";position:absolute;left:0;top:1.2mm;width:3mm;height:3mm;border:.35mm solid #14855A;border-radius:.8mm}
.tree{font:500 8.6pt/1.6 "IBM Plex Mono";background:#0F2330;color:#D7E5E0;border-radius:3mm;padding:4mm 5mm;white-space:pre}
.tree b{color:#3DBB8A;font-weight:500}
.contact{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.footer-note{font-size:8pt;color:#6B7D85;margin-top:6mm}
</style></head><body>

<div class="cover">
  <div class="brand">${seal}<div><div class="name"><i>RS</i> Links</div><div class="tag">Consultants Pvt. Ltd.</div></div></div>
  <div>
    <div class="eyebrow" style="color:#F0B545">Website handover package</div>
    <h1 style="margin-top:4mm">Hosting guide for <em>${DOMAIN}</em></h1>
    <p class="lead">Everything needed to publish the RS Links Consultants website on our domain and hosting, set up the company email, and keep the site updated.</p>
  </div>
  <div class="facts">
    <div><small>Domain</small><b>${DOMAIN}</b></div>
    <div><small>Website type</small><b>Static HTML · no database</b></div>
    <div><small>Company email</small><b>${EMAIL}</b></div>
    <div><small>Total size</small><b>About 3 MB · 11 pages</b></div>
    <div><small>Server needs</small><b>Any web hosting</b></div>
    <div><small>Contact</small><b>${PHONE}</b></div>
  </div>
</div>

<section>
  <div class="eyebrow">1 · Overview</div>
  <h2>What you are publishing</h2>
  <p>The website is a finished, ready-to-publish <b>static website</b> made of HTML, CSS, JavaScript and image files. There is <b>no WordPress, no database, no PHP and nothing to install or build</b>. Uploading the files to the domain's web folder is all that is needed for it to go live.</p>
  <div class="box"><b>In short:</b> upload the contents of the <span class="mono">upload-to-public_html</span> folder into <span class="mono">public_html</span> for ${DOMAIN}, turn on free SSL, and create the mailbox ${EMAIL}.</div>
  <h3>What is in this package</h3>
  <div class="tree">RS-Links-Hosting-Package/
├── <b>READ-ME-FIRST - Website Handover Guide.pdf</b>   ← this guide
├── <b>upload-to-public_html/</b>     ← the website (upload everything inside)
│   ├── index.html                  home page
│   ├── recruitment.html  countries.html  consultancy.html  visas.html
│   ├── partnerships.html  about.html  contact.html
│   ├── privacy.html  terms.html  404.html
│   ├── assets/  (css, js, images, flags)
│   ├── .htaccess                   server settings (hidden file)
│   ├── sitemap.xml  robots.txt  site.webmanifest
│   └── HOSTING-INSTRUCTIONS.txt    short text version of this guide
├── <b>logos/</b>                     logo files (PNG + SVG) for email signatures etc.
└── <b>letterhead/</b>                company letterhead (PDF)</div>
</section>

<section class="breakable">
  <div class="eyebrow">2 · Publish the website</div>
  <h2>Upload to the hosting (cPanel)</h2>
  ${step(1, 'Open File Manager', '<p>Log in to cPanel for <b>' + DOMAIN + '</b> and open <b>File Manager</b>. Go to the <span class="mono">public_html</span> folder (or the document root assigned to this domain).</p>')}
  ${step(2, 'Clear the default page', '<p>Delete any placeholder files the hosting company put there, such as <span class="mono">index.php</span>, <span class="mono">default.html</span> or a "coming soon" page. Leave <span class="mono">cgi-bin</span> and <span class="mono">.well-known</span> if they exist.</p>')}
  ${step(3, 'Upload the files', '<p>Upload <b>everything inside</b> <span class="mono">upload-to-public_html</span>, not the folder itself. Easiest way: zip the contents of that folder, upload the zip into <span class="mono">public_html</span>, right-click it and choose <b>Extract</b>, then delete the zip.</p><p><span class="mono">index.html</span> must end up directly inside <span class="mono">public_html</span>, with the <span class="mono">assets</span> folder next to it.</p>')}
  ${step(4, 'Check the hidden file', '<p>In File Manager, open <b>Settings → Show Hidden Files</b> and confirm <span class="mono">.htaccess</span> was uploaded. It shows our own "page not found" page and speeds up loading.</p>')}
  ${step(5, 'Open the website', '<p>Visit <b>http://' + DOMAIN + '</b>. The RS Links home page should appear with the animated map, menu and logo.</p>')}
  <h3>Using FTP instead (FileZilla or similar)</h3>
  <p>Connect with the FTP details from the hosting account, open the <span class="mono">public_html</span> folder on the server side, and drag in all files and folders from <span class="mono">upload-to-public_html</span>. Make sure hidden files are shown so <span class="mono">.htaccess</span> is transferred.</p>
  <h3>Other hosting types</h3>
  <p>The site also works unchanged on Netlify, Cloudflare Pages, Vercel, GitHub Pages, Hostinger, Bluehost, GoDaddy or any Apache/Nginx/LiteSpeed server. Just publish the same folder as the site root.</p>
</section>

<section>
  <div class="eyebrow">3 · Domain</div>
  <h2>Point ${DOMAIN} to the hosting</h2>
  <p>If the domain was bought from the <b>same company</b> as the hosting, it is usually connected already. Otherwise, update the domain's DNS at the registrar using one of these options:</p>
  <table>
    <tr><th>Option</th><th>What to set</th></tr>
    <tr><td><b>A. Nameservers</b> (simplest)</td><td>Change the domain's nameservers to the ones given in the hosting welcome email (e.g. <span class="mono">ns1.yourhost.com</span>, <span class="mono">ns2.yourhost.com</span>).</td></tr>
    <tr><td><b>B. DNS records</b></td><td><span class="mono">A</span> record for <span class="mono">@</span> → hosting server IP<br><span class="mono">CNAME</span> record for <span class="mono">www</span> → <span class="mono">${DOMAIN}</span></td></tr>
  </table>
  <p>DNS changes usually take a few minutes to a few hours, and occasionally up to 24–48 hours, to work everywhere.</p>
</section>

<section>
  <div class="eyebrow">4 · Security</div>
  <h2>Turn on HTTPS (free SSL)</h2>
  ${step(1, 'Issue the certificate', '<p>In cPanel open <b>SSL/TLS Status</b> and click <b>Run AutoSSL</b> (or use the host\'s Let\'s Encrypt tool). Include both <span class="mono">' + DOMAIN + '</span> and <span class="mono">www.' + DOMAIN + '</span>.</p>')}
  ${step(2, 'Force HTTPS', '<p>Once <b>https://' + DOMAIN + '</b> opens without a warning, edit <span class="mono">.htaccess</span> and remove the <span class="mono">#</span> at the start of the three lines under "Force HTTPS". All visitors will then be sent to the secure address.</p>')}
  <div class="box warn"><b>Important:</b> do not enable the "Force HTTPS" lines before the certificate is working, or visitors will see a security error.</div>
</section>

<section>
  <div class="eyebrow">5 · Company email</div>
  <h2>Create ${EMAIL}</h2>
  <p>The website, letterhead and contact pages show <b>${EMAIL}</b>, so this mailbox must exist and receive mail.</p>
  ${step(1, 'Create the mailbox', '<p>cPanel → <b>Email Accounts</b> → <b>Create</b>. Username <span class="mono">hr</span>, domain <span class="mono">' + DOMAIN + '</span>, a strong password, and a reasonable storage quota.</p>')}
  ${step(2, 'Check mail records', '<p>If the domain\'s DNS is not managed by the hosting, make sure the <span class="mono">MX</span> record points to the hosting\'s mail server, and add the SPF/DKIM records cPanel shows under <b>Email Deliverability</b> so our emails don\'t land in spam.</p>')}
  ${step(3, 'Hand over access', '<p>Share the <b>webmail address</b> (usually <span class="mono">' + DOMAIN + '/webmail</span>) and the mailbox password with RS Links <b>privately and in person or by phone</b>, plus the IMAP/SMTP settings for phones (cPanel → Email Accounts → <b>Connect Devices</b>).</p>')}
</section>

<section>
  <div class="eyebrow">6 · Go-live checklist</div>
  <h2>Please confirm before handing back</h2>
  ${check([
    '<b>https://' + DOMAIN + '</b> and <b>https://www.' + DOMAIN + '</b> both open the home page with a padlock.',
    'All menu pages open: Home, Industries, Countries, Consultancy, Visas &amp; Study, Partnerships, About, Contact.',
    'Logo, flags and the animated backgrounds appear (no broken images).',
    'A wrong address (e.g. ' + DOMAIN + '/test) shows the RS Links "page not found" page.',
    'The green WhatsApp button opens a chat with ' + PHONE + '.',
    'On the Contact page, "Send enquiry" prepares a WhatsApp message.',
    'Facebook and Instagram buttons open the company pages.',
    'An email sent to ' + EMAIL + ' is received, and a reply from it arrives (not in spam).',
    'The site looks correct on a mobile phone.'
  ])}
  <h3>Recommended (optional)</h3>
  <ul>
    <li>Add the site to <b>Google Search Console</b> and submit <span class="mono">https://${DOMAIN}/sitemap.xml</span>. sitemap.xml and robots.txt are already set for ${DOMAIN}.</li>
    <li>Create a <b>Google Business Profile</b> for the Rawalpindi office so the company appears on Google Maps.</li>
    <li>Keep the hosting and domain set to <b>auto-renew</b>, and share the renewal dates with RS Links.</li>
  </ul>
</section>

<section>
  <div class="eyebrow">7 · Future updates</div>
  <h2>How changes will be published</h2>
  <p>When RS Links needs changes, you will receive an updated website folder. To publish it, <b>upload the new files over the old ones</b> in <span class="mono">public_html</span> (choose "overwrite"). Nothing else needs to change.</p>
  <p><b>Automatic updates (optional):</b> the website's source is kept in a GitHub repository. If you prefer, connect the hosting to it (cPanel <b>Git Version Control</b>, or an FTP deploy) so updates go live automatically. Any login details for this must be entered directly into the hosting or GitHub settings, <b>never sent by chat or email</b>.</p>
  <h3>Where things are edited (for a developer)</h3>
  <table>
    <tr><th>File</th><th>Controls</th></tr>
    <tr><td><span class="mono">assets/js/config.js</span></td><td>Company name, phone, WhatsApp, email, address, hours, Facebook/Instagram links, form settings</td></tr>
    <tr><td><span class="mono">assets/js/data.js</span></td><td>Industries and job titles, countries, visit-visa, study and residency destinations</td></tr>
    <tr><td><span class="mono">assets/css/site.css</span></td><td>Colours, fonts and layout</td></tr>
    <tr><td><span class="mono">assets/img/</span></td><td>Logo, favicon and social-sharing image</td></tr>
  </table>
  <h3>Technical notes</h3>
  <ul>
    <li>Fonts load from Google Fonts. All other files are self-hosted.</li>
    <li>Forms do not need a mail server: enquiries are handed to WhatsApp. If email delivery of forms is wanted later, a Formspree address can be added in <span class="mono">config.js</span>.</li>
    <li>No cookies, tracking or analytics are installed. Google Analytics can be added on request.</li>
  </ul>
</section>

<section>
  <div class="eyebrow">8 · Contact</div>
  <h2>RS Links Consultants Pvt. Ltd.</h2>
  <div class="contact box">
    <div><b>Office</b><br>Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi</div>
    <div><b>Mobile / WhatsApp</b><br>${PHONE}<br><b>Email</b><br>${EMAIL}</div>
  </div>
  <p class="footer-note">Thank you for hosting our website. Please let us know once it is live, and share the hosting and domain renewal details with us.</p>
</section>

</body></html>`;

const b = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
const p = await b.newPage();
await p.setContent(html);
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(300);
await p.pdf({ path: OUT + 'RS-Links-Website-Handover-Guide.pdf', format: 'A4', printBackground: true,
  displayHeaderFooter: true, headerTemplate: '<span></span>',
  footerTemplate: '<div style="width:100%;font:8px sans-serif;color:#7A8B92;padding:0 16mm;display:flex;justify-content:space-between"><span>RS Links Consultants Pvt. Ltd. · Website handover guide</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
  margin: { top: '16mm', bottom: '18mm', left: '16mm', right: '16mm' } });
if(process.env.PREVIEW){ await p.emulateMedia({media:'print'}); await p.setViewportSize({width:794,height:1123}); await p.screenshot({path: process.env.PREVIEW, fullPage:true}); }
await b.close();
console.log('wrote handover guide');
