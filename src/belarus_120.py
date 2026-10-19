"""Belarus — 120 workers, 7 trades, English (2026-10-19). Facts: demands/2026-10-19-belarus-120/facts.md (from the
user's demand-letter PDF; employer not named). Design: "green ledger" — deep-green hero with Belarus ornament band,
framed real RS Links photo, red 120-posts seal; full vacancy table with salary chips; benefits grid + requirements
card; white CTA strip with all three numbers."""
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

BENEFITS = [("home", "Free accommodation"), ("food", "3 meals a day or meal allowance"), ("bus", "Free transport to work"),
            ("plane", "Ticket to Belarus + ticket after 2 years"), ("medical", "Medical insurance"),
            ("calendar", "24 days paid annual leave"), ("overtime", "Overtime paid at double rate"),
            ("idcard", "Airport pickup &amp; residence permit help")]


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
        f"<div style='display:flex;align-items:center;height:56px;padding:0 18px;background:{'#fff' if i % 2 == 0 else '#EEF4EF'};border-bottom:1px solid #DCE6DE'>"
        f"<span style='width:34px;height:34px;border-radius:50%;background:{GRN};color:#fff;font:800 17px Archivo;display:flex;align-items:center;justify-content:center;flex:none'>{i + 1}</span>"
        f"<div style='flex:1;margin-left:14px;line-height:1.15'><div style='font:800 21px Archivo;color:{INK}'>{t}</div>"
        + (f"<div style='font:600 15px Archivo;color:{RED}'>{g}</div>" if g else "") + "</div>"
        f"<div style='width:70px;text-align:center;font:400 30px Anton;color:{GRN}'>{q}</div>"
        f"<div style='width:230px;display:flex;align-items:center;gap:6px;font:700 17px Archivo;color:#3C4A42'>{icon('pin', 18, RED, 2.4)}{loc}</div>"
        f"<div style='width:190px;text-align:right'><span style='display:inline-block;background:{GOLD};border-radius:10px;padding:3px 10px;font:400 24px Anton;color:{INK};letter-spacing:.5px'>${sal}</span></div></div>"
        for i, (t, g, q, loc, sal) in enumerate(JOBS))
    head = (f"<div style='display:flex;align-items:center;height:44px;padding:0 18px;background:{GRN};font:800 16px Archivo;color:#fff;letter-spacing:1px'>"
            f"<div style='flex:1;margin-left:48px'>POSITION</div><div style='width:70px;text-align:center'>POSTS</div>"
            f"<div style='width:230px;padding-left:24px;box-sizing:border-box'>LOCATION</div><div style='width:190px;text-align:right'>NET SALARY / MONTH</div></div>")
    ben = "".join(f"<div style='display:flex;align-items:center;gap:10px'><span style='width:38px;height:38px;border-radius:10px;background:{GRN};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 22, '#fff', 2.2)}</span>"
                  f"<span style='font:700 16px Archivo;color:{INK};line-height:1.15'>{t}</span></div>" for ic, t in BENEFITS)
    req = [("Age", "21 – 45 years"), ("Contract", "3 years (renewable)"), ("Visa", "Work visa + work permit"),
           ("Hours", "40 h/week · 12-hour shift rotation"), ("Education", "Matric for milking, woodworking &amp; poultry"),
           ("Documents", "CV, passport (2+ yrs valid), medical")]
    req_li = "".join(f"<div style='display:flex;gap:8px;font:600 17px Archivo;color:#E9F2EC;line-height:1.3;margin-top:7px'>{icon('check', 18, GOLD, 3)}<span><b style='color:{GOLD}'>{k}:</b> {v}</span></div>" for k, v in req)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 28px Anton;color:{INK};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:420px;background:radial-gradient(circle at 75% 40%,#13703F,{GRN} 45%,{GRN2})'></div>
<div class='abs' style='top:0;left:0'>{ornament(1080, 26, RED, '#fff')}</div>
<div class='abs' style='top:46px;left:36px;background:#fff;border-radius:16px;padding:4px 14px;box-shadow:0 6px 16px #0006'>{logo_img('logo-horizontal-light', 'width:330px;height:84px;object-position:left')}</div>
<div class='abs' style='top:158px;left:40px;display:flex;align-items:center;gap:14px'>
 <div style='filter:drop-shadow(0 4px 8px #0006)'>{flag('by', 96, True, 'by120')}</div>
 <div style='background:{RED};border-radius:10px;padding:4px 14px;font:800 20px Archivo;color:#fff;letter-spacing:2px'>URGENT REQUIREMENT</div></div>
<div class='abs' style='top:222px;left:38px;font:400 80px Anton;color:#fff;letter-spacing:2px;line-height:1'>WORK IN BELARUS</div>
<div class='abs' style='top:318px;left:40px;font:700 21px Archivo;color:#CFE6D6;line-height:1.4;width:600px'>Dairy · Woodworking · Poultry · Agriculture · Bakery · Cleaning<br><span style='color:{GOLD}'>Minsk, Minsk Region &amp; Mogilev Region</span></div>
<div class='abs' style='top:44px;right:40px;width:360px;height:340px;border-radius:26px;overflow:hidden;border:6px solid #fff;box-shadow:0 18px 34px #0008'><img src='{photo}' style='width:100%;height:100%;object-fit:cover;object-position:55% 40%'></div>
<div class='abs' style='top:22px;right:338px;width:130px;height:130px;border-radius:50%;background:{RED};border:5px solid #fff;box-shadow:0 10px 22px #0007;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-8deg)'>
 <div style='font:400 50px Anton;color:#fff;line-height:1'>120</div><div style='font:800 17px Archivo;color:#fff;letter-spacing:2px'>POSTS</div></div>

<div class='abs' style='top:440px;left:30px;right:30px;border-radius:18px;overflow:hidden;box-shadow:0 10px 24px rgba(11,77,44,.18)'>{head}{rows}</div>
<div class='abs' style='top:886px;left:34px;right:34px;font:italic 600 15px Archivo;color:#5A6A60'>Net salary = paid to the worker after income tax &amp; statutory deductions; paid monthly in Belarusian Rubles (BYN), USD amounts are indicative. Upper end depends on trade, hours &amp; schedule.</div>

<div class='abs' style='top:928px;left:30px;width:500px;height:250px;background:#fff;border-radius:18px;border-top:6px solid {RED};box-shadow:0 8px 18px rgba(0,0,0,.08);padding:10px 18px;box-sizing:border-box'>
 <div style='font:400 26px Anton;color:{GRN};letter-spacing:1px'>PROVIDED BY THE COMPANY</div>
 <div style='display:grid;grid-template-columns:1fr 1fr;gap:8px 12px;margin-top:6px'>{ben}</div></div>
<div class='abs' style='top:928px;right:30px;width:504px;height:250px;background:{GRN};border-radius:18px;border-top:6px solid {GOLD};padding:10px 20px;box-sizing:border-box'>
 <div style='font:400 26px Anton;color:#fff;letter-spacing:1px'>JOB DETAILS &amp; REQUIREMENTS</div>{req_li}</div>

<div class='abs' style='top:1194px;left:0;width:1080px;height:156px;background:{GRN2}'></div>
<div class='abs' style='top:1194px;left:0'>{ornament(1080, 14, RED, '#fff')}</div>
<div class='abs' style='top:1212px;left:30px;height:126px;padding:0 20px;background:#fff;border-radius:18px;display:flex;flex-direction:column;justify-content:center;gap:0'>{nums}</div>
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
