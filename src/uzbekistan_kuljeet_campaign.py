"""Uzbekistan — consolidated multi-position ad, English (2026-11-17). Partner campaign (ref: Kuljeet; sheet only).
Facts from the partner sheet (UZBEKISTAN DEMAND WITH RAHIM SIR.xlsx): 10 categories, age 21–42, unlimited posts;
taxi drivers $900–1,100, bike riders $1,000–1,300, cyclists $900–1,100 (accommodation & food self); factory workers
$400–500, tailors $500–600, PIR panel chemical technologist / PIR line operator / basalt line operator / basalt line
mechanic $1,500 (accommodation & food by company); teachers $3,000–5,000 (self). All salaries approximate.
Documents: passport front/back scan (PDF), national ID, studio photo. Candidate arranges own ticket.
From partner's reference ad: min. 3 years experience for PIR/basalt roles. Service charges, embassy/settlement fees
and payment terms are internal (briefs/sheet only). Dropped from reference ads: visa wording, "visit to work",
"100% legal", "limited seats", "for Indian/Bangladeshi" lines, slogans.
Design: "Registan majolica" — Registan photo header, cobalt page with faint girih-star tile pattern, four white
category cards (drivers & riders / factory & tailoring / industrial / teachers) each with a photo strip, role list
with saffron salary chips and an accommodation tag, saffron document bar, cobalt footer with six numbers."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

COB, COB2, TQ, SAF, SAF2, CREAM, INK = "#1B3A8C", "#0F2463", "#12A3B5", "#F5A623", "#FFD27A", "#FBF6EC", "#0F2463"
EMAIL = "hr@rslinksconsultants.com"


def tile_bg():
    star = ("<svg xmlns='http://www.w3.org/2000/svg' width='90' height='90'><g fill='none' stroke='%23ffffff' stroke-opacity='.07' stroke-width='2'>"
            "<path d='M45 5 L55 35 L85 45 L55 55 L45 85 L35 55 L5 45 L35 35Z'/><rect x='25' y='25' width='40' height='40' transform='rotate(45 45 45)'/></g></svg>")
    return f"url(\"data:image/svg+xml;utf8,{star}\")"


def card(title, photos, roles, tag, tag_col, note=""):
    ph = "".join(f"<div style='flex:1;height:142px;border-radius:12px;overflow:hidden'><img src='{(PHOTOS / f).as_uri()}' style='width:100%;height:100%;object-fit:{fit};object-position:{pos};background:#EEF1F6'></div>" for f, pos, fit in photos)
    rl = "".join(f"<div style='display:flex;align-items:center;justify-content:space-between;gap:10px;border-bottom:1px dashed #D8DEEA;padding:4px 0'>"
                 f"<span style='font:800 18.5px Archivo;color:{INK};line-height:1.15'>{r}</span>"
                 f"<span style='background:{SAF};color:{INK};font:400 22px Anton;padding:1px 10px;border-radius:8px;white-space:nowrap'>{s}</span></div>" for r, s in roles)
    return (f"<div style='background:#fff;border-radius:20px;padding:12px 12px 14px;box-sizing:border-box;box-shadow:0 14px 28px #0007;display:flex;flex-direction:column'>"
            f"<div style='display:flex;gap:8px'>{ph}</div>"
            f"<div style='font:400 28px Anton;color:{COB};letter-spacing:1px;margin:8px 2px 2px'>{title}</div>{rl}"
            f"<div style='margin-top:auto;padding-top:8px;display:flex;align-items:center;justify-content:space-between;gap:8px'>"
            f"<span style='background:{tag_col};color:#fff;font:800 15px Archivo;padding:5px 10px;border-radius:999px'>{tag}</span>"
            f"<span style='font:700 15px Archivo;color:#55607A'>{note}</span></div></div>")


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    a = card("DRIVERS &amp; RIDERS", [("driver_taxi.jpg", "center 40%", "cover"), ("kw_rider.jpg", "center 30%", "cover"), ("uz_ecycle_rider_ref.jpg", "center 30%", "cover")],
             [("Taxi Drivers", "$900 – 1,100"), ("Bike Riders", "$1,000 – 1,300"), ("Cyclists", "$900 – 1,100")], "Accommodation &amp; food: self", "#6B7280", "Valid licence for drivers")
    b = card("FACTORY &amp; TAILORING", [("uz_factory_line_ref.jpg", "center 35%", "cover"), ("kg_tailor_juki.jpg", "62% 30%", "cover")],
             [("Factory Workers", "$400 – 500"), ("Tailors", "$500 – 600")], "Accommodation &amp; food: by company", "#1E9E55")
    c = card("INDUSTRIAL PLANT", [("uz_pir_1_ref.jpg", "center 30%", "cover"), ("uz_pir_2_ref.jpg", "center 30%", "cover"), ("uz_pir_4_ref.jpg", "center 30%", "cover")],
             [("PIR Panel Chemical Technologist", "$1,500"), ("PIR Panel Line Operator", "$1,500"), ("Basalt Line Operator", "$1,500"), ("Basalt Line Mechanic", "$1,500")],
             "Accommodation &amp; food: by company", "#1E9E55", "Min. 3 yrs experience")
    d = card("ENGLISH TEACHERS", [("teacher_man.jpg", "center", "contain"), ("teacher_woman.jpg", "center 30%", "cover")],
             [("English Teachers", "$3,000 – 5,000")], "Accommodation &amp; food: self", "#6B7280")
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:{COB};background-image:{tile_bg()}'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:330px;overflow:hidden'><img src='{P("uz_registan_ref.jpg")}' style='width:100%;height:100%;object-fit:cover;object-position:center 45%'>
 <div style='position:absolute;inset:0;background:linear-gradient(90deg,{COB2}f2 0%,{COB2}bb 45%,{COB2}22 75%),linear-gradient(0deg,{COB} 0%,{COB}00 25%)'></div></div>
<div class='abs' style='top:22px;left:30px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0006'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:left')}</div>
<div class='abs' style='top:24px;right:30px;filter:drop-shadow(0 6px 10px #0007)'>{flag('uzbekistan', 120, True, 'uzk')}</div>
<div class='abs' style='top:104px;left:40px;width:1000px'>
 <div style='display:inline-block;background:{SAF};color:{INK};font:800 18px Archivo;letter-spacing:4px;padding:6px 14px;border-radius:6px'>URGENT HIRING · 10 POSITIONS</div>
 <div style='font:400 84px Anton;color:#fff;line-height:1;letter-spacing:2px;margin-top:8px'>WORK IN <span style='color:{SAF2}'>UZBEKISTAN</span></div>
 <div style='font:700 21px Archivo;color:#DDE5F7;margin-top:8px'>Multiple vacancies · Age 21 – 42 · Salaries approx. (USD / month)</div></div>

<div class='abs' style='top:300px;left:24px;right:24px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:376px 414px;gap:14px'>{a}{b}{c}{d}</div>

<div class='abs' style='top:1120px;left:24px;right:24px;height:58px;border-radius:14px;background:linear-gradient(90deg,{SAF},{SAF2});display:flex;align-items:center;justify-content:center;gap:12px;font:800 18px Archivo;color:{INK}'>
 {icon('doc', 26, INK, 2.3)}Documents: Passport (front &amp; back scan, PDF) · CNIC · Studio photo &nbsp;|&nbsp; Ticket arranged by candidate</div>

<div class='abs' style='top:1188px;left:0;width:1080px;height:162px;background:{COB2}'></div>
<div class='abs' style='top:1188px;left:0;width:1080px;height:5px;background:linear-gradient(90deg,{TQ},{SAF},{TQ})'></div>
<div class='abs' style='top:1206px;left:30px;right:30px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:8px 0'>{nums}</div>
<div class='abs' style='top:1302px;left:30px;right:30px;display:flex;justify-content:space-between;align-items:center'>
 <span style='font:400 28px Anton;color:{SAF2};letter-spacing:1px'>SEND YOUR CV ON WHATSAPP</span>
 <span style='display:flex;align-items:center;gap:8px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 21px Archivo;color:#fff'>{EMAIL}</span></span></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{COB}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Uzbekistan-10-Positions-Campaign.png"))
