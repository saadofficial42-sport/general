"""Nimra Khalid's business card in the purple logo theme (2026-10-29): same layout as business_cards.py, recoloured —
green -> dark purples, gold/yellow -> white (pearl where it sits on white, so it stays visible), round logo -> the
purple badge (output/logo-vector/RS-Links-Round-Logo-Purple_2000px.png). Outputs output/business-cards/
RS-Links-Business-Card-Nimra-Khalid-Purple-{Front,Back}.png + .pdf, and AI/EPS/SVG print files + zip."""
import shutil
import subprocess
import zipfile

import business_cards as bc
from common import C, OUTPUT, _launch, font_css

PURPLE_LOGO = (OUTPUT / "logo-vector" / "RS-Links-Round-Logo-Purple_2000px.png").as_uri()
GREEN_BADGE = "file:///" + str((OUTPUT.parent / "assets" / "logo" / ".cache" / "logo-badge.png")).lstrip("/")

SWAP = [  # (old, new) — order matters
    ("#22A86E", "#8E5CC9"), (C["green"], "#4A1D73"), ("#03231A", "#1E0838"), ("#1C8A5C", "#7442B0"),     # greens -> purples
    ("#7EE2B5", "#C9B3EC"), ("#1E9E66", "#7A4FB5"),                                                     # mint layer -> lavender
    ("#FFEBA8", "#FFFFFF"), (C["gold2"], "#F4EEFB"), ("#C98A1B", "#D9CCEE"), ("#FFE09A", "#FFFFFF"),   # gold -> pearl white
    (C["gold"], "#B79CDF"), ("#FFF6D6", "#FFFFFF"), ("#FFE7A0", "#FFFFFF"),                             # bars, highlights, tagline
    ("#A87508", "#5B2A86"), ("#DCEBE3", "#E9DDF7"), ("#EEF3EE", "#F3EEF9"), ("#F2F6F3", "#F4F0FA"),
    ("#00140C", "#14052A"),
]


def purple(html):
    html = html.replace(GREEN_BADGE, PURPLE_LOGO)
    for a, b in SWAP:
        html = html.replace(a, b).replace(a.lower(), b)
    return html


def main():
    from playwright.sync_api import sync_playwright
    p = next(x for x in bc.PEOPLE if x["slug"] == "Nimra-Khalid")
    out, vec = OUTPUT / "business-cards", OUTPUT / "for-printer" / "vector"
    vec.mkdir(parents=True, exist_ok=True)
    stem = "RS-Links-Business-Card-Nimra-Khalid-Purple"
    sides = {"Front": purple(bc.front(p)), "Back": purple(bc.back())}
    with sync_playwright() as pw:
        b = _launch(pw)
        for side, body in sides.items():
            f = OUTPUT / ".tmp" / f"purple-{side}.html"
            f.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{bc.CSS}@page{{size:{bc.W}in {bc.H}in;margin:0}}</style></head><body>{body}</body></html>", encoding="utf-8")
            pg = b.new_page(viewport={"width": bc.PX_W, "height": bc.PX_H}, device_scale_factor=600 / bc.PPI)
            pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
            pg.screenshot(path=str(out / f"{stem}-{side}.png"))
            pdf = vec / f"{stem}-{side}.pdf"
            pg.pdf(path=str(pdf), width=f"{bc.W}in", height=f"{bc.H}in", print_background=True)
            pg.close()
            subprocess.run(["pdftocairo", "-svg", str(pdf), str(vec / f"{stem}-{side}.svg")], check=True)
            subprocess.run(["pdftocairo", "-eps", str(pdf), str(vec / f"{stem}-{side}.eps")], check=True)
            shutil.move(pdf, vec / f"{stem}-{side}.ai")
        b.close()
    from PIL import Image
    pages = [Image.open(out / f"{stem}-{s}.png").convert("RGB") for s in ("Front", "Back")]
    pages[0].save(out / f"{stem}.pdf", "PDF", resolution=600.0, save_all=True, append_images=pages[1:])
    with zipfile.ZipFile(out / f"{stem}-Print-Files.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for s in ("Front", "Back"):
            for ext in ("ai", "eps", "svg"):
                z.write(vec / f"{stem}-{s}.{ext}", f"{stem}-{s}.{ext}")
        z.write(out / f"{stem}.pdf", f"{stem}.pdf")
    print(out / stem)


if __name__ == "__main__":
    main()
