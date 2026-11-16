"""Uzbekistan factory workers — v11, English (2026-11-16). User: very attractive, different design, show the country's
landscapes. Facts as v10 (no "visa"). Design: "Charvak panorama" — full-bleed Charvak lake & mountains photo as the
top half with the title in the sky, Samarkand madrasa arch inset, two big circular factory photos floating on the
shoreline, frosted white sheet below with gold salary ribbon, stat pills, duties/free lists, turquoise footer."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

TQ, TQ2, SKY, GOLD, GOLD2, INK = "#0FA3B1", "#066A75", "#1F6FD1", "#F2B705", "#FFD45C", "#0B2340"
EMAIL = "hr@rslinksconsultants.com"


def circ(src, d, pos, cap):
    return (f"<div style='width:{d}px;text-align:center'><div style='width:{d}px;height:{d}px;border-radius:50%;padding:7px;background:linear-gradient(135deg,{GOLD2},{TQ});box-shadow:0 20px 36px #0B234066'>"
            f"<div style='width:100%;height:100%;border-radius:50%;overflow:hidden;border:5px solid #fff;box-sizing:border-box'><img src='{src}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'></div></div>"
            f"<div style='display:inline-block;margin-top:-22px;position:relative;background:{INK};color:#fff;font:800 17px Archivo;padding:6px 14px;border-radius:999px'>{cap}</div></div>")


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    stats = [("user", "50 Posts"), ("clock", "10 hrs duty"), ("calendar", "Age 21 – 35"), ("doc", "30 – 35 days processing")]
    pills = "".join(f"<div style='display:flex;align-items:center;gap:8px;background:#EAF7F8;border:1.5px solid #BFE6EA;border-radius:999px;padding:8px 16px'>{icon(ic, 22, TQ2, 2.3)}<span style='font:800 19px Archivo;color:{INK}'>{t}</span></div>" for ic, t in stats)
    duties = ["General factory work", "Packaging", "Store work (ordering)", "Cleaning goods &amp; materials", "Production line work"]
    free = ["Accommodation", "Transport", "Medical", "Food", "Other company facilities"]
    li = lambda xs, col: "".join(f"<div style='display:flex;align-items:center;gap:9px;font:700 19px Archivo;color:{INK};line-height:1.45'>{icon('check', 20, col, 2.8)}{x}</div>" for x in xs)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:700px;overflow:hidden'><img src='{P("uz_charvak_lake.jpg")}' style='width:100%;height:100%;object-fit:cover;object-position:center 30%'>
 <div style='position:absolute;inset:0;background:linear-gradient(180deg,#0B234055 0%,#0B234000 35%,#0B234000 70%,#F7FBFC 100%)'></div></div>
<div class='abs' style='top:24px;left:30px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0004'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:left')}</div>
<div class='abs' style='top:28px;right:30px;filter:drop-shadow(0 6px 10px #0006)'>{flag('uzbekistan', 120, True, 'uz11')}</div>
<div class='abs' style='top:118px;left:0;width:1080px;text-align:center'>
 <div style='display:inline-block;background:{GOLD};color:{INK};font:800 19px Archivo;letter-spacing:5px;padding:7px 18px;border-radius:999px'>URGENT HIRING · TASHKENT</div>
 <div style='font:400 120px Anton;color:#fff;line-height:.95;letter-spacing:4px;margin-top:12px;text-shadow:0 10px 30px #0B2340aa'>FACTORY WORKERS</div>
 <div style='font:400 60px Anton;color:{GOLD2};letter-spacing:10px;text-shadow:0 6px 18px #0B2340aa'>UZBEKISTAN</div></div>
<div class='abs' style='top:400px;left:40px;width:200px;height:250px;border-radius:100px 100px 14px 14px;overflow:hidden;border:6px solid #fff;box-shadow:0 16px 30px #0006'><img src='{P("uz_samarkand_madrasa.jpg")}' style='width:100%;height:100%;object-fit:cover'></div>
<div class='abs' style='top:640px;left:54px;background:#fff;color:{TQ2};font:800 15px Archivo;padding:4px 10px;border-radius:6px;letter-spacing:1px'>SAMARKAND</div>
<div class='abs' style='top:380px;left:290px;display:flex;gap:30px'>{circ(P("rslinks_worker_hero_blue.png"), 330, '35% 22%', 'Packing &amp; Production')}{circ(P("uz_milk_packing.jpg"), 330, 'center 40%', 'Factory Line Work')}</div>

<div class='abs' style='top:752px;left:30px;right:30px;height:120px;border-radius:22px;background:linear-gradient(90deg,{GOLD},{GOLD2});display:flex;align-items:center;justify-content:space-between;padding:0 34px;box-shadow:0 14px 26px #C9930055'>
 <div><div style='font:800 20px Archivo;color:{INK};letter-spacing:3px'>MONTHLY SALARY</div><div style='font:400 70px Anton;color:{INK};line-height:1'>$350 – $500 <span style='font-size:28px'>USD</span></div></div>
 <div style='background:{INK};color:#fff;border-radius:16px;padding:12px 18px;text-align:center'><div style='font:400 28px Anton;color:{GOLD2};letter-spacing:1px'>INCLUDED</div><div style='font:800 19px Archivo'>Ticket &amp; Protector</div></div></div>
<div class='abs' style='top:890px;left:30px;right:30px;display:flex;flex-wrap:wrap;gap:10px;justify-content:center'>{pills}</div>
<div class='abs' style='top:958px;left:30px;width:500px;background:#fff;border-radius:18px;border-left:6px solid {TQ};padding:12px 20px;box-sizing:border-box;box-shadow:0 8px 18px #0B23401a'>
 <div style='font:400 25px Anton;color:{TQ2};letter-spacing:1.5px'>YOUR WORK</div>{li(duties, TQ)}</div>
<div class='abs' style='top:958px;right:30px;width:500px;background:#fff;border-radius:18px;border-left:6px solid {GOLD};padding:12px 20px;box-sizing:border-box;box-shadow:0 8px 18px #0B23401a'>
 <div style='font:400 25px Anton;color:#B98A00;letter-spacing:1.5px'>FREE FACILITIES</div>{li(free, '#D49E00')}</div>

<div class='abs' style='top:1186px;left:0;width:1080px;height:164px;background:linear-gradient(100deg,{TQ2},{TQ})'></div>
<div class='abs' style='top:1204px;left:30px;right:30px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:8px 0'>{nums}</div>
<div class='abs' style='top:1302px;left:30px;right:30px;display:flex;justify-content:space-between;align-items:center'>
 <span style='font:400 28px Anton;color:{GOLD2};letter-spacing:1px'>SEND YOUR CV ON WHATSAPP</span>
 <span style='display:flex;align-items:center;gap:8px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 21px Archivo;color:#fff'>{EMAIL}</span></span></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#F7FBFC'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Uzbekistan-Factory-Workers-v11-English.png"))
