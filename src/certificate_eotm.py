"""Employee of the Month certificate (2026-11-04). A4 landscape (11.69 x 8.27 in). Blank lines for the employee's name
and month (fill by hand or type in CorelDRAW / Illustrator), two signatories: Rahim Ullah (Co-Founder & CEO) and
Saad Khalid (Co-Founder & COO). Design: white page, layered green + gold 3D waves in opposite corners, guilloche
double border, gold rosette seal with ribbons, round badge logo, script heading.
Outputs output/certificate/: PNG (300 dpi), PDF, AI, EPS, SVG + zip."""
import math
import shutil
import subprocess
import zipfile

from common import C, OUTPUT, _launch, font_css, logo_img

GREEN, DEEP, GOLD, GOLD2, NAVY = C["green"], "#06291D", "#C9962B", "#F3D27A", "#0A1B25"
PX = 96
W, H = round(11.69 * PX), round(8.27 * PX)


def corner_waves(flip=False):
    tf = f" transform='translate({W} {H}) rotate(180)'" if flip else ""
    return f"""<svg style='position:absolute;left:0;top:0' width='{W}' height='{H}'><defs>
 <linearGradient id='g1{flip}' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#1FA36B'/><stop offset='.55' stop-color='{GREEN}'/><stop offset='1' stop-color='{DEEP}'/></linearGradient>
 <linearGradient id='g2{flip}' x1='0' y1='0' x2='1' y2='0'><stop offset='0' stop-color='#FFEBA8'/><stop offset='.45' stop-color='{GOLD2}'/><stop offset='.8' stop-color='{GOLD}'/><stop offset='1' stop-color='#FFE09A'/></linearGradient>
 <filter id='sh{flip}'><feDropShadow dx='3' dy='5' stdDeviation='6' flood-color='#00140C' flood-opacity='.35'/></filter></defs><g{tf}>
 <path d='M0 0 H{W * .46:.0f} C {W * .34:.0f} 40, {W * .2:.0f} 70, 0 {H * .34:.0f}Z' fill='#3CCB8F' opacity='.35'/>
 <path d='M0 0 H{W * .40:.0f} C {W * .29:.0f} 34, {W * .16:.0f} 58, 0 {H * .29:.0f}Z' fill='url(#g2{flip})' filter='url(#sh{flip})'/>
 <path d='M0 0 H{W * .36:.0f} C {W * .26:.0f} 26, {W * .13:.0f} 48, 0 {H * .25:.0f}Z' fill='url(#g1{flip})' filter='url(#sh{flip})'/>
 <path d='M{W * .34:.0f} 4 C {W * .24:.0f} 28, {W * .12:.0f} 46, 4 {H * .23:.0f}' stroke='#fff' stroke-width='1.5' fill='none' opacity='.35'/></g></svg>"""


def guilloche(x, y, w, h):
    s = ""
    for k in range(0, int(w), 14):
        s += f"<circle cx='{x + k}' cy='{y}' r='9' fill='none' stroke='{GOLD}' stroke-width='.8' opacity='.55'/>"
        s += f"<circle cx='{x + k}' cy='{y + h}' r='9' fill='none' stroke='{GOLD}' stroke-width='.8' opacity='.55'/>"
    return s


def seal(size=150):
    c, r = size / 2, size / 2
    pts = " ".join(f"{c + (r if i % 2 == 0 else r * .9) * math.cos(math.radians(i * 7.5)):.1f},{c + (r if i % 2 == 0 else r * .9) * math.sin(math.radians(i * 7.5)):.1f}" for i in range(48))
    return f"""<div style='position:relative;width:{size}px;height:{size + 70}px'>
 <svg width='{size}' height='{size + 70}' style='position:absolute;left:0;top:0'><defs>
  <radialGradient id='sg' cx='.35' cy='.3' r='.8'><stop offset='0' stop-color='#FFF2C2'/><stop offset='.5' stop-color='{GOLD2}'/><stop offset='1' stop-color='{GOLD}'/></radialGradient></defs>
  <path d='M{c - 40} {c} L{c - 58} {size + 66} L{c - 34} {size + 50} L{c - 14} {size + 68} L{c - 2} {c}Z' fill='{GREEN}'/>
  <path d='M{c + 40} {c} L{c + 58} {size + 66} L{c + 34} {size + 50} L{c + 14} {size + 68} L{c + 2} {c}Z' fill='{DEEP}'/>
  <polygon points='{pts}' fill='url(#sg)' stroke='{GOLD}' stroke-width='1'/>
  <circle cx='{c}' cy='{c}' r='{r * .72}' fill='none' stroke='#fff' stroke-width='2' stroke-dasharray='3 3'/></svg>
 <div style='position:absolute;left:0;top:0;width:{size}px;height:{size}px;display:flex;flex-direction:column;align-items:center;justify-content:center'>
  <div style='font:800 11px Archivo;color:{DEEP};letter-spacing:2px'>EMPLOYEE</div>
  <div style='font:400 26px Anton;color:{DEEP};line-height:1;letter-spacing:1px'>OF THE</div>
  <div style='font:400 26px Anton;color:{DEEP};line-height:1;letter-spacing:1px'>MONTH</div>
  <div style='font:800 9px Archivo;color:{DEEP};letter-spacing:2px;margin-top:3px'>★ ★ ★</div></div></div>"""


def sig(name, title):
    return (f"<div style='width:250px;text-align:center'><div style='height:46px'></div>"
            f"<div style='border-top:1.5px solid {NAVY};padding-top:6px;font:800 15px Archivo;color:{NAVY}'>{name}</div>"
            f"<div style='font:700 12.5px Archivo;color:{GREEN};letter-spacing:1px;margin-top:2px'>{title}</div></div>")


def page():
    return f"""<div style='position:relative;width:{W}px;height:{H}px;background:radial-gradient(circle at 50% 45%,#FFFFFF,#F6F3EA);overflow:hidden'>
{corner_waves()}{corner_waves(True)}
<div style='position:absolute;inset:26px;border:2.5px solid {GOLD};border-radius:6px'></div>
<div style='position:absolute;inset:34px;border:1px solid {GREEN}55;border-radius:4px'></div>
<svg style='position:absolute;left:0;top:0' width='{W}' height='{H}'>{guilloche(260, 48, W - 520, H - 96)}</svg>
<div style='position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);opacity:.05'>{logo_img('logo-badge', 'width:430px;height:430px')}</div>
<div style='position:absolute;left:0;right:0;top:62px;display:flex;flex-direction:column;align-items:center'>
 {logo_img('logo-badge', 'width:86px;height:86px')}
 <div style='font:400 17px Anton;color:{GREEN};letter-spacing:4px;margin-top:6px'>RS LINKS CONSULTANTS PVT. LTD.</div>
 <div style='font:700 48px Dancing;color:{NAVY};margin-top:6px;line-height:1'>Certificate of Excellence</div>
 <div style='display:flex;align-items:center;gap:14px;margin-top:10px'><span style='width:90px;height:2px;background:linear-gradient(90deg,transparent,{GOLD})'></span>
  <span style='font:400 30px Anton;color:{GOLD};letter-spacing:8px'>EMPLOYEE OF THE MONTH</span><span style='width:90px;height:2px;background:linear-gradient(90deg,{GOLD},transparent)'></span></div>
 <div style='font:600 15px Archivo;color:#5E6A64;letter-spacing:2px;margin-top:18px'>THIS CERTIFICATE IS PROUDLY PRESENTED TO</div>
 <div style='width:560px;border-bottom:2px solid {NAVY};height:58px;margin-top:6px'></div>
 <div style='font:600 15px Archivo;color:#4E5A54;margin-top:14px;text-align:center;line-height:1.55;width:700px'>
  In recognition of outstanding performance, dedication and commitment to excellence,<br>and for being an inspiration to the RS Links team.</div>
 <div style='display:flex;align-items:flex-end;gap:10px;margin-top:12px;font:700 15px Archivo;color:{NAVY}'>Month: <span style='display:inline-block;width:200px;border-bottom:1.5px solid {NAVY}'></span>
  &nbsp;&nbsp;Year: <span style='display:inline-block;width:110px;border-bottom:1.5px solid {NAVY}'></span></div></div>
<div style='position:absolute;left:120px;right:120px;bottom:70px;display:flex;justify-content:space-between;align-items:flex-end'>
 {sig('Rahim Ullah', 'CO-FOUNDER &amp; CEO')}<div style='margin-bottom:-26px'>{seal()}</div>{sig('Saad Khalid', 'CO-FOUNDER &amp; COO')}</div></div>"""


def main():
    from playwright.sync_api import sync_playwright
    out = OUTPUT / "certificate"
    out.mkdir(parents=True, exist_ok=True)
    f = OUTPUT / ".tmp" / "certificate.html"
    f.parent.mkdir(exist_ok=True)
    f.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{font_css()}@page{{size:11.69in 8.27in;margin:0}}"
                 f"html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden}}</style></head><body>{page()}</body></html>", encoding="utf-8")
    stem = out / "RS-Links-Employee-of-the-Month-Certificate-A4"
    with sync_playwright() as pw:
        b = _launch(pw)
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=300 / PX)
        pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500)
        pg.screenshot(path=str(stem) + ".png")
        pg.pdf(path=str(stem) + ".pdf", width="11.69in", height="8.27in", print_background=True)
        b.close()
    subprocess.run(["pdftocairo", "-svg", str(stem) + ".pdf", str(stem) + ".svg"], check=True)
    subprocess.run(["pdftocairo", "-eps", str(stem) + ".pdf", str(stem) + ".eps"], check=True)
    shutil.copy(str(stem) + ".pdf", str(stem) + ".ai")
    with zipfile.ZipFile(out / "RS-Links-Employee-of-the-Month-Certificate-Print-Files.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for ext in ("pdf", "ai", "eps", "svg", "png"):
            z.write(str(stem) + "." + ext, stem.name + "." + ext)
    print(stem)


if __name__ == "__main__":
    main()
