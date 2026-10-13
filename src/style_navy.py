"""Style: Navy hard-hat.

Navy + gold theme. Navy header with white logo plate and script tagline; hero with a
LARGE real photo in a gold-framed panel, gold "apply today" sticker, big two-tone
headline, ribbon line and waving flag; jobs as a 3x2 card grid (6th card = salary
highlight); 3x3 facilities chips; documents / CV bars; CTA with both WhatsApp
numbers (order from data), email, address and a trust strip. Mirrors for Urdu.

Usage: python3 src/style_navy.py <data module in src/data/>
"""
import importlib
import sys

from common import C, PHOTOS, flag, icon, logo_img, page, render, whatsapp_icon, overflow_report
from style_corporate_grid import T

NAVY, NAVY2, GOLD, AMBER = "#0B1A33", "#12284D", "#F0B443", "#FFC93C"


def css(ur):
    base = 'Nastaliq' if ur else 'Archivo'
    return f"""
.canvas{{font-family:'{base}',sans-serif;background:{NAVY};}}
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
    # ---------------- header
    hh = g["header_h"]
    header = (f"<div class='abs' style='top:0;left:0;width:1080px;height:{hh}px;background:{NAVY}'></div>"
              f"<div class='abs' style='top:14px;inset-inline-start:30px;background:#fff;border-radius:18px;padding:6px 18px;box-shadow:0 6px 16px #0007'>"
              f"{logo_img('logo-horizontal-light', 'width:430px;height:{0}px'.format(hh - 40))}</div>"
              f"<div class='abs' style='top:0;height:{hh}px;inset-inline-end:34px;display:flex;flex-direction:column;justify-content:center;align-items:flex-end'>"
              f"<div class='script' style='font-size:44px;color:{GOLD};line-height:1;direction:ltr'>{d['tagline']}</div>"
              f"<div class='mono' style='font-size:14px;color:#C9D4E6;letter-spacing:3px;margin-top:8px;direction:ltr'>{d['trust_en']}</div></div>")
    # ---------------- hero
    hy, H = hh, g["hero_h"]
    pw, ph = g["photo_w"], H - 30
    p = PHOTOS / f"{d['photo']}.png"
    photo = (f"<div class='abs' style='top:6px;inset-inline-start:30px;width:{pw}px;height:{ph}px;border-radius:26px;overflow:hidden;"
             f"border:6px solid {GOLD};box-shadow:0 14px 30px #000A'>"
             f"<img src='{p.as_uri()}' style='width:100%;height:100%;object-fit:cover;object-position:center 75%;display:block'></div>")
    sticker = (f"<div class='abs' style='top:{ph - 150}px;inset-inline-start:{pw - 80}px;width:170px;height:170px;border-radius:50%;"
               f"background:radial-gradient(circle at 35% 30%,#FFE08A,{GOLD} 60%,#C98B16);box-shadow:0 8px 20px #0009;"
               f"display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate({8 if ur else -8}deg);border:4px dashed {NAVY}'>"
               + "".join(f.txt(s, 22, 20, NAVY, 'font-weight:800;text-align:center', 1.75 if ur else 1.05, 't' if ur else 'anton') for s in t["sticker"])
               + "</div>")
    tx = 30 + pw + 110
    flg = f"<div class='abs' style='top:-4px;inset-inline-start:{pw - 70}px;filter:drop-shadow(0 4px 8px #0008)'>{flag(d['country'], 120, True, 'hf' + lang)}</div>"
    if ur:
        head = (f.txt(t["title_a"], 0, 78, '#fff', 'font-weight:700', 1.45)
                + f.txt(t["title_b"], 0, 62, GOLD, 'font-weight:700;margin-top:-10px', 1.6))
    else:
        head = (f"<div class='anton' style='font-size:92px;line-height:1;color:#fff;white-space:nowrap'>{t['title_a']}</div>"
                f"<div class='anton' style='font-size:78px;line-height:1.05;color:{GOLD}'>{t['title_b']}</div>")
    text = (f"<div class='abs' style='top:{g['head_top_ur' if ur else 'head_top']}px;inset-inline-start:{tx}px;inset-inline-end:30px'>"
            f"{head}"
            f"<div style='display:flex;align-items:center;gap:10px;margin-top:{30 if ur else 14}px'>"
            f"<div style='width:44px;height:4px;background:{GOLD};border-radius:2px'></div>{f.txt(t['field'], 28, 27, '#fff', 'font-weight:800', 1.7 if ur else 1.15)}</div>"
            f"<div style='margin-top:{8 if ur else 16}px;background:{C['red']};border-radius:12px;padding:{'2px 16px 8px' if ur else '10px 16px'};box-shadow:0 6px 14px #0007'>"
            f"{f.txt(t['ribbon'], 22, 22, '#fff', 'font-weight:700', 1.7 if ur else 1.25)}</div></div>")
    deco = (f"<svg class='abs' style='left:0;top:0' width='1080' height='{H}'><path d='M{1080 if not ur else 0} 0 L{760 if not ur else 320} {H} L{720 if not ur else 360} {H} L{1040 if not ur else 40} 0Z' fill='{GOLD}' opacity='.08'/>"
            f"<circle cx='{900 if not ur else 180}' cy='{H - 40}' r='220' fill='#ffffff08'/></svg>")
    hero = (f"<div class='abs' style='top:{hy}px;left:0;width:1080px;height:{H}px;background:linear-gradient(180deg,{NAVY},{NAVY2})'>"
            f"{deco}{photo}{flg}{sticker}{text}</div>")
    # ---------------- job cards
    jy = hy + H + g["gap"]
    ch = g["card_h"]
    cards = "".join(
        f"<div style='position:relative;width:calc(33.333% - 8px);height:{ch}px;background:#fff;border-radius:18px;box-shadow:0 6px 16px #0006;"
        f"padding:{'8px 16px' if ur else '14px 16px'};display:flex;flex-direction:column;justify-content:space-between;border-top:6px solid {GOLD}'>"
        f"<div style='display:flex;align-items:center;gap:12px'><div class='ic' style='width:54px;height:54px;background:{NAVY2}'>{icon(ic, 30, GOLD, 2.2)}</div>"
        f"<div style='min-width:0'>{f.txt(nm, 22, 23, NAVY, 'font-weight:800', 1.45 if ur else 1.08)}"
        f"<div style='font-family:Archivo;font-size:15px;font-weight:700;color:#5A6B85;direction:ltr;text-align:{"right" if ur else "left"};margin-top:{6 if ur else 0}px'>{sub}</div></div></div>"
        f"<div style='display:flex;align-items:center;justify-content:space-between'>"
        f"<div style='direction:ltr'><span class='num' style='font-size:34px;color:{NAVY};line-height:1'>1200 + 300</span>"
        f"<span class='num' style='font-size:20px;color:#B07A10;margin-left:6px'>SAR</span></div>"
        f"<div style='background:{NAVY};border-radius:12px;padding:{'0 12px 4px' if ur else '4px 12px'};display:flex;align-items:center;gap:6px'>"
        f"<span class='num' style='font-size:28px;color:{GOLD};line-height:1.1'>{n}</span>{f.txt(t['posts'], 13, 15, '#fff', 'font-weight:700', 1.5 if ur else 1)}</div></div></div>"
        for ic, nm, sub, n in t["jobs"])
    best = (f"<div style='width:calc(33.333% - 8px);height:{ch}px;border-radius:18px;background:linear-gradient(135deg,#FFE08A,{GOLD} 55%,#D99A1E);"
            f"box-shadow:0 6px 16px #0006;display:flex;align-items:center;gap:14px;padding:0 18px'>"
            f"<div class='ic' style='width:64px;height:64px;background:{NAVY}'>{icon('money', 36, GOLD, 2.2)}</div>"
            f"<div>{f.head(t['best'][0], 30, 26, NAVY)}{f.txt(t['best'][1], 19, 20, NAVY, 'font-weight:800', 1.6 if ur else 1.2)}</div></div>")
    jobs = f"<div class='abs' style='top:{jy}px;left:30px;right:30px;display:flex;flex-wrap:wrap;gap:12px' data-check='jobs-{lang}'>{cards}{best}</div>"
    # ---------------- facilities
    fy = jy + 2 * ch + 12 + g["gap"]
    fh = g["fac_h"]
    chips = "".join(
        f"<div style='width:calc(33.333% - 7px);height:{fh}px;background:{NAVY2};border:1.5px solid #ffffff22;border-radius:14px;"
        f"display:flex;align-items:center;gap:10px;padding:0 12px'>"
        f"<div class='ic {'mir' if ur and ic == 'plane' else ''}' style='width:42px;height:42px;background:{GOLD}'>{icon(ic, 23, NAVY, 2.3)}</div>"
        f"{f.txt(s, 19, 19, '#fff', 'font-weight:700', 1.55 if ur else 1.12)}</div>"
        for ic, s in t["facilities"])
    fac = (f"<div class='abs' style='top:{fy}px;left:30px;right:30px' data-check='fac-{lang}'>"
           f"<div style='display:flex;align-items:center;gap:12px;margin-bottom:{8 if ur else 10}px;margin-top:{0 if ur else 0}px'>"
           f"<div style='width:8px;height:28px;background:{GOLD};border-radius:4px'></div>{f.head(t['fac_title'], 30, 24, GOLD, 'line-height:1.6' if ur else '')}</div>"
           f"<div style='display:flex;flex-wrap:wrap;gap:10px'>{chips}</div></div>")
    # ---------------- bars
    by = fy + g["fac_block_h"] + g["gap"]
    bars = (f"<div class='abs' style='top:{by}px;left:30px;right:30px;height:{g['bar_h']}px;display:flex;gap:12px' data-check='bars-{lang}'>"
            f"<div style='flex:1.2;background:#fff;border-radius:14px;display:flex;align-items:center;gap:12px;padding:0 16px'>"
            f"{icon('doc', 32, NAVY, 2.2)}{f.txt(t['docs'], 22, 21, NAVY, 'font-weight:800', 1.6 if ur else 1.1)}</div>"
            f"<div style='flex:1;background:{C['red']};border-radius:14px;display:flex;align-items:center;justify-content:center;gap:12px;padding:0 16px'>"
            f"{icon('check', 32, '#fff', 3)}{f.head(t['cv'], 32, 27, '#fff')}</div></div>")
    # ---------------- CTA
    ct = g["cta_top"]
    nums = "".join(f"<div class='num' style='display:block;font-size:42px;color:{NAVY};line-height:1.08'>{n}</div>" for n in d["phones"])
    cta = (f"<div class='abs' style='top:{ct}px;left:0;width:1080px;height:{1350 - ct}px;background:linear-gradient(100deg,#06101F,{NAVY2});border-top:5px solid {GOLD}'></div>"
           f"<div class='abs' style='top:{ct + 12}px;inset-inline-start:30px;width:560px'>"
           f"{f.head(t['apply'], 40, 32, GOLD, 'line-height:1.35' if ur else '')}"
           f"<div style='display:flex;align-items:center;gap:8px;margin-top:{4 if ur else 8}px'>{icon('mail', 24, GOLD, 2)}"
           f"<span style='font-family:Archivo;font-size:23px;font-weight:700;color:#fff;direction:ltr;unicode-bidi:isolate'>{d['email']}</span></div>"
           f"<div style='display:flex;align-items:flex-start;gap:8px;margin-top:8px'>{icon('pin', 24, GOLD, 2)}"
           f"<span style='font-family:Archivo;font-size:17px;font-weight:600;color:#DCE4F2;line-height:1.3;direction:ltr;unicode-bidi:isolate'>{d['address']}</span></div></div>"
           f"<div class='abs' style='top:{ct + 16}px;inset-inline-end:30px;height:118px;background:#fff;border-radius:24px;display:flex;align-items:center;gap:14px;"
           f"padding-inline:14px 26px;box-shadow:0 6px 16px #0007'>{whatsapp_icon(68)}<div>{nums}</div></div>"
           f"<div class='abs' style='top:{ct + 146}px;left:0;width:1080px;height:{1350 - ct - 146}px;background:{GOLD};display:flex;align-items:center;justify-content:center;gap:16px'>"
           + "<span style='color:#0B1A33;font-weight:900'>|</span>".join(f.txt(s, 18, 19, NAVY, 'font-weight:800;letter-spacing:' + ('0' if ur else '2px'), 1.5 if ur else 1) for s in t["trust"])
           + "</div>")
    return page(f"<div class='{'ur-on' if ur else ''}'>{header}{hero}{jobs}{fac}{bars}{cta}</div>", css(ur), rtl=ur)


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
