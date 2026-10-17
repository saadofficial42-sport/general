"""General RS Links business card (2026-10-16): no personal name — company details only, for any
employee. 3.5 x 2 in + 0.125 in bleed; same print pipeline as business_cards.py."""
import business_cards as bc
from business_cards import ADDRESS, B, GOLD, GREEN, NAVY, SAFE, TAGLINE, WEBSITE, row
from common import C, PHONES, icon, logo_img, whatsapp_icon

EMAIL = "hr@rslinksconsultants.com"


def front(_p=None):
    W, H = bc.PX_W, bc.PX_H
    wrow = lambda ic, t, sz=8.4: (f"<div style='display:flex;align-items:center;gap:6px'>"
                                  + (f"<span style='line-height:0'>{whatsapp_icon(14)}</span>" if ic == 'wa' else
                                     f"<span style='width:14px;height:14px;border-radius:50%;background:{C['gold2']};display:inline-flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 8.5, NAVY, 2.6)}</span>")
                                  + f"<span style='font-size:{sz}px;font-weight:700;color:#fff;white-space:nowrap'>{t}</span></div>")
    return f"""<div class='card' style='background:radial-gradient(circle at 25% 20%,#FFFFFF,#F2F6F3)'>
{bc.corner_swoosh(right=True)}
<div style='position:absolute;left:{SAFE}px;top:{SAFE - 6}px;display:flex;align-items:center;gap:8px'>
  <div style='border-radius:50%;background:#fff;box-shadow:0 3px 8px #0003;padding:2px'>{logo_img('logo-badge', 'width:52px;height:52px')}</div>
  <div><div style='font-family:Anton;font-size:19px;color:{GREEN};line-height:1;letter-spacing:.3px'>RS LINKS CONSULTANTS</div>
  <div style='font-size:7.2px;font-weight:800;color:{NAVY};letter-spacing:2px;margin-top:2px'>PVT. LTD.</div>
  <div style='font-family:Dancing;font-weight:700;font-size:11px;color:#A87508;margin-top:1px'>{TAGLINE}</div></div></div>
{bc.bottom_wave(H - 122, 9)}
<div style='position:absolute;left:{SAFE}px;right:{SAFE}px;bottom:{SAFE - 2}px;display:flex;flex-direction:column;gap:3.5px'>
  {wrow('wa', ' &nbsp;|&nbsp; '.join(p.replace('+92 ', '0') for p in PHONES), 8.6)}
  {wrow('mail', EMAIL)}{wrow('gear', WEBSITE)}{wrow('pin', ADDRESS, 6.9)}
</div></div>"""


if __name__ == "__main__":
    bc.front, bc.back = (lambda _p=None: bc.back()), bc.back_services
    bc.render_person({"slug": "General", "name": "", "title": "", "phone": "", "email": EMAIL})
