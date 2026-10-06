"""Style: Silk Road / cultural.

Deep-green girih-tile background, white logo plate, a pointed-arch (iwan)
hero with Registan domes and a gold "posts" seal, one arch-topped card per
job, two detail panels, and a gold WhatsApp CTA bar.
Mirrors automatically for Urdu.

Usage: python3 src/style_silk_road.py <data module in src/data/>
"""
import importlib
import sys

from common import C, WHATSAPP, flag, icon, logo_img, page, render, whatsapp_icon, overflow_report
from illustrations import girih_pattern, photo_or_art, registan, skyline, tashkent_tv_tower
from style_corporate_grid import T

GOLD_GRAD = f"linear-gradient(180deg,{C['gold2']},{C['gold']})"


def arch_path(w, h, s=None):
    """CSS clip-path path() for a pointed (iwan) arch of w x h px."""
    s = s or w * 0.42
    return (f'path("M0 {h} L0 {s:.0f} Q0 {s*0.32:.0f} {w/2:.0f} 0 '
            f'Q{w} {s*0.32:.0f} {w} {s:.0f} L{w} {h} Z")')


def css(ur):
    base = 'Nastaliq' if ur else 'Archivo'
    return f"""
.canvas{{font-family:'{base}',sans-serif;background:{C['green']};}}
.ur-on .t{{font-family:'Nastaliq',serif;}}
.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px;}}
.ic{{border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none;}}
.mir{{transform:scaleX(-1);}}
"""


def seal(n, word, f, d=120, uid="s"):
    """Gold rosette seal with a number."""
    import math
    pts = " ".join(
        f"{d/2 + (d/2 if i % 2 == 0 else d/2*0.86) * math.cos(math.radians(i*7.5)):.1f},"
        f"{d/2 + (d/2 if i % 2 == 0 else d/2*0.86) * math.sin(math.radians(i*7.5)):.1f}" for i in range(48))
    return f"""<div style='position:relative;width:{d}px;height:{d}px;filter:drop-shadow(0 4px 8px #0006)'>
<svg width='{d}' height='{d}' class='abs' style='left:0;top:0'><defs><linearGradient id='{uid}' x1='0' y1='0' x2='0' y2='1'>
<stop offset='0' stop-color='{C['gold2']}'/><stop offset='1' stop-color='#D99A22'/></linearGradient></defs>
<polygon points='{pts}' fill='url(#{uid})'/><circle cx='{d/2}' cy='{d/2}' r='{d*0.36}' fill='none' stroke='#fff' stroke-width='2' stroke-dasharray='3 3' opacity='.8'/></svg>
<div class='abs' style='inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;color:{C['navy2']}'>
<div class='num' style='font-size:{d*0.34:.0f}px;line-height:1'>{n}</div>
{f.label(word, d*0.095, d*0.13, C['navy2'], 'text-align:center;line-height:' + ('1.4' if f.ur else '1.2'))}</div></div>"""


def job_card(job, x, y, w, h, f, uid):
    col = job["color"]
    pic_h = job.get("pic_h", 150)
    rows = "".join(
        f"<div style='display:flex;align-items:center;gap:9px;padding:{'1px 0' if f.ur else '6px 0'};border-top:1px solid #E8E2D2'>"
        f"<div class='ic' style='width:30px;height:30px;background:{col}1F'>{icon(ic, 17, col, 2.4)}</div>"
        f"{f.txt(txt, 15.5, 16, C['navy2'], 'flex:1;min-width:0', 1.7 if f.ur else 1.22)}</div>"
        for ic, txt in job["rows"])
    sal = job["salary"]
    sub = f.txt(sal["sub"], 14, 15, "#5A6470", "text-align:center", 1.55 if f.ur else 1.2)
    return f"""<div class='abs' style='inset-inline-start:{x}px;top:{y}px;width:{w}px;height:{h}px' data-check='{uid}'>
<div class='abs' style='inset:0;background:#FBF8F0;clip-path:{arch_path(w, h)};'></div>
<div class='abs' style='top:4px;inset-inline-start:4px;width:{w-8}px;height:{h-8}px;clip-path:{arch_path(w-8, h-8)};border:0;
     background:linear-gradient(#FBF8F0,#FBF8F0) padding-box;'></div>
<div class='abs' style='top:14px;inset-inline-start:{(w-210)//2}px;width:210px;height:{pic_h}px;clip-path:{arch_path(210, pic_h)};
     box-shadow:0 0 0 4px {C['gold']}'>{photo_or_art(job['art'], uid + 'a')}</div>
<svg class='abs' style='top:10px;inset-inline-start:{(w-218)//2}px' width='218' height='{pic_h+8}'>
  <path d='M4 {pic_h+4} L4 {218*0.42+4:.0f} Q4 {218*0.42*0.32+4:.0f} 109 4 Q214 {218*0.42*0.32+4:.0f} 214 {218*0.42+4:.0f} L214 {pic_h+4}'
   fill='none' stroke='{C['gold']}' stroke-width='5'/></svg>
<div class='abs' style='top:{pic_h - 84}px;inset-inline-end:2px'>{seal(job['posts'][0], job['posts'][1], f, 92, uid + 's')}</div>
<div class='abs' style='top:{pic_h + 18}px;inset-inline-start:16px;inset-inline-end:16px;text-align:center'>
  {f.head(job['title'], job.get('title_en_px', 28), job.get('title_ur_px', 25), col, 'text-align:center')}
  {f.txt(job['roles'], 14.5, 15, '#5A6470', 'text-align:center', 1.75 if f.ur else 1.2) if job.get('roles') else ''}
  <div style='display:flex;align-items:center;justify-content:center;gap:5px;margin-top:{0 if f.ur else 4}px'>{icon('pin', 15, C['red'], 2.6)}
   {f.txt(job['location'], 14.5, 15.5, C['navy'], 'font-weight:700', 1.55 if f.ur else 1.2)}</div>
  <div style='margin:{6 if f.ur else 10}px auto 0;background:{col};border-radius:14px;padding:{'4px 8px 6px' if f.ur else '8px 8px'};color:#fff'>
    {f.label(sal['label'], 12, 15, C['gold2'], 'text-align:center')}
    <div class='num' style='font-size:{sal.get('size', 40)}px;line-height:1.05;margin-top:{(14 if sal.get('rtl') else 4) if f.ur else 0}px;{'direction:rtl' if sal.get('rtl') else ''}'>{sal['value']}</div>
    {sub.replace('#5A6470', '#E9F2EE')}</div>
  <div style='margin-top:8px;text-align:start'>{rows}</div>
</div></div>"""


def panel(title, items, x, y, w, h, f, uid, check_icon="check", accent=None):
    accent = accent or C["emerald2"]
    lis = "".join(
        f"<div style='display:flex;align-items:center;gap:9px'>"
        f"<div class='ic' style='width:24px;height:24px;background:{accent}'>{icon(ic or check_icon, 14, '#fff', 3)}</div>"
        f"{f.txt(txt, 16, 16, C['navy2'], 'min-width:0', 1.8 if f.ur else 1.25)}</div>"
        for ic, txt in items)
    return f"""<div class='abs' style='inset-inline-start:{x}px;top:{y}px;width:{w}px;height:{h}px;background:#FBF8F0;border-radius:18px;
 border:3px solid {C['gold']};padding:{'6px 18px' if f.ur else '14px 18px'};display:flex;flex-direction:column;gap:{0 if f.ur else 7}px' data-check='{uid}'>
 <div style='display:flex;align-items:center;gap:8px;margin-bottom:{0 if f.ur else 4}px'>
  <div style='width:10px;height:10px;transform:rotate(45deg);background:{C['gold']}'></div>
  {f.label(title, 13.5, 18, C['green'], 'font-weight:700')}</div>{lis}</div>"""


def build(d, lang):
    ur = lang == "ur"
    f = T(ur)
    t = d[lang]
    g = d["layout"]
    bg = (f"<svg class='abs' style='left:0;top:0' width='1080' height='1350'><defs>{girih_pattern('gp', C['gold'], .16, 90)}"
          f"<radialGradient id='bgg' cx='.5' cy='.3' r='.8'><stop offset='0' stop-color='#13603F'/><stop offset='1' stop-color='#072A1E'/></radialGradient></defs>"
          f"<rect width='1080' height='1350' fill='url(#bgg)'/><rect width='1080' height='1350' fill='url(#gp)'/></svg>")
    # ---------------- logo plate
    logo = f"""<div class='abs' style='top:20px;left:{(1080-600)//2}px;width:600px;height:146px;background:#fff;border-radius:24px;
 box-shadow:0 8px 24px #0005;border:3px solid {C['gold']};display:flex;align-items:center;justify-content:center'>
 {logo_img('logo-horizontal-light', 'width:540px;height:126px')}</div>"""
    # ---------------- arch hero
    ax, ay, aw, ah = 150, 182, 780, g["hero_h"]
    skyl = (f"<svg class='abs' style='left:0;bottom:0' width='{aw}' height='{ah}' viewBox='0 0 {aw} {ah}'>"
            f"<g transform='translate(0 {ah-60})' opacity='.55'>{skyline(aw, 60, '#1C3F78', 5)}</g>"
            f"{registan(aw*0.5-170, ah, 340, '#24508F')}{tashkent_tv_tower(aw*0.9 if not ur else aw*0.1, ah, ah*0.8, '#24508F')}</svg>")
    if ur:
        head = (f.txt(t['kicker'], 0, 22, C['gold2'], 'text-align:center;margin-bottom:30px', 1.5) +
                f.txt(t['country'], 0, 58, '#fff', 'text-align:center;font-weight:700', 1.6) +
                f.txt(t['cities'], 0, 22, C['gold2'], 'text-align:center;margin-top:-6px', 1.5))
    else:
        head = (f.label(t['kicker'], 18, 0, C['gold2'], 'text-align:center') +
                f"<div class='anton' style='font-size:100px;line-height:1;color:#fff;text-align:center;margin-top:8px;letter-spacing:2px'>{t['country']}</div>"
                f"<div class='script' style='font-size:40px;line-height:1.1;color:{C['gold2']};text-align:center'>{t['cities']}</div>")
    dash = f"<div style='width:34px;border-top:3px dashed {C['gold']}'></div>"
    plane = f"<span class='{'mir' if ur else ''}' style='display:inline-flex'>{icon('plane', 28, C['gold2'], 2)}</span>"
    route = (f"<div style='display:flex;justify-content:center;margin-top:{4 if ur else 10}px'><div style='display:inline-flex;align-items:center;gap:9px;background:#0007;border-radius:999px;padding:{'0 16px' if ur else '6px 16px'}'>"
             f"<div style='line-height:0'>{flag('pakistan', 40, False)}</div>{f.txt(t['from'], 15, 17, '#fff', 'font-weight:700', 1.5 if ur else 1)}"
             f"{dash}{plane}{dash}<div style='line-height:0'>{flag('uzbekistan', 52, False)}</div>{f.txt(t['to'], 15, 17, '#fff', 'font-weight:700', 1.5 if ur else 1)}</div></div>")
    hero = f"""<div class='abs' style='left:{ax-8}px;top:{ay-8}px;width:{aw+16}px;height:{ah+8}px;background:{GOLD_GRAD};clip-path:{arch_path(aw+16, ah+8, 300)}'></div>
<div class='abs' style='left:{ax}px;top:{ay}px;width:{aw}px;height:{ah}px;clip-path:{arch_path(aw, ah, 292)};
 background:linear-gradient(180deg,{C['navy']},{C['navy2']});overflow:hidden'>{skyl}
 <div class='abs' style='left:60px;right:60px;top:{g['head_top_ur' if ur else 'head_top']}px'>{head}{route}</div></div>
<div class='abs' style='top:{ay+30}px;inset-inline-start:22px;filter:drop-shadow(0 6px 10px #0007)'>{flag('uzbekistan', 150, True, 'hf' + lang)}</div>
<div class='abs' style='top:{ay+30}px;inset-inline-end:22px'>{seal(t['stat_n'], t['stat_label'], f, 132, 'hs' + lang)}</div>
<div class='abs' style='top:{ay+ah-58}px;inset-inline-start:14px;width:140px;text-align:center'>
 <div style='display:inline-block;background:{C['red']};color:#fff;border-radius:10px;padding:{'0 12px' if ur else '6px 12px'};transform:rotate({4 if ur else -4}deg);box-shadow:0 4px 10px #0005'>
 {f.head(t['urgent'], 26, 24, '#fff')}</div></div>"""
    # ---------------- job cards
    cy, ch, cw, gap = g["cards_top"], g["cards_h"], 326, 18
    cards = "".join(job_card(job, 33 + i * (cw + gap), cy, cw, ch, f, f"c{i}{lang}") for i, job in enumerate(t["jobs"]))
    # ---------------- panels
    py, ph = g["panels_top"], g["panels_h"]
    panels = (panel(t["p1_title"], t["p1"], 33, py, 497, ph, f, "p1" + lang) +
              panel(t["p2_title"], t["p2"], 550, py, 497, ph, f, "p2" + lang, accent=C["green"]))
    # ---------------- CTA
    ct = g["cta_top"]
    cta = f"""<div class='abs' style='top:{ct}px;left:0;width:1080px;height:{1350-ct}px;background:{GOLD_GRAD}'></div>
<div class='abs' style='top:{ct}px;height:{1350-ct}px;inset-inline-start:36px;width:470px;display:flex;flex-direction:column;justify-content:center'>
 {f.head(t['tagline'], 30, 26, C['green'])}
 {f.txt(t['note'], 15, 16, C['navy2'], 'font-weight:600', 1.5 if ur else 1.3)}</div>
<div class='abs' style='top:{ct+12}px;inset-inline-end:30px;height:{1350-ct-24}px;background:{C['green']};border-radius:999px;display:flex;align-items:center;gap:14px;
 padding-inline:10px 32px;box-shadow:0 6px 16px #0004'>{whatsapp_icon(62, C['wa'])}
 <div class='num' style='font-size:52px;color:#fff;line-height:1.15'>{WHATSAPP}</div></div>"""
    return page(f"<div class='{'ur-on' if ur else ''}'>{bg}{logo}{hero}{cards}{panels}{cta}</div>", css(ur), rtl=ur)


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
