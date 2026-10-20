"""Uzbekistan factory workers — v5 English (2026-10-19, user request): same content and design as uzbekistan_v5.py
(Urdu), mirrored for left-to-right reading. Facts: demands/2026-10-17-uzbekistan-factory (B-2 removed, three numbers)."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

TEAL, DEEP, BLUE, GRN, GOLD, INK = "#0A7E9C", "#06324A", "#0099B5", "#1EB53A", "#FFC83D", "#0B2238"
EMAIL = "hr@rslinksconsultants.com"
F = lambda s, px, c, w=700, extra="": f"<div style='font:{w} {px}px Archivo;color:{c};line-height:1.2;{extra}'>{s}</div>"
A = lambda s, px, c, extra="": f"<div style='font:400 {px}px Anton;color:{c};letter-spacing:1px;line-height:1.05;{extra}'>{s}</div>"


def build():
    hero_photo = (PHOTOS / "rslinks_worker_pack_x3.png").as_uri()
    stats = [("user", "50", "Posts"), ("clock", "10 Hours", "Working hours"), ("calendar", "21 – 35", "Age limit"),
             ("doc", "30 – 35 Days", "Processing time")]
    chips = "".join(f"<div style='flex:1;background:#fff;border-radius:18px;box-shadow:0 6px 14px rgba(6,50,74,.18);display:flex;flex-direction:column;align-items:center;justify-content:center;border-bottom:5px solid {BLUE}'>"
                    f"<div style='width:46px;height:46px;border-radius:50%;background:{TEAL};display:flex;align-items:center;justify-content:center'>{icon(ic, 25, '#fff', 2.3)}</div>"
                    f"{A(v, 28, INK, 'margin-top:8px')}{F(l, 16, '#4A6070', 600, 'margin-top:4px')}</div>" for ic, v, l in stats)
    work = ["General factory work", "Packaging", "Store work (ordering)", "Cleaning goods &amp; materials", "Production line work"]
    work_li = "".join(f"<div style='display:flex;align-items:center;gap:12px;padding:12px 0;border-bottom:1px dashed #C9DCE5'>"
                      f"<span style='width:34px;height:34px;border-radius:50%;background:{TEAL};color:#fff;font:400 19px Anton;display:flex;align-items:center;justify-content:center;flex:none'>{i + 1}</span>"
                      f"{F(w, 24, INK, 800)}</div>" for i, w in enumerate(work))
    fac = [("home", "Free accommodation"), ("bus", "Free transport"), ("medical", "Free medical"), ("food", "Free food"), ("gear", "Other facilities by the company")]
    fac_li = "".join(f"<div style='display:flex;align-items:center;gap:12px;padding:12px 0;border-bottom:1px dashed #CBE7D2'>"
                     f"<span style='width:34px;height:34px;border-radius:50%;background:{GRN};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 19, '#fff', 2.4)}</span>"
                     f"{F(w, 24, INK, 800)}</div>" for ic, w in fac)
    card = lambda title, color, body: (f"<div style='flex:1;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 8px 20px rgba(6,50,74,.14)'>"
                                       f"<div style='background:linear-gradient(90deg,{color},{color}cc);padding:12px 20px'>{A(title, 32, '#fff')}</div>"
                                       f"<div style='padding:2px 20px 8px'>{body}</div></div>")
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'><span style='line-height:0'>{whatsapp_icon(28)}</span><span style='font:400 28px Anton;color:{INK};line-height:1.2;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:150px;background:#fff'></div>
<div class='abs' style='top:20px;left:26px'>{logo_img('logo-horizontal-light', 'width:420px;height:108px;object-position:left')}</div>
<div class='abs' style='top:28px;right:26px;display:flex;align-items:center;gap:16px'>
 <div style='background:linear-gradient(135deg,#E53935,#B71C1C);border-radius:14px;padding:12px 22px;box-shadow:0 6px 14px #0004;display:flex;align-items:center;gap:10px'>{icon('megaphone', 30, '#fff', 2.2)}{A('URGENT HIRING', 32, '#fff')}</div>
 <div style='filter:drop-shadow(0 4px 8px #0004)'>{flag('uzbekistan', 160, True, 'uz5e')}</div></div>
<div class='abs' style='top:150px;left:0;width:1080px;height:430px;background:linear-gradient(225deg,{TEAL},{DEEP})'></div>
<svg class='abs' style='left:0;top:150px' width='1080' height='430'><circle cx='100' cy='40' r='200' fill='#ffffff0c'/><circle cx='440' cy='430' r='120' fill='#ffffff08'/>
 <path d='M0 390 C 380 450, 780 360, 1080 400 L1080 430 L0 430Z' fill='{GOLD}'/><path d='M0 402 C 380 462, 780 372, 1080 412 L1080 430 L0 430Z' fill='#EEF5F8'/></svg>
<div class='abs' style='top:170px;right:30px;width:400px;height:360px;border-radius:200px 200px 26px 26px;overflow:hidden;border:6px solid #fff;box-shadow:0 14px 30px #0007'>
 <img src='{hero_photo}' style='width:100%;height:100%;object-fit:cover;object-position:55% 35%'></div>
<div class='abs' style='top:186px;left:40px;width:590px'>
 {F('URGENTLY REQUIRED', 26, GOLD, 800, 'letter-spacing:3px')}
 {A('FACTORY<br>WORKERS', 96, '#fff', 'margin-top:10px;line-height:.98')}
 <div style='display:inline-flex;align-items:center;gap:8px;margin-top:18px;background:#fff;border-radius:999px;padding:8px 22px'>{icon('pin', 26, '#E53935', 2.4)}{F('Tashkent, Uzbekistan', 26, INK, 800)}</div>
 {F('A strong step towards a better future', 22, '#DCEFF6', 700, 'margin-top:12px')}</div>
<div class='abs' style='top:592px;left:30px;right:30px;height:132px;display:flex;gap:12px'>
 <div style='flex:1.35;border-radius:22px;background:radial-gradient(circle at 30% 20%,#FFE38A,{GOLD} 55%,#E0A21A);box-shadow:0 8px 18px rgba(0,0,0,.2);display:flex;flex-direction:column;align-items:center;justify-content:center'>
  <div style='display:flex;align-items:baseline;gap:6px'><span style='font:400 66px Anton;color:{INK};line-height:1'>$550</span><span style='font:400 24px Anton;color:{INK}'>USD</span></div>
  {F('Monthly salary', 20, INK, 800, 'margin-top:4px')}</div>{chips}</div>
<div class='abs' style='top:748px;left:30px;right:30px;display:flex;gap:16px'>{card('JOB DETAILS', TEAL, work_li)}{card('FACILITIES', '#1A9E46', fac_li)}</div>
<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:linear-gradient(250deg,{DEEP},{TEAL})'></div>
<svg class='abs' style='left:0;top:1138px' width='1080' height='30'><path d='M0 6 C 380 24, 780 0, 1080 30 L0 30Z' fill='{GOLD}'/></svg>
<div class='abs' style='top:1166px;right:26px;height:166px;background:#fff;border-radius:22px;display:flex;align-items:center;padding:0 20px;box-shadow:0 8px 18px #0006'><div style='display:flex;flex-direction:column;gap:2px'>{nums}</div></div>
<div class='abs' style='top:1178px;left:34px;width:560px'>
 {A('CONTACT US NOW!', 44, GOLD)}
 {F('For more information, contact us on WhatsApp', 20, '#fff', 700, 'margin-top:10px')}
 <div style='display:flex;align-items:center;gap:8px;margin-top:10px'>{icon('mail', 24, GOLD, 2)}<span style='font:800 23px Archivo;color:#fff'>{EMAIL}</span></div>
 {F('We are with you for a better future', 18, '#BFE3EE', 600, 'margin-top:10px')}</div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#EEF5F8'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Uzbekistan-Factory-Workers-v5-English.png"))
