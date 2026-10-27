"""Kuwait — Bike Riders, English (2026-10-27). Facts: demands/2026-10-27-kuwait-riders/facts.md (converted from another
agency's ad; content only). Needs a REAL rider photo at assets/photos/kw_rider.(jpg|png) supplied by the user —
refuses to render without it (no drawing fallback).
Design: "night delivery" — deep night-blue page, full-height rider photo with speed-line streaks, Kuwait flag band,
neon-orange title, salary meter dial, vertical perk list, orange CTA with all four numbers."""
import sys

from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

NIGHT, NIGHT2, ORG, ORG2, KWG, INK = "#0A1430", "#050A1C", "#FF7A1A", "#FFB547", "#007A3D", "#111827"
EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"


def photo():
    for e in ("jpg", "jpeg", "png", "webp"):
        p = PHOTOS / f"kw_rider.{e}"
        if p.exists():
            return p.as_uri()
    return None


def build(uri):
    streaks = "".join(f"<div class='abs' style='left:{x}px;top:{y}px;width:{w}px;height:4px;border-radius:4px;background:linear-gradient(90deg,{ORG}00,{ORG}cc)'></div>"
                      for x, y, w in [(360, 630, 190), (390, 675, 130), (365, 720, 170)])
    perks = [("clock", "12 HOURS", "Duty timing"), ("home", "ACCOMMODATION", "Provided by company"),
             ("medical", "MEDICAL", "Provided by company"), ("bus", "TRANSPORTATION", "Provided by company")]
    perk = "".join(f"<div style='display:flex;align-items:center;gap:16px;padding:14px 0;border-bottom:1px solid #ffffff22'>"
                   f"<span style='width:60px;height:60px;border-radius:16px;background:linear-gradient(135deg,{ORG},{ORG2});display:flex;align-items:center;justify-content:center;flex:none;box-shadow:0 6px 16px #FF7A1A55'>{icon(ic, 32, '#fff', 2.2)}</span>"
                   f"<div><div style='font:400 30px Anton;color:#fff;letter-spacing:1px;line-height:1'>{a}</div><div style='font:600 17px Archivo;color:#AFC0E6;margin-top:4px'>{b}</div></div></div>" for ic, a, b in perks)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 28px Anton;color:{INK};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:radial-gradient(circle at 80% 20%,#1D3A7A,{NIGHT} 45%,{NIGHT2})'></div>
<div class='abs' style='top:0;right:0;width:560px;height:1150px;overflow:hidden;clip-path:polygon(22% 0,100% 0,100% 100%,0 100%)'>
 <img src='{uri}' style='width:100%;height:100%;object-fit:cover;object-position:center'>
 <div style='position:absolute;inset:0;background:linear-gradient(90deg,{NIGHT}cc 0%,{NIGHT}00 35%),linear-gradient(0deg,{NIGHT} 0%,{NIGHT}00 25%)'></div></div>
{streaks}
<div class='abs' style='top:0;left:0;width:1080px;height:14px;display:flex'><div style='flex:1;background:{KWG}'></div><div style='flex:1;background:#fff'></div><div style='flex:1;background:#CE1126'></div></div>
<div class='abs' style='top:40px;left:40px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:280px;height:72px;object-position:left')}</div>
<div class='abs' style='top:150px;left:40px;width:560px'>
 <div style='display:flex;align-items:center;gap:14px'>{flag('kw', 110, True, 'kwr')}<span style='font:800 20px Archivo;color:{ORG2};letter-spacing:4px'>URGENTLY REQUIRED</span></div>
 <div style='font:400 120px Anton;color:#fff;line-height:.95;letter-spacing:2px;margin-top:20px'>BIKE<br><span style='color:{ORG}'>RIDERS</span></div>
 <div style='font:400 52px Anton;color:#fff;letter-spacing:6px;margin-top:10px'>FOR <span style='background:linear-gradient(90deg,{KWG},#2FBF71);-webkit-background-clip:text;color:transparent'>KUWAIT</span></div></div>
<div class='abs' style='top:590px;left:40px;width:300px;height:170px;border-radius:24px;background:linear-gradient(135deg,{ORG},#E2470F);box-shadow:0 16px 34px #FF7A1A66;display:flex;flex-direction:column;align-items:center;justify-content:center'>
 <div style='font:800 18px Archivo;color:#FFE3C7;letter-spacing:4px'>SALARY</div>
 <div style='font:400 84px Anton;color:#fff;line-height:1'>145</div>
 <div style='font:800 22px Archivo;color:#fff;letter-spacing:6px'>KWD / MONTH</div></div>
<div class='abs' style='top:790px;left:40px;width:480px'>{perk}</div>

<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:linear-gradient(100deg,{ORG},#E2470F)'></div>
<div class='abs' style='top:1172px;left:30px;width:600px;height:156px;background:#fff;border-radius:20px;display:grid;grid-template-columns:1fr 1fr;align-content:center;gap:12px 12px;padding:0 18px;box-sizing:border-box;box-shadow:0 10px 22px #0005'>{nums}</div>
<div class='abs' style='top:1176px;right:34px;width:400px;text-align:right'>
 <div style='font:400 40px Anton;color:#fff;letter-spacing:1px;line-height:1.05'>APPLY NOW!</div>
 <div style='font:700 19px Archivo;color:#FFF1E2;margin-top:6px'>Send your CV on WhatsApp</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div>
 <div style='font:600 13px Archivo;color:#FFE3C7;margin-top:8px'>{ADDRESS}</div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{NIGHT}'>{body}</div></body></html>")


if __name__ == "__main__":
    uri = photo()
    if not uri:
        sys.exit("Missing real rider photo: assets/photos/kw_rider.jpg (not rendered)")
    print(render(build(uri), "RS-Links-Kuwait-Bike-Riders-English.png"))
