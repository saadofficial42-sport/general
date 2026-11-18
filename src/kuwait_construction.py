"""Kuwait — construction trades (625 posts), English (2026-11-18). From the partner's demand letter: assistant
carpenter (shuttering) 50 @ 140 KWD; mason bricks (tabook/block) 100, mason plaster 100, mason tiles ceramic 100,
mason tiles marble 75, painters external & internal 200 (Sigma paint experience preferred) — all 170 KWD.
8 hours/day, six days/week, Friday holiday; overtime paid after 8 hours or on holidays; other benefits per Kuwait
labour law; documents CV, passport, experience certificate. Agreement 1 year; ticket included (partner's package).
Dropped: "visa confirmed in 18 days 100%" (no visa wording, no guarantees). Employer not named.
Design: "Kuwait Towers dusk" — deep navy-to-teal Gulf dusk sky with gold Kuwait Towers silhouette, flag-colour
ribbon, three-photo hero (site / plaster / tiles), black glass vacancy board with gold KWD salaries, white info chips,
green footer."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

NAVY, NAVY2, TEAL, GOLD, GOLD2, GRN, RED, INK = "#0B1E3A", "#06122A", "#0F5E6E", "#E9B44C", "#FFD98A", "#007A3D", "#CE1126", "#0B1E3A"
EMAIL = "hr@rslinksconsultants.com"
PKR = {'140': '1,26,000', '170': '1,53,000'}  # approx. at 1 KWD ≈ 900 PKR (user to confirm)
JOBS = [("Assistant Carpenter (Shuttering)", "", "50", "140"), ("Mason – Bricks (Tabook / Block)", "", "100", "170"), ("Mason – Plaster", "", "100", "170"),
        ("Mason – Tiles Ceramic", "", "100", "170"), ("Mason – Tiles Marble", "", "75", "170"), ("Painters – External &amp; Internal", "Sigma paint experience preferred", "200", "170")]


def towers(col):
    return (f"<svg width='420' height='330' viewBox='0 0 420 330'><g fill='{col}'>"
            "<rect x='120' y='20' width='8' height='310'/><circle cx='124' cy='120' r='46'/><circle cx='124' cy='200' r='30'/><polygon points='118,330 130,330 128,10 120,10'/>"
            "<rect x='230' y='90' width='7' height='240'/><circle cx='233' cy='170' r='34'/><polygon points='228,330 238,330 236,70 230,70'/>"
            "<polygon points='320,330 326,330 324,150 322,150'/></g></svg>")


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    rows = "".join(f"<div style='display:grid;grid-template-columns:1fr 90px 290px;align-items:center;min-height:53px;border-top:1px solid #ffffff1c'>"
                   f"<div><div style='font:800 23px Archivo;color:#fff'>{t}</div>{f'<div style=\"font:700 15px Archivo;color:{GOLD2}\">{n}</div>' if n else ''}</div>"
                   f"<span style='font:400 30px Anton;color:#fff;text-align:center'>{q}</span>"
                   f"<span style='text-align:right;line-height:1;white-space:nowrap'><span style='font:400 32px Anton;color:{GOLD}'>{PKR[s]}</span> <span style='font:400 18px Anton;color:{GOLD}'>PKR</span> <span style='font:700 15px Archivo;color:#B9C4D6'>({s} KWD)</span></span></div>" for t, n, q, s in JOBS)
    chips = [("clock", "8 hrs / day · 6 days / week"), ("calendar", "Friday holiday"), ("overtime", "Overtime paid after 8 hrs &amp; on holidays"),
             ("plane", "Ticket included"), ("doc", "1-year agreement"), ("check", "Other benefits per Kuwait labour law")]
    chip = "".join(f"<div style='display:flex;align-items:center;gap:10px;background:#fff;border-radius:14px;padding:8px 12px;box-shadow:0 8px 16px #0004'>"
                   f"<span style='width:40px;height:40px;border-radius:10px;background:{GRN};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 22, '#fff', 2.3)}</span>"
                   f"<span style='font:800 18px Archivo;color:{INK};line-height:1.2'>{t}</span></div>" for ic, t in chips)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    ph = lambda f, pos: f"<div style='width:100%;height:100%;border-radius:16px;overflow:hidden;border:4px solid {GOLD};box-shadow:0 14px 26px #0008'><img src='{P(f)}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'></div>"
    body = f"""
<div class='abs' style='inset:0;background:linear-gradient(180deg,#F08A4B 0%,#B6506A 14%,{TEAL} 34%,{NAVY} 55%,{NAVY2} 100%)'></div>
<div class='abs' style='top:40px;right:20px;opacity:.9'>{towers('#06122Acc')}</div>
<div class='abs' style='top:0;left:0;width:1080px;height:10px;display:flex'><span style='flex:1;background:{GRN}'></span><span style='flex:1;background:#fff'></span><span style='flex:1;background:{RED}'></span></div>
<div class='abs' style='top:28px;left:30px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0006'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:left')}</div>
<div class='abs' style='top:30px;right:30px;filter:drop-shadow(0 6px 10px #0007)'>{flag('kw', 120, True, 'kwc')}</div>
<div class='abs' style='top:124px;left:40px;width:700px'>
 <div style='display:inline-block;background:{RED};color:#fff;font:800 19px Archivo;letter-spacing:5px;padding:7px 16px;border-radius:6px'>URGENT REQUIREMENT</div>
 <div style='font:400 96px Anton;color:#fff;line-height:.95;letter-spacing:2px;margin-top:12px;text-shadow:0 8px 24px #0008'>CONSTRUCTION<br>JOBS IN <span style='color:{GOLD2}'>KUWAIT</span></div>
 <div style='font:800 23px Archivo;color:#F6E7C8;margin-top:10px'>625 posts · Skilled &amp; unskilled · 1-year agreement</div></div>

<div class='abs' style='top:440px;left:30px;right:30px;height:200px;display:flex;gap:10px'>
 <div style='flex:1.13'>{ph('ua_hero.png', 'center')}</div><div style='flex:2'>{ph('rs_plaster2.jpg', 'center')}</div><div style='flex:1.92'>{ph('rs_tile_mason.png', 'center')}</div></div>

<div class='abs' style='top:666px;left:30px;right:30px;border-radius:22px;background:linear-gradient(180deg,#0A1830ee,#050C1Cee);border:2px solid {GOLD}66;padding:10px 26px 8px;box-sizing:border-box;box-shadow:0 16px 30px #0008'>
 <div style='display:grid;grid-template-columns:1fr 90px 290px;font:800 14px Archivo;color:{GOLD2};letter-spacing:2px;height:28px;align-items:center'><span>CATEGORY</span><span style='text-align:center'>POSTS</span><span style='text-align:right'>SALARY / MONTH (APPROX.)</span></div>{rows}</div>

<div class='abs' style='top:1050px;left:30px;right:30px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px'>{chip}</div>

<div class='abs' style='top:1214px;left:0;width:1080px;height:136px;background:linear-gradient(100deg,#005A2D,{GRN})'></div>
<div class='abs' style='top:1208px;left:0;width:1080px;height:6px;background:{GOLD}'></div>
<div class='abs' style='top:1226px;left:24px;right:24px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:4px 0'>{nums}</div>
<div class='abs' style='top:1310px;left:24px;right:24px;display:flex;justify-content:space-between;align-items:center'><span style='font:400 23px Anton;color:{GOLD2};letter-spacing:.5px'>SEND CV · PASSPORT · EXPERIENCE CERTIFICATE</span><span style='display:inline-flex;align-items:center;gap:8px'>{icon('mail', 20, GOLD2, 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></span></div>
"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{NAVY}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Kuwait-Construction-625-Posts.png"))
