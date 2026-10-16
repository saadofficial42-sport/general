"""General RS Links business card (2026-10-16): no personal name — company details only, for any
employee. 3.5 x 2 in + 0.125 in bleed; same print pipeline as business_cards.py."""
import business_cards as bc
from business_cards import ADDRESS, B, GOLD, GREEN, NAVY, SAFE, TAGLINE, WEBSITE, row
from common import C, PHONES, icon, logo_img

EMAIL = "hr@rslinksconsultants.com"


def front(_p=None):
    return f"""<div class='card' style='background:#fff'>
<div style='position:absolute;left:0;top:0;bottom:0;width:{B + 22}px;background:{GREEN}'></div>
<div style='position:absolute;left:{B + 22}px;top:0;bottom:0;width:4px;background:{GOLD}'></div>
<div style='position:absolute;left:{B + 38}px;top:{SAFE - 4}px;display:flex;align-items:center;gap:8px'>
  {logo_img('logo-badge', 'width:50px;height:50px')}
  <div><div style='font-family:Anton;font-size:19px;color:{GREEN};line-height:1;letter-spacing:.3px'>RS LINKS CONSULTANTS</div>
  <div style='font-size:7.4px;font-weight:800;color:{NAVY};letter-spacing:2px;margin-top:2px'>PVT. LTD.</div>
  <div style='font-family:Dancing;font-weight:700;font-size:11px;color:#A87508;margin-top:1px'>{TAGLINE}</div></div></div>
<div style='position:absolute;left:{B + 38}px;right:{SAFE}px;bottom:{SAFE - 4}px;display:flex;flex-direction:column;gap:3px'>
  {row('phone', ' &nbsp;|&nbsp; '.join(p.replace('+92 ', '0') for p in PHONES), 8.6)}
  {row('mail', EMAIL)}
  {row('gear', WEBSITE)}
  {row('pin', ADDRESS, 7.3)}
</div></div>"""


def back():
    services = ["Manpower Recruitment", "HR Consultancy", "Student Consultancy", "Tax Consultancy",
                "Career Advisory", "Visa &amp; Documentation"]
    svc = "".join(f"<div style='display:flex;align-items:center;gap:4px;font-size:8.4px;font-weight:700;color:#fff'>"
                  f"<span style='color:{C['gold2']};font-size:8px'>&#10003;</span>{x}</div>" for x in services)
    wa = "".join(f"<span style='font-family:Anton;font-size:9.6px;color:#fff;letter-spacing:.3px'>{n}</span>" for n in PHONES)
    return f"""<div class='card' style='background:linear-gradient(135deg,{GREEN},#06291D)'>
<div style='position:absolute;inset:{B + 7}px;border:1px solid {GOLD};border-radius:6px'></div>
<div style='position:absolute;left:{SAFE}px;right:{SAFE}px;top:{SAFE}px;display:flex;align-items:center;justify-content:space-between'>
  <div style='background:#fff;border-radius:8px;padding:4px 8px'>{logo_img('logo-horizontal-light', 'width:132px;height:36px')}</div>
  <div style='text-align:right;font-family:PlexMono;font-weight:700;font-size:6.6px;color:{C['gold2']};letter-spacing:1px;line-height:1.5;width:110px'>RECRUITMENT<br>CONSULTANCY<br>VISA SERVICES</div>
</div>
<div style='position:absolute;left:{SAFE}px;right:{SAFE}px;top:{SAFE + 56}px;display:grid;grid-template-columns:1fr 1fr;gap:6px 10px'>{svc}</div>
<div style='position:absolute;left:{SAFE}px;right:{SAFE}px;bottom:{SAFE - 3}px;border-top:1px solid {GOLD}88;padding-top:4px;
  display:flex;align-items:center;justify-content:space-between'>
  {icon('phone', 10, C['gold2'], 2.6)}{wa}</div></div>"""


if __name__ == "__main__":
    bc.front, bc.back = front, back
    bc.render_person({"slug": "General", "name": "", "title": "", "phone": "", "email": EMAIL})
