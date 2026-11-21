"""Uzbekistan — Drivers, Urdu (2026-11-21). Same facts and design as uzbekistan_drivers.py, set right-to-left."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon
from uzbekistan_drivers import NAVY, NAVY2, GOLD, GOLD2, TQ, CREAM, INK, EMAIL

N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.8: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    ben = [("food", "کھانا فراہم"), ("home", "رہائش فراہم"), ("idcard", "ویلڈ ڈرائیونگ لائسنس لازمی"), ("plane", "ٹکٹ اور پروٹیکٹر شامل")]
    cards = "".join(f"<div style='display:flex;align-items:center;gap:14px;background:#fff;border-radius:18px;padding:0 18px;height:84px;box-shadow:0 10px 20px #13265C1f;border-right:7px solid {GOLD if i % 2 else TQ}'>"
                    f"<span style='width:54px;height:54px;border-radius:14px;background:{NAVY};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 30, GOLD2, 2.2)}</span>"
                    f"{T(t, 27, INK, 'font-weight:700;white-space:nowrap', 1.8)}</div>" for i, (ic, t) in enumerate(ben))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<div class='abs' style='inset:0;background:linear-gradient(180deg,#FFD9A0 0%,#FFE9C9 30%,{CREAM} 60%,#fff 100%)'></div>
<div class='abs' style='top:150px;right:0;width:720px;height:650px;overflow:hidden'><img src='{P("uz_chauffeur_car_ref.jpg")}' style='width:100%;height:100%;object-fit:cover;object-position:left center'>
 <div style='position:absolute;inset:0;background:linear-gradient(90deg,#FFE9C9 0%,#FFE9C900 22%),linear-gradient(0deg,{CREAM} 0%,{CREAM}00 18%),linear-gradient(180deg,#FFE2B8 0%,#FFE2B800 16%)'></div></div>
<div class='abs' style='top:24px;right:30px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0002'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:right')}</div>
<div class='abs' style='top:26px;left:30px;filter:drop-shadow(0 6px 10px #0004)'>{flag('uzbekistan', 120, True, 'uzdru')}</div>
<div class='abs' style='top:130px;left:24px;width:330px;text-align:center'>
 <div style='display:inline-block;background:{NAVY};border-radius:8px;padding:0 18px'>{T('فوری ضرورت', 28, GOLD2, 'font-weight:700', 1.7)}</div>
 {T('ڈرائیورز', 104, NAVY, 'font-weight:700;margin-top:2px', 1.7)}
 {T('برائے ازبکستان', 46, GOLD, 'font-weight:700;margin-top:-10px', 1.7)}
 <div style='font:400 22px Anton;color:{NAVY};letter-spacing:3px;direction:ltr;text-align:center'>DRIVERS · UZBEKISTAN</div></div>
<div class='abs' style='top:570px;left:44px;width:300px;height:210px;border-radius:18px;overflow:hidden;border:6px solid #fff;box-shadow:0 14px 26px #13265C40;transform:rotate(-3deg)'><img src='{P("driver_taxi.jpg")}' style='width:100%;height:100%;object-fit:cover;object-position:40% 40%'></div>

<div class='abs' style='top:810px;left:30px;right:30px;height:140px;border-radius:24px;background:linear-gradient(270deg,{NAVY2},{NAVY});display:flex;align-items:center;justify-content:space-between;padding:0 36px;box-shadow:0 14px 28px #13265C55'>
 <div>{T('ماہانہ تنخواہ', 30, GOLD2, 'font-weight:700', 1.6)}{T(f"{N(500)} امریکی ڈالر", 22, '#C9D3EE', 'font-weight:700', 1.6)}</div>
 <div style='font:400 84px Anton;color:#fff;line-height:1;direction:ltr'>PKR 1,40,000<span style='font-size:28px;color:{GOLD2}'>*</span></div></div>
<div class='abs' style='top:968px;left:30px;right:30px;display:grid;grid-template-columns:1fr 1fr;gap:14px'>{cards}</div>
<div class='abs' style='top:1158px;right:40px'>{T(f"* تقریباً، موجودہ ڈالر ریٹ کے مطابق ({N('USD 500')})", 16, '#6A7280', 'font-weight:700', 1.5)}</div>

<div class='abs' style='top:1190px;left:0;width:1080px;height:160px;background:linear-gradient(100deg,{NAVY2},{NAVY})'></div>
<div class='abs' style='top:1190px;left:0;width:1080px;height:6px;background:linear-gradient(90deg,{TQ},{GOLD},{TQ})'></div>
<div class='abs' style='top:1208px;left:30px;right:30px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:6px 0;direction:ltr'>{nums}</div>
<div class='abs' style='top:1292px;left:30px;right:30px;display:flex;justify-content:space-between;align-items:center'>
 {T(f"اپنی {N('CV')} اور لائسنس واٹس ایپ کریں", 26, GOLD2, 'font-weight:700', 1.7)}
 <span style='display:flex;align-items:center;gap:8px;direction:ltr'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></span></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CREAM}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Uzbekistan-Drivers-Urdu.png"))
