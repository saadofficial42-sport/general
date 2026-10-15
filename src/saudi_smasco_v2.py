"""SMASCO warehouse workers — variation 2 (2026-10-15): "Magazine collage" theme.
White page, royal purple + lime, staggered 3-photo collage on the left, big type on the right,
salary as oversized purple numerals with a lime highlighter stroke, purple CTA band with 3 numbers.
Facts (perk tile = accommodation only): warehouse workers · salary 1500 SAR · SMASCO · accommodation provided (food removed per user)."""
from common import PHOTOS, PHONES, flag, icon, logo_img, page, render, whatsapp_icon
from style_corporate_grid import T

PUR, PUR2, LIME, INK, GREY = "#4B2A86", "#2E1A57", "#C6F432", "#17121F", "#F4F1FA"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"


def pic(name, w, h, rot, pos="center"):
    return (f"<div style='width:{w}px;height:{h}px;border-radius:22px;overflow:hidden;border:7px solid #fff;"
            f"box-shadow:0 14px 30px rgba(46,26,87,.35);transform:rotate({rot}deg)'>"
            f"<img src='{(PHOTOS / (name + '.png')).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos};display:block'></div>")


def build():
    f = T(True)
    nums = "".join(f"<div class='num' style='display:block;font-size:40px;color:{PUR2};line-height:1.05'>{n}</div>" for n in PHONES)
    body = f"""<div class='ur-on'>
<div class='abs' style='top:0;left:0;width:1080px;height:1350px;background:#fff'></div>
<svg class='abs' style='left:0;top:0' width='1080' height='1350'>
 <circle cx='200' cy='520' r='330' fill='{GREY}'/><circle cx='980' cy='140' r='90' fill='{LIME}' opacity='.5'/>
 <g fill='{PUR}' opacity='.12'>""" + "".join(f"<circle cx='{620 + (i % 8) * 22}' cy='{900 + (i // 8) * 22}' r='4'/>" for i in range(32)) + f"""</g></svg>
<div class='abs' style='top:24px;left:30px'>{logo_img('logo-horizontal-light', 'width:430px;height:108px;object-position:left')}</div>
<div class='abs' style='top:34px;right:30px;display:flex;align-items:center;gap:16px'>
 <div style='background:{LIME};border-radius:999px;padding:0 22px 8px'>{f.head('فوری ضرورت', 0, 30, PUR2)}</div>
 <div style='filter:drop-shadow(0 4px 8px #0004)'>{flag('saudi', 120, True, 'sm2')}</div></div>

<div class='abs' style='top:176px;left:40px'>{pic('rslinks_worker_hero', 360, 400, -4, 'center top')}</div>
<div class='abs' style='top:520px;left:200px'>{pic('rslinks_team_scan', 250, 230, 5)}</div>
<div class='abs' style='top:560px;left:24px'>{pic('rslinks_worker_pack', 200, 200, -7)}</div>

<div class='abs' style='top:170px;right:40px;width:560px;text-align:right'>
 {f.txt('سعودی عرب کی معروف کمپنی', 0, 30, PUR, 'font-weight:700', 1.7)}
 <div style='display:inline-block;margin-top:6px;background:{PUR};border-radius:14px;padding:4px 24px;transform:rotate(-2deg);box-shadow:0 8px 18px rgba(46,26,87,.35)'>
  <span style='font-family:Anton;font-size:72px;letter-spacing:5px;color:#fff;line-height:1.1'>SMASCO</span></div>
 {f.txt('کو ضرورت ہے', 0, 30, INK, 'font-weight:700;margin-top:10px', 1.6)}
 {f.txt('ویئر ہاؤس ورکرز', 0, 84, PUR2, 'font-weight:700;margin-top:8px', 1.5)}
 <div style='font-family:Anton;font-size:30px;color:#8B7BAA;letter-spacing:3px;direction:ltr;margin-top:30px'>WAREHOUSE WORKERS</div></div>

<div class='abs' style='top:604px;right:40px;width:520px;text-align:right' data-check='sal'>
 {f.txt('ماہانہ تنخواہ', 0, 30, INK, 'font-weight:700', 1.6)}
 <div style='direction:ltr;display:flex;justify-content:flex-end;align-items:baseline;gap:12px;position:relative'>
  <div style='position:absolute;right:0;bottom:16px;width:420px;height:46px;background:{LIME};border-radius:10px;transform:rotate(-2deg)'></div>
  <span class='num' style='position:relative;font-size:150px;color:{PUR};line-height:1'>1500</span>
  <span class='num' style='position:relative;font-size:52px;color:{INK}'>SAR</span></div></div>

<div class='abs' style='top:848px;left:30px;right:30px;height:132px;display:flex;gap:16px' data-check='perks'>
 <div style='flex:1;background:{GREY};border-radius:24px;display:flex;align-items:center;gap:18px;padding:0 26px;border:3px solid {PUR}'>
  <div style='width:80px;height:80px;border-radius:22px;background:{PUR};display:flex;align-items:center;justify-content:center;flex:none'>{icon('home', 44, LIME, 2.2)}</div>
  <div>{f.txt('رہائش کمپنی کی طرف سے', 0, 44, PUR2, 'font-weight:700', 1.6)}</div></div>
</div>

<div class='abs' style='top:1000px;left:30px;right:30px;height:80px;border-radius:999px;background:{LIME};display:flex;align-items:center;justify-content:center;gap:14px' data-check='cv'>
 {whatsapp_icon(52)}{f.txt(f"اپنی {N('CV')} نیچے دیے گئے کسی بھی نمبر پر واٹس ایپ کریں یا ای میل کریں", 0, 25, PUR2, 'font-weight:700', 1.6)}</div>

<div class='abs' style='top:1100px;left:0;width:1080px;height:250px;background:linear-gradient(110deg,{PUR2},{PUR})'></div>
<svg class='abs' style='left:0;top:1100px' width='1080' height='250'><circle cx='1040' cy='250' r='160' fill='#ffffff10'/><path d='M0 0 H1080 V10 H0Z' fill='{LIME}'/></svg>
<div class='abs' style='top:1134px;left:30px;height:186px;background:#fff;border-radius:28px;display:flex;align-items:center;gap:16px;padding:0 30px 0 18px;direction:ltr;box-shadow:0 10px 24px #0006'>
 {whatsapp_icon(76)}<div>{nums}</div></div>
<div class='abs' style='top:1110px;height:240px;right:36px;width:440px;display:flex;flex-direction:column;justify-content:center;text-align:right'>
 {f.head('ابھی اپلائی کریں!', 0, 44, LIME, 'line-height:1.5')}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:10px;direction:ltr'>{icon('mail', 26, LIME, 2)}
  <span style='font-family:Archivo;font-size:24px;font-weight:700;color:#fff'>{EMAIL}</span></div></div>
</div>"""
    css = (".canvas{font-family:'Nastaliq',serif;background:#fff}.ur-on .t{font-family:'Nastaliq',serif}"
           ".num{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}")
    return page(body, css, rtl=True)


if __name__ == "__main__":
    from common import overflow_report
    h = build(); print(overflow_report(h)); print(render(h, "RS-Links-Saudi-Arabia-SMASCO-Warehouse-Workers-v2-Urdu.png"))
