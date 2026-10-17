"""Uzbekistan factory workers — v5 (2026-10-17): redesign of the user's own ad (demands/2026-10-17-uzbekistan-factory/user-ad.jpg).
Same content, B-2 visa removed (user), all three numbers. "محفوظ قدم" (safe step) kept out per ad rules -> "مضبوط قدم".
Design: white header, deep-teal hero with curved real-photo window, gold salary medallion, 4 stat chips, two cards, green CTA."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

TEAL, DEEP, BLUE, GRN, GOLD, INK = "#0A7E9C", "#06324A", "#0099B5", "#1EB53A", "#FFC83D", "#0B2238"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.75: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def build():
    hero_photo = (PHOTOS / "rslinks_worker_pack.png").as_uri()
    stats = [("user", N(50), "آسامیاں"), ("clock", f"{N(10)} گھنٹے", "کام کے اوقات"), ("calendar", f"{N('21 – 35')} سال", "عمر کی حد"),
             ("doc", f"{N('30 – 35')} دن", "پروسیسنگ ٹائم")]
    chips = "".join(f"<div style='flex:1;background:#fff;border-radius:18px;box-shadow:0 6px 14px rgba(6,50,74,.18);display:flex;flex-direction:column;align-items:center;justify-content:center;border-bottom:5px solid {BLUE}'>"
                    f"<div style='width:46px;height:46px;border-radius:50%;background:{TEAL};display:flex;align-items:center;justify-content:center'>{icon(ic, 25, '#fff', 2.3)}</div>"
                    f"{T(v, 25, INK, 'font-weight:700;margin-top:2px', 1.6)}{T(l, 16, '#4A6070', 'margin-top:-4px', 1.6)}</div>" for ic, v, l in stats)
    work = ["عمومی فیکٹری ورک", "پیکجنگ", "اسٹوری (آرڈرنگ)", "مال سامان کی صفائی کرنا", "پروڈکشن لائن پر کام"]
    work_li = "".join(f"<div style='display:flex;align-items:center;gap:10px;padding:6px 0;border-bottom:1px dashed #C9DCE5'>"
                      f"<span class='num' style='width:32px;height:32px;border-radius:50%;background:{TEAL};color:#fff;font-size:18px;display:flex;align-items:center;justify-content:center;flex:none'>{i + 1}</span>"
                      f"{T(w, 25, INK, 'font-weight:700', 1.75)}</div>" for i, w in enumerate(work))
    fac = [("home", "مفت رہائش"), ("bus", "مفت ٹرانسپورٹ"), ("medical", "مفت میڈیکل"), ("food", "مفت کھانا"), ("gear", "کمپنی کی طرف سے دیگر سہولیات")]
    fac_li = "".join(f"<div style='display:flex;align-items:center;gap:10px;padding:6px 0;border-bottom:1px dashed #CBE7D2'>"
                     f"<span style='width:32px;height:32px;border-radius:50%;background:{GRN};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 18, '#fff', 2.4)}</span>"
                     f"{T(w, 25, INK, 'font-weight:700', 1.75)}</div>" for ic, w in fac)
    card = lambda title, color, body: (f"<div style='flex:1;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 8px 20px rgba(6,50,74,.14)'>"
                                       f"<div style='background:linear-gradient(90deg,{color},{color}cc);padding:0 18px 4px'>{T(title, 31, '#fff', 'font-weight:700', 1.7)}</div>"
                                       f"<div style='padding:4px 18px 8px'>{body}</div></div>")
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'><span style='line-height:0'>{whatsapp_icon(30)}</span><span class='num' style='font-size:31px;color:{INK};line-height:1.15'>{n}</span></div>" for n in PHONES)
    body = f"""<div class='ur-on' dir='rtl'>
<div class='abs' style='top:0;left:0;width:1080px;height:150px;background:#fff'></div>
<div class='abs' style='top:20px;right:26px'>{logo_img('logo-horizontal-light', 'width:420px;height:108px;object-position:right')}</div>
<div class='abs' style='top:22px;left:26px;display:flex;align-items:center;gap:16px;direction:ltr'>
 <div style='filter:drop-shadow(0 4px 8px #0004)'>{flag('uzbekistan', 160, True, 'uz5')}</div>
 <div style='background:linear-gradient(135deg,#E53935,#B71C1C);border-radius:14px;padding:0 20px 8px;box-shadow:0 6px 14px #0004;display:flex;align-items:center;gap:8px'>{icon('megaphone', 30, '#fff', 2.2)}{T('فوری ضرورت', 34, '#fff', 'font-weight:700', 1.6)}</div></div>
<div class='abs' style='top:150px;left:0;width:1080px;height:430px;background:linear-gradient(135deg,{TEAL},{DEEP})'></div>
<svg class='abs' style='left:0;top:150px' width='1080' height='430'><circle cx='980' cy='40' r='200' fill='#ffffff0c'/><circle cx='640' cy='430' r='120' fill='#ffffff08'/>
 <path d='M0 400 C 300 360, 700 450, 1080 390 L1080 430 L0 430Z' fill='{GOLD}'/><path d='M0 412 C 300 372, 700 462, 1080 402 L1080 430 L0 430Z' fill='#EEF5F8'/></svg>
<div class='abs' style='top:170px;left:30px;width:400px;height:360px;border-radius:200px 200px 26px 26px;overflow:hidden;border:6px solid #fff;box-shadow:0 14px 30px #0007'>
 <img src='{hero_photo}' style='width:100%;height:100%;object-fit:cover;object-position:center 30%'></div>
<div class='abs' style='top:168px;right:36px;width:590px;text-align:right'>
 {T('فیکٹری ورکرز کے لیے', 34, GOLD, 'font-weight:700', 1.7)}
 {T('فوری ضرورت', 80, '#fff', 'font-weight:700;margin-top:6px', 1.4)}
 <div style='font-family:Anton;font-size:52px;color:{GOLD};letter-spacing:1px;direction:ltr;text-align:right;margin-top:16px;line-height:1'>FACTORY WORKERS</div>
 <div style='display:inline-flex;align-items:center;gap:8px;margin-top:14px;background:#fff;border-radius:999px;padding:0 20px 6px'>{icon('pin', 26, '#E53935', 2.4)}{T('تاشقند، ازبکستان', 26, INK, 'font-weight:700', 1.6)}</div>
 {T('بہتر مستقبل کی جانب ایک مضبوط قدم', 22, '#DCEFF6', 'font-weight:700;margin-top:4px', 1.7)}</div>
<div class='abs' style='top:0;left:0;width:1080px;height:1350px;background:#EEF5F8;z-index:-1'></div>
<div class='abs' style='top:592px;left:30px;right:30px;height:132px;display:flex;gap:12px'>
 <div style='flex:1.35;border-radius:22px;background:radial-gradient(circle at 30% 20%,#FFE38A,{GOLD} 55%,#E0A21A);box-shadow:0 8px 18px rgba(0,0,0,.2);display:flex;flex-direction:column;align-items:center;justify-content:center'>
  <div style='direction:ltr;display:flex;align-items:baseline;gap:6px'><span class='num' style='font-size:66px;color:{INK};line-height:1'>$550</span><span class='num' style='font-size:24px;color:{INK}'>USD</span></div>
  {T('ماہانہ تنخواہ', 21, INK, 'font-weight:700;margin-top:-2px', 1.6)}</div>{chips}</div>
<div class='abs' style='top:748px;left:30px;right:30px;display:flex;gap:16px'>{card('کام کی تفصیلات', TEAL, work_li)}{card('سہولیات', '#1A9E46', fac_li)}</div>
<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:linear-gradient(110deg,{DEEP},{TEAL})'></div>
<svg class='abs' style='left:0;top:1138px' width='1080' height='30'><path d='M0 30 C 300 0, 700 24, 1080 6 L1080 30Z' fill='{GOLD}'/></svg>
<div class='abs' style='top:1168px;left:26px;height:150px;background:#fff;border-radius:22px;display:flex;align-items:center;padding:0 22px;direction:ltr;box-shadow:0 8px 18px #0006'><div style='display:flex;flex-direction:column;gap:2px'>{nums}</div></div>
<div class='abs' style='top:1168px;right:30px;width:520px;text-align:right'>
 {T('ابھی رابطہ کریں!', 38, GOLD, 'font-weight:700', 1.6)}
 {T('مزید معلومات کے لیے واٹس ایپ پر رابطہ کریں', 21, '#fff', 'font-weight:700', 1.7)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr;margin-top:6px'>{icon('mail', 24, GOLD, 2)}<span style='font-family:Archivo;font-size:23px;font-weight:700;color:#fff'>{EMAIL}</span></div>
 {T('آپ کے بہتر مستقبل کے لیے ہم ساتھ ہیں', 18, '#BFE3EE', 'margin-top:2px', 1.7)}</div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#EEF5F8'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Uzbekistan-Factory-Workers-v5-Urdu.png"))
