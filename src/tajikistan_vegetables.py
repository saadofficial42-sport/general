"""Tajikistan — agriculture / gardening (tomato, cucumber, onion), Urdu (2026-10-28). Facts:
demands/2026-10-28-tajikistan-vegetables/facts.md. Photo: farmer crop from the user's reference (tj_farmer.jpg).
Design: "harvest crate" — deep forest-green page, wide photo banner with wooden-crate frame, three vegetable chips,
cream 'crate label' salary tag, two white cards, gold-green CTA. Differs from the tomato-tunnel ad (cream/arch)."""
from common import PHONES, PHOTOS, font_css, icon, logo_img, render, whatsapp_icon
from tajikistan_tomato import flag_tj

FOREST, FOREST2, WOOD, WOOD2, CREAM, RED, LIME, INK = "#14452F", "#0B2E1F", "#9C6B3C", "#6E4724", "#FFF6E3", "#D7301F", "#9BD45A", "#1E2A22"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.75: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def build():
    photo = (PHOTOS / "tj_farmer.jpg").as_uri()
    veg = [("#D7301F", "ٹماٹر"), ("#2E8B3A", "کھیرا"), ("#8E3A8C", "پیاز")]
    chips = "".join(f"<div style='display:flex;align-items:center;gap:8px;background:#fff;border-radius:999px;padding:0 18px 4px;box-shadow:0 6px 14px #0004'>"
                    f"<span style='width:22px;height:22px;border-radius:50%;background:{c}'></span>{T(t, 28, INK, 'font-weight:700', 1.6)}</div>" for c, t in veg)
    det = [("pin", "مقام: تاجکستان"), ("leaf", "کام: ٹماٹر، کھیرا اور پیاز کی کاشت اور دیکھ بھال"),
           ("calendar", f"معاہدہ: {N(2)} سال (قابلِ توسیع)"), ("user", "صرف پاکستانی مرد کارکنان")]
    fea = [("plane", "ٹکٹ، ویزا اور پروٹیکٹر شامل"), ("home", "کھانا اور رہائش کمپنی کی طرف سے"), ("check", "فصل کی تربیت اور رہنمائی"),
           ("leaf", "صاف ستھرا ماحول"), ("video", "انٹرویو آن لائن (زوم)")]
    li = lambda items, c: "".join(f"<div style='display:flex;align-items:center;gap:12px;padding:3px 0;border-bottom:1px dashed #D9CBB0'>"
                                  f"<span style='width:42px;height:42px;border-radius:50%;background:{c};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 22, '#fff', 2.3)}</span>"
                                  f"{T(t, 22, INK, 'font-weight:700', 1.8)}</div>" for ic, t in items)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:{INK};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<div class='abs' style='inset:0;background:radial-gradient(circle at 80% 10%,#1F6B45,{FOREST} 40%,{FOREST2})'></div>
<div class='abs' style='top:28px;right:34px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:280px;height:72px;object-position:right')}</div>
<div class='abs' style='top:30px;left:36px'>{flag_tj(150)}</div>
<div class='abs' style='top:86px;left:0;right:0;text-align:center'>
 {T('پاکستانی مرد کارکنوں کے لیے', 30, LIME, 'font-weight:700;margin-bottom:46px', 1.7)}
 {T('تاجکستان', 96, '#fff', 'font-weight:700;text-shadow:0 6px 0 #062015,0 14px 26px #0008', 1.4)}
 {T('زراعت / باغبانی کے شعبے میں ملازمت', 30, CREAM, 'font-weight:700;margin-top:14px', 1.7)}</div>

<div class='abs' style='top:420px;left:40px;right:40px;height:330px;border-radius:18px;padding:14px;background:repeating-linear-gradient(90deg,{WOOD} 0 60px,{WOOD2} 60px 64px);box-shadow:0 18px 34px #0008'>
 <div style='width:100%;height:100%;border-radius:10px;overflow:hidden'><img src='{photo}' style='width:100%;height:100%;object-fit:cover;object-position:center 35%'></div></div>
<div class='abs' style='top:388px;right:70px;transform:rotate(3deg);background:{CREAM};border:3px dashed {WOOD};border-radius:14px;padding:6px 22px 10px;box-shadow:0 10px 20px #0006;text-align:center'>
 {T('ماہانہ تنخواہ', 22, WOOD2, 'font-weight:700', 1.5)}
 <div style='direction:ltr'><span class='num' style='font-size:58px;color:{RED};line-height:1'>$700 – 800</span></div>
 {T('+ کھانا اور رہائش', 20, FOREST, 'font-weight:700', 1.6)}</div>
<div class='abs' style='top:722px;left:0;right:0;display:flex;justify-content:center;gap:16px'>{chips}</div>
<div class='abs' style='top:800px;left:0;right:0;text-align:center'>{T('ٹماٹر، کھیرا اور پیاز کی پیداوار میں اضافے کے لیے', 24, CREAM, 'font-weight:700', 1.7)}</div>

<div class='abs' style='top:862px;left:34px;right:34px;display:flex;gap:16px'>
 <div style='flex:1;background:{CREAM};border-radius:20px;padding:2px 18px 8px'>{T('ملازمت کی تفصیلات', 30, FOREST, 'font-weight:700', 1.7)}{li(det, FOREST)}</div>
 <div style='flex:1;background:{CREAM};border-radius:20px;padding:2px 18px 8px'>{T('خصوصیات', 30, RED, 'font-weight:700', 1.7)}{li(fea, RED)}</div></div>

<div class='abs' style='top:1190px;left:0;width:1080px;height:160px;background:linear-gradient(100deg,{LIME},#C9E87A)'></div>
<div class='abs' style='top:1204px;left:30px;width:600px;height:132px;background:#fff;border-radius:18px;display:grid;grid-template-columns:1fr 1fr;align-content:center;gap:10px 12px;padding:0 18px;box-sizing:border-box;box-shadow:0 8px 18px #0003;direction:ltr'>{nums}</div>
<div class='abs' style='top:1196px;right:40px;width:390px;text-align:right'>
 {T('ابھی رابطہ کریں!', 40, FOREST2, 'font-weight:700', 1.6)}
 {T(f"اپنی {N('CV')} واٹس ایپ کریں", 21, INK, 'font-weight:700', 1.8)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr'>{icon('mail', 22, FOREST, 2)}<span style='font:800 20px Archivo;color:{INK}'>{EMAIL}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{FOREST}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Tajikistan-Agriculture-Vegetables-Urdu.png"))
