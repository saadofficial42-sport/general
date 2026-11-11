"""Kyrgyzstan — JUKI machine operators, Urdu (user: do not write "tailors"). Mirror of kyrgyzstan_tailors_juki.py. Original notes: Kyrgyzstan — Trained Tailors (JUKI machine operators), English (2026-11-11). Partner: Anchor Manpower (not named).
Facts from the user's reference ad: 450 USD/month; free accommodation, free food 2x daily, free transport; 1-year visa
extendable on performance; processing 30 days; age 21–40; duty 10 h/day; selection through JUKI machine working videos.
Dropped: "limited vacancies", "work · grow · thrive", "rewarding international career".
Design: "stitched sun" — warm cream page, Kyrgyz red header with the 40-ray sun, dashed 'stitch' borders, big tailor
photo in a stitched frame, gold salary badge, thread-spool fact chips, red video-selection banner, red CTA."""
import math

from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

RED, RED2, SUN, CREAM, INK = "#E8112D", "#9E0B1E", "#FFC400", "#FFF8EC", "#2A1416"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.8: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def sun(size, color, op):
    c, r1, r2 = size / 2, size * .28, size * .5
    rays = "".join(f"<path d='M{c + r1 * math.cos(math.radians(k * 9 - 2)):.1f} {c + r1 * math.sin(math.radians(k * 9 - 2)):.1f} L{c + r2 * math.cos(math.radians(k * 9)):.1f} {c + r2 * math.sin(math.radians(k * 9)):.1f} L{c + r1 * math.cos(math.radians(k * 9 + 2)):.1f} {c + r1 * math.sin(math.radians(k * 9 + 2)):.1f}Z' fill='{color}'/>" for k in range(40))
    return f"<svg width='{size}' height='{size}' style='display:block;opacity:{op}'>{rays}<circle cx='{c}' cy='{c}' r='{r1}' fill='{color}'/></svg>"


def build():
    photo = (PHOTOS / "kg_tailor_juki.jpg").as_uri()
    stitch = f"border:3px dashed {RED}"
    fac = [("home", "مفت رہائش"), ("food", "مفت کھانا (دن میں 2 بار)"), ("bus", "مفت ٹرانسپورٹ")]
    fac_li = "".join(f"<div style='display:flex;align-items:center;gap:12px;padding:2px 0;border-bottom:2px dashed #F2C9CF'>"
                     f"<span style='width:46px;height:46px;border-radius:50%;background:{RED};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 24, '#fff', 2.3)}</span>"
                     f"{T(t.replace('2', N(2)), 25, INK, 'font-weight:700', 1.85)}</div>" for ic, t in fac)
    stats = [("calendar", f"{N(30)} دن", "پروسیسنگ"), ("user", f"{N('21 – 40')} سال", "عمر کی حد"), ("clock", f"{N(10)} گھنٹے", "روزانہ ڈیوٹی"), ("visa", f"{N(1)} سال", "ویزا (قابلِ توسیع)*")]
    stat = "".join(f"<div style='background:#fff;border-radius:18px;{stitch};display:flex;flex-direction:column;align-items:center;justify-content:center'>"
                   f"{icon(ic, 30, RED, 2.3)}{T(v, 28, INK, 'font-weight:700;margin-top:2px', 1.6)}{T(l, 17, '#7A5A5E', 'font-weight:700;margin-top:12px', 1.4)}</div>" for ic, v, l in stats)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<div class='abs' style='top:0;left:0;width:1080px;height:330px;background:linear-gradient(225deg,{RED},{RED2})'></div>
<div class='abs' style='top:-80px;left:-80px'>{sun(420, SUN, .22)}</div>
<div class='abs' style='top:318px;left:0;width:1080px;border-top:4px dashed {SUN}'></div>
<div class='abs' style='top:28px;right:36px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:270px;height:70px;object-position:right')}</div>
<div class='abs' style='top:28px;left:40px;filter:drop-shadow(0 6px 12px #0006)'>{flag('kyrgyzstan', 130, True, 'kgju')}</div>
<div class='abs' style='top:92px;right:40px;text-align:right'>
 {T('فوری ضرورت برائے کرغزستان', 30, SUN, 'font-weight:700', 1.7)}
 {T('جوکی مشین آپریٹرز', 66, '#fff', 'font-weight:700;margin-top:0', 1.75)}
 <div style='font:400 24px Anton;color:#FFE3E6;letter-spacing:2px;direction:ltr;text-align:right;margin-top:10px'>JUKI MACHINE OPERATORS</div></div>

<div class='abs' style='top:366px;right:36px;width:560px;height:430px;border-radius:26px;padding:10px;background:#fff;{stitch};box-sizing:border-box;box-shadow:0 16px 32px rgba(158,11,30,.18)'>
 <div style='width:100%;height:100%;border-radius:18px;overflow:hidden'><img src='{photo}' style='width:100%;height:100%;object-fit:cover;object-position:center 30%'></div></div>
<div class='abs' style='top:730px;right:400px;width:220px;height:220px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFE680,{SUN} 55%,#E0A000);border:7px solid #fff;box-shadow:0 14px 28px #0006;display:flex;flex-direction:column;align-items:center;justify-content:center'>
 {T('تنخواہ', 22, RED2, 'font-weight:700;margin-bottom:10px', 1.4)}<div style='font:400 70px Anton;color:{RED2};line-height:1'>$450</div>{T('ماہانہ', 20, RED2, 'font-weight:700;margin-top:4px', 1.4)}</div>
<div class='abs' style='top:366px;left:36px;width:410px;background:#fff;border-radius:22px;{stitch};padding:4px 22px 6px;box-sizing:border-box'>
 {T('کمپنی کی طرف سے', 30, RED, 'font-weight:700', 1.7)}{fac_li}</div>
<div class='abs' style='top:640px;left:36px;width:410px;height:300px;display:grid;grid-template-columns:1fr 1fr;gap:12px'>{stat}</div>

<div class='abs' style='top:972px;left:36px;right:36px;height:150px;border-radius:24px;background:linear-gradient(240deg,{RED2},{RED});display:flex;align-items:center;gap:24px;padding:0 30px;box-sizing:border-box;box-shadow:0 14px 28px rgba(158,11,30,.3)'>
 <span style='width:92px;height:92px;border-radius:50%;background:{SUN};display:flex;align-items:center;justify-content:center;flex:none'>{icon('video', 48, RED2, 2.2)}</span>
 <div>{T('سلیکشن ورکنگ ویڈیو کے ذریعے', 38, '#fff', 'font-weight:700;margin-bottom:10px', 1.6)}
 {T('جوکی مشین پر کام کرتے ہوئے اپنی ویڈیو بھیجیں', 22, '#FFE3E6', 'font-weight:700', 1.7)}</div></div>
<div class='abs' style='top:1124px;right:36px;left:36px;text-align:right'>{T(f"* {N(1)} سال کا ویزا، کارکردگی کی بنیاد پر قابلِ توسیع", 16, '#7A5A5E', 'font-weight:700', 1.6)}</div>

<div class='abs' style='top:1166px;left:0;width:1080px;height:184px;background:{INK};border-top:5px dashed {SUN}'></div>
<div class='abs' style='top:1194px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px;direction:ltr'>{nums}</div>
<div class='abs' style='top:1180px;right:40px;width:380px;text-align:right'>
 {T('ابھی رابطہ کریں!', 40, SUN, 'font-weight:700', 1.6)}
 {T(f"اپنی {N('CV')} اور جوکی ویڈیو واٹس ایپ کریں", 20, '#E9D9DB', 'font-weight:700', 1.8)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CREAM}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Kyrgyzstan-JUKI-Machine-Operators-Urdu.png"))
