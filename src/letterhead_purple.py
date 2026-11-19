"""RS Links A4 letterhead — purple version (2026-11-19). User supplied details (marketing contact card): call/WhatsApp
+92 325 5547027, rslinksmarketing@gmail.com, office Foundation University Incubation Centre, New Lalazar, Rawalpindi;
plus website and official email hr@rslinksconsultants.com. Purple round logo, deep-violet curved header band with
lavender sparkle, services line, violet wave footer. Outputs output/letterhead-purple/ (PDF/AI/EPS/PNG/DOCX)."""
import shutil
import subprocess

from common import OUTPUT, _launch, font_css, icon
from letterhead import html, PX, W, H
from office_banners import WEBSITE

VIO, VIO2, VIO3, LAV, INK = "#5B2A86", "#3A1663", "#2A0E4A", "#B79BE0", "#2A0E4A"
PHONE = "+92 325 5547027"
EMAILS = ("info@rslinksconsultants.com", "rslinksmarketing@gmail.com")
ADDRESS = "Foundation University, Incubation Centre, New Lalazar, Rawalpindi, Pakistan"
SERVICES = "Branding | Social | Content | Ads | Web | SEO | Strategy | Influence | E-commerce"
LOGO = (OUTPUT / "logo-vector" / "RS-Links-Round-Logo-Purple_2000px.png").as_uri()
HEAD_H, FOOT_H = 150, 150


def header(w=W):
    return f"""<div style='position:absolute;left:0;top:0;width:{w}px;height:{HEAD_H}px;overflow:hidden'>
<svg style='position:absolute;right:0;top:0' width='420' height='{HEAD_H}'><defs><linearGradient id='hv' x1='0' x2='1'><stop offset='0' stop-color='{VIO}'/><stop offset='1' stop-color='{VIO3}'/></linearGradient></defs>
 <path d='M120 0 H420 V{HEAD_H} H300 C200 {HEAD_H} 170 60 120 0Z' fill='url(#hv)'/><path d='M60 0 C120 50 150 110 250 {HEAD_H}' stroke='{LAV}' stroke-width='3' fill='none' opacity='.7'/>
 <path d='M340 40 l4 10 10 4 -10 4 -4 10 -4 -10 -10 -4 10 -4z' fill='#fff'/><path d='M385 95 l3 7 7 3 -7 3 -3 7 -3 -7 -7 -3 7 -3z' fill='{LAV}'/></svg>
<div style='position:absolute;left:44px;top:28px;display:flex;align-items:center;gap:14px'>
 <img src='{LOGO}' style='width:88px;height:88px'>
 <div><div style='font-family:Anton;font-size:30px;color:{VIO};letter-spacing:.5px;line-height:1'>RS LINKS CONSULTANTS</div>
  <div style='font:800 10.5px Archivo;color:{INK};letter-spacing:4px;margin-top:4px'>PVT. LTD.</div>
  <div style='font:600 10px Archivo;color:#7A5E9E;margin-top:5px;letter-spacing:.3px'>{SERVICES}</div></div></div>
<div style='position:absolute;left:44px;right:44px;top:{HEAD_H - 12}px;height:3px;background:linear-gradient(90deg,{VIO},{LAV} 60%,#fff0)'></div></div>"""


def footer(w=W):
    row = lambda ic, t: (f"<div style='display:flex;align-items:center;gap:6px'><span style='width:20px;height:20px;border-radius:50%;background:#fff;display:inline-flex;align-items:center;justify-content:center'>{icon(ic, 12, VIO, 2.6)}</span>"
                         f"<span style='font:700 12px Archivo;color:#fff;white-space:nowrap'>{t}</span></div>")
    return f"""<div style='position:absolute;left:0;bottom:0;width:{w}px;height:{FOOT_H}px;overflow:hidden'>
<svg style='position:absolute;left:0;top:0' width='{w}' height='{FOOT_H}'><defs><linearGradient id='fv' x1='0' x2='1'><stop offset='0' stop-color='{VIO3}'/><stop offset='.5' stop-color='{VIO}'/><stop offset='1' stop-color='{VIO2}'/></linearGradient></defs>
 <path d='M0 40 C {w*.3:.0f} 0, {w*.6:.0f} 60, {w} 20 V{FOOT_H} H0Z' fill='url(#fv)'/><path d='M0 40 C {w*.3:.0f} 0, {w*.6:.0f} 60, {w} 20' stroke='{LAV}' stroke-width='3' fill='none'/></svg>
<div style='position:absolute;left:40px;right:40px;bottom:72px;display:flex;justify-content:center;gap:34px'>{row('phone', 'Call / WhatsApp: ' + PHONE)}{row('gear', WEBSITE)}</div>
<div style='position:absolute;left:40px;right:40px;bottom:44px;display:flex;justify-content:center;gap:34px'>{row('mail', EMAILS[0])}{row('mail', EMAILS[1])}</div>
<div style='position:absolute;left:40px;right:40px;bottom:16px;display:flex;justify-content:center'>{row('pin', ADDRESS)}</div></div>"""


def page():
    return f"""<div style='position:relative;width:{W}px;height:{H}px;background:#fff;overflow:hidden'>
{header()}
<div style='position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);opacity:.05'><img src='{LOGO}' style='width:420px;height:420px'></div>
<div style='position:absolute;right:52px;top:{HEAD_H + 10}px;font:600 12px Archivo;color:#5E5470;text-align:right;line-height:1.9'>Ref: ____________________<br>Date: ____________________</div>
{footer()}</div>"""


def main():
    from playwright.sync_api import sync_playwright
    out = OUTPUT / "letterhead-purple"
    out.mkdir(parents=True, exist_ok=True)
    tmp = OUTPUT / ".tmp"
    tmp.mkdir(exist_ok=True)
    stem = out / "RS-Links-Letterhead-Purple-A4"
    jobs = [("page", page(), W, H, 300 / PX),
            ("header", f"<div style='position:relative;width:{W}px;height:{HEAD_H}px;overflow:hidden;background:#fff'>{header()}</div>", W, HEAD_H, 300 / PX),
            ("footer", f"<div style='position:relative;width:{W}px;height:{FOOT_H}px;overflow:hidden;background:#fff'>{footer()}</div>", W, FOOT_H, 300 / PX)]
    with sync_playwright() as pw:
        b = _launch(pw)
        for name, body, w, h, sc in jobs:
            f = tmp / f"letterhead-purple-{name}.html"
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
