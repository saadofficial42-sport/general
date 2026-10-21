"""RS Links round badge logo redrawn as true vector (2026-10-21) from assets/logo/logo-badge.png (592 px raster, the
only source we have). Same geometry and colours, sampled from the PNG. Outputs to output/logo-vector/:
  RS-Links-Round-Logo.ai  (PDF-compatible Illustrator file, editable shapes + live text)
  RS-Links-Round-Logo.svg (text converted to outlines), RS-Links-Round-Logo.eps, and a 2000 px PNG preview."""
import shutil
import subprocess

from common import OUTPUT, _launch, font_css

NAVY, CREAM, GOLD, GOLD_D, GRN_L, GRN, GRN_D = "#0F2330", "#FBFAF6", "#F0B545", "#C98A12", "#50BB8F", "#2E946D", "#0E6445"
C = 296  # centre of the 592 x 592 artboard


def star4(cx, cy, r, fill):
    k = r * .28
    return f"<path d='M{cx} {cy - r} L{cx + k} {cy - k} L{cx + r} {cy} L{cx + k} {cy + k} L{cx} {cy + r} L{cx - k} {cy + k} L{cx - r} {cy} L{cx - k} {cy - k}Z' fill='{fill}'/>"


def star5(cx, cy, r, fill):
    import math
    pts = []
    for i in range(10):
        a = math.radians(-90 + i * 36)
        rr = r if i % 2 == 0 else r * .42
        pts.append(f"{cx + rr * math.cos(a):.2f},{cy + rr * math.sin(a):.2f}")
    return f"<polygon points='{' '.join(pts)}' fill='{fill}'/>"


def link(cx, cy, color):
    # stadium-shaped chain link along the 45 degree diagonal, drawn as a thick stroke
    return (f"<rect x='{cx - 76}' y='{cy - 35}' width='152' height='70' rx='35' fill='none' stroke='{color}' stroke-width='30' "
            f"transform='rotate(-45 {cx} {cy})'/>")


def svg():
    wx, wy, ox, oy = 266, 326, 326, 266
    return f"""<svg xmlns='http://www.w3.org/2000/svg' width='592' height='592' viewBox='0 0 592 592'>
<defs>
 <radialGradient id='g' cx='.28' cy='.22' r='.95'><stop offset='0' stop-color='{GRN_L}'/><stop offset='.55' stop-color='{GRN}'/><stop offset='1' stop-color='{GRN_D}'/></radialGradient>
 <path id='top' d='M {C - 222} {C} A 222 222 0 0 1 {C + 222} {C}'/>
 <path id='bot' d='M {C - 242} {C} A 242 242 0 0 0 {C + 242} {C}'/>
 <clipPath id='cut'><polygon points='0,0 592,0 0,592'/></clipPath>
</defs>
<circle cx='{C}' cy='{C}' r='293' fill='{NAVY}'/>
<circle cx='{C}' cy='{C}' r='278' fill='{CREAM}'/>
<circle cx='{C}' cy='{C}' r='268' fill='none' stroke='{NAVY}' stroke-width='3'/>
<circle cx='{C}' cy='{C}' r='183' fill='none' stroke='{NAVY}' stroke-width='4.5' stroke-dasharray='6 4'/>
<circle cx='{C}' cy='{C}' r='179' fill='url(#g)'/>
<g transform='translate({C} {C}) scale(1.1) translate(-{C} -{C})'>{link(ox, oy, GOLD)}{link(wx, wy, '#FFFFFF')}
<g clip-path='url(#cut)'>{link(ox, oy, GOLD)}</g></g>
<text font-family='Archivo' font-weight='800' font-size='41' letter-spacing='4.5' fill='{NAVY}' text-anchor='middle'><textPath href='#top' startOffset='50%'>RS LINKS CONSULTANTS</textPath></text>
<text font-family='Archivo' font-weight='800' font-size='34' letter-spacing='6' fill='{NAVY}' text-anchor='middle'><textPath href='#bot' startOffset='50%'>PVT. LTD.</textPath></text>
{star4(69, 296, 15, GOLD_D)}{star4(523, 296, 15, GOLD_D)}
{star5(171, 493, 14, NAVY)}{star5(421, 493, 14, NAVY)}
</svg>"""


def main():
    from playwright.sync_api import sync_playwright
    out = OUTPUT / "logo-vector"
    out.mkdir(parents=True, exist_ok=True)
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{font_css()}@page{{size:592px 592px;margin:0}}"
            f"html,body{{margin:0;width:592px;height:592px;overflow:hidden;background:transparent}}</style></head><body>{svg()}</body></html>")
    tmp = OUTPUT / ".tmp" / "logo-vector.html"
    tmp.parent.mkdir(exist_ok=True)
    tmp.write_text(html, encoding="utf-8")
    stem = out / "RS-Links-Round-Logo"
    with sync_playwright() as pw:
        b = _launch(pw)
        pg = b.new_page(viewport={"width": 592, "height": 592}, device_scale_factor=2000 / 592)
        pg.goto(tmp.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
        pg.screenshot(path=str(stem) + "_2000px.png", omit_background=True)
        pg.pdf(path=str(stem) + ".pdf", width="592px", height="592px", print_background=True)
        b.close()
    subprocess.run(["pdftocairo", "-svg", str(stem) + ".pdf", str(stem) + ".svg"], check=True)
    subprocess.run(["pdftocairo", "-eps", str(stem) + ".pdf", str(stem) + ".eps"], check=True)
    shutil.move(str(stem) + ".pdf", str(stem) + ".ai")
    print(stem)


if __name__ == "__main__":
    main()
