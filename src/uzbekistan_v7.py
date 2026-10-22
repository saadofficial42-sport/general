"""Uzbekistan factory workers — v7, English + Urdu (2026-10-22). User: v6 content is right, but use the pictures and
style of the ads they provided (the milk-company Uzbekistan ad + their lake photo). Content = v6
(demands/2026-10-17-uzbekistan-factory): Tashkent, $550 USD/month, 50 posts, 10 hours, age 21–35, processing 30–35
days, 5 duties, free accommodation / transport / medical / food + other facilities. No woman photo.
Style taken from the reference: bright white page, Uzbek landscape hero, Registan tile-dome inset, navy title,
teal tab headers, round teal icon list with dotted dividers, 2x2 real work-photo grid, teal salary panel with yellow
figure and orange ribbon, icon benefit row with vertical dividers. Photos: see assets/photos/SOURCE.txt."""
import sys

from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

NAVY, TEAL, TEAL2, YEL, ORG, GRN, INK = "#13294B", "#1C7C8C", "#0F5866", "#FFD233", "#F26A21", "#3C8D2F", "#1A2333"
EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"
PICS = [("uz_milk_packing", "center 30%"), ("uz_fruit_packing", "center 30%"), ("uz_forklift", "center 30%"), ("uz_truck_loading", "center 40%")]

TXT = {
    "en": dict(dir="ltr", urgent="URGENT HIRING", kick="JOIN A FACTORY IN TASHKENT", title="FACTORY WORKERS", country="UZBEKISTAN",
               tag="A STRONG STEP TOWARDS A BETTER FUTURE", duties_h="JOB DETAILS",
               duties=["General factory work", "Packaging", "Store work (ordering)", "Cleaning goods &amp; materials", "Production line work"],
               sal_h="SALARY", sal_sub="PER MONTH",
               stats=[("user", "50", "POSTS"), ("clock", "10 HRS", "DAILY DUTY"), ("calendar", "21 – 35", "AGE (YEARS)"), ("doc", "30 – 35", "DAYS PROCESSING")],
               fac_h="FACILITIES",
               fac=[("home", "ACCOMMODATION", "FREE"), ("bus", "TRANSPORT", "FREE"), ("medical", "MEDICAL", "FREE"), ("food", "FOOD", "FREE"), ("gift", "OTHER FACILITIES", "BY COMPANY")],
               apply="APPLY NOW!", apply_sub="Send your CV on WhatsApp", out="RS-Links-Uzbekistan-Factory-Workers-v7-English.png"),
    "ur": dict(dir="rtl", urgent="فوری ضرورت", kick="تاشقند کی فیکٹری کے لیے", title="فیکٹری ورکرز", country="ازبکستان",
               tag="بہتر مستقبل کی جانب ایک مضبوط قدم", duties_h="کام کی تفصیلات",
               duties=["عمومی فیکٹری ورک", "پیکجنگ", "اسٹوری (آرڈرنگ)", "مال سامان کی صفائی کرنا", "پروڈکشن لائن پر کام"],
               sal_h="تنخواہ", sal_sub="ماہانہ",
               stats=[("user", "50", "آسامیاں"), ("clock", "10", "گھنٹے ڈیوٹی"), ("calendar", "21 – 35", "عمر (سال)"), ("doc", "30 – 35", "دن پروسیسنگ")],
               fac_h="سہولیات",
               fac=[("home", "رہائش", "مفت"), ("bus", "ٹرانسپورٹ", "مفت"), ("medical", "میڈیکل", "مفت"), ("food", "کھانا", "مفت"), ("gift", "دیگر سہولیات", "کمپنی کی طرف سے")],
               apply="ابھی رابطہ کریں!", apply_sub="اپنی CV واٹس ایپ کریں", out="RS-Links-Uzbekistan-Factory-Workers-v7-Urdu.png"),
}


def build(lang):
    t = TXT[lang]
    ur = lang == "ur"
    start, end = ("right", "left") if ur else ("left", "right")

    def W(s, px, c, weight=800, extra="", anton=False):
        if ur and not s.replace(" ", "").replace("–", "").replace("-", "").isdigit():
            return f"<div class='t' style='font-size:{px * .92:.0f}px;color:{c};line-height:1.75;font-weight:700;{extra}'>{s}</div>"
        fam = f"400 {px}px Anton" if anton else f"{weight} {px}px Archivo"
        return f"<div style='font:{fam};color:{c};line-height:1.1;direction:ltr;unicode-bidi:isolate;{extra}'>{s}</div>"

    lake, reg = (PHOTOS / "uz_charvak_lake.jpg").as_uri(), (PHOTOS / "uz_registan.jpg").as_uri()
    duties = "".join(f"<div style='display:flex;align-items:center;gap:14px;padding:{4 if ur else 10}px 0;border-bottom:2px dashed #C9D6DE'>"
                     f"<span style='width:46px;height:46px;border-radius:50%;background:{TEAL};border:3px solid #D7EEF1;display:flex;align-items:center;justify-content:center;font:400 22px Anton;color:#fff;flex:none'>{i + 1}</span>"
                     f"{W(d, 24, INK, 800)}</div>" for i, d in enumerate(t["duties"]))
    grid = "".join(f"<div style='border-radius:14px;overflow:hidden;box-shadow:0 6px 14px #0003'><img src='{(PHOTOS / (k + '.jpg')).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{p}'></div>" for k, p in PICS)
    stats = "".join(f"<div style='display:flex;flex-direction:column;align-items:center;justify-content:center;{'border-' + start + ':2px solid #D3DEE5;' if i else ''}'>"
                    f"{icon(ic, 30, TEAL, 2.3)}{W(v, 32, NAVY, anton=True, extra='margin-top:4px')}{W(l, 19 if ur else 13, '#55667A', 800, 'letter-spacing:.3px;margin-top:2px;white-space:nowrap')}</div>" for i, (ic, v, l) in enumerate(t["stats"]))
    fac = "".join(f"<div style='flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;{'border-' + start + ':2px solid #D3DEE5;' if i else ''}'>"
                  f"<span style='width:52px;height:52px;border-radius:50%;background:{GRN};display:flex;align-items:center;justify-content:center'>{icon(ic, 28, '#fff', 2.2)}</span>"
                  f"{W(a, 21 if ur else 16, NAVY, 800, 'margin-top:' + ('0' if ur else '6') + 'px;letter-spacing:.5px')}{W(b, 21 if ur else 18, ORG, 800, 'margin-top:' + ('-2' if ur else '2') + 'px')}</div>" for i, (ic, a, b) in enumerate(t["fac"]))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:{INK};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='{t['dir']}'>
<div class='abs' style='top:0;left:0;width:1080px;height:430px;overflow:hidden'><img src='{lake}' style='width:100%;height:100%;object-fit:cover;object-position:center 35%'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:430px;background:linear-gradient(180deg,#0000 0%,#0000 45%,#ffffffcc 82%,#fff 100%)'></div>
<div class='abs' style='top:0;{end}:0;width:1080px;height:430px;background:linear-gradient({'270' if ur else '90'}deg,#ffffffee 0%,#ffffffb0 38%,#fff0 62%)'></div>
<div class='abs' style='top:22px;{start}:30px'>{logo_img('logo-horizontal-light', f'width:300px;height:78px;object-position:{start}')}</div>
<div class='abs' style='top:{104 if ur else 118}px;{start}:30px;width:620px;text-align:{start}'>
 <div style='display:inline-block;background:{GRN};border-radius:8px;padding:{'0 16px 6px' if ur else '6px 16px'};box-shadow:0 6px 12px #0003'>{W(t['kick'], 20, '#fff', 800, 'letter-spacing:1.5px')}</div>
 {W(t['title'], 70 if ur else 82, NAVY, anton=True, extra='letter-spacing:1px;margin-top:' + ('0' if ur else '8') + 'px')}
 <div style='display:flex;align-items:center;gap:12px;margin-top:{-14 if ur else 4}px;justify-content:{'flex-end' if ur else 'flex-start'};direction:ltr'>
  {flag('uzbekistan', 86, False)}{W(t['country'], 64 if not ur else 50, ORG, anton=True, extra='letter-spacing:2px')}</div>
 <div style='display:inline-block;margin-top:{0 if ur else 10}px;background:{NAVY};border-radius:999px;padding:{'0 18px 6px' if ur else '8px 18px'}'>{W(t['tag'], 16 if not ur else 20, YEL, 800, 'letter-spacing:1.5px')}</div></div>
<div class='abs' style='top:110px;{end}:34px;width:300px;height:250px;border-radius:24px;overflow:hidden;border:6px solid #fff;box-shadow:0 14px 30px #0005'><img src='{reg}' style='width:100%;height:100%;object-fit:cover'></div>
<div class='abs' style='top:28px;{end}:34px;background:#E53935;border-radius:10px;padding:{'0 16px 6px' if ur else '8px 16px'};box-shadow:0 6px 12px #0004'>{W(t['urgent'], 20, '#fff', 800, 'letter-spacing:2px')}</div>

<div class='abs' style='top:{462 if ur else 448}px;{start}:30px;width:520px'>
 <div style='display:inline-flex;align-items:center;gap:10px;background:linear-gradient(90deg,{TEAL2},{TEAL});border-radius:{'0 30px 30px 0' if not ur else '30px 0 0 30px'};padding:{'0 26px 6px 18px' if ur else '8px 26px 8px 18px'}'>{icon('user', 26, '#fff', 2.3)}{W(t['duties_h'], 30, '#fff', anton=True, extra='letter-spacing:1px')}</div>
 <div style='margin-top:6px'>{duties}</div></div>
<div class='abs' style='top:448px;{end}:30px;width:480px;height:400px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:10px'>{grid}</div>

<div class='abs' style='top:868px;{start}:30px;width:380px;height:178px;border-radius:20px;background:linear-gradient(135deg,{TEAL},{NAVY});box-shadow:0 10px 22px #0004;display:flex;flex-direction:column;align-items:center;justify-content:center'>
 {W(t['sal_h'], 30, '#fff', anton=True, extra='letter-spacing:2px')}
 <div style='font:400 78px Anton;color:{YEL};line-height:1;direction:ltr'>$550 <span style='font-size:40px'>USD</span></div>
 <div style='margin-top:6px;background:{ORG};padding:{'0 22px 4px' if ur else '4px 22px'};clip-path:polygon(6% 0,94% 0,100% 50%,94% 100%,6% 100%,0 50%)'>{W(t['sal_sub'], 18, '#fff', 800, 'letter-spacing:2px')}</div></div>
<div class='abs' style='top:868px;{end}:30px;width:620px;height:178px;border-radius:20px;background:#fff;box-shadow:0 10px 22px rgba(19,41,75,.12);display:grid;grid-template-columns:repeat(4,1fr);direction:{t['dir']}'>{stats}</div>

<div class='abs' style='top:1058px;left:30px;right:30px;height:122px;border-radius:20px;background:#fff;box-shadow:0 10px 22px rgba(19,41,75,.12);display:flex;align-items:center;padding:0 10px'>
 <div style='width:120px;display:flex;align-items:center;justify-content:center;align-self:stretch;background:{NAVY};margin:-0 0;border-radius:{'0 14px 14px 0' if ur else '14px 0 0 14px'}'>{W(t['fac_h'], 22, YEL, anton=True, extra='letter-spacing:1px;text-align:center')}</div>{fac}</div>

<div class='abs' style='top:1190px;left:0;width:1080px;height:160px;background:linear-gradient(100deg,{NAVY},{TEAL2})'></div>
<div class='abs' style='top:1204px;left:30px;width:600px;height:132px;background:#fff;border-radius:18px;display:grid;grid-template-columns:1fr 1fr;align-content:center;gap:10px 12px;padding:0 18px;box-sizing:border-box;box-shadow:0 8px 18px #0006;direction:ltr'>{nums}</div>
<div class='abs' style='top:1200px;right:34px;width:400px;text-align:right'>
 {W(t['apply'], 40, YEL, anton=True, extra='letter-spacing:1px')}
 {W(t['apply_sub'], 22 if ur else 18, '#E3F4F7', 700, 'margin-top:' + ('-4' if ur else '6') + 'px')}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px;direction:ltr'>{icon('mail', 22, YEL, 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div>
 {'' if ur else f"<div style='font:600 12.5px Archivo;color:#BFD6E0;margin-top:6px;direction:ltr'>{ADDRESS}</div>"}</div>
</div>"""
    return (f"<!doctype html><html lang='{lang}' dir='{t['dir']}'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#F4F8FB'>{body}</div></body></html>")


if __name__ == "__main__":
    for lang in (sys.argv[1:] or ["en", "ur"]):
        print(render(build(lang), TXT[lang]["out"]))
