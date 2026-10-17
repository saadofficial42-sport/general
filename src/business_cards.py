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


GOLD2 = C["gold2"]
DEF = f"""<defs>
 <linearGradient id='cg' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#22A86E'/><stop offset='.5' stop-color='{GREEN}'/><stop offset='1' stop-color='#03231A'/></linearGradient>
 <linearGradient id='cgold' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#FFEBA8'/><stop offset='.4' stop-color='{GOLD2}'/><stop offset='.75' stop-color='#C98A1B'/><stop offset='1' stop-color='#FFE09A'/></linearGradient>
 <linearGradient id='cmint' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#7EE2B5'/><stop offset='1' stop-color='#1E9E66'/></linearGradient>
 <linearGradient id='ccream' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#FFFFFF'/><stop offset='1' stop-color='#EEF3EE'/></linearGradient>
 <filter id='csh' x='-20%' y='-20%' width='140%' height='140%'><feDropShadow dx='0' dy='0' stdDeviation='3' flood-color='#00140C' flood-opacity='.45'/></filter></defs>"""


def side_panel(x_top, x_bot):
    """Right-hand curved 3D panel: mint, gold, green gradient layers with highlight."""
    W, H = PX_W, PX_H
    edge = lambda d: f"M{x_top - d} 0 C {x_top - 40 - d} {H*0.35:.0f}, {x_bot + 30 - d} {H*0.65:.0f}, {x_bot - d} {H}"
    body = lambda d: f"{edge(d)} L{W} {H} L{W} 0Z"
    return (f"<svg style='position:absolute;left:0;top:0' width='{W}' height='{H}'>{DEF}"
            f"<path d='{body(16)}' fill='url(#cmint)' opacity='.55' filter='url(#csh)'/>"
            f"<path d='{body(7)}' fill='url(#cgold)' filter='url(#csh)'/>"
            f"<path d='{body(0)}' fill='url(#cg)' filter='url(#csh)'/>"
            f"<path d='{edge(4)}' stroke='#FFF6D6' stroke-width='1' fill='none' opacity='.8'/>"
            f"<circle cx='{W - 30}' cy='26' r='70' fill='#ffffff' opacity='.06'/></svg>")


def bottom_wave(y, amp, cream=False):
    W, H = PX_W, PX_H
    edge = lambda d: f"M0 {y + amp - d} C {W*0.3:.0f} {y - amp*0.8 - d:.0f}, {W*0.6:.0f} {y + amp*1.4 - d:.0f}, {W} {y - d}"
    body = lambda d: f"{edge(d)} L{W} {H} L0 {H}Z"
    top = "url(#ccream)" if cream else "url(#cg)"
    return (f"<svg style='position:absolute;left:0;top:0' width='{W}' height='{H}'>{DEF}"
            f"<path d='{body(9)}' fill='url(#cmint)' opacity='.55' filter='url(#csh)'/>"
            f"<path d='{body(4)}' fill='url(#cgold)' filter='url(#csh)'/>"
            f"<path d='{body(0)}' fill='{top}' filter='url(#csh)'/>"
            f"<path d='{edge(2)}' stroke='#FFF6D6' stroke-width='.8' fill='none' opacity='.8'/></svg>")


def corner_swoosh(right=False):
    W, H = PX_W, PX_H
    tf = f" transform='translate({W} 0) scale(-1 1)'" if right else ""
    return (f"<svg style='position:absolute;left:0;top:0' width='{W}' height='{H}'>{DEF}<g{tf}>"
            f"<path d='M0 0 H{W*0.30:.0f} C {W*0.2:.0f} 8, {W*0.1:.0f} 14, 0 34Z' fill='url(#cgold)' filter='url(#csh)'/>"
            f"<path d='M0 0 H{W*0.26:.0f} C {W*0.17:.0f} 6, {W*0.08:.0f} 10, 0 27Z' fill='url(#cg)'/></g></svg>")


def front(p):
    W, H = PX_W, PX_H
    return f"""<div class='card' style='background:radial-gradient(circle at 20% 30%,#FFFFFF,#F2F6F3)'>
{corner_swoosh()}
{side_panel(W - 92, W - 128)}
<div style='position:absolute;right:{SAFE - 6}px;top:{H/2 - 54:.0f}px;width:92px;display:flex;flex-direction:column;align-items:center'>
  <div style='border-radius:50%;background:#fff;padding:3px;box-shadow:0 4px 10px #0007'>{logo_img('logo-badge', 'width:56px;height:56px')}</div>
  <div style='font-family:Dancing;font-weight:700;font-size:10.5px;color:#FFE7A0;text-align:center;line-height:1.05;margin-top:6px'>Turning Your Dreams<br>into Reality</div></div>
<div style='position:absolute;left:{SAFE + 2}px;top:{SAFE + 10}px;width:200px'>
  <div style='font-family:Anton;font-size:23px;color:{NAVY};line-height:1;letter-spacing:.3px'>{p['name']}</div>
  <div style='font-size:9.5px;font-weight:800;color:{GREEN};margin-top:4px;letter-spacing:.3px'>{p['title']}</div>
  <div style='width:44px;height:2.5px;border-radius:2px;background:linear-gradient(90deg,{GOLD},#C98A1B);margin-top:5px'></div>
  <div style='font-size:6.8px;font-weight:700;color:#6B7785;letter-spacing:1.1px;margin-top:4px'>RS LINKS CONSULTANTS PVT. LTD.</div>
</div>
<div style='position:absolute;left:{SAFE + 2}px;bottom:{SAFE + 2}px;display:flex;flex-direction:column;gap:5px'>
  {row('phone', p['phone'], 10.5)}
  {row('mail', p['email'], 9)}
  {row('gear', WEBSITE, 9)}
</div></div>"""


def back():
    W, H = PX_W, PX_H
    services = ["Manpower Recruitment", "HR Consultancy", "Student Consultancy", "Tax Consultancy",
                "Career Advisory", "Visa &amp; Documentation", "Travel &amp; Ticketing", "Document Attestation",
                "Marketing Support", "Website Development"]
    svc = "".join(f"<div style='display:flex;align-items:center;gap:3px;font-size:7.3px;font-weight:700;color:#fff'>"
                  f"<span style='color:{GOLD2};font-size:7.5px'>&#10003;</span>{x}</div>" for x in services)
    mi = lambda ic: (f"<span style='width:11px;height:11px;border-radius:50%;background:{GOLD2};display:inline-flex;align-items:center;justify-content:center;flex:none'>"
                     f"{icon(ic, 7, NAVY, 2.6)}</span>")
    wa = lambda n: (f"<div style='display:flex;align-items:center;gap:3px'><span style='line-height:0'>{whatsapp_icon(11)}</span>"
                    f"<span style='font-family:Anton;font-size:10px;color:{NAVY};letter-spacing:.3px'>{n}</span></div>")
    return f"""<div class='card' style='background:radial-gradient(circle at 80% 0%,#1C8A5C,{GREEN} 45%,#03231A)'>
<svg style='position:absolute;left:0;top:0' width='{W}' height='{H}'><circle cx='{W*0.85:.0f}' cy='10' r='90' fill='#fff' opacity='.05'/><circle cx='20' cy='{H*0.6:.0f}' r='60' fill='#fff' opacity='.04'/></svg>
{corner_swoosh(right=True)}
<div style='position:absolute;left:{SAFE}px;top:{SAFE - 4}px;background:#fff;border-radius:8px;padding:3px 7px;box-shadow:0 3px 8px #0006'>{logo_img('logo-horizontal-light', 'width:112px;height:29px')}</div>
<div style='position:absolute;left:{SAFE}px;right:{SAFE}px;top:{SAFE + 38}px;display:grid;grid-template-columns:1fr 1fr;gap:1.5px 8px'>{svc}</div>
<div style='position:absolute;left:{SAFE}px;right:{SAFE}px;top:{SAFE + 100}px;display:flex;flex-direction:column;gap:2px'>
  <div style='display:flex;align-items:center;gap:5px'>{mi('mail')}<span style='font-size:8px;font-weight:700;color:#fff'>hr@rslinksconsultants.com</span></div>
  <div style='display:flex;align-items:center;gap:5px'>{mi('pin')}<span style='font-size:6.6px;font-weight:600;color:#DCEBE3;white-space:nowrap'>{ADDRESS}</span></div>
</div>
{bottom_wave(H - 58, 8, cream=True)}
<div style='position:absolute;left:{SAFE}px;right:{SAFE}px;bottom:{SAFE - 1}px;display:flex;align-items:center;justify-content:space-between'>
  {''.join(wa(n) for n in PHONES)}</div></div>"""


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
