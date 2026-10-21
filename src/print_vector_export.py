"""Vector print files for the printing shop (2026-10-21): the shop cannot use our raster PDFs and needs
CorelDRAW or Adobe Illustrator files. We cannot write native .cdr, so each design side is exported as:
  - .ai  : Chromium vector PDF (Illustrator's own format is PDF-based; Illustrator and CorelDRAW open it directly)
  - .eps : Encapsulated PostScript (imports into CorelDRAW and Illustrator)
  - .svg : all text converted to outlines (curves), so no fonts are needed on the shop's computer
plus a low-res _preview.png for checking. Sizes include the 0.125 in bleed.
Output: output/for-printer/vector/ and output/for-printer/RS-Links-Print-Files-CorelDraw-Illustrator.zip"""
import shutil
import subprocess
import zipfile

import business_cards as bc
import business_card_general as gen
import file_cover as fc
from common import OUTPUT, _launch, font_css

OUT = OUTPUT / "for-printer" / "vector"
TMP = OUTPUT / ".tmp"


def export(pg, name, body_html, w_px, h_px, css=""):
    w_in, h_in = w_px / 96, h_px / 96
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{font_css()}{css}"
            f"@page{{size:{w_in}in {h_in}in;margin:0}}html,body{{margin:0;padding:0;width:{w_px}px;height:{h_px}px;overflow:hidden}}</style></head>"
            f"<body><div style='position:relative;width:{w_px}px;height:{h_px}px;overflow:hidden'>{body_html}</div></body></html>")
    f = TMP / f"vec-{name}.html"
    f.write_text(html, encoding="utf-8")
    pg.set_viewport_size({"width": w_px, "height": h_px})
    pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
    stem = OUT / name
    pdf = OUT / (name + ".pdf")
    pg.pdf(path=str(pdf), width=f"{w_in}in", height=f"{h_in}in", print_background=True)
    pg.screenshot(path=str(stem) + "_preview.png")
    subprocess.run(["pdftocairo", "-svg", str(pdf), str(stem) + ".svg"], check=True)
    subprocess.run(["pdftocairo", "-eps", str(pdf), str(stem) + ".eps"], check=True)
    shutil.move(pdf, str(stem) + ".ai")
    print(stem)


def main():
    from playwright.sync_api import sync_playwright
    OUT.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(exist_ok=True)
    jobs = []
    for p in bc.PEOPLE:
        jobs += [(f"Business-Card_{p['slug']}_Front", bc.front(p)), (f"Business-Card_{p['slug']}_Back", bc.back())]
    jobs += [("Business-Card_General_Front", bc.back()), ("Business-Card_General_Back", bc.back_services())]
    card_css = ".card{position:relative;width:%dpx;height:%dpx;overflow:hidden;font-family:'Archivo',sans-serif}" % (bc.PX_W, bc.PX_H)
    spine = (f"<div style='position:absolute;left:{fc.W}px;top:0;width:{fc.SW}px;height:{fc.H}px;background:{fc.DEEP};display:flex;align-items:center;justify-content:center'>"
             f"<div style='transform:rotate(-90deg);white-space:nowrap;font-family:Anton;font-size:26px;letter-spacing:6px;color:{fc.GOLD}'>RS LINKS CONSULTANTS PVT. LTD.</div></div>")
    spread = (f"<div style='position:absolute;left:0;top:0;width:{fc.W}px;height:{fc.H}px'>{fc.back()}</div>{spine}"
              f"<div style='position:absolute;left:{fc.W + fc.SW}px;top:0;width:{fc.W}px;height:{fc.H}px'>{fc.front()}</div>")
    with sync_playwright() as pw:
        b = _launch(pw)
        pg = b.new_page()
        for name, html in jobs:
            export(pg, name, html, bc.PX_W, bc.PX_H, card_css)
        export(pg, "File-Cover_Front_9.25x12.25in", fc.front(), fc.W, fc.H)
        export(pg, "File-Cover_Back_9.25x12.25in", fc.back(), fc.W, fc.H)
        export(pg, "File-Cover_Spread-with-Spine_19x12.25in", spread, 2 * fc.W + fc.SW, fc.H)
        b.close()
    z = OUTPUT / "for-printer" / "RS-Links-Print-Files-CorelDraw-Illustrator.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(OUT.iterdir()):
            if f.suffix in (".ai", ".eps", ".svg") and not f.name.endswith("_preview.png"):
                folder = "Business-Cards" if f.name.startswith("Business-Card") else "File-Cover"
                zf.write(f, f"{folder}/{f.suffix[1:].upper()}/{f.name}")
        zf.writestr("READ-ME.txt",
                    "RS Links Consultants - print files\n\n"
                    "Each design is supplied in three formats (same artwork):\n"
                    "  AI  - Adobe Illustrator (PDF-compatible .ai). Opens in Illustrator; CorelDRAW: File > Import/Open.\n"
                    "  EPS - opens/imports in both CorelDRAW and Illustrator.\n"
                    "  SVG - all text already converted to curves (no fonts needed). Imports into CorelDRAW and Illustrator.\n\n"
                    "Business cards: 3.5 x 2 in finished, files are 3.75 x 2.25 in (0.125 in bleed on every side).\n"
                    "File cover: 9.25 x 12.25 in panels + 0.5 in spine, 0.125 in bleed on every side.\n"
                    "Fonts used (if needed for the AI/EPS files): Archivo, Anton (Google Fonts, free).\n")
    print(z)


if __name__ == "__main__":
    main()
