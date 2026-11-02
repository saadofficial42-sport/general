"""New Zealand — "register your interest" post, English (2026-11-02). User agreed to this instead of the visit-visa
scheme ad (declined: visit-to-work route + large upfront fees). No fees, visa type, salary or timeline — only fields
of interest and a CV call-to-action. Photos: RS library dairy / farm photos (user-supplied earlier).
Design: "fern" — deep navy page, silver fern frond motif, three round photos, white register card, teal CTA."""
from common import PHONES, PHOTOS, font_css, icon, logo_img, render, whatsapp_icon

NAVY, NAVY2, TEAL, SILVER, INK = "#0B1F3A", "#061226", "#18A3A3", "#DCE3EA", "#13202E"
EMAIL = "hr@rslinksconsultants.com"


def fern(x, y, s, rot, op):
    leaves = "".join(f"<path d='M0 {-i * 14} q {26 - i * 1.6} -10 {40 - i * 2.6} 6' stroke='#fff' stroke-width='4' fill='none'/>"
                     f"<path d='M0 {-i * 14} q {-(26 - i * 1.6)} -10 {-(40 - i * 2.6)} 6' stroke='#fff' stroke-width='4' fill='none'/>" for i in range(1, 14))
    return f"<g transform='translate({x} {y}) rotate({rot}) scale({s})' opacity='{op}'><path d='M0 0 V-200' stroke='#fff' stroke-width='5'/>{leaves}</g>"


def build():
    pics = [("by_dairy.jpg", "75% 30%", "Dairy Farming"), ("by_agriculture.jpg", "center 40%", "Fruit &amp; Farm Work"), ("by_milking.jpg", "70% 40%", "Milking &amp; Livestock")]
    circles = "".join(f"<div style='display:flex;flex-direction:column;align-items:center;gap:12px'>"
                      f"<div style='width:270px;height:270px;border-radius:50%;overflow:hidden;border:6px solid #fff;box-shadow:0 14px 30px #0008'><img src='{(PHOTOS / f).as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'></div>"
                      f"<div style='font:400 28px Anton;color:#fff;letter-spacing:1px'>{t.upper()}</div></div>" for f, pos, t in pics)
    steps = [("doc", "Send your CV on WhatsApp"), ("user", "Mention your experience &amp; current country (Pakistan / GCC)"),
             ("chat", "We will contact you when New Zealand positions open")]
    step = "".join(f"<div style='display:flex;align-items:center;gap:16px;padding:12px 0;{'border-top:1px solid #E3E8EE;' if i else ''}'>"
                   f"<span style='width:52px;height:52px;border-radius:50%;background:{TEAL};color:#fff;font:400 26px Anton;display:flex;align-items:center;justify-content:center;flex:none'>{i + 1}</span>"
                   f"<span style='font:700 25px Archivo;color:{INK}'>{t}</span></div>" for i, (ic, t) in enumerate(steps))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:{INK};letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:radial-gradient(circle at 80% 0%,#1C3E6E,{NAVY} 45%,{NAVY2})'></div>
<svg class='abs' style='top:0;left:0' width='1080' height='1350'>{fern(980, 520, 2.2, -20, .07)}{fern(90, 1130, 1.6, 25, .06)}</svg>
<div class='abs' style='top:34px;left:40px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:290px;height:74px;object-position:left')}</div>
<div class='abs' style='top:150px;left:0;right:0;text-align:center'>
 <div style='font:800 22px Archivo;color:{TEAL};letter-spacing:8px'>REGISTER YOUR INTEREST</div>
 <div style='font:400 120px Anton;color:#fff;letter-spacing:4px;line-height:1;margin-top:10px'>NEW ZEALAND</div>
 <div style='font:700 26px Archivo;color:{SILVER};margin-top:12px'>Agriculture &amp; dairy farm jobs — candidates from Pakistan and GCC</div></div>
<div class='abs' style='top:400px;left:0;right:0;display:flex;justify-content:center;gap:40px'>{circles}</div>
<div class='abs' style='top:780px;left:60px;right:60px;background:#fff;border-radius:24px;padding:16px 30px;box-shadow:0 18px 36px #0007'>
 <div style='font:400 32px Anton;color:{NAVY};letter-spacing:1px'>HOW TO REGISTER</div>{step}</div>
<div class='abs' style='top:1098px;left:60px;right:60px;text-align:center;font:600 17px Archivo;color:{SILVER}'>Registration only — details of each position will be shared when a confirmed job offer is available.</div>
<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:linear-gradient(100deg,{TEAL},#0E7C86)'></div>
<div class='abs' style='top:1174px;left:30px;width:600px;height:150px;background:#fff;border-radius:18px;display:grid;grid-template-columns:1fr 1fr;align-content:center;gap:12px;padding:0 18px;box-sizing:border-box;box-shadow:0 8px 18px #0005'>{nums}</div>
<div class='abs' style='top:1184px;right:40px;width:380px;text-align:right'>
 <div style='font:400 40px Anton;color:#fff;letter-spacing:1px;line-height:1.05'>SEND YOUR CV</div>
 <div style='font:700 19px Archivo;color:#E2F6F6;margin-top:8px'>on WhatsApp or email</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:10px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{NAVY}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-New-Zealand-Register-Interest-English.png"))
