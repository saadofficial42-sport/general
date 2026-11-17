"""Uzbekistan — Factory Workers, Urdu (2026-11-17). Converted from another agency's Urdu ad (content only; Tashkent
skyline cropped from it at user request). Reference title "پیکٹرے ورکر (Picture Worker)" read as a misspelling of
فیکٹری ورکر (Factory Worker) — flagged to user. Facts: salary 120,000 PKR/month (user; reference said 400 USD); accommodation by company; ticket by
company; protector included; other necessary facilities by company. Dropped: "visa included" (no-visa rule),
"limited seats", slogans. Partner: Mr. Shahid (Karachi) — sheet only.
Design: "Tashkent sky" — Tashkent tower skyline header fading to white, flag-stripe ribbon (sky blue / red / green),
big green Urdu title, framed packing-worker hero + factory-line inset, sky-blue salary disc, four white benefit rows
with coloured icon tabs, navy footer with six numbers."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

SKY, SKY2, GRN, GRN2, RED, NAVY, GOLD, INK = "#1EA7E1", "#0C6FA8", "#1EA34A", "#0F7A34", "#D52B1E", "#0B2545", "#FFC72C", "#0B2545"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.8: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    ben = [("home", SKY2, "رہائش کمپنی کی طرف سے"), ("plane", GRN2, "ٹکٹ کمپنی کی طرف سے"), ("check", RED, "پروٹیکٹر شامل"), ("food", NAVY, "دیگر ضروری سہولیات کمپنی کی طرف سے")]
    rows = "".join(f"<div style='display:flex;align-items:center;gap:14px;background:#fff;border-radius:16px;height:74px;box-shadow:0 8px 16px #0B254514;overflow:hidden'>"
                   f"<span style='width:78px;height:100%;background:{c};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 36, '#fff', 2.2)}</span>"
                   f"{T(t, 27, INK, 'font-weight:700', 1.9)}</div>" for ic, c, t in ben)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<div class='abs' style='inset:0;background:#F4FAFD'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:470px;overflow:hidden'><img src='{P("uz_tashkent_ref.jpg")}' style='width:100%;height:100%;object-fit:cover;object-position:20% 60%'>
 <div style='position:absolute;inset:0;background:linear-gradient(180deg,#0B254566 0%,#0B254500 30%,#F4FAFD00 55%,#F4FAFD 100%)'></div></div>
<div class='abs' style='top:22px;right:30px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0004'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:right')}</div>
<div class='abs' style='top:24px;left:30px;filter:drop-shadow(0 6px 10px #0006)'>{flag('uzbekistan', 120, True, 'uz12')}</div>
<div class='abs' style='top:150px;left:0;width:1080px;text-align:center'>
 <div style='display:inline-block;background:{RED};border-radius:999px;padding:0 30px;box-shadow:0 8px 18px #0005'>{T('فوری ضرورت برائے ازبکستان', 36, '#fff', 'font-weight:700', 1.75)}</div></div>
<div class='abs' style='top:262px;left:0;width:1080px;text-align:center'>
 <div style='display:inline-block;background:#ffffffee;border-radius:26px;padding:0 50px 10px;box-shadow:0 14px 30px #0B254533'>
  {T('فیکٹری ورکرز', 104, GRN, 'font-weight:700;margin-top:-6px', 1.75)}
  <div style='font:400 34px Anton;color:{NAVY};letter-spacing:6px;direction:ltr;margin-top:2px'>FACTORY WORKERS · UZBEKISTAN</div></div></div>
<div class='abs' style='top:520px;left:0;width:1080px;height:10px;display:flex'><span style='flex:1;background:{SKY}'></span><span style='flex:.15;background:{RED}'></span><span style='flex:1;background:#fff'></span><span style='flex:.15;background:{RED}'></span><span style='flex:1;background:{GRN}'></span></div>

<div class='abs' style='top:556px;right:30px;width:560px;height:400px;border-radius:24px;overflow:hidden;border:6px solid #fff;box-shadow:0 18px 34px #0B254533'><img src='{P("rslinks_worker_hero_blue.png")}' style='width:100%;height:100%;object-fit:cover;object-position:35% 22%'></div>
<div class='abs' style='top:870px;right:400px;width:250px;height:170px;border-radius:18px;overflow:hidden;border:5px solid #fff;box-shadow:0 14px 26px #0B254544'><img src='{P("uz_milk_packing.jpg")}' style='width:100%;height:100%;object-fit:cover;object-position:center 40%'></div>
<div class='abs' style='top:560px;left:40px;width:390px;height:300px;border-radius:50%;'>
 <div style='width:300px;height:300px;margin:0 auto;border-radius:50%;background:radial-gradient(circle at 35% 30%,#5CC8F0,{SKY} 50%,{SKY2});border:8px solid {GOLD};box-shadow:0 18px 36px #0C6FA866;display:flex;flex-direction:column;align-items:center;justify-content:center'>
  {T('تنخواہ', 34, '#fff', 'font-weight:700', 1.5)}<div style='font:400 74px Anton;color:#fff;line-height:1;direction:ltr'>120,000</div><div style='font:400 36px Anton;color:{GOLD};line-height:1;direction:ltr;letter-spacing:3px'>PKR</div>{T('ماہانہ', 30, '#fff', 'font-weight:700', 1.5)}</div></div>

<div class='abs' style='top:1056px;left:30px;right:30px;display:grid;grid-template-columns:1fr 1fr;gap:12px 14px'>{rows}</div>
<div class='abs' style='top:878px;left:40px;width:360px;text-align:center'>{T('اپنی ' + N('CV') + ' واٹس ایپ کریں', 30, NAVY, 'font-weight:700', 1.8)}{T('ابھی رابطہ کریں!', 40, RED, 'font-weight:700', 1.7)}</div>

<div class='abs' style='top:1226px;left:0;width:1080px;height:124px;background:linear-gradient(100deg,{NAVY},#14406E)'></div>
<div class='abs' style='top:1220px;left:0;width:1080px;height:6px;background:linear-gradient(90deg,{SKY},#fff,{GRN})'></div>
<div class='abs' style='top:1236px;left:30px;right:30px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:4px 0;direction:ltr'>{nums}</div>
<div class='abs' style='top:1314px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:10px;direction:ltr'>{icon('mail', 20, GOLD, 2)}<span style='font:800 21px Archivo;color:#fff'>{EMAIL}</span></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#F4FAFD'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Uzbekistan-Factory-Workers-v12-Urdu.png"))
