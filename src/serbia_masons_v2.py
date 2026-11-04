"""Serbia — Plaster & Tile Masons, English v2 (2026-11-04). Converted from the ad the user forwarded (content only):
€700–€900/month, free accommodation, free transportation, 8 hours/day, processing 90–120 days, documents: updated CV,
NIC, passport, recent photograph, experience certificate, work-related video (3–4 min). Dropped: "safe | secure | legal".
Design: "Belgrade tricolour" — white page, slim Serbian red/blue/white diagonal bands, two tall photo cards side by
side with angled caption plates, red salary ribbon, blue fact strip, documents checklist, navy CTA with 4 numbers."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

RED, BLUE, NAVY, INK = "#C6363C", "#0C4076", "#0A2342", "#14202E"
EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"


def build():
    card = lambda f, t, c, ic: (f"<div style='flex:1;position:relative;height:400px;border-radius:24px;overflow:hidden;box-shadow:0 16px 32px rgba(10,35,66,.25)'>"
                                f"<img src='{(PHOTOS / f).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:center 30%'>"
                                f"<div style='position:absolute;left:0;right:0;bottom:0;height:120px;background:linear-gradient(0deg,{c}F0,{c}00)'></div>"
                                f"<div style='position:absolute;left:20px;bottom:18px;display:flex;align-items:center;gap:12px'>"
                                f"<span style='width:58px;height:58px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center'>{icon(ic, 32, c, 2.3)}</span>"
                                f"<span style='font:400 46px Anton;color:#fff;letter-spacing:1px;line-height:1'>{t}</span></div></div>")
    facts = [("home", "FREE", "Accommodation"), ("bus", "FREE", "Transportation"), ("clock", "8 HOURS", "per day"), ("calendar", "90 – 120", "days processing")]
    fact = "".join(f"<div style='flex:1;display:flex;align-items:center;gap:12px;justify-content:center;{'border-left:2px solid #ffffff33;' if i else ''}'>{icon(ic, 34, '#fff', 2.2)}"
                   f"<div><div style='font:400 28px Anton;color:#fff;line-height:1'>{a}</div><div style='font:700 15px Archivo;color:#CFDDF0;margin-top:4px'>{b}</div></div></div>" for i, (ic, a, b) in enumerate(facts))
    docs = ["Updated CV", "National Identity Card (NIC)", "Passport", "Recent photograph", "Experience certificate", "Work-related video (3–4 min)"]
    doc = "".join(f"<div style='display:flex;align-items:center;gap:10px'><span style='width:30px;height:30px;border-radius:50%;background:{BLUE};color:#fff;font:400 17px Anton;display:flex;align-items:center;justify-content:center;flex:none'>{i + 1}</span>"
                  f"<span style='font:700 19px Archivo;color:{INK}'>{d}</span></div>" for i, d in enumerate(docs))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<svg class='abs' style='top:0;left:0' width='1080' height='300'><path d='M620 0 H1080 V190Z' fill='{RED}'/><path d='M720 0 H1080 V150 L700 0Z' fill='{BLUE}' opacity='0'/>
 <path d='M760 0 H1080 V130Z' fill='{BLUE}'/><path d='M900 0 H1080 V74Z' fill='#fff'/></svg>
<div class='abs' style='top:30px;left:36px'>{logo_img('logo-horizontal-light', 'width:300px;height:78px;object-position:left')}</div>
<div class='abs' style='top:150px;left:40px;width:700px'>
 <div style='font:800 20px Archivo;color:{RED};letter-spacing:6px'>URGENT REQUIREMENT · EUROPE</div>
 <div style='display:flex;align-items:center;gap:20px;margin-top:6px'><span style='font:400 118px Anton;color:{NAVY};letter-spacing:3px;line-height:1'>SERBIA</span>{flag('serbia', 150, True, 'rsv2')}</div>
 <div style='font:700 24px Archivo;color:#4A5868;margin-top:8px'>Construction jobs for skilled masons</div></div>
<div class='abs' style='top:150px;right:40px;width:270px;height:150px;border-radius:22px;background:linear-gradient(135deg,{RED},#8E1F24);box-shadow:0 14px 28px rgba(198,54,60,.35);display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-3deg)'>
 <div style='font:800 15px Archivo;color:#FFD9DB;letter-spacing:3px'>SALARY</div><div style='font:400 52px Anton;color:#fff;line-height:1'>€700 – €900</div><div style='font:800 15px Archivo;color:#fff;letter-spacing:2px'>PER MONTH</div></div>
<div class='abs' style='top:350px;left:36px;right:36px;display:flex;gap:20px'>{card('rs_plaster2.jpg', 'PLASTER MASON', BLUE, 'roller')}{card('rs_tile2.jpg', 'TILE MASON', RED, 'rebar')}</div>
<div class='abs' style='top:774px;left:36px;right:36px;height:104px;border-radius:20px;background:linear-gradient(90deg,{NAVY},{BLUE});display:flex;align-items:center'>{fact}</div>
<div class='abs' style='top:898px;left:36px;right:36px;height:230px;background:#F3F6FA;border-radius:20px;border-left:8px solid {RED};padding:14px 26px;box-sizing:border-box'>
 <div style='font:400 28px Anton;color:{NAVY};letter-spacing:1px'>REQUIRED DOCUMENTS</div>
 <div style='display:grid;grid-template-columns:1fr 1fr;gap:14px 24px;margin-top:12px'>{doc}</div></div>
<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:{NAVY};border-top:6px solid {RED}'></div>
<div class='abs' style='top:1178px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1176px;right:40px;width:380px;text-align:right'>
 <div style='font:400 38px Anton;color:#fff;letter-spacing:1px;line-height:1.05'>SEND YOUR CV &amp; VIDEO</div>
 <div style='font:700 18px Archivo;color:#CFDDF0;margin-top:6px'>on WhatsApp</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div>
 <div style='font:600 12.5px Archivo;color:#9FB3CC;margin-top:8px'>{ADDRESS}</div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Serbia-Plaster-Tile-Masons-v2-English.png"))
