"""Uzbekistan — Drivers, English (2026-11-21). User content: salary 500 USD (shown in PKR ≈ 1,40,000 at ~280 PKR/$,
marked approx.); food & accommodation provided; must hold a valid driving licence; ticket & protector included
("visa" dropped per the no-visa rule). Reference ad (other agency) used for layout idea + chauffeur/car photo crop.
Design: "golden hour boulevard" — warm sunset-to-cream page, big chauffeur+car photo on the right fading into the
page, navy/gold title stack on the left, gold salary ribbon with USD sub-line, 4 white benefit cards, taxi inset,
deep-navy footer."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

NAVY, NAVY2, GOLD, GOLD2, TQ, CREAM, INK = "#13265C", "#0B173B", "#E9A82B", "#FFD27A", "#14A3B8", "#FFF7EC", "#13265C"
EMAIL = "hr@rslinksconsultants.com"


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    ben = [("food", "Food Provided"), ("home", "Accommodation Provided"), ("idcard", "Valid Driving Licence Required"), ("plane", "Ticket &amp; Protector Included")]
    cards = "".join(f"<div style='display:flex;align-items:center;gap:14px;background:#fff;border-radius:18px;padding:0 18px;height:84px;box-shadow:0 10px 20px #13265C1f;border-left:7px solid {GOLD if i % 2 else TQ}'>"
                    f"<span style='width:54px;height:54px;border-radius:14px;background:{NAVY};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 30, GOLD2, 2.2)}</span>"
                    f"<span style='font:800 23px Archivo;color:{INK};line-height:1.15'>{t}</span></div>" for i, (ic, t) in enumerate(ben))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:linear-gradient(180deg,#FFD9A0 0%,#FFE9C9 30%,{CREAM} 60%,#fff 100%)'></div>
<div class='abs' style='top:150px;right:0;width:720px;height:650px;overflow:hidden'><img src='{P("uz_chauffeur_car_ref.jpg")}' style='width:100%;height:100%;object-fit:cover;object-position:left center'>
 <div style='position:absolute;inset:0;background:linear-gradient(90deg,#FFE9C9 0%,#FFE9C900 22%),linear-gradient(0deg,{CREAM} 0%,{CREAM}00 18%),linear-gradient(180deg,#FFE2B8 0%,#FFE2B800 16%)'></div></div>
<div class='abs' style='top:24px;left:30px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0002'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:left')}</div>
<div class='abs' style='top:26px;right:30px;filter:drop-shadow(0 6px 10px #0004)'>{flag('uzbekistan', 120, True, 'uzdr')}</div>
<div class='abs' style='top:150px;left:44px;width:520px'>
 <div style='display:inline-block;background:{NAVY};color:{GOLD2};font:800 19px Archivo;letter-spacing:5px;padding:7px 16px;border-radius:6px'>URGENT HIRING</div>
 <div style='font:400 128px Anton;color:{NAVY};line-height:.9;letter-spacing:2px;margin-top:14px'>DRIVERS</div>
 <div style='font:400 38px Anton;color:{GOLD};letter-spacing:4px;margin-top:6px'>JOBS IN</div>
 <div style='font:400 78px Anton;color:{NAVY};line-height:.95;letter-spacing:3px'>UZBEKISTAN</div></div>
<div class='abs' style='top:560px;left:44px;width:300px;height:210px;border-radius:18px;overflow:hidden;border:6px solid #fff;box-shadow:0 14px 26px #13265C40;transform:rotate(-3deg)'><img src='{P("driver_taxi.jpg")}' style='width:100%;height:100%;object-fit:cover;object-position:40% 40%'></div>

<div class='abs' style='top:810px;left:30px;right:30px;height:140px;border-radius:24px;background:linear-gradient(90deg,{NAVY2},{NAVY});display:flex;align-items:center;justify-content:space-between;padding:0 36px;box-shadow:0 14px 28px #13265C55'>
 <div><div style='font:800 21px Archivo;color:{GOLD2};letter-spacing:4px'>MONTHLY SALARY</div><div style='font:700 19px Archivo;color:#C9D3EE;margin-top:6px'>USD 500 per month</div></div>
 <div style='text-align:right'><div style='font:400 84px Anton;color:#fff;line-height:1'>PKR 1,40,000<span style='font-size:28px;color:{GOLD2}'>*</span></div></div></div>
<div class='abs' style='top:968px;left:30px;right:30px;display:grid;grid-template-columns:1fr 1fr;gap:14px'>{cards}</div>
<div class='abs' style='top:1166px;left:40px;font:600 14px Archivo;color:#6A7280'>*Approx. at current USD rate; paid as USD 500.</div>

<div class='abs' style='top:1190px;left:0;width:1080px;height:160px;background:linear-gradient(100deg,{NAVY2},{NAVY})'></div>
<div class='abs' style='top:1190px;left:0;width:1080px;height:6px;background:linear-gradient(90deg,{TQ},{GOLD},{TQ})'></div>
<div class='abs' style='top:1210px;left:30px;right:30px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:8px 0'>{nums}</div>
<div class='abs' style='top:1302px;left:30px;right:30px;display:flex;justify-content:space-between;align-items:center'>
 <span style='font:400 28px Anton;color:{GOLD2};letter-spacing:1px'>SEND YOUR CV &amp; LICENCE ON WHATSAPP</span>
 <span style='display:flex;align-items:center;gap:8px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></span></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CREAM}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Uzbekistan-Drivers-English.png"))
