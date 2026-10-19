"""Saudi Arabia — Super Store Workers (Packers), Urdu v2 (2026-10-19): user asked to change the person and the style.
Facts unchanged: demands/2026-10-19-saudi-supermarket-packers/facts.md.
Design: "supermarket sale flyer" — red top with yellow sunburst, circular spotlight photo of a different RS Links staff member
(the packer, rslinks_worker_pack_x3), yellow price-tag salary, white coupon-style fact tiles, red CTA with numbers in one row."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

RED, RED2, YEL, YEL2, INK, PAPER = "#D32F2F", "#9E1B1B", "#FFD54F", "#FFB300", "#2A1A12", "#FFFDF7"
EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.75: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"
img = lambda k, pos="center": f"<img src='{(PHOTOS / (k + '.png')).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos};display:block'>"


def build():
    rays = "".join(f"<path d='M290 420 L{290 + 1400 * __import__('math').cos(a / 100):.0f} {420 + 1400 * __import__('math').sin(a / 100):.0f} "
                   f"L{290 + 1400 * __import__('math').cos(a / 100 + .09):.0f} {420 + 1400 * __import__('math').sin(a / 100 + .09):.0f}Z' fill='#ffffff10'/>"
                   for a in range(0, 628, 18))
    duties = ["گروسری اسٹور میں آنے والا سامان اتار کر ریکس میں لگانا", "پارسلز کسٹمر کا نام اور آرڈر نمبر دیکھ کر پیک کرنا"]
    duty_li = "".join(f"<div style='display:flex;align-items:center;gap:14px;background:#fff;border-radius:16px;padding:8px 16px 12px;margin-top:14px;box-shadow:0 4px 10px rgba(0,0,0,.08);border-inline-start:8px solid {RED}'>"
                      f"<span class='num' style='width:42px;height:42px;border-radius:50%;background:{YEL};color:{RED2};font-size:24px;display:flex;align-items:center;justify-content:center;flex:none;margin-top:4px'>{i + 1}</span>"
                      f"{T(s, 26, INK, 'font-weight:700', 1.8)}</div>" for i, s in enumerate(duties))
    facts = [("clock", f"{N('09')} گھنٹے", "ڈیوٹی"), ("calendar", f"{N(2)} سال", "معاہدہ"), ("user", f"{N('21 – 30')} سال", "عمر"),
             ("chat", "بیسک انگلش", "بول چال لازمی")]
    tiles = "".join(f"<div style='flex:1;border:3px dashed {RED};border-radius:18px;background:#fff;display:flex;align-items:center;gap:10px;padding:0 14px'>"
                    f"<div style='width:52px;height:52px;border-radius:14px;background:{RED};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 30, '#fff', 2.3)}</div>"
                    f"<div>{T(l, 18, '#7A5A4A', 'font-weight:700', 1.5)}{T(v, 26, INK, 'font-weight:700;margin-top:12px', 1.5)}</div></div>" for ic, v, l in facts)
    perks = [("home", "رہائش"), ("medical", "میڈیکل"), ("bus", "ٹرانسپورٹ")]
    perk_li = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{icon(ic, 28, RED2, 2.4)}{T(s, 25, INK, 'font-weight:700', 1.6)}</div>" for ic, s in perks)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'><span style='line-height:0'>{whatsapp_icon(36)}</span><span class='num' style='font-size:31px;color:{INK};line-height:1.2'>{n}</span></div>" for n in PHONES)
    body = f"""<div class='ur-on' dir='rtl'>
<div class='abs' style='top:0;left:0;width:1080px;height:660px;background:radial-gradient(circle at 27% 62%,#E53935,{RED} 40%,{RED2})'></div>
<svg class='abs' style='top:0;left:0' width='1080' height='660'>{rays}
 <path d='M0 600 C 260 650, 640 560, 1080 630 L1080 660 L0 660Z' fill='{YEL}'/><path d='M0 618 C 260 668, 640 578, 1080 648 L1080 660 L0 660Z' fill='{PAPER}'/></svg>
<div class='abs' style='top:20px;right:26px;background:#fff;border-radius:18px;padding:4px 16px;box-shadow:0 6px 16px #0005'>{logo_img('logo-horizontal-light', 'width:360px;height:90px;object-position:right')}</div>
<div class='abs' style='top:16px;left:26px;filter:drop-shadow(0 4px 8px #0006)'>{flag('saudi', 140, True, 'sa10')}</div>

<div class='abs' style='top:168px;left:56px;width:440px;height:440px;border-radius:50%;background:{YEL};box-shadow:0 16px 36px #0007'></div>
<div class='abs' style='top:182px;left:70px;width:412px;height:412px;border-radius:50%;overflow:hidden;border:7px solid #fff;box-sizing:border-box'>{img('rslinks_worker_pack_x3', '55% 40%')}</div>
<div class='abs' style='top:150px;left:372px;width:150px;height:150px;border-radius:50%;background:#fff;box-shadow:0 8px 18px #0006;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(8deg)'>
 <span class='num' style='font-size:54px;color:{RED};line-height:1'>200</span>{T('آسامیاں', 22, INK, 'font-weight:700;margin-top:-4px', 1.5)}</div>

<div class='abs' style='top:132px;right:34px;width:520px;text-align:right'>
 <div style='display:inline-block;background:{YEL};border-radius:12px;padding:0 18px 6px;transform:rotate(-2deg)'>{T('فوری ضرورت برائے', 30, RED2, 'font-weight:700', 1.7)}</div>
 {T('سعودی عرب', 88, '#fff', 'font-weight:700;margin-top:-4px;margin-bottom:36px;text-shadow:0 6px 14px #0005', 1.5)}
 {T('سعودی عرب کی مشہور سپر مارکیٹ کے لیے', 25, '#FFE9E9', 'font-weight:700', 1.7)}
 <div style='margin-top:12px;background:#fff;border-radius:18px;padding:2px 20px 12px;box-shadow:0 8px 18px #0005;border-bottom:7px solid {YEL}'>
  {T('سپر اسٹور ورکرز (پیکرز)', 44, RED, 'font-weight:700', 1.65)}<div style='height:12px'></div>
  <div style='font-family:Anton;font-size:28px;color:{INK};letter-spacing:1px;direction:ltr;text-align:right;line-height:1.1'>SUPER STORE WORKERS (PACKERS)</div></div></div>

<div class='abs' style='top:552px;right:60px;transform:rotate(-4deg);filter:drop-shadow(0 10px 14px rgba(0,0,0,.3))'>
 <div style='position:relative;background:linear-gradient(135deg,{YEL},{YEL2});clip-path:polygon(0 50%,13% 0,100% 0,100% 100%,13% 100%);padding:6px 34px 10px 90px;display:flex;align-items:center;gap:18px;direction:ltr'>
  <div style='position:absolute;left:34px;top:50%;width:22px;height:22px;margin-top:-11px;border-radius:50%;background:{PAPER};box-shadow:inset 0 2px 4px #0005'></div>
  <span class='num' style='font-size:86px;color:{RED2};line-height:1.05'>1300</span>
  <div style='text-align:right'><span class='num' style='font-size:34px;color:{INK};line-height:1'>SAR</span>{T('تنخواہ', 26, INK, 'font-weight:700;margin-top:-4px', 1.5)}</div></div></div>

<div class='abs' style='top:690px;right:34px;left:34px'>
 <div style='display:flex;align-items:center;gap:10px'>{icon('box', 34, RED, 2.4)}{T('کام کی نوعیت', 32, RED, 'font-weight:700', 1.6)}<div style='flex:1;height:3px;background:{RED}33;margin-top:10px'></div></div>
 {duty_li}</div>
<div class='abs' style='top:924px;left:34px;right:34px;height:112px;display:flex;gap:12px'>{tiles}</div>
<div class='abs' style='top:1052px;left:34px;right:34px;height:78px;border-radius:999px;background:{YEL};display:flex;align-items:center;gap:26px;padding:0 26px;box-shadow:0 6px 14px rgba(0,0,0,.12)'>
 {T('بذمہ کمپنی:', 26, RED2, 'font-weight:700', 1.6)}{perk_li}{T('دیگر مراعات مقامی لیبر لاء کے مطابق', 20, INK, 'font-weight:700;margin-inline-start:auto', 1.6)}</div>

<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:linear-gradient(90deg,{RED2},{RED})'></div>
<div class='abs' style='top:1150px;left:0;right:0;height:60px;display:flex;align-items:center;justify-content:center;gap:18px'>
 {T('ابھی رابطہ کریں!', 34, YEL, 'font-weight:700', 1.6)}{T(f"اپنی {N('CV')} اور مکمل کاغذات واٹس ایپ کریں", 23, '#fff', 'font-weight:700', 1.7)}</div>
<div class='abs' style='top:1220px;left:26px;right:26px;height:62px;background:#fff;border-radius:999px;display:flex;align-items:center;justify-content:space-around;direction:ltr;box-shadow:0 8px 18px #0006'>{nums}</div>
<div class='abs' style='top:1294px;left:26px;right:26px;height:44px;display:flex;align-items:center;justify-content:space-between;direction:ltr'>
 <div style='display:flex;align-items:center;gap:8px'>{icon('mail', 24, YEL, 2)}<span style='font-family:Archivo;font-size:23px;font-weight:700;color:#fff'>{EMAIL}</span></div>
 <div style='display:flex;align-items:center;gap:6px'>{icon('pin', 20, YEL, 2.2)}<span style='font-family:Archivo;font-size:15px;font-weight:600;color:#FFE1E1'>{ADDRESS}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{PAPER}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Saudi-Arabia-Super-Store-Packers-v2-Urdu.png"))
