"""Uzbekistan factory workers — v6 Urdu (2026-10-22): Urdu version of uzbekistan_v6_en.py, mirrored for right-to-left,
with the woman photo removed at user request (main photo = RS Links packer).
Original English notes: user asked for a different design, pictures and style.
Facts unchanged from v5 (demands/2026-10-17-uzbekistan-factory): Tashkent, $550 USD/month, 50 posts, 10 hours,
age 21–35, processing 30–35 days, 5 duties, free accommodation / transport / medical / food + other facilities.
Design: "Silk Road mosaic" — cream page, Uzbek turquoise tile-pattern bands, three-photo mosaic (new photos: woman
production worker, RS Links scanner and machine-operator shots), navy title ribbon, eight-point-star salary badge,
duty / facility columns, turquoise CTA with four numbers in a 2x2 grid."""
import math

from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

TQ, TQ2, NAVY, GOLD, CREAM, INK, RED = "#0E8FA8", "#0A6A80", "#0F2A47", "#F2B33D", "#FBF6EC", "#16202B", "#CE1126"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.75: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"


def tiles(w, h, c1, c2, c3):
    """Uzbek majolica-style band: eight-point stars and diamonds."""
    s, step = "", h
    for x in range(0, w + step, step):
        cx, cy, r = x + step / 2, h / 2, h * .42
        pts = " ".join(f"{cx + (r if i % 2 == 0 else r * .55) * math.cos(math.radians(i * 22.5)):.1f},"
                       f"{cy + (r if i % 2 == 0 else r * .55) * math.sin(math.radians(i * 22.5)):.1f}" for i in range(16))
        s += (f"<polygon points='{pts}' fill='{c1}'/><circle cx='{cx}' cy='{cy}' r='{r * .3:.1f}' fill='{c2}'/>"
              f"<path d='M{x} {cy} L{x + 6} {cy - 6} L{x + 12} {cy} L{x + 6} {cy + 6}Z' fill='{c3}'/>")
    return f"<svg width='{w}' height='{h}' style='display:block;background:{TQ2}'>{s}</svg>"


def star8(size, fill):
    c, r1, r2 = size / 2, size / 2, size / 2 * .78
    pts = " ".join(f"{c + (r1 if i % 2 == 0 else r2) * math.cos(math.radians(i * 22.5 - 90)):.1f},"
                   f"{c + (r1 if i % 2 == 0 else r2) * math.sin(math.radians(i * 22.5 - 90)):.1f}" for i in range(16))
    return f"<svg width='{size}' height='{size}' style='display:block'><polygon points='{pts}' fill='{fill}'/></svg>"


def ph(name, pos="center"):
    return f"<img src='{(PHOTOS / name).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos};display:block'>"


def build():
    stats = [("user", N("50"), "آسامیاں"), ("clock", f"{N(10)} &nbsp;گھنٹے", "روزانہ ڈیوٹی"), ("calendar", f"{N('21 – 35')} سال", "عمر کی حد"), ("doc", f"{N('30 – 35')} دن", "پروسیسنگ ٹائم")]
    stat = "".join(f"<div style='flex:1;display:flex;align-items:center;gap:12px;padding:0 16px;{'border-right:2px solid #ffffff33;' if i else ''}'>"
                   f"{icon(ic, 34, GOLD, 2.2)}<div>{T(v, 26, '#fff', 'font-weight:700;white-space:nowrap', 1.9)}{T(l, 17, '#BFE6EE', 'font-weight:700', 1.6)}</div></div>"
                   for i, (ic, v, l) in enumerate(stats))
    duties = ["عمومی فیکٹری ورک", "پیکجنگ", "اسٹوری (آرڈرنگ)", "مال سامان کی صفائی کرنا", "پروڈکشن لائن پر کام"]
    duty_li = "".join(f"<div style='display:flex;align-items:center;gap:14px;padding:3px 0;border-bottom:2px dotted #D9CDB6'>"
                      f"<span style='width:34px;height:34px;background:{NAVY};color:{GOLD};font:400 19px Anton;display:flex;align-items:center;justify-content:center;transform:rotate(45deg);flex:none;margin-right:6px'>"
                      f"<span style='transform:rotate(-45deg)'>{i + 1}</span></span>{T(d, 25, INK, 'font-weight:700', 1.85)}</div>" for i, d in enumerate(duties))
    fac = [("home", "مفت رہائش"), ("bus", "مفت ٹرانسپورٹ"), ("medical", "مفت میڈیکل"), ("food", "مفت کھانا"), ("gift", "کمپنی کی طرف سے دیگر سہولیات")]
    fac_li = "".join(f"<div style='display:flex;align-items:center;gap:12px;padding:1px 0;border-bottom:2px dotted #ffffff40'>"
                     f"<span style='width:38px;height:38px;border-radius:50%;background:#ffffff1f;display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 22, GOLD, 2.3)}</span>"
                     f"{T(t, 25, '#fff', 'font-weight:700', 1.85)}</div>" for ic, t in fac)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:{INK};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<div class='abs' style='top:0;left:0'>{tiles(1080, 34, TQ, GOLD, '#fff')}</div>
<div class='abs' style='top:52px;right:34px'>{logo_img('logo-horizontal-light', 'width:330px;height:86px;object-position:right')}</div>
<div class='abs' style='top:36px;left:34px;display:flex;align-items:center;gap:14px;direction:ltr'>
 <div style='filter:drop-shadow(0 4px 8px #0004)'>{flag('uzbekistan', 130, True, 'uz6u')}</div>
 <div style='text-align:left'>{T('فوری ضرورت', 24, RED, 'font-weight:700;text-align:left', 1.8)}{T('تاشقند، ازبکستان', 30, NAVY, 'font-weight:700;text-align:left;margin-top:4px', 1.8)}</div></div>

<div class='abs' style='top:160px;right:34px;width:620px;height:430px;border-radius:26px 26px 120px 26px;overflow:hidden;box-shadow:0 14px 30px rgba(15,42,71,.25)'>{ph('rslinks_worker_pack_x3.png', '55% 30%')}</div>
<div class='abs' style='top:160px;left:34px;width:372px;height:207px;border-radius:26px;overflow:hidden;box-shadow:0 14px 30px rgba(15,42,71,.25)'>{ph('tr_plastic.png', 'center 40%')}</div>
<div class='abs' style='top:383px;left:34px;width:372px;height:207px;border-radius:120px 26px 26px 26px;overflow:hidden;box-shadow:0 14px 30px rgba(15,42,71,.25)'>{ph('rslinks_team_scan_x3.png', 'center 35%')}</div>
<div class='abs' style='top:420px;right:0;background:{NAVY};padding:6px 34px 10px 40px;border-radius:18px 0 0 18px;box-shadow:0 12px 26px #0006;text-align:right'>
 {T('فیکٹری ورکرز', 70, '#fff', 'font-weight:700;margin-bottom:18px', 1.9)}
 {T('بہتر مستقبل کی جانب ایک مضبوط قدم', 22, GOLD, 'font-weight:700', 1.7)}</div>
<div class='abs' style='top:450px;right:640px;width:200px;height:200px;filter:drop-shadow(0 12px 22px #0007)'>{star8(200, GOLD)}
 <div style='position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center'>
  <div style='font:400 58px Anton;color:{NAVY};line-height:1'>$550</div>
  {T('ماہانہ تنخواہ', 18, NAVY, 'font-weight:700;margin-top:4px', 1.5)}</div></div>

<div class='abs' style='top:690px;left:34px;right:34px;height:110px;border-radius:20px;background:linear-gradient(270deg,{TQ2},{TQ});display:flex;align-items:center'>{stat}</div>
<div class='abs' style='top:806px;right:34px;width:500px'>
 {T('کام کی تفصیلات', 34, NAVY, 'font-weight:700', 1.7)}{duty_li}</div>
<div class='abs' style='top:806px;left:34px;width:470px;height:346px;background:{NAVY};border-radius:22px;padding:4px 24px;box-sizing:border-box'>
 {T('سہولیات', 34, GOLD, 'font-weight:700', 1.7)}{fac_li}</div>

<div class='abs' style='top:1172px;left:0;width:1080px;height:178px;background:{TQ2}'></div>
<div class='abs' style='top:1172px;left:0'>{tiles(1080, 20, TQ, GOLD, '#fff')}</div>
<div class='abs' style='top:1206px;left:30px;width:600px;height:126px;background:#fff;border-radius:18px;display:grid;grid-template-columns:1fr 1fr;align-content:center;gap:10px 12px;padding:0 18px;box-sizing:border-box;box-shadow:0 8px 18px #0006;direction:ltr'>{nums}</div>
<div class='abs' style='top:1196px;right:34px;width:400px;text-align:right'>
 {T('ابھی رابطہ کریں!', 38, GOLD, 'font-weight:700', 1.6)}
 {T(f"اپنی {N('CV')} واٹس ایپ کریں", 21, '#E3F4F7', 'font-weight:700;margin-top:4px', 1.9)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:2px;direction:ltr'>{icon('mail', 22, GOLD, 2)}<span style='font:800 21px Archivo;color:#fff'>{EMAIL}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CREAM}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Uzbekistan-Factory-Workers-v6-Urdu.png"))
