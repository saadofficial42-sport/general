"""Saudi Arabia — Housekeeping Workers, Urdu (2026-11-11). User facts: salary 1000 + 200 SAR, duty 12 hours, age 21–26.
"Rate 490" from the user's note is internal and NOT shown. Design: "fresh linen" — white/aqua page with soft bubble
shapes, big rounded photo card, Saudi-green title band, aqua salary disc, three bold fact tiles, green CTA."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

GRN, GRN2, AQUA, AQUA2, INK = "#0A7A4B", "#05502F", "#19B5C8", "#E6F7F9", "#14231C"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.8: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def build():
    photo = (PHOTOS / "ksa_housekeeping_men.jpg").as_uri()   # men only (user)
    bubbles = "".join(f"<circle cx='{x}' cy='{y}' r='{r}' fill='{AQUA}' opacity='{o}'/>" for x, y, r, o in
                      [(980, 140, 120, .10), (90, 620, 80, .08), (1020, 760, 60, .10), (160, 120, 40, .10), (560, 980, 30, .08)])
    facts = [("money", f"{N('1000 + 200')}", "ریال ماہانہ تنخواہ"), ("clock", f"{N(12)} گھنٹے", "روزانہ ڈیوٹی"), ("user", f"{N('21 – 26')} سال", "عمر کی حد")]
    tiles = "".join(f"<div style='flex:1;background:#fff;border-radius:22px;box-shadow:0 10px 22px rgba(5,80,47,.12);border-bottom:6px solid {AQUA if i else GRN};display:flex;flex-direction:column;align-items:center;justify-content:center'>"
                    f"<span style='width:62px;height:62px;border-radius:50%;background:{GRN if i == 0 else AQUA};display:flex;align-items:center;justify-content:center'>{icon(ic, 32, '#fff', 2.2)}</span>"
                    f"{T(v, 38, INK, 'font-weight:700;margin-top:6px', 1.6)}{T(l, 21, '#56685E', 'font-weight:700;margin-top:4px', 1.5)}</div>" for i, (ic, v, l) in enumerate(facts))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<div class='abs' style='inset:0;background:linear-gradient(180deg,#fff 0%,{AQUA2} 100%)'></div>
<svg class='abs' style='top:0;left:0' width='1080' height='1350'>{bubbles}</svg>
<div class='abs' style='top:30px;right:34px'>{logo_img('logo-horizontal-light', 'width:310px;height:80px;object-position:right')}</div>
<div class='abs' style='top:30px;left:34px;filter:drop-shadow(0 6px 12px #0004)'>{flag('saudi', 130, True, 'sahk')}</div>
<div class='abs' style='top:150px;left:40px;width:470px;height:560px;border-radius:240px 240px 30px 30px;overflow:hidden;border:8px solid #fff;box-shadow:0 20px 40px rgba(5,80,47,.25)'>
 <img src='{photo}' style='width:100%;height:100%;object-fit:cover;object-position:40% 20%'></div>
<div class='abs' style='top:140px;right:40px;width:510px;text-align:right'>
 <div style='display:inline-block;background:#E53935;border-radius:12px;padding:0 20px 6px'>{T('فوری ضرورت', 30, '#fff', 'font-weight:700', 1.6)}</div>
 {T('برائے سعودی عرب', 40, GRN, 'font-weight:700;margin-top:18px;margin-bottom:34px', 1.7)}
 <div style='margin-top:0;background:linear-gradient(135deg,{GRN},{GRN2});border-radius:24px;padding:4px 26px 16px;box-shadow:0 14px 28px rgba(5,80,47,.3)'>
  {T('ہاؤس کیپنگ', 74, '#fff', 'font-weight:700;margin-top:10px', 1.9)}{T('ورکرز', 60, '#BFF2E0', 'font-weight:700;margin-top:6px', 1.9)}
  <div style='font:400 28px Anton;color:#fff;letter-spacing:3px;direction:ltr;text-align:right;margin-top:6px'>HOUSEKEEPING WORKERS</div></div></div>

<div class='abs' style='top:760px;left:40px;right:40px;height:230px;display:flex;gap:18px'>{tiles}</div>
<div class='abs' style='top:1022px;left:40px;right:40px;height:110px;border-radius:24px;background:#fff;border:3px dashed {AQUA};display:flex;align-items:center;justify-content:center;gap:16px'>
 {icon('doc', 40, GRN, 2)}{T(f"اپنی {N('CV')}، پاسپورٹ اور شناختی کارڈ کی کاپی واٹس ایپ کریں", 28, INK, 'font-weight:700', 1.8)}</div>

<div class='abs' style='top:1166px;left:0;width:1080px;height:184px;background:linear-gradient(100deg,{GRN2},{GRN})'></div>
<div class='abs' style='top:1192px;left:34px;display:grid;grid-template-columns:auto auto;gap:14px 30px;direction:ltr'>{nums}</div>
<div class='abs' style='top:1180px;right:40px;width:380px;text-align:right'>
 {T('ابھی رابطہ کریں!', 44, '#fff', 'font-weight:700', 1.6)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr;margin-top:6px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Saudi-Arabia-Housekeeping-Workers-Urdu.png"))
