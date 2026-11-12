"""Saudi Arabia — Security Guards, Urdu (2026-11-12). Converted from a newspaper-style ad (content only): famous Saudi
company; salary 1500–1800 SR; height 5'8"; education graduation; English or Arabic speaking required; duty 12 hours;
contract 2 years; accommodation, medical, transport by company; other benefits per Saudi labour law; send CV + documents
(PDF) by WhatsApp / email. Dropped: "instant visa / instant departure".
Design: "guard badge" — charcoal page with gold shield badge motif, big guard photo, gold salary shield, black/gold
requirement chips, Saudi green CTA."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

CH, CH2, GOLD, GOLD2, GRN, INK = "#15181D", "#0B0D10", "#D4A63A", "#F4D27A", "#0B6B3A", "#15181D"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.8: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def shield(w, h, fill, stroke):
    return (f"<svg width='{w}' height='{h}' viewBox='0 0 100 116' style='position:absolute;inset:0'>"
            f"<path d='M50 3 L94 18 V58 C94 86 74 104 50 113 C26 104 6 86 6 58 V18 Z' fill='{fill}' stroke='{stroke}' stroke-width='4'/></svg>")


def build():
    photo = (PHOTOS / "security_airport.jpg").as_uri()
    req = [("user", f"قد {N(5)} فٹ {N(8)} انچ"), ("doc", "تعلیم: گریجویشن"), ("chat", "انگلش یا عربی بول چال لازمی"), ("check", "پڑھے لکھے افراد اپلائی کریں")]
    req_li = "".join(f"<div style='display:flex;align-items:center;gap:12px;background:#ffffff0d;border:1px solid {GOLD}55;border-radius:14px;padding:0 16px'>"
                     f"<span style='width:44px;height:44px;border-radius:50%;background:{GOLD};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 24, CH2, 2.3)}</span>{T(t, 25, '#fff', 'font-weight:700', 1.85)}</div>" for ic, t in req)
    facts = [("clock", f"{N(12)} گھنٹے", "ڈیوٹی"), ("calendar", f"{N(2)} سال", "معاہدہ"), ("home", "رہائش", "بذمہ کمپنی"), ("medical", "میڈیکل", "بذمہ کمپنی"), ("bus", "ٹرانسپورٹ", "بذمہ کمپنی")]
    fact = "".join(f"<div style='flex:1;background:#fff;border-radius:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;border-bottom:5px solid {GOLD}'>"
                   f"{icon(ic, 30, CH, 2.2)}{T(v, 24, INK, 'font-weight:700', 1.6)}{T(l, 16, '#6B6F78', 'font-weight:700;margin-top:8px', 1.3)}</div>" for ic, v, l in facts)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<div class='abs' style='inset:0;background:radial-gradient(circle at 20% 20%,#2A2F38,{CH} 50%,{CH2})'></div>
<div class='abs' style='top:0;left:0;width:500px;height:700px;overflow:hidden'><img src='{photo}' style='width:100%;height:100%;object-fit:cover;object-position:30% 20%'>
 <div style='position:absolute;inset:0;background:linear-gradient(270deg,{CH} 0%,{CH}00 35%),linear-gradient(0deg,{CH} 0%,{CH}00 30%)'></div></div>
<div class='abs' style='top:28px;right:34px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:270px;height:70px;object-position:right')}</div>
<div class='abs' style='top:130px;right:40px;width:560px;text-align:right'>
 <div style='display:flex;align-items:center;gap:14px;justify-content:flex-start'>{T('فوری ضرورت برائے سعودی عرب', 30, GOLD2, 'font-weight:700', 1.7)}{flag('saudi', 96, True, 'sasg')}</div>
 {T('سعودی عرب کی معروف کمپنی کے لیے', 24, '#C9CDD6', 'font-weight:700;margin-top:6px', 1.7)}
 {T('سیکیورٹی گارڈز', 100, '#fff', 'font-weight:700;margin-top:14px;text-shadow:0 8px 22px #000', 1.6)}
 <div style='font:400 30px Anton;color:{GOLD};letter-spacing:4px;direction:ltr;text-align:right;margin-top:6px'>SECURITY GUARDS</div></div>
<div class='abs' style='top:470px;right:110px;width:290px;height:300px'>{shield(290, 300, GOLD, '#fff')}
 <div style='position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;padding-bottom:20px'>
  {T('تنخواہ', 26, CH2, 'font-weight:700;margin-bottom:6px', 1.5)}<div style='font:400 54px Anton;color:{CH2};line-height:1;direction:ltr;white-space:nowrap'>1500 – 1800</div>{T('سعودی ریال', 22, CH2, 'font-weight:700;margin-top:6px', 1.5)}</div></div>

<div class='abs' style='top:780px;left:36px;right:36px;display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:70px;gap:10px 12px'>{req_li}</div>
<div class='abs' style='top:948px;left:36px;right:36px;height:122px;display:flex;gap:10px'>{fact}</div>
<div class='abs' style='top:1080px;left:36px;right:36px;text-align:center'>{T('دیگر مراعات سعودی لیبر لاء کے مطابق', 20, '#C9CDD6', 'font-weight:700', 1.7)}</div>

<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:linear-gradient(100deg,{GRN},#05472A);border-top:5px solid {GOLD}'></div>
<div class='abs' style='top:1184px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px;direction:ltr'>{nums}</div>
<div class='abs' style='top:1166px;right:40px;width:400px;text-align:right'>
 {T('ابھی رابطہ کریں!', 40, GOLD2, 'font-weight:700', 1.6)}
 {T(f"{N('CV')} اور کاغذات ({N('PDF')}) واٹس ایپ یا ای میل کریں", 18, '#E3F0E8', 'font-weight:700;white-space:nowrap', 1.8)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr'>{icon('mail', 22, GOLD2, 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CH}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Saudi-Arabia-Security-Guards-Urdu.png"))
