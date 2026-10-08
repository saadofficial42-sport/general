"""Style: Full-bleed photo with bold headline overlay.

Top ~half is one large photo of the job (assets/photos/<photo>.jpg|png|webp; a
drawn scene is used only as a flagged placeholder), with a dark gradient, logo
plate, flag and a big headline over it. Below: large high-contrast fact tiles
and a WhatsApp CTA. Mirrors automatically for Urdu.

Usage: python3 src/style_photo.py <data module in src/data/>
"""
import importlib
import sys

import illustrations as IL
from common import C, PHOTOS, WHATSAPP, flag, icon, logo_img, page, render, whatsapp_icon, overflow_report
from style_corporate_grid import T


def photo_html(key, w, h, uid):
    for ext in ("jpg", "jpeg", "png", "webp"):
        p = PHOTOS / f"{key}.{ext}"
        if p.exists():
            return f"<img src='{p.as_uri()}' style='width:{w}px;height:{h}px;object-fit:cover;display:block'>", True
    scene = getattr(IL, key)(400, 300, uid)
    return f"<svg width='{w}' height='{h}' viewBox='0 0 400 300' preserveAspectRatio='xMidYMid slice'>{scene}</svg>", False


def num_div(val, size):
    return f"<div class='num' style='font-size:{size}px;color:{C['navy2']};line-height:1.05'>{val}</div>"


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
    ph = g["photo_h"]
    img, _ = photo_html(d["photo"], 1080, ph, "p" + lang)
    shade = (f"<div class='abs' style='left:0;top:0;width:1080px;height:{ph}px;"
             f"background:linear-gradient(180deg,rgba(10,27,37,.45) 0%,rgba(10,27,37,0) 26%,rgba(10,27,37,.55) 45%,rgba(10,27,37,.95) 100%)'></div>")
    logo = (f"<div class='abs' style='top:22px;inset-inline-start:26px;width:500px;height:126px;background:#fff;border-radius:20px;"
            f"box-shadow:0 8px 20px #0005;display:flex;align-items:center;justify-content:center'>{logo_img('logo-horizontal-light', 'width:460px;height:108px')}</div>")
    flg = f"<div class='abs' style='top:22px;inset-inline-end:28px;filter:drop-shadow(0 6px 12px #0007)'>{flag(d['country'], 200, True, 'pf' + lang)}</div>"
    if ur:
        head = (f"<div style='display:inline-block;background:{C['red']};border-radius:10px;padding:0 16px 6px'>{f.txt(t['kicker'], 0, 26, '#fff', 'font-weight:700', 1.7)}</div>"
                + f.txt(t['title'], 0, 58, '#fff', 'font-weight:700;margin-top:10px;text-shadow:0 3px 12px #000a', 1.7)
                + f.txt(t['sub'], 0, 26, C['gold2'], 'font-weight:700', 1.7))
    else:
        head = (f"<div style='display:inline-block;background:{C['red']};border-radius:10px;padding:6px 16px'><span class='mono' style='font-size:20px;color:#fff'>{t['kicker']}</span></div>"
                f"<div class='anton' style='font-size:96px;line-height:1;color:#fff;margin-top:12px;text-shadow:0 4px 14px #000a'>{t['title']}</div>"
                f"<div class='anton' style='font-size:44px;line-height:1.1;color:{C['gold2']};margin-top:4px'>{t['sub']}</div>")
    headline = f"<div class='abs' style='top:{g['head_top_ur' if ur else 'head_top']}px;inset-inline-start:36px;right:36px'>{head}</div>"
    photo = f"<div class='abs' style='left:0;top:0;width:1080px;height:{ph}px;overflow:hidden'>{img}</div>{shade}{logo}{flg}{headline}"
    # ---------------- fact tiles (2 x 2, big type)
    ty = ph + g["gap"]
    tiles = "".join(
        f"<div style='width:calc(50% - 8px);height:{g['tile_h']}px;background:#fff;border-radius:20px;box-shadow:0 6px 16px rgba(16,33,46,.14);"
        f"border-inline-start:10px solid {col};display:flex;align-items:center;gap:18px;padding:0 22px'>"
        f"<div class='ic' style='width:76px;height:76px;background:{col}'>{icon(ic, 40)}</div>"
        f"<div style='min-width:0'>{f.label(lab, 17, 20, col, 'font-weight:800;margin-bottom:' + ('16px' if ur else '4px'))}"
        f"{num_div(val, vs) if num else f.txt(val, 30, 28, C['navy2'], 'font-weight:800', 1.6 if ur else 1.1)}"
        f"{f.txt(sub, 18, 18, '#3E4A57', 'font-weight:600', 1.6 if ur else 1.2) if sub else ''}</div></div>"
        for ic, lab, val, sub, col, num, vs in t["tiles"])
    tiles_html = f"<div class='abs' style='top:{ty}px;left:30px;right:30px;display:flex;flex-wrap:wrap;gap:16px' data-check='tiles-{lang}'>{tiles}</div>"
    ny = ty + 2 * g["tile_h"] + 16 + g["gap"]
    note = (f"<div class='abs' style='top:{ny}px;left:30px;right:30px;height:{g['note_h']}px;background:{C['navy']};border-radius:18px;"
            f"display:flex;align-items:center;justify-content:center;gap:14px'>"
            f"<div style='line-height:0'>{flag('pakistan', 54, False)}</div>"
            f"<span class='{'mir' if ur else ''}' style='display:inline-flex'>{icon('plane', 36, C['gold2'], 2.2)}</span>"
            f"<div style='line-height:0'>{flag(d['country'], 68, False)}</div>"
            f"{f.txt(t['note'], 26, 26, '#fff', 'font-weight:800', 1.7 if ur else 1.1)}</div>")
    ct = g["cta_top"]
    cta = f"""<div class='abs' style='top:{ct}px;left:0;width:1080px;height:{1350-ct}px;background:linear-gradient(100deg,#B71C1C,{C['red']})'></div>
<div class='abs' style='top:{ct}px;height:{1350-ct}px;inset-inline-start:30px;width:440px;display:flex;align-items:center;gap:12px'>
 <span class='{'mir' if ur else ''}' style='display:inline-flex'>{icon('megaphone', 48, C['gold2'], 2.2)}</span>
 <div>{f.head(t['apply'], 46, 32, '#fff', 'line-height:1.4' if ur else '')}{f.txt(t['apply_sub'], 18, 17, '#FFFFFF', 'margin-top:' + ('22px' if ur else '2px'), 1.5 if ur else 1.2)}</div></div>
<div class='abs' style='top:{ct+13}px;inset-inline-end:30px;height:{1350-ct-26}px;background:#fff;border-radius:999px;display:flex;align-items:center;gap:14px;
 padding-inline:10px 32px;box-shadow:0 6px 16px #0005'>{whatsapp_icon(62)}
 <div class='num' style='font-size:54px;color:{C['navy2']};line-height:1.15'>{WHATSAPP}</div></div>"""
    return page(f"<div class='{'ur-on' if ur else ''}'>{photo}{tiles_html}{note}{cta}</div>", css(ur), rtl=ur)


def main(mod_name):
    d = importlib.import_module(f"data.{mod_name}").DATA
    _, real = photo_html(d["photo"], 10, 10, "x")
    if not real:
        print(f"NOTE: no real photo at assets/photos/{d['photo']}.* — using drawn placeholder")
    for lang, suffix in (("en", "English"), ("ur", "Urdu")):
        html = build(d, lang)
        bad = overflow_report(html)
        if bad:
            print(f"[{lang}] overflowing boxes: {bad}")
        print(render(html, f"{d['stem']}-{suffix}.png"))


if __name__ == "__main__":
    main(sys.argv[1])
