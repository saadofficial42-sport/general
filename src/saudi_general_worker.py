"""Saudi Arabia — General Worker (gardening or loading / unloading) (2026-10-15).
Source: another agency's ad (demands/2026-10-15-saudi-general-worker/ref.jpg) — content only.
Facts: salary 1000 + 200 SR · duty 8 hours/day · selection: self-selecting (no interview) · age up to 35 ·
contract 2 years · basic English required · other benefits per Saudi labour law · accommodation and other
facilities provided. Real RS Links photos. Urdu only. CV via WhatsApp (all three numbers) or email."""
from common import PHOTOS, PHONES, flag, icon, logo_img, page, render, whatsapp_icon
from style_corporate_grid import T

GREEN, DEEP, GOLD, RED, NAVY = "#006C35", "#00401F", "#FFD23F", "#E53935", "#10212E"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"


def ph(name, w, h, r=24, b=6, pos="center"):
    return (f"<div style='width:{w}px;height:{h}px;border-radius:{r}px;overflow:hidden;border:{b}px solid #fff;box-shadow:0 12px 28px #0006;flex:none'>"
            f"<img src='{(PHOTOS / (name + '.png')).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos};display:block'></div>")


def build():
    f = T(True)
    tiles = [("clock", "ڈیوٹی", f"{N(8)} گھنٹے روزانہ"), ("check", "سلیکشن", "بغیر انٹرویو"),
             ("user", "عمر", f"{N(35)} سال تک"), ("calendar", "معاہدہ", f"{N(2)} سال"), ("chat", "زبان", "بنیادی انگریزی")]
    tile_html = "".join(
        f"<div style='flex:1;background:#fff;border-radius:18px;box-shadow:0 5px 14px rgba(0,64,31,.15);display:flex;flex-direction:column;align-items:center;justify-content:center;border-bottom:6px solid {GOLD};padding-bottom:4px'>"
        f"<div style='width:50px;height:50px;border-radius:50%;background:{GREEN};display:flex;align-items:center;justify-content:center'>{icon(ic, 27)}</div>"
        f"{f.txt(lab, 0, 18, '#5A6B75', 'margin-top:6px;margin-bottom:12px', 1.6)}{f.txt(val, 0, 23, NAVY, 'font-weight:800;text-align:center', 1.6)}</div>"
        for ic, lab, val in tiles)
    nums = "".join(f"<div class='num' style='display:block;font-size:37px;color:{NAVY};line-height:1.06'>{n}</div>" for n in PHONES)
    body = f"""<div class='ur-on'>
<div class='abs' style='top:0;left:0;width:1080px;height:140px;background:#fff'></div>
<div class='abs' style='top:10px;right:26px;width:480px;height:120px'>{logo_img('logo-horizontal-light', 'width:480px;height:120px;object-position:right')}</div>
<div class='abs' style='top:20px;left:30px;display:flex;align-items:center;gap:18px'>
 <div style='filter:drop-shadow(0 4px 8px #0004)'>{flag('saudi', 140, True, 'hfgw')}</div>
 <div style='background:{RED};border-radius:12px;padding:0 18px 8px;box-shadow:0 4px 10px #0003'>{f.head('فوری ضرورت', 0, 30, '#fff')}</div></div>
<div class='abs' style='top:140px;left:0;width:1080px;height:6px;background:{GOLD}'></div>

<div class='abs' style='top:146px;left:0;width:1080px;height:500px;background:linear-gradient(135deg,{GREEN},{DEEP})'></div>
<svg class='abs' style='left:0;top:146px' width='1080' height='500'><circle cx='980' cy='500' r='240' fill='#ffffff0d'/><circle cx='120' cy='0' r='200' fill='#ffffff0a'/>
 <path d='M0 500 L1080 420 L1080 500Z' fill='#EEF4F0'/></svg>
<div class='abs' style='top:172px;left:40px'>{ph('rslinks_team_scan', 420, 420, 28, 7)}</div>
<div class='abs' style='top:170px;right:40px;width:560px;text-align:right'>
 {f.txt('فوری ضرورت برائے سعودی عرب', 0, 30, GOLD, 'font-weight:700', 1.7)}<div style='height:22px'></div>
 {f.txt('جنرل ورکر', 0, 92, '#fff', 'font-weight:700;margin-top:0', 1.45)}
 <div style='font-family:Anton;font-size:34px;color:#CFE8D9;letter-spacing:2px;direction:ltr;text-align:right;margin-top:24px'>GENERAL WORKER</div>
 <div style='display:inline-block;margin-top:14px;background:#fff;border-radius:16px;padding:0 20px 8px;box-shadow:0 6px 16px #0005'>
  {f.txt('گارڈننگ یا لوڈنگ / اَن لوڈنگ', 0, 30, GREEN, 'font-weight:700', 1.7)}</div></div>

<div class='abs' style='top:660px;left:30px;right:30px;height:250px;display:flex;gap:20px;align-items:center;direction:ltr' data-check='mid'>
 {ph('rslinks_worker_hero', 260, 244, 22, 5, 'center top')}
 <div style='flex:1;height:244px;border-radius:24px;background:#fff;border:6px solid {GOLD};box-shadow:0 10px 24px rgba(0,64,31,.22);display:flex;flex-direction:column;align-items:center;justify-content:center;direction:rtl'>
  <div style='display:flex;align-items:center;gap:10px'><div style='width:50px;height:50px;border-radius:50%;background:{GREEN};display:flex;align-items:center;justify-content:center'>{icon('money', 28)}</div>
   {f.txt('تنخواہ', 0, 30, NAVY, 'font-weight:700', 1.6)}</div>
  <div style='direction:ltr;display:flex;align-items:baseline;gap:10px;margin-top:4px'><span class='num' style='font-size:76px;color:{GREEN};line-height:1;white-space:nowrap'>1000 + 200</span>
   <span class='num' style='font-size:34px;color:{NAVY}'>SAR</span></div></div>
 {ph('rslinks_worker_pack', 260, 244, 22, 5)}
</div>

<div class='abs' style='top:920px;left:30px;right:30px;height:138px;display:flex;gap:12px' data-check='tiles'>{tile_html}</div>

<div class='abs' style='top:1064px;left:30px;right:30px;height:62px;border-radius:16px;background:{GREEN};display:flex;align-items:center;justify-content:space-around;padding:0 18px' data-check='fac'>
 <div style='display:flex;align-items:center;gap:10px'>{icon('home', 30, GOLD, 2.3)}{f.txt('رہائش اور دیگر سہولیات کمپنی کی طرف سے', 0, 23, '#fff', 'font-weight:700', 1.6)}</div>
 <div style='display:flex;align-items:center;gap:10px'>{icon('doc', 28, GOLD, 2.3)}{f.txt('دیگر مراعات سعودی لیبر لاء کے مطابق', 0, 23, '#fff', 'font-weight:700', 1.6)}</div></div>

<div class='abs' style='top:1138px;left:30px;right:30px;height:56px;border-radius:16px;background:{NAVY};display:flex;align-items:center;justify-content:center;gap:12px' data-check='cv'>
 {whatsapp_icon(40)}{f.txt(f"اپنی {N('CV')} نیچے دیے گئے کسی بھی نمبر پر واٹس ایپ کریں یا ای میل کریں", 0, 23, '#fff', 'font-weight:700', 1.6)}</div>

<div class='abs' style='top:1206px;left:0;width:1080px;height:144px;background:linear-gradient(100deg,{DEEP},{GREEN});border-top:6px solid {GOLD}'></div>
<div class='abs' style='top:1206px;height:144px;right:30px;width:500px;display:flex;flex-direction:column;justify-content:center;text-align:right'>
 {f.head('ابھی اپلائی کریں!', 0, 34, GOLD, 'line-height:1.5')}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:6px;direction:ltr'>{icon('mail', 26, GOLD, 2)}
  <span style='font-family:Archivo;font-size:25px;font-weight:700;color:#fff'>{EMAIL}</span></div></div>
<div class='abs' style='top:1216px;left:30px;height:124px;background:#fff;border-radius:24px;display:flex;align-items:center;gap:14px;padding:0 26px 0 14px;box-shadow:0 6px 16px #0006;direction:ltr'>
 {whatsapp_icon(68)}<div>{nums}</div></div>
</div>"""
    css = (".canvas{font-family:'Nastaliq',serif;background:#EEF4F0}.ur-on .t{font-family:'Nastaliq',serif}"
           ".num{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}")
    return page(body, css, rtl=True)


if __name__ == "__main__":
    from common import overflow_report
    h = build(); print(overflow_report(h)); print(render(h, "RS-Links-Saudi-Arabia-General-Worker-Urdu.png"))
