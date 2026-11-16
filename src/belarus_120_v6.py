"""Belarus — 120 workers, 7 trades, v6, English (2026-11-16). User: very attractive, different design, with the
country's landscape. Facts as v5 (no "visa"). Design: "Minsk riverside" — full-bleed Minsk old-town riverside photo,
big white title in the sky with red/green flag ribbon, five tilted polaroid trade photos (incl. women: production, bakery, cleaners — user request) on the waterline, white
sheet with 7 trade rows as two-column salary cards, benefit icons, forest-green footer with red rule."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

RED, GRN, GRN2, CREAM, GOLD, INK = "#C8313E", "#1E6B47", "#0F4430", "#FAF7F0", "#E8B33A", "#14231B"
EMAIL = "hr@rslinksconsultants.com"
JOBS = [("Machine Milking Operators", "M/F", "10", "Mogilev", "700 – 800"), ("Dairy Plant Labourers", "Men", "6", "Mogilev", "700 – 800"),
        ("Woodworking &amp; Production", "", "20", "Berezino", "800 – 1,100"), ("Poultry Processing", "", "40", "Minsk", "1,000 – 1,600"),
        ("Agriculture &amp; Harvesting", "Men", "10", "Mogilev Region", "600 – 1,200"), ("Bakery Production", "M/F", "30", "Borisov", "700 – 850"),
        ("Facility Cleaners", "Women", "4", "Borisov", "600 – 750")]


def polaroid(src, pos, cap, rot):
    return (f"<div style='width:202px;background:#fff;padding:10px 10px 0;box-sizing:border-box;transform:rotate({rot}deg);box-shadow:0 20px 34px #0007'>"
            f"<div style='height:196px;overflow:hidden'><img src='{src}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'></div>"
            f"<div style='font:800 17px Archivo;color:{INK};text-align:center;line-height:38px;white-space:nowrap'>{cap}</div></div>")


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    cards = "".join(f"<div style='display:flex;align-items:center;justify-content:space-between;background:#fff;border-radius:14px;padding:0 16px;height:62px;border-left:6px solid {RED if i % 2 else GRN};box-shadow:0 6px 14px #14231B14'>"
                    f"<div><div style='font:800 19px Archivo;color:{INK};line-height:1.15'>{t}{f' <span style=\"font:700 14px Archivo;color:#6A7A70\">({g})</span>' if g else ''}</div>"
                    f"<div style='font:700 15px Archivo;color:#6A7A70'>{q} posts · {c}</div></div>"
                    f"<div style='font:400 26px Anton;color:{GRN};white-space:nowrap'>${s}</div></div>" for i, (t, g, q, c, s) in enumerate(JOBS))
    ben = [("home", "Free accommodation"), ("food", "3 meals / allowance"), ("bus", "Free transport"), ("plane", "Ticket + return after 2 yrs"),
           ("medical", "Medical insurance"), ("calendar", "24 days paid leave"), ("overtime", "Overtime at least double"), ("idcard", "Residence permit help")]
    ben_html = "".join(f"<div style='display:flex;align-items:center;gap:8px'><span style='width:36px;height:36px;border-radius:10px;background:{GRN};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 20, '#fff', 2.3)}</span>"
                       f"<span style='font:700 17px Archivo;color:{INK};line-height:1.15'>{t}</span></div>" for ic, t in ben)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:{CREAM}'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:620px;overflow:hidden'><img src='{P("by_minsk_oldtown.jpg")}' style='width:100%;height:100%;object-fit:cover;object-position:center 40%'>
 <div style='position:absolute;inset:0;background:linear-gradient(180deg,#0F4430cc 0%,#0F443055 32%,#0F443000 55%,{CREAM} 100%)'></div></div>
<div class='abs' style='top:24px;left:30px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0004'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:left')}</div>
<div class='abs' style='top:26px;right:30px;filter:drop-shadow(0 6px 10px #0006)'>{flag('by', 120, True, 'by6')}</div>
<div class='abs' style='top:120px;left:0;width:1080px;text-align:center'>
 <div style='display:inline-block;background:{RED};color:#fff;font:800 19px Archivo;letter-spacing:5px;padding:7px 18px;border-radius:999px'>URGENT REQUIREMENT · 120 POSTS</div>
 <div style='font:400 124px Anton;color:#fff;line-height:.95;letter-spacing:4px;margin-top:12px;text-shadow:0 10px 30px #0008'>WORK IN BELARUS</div>
 <div style='display:inline-block;font:700 23px Archivo;color:#fff;margin-top:8px;background:#0F4430cc;padding:6px 18px;border-radius:10px'>3-year contract · Work permit · Net salary up to <b style='color:{GOLD}'>$1,600</b> / month</div></div>
<div class='abs' style='top:388px;left:18px;right:18px;display:flex;justify-content:space-between'>
 {polaroid(P("by_woodworking.jpg"), '78% 35%', 'Woodworking', -5)}{polaroid(P("by_woman_production.jpg"), 'center 25%', 'Production', 3)}{polaroid(P("by_dairy.jpg"), '72% 30%', 'Dairy &amp; Milking', -2)}{polaroid(P("by_bakery.jpg"), '30% 45%', 'Bakery', 4)}{polaroid(P("by_cleaners.jpg"), 'center 30%', 'Facility Cleaners', -4)}</div>

<div class='abs' style='top:668px;left:30px;right:30px;display:grid;grid-template-columns:1fr 1fr;gap:10px 14px'>{cards}
 <div style='display:flex;align-items:center;justify-content:center;background:{GRN};border-radius:14px;height:62px;font:700 16px Archivo;color:#E3F1E9;text-align:center;line-height:1.25;padding:0 10px'>Net = after tax, paid monthly in BYN · USD indicative · Age 21–45 · 40 h/week</div></div>
<div class='abs' style='top:968px;left:30px;right:30px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px 12px'>{ben_html}</div>
<div class='abs' style='top:1080px;left:30px;right:30px;font:700 17px Archivo;color:#4D5A52;text-align:center'>Documents: CV · Passport (2+ yrs validity) · CNIC · Photos · PCC · Medical fitness</div>
<div class='abs' style='top:1120px;left:0;width:1080px;text-align:center;font:400 34px Anton;color:{RED};letter-spacing:2px'>SEND YOUR CV ON WHATSAPP</div>

<div class='abs' style='top:1180px;left:0;width:1080px;height:170px;background:linear-gradient(100deg,{GRN2},{GRN})'></div>
<div class='abs' style='top:1180px;left:0;width:1080px;height:7px;background:{RED}'></div>
<div class='abs' style='top:1204px;left:30px;right:30px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:10px 0'>{nums}</div>
<div class='abs' style='top:1300px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:10px'>{icon('mail', 22, GOLD, 2)}<span style='font:800 22px Archivo;color:#fff'>{EMAIL}</span></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CREAM}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Belarus-120-Workers-v6-English.png"))
