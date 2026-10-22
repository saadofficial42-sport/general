"""Belarus — 120 workers, 7 trades, combined ad v3, English (2026-10-22). User: all four numbers, new design and
pictures, 3D gradient colours, different from every other ad. Facts unchanged from belarus_120.py
(demands/2026-10-19-belarus-120/facts.md); employer not named.
Design: "3D glass" — deep indigo -> magenta -> amber mesh gradient with glossy 3D orbs, extruded gradient BELARUS
wordmark, a perspective fan of the seven real trade photos, frosted-glass vacancy list with round photo chips,
glass benefit pills, glass CTA with four numbers."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

INK, GOLD = "#130B2E", "#FFC94D"
EMAIL = "hr@rslinksconsultants.com"

JOBS = [("by_milking", "Machine Milking Operators", "Men &amp; Women", "10", "Mogilev", "700 – 800"),
        ("by_dairy", "General Labourers – Dairy Plant", "Men", "6", "Mogilev", "700 – 800"),
        ("by_woodworking", "Woodworking &amp; Production", "", "20", "Berezino", "800 – 1,100"),
        ("by_poultry", "Poultry Processing Plant", "", "40", "Minsk", "1,000 – 1,600"),
        ("by_agriculture", "Agricultural &amp; Harvesting", "Men only", "10", "Mogilev Region", "600 – 1,200"),
        ("by_bakery", "Bakery Production Workers", "Men &amp; Women", "30", "Borisov", "700 – 850"),
        ("by_cleaners", "Facility Cleaners", "Women", "4", "Borisov", "600 – 750")]
POS = {"by_cleaners": "center 8%", "by_milking": "70% 40%", "by_dairy": "75% 30%"}
GLASS = "background:linear-gradient(135deg,#ffffff2e,#ffffff0d);border:1.5px solid #ffffff55;box-shadow:0 12px 30px #0006, inset 0 1px 0 #ffffff66;backdrop-filter:blur(8px)"


def uri(k):
    return (PHOTOS / f"{k}.jpg").as_uri()


def orb(x, y, r, c1, c2):
    return (f"<div class='abs' style='left:{x - r}px;top:{y - r}px;width:{2 * r}px;height:{2 * r}px;border-radius:50%;"
            f"background:radial-gradient(circle at 32% 28%,#ffffffcc 0,{c1} 18%,{c2} 70%,#00000055 100%);box-shadow:0 20px 40px #0007'></div>")


def build():
    fan = ""
    n = len(JOBS)
    for i, (k, *_r) in enumerate(JOBS):
        off = i - (n - 1) / 2
        x, rot, z = 540 + off * 124 - 90, off * 5, 10 - abs(off)
        fan += (f"<div class='abs' style='left:{x:.0f}px;top:{308 + abs(off) * 9:.0f}px;width:180px;height:222px;border-radius:22px;overflow:hidden;"
                f"transform:perspective(900px) rotate({rot:.1f}deg) rotateY({-off * 7:.1f}deg);z-index:{int(z)};border:4px solid #ffffffcc;box-shadow:0 18px 34px #0009'>"
                f"<img src='{uri(k)}' style='width:100%;height:100%;object-fit:cover;object-position:{POS.get(k, 'center 35%')}'></div>")
    rows = "".join(
        f"<div style='display:flex;align-items:center;height:52px;padding:0 14px;{'border-top:1px solid #ffffff2a;' if i else ''}'>"
        f"<div style='width:44px;height:44px;border-radius:50%;overflow:hidden;border:2px solid {GOLD};flex:none'><img src='{uri(k)}' style='width:100%;height:100%;object-fit:cover;object-position:{POS.get(k, 'center 35%')}'></div>"
        f"<div style='flex:1;margin-left:14px;line-height:1.1'><span style='font:800 20px Archivo;color:#fff'>{t}</span>"
        + (f" <span style='font:700 14px Archivo;color:#FFB3D9'>· {g}</span>" if g else "") + "</div>"
        f"<div style='width:62px;text-align:center;font:400 28px Anton;color:{GOLD}'>{q}</div>"
        f"<div style='width:170px;font:700 16px Archivo;color:#E3DBFF;display:flex;align-items:center;gap:5px'>{icon('pin', 16, '#FF8FC7', 2.4)}{loc}</div>"
        f"<div style='width:156px;text-align:right'><span style='display:inline-block;padding:3px 12px;border-radius:12px;background:linear-gradient(135deg,#FFE58A,#FFB020 60%,#F07A12);"
        f"box-shadow:0 4px 0 #A94E00,0 8px 14px #0006;font:400 22px Anton;color:{INK}'>${s}</span></div></div>"
        for i, (k, t, g, q, loc, s) in enumerate(JOBS))
    ben = [("home", "Free accommodation"), ("food", "3 meals / meal allowance"), ("bus", "Free transport"), ("plane", "Ticket + ticket after 2 yrs"),
           ("medical", "Medical insurance"), ("calendar", "24 days paid leave"), ("overtime", "Overtime ≥ double rate"), ("idcard", "Residence permit help")]
    pills = "".join(f"<div style='display:flex;align-items:center;gap:8px;padding:8px 12px;border-radius:14px;{GLASS}'>"
                    f"<span style='width:30px;height:30px;border-radius:50%;background:linear-gradient(135deg,#FF7EB3,#7C4DFF);display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 17, '#fff', 2.3)}</span>"
                    f"<span style='font:700 15px Archivo;color:#fff;line-height:1.1'>{t}</span></div>" for ic, t in ben)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{p}</span></div>" for p in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:radial-gradient(circle at 15% 10%,#7C3AED 0,#3B1A8F 30%,transparent 55%),radial-gradient(circle at 95% 35%,#E0218A 0,transparent 45%),
 radial-gradient(circle at 10% 85%,#FF8A00 0,transparent 40%),linear-gradient(160deg,#1B0E4A,#2A0B4F 50%,#120726)'></div>
{orb(1015, 330, 46, '#FF6FB5', '#B0127A')}{orb(62, 300, 34, '#FFD36E', '#E07800')}{orb(850, 150, 16, '#8EC5FF', '#3550D8')}{orb(215, 205, 12, '#FFFFFF', '#C59BFF')}
<div class='abs' style='top:28px;left:30px;padding:6px 14px;border-radius:18px;background:#fff;box-shadow:0 10px 24px #0007'>{logo_img('logo-horizontal-light', 'width:280px;height:72px;object-position:left')}</div>
<div class='abs' style='top:30px;right:150px;padding:10px 18px;border-radius:999px;{GLASS};font:800 18px Archivo;color:#fff;letter-spacing:3px'>URGENT · 120 POSTS</div>
<div class='abs' style='top:20px;right:30px;filter:drop-shadow(0 8px 14px #0008)'>{flag('by', 104, True, 'by3d')}</div>

<div class='abs' style='top:118px;left:0;right:0;text-align:center'>
 <div style='font:800 22px Archivo;color:#FFD0EA;letter-spacing:8px'>WORK &amp; BUILD YOUR FUTURE IN</div>
 <div style='font:400 150px Anton;letter-spacing:10px;line-height:1;margin-top:4px;background:linear-gradient(180deg,#FFFFFF 0,#FFE08A 45%,#FF8A3D 75%,#E0218A 100%);
  -webkit-background-clip:text;color:transparent;filter:drop-shadow(0 3px 0 #9B1B66) drop-shadow(0 6px 0 #6A1050) drop-shadow(0 14px 18px #000a)'>BELARUS</div></div>
{fan}

<div class='abs' style='top:628px;left:30px;right:30px;border-radius:22px;overflow:hidden;{GLASS}'>
 <div style='display:flex;align-items:center;height:38px;padding:0 14px;background:linear-gradient(90deg,#7C4DFFaa,#E0218Aaa);font:800 14px Archivo;color:#fff;letter-spacing:1.5px'>
  <div style='flex:1;margin-left:58px'>POSITION</div><div style='width:62px;text-align:center'>POSTS</div><div style='width:170px;padding-left:14px;box-sizing:border-box'>LOCATION</div><div style='width:156px;text-align:right'>NET SALARY / MONTH</div></div>
 {rows}</div>
<div class='abs' style='top:1042px;left:30px;right:30px;display:grid;grid-template-columns:repeat(4,1fr);gap:8px'>{pills}</div>
<div class='abs' style='top:1150px;left:34px;right:34px;font:600 15px Archivo;color:#D9CFFF;text-align:center'>Age 21–45 · 3-year renewable contract · Work visa + permit · 40 h/week, shifts up to 12 h · Net salary paid in BYN, USD indicative</div>

<div class='abs' style='top:1186px;left:30px;right:30px;height:146px;border-radius:24px;{GLASS};display:flex;align-items:center;padding:0 24px;gap:20px'>
 <div style='display:grid;grid-template-columns:1fr 1fr;gap:10px 22px;flex:none'>{nums}</div>
 <div style='margin-left:auto;text-align:right'>
  <div style='font:400 34px Anton;letter-spacing:1px;line-height:1.05;background:linear-gradient(90deg,#FFE58A,#FF8A3D);-webkit-background-clip:text;color:transparent'>SEND YOUR CV ON WHATSAPP</div>
  <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:10px'>{icon('mail', 20, GOLD, 2)}<span style='font:800 19px Archivo;color:#fff'>{EMAIL}</span></div>
  <div style='font:600 12.5px Archivo;color:#CFC4F5;margin-top:8px'>Office 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi</div></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:#120726'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Belarus-120-Workers-v3-English.png"))
