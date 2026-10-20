"""Kyrgyzstan — Production Line Operators, English (2026-10-20). Facts: demands/2026-10-20-kyrgyzstan-production/facts.md
(from the user's demand-letter photo; employer not named at user request). Costs the letter puts on the worker
(air ticket, medical, insurance) are stated plainly, not hidden.
Design: "dark spotlight + Kyrgyz sun" — charcoal page, diagonal-cut real photo, red title slab, yellow 40-ray sun
salary badge (from the Kyrgyz flag), dark term tiles, amber 'own expense' notice, red CTA."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon
import math

RED, RED2, SUN, DARK, DARK2, INK = "#E8112D", "#A50C20", "#FFD21F", "#121417", "#1E2227", "#16181C"
EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"


def sun(size):
    c, r1, r2 = size / 2, size * .30, size * .5
    rays = ""
    for k in range(40):
        a, b = math.radians(k * 9 - 2.2), math.radians(k * 9 + 2.2)
        rays += (f"<path d='M{c + r1 * math.cos(a):.1f} {c + r1 * math.sin(a):.1f} L{c + r2 * math.cos((a + b) / 2):.1f} {c + r2 * math.sin((a + b) / 2):.1f} "
                 f"L{c + r1 * math.cos(b):.1f} {c + r1 * math.sin(b):.1f}Z' fill='{SUN}'/>")
    return f"<svg width='{size}' height='{size}' style='display:block'>{rays}<circle cx='{c}' cy='{c}' r='{r1 + 2}' fill='{SUN}'/><circle cx='{c}' cy='{c}' r='{r1 - 8}' fill='{RED}'/></svg>"


def build():
    hero = (PHOTOS / "rslinks_worker_hero.png").as_uri()
    inset = (PHOTOS / "tr_plastic.png").as_uri()
    terms = [("calendar", "6 days", "working days per week"), ("clock", "8 hours", "working day"),
             ("home", "Accommodation", "provided by the employer"), ("food", "Meals", "provided by the employer")]
    tiles = "".join(f"<div style='background:{DARK2};border-radius:18px;border-left:6px solid {SUN};display:flex;align-items:center;gap:16px;padding:0 20px'>"
                    f"<div style='width:62px;height:62px;border-radius:16px;background:{RED};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 34, '#fff', 2.2)}</div>"
                    f"<div><div style='font:400 34px Anton;color:#fff;letter-spacing:.5px;line-height:1.1'>{v}</div><div style='font:600 18px Archivo;color:#B9BEC6'>{l}</div></div></div>"
                    for ic, v, l in terms)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(34)}<span style='font:400 31px Anton;color:{INK};letter-spacing:.5px;line-height:1.15'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:120px;background:{DARK}'></div>
<div class='abs' style='top:16px;left:28px;background:#fff;border-radius:16px;padding:2px 14px'>{logo_img('logo-horizontal-light', 'width:330px;height:84px;object-position:left')}</div>
<div class='abs' style='top:22px;right:28px;display:flex;align-items:center;gap:16px'>
 <div style='background:{RED};border-radius:12px;padding:10px 18px;display:flex;align-items:center;gap:8px'>{icon('megaphone', 26, '#fff', 2.2)}<span style='font:400 28px Anton;color:#fff;letter-spacing:1px'>URGENT HIRING</span></div>
 <div style='filter:drop-shadow(0 4px 8px #0008)'>{flag('kyrgyzstan', 120, True, 'kgp')}</div></div>

<div class='abs' style='top:120px;left:0;width:1080px;height:1030px;background:{DARK}'></div>
<div class='abs' style='top:120px;left:380px;width:700px;height:540px;clip-path:polygon(22% 0,100% 0,100% 100%,0 100%);overflow:hidden'>
 <img src='{hero}' style='width:100%;height:100%;object-fit:cover;object-position:center 22%'>
 <div style='position:absolute;inset:0;background:linear-gradient(90deg,{DARK} 0%,{DARK}00 40%)'></div></div>
<div class='abs' style='top:150px;left:40px;width:560px'>
 <div style='font:800 22px Archivo;color:{SUN};letter-spacing:4px'>JOBS IN KYRGYZSTAN</div>
 <div style='margin-top:14px;display:inline-block;background:{RED};padding:14px 22px 10px;box-shadow:10px 10px 0 {RED2}'>
  <div style='font:400 78px Anton;color:#fff;line-height:.98;letter-spacing:1px'>PRODUCTION<br>LINE<br>OPERATORS</div></div>
 <div style='margin-top:26px;display:flex;align-items:center;gap:12px'>
  <span style='font:400 46px Anton;color:{SUN};line-height:1'>10</span><span style='font:800 24px Archivo;color:#fff;letter-spacing:2px'>POSTS</span>
  <span style='width:2px;height:34px;background:#ffffff44;margin:0 6px'></span>{icon('pin', 26, SUN, 2.4)}<span style='font:800 24px Archivo;color:#fff'>Kyrgyz Republic</span></div></div>
<div class='abs' style='top:520px;left:40px;width:236px;height:236px;filter:drop-shadow(0 12px 22px #000a)'>{sun(236)}
 <div style='position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center'>
  <div style='font:800 15px Archivo;color:#fff;letter-spacing:2px'>SALARY</div>
  <div style='font:400 50px Anton;color:#fff;line-height:1'>$450+</div>
  <div style='font:800 14px Archivo;color:#fff;letter-spacing:1px'>USD / MONTH</div></div></div>
<div class='abs' style='top:470px;right:40px;width:250px;height:170px;border-radius:18px;overflow:hidden;border:5px solid {SUN};box-shadow:0 12px 24px #000a'><img src='{inset}' style='width:100%;height:100%;object-fit:cover'></div>

<div class='abs' style='top:676px;left:300px;right:40px;font:800 21px Archivo;color:#fff;line-height:1.3'>Salary <span style='color:{SUN}'>USD 450 per month or more</span><br><span style='color:#B9BEC6;font-weight:600'>Six-day week · eight-hour working day</span></div>
<div class='abs' style='top:784px;left:40px;right:40px;display:grid;grid-template-columns:1fr 1fr;gap:16px;height:224px'>{tiles}</div>
<div class='abs' style='top:1026px;left:40px;right:40px;height:106px;border-radius:18px;border:3px dashed {SUN};display:flex;align-items:center;gap:18px;padding:0 22px;box-sizing:border-box'>
 <div style='font:400 24px Anton;color:{SUN};letter-spacing:1px;line-height:1.05;width:150px;flex:none'>AT EMPLOYEE'S<br>OWN EXPENSE</div>
 {''.join(f"<div style='flex:1;display:flex;align-items:center;gap:10px'>{icon(ic, 30, '#fff', 2.2)}<span style='font:800 21px Archivo;color:#fff;line-height:1.15'>{t}</span></div>" for ic, t in [('plane', 'Air ticket'), ('medical', 'Medical examination'), ('shield', 'Insurance')])}</div>

<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:linear-gradient(100deg,{RED2},{RED})'></div>
<div class='abs' style='top:1170px;left:28px;height:160px;padding:0 20px;background:#fff;border-radius:20px;display:flex;flex-direction:column;justify-content:center;box-shadow:0 10px 22px #0006'>{nums}</div>
<div class='abs' style='top:1176px;right:34px;width:540px;text-align:right'>
 <div style='font:400 44px Anton;color:{SUN};letter-spacing:1px;line-height:1.05'>SEND YOUR CV ON WHATSAPP</div>
 <div style='font:700 20px Archivo;color:#fff;margin-top:8px'>Apply now — limited to 10 posts</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:10px'>{icon('mail', 24, SUN, 2)}<span style='font:800 23px Archivo;color:#fff'>{EMAIL}</span></div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:6px;margin-top:8px'>{icon('pin', 18, SUN, 2.2)}<span style='font:600 14px Archivo;color:#FFD9DE'>{ADDRESS}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{DARK}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Kyrgyzstan-Production-Line-Operators-English.png"))
