"""Kuwait — Bike Riders v2, English (2026-11-08). Same facts as kuwait_riders.py (demands/2026-10-27-kuwait-riders):
145 KWD, 12 hours, accommodation / medical / transportation by company. User re-sent the source ad; this version
uses its rider + Kuwait Towers photo (kw_rider_towers.jpg). Dropped again: "stable job, good salary, better future",
"genuine opportunities", "your trust our commitment". Design: "route card" — white page, tall right photo panel with
red-white-green edge stripe, red 145 KWD price tag, numbered route-stop perk list on a dashed line, black CTA."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

RED, RED2, KG, INK, SOFT = "#D7262E", "#9E141B", "#007A3D", "#14171C", "#F4F5F7"
EMAIL = "hr@rslinksconsultants.com"


def build():
    photo = (PHOTOS / "kw_rider_towers.jpg").as_uri()
    perks = [("clock", "12 HOURS", "Duty timing"), ("home", "ACCOMMODATION", "Provided by company"),
             ("medical", "MEDICAL", "Provided by company"), ("bus", "TRANSPORTATION", "Provided by company")]
    stops = "".join(f"<div style='position:relative;display:flex;align-items:center;gap:18px;height:96px'>"
                    f"<span style='width:64px;height:64px;border-radius:50%;background:{RED if i == 0 else '#fff'};border:4px solid {RED};display:flex;align-items:center;justify-content:center;flex:none;z-index:1'>{icon(ic, 30, '#fff' if i == 0 else RED, 2.3)}</span>"
                    f"<div><div style='font:400 32px Anton;color:{INK};letter-spacing:1px;line-height:1'>{a}</div><div style='font:700 17px Archivo;color:#6A717C;margin-top:4px'>{b}</div></div></div>"
                    for i, (ic, a, b) in enumerate(perks))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;right:0;width:470px;height:1170px;overflow:hidden'><img src='{photo}' style='width:100%;height:100%;object-fit:cover;object-position:center 20%'>
 <div style='position:absolute;inset:0;background:linear-gradient(90deg,#fff 0%,#fff0 18%)'></div></div>
<div class='abs' style='top:0;right:470px;width:14px;height:1170px;display:flex;flex-direction:column'><div style='flex:1;background:{KG}'></div><div style='flex:1;background:#fff;border-left:1px solid #ddd'></div><div style='flex:1;background:{RED}'></div><div style='flex:.4;background:#111'></div></div>
<div class='abs' style='top:36px;left:40px'>{logo_img('logo-horizontal-light', 'width:300px;height:78px;object-position:left')}</div>
<div class='abs' style='top:150px;left:40px;width:560px'>
 <div style='display:flex;align-items:center;gap:14px'>{flag('kw', 100, True, 'kwv2')}<span style='background:{RED};color:#fff;font:800 18px Archivo;letter-spacing:3px;padding:7px 14px;border-radius:8px'>URGENTLY REQUIRED</span></div>
 <div style='font:400 118px Anton;color:{INK};line-height:.95;letter-spacing:2px;margin-top:20px'>BIKE<br>RIDERS</div>
 <div style='font:400 48px Anton;color:{RED};letter-spacing:8px;margin-top:8px'>FOR KUWAIT</div></div>
<div class='abs' style='top:600px;left:40px;width:420px;height:130px;background:linear-gradient(135deg,{RED},{RED2});clip-path:polygon(0 0,88% 0,100% 50%,88% 100%,0 100%);display:flex;align-items:center;gap:18px;padding-left:26px;box-sizing:border-box;filter:drop-shadow(0 10px 16px rgba(158,20,27,.35))'>
 <span style='width:22px;height:22px;border-radius:50%;background:#fff'></span>
 <div><div style='font:800 15px Archivo;color:#FFD9DB;letter-spacing:3px'>SALARY / MONTH</div><div style='font:400 70px Anton;color:#fff;line-height:1'>145 KWD</div></div></div>
<div class='abs' style='top:770px;left:40px;width:520px'>
 <div style='position:absolute;left:30px;top:30px;bottom:30px;border-left:4px dashed {RED}66'></div>{stops}</div>
<div class='abs' style='top:1170px;left:0;width:1080px;height:180px;background:{INK};border-top:6px solid {RED}'></div>
<div class='abs' style='top:1196px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1194px;right:40px;width:380px;text-align:right'>
 <div style='font:400 40px Anton;color:#fff;letter-spacing:1px;line-height:1.05'>APPLY NOW!</div>
 <div style='font:700 19px Archivo;color:#C9CED6;margin-top:6px'>Send your CV on WhatsApp</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Kuwait-Bike-Riders-v2-English.png"))
