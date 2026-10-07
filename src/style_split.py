"""Style: Split columns with large job scenes.

Destination-green hero (logo plate, headline, waving flag, skyline), then
one tall column per job: a LARGE scene of the work (CLAUDE.md picture rule)
with the job title on a ribbon, a burst salary panel and fact rows; then a
shared facilities/requirements strip, an "interviews ongoing" banner and a
WhatsApp CTA. Mirrors automatically for Urdu.

Usage: python3 src/style_split.py <data module in src/data/>
"""
import importlib
import sys

from common import C, WHATSAPP, flag, icon, logo_img, page, render, whatsapp_icon, overflow_report
import illustrations as IL
from style_corporate_grid import T


def css(ur, green):
    base = 'Nastaliq' if ur else 'Archivo'
    return f"""
.canvas{{font-family:'{base}',sans-serif;background:{C['offwhite']};}}
.ur-on .t{{font-family:'Nastaliq',serif;}}
.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px;}}
.ic{{border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none;}}
.mir{{transform:scaleX(-1);}}
.col{{position:absolute;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 8px 24px rgba(16,33,46,.16);}}
.frow{{display:flex;align-items:center;gap:10px;border-top:1px dashed #D6DEE8;}}
"""


def burst(color):
    """Starburst behind the salary."""
    import math
    pts = " ".join(f"{100 + (100 if i % 2 == 0 else 86) * math.cos(math.radians(i * 7.5)):.1f},"
                   f"{60 + (60 if i % 2 == 0 else 50) * math.sin(math.radians(i * 7.5)):.1f}" for i in range(48))
    return f"<svg class='abs' style='left:0;top:0' width='100%' height='100%' viewBox='0 0 200 120' preserveAspectRatio='none'><polygon points='{pts}' fill='{color}'/></svg>"


def column(job, x, y, w, h, f, d, uid):
    ur = f.ur
    green = d["green"]
    sh = d["layout"]["scene_h"]
    scene = getattr(IL, job["scene"])(400, 300, uid)
    rows = "".join(
        f"<div class='frow' style='padding:{'0' if ur else '6px'} 0'>"
        f"<div class='ic' style='width:34px;height:34px;background:{green}1A'>{icon(ic, 19, green, 2.4)}</div>"
        f"<div style='min-width:0;flex:1'>{f.txt(txt, 17.5, 17.5, C['navy2'], '', 1.75 if ur else 1.25)}</div></div>"
        for ic, txt in job["rows"])
    tasks = ""
    if job.get("tasks"):
        chips = "".join(f"<div style='display:flex;align-items:center;gap:6px;background:{green};color:#fff;border-radius:999px;padding:{'0 12px 2px' if ur else '5px 12px'}'>"
                        f"{icon('check', 14, '#fff', 3.2)}{f.txt(tk, 15, 16, '#fff', 'font-weight:700;white-space:nowrap', 1.6 if ur else 1.1)}</div>" for tk in job["tasks"])
        tasks = (f"<div style='margin-top:{4 if ur else 10}px'>{f.label(job['tasks_title'], 12, 15, '#5A6470', 'margin-bottom:' + ('2px' if ur else '6px'))}"
                 f"<div style='display:flex;flex-wrap:wrap;gap:6px'>{tasks if False else chips}</div></div>")
    sal = job["salary"]
    return f"""<div class='col' style='inset-inline-start:{x}px;top:{y}px;width:{w}px;height:{h}px' data-check='{uid}'>
<div class='abs' style='left:0;top:0;width:{w}px;height:{sh}px'><svg width='{w}' height='{sh}' viewBox='0 0 400 300' preserveAspectRatio='xMidYMid slice'>{scene}</svg></div>
<div class='abs' style='top:{sh - (64 if ur else 54)}px;inset-inline-start:0;background:{C['navy']};color:#fff;padding:{'0 22px 4px' if ur else '8px 22px'};
  border-start-end-radius:18px;border-end-end-radius:18px;box-shadow:0 4px 10px #0004'>{f.head(job['title'], 38, 30, '#fff', 'line-height:1.55' if ur else '')}</div>
<div class='abs' style='top:{sh - 54}px;inset-inline-end:16px;background:{C['red']};color:#fff;border-radius:10px;padding:{'0 12px 2px' if ur else '6px 12px'}'>
  {f.label(job['badge'], 12, 15, '#fff')}</div>
<div class='abs' style='top:{sh + 14}px;left:20px;right:20px;height:118px'>
  <div class='abs' style='inset:0'>{burst(C['gold2'])}</div>
  <div class='abs' style='inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center'>
   <div style='background:{C['red']};border-radius:8px;padding:{'0 12px 2px' if ur else '2px 12px'}'>{f.label(sal['label'], 13, 16, '#fff')}</div>
   <div class='num' style='font-size:58px;color:{C['navy2']};line-height:1.05'>{sal['value']}</div></div></div>
<div class='abs' style='top:{sh + 142}px;left:20px;right:20px'>{rows}{tasks}</div>
</div>"""


def build(d, lang):
    ur = lang == "ur"
    f = T(ur)
    t = d[lang]
    g = d["layout"]
    green = d["green"]
    hh = g["hero_h"]
    # ---------------- hero
    sky = (f"<svg class='abs' style='left:0;top:0' width='1080' height='{hh}'>"
           f"<defs><linearGradient id='hg{lang}' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='{green}'/><stop offset='1' stop-color='#003D1E'/></linearGradient></defs>"
           f"<rect width='1080' height='{hh}' fill='url(#hg{lang})'/>"
           f"<g transform='{'translate(1080 0) scale(-1 1)' if ur else ''}' opacity='.45'>{IL.riyadh_skyline(1080, hh, '#2FA466')}</g>"
           f"<rect y='{hh-6}' width='1080' height='6' fill='{C['gold2']}'/></svg>")
    logo = (f"<div class='abs' style='top:22px;inset-inline-start:28px;width:520px;height:132px;background:#fff;border-radius:22px;"
            f"box-shadow:0 8px 20px #0004;display:flex;align-items:center;justify-content:center'>{logo_img('logo-horizontal-light', 'width:480px;height:114px')}</div>")
    flg = f"<div class='abs' style='top:20px;inset-inline-end:30px;filter:drop-shadow(0 6px 10px #0006)'>{flag(d['country'], 210, True, 'sf' + lang)}</div>"
    if ur:
        head = (f"<div style='display:inline-block;background:{C['red']};border-radius:8px;padding:0 14px 4px'>{f.txt(t['kicker'], 0, 22, '#fff', 'font-weight:700', 1.6)}</div>"
                + f.txt(t['title'], 0, 50, '#fff', 'font-weight:700;margin-top:8px', 1.7)
                + f.txt(t['opener'], 0, 20, C['gold2'], 'font-weight:700', 1.7))
    else:
        head = (f"<div style='display:inline-block;background:{C['red']};border-radius:8px;padding:5px 14px'><span class='mono' style='font-size:16px;color:#fff'>{t['kicker']}</span></div>"
                f"<div class='anton' style='font-size:74px;line-height:1;color:#fff;margin-top:10px'>{t['title']}</div>"
                f"<div style='font-size:20px;font-weight:700;color:{C['gold2']};margin-top:6px'>{t['opener']}</div>")
    hero = (f"<div class='abs' style='top:0;left:0;width:1080px;height:{hh}px;overflow:hidden'>{sky}</div>{logo}{flg}"
            f"<div class='abs' style='top:{g['head_top_ur' if ur else 'head_top']}px;inset-inline-start:36px;width:760px'>{head}</div>")
    # ---------------- job columns
    cy, ch = hh + g["gap"], g["col_h"]
    cols = "".join(column(job, 30 + i * 520, cy, 500, ch, f, d, f"c{i}{lang}") for i, job in enumerate(t["jobs"]))
    # ---------------- shared strip
    sy = cy + ch + g["gap"]
    items = "".join(
        f"<div style='display:flex;align-items:center;gap:10px;flex:{fl};min-width:0'>"
        f"<div class='ic' style='width:46px;height:46px;background:{C['gold2']}'>{icon(ic, 24, C['navy2'])}</div>"
        f"<div style='min-width:0'>{f.label(lab, 11.5, 14, '#CFE9DA', 'margin-bottom:' + ('4px' if ur else '2px'))}{f.txt(val, 18, 18, '#fff', 'font-weight:800', 1.7 if ur else 1.15)}</div></div>"
        for ic, lab, val, fl in t["shared"])
    strip = (f"<div class='abs' style='top:{sy}px;left:30px;right:30px;height:{g['strip_h']}px;background:{green};border-radius:20px;"
             f"display:flex;align-items:center;gap:14px;padding:0 22px;box-shadow:0 6px 16px {green}55' data-check='strip-{lang}'>{items}</div>"
             f"<div class='abs' style='top:{sy + g['strip_h'] + 8}px;left:30px;right:30px;text-align:center'>"
             f"<div style='display:inline-flex;align-items:center;gap:8px'>{icon('check', 20, green, 3)}{f.txt(t['law'], 18, 19, C['navy2'], 'font-weight:700', 1.7 if ur else 1.2)}</div></div>")
    # ---------------- interviews + CTA
    ct = g["cta_top"]
    cta = f"""<div class='abs' style='top:{ct}px;left:0;width:1080px;height:{1350-ct}px;background:linear-gradient(100deg,#B71C1C,{C['red']})'></div>
<div class='abs' style='top:{ct}px;height:{1350-ct}px;inset-inline-start:30px;width:470px;display:flex;align-items:center;gap:12px'>
 <span class='{'mir' if ur else ''}' style='display:inline-flex'>{icon('megaphone', 44, C['gold2'], 2.2)}</span>
 <div>{f.head(t['interviews'], 40, 32, '#fff', 'line-height:1.5' if ur else '')}{f.txt(t['apply_sub'], 15, 15, '#FFE3E3', 'margin-top:' + ('8px' if ur else '0'), 1.5 if ur else 1.25)}</div></div>
<div class='abs' style='top:{ct+13}px;inset-inline-end:30px;height:{1350-ct-26}px;background:#fff;border-radius:999px;display:flex;align-items:center;gap:14px;
 padding-inline:10px 32px;box-shadow:0 6px 16px #0005'>{whatsapp_icon(62)}
 <div class='num' style='font-size:54px;color:{C['navy2']};line-height:1.15'>{WHATSAPP}</div></div>"""
    return page(f"<div class='{'ur-on' if ur else ''}'>{hero}{cols}{strip}{cta}</div>", css(ur, green), rtl=ur)


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
