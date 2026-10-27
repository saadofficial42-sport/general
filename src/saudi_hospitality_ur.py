"""Saudi Arabia — Hospitality Staff, Urdu (2026-10-27). Same facts as saudi_hospitality.py
(demands/2026-10-27-saudi-hospitality/facts.md). User: unique design.
Design: "serving tray" — white/mint page, deep teal header with a cloche (dome) silhouette, three tall arched
position columns (photo top, Urdu title, salary on a gold plate), teal ribbon perks, white CTA."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

TEAL, TEAL2, GOLD, GOLD2, MINT, INK = "#0F5C63", "#083A40", "#D4A537", "#F3D27A", "#EEF7F5", "#17262A"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.75: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"

JOBS = [("sa_waiter.jpg", "center 25%", "ویٹر", "WAITER", "1000 – 1100"),
        ("sa_kitchen_helper.jpg", "center 30%", "کچن ہیلپر", "KITCHEN HELPER", "1000"),
        ("sa_rice_cook.jpg", "center 25%", "رائس کک", "RICE COOK", "1300 – 1500")]


def build():
    cols = "".join(
        f"<div style='background:#fff;border-radius:150px 150px 24px 24px;box-shadow:0 14px 30px rgba(8,58,64,.16);overflow:hidden;display:flex;flex-direction:column;align-items:center'>"
        f"<div style='width:100%;height:300px;overflow:hidden;border-bottom:6px solid {GOLD}'><img src='{(PHOTOS / f).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'></div>"
        f"{T(ur, 42, TEAL2, 'font-weight:700;margin-top:4px', 1.9)}"
        f"<div style='font:400 20px Anton;color:{GOLD};letter-spacing:3px;margin-top:10px'>{en}</div>"
        f"<div style='margin-top:14px;width:240px;height:96px;border-radius:50%;background:radial-gradient(circle at 40% 30%,{GOLD2},{GOLD} 60%,#A97F1F);box-shadow:0 8px 16px rgba(0,0,0,.2),inset 0 -4px 0 #0002;display:flex;flex-direction:column;align-items:center;justify-content:center'>"
        f"<span class='num' style='font-size:{38 if '–' in sal else 46}px;color:{TEAL2};line-height:1'>{sal}</span><span class='num' style='font-size:16px;color:{TEAL2}'>SAR</span></div>"
        f"<div style='margin:14px 0 18px;background:{MINT};border-radius:999px;padding:0 16px 4px;display:flex;align-items:center;gap:6px'>{icon('food', 20, TEAL, 2.3)}{T('کھانا + اوور ٹائم', 20, TEAL, 'font-weight:700', 1.7)}</div></div>"
        for f, pos, ur, en, sal in JOBS)
    perks = [("home", "رہائش"), ("medical", "میڈیکل"), ("bus", "ٹرانسپورٹ")]
    perk = "".join(f"<div style='display:flex;align-items:center;gap:10px'>{icon(ic, 32, GOLD2, 2.2)}{T(a, 30, '#fff', 'font-weight:700', 1.7)}</div>" for ic, a in perks)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<div class='abs' style='top:0;left:0;width:1080px;height:360px;background:linear-gradient(160deg,{TEAL},{TEAL2})'></div>
<svg class='abs' style='top:0;left:0' width='1080' height='420'>
 <path d='M0 360 Q540 430 1080 360 L1080 420 L0 420Z' fill='{MINT}'/>
 <g opacity='.12' fill='#fff'><path d='M110 250 a120 110 0 0 1 240 0Z'/><rect x='90' y='250' width='280' height='14' rx='7'/><circle cx='230' cy='132' r='12'/></g></svg>
<div class='abs' style='top:28px;right:34px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:280px;height:72px;object-position:right')}</div>
<div class='abs' style='top:26px;left:34px;filter:drop-shadow(0 6px 12px #0008)'>{flag('saudi', 130, True, 'sahu')}</div>
<div class='abs' style='top:116px;left:0;right:0;text-align:center'>
 {T('فوری ضرورت برائے سعودی عرب', 34, GOLD2, 'font-weight:700', 1.8)}
 {T('ہوٹل و ریسٹورنٹ اسٹاف', 76, '#fff', 'font-weight:700;margin-top:6px;text-shadow:0 6px 16px #0006', 1.8)}</div>

<div class='abs' style='top:400px;left:34px;right:34px;display:grid;grid-template-columns:repeat(3,1fr);gap:22px'>{cols}</div>

<div class='abs' style='top:1030px;left:34px;right:34px;height:96px;background:{TEAL};border-radius:20px;display:flex;align-items:center;justify-content:space-around;padding:0 20px'>
 {T('کمپنی کی طرف سے:', 28, GOLD2, 'font-weight:700', 1.7)}{perk}</div>

<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:linear-gradient(100deg,{TEAL2},{TEAL})'></div>
<div class='abs' style='top:1150px;left:0;width:1080px;height:6px;background:{GOLD}'></div>
<div class='abs' style='top:1186px;left:34px;display:grid;grid-template-columns:auto auto;gap:14px 30px;direction:ltr'>{nums}</div>
<div class='abs' style='top:1172px;right:40px;width:380px;text-align:right'>
 {T('ابھی رابطہ کریں!', 42, GOLD2, 'font-weight:700', 1.6)}
 {T(f"اپنی {N('CV')} واٹس ایپ کریں", 22, '#fff', 'font-weight:700', 1.8)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr'>{icon('mail', 22, GOLD2, 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{MINT}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Saudi-Arabia-Hospitality-Staff-Urdu.png"))
