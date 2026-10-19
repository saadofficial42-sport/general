"""Turkey — 5 positions, Urdu (2026-10-19). Facts: demands/2026-10-19-turkey-multi/facts.md (user gave positions only:
Factory Workers, Welders, Tailors, Plastic Factory Worker, Aluminum Factory Worker). Salaries taken from the two
reference ads the user sent ("take info from here"): factory worker 28000 Lira, welder & tailor 33,000 Lira monthly;
plastic / aluminium have no figure in the references -> "salary: contact us".
Design: "Istanbul skyline + photo grid" — white header, Turkish-red hero with Istanbul mosque/minaret skyline, tilted
polaroid hero photo, 3+2 grid of large picture cards, charcoal CTA.
Photos (all real people, no drawings — user 2026-10-19): factory = RS Links staff; plastic = RS Links machine operator
from the user's own Belarus ad; welder / tailor / aluminium (CNC metal machining) = cropped from the Phoenix reference ad,
used at the user's explicit request (see assets/photos/SOURCE.txt)."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

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
    N = lambda v: f"<span class='num' style='font-size:30px;color:{RED2};line-height:1'>{v}</span>"
    lira = lambda v, monthly=False: f"{N(v)} {T('لیرا ماہانہ' if monthly else 'لیرا', 20, INK, 'font-weight:700;display:inline-block', 1.4)}"
    jobs = [("فیکٹری ورکرز", "FACTORY WORKERS", photo("rslinks_team_scan_x3", "center 30%"), lira("28,000")),
            ("پلاسٹک فیکٹری ورکرز", "PLASTIC FACTORY WORKERS", photo("tr_plastic", "center 40%"), T("تنخواہ: رابطہ کریں", 20, INK, "font-weight:700", 1.5)),
            ("ایلومینیم فیکٹری ورکرز", "ALUMINIUM FACTORY WORKERS", photo("tr_aluminium", "center 30%"), T("تنخواہ: رابطہ کریں", 20, INK, "font-weight:700", 1.5)),
            ("ویلڈرز", "WELDERS", photo("tr_welder", "center 35%"), lira("33,000", True)),
            ("ٹیلرز", "TAILORS", photo("tr_tailor", "center 12%"), lira("33,000", True))]

    def card(i, j, x, y, w):
        ur, en, pic, sal = j
        return (f"<div class='abs' style='top:{y}px;left:{x}px;width:{w}px;height:236px;background:#fff;border-radius:20px;overflow:hidden;box-shadow:0 8px 20px rgba(28,30,38,.16)'>"
                f"<div style='height:150px;overflow:hidden;position:relative'>{pic}"
                f"<span class='num' style='position:absolute;top:10px;right:10px;width:44px;height:44px;border-radius:50%;background:{RED};color:#fff;font-size:24px;display:flex;align-items:center;justify-content:center;box-shadow:0 3px 8px #0006'>{i + 1}</span>"
                f"<div style='position:absolute;bottom:10px;left:10px;background:{GOLD};border-radius:12px;padding:2px 14px 4px;display:flex;align-items:center;gap:8px;box-shadow:0 4px 10px #0006'>{sal}</div></div>"
                f"<div style='height:86px;border-top:6px solid {RED};display:flex;flex-direction:column;align-items:center;justify-content:center'>"
                f"{T(ur, 28, INK, 'font-weight:700;margin-top:-6px', 1.5)}<div style='font-family:Anton;font-size:20px;color:{RED};letter-spacing:1px;line-height:1.1;margin-top:10px'>{en}</div></div></div>")

    cw3, cw2, gx = 324, 497, 18
    cards = "".join(card(i, jobs[i], 1080 - 30 - cw3 - i * (cw3 + gx), 590, cw3) for i in range(3))
    cards += "".join(card(3 + k, jobs[3 + k], 1080 - 30 - cw2 - k * (cw2 + gx), 840, cw2) for k in range(2))
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

<div class='abs' style='top:1086px;left:30px;right:30px;height:56px;border-radius:16px;background:#fff;border:3px solid {RED};display:flex;align-items:center;justify-content:space-around;box-shadow:0 6px 14px rgba(28,30,38,.12)'>
 <div style='display:flex;align-items:center;gap:8px'>{icon('clock', 28, RED, 2.3)}{T("ٹائم لائن: <span class='num' style='color:" + RED + "'>4</span> ماہ", 23, INK, 'font-weight:700', 1.5)}</div>
 <div style='width:2px;height:34px;background:#E6D9CC'></div>
 <div style='display:flex;align-items:center;gap:8px'>{icon('doc', 28, RED, 2.3)}<span style='font-family:Archivo;font-size:22px;font-weight:800;color:{INK};direction:ltr;unicode-bidi:isolate'>PCC + FRC <span style='color:{RED}'>(MOFA Attested)</span></span></div>
 <div style='width:2px;height:34px;background:#E6D9CC'></div>
 <div style='display:flex;align-items:center;gap:8px'>{icon('check', 26, RED, 3)}{T('دیگر معیاری دستاویزات', 23, INK, 'font-weight:700', 1.5)}</div></div>
<div class='abs' style='top:1150px;left:0;width:1080px;height:200px;background:{INK};border-top:6px solid {RED}'></div>
<div class='abs' style='top:1170px;left:26px;height:160px;background:#fff;border-radius:22px;display:flex;align-items:center;padding:0 22px;direction:ltr;box-shadow:0 8px 18px #0008'><div style='display:flex;flex-direction:column;gap:2px'>{nums}</div></div>
<div class='abs' style='top:1162px;right:30px;width:560px;text-align:right'>
 {T('مزید تفصیلات کے لیے ابھی رابطہ کریں!', 27, GOLD, 'font-weight:700', 1.7)}
 {T("اپنی <span class='num'>CV</span> واٹس ایپ کریں", 23, '#fff', 'font-weight:700', 1.7)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr;margin-top:4px'>{icon('mail', 24, GOLD, 2)}<span style='font-family:Archivo;font-size:23px;font-weight:700;color:#fff'>{EMAIL}</span></div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:6px;direction:ltr;margin-top:6px'>{icon('pin', 20, GOLD, 2.2)}<span style='font-family:Archivo;font-size:15px;font-weight:600;color:#D5D8DC'>{ADDRESS}</span></div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{CREAM}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Turkey-5-Positions-Urdu.png"))
