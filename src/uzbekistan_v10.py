"""Uzbekistan factory workers — v10, English (2026-11-16). User: updated ad, different design, all six numbers.
Facts as v9 (demands/2026-10-17-uzbekistan-factory): Tashkent factory, 50 posts, 10 h duty, age 21–35, processing
30–35 days, ticket & protector included ("visa" dropped per the no-visa rule), $350–500/month, 5 duties, free
accommodation / transport / medical / food / other facilities. Factory photos only.
Design: "turquoise split" — full-height packing-worker photo on the left, Uzbek-turquoise title column on the right
with gold salary medallion over the seam, midnight stat bar, two small factory photo tiles + duties / free facilities
cards, midnight footer with gold rule."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

TQ, TQ2, MID, MID2, GOLD, GOLD2, INK = "#0FA3B1", "#087C88", "#0B2340", "#071729", "#F2B705", "#FFD45C", "#0B2340"
EMAIL = "hr@rslinksconsultants.com"


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    stats = [("user", "50", "Posts"), ("clock", "10 hrs", "Daily duty"), ("calendar", "21 – 35", "Age (years)"), ("doc", "30 – 35", "Days processing")]
    stat = "".join(f"<div style='flex:1;display:flex;align-items:center;gap:12px;justify-content:center;{'border-left:2px solid #ffffff22;' if i else ''}'>{icon(ic, 34, GOLD, 2.2)}"
                   f"<div><div style='font:400 34px Anton;color:#fff;line-height:1'>{v}</div><div style='font:700 16px Archivo;color:#B9C7D6'>{l}</div></div></div>" for i, (ic, v, l) in enumerate(stats))
    duties = ["General factory work", "Packaging", "Store work (ordering)", "Cleaning goods &amp; materials", "Production line work"]
    free = ["Accommodation", "Transport", "Medical", "Food", "Other company facilities"]
    li = lambda xs, col: "".join(f"<div style='display:flex;align-items:center;gap:10px;font:700 20px Archivo;color:{INK};line-height:1.5'>{icon('check', 22, col, 2.8)}{x}</div>" for x in xs)
    tile = lambda f, pos: f"<div style='height:150px;border-radius:14px;overflow:hidden;border:4px solid #fff;box-shadow:0 8px 16px #0B234033'><img src='{P(f)}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'></div>"
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:#F3FAFB'></div>
<div class='abs' style='top:0;left:0;width:560px;height:640px;overflow:hidden'><img src='{P("rslinks_worker_hero_blue.png")}' style='width:100%;height:100%;object-fit:cover;object-position:35% 20%'>
 <div style='position:absolute;inset:0;background:linear-gradient(0deg,#0B234099 0%,#0B234000 30%)'></div></div>
<div class='abs' style='top:0;left:560px;width:520px;height:640px;background:linear-gradient(165deg,{TQ},{TQ2});overflow:hidden'>
 <div style='position:absolute;inset:0;background:repeating-linear-gradient(45deg,#ffffff0a 0 18px,transparent 18px 36px)'></div></div>
<div class='abs' style='top:24px;left:24px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0005'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:left')}</div>
<div class='abs' style='top:34px;right:34px;filter:drop-shadow(0 6px 10px #0005)'>{flag('uzbekistan', 120, True, 'uz10')}</div>
<div class='abs' style='top:150px;left:610px;width:440px'>
 <div style='display:inline-block;background:{GOLD};color:{INK};font:800 19px Archivo;letter-spacing:4px;padding:6px 14px;border-radius:6px'>URGENT HIRING</div>
 <div style='font:400 96px Anton;color:#fff;line-height:.95;letter-spacing:2px;margin-top:14px'>FACTORY<br>WORKERS</div>
 <div style='font:400 50px Anton;color:{GOLD2};letter-spacing:3px;margin-top:8px'>UZBEKISTAN</div>
 <div style='font:700 22px Archivo;color:#E6F7F9;margin-top:6px'>For a factory in Tashkent</div></div>
<div class='abs' style='top:400px;left:330px;width:220px;height:220px;border-radius:50%;background:radial-gradient(circle at 35% 30%,{GOLD2},{GOLD} 60%,#C99300);border:7px solid #fff;box-shadow:0 16px 30px #0006;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center'>
 <div style='font:800 16px Archivo;color:{INK};letter-spacing:3px'>SALARY</div><div style='font:400 50px Anton;color:{INK};line-height:1'>$350–500</div><div style='font:800 14px Archivo;color:{INK};letter-spacing:1px'>USD / MONTH</div></div>
<div class='abs' style='top:540px;left:610px;right:30px;background:#fff;border-radius:12px;padding:10px 14px;font:800 20px Archivo;color:{TQ2};box-shadow:0 8px 16px #0003'>✈ Ticket &amp; Protector included</div>

<div class='abs' style='top:640px;left:0;width:1080px;height:110px;background:linear-gradient(90deg,{MID2},{MID});display:flex;align-items:center;padding:0 16px;box-sizing:border-box'>{stat}</div>

<div class='abs' style='top:772px;left:30px;width:300px;display:flex;flex-direction:column;gap:14px'>{tile("uz_milk_packing.jpg", "center 40%")}{tile("tr_plastic.png", "center 30%")}</div>
<div class='abs' style='top:772px;left:352px;width:340px;height:314px;background:#fff;border-radius:18px;border-top:6px solid {TQ};padding:14px 18px;box-sizing:border-box;box-shadow:0 8px 18px #0B23401a'>
 <div style='font:400 26px Anton;color:{TQ2};letter-spacing:1.5px;margin-bottom:6px'>YOUR WORK</div>{li(duties, TQ)}</div>
<div class='abs' style='top:772px;right:30px;width:336px;height:314px;background:#fff;border-radius:18px;border-top:6px solid {GOLD};padding:14px 18px;box-sizing:border-box;box-shadow:0 8px 18px #0B23401a'>
 <div style='font:400 26px Anton;color:#B98A00;letter-spacing:1.5px;margin-bottom:6px'>FREE FACILITIES</div>{li(free, '#D49E00')}</div>

<div class='abs' style='top:1104px;left:30px;right:30px;text-align:center;font:400 30px Anton;color:{MID};letter-spacing:1.5px'>SEND YOUR CV ON WHATSAPP · APPLY TODAY</div>
<div class='abs' style='top:1160px;left:0;width:1080px;height:190px;background:linear-gradient(100deg,{MID2},{MID})'></div>
<div class='abs' style='top:1160px;left:0;width:1080px;height:7px;background:linear-gradient(90deg,{TQ},{GOLD})'></div>
<div class='abs' style='top:1190px;left:30px;right:30px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:12px 0'>{nums}</div>
<div class='abs' style='top:1296px;left:30px;right:30px;display:flex;justify-content:center;align-items:center;gap:10px'>{icon('mail', 24, GOLD2, 2)}<span style='font:800 23px Archivo;color:#fff'>{EMAIL}</span></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#F3FAFB'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Uzbekistan-Factory-Workers-v10-English.png"))
