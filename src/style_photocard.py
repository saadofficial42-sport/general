"""Style: Photo card.

White logo header; destination-green hero with headline on one side and a LARGE real
photo (rounded frame) on the other, plus two smaller real photos; salary/benefit tiles;
numbered documents grid; payment-terms box; CTA with both WhatsApp numbers + email.
Mirrors automatically for Urdu.

Usage: python3 src/style_photocard.py <data module in src/data/>
"""
import importlib
import sys

import illustrations as IL
from common import C, PHOTOS, WHATSAPP, flag, icon, logo_img, page, render, whatsapp_icon, overflow_report
from style_corporate_grid import T

PHONE2 = "+92 317 0363690"
EMAIL = "hr@rslinksconsultants.com"


def photo(name, w, h, radius=22, border=6, extra=""):
    p = next(PHOTOS / f"{name}.{e}" for e in ("png", "jpg", "jpeg", "webp") if (PHOTOS / f"{name}.{e}").exists())
    return (f"<div style='width:{w}px;height:{h}px;border-radius:{radius}px;overflow:hidden;border:{border}px solid #fff;"
            f"box-shadow:0 10px 26px #0006;{extra}'><img src='{p.as_uri()}' style='width:100%;height:100%;object-fit:cover;display:block'></div>")


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
    green = d["green"]
    # ---------------- header
    hh = g["header_h"]
    header = (f"<div class='abs' style='top:0;left:0;width:1080px;height:{hh}px;background:#fff'></div>"
              f"<div class='abs' style='top:{(hh-120)//2}px;inset-inline-start:26px;width:500px;height:120px'>"
              f"{logo_img('logo-horizontal-light', 'width:500px;height:120px;object-position:' + ('right' if ur else 'left'))}</div>"
              f"<div class='abs' style='top:16px;inset-inline-end:30px;display:flex;align-items:center;gap:16px'>"
              f"<div style='background:{C['red']};border-radius:12px;padding:{'2px 18px 8px' if ur else '8px 18px'};display:flex;align-items:center;gap:10px'>"
              f"<span class='{'mir' if ur else ''}' style='display:inline-flex'>{icon('megaphone', 32)}</span>{f.head(t['urgent'], 34, 30, '#fff')}</div>"
              f"<div style='filter:drop-shadow(0 4px 8px #0005)'>{flag(d['country'], 150, True, 'hf' + lang)}</div></div>"
              f"<div class='abs' style='top:{hh}px;left:0;width:1080px;height:6px;background:{C['gold2']}'></div>")
    # ---------------- hero
    hy, hh2 = hh + 6, g["hero_h"]
    sky = (f"<svg class='abs' style='left:0;top:0' width='1080' height='{hh2}'>"
           f"<defs><linearGradient id='hg{lang}' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='{green}'/><stop offset='1' stop-color='#00331A'/></linearGradient></defs>"
           f"<rect width='1080' height='{hh2}' fill='url(#hg{lang})'/>"
           f"<g opacity='.35'>{IL.riyadh_skyline(1080, hh2, '#2FA466')}</g></svg>")
    main = f"<div class='abs' style='top:22px;inset-inline-end:30px'>{photo(d['photos'][0], 470, hh2 - 44)}</div>"
    thumbs = (f"<div class='abs' style='top:{g['thumb_top']}px;inset-inline-start:36px;display:flex;gap:18px'>"
              + "".join(photo(n, 236, g['thumb_h'], 16, 5) for n in d["photos"][1:]) + "</div>")
    if ur:
        head = (f.txt(t['opener'], 0, 22, C['gold2'], 'font-weight:700', 1.7)
                + f.txt(t['title'], 0, 64, '#fff', 'font-weight:700', 1.6)
                + f.txt(t['subtitle'], 0, 28, '#fff', 'font-weight:700', 1.7))
    else:
        head = (f"<div style='font-size:22px;font-weight:800;color:{C['gold2']};line-height:1.25'>{t['opener']}</div>"
                f"<div class='anton' style='font-size:104px;line-height:1;color:#fff;margin-top:8px'>{t['title']}</div>"
                f"<div class='anton' style='font-size:42px;line-height:1.05;color:#fff'>{t['subtitle']}</div>")
    posts = (f"<div style='display:inline-flex;align-items:center;gap:12px;background:{C['gold2']};border-radius:14px;"
             f"padding:{'0 18px 4px' if ur else '6px 18px'};margin-top:{8 if ur else 16}px;box-shadow:0 4px 12px #0004'>"
             f"<span class='num' style='font-size:46px;color:{C['navy2']};line-height:1.1'>{t['posts_n']}</span>"
             f"{f.head(t['posts_word'], 30, 26, C['navy2'])}</div>")
    hero = (f"<div class='abs' style='top:{hy}px;left:0;width:1080px;height:{hh2}px;overflow:hidden'>{sky}{main}"
            f"<div class='abs' style='top:{g['head_top_ur' if ur else 'head_top']}px;inset-inline-start:36px;width:510px'>{head}{posts}</div>{thumbs}</div>")
    # ---------------- salary / benefits tiles
    sy = hy + hh2 + g["gap"]
    tiles = "".join(
        f"<div style='flex:{fl};height:{g['tile_h']}px;background:{bg};border-radius:18px;box-shadow:0 6px 16px rgba(16,33,46,.16);"
        f"display:flex;align-items:center;gap:14px;padding:0 18px;min-width:0'>"
        f"<div class='ic' style='width:62px;height:62px;background:#ffffff2E'>{icon(ic, 34)}</div>"
        f"<div style='min-width:0'>{f.label(lab, 15, 18, '#FFFFFFD9', 'margin-bottom:' + ('6px' if ur else '4px'))}"
        f"{(f'<div class=num style=\"font-size:{vs}px;color:#fff;line-height:1.05\">{val}</div>') if num else f.txt(val, 26, 24, '#fff', 'font-weight:800', 1.6 if ur else 1.1)}"
        f"</div></div>"
        for ic, lab, val, num, vs, fl, bg in t["tiles"])
    tiles_html = f"<div class='abs' style='top:{sy}px;left:30px;right:30px;display:flex;gap:14px' data-check='tiles-{lang}'>{tiles}</div>"
    # ---------------- documents
    dy = sy + g["tile_h"] + g["gap"]
    docs = "".join(
        f"<div style='width:calc(25% - 9px);height:{g['doc_h']}px;background:#fff;border-radius:14px;box-shadow:0 3px 10px rgba(16,33,46,.12);"
        f"display:flex;align-items:center;gap:10px;padding:0 12px;position:relative'>"
        f"<div class='num' style='width:30px;height:30px;border-radius:50%;background:{green};color:#fff;font-size:17px;line-height:30px;text-align:center;flex:none'>{n+1}</div>"
        f"{f.txt(txt, 19, 18, C['navy2'], 'font-weight:800;min-width:0', 1.7 if ur else 1.15)}</div>"
        for n, txt in enumerate(t["documents"]))
    docs_html = (f"<div class='abs' style='top:{dy}px;left:30px;right:30px' data-check='docs-{lang}'>"
                 f"<div style='display:flex;align-items:center;gap:10px;margin-bottom:{4 if ur else 12}px'>"
                 f"<div class='ic' style='width:40px;height:40px;background:{green}'>{icon('doc', 22)}</div>"
                 f"{f.head(t['docs_title'], 30, 28, C['navy2'])}</div>"
                 f"<div style='display:flex;flex-wrap:wrap;gap:12px'>{docs}</div></div>")
    # ---------------- payment terms
    py = dy + g["docs_block_h"] + g["gap"]
    pay = (f"<div class='abs' style='top:{py}px;left:30px;right:30px;height:{g['pay_h']}px;background:#FFF6DA;border:3px solid {C['gold']};"
           f"border-radius:18px;display:flex;align-items:center;gap:18px;padding:0 22px' data-check='pay-{lang}'>"
           f"<div class='ic' style='width:62px;height:62px;background:{C['gold']}'>{icon('money', 34, C['navy2'])}</div>"
           f"<div style='min-width:0;flex:1'>{f.head(t['pay_title'], 28, 26, C['navy2'])}"
           f"<div style='display:flex;gap:26px;flex-wrap:wrap;margin-top:{2 if ur else 6}px'>"
           + "".join(f"<div style='display:flex;align-items:center;gap:8px'>{icon('check', 22, green, 3)}"
                     f"{f.txt(p, 21, 20, C['navy2'], 'font-weight:700', 1.7 if ur else 1.2)}</div>" for p in t["pay"])
           + "</div></div></div>")
    # ---------------- CTA
    ct = g["cta_top"]
    nums = "".join(f"<div class='num' style='display:block;font-size:40px;color:{C['navy2']};line-height:1.08'>{n}</div>" for n in (WHATSAPP, PHONE2))
    cta = (f"<div class='abs' style='top:{ct}px;left:0;width:1080px;height:{1350-ct}px;background:linear-gradient(100deg,{green},#004D26)'></div>"
           f"<div class='abs' style='top:{ct}px;height:{1350-ct}px;inset-inline-start:30px;width:520px;display:flex;flex-direction:column;justify-content:center'>"
           f"{f.head(t['apply'], 44, 34, C['gold2'], 'line-height:1.4' if ur else '')}"
           f"<div style='display:flex;align-items:center;gap:8px;margin-top:{8 if ur else 4}px'>{icon('mail', 24, '#fff', 2)}"
           f"<span style='font-family:Archivo;font-size:22px;font-weight:700;color:#fff;direction:ltr;unicode-bidi:isolate'>{EMAIL}</span></div></div>"
           f"<div class='abs' style='top:{ct+10}px;inset-inline-end:30px;height:{1350-ct-20}px;background:#fff;border-radius:24px;display:flex;align-items:center;gap:14px;"
           f"padding-inline:14px 28px;box-shadow:0 6px 16px #0005'>{whatsapp_icon(66)}<div>{nums}</div></div>")
    return page(f"<div class='{'ur-on' if ur else ''}'>{header}{hero}{tiles_html}{docs_html}{pay}{cta}</div>", css(ur), rtl=ur)


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
