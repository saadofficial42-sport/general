"""Turkey — Seasonal Tourism & Hospitality jobs, English (2026-11-14). Converted from another agency's ad (content only;
Istanbul backdrop cropped from it at user request). Facts: 50 vacancies; February 2027 intake; season Feb 2027 –
Sep/Oct 2027; hotel cleaning, hotel housekeeping, dishwashers, cleaning staff for shipping companies, shipyard cleaning,
tourism & hospitality support, other related positions; €700–€800/month (varies by position, employer & selection);
employer provides official employment contract, free accommodation, food, medical facilities, Turkish Kimlik (residence
documentation), employment documentation; requirements: good English (mandatory), basic education, fresh & experienced
welcome, physically fit; selection: CV -> shortlist -> online interview. Agency: Anchor Manpower (sheet only).
Dropped: "Seasonal Work Visa" (no-visa rule), "Limited vacancies", slogans.
Design: "Bosphorus postcard" — Istanbul photo header under a Turkish-red diagonal wash with stamp-style season badge,
two big job photos with red caption tabs, deep-teal positions card + red salary ticket, benefits icon ribbon,
requirement + 3-step selection columns, teal footer."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

RED, RED2, TEAL, TEAL2, CREAM, GOLD, INK = "#E30A17", "#A80612", "#0B4F5C", "#073640", "#FFF8EE", "#F4B400", "#14232A"
EMAIL = "hr@rslinksconsultants.com"


def photo(src, pos, cap, fl=1):
    return (f"<div style='flex:{fl};position:relative'><div style='height:250px;border-radius:18px;overflow:hidden;box-shadow:0 14px 26px #14232A40'>"
            f"<img src='{src}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'></div>"
            f"<div style='position:absolute;left:16px;bottom:-18px;background:{RED};color:#fff;font:400 27px Anton;letter-spacing:1px;padding:7px 18px;border-radius:10px;box-shadow:0 8px 14px #0005'>{cap}</div></div>")


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    jobs = ["Hotel Cleaning Staff", "Hotel Housekeeping Staff", "Dishwashers", "Cleaning Staff – Shipping Companies",
            "Shipyard Cleaning Staff", "Tourism &amp; Hospitality Support Staff", "Other Related Hospitality Positions"]
    job_li = "".join(f"<div style='display:flex;align-items:center;gap:10px;font:700 18.5px Archivo;color:#fff;line-height:1.42'><span style='color:{GOLD};font:900 18px Archivo'>›</span>{j}</div>" for j in jobs)
    ben = [("doc", "Official Contract"), ("home", "Free Accommodation"), ("food", "Food"), ("medical", "Medical Facilities"),
           ("user", "Turkish Kimlik (Residence Card)"), ("check", "Employment Documentation")]
    ben_li = "".join(f"<div style='flex:1;display:flex;flex-direction:column;align-items:center;gap:6px;text-align:center;padding:0 4px;{'border-left:1.5px solid #E7D9C6;' if i else ''}'>"
                     f"<span style='width:54px;height:54px;border-radius:50%;background:{TEAL};display:flex;align-items:center;justify-content:center'>{icon(ic, 28, '#fff', 2.2)}</span>"
                     f"<span style='font:800 16px Archivo;color:{INK};line-height:1.15'>{t}</span></div>" for i, (ic, t) in enumerate(ben))
    req = ["Good English communication – <b style='color:#E30A17'>mandatory</b>", "Basic educational qualification", "Fresh &amp; experienced candidates welcome", "Physically fit for the duties"]
    req_li = "".join(f"<div style='display:flex;align-items:flex-start;gap:9px;font:600 18px Archivo;color:{INK};line-height:1.3;margin-top:6px'>{icon('check', 20, TEAL, 2.6)}<span>{r}</span></div>" for r in req)
    steps = ["Send your updated CV", "Profiles reviewed &amp; shortlisted", "Online interview"]
    step_li = "".join(f"<div style='display:flex;align-items:center;gap:10px;margin-top:7px'><span style='width:30px;height:30px;border-radius:50%;background:{RED};color:#fff;font:400 18px Anton;display:flex;align-items:center;justify-content:center;flex:none'>{i}</span><span style='font:700 18px Archivo;color:{INK}'>{s}</span></div>" for i, s in enumerate(steps, 1))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:{CREAM}'></div>
<div class='abs' style='top:0;right:0;width:620px;height:340px;overflow:hidden'><img src='{P("tr_istanbul_ref.jpg")}' style='width:100%;height:100%;object-fit:cover;object-position:center 35%'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:340px;background:linear-gradient(100deg,{RED} 0%,{RED} 44%,{RED}d9 52%,{RED}00 70%)'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:340px;background:radial-gradient(circle at 12% 120%,#ffffff22 0,transparent 40%)'></div>
<div class='abs' style='top:24px;left:30px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0004'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:left')}</div>
<div class='abs' style='top:102px;left:40px;width:600px'>
 <div style='display:flex;align-items:center;gap:16px'><span style='font:400 106px Anton;color:#fff;line-height:.9;letter-spacing:3px'>TURKEY</span><span style='filter:drop-shadow(0 6px 10px #0006)'>{flag('tr', 110, True, 'trs')}</span></div>
 <div style='font:400 40px Anton;color:{GOLD};letter-spacing:2px;margin-top:8px'>SEASONAL JOBS</div>
 <div style='font:800 23px Archivo;color:#fff;letter-spacing:2px'>TOURISM &amp; HOSPITALITY SECTOR</div>
 <div style='display:inline-block;margin-top:10px;background:#fff;color:{RED};font:800 19px Archivo;padding:5px 14px;border-radius:8px'>SEASON: FEB 2027 – SEP/OCT 2027</div></div>
<div class='abs' style='top:30px;right:36px;width:200px;height:200px;border-radius:50%;background:#fff;border:5px dashed {RED};box-shadow:0 12px 24px #0006;transform:rotate(8deg);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center'>
 <div style='font:400 64px Anton;color:{RED};line-height:.9'>50</div><div style='font:800 17px Archivo;color:{INK};letter-spacing:2px'>VACANCIES</div>
 <div style='width:120px;height:2px;background:{RED};margin:6px 0'></div><div style='font:800 15px Archivo;color:{TEAL};line-height:1.2'>FEBRUARY 2027<br>INTAKE</div></div>

<div class='abs' style='top:360px;left:30px;right:30px;display:flex;gap:22px'>{photo(P("ksa_housekeeping_men.jpg"), "center 30%", "HOTEL HOUSEKEEPING &amp; CLEANING", 1.45)}{photo(P("sa_kitchen_helper_sharp.jpg"), "center 35%", "DISHWASHERS", 1)}</div>

<div class='abs' style='top:640px;left:30px;width:560px;height:250px;border-radius:20px;background:linear-gradient(160deg,{TEAL},{TEAL2});padding:12px 22px;box-sizing:border-box;box-shadow:0 12px 24px #14232A40'>
 <div style='font:400 28px Anton;color:{GOLD};letter-spacing:2px;margin-bottom:4px'>JOB POSITIONS</div>{job_li}</div>
<div class='abs' style='top:640px;right:30px;width:440px;height:250px;border-radius:20px;background:#fff;border:3px solid {RED};box-sizing:border-box;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;box-shadow:0 12px 24px #14232A26'>
 <div style='font:800 20px Archivo;color:{TEAL};letter-spacing:3px'>SALARY PACKAGE</div>
 <div style='font:400 82px Anton;color:{RED};line-height:1;margin-top:4px'>€700 – €800</div>
 <div style='background:{GOLD};font:400 28px Anton;color:{INK};padding:2px 20px;border-radius:8px;margin-top:6px;letter-spacing:1px'>PER MONTH</div>
 <div style='font:600 16px Archivo;color:#4A5A60;margin-top:10px;padding:0 18px;line-height:1.3'>Varies by position, employer requirements &amp; selection</div></div>

<div class='abs' style='top:912px;left:30px;right:30px;height:116px;border-radius:18px;background:#fff;box-shadow:0 10px 20px #14232A1f;display:flex;align-items:center;padding:14px 8px 0'>{ben_li}</div>
<div class='abs' style='top:908px;left:50px;background:{RED};color:#fff;font:800 14px Archivo;letter-spacing:2px;padding:3px 12px;border-radius:6px;transform:translateY(-50%)'>EMPLOYER-PROVIDED BENEFITS</div>

<div class='abs' style='top:1040px;left:30px;width:540px'>
 <div style='font:400 24px Anton;color:{TEAL};letter-spacing:1.5px'>CANDIDATE REQUIREMENTS</div>{req_li}</div>
<div class='abs' style='top:1040px;right:30px;width:440px'>
 <div style='font:400 24px Anton;color:{TEAL};letter-spacing:1.5px'>SELECTION PROCEDURE</div>{step_li}</div>

<div class='abs' style='top:1222px;left:0;width:1080px;height:128px;background:linear-gradient(100deg,{TEAL2},{TEAL})'></div>
<div class='abs' style='top:1216px;left:0;width:1080px;height:6px;background:{RED}'></div>
<div class='abs' style='top:1240px;left:24px;display:grid;grid-template-columns:auto auto auto auto;gap:4px 18px'>{nums}</div>
<div class='abs' style='top:1296px;left:24px;right:24px;display:flex;justify-content:space-between;align-items:center'>
 <span style='font:400 28px Anton;color:{GOLD};letter-spacing:1px'>SEND YOUR CV ON WHATSAPP</span>
 <span style='display:flex;align-items:center;gap:8px'>{icon('mail', 20, '#fff', 2)}<span style='font:800 21px Archivo;color:#fff'>{EMAIL}</span></span></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CREAM}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Turkey-Seasonal-Tourism-Hospitality.png"))
