"""RS Links A4 letterhead (2026-10-23). Same family as the file cover / business cards: white page, round badge logo,
green-gold 3D swoosh top-right, slim gold rule, 3D wave footer with all four numbers, email, website, address.
Outputs (output/letterhead/):
  RS-Links-Letterhead-A4.pdf / .ai / .eps  vector print files (Chromium PDF; .ai is PDF-compatible)
  RS-Links-Letterhead-A4.png               300 dpi image
  RS-Links-Letterhead-A4.docx              Word template: header + footer artwork, blank body to type letters in"""
import shutil
import subprocess

from common import C, OUTPUT, PHONES, _launch, font_css, icon, logo_img, whatsapp_icon
from file_cover import swoosh, wave3d
from office_banners import TAGLINE_EN, WEBSITE

# Office number corrected to 320 (user, 2026-10-26)
ADDRESS = "Office No. 320, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"

GREEN, GOLD, NAVY = C["green"], C["gold2"], "#0A1B25"
EMAIL = "hr@rslinksconsultants.com"
PX = 96
W, H = round(8.27 * PX), round(11.69 * PX)            # A4 at 96 css px / in
HEAD_H, FOOT_H = 150, 190                              # header / footer bands (also used for the Word template)


def header(w=W):
    return f"""<div style='position:absolute;left:0;top:0;width:{w}px;height:{HEAD_H}px'>
{swoosh(w, H, 'lh', right=True)}
<div style='position:absolute;left:44px;top:30px;display:flex;align-items:center;gap:14px'>
 {logo_img('logo-badge', 'width:84px;height:84px')}
 <div><div style='font-family:Anton;font-size:30px;color:{GREEN};letter-spacing:.5px;line-height:1'>RS LINKS CONSULTANTS</div>
  <div style='font:800 10.5px Archivo;color:{NAVY};letter-spacing:4px;margin-top:4px'>PVT. LTD.</div>
  <div style='font-family:Dancing;font-weight:700;font-size:17px;color:#A87508;margin-top:2px'>{TAGLINE_EN}</div></div></div>
<div style='position:absolute;left:44px;right:44px;top:{HEAD_H - 14}px;height:3px;background:linear-gradient(90deg,{GREEN},{GOLD} 60%,#fff0)'></div></div>"""


def footer(w=W):
    row = lambda ic, t: (f"<div style='display:flex;align-items:center;gap:6px'><span style='width:18px;height:18px;border-radius:50%;background:{GOLD};display:inline-flex;align-items:center;justify-content:center'>{icon(ic, 11, NAVY, 2.6)}</span>"
                         f"<span style='font:700 11.5px Archivo;color:#fff;white-space:nowrap'>{t}</span></div>")
    nums = "".join(f"<div style='display:flex;align-items:center;gap:4px'>{whatsapp_icon(16)}<span style='font-family:Anton;font-size:14px;color:#fff;letter-spacing:.3px'>{n}</span></div>" for n in PHONES)
    return f"""<div style='position:absolute;left:0;bottom:0;width:{w}px;height:{FOOT_H}px;overflow:hidden'>
<div style='position:absolute;left:0;top:{-(H - FOOT_H)}px;width:{w}px;height:{H}px'>{wave3d(w, H, 0.9, 0.02, 'lf')}</div>
<div style='position:absolute;left:40px;right:40px;bottom:62px;display:flex;justify-content:space-between'>{nums}</div>
<div style='position:absolute;left:40px;right:40px;bottom:36px;display:flex;justify-content:center;gap:40px'>{row('mail', EMAIL)}{row('gear', WEBSITE)}</div>
<div style='position:absolute;left:40px;right:40px;bottom:12px;display:flex;justify-content:center'>{row('pin', ADDRESS + ', Pakistan')}</div></div>"""


def page():
    return f"""<div style='position:relative;width:{W}px;height:{H}px;background:#fff;overflow:hidden'>
{header()}
<div style='position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);opacity:.045'>{logo_img('logo-badge', 'width:420px;height:420px')}</div>
<div style='position:absolute;right:52px;top:{HEAD_H + 10}px;font:600 12px Archivo;color:#55606A;text-align:right;line-height:1.9'>Ref: ____________________<br>Date: ____________________</div>
{footer()}</div>"""


def html(body, w, h):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{font_css()}@page{{size:{w}px {h}px;margin:0}}"
            f"html,body{{margin:0;width:{w}px;height:{h}px;overflow:hidden}}</style></head><body>{body}</body></html>")


def main():
    from playwright.sync_api import sync_playwright
    out = OUTPUT / "letterhead"
    out.mkdir(parents=True, exist_ok=True)
    tmp = OUTPUT / ".tmp"
    tmp.mkdir(exist_ok=True)
    stem = out / "RS-Links-Letterhead-A4"
    jobs = [("page", page(), W, H, 300 / PX),
            ("header", f"<div style='position:relative;width:{W}px;height:{HEAD_H}px;overflow:hidden;background:#fff'>{header()}</div>", W, HEAD_H, 300 / PX),
            ("footer", f"<div style='position:relative;width:{W}px;height:{FOOT_H}px;overflow:hidden;background:#fff'>{footer()}</div>", W, FOOT_H, 300 / PX)]
    with sync_playwright() as pw:
        b = _launch(pw)
        for name, body, w, h, sc in jobs:
            f = tmp / f"letterhead-{name}.html"
            f.write_text(html(body, w, h), encoding="utf-8")
            pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=sc)
            pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
            pg.screenshot(path=str(stem) + ("" if name == "page" else f"_{name}") + ".png")
            if name == "page":
                pg.pdf(path=str(stem) + ".pdf", width="8.27in", height="11.69in", print_background=True)
            pg.close()
        b.close()
    subprocess.run(["pdftocairo", "-eps", str(stem) + ".pdf", str(stem) + ".eps"], check=True)
    shutil.copy(str(stem) + ".pdf", str(stem) + ".ai")
    # Word template: artwork as full-width header / footer pictures, body left empty for typing.
    from docx import Document
    from docx.shared import Inches, Pt
    d = Document()
    s = d.sections[0]
    s.page_width, s.page_height = Inches(8.27), Inches(11.69)
    s.left_margin = s.right_margin = Inches(0.8)
    s.top_margin, s.bottom_margin = Inches(HEAD_H / PX + 0.25), Inches(FOOT_H / PX + 0.2)
    s.header_distance = s.footer_distance = Inches(0)
    for part, img in ((s.header, "_header"), (s.footer, "_footer")):
        p = part.paragraphs[0]
        p.paragraph_format.left_indent = Inches(-0.8)
        p.paragraph_format.right_indent = Inches(-0.8)
        p.add_run().add_picture(str(stem) + img + ".png", width=Inches(8.27))
    body = d.paragraphs[0] if d.paragraphs else d.add_paragraph()
    for t in ("Ref: ______________", "Date: ______________", "", "To,", "", "Subject: ", "", "Dear Sir / Madam,", ""):
        para = d.add_paragraph(t)
        para.style.font.name, para.style.font.size = "Calibri", Pt(11)
    d.save(str(stem) + ".docx")
    for f in sorted(out.iterdir()):
        print(f)


if __name__ == "__main__":
    main()
