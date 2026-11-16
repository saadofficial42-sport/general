"""Belarus — 120 workers, 7 trades, combined ad v5, English (2026-11-16). User: updated ad with a different design and
all six numbers. Facts unchanged (demands/2026-10-19-belarus-120/facts.md); employer not named; no "visa" wording.
Design: "departure board" — white header, 3-photo hero collage (woodworking / dairy / bakery), Belarus-red title slab,
charcoal flip-board listing the 7 trades with posts, city and net USD in amber, benefits strip, red footer."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

RED, RED2, GRN, CH, CH2, AMB, INK = "#C8313E", "#8F1C27", "#2E8B57", "#1C2024", "#121518", "#FFC233", "#1C2024"
EMAIL = "hr@rslinksconsultants.com"
JOBS = [("Machine Milking Operators", "M/F", "10", "Mogilev", "700 – 800"), ("Dairy Plant Labourers", "Men", "6", "Mogilev", "700 – 800"),
        ("Woodworking &amp; Production", "", "20", "Berezino", "800 – 1,100"), ("Poultry Processing", "", "40", "Minsk", "1,000 – 1,600"),
        ("Agriculture &amp; Harvesting", "Men", "10", "Mogilev Region", "600 – 1,200"), ("Bakery Production", "M/F", "30", "Borisov", "700 – 850"),
        ("Facility Cleaners", "Women", "4", "Borisov", "600 – 750")]


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    img = lambda f, pos, cap: (f"<div style='position:relative;width:100%;height:100%;overflow:hidden;border-radius:14px'><img src='{P(f)}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'>"
                               f"<span style='position:absolute;left:12px;bottom:12px;background:#fffffff0;color:{INK};font:800 16px Archivo;padding:4px 10px;border-radius:6px'>{cap}</span></div>")
    rows = "".join(f"<div style='display:grid;grid-template-columns:1fr 90px 210px 230px;align-items:center;height:50px;border-top:1px solid #ffffff1a'>"
                   f"<span style='font:800 22px Archivo;color:#fff'>{t}{f' <span style=\"font:700 15px Archivo;color:#9AA4AD\">({g})</span>' if g else ''}</span>"
                   f"<span style='font:400 28px Anton;color:{AMB};text-align:center'>{q}</span><span style='font:700 19px Archivo;color:#D7DDE2'>{c}</span>"
                   f"<span style='font:400 28px Anton;color:{AMB};text-align:right;letter-spacing:.5px'>${s}</span></div>" for t, g, q, c, s in JOBS)
    ben = [("home", "Free accommodation"), ("food", "3 meals / allowance"), ("bus", "Free transport"), ("plane", "Ticket + return after 2 yrs"),
           ("medical", "Medical insurance"), ("calendar", "24 days paid leave"), ("overtime", "Overtime at least double"), ("idcard", "Residence permit help")]
    ben_html = "".join(f"<div style='display:flex;align-items:center;gap:8px'><span style='width:36px;height:36px;border-radius:50%;background:{RED};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 20, '#fff', 2.3)}</span>"
                       f"<span style='font:700 17px Archivo;color:{INK};line-height:1.15'>{t}</span></div>" for ic, t in ben)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:#F6F6F4'></div>
<div class='abs' style='top:20px;left:30px'>{logo_img('logo-horizontal-light', 'width:270px;height:70px;object-position:left')}</div>
<div class='abs' style='top:26px;right:30px;display:flex;align-items:center;gap:14px'><span style='font:800 17px Archivo;color:{RED};letter-spacing:3px'>URGENT REQUIREMENT</span>{flag('by', 96, True, 'by5')}</div>
<div class='abs' style='top:104px;left:30px;right:30px;height:336px;display:grid;grid-template-columns:1.25fr 1fr;grid-template-rows:162px 162px;gap:12px;overflow:hidden'>
 <div style='grid-row:1/3'>{img('by_woodworking.jpg', '78% 35%', 'Woodworking &amp; Production · 20 posts')}</div>
 <div>{img('by_dairy.jpg', '70% 30%', 'Dairy Plant · Mogilev')}</div>
 <div>{img('by_bakery.jpg', 'center 45%', 'Bakery Production · 30 posts')}</div></div>
<div class='abs' style='top:452px;left:30px;right:30px;height:108px;background:linear-gradient(90deg,{RED2},{RED});border-radius:18px;box-shadow:0 16px 30px #8F1C2766;display:flex;align-items:center;justify-content:space-between;padding:0 34px;border-bottom:8px solid {GRN}'>
 <div><div style='font:400 70px Anton;color:#fff;letter-spacing:3px;line-height:1'>WORK IN BELARUS</div>
  <div style='font:700 19px Archivo;color:#FFE1E4;margin-top:4px'>3-year contract · Work permit · Age 21–45 · 40 h/week</div></div>
 <div style='text-align:center;background:#fff;border-radius:14px;padding:8px 18px'><div style='font:400 52px Anton;color:{RED};line-height:1'>120</div><div style='font:800 14px Archivo;color:{INK};letter-spacing:2px'>POSTS</div></div></div>

<div class='abs' style='top:572px;left:30px;right:30px;height:426px;background:linear-gradient(180deg,{CH},{CH2});border-radius:20px;padding:14px 26px;box-sizing:border-box;box-shadow:0 14px 28px #0004'>
 <div style='display:grid;grid-template-columns:1fr 90px 210px 230px;font:800 14px Archivo;color:#9AA4AD;letter-spacing:2px;height:30px;align-items:center'>
  <span>TRADE</span><span style='text-align:center'>POSTS</span><span>CITY</span><span style='text-align:right'>NET USD / MONTH</span></div>{rows}
 <div style='font:600 14px Archivo;color:#9AA4AD;margin-top:8px'>Net = after tax, paid monthly in BYN; USD indicative.</div></div>

<div class='abs' style='top:1016px;left:30px;right:30px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px 12px'>{ben_html}</div>
<div class='abs' style='top:1122px;left:30px;right:30px;font:700 17px Archivo;color:#4D555C;text-align:center'>Documents: CV · Passport (2+ yrs validity) · CNIC · Photos · PCC · Medical fitness</div>

<div class='abs' style='top:1186px;left:0;width:1080px;height:164px;background:linear-gradient(100deg,{RED2},{RED})'></div>
<div class='abs' style='top:1186px;left:0;width:1080px;height:7px;background:{GRN}'></div>
<div class='abs' style='top:1206px;left:30px;right:30px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:8px 0'>{nums}</div>
<div class='abs' style='top:1302px;left:30px;right:30px;display:flex;justify-content:space-between;align-items:center'>
 <span style='font:400 28px Anton;color:#fff;letter-spacing:1px'>SEND YOUR CV ON WHATSAPP</span>
 <span style='display:flex;align-items:center;gap:8px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 21px Archivo;color:#fff'>{EMAIL}</span></span></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#F6F6F4'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Belarus-120-Workers-v5-English.png"))
