"""Saudi General Worker — variation 2 (2026-10-15): "Sunset poster" theme.
Charcoal + sunset orange + cream. Full-bleed photo top with angled orange cut, huge circular salary
seal overlapping the cut, ticket-stub fact strip, cream facilities list, orange CTA with 3 numbers."""
from common import PHOTOS, PHONES, flag, icon, logo_img, page, render, whatsapp_icon
from style_corporate_grid import T

CH, OR, OR2, CREAM, INK = "#1B1B1F", "#F26B1D", "#FF9F43", "#FFF4E6", "#141414"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"


def build():
    f = T(True)
    hero = (PHOTOS / "rslinks_worker_hero.png").as_uri()
    stubs = [("clock", f"{N(8)} گھنٹے", "ڈیوٹی روزانہ"), ("check", "بغیر انٹرویو", "سلیکشن"),
             ("user", f"{N(35)} سال تک", "عمر"), ("calendar", f"{N(2)} سال", "معاہدہ"), ("chat", "بنیادی انگریزی", "ضروری")]
    stub = "".join(
        f"<div style='flex:1;position:relative;background:{CH};display:flex;flex-direction:column;align-items:center;justify-content:center;"
        f"border-inline-start:{'0' if i == 0 else '3px dashed #ffffff40'}'>"
        f"{icon(ic, 34, OR2, 2.2)}{f.txt(v, 0, 25, '#fff', 'font-weight:700;margin-top:2px;text-align:center', 1.6)}"
        f"{f.txt(l, 0, 17, '#C9C3BC', 'margin-top:8px', 1.5)}</div>" for i, (ic, v, l) in enumerate(stubs))
    nums = "".join(f"<div class='num' style='display:block;font-size:40px;color:{INK};line-height:1.05'>{n}</div>" for n in PHONES)
    body = f"""<div class='ur-on'>
<div class='abs' style='top:0;left:0;width:1080px;height:620px;overflow:hidden'>
 <img src='{hero}' style='width:1080px;height:620px;object-fit:cover;object-position:center 20%;display:block;filter:saturate(1.1)'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:620px;background:linear-gradient(180deg,#000a 0,#0000 30%,#0000 55%,#000c 100%)'></div>
<svg class='abs' style='left:0;top:470px' width='1080' height='160'><path d='M0 160 L0 90 L1080 0 L1080 160Z' fill='{OR}'/><path d='M0 160 L0 120 L1080 30 L1080 160Z' fill='{CREAM}'/></svg>
<div class='abs' style='top:22px;right:26px;background:#fff;border-radius:18px;padding:6px 16px;box-shadow:0 6px 16px #0006'>{logo_img('logo-horizontal-light', 'width:400px;height:100px')}</div>
<div class='abs' style='top:30px;left:30px;filter:drop-shadow(0 4px 8px #0008)'>{flag('saudi', 130, True, 'gw2')}</div>
<div class='abs' style='top:180px;right:40px;text-align:right'>
 <div style='display:inline-block;background:{OR};padding:0 18px 8px;border-radius:10px'>{f.txt('فوری ضرورت برائے سعودی عرب', 0, 28, '#fff', 'font-weight:700', 1.6)}</div>
 {f.txt('جنرل ورکر', 0, 104, '#fff', 'font-weight:700;margin-top:34px;text-shadow:0 4px 14px #000c', 1.4)}
 </div>
<div class='abs' style='top:640px;right:30px;width:680px;display:flex;gap:14px' data-check='jobs'>
 <div style='flex:1;background:{CH};border-radius:20px;height:110px;display:flex;align-items:center;justify-content:center;gap:12px;box-shadow:0 8px 18px #0004'>
  <div style='width:62px;height:62px;border-radius:50%;background:{OR};display:flex;align-items:center;justify-content:center'>{icon('leaf', 34, '#fff', 2.2)}</div>
  {f.txt('گارڈننگ', 0, 36, '#fff', 'font-weight:700', 1.6)}</div>
 <div style='font-size:30px;font-weight:900;color:{OR};align-self:center;font-family:Archivo'>یا</div>
 <div style='flex:1.3;background:{CH};border-radius:20px;height:110px;display:flex;align-items:center;justify-content:center;gap:12px;box-shadow:0 8px 18px #0004'>
  <div style='width:62px;height:62px;border-radius:50%;background:{OR};display:flex;align-items:center;justify-content:center'>{icon('dolly', 34, '#fff', 2.2)}</div>
  {f.txt('لوڈنگ / اَن لوڈنگ', 0, 36, '#fff', 'font-weight:700', 1.6)}</div></div>

<div class='abs' style='top:470px;left:46px;width:280px;height:280px;border-radius:50%;background:radial-gradient(circle at 35% 30%,{OR2},{OR} 65%,#C94D0C);
 border:8px solid {CREAM};box-shadow:0 14px 30px #0007;display:flex;flex-direction:column;align-items:center;justify-content:center'>
 {f.txt('تنخواہ', 0, 28, '#fff', 'font-weight:700', 1.4)}
 <div class='num' style='font-size:66px;color:#fff;line-height:1'>1000</div>
 <div class='num' style='font-size:44px;color:{INK};line-height:1'>+ 200</div>
 <div class='num' style='font-size:28px;color:#fff;margin-top:4px'>SAR</div></div>

<div class='abs' style='top:0;left:0;width:1080px;height:1350px;background:{CREAM};z-index:-1'></div>
<div class='abs' style='top:772px;left:30px;right:30px;height:150px;border-radius:22px;overflow:hidden;display:flex;box-shadow:0 10px 24px #0003' data-check='stub'>{stub}</div>

<div class='abs' style='top:944px;left:30px;right:30px;height:176px;display:flex;gap:16px;direction:ltr' data-check='fac'>
 <div style='width:300px;height:176px;border-radius:20px;overflow:hidden;box-shadow:0 8px 20px #0004'><img src='{(PHOTOS / "rslinks_worker_pack.png").as_uri()}' style='width:100%;height:100%;object-fit:cover'></div>
 <div style='flex:1;background:#fff;border-radius:20px;border:3px solid {OR};padding:0 22px;direction:rtl;display:flex;flex-direction:column;justify-content:center;box-shadow:0 8px 20px #0002'>
  <div style='display:flex;align-items:center;gap:10px'>{icon('home', 30, OR, 2.4)}{f.txt('رہائش اور دیگر سہولیات کمپنی کی طرف سے', 0, 23, INK, 'font-weight:700', 1.85)}</div>
  <div style='display:flex;align-items:center;gap:10px'>{icon('doc', 28, OR, 2.4)}{f.txt('دیگر مراعات سعودی لیبر لاء کے مطابق', 0, 23, INK, 'font-weight:700', 1.85)}</div>
  <div style='display:flex;align-items:center;gap:10px'>{icon('mail', 28, OR, 2.4)}{f.txt(f"اپنی {N('CV')} واٹس ایپ یا ای میل کریں", 0, 23, INK, 'font-weight:700', 1.85)}</div></div></div>

<div class='abs' style='top:1140px;left:0;width:1080px;height:210px;background:{CH}'></div>
<div class='abs' style='top:1140px;left:0;width:1080px;height:10px;background:repeating-linear-gradient(90deg,{OR} 0 40px,{CH} 40px 60px)'></div>
<div class='abs' style='top:1166px;left:30px;height:166px;background:{OR};border-radius:24px;display:flex;align-items:center;gap:14px;padding:0 26px 0 16px;direction:ltr;box-shadow:0 8px 20px #0007'>
 <div style='background:#fff;border-radius:50%;padding:6px;line-height:0'>{whatsapp_icon(66)}</div>
 <div style='background:#fff;border-radius:16px;padding:4px 16px'>{nums}</div></div>
<div class='abs' style='top:1150px;height:200px;right:34px;width:470px;display:flex;flex-direction:column;justify-content:center;text-align:right'>
 {f.head('ابھی اپلائی کریں!', 0, 40, OR2, 'line-height:1.5')}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px;direction:ltr'>{icon('mail', 26, OR2, 2)}
  <span style='font-family:Archivo;font-size:25px;font-weight:700;color:#fff'>{EMAIL}</span></div></div>
</div>"""
    css = (".canvas{font-family:'Nastaliq',serif;background:#FFF4E6}.ur-on .t{font-family:'Nastaliq',serif}"
           ".num{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}")
    return page(body, css, rtl=True)


if __name__ == "__main__":
    from common import overflow_report
    h = build(); print(overflow_report(h)); print(render(h, "RS-Links-Saudi-Arabia-General-Worker-v2-Urdu.png"))
