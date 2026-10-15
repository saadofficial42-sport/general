"""Belarus factory workers (2026-10-15). Source: user demand text (visa-on-arrival procedure at Minsk
airport) + a sample special work permit (Заводской рабочий / factory worker, employer in Minsk).
The permit image contains a third person's personal data and is NOT used in the ad. Urdu only."""
from common import C, PHOTOS, WHATSAPP, flag, icon, logo_img, page, render, whatsapp_icon
from style_corporate_grid import T

RED, GREEN, INK, GOLD = "#C8102E", "#00843D", "#14161C", "#F0B443"
PHONES = ["+92 317 0363690", WHATSAPP]
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"


def ph(name, w, h, r=24, b=6, pos="center"):
    return (f"<div style='width:{w}px;height:{h}px;border-radius:{r}px;overflow:hidden;border:{b}px solid #fff;box-shadow:0 12px 28px #0007;flex:none'>"
            f"<img src='{(PHOTOS / (name + '.png')).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos};display:block'></div>")


def build():
    f = T(True)
    steps = [
        ("doc", "ورک پرمٹ", f"کمپنی ورک پرمٹ منسک ایئرپورٹ کے ویزا آفس میں جمع کرواتی ہے اور مہر شدہ کاپی آپ کو بھیجتی ہے"),
        ("plane", "براہِ راست پرواز", f"استنبول، دبئی یا باکو کے راستے سیدھا منسک {N('(MSQ)')} پہنچیں"),
        ("visa", "ایئرپورٹ پر ویزا", f"پاسپورٹ کنٹرول سے پہلے قونصلر سینٹر سے {N('D')} ٹائپ ورک ویزا حاصل کریں"),
    ]
    step_html = "".join(
        f"<div style='flex:1;background:#fff;border-radius:20px;box-shadow:0 8px 20px rgba(20,22,28,.14);padding:8px 16px 10px;position:relative;border-top:7px solid {GREEN if i != 1 else RED}'>"
        f"<div style='display:flex;align-items:center;gap:10px'>"
        f"<div class='num' style='width:44px;height:44px;border-radius:50%;background:{INK};color:{GOLD};font-size:26px;line-height:44px;text-align:center;flex:none'>{i + 1}</div>"
        f"<div style='width:44px;height:44px;border-radius:50%;background:{GREEN if i != 1 else RED};display:flex;align-items:center;justify-content:center;flex:none' class='{'mir' if ic == 'plane' else ''}'>{icon(ic, 24)}</div>"
        f"{f.txt(t, 0, 26, INK, 'font-weight:700', 1.6)}</div>"
        f"{f.txt(d, 0, 18, '#3A4250', 'font-weight:600;margin-top:4px', 1.85)}</div>"
        for i, (ic, t, d) in enumerate(steps))
    docs = [("idcard", f"پاسپورٹ (کم از کم {N(2)} خالی صفحات، واپسی کے بعد {N('90+')} دن کی میعاد)"),
            ("camera", f"ویزا فارم اور تصویر {N('35×45 mm')}"),
            ("medical", f"میڈیکل انشورنس (کم از کم {N('€10,000')} — ایئرپورٹ پر بھی دستیاب)"),
            ("money", "قیام کے اخراجات کے لیے مناسب رقم کا ثبوت"),
            ("visa", f"ویزا فیس نقد: {N('€225')} یا {N('€450')} (قومیت کے مطابق)")]
    doc_html = "".join(
        f"<div style='display:flex;align-items:center;gap:12px;margin-top:4px'>"
        f"<div style='width:38px;height:38px;border-radius:50%;background:{GREEN};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 21)}</div>"
        f"{f.txt(s, 0, 21, INK, 'font-weight:600', 1.75)}</div>" for ic, s in docs)
    nums = "".join(f"<div class='num' style='display:block;font-size:46px;color:{INK};line-height:1.06'>{n}</div>" for n in PHONES)
    body = f"""<div class='ur-on'>
<div class='abs' style='top:0;left:0;width:1080px;height:140px;background:#fff'></div>
<div class='abs' style='top:10px;right:26px;width:480px;height:120px'>{logo_img('logo-horizontal-light', 'width:480px;height:120px;object-position:right')}</div>
<div class='abs' style='top:20px;left:30px;display:flex;align-items:center;gap:18px'>
 <div style='filter:drop-shadow(0 4px 8px #0004)'>{flag('by', 170, True, 'hfby')}</div>
 <div style='background:{RED};border-radius:12px;padding:0 18px 8px;box-shadow:0 4px 10px #0003'>{f.head('فوری ضرورت', 0, 30, '#fff')}</div></div>
<div class='abs' style='top:140px;left:0;width:1080px;height:8px;background:linear-gradient(90deg,{RED} 0 66%,{GREEN} 66% 100%)'></div>

<div class='abs' style='top:148px;left:0;width:1080px;height:430px;background:linear-gradient(135deg,{INK},#2A1418)'></div>
<svg class='abs' style='left:0;top:148px' width='1080' height='430'><circle cx='560' cy='430' r='240' fill='#ffffff08'/>
 <path d='M0 430 L460 430 L520 0 L470 0Z' fill='{RED}' opacity='.18'/><path d='M500 430 L530 430 L590 0 L560 0Z' fill='{GREEN}' opacity='.35'/></svg>
<div class='abs' style='top:170px;left:36px'>{ph('rslinks_worker_pack', 400, 386, 26, 7)}</div>
<div class='abs' style='top:162px;right:36px;width:560px;text-align:right'>
 {f.txt('یورپ میں روزگار کا سنہری موقع', 0, 28, GOLD, 'font-weight:700', 1.7)}
 {f.txt('بیلاروس', 0, 88, '#fff', 'font-weight:700;margin-top:4px;padding-right:18px', 1.4)}
 {f.txt('فیکٹری ورکرز', 0, 58, GOLD, 'font-weight:700;margin-top:10px', 1.5)}
 <div style='font-family:Anton;font-size:30px;color:#D9C9CC;letter-spacing:2px;direction:ltr;margin-top:6px'>FACTORY WORKERS · BELARUS</div>
 <div style='display:inline-flex;align-items:center;gap:10px;margin-top:14px;background:{GREEN};border-radius:14px;padding:0 18px 6px'>
  {icon('doc', 26, '#fff', 2.2)}{f.txt('ورک پرمٹ کی بنیاد پر • منسک ایئرپورٹ پر ویزا', 0, 22, '#fff', 'font-weight:700', 1.6)}</div></div>

<div class='abs' style='top:590px;right:36px;display:flex;align-items:center;gap:10px'>
 <div style='width:8px;height:30px;background:{RED};border-radius:4px'></div>{f.head('ویزا کا طریقہ کار', 0, 30, INK)}</div>
<div class='abs' style='top:646px;left:30px;right:30px;height:176px;display:flex;gap:14px' data-check='steps'>{step_html}</div>

<div class='abs' style='top:834px;left:30px;right:30px;height:284px;background:#fff;border-radius:22px;box-shadow:0 8px 20px rgba(20,22,28,.12);padding:6px 22px;border-inline-start:8px solid {GREEN}' data-check='docs'>
 {f.head('ایئرپورٹ پر ساتھ رکھیں', 0, 26, GREEN)}{doc_html}</div>

<div class='abs' style='top:1130px;left:30px;right:30px;height:62px;border-radius:16px;background:{RED};display:flex;align-items:center;justify-content:center;gap:12px' data-check='warn'>
 {icon('shield', 30, '#fff', 2.4)}{f.txt('اہم: روس کے راستے سفر نہ کریں — روس سے آنے پر ایئرپورٹ ویزا نہیں ملتا', 0, 23, '#fff', 'font-weight:700', 1.6)}</div>

<div class='abs' style='top:1206px;left:0;width:1080px;height:144px;background:linear-gradient(100deg,{INK},#3A0F17);border-top:6px solid {GOLD}'></div>
<div class='abs' style='top:1206px;height:144px;right:30px;width:500px;display:flex;flex-direction:column;justify-content:center;text-align:right'>
 {f.head('ابھی رابطہ کریں!', 0, 34, GOLD, 'line-height:1.5')}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:6px;direction:ltr'>{icon('mail', 24, GOLD, 2)}
  <span style='font-family:Archivo;font-size:23px;font-weight:700;color:#fff'>{EMAIL}</span></div></div>
<div class='abs' style='top:1220px;left:30px;height:116px;background:#fff;border-radius:24px;display:flex;align-items:center;gap:14px;padding:0 26px 0 14px;box-shadow:0 6px 16px #0006;direction:ltr'>
 {whatsapp_icon(68)}<div>{nums}</div></div>
</div>"""
    css = (".canvas{font-family:'Nastaliq',serif;background:#F3F1EE}.ur-on .t{font-family:'Nastaliq',serif}.mir svg{transform:scaleX(-1)}"
           ".num{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}")
    return page(body, css, rtl=True)


if __name__ == "__main__":
    from common import overflow_report
    h = build(); print(overflow_report(h)); print(render(h, "RS-Links-Belarus-Factory-Workers-Urdu.png"))
