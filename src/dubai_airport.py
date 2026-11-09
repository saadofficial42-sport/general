"""Dubai Airport — 7 positions, English (2026-11-09). Facts: demands/2026-11-09-dubai-airport/facts.md (converted from
another agency's ad; content only). The airline's name/logos are not used (third-party trademark; employer not named).
Design: "departures board" — sky-to-navy gradient, airplane silhouette, big DUBAI AIRPORT title, a black split-flap
style departure board listing positions / salary / remarks in amber, real RS Links worker photo, UAE flag stripe."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

NAVY, NAVY2, SKY, AMBER, RED, INK = "#0B2550", "#06142E", "#3FA9F5", "#FFC21A", "#E0262F", "#0F1724"
EMAIL = "hr@rslinksconsultants.com"
ROWS = [("SECURITY GUARD", "2267", "Height 5'8\" · 14 yrs education"), ("AIRPORT LOADER", "1105", ""), ("AIRCRAFT CLEANER", "1120", ""),
        ("GENERAL ASSISTANT", "900", "With food"), ("KITCHEN HELPER", "900", "With food"), ("HOUSEKEEPER", "900", "With food"), ("CLEANER", "900", "")]


def plane():
    return ("<svg width='260' height='110' viewBox='0 0 260 110'><path d='M10 62 L190 50 C225 48 250 52 252 58 C250 64 225 68 190 66 L120 64 L80 100 L62 100 L86 63 L40 61 L24 78 L12 78 L20 60 Z' fill='#fff' opacity='.9'/>"
            "<path d='M120 52 L84 14 L66 14 L88 50 Z' fill='#fff' opacity='.9'/></svg>")


def build():
    hero = (PHOTOS / "rslinks_worker_hero.png").as_uri()
    rows = "".join(f"<div style='display:flex;align-items:center;height:62px;padding:0 20px;border-top:{'0' if i == 0 else '1px solid #ffffff14'};background:{'#ffffff06' if i % 2 else 'transparent'}'>"
                   f"<span style='width:38px;font:400 22px Anton;color:{SKY}'>{i + 1:02d}</span>"
                   f"<span style='flex:1;font:400 30px Anton;color:#fff;letter-spacing:1.5px'>{t}</span>"
                   f"<span style='width:190px;text-align:right'><span style='display:inline-block;background:#1B1F27;border:1px solid #333;border-radius:6px;padding:2px 10px;font:400 32px Anton;color:{AMBER};letter-spacing:2px'>{s}</span> <span style='font:800 15px Archivo;color:#C9D3E0'>AED</span></span>"
                   f"<span style='width:300px;text-align:right;font:700 17px Archivo;color:{'#7BE495' if 'food' in r else '#C9D3E0'}'>{r or '—'}</span></div>"
                   for i, (t, s, r) in enumerate(ROWS))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:linear-gradient(180deg,#8FD0FF 0%,{SKY} 22%,{NAVY} 48%,{NAVY2} 100%)'></div>
<div class='abs' style='top:400px;left:470px;transform:rotate(-10deg) scale(.8)'>{plane()}</div>
<div class='abs' style='top:0;left:0;width:1080px;height:12px;display:flex'><div style='width:120px;background:{RED}'></div><div style='flex:1;background:#00843D'></div><div style='flex:1;background:#fff'></div><div style='flex:1;background:#000'></div></div>
<div class='abs' style='top:32px;left:36px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:280px;height:72px;object-position:left')}</div>
<div class='abs' style='top:150px;left:40px;width:640px'>
 <div style='display:flex;align-items:center;gap:14px'>{flag('ae', 100, True, 'aeD')}<span style='background:{RED};color:#fff;font:800 18px Archivo;letter-spacing:3px;padding:7px 14px;border-radius:8px'>URGENT HIRING</span></div>
 <div style='font:400 50px Anton;color:#fff;letter-spacing:3px;margin-top:16px;line-height:1'>JOBS AT</div>
 <div style='font:400 104px Anton;color:#fff;letter-spacing:2px;line-height:1;text-shadow:0 8px 22px #0007'>DUBAI AIRPORT</div>
 <div style='font:700 22px Archivo;color:#DCEBFA;margin-top:12px'>With a leading airline group at Dubai International Airport</div></div>
<div class='abs' style='top:120px;right:36px;width:290px;height:330px;border-radius:24px;overflow:hidden;border:5px solid #fff;box-shadow:0 18px 36px #0008'>
 <img src='{hero}' style='width:100%;height:100%;object-fit:cover;object-position:center 22%'></div>

<div class='abs' style='top:500px;left:36px;right:36px;border-radius:20px;overflow:hidden;background:#11161F;box-shadow:0 20px 40px #000a;border:2px solid #232A36'>
 <div style='display:flex;align-items:center;height:52px;padding:0 20px;background:#1B2230;font:800 15px Archivo;color:{AMBER};letter-spacing:3px'>
  {icon('plane', 24, AMBER, 2)}<span style='margin-left:12px;flex:1'>DEPARTURES · POSITIONS</span><span style='width:190px;text-align:right'>SALARY / MONTH</span><span style='width:300px;text-align:right'>REMARKS</span></div>
 {rows}</div>

<div class='abs' style='top:1028px;left:36px;right:36px;height:110px;display:flex;gap:14px'>
 <div style='flex:1;background:#fff;border-radius:16px;display:flex;align-items:center;gap:12px;padding:0 18px'>{icon('user', 34, NAVY, 2.2)}<div><div style='font:800 14px Archivo;color:#5A6A80;letter-spacing:2px'>AGE</div><div style='font:400 32px Anton;color:{NAVY}'>21 – 40 YEARS</div></div></div>
 <div style='flex:1.3;background:{AMBER};border-radius:16px;display:flex;align-items:center;gap:12px;padding:0 18px'>{icon('calendar', 34, NAVY2, 2.2)}<div><div style='font:800 14px Archivo;color:{NAVY2};letter-spacing:2px'>INTERVIEWS</div><div style='font:400 28px Anton;color:{NAVY2};white-space:nowrap'>10 – 13 NOV 2026</div></div></div>
 <div style='flex:1.25;background:{RED};border-radius:16px;display:flex;align-items:center;gap:12px;padding:0 18px'>{icon('shield', 34, '#fff', 2.2)}<div><div style='font:800 14px Archivo;color:#FFD9DB;letter-spacing:1px'>ALL CANDIDATES MUST HAVE</div><div style='font:400 25px Anton;color:#fff'>PCC · MOFA ATTESTED</div></div></div></div>

<div class='abs' style='top:1166px;left:0;width:1080px;height:184px;background:#050C1C;border-top:4px solid {AMBER}'></div>
<div class='abs' style='top:1194px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1192px;right:40px;width:380px;text-align:right'>
 <div style='font:400 40px Anton;color:{AMBER};letter-spacing:1px;line-height:1.05'>APPLY NOW!</div>
 <div style='font:700 19px Archivo;color:#C9D3E0;margin-top:6px'>Send your CV on WhatsApp</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{NAVY}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Dubai-Airport-Jobs-English.png"))
