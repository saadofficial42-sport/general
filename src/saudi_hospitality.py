"""Saudi Arabia — Hospitality Staff, English (2026-10-27). Facts: demands/2026-10-27-saudi-hospitality/facts.md
(converted from another agency's ad shared by the user; content only; interview date dropped per user's standing
preference). Photos: the three staff photos cropped from that ad (see assets/photos/SOURCE.txt).
Design: "restaurant menu" — warm cream paper, charcoal header, gold rules, three menu-style rows (round photo ·
title · dotted leader · salary 'price'), Saudi-green accents, charcoal CTA with all four numbers."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

PAPER, CHAR, GOLD, GOLD2, GRN, INK = "#FBF5EA", "#1F1B18", "#C9A24A", "#E8C878", "#0B6E3F", "#231F1B"
EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"

JOBS = [("sa_waiter.jpg", "center 25%", "WAITER", "Restaurant service", "1,000 – 1,100"),
        ("sa_kitchen_helper.jpg", "center 30%", "KITCHEN HELPER", "Kitchen support", "1,000"),
        ("sa_rice_cook.jpg", "center 25%", "RICE COOK", "Rice &amp; main dishes", "1,300 – 1,500")]


def build():
    rows = "".join(
        f"<div style='display:flex;align-items:center;gap:26px;padding:20px 0;{'border-top:2px dashed #D9C9A8;' if i else ''}'>"
        f"<div style='width:170px;height:170px;border-radius:50%;overflow:hidden;border:6px solid #fff;outline:3px solid {GOLD};box-shadow:0 10px 22px rgba(0,0,0,.18);flex:none'>"
        f"<img src='{(PHOTOS / f).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'></div>"
        f"<div style='flex:1'><div style='display:flex;align-items:baseline;gap:12px'>"
        f"<span style='font:400 46px Anton;color:{CHAR};letter-spacing:1.5px'>{t}</span>"
        f"<span style='flex:1;border-bottom:4px dotted {GOLD};transform:translateY(-10px)'></span>"
        f"<span style='font:400 46px Anton;color:{GRN};white-space:nowrap'>{sal} <span style='font-size:24px;color:{CHAR}'>SAR</span></span></div>"
        f"<div style='display:flex;align-items:center;gap:18px;margin-top:8px'>"
        f"<span style='display:inline-flex;align-items:center;gap:6px;background:{GRN};color:#fff;font:800 16px Archivo;letter-spacing:1px;padding:5px 12px;border-radius:999px'>{icon('food', 16, '#fff', 2.4)} + FOOD + OVERTIME</span></div></div></div>"
        for i, (f, pos, t, sub, sal) in enumerate(JOBS))
    perks = [("home", "Accommodation"), ("medical", "Medical"), ("bus", "Transport")]
    perk = "".join(f"<div style='flex:1;display:flex;align-items:center;justify-content:center;gap:12px;{'border-left:2px solid #ffffff33;' if i else ''}'>"
                   f"{icon(ic, 34, GOLD2, 2.2)}<div><div style='font:400 26px Anton;color:#fff;letter-spacing:1px'>{a.upper()}</div><div style='font:600 15px Archivo;color:#CFC6B8'>by company</div></div></div>" for i, (ic, a) in enumerate(perks))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 28px Anton;color:{INK};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:330px;background:{CHAR}'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:330px;background:radial-gradient(circle at 85% 10%,#3A2F22,transparent 60%)'></div>
<div class='abs' style='top:30px;left:40px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:280px;height:72px;object-position:left')}</div>
<div class='abs' style='top:26px;right:40px;filter:drop-shadow(0 6px 12px #0008)'>{flag('saudi', 130, True, 'sah')}</div>
<div class='abs' style='top:132px;left:0;right:0;text-align:center'>
 <div style='font:800 20px Archivo;color:{GOLD2};letter-spacing:8px'>URGENTLY REQUIRED FOR SAUDI ARABIA</div>
 <div style='display:flex;align-items:center;justify-content:center;gap:22px;margin-top:10px'>
  <span style='width:110px;height:2px;background:{GOLD}'></span>
  <span style='font:400 92px Anton;color:#fff;letter-spacing:6px;line-height:1'>HOSPITALITY STAFF</span>
  <span style='width:110px;height:2px;background:{GOLD}'></span></div>
 <div style='font:italic 600 22px Archivo;color:#CFC6B8;margin-top:12px'>Restaurant &amp; kitchen positions</div></div>
<div class='abs' style='top:330px;left:0;width:1080px;height:14px;background:repeating-linear-gradient(90deg,{GOLD} 0 24px,{CHAR} 24px 30px)'></div>

<div class='abs' style='top:368px;left:50px;right:50px'>{rows}</div>
<div class='abs' style='top:1006px;left:50px;right:50px;height:118px;border-radius:20px;background:{GRN};display:flex;align-items:center'>{perk}</div>

<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:{CHAR};border-top:6px solid {GOLD}'></div>
<div class='abs' style='top:1176px;left:30px;width:600px;height:150px;background:{PAPER};border-radius:18px;display:grid;grid-template-columns:1fr 1fr;align-content:center;gap:12px;padding:0 18px;box-sizing:border-box'>{nums}</div>
<div class='abs' style='top:1180px;right:36px;width:390px;text-align:right'>
 <div style='font:400 40px Anton;color:{GOLD2};letter-spacing:1px;line-height:1.05'>APPLY NOW!</div>
 <div style='font:700 18px Archivo;color:#E8E0D2;margin-top:6px'>Send your CV on WhatsApp</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px'>{icon('mail', 22, GOLD2, 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div>
 <div style='font:600 12.5px Archivo;color:#B9AF9F;margin-top:8px'>{ADDRESS}</div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{PAPER}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Saudi-Arabia-Hospitality-Staff-English.png"))
