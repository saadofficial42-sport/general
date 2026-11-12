"""Poland — Food & Mushroom factory workers v2, English (2026-11-12). User: v1 design/colour not good.
Same facts as poland_food.py. Design: "night market" — deep navy page, full-width mushroom-sorting hero photo fading
into navy, big white title, gold salary plate, three-photo filmstrip, glassy white benefit chips, gold 'included'
row, white CTA strip. Palette: navy / gold / soft white (Polish red only as a thin accent)."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

NAVY, NAVY2, GOLD, GOLD2, RED, INK = "#0C1C3A", "#060F22", "#E9B949", "#FFE29A", "#DC143C", "#0C1C3A"
EMAIL = "hr@rslinksconsultants.com"


def build():
    ph = lambda f, pos="center": f"<img src='{(PHOTOS / f).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'>"
    strip = "".join(f"<div style='flex:1;position:relative;border-radius:16px;overflow:hidden;border:3px solid {GOLD}'>{ph(f)}"
                    f"<div style='position:absolute;left:0;right:0;bottom:0;padding:24px 12px 8px;background:linear-gradient(0deg,{NAVY2}EE,{NAVY2}00);font:400 20px Anton;color:#fff;letter-spacing:1px'>{t}</div></div>"
                    for f, t in [("pl_sandwich.jpg", "SANDWICH MAKING"), ("pl_unloading.jpg", "UNLOADING &amp; RECEIVING"), ("pl_packing.jpg", "SORTING &amp; PACKING")])
    req = [("video", "Interview-based selection"), ("user", "Age 21 – 55 years"), ("doc", "Matric + good spoken English"), ("home", "Free accommodation &amp; medical"),
           ("plane", "Schengen visa · travel in Schengen"), ("family", "Family may join after residence permit*")]
    chips = "".join(f"<div style='display:flex;align-items:center;gap:12px;background:#ffffff12;border:1px solid #ffffff2a;border-radius:14px;padding:7px 16px'>"
                    f"{icon(ic, 26, GOLD2, 2.2)}<span style='font:700 18px Archivo;color:#fff;line-height:1.2'>{t}</span></div>" for ic, t in req)
    inc = "".join(f"<div style='flex:1;display:flex;align-items:center;justify-content:center;gap:10px'>{icon(ic, 30, NAVY, 2.3)}"
                  f"<div><div style='font:400 24px Anton;color:{NAVY};line-height:1'>{t}</div><div style='font:800 12px Archivo;color:{NAVY};letter-spacing:2px'>INCLUDED</div></div></div>"
                  for ic, t in [("visa", "VISA FEE"), ("shield", "PROTECTOR"), ("plane", "AIR TICKET")])
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:{INK};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:560px'>{ph('pl_mushroom.jpg', 'center 30%')}</div>
<div class='abs' style='top:0;left:0;width:1080px;height:560px;background:linear-gradient(180deg,{NAVY2}CC 0%,{NAVY2}33 30%,{NAVY}00 50%,{NAVY} 100%)'></div>
<div class='abs' style='top:28px;left:36px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:270px;height:70px;object-position:left')}</div>
<div class='abs' style='top:30px;right:40px;display:flex;align-items:center;gap:12px'><span style='font:800 16px Archivo;color:#fff;letter-spacing:4px'>SCHENGEN · EU</span>{flag('pl', 110, True, 'plv2')}</div>
<div class='abs' style='top:380px;left:44px'>
 <div style='font:800 20px Archivo;color:{GOLD2};letter-spacing:6px'>URGENT HIRING</div>
 <div style='font:400 104px Anton;color:#fff;letter-spacing:2px;line-height:1;text-shadow:0 8px 24px #000a'>JOBS IN POLAND</div>
 <div style='display:flex;align-items:center;gap:12px;margin-top:6px'><span style='width:60px;height:4px;background:{RED}'></span><span style='font:700 26px Archivo;color:#E6ECF6'>Food &amp; Mushroom Factory Workers</span></div></div>

<div class='abs' style='top:590px;left:36px;right:36px;height:104px;border-radius:18px;background:linear-gradient(135deg,{GOLD2},{GOLD});display:flex;align-items:center;justify-content:center;gap:18px;box-shadow:0 14px 30px #0008'>
 {icon('money', 40, NAVY, 2.2)}<span style='font:800 17px Archivo;color:{NAVY};letter-spacing:3px'>SALARY</span>
 <span style='font:400 52px Anton;color:{NAVY}'>IN EUROS (€) · AS PER INTERVIEW</span></div>

<div class='abs' style='top:720px;left:36px;width:560px;height:300px;display:flex;gap:10px'>{strip}</div>
<div class='abs' style='top:716px;right:36px;width:420px;display:flex;flex-direction:column;gap:6px'>{chips}</div>
<div class='abs' style='top:1028px;right:36px;width:420px;font:600 12.5px Archivo;color:#9FB0CC'>*Subject to Polish immigration rules.</div>

<div class='abs' style='top:1056px;left:36px;right:36px;height:88px;border-radius:18px;background:#fff;display:flex;align-items:center;padding:0 14px'>
 <div style='font:400 26px Anton;color:{GOLD};letter-spacing:1px;padding:0 14px;border-right:2px solid #E3E7EF'>PACKAGE</div>{inc}</div>

<div class='abs' style='top:1170px;left:0;width:1080px;height:180px;background:#fff'></div>
<div class='abs' style='top:1170px;left:0;width:1080px;height:6px;background:linear-gradient(90deg,{GOLD},{GOLD2},{GOLD})'></div>
<div class='abs' style='top:1200px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1196px;right:40px;width:380px;text-align:right'>
 <div style='font:400 44px Anton;color:{NAVY};letter-spacing:1px;line-height:1.05'>APPLY NOW!</div>
 <div style='font:700 18px Archivo;color:#5A6680;margin-top:6px'>Send your CV on WhatsApp</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:6px'>{icon('mail', 22, NAVY, 2)}<span style='font:800 20px Archivo;color:{INK}'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{NAVY}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Poland-Food-Mushroom-Factories-v2-English.png"))
