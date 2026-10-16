"""Saudi Arabia — Technical & Maintenance Staff (2026-10-16). Source: SBM ad (demands/2026-10-16-saudi-technical/ref.jpg),
content only: no SBM / employer (facilities-management company) logo or name, no SBM photos or contacts.
18 positions copied row by row (head count + salary SAR); +200 = food allowance. 85 posts total.
Design: dark navy 'spec sheet', two columns of trade tables, real RS Links hard-hat photo."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

NAVY, NAVY2, TEAL, GOLD, INK = "#0A1F33", "#12304D", "#18A39A", "#F2B544", "#0A1F33"
EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"
SECTIONS = [
    ("MECHANICAL", "gear", "#18A39A", [("Laundry Equipment Technician", 2, 1200), ("Boiler Technician", 3, 1400), ("Fire Fighting Technician", 5, 1400),
      ("Generator Mechanical Technician", 4, 1300), ("Laundry Equipment Operator", 5, 1100), ("Medical Gas Technician", 2, 1500),
      ("STP &amp; WTP Technician", 10, 1400), ("HVAC Technician", 10, 1400), ("Chiller Technician", 3, 1600), ("STP &amp; WTP Operator", 5, 1200)]),
    ("ELECTRONICS", "video", "#4F8BE8", [("Audio &amp; Video Technician", 2, 1500), ("CCTV Technician", 4, 1400), ("Fire Alarm Technician", 3, 1400),
      ("Telephone &amp; Networking Technician", 5, 1400)]),
    ("ELECTRICAL", "bolt", "#F2B544", [("Elevator Technician", 2, 1400), ("Generator Electrical Technician", 5, 1400)]),
    ("CIVIL", "hammer", "#E0734A", [("Gardener Technician", 5, 1100), ("Furniture Carpenter", 10, 1100)]),
]


def table(title, ic, color, rows, rh=40):
    head = (f"<div style='display:flex;align-items:center;gap:10px;padding:8px 14px;background:{color}'>{icon(ic, 26, NAVY, 2.4)}"
            f"<span style='font-family:Anton;font-size:28px;color:{NAVY};letter-spacing:1px'>{title}</span>"
            f"<span style='margin-left:auto;font-family:PlexMono;font-weight:700;font-size:13px;color:{NAVY}'>POSTS · SAR</span></div>")
    body = "".join(
        f"<div style='display:flex;align-items:center;height:{rh}px;padding:0 14px;background:{'#ffffff0c' if i % 2 else 'transparent'}'>"
        f"<span style='flex:1;font-family:Archivo;font-weight:700;font-size:18px;color:#fff;white-space:nowrap'>{n}</span>"
        f"<span style='width:44px;text-align:center;font-family:Anton;font-size:22px;color:{color}'>{h}</span>"
        f"<span style='width:118px;text-align:right;font-family:Anton;font-size:22px;color:#fff'>{s} <span style='color:{GOLD}'>+ 200</span></span></div>"
        for i, (n, h, s) in enumerate(rows))
    return f"<div style='background:{NAVY2};border-radius:18px;overflow:hidden;border:1.5px solid {color}66'>{head}{body}</div>"


def build():
    total = sum(h for *_, rows in SECTIONS for _, h, _ in rows)
    nums = "".join(f"<div style='font-family:Anton;font-size:34px;color:{NAVY};line-height:1.06'>{n}</div>" for n in PHONES)
    facts = "".join(f"<div style='flex:1;display:flex;align-items:center;gap:10px;padding:0 12px;border-left:{'0' if i == 0 else '2px solid #0A1F3322'}'>"
                    f"{icon(ic, 32, TEAL, 2.2)}<div><div style='font-family:PlexMono;font-weight:700;font-size:13px;color:#5A6B7B'>{l}</div>"
                    f"<div style='font-family:Anton;font-size:24px;color:{NAVY};line-height:1.05'>{v}</div></div></div>"
                    for i, (ic, l, v) in enumerate((("clock", "DUTY", "8 HOURS / DAY"), ("calendar", "CONTRACT", "2 YEARS"), ("user", "AGE LIMIT", "UP TO 35"),
                                                     ("food", "FOOD ALLOWANCE", "+200 SAR INCL."), ("home", "ACCOMMODATION", "&amp; FACILITIES"))))
    photo = (PHOTOS / "rslinks_construction_engineer.png").as_uri()
    body = f"""
<div style='position:absolute;inset:0;background:linear-gradient(170deg,#0F2B47,{NAVY} 45%,#06121F)'></div>
<svg style='position:absolute;left:0;top:0' width='1080' height='1350'><g stroke='#ffffff08' stroke-width='1'>""" + "".join(f"<path d='M{x} 0 V1350'/>" for x in range(0, 1080, 36)) + "".join(f"<path d='M0 {y} H1080'/>" for y in range(0, 1350, 36)) + f"""</g></svg>
<div style='position:absolute;right:0;top:0;width:380px;height:330px;overflow:hidden;clip-path:polygon(18% 0,100% 0,100% 100%,0 100%)'>
 <img src='{photo}' style='width:100%;height:100%;object-fit:cover;object-position:center 70%'>
 <div style='position:absolute;inset:0;background:linear-gradient(90deg,{NAVY}aa,#0000 40%)'></div></div>
<div style='position:absolute;right:20px;top:18px;filter:drop-shadow(0 4px 8px #0008)'>{flag('saudi', 120, True, 'tsa')}</div>
<div style='position:absolute;left:30px;top:22px;background:#fff;border-radius:16px;padding:4px 14px'>{logo_img('logo-horizontal-light', 'width:340px;height:84px')}</div>
<div style='position:absolute;left:32px;top:128px;width:660px'>
 <div style='display:inline-block;background:{GOLD};padding:4px 14px;border-radius:8px'><span style='font-family:PlexMono;font-weight:700;font-size:18px;color:{NAVY};letter-spacing:3px'>URGENT REQUIREMENT · SAUDI ARABIA</span></div>
 <div style='font-family:Anton;font-size:72px;color:#fff;line-height:1;margin-top:10px'>TECHNICAL &amp; <span style='color:{TEAL}'>MAINTENANCE</span> STAFF</div>
</div>
<div style='position:absolute;left:24px;top:344px;width:548px'>{table(*SECTIONS[0])}</div>
<div style='position:absolute;left:586px;top:344px;width:470px;display:flex;flex-direction:column;gap:12px'>{table(*SECTIONS[1])}{table(*SECTIONS[2])}{table(*SECTIONS[3])}</div>
<div style='position:absolute;left:586px;top:882px;width:470px;height:170px;border-radius:18px;background:{GOLD};display:flex;flex-direction:column;align-items:center;justify-content:center'><div style='font-family:Anton;font-size:84px;color:{NAVY};line-height:1'>{total} POSTS</div><div style='font-family:Archivo;font-weight:800;font-size:19px;color:{NAVY};margin-top:4px'>18 positions · salary SAR + 200 food allowance</div></div>
<div style='position:absolute;left:24px;top:808px;width:548px;height:244px;border-radius:18px;background:{NAVY2};border:1.5px solid {TEAL}66;padding:14px 18px;box-sizing:border-box'>
 <div style='font-family:Anton;font-size:26px;color:{TEAL}'>WHAT THE COMPANY PROVIDES</div>
 """ + "".join(f"<div style='display:flex;align-items:center;gap:10px;margin-top:10px'>{icon(ic, 24, GOLD, 2.4)}<span style='font-family:Archivo;font-weight:700;font-size:20px;color:#fff'>{t}</span></div>"
               for ic, t in (("home", "Accommodation &amp; other facilities provided"), ("food", "Food allowance included (+200 SAR)"),
                             ("check", "Other benefits as per Saudi labour law"), ("calendar", "2-year contract · 8 hours per day"), ("user", "Age limit up to 35 years"))) + f"""</div>
<div style='position:absolute;left:24px;right:24px;top:1066px;height:96px;background:#fff;border-radius:18px;display:flex;align-items:center;padding:0 6px'>{facts}</div>
<div style='position:absolute;left:0;top:1176px;width:1080px;height:174px;background:{TEAL}'></div>
<div style='position:absolute;left:24px;top:1190px;height:128px;background:#fff;border-radius:22px;display:flex;align-items:center;gap:12px;padding:0 22px 0 12px;box-shadow:0 8px 18px #0005'>{whatsapp_icon(66)}<div>{nums}</div></div>
<div style='position:absolute;right:30px;top:1196px;width:540px;text-align:right'>
 <div style='font-family:Anton;font-size:46px;color:{NAVY};line-height:1'>SHARE YOUR CV</div>
 <div style='font-family:Archivo;font-weight:700;font-size:20px;color:{NAVY};margin-top:6px'>on WhatsApp or email</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px'>{icon('mail', 24, NAVY, 2.2)}<span style='font-family:Archivo;font-size:24px;font-weight:800;color:{NAVY}'>{EMAIL}</span></div></div>
<div style='position:absolute;left:0;bottom:0;width:1080px;height:30px;background:{NAVY};display:flex;align-items:center;justify-content:center;gap:8px'>
 {icon('pin', 18, GOLD, 2.4)}<span style='font-family:Archivo;font-size:16px;font-weight:700;color:#fff'>{ADDRESS}</span></div>"""
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Saudi-Arabia-Technical-Maintenance-Staff-English.png"))
