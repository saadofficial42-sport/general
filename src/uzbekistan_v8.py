"""Uzbekistan factory workers — v8, English + Urdu (2026-11-04). User: new design / texture, very visible; salary now
$400 (was $550); add "visa, ticket & protector included". Other content unchanged from v7 (demands/2026-10-17-uzbekistan-factory):
Tashkent, 50 posts, 10 hours, age 21–35, processing 30–35 days, 5 duties, free accommodation / transport / medical / food
+ other facilities. Design: "Samarkand night" — deep cobalt page with a gold majolica tile texture, full-width hero
photo under a tile arch, giant gold $400 medallion, white high-contrast cards, bright green 'included' banner."""
import math
import sys

from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

COB, COB2, TQ, GOLD, GOLD2, GRN, INK = "#0D2C6B", "#071A44", "#13A7C4", "#E9B23C", "#FFD978", "#1DA851", "#13213A"
EMAIL = "hr@rslinksconsultants.com"

TXT = {
    "en": dict(dir="ltr", urgent="URGENT HIRING", title="FACTORY WORKERS", where="TASHKENT · UZBEKISTAN", sal_sub="USD / MONTH",
               incl="VISA, TICKET &amp; PROTECTOR INCLUDED",
               stats=[("user", "50", "POSTS"), ("clock", "10 HRS", "DAILY DUTY"), ("calendar", "21 – 35", "AGE"), ("doc", "30 – 35", "DAYS PROCESSING")],
               jobs_h="JOB DETAILS", jobs=["General factory work", "Packaging", "Store work (ordering)", "Cleaning goods &amp; materials", "Production line work"],
               fac_h="FREE FACILITIES", fac=[("home", "Accommodation"), ("bus", "Transport"), ("medical", "Medical"), ("food", "Food"), ("gift", "Other company facilities")],
               apply="APPLY NOW!", apply_sub="Send your CV on WhatsApp", out="RS-Links-Uzbekistan-Factory-Workers-v8-English.png"),
    "ur": dict(dir="rtl", urgent="فوری ضرورت", title="فیکٹری ورکرز", where="تاشقند، ازبکستان", sal_sub="ماہانہ تنخواہ",
               incl="ویزا، ٹکٹ اور پروٹیکٹر شامل",
               stats=[("user", "50", "آسامیاں"), ("clock", "10", "گھنٹے ڈیوٹی"), ("calendar", "21 – 35", "عمر (سال)"), ("doc", "30 – 35", "دن پروسیسنگ")],
               jobs_h="کام کی تفصیلات", jobs=["عمومی فیکٹری ورک", "پیکجنگ", "اسٹوری (آرڈرنگ)", "مال سامان کی صفائی کرنا", "پروڈکشن لائن پر کام"],
               fac_h="مفت سہولیات", fac=[("home", "رہائش"), ("bus", "ٹرانسپورٹ"), ("medical", "میڈیکل"), ("food", "کھانا"), ("gift", "کمپنی کی دیگر سہولیات")],
               apply="ابھی رابطہ کریں!", apply_sub="اپنی CV واٹس ایپ کریں", out="RS-Links-Uzbekistan-Factory-Workers-v8-Urdu.png"),
}


def tile_texture():
    s = ""
    for gx in range(0, 1080 + 90, 90):
        for gy in range(0, 1350 + 90, 90):
            cx, cy = gx, gy
            pts = " ".join(f"{cx + (34 if i % 2 == 0 else 15) * math.cos(math.radians(i * 22.5)):.1f},{cy + (34 if i % 2 == 0 else 15) * math.sin(math.radians(i * 22.5)):.1f}" for i in range(16))
            s += f"<polygon points='{pts}' fill='none' stroke='{GOLD}' stroke-width='1.2'/><circle cx='{cx + 45}' cy='{cy + 45}' r='5' fill='{TQ}'/>"
    return f"<svg width='1080' height='1350' style='display:block;opacity:.10'>{s}</svg>"


def build(lang):
    t, ur = TXT[lang], lang == "ur"
    start, end = ("right", "left") if ur else ("left", "right")

    def W(s, px, c, extra="", anton=False, weight=800):
        if ur and not s.replace(" ", "").replace("–", "").isdigit():
            return f"<div class='t' style='font-size:{px * .9:.0f}px;color:{c};line-height:1.8;font-weight:700;{extra}'>{s.replace('CV', '<span class=num>CV</span>')}</div>"
        fam = f"400 {px}px Anton" if anton else f"{weight} {px}px Archivo"
        return f"<div style='font:{fam};color:{c};line-height:1.1;direction:ltr;unicode-bidi:isolate;{extra}'>{s}</div>"

    hero, reg = (PHOTOS / "uz_milk_packing.jpg").as_uri(), (PHOTOS / "uz_registan.jpg").as_uri()
    stats = "".join(f"<div style='display:flex;flex-direction:column;align-items:center;justify-content:center;{'border-' + start + ':2px solid #E1E7F2;' if i else ''}'>"
                    f"{icon(ic, 32, COB, 2.3)}{W(v, 34, COB2, 'margin-top:4px', anton=True)}{W(l, 18 if ur else 13, '#5A6886', 'margin-top:2px;letter-spacing:.5px')}</div>"
                    for i, (ic, v, l) in enumerate(t["stats"]))
    jobs = "".join(f"<div style='display:flex;align-items:center;gap:12px;padding:{2 if ur else 9}px 0;border-bottom:1px dashed #D5DDEA'>"
                   f"<span style='width:36px;height:36px;border-radius:10px;background:{COB};color:{GOLD2};font:400 20px Anton;display:flex;align-items:center;justify-content:center;flex:none'>{i + 1}</span>{W(j, 26 if ur else 22, INK)}</div>"
                   for i, j in enumerate(t["jobs"]))
    fac = "".join(f"<div style='display:flex;align-items:center;gap:12px;padding:{2 if ur else 9}px 0;border-bottom:1px dashed #ffffff33'>"
                  f"<span style='width:38px;height:38px;border-radius:50%;background:{GOLD};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 21, COB2, 2.3)}</span>{W(f, 26 if ur else 22, '#fff')}</div>"
                  for ic, f in t["fac"])
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:{INK};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='{t['dir']}'>
<div class='abs' style='inset:0;background:radial-gradient(circle at 50% 0%,#1B4AA8,{COB} 45%,{COB2})'></div>
<div class='abs' style='inset:0'>{tile_texture()}</div>
<div class='abs' style='top:22px;{start}:30px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', f'width:270px;height:70px;object-position:{start}')}</div>
<div class='abs' style='top:24px;{end}:30px;display:flex;align-items:center;gap:12px;direction:ltr'>
 <div style='background:#E53935;border-radius:10px;padding:{'0 14px 6px' if ur else '8px 14px'}'>{W(t['urgent'], 20, '#fff', 'letter-spacing:2px')}</div>{flag('uzbekistan', 120, True, 'uz8')}</div>
<div class='abs' style='top:118px;left:30px;right:30px;height:380px;border-radius:190px 190px 24px 24px;overflow:hidden;border:6px solid {GOLD};box-shadow:0 20px 40px #0009'>
 <img src='{hero}' style='width:100%;height:100%;object-fit:cover;object-position:center 30%'>
 <div style='position:absolute;inset:0;background:linear-gradient(0deg,{COB2}EE 0%,{COB2}00 55%)'></div>
 <div style='position:absolute;left:0;right:0;bottom:{70 if ur else 16}px;text-align:center'>{W(t['title'], 88 if not ur else 80, '#fff', 'letter-spacing:2px;text-shadow:0 6px 18px #000a', anton=True)}
  {W(t['where'], 30 if ur else 26, GOLD2, 'letter-spacing:3px;margin-top:' + ('-6' if ur else '4') + 'px')}</div></div>
<div class='abs' style='top:130px;{start}:50px;width:150px;height:150px;border-radius:50%;overflow:hidden;border:5px solid #fff;box-shadow:0 10px 22px #0008'><img src='{reg}' style='width:100%;height:100%;object-fit:cover'></div>
<div class='abs' style='top:440px;{end}:40px;width:210px;height:210px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFF1BE,{GOLD2} 45%,{GOLD} 80%,#B9831C);border:6px solid #fff;box-shadow:0 14px 30px #0009;display:flex;flex-direction:column;align-items:center;justify-content:center'>
 <span style='font:400 74px Anton;color:{COB2};line-height:1'>$400</span>{W(t['sal_sub'], 18 if ur else 15, COB2, 'letter-spacing:1px')}</div>
<div class='abs' style='top:520px;{start}:30px;{end}:270px;height:66px;border-radius:14px;background:linear-gradient(90deg,{GRN},#14833E);display:flex;align-items:center;justify-content:center;gap:12px;box-shadow:0 10px 20px #0006'>
 {icon('plane', 32, '#fff', 2.2)}{W(t['incl'], 28 if ur else 24, '#fff', 'letter-spacing:1px')}</div>
<div class='abs' style='top:676px;left:30px;right:30px;height:120px;background:#fff;border-radius:20px;display:grid;grid-template-columns:repeat(4,1fr);box-shadow:0 12px 26px #0007'>{stats}</div>
<div class='abs' style='top:816px;left:30px;right:30px;display:flex;gap:16px'>
 <div style='flex:1;background:#fff;border-radius:20px;padding:8px 20px 10px;box-shadow:0 12px 26px #0007'>{W(t['jobs_h'], 28, COB, 'letter-spacing:1px', anton=True)}{jobs}</div>
 <div style='flex:1;background:linear-gradient(160deg,#16408F,{COB2});border:2px solid {GOLD};border-radius:20px;padding:8px 20px 10px'>{W(t['fac_h'], 28, GOLD2, 'letter-spacing:1px', anton=True)}{fac}</div></div>
<div class='abs' style='top:1196px;left:0;width:1080px;height:154px;background:linear-gradient(100deg,{GOLD},{GOLD2})'></div>
<div class='abs' style='top:1208px;left:30px;width:600px;height:130px;background:#fff;border-radius:18px;display:grid;grid-template-columns:1fr 1fr;align-content:center;gap:10px 12px;padding:0 18px;box-sizing:border-box;box-shadow:0 8px 18px #0004;direction:ltr'>{nums}</div>
<div class='abs' style='top:1206px;right:34px;width:400px;text-align:right'>
 {W(t['apply'], 40, COB2, 'letter-spacing:1px', anton=True)}{W(t['apply_sub'], 19, COB2, 'margin-top:4px')}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:6px;direction:ltr'>{icon('mail', 22, COB2, 2)}<span style='font:800 20px Archivo;color:{COB2}'>{EMAIL}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='{lang}' dir='{t['dir']}'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{COB}'>{body}</div></body></html>")


if __name__ == "__main__":
    for lang in (sys.argv[1:] or ["en", "ur"]):
        print(render(build(lang), TXT[lang]["out"]))
