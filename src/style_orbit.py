"""Style: Circular centrepiece with orbiting badges.

White big-logo header, deep-green headline band with waving destination
flag, a landscape scene (mountains + local landmark) with a large circular
photo/illustration of the worker and benefit badges orbiting it, a route
pill, a numbered documents grid, and a navy WhatsApp CTA bar.
Mirrors automatically for Urdu.

Usage: python3 src/style_orbit.py <data module in src/data/>
"""
import importlib
import sys

from common import C, WHATSAPP, flag, icon, logo_img, page, render, whatsapp_icon, overflow_report
from illustrations import mountains, photo_or_art, yurt
from style_corporate_grid import T


def css(ur, bw=262):
    base = 'Nastaliq' if ur else 'Archivo'
    return f"""
.canvas{{font-family:'{base}',sans-serif;background:{C['offwhite']};}}
.ur-on .t{{font-family:'Nastaliq',serif;}}
.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px;}}
.ic{{border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none;}}
.mir{{transform:scaleX(-1);}}
.badge{{position:absolute;width:{bw}px;background:#fff;border-radius:18px;box-shadow:0 6px 18px rgba(16,33,46,.18);
        display:flex;align-items:center;gap:12px;padding:10px 14px;}}
"""


def badge(b, side, top, f, color, big=False):
    pos = "inset-inline-start:24px" if side == "start" else "inset-inline-end:24px"
    val = ""
    if b.get("value"):
        val = (f"<div class='num' style='font-size:{b.get('size', 30)}px;color:{C['navy2']};line-height:1.1'>{b['value']}</div>"
               if b.get("num", True) else f.txt(b["value"], 23 if big else 17, 22 if big else 18, C["navy2"], "font-weight:800", 1.8 if f.ur else 1.15))
    sub = f.txt(b["sub"], 17 if big else 13.5, 17 if big else 14.5, "#3E4A57", "font-weight:600", 1.5 if f.ur else 1.15) if b.get("sub") else ""
    return (f"<div class='badge' style='{pos};top:{top}px;border-inline-start:6px solid {color}'>"
            f"<div class='ic' style='width:{58 if big else 50}px;height:{58 if big else 50}px;background:{color}'>{icon(b['icon'], 31 if big else 27)}</div>"
            f"<div style='min-width:0'>{f.label(b['label'], 14 if big else 11.5, 17 if big else 14.5, color, 'font-weight:800;line-height:' + ('1.9;margin-bottom:6px' if f.ur else '1.25'))}{val}{sub}</div></div>")


def build(d, lang):
    ur = lang == "ur"
    f = T(ur)
    t = d[lang]
    g = d["layout"]
    accent = d.get("accent", C["red"])
    # ---------------- header
    header = f"""<div class='abs' style='top:0;left:0;width:1080px;height:{g['header_h']}px;background:#fff'></div>
<div class='abs' style='top:{(g['header_h']-150)//2}px;left:{(1080-580)//2}px;width:580px;height:150px'>{logo_img('logo-horizontal-light', 'width:580px;height:150px')}</div>
<div class='abs' style='top:{g['header_h']}px;left:0;width:1080px;height:8px;background:linear-gradient(90deg,{accent} 0 50%,{C['gold']} 50% 100%)'></div>"""
    # ---------------- headline band
    by, bh = g["header_h"] + 8, g["band_h"]
    if ur:
        title = (f.txt(t['title'], 0, 50, '#fff', 'font-weight:700;text-align:center', 1.7) +
                 f.txt(t['dest'], 0, 28, C['gold2'], 'text-align:center;margin-top:6px', 1.5))
    else:
        title = (f"<div class='anton' style='font-size:82px;color:#fff;line-height:1;text-align:center;letter-spacing:1px'>{t['title']}</div>"
                 f"<div class='script' style='font-size:50px;color:{C['gold2']};line-height:1.05;text-align:center'>{t['dest']}</div>")
    band = f"""<div class='abs' style='top:{by}px;left:0;width:1080px;height:{bh}px;background:linear-gradient(135deg,{C['green']},#0A3A29);overflow:hidden'>
 <svg class='abs' style='left:0;top:0' width='1080' height='{bh}'><path d='M0 {bh} L1080 {bh*0.35} L1080 {bh} Z' fill='#ffffff' opacity='.05'/></svg>
 <div class='abs' style='left:240px;right:240px;top:{g['title_top_ur' if ur else 'title_top']}px'>{title}</div></div>
<div class='abs' style='top:{by + 26}px;inset-inline-start:-46px;width:250px;background:{accent};color:#fff;text-align:center;
 transform:rotate({45 if ur else -45}deg) translateY(10px);box-shadow:0 4px 10px #0005;padding:{'4px 0 8px' if ur else '6px 0'}'>{f.head(t['urgent'], 26, 26, '#fff', 'text-align:center;line-height:1.5')}</div>
<div class='abs' style='top:{by + 16}px;inset-inline-end:26px;filter:drop-shadow(0 6px 10px #0006)'>{flag(d['country'], 190, True, 'kf' + lang)}</div>"""
    # ---------------- orbit scene
    sy, sh = by + bh, g["scene_h"]
    cx, cr = 540, g["circle_r"]
    ccy = g["circle_cy"]
    scene_bg = (f"<svg class='abs' style='left:0;top:0' width='1080' height='{sh}'><defs><linearGradient id='sky{lang}' x1='0' y1='0' x2='0' y2='1'>"
                f"<stop offset='0' stop-color='#CFE3F2'/><stop offset='1' stop-color='{C['offwhite']}'/></linearGradient></defs>"
                f"<rect width='1080' height='{sh}' fill='url(#sky{lang})'/>"
                f"<g transform='translate(0 {sh-230})' opacity='.9'>{mountains(1080, 200, '#A9C0D2', '#7E9AB2')}</g>"
                f"<rect y='{sh-34}' width='1080' height='34' fill='#7E9AB2' opacity='.9'/>"
                f"{yurt(150 if not ur else 840, sh - 30, 90, '#FBF8F0', accent)}{yurt(850 if not ur else 150, sh - 30, 80, '#FBF8F0', accent)}</svg>")
    ring = (f"<svg class='abs' style='left:{cx-cr-58}px;top:{ccy-cr-58}px' width='{2*cr+116}' height='{2*cr+116}'>"
            f"<circle cx='{cr+58}' cy='{cr+58}' r='{cr+44}' fill='none' stroke='{C['gold']}' stroke-width='3' stroke-dasharray='10 8'/>"
            f"<circle cx='{cr+58}' cy='{cr+58}' r='{cr+10}' fill='#fff'/></svg>")
    circle = (f"<div class='abs' style='left:{cx-cr}px;top:{ccy-cr}px;width:{2*cr}px;height:{2*cr}px;border-radius:50%;overflow:hidden;"
              f"box-shadow:0 0 0 7px {accent},0 12px 30px #0004'>{photo_or_art(d['art'], 'big' + lang)}</div>")
    opener = (f"<div class='abs' style='top:18px;left:0;right:0;display:flex;justify-content:center'>"
              f"<div style='background:{C['navy']};color:#fff;border-radius:999px;padding:{'2px 26px 6px' if ur else '9px 24px'};box-shadow:0 4px 12px #0003'>"
              f"{f.txt(t['opener'], 23 if g.get('big_text') else 18, 22 if g.get('big_text') else 19, '#fff', 'font-weight:700;text-align:center', 1.8 if ur else 1.2)}</div></div>")
    big = g.get("big_text", False)
    badges = "".join(badge(b, "start", g["badge_tops"][i], f, b.get("color", C["green"]), big) for i, b in enumerate(t["badges_start"]))
    badges += "".join(badge(b, "end", g["badge_tops"][i], f, b.get("color", accent), big) for i, b in enumerate(t["badges_end"]))
    dash = f"<div style='width:34px;border-top:3px dashed {C['navy']}'></div>"
    plane = f"<span class='{'mir' if ur else ''}' style='display:inline-flex'>{icon('plane', 28, accent, 2.2)}</span>"
    route = (f"<div class='abs' style='top:{g['route_top']}px;left:0;right:0;display:flex;justify-content:center'>"
             f"<div style='display:inline-flex;align-items:center;gap:9px;background:#fff;border-radius:999px;padding:{'2px 18px 4px' if ur else '6px 18px'};box-shadow:0 4px 12px #0003'>"
             f"<div style='line-height:0;box-shadow:0 1px 3px #0005'>{flag('pakistan', 42, False)}</div>{f.txt(t['from'], 19, 19, C['navy2'], 'font-weight:800', 1.8 if ur else 1)}"
             f"{dash}{plane}{dash}<div style='line-height:0;box-shadow:0 1px 3px #0005'>{flag(d['country'], 48, False)}</div>"
             f"{f.txt(t['to'], 19, 19, C['navy2'], 'font-weight:800', 1.8 if ur else 1)}</div></div>")
    scene = f"""<div class='abs' style='top:{sy}px;left:0;width:1080px;height:{sh}px;overflow:hidden'>{scene_bg}{ring}{circle}{opener}{badges}{route}</div>"""
    # ---------------- documents
    dy = sy + sh
    items = "".join(
        f"<div style='width:calc(33.33% - 10px);background:#fff;border-radius:14px;box-shadow:0 3px 10px rgba(16,33,46,.12);"
        f"display:flex;align-items:center;gap:10px;padding:{'4px 12px' if ur else '10px 12px'};min-height:{g['doc_h']}px;position:relative'>"
        f"<div class='num' style='position:absolute;top:-8px;inset-inline-start:-6px;width:28px;height:28px;border-radius:50%;background:{accent};color:#fff;"
        f"font-size:16px;line-height:28px;text-align:center'>{n+1}</div>"
        f"<div class='ic' style='width:44px;height:44px;background:{C['green']}14'>{icon(ic, 24, C['green'], 2)}</div>"
        f"{f.txt(txt, 15.5, 15.5, C['navy2'], 'min-width:0;font-weight:600', 1.7 if ur else 1.2)}</div>"
        for n, (ic, txt) in enumerate(t.get("documents", [])))
    docs = f"""<div class='abs' style='top:{dy}px;left:0;width:1080px;height:{g['cta_top']-dy}px;background:{C['offwhite']}'></div>
<div class='abs' style='top:{dy + 14}px;left:30px;right:30px' data-check='docs-{lang}'>
 <div style='display:flex;align-items:center;gap:12px;margin-bottom:{8 if ur else 18}px'>
  <div style='flex:1;height:2px;background:{C['gold']}'></div>
  <div class='ic' style='width:36px;height:36px;background:{C['gold']}'>{icon('doc', 20, C['navy2'])}</div>
  {f.head(t.get('docs_title', ''), 28, 26, C['green'])}
  <div style='flex:1;height:2px;background:{C['gold']}'></div></div>
 <div style='display:flex;flex-wrap:wrap;gap:{g['doc_gap']}px 15px'>{items}</div></div>"""
    if t.get("highlights"):  # big highlight tiles instead of a documents grid
        hl = "".join(
            f"<div style='flex:1;min-width:0;background:{bg};border-radius:18px;box-shadow:0 4px 12px rgba(16,33,46,.14);"
            f"display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:{2 if ur else 6}px;padding:10px'>"
            f"<div class='ic' style='width:58px;height:58px;background:#ffffff2E'>{icon(ic, 32)}</div>"
            f"{f.head(big, 36, 28, '#fff', 'text-align:center')}"
            f"{f.txt(small, 19, 16, '#FFFFFF', 'text-align:center;font-weight:600;margin-top:' + ('6px' if ur else '0'), 1.75 if ur else 1.2)}</div>"
            for ic, big, small, bg in t["highlights"])
        docs = (f"<div class='abs' style='top:{dy}px;left:0;width:1080px;height:{g['cta_top']-dy}px;background:{C['offwhite']}'></div>"
                f"<div class='abs' style='top:{dy + 18}px;left:30px;right:30px;height:{g['cta_top'] - dy - 36}px;display:flex;gap:16px' data-check='docs-{lang}'>{hl}</div>")
    # ---------------- CTA
    ct = g["cta_top"]
    cta = f"""<div class='abs' style='top:{ct}px;left:0;width:1080px;height:{1350-ct}px;background:linear-gradient(100deg,{C['navy2']},{C['navy']})'></div>
<div class='abs' style='top:{ct}px;height:{1350-ct}px;inset-inline-start:36px;width:440px;display:flex;flex-direction:column;justify-content:center'>
 {f.head(t['apply'], 44, 34, C['gold2'])}
 {f.txt(t['note'], 18, 18, '#FFFFFF', 'margin-top:' + ('10px' if ur else '4px'), 1.5 if ur else 1.3)}</div>
<div class='abs' style='top:{ct+13}px;inset-inline-end:30px;height:{1350-ct-26}px;background:#fff;border-radius:999px;display:flex;align-items:center;gap:14px;
 padding-inline:10px 32px;box-shadow:0 6px 16px #0006'>{whatsapp_icon(62)}
 <div class='num' style='font-size:54px;color:{C['navy2']};line-height:1.15'>{WHATSAPP}</div></div>"""
    return page(f"<div class='{'ur-on' if ur else ''}'>{header}{band}{scene}{docs}{cta}</div>", css(ur, g.get('badge_w', 262)), rtl=ur)


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
