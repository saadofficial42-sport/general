"""Saudi Arabia — Dumper Drivers, Urdu (2026-11-20). Converted from a WhatsApp text demand (content only): well-known
Saudi company (not named); city Riyadh; 20 fresh Pakistani drivers; dumper driver; salary 1700 SAR + trip overtime;
contract 2 years; accommodation by sponsor (written "رہائش فراہم"); other benefits per Saudi labour law.
No dumper-driver photo in the library (the truck photo carries a retailer's branding) — a vector dumper truck is used
as a TEMPORARY fallback and a real photo has been requested.
Design: "hazard yard" — charcoal page with yellow/black hazard stripes, Riyadh skyline silhouette, huge yellow Nastaliq
title, big dumper on a dusty road band, yellow salary plate, white fact tiles with Saudi-green icons, green footer."""
from common import PHONES, flag, font_css, icon, logo_img, render, whatsapp_icon

CH, CH2, YEL, YEL2, GRN, GRN2, INK = "#1D1F22", "#121315", "#FFC21A", "#FFD95C", "#006C35", "#00431F", "#1D1F22"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.8: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"
HAZ = f"repeating-linear-gradient(-45deg,{YEL} 0 26px,{CH2} 26px 52px)"


def dumper(w):
    return (f"<svg width='{w}' height='{w * .52:.0f}' viewBox='0 0 600 312'>"
            f"<path d='M40 70 L330 70 L360 190 L60 190 Z' fill='{YEL}' stroke='{CH2}' stroke-width='6'/>"
            f"<path d='M70 90 L320 90 M80 120 L330 120 M90 150 L340 150' stroke='#E0A400' stroke-width='6'/>"
            f"<rect x='370' y='96' width='150' height='104' rx='10' fill='{YEL}' stroke='{CH2}' stroke-width='6'/>"
            f"<path d='M395 112 H470 L490 150 H395Z' fill='#9CC9E8' stroke='{CH2}' stroke-width='5'/>"
            f"<rect x='520' y='150' width='40' height='50' rx='6' fill='{YEL}' stroke='{CH2}' stroke-width='6'/>"
            f"<rect x='30' y='190' width='540' height='34' rx='6' fill='#3A3D42'/>"
            + "".join(f"<circle cx='{x}' cy='245' r='44' fill='{CH2}'/><circle cx='{x}' cy='245' r='18' fill='#8A8F96'/>" for x in (110, 220, 470))
            + "</svg>")


def skyline(w, col):
    s = "".join(f"<rect x='{x}' y='{120 - h}' width='{bw}' height='{h}' fill='{col}'/>" for x, bw, h in [(0, 60, 40), (70, 40, 70), (120, 70, 50), (200, 36, 90), (250, 80, 45), (340, 50, 60), (400, 60, 38), (470, 44, 76), (530, 90, 48), (630, 50, 64), (690, 70, 40), (770, 40, 58), (820, 90, 46), (920, 60, 70), (990, 90, 42)])
    s += f"<path d='M600 120 L612 10 L624 120Z' fill='{col}'/><ellipse cx='612' cy='34' rx='16' ry='9' fill='none' stroke='{col}' stroke-width='5'/>"
    s += f"<path d='M300 120 V30 Q330 0 360 30 V120Z' fill='{col}'/>"
    return f"<svg width='{w}' height='120' viewBox='0 0 1080 120' preserveAspectRatio='none'>{s}</svg>"


def build():
    facts = [("pin", "شہر: ریاض"), ("user", f"{N(20)} فریش پاکستانی ڈرائیورز"), ("calendar", f"معاہدہ {N(2)} سال"),
             ("home", "رہائش فراہم"), ("check", "دیگر مراعات سعودی لیبر لاء کے مطابق"), ("doc", f"اپنی {N('CV')} واٹس ایپ کریں")]
    tiles = "".join(f"<div style='display:flex;align-items:center;gap:12px;background:#fff;border-radius:14px;padding:0 14px;height:70px;box-shadow:0 8px 16px #0005'>"
                    f"<span style='width:46px;height:46px;border-radius:12px;background:{GRN};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 26, '#fff', 2.2)}</span>"
                    f"{T(t, 23, INK, 'font-weight:700;white-space:nowrap', 1.8)}</div>" for ic, t in facts)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<div class='abs' style='inset:0;background:radial-gradient(circle at 70% 30%,#33363B,{CH} 55%,{CH2})'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:22px;background:{HAZ}'></div>
<div class='abs' style='top:40px;right:30px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:right')}</div>
<div class='abs' style='top:42px;left:30px;filter:drop-shadow(0 6px 10px #0008)'>{flag('saudi', 120, True, 'sadd')}</div>
<div class='abs' style='top:130px;right:40px;left:40px;text-align:center'>
 <div style='display:inline-block;background:{GRN};border-radius:999px;padding:0 28px;border:3px solid {YEL}'>{T('فوری ضرورت برائے سعودی عرب', 32, '#fff', 'font-weight:700', 1.75)}</div>
 {T('ڈمپر ڈرائیورز', 124, YEL, 'font-weight:700;margin-top:6px;text-shadow:0 10px 28px #000', 1.7)}
 <div style='font:400 28px Anton;color:#fff;letter-spacing:8px;direction:ltr;margin-top:-10px'>DUMPER DRIVERS · RIYADH</div></div>

<div class='abs' style='top:470px;left:0;width:1080px;opacity:.22'>{skyline(1080, '#8A8F96')}</div>
<div class='abs' style='top:590px;left:0;width:1080px;height:70px;background:linear-gradient(180deg,#5A4A32,#3A3022)'></div>
<div class='abs' style='top:420px;left:30px;filter:drop-shadow(0 20px 26px #000c)'>{dumper(560)}</div>

<div class='abs' style='top:450px;right:40px;width:380px;height:210px;border-radius:24px;background:linear-gradient(135deg,{YEL2},{YEL});box-shadow:0 18px 34px #0009;display:flex;flex-direction:column;align-items:center;justify-content:center;border:5px solid {CH2}'>
 {T('ماہانہ تنخواہ', 28, INK, 'font-weight:700', 1.5)}
 <div style='font:400 96px Anton;color:{INK};line-height:1;direction:ltr'>1700 <span style='font-size:36px'>SAR</span></div>
 {T('+ ٹرپ اوور ٹائم', 30, GRN2, 'font-weight:700', 1.7)}</div>

<div class='abs' style='top:690px;left:0;width:1080px;height:16px;background:{HAZ}'></div>
<div class='abs' style='top:736px;left:30px;right:30px;display:grid;grid-template-columns:1fr 1fr;gap:14px'>{tiles}</div>
<div class='abs' style='top:1010px;left:0;width:1080px;text-align:center'>{T('سعودیہ کی معروف کمپنی کے لیے · ابھی رابطہ کریں!', 36, YEL, 'font-weight:700', 1.75)}</div>

<div class='abs' style='top:1180px;left:0;width:1080px;height:170px;background:linear-gradient(100deg,{GRN2},{GRN})'></div>
<div class='abs' style='top:1172px;left:0;width:1080px;height:8px;background:{HAZ}'></div>
<div class='abs' style='top:1200px;left:30px;right:30px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:10px 0;direction:ltr'>{nums}</div>
<div class='abs' style='top:1300px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:10px;direction:ltr'>{icon('mail', 22, YEL, 2)}<span style='font:800 22px Archivo;color:#fff'>{EMAIL}</span></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CH}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Saudi-Dumper-Drivers-Urdu.png"))
