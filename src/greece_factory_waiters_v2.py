"""Greece — Factory Workers & Waiters v2, English (2026-11-13). User: processing 3.5 months; change the factory worker's
shirt colour (recoloured green -> navy: rslinks_worker_hero_blue.png); very dynamic and impressive.
Design: "Aegean sunset" — deep indigo-to-coral sunset sky with glowing sun, Santorini dome skyline silhouette, huge
gradient WORK IN GREECE title, two big tilted photo cards with angled clip + glowing borders, 3.5-month sun badge,
glass benefit chips, coral diagonal CTA strip. Cost / shares / rate stay off the ad."""
from common import PHONES, PHOTOS, font_css, icon, logo_img, render, whatsapp_icon
from greece_ecycle import flag_gr

IND, IND2, CORAL, SUN, AEG, INK = "#1B1446", "#0D0A2B", "#FF6B4A", "#FFC547", "#1E6FD9", "#0D0A2B"
EMAIL = "hr@rslinksconsultants.com"
GLASS = "background:linear-gradient(135deg,#ffffff2e,#ffffff0d);border:1.5px solid #ffffff4d;box-shadow:0 12px 26px #0006"


def skyline(w, h, col):
    s = ""
    for x, bw, bh in [(0, 120, 80), (110, 90, 120), (190, 130, 70), (310, 80, 105), (380, 140, 85), (510, 90, 130), (590, 120, 75), (700, 100, 110), (790, 140, 80), (920, 90, 120), (1000, 80, 90)]:
        s += f"<rect x='{x}' y='{h - bh}' width='{bw}' height='{bh}' fill='{col}'/>"
    for cx, r in [(150, 40), (550, 54), (960, 44)]:
        s += f"<path d='M{cx - r} {h - 118} A{r} {r} 0 0 1 {cx + r} {h - 118}Z' fill='{col}'/><rect x='{cx - r}' y='{h - 120}' width='{2 * r}' height='120' fill='{col}'/><rect x='{cx - 3}' y='{h - 118 - r - 24}' width='6' height='24' fill='{col}'/><rect x='{cx - 10}' y='{h - 118 - r - 16}' width='20' height='5' fill='{col}'/>"
    return f"<svg width='{w}' height='{h}' style='display:block'>{s}</svg>"


def card(src, pos, label, rot, ring):
    return (f"<div style='transform:rotate({rot}deg);width:440px'>"
            f"<div style='width:440px;height:470px;padding:7px;background:linear-gradient(135deg,{ring});clip-path:polygon(0 4%,100% 0,100% 96%,0 100%);box-shadow:0 30px 50px #0009'>"
            f"<div style='width:100%;height:100%;clip-path:polygon(0 4%,100% 0,100% 96%,0 100%);overflow:hidden'><img src='{src}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'></div></div>"
            f"<div style='margin:-40px 0 0 24px;position:relative;display:inline-block;background:linear-gradient(90deg,{SUN},{CORAL});padding:10px 26px;border-radius:12px;font:400 40px Anton;color:{INK};letter-spacing:2px;box-shadow:0 12px 22px #0007'>{label}</div></div>")


def build():
    fac, wai = (PHOTOS / "rslinks_worker_hero_blue.png").as_uri(), (PHOTOS / "sa_waiter2.jpg").as_uri()
    items = [("home", "ACCOMMODATION"), ("medical", "MEDICAL"), ("doc", "WORK PERMIT · TAX-PAYER COMPANIES"), ("calendar", "WALK-IN EMBASSY APPOINTMENT INCLUDED")]
    chips = "".join(f"<div style='display:flex;align-items:center;gap:14px;border-radius:18px;padding:10px 16px;{GLASS}'>"
                    f"<span style='width:56px;height:56px;border-radius:14px;background:linear-gradient(135deg,{SUN},{CORAL});display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 30, INK, 2.3)}</span>"
                    f"<span style='font:400 25px Anton;color:#fff;letter-spacing:1px;line-height:1.1'>{t}</span></div>" for ic, t in items)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:linear-gradient(180deg,{IND2} 0%,{IND} 30%,#5B2A6E 40%,#C2456A 54%,{CORAL} 63%,#FF9A4A 68%,{IND2} 68.2%)'></div>
<div class='abs' style='top:520px;left:340px;width:400px;height:400px;border-radius:50%;background:radial-gradient(circle,#FFE38A,{SUN} 40%,#FF9A4A00 70%)'></div>
<div class='abs' style='top:-80px;left:-100px;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,#1E6FD966,transparent 70%)'></div>
<div class='abs' style='inset:0;background:repeating-linear-gradient(120deg,#ffffff06 0 60px,transparent 60px 120px)'></div>
<div class='abs' style='top:700px;left:0'>{skyline(1080, 236, IND2)}</div>
<div class='abs' style='top:28px;left:36px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 8px 18px #0006'>{logo_img('logo-horizontal-light', 'width:270px;height:70px;object-position:left')}</div>
<div class='abs' style='top:34px;right:40px;transform:rotate(5deg);filter:drop-shadow(0 8px 14px #0008)'>{flag_gr(126)}</div>

<div class='abs' style='top:122px;left:40px;width:700px'>
 <div style='display:inline-block;background:linear-gradient(90deg,{CORAL},{SUN});color:{INK};font:800 20px Archivo;letter-spacing:5px;padding:8px 18px;border-radius:999px'>URGENT HIRING · EUROPE</div>
 <div style='font:400 104px Anton;line-height:.92;letter-spacing:3px;margin-top:12px;background:linear-gradient(180deg,#fff 30%,#FFD9A8);-webkit-background-clip:text;color:transparent;filter:drop-shadow(6px 6px 0 #C2456A)'>WORK IN<br>GREECE</div></div>

<div class='abs' style='top:120px;right:44px;width:250px;height:250px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFE9A6,{SUN} 55%,{CORAL});box-shadow:0 0 60px #FFC54788,0 16px 30px #0008;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-8deg)'>
 <div style='font:800 17px Archivo;color:{INK};letter-spacing:3px'>PROCESSING</div>
 <div style='font:400 88px Anton;color:{INK};line-height:.95'>3.5</div>
 <div style='font:400 32px Anton;color:{INK};letter-spacing:3px'>MONTHS</div></div>

<div class='abs' style='top:390px;left:50px'>{card(fac, 'center 25%', 'FACTORY WORKERS', -4, f"{SUN},{CORAL}")}</div>
<div class='abs' style='top:410px;right:50px'>{card(wai, 'center 18%', 'WAITERS', 4, f"{CORAL},{AEG}")}</div>

<div class='abs' style='top:930px;left:36px;right:36px;display:grid;grid-template-columns:1fr 1fr;gap:12px 14px'>{chips}</div>

<div class='abs' style='top:1118px;left:-30px;width:1140px;height:66px;background:linear-gradient(90deg,{SUN},{CORAL});transform:rotate(-1.5deg);display:flex;align-items:center;justify-content:center;gap:14px;box-shadow:0 10px 20px #0007'>
 {icon('doc', 32, INK, 2.3)}<span style='font:400 34px Anton;color:{INK};letter-spacing:2px'>SEND YOUR CV ON WHATSAPP TODAY</span></div>

<div class='abs' style='top:1196px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1198px;right:40px;width:380px;text-align:right'>
 <div style='font:400 46px Anton;color:{SUN};letter-spacing:1px;line-height:1.05'>APPLY NOW!</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:12px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{IND2}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Greece-Factory-Workers-Waiters-v2.png"))
