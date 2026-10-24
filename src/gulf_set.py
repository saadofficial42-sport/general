"""Four converted ads (2026-10-24) from the user's references (other agencies' ads + a workforce proposal; content
only, their photos/branding/licence numbers not reused, employers not named). Facts: demands/2026-10-24-gulf-set/facts.md
  1 oman      — Oman, Azad visa (Urdu)                          "passport stamp": sand page, Oman red/green sash
  2 warehouse — Saudi warehouse worker, 1500 + 300 SAR (Urdu)    "safety stripe": navy + hi-vis yellow hazard bands
  3 wood      — Saudi wood factory helper, 10 posts (Urdu)       "timber": warm wood tones, plank bands
  4 workforce — Saudi 140 warehouse operators (English)          "spec sheet": white/teal table layout
Run: python gulf_set.py [oman warehouse wood workforce]"""
import sys

from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.75: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def img(name, pos="center"):
    return f"<img src='{(PHOTOS / name).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos};display:block'>"


def nums_grid(color="#14181C", size=29):
    return "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 {size}px Anton;color:{color};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)


def page(body, bg, rtl=True):
    d = "rtl" if rtl else "ltr"
    return (f"<!doctype html><html lang='{'ur' if rtl else 'en'}' dir='{d}'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div dir='{d}' style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{bg}'>{body}</div></body></html>")


def cta_ur(top, bg, accent, sub="اپنی CV اور پاسپورٹ کاپی واٹس ایپ کریں"):
    return f"""<div class='abs' style='top:{top}px;left:0;width:1080px;height:{1350 - top}px;background:{bg}'></div>
<div class='abs' style='top:{top + 22}px;left:30px;width:600px;height:132px;background:#fff;border-radius:18px;display:grid;grid-template-columns:1fr 1fr;align-content:center;gap:10px 12px;padding:0 18px;box-sizing:border-box;box-shadow:0 8px 18px #0006;direction:ltr'>{nums_grid()}</div>
<div class='abs' style='top:{top + 12}px;right:34px;width:400px;text-align:right'>
 {T('ابھی رابطہ کریں!', 40, accent, 'font-weight:700', 1.6)}
 {T(sub.replace('CV', N('CV')), 20, '#fff', 'font-weight:700', 1.8)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr'>{icon('mail', 22, accent, 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>"""


# ------------------------------------------------------------------ 1 Oman
def oman():
    RED, GRN, SAND, INK = "#C8102E", "#008000", "#F6EEDF", "#1B1B1B"
    body = f"""
<div class='abs' style='inset:0;background:radial-gradient(circle at 80% 15%,#FFFFFF,{SAND} 55%,#EADBC0)'></div>
<svg class='abs' style='top:0;left:0' width='1080' height='1350'>
 <path d='M0 300 L1080 120 L1080 230 L0 410Z' fill='{RED}'/><path d='M0 410 L1080 230 L1080 270 L0 450Z' fill='#fff'/><path d='M0 450 L1080 270 L1080 380 L0 560Z' fill='{GRN}'/></svg>
<div class='abs' style='top:28px;right:30px;background:#fff;border-radius:16px;padding:4px 14px;box-shadow:0 8px 20px #0003'>{logo_img('logo-horizontal-light', 'width:300px;height:78px;object-position:right')}</div>
<div class='abs' style='top:26px;left:30px;filter:drop-shadow(0 8px 14px #0005)'>{flag('om', 190, True, 'om1')}</div>
<div class='abs' style='top:170px;right:60px;text-align:right'>
 <div style='display:inline-block;background:{INK};border-radius:14px;padding:0 24px 8px'>{T('فوری ضرورت برائے', 36, '#FFD54F', 'font-weight:700', 1.7)}</div>
 {T('عُمان', 150, '#fff', 'font-weight:700;margin-top:20px;text-shadow:0 8px 0 #7A0A1C,0 18px 30px #0007', 1.3)}</div>

<div class='abs' style='top:610px;left:90px;width:900px;height:430px;border-radius:30px;background:linear-gradient(160deg,#16325C,#0B1D3A);box-shadow:0 30px 60px #0006'>
 <div style='position:absolute;inset:18px;border:2px dashed #C9A54B88;border-radius:22px'></div>
 <div style='position:absolute;top:44px;left:60px;display:flex;flex-direction:column;align-items:center;gap:10px'>
  <div style='width:130px;height:130px;border-radius:50%;border:4px solid #C9A54B;display:flex;align-items:center;justify-content:center'>{icon('visa', 76, '#C9A54B', 1.6)}</div>
  <div style='font:800 22px Archivo;color:#C9A54B;letter-spacing:6px'>VISA</div>
  <div style='font:700 16px Archivo;color:#8FA3C4;letter-spacing:3px'>SULTANATE OF OMAN</div></div>
 <div style='position:absolute;top:70px;right:60px;width:470px;height:250px;border:8px solid {RED};border-radius:26px;transform:rotate(-7deg);display:flex;flex-direction:column;align-items:center;justify-content:center;background:#ffffff0d'>
  {T('آزاد ویزا', 118, '#fff', 'font-weight:700', 1.5)}
  <div style='font:800 22px Archivo;color:#FF8A8A;letter-spacing:8px;margin-top:14px'>AZAD VISA</div></div>
 <div style='position:absolute;left:60px;right:60px;bottom:36px;display:flex;align-items:center;gap:14px'>
  {icon('plane', 40, '#C9A54B', 1.8)}<div style='flex:1;border-top:3px dashed #C9A54B88'></div>
  <div style='font:400 32px Anton;color:#fff;letter-spacing:3px'>PAKISTAN → OMAN</div></div></div>

<div class='abs' style='top:1066px;left:90px;right:90px;text-align:center'>
 {T('خواہشمند حضرات ہم سے رابطہ کریں', 40, INK, 'font-weight:700', 1.8)}</div>
{cta_ur(1176, f'linear-gradient(100deg,{GRN},#005A1E)', '#FFD54F')}"""
    return page(body, SAND)


# ------------------------------------------------------------------ 2 Warehouse
def warehouse():
    NAVY, YEL, INK = "#0E1A2B", "#FFD31A", "#14181C"
    hazard = "repeating-linear-gradient(-45deg,#FFD31A 0 26px,#14181C 26px 52px)"
    perks = [("star", "بہترین ماحول", "کام کی جگہ"), ("home", "رہائش", "کمپنی کی طرف سے"), ("food", "کھانا", "کمپنی کی طرف سے"), ("bus", "ٹرانسپورٹ", "مفت")]
    perks = [p if p[0] != "star" else ("check",) + p[1:] for p in perks]
    perk = "".join(f"<div style='flex:1;background:#fff;border-radius:18px;display:flex;flex-direction:column;align-items:center;justify-content:center;border-bottom:6px solid {YEL};box-shadow:0 8px 18px #0005'>"
                   f"<span style='width:58px;height:58px;border-radius:50%;background:{NAVY};display:flex;align-items:center;justify-content:center'>{icon(ic, 32, YEL, 2.2)}</span>"
                   f"{T(a, 26, INK, 'font-weight:700;margin-top:4px', 1.8)}{T(b, 18, '#5A6577', 'font-weight:700;margin-top:8px', 1.6)}</div>" for ic, a, b in perks)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:640px;overflow:hidden'>{img('rslinks_worker_hero.png', 'center 22%')}</div>
<div class='abs' style='top:0;left:0;width:1080px;height:640px;background:linear-gradient(270deg,{NAVY}F2 0%,{NAVY}C0 42%,{NAVY}00 72%)'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:22px;background:{hazard}'></div>
<div class='abs' style='top:44px;right:30px;background:#fff;border-radius:16px;padding:4px 14px'>{logo_img('logo-horizontal-light', 'width:290px;height:74px;object-position:right')}</div>
<div class='abs' style='top:44px;left:30px;filter:drop-shadow(0 8px 14px #0007)'>{flag('saudi', 150, True, 'saw')}</div>
<div class='abs' style='top:160px;right:44px;width:560px;text-align:right'>
 {T('فوری ضرورت برائے سعودی عرب', 36, YEL, 'font-weight:700', 1.8)}
 {T('ویئر ہاؤس ورکرز', 80, '#fff', 'font-weight:700;margin-top:16px;white-space:nowrap;text-shadow:0 8px 20px #000a', 1.9)}
 <div style='font:400 44px Anton;color:#fff;letter-spacing:3px;direction:ltr;text-align:right;margin-top:14px'>WAREHOUSE <span style='color:{YEL}'>WORKERS</span></div></div>
<div class='abs' style='top:640px;left:0;width:1080px;height:22px;background:{hazard}'></div>

<div class='abs' style='top:662px;left:0;width:1080px;height:520px;background:{NAVY}'></div>
<div class='abs' style='top:696px;left:40px;right:40px;height:190px;display:flex;gap:20px'>
 <div style='flex:1.4;background:{YEL};border-radius:22px;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 10px 24px #0007'>
  {T('ماہانہ تنخواہ', 28, INK, 'font-weight:700;margin-bottom:14px', 1.6)}
  <div style='direction:ltr;display:flex;align-items:baseline;gap:10px'><span class='num' style='font-size:84px;color:{INK};line-height:1'>1500 + 300</span><span class='num' style='font-size:30px;color:{INK}'>SAR</span></div></div>
 <div style='flex:1;background:#fff;border-radius:22px;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 10px 24px #0007'>
  <span style='width:58px;height:58px;border-radius:50%;background:{NAVY};display:flex;align-items:center;justify-content:center'>{icon('user', 32, YEL, 2.2)}</span>
  {T('عمر کی حد', 24, '#5A6577', 'font-weight:700;margin-top:2px', 1.6)}{T(f"{N('21 – 35')} سال", 40, INK, 'font-weight:700;margin-top:8px', 1.6)}</div></div>
<div class='abs' style='top:914px;left:40px;right:40px;height:220px;display:flex;gap:16px'>{perk}</div>
{cta_ur(1182, f'linear-gradient(100deg,#000,{NAVY})', YEL)}"""
    return page(body, NAVY)


# ------------------------------------------------------------------ 3 Wood factory
def wood():
    WD, WD2, CRM, INK, GRN, ORG = "#5B3A1E", "#3A2412", "#FBF4E8", "#2A1C10", "#1F6B3A", "#E8952E"
    planks = "repeating-linear-gradient(180deg,#8A5A2B 0 46px,#7A4E24 46px 48px,#94643A 48px 94px,#6E4520 94px 96px)"
    perks = [("plane", "ٹکٹ"), ("home", "رہائش"), ("food", "کھانا"), ("medical", "میڈیکل"), ("shield", "سیکیورٹی")]
    perk = "".join(f"<div style='flex:1;display:flex;flex-direction:column;align-items:center;{'border-right:2px solid #E5D3B8;' if i else ''}'>"
                   f"<span style='width:62px;height:62px;border-radius:50%;background:{GRN};display:flex;align-items:center;justify-content:center'>{icon(ic, 32, '#fff', 2.2)}</span>"
                   f"{T(a, 26, INK, 'font-weight:700;margin-top:0', 1.8)}{T('کمپنی کی طرف سے', 16, '#7A6450', 'font-weight:700;margin-top:6px', 1.6)}</div>" for i, (ic, a) in enumerate(perks))
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:600px;background:{planks}'></div>
<div class='abs' style='top:40px;left:40px;width:470px;height:520px;border-radius:24px;overflow:hidden;border:8px solid {CRM};box-shadow:0 20px 40px #0008;transform:rotate(-2deg)'>{img('by_woodworking.jpg', 'center 40%')}</div>
<div class='abs' style='top:30px;right:30px;background:#fff;border-radius:16px;padding:4px 14px;box-shadow:0 8px 18px #0005'>{logo_img('logo-horizontal-light', 'width:290px;height:74px;object-position:right')}</div>
<div class='abs' style='top:140px;right:40px;width:500px;text-align:right'>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:12px;direction:ltr'>{flag('saudi', 96, True, 'saw2')}<div style='background:{ORG};border-radius:12px;padding:0 18px 6px'>{T('فوری ضرورت', 30, '#fff', 'font-weight:700', 1.6)}</div></div>
 {T('سعودی عرب', 88, CRM, 'font-weight:700;margin-top:16px;text-shadow:0 6px 16px #0008', 1.75)}
 {T('چائنیز کمپنی — لکڑی کی فیکٹری', 30, '#FFD9A0', 'font-weight:700;margin-top:18px', 1.8)}</div>
<div class='abs' style='top:600px;left:0;width:1080px;height:580px;background:{CRM}'></div>
<div class='abs' style='top:560px;right:40px;left:40px;height:120px;background:{GRN};border-radius:24px;display:flex;align-items:center;justify-content:center;gap:20px;box-shadow:0 12px 26px #0005'>
 {icon('user', 44, '#fff', 2.2)}{T('فیکٹری ہیلپر', 72, '#fff', 'font-weight:700', 1.6)}
 <div style='font:400 34px Anton;color:#C9F2D6;letter-spacing:2px;direction:ltr'>FACTORY HELPER</div></div>
<div class='abs' style='top:706px;left:40px;right:40px;height:170px;display:flex;gap:18px'>
 <div style='flex:1.6;background:linear-gradient(135deg,{WD},{WD2});border-radius:22px;display:flex;flex-direction:column;align-items:center;justify-content:center'>
  {T('ماہانہ تنخواہ', 26, '#FFD9A0', 'font-weight:700;margin-bottom:14px', 1.6)}
  <div style='direction:ltr;display:flex;align-items:baseline;gap:10px'><span class='num' style='font-size:80px;color:#fff;line-height:1'>1300 + 200</span><span class='num' style='font-size:28px;color:#FFD9A0'>SAR</span></div></div>
 <div style='flex:1;background:{ORG};border-radius:22px;display:flex;flex-direction:column;align-items:center;justify-content:center'>
  {T('آسامیاں', 28, '#fff', 'font-weight:700;margin-bottom:12px', 1.6)}<span class='num' style='font-size:84px;color:#fff;line-height:1'>10</span></div></div>
<div class='abs' style='top:896px;left:40px;right:40px;text-align:center;background:#fff;border:2px dashed #CDB48F;border-radius:18px;padding:0 20px 8px'>
 {T('کام: لکڑی کے سامان کی تیاری (فیکٹری ورک)', 30, INK, 'font-weight:700', 1.8)}</div>
<div class='abs' style='top:994px;left:40px;right:40px;height:172px;background:#fff;border-radius:22px;box-shadow:0 8px 20px #0002;display:flex;align-items:center;padding:0 10px'>{perk}</div>
{cta_ur(1182, f'linear-gradient(100deg,{WD2},{WD})', '#FFD9A0')}"""
    return page(body, CRM)


# ------------------------------------------------------------------ 4 Workforce 140
def workforce():
    TEAL, NAVY, INK, AMB = "#0E7C86", "#14213D", "#1A2332", "#F4B000"
    rows = [("PI System Operator", 6, "2,200"), ("PI Inbound Operator", 36, "1,500"), ("Forklift Operator", 7, "1,800"),
            ("PI OB Supervisor", 1, "3,000"), ("PI OB Operator", 44, "1,500"), ("FG System Operator", 3, "2,200"),
            ("FG Inbound Operator", 21, "1,500"), ("FG Outbound Supervisor", 1, "3,000"), ("FG Outbound Operator", 21, "1,500")]
    tbl = "".join(f"<div style='display:flex;align-items:center;height:46px;padding:0 22px;background:{'#fff' if i % 2 == 0 else '#EEF6F7'}'>"
                  f"<span style='width:32px;font:400 20px Anton;color:{TEAL}'>{i + 1:02d}</span><span style='flex:1;font:800 20px Archivo;color:{INK}'>{p}</span>"
                  f"<span style='width:110px;text-align:center;font:400 26px Anton;color:{NAVY}'>{q}</span>"
                  f"<span style='width:200px;text-align:right'><span style='display:inline-block;background:{AMB};border-radius:8px;padding:2px 12px;font:400 22px Anton;color:{INK}'>SAR {s}</span></span></div>"
                  for i, (p, q, s) in enumerate(rows))
    perks = [("food", "SAR 300 food allowance", "per month (or meals by agreement)"), ("home", "Accommodation", "by employer"),
             ("bus", "Transport", "by employer"), ("medical", "Medical insurance", "by employer"), ("overtime", "Overtime", "paid additionally")]
    perk = "".join(f"<div style='display:flex;align-items:center;gap:10px'><span style='width:42px;height:42px;border-radius:12px;background:{TEAL};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 24, '#fff', 2.2)}</span>"
                   f"<div style='line-height:1.15'><div style='font:800 17px Archivo;color:{INK}'>{a}</div><div style='font:600 13px Archivo;color:#5C6B78'>{b}</div></div></div>" for ic, a, b in perks)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:330px;background:linear-gradient(120deg,{NAVY},{TEAL})'></div>
<div class='abs' style='top:0;right:0;width:430px;height:330px;overflow:hidden;clip-path:polygon(18% 0,100% 0,100% 100%,0 100%)'>{img('rslinks_team_scan_x3.png', 'center 35%')}</div>
<div class='abs' style='top:28px;left:34px;background:#fff;border-radius:14px;padding:4px 12px'>{logo_img('logo-horizontal-light', 'width:270px;height:70px;object-position:left')}</div>
<div class='abs' style='top:118px;left:36px;width:620px'>
 <div style='display:flex;align-items:center;gap:12px'>{flag('saudi', 80, True, 'saw3')}<span style='font:800 18px Archivo;color:{AMB};letter-spacing:4px'>URGENT · SAUDI ARABIA</span></div>
 <div style='font:400 58px Anton;color:#fff;letter-spacing:1px;line-height:1;margin-top:10px;white-space:nowrap'>WAREHOUSE OPERATIONS</div>
 <div style='font:700 21px Archivo;color:#CFE9EC;margin-top:10px'>140 posts · Supervisors, operators &amp; forklift drivers</div></div>

<div class='abs' style='top:356px;left:40px;right:40px;border-radius:18px;overflow:hidden;box-shadow:0 12px 28px rgba(20,33,61,.18)'>
 <div style='display:flex;align-items:center;height:44px;padding:0 22px;background:{NAVY};font:800 14px Archivo;color:#fff;letter-spacing:1.5px'>
  <span style='width:32px'>#</span><span style='flex:1'>POSITION</span><span style='width:110px;text-align:center'>POSTS</span><span style='width:200px;text-align:right'>BASIC SALARY / MONTH</span></div>
 {tbl}
 <div style='display:flex;align-items:center;height:48px;padding:0 22px;background:{TEAL};font:800 18px Archivo;color:#fff'><span style='flex:1'>TOTAL</span><span style='width:110px;text-align:center;font:400 28px Anton'>140</span><span style='width:200px'></span></div></div>

<div class='abs' style='top:924px;left:40px;right:40px;height:214px;background:#fff;border-radius:18px;box-shadow:0 10px 24px rgba(20,33,61,.12);padding:14px 24px;box-sizing:border-box'>
 <div style='font:400 26px Anton;color:{NAVY};letter-spacing:1px'>BENEFITS</div>
 <div style='display:grid;grid-template-columns:repeat(3,1fr);gap:14px 18px;margin-top:10px'>{perk}</div>
 <div style='font:600 13px Archivo;color:#6A7684;margin-top:12px'>Salaries are basic, subject to final job descriptions, experience, interview and approved employment contract.</div></div>

<div class='abs' style='top:1160px;left:0;width:1080px;height:190px;background:linear-gradient(100deg,{NAVY},{TEAL})'></div>
<div class='abs' style='top:1186px;left:30px;width:600px;height:136px;background:#fff;border-radius:18px;display:grid;grid-template-columns:1fr 1fr;align-content:center;gap:10px 12px;padding:0 18px;box-sizing:border-box;box-shadow:0 8px 18px #0006'>{nums_grid()}</div>
<div class='abs' style='top:1186px;right:34px;width:390px;text-align:right'>
 <div style='font:400 38px Anton;color:{AMB};letter-spacing:1px;line-height:1.05'>APPLY NOW!</div>
 <div style='font:700 18px Archivo;color:#DDEFF1;margin-top:6px'>Send your CV on WhatsApp</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px'>{icon('mail', 22, AMB, 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div>
 <div style='font:600 12.5px Archivo;color:#BFD9DD;margin-top:8px'>{ADDRESS}</div></div>"""
    return page(body, "#F2F6F8", rtl=False)


# ------------------------------------------------------------------ 4b Workforce 140, Urdu
def workforce_ur():
    G, G2, ORG, INK, BG = "#0B6E4F", "#064530", "#F28C28", "#18221D", "#F3F1EA"
    rows = [("پی آئی سسٹم آپریٹر", "PI System Operator", 6, "2,200"), ("پی آئی اِن باؤنڈ آپریٹر", "PI Inbound Operator", 36, "1,500"),
            ("فورک لفٹ آپریٹر", "Forklift Operator", 7, "1,800"), ("پی آئی او بی سپروائزر", "PI OB Supervisor", 1, "3,000"),
            ("پی آئی او بی آپریٹر", "PI OB Operator", 44, "1,500"), ("ایف جی سسٹم آپریٹر", "FG System Operator", 3, "2,200"),
            ("ایف جی اِن باؤنڈ آپریٹر", "FG Inbound Operator", 21, "1,500"), ("ایف جی آؤٹ باؤنڈ سپروائزر", "FG Outbound Supervisor", 1, "3,000"),
            ("ایف جی آؤٹ باؤنڈ آپریٹر", "FG Outbound Operator", 21, "1,500")]
    tiles = "".join(
        f"<div style='background:#fff;border-radius:18px;box-shadow:0 6px 16px rgba(6,69,48,.14);overflow:hidden;display:flex;flex-direction:column'>"
        f"<div style='display:flex;align-items:center;justify-content:space-between;padding:0 14px;height:40px;background:{G}'>"
        f"<span style='font:800 14px Archivo;color:#CFEDE1;direction:ltr'>{en}</span>"
        f"<span style='display:flex;align-items:baseline;gap:4px'>{T('آسامیاں', 15, '#fff', 'font-weight:700', 1.4)}<span class='num' style='font-size:22px;color:#FFD9A8'>{q}</span></span></div>"
        f"<div style='flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:0 8px'>"
        f"{T(ur, 23, INK, 'font-weight:700;text-align:center', 1.75)}"
        f"<div style='direction:ltr;background:{ORG};border-radius:10px;padding:2px 12px;margin-top:2px'><span class='num' style='font-size:22px;color:#fff'>{sal}</span> <span class='num' style='font-size:14px;color:#fff'>SAR</span></div></div></div>"
        for ur, en, q, sal in rows)
    perks = [("food", "کھانا الاؤنس", f"{N(300)} ریال ماہانہ"), ("home", "رہائش", "کمپنی کی طرف سے"), ("bus", "ٹرانسپورٹ", "کمپنی کی طرف سے"),
             ("medical", "میڈیکل انشورنس", "کمپنی کی طرف سے"), ("overtime", "اوور ٹائم", "الگ سے")]
    perk = "".join(f"<div style='flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;{'border-right:2px solid #ffffff33;' if i else ''}'>"
                   f"{icon(ic, 32, '#FFD9A8', 2.2)}{T(a, 21, '#fff', 'font-weight:700', 1.7)}{T(b, 15, '#BFE6D6', 'font-weight:700;margin-top:4px', 1.6)}</div>" for i, (ic, a, b) in enumerate(perks))
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:370px;background:linear-gradient(135deg,{G},{G2})'></div>
<svg class='abs' style='top:0;left:0' width='1080' height='400'><path d='M0 340 C 300 400, 700 300, 1080 370 L1080 400 L0 400Z' fill='{BG}'/><path d='M0 330 C 300 390, 700 290, 1080 360' stroke='{ORG}' stroke-width='6' fill='none'/></svg>
<div class='abs' style='top:34px;left:40px;width:250px;height:250px;border-radius:50%;overflow:hidden;border:7px solid #fff;box-shadow:0 14px 30px #0007'>{img('rslinks_worker_hero.png', 'center 20%')}</div>
<div class='abs' style='top:22px;left:250px;width:120px;height:120px;border-radius:50%;background:{ORG};border:5px solid #fff;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 8px 18px #0006'>
 <span class='num' style='font-size:44px;color:#fff;line-height:1'>140</span>{T('آسامیاں', 18, '#fff', 'font-weight:700', 1.5)}</div>
<div class='abs' style='top:24px;right:30px;display:flex;align-items:center;gap:14px;direction:ltr'>{flag('saudi', 96, True, 'saw4')}<div style='background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:right')}</div></div>
<div class='abs' style='top:108px;right:40px;width:640px;text-align:right'>
 {T('فوری ضرورت برائے سعودی عرب', 32, '#FFD9A8', 'font-weight:700', 1.8)}
 {T('ویئر ہاؤس آپریشنز', 64, '#fff', 'font-weight:700;margin-top:4px;white-space:nowrap', 1.8)}
 {T('سپروائزرز، آپریٹرز اور فورک لفٹ ڈرائیورز', 24, '#CFEDE1', 'font-weight:700;margin-top:4px', 1.8)}</div>

<div class='abs' style='top:404px;left:34px;right:34px;display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:140px;gap:12px'>{tiles}</div>
<div class='abs' style='top:854px;left:34px;right:34px;text-align:center'>{T('تنخواہیں بنیادی ہیں، حتمی ملازمت کی تفصیل، تجربے، انٹرویو اور معاہدے کے مطابق', 17, '#5C6A62', 'font-weight:700', 1.8)}</div>
<div class='abs' style='top:910px;left:34px;right:34px;height:212px;border-radius:22px;background:linear-gradient(135deg,{G},{G2});display:flex;flex-direction:column;padding:6px 10px 10px;box-sizing:border-box'>
 {T('کمپنی کی طرف سے سہولیات', 28, '#FFD9A8', 'font-weight:700;text-align:center', 1.7)}
 <div style='flex:1;display:flex;align-items:center'>{perk}</div></div>
{cta_ur(1150, f'linear-gradient(100deg,#111,{INK})', '#FFD9A8')}"""
    return page(body, BG)


ADS = {"oman": (oman, "RS-Links-Oman-Azad-Visa-Urdu.png"),
       "warehouse": (warehouse, "RS-Links-Saudi-Arabia-Warehouse-Workers-1500-Urdu.png"),
       "wood": (wood, "RS-Links-Saudi-Arabia-Wood-Factory-Helper-Urdu.png"),
       "workforce": (workforce, "RS-Links-Saudi-Arabia-Warehouse-Operations-140-English.png"),
       "workforce_ur": (workforce_ur, "RS-Links-Saudi-Arabia-Warehouse-Operations-140-Urdu.png")}

if __name__ == "__main__":
    for k in (sys.argv[1:] or ADS):
        fn, out = ADS[k]
        print(render(fn(), out))
