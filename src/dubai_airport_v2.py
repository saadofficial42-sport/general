"""Dubai Airport — 7 positions, English v2 (2026-11-09). User: v1 design "not good". Same facts
(demands/2026-11-09-dubai-airport/facts.md); no airline name/logos.
Design: "premium terminal" — full-bleed photo hero (airport security guard) under a deep-navy fade with big white
title and gold accents, white page below with clean job cards (icon · title · note · gold salary pill), three info
tiles, navy CTA. Bright, airy, high contrast."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

NAVY, NAVY2, GOLD, GOLD2, RED, INK, SOFT = "#0A1F44", "#06132B", "#C9A04A", "#F2D58C", "#D71A28", "#14213A", "#F4F6FA"
EMAIL = "hr@rslinksconsultants.com"
JOBS = [("shield", "Security Guard", "Height 5'8\" · 14 yrs education", "2267"), ("box", "Airport Loader", "", "1105"),
        ("plane", "Aircraft Cleaner", "", "1120"), ("user", "General Assistant", "With food", "900"),
        ("food", "Kitchen Helper", "With food", "900"), ("home", "Housekeeper", "With food", "900"), ("mop", "Cleaner", "", "900")]


def build():
    hero = (PHOTOS / "security_airport.jpg").as_uri()
    card = lambda ic, t, note, sal: (
        f"<div style='display:flex;align-items:center;gap:14px;background:#fff;border-radius:16px;padding:0 16px;height:78px;box-shadow:0 6px 16px rgba(10,31,68,.08);border:1px solid #E6EAF2'>"
        f"<span style='width:48px;height:48px;border-radius:14px;background:{NAVY};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 26, GOLD2, 2.2)}</span>"
        f"<div style='flex:1'><div style='font:800 21px Archivo;color:{INK}'>{t}</div>"
        + (f"<div style='font:700 14px Archivo;color:{'#1E8E4E' if 'food' in note else '#6B7690'};margin-top:3px'>{note}</div>" if note else "") + "</div>"
        f"<span style='background:linear-gradient(135deg,{GOLD2},{GOLD});border-radius:999px;padding:4px 14px;font:400 26px Anton;color:{NAVY2};white-space:nowrap'>{sal} <span style='font:800 13px Archivo'>AED</span></span></div>")
    cards = "".join(card(*j) for j in JOBS[:6])
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:520px;background:linear-gradient(135deg,{NAVY2},{NAVY})'></div><div class='abs' style='top:0;right:0;width:600px;height:520px;overflow:hidden'><img src='{hero}' style='width:100%;height:100%;object-fit:cover;object-position:25% 20%'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:520px;background:linear-gradient(90deg,{NAVY2} 0%,{NAVY} 44%,{NAVY}00 62%)'></div>
<div class='abs' style='top:28px;left:36px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:270px;height:70px;object-position:left')}</div>
<div class='abs' style='top:128px;left:44px;width:560px'>
 <div style='display:flex;align-items:center;gap:12px'>{flag('ae', 84, False)}<span style='font:800 18px Archivo;color:{GOLD2};letter-spacing:5px'>URGENT HIRING · UAE</span></div>
 <div style='font:400 46px Anton;color:#fff;letter-spacing:4px;margin-top:20px;line-height:1'>JOBS AT</div>
 <div style='font:400 100px Anton;color:#fff;letter-spacing:2px;line-height:.95'>DUBAI<br><span style='color:{GOLD2}'>AIRPORT</span></div>
 <div style='font:600 19px Archivo;color:#D6DEEC;margin-top:10px;width:470px'>With a leading airline group<br>at Dubai International Airport</div></div>

<div class='abs' style='top:488px;left:36px;right:36px;height:64px;border-radius:16px;background:{RED};display:flex;align-items:center;justify-content:center;gap:12px;box-shadow:0 10px 22px rgba(215,26,40,.35)'>
 {icon('shield', 30, '#fff', 2.2)}<span style='font:800 22px Archivo;color:#fff;letter-spacing:1px'>ALL CANDIDATES MUST HAVE <span style='font:400 26px Anton;letter-spacing:1.5px'>PCC · MOFA ATTESTED</span></span></div>

<div class='abs' style='top:576px;left:36px;right:36px;display:flex;align-items:baseline;justify-content:space-between'>
 <span style='font:400 30px Anton;color:{NAVY};letter-spacing:1.5px'>AVAILABLE POSITIONS</span><span style='font:700 16px Archivo;color:#6B7690'>Salary per month</span></div>
<div class='abs' style='top:624px;left:36px;right:36px;display:grid;grid-template-columns:1fr 1fr;gap:12px 14px'>{cards}</div>
<div class='abs' style='top:900px;left:36px;width:497px'>{card(*JOBS[6])}</div>
<div class='abs' style='top:900px;right:36px;width:497px;height:78px;display:flex;gap:12px'>
 <div style='flex:1;border-radius:16px;background:{NAVY};display:flex;flex-direction:column;align-items:center;justify-content:center'><div style='font:800 13px Archivo;color:{GOLD2};letter-spacing:2px'>AGE</div><div style='font:400 28px Anton;color:#fff'>21 – 40 YRS</div></div>
 <div style='flex:1.3;border-radius:16px;background:linear-gradient(135deg,{GOLD2},{GOLD});display:flex;flex-direction:column;align-items:center;justify-content:center'><div style='font:800 13px Archivo;color:{NAVY2};letter-spacing:2px'>INTERVIEWS</div><div style='font:400 28px Anton;color:{NAVY2}'>10 – 13 NOV 2026</div></div></div>

<div class='abs' style='top:1002px;left:36px;right:36px;height:140px;border-radius:20px;background:{SOFT};border:2px dashed #C9D2E2;display:flex;align-items:center;gap:22px;padding:0 28px;box-sizing:border-box'>
 <div style='width:84px;height:84px;border-radius:50%;background:{NAVY};display:flex;align-items:center;justify-content:center;flex:none'>{icon('doc', 44, GOLD2, 2)}</div>
 <div><div style='font:400 36px Anton;color:{NAVY};letter-spacing:1px'>SEND YOUR CV ON WHATSAPP</div>
  <div style='font:700 18px Archivo;color:#5A6680;margin-top:6px'>Mention the position you are applying for and your experience</div></div></div>

<div class='abs' style='top:1166px;left:0;width:1080px;height:184px;background:linear-gradient(100deg,{NAVY2},{NAVY});border-top:5px solid {GOLD}'></div>
<div class='abs' style='top:1194px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1196px;right:40px;width:380px;text-align:right'>
 <div style='font:400 42px Anton;color:{GOLD2};letter-spacing:1px;line-height:1.05'>APPLY NOW!</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:12px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Dubai-Airport-Jobs-v2-English.png"))
