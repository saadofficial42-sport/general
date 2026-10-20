"""Belarus — one ad per trade (7 ads), English (2026-10-20). Facts: demands/2026-10-19-belarus-120/facts.md, taken
from the user's demand letter (same PDF re-sent 2026-10-20); employer not named. Each ad needs a REAL photo of that
trade at assets/photos/by_<slug>.(jpg|png); a missing photo stops the render instead of falling back to a drawing.
Design: Belarus-red/green poster series — big full-bleed trade photo with giant BELARUS wordmark + waving flag,
ornament band, salary burst, duties / requirements / benefits, all four numbers. Each ad gets its own accent palette
and alternates the photo side, so the seven read as a set without looking identical."""
import sys

from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

RED, GRN, INK, CREAM = "#C8102E", "#00843D", "#14181C", "#FBF8F2"
EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"

# Common terms (letter sections 2, 5, 6, 7).
BENEFITS = [("home", "Free accommodation"), ("food", "3 meals a day or meal allowance"), ("bus", "Free transport to &amp; from work"),
            ("plane", "Ticket to Belarus + ticket after 2 years"), ("medical", "Medical insurance"), ("calendar", "24 days paid annual leave"),
            ("overtime", "Overtime at least double hourly rate"), ("idcard", "Airport pickup, registration &amp; residence permit")]
DOCS = "CV · Passport (2+ yrs validity) · CNIC · Photos · PCC · Medical fitness · Experience certificates"

ROLES = [
    dict(slug="milking", title="MACHINE MILKING OPERATORS", who="Men &amp; Women", posts=10, city="Mogilev", sal="700 – 800",
         accent="#0E6BA8", duties=["Machine milking at a dairy plant", "2/2 shift rotation, 12-hour shifts (year-round)",
                                     "Free dormitory &amp; meals at the production site"],
         reqs=["Age 21 – 45 years", "1+ year livestock / dairy experience preferred", "On-site training provided",
               "Matric (Secondary School Certificate)", "Medical fitness"]),
    dict(slug="dairy", title="GENERAL LABOURERS – DAIRY PLANT", who="Men", posts=6, city="Mogilev", sal="700 – 800",
         accent="#2E7D32", duties=["General labour at a dairy plant", "2/2 shift rotation, 12-hour shifts (year-round)",
                                     "Free dormitory &amp; meals at the production site"],
         reqs=["Age 21 – 45 years", "No experience required", "Literate", "Medical fitness"]),
    dict(slug="woodworking", title="WOODWORKING &amp; PRODUCTION WORKERS", who="", posts=20, city="Berezino, Minsk Region", sal="800 – 1,100",
         accent="#8D5524", duties=["Pallet assembly, sawdust pressing, wood processing", "Facility cleaning, painting &amp; quality control",
                                     "2/2 or by agreement, 12-hour shifts", "Houses for 4–6 people (separate quarters for couples)"],
         reqs=["Age 21 – 45 years", "1+ year pallet assembly, sawmill or wood processing", "Matric; able to use hand / power tools"]),
    dict(slug="poultry", title="POULTRY PROCESSING PLANT WORKERS", who="", posts=40, city="Minsk", sal="1,000 – 1,600",
         accent="#C8102E", duties=["Production line work, deboning, cutting", "Portioning (legs, wings) &amp; sorting",
                                     "2/2, 4/2 or 3/1 by agreement, 12-hour shifts", "Free dormitory: 2 per room (separate rooms for couples)"],
         reqs=["Age 21 – 45 years", "1+ year meat / poultry processing preferred", "Matric (Secondary School Certificate)", "Medical fitness"]),
    dict(slug="agriculture", title="AGRICULTURAL &amp; HARVESTING WORKERS", who="Men only", posts=10, city="Mogilev Region", sal="600 – 1,200",
         accent="#6A8E23", duties=["Harvesting crops (cabbage, potatoes)", "General farm work, crop handling, loading &amp; unloading",
                                     "5/2 or 6/1, 8–12 hours per day", "Free dormitory: 2 per room (separate rooms for couples)"],
         reqs=["Age 21 – 45 years", "1+ year farm work preferred", "Literate; good physical health"]),
    dict(slug="bakery", title="BAKERY PRODUCTION WORKERS", who="Men &amp; Women", posts=30, city="Borisov, Minsk Region", sal="700 – 850",
         accent="#D9822B", duties=["General work in bakery production", "2/2 shift rotation, 12-hour shifts", "Free dormitory housing"],
         reqs=["Age 21 – 45 years", "No experience required", "Literate", "Medical fitness"]),
    dict(slug="cleaners", pos="center 6%", title="FACILITY CLEANERS", who="Women", posts=4, city="Borisov, Minsk Region", sal="600 – 750",
         accent="#7B3FA0", duties=["Cleaning of production premises (bakery)", "2/2 shift rotation, 12-hour shifts", "Free dormitory housing"],
         reqs=["Age 21 – 45 years", "No experience required", "Literate", "Medical fitness"]),
]


def photo_uri(slug):
    for e in ("jpg", "jpeg", "png", "webp"):
        p = PHOTOS / f"by_{slug}.{e}"
        if p.exists():
            return p.as_uri()
    return None


def ornament(w, h, c1, c2):
    s, m = "", h / 2
    for x in range(0, w + h, h):
        s += (f"<path d='M{x} {m} L{x + m} 0 L{x + h} {m} L{x + m} {h}Z' fill='{c1}'/>"
              f"<path d='M{x + m * .55} {m} L{x + m} {m * .45} L{x + h - m * .55} {m} L{x + m} {h - m * .45}Z' fill='{c2}'/>")
    return f"<svg width='{w}' height='{h}' style='display:block'>{s}</svg>"


def build(r, i, uri):
    A = r["accent"]
    flip = i % 2 == 1          # alternate the photo / title side
    side, other = ("right", "left") if flip else ("left", "right")
    grad = f"linear-gradient({'270' if flip else '90'}deg,{INK}F2 0%,{INK}B0 38%,{INK}00 70%)"
    who = (f"<span style='display:inline-block;background:#fff;color:{RED};font:800 20px Archivo;border-radius:8px;padding:4px 12px;margin-top:12px'>{r['who'].upper()}</span>"
           if r["who"] else "")
    duty_li = "".join(f"<div style='display:flex;gap:10px;align-items:flex-start;margin-top:13px'>{icon('check', 22, A, 3)}<span style='font:700 20px Archivo;color:{INK};line-height:1.25'>{d}</span></div>" for d in r["duties"])
    req_li = "".join(f"<div style='display:flex;gap:10px;align-items:flex-start;margin-top:12px'>{icon('user' if k == 0 else 'check', 22, '#fff', 2.6)}<span style='font:700 20px Archivo;color:#fff;line-height:1.25'>{d}</span></div>" for k, d in enumerate(r["reqs"]))
    ben = "".join(f"<div style='display:flex;align-items:center;gap:8px'><span style='width:32px;height:32px;border-radius:8px;background:{A};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 19, '#fff', 2.2)}</span>"
                  f"<span style='font:700 15px Archivo;color:{INK};line-height:1.15'>{t}</span></div>" for ic, t in BENEFITS)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:7px'>{whatsapp_icon(30)}<span style='font:400 27px Anton;color:{INK};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:640px;overflow:hidden'><img src='{uri}' style='width:100%;height:100%;object-fit:cover;object-position:{r.get("pos", "center 35%")}'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:640px;background:{grad}'></div>
<div class='abs' style='top:470px;left:0;width:1080px;height:170px;background:linear-gradient(180deg,{INK}00,{INK}CC)'></div>
<div class='abs' style='top:0;left:0'>{ornament(1080, 22, RED, '#fff')}</div>
<div class='abs' style='top:38px;{side}:34px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 16px #0007'>{logo_img('logo-horizontal-light', f'width:290px;height:74px;object-position:{side}')}</div>
<div class='abs' style='top:36px;{other}:34px;filter:drop-shadow(0 6px 12px #0009)'>{flag('by', 150, True, f'byr{i}')}</div>
<div class='abs' style='top:150px;{side}:40px;width:640px;text-align:{side}'>
 <div style='display:inline-block;background:{RED};color:#fff;font:800 20px Archivo;letter-spacing:3px;padding:6px 14px;border-radius:8px'>URGENT REQUIREMENT · {r['posts']} POSTS</div>
 <div style='font:400 150px Anton;line-height:.95;letter-spacing:4px;margin-top:10px;color:transparent;-webkit-text-stroke:3px #fff;text-shadow:0 0 0 #fff0'>BELARUS</div>
 <div style='font:400 {54 if len(r['title']) < 26 else 44}px Anton;color:#fff;line-height:1.02;letter-spacing:1px;margin-top:6px;text-shadow:0 4px 14px #000a'>{r['title']}</div>
 {who}
 <div style='display:flex;align-items:center;gap:8px;margin-top:12px;justify-content:{'flex-end' if flip else 'flex-start'}'>{icon('pin', 26, '#FFD54F', 2.4)}<span style='font:800 24px Archivo;color:#fff'>{r['city']}, Belarus</span></div></div>
<div class='abs' style='top:500px;{other}:40px;min-width:300px;padding:0 22px;box-sizing:border-box;height:118px;border-radius:20px;background:linear-gradient(135deg,#FFE27A,#F5B700);box-shadow:0 12px 26px #000a;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate({'3' if flip else '-3'}deg)'>
 <div style='font:800 15px Archivo;color:{INK};letter-spacing:2px'>NET SALARY / MONTH</div>
 <div style='font:400 54px Anton;color:{RED};line-height:1.05'>${r['sal']}</div></div>

<div class='abs' style='top:640px;left:0;width:1080px;height:8px;background:linear-gradient(90deg,{RED} 0 66%,{GRN} 66%)'></div>
<div class='abs' style='top:666px;left:30px;width:520px;height:286px;background:#fff;border-radius:18px;border-top:6px solid {A};box-shadow:0 8px 20px rgba(0,0,0,.1);padding:10px 20px;box-sizing:border-box'>
 <div style='font:400 28px Anton;color:{A};letter-spacing:1px'>THE JOB</div>{duty_li}</div>
<div class='abs' style='top:666px;right:30px;width:476px;height:286px;background:{A};border-radius:18px;padding:10px 20px;box-sizing:border-box;box-shadow:0 8px 20px rgba(0,0,0,.15)'>
 <div style='font:400 28px Anton;color:#fff;letter-spacing:1px'>REQUIREMENTS</div>{req_li}
 <div style='margin-top:16px;font:800 18px Archivo;color:#FFE27A'>3-year contract (renewable) · Work visa + work permit</div></div>
<div class='abs' style='top:966px;left:30px;right:30px;height:168px;background:#fff;border-radius:18px;box-shadow:0 8px 20px rgba(0,0,0,.08);padding:8px 18px;box-sizing:border-box'>
 <div style='font:400 24px Anton;color:{GRN};letter-spacing:1px'>PROVIDED BY THE COMPANY</div>
 <div style='display:grid;grid-template-columns:repeat(4,1fr);gap:8px 12px;margin-top:6px'>{ben}</div></div>
<div class='abs' style='top:1140px;left:34px;right:34px;font:600 14px Archivo;color:#59616A;line-height:1.3'><b style='color:{INK}'>Documents:</b> {DOCS}. Net salary paid monthly in BYN; USD amounts indicative.</div>

<div class='abs' style='top:1180px;left:0;width:1080px;height:170px;background:linear-gradient(100deg,{GRN},#005A2B)'></div>
<div class='abs' style='top:1180px;left:0'>{ornament(1080, 14, RED, '#fff')}</div>
<div class='abs' style='top:1206px;left:26px;width:560px;height:128px;background:#fff;border-radius:18px;display:grid;grid-template-columns:1fr 1fr;align-content:center;gap:8px 10px;padding:0 16px;box-sizing:border-box;box-shadow:0 8px 18px #0006'>{nums}</div>
<div class='abs' style='top:1206px;right:32px;width:440px;text-align:right'>
 <div style='font:400 36px Anton;color:#FFE27A;letter-spacing:1px;line-height:1.05'>SEND YOUR CV ON WHATSAPP</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:10px'>{icon('mail', 22, '#FFE27A', 2)}<span style='font:800 21px Archivo;color:#fff'>{EMAIL}</span></div>
 <div style='font:600 13px Archivo;color:#D6EDDD;margin-top:10px;line-height:1.3'>{ADDRESS}</div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CREAM}'>{body}</div></body></html>")


if __name__ == "__main__":
    only = sys.argv[1:]
    missing = []
    for i, r in enumerate(ROLES):
        if only and r["slug"] not in only:
            continue
        uri = photo_uri(r["slug"])
        if not uri:
            missing.append(f"assets/photos/by_{r['slug']}.jpg")
            continue
        print(render(build(r, i, uri), f"RS-Links-Belarus-{r['slug'].capitalize()}-English.png"))
    if missing:
        print("Missing real photos (not rendered):", ", ".join(missing))
