"""Saudi Arabia — General Workers (gardening or loading/unloading), Urdu v2 (2026-11-18). Converted from another
agency's Urdu newspaper ad (content only; same demand as demands/2026-10-20-saudi-general-workers). Facts: well-known
facility management & catering services company (employer not named); salary 1000 + 200 riyal + overtime; duty 8 h +
overtime; contract 2 years; basic English speaking required; accommodation, medical, transport by company; other
benefits per Saudi labour law; contact with passport & documents. Dropped: instant visa / instant departure, "no fee
for test interview", "self selection", the other agency's name/address/number. Partner agency: Shoaib & Brothers
(sheet only). No sharp gardener photo in the library — loading/logistics photos used; gardener photo requested.
Design: "desert dune" — warm sand-to-white page with dune curves and sun glow, terracotta urgency pill, giant Saudi-green
Nastaliq title, angled hero photo + inset, green salary shield-card, white fact tiles, Saudi-green footer."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

SAND, SAND2, TERRA, GRN, GRN2, GOLD, INK = "#F4E3C4", "#E9CC98", "#C2652A", "#006C35", "#00431F", "#F2B705", "#1E1A14"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.8: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    facts = [("clock", f"ڈیوٹی {N(8)} گھنٹے + اوور ٹائم"), ("calendar", f"معاہدہ {N(2)} سال"), ("home", "رہائش، میڈیکل، ٹرانسپورٹ بذمہ کمپنی"),
             ("chat", "بیسک انگلش بول چال لازمی"), ("check", "دیگر مراعات سعودی لیبر لاء کے مطابق"), ("doc", "پاسپورٹ اور کاغذات کے ساتھ رابطہ کریں")]
    tiles = "".join(f"<div style='display:flex;align-items:center;gap:12px;background:#fff;border-radius:16px;padding:0 14px;height:72px;box-shadow:0 8px 16px #1E1A1414;border-right:6px solid {GRN if i % 2 == 0 else TERRA}'>"
                    f"<span style='width:46px;height:46px;border-radius:12px;background:{GRN if i % 2 == 0 else TERRA};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 26, '#fff', 2.2)}</span>"
                    f"{T(t, 22, INK, 'font-weight:700;white-space:nowrap', 1.8)}</div>" for i, (ic, t) in enumerate(facts))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<div class='abs' style='inset:0;background:linear-gradient(180deg,#FFF9EF 0%,{SAND} 55%,{SAND2} 100%)'></div>
<div class='abs' style='top:-160px;left:-160px;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,#FFD98A,#FFD98A00 70%)'></div>
<svg class='abs' style='top:560px;left:0' width='1080' height='300'><path d='M0 120 C 220 40, 420 160, 640 90 S 960 40, 1080 100 V300 H0Z' fill='{SAND2}' opacity='.55'/><path d='M0 200 C 260 130, 520 230, 760 170 S 1000 140, 1080 180 V300 H0Z' fill='#DDB67A' opacity='.45'/></svg>
<div class='abs' style='top:22px;right:30px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0003'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:right')}</div>
<div class='abs' style='top:24px;left:30px;filter:drop-shadow(0 6px 10px #0004)'>{flag('saudi', 120, True, 'sagw2')}</div>
<div class='abs' style='top:112px;right:36px;width:620px'>
 <div style='display:inline-block;background:{TERRA};border-radius:999px;padding:0 26px;box-shadow:0 8px 16px #C2652A55'>{T('فوری ضرورت برائے سعودی عرب', 32, '#fff', 'font-weight:700', 1.75)}</div>
 {T('معروف فیسلٹی مینجمنٹ اینڈ کیٹرنگ کمپنی کے لیے', 24, '#5A4A35', 'font-weight:700;margin-top:6px', 1.8)}
 {T('جنرل ورکرز', 104, GRN, 'font-weight:700;margin-top:18px', 1.75)}
 {T('( گارڈننگ یا لوڈنگ اَن لوڈنگ )', 34, TERRA, 'font-weight:700;margin-top:16px', 1.7)}
 <div style='font:400 28px Anton;color:{GRN2};letter-spacing:4px;direction:ltr;text-align:right;margin-top:0'>GENERAL WORKERS · SAUDI ARABIA</div></div>

<div class='abs' style='top:150px;left:40px;width:360px;height:420px;border-radius:24px;overflow:hidden;border:7px solid #fff;transform:rotate(-3deg);box-shadow:0 22px 40px #1E1A1444'><img src='{P("rslinks_worker_hero_blue.png")}' style='width:100%;height:100%;object-fit:cover;object-position:35% 22%'></div>
<div class='abs' style='top:500px;left:300px;width:250px;height:180px;border-radius:18px;overflow:hidden;border:6px solid #fff;transform:rotate(4deg);box-shadow:0 16px 30px #1E1A1444'><img src='{P("uz_truck_loading.jpg")}' style='width:100%;height:100%;object-fit:cover;object-position:center 40%'></div>

<div class='abs' style='top:620px;right:40px;width:440px;height:200px;border-radius:26px;background:linear-gradient(135deg,{GRN},{GRN2});box-shadow:0 18px 34px #00431F55;display:flex;flex-direction:column;align-items:center;justify-content:center;border:4px solid {GOLD}'>
 {T('تنخواہ', 28, GOLD, 'font-weight:700', 1.5)}
 <div style='font:400 78px Anton;color:#fff;line-height:1;direction:ltr'>1000 + 200</div>
 {T('ریال + اوور ٹائم', 28, '#fff', 'font-weight:700', 1.7)}</div>

<div class='abs' style='top:830px;left:30px;right:30px;display:grid;grid-template-columns:1fr 1fr;gap:12px 14px'>{tiles}</div>
<div class='abs' style='top:1092px;left:0;width:1080px;text-align:center'>{T(f"اپنی {N('CV')} واٹس ایپ کریں — ابھی رابطہ کریں!", 34, TERRA, 'font-weight:700', 1.75)}</div>

<div class='abs' style='top:1196px;left:0;width:1080px;height:154px;background:linear-gradient(100deg,{GRN2},{GRN})'></div>
<div class='abs' style='top:1190px;left:0;width:1080px;height:6px;background:{GOLD}'></div>
<div class='abs' style='top:1212px;left:30px;right:30px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:6px 0;direction:ltr'>{nums}</div>
<div class='abs' style='top:1302px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:10px;direction:ltr'>{icon('mail', 22, GOLD, 2)}<span style='font:800 22px Archivo;color:#fff'>{EMAIL}</span></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{SAND}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Saudi-General-Workers-v2-Urdu.png"))
