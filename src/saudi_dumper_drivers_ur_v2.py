"""Saudi Arabia — Dumper Drivers, Urdu v2 (2026-11-20). User: apply pictures, change the design. Same facts as
saudi_dumper_drivers_ur.py. Still no dumper/tipper-driver photo in the library — construction-site photos used as
context (where dumper drivers work); dumper photo requested from the user.
Design: "site poster" — full-bleed construction-site photo top half under a dark gradient with the title over it,
diagonal Saudi-green cut, inset team photo, round yellow salary sticker, white lower panel with green-edged fact rows."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

GRN, GRN2, YEL, YEL2, INK = "#006C35", "#00431F", "#FFC21A", "#FFE07A", "#14201A"
EMAIL = "hr@rslinksconsultants.com"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.8: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    facts = [("pin", "شہر: ریاض"), ("user", f"{N(20)} فریش پاکستانی ڈرائیورز"), ("calendar", f"معاہدہ {N(2)} سال"),
             ("home", "رہائش فراہم"), ("check", "دیگر مراعات سعودی لیبر لاء کے مطابق"), ("doc", f"اپنی {N('CV')} واٹس ایپ کریں")]
    rows = "".join(f"<div style='display:flex;align-items:center;gap:12px;background:#F4F8F5;border-radius:14px;padding:0 14px;height:68px;border-right:6px solid {GRN if i % 2 == 0 else YEL}'>"
                   f"<span style='width:44px;height:44px;border-radius:50%;background:{GRN};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 24, '#fff', 2.2)}</span>"
                   f"{T(t, 23, INK, 'font-weight:700;white-space:nowrap', 1.8)}</div>" for i, (ic, t) in enumerate(facts))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<div class='abs' style='inset:0;background:#fff'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:330px;background:linear-gradient(120deg,{GRN2},{GRN})'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:330px;background:repeating-linear-gradient(-45deg,#ffffff08 0 30px,transparent 30px 60px)'></div>
<div class='abs' style='top:24px;right:30px;background:#fff;border-radius:14px;padding:2px 12px'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:right')}</div>
<div class='abs' style='top:26px;left:30px;filter:drop-shadow(0 6px 10px #0008)'>{flag('saudi', 120, True, 'sad2')}</div>
<div class='abs' style='top:106px;right:44px;width:1000px'>
 <div style='display:inline-block;background:{YEL};border-radius:10px;padding:0 22px'>{T('فوری ضرورت برائے سعودی عرب', 28, INK, 'font-weight:700', 1.75)}</div>
 {T('ڈمپر ڈرائیورز', 104, '#fff', 'font-weight:700;margin-top:0', 1.7)}</div>
<div class='abs' style='top:150px;left:44px;text-align:left'>
 <div style='font:400 34px Anton;color:{YEL2};letter-spacing:5px'>DUMPER DRIVERS</div>
 <div style='font:400 26px Anton;color:#fff;letter-spacing:6px;margin-top:4px'>RIYADH · SAUDI ARABIA</div>
 <div style='margin-top:8px'>{T('سعودیہ کی معروف کمپنی کے لیے', 22, '#DDEFE3', 'font-weight:700;text-align:left', 1.8)}</div></div>
<div class='abs' style='top:330px;left:0;width:1080px;height:500px;overflow:hidden'><img src='{P("sa_dumper_truck.jpg")}' style='width:100%;height:100%;object-fit:cover;object-position:center 55%'></div>
<div class='abs' style='top:322px;left:0;width:1080px;height:8px;background:{YEL}'></div>
<div class='abs' style='top:350px;left:40px;width:250px;height:250px;border-radius:50%;background:radial-gradient(circle at 35% 30%,{YEL2},{YEL} 60%,#E0A000);border:7px solid #fff;box-shadow:0 18px 34px #0007;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-6deg)'>
 {T('ماہانہ تنخواہ', 22, INK, 'font-weight:700', 1.5)}
 <div style='font:400 78px Anton;color:{INK};line-height:1;direction:ltr'>1700</div>
 <div style='font:400 24px Anton;color:{INK};direction:ltr;letter-spacing:2px'>SAR</div>
 {T('+ ٹرپ اوور ٹائم', 22, GRN2, 'font-weight:700', 1.6)}</div>

<div class='abs' style='top:852px;left:30px;right:30px;display:grid;grid-template-columns:1fr 1fr;gap:12px 14px'>{rows}</div>
<div class='abs' style='top:1094px;left:0;width:1080px;text-align:center'>{T('ابھی رابطہ کریں!', 40, GRN, 'font-weight:700', 1.7)}</div>

<div class='abs' style='top:1190px;left:0;width:1080px;height:160px;background:linear-gradient(100deg,{GRN2},{GRN})'></div>
<div class='abs' style='top:1184px;left:0;width:1080px;height:6px;background:{YEL}'></div>
<div class='abs' style='top:1206px;left:30px;right:30px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:10px 0;direction:ltr'>{nums}</div>
<div class='abs' style='top:1304px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:10px;direction:ltr'>{icon('mail', 22, YEL, 2)}<span style='font:800 22px Archivo;color:#fff'>{EMAIL}</span></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Saudi-Dumper-Drivers-v2-Urdu.png"))
