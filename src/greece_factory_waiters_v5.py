"""Greece — Factory Workers & Waiters v5, English (2026-11-13). User sent a "Jobs in Greece (Schengen)" reference ad and
asked to use it as the reference and update our ad. Layout follows the reference: sky + Acropolis header with Greek flag,
navy curved title panel (JOBS IN / Greece / (Schengen)), two photo panels with yellow labels, navy salary bar with free
medical + accommodation, yellow processing strip + package line, required-documents checklist, navy Apply Now footer.
Facts: €1,100/month; free medical; free accommodation; work permit (tax-payer companies) + walk-in embassy appointment +
no "visa" wording (user rule); processing 3.5 months (user's figure — the reference says 2–3); documents from the reference.
Dropped from reference: slogans ("Build your better future", "Your dream job awaits"), "Work Visa Included" removed —
visa processing (the visa itself is the embassy's decision). Photos cropped from the reference (user-approved)."""
from common import PHONES, PHOTOS, font_css, icon, logo_img, render, whatsapp_icon
from greece_ecycle import flag_gr

NAVY, NAVY2, YEL, YEL2, RED, INK = "#0F2C7A", "#0A1E57", "#FFD400", "#FFC400", "#D7262E", "#0A1E57"
EMAIL = "hr@rslinksconsultants.com"


def tick(s):
    return (f"<svg width='{s}' height='{s}' viewBox='0 0 24 24'><circle cx='12' cy='12' r='11' fill='{YEL}' stroke='{NAVY}' stroke-width='1.5'/>"
            f"<path d='M6.5 12.5l3.5 3.5 7.5-8' stroke='{NAVY}' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>")


def panel(src, label, pos):
    return (f"<div style='flex:1;position:relative;padding-top:30px'>"
            f"<div style='height:290px;border-radius:20px;overflow:hidden;border:5px solid #fff;box-shadow:0 14px 28px #0A1E5740'><img src='{src}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'></div>"
            f"<div style='position:absolute;top:0;left:50%;transform:translateX(-50%);background:linear-gradient(180deg,{YEL},{YEL2});border-radius:999px;padding:6px 40px;font:800 38px Archivo;color:{NAVY};white-space:nowrap;box-shadow:0 8px 16px #0A1E5740;border:3px solid #fff'>{label}</div></div>")


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    docs = [("Scanned Coloured Passport", "(complete, all pages)"), ("CNIC", "(front &amp; back)"), ("FRC, MRC", ""),
            ("PCC – Police Clearance", "(MOFA attested)"), ("Schengen Photo", "(white background)")]
    doc_li = "".join(f"<div style='{'grid-column:1/3;' if i == 0 else ''}display:flex;align-items:center;gap:12px'>{tick(34)}<span style='font:800 25px Archivo;color:{INK}'>{a} <span style='font:600 19px Archivo;color:#3A4A6B'>{b}</span></span></div>" for i, (a, b) in enumerate(docs))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:linear-gradient(180deg,#CFE6FF 0%,#FFFFFF 30%,#FFFFFF 100%)'></div>
<div class='abs' style='top:0;right:0;width:700px;height:330px;overflow:hidden'><img src='{P("gr_acropolis_ref.jpg")}' style='width:100%;height:100%;object-fit:cover;object-position:center 30%'></div>
<svg class='abs' style='top:0;left:0' width='1080' height='350'><path d='M0 0 H560 C700 60 720 230 900 300 C960 322 1020 330 1080 332 V350 H0Z' fill='{NAVY}'/>
 <path d='M560 0 C700 60 720 230 900 300 C960 322 1020 330 1080 332' stroke='{YEL}' stroke-width='8' fill='none'/></svg>
<div class='abs' style='top:22px;left:30px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0004'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:left')}</div>
<div class='abs' style='top:24px;left:316px;transform:rotate(-4deg)'>{flag_gr(108)}</div>
<div class='abs' style='top:100px;left:40px;width:560px'>
 <div style='font:900 60px Archivo;color:#fff;letter-spacing:1px;line-height:1'>JOBS IN</div>
 <div style='font:900 128px Archivo;color:{YEL};line-height:.95;letter-spacing:-2px;text-shadow:0 6px 0 {NAVY2}'>Greece</div>
 <div style='font:800 40px Archivo;color:#fff;line-height:1.1'>(Schengen)</div></div>

<div class='abs' style='top:330px;left:30px;right:30px;display:flex;gap:24px'>{panel(P("gr_factory_ref.jpg"), "Factory Workers", "center 30%")}{panel(P("gr_waiters_ref.jpg"), "Waiters", "center 25%")}</div>

<div class='abs' style='top:676px;left:30px;right:30px;height:130px;border-radius:24px;background:linear-gradient(90deg,{NAVY2},{NAVY});display:flex;align-items:center;box-shadow:0 12px 24px #0A1E5744'>
 <div style='flex:1.25;padding-left:34px;border-right:4px solid {YEL}'><div style='font:800 30px Archivo;color:#fff'>Monthly Salary:</div><div style='font:900 74px Archivo;color:{YEL};line-height:1'>€1,100</div></div>
 <div style='flex:1;display:flex;flex-direction:column;align-items:center;gap:6px'>{icon('medical', 50, '#fff', 2.2)}<span style='font:800 22px Archivo;color:#fff;text-align:center;line-height:1.1'>Free Medical</span></div>
 <div style='flex:1;display:flex;flex-direction:column;align-items:center;gap:6px'>{icon('home', 50, '#fff', 2.2)}<span style='font:800 22px Archivo;color:#fff;text-align:center;line-height:1.1'>Free Accommodation</span></div></div>

<div class='abs' style='top:822px;left:0;right:0;height:100px;display:flex;align-items:center'>
 <div style='width:520px;height:100%;background:linear-gradient(90deg,{YEL},{YEL2});clip-path:polygon(0 0,100% 0,94% 100%,0 100%);display:flex;align-items:center;gap:16px;padding-left:34px;box-sizing:border-box'>
  {icon('clock', 56, NAVY, 2.4)}<div><div style='font:800 26px Archivo;color:{NAVY}'>Processing Time:</div><div style='font:900 40px Archivo;color:{NAVY};line-height:1'>3.5 Months</div></div></div>
 <div style='flex:1;padding-left:16px'><div style='font:800 25px Archivo;color:{NAVY}'>Work Permit + Embassy Appointment</div>
  <div style='font:italic 900 34px Archivo;color:{RED};line-height:1.15'>Included in Package</div>
  <div style='font:700 17px Archivo;color:#3A4A6B'>Work permit through tax-payer companies</div></div></div>

<div class='abs' style='top:940px;left:30px;background:{NAVY};border-radius:0 16px 16px 0;padding:8px 26px;font:800 30px Archivo;color:#fff'>Required Documents:</div>
<div class='abs' style='top:996px;left:36px;right:30px;display:grid;grid-template-columns:1fr 1fr;gap:10px 16px'>{doc_li}</div>

<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:linear-gradient(100deg,{NAVY2},{NAVY})'></div>
<div class='abs' style='top:1150px;left:0;width:1080px;height:8px;background:{YEL}'></div>
<div class='abs' style='top:1180px;left:30px;display:grid;grid-template-columns:auto auto;gap:14px 26px'>{nums}</div>
<div class='abs' style='top:1176px;right:34px;text-align:right'>
 <div style='display:inline-flex;align-items:center;gap:10px;background:linear-gradient(180deg,{YEL},{YEL2});border-radius:999px;padding:8px 30px;font:italic 900 40px Archivo;color:{NAVY};box-shadow:0 8px 16px #0006'>Apply Now »</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:16px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Greece-Factory-Workers-Waiters-v5.png"))
