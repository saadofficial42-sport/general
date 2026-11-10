"""Serbia — Plaster & Tile Masons v3, English (2026-11-10). From the user's demand sheet row (partner not named):
€700–€900/month, free accommodation, free transportation, 8 h/day, processing 90–120 days; selection-based:
6 weeks free training at an institute -> work videos sent to the client -> on approval the work permit is processed.
Docs: updated CV, CNIC, passport, recent photograph, experience certificate, working video (3–4 min).
Fees / payment schedule from the sheet are internal and NOT shown on the ad.
Design: "selection roadmap" — white page, navy header with Serbian red/blue/white chevrons, two photo cards,
red salary seal, 4-step horizontal process timeline, fact chips, docs grid, navy CTA."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

RED, BLUE, NAVY, INK, SOFT = "#C6363C", "#0C4076", "#0A2342", "#14202E", "#F2F5F9"
EMAIL = "hr@rslinksconsultants.com"


def build():
    ph = lambda f, pos: f"<img src='{(PHOTOS / f).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'>"
    card = lambda f, pos, t, c: (f"<div style='flex:1;position:relative;height:300px;border-radius:22px;overflow:hidden;box-shadow:0 14px 28px rgba(10,35,66,.22)'>{ph(f, pos)}"
                                 f"<div style='position:absolute;left:0;top:0;background:{c};padding:8px 18px;border-bottom-right-radius:16px;font:400 32px Anton;color:#fff;letter-spacing:1px'>{t}</div></div>")
    steps = [("doc", "SEND CV", "&amp; documents"), ("user", "6 WEEKS TRAINING", "at an institute · free of cost"),
             ("video", "WORK VIDEO", "sent to the client"), ("check", "WORK PERMIT", "processed on approval")]
    step = "".join(f"<div style='flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;position:relative;z-index:1'>"
                   f"<span style='width:70px;height:70px;border-radius:50%;background:{RED if i == 3 else BLUE};border:5px solid #fff;box-shadow:0 6px 14px #0003;display:flex;align-items:center;justify-content:center'>{icon(ic, 32, '#fff', 2.2)}</span>"
                   f"<div style='font:400 23px Anton;color:{NAVY};letter-spacing:.5px;margin-top:8px;line-height:1.05'>{i + 1}. {a}</div><div style='font:700 15px Archivo;color:#5A6878;margin-top:4px'>{b}</div></div>"
                   for i, (ic, a, b) in enumerate(steps))
    facts = [("home", "Free accommodation"), ("bus", "Free transportation"), ("clock", "8 hours / day"), ("calendar", "90–120 days")]
    fact = "".join(f"<div style='flex:1;display:flex;align-items:center;gap:10px;justify-content:center;background:#fff;border-radius:14px;height:64px;box-shadow:0 4px 12px rgba(10,35,66,.08)'>{icon(ic, 26, RED, 2.3)}<span style='font:800 16px Archivo;color:{INK};white-space:nowrap'>{t}</span></div>" for ic, t in facts)
    docs = ["Updated CV", "CNIC", "Passport", "Recent photograph", "Experience certificate", "Working video (3–4 min)"]
    doc = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{icon('check', 20, BLUE, 3)}<span style='font:700 18px Archivo;color:{INK}'>{d}</span></div>" for d in docs)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:300px;background:linear-gradient(120deg,{NAVY},{BLUE})'></div>
<svg class='abs' style='top:0;right:0' width='420' height='300'><path d='M420 0 V300 H330 L230 150 L330 0Z' fill='{RED}'/><path d='M300 0 L200 150 L300 300 H260 L160 150 L260 0Z' fill='#fff' opacity='.9'/><path d='M230 0 L130 150 L230 300 H200 L100 150 L200 0Z' fill='{RED}' opacity='.75'/></svg>
<div class='abs' style='top:28px;left:36px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:270px;height:70px;object-position:left')}</div>
<div class='abs' style='top:34px;right:40px;filter:drop-shadow(0 6px 12px #0007)'>{flag('serbia', 130, True, 'rs3')}</div>
<div class='abs' style='top:122px;left:40px'>
 <div style='font:800 19px Archivo;color:#FFB3B6;letter-spacing:5px'>SELECTION-BASED · EUROPE</div>
 <div style='font:400 100px Anton;color:#fff;letter-spacing:3px;line-height:1'>WORK IN SERBIA</div>
 <div style='font:700 22px Archivo;color:#D4E1F2;margin-top:6px'>Plaster Masons &amp; Tile Masons</div></div>

<div class='abs' style='top:326px;left:36px;width:760px;display:flex;gap:16px'>{card('rs_plaster2.jpg', 'center 30%', 'PLASTER MASON', BLUE)}{card('rs_tile2.jpg', 'center 30%', 'TILE MASON', RED)}</div>
<div class='abs' style='top:350px;right:36px;width:236px;height:252px;border-radius:24px;background:linear-gradient(160deg,{RED},#8E1F24);box-shadow:0 14px 28px rgba(198,54,60,.35);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center'>
 <div style='font:800 15px Archivo;color:#FFD9DB;letter-spacing:3px'>SALARY</div>
 <div style='font:400 60px Anton;color:#fff;line-height:1;margin-top:6px'>€700</div><div style='font:400 26px Anton;color:#FFD9DB'>to</div><div style='font:400 60px Anton;color:#fff;line-height:1'>€900</div>
 <div style='font:800 15px Archivo;color:#fff;letter-spacing:2px;margin-top:6px'>PER MONTH</div></div>

<div class='abs' style='top:648px;left:36px;right:36px'>
 <div style='font:400 28px Anton;color:{NAVY};letter-spacing:1px'>SELECTION PROCESS</div>
 <div style='position:relative;display:flex;margin-top:14px'><div style='position:absolute;left:12%;right:12%;top:35px;height:4px;background:repeating-linear-gradient(90deg,{BLUE} 0 14px,transparent 14px 24px)'></div>{step}</div></div>

<div class='abs' style='top:880px;left:36px;right:36px;display:flex;gap:12px'>{fact}</div>
<div class='abs' style='top:964px;left:36px;right:36px;height:150px;background:{SOFT};border-radius:20px;border-left:8px solid {RED};padding:12px 26px;box-sizing:border-box'>
 <div style='font:400 26px Anton;color:{NAVY};letter-spacing:1px'>REQUIRED DOCUMENTS</div>
 <div style='display:grid;grid-template-columns:repeat(3,1fr);gap:14px 18px;margin-top:14px'>{doc}</div></div>

<div class='abs' style='top:1160px;left:0;width:1080px;height:190px;background:{NAVY};border-top:6px solid {RED}'></div>
<div class='abs' style='top:1188px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1186px;right:40px;width:380px;text-align:right'>
 <div style='font:400 36px Anton;color:#fff;letter-spacing:1px;line-height:1.05'>SEND CV &amp; WORK VIDEO</div>
 <div style='font:700 18px Archivo;color:#B9CCE4;margin-top:6px'>on WhatsApp</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Serbia-Masons-Selection-v3-English.png"))
