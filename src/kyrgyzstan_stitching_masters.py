"""Kyrgyzstan — Stitching Masters, English (2026-11-16). User (voice note): stitching masters; salary $500; food &
accommodation by company; 1 year ("visa" dropped per the no-visa rule -> "1-year duration"); 15–20 working days
processing, candidate flies within that period. Partner / rate not given yet.
Design: "golden sun spotlight" — deep crimson-to-charcoal page, Kyrgyz-flag golden sun rays radiating behind a big
circular hero photo of a stitching master at a JUKI machine, gold salary bar, four dark glass fact tiles, two small
sewing photos, gold CTA, charcoal footer with all six numbers."""
import math

from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

RED, RED2, CH, GOLD, GOLD2, INK = "#E8112D", "#8E0A1C", "#17110F", "#FFC72C", "#FFE27A", "#17110F"
EMAIL = "hr@rslinksconsultants.com"
GLASS = "background:linear-gradient(135deg,#ffffff1f,#ffffff08);border:1.5px solid #ffffff33"


def rays(size, n=40):
    c = size / 2
    p = ""
    for i in range(n):
        a1, a2 = math.radians(i * 360 / n), math.radians(i * 360 / n + 360 / n / 2)
        p += f"<polygon points='{c},{c} {c + c * math.cos(a1):.1f},{c + c * math.sin(a1):.1f} {c + c * math.cos(a2):.1f},{c + c * math.sin(a2):.1f}' fill='{GOLD}' opacity='.22'/>"
    return f"<svg width='{size}' height='{size}' style='position:absolute;inset:0'>{p}</svg>"


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    facts = [("home", "Food &amp; Stay", "By the company"), ("calendar", "1 Year", "Duration"), ("plane", "15 – 20", "Working days to fly")]
    tiles = "".join(f"<div style='flex:1;border-radius:18px;padding:14px 10px;{GLASS};display:flex;flex-direction:column;align-items:center;text-align:center;gap:6px'>"
                    f"<span style='width:54px;height:54px;border-radius:50%;background:{GOLD};display:flex;align-items:center;justify-content:center'>{icon(ic, 28, INK, 2.3)}</span>"
                    f"<div style='font:400 34px Anton;color:#fff;line-height:1'>{v}</div><div style='font:700 17px Archivo;color:#F3D7D9'>{l}</div></div>" for ic, v, l in facts)
    small = lambda f, pos: f"<div style='flex:1;height:200px;border-radius:16px;overflow:hidden;border:4px solid {GOLD};box-shadow:0 12px 22px #0008'><img src='{P(f)}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'></div>"
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:radial-gradient(circle at 72% 28%,{RED} 0%,{RED2} 38%,{CH} 78%)'></div>
<div class='abs' style='top:-150px;left:330px;width:900px;height:900px'>{rays(900)}</div>
<div class='abs' style='top:24px;left:30px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0006'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:left')}</div>
<div class='abs' style='top:28px;right:30px;filter:drop-shadow(0 6px 10px #0008)'>{flag('kyrgyzstan', 120, True, 'kgsm')}</div>
<div class='abs' style='top:150px;left:40px;width:470px'>
 <div style='display:inline-block;background:{GOLD};color:{INK};font:800 19px Archivo;letter-spacing:5px;padding:7px 16px;border-radius:6px'>URGENT HIRING</div>
 <div style='font:400 108px Anton;color:#fff;line-height:.92;letter-spacing:2px;margin-top:14px;text-shadow:0 8px 24px #0008'>STITCHING<br>MASTERS</div>
 <div style='font:400 54px Anton;color:{GOLD2};letter-spacing:6px;margin-top:10px'>KYRGYZSTAN</div>
 <div style='font:700 22px Archivo;color:#F6DADC;margin-top:10px;line-height:1.35'>Fly within <b style='color:{GOLD2}'>15–20 working days</b></div></div>
<div class='abs' style='top:118px;right:40px;width:500px;height:500px;border-radius:50%;padding:10px;background:conic-gradient({GOLD},{GOLD2},{GOLD},#C99300,{GOLD});box-shadow:0 0 80px #FFC72C66,0 24px 44px #000a'>
 <div style='width:100%;height:100%;border-radius:50%;overflow:hidden;border:6px solid #fff;box-sizing:border-box'><img src='{P("kg_tailor_juki.jpg")}' style='width:100%;height:100%;object-fit:cover;object-position:62% 30%'></div></div>

<div class='abs' style='top:650px;left:30px;right:30px;height:120px;border-radius:22px;background:linear-gradient(90deg,{GOLD},{GOLD2});display:flex;align-items:center;justify-content:center;gap:26px;box-shadow:0 14px 26px #0007'>
 {icon('money', 58, INK, 2.2)}<div style='font:800 26px Archivo;color:{INK};letter-spacing:3px'>SALARY</div>
 <div style='font:400 92px Anton;color:{INK};line-height:1'>$500</div><div style='font:400 34px Anton;color:{INK};letter-spacing:2px'>PER MONTH</div></div>
<div class='abs' style='top:792px;left:30px;right:30px;display:flex;gap:14px'>{tiles}</div>
<div class='abs' style='top:986px;left:30px;right:30px;display:flex;gap:16px;align-items:center'>
 {small("tr_tailor.png", "center 30%")}{small("sewing_woman.jpg", "60% 30%")}
 <div style='flex:1.1;text-align:center'><div style='font:400 38px Anton;color:#fff;line-height:1.1;letter-spacing:1px'>SEND YOUR CV<br><span style='color:{GOLD2}'>ON WHATSAPP</span></div></div></div>

<div class='abs' style='top:1206px;left:0;width:1080px;height:144px;background:{CH}'></div>
<div class='abs' style='top:1200px;left:0;width:1080px;height:6px;background:linear-gradient(90deg,{RED},{GOLD},{RED})'></div>
<div class='abs' style='top:1218px;left:30px;right:30px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:6px 0'>{nums}</div>
<div class='abs' style='top:1306px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:10px'>{icon('mail', 22, GOLD, 2)}<span style='font:800 22px Archivo;color:#fff'>{EMAIL}</span></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CH}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Kyrgyzstan-Stitching-Masters-English.png"))
