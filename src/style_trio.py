"""Style: Trio photo columns.

White header (big logo, flag, red urgent ribbon); destination-coloured title band
with route pill and posts badge; three tall job columns, each topped by a LARGE
picture of the job (real photo from assets/photos/<photo>.* if present, otherwise
a silhouette scene flagged as a placeholder), salary band and key rows; two detail
panels; CTA with both WhatsApp numbers (order from data) + email. Mirrors for Urdu.

Usage: python3 src/style_trio.py <data module in src/data/>
"""
import importlib
import sys

from common import C, PHOTOS, flag, icon, logo_img, page, render, whatsapp_icon, overflow_report
from style_corporate_grid import T
from style_site import _fig, INK


# ---------------------------------------------------------------- placeholder scenes
def _sky(w, h, uid, top, bottom):
    return (f"<defs><linearGradient id='s{uid}' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='{top}'/>"
            f"<stop offset='1' stop-color='{bottom}'/></linearGradient></defs><rect width='{w}' height='{h}' fill='url(#s{uid})'/>")


def _city(w, base, fill, seed=0):
    xs = [(0, 40, 70), (38, 30, 110), (66, 44, 60), (108, 26, 130), (132, 50, 80), (180, 34, 150), (212, 46, 90),
          (256, 30, 120), (284, 52, 70), (334, 40, 100)]
    return "".join(f"<rect x='{(x + seed) % (w + 40) - 20}' y='{base - hh}' width='{ww}' height='{hh}' fill='{fill}'/>" for x, ww, hh in xs)


def rider_scene(w, h, uid):
    G = h - 18
    sc = (f"<g fill='{INK}' stroke='{INK}' stroke-linecap='round' stroke-linejoin='round'>"
          f"<circle cx='{w*.30}' cy='{G-28}' r='28' fill='none' stroke-width='9'/><circle cx='{w*.70}' cy='{G-28}' r='28' fill='none' stroke-width='9'/>"
          f"<path d='M{w*.30} {G-28} L{w*.40} {G-62} L{w*.62} {G-62} Q{w*.70} {G-60} {w*.72} {G-30}' fill='none' stroke-width='12'/>"
          f"<path d='M{w*.40} {G-60} L{w*.56} {G-60} L{w*.58} {G-80} L{w*.38} {G-80}Z'/>"
          f"<path d='M{w*.70} {G-30} L{w*.66} {G-120} L{w*.72} {G-124}' fill='none' stroke-width='8'/>"
          f"<rect x='{w*.20}' y='{G-140}' width='{w*.17}' height='{w*.15}' rx='6'/><path d='M{w*.28} {G-140+w*.15} L{w*.40} {G-80}' stroke-width='7'/></g>")
    man = _fig(w * .52, G - 78, .62, hip=(-10, -10), sh=(-2, -66), head=(4, -88), lk=(26, -12), lf=(34, 40),
               rk=(30, -16), rf=(36, 40), le=(26, -50), lh=(46, -62), re=(22, -48), rh=(44, -60))
    return (f"<svg width='{w}' height='{h}' style='display:block'>{_sky(w, h, uid, '#7EC8E3', '#FDE7B0')}"
            f"<circle cx='{w*.82}' cy='{h*.3}' r='34' fill='#FFE7A0' opacity='.9'/><g opacity='.35'>{_city(w, G, '#2B5C74')}</g>"
            f"{sc}{man}<rect x='0' y='{G}' width='{w}' height='{h-G}' fill='{INK}'/></svg>")


def driver_scene(w, h, uid):
    G = h - 18
    car = (f"<g fill='{INK}'>"
           f"<path d='M{w*.08} {G-30} Q{w*.08} {G-70} {w*.20} {G-74} L{w*.32} {G-78} Q{w*.40} {G-128} {w*.52} {G-130} "
           f"L{w*.70} {G-130} Q{w*.80} {G-128} {w*.86} {G-82} Q{w*.95} {G-76} {w*.94} {G-30}Z'/>"
           f"<path d='M{w*.37} {G-84} Q{w*.44} {G-118} {w*.53} {G-120} L{w*.60} {G-120} L{w*.60} {G-84}Z' fill='#BFE4F2'/>"
           f"<path d='M{w*.63} {G-84} L{w*.63} {G-120} L{w*.70} {G-120} Q{w*.77} {G-116} {w*.81} {G-84}Z' fill='#BFE4F2'/>"
           f"<circle cx='{w*.25}' cy='{G-26}' r='26' stroke='#2A3A33' stroke-width='6'/><circle cx='{w*.77}' cy='{G-26}' r='26' stroke='#2A3A33' stroke-width='6'/>"
           # driver in the window: head, cap, hands on the wheel
           f"<circle cx='{w*.55}' cy='{G-100}' r='10'/><path d='M{w*.55-11} {G-104} Q{w*.55} {G-120} {w*.55+12} {G-104}Z'/>"
           f"<path d='M{w*.53} {G-90} L{w*.49} {G-84} L{w*.53} {G-84}Z'/><ellipse cx='{w*.47}' cy='{G-94}' rx='4' ry='9'/></g>")
    return (f"<svg width='{w}' height='{h}' style='display:block'>{_sky(w, h, uid, '#3E7FB0', '#F3C978')}"
            f"<g opacity='.4'>{_city(w, G - 6, '#1E3F5A', 30)}</g><rect x='0' y='{G-8}' width='{w}' height='8' fill='#5D6A70'/>"
            + "".join(f"<rect x='{x}' y='{G+4}' width='26' height='4' fill='#E8E2C8'/>" for x in range(6, int(w), 52))
            + f"{car}<rect x='0' y='{G+10}' width='{w}' height='{h-G}' fill='{INK}'/></svg>")


def factory_scene(w, h, uid):
    G = h - 18
    shelves = (f"<g fill='{INK}' opacity='.55'><rect x='{w*.66}' y='{G-170}' width='6' height='170'/><rect x='{w*.96}' y='{G-170}' width='6' height='170'/>"
               + "".join(f"<rect x='{w*.66}' y='{G-y}' width='{w*.31}' height='5'/>" for y in (56, 112, 168))
               + "".join(f"<rect x='{w*.68 + i*30}' y='{G-y-30}' width='26' height='28'/>" for y in (56, 112) for i in range(3)) + "</g>")
    table = (f"<g fill='{INK}'><rect x='{w*.08}' y='{G-80}' width='{w*.48}' height='9'/>"
             f"<rect x='{w*.10}' y='{G-80}' width='7' height='80'/><rect x='{w*.52}' y='{G-80}' width='7' height='80'/>"
             f"<path d='M{w*.14} {G-80} L{w*.14} {G-104} L{w*.30} {G-104} L{w*.30} {G-80}Z'/>"
             f"<path d='M{w*.33} {G-80} L{w*.33} {G-92} Q{w*.40} {G-102} {w*.48} {G-92} L{w*.48} {G-80}Z'/></g>")
    man = _fig(w * .40, G, .70, le=(-14, -112), lh=(-26, -96), re=(16, -110), rh=(4, -96))
    man2 = _fig(w * .80, G, .62, flip=True, le=(-22, -160), lh=(-22, -196), re=(20, -160), rh=(22, -196))
    box = f"<rect x='{w*.80-24}' y='{G-150}' width='48' height='30' rx='3' fill='{INK}'/>"
    win = "".join(f"<rect x='{x}' y='22' width='{w*.16}' height='{h*.30}' rx='4' fill='#FFF3D1' opacity='.75'/>" for x in (w * .06, w * .26, w * .46))
    return (f"<svg width='{w}' height='{h}' style='display:block'>{_sky(w, h, uid, '#B9D3DE', '#F5E3C0')}{win}"
            f"{shelves}{table}{man}{man2}{box}<rect x='0' y='{G}' width='{w}' height='{h-G}' fill='{INK}'/></svg>")


SCENES = {"rider": rider_scene, "driver": driver_scene, "factory": factory_scene}


def job_picture(job, w, h, uid):
    for e in ("jpg", "jpeg", "png", "webp"):
        p = PHOTOS / f"{job['photo']}.{e}"
        if p.exists():
            return f"<img src='{p.as_uri()}' style='width:{w}px;height:{h}px;object-fit:cover;display:block'>"
    return SCENES[job["art"]](w, h, uid)


def css(ur):
    base = 'Nastaliq' if ur else 'Archivo'
    return f"""
.canvas{{font-family:'{base}',sans-serif;background:#EEF4F7;}}
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
    blue, deep, gold, navy = d["blue"], d["deep"], C["gold2"], C["navy2"]
    # ---------------- header
    hh = g["header_h"]
    header = (f"<div class='abs' style='top:0;left:0;width:1080px;height:{hh}px;background:#fff'></div>"
              f"<div class='abs' style='top:{(hh-120)//2}px;inset-inline-start:26px;width:480px;height:120px'>"
              f"{logo_img('logo-horizontal-light', 'width:480px;height:120px;object-position:' + ('right' if ur else 'left'))}</div>"
              f"<div class='abs' style='top:{(hh-104)//2}px;inset-inline-end:30px;display:flex;align-items:center;gap:18px'>"
              f"<div style='background:{C['red']};border-radius:12px;padding:{'0 18px 8px' if ur else '8px 18px'};transform:rotate({3 if ur else -3}deg);box-shadow:0 4px 10px #0003'>"
              f"{f.head(t['urgent'], 34, 30, '#fff')}</div>"
              f"<div style='filter:drop-shadow(0 4px 8px #0004)'>{flag(d['country'], 150, True, 'hf' + lang)}</div></div>")
    # ---------------- title band
    by, bh = hh, g["band_h"]
    if ur:
        title = (f.txt(t['kicker'], 0, 24, gold, 'font-weight:700', 1.7)
                 + f.txt(t['country'], 0, 54, '#fff', 'font-weight:700;margin-top:16px', 1.5))
    else:
        title = (f"<div class='mono' style='font-size:18px;color:{gold};letter-spacing:3px'>{t['kicker']}</div>"
                 f"<div class='anton' style='font-size:76px;line-height:1;color:#fff;margin-top:6px'>{t['country']}</div>")
    route = (f"<div style='display:inline-flex;align-items:center;gap:10px;background:#fff;border-radius:999px;padding:{'0 16px' if ur else '6px 16px'};box-shadow:0 3px 10px #0004'>"
             f"<div style='line-height:0'>{flag('pakistan', 38, False)}</div>{f.txt(t['from'], 17, 18, navy, 'font-weight:800', 1.6 if ur else 1)}"
             f"<div style='width:26px;border-top:3px dashed {blue}'></div><span class='{'mir' if ur else ''}' style='display:inline-flex'>{icon('plane', 26, blue, 2.2)}</span>"
             f"<div style='width:26px;border-top:3px dashed {blue}'></div><div style='line-height:0'>{flag(d['country'], 38, False)}</div>"
             f"{f.txt(t['to'], 17, 18, navy, 'font-weight:800', 1.6 if ur else 1)}</div>"
             f"<div style='display:flex;align-items:center;gap:8px;margin-top:{6 if ur else 10}px'>{icon('pin', 24, gold, 2.4)}"
             f"{f.txt(t['cities'], 22, 21, '#fff', 'font-weight:700', 1.6 if ur else 1)}</div>")
    stat = (f"<div style='width:150px;height:150px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFE9A0,{gold} 60%,#C98B16);"
            f"box-shadow:0 8px 18px #0006;display:flex;flex-direction:column;align-items:center;justify-content:center;border:5px solid #fff'>"
            f"<div class='num' style='font-size:60px;color:{navy};line-height:1'>{t['stat_n']}</div>{f.label(t['stat_label'], 16, 19, navy, 'font-weight:700')}</div>")
    band = (f"<div class='abs' style='top:{by}px;left:0;width:1080px;height:{bh}px;background:linear-gradient(100deg,{deep},{blue})'>"
            f"<svg class='abs' style='left:0;top:0' width='1080' height='{bh}'><path d='M0 {bh} L1080 {bh-34} L1080 {bh}Z' fill='{d['green_stripe']}'/>"
            f"<path d='M0 {bh-6} L1080 {bh-40}' stroke='#fff' stroke-width='5'/><circle cx='{140 if ur else 940}' cy='-30' r='160' fill='#ffffff10'/></svg>"
            f"<div class='abs' style='top:{g['title_top_ur' if ur else 'title_top']}px;inset-inline-start:36px'>{title}</div>"
            f"<div class='abs' style='top:{g['route_top_ur' if ur else 'route_top']}px;inset-inline-start:{g['route_x']}px'>{route}</div>"
            f"<div class='abs' style='top:{(bh-150)//2 - 6}px;inset-inline-end:40px'>{stat}</div></div>")
    # ---------------- job columns
    cy, chh = by + bh + g["gap"], g["col_h"]
    cw, ph = (1080 - 60 - 2 * 14) // 3, g["photo_h"]
    cols = ""
    for i, j in enumerate(t["jobs"]):
        col = j["color"]
        rows = "".join(f"<div style='display:flex;align-items:center;gap:10px;padding:{'1px 0' if ur else '6px 0'};border-top:1px solid #E3E9EE'>"
                       f"<div class='ic' style='width:32px;height:32px;background:{col}1F'>{icon(ic, 19, col, 2.3)}</div>"
                       f"{f.txt(s, 18, 18, navy, 'font-weight:600', 1.6 if ur else 1.15)}</div>" for ic, s in j["rows"])
        cols += (f"<div style='width:{cw}px;height:{chh}px;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 8px 22px rgba(16,33,46,.18);position:relative'>"
                 f"<div style='position:relative;height:{ph}px;overflow:hidden'>{job_picture(j, cw, ph, f'{lang}{i}')}"
                 f"<div style='position:absolute;bottom:0;left:0;right:0;height:60px;background:linear-gradient(0deg,#000a,#0000)'></div>"
                 f"<div style='position:absolute;top:12px;inset-inline-start:12px;background:{gold};border-radius:12px;padding:{'0 12px 4px' if ur else '4px 12px'};display:flex;align-items:center;gap:6px;box-shadow:0 3px 8px #0005'>"
                 f"<span class='num' style='font-size:32px;color:{navy};line-height:1.1'>{j['posts'][0]}</span>{f.label(j['posts'][1], 13, 15, navy, 'font-weight:700')}</div></div>"
                 f"<div style='background:{col};padding:{'2px 16px 6px' if ur else '10px 16px'}'>{f.head(j['title'], 32, 30, '#fff')}"
                 f"{f.txt(j['roles'], 15, 16, '#FFFFFFE0', 'font-weight:600', 1.55 if ur else 1.2)}</div>"
                 f"<div style='padding:{'4px 16px' if ur else '10px 16px'}'>"
                 f"<div style='display:flex;align-items:center;gap:6px'>{icon('pin', 20, C['red'], 2.4)}{f.txt(j['location'], 18, 18, navy, 'font-weight:800', 1.6 if ur else 1.1)}</div>"
                 f"<div style='margin:{'2px 0 4px' if ur else '8px 0'};border:3px solid {col};border-radius:16px;padding:{'0 12px 4px' if ur else '6px 12px'};display:flex;align-items:center;justify-content:space-between;gap:8px'>"
                 f"<div>{f.label(j['salary']['label'], 13, 15, col, 'font-weight:700')}{f.txt(j['salary']['sub'], 14, 15, '#4A5868', 'font-weight:600', 1.5 if ur else 1.15)}</div>"
                 f"<div class='num' style='font-size:54px;color:{navy};line-height:1.05'>{j['salary']['value']}</div></div>"
                 f"{rows}</div></div>")
    columns = f"<div class='abs' style='top:{cy}px;left:30px;right:30px;display:flex;gap:14px' data-check='cols-{lang}'>{cols}</div>"
    # ---------------- panels
    py, pnh = cy + chh + g["gap"], g["panel_h"]

    def panel(title, items, color, numbered):
        li = "".join(f"<div style='display:flex;align-items:center;gap:10px;margin-top:{3 if ur else 5}px'>"
                     f"<div class='ic' style='width:28px;height:28px;background:{color}'>{icon(ic or 'check', 16, '#fff', 2.6)}</div>"
                     f"{f.txt(s, 18, 16, navy, 'font-weight:600', 1.95 if ur else 1.15)}</div>" for ic, s in items)
        return (f"<div style='flex:1;height:{pnh}px;background:#fff;border-radius:20px;box-shadow:0 6px 18px rgba(16,33,46,.14);padding:{'6px 18px' if ur else '14px 18px'};"
                f"border-inline-start:8px solid {color}'>{f.head(title, 22, 21, color)}{li}</div>")
    panels = (f"<div class='abs' style='top:{py}px;left:30px;right:30px;display:flex;gap:14px' data-check='panels-{lang}'>"
              f"{panel(t['p1_title'], t['p1'], blue, False)}{panel(t['p2_title'], t['p2'], t['jobs'][2]['color'], True)}</div>")
    # ---------------- CTA
    ct = g["cta_top"]
    nums = "".join(f"<div class='num' style='display:block;font-size:42px;color:{navy};line-height:1.08'>{n}</div>" for n in d["phones"])
    cta = (f"<div class='abs' style='top:{ct}px;left:0;width:1080px;height:{1350-ct}px;background:linear-gradient(100deg,{deep},{blue})'></div>"
           f"<div class='abs' style='top:{ct}px;height:{1350-ct}px;inset-inline-start:30px;width:540px;display:flex;flex-direction:column;justify-content:center'>"
           f"{f.head(t['tagline'], 30, 26, gold, 'line-height:1.55' if ur else 'line-height:1.1')}"
           f"{f.txt(t['note'], 17, 17, '#E2EEF5', 'font-weight:600;margin-top:' + ('4px' if ur else '6px'), 1.7 if ur else 1.2)}"
           f"<div style='display:flex;align-items:center;gap:8px;margin-top:{10 if ur else 8}px'>{icon('mail', 22, '#fff', 2)}"
           f"<span style='font-family:Archivo;font-size:21px;font-weight:700;color:#fff;direction:ltr;unicode-bidi:isolate'>{d['email']}</span></div></div>"
           f"<div class='abs' style='top:{ct+14}px;inset-inline-end:30px;height:{1350-ct-28}px;background:#fff;border-radius:24px;display:flex;align-items:center;gap:14px;"
           f"padding-inline:14px 26px;box-shadow:0 6px 16px #0005'>{whatsapp_icon(68)}<div>{nums}</div></div>")
    return page(f"<div class='{'ur-on' if ur else ''}'>{header}{band}{columns}{panels}{cta}</div>", css(ur), rtl=ur)


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
