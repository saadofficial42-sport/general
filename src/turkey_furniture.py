"""Turkey — General Workers, furniture factory in Kayseri, Urdu (2026-11-02). Facts: demands/2026-11-02-turkey-furniture/facts.md.
Photos cropped from the reference the user asked to convert (tr_furniture_worker / tr_furniture_showroom).
Design: "joinery" — warm white page, big Turkish-red crescent sweep on the left, oak plank band, photo with a
red frame and wood-grain caption bar, six round-icon fact tiles in two rows, red CTA."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

RED, RED2, OAK, OAK2, CREAM, INK = "#E30A17", "#A30711", "#C8915A", "#8A5A2E", "#FFFBF5", "#1F1A17"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.75: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def build():
    worker, room = (PHOTOS / "tr_furniture_worker.jpg").as_uri(), (PHOTOS / "tr_furniture_showroom.jpg").as_uri()
    facts = [("money", "تنخواہ", f"{N('30,000')} لیرا", "ماہانہ"), ("clock", "ڈیوٹی", f"{N(8)} گھنٹے", "روزانہ"),
             ("overtime", "اوور ٹائم", "باقاعدگی سے", "دیا جائے گا"), ("doc", "معاہدہ", f"{N(1)} سال", "بعد میں قابلِ توسیع"),
             ("home", "رہائش", "کمپنی کی طرف سے", "فراہم کی جائے گی"), ("food", "کھانا", "کمپنی کی طرف سے", "فراہم کیا جائے گا")]
    tiles = "".join(f"<div style='background:#fff;border-radius:20px;box-shadow:0 8px 18px rgba(0,0,0,.08);border-bottom:6px solid {RED if i < 3 else OAK};display:flex;align-items:center;gap:14px;padding:0 18px'>"
                    f"<span style='width:62px;height:62px;border-radius:50%;background:{RED if i < 3 else OAK2};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 32, '#fff', 2.2)}</span>"
                    f"<div>{T(h, 18, '#7A6A5E', 'font-weight:700', 1.5)}{T(v, 26, INK, 'font-weight:700;white-space:nowrap;margin-top:16px', 1.5)}{T(sub, 15, '#7A6A5E', 'font-weight:700;margin-top:10px', 1.4)}</div></div>"
                    for i, (ic, h, v, sub) in enumerate(facts))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<svg class='abs' style='top:0;left:0' width='1080' height='700'><circle cx='-60' cy='250' r='420' fill='{RED}'/><circle cx='70' cy='250' r='340' fill='{CREAM}'/>
 <polygon points='330,170 352,232 418,232 365,270 385,334 330,295 275,334 295,270 242,232 308,232' fill='{RED}' transform='rotate(-18 330 250) scale(.55) translate(270 205)'/></svg>
<div class='abs' style='top:28px;right:34px'>{logo_img('logo-horizontal-light', 'width:320px;height:84px;object-position:right')}</div>
<div class='abs' style='top:30px;left:30px;filter:drop-shadow(0 6px 12px #0005)'>{flag('tr', 130, True, 'trf')}</div>
<div class='abs' style='top:140px;right:40px;width:600px;text-align:right'>
 <div style='display:inline-block;background:{RED};border-radius:12px;padding:0 20px 6px'>{T('ترکی میں فوری ضرورت', 30, '#fff', 'font-weight:700', 1.7)}</div>
 {T('جنرل ورکرز', 84, INK, 'font-weight:700;margin-top:40px', 1.7)}
 <div style='display:inline-flex;align-items:center;gap:10px;margin-top:14px;background:linear-gradient(90deg,{OAK},{OAK2});border-radius:999px;padding:0 22px 6px'>{icon('pin', 26, '#fff', 2.4)}{T('قیصری (Kayseri) فرنیچر فیکٹری', 28, '#fff', 'font-weight:700', 1.7)}</div>
 {T('فیکٹری میں فرنیچر بنانے کے مختلف کاموں کے لیے ملازمین کی ضرورت ہے', 22, '#5E5148', 'font-weight:700;margin-top:10px', 1.8)}</div>
<div class='abs' style='top:200px;left:60px;width:360px;height:420px;border-radius:26px;overflow:hidden;border:8px solid #fff;outline:5px solid {RED};box-shadow:0 18px 36px rgba(0,0,0,.25)'>
 <img src='{worker}' style='width:100%;height:100%;object-fit:cover;object-position:center 30%'></div>

<div class='abs' style='top:660px;left:0;width:1080px;height:22px;background:repeating-linear-gradient(90deg,{OAK} 0 120px,{OAK2} 120px 123px)'></div>
<div class='abs' style='top:706px;left:34px;right:34px;display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:138px;gap:14px'>{tiles}</div>
<div class='abs' style='top:1014px;left:34px;right:34px;height:140px;border-radius:22px;overflow:hidden;box-shadow:0 10px 22px rgba(0,0,0,.15)'>
 <img src='{room}' style='width:100%;height:100%;object-fit:cover;object-position:center 55%'></div>

<div class='abs' style='top:1170px;left:0;width:1080px;height:180px;background:linear-gradient(100deg,{RED2},{RED})'></div>
<div class='abs' style='top:1192px;left:34px;display:grid;grid-template-columns:auto auto;gap:14px 30px;direction:ltr'>{nums}</div>
<div class='abs' style='top:1180px;right:40px;width:380px;text-align:right'>
 {T('ابھی رابطہ کریں!', 40, '#fff', 'font-weight:700', 1.6)}
 {T(f"اپنی {N('CV')} واٹس ایپ کریں", 21, '#FFE1E3', 'font-weight:700', 1.8)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CREAM}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Turkey-Furniture-General-Workers-Urdu.png"))
