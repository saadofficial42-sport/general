"""RS Links stickers (2026-11-05) for envelopes, passports, files.
  1. Round seal sticker, 2 in diameter (logo badge + name ring + tagline)
  2. Rectangular label, 3.5 x 1.5 in (logo, name, tagline, email, website, 4 WhatsApp numbers)
Each sticker: single file with 0.0625 in bleed (PNG 600 dpi, PDF, AI, EPS, SVG) plus an A4 print sheet of each with
light grey cut guides. Address left off (small size; office number 20 vs 320 still to be confirmed).
Outputs output/stickers/ + RS-Links-Stickers-Print-Files.zip."""
import math
import shutil
import subprocess
import zipfile

from common import C, OUTPUT, PHONES, _launch, font_css, icon, logo_img, whatsapp_icon

GREEN, DEEP, GOLD, GOLD2, NAVY = C["green"], "#06291D", "#C9962B", "#F3D27A", "#0A1B25"
EMAIL, WEBSITE, TAGLINE = "hr@rslinksconsultants.com", "www.rslinksconsultants.com", "Turning Your Dreams into Reality"
PX, BLEED = 96, 0.0625


def round_sticker():
    d = round((2 + 2 * BLEED) * PX)
    c, r = d / 2, 2 * PX / 2
    text_r = r - 17
    return d, d, f"""<div style='position:relative;width:{d}px;height:{d}px'>
<svg width='{d}' height='{d}' style='position:absolute;left:0;top:0'><defs>
 <radialGradient id='rg' cx='.3' cy='.25' r='.9'><stop offset='0' stop-color='#1FA36B'/><stop offset='.55' stop-color='{GREEN}'/><stop offset='1' stop-color='{DEEP}'/></radialGradient>
 <linearGradient id='rgold' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#FFEBA8'/><stop offset='.5' stop-color='{GOLD2}'/><stop offset='1' stop-color='{GOLD}'/></linearGradient>
 <path id='tp' d='M {c - text_r} {c} A {text_r} {text_r} 0 0 1 {c + text_r} {c}'/>
 <path id='bp' d='M {c - text_r - 9} {c} A {text_r + 9} {text_r + 9} 0 0 0 {c + text_r + 9} {c}'/></defs>
 <circle cx='{c}' cy='{c}' r='{d / 2}' fill='url(#rg)'/>
 <circle cx='{c}' cy='{c}' r='{r - 4}' fill='none' stroke='url(#rgold)' stroke-width='3'/>
 <circle cx='{c}' cy='{c}' r='{r - 30}' fill='none' stroke='url(#rgold)' stroke-width='1.2' stroke-dasharray='2 2'/>
 <text font-family='Anton' font-size='15' letter-spacing='2.2' fill='#fff' text-anchor='middle'><textPath href='#tp' startOffset='50%'>RS LINKS CONSULTANTS</textPath></text>
 <text font-family='Archivo' font-weight='800' font-size='8.5' letter-spacing='2.5' fill='{GOLD2}' text-anchor='middle'><textPath href='#bp' startOffset='50%'>PVT. LTD. • RAWALPINDI</textPath></text>
 <text x='{c - r + 14}' y='{c + 4}' font-size='11' fill='{GOLD2}' text-anchor='middle'>★</text><text x='{c + r - 14}' y='{c + 4}' font-size='11' fill='{GOLD2}' text-anchor='middle'>★</text></svg>
<div style='position:absolute;left:{c - 38}px;top:{c - 44}px;width:76px;height:76px;border-radius:50%;background:#fff;box-shadow:0 2px 6px #0006'>{logo_img('logo-badge', 'width:76px;height:76px')}</div>
<div style='position:absolute;left:0;right:0;top:{c + 36}px;text-align:center;font-family:Dancing;font-weight:700;font-size:10px;color:{GOLD2};line-height:1'>{TAGLINE}</div></div>"""


def rect_sticker():
    w, h = round((3.5 + 2 * BLEED) * PX), round((1.5 + 2 * BLEED) * PX)
    b = round(BLEED * PX) + 9
    wa = "".join(f"<div style='display:flex;align-items:center;gap:3px'>{whatsapp_icon(11)}<span style='font:400 10.5px Anton;color:#fff;letter-spacing:.2px'>{n.replace('+92 ', '0')}</span></div>" for n in PHONES)
    row = lambda ic, t: (f"<div style='display:flex;align-items:center;gap:5px'><span style='width:13px;height:13px;border-radius:50%;background:{GREEN};display:inline-flex;align-items:center;justify-content:center'>{icon(ic, 8, '#fff', 2.6)}</span>"
                         f"<span style='font:700 8.6px Archivo;color:{NAVY}'>{t}</span></div>")
    return w, h, f"""<div style='position:relative;width:{w}px;height:{h}px;background:radial-gradient(circle at 20% 20%,#fff,#F2F6F3);overflow:hidden'>
<svg width='{w}' height='{h}' style='position:absolute;left:0;top:0'><defs>
 <linearGradient id='qg' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#1FA36B'/><stop offset='.55' stop-color='{GREEN}'/><stop offset='1' stop-color='{DEEP}'/></linearGradient>
 <linearGradient id='qgold' x1='0' y1='0' x2='1' y2='0'><stop offset='0' stop-color='#FFEBA8'/><stop offset='.5' stop-color='{GOLD2}'/><stop offset='1' stop-color='{GOLD}'/></linearGradient></defs>
 <path d='M0 {h - 40} C {w * .3:.0f} {h - 56}, {w * .65:.0f} {h - 30}, {w} {h - 50} V{h} H0Z' fill='url(#qgold)'/>
 <path d='M0 {h - 35} C {w * .3:.0f} {h - 51}, {w * .65:.0f} {h - 25}, {w} {h - 45} V{h} H0Z' fill='url(#qg)'/>
 <path d='M{w - 70} 0 H{w} V60 C {w - 20} 40, {w - 50} 20, {w - 70} 0Z' fill='url(#qgold)'/><path d='M{w - 58} 0 H{w} V48 C {w - 18} 32, {w - 40} 16, {w - 58} 0Z' fill='url(#qg)'/></svg>
<div style='position:absolute;left:{b}px;top:{b - 2}px;display:flex;align-items:center;gap:9px'>
 {logo_img('logo-badge', 'width:56px;height:56px')}
 <div><div style='font:400 19px Anton;color:{GREEN};letter-spacing:.4px;line-height:1'>RS LINKS CONSULTANTS</div>
  <div style='font:800 7px Archivo;color:{NAVY};letter-spacing:2.6px;margin-top:2px'>PVT. LTD.</div>
  <div style='font-family:Dancing;font-weight:700;font-size:11px;color:#A87508;margin-top:1px'>{TAGLINE}</div></div></div>
<div style='position:absolute;left:{b + 65}px;top:{b + 58}px;display:flex;gap:12px'>{row('mail', EMAIL)}{row('gear', WEBSITE)}</div>
<div style='position:absolute;left:{b}px;right:{b}px;bottom:{b - 4}px;display:flex;justify-content:space-between'>{wa}</div></div>"""


def sheet(w, h, body, cols, rows, gap, round_cut=False):
    A4W, A4H = round(8.27 * PX), round(11.69 * PX)
    gw, gh = cols * w + (cols - 1) * gap, rows * h + (rows - 1) * gap
    x0, y0 = (A4W - gw) / 2, (A4H - gh) / 2
    cells = ""
    for i in range(rows):
        for j in range(cols):
            x, y = x0 + j * (w + gap), y0 + i * (h + gap)
            cut = (f"border-radius:50%;" if round_cut else "")
            cells += (f"<div style='position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;overflow:hidden;{cut}'>{body}</div>"
                      f"<div style='position:absolute;left:{x + BLEED * PX}px;top:{y + BLEED * PX}px;width:{w - 2 * BLEED * PX}px;height:{h - 2 * BLEED * PX}px;border:.5px dashed #9AA5A0;{cut}box-sizing:border-box'></div>")
    return A4W, A4H, f"<div style='position:relative;width:{A4W}px;height:{A4H}px;background:#fff'>{cells}</div>"


def export(pg, stem, w, h, body, dpi=600):
    f = OUTPUT / ".tmp" / f"{stem.name}.html"
    f.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{font_css()}@page{{size:{w}px {h}px;margin:0}}"
                 f"html,body{{margin:0;width:{w}px;height:{h}px;overflow:hidden;background:transparent}}</style></head><body>{body}</body></html>", encoding="utf-8")
    pg.set_viewport_size({"width": w, "height": h})
    pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
    pg.screenshot(path=str(stem) + ".png", omit_background=True)
    pg.pdf(path=str(stem) + ".pdf", width=f"{w}px", height=f"{h}px", print_background=True)
    subprocess.run(["pdftocairo", "-svg", str(stem) + ".pdf", str(stem) + ".svg"], check=True)
    subprocess.run(["pdftocairo", "-eps", str(stem) + ".pdf", str(stem) + ".eps"], check=True)
    shutil.copy(str(stem) + ".pdf", str(stem) + ".ai")


def main():
    from playwright.sync_api import sync_playwright
    out = OUTPUT / "stickers"
    out.mkdir(parents=True, exist_ok=True)
    (OUTPUT / ".tmp").mkdir(exist_ok=True)
    rw, rh, rb = round_sticker()
    qw, qh, qb = rect_sticker()
    jobs = [("RS-Links-Sticker-Round-2in", rw, rh, f"<div style='width:{rw}px;height:{rh}px;border-radius:50%;overflow:hidden'>{rb}</div>"),
            ("RS-Links-Sticker-Label-3.5x1.5in", qw, qh, qb),
            ("RS-Links-Sticker-Round-A4-Sheet-12", *sheet(rw, rh, rb, 3, 4, 26, True)),
            ("RS-Links-Sticker-Label-A4-Sheet-14", *sheet(qw, qh, qb, 2, 7, 12))]
    with sync_playwright() as pw:
        b = _launch(pw)
        pg = b.new_page(device_scale_factor=600 / PX)
        for name, w, h, body in jobs:
            export(pg, out / name, w, h, body)
            print(out / name)
        b.close()
    with zipfile.ZipFile(out / "RS-Links-Stickers-Print-Files.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for name, *_ in jobs:
            for ext in ("pdf", "ai", "eps", "svg", "png"):
                z.write(out / f"{name}.{ext}", f"{name}.{ext}")
        z.writestr("READ-ME.txt", "RS Links stickers\n- Round: 2 in diameter (+1/16 in bleed). Label: 3.5 x 1.5 in (+1/16 in bleed).\n"
                   "- A4 sheets: 12 round / 14 labels; dashed grey lines are cut guides (do not print if die-cutting).\n"
                   "- CorelDRAW: import the EPS or SVG. Illustrator: open the AI.\n")


if __name__ == "__main__":
    main()
