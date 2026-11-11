"""Greece — E-bike factory workers v2, English (2026-11-11). User: separate, very dynamic ad. Same facts as greece_ecycle.py
(EUR 900/month + accommodation, ~3 months processing). Design: "Santorini speed" — deep Aegean blue page cut by bold
diagonal white/blue slabs, Santorini dome-and-cube skyline silhouette, tilted 3-photo stack (technicians), huge
outlined €900 with gold sticker, e-bike line icon, motion streaks, diagonal CTA band."""
from common import PHONES, PHOTOS, font_css, icon, logo_img, render, whatsapp_icon
from greece_ecycle import flag_gr

BLUE, BLUE2, BLUE3, GOLD, INK = "#0D5EAF", "#06305E", "#2B8CE6", "#FFC72C", "#0B1A2E"
EMAIL = "hr@rslinksconsultants.com"


def santorini(w, h):
    s = ""
    for x, bw, bh in [(20, 90, 70), (120, 70, 100), (200, 110, 60), (330, 80, 90), (430, 120, 70), (570, 70, 110), (650, 100, 60), (770, 90, 85), (880, 120, 65), (1010, 70, 95)]:
        s += f"<rect x='{x}' y='{h - bh}' width='{bw}' height='{bh}' fill='#fff'/><rect x='{x + bw * .35}' y='{h - bh + 20}' width='{bw * .22}' height='{bh * .35}' fill='{BLUE}' opacity='.6'/>"
    for cx, r in [(165, 34), (470, 46), (820, 38)]:
        s += f"<path d='M{cx - r} {h - 100} A{r} {r} 0 0 1 {cx + r} {h - 100}Z' fill='{BLUE3}'/><rect x='{cx - r}' y='{h - 100}' width='{2 * r}' height='100' fill='#fff'/><rect x='{cx - 2}' y='{h - 100 - r - 16}' width='4' height='16' fill='#fff'/>"
    return f"<svg width='{w}' height='{h}' style='display:block'>{s}</svg>"


def ebike(size, color):
    return (f"<svg width='{size}' height='{size * .62:.0f}' viewBox='0 0 100 62' fill='none' stroke='{color}' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'>"
            f"<circle cx='20' cy='42' r='16'/><circle cx='80' cy='42' r='16'/><path d='M20 42 L38 18 H62 L80 42 M38 18 L50 42 H20 M62 18 L58 8 H66 M34 10 H44'/>"
            f"<path d='M47 26 l-4 8 h6 l-4 8' stroke='{GOLD}'/></svg>")


def build():
    ph = lambda f, pos: f"<img src='{(PHOTOS / f).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'>"
    streaks = "".join(f"<div class='abs' style='left:{x}px;top:{y}px;width:{w}px;height:5px;border-radius:5px;background:linear-gradient(90deg,#fff0,#ffffffaa)'></div>" for x, y, w in [(40, 640, 220), (70, 668, 150), (30, 696, 260)])
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:{INK};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:radial-gradient(circle at 80% 10%,{BLUE3},{BLUE} 40%,{BLUE2})'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:1350px;background:repeating-linear-gradient(115deg,#ffffff07 0 60px,transparent 60px 120px)'></div>
<div class='abs' style='top:420px;left:0;opacity:.18'>{santorini(1080, 180)}</div>
<div class='abs' style='top:30px;left:36px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:270px;height:70px;object-position:left')}</div>
<div class='abs' style='top:34px;right:40px;transform:rotate(4deg)'>{flag_gr(130)}</div>
<div class='abs' style='top:140px;left:40px;transform:rotate(-4deg);transform-origin:left'>
 <div style='display:inline-block;background:{GOLD};color:{INK};font:800 20px Archivo;letter-spacing:4px;padding:8px 16px;border-radius:8px'>URGENT · EUROPE</div>
 <div style='font:400 154px Anton;color:#fff;line-height:.9;letter-spacing:3px;margin-top:12px;text-shadow:8px 8px 0 {BLUE2}'>GREECE</div>
 <div style='font:400 50px Anton;color:{GOLD};letter-spacing:2px;margin-top:8px'>FACTORY WORKERS</div>
 <div style='display:flex;align-items:center;gap:14px;margin-top:6px'>{ebike(90, '#fff')}<span style='font:800 22px Archivo;color:#DCEBFF;letter-spacing:1px'>ELECTRIC CYCLE MANUFACTURING</span></div></div>

<div class='abs' style='top:130px;right:40px;width:330px;height:250px;border-radius:18px;overflow:hidden;border:6px solid #fff;transform:rotate(5deg);box-shadow:0 18px 36px #0008'>{ph('elec_factory_floor.jpg', '70% 30%')}</div>
<div class='abs' style='top:350px;right:120px;width:300px;height:230px;border-radius:18px;overflow:hidden;border:6px solid #fff;transform:rotate(-6deg);box-shadow:0 18px 36px #0008'>{ph('elec_panel_main.jpg', '60% 25%')}</div>
<div class='abs' style='top:470px;right:30px;width:220px;height:200px;border-radius:18px;overflow:hidden;border:6px solid #fff;transform:rotate(8deg);box-shadow:0 18px 36px #0008'>{ph('elec_blue.jpg', '70% 30%')}</div>

{streaks}
<div class='abs' style='top:610px;left:300px;width:280px;height:280px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFE58A,{GOLD} 55%,#D99A00);border:8px solid #fff;box-shadow:0 20px 40px #0009;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-8deg)'>
 <div style='font:800 18px Archivo;color:{INK};letter-spacing:4px'>SALARY</div>
 <div style='font:400 110px Anton;color:{INK};line-height:.95'>€900</div>
 <div style='font:800 16px Archivo;color:{INK};letter-spacing:2px'>PER MONTH</div></div>
<div class='abs' style='top:730px;left:600px;width:440px;height:96px;background:#fff;clip-path:polygon(6% 0,100% 0,94% 100%,0 100%);display:flex;align-items:center;justify-content:center;gap:14px;box-shadow:0 10px 22px #0006'>
 {icon('home', 40, BLUE, 2.2)}<span style='font:400 38px Anton;color:{BLUE2};letter-spacing:1px'>+ ACCOMMODATION</span></div>
<div class='abs' style='top:842px;left:620px;width:400px;height:80px;background:{GOLD};clip-path:polygon(6% 0,100% 0,94% 100%,0 100%);display:flex;align-items:center;justify-content:center;gap:12px'>
 {icon('calendar', 32, INK, 2.2)}<span style='font:400 30px Anton;color:{INK};letter-spacing:1px'>PROCESSING ~3 MONTHS</span></div>

<div class='abs' style='top:960px;left:-40px;width:1160px;height:150px;background:#fff;transform:rotate(-3deg);display:flex;align-items:center;justify-content:center;gap:24px;box-shadow:0 16px 30px #0007'>
 {icon('doc', 56, BLUE, 2)}<div><div style='font:400 52px Anton;color:{BLUE2};letter-spacing:2px;line-height:1'>SEND YOUR CV ON WHATSAPP</div>
 <div style='font:800 18px Archivo;color:#4A6280;letter-spacing:3px;margin-top:6px'>START YOUR EUROPEAN JOURNEY WITH RS LINKS</div></div></div>

<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:#fff'></div>
<div class='abs' style='top:1150px;left:0;width:1080px;height:8px;background:linear-gradient(90deg,{BLUE},{GOLD},{BLUE})'></div>
<div class='abs' style='top:1186px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1186px;right:40px;width:380px;text-align:right'>
 <div style='font:400 46px Anton;color:{BLUE};letter-spacing:1px;line-height:1.05'>APPLY NOW!</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:12px'>{icon('mail', 22, BLUE, 2)}<span style='font:800 20px Archivo;color:{INK}'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{BLUE}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Greece-E-Bike-Factory-Workers-v2-English.png"))
