"""Turkey — 5 positions, Urdu (2026-10-19). Facts: demands/2026-10-19-turkey-multi/facts.md (user gave positions only:
Factory Workers, Welders, Tailors, Plastic Factory Worker, Aluminum Factory Worker — no salary/posts/benefits, so none shown).
Design: "Istanbul skyline + photo grid" — white header, Turkish-red hero with Istanbul mosque/minaret skyline, tilted
polaroid hero photo, 3+2 grid of large picture cards, charcoal CTA.
Photos: real RS Links photos (factory) and the user's own tailor photo; welder / plastic / aluminium cards are
drawn placeholders until real photos (assets/photos/tr_welder.*, tr_plastic.*, tr_aluminium.*) are supplied."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon
from illustrations import SKIN, _person

RED, RED2, INK, CREAM, GOLD = "#E30A17", "#9C0610", "#1C1E26", "#FBF7F2", "#F6C445"
EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"
T = lambda s, px, c, extra="", lh=1.75: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def photo(key, pos="center"):
    for e in ("png", "jpg", "jpeg"):
        p = PHOTOS / f"{key}.{e}"
        if p.exists():
            return f"<img src='{p.as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:{pos};display:block'>"
    return None


def welder_svg(w, h, uid="wd"):
    fl = h * 0.88
    arms = (f'<path d="M18 -124 Q40 -110 50 -92" stroke="#34495E" stroke-width="13" fill="none" stroke-linecap="round"/>'
            f'<path d="M-18 -124 Q0 -100 30 -94" stroke="#34495E" stroke-width="13" fill="none" stroke-linecap="round"/>'
            f'<path d="M48 -92 L70 -70" stroke="#222" stroke-width="7" stroke-linecap="round"/>'
            f'<rect x="-21" y="-184" width="42" height="40" rx="8" fill="#2B2F36"/><rect x="-14" y="-170" width="28" height="9" rx="2" fill="#4FC3F7" opacity=".85"/>')
    sx, sy = w * 0.42 + 52, fl - 54
    sparks = "".join(f'<path d="M{sx} {sy} l{dx} {dy}" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/>'
                     for dx, dy, c in [(40, -30, "#FFF59D"), (55, -5, "#FFD54F"), (35, 25, "#FFB300"), (-10, -45, "#FFF59D"), (60, -40, "#FFCC80"),
                                       (20, 40, "#FFD54F"), (70, 15, "#FFF59D"), (-25, -30, "#FFB300"), (45, 45, "#FFCC80")])
    return f"""<defs><radialGradient id="{uid}g" cx="{sx/w:.2f}" cy="{sy/h:.2f}" r=".6"><stop offset="0" stop-color="#FFB74D" stop-opacity=".9"/><stop offset=".25" stop-color="#F57C00" stop-opacity=".45"/><stop offset="1" stop-color="#1A1F2B" stop-opacity="0"/></radialGradient></defs>
<rect width="{w}" height="{h}" fill="#1A1F2B"/><rect width="{w}" height="{h}" fill="url(#{uid}g)"/>
<path d="M0 {h*0.3} H{w}" stroke="#2C3442" stroke-width="10"/><rect y="{fl}" width="{w}" height="{h-fl}" fill="#2C3442"/>
<rect x="{w*0.5}" y="{fl-48}" width="{w*0.44}" height="10" fill="#6B7785"/><path d="M{w*0.54} {fl-38} V{fl} M{w*0.9} {fl-38} V{fl}" stroke="#6B7785" stroke-width="8"/>
<rect x="{w*0.5}" y="{fl-60}" width="{w*0.3}" height="12" fill="#9AA6B2"/>
{_person(w*0.42, fl, 0.74, "#34495E", vest=False, arms=arms)}
<circle cx="{sx}" cy="{sy}" r="9" fill="#FFFDE7"/>{sparks}"""


def plastic_svg(w, h, uid="pl"):
    fl = h * 0.88
    cy = fl - 70
    belt = (f'<rect x="{w*0.36}" y="{cy}" width="{w*0.64}" height="14" rx="7" fill="#37474F"/>'
            + f'<path d="M{w*0.4} {cy+14} V{fl} M{w*0.95} {cy+14} V{fl}" stroke="#546E7A" stroke-width="7"/>')
    cols = ["#29B6F6", "#66BB6A", "#FFCA28", "#EF5350", "#AB47BC", "#29B6F6"]
    bottles = "".join(f'<path d="M{x} {cy} v-34 q0 -8 6 -12 v-8 h8 v8 q6 4 6 12 v34z" fill="{cols[i % 6]}" opacity=".92"/>'
                      for i, x in enumerate(range(int(w * 0.56), int(w * 0.96), 30)))
    arms = (f'<path d="M18 -124 Q40 -110 52 -96" stroke="#00897B" stroke-width="13" fill="none" stroke-linecap="round"/>'
            f'<path d="M-18 -124 Q4 -104 30 -98" stroke="#00897B" stroke-width="13" fill="none" stroke-linecap="round"/>'
            f'<circle cx="52" cy="-96" r="7" fill="#E0F2F1"/><circle cx="30" cy="-98" r="7" fill="#E0F2F1"/>')
    return f"""<rect width="{w}" height="{h}" fill="#E3F2FD"/>
<rect x="{w*0.05}" y="{h*0.1}" width="{w*0.32}" height="{fl-h*0.1}" rx="8" fill="#455A64"/><rect x="{w*0.09}" y="{h*0.16}" width="{w*0.24}" height="{h*0.18}" rx="4" fill="#80DEEA"/>
<circle cx="{w*0.13}" cy="{h*0.48}" r="8" fill="#EF5350"/><circle cx="{w*0.2}" cy="{h*0.48}" r="8" fill="#66BB6A"/>
<rect y="{fl}" width="{w}" height="{h-fl}" fill="#B0BEC5"/>{belt}{bottles}
{_person(w*0.45, fl, 0.74, "#00897B", vest=False, cap="#00897B", arms=arms)}"""


def aluminium_svg(w, h, uid="al"):
    fl = h * 0.88
    rack = "".join(f'<rect x="{w*0.48}" y="{h*0.18 + k*22}" width="{w*0.48}" height="14" rx="2" fill="url(#{uid}m)"/>' for k in range(7))
    arms = (f'<path d="M18 -124 Q34 -160 24 -192" stroke="#1565C0" stroke-width="13" fill="none" stroke-linecap="round"/>'
            f'<path d="M-18 -124 Q-34 -160 -22 -192" stroke="#1565C0" stroke-width="13" fill="none" stroke-linecap="round"/>'
            f'<rect x="-120" y="-206" width="240" height="14" rx="2" fill="url(#{uid}m)"/>')
    return f"""<defs><linearGradient id="{uid}m" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F5F7FA"/><stop offset=".5" stop-color="#B0BEC5"/><stop offset="1" stop-color="#78909C"/></linearGradient></defs>
<rect width="{w}" height="{h}" fill="#ECEFF1"/><path d="M{w*0.46} {h*0.14} V{fl} M{w*0.98} {h*0.14} V{fl}" stroke="#455A64" stroke-width="8"/>{rack}
<rect y="{fl}" width="{w}" height="{h-fl}" fill="#B0BEC5"/>
{_person(w*0.3, fl, 0.7, "#1565C0", vest=False, helmet="#F2C230", arms=arms)}"""


def art(fn, w, h):
    return f"<svg width='{w}' height='{h}' viewBox='0 0 {w} {h}' style='display:block'>{fn(w, h)}</svg>"


def istanbul(w, h, fill):
    """Istanbul skyline: two big domed mosques with minarets, smaller domes, Galata-like tower."""
    b = h
    s = f'<rect x="0" y="{b-30}" width="{w}" height="30" fill="{fill}"/>'
    for cx, r, mins in [(w * 0.30, 70, [-120, -95, 95, 120]), (w * 0.72, 58, [-100, 100])]:
        s += f'<path d="M{cx-r-40} {b} V{b-60} H{cx+r+40} V{b}Z" fill="{fill}"/>'
        s += f'<path d="M{cx-r} {b-60} A{r} {r*0.85} 0 0 1 {cx+r} {b-60}Z" fill="{fill}"/><rect x="{cx-3}" y="{b-60-r*0.85-18}" width="6" height="18" fill="{fill}"/>'
        for sx in (-r - 20, r + 20):
            s += f'<path d="M{cx+sx-26} {b-60} A26 22 0 0 1 {cx+sx+26} {b-60}Z" fill="{fill}"/>'
        for m in mins:
            s += f'<rect x="{cx+m-5}" y="{b-200}" width="10" height="200" fill="{fill}"/><path d="M{cx+m-6} {b-200} L{cx+m} {b-232} L{cx+m+6} {b-200}Z" fill="{fill}"/><rect x="{cx+m-8}" y="{b-150}" width="16" height="5" fill="{fill}"/>'
    s += f'<rect x="{w*0.52-14}" y="{b-150}" width="28" height="150" fill="{fill}"/><path d="M{w*0.52-18} {b-150} L{w*0.52} {b-190} L{w*0.52+18} {b-150}Z" fill="{fill}"/>'
    return f"<svg width='{w}' height='{h}' style='display:block'>{s}</svg>"


def build():
    jobs = [("فیکٹری ورکرز", "FACTORY WORKERS", photo("rslinks_team_scan_x3", "center 30%")),
            ("ویلڈرز", "WELDERS", photo("tr_welder") or art(welder_svg, 324, 170)),
            ("ٹیلرز", "TAILORS", photo("by_tailor", "center 35%")),
            ("پلاسٹک فیکٹری ورکرز", "PLASTIC FACTORY WORKERS", photo("tr_plastic") or art(plastic_svg, 497, 170)),
            ("ایلومینیم فیکٹری ورکرز", "ALUMINIUM FACTORY WORKERS", photo("tr_aluminium") or art(aluminium_svg, 497, 170))]

    def card(i, j, x, y, w):
        ur, en, pic = j
        return (f"<div class='abs' style='top:{y}px;left:{x}px;width:{w}px;height:266px;background:#fff;border-radius:20px;overflow:hidden;box-shadow:0 8px 20px rgba(28,30,38,.16)'>"
                f"<div style='height:170px;overflow:hidden;position:relative'>{pic}"
                f"<span class='num' style='position:absolute;top:10px;right:10px;width:44px;height:44px;border-radius:50%;background:{RED};color:#fff;font-size:24px;display:flex;align-items:center;justify-content:center;box-shadow:0 3px 8px #0006'>{i + 1}</span></div>"
                f"<div style='height:96px;border-top:6px solid {RED};display:flex;flex-direction:column;align-items:center;justify-content:center'>"
                f"{T(ur, 28, INK, 'font-weight:700;margin-top:-6px', 1.5)}<div style='font-family:Anton;font-size:20px;color:{RED};letter-spacing:1px;line-height:1.1;margin-top:10px'>{en}</div></div></div>")

    cw3, cw2, gx = 324, 497, 18
    cards = "".join(card(i, jobs[i], 1080 - 30 - cw3 - i * (cw3 + gx), 598, cw3) for i in range(3))
    cards += "".join(card(3 + k, jobs[3 + k], 1080 - 30 - cw2 - k * (cw2 + gx), 880, cw2) for k in range(2))
    nums = "".join(f"<div style='display:flex;align-items:center;gap:10px'><span style='line-height:0'>{whatsapp_icon(34)}</span><span class='num' style='font-size:34px;color:{INK};line-height:1.15'>{n}</span></div>" for n in PHONES)
    hero = photo("rslinks_worker_pack_x3", "55% 40%")
    body = f"""<div class='ur-on' dir='rtl'>
<div class='abs' style='top:0;left:0;width:1080px;height:140px;background:#fff'></div>
<div class='abs' style='top:18px;right:26px'>{logo_img('logo-horizontal-light', 'width:400px;height:104px;object-position:right')}</div>
<div class='abs' style='top:20px;left:26px;display:flex;align-items:center;gap:16px;direction:ltr'>
 <div style='filter:drop-shadow(0 4px 8px #0004)'>{flag('tr', 150, True, 'trm')}</div>
 <div style='background:{INK};border-radius:14px;padding:0 20px 8px;display:flex;align-items:center;gap:8px;box-shadow:0 6px 14px #0004'>{icon('megaphone', 30, GOLD, 2.2)}{T('فوری ضرورت', 34, '#fff', 'font-weight:700', 1.6)}</div></div>

<div class='abs' style='top:140px;left:0;width:1080px;height:420px;background:linear-gradient(160deg,{RED},{RED2})'></div>
<div class='abs' style='top:310px;left:0;opacity:.28'>{istanbul(1080, 250, '#5A0309')}</div>
<div class='abs' style='top:170px;left:56px;width:370px;height:350px;background:#fff;padding:12px 12px 0;box-sizing:border-box;transform:rotate(-4deg);box-shadow:0 18px 34px #0007'>
 <div style='width:346px;height:280px;overflow:hidden'>{hero}</div>
 <div style='font-family:Anton;font-size:26px;color:{RED};text-align:center;letter-spacing:2px;line-height:2.1'>WORK IN TÜRKİYE</div></div>
<div class='abs' style='top:146px;right:40px;width:560px;text-align:right'>
 {T('فوری ضرورت برائے', 32, GOLD, 'font-weight:700', 1.7)}
 {T('ترکی', 104, '#fff', 'font-weight:700;margin-top:18px;margin-bottom:34px;text-shadow:0 8px 18px #0005', 1.4)}
 <div style='font-family:Anton;font-size:46px;color:#fff;letter-spacing:3px;direction:ltr;text-align:right;line-height:1.1'>JOBS IN TURKEY</div>
 <div style='display:inline-flex;align-items:center;gap:10px;margin-top:16px;background:#fff;border-radius:999px;padding:0 22px 6px'>{icon('user', 26, RED, 2.4)}{T('پانچ شعبوں میں ملازمت کے مواقع', 26, INK, 'font-weight:700', 1.6)}</div></div>

<div class='abs' style='top:580px;left:0;width:1080px;height:580px;background:{CREAM}'></div>
<div class='abs' style='top:534px;right:30px;background:{INK};border-radius:14px;padding:0 24px 6px;box-shadow:0 6px 14px #0005'>{T('دستیاب آسامیاں', 30, GOLD, 'font-weight:700', 1.6)}</div>
{cards}

<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:{INK};border-top:6px solid {RED}'></div>
<div class='abs' style='top:1170px;left:26px;height:160px;background:#fff;border-radius:22px;display:flex;align-items:center;padding:0 22px;direction:ltr;box-shadow:0 8px 18px #0008'><div style='display:flex;flex-direction:column;gap:2px'>{nums}</div></div>
<div class='abs' style='top:1162px;right:30px;width:560px;text-align:right'>
 {T('تنخواہ اور مکمل تفصیلات کے لیے ابھی رابطہ کریں!', 27, GOLD, 'font-weight:700', 1.7)}
 {T("اپنی <span class='num'>CV</span> واٹس ایپ کریں", 23, '#fff', 'font-weight:700', 1.7)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr;margin-top:4px'>{icon('mail', 24, GOLD, 2)}<span style='font-family:Archivo;font-size:23px;font-weight:700;color:#fff'>{EMAIL}</span></div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:6px;direction:ltr;margin-top:6px'>{icon('pin', 20, GOLD, 2.2)}<span style='font-family:Archivo;font-size:15px;font-weight:600;color:#D5D8DC'>{ADDRESS}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CREAM}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Turkey-5-Positions-Urdu.png"))
