"""Saudi Arabia drivers ad (2026-10-14) — redesign of the user's RS Links ad
(demands/2026-10-14-saudi-drivers/ref.jpg). Trucks photo kept with the noon / Luna branding removed
(assets/photos/rslinks_drivers_trucks.png). Urdu only.
Facts used: Saudi Arabia drivers · total package 2000 riyal monthly + transport · only Gulf / Saudi HTV or LTV
licence accepted · duty 9 hours, 6 days a week · visa, medical, transport by company.
Not used (unclear in source): "1800 + 2000" salary line, "daily 120 Pakistani ..." line."""
from common import C, PHOTOS, WHATSAPP, flag, icon, logo_img, page, render, whatsapp_icon
from style_corporate_grid import T

NAVY, NAVY2, YEL, RED = "#0D2D63", "#12285A", "#FFD23F", "#E53935"
PHONES = ["+92 317 0363690", WHATSAPP]
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"


def build():
    f = T(True)
    photo = (PHOTOS / "rslinks_drivers_trucks.png").as_uri()
    badges = "".join(
        f"<div style='display:flex;align-items:center;gap:8px;background:{YEL};border-radius:999px;padding:0 18px 6px'>"
        f"{icon(ic, 24, NAVY, 2.6)}{f.txt(s, 0, 22, NAVY, 'font-weight:700', 1.6)}</div>"
        for ic, s in (("money", "بہترین تنخواہ"), ("visa", "ویزا کمپنی کی طرف سے"), ("calendar", "فوری بھرتی")))
    facts = "".join(
        f"<div style='flex:1;background:#fff;border-radius:18px;box-shadow:0 5px 14px rgba(13,45,99,.14);display:flex;align-items:center;gap:12px;"
        f"padding:4px 16px 8px;border-bottom:6px solid {YEL}'>"
        f"<div style='width:56px;height:56px;border-radius:50%;background:{NAVY};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 30, YEL, 2.2)}</div>"
        f"<div>{f.txt(lab, 0, 20, '#5A6B85', 'margin-bottom:16px', 1.6)}{f.txt(val, 0, 27, NAVY, 'font-weight:800', 1.55)}</div></div>"
        for ic, lab, val in (("clock", "ڈیوٹی", f"{N(9)} گھنٹے"), ("calendar", "ہفتے میں", f"{N(6)} دن"),
                             ("doc", "ویزا", "کمپنی کی طرف سے")))
    perks = "".join(
        f"<div style='display:flex;align-items:center;gap:10px'><div style='width:46px;height:46px;border-radius:50%;background:{YEL};display:flex;align-items:center;justify-content:center'>{icon(ic, 26, NAVY, 2.3)}</div>"
        f"{f.txt(s, 0, 24, '#fff', 'font-weight:700', 1.6)}</div>"
        for ic, s in (("visa", "ویزا"), ("medical", "میڈیکل"), ("bus", "ٹرانسپورٹ")))
    nums = "".join(f"<div class='num' style='display:block;font-size:46px;color:{NAVY};line-height:1.06'>{n}</div>" for n in PHONES)
    body = f"""
<div class='ur-on'>
<div class='abs' style='top:0;left:0;width:1080px;height:140px;background:#fff'></div>
<div class='abs' style='top:10px;right:26px;width:480px;height:120px'>{logo_img('logo-horizontal-light', 'width:480px;height:120px;object-position:right')}</div>
<div class='abs' style='top:20px;left:30px;display:flex;align-items:center;gap:18px'>
 <div style='filter:drop-shadow(0 4px 8px #0004)'>{flag('saudi', 140, True, 'hfsd')}</div>
 <div style='background:{RED};border-radius:12px;padding:0 18px 8px;box-shadow:0 4px 10px #0003'>{f.head('فوری ضرورت', 0, 30, '#fff')}</div></div>

<div class='abs' style='top:140px;left:0;width:1080px;height:200px;background:linear-gradient(100deg,{NAVY2},{NAVY})'></div>
<div class='abs' style='top:132px;right:36px;text-align:right'>
 {f.txt('سعودی عرب میں', 0, 32, '#fff', 'font-weight:700', 1.6)}
 {f.txt(f"ڈرائیورز <span style='color:{YEL}'>کی ضرورت</span>", 0, 66, '#fff', 'font-weight:700;margin-top:18px', 1.4)}</div>
<div class='abs' style='top:176px;left:30px;display:flex;flex-direction:column;align-items:flex-start;gap:10px'>{badges}</div>

<div class='abs' style='top:340px;left:0;width:1080px;height:420px;overflow:hidden'>
 <img src='{photo}' style='width:1080px;height:422px;object-fit:cover;display:block'></div>
<div class='abs' style='top:340px;left:0;width:1080px;height:6px;background:{YEL}'></div>

<div class='abs' style='top:744px;left:30px;right:30px;height:236px;background:#fff;border-radius:24px;box-shadow:0 10px 26px rgba(13,45,99,.22);overflow:hidden;display:flex' data-check='job'>
 <div style='width:380px;background:linear-gradient(160deg,{RED},#B71C1C);display:flex;flex-direction:column;align-items:center;justify-content:center;flex:none'>
  {icon('truck', 64, '#fff', 2)}
  <div class='num' style='font-size:58px;color:#fff;line-height:1.1;margin-top:6px'>HTV / LTV</div>
  {f.txt('ڈرائیورز', 0, 44, YEL, 'font-weight:700', 1.5)}</div>
 <div style='flex:1;padding:0 22px;display:flex;flex-direction:column;justify-content:center'>
  {f.txt('کل پیکج (ماہانہ)', 0, 24, '#5A6B85', 'font-weight:700', 1.6)}
  <div style='display:flex;align-items:center;gap:14px;direction:rtl'>
   <div style='direction:ltr;display:flex;align-items:baseline;gap:10px'><span class='num' style='font-size:80px;color:{NAVY};line-height:1'>2000</span>
    <span class='num' style='font-size:38px;color:{C['green']}'>SAR</span></div>
   <div style='background:#E9F6EE;border-radius:14px;padding:0 14px 6px;display:flex;align-items:center;gap:6px'>{icon('bus', 28, C['green'], 2.3)}{f.txt('+ ٹرانسپورٹ', 0, 26, C['green'], 'font-weight:800', 1.6)}</div></div>
  <div style='margin-top:6px;background:#FFF6DA;border:3px solid {YEL};border-radius:14px;padding:0 14px 6px'>
   {f.txt(f"صرف گلف / سعودی {N('HTV')} یا {N('LTV')} لائسنس قابلِ قبول ہے", 0, 20, NAVY, 'font-weight:800', 1.75)}</div></div></div>

<div class='abs' style='top:1000px;left:30px;right:30px;height:104px;display:flex;gap:14px' data-check='facts'>{facts}</div>

<div class='abs' style='top:1120px;left:30px;right:30px;height:66px;border-radius:16px;background:{C['green']};display:flex;align-items:center;justify-content:space-around;padding:0 16px'>
 {f.txt('کمپنی کی طرف سے:', 0, 24, YEL, 'font-weight:800', 1.6)}{perks}</div>

<div class='abs' style='top:1202px;left:0;width:1080px;height:148px;background:linear-gradient(100deg,{NAVY2},{NAVY});border-top:6px solid {YEL}'></div>
<div class='abs' style='top:1202px;height:148px;right:30px;width:500px;display:flex;flex-direction:column;justify-content:center;text-align:right'>
 {f.head('آج ہی رابطہ کریں!', 0, 34, YEL, 'line-height:1.5')}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:6px;direction:ltr'>{icon('mail', 24, YEL, 2)}
  <span style='font-family:Archivo;font-size:23px;font-weight:700;color:#fff'>{EMAIL}</span></div></div>
<div class='abs' style='top:1218px;left:30px;height:118px;background:#fff;border-radius:24px;display:flex;align-items:center;gap:14px;padding:0 26px 0 14px;box-shadow:0 6px 16px #0006;direction:ltr'>
 {whatsapp_icon(68)}<div>{nums}</div></div>
</div>"""
    css = (".canvas{font-family:'Nastaliq',serif;background:#EEF2F8}.ur-on .t{font-family:'Nastaliq',serif}"
           ".num{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}")
    return page(body, css, rtl=True)


if __name__ == "__main__":
    print(render(build(), "RS-Links-Saudi-Arabia-Drivers-Urdu.png"))
