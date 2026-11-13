"""Uzbekistan — English Teachers v4, English (2026-11-13). User: the reference ad's design was good — reuse its layout
with our pictures and details. Layout follows the reference: light sky page with Samarkand madrasa, flag top right,
red URGENT HIRING ribbon with megaphone, big navy title, cream salary box + light-blue work-permit box, navy bar with
age + IELTS, yellow contact banner. Our additions: both teacher photos in big circles (uncropped people), RS Links
logo, four WhatsApp numbers, email."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

NAVY, NAVY2, RED, YEL, CREAM, SKY, INK = "#0E2A66", "#081B45", "#E3262F", "#FFD43B", "#FFF6E0", "#DCEBFF", "#0E2A66"
EMAIL = "hr@rslinksconsultants.com"


def megaphone(s):
    return (f"<svg width='{s}' height='{s}' viewBox='0 0 64 64'><path d='M6 26 v12 h10 l24 14 V12 L16 26Z' fill='#F7B731' stroke='#7A4A00' stroke-width='2'/>"
            f"<rect x='12' y='38' width='8' height='14' rx='2' fill='#C0392B'/><path d='M46 22 q8 10 0 20 M51 16 q14 16 0 32' stroke='#F7B731' stroke-width='4' fill='none' stroke-linecap='round'/></svg>")


def circle(src, d, fit, pos, bg):
    return (f"<div style='width:{d}px;height:{d}px;border-radius:50%;padding:8px;background:linear-gradient(135deg,{YEL},{RED});box-shadow:0 18px 36px rgba(8,27,69,.3)'>"
            f"<div style='width:100%;height:100%;border-radius:50%;overflow:hidden;background:{bg};border:6px solid #fff;box-sizing:border-box'>"
            f"<img src='{src}' style='width:100%;height:100%;object-fit:{fit};object-position:{pos}'></div></div>")


def build():
    man, woman, mad = (PHOTOS / "teacher_man.jpg").as_uri(), (PHOTOS / "teacher_woman.jpg").as_uri(), (PHOTOS / "uz_samarkand_madrasa.jpg").as_uri()
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:linear-gradient(180deg,#BFE0FF 0%,#EAF4FF 40%,#FFFFFF 70%)'></div>
<div class='abs' style='top:0;right:0;width:560px;height:620px;overflow:hidden;opacity:.9;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 30%)'><img src='{mad}' style='width:100%;height:100%;object-fit:cover'></div>
<div class='abs' style='top:20px;left:30px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0002'>{logo_img('logo-horizontal-light', 'width:260px;height:68px;object-position:left')}</div>
<div class='abs' style='top:20px;right:30px;filter:drop-shadow(0 6px 12px #0004)'>{flag('uzbekistan', 150, True, 'uzt4')}</div>

<div class='abs' style='top:120px;left:20px;display:flex;align-items:center'>
 <div style='transform:rotate(-12deg);margin-right:-12px;z-index:1'>{megaphone(110)}</div>
 <div style='background:linear-gradient(180deg,#F23A43,{RED});padding:10px 30px 12px 24px;clip-path:polygon(0 0,100% 0,95% 50%,100% 100%,0 100%);transform:rotate(-4deg);box-shadow:0 8px 16px #0004'>
  <span style='font:italic 400 56px Anton;color:#fff;letter-spacing:1px'>URGENT HIRING</span></div></div>
<div class='abs' style='top:258px;left:40px;width:560px;text-align:center'>
 <div style='display:flex;align-items:center;gap:14px;justify-content:center'><span style='flex:1;height:3px;background:{NAVY}'></span><span style='font:800 34px Archivo;color:{NAVY}'>for</span><span style='flex:1;height:3px;background:{NAVY}'></span></div>
 <div style='font:400 112px Anton;color:{NAVY};line-height:.95;letter-spacing:2px;margin-top:4px'>ENGLISH<br>TEACHERS</div>
 <div style='display:inline-block;margin-top:12px;background:{NAVY};border-radius:16px;padding:8px 30px'><span style='font:800 40px Archivo;color:#fff'>in </span><span style='font:400 48px Anton;color:{YEL};letter-spacing:1px'>UZBEKISTAN</span></div></div>

<div class='abs' style='top:130px;right:24px'>{circle(woman, 330, 'cover', 'center 30%', '#2B3B3A')}</div>
<div class='abs' style='top:400px;right:200px'>{circle(man, 320, 'contain', 'center', '#EEF2F5')}</div>

<div class='abs' style='top:700px;left:30px;right:30px;height:170px;display:flex;gap:20px'>
 <div style='flex:1;background:{CREAM};border-radius:22px;border:2px solid #F1DDAE;box-shadow:0 10px 22px rgba(8,27,69,.12);display:flex;align-items:center;gap:20px;padding:0 26px'>
  <span style='width:96px;height:96px;border-radius:50%;background:{NAVY};display:flex;align-items:center;justify-content:center;flex:none;font:400 56px Anton;color:{YEL}'>$</span>
  <div><div style='font:800 26px Archivo;color:{NAVY}'>Salary Starts From</div><div style='font:400 84px Anton;color:{RED};line-height:1'>$3,000</div></div></div>
 <div style='flex:1;background:{SKY};border-radius:22px;border:2px solid #BCD6F7;box-shadow:0 10px 22px rgba(8,27,69,.12);display:flex;align-items:center;gap:20px;padding:0 26px'>
  {icon('doc', 80, NAVY, 2)}<div style='border-left:3px solid {NAVY};padding-left:18px'><div style='font:800 30px Archivo;color:{NAVY}'>Direct Work Permit</div><div style='font:400 56px Anton;color:{NAVY};line-height:1'>PROVIDED</div></div></div></div>

<div class='abs' style='top:894px;left:30px;right:30px;height:130px;border-radius:22px;background:linear-gradient(90deg,{NAVY2},{NAVY});display:flex;align-items:center;box-shadow:0 10px 22px rgba(8,27,69,.25)'>
 <div style='flex:1;display:flex;align-items:center;justify-content:center;gap:18px;border-right:3px solid #ffffff44'>{icon('user', 64, '#fff', 2)}<div><div style='font:800 26px Archivo;color:#fff'>Age Limit:</div><div style='font:400 58px Anton;color:{YEL};line-height:1'>22 to 45</div></div></div>
 <div style='flex:1;display:flex;align-items:center;justify-content:center;gap:18px'>{icon('check', 64, '#fff', 2.4)}<div><div style='font:800 24px Archivo;color:#fff'>NEED IELTS SCORE</div><div style='font:400 58px Anton;color:{YEL};line-height:1'>6 BAND</div></div></div></div>

<div class='abs' style='top:1050px;left:180px;right:30px;height:100px;background:linear-gradient(90deg,{YEL},#FFC107);clip-path:polygon(4% 0,100% 0,100% 100%,0 100%);display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 10px 18px #0003'>
 <div style='font:800 24px Archivo;color:{NAVY}'>FOR MORE INFORMATION &amp; TO SEND YOUR CV</div><div style='font:400 44px Anton;color:{NAVY};letter-spacing:1px;line-height:1'>CONTACT US ON WHATSAPP</div></div>
<div class='abs' style='top:1040px;left:30px;display:flex;flex-direction:column;gap:4px;transform:rotate(-4deg)'>
 <div style='width:150px;height:30px;background:#1E5BB8;border-radius:4px;font:800 13px Archivo;color:#fff;display:flex;align-items:center;padding-left:10px'>English</div>
 <div style='width:140px;height:30px;background:#D63A3A;border-radius:4px;font:800 13px Archivo;color:#fff;display:flex;align-items:center;padding-left:10px'>Education</div>
 <div style='width:160px;height:30px;background:{NAVY};border-radius:4px;font:800 12px Archivo;color:#fff;display:flex;align-items:center;padding-left:10px'>Global Opportunities</div></div>

<div class='abs' style='top:1172px;left:0;width:1080px;height:178px;background:linear-gradient(100deg,{NAVY2},{NAVY})'></div>
<div class='abs' style='top:1172px;left:0;width:1080px;height:6px;background:{YEL}'></div>
<div class='abs' style='top:1200px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1206px;right:40px;width:380px;text-align:right'>
 <div style='font:400 40px Anton;color:{YEL};letter-spacing:1px;line-height:1.05'>APPLY NOW!</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:12px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Uzbekistan-English-Teachers-v4-English.png"))
