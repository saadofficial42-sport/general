"""Uzbekistan — English Teachers v2, English (2026-11-13). User: v1 'ridiculous'; wants very dynamic, gradients, different
colours, both teacher photos in big prominent circles, people shown fully (no cropping of the people).
Design: "aurora" — teal→royal-blue→violet mesh gradient with glowing orbs, two large ringed circles (man photo shown
whole with contain on white; woman photo nearly square, corners only), orange-gold salary burst, glass fact chips,
diagonal white CTA. Same facts: from $3000/month, direct work permit, age 22–45, IELTS 6 band."""
import math

from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

TEAL, BLUE, VIOLET, ORG, GOLD, INK = "#0FB5B0", "#2453D6", "#6A2FD1", "#FF8A1F", "#FFD25A", "#101A3A"
EMAIL = "hr@rslinksconsultants.com"
GLASS = "background:linear-gradient(135deg,#ffffff30,#ffffff10);border:1.5px solid #ffffff55;box-shadow:0 10px 24px #0005"


def burst(size):
    c = size / 2
    pts = " ".join(f"{c + (c if i % 2 == 0 else c * .82) * math.cos(math.radians(i * 10)):.1f},{c + (c if i % 2 == 0 else c * .82) * math.sin(math.radians(i * 10)):.1f}" for i in range(36))
    return (f"<svg width='{size}' height='{size}' style='position:absolute;inset:0'><defs><radialGradient id='bg' cx='.35' cy='.3' r='.8'>"
            f"<stop offset='0' stop-color='#FFF1B0'/><stop offset='.5' stop-color='{GOLD}'/><stop offset='1' stop-color='{ORG}'/></radialGradient></defs><polygon points='{pts}' fill='url(#bg)'/></svg>")


def circle(src, d, ring, fit, pos, bg):
    return (f"<div style='width:{d}px;height:{d}px;border-radius:50%;padding:10px;background:conic-gradient({ring});box-shadow:0 24px 50px #0008'>"
            f"<div style='width:100%;height:100%;border-radius:50%;overflow:hidden;background:{bg};border:6px solid #fff;box-sizing:border-box'>"
            f"<img src='{src}' style='width:100%;height:100%;object-fit:{fit};object-position:{pos}'></div></div>")


def build():
    man, woman = (PHOTOS / "teacher_man.jpg").as_uri(), (PHOTOS / "teacher_woman.jpg").as_uri()
    chips = "".join(f"<div style='flex:1;display:flex;align-items:center;gap:14px;border-radius:20px;padding:16px 18px;{GLASS}'>"
                    f"<span style='width:58px;height:58px;border-radius:16px;background:linear-gradient(135deg,{GOLD},{ORG});display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 30, INK, 2.3)}</span>"
                    f"<div><div style='font:800 14px Archivo;color:#D9E4FF;letter-spacing:2px'>{a}</div><div style='font:400 32px Anton;color:#fff;line-height:1.05'>{b}</div></div></div>"
                    for ic, a, b in [("visa", "WORK PERMIT", "DIRECT"), ("user", "AGE LIMIT", "22 – 45 YRS"), ("doc", "IELTS SCORE", "6.0 BAND")])
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:{INK};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:radial-gradient(circle at 10% 0%,{TEAL} 0,transparent 45%),radial-gradient(circle at 100% 30%,{VIOLET} 0,transparent 50%),linear-gradient(160deg,{BLUE},#162C8C 55%,#1B0F5C)'></div>
<div class='abs' style='top:560px;left:-120px;width:420px;height:420px;border-radius:50%;background:radial-gradient(circle,#0FB5B055,transparent 70%)'></div>
<div class='abs' style='top:-100px;right:-80px;width:460px;height:460px;border-radius:50%;background:radial-gradient(circle,#FF8A1F44,transparent 70%)'></div>
<div class='abs' style='inset:0;background:repeating-linear-gradient(125deg,#ffffff06 0 50px,transparent 50px 100px)'></div>
<div class='abs' style='top:28px;left:36px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 8px 18px #0005'>{logo_img('logo-horizontal-light', 'width:270px;height:70px;object-position:left')}</div>
<div class='abs' style='top:30px;right:40px;filter:drop-shadow(0 6px 12px #0007)'>{flag('uzbekistan', 130, True, 'uzt2')}</div>
<div class='abs' style='top:122px;left:44px;width:560px'>
 <div style='display:inline-block;background:linear-gradient(90deg,{ORG},{GOLD});color:{INK};font:800 19px Archivo;letter-spacing:4px;padding:8px 16px;border-radius:999px'>URGENT HIRING</div>
 <div style='font:400 100px Anton;line-height:.92;letter-spacing:2px;margin-top:14px;background:linear-gradient(180deg,#fff 0%,#fff 55%,#BFE9FF 100%);-webkit-background-clip:text;color:transparent;filter:drop-shadow(0 8px 0 #0B1F6E)'>ENGLISH<br>TEACHERS</div>
 <div style='font:400 52px Anton;letter-spacing:6px;margin-top:10px;background:linear-gradient(90deg,{GOLD},{ORG});-webkit-background-clip:text;color:transparent'>IN UZBEKISTAN</div></div>

<div class='abs' style='top:150px;right:30px'>{circle(woman, 400, f"{GOLD},{ORG},{VIOLET},{TEAL},{GOLD}", 'cover', 'center 30%', '#2B3B3A')}</div>
<div class='abs' style='top:470px;left:30px'>{circle(man, 470, f"{TEAL},{BLUE},{GOLD},{TEAL}", 'contain', 'center', '#F3F5F7')}</div>

<div class='abs' style='top:600px;right:40px;width:310px;height:310px;transform:rotate(-8deg)'>{burst(310)}
 <div style='position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center'>
  <div style='font:800 17px Archivo;color:{INK};letter-spacing:3px'>SALARY FROM</div>
  <div style='font:400 92px Anton;color:{INK};line-height:.95'>$3,000</div>
  <div style='font:800 18px Archivo;color:{INK};letter-spacing:3px'>PER MONTH</div></div></div>

<div class='abs' style='top:948px;left:36px;right:36px;display:flex;gap:14px'>{chips}</div>

<div class='abs' style='top:1080px;left:-30px;width:1140px;height:90px;background:linear-gradient(90deg,{ORG},{GOLD});transform:rotate(-2deg);display:flex;align-items:center;justify-content:center;gap:16px;box-shadow:0 12px 24px #0006'>
 {icon('doc', 40, INK, 2.2)}<span style='font:400 40px Anton;color:{INK};letter-spacing:1.5px'>SEND YOUR CV &amp; IELTS RESULT ON WHATSAPP</span></div>

<div class='abs' style='top:1180px;left:0;width:1080px;height:170px;background:#fff'></div>
<div class='abs' style='top:1206px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1206px;right:40px;width:380px;text-align:right'>
 <div style='font:400 44px Anton;letter-spacing:1px;line-height:1.05;background:linear-gradient(90deg,{BLUE},{VIOLET});-webkit-background-clip:text;color:transparent'>CONTACT US NOW!</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:12px'>{icon('mail', 22, BLUE, 2)}<span style='font:800 20px Archivo;color:{INK}'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{BLUE}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Uzbekistan-English-Teachers-v2-English.png"))
