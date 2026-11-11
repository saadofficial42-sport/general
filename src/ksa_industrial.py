"""KSA — 14 industrial technician / operator positions, English (2026-11-09). Facts: demands/2026-11-09-ksa-industrial/facts.md
(converted from another agency's ad; content only). Design: "plant permit" — white page, Saudi-green header with
orange safety stripe, two-column position grid (7 + 7) with orange salary chips, requirements panel with tall
engineer photo, welder + machinist photo strip, green CTA with all four numbers."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

GRN, GRN2, ORG, INK, SOFT = "#0B6B3A", "#064726", "#F28A1E", "#14211A", "#F3F6F4"
EMAIL = "hr@rslinksconsultants.com"
JOBS = [("Materials Controller", "2700"), ("DDC Technician", "2200"), ("Electrical Technician", "1600"), ("HVAC Technician", "2000"),
        ("Instrument Technician", "2000"), ("Machinist", "1500"), ("Multicraft Technician", "1700"), ("Pipe Fitter", "1300"),
        ("SS Welder", "2200"), ("TIG Welder", "1700"), ("Fabricator", "1400"), ("Manlift Operator", "1400"),
        ("Backhoe / Loader Operator", "1400"), ("Hydraulic Gangway Operator", "1400")]


def build():
    ph = lambda f, pos="center": f"<img src='{(PHOTOS / f).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'>"
    row = lambda i, t, s: (f"<div style='display:flex;align-items:center;height:56px;padding:0 14px;background:{'#fff' if i % 2 else SOFT};border-radius:10px'>"
                           f"<span style='width:30px;font:400 18px Anton;color:{GRN}'>{i + 1:02d}</span>"
                           f"<span style='flex:1;font:800 {18 if len(t) > 22 else 20}px Archivo;color:{INK};white-space:nowrap'>{t}</span>"
                           f"<span style='background:{ORG};border-radius:8px;padding:3px 10px;font:400 22px Anton;color:#fff;letter-spacing:.5px'>{s}+300</span></div>")
    col = lambda a, b: "".join(row(i, *JOBS[i]) for i in range(a, b))
    req = [("Industrial experience only", "check"), ("GCC experience is a must", "check"), ("Aramco experience preferred", "star")]
    req_li = "".join(f"<div style='display:flex;align-items:center;gap:10px;margin-top:8px'><span style='width:30px;height:30px;border-radius:50%;background:{ORG};display:flex;align-items:center;justify-content:center;flex:none'>{icon('check', 20, '#fff', 3)}</span>"
                     f"<span style='font:800 17px Archivo;color:#fff;line-height:1.2'>{t}</span></div>" for t, _ in req)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:250px;background:linear-gradient(120deg,{GRN},{GRN2})'></div>
<div class='abs' style='top:250px;left:0;width:1080px;height:14px;background:repeating-linear-gradient(-45deg,{ORG} 0 18px,{INK} 18px 36px)'></div>
<div class='abs' style='top:28px;left:36px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:270px;height:70px;object-position:left')}</div>
<div class='abs' style='top:22px;right:36px;filter:drop-shadow(0 6px 12px #0006)'>{flag('saudi', 140, True, 'saI')}</div>
<div class='abs' style='top:120px;left:40px;right:40px;display:flex;align-items:flex-end;justify-content:space-between'>
 <div><div style='font:800 20px Archivo;color:{ORG};letter-spacing:5px'>URGENT JOB OPPORTUNITY</div>
  <div style='font:400 84px Anton;color:#fff;letter-spacing:2px;line-height:1'>SAUDI ARABIA <span style='color:{ORG}'>(KSA)</span></div></div>
 <div style='font:700 18px Archivo;color:#CFE8DA;text-align:right;line-height:1.35'>Industrial technicians<br>&amp; operators · 14 trades</div></div>

<div class='abs' style='top:286px;left:36px;width:1008px;display:flex;align-items:center;justify-content:space-between;padding:0 4px'>
 <span style='font:400 26px Anton;color:{GRN2};letter-spacing:1px'>CATEGORY &amp; MONTHLY SALARY</span><span style='font:800 15px Archivo;color:#5A6A60'>SAR (basic + 300)</span></div>
<div class='abs' style='top:330px;left:36px;width:1008px;display:grid;grid-template-columns:1fr 1fr;gap:8px 14px'>
 <div style='display:flex;flex-direction:column;gap:8px'>{col(0, 7)}</div><div style='display:flex;flex-direction:column;gap:8px'>{col(7, 14)}</div></div>

<div class='abs' style='top:796px;left:36px;width:240px;height:200px;border-radius:18px;overflow:hidden;box-shadow:0 12px 26px rgba(0,0,0,.2)'>{ph('elec_panel_main.jpg', '65% 20%')}
 <div style='position:absolute;left:0;right:0;bottom:0;height:60px;background:linear-gradient(0deg,{GRN2}99,{GRN2}00)'></div><span style='position:absolute;left:12px;bottom:10px;background:{ORG};color:#fff;font:400 20px Anton;padding:2px 10px;border-radius:6px;letter-spacing:1px'>ELECTRICIANS</span></div>
<div class='abs' style='top:796px;right:36px;width:300px;height:200px;border-radius:18px;background:{GRN2};padding:8px 18px;box-sizing:border-box;border-top:6px solid {ORG}'>
 <div style='font:400 26px Anton;color:{ORG};letter-spacing:1px'>REQUIREMENTS</div>{req_li}</div>

<div class='abs' style='top:796px;left:288px;width:420px;height:200px;display:flex;gap:12px'>
 <div style='flex:1;border-radius:18px;overflow:hidden;position:relative'>{ph('tr_welder.png', 'center 35%')}<span style='position:absolute;left:12px;bottom:10px;background:{ORG};color:#fff;font:400 20px Anton;padding:2px 10px;border-radius:6px;letter-spacing:1px'>WELDERS</span></div>
 <div style='flex:1;border-radius:18px;overflow:hidden;position:relative'>{ph('tr_aluminium.png', 'center 30%')}<span style='position:absolute;left:12px;bottom:10px;background:{ORG};color:#fff;font:400 20px Anton;padding:2px 10px;border-radius:6px;letter-spacing:1px'>MACHINISTS</span></div></div>

<div class='abs' style='top:1012px;left:36px;right:36px;height:120px;border-radius:20px;background:linear-gradient(90deg,{ORG},#FFB347);display:flex;align-items:center;justify-content:center;gap:20px;box-shadow:0 10px 22px rgba(242,138,30,.35)'>
 {icon('doc', 50, '#fff', 2)}<div><div style='font:400 46px Anton;color:#fff;letter-spacing:2px;line-height:1'>SHARE YOUR CV FOR SHORTLISTING</div>
 <div style='font:800 18px Archivo;color:#FFF3E3;margin-top:6px'>Mention your trade, GCC experience &amp; years of industrial work</div></div></div>

<div class='abs' style='top:1160px;left:0;width:1080px;height:190px;background:linear-gradient(100deg,{GRN2},{GRN})'></div>
<div class='abs' style='top:1188px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1186px;right:40px;width:380px;text-align:right'>
 <div style='font:400 40px Anton;color:{ORG};letter-spacing:1px;line-height:1.05'>APPLY NOW!</div>
 <div style='font:700 19px Archivo;color:#CFE8DA;margin-top:6px'>Send your CV on WhatsApp</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:8px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-KSA-Industrial-Technicians-English.png"))
