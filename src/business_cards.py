"""RS Links business cards (print).

Standard Pakistani/US card 3.5 x 2 in with 0.125 in bleed on every side (page 3.75 x 2.25 in);
keep text inside the 0.125 in safe margin. Each person gets a 2-page PDF (front = person,
back = company) at exact physical size, plus 600 dpi PNGs of each side.
"""
from common import C, OUTPUT, PHONES, font_css, icon, logo_img, whatsapp_icon
from common import _launch

GREEN, GOLD, NAVY = C["green"], C["gold"], "#0A1B25"
WEBSITE = "www.rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"
TAGLINE = "Turning Your Dreams into Reality"
PPI = 96                     # CSS px per inch (PDF native)
BLEED = 0.125
W, H = 3.5 + 2 * BLEED, 2 + 2 * BLEED
PX_W, PX_H = round(W * PPI), round(H * PPI)
B = round(BLEED * PPI)       # bleed in px
SAFE = B + 14                # bleed + ~0.15 in safe margin

PEOPLE = [
    {"slug": "Saad-Khalid", "name": "Saad Khalid", "title": "Co-Founder &amp; COO",
     "phone": "0344-5899955", "email": "saad@rslinksconsultants.com"},
    {"slug": "Rahim-Ullah", "name": "Rahim Ullah", "title": "Co-Founder &amp; CEO",
     "phone": "0319-0727427", "email": "raheem@rslinksconsultants.com"},
    {"slug": "Hassan-Sultan", "name": "Hassan Sultan", "title": "Admin &amp; HR Officer",
     "phone": "0317-0363690", "email": "hr@rslinksconsultants.com"},
    {"slug": "Hameeda-Zia", "name": "Hameeda Zia", "title": "Recruitment &amp; Sales Officer",
     "phone": "0371-9051589", "email": "hr@rslinksconsultants.com"},
    {"slug": "Ayesha-Ghafoor", "name": "Ayesha Ghafoor", "title": "Social Media Specialist",
     "phone": "+92 321 5128989", "email": "hr@rslinksconsultants.com"},
]


def row(ic, text, size=8.6):
    badge = (f"<div style='width:15px;height:15px;flex:none;line-height:0'>{whatsapp_icon(15)}</div>" if ic == 'wa' else
             f"<div style='width:15px;height:15px;border-radius:50%;background:{GREEN};display:flex;align-items:center;justify-content:center;flex:none'>"
             f"{icon(ic, 9, '#fff', 2.6)}</div>")
    return (f"<div style='display:flex;align-items:center;gap:6px'>{badge}"
            f"<div style='font-size:{size}px;font-weight:600;color:{NAVY};line-height:1.25'>{text}</div></div>")


def front(p):
    return f"""<div class='card' style='background:#fff'>
<div style='position:absolute;left:0;top:0;bottom:0;width:{B + 22}px;background:{GREEN}'></div>
<div style='position:absolute;left:{B + 22}px;top:0;bottom:0;width:4px;background:{GOLD}'></div>
<div style='position:absolute;right:{SAFE}px;top:{SAFE - 2}px'>{logo_img('logo-badge', 'width:46px;height:46px')}</div>
<div style='position:absolute;left:{B + 40}px;top:{SAFE + 2}px;right:{SAFE + 54}px'>
  <div style='font-family:Anton;font-size:23px;color:{NAVY};line-height:1;letter-spacing:.3px'>{p['name']}</div>
  <div style='font-size:9.5px;font-weight:800;color:{GREEN};margin-top:4px;letter-spacing:.3px'>{p['title']}</div>
  <div style='font-size:7.2px;font-weight:700;color:#6B7785;letter-spacing:1.2px;margin-top:2px'>RS LINKS CONSULTANTS PVT. LTD.</div>
</div>
<div style='position:absolute;left:{B + 40}px;right:{SAFE}px;bottom:{SAFE - 4}px;display:flex;flex-direction:column;gap:2.5px'>
  {row('phone', p['phone'], 9.4)}
  {row('wa', 'Office: ' + ' | '.join(n.replace('+92 ', '0') for n in PHONES), 7.9)}
  {row('mail', p['email'])}
  {row('gear', WEBSITE)}
  {row('pin', ADDRESS, 7.4)}
</div></div>"""


def back():
    services = ["Manpower Recruitment", "HR Consultancy", "Student Consultancy", "Tax Consultancy",
                "Career Advisory", "Visa &amp; Documentation"]
    svc = "".join(f"<div style='display:flex;align-items:center;gap:4px;font-size:8.6px;font-weight:700;color:#fff'>"
                  f"<span style='color:{C['gold2']};font-size:8px'>&#10003;</span>{x}</div>" for x in services)
    wa = lambda n: (f"<div style='display:flex;align-items:center;gap:4px'><span style='line-height:0'>{whatsapp_icon(11)}</span>"
                    f"<span style='font-family:Anton;font-size:10px;color:#fff;letter-spacing:.3px'>{n}</span></div>")
    return f"""<div class='card' style='background:linear-gradient(135deg,{GREEN},#06291D)'>
<div style='position:absolute;inset:{B + 7}px;border:1px solid {GOLD};border-radius:6px'></div>
<div style='position:absolute;left:{SAFE}px;right:{SAFE}px;top:{SAFE}px;display:flex;align-items:center;justify-content:space-between'>
  <div style='background:#fff;border-radius:8px;padding:4px 8px'>{logo_img('logo-horizontal-light', 'width:132px;height:36px')}</div>
  <div style='text-align:right;font-family:Dancing;font-weight:700;font-size:11.5px;color:{C['gold2']};line-height:1.1;width:110px'>{TAGLINE}</div>
</div>
<div style='position:absolute;left:{SAFE}px;right:{SAFE}px;top:{SAFE + 58}px;display:grid;grid-template-columns:1fr 1fr;gap:7px 10px'>{svc}</div>
<div style='position:absolute;left:{SAFE}px;right:{SAFE}px;bottom:{SAFE - 2}px;border-top:1px solid {GOLD}88;padding-top:5px;
  display:flex;align-items:center;justify-content:space-between'>
  {''.join(wa(n) for n in PHONES)}
</div>
<div style='position:absolute;left:{SAFE}px;right:{SAFE}px;bottom:{SAFE + 17}px;display:flex;align-items:center;justify-content:flex-end;gap:5px'>
  <span style='width:13px;height:13px;border-radius:50%;background:{C['gold2']};display:flex;align-items:center;justify-content:center'>{icon('mail', 8, NAVY, 2.6)}</span>
  <span style='font-size:8px;font-weight:700;color:#fff'>hr@rslinksconsultants.com</span>
</div></div>"""


CSS = f"""{font_css()}
html,body{{margin:0;padding:0;width:{PX_W}px;height:{PX_H}px;overflow:hidden}}
@page{{size:{W}in {H}in;margin:0}}
.card{{position:relative;width:{PX_W}px;height:{PX_H}px;overflow:hidden;font-family:'Archivo',sans-serif;page-break-after:always}}
"""


def render_person(p):
    from playwright.sync_api import sync_playwright
    out = OUTPUT / "business-cards"
    out.mkdir(parents=True, exist_ok=True)
    tmp = OUTPUT / ".tmp"
    tmp.mkdir(exist_ok=True)
    sides = {"Front": front(p), "Back": back()}
    with sync_playwright() as pw:
        b = _launch(pw)
        # 2-page print PDF
        both = tmp / f"card-{p['slug']}.html"
        both.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}html,body{{height:auto;overflow:visible}}</style></head>"
                        f"<body>{sides['Front']}{sides['Back']}</body></html>", encoding="utf-8")
        pg = b.new_page(viewport={"width": PX_W, "height": PX_H})
        pg.goto(both.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        pg.pdf(path=str(out / f"RS-Links-Business-Card-{p['slug']}.pdf"), width=f"{W}in", height=f"{H}in", print_background=True)
        pg.close()
        # 600 dpi PNG per side
        for side, html in sides.items():
            f = tmp / f"card-{p['slug']}-{side}.html"
            f.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{html}</body></html>", encoding="utf-8")
            pg = b.new_page(viewport={"width": PX_W, "height": PX_H}, device_scale_factor=600 / PPI)
            pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
            pg.screenshot(path=str(out / f"RS-Links-Business-Card-{p['slug']}-{side}.png"))
            pg.close()
        b.close()
    print(out / f"RS-Links-Business-Card-{p['slug']}.pdf")


if __name__ == "__main__":
    for person in PEOPLE:
        render_person(person)
