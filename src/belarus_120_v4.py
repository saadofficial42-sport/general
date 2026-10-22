"""Belarus — 120 workers, 7 trades, combined ad v4, English (2026-10-22). User: v3 was "too sharp and pinkish" —
wants something calmer. Facts unchanged (demands/2026-10-19-belarus-120/facts.md); employer not named.
Design: "Minsk morning" — soft, natural palette (forest green, cream, warm gold, muted Belarus red accents only),
Minsk old-town photo (user) fading into cream, elegant serif-free title on a frosted cream plate, 4+3 grid of
real trade-photo tiles with soft gold salary tags, calm benefit row, deep-green CTA with all four numbers."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

GRN, GRN2, CREAM, GOLD, GOLD2, INK, RED = "#1F5E45", "#123B2C", "#F8F4EA", "#D9A441", "#F3D58A", "#1D2A24", "#B8463F"
EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"

JOBS = [("by_milking", "70% 40%", "Machine Milking Operators", "Men &amp; Women", "10", "Mogilev", "700 – 800"),
        ("by_dairy", "75% 30%", "Dairy Plant Labourers", "Men", "6", "Mogilev", "700 – 800"),
        ("by_woodworking", "center 35%", "Woodworking &amp; Production", "", "20", "Berezino", "800 – 1,100"),
        ("by_poultry", "center 40%", "Poultry Processing", "", "40", "Minsk", "1,000 – 1,600"),
        ("by_agriculture", "center 40%", "Agriculture &amp; Harvesting", "Men only", "10", "Mogilev Region", "600 – 1,200"),
        ("by_bakery", "center 40%", "Bakery Production", "Men &amp; Women", "30", "Borisov", "700 – 850"),
        ("by_cleaners", "center 8%", "Facility Cleaners", "Women", "4", "Borisov", "600 – 750")]


def tile(j, w):
    k, pos, t, who, q, loc, sal = j
    tag = f"<div style='font:700 13px Archivo;color:{RED};margin-top:2px'>{who}</div>" if who else ""
    return (f"<div style='width:{w}px;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 8px 20px rgba(18,59,44,.14)'>"
            f"<div style='height:150px;position:relative'><img src='{(PHOTOS / (k + '.jpg')).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'>"
            f"<div style='position:absolute;left:0;right:0;bottom:0;height:60px;background:linear-gradient(180deg,#0000,#000a)'></div>"
            f"<span style='position:absolute;left:10px;bottom:8px;font:400 22px Anton;color:#fff;letter-spacing:.5px'>{q} POSTS</span>"
            f"<span style='position:absolute;right:10px;top:10px;background:linear-gradient(135deg,{GOLD2},{GOLD});border-radius:10px;padding:2px 10px;font:400 21px Anton;color:{INK};box-shadow:0 4px 10px #0004'>${sal}</span></div>"
            f"<div style='padding:8px 12px 10px'><div style='font:800 17px Archivo;color:{INK};line-height:1.15'>{t}</div>{tag}"
            f"<div style='display:flex;align-items:center;gap:4px;font:600 14px Archivo;color:#5C6B63;margin-top:4px'>{icon('pin', 14, GRN, 2.4)}{loc}</div></div></div>")


def build():
    city = (PHOTOS / "by_minsk_oldtown.jpg").as_uri()
    row1 = "".join(tile(j, 240) for j in JOBS[:4])
    row2 = "".join(tile(j, 240) for j in JOBS[4:])
    ben = [("home", "Free accommodation"), ("food", "3 meals / allowance"), ("bus", "Free transport"), ("plane", "Ticket + return after 2 yrs"),
           ("medical", "Medical insurance"), ("calendar", "24 days paid leave"), ("overtime", "Overtime: at least double"), ("idcard", "Residence permit help")]
    ben_html = "".join(f"<div style='display:flex;align-items:center;gap:8px'><span style='width:34px;height:34px;border-radius:50%;background:#E7EFE9;display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 19, GRN, 2.3)}</span>"
                       f"<span style='font:700 15px Archivo;color:{INK};line-height:1.15'>{t}</span></div>" for ic, t in ben)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:520px;overflow:hidden'><img src='{city}' style='width:100%;height:100%;object-fit:cover;object-position:center 45%;filter:saturate(.9)'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:520px;background:linear-gradient(180deg,#123B2C80 0%,#123B2C10 35%,#F8F4EA00 60%,{CREAM} 100%)'></div>
<div class='abs' style='top:24px;left:30px;background:#fff;border-radius:16px;padding:4px 14px;box-shadow:0 8px 20px #0003'>{logo_img('logo-horizontal-light', 'width:280px;height:72px;object-position:left')}</div>
<div class='abs' style='top:22px;right:30px;filter:drop-shadow(0 6px 12px #0005)'>{flag('by', 120, True, 'by4')}</div>
<div class='abs' style='top:188px;left:50%;transform:translateX(-50%);width:820px;background:#F8F4EAee;border-radius:26px;padding:16px 30px 20px;text-align:center;box-shadow:0 16px 36px rgba(18,59,44,.25)'>
 <div style='font:800 17px Archivo;color:{RED};letter-spacing:5px'>URGENT REQUIREMENT · 120 POSTS · 7 TRADES</div>
 <div style='font:400 96px Anton;color:{GRN};letter-spacing:4px;line-height:1;margin-top:8px'>WORK IN BELARUS</div>
 <div style='font:700 19px Archivo;color:#4C5B53;margin-top:10px'>Net salary up to <b style='color:{INK}'>$1,600 / month</b> · Free accommodation · 3-year contract</div></div>

<div class='abs' style='top:426px;left:30px;right:30px;display:flex;gap:16px'>{row1}</div>
<div class='abs' style='top:678px;left:158px;right:158px;display:flex;gap:16px'>{row2}</div>

<div class='abs' style='top:938px;left:30px;right:30px;height:180px;background:#fff;border-radius:20px;box-shadow:0 8px 20px rgba(18,59,44,.10);padding:12px 22px;box-sizing:border-box'>
 <div style='display:flex;align-items:baseline;justify-content:space-between'><span style='font:400 26px Anton;color:{GRN};letter-spacing:1px'>PROVIDED BY THE COMPANY</span>
  <span style='font:700 14px Archivo;color:#5C6B63'>Age 21–45 · Work visa + permit · 40 h/week</span></div>
 <div style='display:grid;grid-template-columns:repeat(4,1fr);gap:12px 14px;margin-top:12px'>{ben_html}</div></div>
<div class='abs' style='top:1128px;left:34px;right:34px;font:600 14px Archivo;color:#6A776F;text-align:center'>Net salary = after tax, paid monthly in BYN; USD amounts indicative. Documents: CV, passport (2+ yrs), CNIC, photos, PCC, medical.</div>

<div class='abs' style='top:1166px;left:0;width:1080px;height:184px;background:linear-gradient(120deg,{GRN},{GRN2})'></div>
<div class='abs' style='top:1166px;left:0;width:1080px;height:6px;background:linear-gradient(90deg,{GOLD},{GOLD2},{GOLD})'></div>
<div class='abs' style='top:1196px;left:34px;display:grid;grid-template-columns:auto auto;gap:12px 30px'>{nums}</div>
<div class='abs' style='top:1196px;right:36px;width:420px;text-align:right'>
 <div style='font:400 31px Anton;color:{GOLD2};letter-spacing:.5px;line-height:1.05;white-space:nowrap'>SEND YOUR CV ON WHATSAPP</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:10px'>{icon('mail', 20, GOLD2, 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div>
 <div style='font:600 13px Archivo;color:#C8DCD1;margin-top:8px;line-height:1.3'>{ADDRESS}</div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CREAM}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Belarus-120-Workers-v4-English.png"))
