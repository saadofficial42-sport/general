"""Uzbekistan all jobs — v4 redesign (2026-10-16): "horizontal job rows" in Uzbek flag stripes.
Same facts as data/uzbekistan_all.py; all three numbers. Factory row uses a real RS Links photo;
rider / car-driver rows use silhouette placeholders until real photos (assets/photos/uz_rider.*, uz_driver.*) exist."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon
from style_trio import driver_scene, rider_scene

BLU, NAVY, GRN, RED, GOLD = "#0099B5", "#0B2545", "#1EB53A", "#CE1126", "#F0B443"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"


def pic(key, w, h, uid):
    for e in ("png", "jpg", "jpeg"):
        p = PHOTOS / f"{key}.{e}"
        if p.exists():
            return f"<img src='{p.as_uri()}' style='width:{w}px;height:{h}px;object-fit:cover;display:block'>"
    return {"uz_rider": rider_scene, "uz_driver": driver_scene}[key](w, h, uid)


def txt(s, px, color, extra="", lh=1.75):
    return f"<div class='t' style='font-size:{px}px;color:{color};line-height:{lh};{extra}'>{s}</div>"


JOBS = [
    {"photo": "uz_rider", "color": GRN, "title": "بائیک رائیڈرز", "sub": "اسکوٹر / موٹر سائیکل", "city": "تاشقند",
     "posts": "50", "sal": "$400", "sal_sub": "ماہانہ + بونس + اوور ٹائم",
     "rows": [("clock", f"ڈیوٹی: {N(12)} گھنٹے روزانہ"), ("home", "رہائش: کمپنی کی طرف سے"), ("food", f"کھانا: دن میں {N(2)} مرتبہ")]},
    {"photo": "uz_driver", "color": NAVY, "title": "کار ڈرائیورز", "sub": "تجربہ کار ڈرائیورز", "city": "تاشقند",
     "posts": "20", "sal": "$450", "sal_sub": "ماہانہ",
     "rows": [("clock", f"ڈیوٹی: {N(12)} گھنٹے روزانہ"), ("home", "رہائش: کمپنی کی طرف سے"), ("food", "کھانا: کمپنی کی طرف سے")]},
    {"photo": "rslinks_worker_pack", "color": "#9A5B0E", "title": "فیکٹری ورکرز", "sub": "ہوزری، پیکنگ، استری، سامان شفٹ کرنا", "city": "تاشقند اور ثمرقند",
     "posts": "50", "sal": "$400", "sal_sub": "امریکی ڈالر",
     "rows": [("clock", f"ڈیوٹی: {N(10)} گھنٹے + اوور ٹائم"), ("home", "رہائش اور میڈیکل"), ("bus", "ٹرانسپورٹ: بذمہ کمپنی")]},
]


def row(j, top, i):
    ph = pic(j["photo"], 330, 212, f"r{i}")
    li = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{icon(ic, 22, j['color'], 2.4)}{txt(t, 18, NAVY, 'font-weight:700', 1.8)}</div>" for ic, t in j["rows"])
    return f"""<div class='abs' style='top:{top}px;left:28px;right:28px;height:212px;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 8px 20px rgba(11,37,69,.16);display:flex;direction:rtl'>
 <div style='width:10px;background:{j['color']}'></div>
 <div style='flex:1;padding:6px 22px 0 14px;display:flex;flex-direction:column'>
  <div style='display:flex;align-items:center;gap:14px'>{txt(j['title'], 36, j['color'], 'font-weight:700', 1.5)}
   <div style='display:flex;align-items:center;gap:4px;margin-inline-start:auto'>{icon('pin', 20, RED, 2.4)}{txt(j['city'], 19, NAVY, 'font-weight:700', 1.6)}</div></div>
  {txt(j['sub'], 16, '#5A6878', 'margin-top:2px', 1.7)}
  <div style='display:flex;gap:16px;align-items:center;margin-top:4px'><div style='display:flex;flex-direction:column;gap:2px'>{li}</div></div></div>
 <div style='width:170px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:{j['color']}12;border-inline-start:2px dashed {j['color']}55'>
  {txt('تنخواہ', 18, j['color'], 'font-weight:700', 1.4)}<div class='num' style='font-size:58px;color:{j['color']};line-height:1.05'>{j['sal']}</div>
  {txt(j['sal_sub'], 15, '#5A6878', 'text-align:center;font-weight:600', 1.5)}</div>
 <div style='position:relative;width:330px;height:212px;flex:none'>{ph}
  <div style='position:absolute;top:12px;left:12px;background:{GOLD};border-radius:12px;padding:0 12px 4px;display:flex;align-items:center;gap:6px;box-shadow:0 3px 8px #0005'>
   <span class='num' style='font-size:34px;color:{NAVY};line-height:1.2'>{j['posts']}</span>{txt('آسامیاں', 15, NAVY, 'font-weight:700', 1.5)}</div></div>
</div>"""


def build():
    nums = "".join(f"<div class='num' style='display:block;font-size:34px;color:{NAVY};line-height:1.06'>{n}</div>" for n in PHONES)
    req1 = [f"عمر: {N('21 – 33')} سال", "متعلقہ تجربہ ضروری", "ذمہ دار اور محنتی", "موٹر سائیکل / اسکوٹر یا کار چلانے میں مہارت", f"{N('Google Maps')} کے استعمال کی صلاحیت"]
    req2 = [f"عمر: {N('21 – 35')} سال", f"ویزا کیٹیگری: {N('B-2')}", f"پروسیسنگ: {N('30 – 35')} دن", "دیگر مراعات مقامی لیبر لاء کے مطابق", "<b style='color:#CE1126'>نوٹ: ٹکٹ پنجاب سے ہوگا</b>"]
    panel = lambda title, items, c: (f"<div style='flex:1;background:#fff;border-radius:20px;padding:4px 18px 8px;border-top:6px solid {c};box-shadow:0 6px 16px rgba(11,37,69,.12)'>"
                                     f"{txt(title, 23, c, 'font-weight:700', 1.7)}"
                                     + "".join(f"<div style='display:flex;align-items:center;gap:8px'>{icon('check', 18, c, 3)}{txt(s, 16, NAVY, 'font-weight:600', 1.85)}</div>" for s in items) + "</div>")
    body = f"""<div class='ur-on' dir='rtl'>
<div class='abs' style='top:0;left:0;width:1080px;height:300px;background:linear-gradient(180deg,{BLU} 0 33%,{RED} 33% 34%,#fff 34% 66%,{RED} 66% 67%,{GRN} 67%)'></div>
<div class='abs' style='top:18px;right:28px;background:#fff;border-radius:18px;padding:4px 14px;box-shadow:0 6px 16px #0004'>{logo_img('logo-horizontal-light', 'width:360px;height:84px')}</div>
<div class='abs' style='top:14px;left:28px;filter:drop-shadow(0 4px 8px #0005)'>{flag('uzbekistan', 150, True, 'uz4')}</div>
<div class='abs' style='top:92px;left:0;right:0;text-align:center'>
 <div style='display:inline-block;background:{NAVY};border-radius:22px;padding:0 40px 8px;box-shadow:0 10px 24px #0006'>
  {txt('فوری ضرورت برائے', 22, GOLD, 'font-weight:700', 1.9)}{txt('ازبکستان', 60, '#fff', 'font-weight:700;margin-top:26px', 1.3)}
  {txt(f"تاشقند اور ثمرقند • کل {N(120)} آسامیاں", 21, '#CFE3F2', 'font-weight:700;margin-top:6px', 1.7)}</div></div>
<div class='abs' style='top:300px;left:0;width:1080px;height:1050px;background:#EEF3F8'></div>
{row(JOBS[0], 316, 0)}{row(JOBS[1], 540, 1)}{row(JOBS[2], 764, 2)}
<div class='abs' style='top:1052px;left:28px;right:28px;height:0'></div>
<div class='abs' style='top:990px;left:28px;right:28px;display:flex;gap:14px'>{panel('بائیک رائیڈرز و ڈرائیورز — شرائط', req1, NAVY)}{panel('فیکٹری ورکرز — تفصیلات', req2, '#9A5B0E')}</div>
<div class='abs' style='top:1236px;left:0;width:1080px;height:114px;background:{NAVY};border-top:5px solid {GOLD}'></div>
<div class='abs' style='top:1210px;left:28px;height:132px;background:#fff;border-radius:22px;display:flex;align-items:center;gap:12px;padding:0 22px 0 12px;direction:ltr;box-shadow:0 8px 18px #0006'>{whatsapp_icon(64)}<div>{nums}</div></div>
<div class='abs' style='top:1232px;right:30px;width:560px;text-align:right'>{txt('اپنا روشن مستقبل ازبکستان سے شروع کریں!', 27, GOLD, 'font-weight:700', 1.6)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr;margin-top:12px'>{icon('mail', 22, GOLD, 2)}<span style='font-family:Archivo;font-size:22px;font-weight:700;color:#fff'>{EMAIL}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#EEF3F8'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Uzbekistan-All-Jobs-v4-Urdu.png"))
