"""Style: Shield / single-role spotlight.

Charcoal + emerald + gold. White header (big logo, red urgent tag, flag); charcoal hero
with a LARGE job picture on one side (real photo from assets/photos/<photo>.* if present,
otherwise a silhouette store-aisle scene with a uniformed officer, flagged as placeholder)
and a shield-badge title block on the other; a row of pay/terms tiles; duties and
requirements columns; CTA with both WhatsApp numbers (order from data) + email.
Renders only the languages present in the data (e.g. Urdu only).

Usage: python3 src/style_shield.py <data module in src/data/>
"""
import importlib
import sys

from common import C, PHOTOS, flag, icon, logo_img, page, render, whatsapp_icon, overflow_report
from style_corporate_grid import T

INK, CHAR, CHAR2, EM, GOLD = "#0B1512", "#151D22", "#22303A", "#1E9E4A", "#F0B443"


def aisle_scene(w, h, uid, label="SECURITY"):
    """Store aisle in perspective with a uniformed officer (back view) holding a radio, CCTV camera above."""
    vx, vy = w * .5, h * .42
    shelf = ""
    for side in (-1, 1):
        x0 = 0 if side < 0 else w
        xin = vx - 70 if side < 0 else vx + 70
        shelf += f"<path d='M{x0} 0 L{xin} {vy-80} L{xin} {vy+70} L{x0} {h}Z' fill='#1B2A30'/>"
        for k in range(1, 6):
            t = k / 6
            y_out, y_in = h * t, (vy - 80) + 150 * t
            shelf += f"<path d='M{x0} {y_out} L{xin} {y_in}' stroke='#0E171B' stroke-width='{7 - k * .6:.1f}'/>"
            # product boxes along each shelf
            for m in range(6):
                u = m / 6 + .04
                bx = x0 + (xin - x0) * u
                by_ = y_out + (y_in - y_out) * u
                bw = 26 * (1 - u * .8)
                col = ("#C9653A", "#3E7CB1", "#E2B33C", "#5FA05B", "#B54A4A", "#8A6FB0")[(k + m) % 6]
                shelf += (f"<rect x='{bx - (bw if side > 0 else 0):.1f}' y='{by_ - bw * 1.1:.1f}' width='{bw:.1f}' height='{bw * 1.05:.1f}' "
                          f"fill='{col}' opacity='.55'/>")
    floor = f"<path d='M0 {h} L{vx-70} {vy+70} L{vx+70} {vy+70} L{w} {h}Z' fill='#9AA6A8'/>"
    glow = (f"<defs><radialGradient id='gl{uid}'><stop offset='0' stop-color='#FFF6DC'/><stop offset='1' stop-color='#FFF6DC' stop-opacity='0'/></radialGradient>"
            f"<linearGradient id='bk{uid}' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#E8E2CF'/><stop offset='1' stop-color='#B7BDB6'/></linearGradient></defs>"
            f"<rect width='{w}' height='{h}' fill='url(#bk{uid})'/><ellipse cx='{vx}' cy='{vy}' rx='{w*.5}' ry='{h*.5}' fill='url(#gl{uid})'/>")
    lights = "".join(f"<rect x='{vx - 60 + i * 4}' y='{8 + i * 22}' width='{120 - i * 8}' height='6' rx='3' fill='#FFFDF2' opacity='.9'/>" for i in range(4))
    cam = (f"<g transform='translate({w*.80} 30)' fill='{INK}'><rect x='-4' y='0' width='8' height='22'/>"
           f"<rect x='-38' y='18' width='46' height='22' rx='5' transform='rotate(18 0 30)'/><circle cx='-34' cy='38' r='5' fill='#E53935'/></g>")
    # officer (back view): cap, broad jacket, radio with antenna at the shoulder
    ox, oy, s = w * .5, h - 8, h / 330
    off = (f"<g transform='translate({ox} {oy}) scale({s})' fill='{INK}'>"
           f"<path d='M-34 0 L-30 -118 L30 -118 L34 0 L10 0 L4 -70 L-4 -70 L-10 0Z'/>"
           f"<path d='M-62 -120 Q-64 -200 -40 -214 L40 -214 Q64 -200 62 -120 L54 -116 L52 -150 L46 -112 L-46 -112 L-52 -150 L-54 -116Z'/>"
           f"<path d='M-64 -126 L-70 -60 L-58 -58 L-54 -122Z'/><path d='M64 -126 L54 -96 L42 -150Z'/>"
           f"<rect x='-14' y='-232' width='28' height='22'/><circle cx='0' cy='-250' r='26'/>"
           f"<path d='M-28 -252 Q-28 -284 0 -286 Q28 -284 28 -252Z'/><path d='M-30 -254 L12 -258 L40 -246 L10 -250Z'/>"
           f"<rect x='30' y='-208' width='16' height='36' rx='3'/><rect x='40' y='-246' width='4' height='40'/>"
           f"<text x='0' y='-150' font-family='Anton' font-size='26' fill='#E8E2CF' text-anchor='middle' letter-spacing='1'>{label}</text></g>")
    return f"<svg width='{w}' height='{h}' style='display:block'>{glow}{lights}{floor}{shelf}{cam}{off}</svg>"


def job_picture(name, w, h, uid, label="SECURITY"):
    for e in ("jpg", "jpeg", "png", "webp"):
        p = PHOTOS / f"{name}.{e}"
        if p.exists():
            return f"<img src='{p.as_uri()}' style='width:{w}px;height:{h}px;object-fit:cover;display:block'>"
    return aisle_scene(w, h, uid, label)


def css(ur):
    base = 'Nastaliq' if ur else 'Archivo'
    return f"""
.canvas{{font-family:'{base}',sans-serif;background:#EEF2EF;}}
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
              f"<div style='background:{C['red']};border-radius:12px;padding:{'0 18px 8px' if ur else '8px 18px'};display:flex;align-items:center;gap:10px;box-shadow:0 4px 10px #0003'>"
              f"<span class='{'mir' if ur else ''}' style='display:inline-flex'>{icon('megaphone', 30)}</span>{f.head(t['urgent'], 32, 30, '#fff')}</div>"
              f"<div style='filter:drop-shadow(0 4px 8px #0004)'>{flag(d['country'], 140, True, 'hf' + lang)}</div></div>"
              f"<div class='abs' style='top:{hh}px;left:0;width:1080px;height:6px;background:{EM}'></div>")
    # ---------------- hero
    hy, H = hh + 6, g["hero_h"]
    pw = g["pic_w"]
    pic = (f"<div class='abs' style='top:0;inset-inline-end:0;width:{pw}px;height:{H}px;overflow:hidden'>{job_picture(d['photo'], pw, H, lang, d.get('jacket', 'SECURITY'))}"
           f"<div style='position:absolute;inset:0;background:linear-gradient({'270deg' if ur else '90deg'},{CHAR} 0,#151D2200 30%)'></div></div>")
    shield = (f"<svg width='92' height='106' viewBox='0 0 92 106' style='flex:none'><path d='M46 4 L86 18 V52 Q86 86 46 102 Q6 86 6 52 V18Z' fill='{EM}' stroke='{GOLD}' stroke-width='5'/>"
              f"<path d='M28 54 L42 68 L66 40' fill='none' stroke='#fff' stroke-width='8' stroke-linecap='round' stroke-linejoin='round'/></svg>")
    if ur:
        title = (f.txt(t["kicker"], 0, 24, GOLD, 'font-weight:700', 1.7)
                 + f.txt(t["title"], 0, 52, '#fff', 'font-weight:700;margin-top:10px', 1.6)
                 + f"<div style='font-family:Anton;font-size:30px;color:#B9C6C0;letter-spacing:1.5px;direction:ltr;text-align:right;margin-top:2px'>{t['title_en']}</div>")
    else:
        title = (f"<div class='mono' style='font-size:18px;color:{GOLD};letter-spacing:3px'>{t['kicker']}</div>"
                 f"<div class='anton' style='font-size:76px;line-height:1;color:#fff;margin-top:8px'>{t['title']}</div>")
    loc = (f"<div style='display:inline-flex;align-items:center;gap:10px;background:{EM};border-radius:12px;padding:{'0 16px 6px' if ur else '8px 16px'};margin-top:{14 if ur else 18}px'>"
           f"{icon('pin', 26, '#fff', 2.4)}{f.txt(t['where'], 22, 23, '#fff', 'font-weight:800', 1.7 if ur else 1.1)}</div>")
    opener = f.txt(t["opener"], 22, 22, "#DCE5E1", "font-weight:600;margin-top:" + ("10px" if ur else "16px"), 1.75 if ur else 1.3)
    hero = (f"<div class='abs' style='top:{hy}px;left:0;width:1080px;height:{H}px;background:{CHAR};overflow:hidden'>{pic}"
            f"<div class='abs' style='top:{g['title_top']}px;inset-inline-start:36px;width:{1080 - pw - 20}px'>"
            f"<div style='display:flex;align-items:flex-start;gap:16px'>{shield}<div>{title}</div></div>{loc}{opener}</div></div>")
    # ---------------- terms tiles
    ty = hy + H
    tiles = "".join(
        f"<div style='flex:{fl};min-width:0;padding:{'6px 12px 8px' if ur else '14px 14px'};display:flex;align-items:center;gap:10px;"
        f"border-inline-start:{'0' if i == 0 else '1px solid #ffffff22'}'>"
        f"<div class='ic' style='width:50px;height:50px;background:{GOLD}'>{icon(ic, 27, CHAR, 2.3)}</div>"
        f"<div style='min-width:0'>{f.label(lab, 14, 16, '#BFD9CB', 'margin-bottom:' + ('2px' if ur else '4px'))}"
        f"{(f'<div class=num style=\"font-size:{vs}px;color:#fff;line-height:1.05;white-space:nowrap\">{val}</div>') if num else f.txt(val, 19, 19, '#fff', 'font-weight:800', 1.6 if ur else 1.15)}"
        f"{f.txt(sub, 14, 15, '#BFD9CB', 'font-weight:600', 1.5 if ur else 1.15) if sub else ''}</div></div>"
        for i, (ic, lab, val, num, vs, sub, fl) in enumerate(t["tiles"]))
    tiles_html = (f"<div class='abs' style='top:{ty}px;left:0;width:1080px;height:{g['tiles_h']}px;background:linear-gradient(100deg,#0F5E35,{EM});"
                  f"display:flex;align-items:stretch;padding:0 20px;box-sizing:border-box' data-check='tiles-{lang}'>{tiles}</div>")
    # ---------------- duties + requirements
    ly = ty + g["tiles_h"] + g["gap"]
    lh_ = 1350 - ly - (1350 - g["cta_top"]) - g["gap"]

    def column(title, ic, items, color, flex, numbered):
        li = "".join(
            f"<div style='display:flex;align-items:flex-start;gap:10px;margin-top:{g['li_gap_ur'] if ur else 8}px'>"
            + (f"<div class='num' style='width:28px;height:28px;border-radius:8px;background:{color};color:#fff;font-size:16px;line-height:28px;text-align:center;flex:none;margin-top:{6 if ur else 0}px'>{n + 1}</div>"
               if numbered else f"<div class='ic' style='width:28px;height:28px;background:{color};margin-top:{6 if ur else 0}px'>{icon('check', 17, '#fff', 3)}</div>")
            + f"{f.txt(s, 18, g['li_px_ur'], navy, 'font-weight:600', g['li_lh_ur'] if ur else 1.22)}</div>"
            for n, s in enumerate(items))
        return (f"<div style='flex:{flex};min-width:0;height:{lh_}px;background:#fff;border-radius:20px;box-shadow:0 6px 18px rgba(16,33,46,.12);"
                f"padding:{'8px 20px' if ur else '16px 20px'};border-top:7px solid {color}'>"
                f"<div style='display:flex;align-items:center;gap:12px'><div class='ic' style='width:44px;height:44px;background:{color}'>{icon(ic, 24)}</div>"
                f"{f.head(title, 26, 25, color)}</div>{li}</div>")
    lists = (f"<div class='abs' style='top:{ly}px;left:30px;right:30px;display:flex;gap:14px' data-check='lists-{lang}'>"
             f"{column(t['duties_title'], 'doc', t['duties'], CHAR2, 1.08, True)}{column(t['req_title'], 'user', t['reqs'], EM, 1, False)}</div>")
    # ---------------- CTA
    ct = g["cta_top"]
    nums = "".join(f"<div class='num' style='display:block;font-size:42px;color:{navy};line-height:1.08'>{n}</div>" for n in d["phones"])
    cta = (f"<div class='abs' style='top:{ct}px;left:0;width:1080px;height:{1350-ct}px;background:{CHAR};border-top:6px solid {GOLD}'></div>"
           f"<div class='abs' style='top:{ct}px;height:{1350-ct}px;inset-inline-start:30px;width:540px;display:flex;flex-direction:column;justify-content:center'>"
           f"{f.head(t['apply'], 42, 32, GOLD, 'line-height:1.5' if ur else '')}"
           f"{f.txt(t['apply_sub'], 18, 18, '#DCE5E1', 'font-weight:600', 1.7 if ur else 1.2)}"
           f"<div style='display:flex;align-items:center;gap:8px;margin-top:{6 if ur else 8}px'>{icon('mail', 23, GOLD, 2)}"
           f"<span style='font-family:Archivo;font-size:22px;font-weight:700;color:#fff;direction:ltr;unicode-bidi:isolate'>{d['email']}</span></div></div>"
           f"<div class='abs' style='top:{ct+18}px;inset-inline-end:30px;height:{1350-ct-36}px;background:#fff;border-radius:24px;display:flex;align-items:center;gap:14px;"
           f"padding-inline:14px 26px;box-shadow:0 6px 16px #0006'>{whatsapp_icon(68)}<div>{nums}</div></div>")
    return page(f"<div class='{'ur-on' if ur else ''}'>{header}{hero}{tiles_html}{lists}{cta}</div>", css(ur), rtl=ur)


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
