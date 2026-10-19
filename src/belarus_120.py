"""Belarus — 120 workers, 7 trades, English (2026-10-19). Facts: demands/2026-10-19-belarus-120/facts.md (from the
user's demand-letter PDF; employer not named). Design: "green ledger" — deep-green hero with Belarus ornament band,
framed real RS Links photo, red 120-posts seal; full vacancy table with salary chips; benefits grid + requirements
card; white CTA strip with all three numbers.
v2 (user): re-checked against the document; added visa-process steps and required-documents list in the style of the
user's previous RS Links Belarus ad (output/RS-Links-Belarus-Factory-Workers-English-Final.png). Where the two differ,
the demand letter wins (passport validity 2+ years, contract 3 years, salaries)."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

GRN, GRN2, RED, CREAM, INK, GOLD = "#0B4D2C", "#08371F", "#C8102E", "#F7F4EC", "#16201B", "#F2C14E"
EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"

JOBS = [("Machine Milking Operators", "Men / Women", "10", "Mogilev", "700 – 800"),
        ("General Labourers – Dairy Plant", "Men", "6", "Mogilev", "700 – 800"),
        ("Woodworking &amp; Production Workers", "", "20", "Berezino, Minsk Region", "800 – 1,100"),
        ("Poultry Processing Plant Workers", "", "40", "Minsk", "1,000 – 1,600"),
        ("Agricultural &amp; Harvesting Workers", "Men only", "10", "Mogilev Region", "600 – 1,200"),
        ("Bakery Production Workers", "Men / Women", "30", "Borisov, Minsk Region", "700 – 850"),
        ("Facility Cleaners", "Women", "4", "Borisov, Minsk Region", "600 – 750")]

BENEFITS = [("home", "Free accommodation"), ("food", "3 meals a day or meal allowance"), ("bus", "Free transport to &amp; from work"),
            ("plane", "Ticket to Belarus + ticket after 2 years"), ("medical", "Medical insurance"),
            ("calendar", "24 days paid annual leave"), ("overtime", "Overtime at least double hourly rate"),
            ("idcard", "Airport pickup &amp; residence permit help")]
FACTS = [("user", "Age 21 – 45"), ("doc", "3-year contract (renewable)"), ("visa", "Work visa + work permit"),
         ("clock", "40 h/week · max 12-h shift")]
STEPS = ["Send CV &amp; documents", "Shortlisting", "Employer approval", "Visa invitation", "Visa via Belarus Embassy", "Travel &amp; start work"]
DOCS = ["CV / Resume", "Passport (2+ yrs validity)", "CNIC copy", "White-background photos", "Police Clearance (PCC)",
        "Medical fitness certificate", "Matric (where required)", "Experience certificates"]


def ornament(w, h, c1, c2):
    """Belarusian rushnyk-style band: repeating diamonds and crosses."""
    s, step = "", h
    for x in range(0, w + step, step):
        m = h / 2
        s += (f"<path d='M{x} {m} L{x + m} 0 L{x + h} {m} L{x + m} {h}Z' fill='{c1}'/>"
              f"<path d='M{x + m * .55} {m} L{x + m} {m * .45} L{x + h - m * .55} {m} L{x + m} {h - m * .45}Z' fill='{c2}'/>"
              f"<rect x='{x + m - 2}' y='{m - 2}' width='4' height='4' fill='{c1}'/>")
    return f"<svg width='{w}' height='{h}' style='display:block'>{s}</svg>"


def build():
    photo = (PHOTOS / "rslinks_worker_pack_x3.png").as_uri()
    rows = "".join(
        f"<div style='display:flex;align-items:center;height:50px;padding:0 18px;background:{'#fff' if i % 2 == 0 else '#EEF4EF'};border-bottom:1px solid #DCE6DE'>"
        f"<span style='width:32px;height:32px;border-radius:50%;background:{GRN};color:#fff;font:800 16px Archivo;display:flex;align-items:center;justify-content:center;flex:none'>{i + 1}</span>"
        f"<div style='flex:1;margin-left:14px;line-height:1.12'><div style='font:800 20px Archivo;color:{INK}'>{t}</div>"
        + (f"<div style='font:600 15px Archivo;color:{RED}'>{g}</div>" if g else "") + "</div>"
        f"<div style='width:70px;text-align:center;font:400 28px Anton;color:{GRN}'>{q}</div>"
        f"<div style='width:230px;display:flex;align-items:center;gap:6px;font:700 17px Archivo;color:#3C4A42'>{icon('pin', 18, RED, 2.4)}{loc}</div>"
        f"<div style='width:190px;text-align:right'><span style='display:inline-block;background:{GOLD};border-radius:10px;padding:2px 10px;font:400 23px Anton;color:{INK};letter-spacing:.5px'>${sal}</span></div></div>"
        for i, (t, g, q, loc, sal) in enumerate(JOBS))
    head = (f"<div style='display:flex;align-items:center;height:40px;padding:0 18px;background:{GRN};font:800 15px Archivo;color:#fff;letter-spacing:1px'>"
            f"<div style='flex:1;margin-left:46px'>POSITION</div><div style='width:70px;text-align:center'>POSTS</div>"
            f"<div style='width:230px;padding-left:24px;box-sizing:border-box'>LOCATION</div><div style='width:190px;text-align:right'>NET SALARY / MONTH</div></div>")
    facts = "".join(f"<div style='flex:1;display:flex;align-items:center;justify-content:center;gap:8px;background:#fff;border-radius:12px;border:2px solid {GRN}33;font:800 16px Archivo;line-height:1.15;text-align:left;color:{INK}'>{icon(ic, 22, RED, 2.3)}{t}</div>" for ic, t in FACTS)
    steps = "".join(f"<div style='flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;position:relative'>"
                    f"<span style='width:36px;height:36px;border-radius:50%;background:{GOLD if i == 5 else '#fff'};color:{GRN};font:400 21px Anton;display:flex;align-items:center;justify-content:center;z-index:1'>{i + 1}</span>"
                    f"<div style='font:700 15px Archivo;color:#fff;line-height:1.15;margin-top:4px'>{t}</div></div>" for i, t in enumerate(STEPS))
    ben = "".join(f"<div style='display:flex;align-items:center;gap:9px'><span style='width:34px;height:34px;border-radius:9px;background:{GRN};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 20, '#fff', 2.2)}</span>"
                  f"<span style='font:700 16px Archivo;color:{INK};line-height:1.15'>{t}</span></div>" for ic, t in BENEFITS)
    docs = "".join(f"<div style='display:flex;align-items:center;gap:7px;font:600 16px Archivo;color:#E9F2EC;line-height:1.15'>{icon('check', 17, GOLD, 3)}<span>{d}</span></div>" for d in DOCS)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 28px Anton;color:{INK};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:362px;background:radial-gradient(circle at 75% 40%,#13703F,{GRN} 45%,{GRN2})'></div>
<div class='abs' style='top:0;left:0'>{ornament(1080, 24, RED, '#fff')}</div>
<div class='abs' style='top:40px;left:36px;background:#fff;border-radius:16px;padding:4px 14px;box-shadow:0 6px 16px #0006'>{logo_img('logo-horizontal-light', 'width:300px;height:76px;object-position:left')}</div>
<div class='abs' style='top:140px;left:40px;display:flex;align-items:center;gap:14px'>
 <div style='filter:drop-shadow(0 4px 8px #0006)'>{flag('by', 84, True, 'by120')}</div>
 <div style='background:{RED};border-radius:10px;padding:4px 14px;font:800 19px Archivo;color:#fff;letter-spacing:2px'>URGENT REQUIREMENT</div></div>
<div class='abs' style='top:196px;left:38px;font:400 78px Anton;color:#fff;letter-spacing:2px;line-height:1'>WORK IN BELARUS</div>
<div class='abs' style='top:286px;left:40px;font:700 19px Archivo;color:#CFE6D6;line-height:1.45;width:620px'>Dairy · Woodworking · Poultry · Agriculture · Bakery · Cleaning<br><span style='color:{GOLD}'>Minsk, Minsk Region &amp; Mogilev Region</span></div>
<div class='abs' style='top:38px;right:40px;width:340px;height:296px;border-radius:24px;overflow:hidden;border:6px solid #fff;box-shadow:0 18px 34px #0008'><img src='{photo}' style='width:100%;height:100%;object-fit:cover;object-position:55% 40%'></div>
<div class='abs' style='top:20px;right:318px;width:124px;height:124px;border-radius:50%;background:{RED};border:5px solid #fff;box-shadow:0 10px 22px #0007;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-8deg)'>
 <div style='font:400 48px Anton;color:#fff;line-height:1'>120</div><div style='font:800 16px Archivo;color:#fff;letter-spacing:2px'>POSTS</div></div>

<div class='abs' style='top:376px;left:30px;right:30px;border-radius:16px;overflow:hidden;box-shadow:0 10px 24px rgba(11,77,44,.18)'>{head}{rows}</div>
<div class='abs' style='top:772px;left:34px;right:34px;font:italic 600 14px Archivo;color:#5A6A60;line-height:1.3'>Net salary = paid to the worker after income tax &amp; statutory deductions; paid monthly in Belarusian Rubles (BYN), USD amounts are indicative. Upper end depends on trade, hours &amp; schedule.</div>
<div class='abs' style='top:816px;left:30px;right:30px;height:42px;display:flex;gap:10px'>{facts}</div>

<div class='abs' style='top:868px;left:30px;right:30px;height:82px;border-radius:16px;background:{RED};display:flex;align-items:center;padding:0 14px;box-sizing:border-box'>
 <div style='font:400 24px Anton;color:#fff;letter-spacing:1px;line-height:1;width:96px;flex:none'>VISA<br>PROCESS</div>
 <div style='flex:1;display:flex;position:relative'><div style='position:absolute;left:7%;right:7%;top:17px;height:2px;background:#ffffff88'></div>{steps}</div></div>

<div class='abs' style='top:958px;left:30px;width:556px;height:228px;background:#fff;border-radius:16px;border-top:6px solid {RED};box-shadow:0 8px 18px rgba(0,0,0,.08);padding:6px 16px;box-sizing:border-box'>
 <div style='font:400 24px Anton;color:{GRN};letter-spacing:1px'>PROVIDED BY THE COMPANY</div>
 <div style='display:grid;grid-template-columns:1fr 1fr;gap:7px 12px;margin-top:4px'>{ben}</div></div>
<div class='abs' style='top:958px;right:30px;width:450px;height:228px;background:{GRN};border-radius:16px;border-top:6px solid {GOLD};padding:6px 18px;box-sizing:border-box'>
 <div style='font:400 24px Anton;color:#fff;letter-spacing:1px'>REQUIRED DOCUMENTS</div>
 <div style='display:grid;grid-template-columns:1fr 1fr;gap:12px 10px;margin-top:10px'>{docs}</div></div>

<div class='abs' style='top:1194px;left:0;width:1080px;height:156px;background:{GRN2}'></div>
<div class='abs' style='top:1194px;left:0'>{ornament(1080, 14, RED, '#fff')}</div>
<div class='abs' style='top:1212px;left:30px;height:126px;padding:0 20px;background:#fff;border-radius:18px;display:flex;flex-direction:column;justify-content:center'>{nums}</div>
<div class='abs' style='top:1220px;right:34px;width:500px;text-align:right'>
 <div style='font:400 38px Anton;color:{GOLD};letter-spacing:1px;line-height:1.1'>SEND YOUR CV ON WHATSAPP</div>
 <div style='font:700 19px Archivo;color:#E2EFE6;margin-top:6px'>Apply now with your CV &amp; documents</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px'>{icon('mail', 22, GOLD, 2)}<span style='font:800 22px Archivo;color:#fff'>{EMAIL}</span></div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:6px;margin-top:6px'>{icon('pin', 18, GOLD, 2.2)}<span style='font:600 14px Archivo;color:#C9DCCF'>{ADDRESS}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CREAM}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Belarus-120-Workers-English.png"))
