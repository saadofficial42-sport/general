"""Saudi Arabia — Warehouse Workers for SMASCO (2026-10-14). Facts from the user: warehouse workers,
salary 1500 SAR, SMASCO company (named at user request). Real RS Links photos. Urdu only."""
from common import C, PHOTOS, WHATSAPP, flag, icon, logo_img, page, render, whatsapp_icon
from style_corporate_grid import T

GREEN, DEEP, GOLD, RED, NAVY = "#006C35", "#00401F", "#FFD23F", "#E53935", "#10212E"
PHONES = ["+92 317 0363690", WHATSAPP]
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"


def ph(name, w, h, r=24, b=6, pos="center"):
    return (f"<div style='width:{w}px;height:{h}px;border-radius:{r}px;overflow:hidden;border:{b}px solid #fff;box-shadow:0 12px 28px #0006;flex:none'>"
            f"<img src='{(PHOTOS / (name + '.png')).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos};display:block'></div>")


def build():
    f = T(True)
    nums = "".join(f"<div class='num' style='display:block;font-size:46px;color:{NAVY};line-height:1.06'>{n}</div>" for n in PHONES)
    body = f"""<div class='ur-on'>
<div class='abs' style='top:0;left:0;width:1080px;height:140px;background:#fff'></div>
<div class='abs' style='top:10px;right:26px;width:480px;height:120px'>{logo_img('logo-horizontal-light', 'width:480px;height:120px;object-position:right')}</div>
<div class='abs' style='top:20px;left:30px;display:flex;align-items:center;gap:18px'>
 <div style='filter:drop-shadow(0 4px 8px #0004)'>{flag('saudi', 140, True, 'hfsm')}</div>
 <div style='background:{RED};border-radius:12px;padding:0 18px 8px;box-shadow:0 4px 10px #0003'>{f.head('فوری ضرورت', 0, 30, '#fff')}</div></div>
<div class='abs' style='top:140px;left:0;width:1080px;height:6px;background:{GOLD}'></div>

<div class='abs' style='top:146px;left:0;width:1080px;height:560px;background:linear-gradient(135deg,{GREEN},{DEEP})'></div>
<svg class='abs' style='left:0;top:146px' width='1080' height='560'><circle cx='980' cy='560' r='260' fill='#ffffff0d'/><circle cx='120' cy='0' r='200' fill='#ffffff0a'/>
 <path d='M0 560 L1080 470 L1080 560Z' fill='#EEF4F0'/></svg>
<div class='abs' style='top:176px;left:40px'>{ph('rslinks_worker_hero', 420, 470, 28, 7, 'center top')}</div>
<div class='abs' style='top:186px;right:40px;width:560px;text-align:right'>
 {f.txt('سعودی عرب کی معروف کمپنی', 0, 30, GOLD, 'font-weight:700', 1.7)}
 <div style='display:inline-block;margin-top:8px;background:#fff;border-radius:16px;padding:6px 26px;box-shadow:0 6px 16px #0005'>
  <span style='font-family:Anton;font-size:64px;letter-spacing:4px;color:{GREEN};line-height:1.1'>SMASCO</span></div>
 {f.txt('کے لیے', 0, 30, '#fff', 'font-weight:700;margin-top:6px', 1.6)}
 {f.txt('ویئر ہاؤس ورکرز', 0, 76, '#fff', 'font-weight:700;margin-top:6px', 1.55)}
 <div style='font-family:Anton;font-size:34px;color:#CFE8D9;letter-spacing:2px;direction:ltr;text-align:right;margin-top:22px'>WAREHOUSE WORKERS</div></div>

<div class='abs' style='top:720px;left:30px;right:30px;height:290px;display:flex;gap:20px;align-items:center;direction:ltr' data-check='mid'>
 {ph('rslinks_team_scan', 290, 280, 22, 5)}
 <div style='flex:1;height:280px;border-radius:24px;background:#fff;border:6px solid {GOLD};box-shadow:0 10px 24px rgba(0,64,31,.22);display:flex;flex-direction:column;align-items:center;justify-content:center;direction:rtl'>
  <div style='display:flex;align-items:center;gap:10px'><div style='width:54px;height:54px;border-radius:50%;background:{GREEN};display:flex;align-items:center;justify-content:center'>{icon('money', 30)}</div>
   {f.txt('ماہانہ تنخواہ', 0, 30, NAVY, 'font-weight:700', 1.6)}</div>
  <div style='direction:ltr;display:flex;align-items:baseline;gap:10px;margin-top:6px'><span class='num' style='font-size:110px;color:{GREEN};line-height:1'>1500</span>
   <span class='num' style='font-size:44px;color:{NAVY}'>SAR</span></div></div>
 {ph('rslinks_worker_pack', 290, 280, 22, 5)}
</div>

<div class='abs' style='top:1030px;left:30px;right:30px;height:150px;border-radius:24px;background:{NAVY};display:flex;align-items:center;gap:22px;padding:0 30px;box-shadow:0 8px 22px #0003' data-check='cv'>
 <div style='flex:none'>{whatsapp_icon(86)}</div>
 <div>{f.txt(f"خواہشمند حضرات اپنی {N('CV')} نیچے دیے گئے نمبرز پر واٹس ایپ کریں", 0, 30, '#fff', 'font-weight:700', 1.7)}
  {f.txt('مزید تفصیلات کے لیے ابھی رابطہ کریں', 0, 24, GOLD, 'font-weight:700', 1.7)}</div></div>

<div class='abs' style='top:1196px;left:0;width:1080px;height:154px;background:linear-gradient(100deg,{DEEP},{GREEN});border-top:6px solid {GOLD}'></div>
<div class='abs' style='top:1196px;height:154px;right:30px;width:500px;display:flex;flex-direction:column;justify-content:center;text-align:right'>
 {f.head('ابھی اپلائی کریں!', 0, 36, GOLD, 'line-height:1.5')}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:6px;direction:ltr'>{icon('mail', 24, GOLD, 2)}
  <span style='font-family:Archivo;font-size:23px;font-weight:700;color:#fff'>{EMAIL}</span></div></div>
<div class='abs' style='top:1214px;left:30px;height:118px;background:#fff;border-radius:24px;display:flex;align-items:center;gap:14px;padding:0 26px 0 14px;box-shadow:0 6px 16px #0006;direction:ltr'>
 {whatsapp_icon(68)}<div>{nums}</div></div>
</div>"""
    css = (".canvas{font-family:'Nastaliq',serif;background:#EEF4F0}.ur-on .t{font-family:'Nastaliq',serif}"
           ".num{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}")
    return page(body, css, rtl=True)


if __name__ == "__main__":
    print(render(build(), "RS-Links-Saudi-Arabia-SMASCO-Warehouse-Workers-Urdu.png"))
