"""Style: High-voltage.

Deep teal/black + electric yellow + brand green. White header (logo, red urgent tag, flag);
full-width dusk hero with transmission towers, power lines and linemen climbing in silhouette
(or a real photo from assets/photos/<photo>.* when present) and a big headline; grade cards
with large salary; interview-schedule card with date chips beside 2x2 fact tiles; benefits
bar; CTA with both WhatsApp numbers (order from data) + email. Renders the languages in data.

Usage: python3 src/style_volt.py <data module in src/data/>
"""
import importlib
import sys

from common import C, PHOTOS, flag, icon, logo_img, page, render, whatsapp_icon, overflow_report
from style_corporate_grid import T
from style_site import _fig, INK

DEEP, TEAL, VOLT, EM = "#071C24", "#0D3B4A", "#FFD23F", "#1E9E4A"


def _tower(cx, base, h, w):
    """Lattice transmission tower centred at cx, feet on base."""
    top, half = base - h, w / 2
    xs = lambda y, k=1: half * (0.18 + 0.82 * (y - top) / h) * k
    legs = f"M{cx - half} {base} L{cx - xs(top)} {top} M{cx + half} {base} L{cx + xs(top)} {top}"
    braces = ""
    n = 9
    for i in range(n):
        y1, y2 = top + h * i / n, top + h * (i + 1) / n
        braces += f" M{cx - xs(y1)} {y1} L{cx + xs(y2)} {y2} M{cx + xs(y1)} {y1} L{cx - xs(y2)} {y2} M{cx - xs(y2)} {y2} L{cx + xs(y2)} {y2}"
    arms = ""
    for k, (ay, aw) in enumerate(((top + h * .05, w * 1.25), (top + h * .22, w * 1.55), (top + h * .40, w * 1.25))):
        arms += f" M{cx - aw} {ay} L{cx + aw} {ay} M{cx - aw} {ay} L{cx - xs(ay + 22)} {ay + 22} M{cx + aw} {ay} L{cx + xs(ay + 22)} {ay + 22}"
    ins = "".join(f"<rect x='{cx + sx * aw - 3}' y='{ay}' width='6' height='18' rx='2' fill='{INK}'/>"
                  for ay, aw in ((top + h * .05, w * 1.25), (top + h * .22, w * 1.55), (top + h * .40, w * 1.25)) for sx in (-1, 1))
    return (f"<path d='{legs}' stroke='{INK}' stroke-width='5' fill='none'/>"
            f"<path d='{braces}{arms}' stroke='{INK}' stroke-width='2.4' fill='none'/>{ins}"
            f"<path d='M{cx} {top} L{cx} {top - 18}' stroke='{INK}' stroke-width='4'/>")


def tower_scene(w, h, uid):
    G = h - 6
    sky = (f"<defs><linearGradient id='sk{uid}' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='{DEEP}'/>"
           f"<stop offset='.5' stop-color='{TEAL}'/><stop offset='.82' stop-color='#C97A2E'/><stop offset='1' stop-color='#F4C25A'/></linearGradient></defs>"
           f"<rect width='{w}' height='{h}' fill='url(#sk{uid})'/><circle cx='{w*.30}' cy='{G-30}' r='70' fill='#FFE29A' opacity='.85'/>")
    T1 = (w * .72, 330, 120)            # main tower: centre, height, base width
    t2 = (w * .12, 190, 70)
    lines = ""
    for (ay_frac, aw_k) in ((.05, 1.25), (.22, 1.55), (.40, 1.25)):
        for sx in (-1, 1):
            x1 = t2[0] + sx * t2[2] * aw_k
            y1 = G - t2[1] + t2[1] * ay_frac + 18
            x2 = T1[0] + sx * T1[2] * aw_k
            y2 = G - T1[1] + T1[1] * ay_frac + 18
            mx, my = (x1 + x2) / 2, max(y1, y2) + 40
            lines += f"<path d='M{x1} {y1} Q{mx} {my} {x2} {y2} T{w + 80} {y2 + 30}' stroke='{INK}' stroke-width='2.2' fill='none' opacity='.9'/>"
    tw = _tower(*((T1[0], G, T1[1], T1[2]))) + _tower(t2[0], G, t2[1], t2[2])
    # linemen: one climbing the main tower leg, one working out on the middle arm
    top = G - T1[1]
    men = (_fig(T1[0] - 50, top + 190, .5, le=(-10, -150), lh=(-6, -186), re=(16, -150), rh=(20, -184),
                lk=(-18, -58), lf=(-8, -20), rk=(14, -40), rf=(10, 0))
           + _fig(T1[0] + 128, top + T1[1] * .22 - 2, .48, flip=True, re=(18, -150), rh=(28, -176), le=(-16, -120), lh=(-34, -138)))
    ground = f"<rect x='0' y='{G}' width='{w}' height='{h - G}' fill='{INK}'/>"
    return f"<svg class='abs' style='left:0;top:0' width='{w}' height='{h}'>{sky}{lines}{tw}{men}{ground}</svg>"


def hero_picture(name, w, h, uid):
    for e in ("jpg", "jpeg", "png", "webp"):
        p = PHOTOS / f"{name}.{e}"
        if p.exists():
            return f"<img class='abs' src='{p.as_uri()}' style='left:0;top:0;width:{w}px;height:{h}px;object-fit:cover'>"
    return tower_scene(w, h, uid)


def css(ur):
    base = 'Nastaliq' if ur else 'Archivo'
    return f"""
.canvas{{font-family:'{base}',sans-serif;background:#EDF3F4;}}
.ur-on .t{{font-family:'Nastaliq',serif;}}
.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px;}}
.ic{{border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none;}}
.mir{{transform:scaleX(-1);}}
"""


def build(d, lang):
    ur = lang == "ur"
    f = T(ur)
    t = d[lang]
    g = d["layout"]
    navy = C["navy2"]
    # ---------------- header
    hh = g["header_h"]
    header = (f"<div class='abs' style='top:0;left:0;width:1080px;height:{hh}px;background:#fff'></div>"
              f"<div class='abs' style='top:{(hh-120)//2}px;inset-inline-start:26px;width:480px;height:120px'>"
              f"{logo_img('logo-horizontal-light', 'width:480px;height:120px;object-position:' + ('right' if ur else 'left'))}</div>"
              f"<div class='abs' style='top:{(hh-100)//2}px;inset-inline-end:30px;display:flex;align-items:center;gap:18px'>"
              f"<div style='background:{C['red']};border-radius:12px;padding:{'0 18px 8px' if ur else '8px 18px'};box-shadow:0 4px 10px #0003'>{f.head(t['urgent'], 32, 30, '#fff')}</div>"
              f"<div style='filter:drop-shadow(0 4px 8px #0004)'>{flag(d['country'], 140, True, 'hf' + lang)}</div></div>"
              f"<div class='abs' style='top:{hh}px;left:0;width:1080px;height:6px;background:{VOLT}'></div>")
    # ---------------- hero
    hy, H = hh + 6, g["hero_h"]
    pic = hero_picture(d["photo"], 1080, H, lang)
    if ur:
        pic = f"<div class='abs' style='left:0;top:0;width:1080px;height:{H}px;transform:scaleX(-1)'>{pic}</div>"
    bolt = f"<svg width='64' height='84' viewBox='0 0 24 32'><path d='M14 1 L3 18 H11 L9 31 L21 12 H13Z' fill='{VOLT}' stroke='{INK}' stroke-width='1'/></svg>"
    if ur:
        head = (f.txt(t["kicker"], 0, 28, VOLT, "font-weight:700;text-shadow:0 2px 6px #0009", 1.7)
                + f"<div style='display:flex;align-items:center;gap:10px'>{bolt}{f.txt(t['title'], 0, 96, '#fff', 'font-weight:700;text-shadow:0 4px 12px #000A', 1.5)}</div>")
    else:
        head = (f"<div class='mono' style='font-size:20px;color:{VOLT};letter-spacing:3px'>{t['kicker']}</div>"
                f"<div style='display:flex;align-items:center;gap:10px;margin-top:8px'>{bolt}<div class='anton' style='font-size:120px;line-height:1;color:#fff'>{t['title']}</div></div>")
    opener = (f"<div style='display:inline-block;margin-top:{44 if ur else 14}px;background:#000000A0;border-radius:12px;padding:{'2px 16px 8px' if ur else '8px 16px'}'>"
              f"{f.txt(t['opener'], 22, 23, '#fff', 'font-weight:700', 1.7 if ur else 1.2)}</div>")
    hero = (f"<div class='abs' style='top:{hy}px;left:0;width:1080px;height:{H}px;overflow:hidden'>{pic}"
            f"<div class='abs' style='top:{g['head_top']}px;inset-inline-start:40px;width:600px'>{head}{opener}</div></div>")
    # ---------------- grade cards
    gy, gh = hy + H + g["gap"], g["grade_h"]
    cards = "".join(
        f"<div style='flex:1;height:{gh}px;border-radius:22px;overflow:hidden;background:#fff;box-shadow:0 8px 22px rgba(7,28,36,.2);display:flex;flex-direction:column'>"
        f"<div style='background:linear-gradient(100deg,{DEEP},{TEAL});height:{g['grade_head_h']}px;display:flex;align-items:center;justify-content:space-between;padding:0 20px'>"
        f"{f.head(t['role'], 36, 34, '#fff')}"
        f"<div style='background:{VOLT};border-radius:12px;padding:{'0 14px 6px' if ur else '4px 14px'};display:flex;align-items:center;gap:8px'>"
        f"{f.head(t['grade_word'], 24, 24, INK)}<span class='num' style='font-size:40px;color:{INK};line-height:1'>{n}</span></div></div>"
        f"<div style='flex:1;display:flex;align-items:center;justify-content:center;gap:14px;padding:0 18px'>"
        f"<div class='ic' style='width:58px;height:58px;background:{EM}'>{icon('money', 32)}</div>"
        f"<div style='direction:ltr;display:flex;align-items:baseline;gap:8px'><span class='num' style='font-size:76px;color:{navy};line-height:1'>{sal}</span>"
        f"<span class='num' style='font-size:30px;color:{EM}'>SAR</span></div>"
        f"<div style='font-size:40px;font-weight:900;color:{navy}'>+</div>"
        f"<div style='display:flex;align-items:center;gap:6px;background:#E9F6EE;border-radius:14px;padding:{'0 14px 4px' if ur else '6px 14px'}'>"
        f"{icon('food', 28, EM, 2.3)}{f.head(t['food'], 30, 30, EM)}</div></div></div>"
        for n, sal in t["grades"])
    grades = f"<div class='abs' style='top:{gy}px;left:30px;right:30px;display:flex;gap:16px' data-check='grades-{lang}'>{cards}</div>"
    # ---------------- interview + facts
    iy, ih = gy + gh + g["gap"], g["info_h"]
    chips = "".join(
        f"<div style='display:flex;align-items:center;gap:12px;background:#fff;border-radius:14px;padding:{'0 14px 4px' if ur else '6px 14px'};margin-top:10px'>"
        f"<div style='direction:ltr;display:flex;align-items:baseline;gap:6px'><span class='num' style='font-size:46px;color:{C['red']};line-height:1.05'>{dd}</span>"
        f"<span class='num' style='font-size:20px;color:{navy}'>2026</span></div>"
        f"{f.txt(mo, 22, 22, navy, 'font-weight:800', 1.6 if ur else 1.1)}"
        f"<div style='margin-inline-start:auto;background:{EM};border-radius:10px;padding:{'0 12px 4px' if ur else '4px 12px'}'>{f.txt(day, 20, 20, '#fff', 'font-weight:800', 1.6 if ur else 1.1)}</div></div>"
        for dd, mo, day in t["dates"])
    interview = (f"<div style='width:{g['int_w']}px;height:{ih}px;border-radius:22px;background:linear-gradient(160deg,{C['red']},#9E1F1C);padding:{'8px 18px' if ur else '16px 18px'};box-sizing:border-box;box-shadow:0 8px 22px #0003'>"
                 f"<div style='display:flex;align-items:center;gap:10px'>{icon('calendar', 30, VOLT, 2.3)}{f.head(t['int_title'], 28, 26, '#fff')}</div>"
                 f"<div style='display:flex;align-items:center;gap:8px;margin-top:{0 if ur else 6}px'>{icon('pin', 24, VOLT, 2.4)}{f.head(t['int_city'], 30, 30, VOLT)}</div>{chips}</div>")
    facts = "".join(
        f"<div style='width:100%;height:{(ih - 14) / 2}px;background:#fff;border-radius:18px;box-shadow:0 5px 14px rgba(7,28,36,.12);display:flex;align-items:center;gap:12px;padding:0 16px;box-sizing:border-box;border-bottom:5px solid {TEAL}'>"
        f"<div class='ic' style='width:52px;height:52px;background:{TEAL}'>{icon(ic, 28, VOLT, 2.2)}</div>"
        f"<div>{f.label(lab, 16, 22, '#5A6B75', 'margin-bottom:' + ('12px' if ur else '4px'))}{f.txt(val, 34, 34, navy, 'font-weight:800', 1.55 if ur else 1.1)}</div></div>"
        for ic, lab, val in t["facts"])
    info = (f"<div class='abs' style='top:{iy}px;left:30px;right:30px;display:flex;gap:16px' data-check='info-{lang}'>{interview}"
            f"<div style='flex:1;display:flex;flex-wrap:wrap;gap:14px;align-content:flex-start'>{facts}</div></div>")
    # ---------------- benefits bar
    by = iy + ih + g["gap"]
    bens = "".join(f"<div style='display:flex;align-items:center;gap:8px'><div class='ic' style='width:40px;height:40px;background:{VOLT}'>{icon(ic, 22, INK, 2.3)}</div>"
                   f"{f.txt(s, 20, 21, '#fff', 'font-weight:700', 1.6 if ur else 1.1)}</div>" for ic, s in t["benefits"])
    bar = (f"<div class='abs' style='top:{by}px;left:30px;right:30px;height:{g['bar_h']}px;border-radius:18px;background:{EM};display:flex;align-items:center;justify-content:space-around;padding:0 14px' data-check='bar-{lang}'>{bens}</div>")
    # ---------------- CTA
    ct = g["cta_top"]
    nums = "".join(f"<div class='num' style='display:block;font-size:42px;color:{navy};line-height:1.08'>{n}</div>" for n in d["phones"])
    cta = (f"<div class='abs' style='top:{ct}px;left:0;width:1080px;height:{1350-ct}px;background:linear-gradient(100deg,{DEEP},{TEAL});border-top:6px solid {VOLT}'></div>"
           f"<div class='abs' style='top:{ct}px;height:{1350-ct}px;inset-inline-start:30px;width:540px;display:flex;flex-direction:column;justify-content:center'>"
           f"{f.head(t['apply'], 44, 34, VOLT, 'line-height:1.5' if ur else '')}"
           f"{f.txt(t['apply_sub'], 18, 18, '#DCE8EC', 'font-weight:600', 1.7 if ur else 1.2)}"
           f"<div style='display:flex;align-items:center;gap:8px;margin-top:{6 if ur else 8}px'>{icon('mail', 23, VOLT, 2)}"
           f"<span style='font-family:Archivo;font-size:22px;font-weight:700;color:#fff;direction:ltr;unicode-bidi:isolate'>{d['email']}</span></div></div>"
           f"<div class='abs' style='top:{ct+18}px;inset-inline-end:30px;height:{1350-ct-36}px;background:#fff;border-radius:24px;display:flex;align-items:center;gap:14px;"
           f"padding-inline:14px 26px;box-shadow:0 6px 16px #0006'>{whatsapp_icon(68)}<div>{nums}</div></div>")
    return page(f"<div class='{'ur-on' if ur else ''}'>{header}{hero}{grades}{info}{bar}{cta}</div>", css(ur), rtl=ur)


def main(mod_name):
    d = importlib.import_module(f"data.{mod_name}").DATA
    for lang, suffix in (("en", "English"), ("ur", "Urdu")):
        if lang not in d:
            continue
        html = build(d, lang)
        bad = overflow_report(html)
        if bad:
            print(f"[{lang}] overflowing boxes: {bad}")
        print(render(html, f"{d['stem']}-{suffix}.png"))


if __name__ == "__main__":
    main(sys.argv[1])
