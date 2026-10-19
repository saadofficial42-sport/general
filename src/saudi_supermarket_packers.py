"""Saudi Arabia — Super Store Workers (Packers), Urdu (2026-10-19). Facts: demands/2026-10-19-saudi-supermarket-packers/facts.md.
Design: "split column + receipt" — charcoal header, left column of stacked real RS Links photos, cream right column with a
supermarket-receipt salary ticket, orange/Saudi-green palette, full-width fact strip, charcoal CTA with all three numbers.
Interview date / delegation and "urgent visa / departure" dropped (see facts.md)."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

ORG, ORG2, GRN, CREAM, CHAR, INK = "#F57C00", "#FFB300", "#0B7A43", "#FFF5E6", "#1E2226", "#22262B"
EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.75: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"
img = lambda k, pos="center": f"<img src='{(PHOTOS / (k + '.png')).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos};display:block'>"


def build():
    zig = "".join(f"L{x + 10} 0 L{x + 20} 10 " for x in range(0, 540, 20))
    duties = [("dolly", "گروسری اسٹور میں آنے والا سامان اتار کر ریکس میں لگانا"),
              ("box", "پارسلز کسٹمر کا نام اور آرڈر نمبر دیکھ کر پیک کرنا")]
    duty_li = "".join(f"<div style='display:flex;align-items:center;gap:12px;margin-top:14px'>"
                      f"<span style='width:46px;height:46px;border-radius:12px;background:{GRN};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 26, '#fff', 2.2)}</span>"
                      f"{T(s, 22, INK, 'font-weight:700', 1.75)}</div>" for ic, s in duties)
    facts = [("clock", f"{N('09')} گھنٹے", "ڈیوٹی"), ("calendar", f"{N(2)} سال", "معاہدہ"), ("user", f"{N('21 – 30')} سال", "عمر"),
             ("chat", "بیسک انگلش", "بول چال لازمی")]
    fact_tiles = "".join(f"<div style='flex:1;background:#fff;border-radius:18px;border-top:6px solid {ORG};box-shadow:0 6px 14px rgba(0,0,0,.12);display:flex;flex-direction:column;align-items:center;padding-bottom:6px'>"
                         f"<div style='margin-top:12px;width:50px;height:50px;border-radius:50%;background:{ORG}1f;display:flex;align-items:center;justify-content:center'>{icon(ic, 28, ORG, 2.3)}</div>"
                         f"{T(v, 27, INK, 'font-weight:700;margin-top:2px', 1.6)}{T(l, 18, '#5B6168', 'font-weight:700;margin-top:-6px', 1.6)}</div>" for ic, v, l in facts)
    perks = [("home", "رہائش"), ("medical", "میڈیکل"), ("bus", "ٹرانسپورٹ")]
    perk_li = "".join(f"<div style='display:flex;align-items:center;gap:8px;background:#ffffff22;border-radius:999px;padding:0 16px 4px 10px'>{icon(ic, 26, ORG2, 2.3)}{T(s, 24, '#fff', 'font-weight:700', 1.6)}</div>" for ic, s in perks)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:10px'><span style='line-height:0'>{whatsapp_icon(34)}</span><span class='num' style='font-size:34px;color:{INK};line-height:1.15'>{n}</span></div>" for n in PHONES)
    body = f"""<div class='ur-on' dir='rtl'>
<div class='abs' style='top:0;left:0;width:1080px;height:150px;background:{CHAR}'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:8px;background:linear-gradient(90deg,{GRN},{ORG})'></div>
<div class='abs' style='top:22px;right:26px;background:#fff;border-radius:18px;padding:4px 16px'>{logo_img('logo-horizontal-light', 'width:380px;height:96px;object-position:right')}</div>
<div class='abs' style='top:20px;left:26px;display:flex;align-items:center;gap:18px;direction:ltr'>
 <div style='filter:drop-shadow(0 4px 8px #0008)'>{flag('saudi', 150, True, 'sa9')}</div>
 <div style='background:{ORG};border-radius:14px;padding:0 20px 8px;box-shadow:0 6px 14px #0006;display:flex;align-items:center;gap:8px'>{icon('megaphone', 30, '#fff', 2.2)}{T('فوری ضرورت', 34, '#fff', 'font-weight:700', 1.6)}</div></div>

<div class='abs' style='top:150px;left:0;width:420px;height:760px;background:{CHAR}'></div>
<div class='abs' style='top:170px;left:20px;width:380px;height:440px;border-radius:24px;overflow:hidden;border:5px solid {ORG}'>{img('rslinks_worker_hero', 'center 20%')}</div>
<div class='abs' style='top:626px;left:20px;width:182px;height:182px;border-radius:20px;overflow:hidden;border:4px solid #fff'>{img('rslinks_team_scan')}</div>
<div class='abs' style='top:626px;left:218px;width:182px;height:182px;border-radius:20px;overflow:hidden;border:4px solid #fff'>{img('rslinks_worker_pack')}</div>
<div class='abs' style='top:822px;left:20px;width:380px;height:72px;border-radius:18px;background:{GRN};display:flex;align-items:center;justify-content:center;gap:12px'>
 <span class='num' style='font-size:50px;color:#fff;line-height:1'>200</span>{T('آسامیاں', 30, '#fff', 'font-weight:700', 1.5)}</div>

<div class='abs' style='top:150px;left:420px;width:660px;height:760px;background:{CREAM}'></div>
<div class='abs' style='top:160px;right:36px;width:600px;text-align:right'>
 {T('فوری ضرورت برائے', 30, ORG, 'font-weight:700', 1.7)}
 {T('سعودی عرب', 86, GRN, 'font-weight:700;margin-top:-10px;margin-bottom:30px', 1.5)}
 {T('سعودی عرب کی مشہور سپر مارکیٹ کے لیے', 25, INK, 'font-weight:700;margin-top:4px', 1.7)}
 <div style='margin-top:16px;background:{GRN};border-radius:18px;padding:2px 22px 12px;box-shadow:0 8px 16px rgba(11,122,67,.3)'>
  {T('سپر اسٹور ورکرز (پیکرز)', 46, '#fff', 'font-weight:700', 1.65)}<div style='height:14px'></div>
  <div style='font-family:Anton;font-size:30px;color:{ORG2};letter-spacing:1px;direction:ltr;text-align:right;line-height:1.1'>SUPER STORE WORKERS (PACKERS)</div></div></div>
<div class='abs' style='top:612px;right:36px;width:600px;filter:drop-shadow(0 8px 12px rgba(0,0,0,.18))'>
 <svg width='600' height='10' style='display:block'><path d='M0 10 {zig} L600 10Z' fill='#fff'/></svg>
 <div style='background:#fff;padding:0 24px 10px;display:flex;align-items:center;justify-content:space-between'>
  <div>{T('تنخواہ', 30, INK, 'font-weight:700', 1.6)}{T('سعودی ریال', 19, '#6B7178', 'font-weight:700;margin-top:-6px', 1.6)}</div>
  <div style='direction:ltr;display:flex;align-items:baseline;gap:8px'><span class='num' style='font-size:84px;color:{ORG};line-height:1'>1300</span><span class='num' style='font-size:32px;color:{INK}'>SAR</span></div></div>
 <div style='background:#fff;border-top:2px dashed #D8CFC0;padding:2px 24px 16px'>{duty_li}</div>
 <svg width='600' height='10' style='display:block;transform:scaleY(-1)'><path d='M0 10 {zig} L600 10Z' fill='#fff'/></svg></div>

<div class='abs' style='top:910px;left:0;width:1080px;height:240px;background:#F1ECE3'></div>
<div class='abs' style='top:928px;left:30px;right:30px;height:128px;display:flex;gap:14px'>{fact_tiles}</div>
<div class='abs' style='top:1068px;left:30px;right:30px;height:70px;border-radius:18px;background:{GRN};display:flex;align-items:center;gap:12px;padding:0 18px'>
 {T('بذمہ کمپنی:', 25, ORG2, 'font-weight:700', 1.6)}{perk_li}{T('دیگر مراعات مقامی لیبر لاء کے مطابق', 20, '#fff', 'font-weight:700;margin-inline-start:auto', 1.6)}</div>

<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:{CHAR};border-top:6px solid {ORG}'></div>
<div class='abs' style='top:1172px;left:26px;height:156px;background:#fff;border-radius:22px;display:flex;align-items:center;padding:0 22px;direction:ltr;box-shadow:0 8px 18px #0008'><div style='display:flex;flex-direction:column;gap:2px'>{nums}</div></div>
<div class='abs' style='top:1164px;right:30px;width:560px;text-align:right'>
 {T('ابھی رابطہ کریں!', 38, ORG2, 'font-weight:700', 1.6)}
 {T(f"اپنی {N('CV')} اور مکمل کاغذات واٹس ایپ کریں", 22, '#fff', 'font-weight:700', 1.7)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr;margin-top:4px'>{icon('mail', 24, ORG2, 2)}<span style='font-family:Archivo;font-size:23px;font-weight:700;color:#fff'>{EMAIL}</span></div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:6px;direction:ltr;margin-top:6px'>{icon('pin', 20, ORG2, 2.2)}<span style='font-family:Archivo;font-size:15px;font-weight:600;color:#D5D8DC'>{ADDRESS}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CREAM}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Saudi-Arabia-Super-Store-Packers-Urdu.png"))
