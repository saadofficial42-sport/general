"""Uzbekistan — English Teachers, English (2026-11-13). Converted from another agency's ad (content only): salary starts
from $3000; direct work permit provided; age 22–45; IELTS 6 band required. Design: "chalkboard" — deep slate-green
board with chalk-white title and dashed chalk lines, wooden frame top/bottom, Samarkand madrasa photo in a polaroid,
gold salary ribbon, three pinned note cards, navy CTA. No teacher photo available yet (flagged)."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

BOARD, BOARD2, WOOD, WOOD2, GOLD, CHALK, NAVY = "#1F3B33", "#152B25", "#A8743F", "#7A512A", "#F5C445", "#F4F1E8", "#0D2347"
EMAIL = "hr@rslinksconsultants.com"


def build():
    photo = (PHOTOS / "uz_samarkand_madrasa.jpg").as_uri()
    note = lambda ic, a, b, rot, bg: (f"<div style='flex:1;background:{bg};border-radius:6px;transform:rotate({rot}deg);box-shadow:0 10px 18px #0007;display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative'>"
                                      f"<span style='position:absolute;top:-10px;width:22px;height:22px;border-radius:50%;background:#D62828;box-shadow:0 3px 6px #0006'></span>"
                                      f"{icon(ic, 40, NAVY, 2.2)}<div style='font:800 15px Archivo;color:#4A4A4A;letter-spacing:2px;margin-top:8px'>{a}</div><div style='font:400 38px Anton;color:{NAVY};line-height:1.05;text-align:center'>{b}</div></div>")
    notes = note('visa', 'WORK PERMIT', 'DIRECT<br>PROVIDED', -3, '#FFF7C2') + note('user', 'AGE LIMIT', '22 – 45<br>YEARS', 2, '#D8F0FF') + note('doc', 'IELTS SCORE', '6.0<br>BAND', -2, '#FFE0E6')
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:repeating-linear-gradient(90deg,{WOOD} 0 80px,{WOOD2} 80px 83px)'></div>
<div class='abs' style='top:24px;left:24px;right:24px;bottom:206px;border-radius:14px;background:radial-gradient(circle at 30% 30%,#2C5246,{BOARD} 50%,{BOARD2});box-shadow:inset 0 0 40px #0008'></div>
<div class='abs' style='top:50px;left:56px;background:#fff;border-radius:12px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:260px;height:68px;object-position:left')}</div>
<div class='abs' style='top:52px;right:56px;filter:drop-shadow(0 6px 10px #0007)'>{flag('uzbekistan', 120, True, 'uzt')}</div>
<div class='abs' style='top:150px;left:60px;width:560px'>
 <div style='font:800 20px Archivo;color:{GOLD};letter-spacing:5px'>URGENT HIRING · UZBEKISTAN</div>
 <div style='font:400 112px Anton;color:{CHALK};line-height:.95;letter-spacing:2px;margin-top:10px;text-shadow:0 0 2px #fff8'>ENGLISH<br>TEACHERS</div>
 <div style='width:380px;border-top:4px dashed #F4F1E899;margin-top:16px'></div>
 <div style='font:700 24px Archivo;color:#DCE7E0;margin-top:14px;line-height:1.35'>Teach English in Uzbekistan<br>with a direct work permit</div></div>
<div class='abs' style='top:150px;right:60px;width:360px;height:420px;background:#fff;padding:14px 14px 0;box-sizing:border-box;transform:rotate(4deg);box-shadow:0 18px 34px #000a'>
 <div style='width:100%;height:340px;overflow:hidden'><img src='{photo}' style='width:100%;height:100%;object-fit:cover'></div>
 <div style='font:400 24px Anton;color:{NAVY};text-align:center;letter-spacing:2px;line-height:2.4'>SAMARKAND · UZBEKISTAN</div></div>

<div class='abs' style='top:610px;left:60px;right:60px;height:150px;background:linear-gradient(135deg,#FFE27A,{GOLD} 55%,#D99A12);clip-path:polygon(3% 0,100% 0,97% 100%,0 100%);display:flex;align-items:center;justify-content:center;gap:26px;box-shadow:0 14px 28px #0008'>
 {icon('money', 56, NAVY, 2)}<div><div style='font:800 20px Archivo;color:{NAVY};letter-spacing:4px'>SALARY STARTS FROM</div>
 <div style='font:400 96px Anton;color:{NAVY};line-height:.95'>$3,000 <span style='font-size:36px'>/ MONTH</span></div></div></div>

<div class='abs' style='top:810px;left:70px;right:70px;height:270px;display:flex;gap:28px'>{notes}</div>

<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:{NAVY};border-top:6px solid {GOLD}'></div>
<div class='abs' style='top:1180px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1176px;right:40px;width:380px;text-align:right'>
 <div style='font:400 40px Anton;color:{GOLD};letter-spacing:1px;line-height:1.05'>CONTACT US NOW!</div>
 <div style='font:700 18px Archivo;color:#C9D3E6;margin-top:6px'>Send your CV &amp; IELTS result on WhatsApp</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{WOOD}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Uzbekistan-English-Teachers-English.png"))
