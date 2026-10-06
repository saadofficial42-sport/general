"""Style: Scene-led.

A full-width illustrated workplace scene (big windows onto the destination's
landmarks, workers doing the job) with the logo plate and headline set in
the sky; below it a wave-edged info section: job tiles, a big salary card +
2x2 detail tiles, a facilities row, a highlighted note bar, and a red
WhatsApp CTA bar. Mirrors automatically for Urdu.

Usage: python3 src/style_scene.py <data module in src/data/>
"""
import importlib
import sys

from common import C, WHATSAPP, flag, icon, logo_img, page, render, whatsapp_icon, overflow_report
from illustrations import factory_scene
from style_corporate_grid import T


def css(ur):
    base = 'Nastaliq' if ur else 'Archivo'
    return f"""
.canvas{{font-family:'{base}',sans-serif;background:{C['offwhite']};}}
.ur-on .t{{font-family:'Nastaliq',serif;}}
.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px;}}
.ic{{border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none;}}
.mir{{transform:scaleX(-1);}}
.sec{{display:flex;align-items:center;gap:10px;}}
.sec .bar{{width:6px;height:24px;border-radius:3px;}}
"""


def section_title(txt, color, f):
    return (f"<div class='sec' style='margin-bottom:{6 if f.ur else 12}px'><div class='bar' style='background:{color}'></div>"
            f"{f.label(txt, 15, 19, color, 'font-weight:700')}</div>")


def build(d, lang):
    ur = lang == "ur"
    f = T(ur)
    t = d[lang]
    g = d["layout"]
    sh = g["scene_h"]
    # ---------------- scene + headline in the sky
    scene = f"<svg class='abs' style='left:0;top:0' width='1080' height='{sh}'>{factory_scene(1080, sh, ur)}</svg>"
    logo = (f"<div class='abs' style='top:18px;left:{(1080-560)//2}px;width:560px;height:132px;background:#fff;border-radius:22px;"
            f"box-shadow:0 8px 22px rgba(16,33,46,.22);display:flex;align-items:center;justify-content:center'>"
            f"{logo_img('logo-horizontal-light', 'width:510px;height:116px')}</div>")
    flag_el = f"<div class='abs' style='top:22px;inset-inline-start:24px;filter:drop-shadow(0 6px 10px #0005)'>{flag('uzbekistan', 170, True, 'sf' + lang)}</div>"
    posts = (f"<div class='abs' style='top:20px;inset-inline-end:26px;width:150px;height:150px;border-radius:50%;background:{C['red']};"
             f"box-shadow:0 6px 16px {C['red']}66;border:5px solid #fff;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff'>"
             f"{f.label(t['posts_label'], 12, 16, '#FFE7E7', 'text-align:center')}"
             f"<div class='num' style='font-size:58px;line-height:1'>{t['posts_n']}</div>"
             f"{f.label(t['posts_word'], 13, 16, '#fff', 'text-align:center')}</div>")
    if ur:
        head = (f"<div style='display:inline-block;background:{C['red']};color:#fff;border-radius:10px;padding:0 16px 4px'>{f.txt(t['kicker'], 0, 26, '#fff', 'font-weight:700', 1.6)}</div>"
                + f.txt(t['country'], 0, 56, C['navy'], 'font-weight:700;margin-top:52px', 1.4)
                + f.txt(t['subhead'], 0, 26, C['green'], 'font-weight:700', 1.6))
    else:
        head = (f"<div style='display:inline-block;background:{C['red']};color:#fff;border-radius:10px;padding:6px 16px'>"
                f"<span class='mono' style='font-size:18px'>{t['kicker']}</span></div>"
                f"<div class='anton' style='font-size:104px;line-height:1;color:{C['navy']};margin-top:8px;letter-spacing:2px'>{t['country']}</div>"
                f"<div class='anton' style='font-size:40px;line-height:1.05;color:{C['green']}'>{t['subhead']}</div>")
    headline = f"<div class='abs' style='top:{g['head_top_ur' if ur else 'head_top']}px;left:0;right:0;text-align:center'>{head}</div>"
    cities = (f"<div class='abs' style='top:{g['cities_top']}px;left:0;right:0;display:flex;justify-content:center'>"
              f"<div style='display:inline-flex;align-items:center;gap:10px;background:#fff;border-radius:999px;padding:{'0 20px' if ur else '7px 20px'};box-shadow:0 4px 12px #0002'>"
              f"{icon('pin', 22, C['red'], 2.6)}{f.txt(t['cities'], 18, 20, C['navy2'], 'font-weight:700', 1.6 if ur else 1)}"
              f"<span style='color:#B6C2CE'>|</span><div style='line-height:0'>{flag('pakistan', 36, False)}</div>"
              f"<span class='{'mir' if ur else ''}' style='display:inline-flex'>{icon('plane', 24, C['red'], 2.2)}</span>"
              f"<div style='line-height:0'>{flag('uzbekistan', 46, False)}</div></div></div>")
    # ---------------- info section with wave edge
    iy = sh - 40
    wave = (f"<svg class='abs' style='left:0;top:{iy - 30}px' width='1080' height='70'>"
            f"<path d='M0 40 Q270 0 540 30 T1080 20 V70 H0Z' fill='{C['green']}'/>"
            f"<path d='M0 52 Q270 14 540 42 T1080 32 V70 H0Z' fill='{C['offwhite']}'/></svg>")
    info_bg = f"<div class='abs' style='top:{iy + 30}px;left:0;width:1080px;height:{g['cta_top'] - iy - 30}px;background:{C['offwhite']}'></div>"
    # jobs row
    jobs = "".join(
        f"<div style='flex:1;background:#fff;border-radius:16px;box-shadow:0 3px 10px rgba(16,33,46,.1);display:flex;align-items:center;gap:10px;padding:{'4px 12px' if ur else '12px 12px'};min-width:0'>"
        f"<div class='ic' style='width:46px;height:46px;background:{C['green']}'>{icon(ic, 25)}</div>"
        f"{f.txt(txt, 17, 19, C['navy2'], 'font-weight:700;min-width:0', 1.6 if ur else 1.15)}</div>"
        for ic, txt in t["jobs"])
    jy = iy + 46
    jobs_block = (f"<div class='abs' style='top:{jy}px;left:30px;right:30px'>{section_title(t['jobs_title'], C['green'], f)}"
                  f"<div style='display:flex;gap:12px'>{jobs}</div>"
                  f"{f.txt(t['jobs_note'], 15, 16, '#5A6470', 'margin-top:' + ('2px' if ur else '8px'), 1.6 if ur else 1.2)}</div>")
    # salary + detail tiles
    sy = g["details_top"]
    sal = t["salary"]
    tiles = "".join(
        f"<div style='width:calc(50% - 6px);background:#fff;border-radius:14px;box-shadow:0 3px 10px rgba(16,33,46,.1);display:flex;align-items:center;gap:12px;padding:{'2px 14px' if ur else '10px 14px'}'>"
        f"<div class='ic' style='width:42px;height:42px;background:{C['navy']}14'>{icon(ic, 22, C['navy'], 2.2)}</div>"
        f"<div style='min-width:0'>{f.label(lab, 11.5, 15, '#5A6470')}{f.txt(val, 22, 20, C['navy2'], 'font-weight:800', 1.6 if ur else 1.15)}</div></div>"
        for ic, lab, val in t["details"])
    details = f"""<div class='abs' style='top:{sy}px;left:30px;right:30px'>{section_title(t['details_title'], C['navy'], f)}
<div style='display:flex;gap:14px;height:{g['details_h']}px'>
 <div style='width:300px;flex:none;border-radius:18px;background:linear-gradient(140deg,{C['emerald2']},{C['green']});color:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center;
  box-shadow:0 6px 16px {C['green']}55;padding:10px'>
  <div style='display:flex;align-items:center;gap:8px'><div class='ic' style='width:34px;height:34px;background:#ffffff26'>{icon('money', 20)}</div>
  {f.label(sal['label'], 13, 17, C['gold2'])}</div>
  <div class='num' style='font-size:68px;line-height:1'>{sal['value']}</div>
  {f.txt(sal['sub'], 16, 18, '#E6F4EC', '', 1.5 if ur else 1.2)}</div>
 <div style='flex:1;display:flex;flex-wrap:wrap;gap:12px;align-content:space-between'>{tiles}</div></div></div>"""
    # facilities row
    fy = g["fac_top"]
    facs = "".join(
        f"<div style='flex:{fl};display:flex;align-items:center;gap:10px;min-width:0'>"
        f"<div class='ic' style='width:44px;height:44px;background:{C['gold']}'>{icon(ic, 24, C['navy2'])}</div>"
        f"{f.txt(txt, 16, 17, C['navy2'], 'font-weight:700;min-width:0', 1.6 if ur else 1.2)}</div>"
        for ic, txt, fl in t["facilities"])
    fac = (f"<div class='abs' style='top:{fy}px;left:30px;right:30px'>{section_title(t['fac_title'], '#B7791F', f)}"
           f"<div style='display:flex;gap:16px;background:#fff;border-radius:16px;padding:{'4px 18px' if ur else '14px 18px'};box-shadow:0 3px 10px rgba(16,33,46,.1)'>{facs}</div></div>")
    # note bar
    ny = g["note_top"]
    note = (f"<div class='abs' style='top:{ny}px;left:30px;right:30px;display:flex;gap:14px;align-items:stretch'>"
            f"<div style='display:flex;align-items:center;gap:10px;background:{C['gold2']};border-radius:14px;padding:{'6px 18px 8px' if ur else '10px 18px'};box-shadow:0 3px 10px #0002'>"
            f"<span class='{'mir' if ur else ''}' style='display:inline-flex'>{icon('plane', 26, C['navy2'], 2.4)}</span>"
            f"{f.txt(t['note'], 19, 21, C['navy2'], 'font-weight:800;white-space:nowrap', 1.8 if ur else 1.1)}</div>"
            f"<div style='flex:1;display:flex;align-items:center;justify-content:center;border:2px dashed {C['green']};border-radius:14px;padding:{'6px 10px 8px' if ur else '6px 10px'}'>"
            f"{f.txt(t['tagline'], 22, 21, C['green'], 'font-weight:700;text-align:center', 1.8 if ur else 1.1, 't' if ur else 'script')}</div></div>")
    # CTA
    ct = g["cta_top"]
    cta = f"""<div class='abs' style='top:{ct}px;left:0;width:1080px;height:{1350-ct}px;background:linear-gradient(100deg,#B71C1C,{C['red']})'></div>
<div class='abs' style='top:{ct}px;height:{1350-ct}px;inset-inline-start:36px;width:440px;display:flex;flex-direction:column;justify-content:center'>
 {f.head(t['apply'], 44, 34, '#fff')}
 {f.txt(t['apply_sub'], 15, 16.5, '#FFE3E3', 'margin-top:' + ('8px' if ur else '4px'), 1.5 if ur else 1.3)}</div>
<div class='abs' style='top:{ct+13}px;inset-inline-end:30px;height:{1350-ct-26}px;background:#fff;border-radius:999px;display:flex;align-items:center;gap:14px;
 padding-inline:10px 32px;box-shadow:0 6px 16px #0005'>{whatsapp_icon(62)}
 <div class='num' style='font-size:54px;color:{C['navy2']};line-height:1.15'>{WHATSAPP}</div></div>"""
    body = scene + logo + flag_el + posts + headline + cities + info_bg + wave + jobs_block + details + fac + note + cta
    return page(f"<div class='{'ur-on' if ur else ''}'>{body}</div>", css(ur), rtl=ur)


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
