"""Style: Corporate navy/gold grid.

White logo header, navy skyline hero with a Pakistan -> destination route
and posts stat, one wide "group" card (two related jobs side by side +
requirements + shared facts strip), two tall job cards (stat tiles, fact
rows, optional numbered documents grid), and a WhatsApp CTA bar.
Mirrors automatically for Urdu (logical CSS properties).

Usage: python3 src/style_corporate_grid.py <data module in src/data/>
"""
import importlib
import sys

from common import C, WHATSAPP, flag, icon, logo_img, page, render, whatsapp_icon, overflow_report
from illustrations import photo_or_art, registan, skyline, tashkent_tv_tower


def css(ur):
    base = 'Nastaliq' if ur else 'Archivo'
    return f"""
body{{background:{C['offwhite']};}}
.canvas{{background:{C['offwhite']};font-family:'{base}',sans-serif;}}
.ur-on .t{{font-family:'Nastaliq',serif;}}
.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px;}}
.card{{position:absolute;background:#fff;border-radius:22px;box-shadow:0 6px 22px rgba(13,45,99,.13);overflow:hidden;}}
.pic{{border-radius:50%;overflow:hidden;border:4px solid #fff;box-shadow:0 3px 10px rgba(0,0,0,.2);flex:none;}}
.ribbon{{position:absolute;top:0;inset-inline-end:22px;background:{C['red']};color:#fff;padding:6px 14px 12px;
        clip-path:polygon(0 0,100% 0,100% 100%,50% 84%,0 100%);text-align:center;}}
.tile{{position:relative;border-radius:14px;padding:16px 14px 8px;display:flex;align-items:center;gap:12px;min-width:0;}}
.tile .lab{{position:absolute;top:-11px;inset-inline-start:14px;color:#fff;border-radius:999px;padding:0 10px;white-space:nowrap;}}
.ic{{border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none;}}
.row{{display:flex;align-items:center;gap:10px;border-top:1px dashed #D6DEE8;}}
.mir{{transform:scaleX(-1);}}
"""


class T:
    """Per-language typography helper."""
    def __init__(self, ur):
        self.ur = ur

    def txt(self, s, en_px, ur_px, color, extra="", lh=None, cls="t"):
        lh = lh or (1.75 if self.ur else 1.25)
        px = ur_px if self.ur else en_px
        return f"<div class='{cls}' style='font-size:{px}px;color:{color};line-height:{lh};{extra}'>{s}</div>"

    def label(self, s, en_px, ur_px, color, extra=""):
        """Spaced mono label in EN; plain Nastaliq in UR."""
        if self.ur:
            return self.txt(s, 0, ur_px, color, extra, 1.6)
        return f"<div class='mono' style='font-size:{en_px}px;color:{color};line-height:1.2;{extra}'>{s}</div>"

    def head(self, s, en_px, ur_px, color, extra=""):
        """Anton headline in EN; bold Nastaliq in UR."""
        if self.ur:
            return self.txt(s, 0, ur_px, color, "font-weight:700;" + extra, 1.7)
        return f"<div class='anton' style='font-size:{en_px}px;color:{color};line-height:1.05;text-transform:uppercase;{extra}'>{s}</div>"


def tile(tl, color, f, height):
    ur = f.ur
    lab = (f"<div class='lab {'t' if ur else 'mono'}' style='background:{color};font-size:{15 if ur else 12}px;"
           f"line-height:{1.55 if ur else 22}{'' if ur else 'px'};{'' if ur else 'letter-spacing:2px'}'>{tl['label']}</div>")
    val = f"<div class='num' style='font-size:{tl.get('size', 40)}px;color:{C['navy2']};line-height:1.05'>{tl['value']}</div>"
    sub = f.txt(tl["sub"], 15, 16, "#4A5868", "", 1.5 if ur else 1.2) if tl.get("sub") else ""
    inline = tl.get("inline_sub", False)
    body = (f"<div style='display:flex;align-items:center;gap:10px;min-width:0'>{val}<div style='min-width:0'>{sub}</div></div>"
            if inline else f"<div style='min-width:0'>{val}{sub}</div>")
    return (f"<div class='tile' style='background:{color}14;flex:{tl.get('flex', 1)};height:{height}px'>{lab}"
            f"<div class='ic' style='width:46px;height:46px;background:{color}'>{icon(tl['icon'], 26)}</div>{body}</div>")


def row(ic, color, html, f, pad=None, px=(18, 19)):
    pad = pad if pad is not None else (2 if f.ur else 8)
    return (f"<div class='row' style='padding:{pad}px 0'><div class='ic' style='width:32px;height:32px;background:{color}1F'>{icon(ic, 19, color, 2.4)}</div>"
            f"{f.txt(html, px[0], px[1], C['navy2'], 'flex:1;min-width:0')}</div>")


def ribbon(posts, f):
    n, word = posts
    return (f"<div class='ribbon'><div class='num' style='font-size:34px;line-height:1'>{n}</div>"
            f"<div class='{'t' if f.ur else 'mono'}' style='font-size:{16 if f.ur else 12}px;line-height:1.3;{'' if f.ur else 'letter-spacing:2px'}'>{word}</div></div>")


def head_block(job, f, pic, ribbon_space=110):
    col = job["color"]
    pin = icon("pin", 18, C["red"], 2.6)
    roles = f.txt(job["roles"], 16, 17, "#4A5868", "", 1.6 if f.ur else None) if job.get("roles") else ""
    loc = (f"<div style='display:flex;align-items:center;gap:6px'>{pin}"
           f"{f.txt(job['location'], 16, 18, C['navy'], 'font-weight:700', 1.6 if f.ur else None)}</div>") if job.get("location") else ""
    return (f"<div style='display:flex;align-items:center;gap:16px'>"
            f"<div class='pic' style='width:{pic}px;height:{pic}px'>{photo_or_art(job['art'], job['art'] + str(pic) + ('u' if f.ur else 'e'))}</div>"
            f"<div style='min-width:0'>"
            f"{f.head(job['title'], job.get('title_en_px', 32), job.get('title_ur_px', 28), col, 'padding-inline-end:' + str(ribbon_space if job.get('posts') else 0) + 'px')}{roles}{loc}</div></div>")


# ------------------------------------------------------------------ blocks

def group_card(gc, box, f, uid):
    """Wide card: shared location header, N job columns, requirements, shared facts strip."""
    x, y, w, h = box
    ur = f.ur
    cols = ""
    for job in gc["jobs"]:
        col = job["color"]
        posts = (f"<div style='display:inline-flex;align-items:center;gap:6px;background:{C['red']};color:#fff;border-radius:8px;padding:{'0 10px' if ur else '3px 10px'};margin-top:4px'>"
                 f"<span class='num' style='font-size:22px;line-height:1.2'>{job['posts'][0]}</span>"
                 f"<span class='{'t' if ur else 'mono'}' style='font-size:{15 if ur else 12}px;line-height:1.5;{'' if ur else 'letter-spacing:2px'}'>{job['posts'][1]}</span></div>")
        cols += f"""<div style='width:{job['col_w']}px;flex:none;display:flex;flex-direction:column;gap:{gc.get('col_gap', 18)}px'>
<div style='display:flex;align-items:center;gap:14px'>
  <div class='pic' style='width:86px;height:86px'>{photo_or_art(job['art'], job['art'] + 'g' + ('u' if ur else 'e'))}</div>
  <div style='min-width:0'>{f.head(job['title'], job.get('title_en_px', 28), job.get('title_ur_px', 24), col)}{posts}</div></div>
{tile(job['salary'], col, f, gc['tile_h'])}</div>"""
    req = "".join(
        f"<div style='display:flex;align-items:{'center' if ur else 'flex-start'};gap:8px'>"
        f"<div class='ic' style='width:22px;height:22px;background:{C['emerald2']};margin-top:{0 if ur else 1}px'>{icon('check', 14, '#fff', 3.4)}</div>"
        f"{f.txt(r, 15, 15, C['navy2'], '', 1.74 if ur else 1.2)}</div>"
        for r in gc["requirements"])
    reqbox = (f"<div style='flex:1;min-width:0;background:#F1F7F3;border-radius:16px;padding:{'8px 16px' if ur else '14px 16px'};"
              f"display:flex;flex-direction:column;gap:{0 if ur else 3}px' data-check='req-{uid}'>"
              f"{f.label(gc['req_title'], 13, 17, C['emerald2'], 'margin-bottom:' + ('0' if ur else '4px'))}{req}</div>")
    chips = "".join(
        f"<div style='display:flex;align-items:center;gap:8px;flex:{c.get('flex', 1)};min-width:0'>"
        f"<div class='ic' style='width:38px;height:38px;background:{C['gold']}'>{icon(c['icon'], 22, C['navy2'])}</div>"
        f"{f.txt(c['text'], 16, 17, '#fff', 'min-width:0', 1.6 if ur else 1.2)}</div>"
        for c in gc["shared"])
    pin = icon("pin", 26, C["red"], 2.6)
    return f"""<div class='card' style='inset-inline-start:{x}px;top:{y}px;width:{w}px;height:{h}px' data-check='{uid}'>
<div style='display:flex;align-items:center;gap:10px;padding:{'4px 26px' if ur else '14px 26px 10px'};border-bottom:1px solid #E3E9F0'>
  {pin}{f.head(gc['place'], 30, 26, C['navy'])}
  <div style='width:2px;height:26px;background:#CFD8E3;margin:0 6px'></div>
  {f.txt(gc['tagline'], 17, 18, '#4A5868', 'flex:1')}
  <div style='line-height:0;box-shadow:0 1px 4px #0004'>{flag(gc['flag'], 54, False)}</div></div>
<div style='display:flex;gap:22px;padding:{'10px 22px 0' if ur else '16px 22px 0'};height:{gc['body_h']}px'>{cols}{reqbox}</div>
<div style='position:absolute;bottom:0;inset-inline-start:0;inset-inline-end:0;height:{gc['strip_h']}px;background:{C['navy']};display:flex;align-items:center;gap:18px;padding:0 24px'>{chips}</div>
</div>"""


def job_card(job, box, f, uid):
    x, y, w, h = box
    col = job["color"]
    tiles = "".join(tile(tl, col, f, job.get("tile_h", 84)) for tl in job["tiles"])
    rows = "".join(row(ic, col, txt, f, job.get("row_pad"), job.get("row_px", (18, 19))) for ic, txt in job["rows"])
    docs = ""
    if job.get("documents"):
        items = "".join(
            f"<div style='display:flex;align-items:center;gap:7px;width:calc(33.33% - 6px);background:#fff;border-radius:9px;"
            f"padding:{'2px 7px' if f.ur else '4px 7px'};min-height:{job.get('chip_h', 52 if f.ur else 40)}px;box-shadow:0 1px 3px #0002'>"
            f"<div class='num' style='width:24px;height:24px;border-radius:50%;background:{C['red']};color:#fff;font-size:14px;line-height:24px;text-align:center;flex:none'>{n+1}</div>"
            f"{f.txt(dname, 13.5, 14, C['navy2'], 'min-width:0', 1.7 if f.ur else 1.15)}</div>"
            for n, dname in enumerate(job["documents"]))
        docs = (f"<div style='position:absolute;inset-inline-start:16px;inset-inline-end:16px;bottom:16px;background:{C['navy']};border-radius:16px;"
                f"padding:{'4px 10px 10px' if f.ur else '12px 10px 10px'}' data-check='docs-{uid}'>"
                f"{f.label(job['docs_title'], 13, 18, C['gold2'], 'margin:0 4px ' + ('4px' if f.ur else '10px'))}"
                f"<div style='display:flex;flex-wrap:wrap;gap:8px'>{items}</div></div>")
    note = ""
    if job.get("footer"):
        note = (f"<div style='position:absolute;inset-inline-start:24px;inset-inline-end:24px;bottom:16px;background:{col};border-radius:14px;"
                f"padding:{'2px 12px' if f.ur else '9px 12px'};text-align:center'>{f.txt(job['footer'], 16.5, 20, '#fff', 'font-weight:700;white-space:nowrap')}</div>")
    return f"""<div class='card' style='inset-inline-start:{x}px;top:{y}px;width:{w}px;height:{h}px' data-check='{uid}'>
<div style='position:absolute;top:0;inset-inline-start:0;inset-inline-end:0;height:8px;background:{col}'></div>
{ribbon(job['posts'], f) if job.get('posts') else ''}
<div style='padding:{'22px 22px 0' if f.ur else '26px 22px 0'}'>{head_block(job, f, job.get('pic', 108))}</div>
<div style='display:flex;gap:12px;padding:0 22px;margin-top:{job.get('tiles_gap', 26)}px'>{tiles}</div>
<div style='padding:0 22px;margin-top:12px'>{rows}</div>{docs}{note}
</div>"""


def build(d, lang):
    ur = lang == "ur"
    f = T(ur)
    t = d[lang]
    g = d["layout"]
    # ---------------- header: big logo on white
    hh = g["header_h"]
    header = f"""<div class='abs' style='inset-inline-start:0;top:0;width:1080px;height:{hh}px;background:#fff'></div>
<div class='abs' style='top:{(hh-146)//2}px;inset-inline-start:30px;width:580px;height:146px'>
  {logo_img('logo-horizontal-light', 'width:580px;height:146px;object-position:' + ('right' if ur else 'left'))}</div>
<div class='abs' style='top:0;height:{hh}px;inset-inline-end:34px;width:400px;display:flex;flex-direction:column;justify-content:center;align-items:flex-end;gap:{4 if ur else 10}px;text-align:end'>
  <div style='background:{C['red']};color:#fff;border-radius:10px;padding:{'0 18px' if ur else '6px 18px'};display:flex;align-items:center;gap:10px;box-shadow:0 3px 8px {C['red']}55'>
    <span class='{'mir' if ur else ''}' style='display:inline-flex'>{icon('megaphone', 30)}</span>{f.head(t['urgent'], 36, 34, '#fff', 'letter-spacing:1px' if not ur else '')}</div>
  {f.label(t['header_sub'], 16, 21, C['navy'])}
  {f.txt(t['header_tag'], 28, 19, C['emerald2'], '', 1.6 if ur else 1, 't' if ur else 'script')}
</div>
<div class='abs' style='top:{hh}px;inset-inline-start:0;width:1080px;height:6px;background:linear-gradient(90deg,{C['gold']},{C['gold2']},{C['gold']})'></div>"""
    # ---------------- hero
    ht, hh2 = hh + 6, g["hero_h"]
    tower_x = 760 if not ur else 320
    sil = (f"<svg class='abs' style='left:0;top:0' width='1080' height='{hh2}' viewBox='0 0 1080 {hh2}'>"
           f"<defs><linearGradient id='hg' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='{C['navy']}'/><stop offset='1' stop-color='{C['navy2']}'/></linearGradient>"
           f"<radialGradient id='glow' cx='{.78 if not ur else .22}' cy='.45' r='.45'><stop offset='0' stop-color='#3E74C4' stop-opacity='.55'/><stop offset='1' stop-color='#3E74C4' stop-opacity='0'/></radialGradient></defs>"
           f"<rect width='1080' height='{hh2}' fill='url(#hg)'/><rect width='1080' height='{hh2}' fill='url(#glow)'/>"
           f"<g transform='translate(0 {hh2-80})' opacity='.6'>{skyline(1080, 80, '#1A3C73')}</g>"
           f"{registan(470 if not ur else 380, hh2, 250, '#21487F')}"
           f"{tashkent_tv_tower(tower_x, hh2, hh2 - 12, '#2E5FA6')}"
           f"<rect y='{hh2-4}' width='1080' height='4' fill='{C['gold']}'/></svg>")
    plane = f"<span class='{'mir' if ur else ''}' style='display:inline-flex'>{icon('plane', 32, C['gold2'], 2)}</span>"
    dash = f"<div style='width:40px;border-top:3px dashed {C['gold']}'></div>"
    place = lambda s: f.txt(s, 17, 19, '#fff', 'font-weight:700', 1.5 if ur else 1)
    route = f"""<div style='display:inline-flex;align-items:center;gap:10px;margin-top:{4 if ur else 12}px;background:#0008;border-radius:999px;padding:{'0 18px' if ur else '6px 18px'}'>
  <div style='line-height:0;box-shadow:0 1px 4px #0006'>{flag('pakistan', 42, False)}</div>{place(t['from'])}
  {dash}{plane}{dash}
  <div style='line-height:0;box-shadow:0 1px 4px #0006'>{flag('uzbekistan', 56, False)}</div>{place(t['to'])}</div>"""
    if ur:
        headline = (f.txt(t['opener'], 0, 20, C['gold2'], '', 1.55) +
                    f.txt(t['headline1'], 0, 34, '#fff', 'font-weight:700', 1.55) +
                    f.txt(t['headline2'], 0, 34, C['gold2'], 'font-weight:700', 1.55))
    else:
        headline = (f.label(t['opener'], 16, 0, C['gold2']) +
                    f"<div class='anton' style='font-size:50px;color:#fff;line-height:1.04;margin-top:8px'>{t['headline1']}</div>"
                    f"<div class='anton' style='font-size:50px;color:{C['gold2']};line-height:1.04'>{t['headline2']}</div>")
    stat = f"""<div class='abs' style='top:{g['stat_top']}px;inset-inline-end:36px;width:230px;text-align:center'>
  <div style='display:inline-block;filter:drop-shadow(0 6px 10px #0007)'>{flag('uzbekistan', 200, True, 'heroflag' + lang)}</div>
  <div style='background:#fff;border-radius:14px;padding:{'0 10px 4px' if ur else '6px 10px 8px'};margin-top:2px;box-shadow:0 4px 14px #0005;display:flex;align-items:center;justify-content:center;gap:10px'>
    <div class='num' style='font-size:42px;color:{C['red']};line-height:1.05'>{t['stat_n']}</div>
    <div style='text-align:start'>{f.label(t['stat_label'], 12, 16, C['navy'], 'line-height:' + ('1.5' if ur else '1.3'))}</div></div></div>"""
    hero = f"""<div class='abs' style='top:{ht}px;inset-inline-start:0;width:1080px;height:{hh2}px;overflow:hidden'>{sil}
<div class='abs' style='top:{g['headline_top_ur' if ur else 'headline_top']}px;inset-inline-start:36px;width:720px'>{headline}{route}</div>{stat}</div>"""
    # ---------------- cards
    gy = ht + hh2 + g["gap"]
    group = group_card(t["group"], (30, gy, 1020, g["group_h"]), f, f"group-{lang}")
    jy = gy + g["group_h"] + g["gap"]
    jh = g["cta_top"] - g["gap"] - jy
    jobs = "".join(job_card(job, (30 + i * 520, jy, 500, jh), f, f"job{i}-{lang}") for i, job in enumerate(t["jobs"]))
    # ---------------- CTA
    cy = g["cta_top"]
    cta = f"""<div class='abs' style='top:{cy}px;inset-inline-start:0;width:1080px;height:{1350-cy}px;background:linear-gradient(100deg,{C['green']},#13704A 60%,{C['emerald2']})'></div>
<div class='abs' style='top:{cy}px;height:{1350-cy}px;inset-inline-start:36px;width:420px;display:flex;flex-direction:column;justify-content:center'>
  {f.head(t['apply'], 42, 34, C['gold2'])}
  {f.txt(t['note'], 15, 17, '#E6F4EC', 'margin-top:' + ('0' if ur else '6px'), 1.5 if ur else 1.3)}</div>
<div class='abs' style='top:{cy+12}px;inset-inline-end:30px;height:{1350-cy-24}px;background:#fff;border-radius:999px;display:flex;align-items:center;gap:16px;padding-inline:10px 34px;box-shadow:0 6px 18px #0004' data-check='wa-{lang}'>
  {whatsapp_icon(60)}<div class='num' style='font-size:56px;color:{C['navy2']};line-height:1.15'>{WHATSAPP}</div></div>"""
    return page(f"<div class='{'ur-on' if ur else ''}'>{header}{hero}{group}{jobs}{cta}</div>", css(ur), rtl=ur)


def main(mod_name):
    d = importlib.import_module(f"data.{mod_name}").DATA
    for lang, suffix in (("en", "English"), ("ur", "Urdu")):
        html = build(d, lang)
        bad = overflow_report(html)
        if bad:
            print(f"[{lang}] overflowing boxes: {bad}")
        print(render(html, f"{d['stem']}-{suffix}.png"))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "uzbekistan_combined")
