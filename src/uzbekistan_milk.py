"""Uzbekistan — milk product company, 3 positions, English (2026-10-22). Facts: demands/2026-10-22-uzbekistan-milk/facts.md
(from another agency's ad; content only, employer not named, their photos not reused).
Design: "boarding pass" — full-bleed Uzbek lake landscape (user photo) with sky-blue title, a big white boarding-pass
card with perforated stub (salary as the 'fare'), three tall real-photo position cards, icon benefit grid, deep-blue CTA."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

SKY, BLUE, DEEP, TQ, SUN, INK = "#2F8CFF", "#1554C0", "#0A2A6B", "#12B5C9", "#FFC233", "#0F1B33"
EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"

POSITIONS = [("rslinks_worker_pack_x3.png", "55% 35%", "box", "Factory Packing Workers", "Milk, yogurt &amp; cream products"),
             ("rslinks_team_scan_x3.png", "center 35%", "leaf", "Fruit &amp; Vegetable Packing Workers", "Sorting &amp; packing fresh produce"),
             ("rslinks_worker_hero.png", "center 25%", "truck", "Loading &amp; Unloading Workers", "Warehouse &amp; dispatch")]


def build():
    lake = (PHOTOS / "uz_charvak_lake.jpg").as_uri()
    cards = "".join(
        f"<div style='flex:1;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 12px 26px rgba(10,42,107,.22)'>"
        f"<div style='height:186px;position:relative'><img src='{(PHOTOS / f).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'>"
        f"<span style='position:absolute;left:14px;bottom:-24px;width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,{TQ},{BLUE});border:4px solid #fff;display:flex;align-items:center;justify-content:center'>{icon(ic, 26, '#fff', 2.3)}</span></div>"
        f"<div style='padding:28px 16px 12px'><div style='font:400 26px Anton;color:{DEEP};line-height:1.05;letter-spacing:.3px'>{t}</div>"
        f"<div style='font:700 16px Archivo;color:#5A6B85;margin-top:6px'>{s}</div></div></div>" for f, pos, ic, t, s in POSITIONS)
    ben = [("clock", "8 hours", "per day"), ("home", "Accommodation", "by employer"), ("bus", "Transportation", "by employer"),
           ("medical", "Medical insurance", "by employer"), ("overtime", "Overtime", "as per company policy"),
           ("calendar", "Contract &amp; leave", "as per Uzbek labour law"), ("food", "Food", "self-arranged")]
    ben_html = "".join(f"<div style='display:flex;align-items:center;gap:10px'><span style='width:44px;height:44px;border-radius:12px;background:#EAF2FF;display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 25, BLUE, 2.3)}</span>"
                       f"<div style='line-height:1.15'><div style='font:800 18px Archivo;color:{INK}'>{a}</div><div style='font:600 14px Archivo;color:#5A6B85'>{b}</div></div></div>" for ic, a, b in ben)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:{INK};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:560px;overflow:hidden'><img src='{lake}' style='width:100%;height:100%;object-fit:cover;object-position:center 30%'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:560px;background:linear-gradient(180deg,#0A2A6Bcc 0%,#0A2A6B33 45%,#0A2A6B00 70%,#EEF5FF 100%)'></div>
<div class='abs' style='top:26px;left:30px;background:#fff;border-radius:16px;padding:4px 14px;box-shadow:0 8px 20px #0005'>{logo_img('logo-horizontal-light', 'width:290px;height:74px;object-position:left')}</div>
<div class='abs' style='top:24px;right:30px;filter:drop-shadow(0 6px 12px #0007)'>{flag('uzbekistan', 130, True, 'uzm')}</div>
<div class='abs' style='top:132px;left:0;right:0;text-align:center'>
 <div style='display:inline-block;background:{SUN};color:{INK};font:800 18px Archivo;letter-spacing:4px;padding:6px 18px;border-radius:999px'>URGENT HIRING · MILK PRODUCT COMPANY</div>
 <div style='font:400 128px Anton;color:#fff;letter-spacing:6px;line-height:1;margin-top:12px;text-shadow:0 6px 0 {BLUE},0 14px 24px #0009'>UZBEKISTAN</div></div>

<div class='abs' style='top:350px;left:40px;right:40px;height:170px;display:flex;filter:drop-shadow(0 16px 26px rgba(10,42,107,.35))'>
 <div style='flex:1;background:#fff;border-radius:22px 0 0 22px;padding:16px 26px;display:flex;flex-direction:column;justify-content:center'>
  <div style='display:flex;align-items:center;gap:16px'>
   <div><div style='font:800 13px Archivo;color:#7A8AA6;letter-spacing:2px'>FROM</div><div style='font:400 46px Anton;color:{DEEP};line-height:1'>PAKISTAN</div></div>
   <div style='flex:1;display:flex;align-items:center;gap:6px'><div style='flex:1;border-top:3px dashed #BFD3F5'></div>{icon('plane', 34, BLUE, 2)}<div style='flex:1;border-top:3px dashed #BFD3F5'></div></div>
   <div style='text-align:right'><div style='font:800 13px Archivo;color:#7A8AA6;letter-spacing:2px'>TO</div><div style='font:400 46px Anton;color:{DEEP};line-height:1'>UZBEKISTAN</div></div></div>
  <div style='display:flex;gap:28px;margin-top:14px;font:800 15px Archivo;color:#5A6B85;letter-spacing:1px'>
   <span>POSITIONS <b style='color:{INK}'>3</b></span><span>DUTY <b style='color:{INK}'>8 HRS / DAY</b></span><span>STAY <b style='color:{INK}'>PROVIDED</b></span></div></div>
 <div style='width:0;border-left:4px dotted #BFD3F5;margin:14px 0'></div>
 <div style='width:250px;background:linear-gradient(160deg,{SKY},{DEEP});border-radius:0 22px 22px 0;display:flex;flex-direction:column;align-items:center;justify-content:center'>
  <div style='font:800 14px Archivo;color:#CFE2FF;letter-spacing:3px'>SALARY</div>
  <div style='font:400 70px Anton;color:{SUN};line-height:1'>$600</div>
  <div style='font:800 15px Archivo;color:#fff;letter-spacing:2px'>USD / MONTH</div></div></div>

<div class='abs' style='top:560px;left:0;width:1080px;height:640px;background:#EEF5FF'></div>
<div class='abs' style='top:548px;left:40px;font:400 34px Anton;color:{DEEP};letter-spacing:1px'>AVAILABLE POSITIONS</div>
<div class='abs' style='top:600px;left:40px;right:40px;display:flex;gap:18px'>{cards}</div>
<div class='abs' style='top:930px;left:40px;right:40px;height:232px;background:#fff;border-radius:22px;box-shadow:0 10px 24px rgba(10,42,107,.12);padding:16px 26px;box-sizing:border-box'>
 <div style='font:400 28px Anton;color:{DEEP};letter-spacing:1px'>SALARY &amp; BENEFITS</div>
 <div style='display:grid;grid-template-columns:repeat(3,1fr);gap:14px 18px;margin-top:10px'>
  <div style='display:flex;align-items:center;gap:10px'><span style='width:44px;height:44px;border-radius:12px;background:{SUN};display:flex;align-items:center;justify-content:center;flex:none'>{icon('money', 25, INK, 2.3)}</span>
   <div style='line-height:1.15'><div style='font:800 18px Archivo;color:{INK}'>600 USD</div><div style='font:600 14px Archivo;color:#5A6B85'>per month</div></div></div>{ben_html}</div></div>

<div class='abs' style='top:1176px;left:0;width:1080px;height:174px;background:linear-gradient(100deg,{DEEP},{BLUE})'></div>
<div class='abs' style='top:1196px;left:30px;width:600px;height:134px;background:#fff;border-radius:18px;display:grid;grid-template-columns:1fr 1fr;align-content:center;gap:10px 12px;padding:0 18px;box-sizing:border-box;box-shadow:0 8px 18px #0006'>{nums}</div>
<div class='abs' style='top:1198px;right:34px;width:390px;text-align:right'>
 <div style='font:400 38px Anton;color:{SUN};letter-spacing:1px;line-height:1.05'>APPLY NOW!</div>
 <div style='font:700 18px Archivo;color:#DCE8FF;margin-top:6px'>Send your CV on WhatsApp</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px'>{icon('mail', 22, SUN, 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div>
 <div style='font:600 13px Archivo;color:#B9CCF0;margin-top:8px;line-height:1.3'>{ADDRESS}</div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#EEF5FF'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Uzbekistan-Milk-Company-3-Positions-English.png"))
