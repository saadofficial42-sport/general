"""Tajikistan — tomato tunnel farming, Urdu (2026-10-28). Facts: demands/2026-10-28-tajikistan-tomato/facts.md
(converted from another agency's illustrated ad; content only). Real photo: by_agriculture.jpg (farm harvest) until a
real tomato-tunnel photo is supplied (assets/photos/tj_tomato.*). Design: "greenhouse" — white page with soft green
arches (polytunnel ribs), tomato-red accents, photo in a tunnel-arch frame, two-column requirements / facilities."""
import math

from common import PHONES, PHOTOS, font_css, icon, logo_img, render, whatsapp_icon

GRN, GRN2, RED, LEAF, INK, CREAM = "#2E7D32", "#1B5E20", "#D7301F", "#E8F5E9", "#1D2A1F", "#FFFDF7"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.75: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def flag_tj(w=150):
    """Tajikistan: red / white (wider) / green, gold crown under an arc of seven stars; ratio 1:2."""
    h = w / 2
    cx, cy = w / 2, h / 2
    stars = ""
    for k in range(7):
        a = math.radians(-160 + k * (140 / 6))
        sx, sy, r = cx + h * .26 * math.cos(a), cy + h * .02 + h * .26 * math.sin(a), h * .045
        pts = " ".join(f"{sx + (r if i % 2 == 0 else r * .4) * math.cos(math.radians(-90 + i * 36)):.1f},"
                       f"{sy + (r if i % 2 == 0 else r * .4) * math.sin(math.radians(-90 + i * 36)):.1f}" for i in range(10))
        stars += f"<polygon points='{pts}' fill='#F8C300'/>"
    crown = (f"<path d='M{cx - h * .14} {cy + h * .1} L{cx - h * .14} {cy - h * .02} L{cx - h * .07} {cy + h * .04} L{cx} {cy - h * .06} "
             f"L{cx + h * .07} {cy + h * .04} L{cx + h * .14} {cy - h * .02} L{cx + h * .14} {cy + h * .1}Z' fill='#F8C300'/>")
    return (f"<svg width='{w}' height='{h}' style='display:block;box-shadow:0 4px 10px #0003'><rect width='{w}' height='{h * 2 / 7}' fill='#CC0000'/>"
            f"<rect y='{h * 2 / 7}' width='{w}' height='{h * 3 / 7}' fill='#fff'/><rect y='{h * 5 / 7}' width='{w}' height='{h * 2 / 7}' fill='#006600'/>{crown}{stars}</svg>")


def build():
    photo = (PHOTOS / "by_agriculture.jpg").as_uri()
    ribs = "".join(f"<path d='M{x} 600 C {x} 330, {x + 260} 330, {x + 260} 600' stroke='{GRN}' stroke-opacity='.10' stroke-width='6' fill='none'/>" for x in range(-120, 1100, 180))
    req = [("user", f"{N('3 – 5')} سال ٹنل فارمنگ کا تجربہ"), ("gear", "درجہ حرارت اور موسمیاتی کنٹرول کا ماہر"),
           ("check", "اسپرے شیڈول اور کیڑے مار ادویات کی معلومات"), ("leaf", "آبپاشی اور کھاد کا انتظام"), ("shield", "ٹماٹر کی فصل کی بیماریوں کی روک تھام")]
    fac = [("plane", "ویزا، ٹکٹ اور پروٹیکٹر شامل"), ("money", f"ماہانہ تنخواہ: {N('450')} ڈالر"), ("home", "کھانا اور رہائش کمپنی کی طرف سے"),
           ("plane", "واپسی کا ہوائی ٹکٹ مفت"), ("video", "انٹرویو آن لائن (زوم)")]
    li = lambda items, c, bg: "".join(f"<div style='display:flex;align-items:center;gap:12px;padding:4px 0;border-bottom:1px dashed {c}44'>"
                                      f"<span style='width:44px;height:44px;border-radius:12px;background:{bg};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 24, c, 2.3)}</span>"
                                      f"{T(t, 22, INK, 'font-weight:700', 1.8)}</div>" for ic, t in items)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<svg class='abs' style='top:0;left:0' width='1080' height='620'>{ribs}</svg>
<div class='abs' style='top:0;left:0;width:1080px;height:12px;display:flex'><div style='flex:2;background:#CC0000'></div><div style='flex:3;background:#fff'></div><div style='flex:2;background:#006600'></div></div>
<div class='abs' style='top:34px;right:34px'>{logo_img('logo-horizontal-light', 'width:320px;height:84px;object-position:right')}</div>
<div class='abs' style='top:40px;left:40px'>{flag_tj(160)}</div>
<div class='abs' style='top:150px;right:40px;width:560px;text-align:right'>
 <div style='display:inline-block;background:{RED};border-radius:12px;padding:0 18px 6px'>{T('فوری ضرورت', 28, '#fff', 'font-weight:700', 1.6)}</div>
 {T('تاجکستان ورک ویزا', 70, GRN2, 'font-weight:700;margin-top:30px', 1.75)}
 {T('ٹماٹر ٹنل فارمنگ', 56, RED, 'font-weight:700;margin-top:4px', 1.75)}
 <div style='display:inline-flex;align-items:center;gap:8px;margin-top:10px;background:{LEAF};border-radius:999px;padding:0 18px 6px'>{icon('pin', 24, GRN, 2.4)}{T('دوشنبے (دارالحکومت)، تاجکستان', 24, INK, 'font-weight:700', 1.6)}</div></div>
<div class='abs' style='top:130px;left:40px;width:400px;height:470px;border-radius:200px 200px 24px 24px;overflow:hidden;border:8px solid #fff;outline:4px solid {GRN};box-shadow:0 18px 36px rgba(27,94,32,.25)'>
 <img src='{photo}' style='width:100%;height:100%;object-fit:cover;object-position:center 40%'></div>
<div class='abs' style='top:500px;left:300px;width:190px;height:190px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FF6A55,{RED} 60%,#9E1B10);border:6px solid #fff;box-shadow:0 12px 24px #0004;display:flex;flex-direction:column;align-items:center;justify-content:center'>
 <span class='num' style='font-size:56px;color:#fff;line-height:1'>$450</span>{T('ماہانہ تنخواہ', 20, '#fff', 'font-weight:700', 1.6)}</div>

<div class='abs' style='top:720px;left:34px;right:34px;display:flex;gap:18px'>
 <div style='flex:1;background:#fff;border-radius:22px;border-top:8px solid {GRN};box-shadow:0 10px 24px rgba(0,0,0,.08);padding:4px 20px 10px'>
  {T('ضروریات', 34, GRN2, 'font-weight:700', 1.7)}{li(req, GRN, LEAF)}</div>
 <div style='flex:1;background:#fff;border-radius:22px;border-top:8px solid {RED};box-shadow:0 10px 24px rgba(0,0,0,.08);padding:4px 20px 10px'>
  {T('سہولیات', 34, RED, 'font-weight:700', 1.7)}{li(fac, RED, '#FDECEA')}</div></div>

<div class='abs' style='top:1176px;left:0;width:1080px;height:174px;background:linear-gradient(100deg,{GRN2},{GRN})'></div>
<div class='abs' style='top:1196px;left:34px;display:grid;grid-template-columns:auto auto;gap:14px 30px;direction:ltr'>{nums}</div>
<div class='abs' style='top:1184px;right:40px;width:380px;text-align:right'>
 {T('ابھی رابطہ کریں!', 40, '#FFE082', 'font-weight:700', 1.6)}
 {T(f"اپنی {N('CV')} واٹس ایپ کریں", 21, '#fff', 'font-weight:700', 1.8)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr'>{icon('mail', 22, '#FFE082', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CREAM}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Tajikistan-Tomato-Tunnel-Farming-Urdu.png"))
