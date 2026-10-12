"""RS Links office gate banners (print).

Three pieces:
  top   — circular badge | horizontal logo | circular badge, tagline, official email
  left  — logo, destination-country flags (GCC / Asia / Europe), contacts
  right — logo, services list, contacts

Each is rendered as a print PDF at its physical size (vector text and flags) and a
high-resolution PNG preview into output/banners/.
"""
from pathlib import Path

from common import C, OUTPUT, ROOT, WHATSAPP, font_css, icon, logo_img, whatsapp_icon
from common import _launch

PHONE2 = "+92 317 0363690"
EMAIL = "hr@rslinksconsultants.com"
WEBSITE = "www.rslinksconsultants.com"
TAGLINE_EN = "Turning Your Dreams into Reality"
TAGLINE_UR = "آپ کے خوابوں کو حقیقت بنانے میں ہمارا ساتھ"
GREEN, GOLD, NAVY = C["green"], C["gold"], "#0A1B25"
FLAGS = ROOT / "assets" / "flags"

# Physical sizes in inches (width, height). CSS px are laid out at 48 px per inch.
SIZES = {"top": (120, 36), "left": (36, 96), "right": (36, 96)}  # 10x3 ft, 3x8 ft
PPI = 48

REGIONS = [
    ("GCC", [("sa", "Saudi Arabia"), ("ae", "UAE"), ("qa", "Qatar"),
             ("kw", "Kuwait"), ("om", "Oman"), ("bh", "Bahrain")]),
    ("ASIA", [("uz", "Uzbekistan"), ("kg", "Kyrgyzstan"), ("kz", "Kazakhstan"),
              ("my", "Malaysia"), ("jp", "Japan"), ("kr", "South Korea")]),
    ("EUROPE", [("rs", "Serbia"), ("xk", "Kosovo"), ("ro", "Romania"),
                ("pl", "Poland"), ("hr", "Croatia"), ("de", "Germany")]),
]

SERVICES = [
    ("user", "Manpower Recruitment"),
    ("shield", "HR Consultancy"),
    ("doc", "Student Consultancy"),
    ("money", "Tax Consultancy"),
    ("chat", "Career Advisory"),
    ("megaphone", "Marketing Support"),
    ("gear", "Website Development Support"),
    ("visa", "Visa &amp; Documentation Assistance"),
    ("check", "Trade Testing &amp; Skill Assessment"),
    ("calendar", "Interview &amp; Selection Arrangement"),
    ("plane", "Travel &amp; Ticketing Assistance"),
    ("idcard", "Document Attestation Support"),
    ("box", "Corporate Staffing Solutions"),
    ("pin", "Pre-Departure Orientation"),
]

BASE_CSS = f"""
{font_css()}
html,body{{margin:0;padding:0}}
.b{{position:relative;overflow:hidden;background:#FFFFFF;font-family:'Archivo',sans-serif;color:{NAVY}}}
.ic{{border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none}}
"""


def frame(w, h):
    """Gold inner keyline + green edge bands."""
    return (f"<div style='position:absolute;inset:0;border:{h*0.018 if w > h else w*0.03:.0f}px solid {GREEN}'></div>"
            f"<div style='position:absolute;inset:{(h*0.03 if w > h else w*0.045):.0f}px;border:3px solid {GOLD};border-radius:10px'></div>")


def contacts(w, size):
    row = lambda ic, txt, mono=False: (
        f"<div style='display:flex;align-items:center;gap:{size*0.5:.0f}px'>{ic}"
        f"<div style='font-family:{'Anton' if mono else 'Archivo'};font-weight:800;font-size:{size}px;color:#fff;letter-spacing:.5px'>{txt}</div></div>")
    wa = whatsapp_icon(size * 1.5)
    circ = lambda name: f"<div class='ic' style='width:{size*1.5:.0f}px;height:{size*1.5:.0f}px;background:{GOLD}'>{icon(name, size*0.85, NAVY, 2.4)}</div>"
    return (f"<div style='background:{GREEN};border-radius:18px;padding:{size*0.9:.0f}px {size:.0f}px;display:flex;flex-direction:column;gap:{size*0.55:.0f}px;"
            f"box-shadow:0 6px 18px #0003'>"
            f"{row(wa, WHATSAPP, True)}{row(wa, PHONE2, True)}"
            f"{row(circ('mail'), EMAIL)}{row(circ('pin'), WEBSITE)}</div>")


def top_banner():
    w, h = (v * PPI for v in SIZES["top"])
    badge = logo_img("logo-badge", f"width:{h*0.66:.0f}px;height:{h*0.66:.0f}px")
    body = f"""{frame(w, h)}
<div style='position:absolute;left:{w*0.05:.0f}px;top:{h*0.17:.0f}px'>{badge}</div>
<div style='position:absolute;right:{w*0.05:.0f}px;top:{h*0.17:.0f}px'>{badge}</div>
<div style='position:absolute;left:0;right:0;top:{h*0.08:.0f}px;display:flex;flex-direction:column;align-items:center'>
  {logo_img('logo-horizontal-light', f'width:{w*0.42:.0f}px;height:{h*0.45:.0f}px')}
  <div style='width:{w*0.42:.0f}px;height:4px;background:linear-gradient(90deg,transparent,{GOLD},transparent);margin:{h*0.015:.0f}px 0'></div>
  <div style='font-family:Dancing;font-weight:700;font-size:{h*0.11:.0f}px;color:{GREEN};line-height:1.1'>{TAGLINE_EN}</div>
  <div style='font-family:Nastaliq;font-size:{h*0.06:.0f}px;color:{NAVY};line-height:1.7;direction:rtl'>{TAGLINE_UR}</div>
  <div style='display:flex;align-items:center;gap:14px;background:{GREEN};border-radius:999px;padding:{h*0.012:.0f}px {h*0.06:.0f}px;margin-top:{h*0.005:.0f}px'>
    <div class='ic' style='width:{h*0.075:.0f}px;height:{h*0.075:.0f}px;background:{GOLD}'>{icon('mail', h*0.045, NAVY, 2.4)}</div>
    <div style='font-weight:800;font-size:{h*0.058:.0f}px;color:#fff'>{EMAIL}</div></div>
</div>"""
    return w, h, body


def side_header(w, h, title):
    return (f"<div style='display:flex;flex-direction:column;align-items:center;padding-top:{h*0.04:.0f}px'>"
            f"{logo_img('logo-stacked', f'width:{w*0.4:.0f}px;height:{w*0.4:.0f}px')}"
            f"<div style='margin-top:{h*0.008:.0f}px;background:{GREEN};color:#fff;border-radius:999px;padding:{w*0.012:.0f}px {w*0.06:.0f}px;"
            f"font-family:Anton;font-size:{w*0.058:.0f}px;letter-spacing:1px;white-space:nowrap'>{title}</div></div>")


def left_banner():
    w, h = (v * PPI for v in SIZES["left"])
    blocks = ""
    for region, items in REGIONS:
        cells = "".join(
            f"<div style='width:{w*0.18:.0f}px;display:flex;flex-direction:column;align-items:center;gap:6px'>"
            f"<div style='width:100%;aspect-ratio:3/2;background:#fff;border-radius:8px;box-shadow:0 3px 10px #0003;"
            f"display:flex;align-items:center;justify-content:center;overflow:hidden'>"
            f"<img src='{(FLAGS / (code + '.svg')).as_uri()}' style='width:100%;height:100%;object-fit:cover'></div>"
            f"<div style='font-weight:800;font-size:{w*0.034:.0f}px;text-align:center;line-height:1.1;white-space:nowrap'>{name}</div></div>"
            for code, name in items)
        blocks += (f"<div style='margin-top:{h*0.01:.0f}px'><div style='display:flex;align-items:center;gap:12px;margin-bottom:{h*0.008:.0f}px'>"
                   f"<div style='flex:1;height:3px;background:{GOLD}'></div>"
                   f"<div style='font-family:Anton;font-size:{w*0.065:.0f}px;color:{GREEN};letter-spacing:2px'>{region}</div>"
                   f"<div style='flex:1;height:3px;background:{GOLD}'></div></div>"
                   f"<div style='display:flex;flex-wrap:wrap;justify-content:center;gap:{w*0.015:.0f}px {w*0.08:.0f}px'>{cells}</div></div>")
    body = (f"{frame(w, h)}<div style='position:absolute;inset:{w*0.07:.0f}px;display:flex;flex-direction:column'>"
            f"{side_header(w, h, 'WE CONNECT YOU WORLDWIDE')}"
            f"<div style='padding:0 {w*0.01:.0f}px'>{blocks}</div>"
            f"<div style='margin-top:auto'>{contacts(w, w*0.043)}</div></div>")
    return w, h, body


def right_banner():
    w, h = (v * PPI for v in SIZES["right"])
    items = "".join(
        f"<div style='display:flex;align-items:center;gap:{w*0.035:.0f}px;padding:{h*0.0026:.0f}px 0;border-bottom:2px dashed #D9E2DC'>"
        f"<div class='ic' style='width:{w*0.085:.0f}px;height:{w*0.085:.0f}px;background:{GREEN}'>{icon(ic, w*0.048, '#fff', 2.2)}</div>"
        f"<div style='font-weight:800;font-size:{w*0.044:.0f}px;line-height:1.12'>{name}</div></div>"
        for ic, name in SERVICES)
    body = (f"{frame(w, h)}<div style='position:absolute;inset:{w*0.07:.0f}px;display:flex;flex-direction:column'>"
            f"{side_header(w, h, 'OUR SERVICES')}"
            f"<div style='margin-top:{h*0.01:.0f}px;padding:0 {w*0.02:.0f}px'>{items}</div>"
            f"<div style='margin-top:auto'>{contacts(w, w*0.043)}</div></div>")
    return w, h, body


def render(name, build):
    from playwright.sync_api import sync_playwright
    w, h, body = build()
    out = OUTPUT / "banners"
    out.mkdir(parents=True, exist_ok=True)
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{BASE_CSS}html,body{{width:{w}px;height:{h}px;overflow:hidden}}@page{{size:{w}px {h}px;margin:0}}</style></head>"
            f"<body><div class='b' style='width:{w}px;height:{h}px'>{body}</div></body></html>")
    tmp = OUTPUT / ".tmp" / f"banner-{name}.html"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(html, encoding="utf-8")
    with sync_playwright() as pw:
        b = _launch(pw)
        pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
        pg.goto(tmp.as_uri())
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(400)
        pg.screenshot(path=str(out / f"RS-Links-Gate-Banner-{name}.png"))
        pg.pdf(path=str(out / f"RS-Links-Gate-Banner-{name}.pdf"), width=f"{w}px", height=f"{h}px", print_background=True)
        b.close()
    print(out / f"RS-Links-Gate-Banner-{name}.png")


if __name__ == "__main__":
    render("Top", top_banner)
    render("Left", left_banner)
    render("Right", right_banner)
