"""Kuwait — Bike Riders, Urdu (2026-10-27). Same facts as kuwait_riders.py (demands/2026-10-27-kuwait-riders/facts.md).
User: different design, more white. Design: "clean white card" — white page, Kuwait-flag corner ribbon, rounded
rider photo with orange frame, green title, orange salary pill, white perk cards with thin borders, light CTA."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

GRN, ORG, RED, INK, SOFT = "#007A3D", "#F2711C", "#CE1126", "#1B1F24", "#F5F7F6"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.75: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def build():
    rider = (PHOTOS / "kw_rider_tight.jpg").as_uri()
    perks = [("clock", f"{N(12)} گھنٹے", "ڈیوٹی ٹائم"), ("home", "رہائش", "کمپنی کی طرف سے"),
             ("medical", "میڈیکل", "کمپنی کی طرف سے"), ("bus", "ٹرانسپورٹ", "کمپنی کی طرف سے")]
    perk = "".join(f"<div style='background:#fff;border:2px solid #E3E8E5;border-radius:20px;display:flex;align-items:center;gap:14px;padding:0 18px'>"
                   f"<span style='width:58px;height:58px;border-radius:50%;background:#EAF5EF;display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 30, GRN, 2.3)}</span>"
                   f"<div>{T(a, 30, INK, 'font-weight:700', 1.7)}{T(b, 18, '#6B7570', 'font-weight:700;margin-top:12px', 1.6)}</div></div>" for ic, a, b in perks)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:{INK};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<svg class='abs' style='top:0;left:0' width='1080' height='1350'>
 <path d='M0 0 H330 L0 230Z' fill='{GRN}'/><path d='M0 230 L330 0 H390 L0 272Z' fill='#fff'/><path d='M0 272 L390 0 H450 L0 314Z' fill='{RED}'/><path d='M0 0 H120 L0 84Z' fill='#111'/>
 <circle cx='1000' cy='1180' r='220' fill='{SOFT}'/></svg>
<div class='abs' style='top:30px;right:34px'>{logo_img('logo-horizontal-light', 'width:320px;height:84px;object-position:right')}</div>
<div class='abs' style='top:150px;right:40px;width:560px;text-align:right'>
 <div style='display:inline-flex;align-items:center;gap:12px;background:{SOFT};border-radius:999px;padding:0 20px 6px'>{T('فوری ضرورت برائے', 30, RED, 'font-weight:700', 1.7)}{flag('kw', 70, False)}</div>
 {T('کویت', 120, GRN, 'font-weight:700;margin-top:6px', 1.45)}
 {T('بائیک رائیڈرز', 84, INK, 'font-weight:700;margin-top:4px', 1.6)}
 <div style='font:400 34px Anton;color:{ORG};letter-spacing:4px;direction:ltr;text-align:right;margin-top:6px'>BIKE RIDERS · KUWAIT</div></div>
<div class='abs' style='top:170px;left:40px;width:400px;height:560px;border-radius:200px 200px 30px 30px;overflow:hidden;border:8px solid #fff;outline:4px solid {ORG};box-shadow:0 20px 40px rgba(0,0,0,.18)'>
 <img src='{rider}' style='width:100%;height:100%;object-fit:cover;object-position:center 0%'></div>

<div class='abs' style='top:690px;right:40px;width:560px;height:150px;border-radius:24px;background:linear-gradient(135deg,{ORG},#E2470F);box-shadow:0 14px 28px rgba(242,113,28,.35);display:flex;align-items:center;justify-content:center;gap:24px'>
 {T('ماہانہ تنخواہ', 32, '#fff', 'font-weight:700', 1.6)}
 <div style='direction:ltr;display:flex;align-items:baseline;gap:8px'><span class='num' style='font-size:92px;color:#fff;line-height:1'>145</span><span class='num' style='font-size:34px;color:#FFE3C7'>KWD</span></div></div>

<div class='abs' style='top:780px;left:40px;width:400px;height:0'></div>
<div class='abs' style='top:870px;left:40px;right:40px;display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:118px;gap:16px'>{perk}</div>

<div class='abs' style='top:1140px;left:40px;right:40px;height:2px;background:#E3E8E5'></div>
<div class='abs' style='top:1166px;left:30px;width:600px;height:150px;background:{SOFT};border:2px solid #E3E8E5;border-radius:20px;display:grid;grid-template-columns:1fr 1fr;align-content:center;gap:12px;padding:0 18px;box-sizing:border-box;direction:ltr'>{nums}</div>
<div class='abs' style='top:1156px;right:40px;width:390px;text-align:right'>
 {T('ابھی رابطہ کریں!', 42, GRN, 'font-weight:700', 1.6)}
 {T(f"اپنی {N('CV')} واٹس ایپ کریں", 22, INK, 'font-weight:700', 1.8)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr;margin-top:2px'>{icon('mail', 22, ORG, 2)}<span style='font:800 20px Archivo;color:{INK}'>{EMAIL}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Kuwait-Bike-Riders-Urdu.png"))
