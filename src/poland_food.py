"""Poland — Food & Mushroom factory workers, English (2026-11-12). Converted from another agency's ad (content only).
Kept: PKR 4,00,000–4,50,000 / month; Food & Mushroom factories (Schengen); sandwich making, mushroom sorting,
unloading & receiving, sorting & packing; age 21–55; matric + good English conversation; free accommodation & medical;
visa fee, protector & air ticket included; family may join after residence permit (subject to Polish rules).
Dropped as unverifiable promises: "guaranteed job upon arrival", "citizenship after 4 years", "no hidden charges",
"high success rate", "new immigration rules 2026 / easy appointments", "affordable cost of living".
Design: "fresh market" — white page, crimson diagonal header with Polish flag, 2x2 labelled photo grid with crimson
tags, giant salary ribbon, green-tick requirement list, 'included' trio, crimson CTA."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

RED, RED2, GRN, INK, SOFT = "#DC143C", "#8E0D26", "#1E8A4C", "#1A1A24", "#F6F4F2"
EMAIL = "hr@rslinksconsultants.com"


def build():
    tile = lambda f, t: (f"<div style='position:relative;border-radius:18px;overflow:hidden;box-shadow:0 8px 18px rgba(0,0,0,.15)'>"
                         f"<img src='{(PHOTOS / f).as_uri()}' style='width:100%;height:100%;object-fit:cover'>"
                         f"<span style='position:absolute;left:0;bottom:0;background:{RED};color:#fff;font:400 21px Anton;letter-spacing:1px;padding:5px 14px;border-top-right-radius:12px'>{t}</span></div>")
    grid = tile('pl_sandwich.jpg', 'SANDWICH MAKING') + tile('pl_mushroom.jpg', 'MUSHROOM SORTING') + tile('pl_unloading.jpg', 'UNLOADING &amp; RECEIVING') + tile('pl_packing.jpg', 'SORTING &amp; PACKING')
    req = [("user", "Age 21 – 55 years"), ("doc", "Matric (minimum) + good spoken English"), ("home", "Free accommodation &amp; medical"),
           ("family", "Family may join after residence permit*"), ("plane", "Schengen visa: travel within Schengen countries")]
    req_li = "".join(f"<div style='display:flex;align-items:center;gap:12px;padding:10px 0;border-bottom:1px dashed #E2D9D6'>"
                     f"<span style='width:44px;height:44px;border-radius:50%;background:{GRN};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 24, '#fff', 2.2)}</span>"
                     f"<span style='font:800 19px Archivo;color:{INK};line-height:1.2'>{t}</span></div>" for ic, t in req)
    inc = [("visa", "VISA FEE"), ("shield", "PROTECTOR"), ("plane", "AIR TICKET")]
    inc_li = "".join(f"<div style='flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px'>"
                     f"<span style='width:58px;height:58px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center'>{icon(ic, 30, RED, 2.2)}</span>"
                     f"<span style='font:400 22px Anton;color:#fff;letter-spacing:1px'>{t}</span><span style='font:800 13px Archivo;color:#FFD3DB;letter-spacing:2px'>INCLUDED</span></div>" for ic, t in inc)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:300px;background:linear-gradient(120deg,{RED},{RED2});clip-path:polygon(0 0,100% 0,100% 82%,0 100%)'></div>
<div class='abs' style='top:28px;left:36px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:270px;height:70px;object-position:left')}</div>
<div class='abs' style='top:26px;right:40px;filter:drop-shadow(0 6px 12px #0006)'>{flag('pl', 140, True, 'plf')}</div>
<div class='abs' style='top:118px;left:40px'>
 <div style='font:800 19px Archivo;color:#FFD3DB;letter-spacing:5px'>SCHENGEN · EUROPE</div>
 <div style='font:400 96px Anton;color:#fff;letter-spacing:2px;line-height:1'>JOBS IN POLAND</div>
 <div style='font:700 24px Archivo;color:#fff;margin-top:6px'>Food &amp; Mushroom Factories</div></div>

<div class='abs' style='top:290px;left:36px;right:36px;height:110px;border-radius:20px;background:#fff;box-shadow:0 14px 30px rgba(142,13,38,.22);border:3px solid {RED};display:flex;align-items:center;justify-content:center;gap:20px'>
 <span style='font:800 18px Archivo;color:{RED};letter-spacing:3px'>SALARY</span>
 <span style='font:400 64px Anton;color:{INK};letter-spacing:1px'>PKR 4,00,000 – 4,50,000</span>
 <span style='font:800 16px Archivo;color:#6B6B76;letter-spacing:2px'>PER MONTH</span></div>

<div class='abs' style='top:428px;left:36px;width:620px;height:500px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:12px'>{grid}</div>
<div class='abs' style='top:428px;right:36px;width:370px;height:500px;background:{SOFT};border-radius:20px;padding:10px 20px;box-sizing:border-box;border-top:6px solid {GRN}'>
 <div style='font:400 28px Anton;color:{GRN};letter-spacing:1px'>REQUIREMENTS &amp; BENEFITS</div>{req_li}
 <div style='font:600 12.5px Archivo;color:#6B6B76;margin-top:10px'>*Subject to Polish immigration rules.</div></div>

<div class='abs' style='top:952px;left:36px;right:36px;height:170px;border-radius:22px;background:linear-gradient(120deg,{RED2},{RED});display:flex;align-items:center;padding:0 10px'>
 <div style='width:230px;font:400 34px Anton;color:#fff;letter-spacing:1px;line-height:1.05;padding-left:16px'>PACKAGE<br>INCLUDES</div>{inc_li}</div>

<div class='abs' style='top:1146px;left:0;width:1080px;height:204px;background:{INK}'></div>
<div class='abs' style='top:1146px;left:0;width:1080px;height:8px;display:flex'><div style='flex:1;background:#fff'></div><div style='flex:1;background:{RED}'></div></div>
<div class='abs' style='top:1182px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1180px;right:40px;width:380px;text-align:right'>
 <div style='font:400 42px Anton;color:#fff;letter-spacing:1px;line-height:1.05'>APPLY NOW!</div>
 <div style='font:700 18px Archivo;color:#C9C9D2;margin-top:6px'>Send your CV on WhatsApp</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Poland-Food-Mushroom-Factories-English.png"))
