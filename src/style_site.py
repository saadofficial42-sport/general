"""Style: Construction-site silhouette.

White big-logo header with waving flag; full-width sunset hero with a construction
site in silhouette (tower crane, building frame, scaffold and workers doing each
trade) — or a real photo from assets/photos/<hero_photo>.* when one exists;
headline + visa/departure badges in the sky. Below: trades table (posts + salary)
beside a highlighted certified-workers card, a terms strip, a documents/selection
note bar and a CTA with both WhatsApp numbers + email. Mirrors for Urdu.

Usage: python3 src/style_site.py <data module in src/data/>
"""
import importlib
import sys

import illustrations as IL
from common import C, PHOTOS, WHATSAPP, flag, icon, logo_img, page, render, whatsapp_icon, overflow_report
from style_corporate_grid import T
from style_photocard import EMAIL, PHONE2

INK = "#071510"


# ---------------------------------------------------------------- silhouettes
def _fig(x, y, s=1.0, flip=False, **j):
    """Worker silhouette with hard hat. Feet at (x, y). Joints in local units (standing ~175 tall)."""
    P = dict(head=(0, -160), sh=(0, -138), hip=(0, -88), le=(-14, -108), lh=(-16, -80), re=(14, -108), rh=(16, -80),
             lk=(-6, -45), lf=(-10, 0), rk=(6, -45), rf=(10, 0))
    P.update(j)
    L = lambda a, b, w: f'<path d="M{a[0]} {a[1]} L{b[0]} {b[1]}" stroke-width="{w}"/>'
    hx, hy = P["head"]
    body = (L(P["hip"], P["lk"], 17) + L(P["lk"], P["lf"], 14) + L(P["hip"], P["rk"], 17) + L(P["rk"], P["rf"], 14)
            + L(P["sh"], P["hip"], 30)
            + L(P["sh"], P["le"], 12) + L(P["le"], P["lh"], 10) + L(P["sh"], P["re"], 12) + L(P["re"], P["rh"], 10))
    feet = "".join(f'<path d="M{f[0]-4} {f[1]} L{f[0]+9} {f[1]}" stroke-width="9"/>' for f in (P["lf"], P["rf"]))
    head = (f'<circle cx="{hx}" cy="{hy}" r="12"/>'
            f'<path d="M{hx-14} {hy-4} Q{hx-13} {hy-22} {hx} {hy-22} Q{hx+13} {hy-22} {hx+14} {hy-4}Z"/>'
            f'<path d="M{hx-17} {hy-4} L{hx+19} {hy-4}" stroke-width="4"/>')
    tf = f"translate({x} {y}) scale({-s if flip else s} {s})"
    return (f'<g transform="{tf}" fill="{INK}" stroke="{INK}" stroke-linecap="round" stroke-linejoin="round">'
            f'{body}{feet}{head}</g>')


def site_scene(w, h, uid):
    G = h - 8                       # ground line
    f1, f2, f3 = G - 112, G - 218, G - 318   # slab levels
    x0, x1 = 548, 905                # building frame extent
    sky = (f"<defs><linearGradient id='sk{uid}' x1='0' y1='0' x2='0' y2='1'>"
           f"<stop offset='0' stop-color='#05261A'/><stop offset='.45' stop-color='#0C4A34'/>"
           f"<stop offset='.78' stop-color='#C9832A'/><stop offset='1' stop-color='#F6C35A'/></linearGradient>"
           f"<radialGradient id='sun{uid}'><stop offset='0' stop-color='#FFE9A8'/><stop offset='.35' stop-color='#FFD23F' stop-opacity='.9'/>"
           f"<stop offset='1' stop-color='#FFD23F' stop-opacity='0'/></radialGradient></defs>"
           f"<rect width='{w}' height='{h}' fill='url(#sk{uid})'/>"
           f"<circle cx='735' cy='{G-40}' r='190' fill='url(#sun{uid})'/><circle cx='735' cy='{G-40}' r='58' fill='#FFE7A0'/>")
    city = f"<g opacity='.55' transform='translate(0 {h - 175})'>{IL.riyadh_skyline(w, 175, '#2E3F2A')}</g>"
    col = lambda x, top: f'<rect x="{x-7}" y="{top}" width="14" height="{G-top}"/>'
    slab = lambda y, a, b: f'<rect x="{a}" y="{y-12}" width="{b-a}" height="12"/>'
    frame = (f'<g fill="{INK}">' + "".join(col(x, f2 - 2) for x in (x0, 668, 788, x1))
             + col(x0, f3) + col(668, f3) + slab(f1, x0 - 12, x1 + 12) + slab(f2, x0 - 12, x1 + 12)
             + slab(f3, x0 - 12, 700)
             # rebar sticking up from unfinished columns + top slab
             + "".join(f'<path d="M{x+dx} {f2-12} V{f2-62}" stroke="{INK}" stroke-width="3"/>' for x in (788, x1) for dx in (-4, 4))
             + "".join(f'<path d="M{x} {f3-12} V{f3-34}" stroke="{INK}" stroke-width="3"/>' for x in range(x0, 700, 22))
             + "</g>")
    # scaffold on the building's left face
    sc = (f'<g stroke="{INK}" stroke-width="5" fill="none">'
          f'<path d="M488 {G} V{f2-60} M528 {G} V{f2-60}"/>'
          + "".join(f'<path d="M482 {y} H{x0-8}"/>' for y in (f1 - 4, f2 - 4, G - 56))
          + "".join(f'<path d="M488 {a} L528 {b}"/>' for a, b in ((G, f1 - 4), (f1 - 4, f2 - 4)))
          + '</g>')
    # tower crane
    cx = 985
    crane = (f'<g fill="none" stroke="{INK}" stroke-width="4">'
             f'<path d="M{cx-12} {G} V40 M{cx+12} {G} V40"/>'
             + "".join(f'<path d="M{cx-12} {y} L{cx+12} {y-26} M{cx-12} {y-26} H{cx+12}"/>' for y in range(G, 52, -26))
             + f'<path d="M{cx-12} 40 H{cx+12} L{cx} 4Z M600 44 H{cx+90} M600 58 H{cx+90} M{cx} 4 L620 44 M{cx} 4 L{cx+90} 44"/>'
             + "".join(f'<path d="M{x} 44 L{x+18} 58 L{x+36} 44"/>' for x in range(604, cx + 80, 36))
             + f'<path d="M640 58 V{f2-120}" stroke-width="2"/></g>'
             f'<rect x="{cx+52}" y="58" width="34" height="26" fill="{INK}"/>'
             f'<rect x="{cx-22}" y="62" width="20" height="18" fill="{INK}"/>'
             # hanging rebar bundle
             f'<path d="M640 {f2-120} L610 {f2-100} M640 {f2-120} L670 {f2-100}" stroke="{INK}" stroke-width="2"/>'
             f'<rect x="592" y="{f2-100}" width="96" height="8" rx="2" fill="{INK}"/>')
    # ---- workers
    men = [
        # steel fixer crouched tying rebar on the top slab
        _fig(612, f3 - 12, .62, hip=(0, -62), sh=(10, -108), head=(20, -128), lk=(18, -40), lf=(-6, 0), rk=(26, -34), rf=(8, 0),
             le=(30, -86), lh=(46, -58), re=(26, -92), rh=(44, -64)),
        # electrician on a step ladder, reaching to the ceiling of floor 1
        f'<path d="M802 {f1-12} L822 {f1-90} L842 {f1-12} M807 {f1-34} H837 M812 {f1-58} H832" stroke="{INK}" stroke-width="5" fill="none"/>',
        _fig(822, f1 - 92, .48, re=(10, -170), rh=(12, -205), le=(-16, -110), lh=(-22, -84)),
        # plumber kneeling with a long pipe on floor 1
        _fig(700, f1 - 12, .52, hip=(0, -70), sh=(4, -122), head=(6, -144), lk=(22, -38), lf=(26, 0), rk=(-10, -6), rf=(-46, -2),
             le=(26, -98), lh=(44, -76), re=(18, -100), rh=(40, -82)),
        f'<path d="M712 {f1-48} L762 {f1-36}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>',
        # painter on the scaffold with a roller on a pole
        _fig(508, f1 - 8, .52, re=(22, -150), rh=(30, -178), le=(10, -128), lh=(24, -150)),
        f'<path d="M520 {f1-96} L{x0-14} {f1-170}" stroke="{INK}" stroke-width="4"/><rect x="{x0-22}" y="{f1-186}" width="10" height="34" rx="3" fill="{INK}"/>',
        # carpenter carrying a plank on his shoulder
        _fig(400, G, .52, le=(-20, -150), lh=(-8, -168), re=(18, -110), rh=(24, -84), lk=(-14, -44), lf=(-28, 0), rk=(10, -46), rf=(22, 0)),
        f'<rect x="340" y="{G-92}" width="124" height="8" rx="2" fill="{INK}" transform="rotate(-6 400 {G-88})"/>',
        # loader carrying a carton
        _fig(300, G, .52, flip=True, le=(-26, -122), lh=(-32, -152), re=(22, -122), rh=(30, -152), lk=(-12, -44), lf=(-26, 0), rk=(10, -46), rf=(20, 0)),
        f'<rect x="276" y="{G-112}" width="48" height="32" rx="3" fill="{INK}"/>',
        f'<g fill="{INK}"><rect x="186" y="{G-34}" width="46" height="34"/><rect x="194" y="{G-64}" width="38" height="30"/><rect x="236" y="{G-34}" width="34" height="34"/></g>',
    ]
    ground = f'<rect x="0" y="{G}" width="{w}" height="{h-G}" fill="{INK}"/>'
    return f"<svg class='abs' style='left:0;top:0' width='{w}' height='{h}'>{sky}{city}{crane}{frame}{sc}{''.join(men)}{ground}</svg>"


def hero_photo(name, w, h):
    for e in ("jpg", "jpeg", "png", "webp"):
        p = PHOTOS / f"{name}.{e}"
        if p.exists():
            return (f"<img class='abs' src='{p.as_uri()}' style='left:0;top:0;width:{w}px;height:{h}px;object-fit:cover'>"
                    f"<div class='abs' style='left:0;top:0;width:{w}px;height:{h}px;background:linear-gradient(90deg,#05261AEE 0,#05261AAA 45%,#0000 75%)'></div>")
    return None


def css(ur):
    base = 'Nastaliq' if ur else 'Archivo'
    return f"""
.canvas{{font-family:'{base}',sans-serif;background:{C['offwhite']};}}
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
    green, gold, navy = d["green"], C["gold2"], C["navy2"]
    # ---------------- header
    hh = g["header_h"]
    header = (f"<div class='abs' style='top:0;left:0;width:1080px;height:{hh}px;background:#fff'></div>"
              f"<div class='abs' style='top:{(hh-130)//2}px;inset-inline-start:24px;width:560px;height:130px'>"
              f"{logo_img('logo-horizontal-light', 'width:560px;height:130px;object-position:' + ('right' if ur else 'left'))}</div>"
              f"<div class='abs' style='top:{(hh-110)//2}px;inset-inline-end:36px;filter:drop-shadow(0 4px 8px #0005)'>{flag(d['country'], 165, True, 'hf' + lang)}</div>"
              f"<div class='abs' style='top:{hh}px;left:0;width:1080px;height:6px;background:{gold}'></div>")
    # ---------------- hero
    hy, H = hh + 6, g["hero_h"]
    bg = hero_photo(d.get("hero_photo", ""), 1080, H) or site_scene(1080, H, lang)
    if ur:  # mirror the scene so the headline side stays clear
        bg = f"<div class='abs' style='left:0;top:0;width:1080px;height:{H}px;transform:scaleX(-1)'>{bg}</div>"
    if ur:
        head = (f"<div style='display:inline-block;background:{C['red']};border-radius:10px;padding:0 16px 6px'>{f.txt(t['kicker'], 0, 26, '#fff', 'font-weight:700', 1.6)}</div>"
                + f.txt(t['country'], 0, 70, '#fff', 'font-weight:700;margin-top:2px', 1.65))
    else:
        head = (f"<div style='display:inline-block;background:{C['red']};border-radius:10px;padding:6px 16px'><span class='mono' style='font-size:20px;color:#fff;letter-spacing:3px'>{t['kicker']}</span></div>"
                f"<div class='anton' style='font-size:104px;line-height:1;color:#fff;margin-top:10px'>{t['country']}</div>")
    badges = "".join(
        f"<div style='display:flex;align-items:center;gap:10px;background:{bgc};border-radius:999px;padding:{'0 18px 4px 14px' if ur else '7px 20px 7px 12px'};box-shadow:0 4px 12px #0005'>"
        f"<div class='ic {'mir' if ur and ic == 'plane' else ''}' style='width:38px;height:38px;background:{fg}'>{icon(ic, 22, bgc, 2.4)}</div>"
        f"{f.head(txt, 26, 24, fg)}</div>"
        for ic, txt, bgc, fg in ((
            "visa", t["badges"][0], gold, navy), ("plane", t["badges"][1], "#fff", green)))
    opener = f.txt(t["opener"], 25, 24, "#fff", "font-weight:700;text-shadow:0 2px 6px #0008", 1.7 if ur else 1.25)
    hero = (f"<div class='abs' style='top:{hy}px;left:0;width:1080px;height:{H}px;overflow:hidden'>{bg}"
            f"<div class='abs' style='top:{g['head_top_ur' if ur else 'head_top']}px;inset-inline-start:36px;width:560px'>{head}"
            f"<div style='display:flex;gap:12px;margin-top:{6 if ur else 16}px'>{badges}</div>"
            f"<div style='margin-top:{4 if ur else 14}px'>{opener}</div></div></div>")
    # ---------------- trades table
    ty = hy + H + g["gap"]
    rh, th = g["row_h"], g["thead_h"]
    thead = (f"<div style='display:flex;align-items:center;height:{th}px;background:{navy};padding-inline:18px'>"
             f"<div style='flex:1'>{f.label(t['th'][0], 15, 19, gold)}</div>"
             f"<div style='width:110px;text-align:center'>{f.label(t['th'][1], 15, 19, gold)}</div>"
             f"<div style='width:200px;text-align:center'>{f.label(t['th'][2], 15, 19, gold)}</div></div>")
    rows = "".join(
        f"<div style='display:flex;align-items:center;height:{rh}px;padding-inline:14px 18px;background:{'#fff' if i % 2 == 0 else '#EEF5F0'}'>"
        f"<div style='flex:1;display:flex;align-items:center;gap:12px;min-width:0'>"
        f"<div class='ic' style='width:46px;height:46px;background:{green}'>{icon(ic, 26)}</div>"
        f"{f.txt(name, 24, 23, navy, 'font-weight:800;white-space:nowrap', 1.7 if ur else 1.1)}</div>"
        f"<div style='width:110px;text-align:center'><span class='num' style='background:{gold};border-radius:10px;padding:0 14px;font-size:32px;color:{navy};line-height:1.25'>{n}</span></div>"
        f"<div style='width:200px;text-align:center;direction:ltr'><span class='num' style='font-size:30px;color:{navy};line-height:1.1'>1200 + 300</span>"
        f"<span class='num' style='font-size:20px;color:{green};margin-inline-start:6px'>SAR</span></div></div>"
        for i, (ic, name, n) in enumerate(t["rows"]))
    table = (f"<div class='abs' style='top:{ty}px;inset-inline-start:30px;width:{g['table_w']}px;border-radius:18px;overflow:hidden;"
             f"box-shadow:0 8px 22px rgba(16,33,46,.16);background:#fff' data-check='table-{lang}'>{thead}{rows}</div>")
    # ---------------- certified card
    cw = 1080 - 60 - g["table_w"] - 16
    chh = th + rh * len(t["rows"])
    cert = (f"<div class='abs' style='top:{ty}px;inset-inline-end:30px;width:{cw}px;height:{chh}px;border-radius:18px;overflow:hidden;"
            f"background:linear-gradient(160deg,{green},#003A1D);box-shadow:0 8px 22px rgba(16,33,46,.22);color:#fff' data-check='cert-{lang}'>"
            f"<div style='background:{gold};height:{th}px;display:flex;align-items:center;justify-content:center;gap:8px'>"
            f"{icon('shield', 24, navy, 2.4)}<span class='num' style='font-size:26px;color:{navy}'>NAVTTC</span>{f.label(t['cert_word'], 15, 19, navy, 'font-weight:700')}</div>"
            f"<div style='padding:{'4px 18px' if ur else '12px 18px'}'>"
            + "".join(f"<div style='display:flex;align-items:center;gap:10px;margin-bottom:{4 if ur else 6}px'>"
                      f"<div class='ic' style='width:40px;height:40px;background:#ffffff26'>{icon(ic, 22)}</div>"
                      f"{f.txt(s, 23, 22, '#fff', 'font-weight:800', 1.7 if ur else 1.12)}</div>" for ic, s in t["cert_roles"])
            + f"<div style='margin-top:{2 if ur else 8}px;background:#ffffff1F;border-radius:14px;padding:{'2px 14px 6px' if ur else '8px 14px'}'>"
            f"{f.label(t['total_label'], 14, 17, '#FFFFFFD9')}"
            f"<div style='direction:ltr;text-align:{"right" if ur else "left"}'><span class='num' style='font-size:52px;color:{gold};line-height:1.05'>1500</span>"
            f"<span class='num' style='font-size:26px;color:#fff;margin-inline-start:8px'>SAR</span></div>"
            f"<div style='direction:ltr;text-align:{"right" if ur else "left"};font-family:Archivo;font-size:18px;font-weight:700;color:#fff'>{t['basic']}</div></div>"
            f"<div style='display:flex;align-items:center;gap:10px;margin-top:{4 if ur else 10}px'>{icon('user', 26, gold, 2.4)}"
            f"{f.txt(t['age'], 23, 22, '#fff', 'font-weight:800', 1.7 if ur else 1.1)}</div></div></div>")
    # ---------------- terms strip
    sy = ty + chh + g["gap"]
    terms = "".join(
        f"<div style='flex:{fl};height:{g['term_h']}px;background:#fff;border-radius:16px;box-shadow:0 4px 12px rgba(16,33,46,.12);"
        f"display:flex;align-items:center;gap:12px;padding:0 14px;min-width:0;border-bottom:5px solid {green}'>"
        f"<div class='ic' style='width:50px;height:50px;background:{green}'>{icon(ic, 27)}</div>"
        f"<div style='min-width:0'>{f.label(lab, 14, 17, '#4A5868', 'margin-bottom:' + ('10px' if ur else '4px'))}"
        f"{f.txt(val, vpx, vpx - 2, navy, 'font-weight:800' + (';white-space:nowrap' if vpx > 22 else ''), 1.6 if ur else 1.1)}</div></div>"
        for ic, lab, val, vpx, fl in t["terms"])
    terms_html = f"<div class='abs' style='top:{sy}px;left:30px;right:30px;display:flex;gap:12px' data-check='terms-{lang}'>{terms}</div>"
    # ---------------- note bar
    ny = sy + g["term_h"] + g["gap"]
    note = (f"<div class='abs' style='top:{ny}px;left:30px;right:30px;height:{g['note_h']}px;display:flex;gap:12px' data-check='note-{lang}'>"
            f"<div style='flex:1.25;background:#FFF6DA;border:3px solid {C['gold']};border-radius:16px;display:flex;align-items:center;gap:12px;padding:0 16px'>"
            f"{icon('doc', 34, navy, 2.2)}{f.txt(t['docs'], 21, 20, navy, 'font-weight:800', 1.6 if ur else 1.15)}</div>"
            f"<div style='flex:1;background:{C['red']};border-radius:16px;display:flex;align-items:center;justify-content:center;gap:12px;padding:0 16px'>"
            f"{icon('check', 34, '#fff', 3)}{f.head(t['cv'], 34, 28, '#fff')}</div></div>")
    # ---------------- CTA
    ct = g["cta_top"]
    nums = "".join(f"<div class='num' style='display:block;font-size:40px;color:{navy};line-height:1.08'>{n}</div>" for n in (WHATSAPP, PHONE2))
    cta = (f"<div class='abs' style='top:{ct}px;left:0;width:1080px;height:{1350-ct}px;background:linear-gradient(100deg,{C['navy']},{green})'></div>"
           f"<div class='abs' style='top:{ct}px;height:{1350-ct}px;inset-inline-start:30px;width:520px;display:flex;flex-direction:column;justify-content:center'>"
           f"{f.head(t['apply'], 46, 34, gold, 'line-height:1.4' if ur else '')}"
           f"<div style='display:flex;align-items:center;gap:8px;margin-top:{14 if ur else 6}px'>{icon('mail', 24, '#fff', 2)}"
           f"<span style='font-family:Archivo;font-size:23px;font-weight:700;color:#fff;direction:ltr;unicode-bidi:isolate'>{EMAIL}</span></div></div>"
           f"<div class='abs' style='top:{ct+10}px;inset-inline-end:30px;height:{1350-ct-20}px;background:#fff;border-radius:24px;display:flex;align-items:center;gap:14px;"
           f"padding-inline:14px 28px;box-shadow:0 6px 16px #0005'>{whatsapp_icon(66)}<div>{nums}</div></div>")
    return page(f"<div class='{'ur-on' if ur else ''}'>{header}{hero}{table}{cert}{terms_html}{note}{cta}</div>", css(ur), rtl=ur)


def main(mod_name):
    d = importlib.import_module(f"data.{mod_name}").DATA
    for lang, suffix in (("en", "English"), ("ur", "Urdu")):
        html = build(d, lang)
        bad = overflow_report(html)
        if bad:
            print(f"[{lang}] overflowing boxes: {bad}")
        print(render(html, f"{d['stem']}-{suffix}.png"))


if __name__ == "__main__":
    main(sys.argv[1])
