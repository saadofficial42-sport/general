"""Kuwait — Bike Riders v2, Urdu (mirror of kuwait_riders_v2.py). Original notes: Kuwait — Bike Riders v2, English (2026-11-08). Same facts as kuwait_riders.py (demands/2026-10-27-kuwait-riders):
145 KWD, 12 hours, accommodation / medical / transportation by company. User re-sent the source ad; this version
uses its rider + Kuwait Towers photo (kw_rider_towers.jpg). Dropped again: "stable job, good salary, better future",
"genuine opportunities", "your trust our commitment". Design: "route card" — white page, tall right photo panel with
red-white-green edge stripe, red 145 KWD price tag, numbered route-stop perk list on a dashed line, black CTA."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

RED, RED2, KG, INK, SOFT = "#D7262E", "#9E141B", "#007A3D", "#14171C", "#F4F5F7"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.8: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def build():
    photo = (PHOTOS / "kw_rider_towers.jpg").as_uri()
    perks = [("clock", f"{N(12)} گھنٹے", "ڈیوٹی ٹائم"), ("home", "رہائش", "کمپنی کی طرف سے"),
             ("medical", "میڈیکل", "کمپنی کی طرف سے"), ("bus", "ٹرانسپورٹ", "کمپنی کی طرف سے")]
    stops = "".join(f"<div style='position:relative;display:flex;align-items:center;gap:18px;height:100px'>"
                    f"<span style='width:64px;height:64px;border-radius:50%;background:{RED if i == 0 else '#fff'};border:4px solid {RED};display:flex;align-items:center;justify-content:center;flex:none;z-index:1'>{icon(ic, 30, '#fff' if i == 0 else RED, 2.3)}</span>"
                    f"<div style='display:flex;align-items:baseline;gap:12px'>{T(a, 32, INK, 'font-weight:700', 1.7)}{T('(' + b + ')', 20, '#6A717C', 'font-weight:700', 1.7)}</div></div>"
                    for i, (ic, a, b) in enumerate(perks))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<div class='abs' style='top:0;left:0;width:470px;height:1170px;overflow:hidden'><img src='{photo}' style='width:100%;height:100%;object-fit:cover;object-position:center 20%'>
 <div style='position:absolute;inset:0;background:linear-gradient(270deg,#fff 0%,#fff0 18%)'></div></div>
<div class='abs' style='top:0;left:470px;width:14px;height:1170px;display:flex;flex-direction:column'><div style='flex:1;background:{KG}'></div><div style='flex:1;background:#fff;border-right:1px solid #ddd'></div><div style='flex:1;background:{RED}'></div><div style='flex:.4;background:#111'></div></div>
<div class='abs' style='top:36px;right:40px'>{logo_img('logo-horizontal-light', 'width:300px;height:78px;object-position:right')}</div>
<div class='abs' style='top:140px;right:40px;width:560px;text-align:right'>
 <div style='display:flex;align-items:center;gap:14px;justify-content:flex-start'><span style='background:{RED};border-radius:8px;padding:0 16px 6px'>{T('فوری ضرورت', 26, '#fff', 'font-weight:700', 1.6)}</span>{flag('kw', 100, True, 'kwv2u')}</div>
 {T('بائیک رائیڈرز', 100, INK, 'font-weight:700;margin-top:20px', 1.6)}
 {T('برائے کویت', 64, RED, 'font-weight:700;margin-top:10px', 1.6)}</div>
<div class='abs' style='top:590px;right:40px;width:440px;height:140px;background:linear-gradient(225deg,{RED},{RED2});clip-path:polygon(12% 0,100% 0,100% 100%,12% 100%,0 50%);display:flex;align-items:center;justify-content:flex-start;gap:16px;padding-right:26px;box-sizing:border-box;filter:drop-shadow(0 10px 16px rgba(158,20,27,.35))'>
 <span style='width:22px;height:22px;border-radius:50%;background:#fff'></span>
 <div>{T('ماہانہ تنخواہ', 20, '#FFD9DB', 'font-weight:700;margin-bottom:8px', 1.3)}<div style='font:400 64px Anton;color:#fff;line-height:1;direction:ltr'>145 KWD</div></div></div>
<div class='abs' style='top:756px;right:40px;width:520px'>
 <div style='position:absolute;right:30px;top:30px;bottom:30px;border-right:4px dashed {RED}66'></div>{stops}</div>
<div class='abs' style='top:1170px;left:0;width:1080px;height:180px;background:{INK};border-top:6px solid {RED}'></div>
<div class='abs' style='top:1196px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px;direction:ltr'>{nums}</div>
<div class='abs' style='top:1180px;right:40px;width:380px;text-align:right'>
 {T('ابھی رابطہ کریں!', 42, '#fff', 'font-weight:700', 1.6)}
 {T(f"اپنی {N('CV')} واٹس ایپ کریں", 21, '#C9CED6', 'font-weight:700', 1.8)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Kuwait-Bike-Riders-v2-Urdu.png"))
