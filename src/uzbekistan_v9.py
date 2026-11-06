"""Uzbekistan factory workers — v9, English + Urdu (2026-11-06). User: new design, pictures and style; salary range
350–500 USD per month. Rest as v8 (demands/2026-10-17-uzbekistan-factory): Tashkent, 50 posts, 10 hours, age 21–35,
processing 30–35 days, visa/ticket/protector included, 5 duties, free accommodation / transport / medical / food.
Design: "sunrise split" — white page, diagonal emerald-to-teal block on the right holding a big photo collage
(fruit packing / forklift / truck loading), Uzbek flag ribbon, sunrise-orange salary bar, white stat chips."""
import sys

from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

EM, EM2, TEAL, ORG, ORG2, INK, SOFT = "#0E7A55", "#08513A", "#1AA7B8", "#FF8A1F", "#FFB547", "#132A22", "#F2F7F4"
EMAIL = "hr@rslinksconsultants.com"

TXT = {
    "en": dict(dir="ltr", urgent="URGENT HIRING", kick="FOR A FACTORY IN TASHKENT", title="FACTORY<br>WORKERS", country="UZBEKISTAN",
               sal_h="SALARY", sal="$350 – $500", sal_sub="USD PER MONTH", incl="Visa, ticket &amp; protector included",
               stats=[("user", "50", "Posts"), ("clock", "10 hrs", "Daily duty"), ("calendar", "21 – 35", "Age"), ("doc", "30 – 35", "Days processing")],
               jobs_h="WORK", jobs=["General factory work", "Packaging", "Store work (ordering)", "Cleaning goods &amp; materials", "Production line work"],
               fac_h="FREE", fac=["Accommodation", "Transport", "Medical", "Food", "Other company facilities"],
               apply="APPLY NOW!", apply_sub="Send your CV on WhatsApp", out="RS-Links-Uzbekistan-Factory-Workers-v9-English.png"),
    "ur": dict(dir="rtl", urgent="فوری ضرورت", kick="تاشقند کی فیکٹری کے لیے", title="فیکٹری ورکرز", country="ازبکستان",
               sal_h="تنخواہ", sal="$350 – $500", sal_sub="ماہانہ (امریکی ڈالر)", incl="ویزا، ٹکٹ اور پروٹیکٹر شامل",
               stats=[("user", "50", "آسامیاں"), ("clock", "10", "گھنٹے ڈیوٹی"), ("calendar", "21 – 35", "عمر (سال)"), ("doc", "30 – 35", "دن پروسیسنگ")],
               jobs_h="کام کی تفصیلات", jobs=["عمومی فیکٹری ورک", "پیکجنگ", "اسٹوری (آرڈرنگ)", "مال سامان کی صفائی کرنا", "پروڈکشن لائن پر کام"],
               fac_h="مفت سہولیات", fac=["رہائش", "ٹرانسپورٹ", "میڈیکل", "کھانا", "کمپنی کی دیگر سہولیات"],
               apply="ابھی رابطہ کریں!", apply_sub="اپنی CV واٹس ایپ کریں", out="RS-Links-Uzbekistan-Factory-Workers-v9-Urdu.png"),
}


def build(lang):
    t, ur = TXT[lang], lang == "ur"
    start, end = ("right", "left") if ur else ("left", "right")

    def W(s, px, c, extra="", anton=False, weight=800):
        plain = s.replace(" ", "").replace("–", "").replace("$", "").replace("<br>", "")
        if ur and not plain.isdigit():
            s2 = s.replace("CV", "<span class=num>CV</span>")
            return f"<div class='t' style='font-size:{px * .9:.0f}px;color:{c};line-height:{1.65 if px < 30 else 1.8};font-weight:700;{extra}'>{s2}</div>"
        fam = f"400 {px}px Anton" if anton else f"{weight} {px}px Archivo"
        return f"<div style='font:{fam};color:{c};line-height:1.05;direction:ltr;unicode-bidi:isolate;{extra}'>{s}</div>"

    ph = lambda k, pos="center": f"<img src='{(PHOTOS / (k + '.jpg')).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'>"
    poly = "polygon(18% 0,100% 0,100% 100%,0 100%)" if not ur else "polygon(0 0,82% 0,100% 100%,0 100%)"
    stats = "".join(f"<div style='background:#fff;border-radius:16px;box-shadow:0 8px 18px rgba(8,81,58,.14);display:flex;flex-direction:column;align-items:center;justify-content:center;border-top:5px solid {TEAL}'>"
                    f"{icon(ic, 28, EM, 2.3)}{W(v, 32, INK, 'margin-top:6px', anton=True)}{W(l, 18 if ur else 14, '#5B6B63', 'margin-top:2px')}</div>" for ic, v, l in t["stats"])
    jobs = "".join(f"<div style='display:flex;align-items:center;gap:10px;padding:{0 if ur else 7}px 0;{'line-height:1.6' if ur else ''}'>"
                   f"<span style='width:28px;height:28px;border-radius:8px;background:{EM};color:#fff;font:400 16px Anton;display:flex;align-items:center;justify-content:center;flex:none'>{i + 1}</span>{W(j, 23 if ur else 21, INK)}</div>"
                   for i, j in enumerate(t["jobs"]))
    fac = "".join(f"<div style='display:flex;align-items:center;gap:10px;padding:{1 if ur else 7}px 0'>{icon(ic, 26, ORG2, 2.3)}{W(f, 23 if ur else 21, '#fff')}</div>"
                  for ic, f in zip(["home", "bus", "medical", "food", "gift"], t["fac"]))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='{t['dir']}'>
<div class='abs' style='top:0;{end}:0;width:560px;height:700px;background:linear-gradient(160deg,{TEAL},{EM} 45%,{EM2});clip-path:{poly}'></div>
<div class='abs' style='top:40px;{end}:30px;width:440px;height:300px;border-radius:22px;overflow:hidden;border:5px solid #fff;box-shadow:0 16px 32px #0006'>{ph('uz_fruit_packing', 'center 35%')}</div>
<div class='abs' style='top:356px;{end}:30px;width:212px;height:210px;border-radius:20px;overflow:hidden;border:5px solid #fff;box-shadow:0 12px 24px #0006'>{ph('uz_forklift')}</div>
<div class='abs' style='top:356px;{end}:258px;width:212px;height:210px;border-radius:20px;overflow:hidden;border:5px solid #fff;box-shadow:0 12px 24px #0006'>{ph('uz_truck_loading')}</div>
<div class='abs' style='top:592px;{end}:30px;width:440px;display:flex;justify-content:center'>{flag('uzbekistan', 150, True, 'uz9')}</div>
<div class='abs' style='top:28px;{start}:36px'>{logo_img('logo-horizontal-light', f'width:300px;height:78px;object-position:{start}')}</div>
<div class='abs' style='top:136px;{start}:40px;width:500px;text-align:{start}'>
 <div style='display:inline-block;background:#E53935;border-radius:10px;padding:{'0 16px 6px' if ur else '7px 16px'}'>{W(t['urgent'], 20, '#fff', 'letter-spacing:2px')}</div>
 {W(t['kick'], 20 if not ur else 26, EM, 'letter-spacing:2px;margin-top:18px')}
 {W(t['title'], 104 if not ur else 84, INK, 'margin-top:6px;letter-spacing:1px', anton=True)}
 {W(t['country'], 64 if not ur else 60, ORG, 'margin-top:' + ('6' if not ur else '-6') + 'px;letter-spacing:3px', anton=True)}</div>
<div class='abs' style='top:{530 if ur else 560}px;{start}:40px;width:470px;border-radius:22px;background:linear-gradient(135deg,{ORG2},{ORG});box-shadow:0 14px 28px rgba(255,138,31,.35);padding:14px 22px;box-sizing:border-box;text-align:center'>
 {W(t['sal_h'], 20 if not ur else 24, '#fff', 'letter-spacing:3px;margin-top:' + ('-6' if ur else '0') + 'px')}
 <div style='font:400 {66 if ur else 72}px Anton;color:#fff;line-height:1;direction:ltr'>{t['sal']}</div>
 {W(t['sal_sub'], 18 if not ur else 20, '#FFF3E3', 'letter-spacing:2px;margin-top:' + ('0' if ur else '4') + 'px')}</div>
<div class='abs' style='top:722px;left:36px;right:36px;height:64px;border-radius:14px;background:{EM2};display:flex;align-items:center;justify-content:center;gap:12px'>
 {icon('plane', 30, ORG2, 2.2)}{W(t['incl'], 28 if ur else 25, '#fff', 'letter-spacing:1px')}</div>
<div class='abs' style='top:804px;left:36px;right:36px;height:128px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px'>{stats}</div>
<div class='abs' style='top:{944 if ur else 950}px;left:36px;right:36px;display:flex;gap:16px'>
 <div style='flex:1.2;background:{SOFT};border-radius:20px;padding:6px 20px 8px'>{W(t['jobs_h'], 26, EM, 'letter-spacing:2px', anton=not ur)}{jobs}</div>
 <div style='flex:1;background:linear-gradient(160deg,{EM},{EM2});border-radius:20px;padding:6px 20px 8px'>{W(t['fac_h'], 26, ORG2, 'letter-spacing:2px', anton=not ur)}{fac}</div></div>
<div class='abs' style='top:1210px;left:0;width:1080px;height:140px;background:{INK}'></div>
<div class='abs' style='top:1222px;left:30px;display:grid;grid-template-columns:auto auto;gap:12px 30px;direction:ltr'>{nums}</div>
<div class='abs' style='top:1218px;right:34px;width:380px;text-align:right'>
 {W(t['apply'], 38, ORG2, 'letter-spacing:1px', anton=True)}{W(t['apply_sub'], 18, '#DDEBE4', 'margin-top:4px')}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:4px;direction:ltr'>{icon('mail', 20, ORG2, 2)}<span style='font:800 19px Archivo;color:#fff'>{EMAIL}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='{lang}' dir='{t['dir']}'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff'>{body}</div></body></html>")


if __name__ == "__main__":
    for lang in (sys.argv[1:] or ["en", "ur"]):
        print(render(build(lang), TXT[lang]["out"]))
