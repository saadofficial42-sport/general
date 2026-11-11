"""Greece — Electric cycle manufacturing workers, English (2026-11-11). Facts: demands/2026-11-11-greece-ecycle/facts.md
(user's partner chat: EUR 900/month + accommodation, ~3 months processing; B2B rate is internal and not shown).
Design: "Aegean" — white page with Greek-blue waves and meander (key) border, Greek flag drawn in SVG, big photo of a
factory worker, blue salary medallion, three white fact cards, blue CTA. Photo: RS library factory machine-operator
(no real e-bike assembly photo available — flagged)."""
from common import PHONES, PHOTOS, font_css, icon, logo_img, render, whatsapp_icon

BLUE, BLUE2, SKY, INK, GOLD = "#0D5EAF", "#073B73", "#E8F1FB", "#10233D", "#F2B43C"
EMAIL = "hr@rslinksconsultants.com"


def flag_gr(w=150):
    h = w * 2 / 3
    s = h / 9
    stripes = "".join(f"<rect y='{i * s}' width='{w}' height='{s}' fill='{BLUE if i % 2 == 0 else '#fff'}'/>" for i in range(9))
    c = 5 * s
    canton = f"<rect width='{c}' height='{c}' fill='{BLUE}'/><rect x='{2 * s}' width='{s}' height='{c}' fill='#fff'/><rect y='{2 * s}' width='{c}' height='{s}' fill='#fff'/>"
    return f"<svg width='{w}' height='{h}' style='display:block;box-shadow:0 6px 14px #0003'>{stripes}{canton}</svg>"


def meander(w, color):
    unit = 40
    p = "".join(f"M{x} 30 V6 H{x + 30} V24 H{x + 14} V16" for x in range(0, w, unit))
    return f"<svg width='{w}' height='34' style='display:block'><path d='{p}' stroke='{color}' stroke-width='4' fill='none'/></svg>"


def build():
    ph = lambda f, pos: f"<img src='{(PHOTOS / f).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'>"
    facts = [("home", "ACCOMMODATION", "Provided"), ("calendar", "PROCESSING", "Approx. 3 months"), ("gear", "INDUSTRY", "E-bike manufacturing")]
    fact = "".join(f"<div style='flex:1;background:#fff;border-radius:20px;box-shadow:0 10px 22px rgba(7,59,115,.12);border-top:6px solid {BLUE};display:flex;flex-direction:column;align-items:center;justify-content:center'>"
                   f"<span style='width:60px;height:60px;border-radius:50%;background:{SKY};display:flex;align-items:center;justify-content:center'>{icon(ic, 32, BLUE, 2.2)}</span>"
                   f"<div style='font:800 15px Archivo;color:#5A6C84;letter-spacing:2px;margin-top:10px'>{a}</div><div style='font:400 28px Anton;color:{INK};margin-top:4px'>{b}</div></div>" for ic, a, b in facts)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px'>{meander(1080, BLUE)}</div>
<svg class='abs' style='top:0;left:0' width='1080' height='1350'><path d='M0 640 C 300 590, 700 700, 1080 620 V1350 H0Z' fill='{SKY}'/></svg>
<div class='abs' style='top:58px;left:40px'>{logo_img('logo-horizontal-light', 'width:300px;height:78px;object-position:left')}</div>
<div class='abs' style='top:58px;right:40px'>{flag_gr(150)}</div>
<div class='abs' style='top:190px;left:44px;width:560px'>
 <div style='font:800 20px Archivo;color:#E53935;letter-spacing:5px'>URGENT HIRING · EUROPE</div>
 <div style='font:400 44px Anton;color:{BLUE};letter-spacing:4px;margin-top:14px;line-height:1'>WORK IN</div>
 <div style='font:400 150px Anton;color:{INK};letter-spacing:4px;line-height:.95'>GREECE</div>
 <div style='margin-top:18px;display:inline-block;background:{BLUE};border-radius:14px;padding:12px 22px'>
  <div style='font:400 36px Anton;color:#fff;letter-spacing:1.5px;line-height:1.05'>FACTORY WORKERS</div>
  <div style='font:800 18px Archivo;color:#CFE2F8;margin-top:6px;letter-spacing:1px'>Electric cycle (e-bike) manufacturing</div></div></div>
<div class='abs' style='top:170px;right:40px;width:420px;height:470px;border-radius:210px 210px 28px 28px;overflow:hidden;border:8px solid #fff;outline:4px solid {BLUE};box-shadow:0 20px 40px rgba(7,59,115,.3)'>{ph('elec_factory_floor.jpg', '70% 30%')}</div>
<div class='abs' style='top:556px;left:44px;width:430px;height:180px;border-radius:24px;background:linear-gradient(135deg,{BLUE},{BLUE2});box-shadow:0 16px 32px rgba(7,59,115,.35);display:flex;flex-direction:column;align-items:center;justify-content:center'>
 <div style='font:800 16px Archivo;color:#CFE2F8;letter-spacing:3px'>SALARY</div>
 <div style='font:400 84px Anton;color:#fff;line-height:1'>€900</div>
 <div style='font:800 17px Archivo;color:{GOLD};letter-spacing:2px;white-space:nowrap'>PER MONTH + ACCOMMODATION</div></div>
<div class='abs' style='top:790px;left:40px;right:40px;height:200px;display:flex;gap:18px'>{fact}</div>
<div class='abs' style='top:1022px;left:40px;right:40px;height:110px;border-radius:22px;background:#fff;border:3px dashed {BLUE};display:flex;align-items:center;justify-content:center;gap:16px'>
 {icon('doc', 42, BLUE, 2)}<div style='font:400 38px Anton;color:{INK};letter-spacing:1px'>SEND YOUR CV ON WHATSAPP</div></div>
<div class='abs' style='top:1160px;left:0;width:1080px;height:190px;background:linear-gradient(100deg,{BLUE2},{BLUE})'></div>
<div class='abs' style='top:1160px;left:0;width:1080px'>{meander(1080, '#ffffff55')}</div>
<div class='abs' style='top:1206px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1206px;right:40px;width:380px;text-align:right'>
 <div style='font:400 42px Anton;color:#fff;letter-spacing:1px;line-height:1.05'>APPLY NOW!</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:12px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Greece-E-Bike-Factory-Workers-English.png"))
