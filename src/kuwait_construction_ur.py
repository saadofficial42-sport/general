"""Kuwait — construction trades (625 posts), Urdu (2026-11-18). Same facts and design family as kuwait_construction.py
(Kuwait Towers dusk), set right-to-left in Nastaliq; towers mirrored to the left."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon
from kuwait_construction import NAVY, NAVY2, TEAL, GOLD, GOLD2, GRN, RED, INK, EMAIL, towers

N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.8: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"
JOBS = [("اسسٹنٹ کارپینٹر (شٹرنگ)", "", "50", "140"), ("میسن – برک (طابوق / بلاک)", "", "100", "170"), ("میسن – پلستر", "", "100", "170"),
        ("میسن – سرامک ٹائلز", "", "100", "170"), ("میسن – ماربل ٹائلز", "", "75", "170"), ("پینٹرز – ایکسٹرنل و انٹرنل", "سگما پینٹ کا تجربہ رکھنے والوں کو ترجیح", "200", "170")]


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    rows = "".join(f"<div style='display:grid;grid-template-columns:1fr 110px 170px;align-items:center;min-height:56px;border-top:1px solid #ffffff1c'>"
                   f"<div>{T(t, 25, '#fff', 'font-weight:700', 1.75)}{T(n, 15, GOLD2, 'font-weight:700;margin-top:10px', 1.4) if n else ''}</div>"
                   f"<span style='font:400 30px Anton;color:#fff;text-align:center'>{q}</span>"
                   f"<span style='font:400 34px Anton;color:{GOLD};text-align:left;direction:ltr'>{s} <span style='font-size:20px'>KWD</span></span></div>" for t, n, q, s in JOBS)
    chips = [("clock", f"ڈیوٹی {N(8)} گھنٹے · ہفتے میں {N(6)} دن"), ("calendar", "جمعہ چھٹی"), ("overtime", f"{N(8)} گھنٹے کے بعد اور چھٹی پر اوور ٹائم"),
             ("plane", "ٹکٹ شامل"), ("doc", f"{N(1)} سال کا معاہدہ"), ("check", "دیگر مراعات کویت لیبر لاء کے مطابق")]
    chip = "".join(f"<div style='display:flex;align-items:center;gap:10px;background:#fff;border-radius:14px;padding:4px 12px;box-shadow:0 8px 16px #0004'>"
                   f"<span style='width:40px;height:40px;border-radius:10px;background:{GRN};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 22, '#fff', 2.3)}</span>"
                   f"{T(t, 19, INK, 'font-weight:700', 1.75)}</div>" for ic, t in chips)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    ph = lambda f, pos: f"<div style='width:100%;height:100%;border-radius:16px;overflow:hidden;border:4px solid {GOLD};box-shadow:0 14px 26px #0008'><img src='{P(f)}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'></div>"
    body = f"""<div dir='rtl'>
<div class='abs' style='inset:0;background:linear-gradient(180deg,#F08A4B 0%,#B6506A 14%,{TEAL} 34%,{NAVY} 55%,{NAVY2} 100%)'></div>
<div class='abs' style='top:40px;left:20px;opacity:.9;transform:scaleX(-1)'>{towers('#06122Acc')}</div>
<div class='abs' style='top:0;left:0;width:1080px;height:10px;display:flex'><span style='flex:1;background:{GRN}'></span><span style='flex:1;background:#fff'></span><span style='flex:1;background:{RED}'></span></div>
<div class='abs' style='top:28px;right:30px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0006'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:right')}</div>
<div class='abs' style='top:30px;left:30px;filter:drop-shadow(0 6px 10px #0007)'>{flag('kw', 120, True, 'kwcu')}</div>
<div class='abs' style='top:120px;right:40px;width:760px'>
 <div style='display:inline-block;background:{RED};border-radius:8px;padding:0 18px'>{T('فوری ضرورت برائے کویت', 28, '#fff', 'font-weight:700', 1.7)}</div>
 {T(f"کویت میں <span style='color:{GOLD2}'>کنسٹرکشن</span> جابز", 70, '#fff', 'font-weight:700;margin-top:6px;white-space:nowrap;text-shadow:0 8px 24px #0008', 1.75)}
 {T(f"{N(625)} آسامیاں · ہنرمند اور غیر ہنرمند · {N(1)} سال کا معاہدہ", 24, '#F6E7C8', 'font-weight:700;margin-top:2px', 1.75)}</div>

<div class='abs' style='top:430px;left:30px;right:30px;height:220px;display:grid;grid-template-columns:1.25fr 1.25fr 1fr;gap:14px'>
 {ph('rslinks_construction_engineer.png', 'center 30%')}{ph('rs_plaster2.jpg', '30% 30%')}{ph('rs_tile2.jpg', '45% 30%')}</div>

<div class='abs' style='top:666px;left:30px;right:30px;border-radius:22px;background:linear-gradient(180deg,#0A1830ee,#050C1Cee);border:2px solid {GOLD}66;padding:6px 26px 8px;box-sizing:border-box;box-shadow:0 16px 30px #0008'>
 <div style='display:grid;grid-template-columns:1fr 110px 170px;height:36px;align-items:center'>{T('شعبہ', 18, GOLD2, 'font-weight:700', 1.6)}{T('آسامیاں', 18, GOLD2, 'font-weight:700;text-align:center', 1.6)}{T('ماہانہ تنخواہ', 18, GOLD2, 'font-weight:700;text-align:left', 1.6)}</div>{rows}</div>

<div class='abs' style='top:1074px;left:30px;right:30px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px'>{chip}</div>

<div class='abs' style='top:1214px;left:0;width:1080px;height:136px;background:linear-gradient(100deg,#005A2D,{GRN})'></div>
<div class='abs' style='top:1208px;left:0;width:1080px;height:6px;background:{GOLD}'></div>
<div class='abs' style='top:1220px;left:24px;right:24px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:2px 0;direction:ltr'>{nums}</div>
<div class='abs' style='top:1302px;left:24px;right:24px;display:flex;justify-content:space-between;align-items:center'>
 {T("سی وی، پاسپورٹ اور تجربہ سرٹیفکیٹ واٹس ایپ کریں", 22, GOLD2, 'font-weight:700', 1.7)}
 <span style='display:inline-flex;align-items:center;gap:8px;direction:ltr'>{icon('mail', 20, GOLD2, 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></span></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{NAVY}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Kuwait-Construction-625-Posts-Urdu.png"))
