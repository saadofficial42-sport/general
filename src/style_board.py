"""Style: Vacancy board.

White big-logo header, destination-coloured hero (title, script tagline,
waving flag, posts seal, landmark skyline, route pill), a vacancy table
(one row per position: trade thumbnail, posts, salary, age limit) with a
total row, a grid of terms common to all positions, and a WhatsApp CTA.
Mirrors automatically for Urdu.

Usage: python3 src/style_board.py <data module in src/data/>
"""
import importlib
import sys

from common import C, WHATSAPP, flag, icon, logo_img, page, render, whatsapp_icon, overflow_report
from illustrations import belgrade_skyline, kosovo_skyline, photo_or_art
from style_corporate_grid import T

SKYLINES = {"kosovo": kosovo_skyline, "serbia": belgrade_skyline}


def css(ur, d):
    base = 'Nastaliq' if ur else 'Archivo'
    return f"""
.canvas{{font-family:'{base}',sans-serif;background:{C['offwhite']};}}
.ur-on .t{{font-family:'Nastaliq',serif;}}
.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px;}}
.ic{{border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none;}}
.mir{{transform:scaleX(-1);}}
.trow{{display:flex;align-items:center;border-top:1px solid #E3E8F0;}}
.c1{{flex:1;display:flex;align-items:center;gap:14px;min-width:0;padding-inline-start:16px;}}
.c2{{width:{d['cols'][0]}px;text-align:center;flex:none;}}
.c3{{width:{d['cols'][1]}px;text-align:center;flex:none;}}
.c4{{width:{d['cols'][2]}px;text-align:center;flex:none;padding-inline-end:10px;}}
"""


def build(d, lang):
    ur = lang == "ur"
    f = T(ur)
    t = d[lang]
    g = d["layout"]
    blue, gold = d["blue"], d["gold"]
    # ---------------- header
    hh = g["header_h"]
    header = (f"<div class='abs' style='top:0;left:0;width:1080px;height:{hh}px;background:#fff'></div>"
              f"<div class='abs' style='top:{(hh-150)//2}px;left:{(1080-580)//2}px;width:580px;height:150px'>{logo_img('logo-horizontal-light', 'width:580px;height:150px')}</div>"
              f"<div class='abs' style='top:{hh}px;left:0;width:1080px;height:7px;background:linear-gradient(90deg,{blue} 0 70%,{gold} 70% 100%)'></div>")
    # ---------------- hero
    hy, hh2 = hh + 7, g["hero_h"]
    sky = (f"<svg class='abs' style='left:0;bottom:0' width='1080' height='{hh2}'>"
           f"<defs><linearGradient id='hb{lang}' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='{blue}'/><stop offset='1' stop-color='{C['navy']}'/></linearGradient></defs>"
           f"<rect width='1080' height='{hh2}' fill='url(#hb{lang})'/>"
           f"<g opacity='.55'>{SKYLINES[d['country']](1080, hh2, '#3458B8', gold)}</g></svg>")
    if ur:
        title = (f"<div style='display:inline-block;background:{C['red']};border-radius:8px;padding:0 14px 4px'>{f.txt(t['kicker'], 0, 22, '#fff', 'font-weight:700', 1.6)}</div>"
                 + f.txt(t['title'], 0, 50, '#fff', 'font-weight:700;margin-top:4px', 1.75)
                 + f.txt(t['tagline'], 0, 21, gold, 'font-weight:700;margin-top:14px', 1.8))
    else:
        title = (f"<div style='display:inline-block;background:{C['red']};border-radius:8px;padding:5px 14px'><span class='mono' style='font-size:16px;color:#fff'>{t['kicker']}</span></div>"
                 f"<div class='anton' style='font-size:92px;line-height:1;color:#fff;margin-top:10px'>{t['title_a']} <span style='color:{gold}'>{t['title_b']}</span></div>"
                 f"<div class='script' style='font-size:40px;line-height:1.1;color:{gold}'>{t['tagline']}</div>")
    route = (f"<div style='display:inline-flex;align-items:center;gap:10px;margin-top:{12 if ur else 14}px;background:#fff;border-radius:999px;padding:{'0 16px' if ur else '6px 16px'};box-shadow:0 3px 10px #0004'>"
             f"<div style='line-height:0;box-shadow:0 1px 3px #0005'>{flag('pakistan', 40, False)}</div>{f.txt(t['from'], 15, 17, C['navy2'], 'font-weight:700', 1.6 if ur else 1)}"
             f"<div style='width:30px;border-top:3px dashed {blue}'></div><span class='{'mir' if ur else ''}' style='display:inline-flex'>{icon('plane', 26, blue, 2.2)}</span>"
             f"<div style='width:30px;border-top:3px dashed {blue}'></div><div style='line-height:0;box-shadow:0 1px 3px #0005'>{flag(d['country'], 40, False)}</div>"
             f"{f.txt(t['to'], 15, 17, C['navy2'], 'font-weight:700', 1.6 if ur else 1)}</div>")
    seal = (f"<div class='abs' style='top:{g['seal_top']}px;inset-inline-end:36px;width:230px;text-align:center'>"
            f"<div style='display:inline-block;filter:drop-shadow(0 6px 10px #0007)'>{flag(d['country'], 180, True, 'hf' + lang)}</div>"
            f"<div style='margin:4px auto 0;width:200px;background:{gold};border-radius:16px;padding:{'2px 10px 6px' if ur else '6px 10px'};box-shadow:0 4px 12px #0005;display:flex;align-items:center;justify-content:center;gap:10px'>"
            f"<div class='num' style='font-size:46px;color:{C['navy2']};line-height:1.05'>{t['total_n']}</div>"
            f"<div style='text-align:start'>{f.label(t['total_label'], 12, 16, C['navy2'], 'line-height:' + ('1.5' if ur else '1.25'))}</div></div></div>")
    hero = (f"<div class='abs' style='top:{hy}px;left:0;width:1080px;height:{hh2}px;overflow:hidden'>{sky}"
            f"<div class='abs' style='top:{g['title_top_ur' if ur else 'title_top']}px;inset-inline-start:40px;width:700px'>{title}{route}</div>{seal}</div>")
    # ---------------- vacancy table
    ty = hy + hh2 + g["gap"]
    head = (f"<div class='trow' style='background:{C['navy']};border:0;height:{g['thead_h']}px;color:#fff'>"
            f"<div class='c1' style='padding-inline-start:24px'>{f.label(t['th'][0], 14, 18, gold)}</div>"
            f"<div class='c2'>{f.label(t['th'][1], 14, 18, gold, 'text-align:center')}</div>"
            f"<div class='c3'>{f.label(t['th'][2], 14, 18, gold, 'text-align:center')}</div>"
            f"<div class='c4'>{f.label(t['th'][3], 14, 18, gold, 'text-align:center')}</div></div>")
    rows = ""
    for i, r in enumerate(t["rows"]):
        bg = "#fff" if i % 2 == 0 else "#F3F6FC"
        sal_style = f"font-size:{r.get('sal_px', 28)}px;color:{C['navy2']};line-height:1.1"
        rows += (f"<div class='trow' style='background:{bg};height:{g['row_h']}px'>"
                 f"<div class='c1'><div style='width:58px;height:58px;border-radius:50%;overflow:hidden;flex:none;box-shadow:0 0 0 3px {gold}'>{photo_or_art(r['art'], r['art'] + str(i) + lang)}</div>"
                 f"{f.txt(r['name'], 20, 19, C['navy2'], 'font-weight:800;min-width:0', 1.6 if ur else 1.15)}</div>"
                 f"<div class='c2'><div style='display:inline-block;background:{blue};color:#fff;border-radius:12px;padding:2px 14px'><span class='num' style='font-size:32px;line-height:1.15'>{r['posts']}</span></div></div>"
                 f"<div class='c3'>{f.txt(r['sal_label'], 12, 14, '#5A6470', 'text-align:center', 1.4 if ur else 1.1) if r.get('sal_label') else ''}<div class='num' style='{sal_style}'>{r['salary']}</div>"
                 f"{f.txt(r['sal_sub'], 14, 14, '#5A6470', 'text-align:center;font-weight:600', 1.5 if ur else 1.15) if r.get('sal_sub') else ''}</div>"
                 f"<div class='c4'>{f.txt(r['age'], 18, 18, C['navy2'], 'font-weight:700;text-align:center', 1.6 if ur else 1.15)}</div></div>")
    total = (f"<div class='trow' style='background:{gold};height:{g['total_h']}px;border:0'>"
             f"<div class='c1' style='padding-inline-start:24px'>{f.head(t['total_row'], 26, 24, C['navy2'])}</div>"
             f"<div class='c2'><span class='num' style='font-size:40px;color:{C['navy2']};line-height:1'>{t['total_n']}</span></div>"
             f"<div class='c3'></div><div class='c4'></div></div>")
    table = (f"<div class='abs' style='top:{ty}px;left:30px;width:1020px;border-radius:20px;overflow:hidden;box-shadow:0 8px 24px rgba(16,33,46,.16)' data-check='table-{lang}'>"
             f"{head}{rows}{total}</div>")
    # ---------------- common terms
    ny = ty + g["thead_h"] + g["row_h"] * len(t["rows"]) + g["total_h"] + g["gap"] + 4
    tiles = "".join(
        f"<div style='width:calc({100 / g.get('term_cols', 3):.2f}% - {12 * (g.get('term_cols', 3) - 1) / g.get('term_cols', 3):.1f}px);background:#fff;border-radius:16px;box-shadow:0 3px 10px rgba(16,33,46,.1);display:flex;align-items:center;gap:12px;padding:{'4px 14px' if ur else '12px 14px'};height:{g['term_h']}px'>"
        f"<div class='ic' style='width:46px;height:46px;background:{blue}'>{icon(ic, 24)}</div>"
        f"<div style='min-width:0'>{f.label(lab, 11.5, 14, '#5A6470', 'margin-bottom:6px' if ur else '')}"
        f"<div style='display:flex;align-items:center;gap:8px'>{f.txt(val, g.get('term_px', (21, 20))[0], g.get('term_px', (21, 20))[1], C['navy2'], 'font-weight:' + str(g.get('term_w', 800)), 1.85 if ur else 1.18)}"
        f"{('<div style=\"line-height:0;box-shadow:0 1px 3px #0004\">' + flag(extra, 34, False) + '</div>') if extra else ''}</div></div></div>"
        for ic, lab, val, extra in t["terms"])
    terms = (f"<div class='abs' style='top:{ny}px;left:30px;right:30px' data-check='terms-{lang}'>"
             f"<div style='display:flex;align-items:center;gap:10px;margin-bottom:{4 if ur else 12}px'><div style='width:6px;height:24px;border-radius:3px;background:{blue}'></div>"
             f"{f.label(t['terms_title'], 15, 19, blue, 'font-weight:700')}</div>"
             f"<div style='display:flex;flex-wrap:wrap;gap:12px 12px'>{tiles}</div>"
             f"{f.txt(t['footnote'], 14, 15, '#5A6470', 'margin-top:' + ('2px' if ur else '10px'), 1.6 if ur else 1.25) if t.get('footnote') else ''}</div>")
    # ---------------- CTA
    ct = g["cta_top"]
    cta = f"""<div class='abs' style='top:{ct}px;left:0;width:1080px;height:{1350-ct}px;background:linear-gradient(100deg,{C['navy']},{blue})'></div>
<div class='abs' style='top:{ct}px;height:{1350-ct}px;inset-inline-start:36px;width:440px;display:flex;flex-direction:column;justify-content:center'>
 {f.head(t['apply'], 44, 34, gold)}
 {f.txt(t['apply_sub'], 18, 17, '#DCE6F7', 'margin-top:' + ('2px' if ur else '2px'), 1.5 if ur else 1.2, 't' if ur else 'script')}</div>
<div class='abs' style='top:{ct+13}px;inset-inline-end:30px;height:{1350-ct-26}px;background:#fff;border-radius:999px;display:flex;align-items:center;gap:14px;
 padding-inline:10px 32px;box-shadow:0 6px 16px #0006'>{whatsapp_icon(62)}
 <div class='num' style='font-size:54px;color:{C['navy2']};line-height:1.15'>{WHATSAPP}</div></div>"""
    return page(f"<div class='{'ur-on' if ur else ''}'>{header}{hero}{table}{terms}{cta}</div>", css(ur, g), rtl=ur)


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
