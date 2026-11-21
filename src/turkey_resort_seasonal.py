"""Turkey — Seasonal hotel, resort & hospitality jobs, English (2026-11-21). Converted from Anchor Manpower's ad
(content only; vacancy photos cropped from it at user request where we had none). Facts: age 20–39 for all;
cooks & assistant cooks, kitchen helpers, waiters & waiter assistants, baristas & bartenders, housemen, grounds
cleaners; male candidates; basic English mandatory; experience preferred for skilled roles; fresh accepted for
housekeeping & grounds; physically fit; valid medical certificate (diploma) mandatory; passport 1 yr validity + 2 blank
pages; salary from USD 700/month; 6 days work / 1 day off; free accommodation; 3 meals daily free; medical insurance;
work uniform; tips & extra earnings; process CV + 2–3 full-length photos -> online interview / employer casting ->
selection & processing. Dropped: "work visa", "limited", "world-class", "exciting".
Design: "Riviera tiles" — turquoise-sea gradient header with white wave edge and coral title, resort photo in an
arched frame, 3x2 white vacancy tiles with photos, coral salary disc + navy benefits card, requirement and 3-step
process columns, navy footer."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

SEA, SEA2, CORAL, CORAL2, NAVY, SAND, INK = "#0FB2C8", "#06788C", "#F2545B", "#C7303A", "#10284F", "#FFF8EE", "#10284F"
EMAIL = "hr@rslinksconsultants.com"
JOBS = [("tr_cook_ref.jpg", "center 30%", "Cooks &amp; Assistant Cooks"), ("sa_kitchen_helper_sharp.jpg", "center 30%", "Kitchen Helpers"),
        ("sa_waiter_sharp.jpg", "center 25%", "Waiters &amp; Waiter Assistants"), ("tr_barista_ref.jpg", "center 30%", "Baristas &amp; Bartenders"),
        ("tr_houseman_ref.jpg", "center 30%", "Housemen"), ("tr_grounds_ref.jpg", "center 30%", "Grounds Cleaners")]


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    tiles = "".join(f"<div style='background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 10px 20px #10284F26'>"
                    f"<div style='height:132px;overflow:hidden'><img src='{P(f)}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'></div>"
                    f"<div style='height:46px;display:flex;align-items:center;justify-content:center;font:800 19px Archivo;color:{NAVY};text-align:center;padding:0 6px;border-top:4px solid {CORAL}'>{t}</div></div>" for f, pos, t in JOBS)
    ben = ["6 days work, 1 day off", "Free accommodation", "3 meals daily – free", "Medical insurance", "Work uniform", "Tips &amp; extra earnings"]
    ben_li = "".join(f"<div style='display:flex;align-items:center;gap:8px;font:700 21px Archivo;color:#fff;line-height:1.75'>{icon('check', 18, '#7FE6F2', 2.8)}{b}</div>" for b in ben)
    req = ["Male candidates", "Basic English – <b>mandatory</b>", "Experience preferred (skilled roles)", "Freshers OK: housemen &amp; grounds",
           "Physically fit &amp; hardworking", "Valid medical cert. – <b>mandatory</b>", "Passport: 1 yr validity, 2 blank pages"]
    req_li = "".join(f"<div style='display:flex;align-items:flex-start;gap:8px;font:600 17px Archivo;color:{INK};line-height:1.25;margin-top:6px'>{icon('check', 18, SEA2, 2.8)}<span>{r}</span></div>" for r in req)
    steps = ["Send updated CV + 2–3 recent full-length photos", "Online interview or employer casting", "Selection &amp; processing"]
    step_li = "".join(f"<div style='display:flex;align-items:flex-start;gap:10px;margin-top:9px'><span style='width:30px;height:30px;border-radius:50%;background:{CORAL};color:#fff;font:400 18px Anton;display:flex;align-items:center;justify-content:center;flex:none'>{i}</span><span style='font:700 17px Archivo;color:{INK};line-height:1.3'>{s}</span></div>" for i, s in enumerate(steps, 1))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:{SAND}'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:330px;background:linear-gradient(160deg,#47D3E3 0%,{SEA} 45%,{SEA2} 100%)'></div>
<svg class='abs' style='top:290px;left:0' width='1080' height='60'><path d='M0 30 C 180 0, 360 60, 540 30 S 900 0, 1080 30 V60 H0Z' fill='{SAND}'/></svg>
<div class='abs' style='top:22px;left:30px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0003'>{logo_img('logo-horizontal-light', 'width:240px;height:62px;object-position:left')}</div>
<div class='abs' style='top:26px;left:300px;filter:drop-shadow(0 6px 10px #0005)'>{flag('tr', 100, True, 'trres')}</div>
<div class='abs' style='top:104px;left:40px;width:700px'>
 <div style='font:400 104px Anton;color:#fff;line-height:.9;letter-spacing:4px;text-shadow:0 6px 0 {SEA2}'>TURKEY</div>
 <div style='display:inline-block;background:{CORAL};color:#fff;font:400 38px Anton;letter-spacing:2px;padding:2px 16px;border-radius:10px;margin-top:8px'>SEASONAL HOTEL &amp; RESORT JOBS</div>
 <div style='display:inline-block;background:#FFE15A;color:{NAVY};font:800 21px Archivo;padding:5px 14px;border-radius:8px;margin-top:10px'>Age limit for all vacancies: 20 – 39 years</div></div>
<div class='abs' style='top:22px;right:34px;width:250px;height:300px;border-radius:125px 125px 18px 18px;overflow:hidden;border:6px solid #fff;box-shadow:0 14px 26px #0005'><img src='{P("tr_resort_ref.jpg")}' style='width:100%;height:100%;object-fit:cover'></div>

<div class='abs' style='top:350px;left:30px;right:30px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px'>{tiles}</div>

<div class='abs' style='top:752px;left:30px;width:220px;height:220px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FF8A8F,{CORAL} 55%,{CORAL2});border:6px solid #fff;box-shadow:0 14px 26px #C7303A66;display:flex;flex-direction:column;align-items:center;justify-content:center'>
 <div style='font:800 15px Archivo;color:#fff;letter-spacing:1.5px'>STARTING FROM</div><div style='font:400 74px Anton;color:#fff;line-height:1'>$700</div><div style='font:800 18px Archivo;color:#FFE15A;letter-spacing:2px'>PER MONTH</div></div>
<div class='abs' style='top:766px;left:270px;right:30px;height:190px;border-radius:20px;background:linear-gradient(135deg,{NAVY},#1C3E78);padding:16px 24px;box-sizing:border-box'>
 <div style='font:400 26px Anton;color:#7FE6F2;letter-spacing:1.5px;margin-bottom:6px'>EMPLOYMENT BENEFITS</div>
 <div style='display:grid;grid-template-columns:1fr 1fr;gap:0 16px'>{ben_li}</div></div>

<div class='abs' style='top:978px;left:30px;width:600px'>
 <div style='font:400 23px Anton;color:{SEA2};letter-spacing:1.5px'>CANDIDATE REQUIREMENTS</div>
 <div style='display:grid;grid-template-columns:1fr 1fr;gap:0 14px'>{req_li}</div></div>
<div class='abs' style='top:978px;right:30px;width:390px'>
 <div style='font:400 23px Anton;color:{SEA2};letter-spacing:1.5px'>SELECTION PROCESS</div>{step_li}</div>

<div class='abs' style='top:1196px;left:0;width:1080px;height:154px;background:linear-gradient(100deg,{NAVY},#1C3E78)'></div>
<div class='abs' style='top:1190px;left:0;width:1080px;height:6px;background:linear-gradient(90deg,{SEA},{CORAL},{SEA})'></div>
<div class='abs' style='top:1210px;left:30px;right:30px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:6px 0'>{nums}</div>
<div class='abs' style='top:1302px;left:30px;right:30px;display:flex;justify-content:space-between;align-items:center'>
 <span style='font:400 26px Anton;color:#7FE6F2;letter-spacing:1px'>SEND CV + PHOTOS ON WHATSAPP</span>
 <span style='display:flex;align-items:center;gap:8px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></span></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{SAND}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Turkey-Seasonal-Hotel-Resort.png"))
