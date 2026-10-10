"""Rebrand partner (ME Career) Kuwait dermatology ads for RS Links — partnership confirmed by
the user 2026-10-10. Photos and layout are kept; only the partner's logo, email, website,
social handles and slogan are covered and replaced with RS Links branding + WhatsApp."""
from pathlib import Path

from common import C, WHATSAPP, font_css, logo_img, whatsapp_icon, OUTPUT
from common import _launch

SRC = Path(__file__).resolve().parent.parent / "demands" / "2026-10-10-kuwait-derma"
S = 1254
NAVY = "#03284F"


def patch(x, y, w, h, bg, inner="", radius=0, extra=""):
    return (f"<div style='position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};"
            f"border-radius:{radius}px;display:flex;align-items:center;justify-content:center;{extra}'>{inner}</div>")


def wa_pill(w, h, size=40, label=None):
    lab = (f"<div style='font-family:PlexMono;font-weight:700;letter-spacing:2px;font-size:{max(12, size*0.32):.0f}px;color:#128C4A'>{label}</div>"
           if label else "")
    return (f"<div style='display:flex;align-items:center;gap:12px;background:#fff;border-radius:999px;height:{h}px;width:{w}px;"
            f"justify-content:center;box-shadow:0 4px 12px #0003'>{whatsapp_icon(h - 14)}"
            f"<div>{lab}<div class='anton' style='font-size:{size}px;color:{C['navy2']};line-height:1.05'>{WHATSAPP}</div></div></div>")


def logo_plate(w, h):
    return logo_img("logo-horizontal-light", f"width:{w - 24}px;height:{h - 20}px")


def ad_dermatologist():
    p = []
    # partner logo + "People Matter" -> RS Links logo
    p.append(patch(22, 14, 400, 160, "#F6F6F6", logo_plate(400, 156)))
    # left part of the dark "send the following to" panel
    p.append(patch(42, 962, 392, 192, "linear-gradient(180deg,#02264E,#03284F)",
                   "<div style='text-align:center'>"
                   "<div style='font-family:Archivo;font-weight:800;font-size:19px;color:#fff;line-height:1.2'>INTERESTED CANDIDATES NEED TO</div>"
                   f"<div style='font-family:Archivo;font-weight:800;font-size:20px;color:#5FB2FF;line-height:1.3;margin-bottom:10px'>SEND THE FOLLOWING ON WHATSAPP</div>"
                   f"<div style='display:flex;justify-content:center'>{wa_pill(366, 64, 36)}</div>"
                   "<div style='font-family:Archivo;font-weight:600;font-size:17px;color:#fff;margin-top:10px'>"
                   "mentioning <span style='color:#5FB2FF'>(Dermatologist)</span></div></div>"))
    # footer: social handles, website, Arabic slogan
    p.append(patch(0, 1172, S, 82, "#F0F1F3",
                   "<div style='display:flex;align-items:center;gap:22px'>"
                   f"<div style='font-family:Anton;font-size:30px;color:{C['green']};letter-spacing:.5px'>RS LINKS CONSULTANTS PVT. LTD.</div>"
                   "<div style='width:2px;height:40px;background:#B9C2CC'></div>"
                   f"{whatsapp_icon(46)}<div class='anton' style='font-size:38px;color:{C['navy2']}'>{WHATSAPP}</div></div>"))
    return p


def ad_consultant():
    p = []
    p.append(patch(44, 16, 420, 160, "#FBFBFD", logo_plate(410, 150), 18, "box-shadow:0 4px 14px #0002"))
    # "How to Apply" intro lines inside the right card
    p.append(patch(926, 728, 296, 92, "linear-gradient(180deg,#132F57,#082D57)",
                   "<div style='font-family:Archivo;font-size:15.5px;line-height:1.35;color:#E8EEF7;width:280px'>"
                   "Interested candidates need to send the following on WhatsApp "
                   f"<b style='color:#5FB2FF;white-space:nowrap'>{WHATSAPP}</b> mentioning <b>(Dermatology Consultant)</b>.</div>"))
    # "Send your application to" box: replace email pill + subject line
    p.append(patch(190, 1060, 370, 98, "linear-gradient(180deg,#012B56,#012748)",
                   f"<div style='text-align:center'>{wa_pill(354, 56, 32)}"
                   "<div style='font-family:Archivo;font-size:15px;color:#fff;margin-top:6px'>Mention <b>(Dermatology Consultant)</b> in your message.</div></div>"))
    p.append(patch(190, 1024, 372, 36, "#012D58",
                   "<div style='font-family:Archivo;font-size:19px;color:#fff;width:360px'>Send your application on WhatsApp:</div>"))
    # envelope icon circle -> WhatsApp icon
    p.append(patch(74, 1028, 106, 106, "radial-gradient(circle,#0A4FA0,#012D58)", whatsapp_icon(78), 53,
                   "box-shadow:0 0 0 4px #1E6FCC66"))
    # website bottom-right
    p.append(patch(990, 1196, 250, 46, "#F1F0F5",
                   f"<div style='font-family:Anton;font-size:20px;color:{C['green']}'>RS LINKS CONSULTANTS</div>"))
    return p


def render(src, patches, out):
    from playwright.sync_api import sync_playwright
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{font_css()} html,body{{width:{S}px;height:{S}px;margin:0}}</style></head>"
            f"<body><div style='position:relative;width:{S}px;height:{S}px;background:url({(SRC / src).as_uri()}) 0 0/{S}px {S}px'>"
            f"{''.join(patches)}</div></body></html>")
    tmp = OUTPUT / ".tmp" / (Path(out).stem + ".html")
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(html, encoding="utf-8")
    with sync_playwright() as pw:
        b = _launch(pw)
        pg = b.new_page(viewport={"width": S, "height": S})
        pg.goto(tmp.as_uri())
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(300)
        pg.screenshot(path=str(OUTPUT / out))
        b.close()
    print(OUTPUT / out)


if __name__ == "__main__":
    render("src-dermatologist.jpg", ad_dermatologist(), "RS-Links-Kuwait-Dermatologist-English.png")
    render("src-consultant.jpg", ad_consultant(), "RS-Links-Kuwait-Dermatology-Consultant-English.png")
