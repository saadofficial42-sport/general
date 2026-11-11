"""Kyrgyzstan — Trained Tailors (JUKI machine operators), English (2026-11-11). Partner: Anchor Manpower (not named).
Facts from the user's reference ad: 450 USD/month; free accommodation, free food 2x daily, free transport; 1-year visa
extendable on performance; processing 30 days; age 21–40; duty 10 h/day; selection through JUKI machine working videos.
Dropped: "limited vacancies", "work · grow · thrive", "rewarding international career".
Design: "stitched sun" — warm cream page, Kyrgyz red header with the 40-ray sun, dashed 'stitch' borders, big tailor
photo in a stitched frame, gold salary badge, thread-spool fact chips, red video-selection banner, red CTA."""
import math

from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

RED, RED2, SUN, CREAM, INK = "#E8112D", "#9E0B1E", "#FFC400", "#FFF8EC", "#2A1416"
EMAIL = "hr@rslinksconsultants.com"


def sun(size, color, op):
    c, r1, r2 = size / 2, size * .28, size * .5
    rays = "".join(f"<path d='M{c + r1 * math.cos(math.radians(k * 9 - 2)):.1f} {c + r1 * math.sin(math.radians(k * 9 - 2)):.1f} L{c + r2 * math.cos(math.radians(k * 9)):.1f} {c + r2 * math.sin(math.radians(k * 9)):.1f} L{c + r1 * math.cos(math.radians(k * 9 + 2)):.1f} {c + r1 * math.sin(math.radians(k * 9 + 2)):.1f}Z' fill='{color}'/>" for k in range(40))
    return f"<svg width='{size}' height='{size}' style='display:block;opacity:{op}'>{rays}<circle cx='{c}' cy='{c}' r='{r1}' fill='{color}'/></svg>"


def build():
    photo = (PHOTOS / "kg_tailor_juki.jpg").as_uri()
    stitch = f"border:3px dashed {RED}"
    fac = [("home", "Free accommodation"), ("food", "Free food · 2 times daily"), ("bus", "Free transport")]
    fac_li = "".join(f"<div style='display:flex;align-items:center;gap:12px;padding:10px 0;border-bottom:2px dashed #F2C9CF'>"
                     f"<span style='width:46px;height:46px;border-radius:50%;background:{RED};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 24, '#fff', 2.3)}</span>"
                     f"<span style='font:800 21px Archivo;color:{INK}'>{t}</span></div>" for ic, t in fac)
    stats = [("calendar", "30 DAYS", "Processing"), ("user", "21 – 40", "Age (years)"), ("clock", "10 HRS", "Daily duty"), ("visa", "1 YEAR", "Visa, extendable*")]
    stat = "".join(f"<div style='background:#fff;border-radius:18px;{stitch};display:flex;flex-direction:column;align-items:center;justify-content:center'>"
                   f"{icon(ic, 30, RED, 2.3)}<div style='font:400 30px Anton;color:{INK};margin-top:4px'>{v}</div><div style='font:700 14px Archivo;color:#7A5A5E'>{l}</div></div>" for ic, v, l in stats)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:330px;background:linear-gradient(135deg,{RED},{RED2})'></div>
<div class='abs' style='top:-80px;right:-80px'>{sun(420, SUN, .22)}</div>
<div class='abs' style='top:318px;left:0;width:1080px;border-top:4px dashed {SUN}'></div>
<div class='abs' style='top:28px;left:36px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:270px;height:70px;object-position:left')}</div>
<div class='abs' style='top:28px;right:40px;filter:drop-shadow(0 6px 12px #0006)'>{flag('kyrgyzstan', 130, True, 'kgj')}</div>
<div class='abs' style='top:126px;left:40px'>
 <div style='font:800 20px Archivo;color:{SUN};letter-spacing:5px'>URGENT REQUIREMENT · KYRGYZSTAN</div>
 <div style='font:400 104px Anton;color:#fff;letter-spacing:3px;line-height:1;margin-top:6px'>TRAINED TAILORS</div>
 <div style='display:inline-block;margin-top:10px;background:{SUN};border-radius:10px;padding:6px 16px;font:400 28px Anton;color:{RED2};letter-spacing:1px'>JUKI MACHINE OPERATORS</div></div>

<div class='abs' style='top:366px;left:36px;width:560px;height:430px;border-radius:26px;padding:10px;background:#fff;{stitch};box-sizing:border-box;box-shadow:0 16px 32px rgba(158,11,30,.18)'>
 <div style='width:100%;height:100%;border-radius:18px;overflow:hidden'><img src='{photo}' style='width:100%;height:100%;object-fit:cover;object-position:center 30%'></div></div>
<div class='abs' style='top:730px;left:400px;width:220px;height:220px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFE680,{SUN} 55%,#E0A000);border:7px solid #fff;box-shadow:0 14px 28px #0006;display:flex;flex-direction:column;align-items:center;justify-content:center'>
 <div style='font:800 15px Archivo;color:{RED2};letter-spacing:3px'>SALARY</div><div style='font:400 74px Anton;color:{RED2};line-height:1'>$450</div><div style='font:800 14px Archivo;color:{RED2};letter-spacing:1px'>USD / MONTH</div></div>
<div class='abs' style='top:366px;right:36px;width:410px;background:#fff;border-radius:22px;{stitch};padding:10px 22px 6px;box-sizing:border-box'>
 <div style='font:400 28px Anton;color:{RED};letter-spacing:1px'>PROVIDED BY COMPANY</div>{fac_li}</div>
<div class='abs' style='top:640px;right:36px;width:410px;height:300px;display:grid;grid-template-columns:1fr 1fr;gap:12px'>{stat}</div>

<div class='abs' style='top:972px;left:36px;right:36px;height:150px;border-radius:24px;background:linear-gradient(120deg,{RED2},{RED});display:flex;align-items:center;gap:24px;padding:0 30px;box-sizing:border-box;box-shadow:0 14px 28px rgba(158,11,30,.3)'>
 <span style='width:92px;height:92px;border-radius:50%;background:{SUN};display:flex;align-items:center;justify-content:center;flex:none'>{icon('video', 48, RED2, 2.2)}</span>
 <div><div style='font:400 40px Anton;color:#fff;letter-spacing:1px;line-height:1.05'>SELECTION THROUGH WORKING VIDEO</div>
 <div style='font:700 19px Archivo;color:#FFE3E6;margin-top:6px'>Send a video of yourself working on a JUKI machine</div></div></div>
<div class='abs' style='top:1128px;left:36px;right:36px;font:600 13px Archivo;color:#7A5A5E'>*1-year visa, extendable on the basis of performance.</div>

<div class='abs' style='top:1156px;left:0;width:1080px;height:194px;background:{INK};border-top:5px dashed {SUN}'></div>
<div class='abs' style='top:1188px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1186px;right:40px;width:380px;text-align:right'>
 <div style='font:400 34px Anton;color:{SUN};letter-spacing:1px;line-height:1.05'>SEND CV + JUKI VIDEO</div>
 <div style='font:700 18px Archivo;color:#E9D9DB;margin-top:6px'>on WhatsApp</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CREAM}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Kyrgyzstan-JUKI-Tailors-English.png"))
