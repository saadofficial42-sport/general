"""Shared building blocks for RS Links ad generators.

Every style script builds a full HTML page on a fixed 1080x1350 canvas and
calls `render()` to turn it into a PNG with Playwright (Chromium).
"""
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
LOGO = ROOT / "assets" / "logo"
PHOTOS = ROOT / "assets" / "photos"
OUTPUT = ROOT / "output"

W, H = 1080, 1350
WHATSAPP = "+92 371 9051589"
WHATSAPP_LINK = "923719051589"

C = {
    "green": "#0C4A34",
    "emerald": "#2DB077",
    "emerald2": "#1E9E4A",
    "gold": "#F0B443",
    "gold2": "#FFD23F",
    "navy": "#0D2D63",
    "navy2": "#10212E",
    "offwhite": "#F9F8F4",
    "red": "#E53935",
    "wa": "#25D366",
}


def font_css():
    """@font-face rules pointing at the local TTFs, plus base classes."""
    faces = [
        ("Nastaliq", "NotoNastaliqUrdu.ttf", "400 700"),
        ("Anton", "Anton-Regular.ttf", "400"),
        ("Archivo", "Archivo.ttf", "100 900"),
        ("PlexMono", "IBMPlexMono-Bold.ttf", "700"),
        ("Dancing", "DancingScript.ttf", "400 700"),
    ]
    css = "".join(
        f"@font-face{{font-family:'{n}';src:url('{(FONTS / f).as_uri()}');font-weight:{w};}}"
        for n, f, w in faces
    )
    return css + """
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:1080px;height:1350px;overflow:hidden;}
.canvas{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Archivo',sans-serif;}
.abs{position:absolute;}
.anton{font-family:'Anton',sans-serif;letter-spacing:.5px;}
.mono{font-family:'PlexMono',monospace;font-weight:700;letter-spacing:3px;}
.script{font-family:'Dancing',cursive;font-weight:700;}
.ur{font-family:'Nastaliq',serif;line-height:1.8;direction:rtl;}
.ltr{direction:ltr;unicode-bidi:isolate;display:inline-block;}
"""


def page(body, extra_css="", rtl=False):
    d = "rtl" if rtl else "ltr"
    lang = "ur" if rtl else "en"
    return (f"<!doctype html><html lang='{lang}' dir='{d}'><head><meta charset='utf-8'>"
            f"<style>{font_css()}{extra_css}</style></head>"
            f"<body><div class='canvas'>{body}</div></body></html>")


def _launch(p):
    """Launch Chromium; prefer the pre-installed build if present."""
    exe = Path("/opt/pw-browsers/chromium")
    if exe.exists():
        return p.chromium.launch(executable_path=str(exe))
    return p.chromium.launch()


def render(html, out_name):
    """Render an HTML string to output/<out_name> at exactly 1080x1350."""
    from playwright.sync_api import sync_playwright
    OUTPUT.mkdir(exist_ok=True)
    tmp = OUTPUT / ".tmp" / (Path(out_name).stem + ".html")
    tmp.parent.mkdir(exist_ok=True)
    tmp.write_text(html, encoding="utf-8")
    out = OUTPUT / out_name
    with sync_playwright() as p:
        b = _launch(p)
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg.goto(tmp.as_uri())
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(300)
        pg.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": W, "height": H})
        b.close()
    return out


def overflow_report(html):
    """Return elements whose content overflows their box (clipping check)."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = _launch(p)
        pg = b.new_page(viewport={"width": W, "height": H})
        tmp = OUTPUT / ".tmp" / "_check.html"
        tmp.parent.mkdir(parents=True, exist_ok=True)
        tmp.write_text(html, encoding="utf-8")
        pg.goto(tmp.as_uri())  # file:// so the local fonts load
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(300)
        res = pg.evaluate("""() => [...document.querySelectorAll('[data-check]')]
            .filter(e => e.scrollWidth > e.clientWidth + 1 || e.scrollHeight > e.clientHeight + 1)
            .map(e => e.dataset.check)""")
        b.close()
    return res


# ---------------------------------------------------------------- logos

def ensure_logos():
    """Derive any missing logo variant from the ones present.

    Returns a dict of variant -> file URI (None if it can't be derived).
    """
    from PIL import Image, ImageDraw
    names = ["logo-stacked", "logo-horizontal-light", "logo-horizontal-dark", "logo-badge"]
    paths = {n: LOGO / f"{n}.png" for n in names}
    have = [n for n in names if paths[n].exists()]
    if have and not paths["logo-badge"].exists():
        # Cut the round badge out of the stacked logo (top, centred) or the
        # horizontal one (left, full height) with a circular transparent mask.
        src = "logo-stacked" if "logo-stacked" in have else have[0]
        im = Image.open(paths[src]).convert("RGBA")
        w, h = im.size
        if src == "logo-stacked":
            d = int(min(w, h * 0.62))
            box = ((w - d) // 2, 0, (w - d) // 2 + d, d)
        else:
            d = h
            box = (0, 0, d, d)
        crop = im.crop(box)
        mask = Image.new("L", crop.size, 0)
        ImageDraw.Draw(mask).ellipse((0, 0, d - 1, d - 1), fill=255)
        crop.putalpha(mask)
        crop.save(paths["logo-badge"])
    if paths["logo-horizontal-light"].exists() and not paths["logo-horizontal-dark"].exists():
        im = Image.open(paths["logo-horizontal-light"]).convert("RGBA")
        bg = Image.new("RGBA", (im.width + 80, im.height + 60), "#0A1B25")
        bg.alpha_composite(im, (40, 30))
        bg.save(paths["logo-horizontal-dark"])
    return {n: (paths[n].as_uri() if paths[n].exists() else None) for n in names}


def _trimmed(variant):
    """Copy of a logo with its transparent padding removed (cached)."""
    from PIL import Image
    src = LOGO / f"{variant}.png"
    out = LOGO / ".cache" / f"{variant}.png"
    if not src.exists():
        return None
    if not out.exists() or out.stat().st_mtime < src.stat().st_mtime:
        out.parent.mkdir(exist_ok=True)
        im = Image.open(src).convert("RGBA")
        bb = im.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
        im.crop(bb).save(out)
    return out.as_uri()


def logo_img(variant="logo-stacked", style=""):
    """<img> of a logo variant (padding trimmed). Variants: logo-stacked,
    logo-horizontal-light, logo-horizontal-dark (navy plate),
    logo-horizontal-dark-transparent (white text, for dark backgrounds),
    logo-badge."""
    ensure_logos()
    uri = _trimmed(variant) or _trimmed("logo-stacked")
    if uri:
        return f"<img src='{uri}' style='display:block;object-fit:contain;{style}'>"
    # Placeholder wordmark until the real logo files are added.
    return (f"<div style='{style};display:flex;flex-direction:column;align-items:center;justify-content:center;"
            f"color:{C['green']};text-align:center'><div class='anton' style='font-size:64px;line-height:1'>RS Links</div>"
            f"<div class='mono' style='font-size:18px;color:{C['navy']}'>CONSULTANTS PVT. LTD.</div></div>")


# ---------------------------------------------------------------- icons

def whatsapp_icon(size=64, bg=C["wa"], fg="#fff"):
    return f"""<svg width="{size}" height="{size}" viewBox="0 0 64 64">
<path fill="{bg}" d="M32 3C16 3 3 15.7 3 31.4c0 5.4 1.6 10.5 4.3 14.8L4 61l15.3-4c4 2.2 8.2 3.3 12.7 3.3 16 0 29-12.7 29-28.4S48 3 32 3z"/>
<path fill="{fg}" d="M24.3 18.6c-.6-1.3-1.2-1.3-1.8-1.3h-1.5c-.5 0-1.4.2-2.1 1-.7.8-2.8 2.7-2.8 6.6s2.8 7.7 3.2 8.2c.4.5 5.5 8.7 13.6 11.9 6.7 2.6 8.1 2.1 9.5 2 1.5-.1 4.7-1.9 5.3-3.8.7-1.9.7-3.5.5-3.8-.2-.3-.7-.5-1.5-.9s-4.7-2.3-5.4-2.6c-.7-.3-1.3-.4-1.8.4-.5.8-2.1 2.6-2.5 3.1-.5.5-.9.6-1.7.2-.8-.4-3.4-1.2-6.4-3.9-2.4-2.1-4-4.7-4.4-5.5-.5-.8 0-1.2.4-1.6.4-.4.8-.9 1.2-1.4.4-.5.5-.8.8-1.3.3-.5.1-1-.1-1.4-.2-.4-1.7-4.4-2.4-5.9z"/>
</svg>"""


ICONS = {
    # 24x24 stroke icons, drawn in currentColor
    "money": '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="3"/><path d="M6 12h.01M18 12h.01"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "home": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
    "food": '<path d="M7 3v8M5 3v4a2 2 0 0 0 4 0V3M7 11v10"/><path d="M17 3c-2 0-3 2-3 5s1 4 3 4v9"/>',
    "bus": '<rect x="4" y="3" width="16" height="14" rx="2"/><path d="M4 10h16M8 21v-4M16 21v-4"/><circle cx="8" cy="14" r=".5"/><circle cx="16" cy="14" r=".5"/>',
    "medical": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M12 8v8M8 12h8"/>',
    "plane": '<path d="M2 16l20-6-3-3-7 3-5-5-2 1 3 6-4 2-2-1-1 1 3 3z"/>',
    "doc": '<path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h8"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-7 8-7s8 3 8 7"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "pin": '<path d="M12 22s7-7 7-12a7 7 0 0 0-14 0c0 5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
    "check": '<path d="M5 12l5 5 9-10"/>',
    "overtime": '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l3 2M9 2h6"/>',
    "visa": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="11" r="2.5"/><path d="M6 17c1-2 5-2 6 0M14 9h4M14 13h4"/>',
    "video": '<rect x="2" y="6" width="14" height="12" rx="2"/><path d="M16 10l6-3v10l-6-3z"/>',
    "idcard": '<rect x="2" y="5" width="20" height="14" rx="2"/><circle cx="8" cy="11" r="2"/><path d="M5 16c.6-1.6 5.4-1.6 6 0M14 10h5M14 14h4"/>',
    "shield": '<path d="M12 2l8 3v6c0 5-3.5 9-8 11-4.5-2-8-6-8-11V5z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "camera": '<path d="M3 8h4l2-3h6l2 3h4v12H3z"/><circle cx="12" cy="13" r="4"/>',
    "family": '<circle cx="8" cy="7" r="3"/><circle cx="17" cy="9" r="2.4"/><path d="M2 21c0-4 3-6.5 6-6.5s6 2.5 6 6.5M13 21c.3-3 2-4.6 4-4.6s3.8 1.6 4 4.6"/>',
    "scissors": '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M8.1 8.1L20 20M8.1 15.9L20 4"/>',
    "box": '<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/>',
    "iron": '<path d="M3 17h17v-3a6 6 0 0 0-6-6H8"/><path d="M3 17l2-6h9"/><path d="M8 8V6h7"/>',
    "sock": '<path d="M8 2h7v10l-6 7a3 3 0 0 1-5-3l4-5z"/><path d="M8 6h7"/>',
    "dolly": '<path d="M4 3h3l3 13h10"/><rect x="10" y="6" width="9" height="7" rx="1"/><circle cx="10" cy="19" r="2"/><circle cx="19" cy="19" r="2"/>',
    "gift": '<rect x="3" y="9" width="18" height="12" rx="1"/><path d="M3 13h18M12 9v12"/><path d="M12 9c-2-4-6-4-6-1s6 1 6 1zm0 0c2-4 6-4 6-1s-6 1-6 1z"/>',
    "truck": '<rect x="1" y="6" width="13" height="10" rx="1"/><path d="M14 9h4l3 4v3h-7z"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    "crane": '<path d="M5 21V3h2v18M5 4h15M7 7l4-3M17 4v6"/><rect x="14" y="10" width="6" height="4"/><path d="M3 21h8"/>',
    "mop": '<path d="M14 3l-4 12"/><path d="M6 15h8l2 6H4z"/><path d="M7 18v3M10 18v3M13 18v3"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>',
    "male": '<circle cx="10" cy="14" r="5"/><path d="M14 10l6-6M15 4h5v5"/>',
    "megaphone": '<path d="M3 10v4h4l8 5V5L7 10z"/><path d="M18 9a4 4 0 0 1 0 6"/>',
}


def icon(name, size=40, color="#fff", stroke=2.2):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>')


# ---------------------------------------------------------------- flags

def _star_points(cx, cy, r, n=5, inner=0.382, rot=-90):
    pts = []
    for i in range(n * 2):
        rr = r if i % 2 == 0 else r * inner
        a = math.radians(rot + i * 180 / n)
        pts.append(f"{cx + rr * math.cos(a):.2f},{cy + rr * math.sin(a):.2f}")
    return " ".join(pts)


def flag_pakistan(uid="pk"):
    """Pakistan flag, 3:2, per official spec (viewBox 900x600)."""
    # White hoist = 1/4 width. Crescent and star centred in the green field.
    return f"""<rect width="900" height="600" fill="#fff"/>
<rect x="225" width="675" height="600" fill="#01411C"/>
<g transform="rotate(-45 562.5 300)">
  <circle cx="562.5" cy="300" r="180" fill="#fff"/>
  <circle cx="610" cy="300" r="165" fill="#01411C"/>
  <polygon fill="#fff" points="{_star_points(720, 300, 60, rot=0)}"/>
</g>"""


def flag_uzbekistan(uid="uz"):
    """Uzbekistan flag, 2:1 (viewBox 500x250). Bands blue/red/white/red/green
    in ratio 10:1:10:1:10; white crescent + 12 stars (rows of 3, 4, 5,
    right-aligned) in the blue band at the hoist."""
    u = 250 / 32
    stars = []
    for row, start in enumerate((2, 1, 0)):
        for col in range(start, 5):
            cx, cy = 118 + col * 25, 15 + row * 24
            stars.append(f'<polygon fill="#fff" points="{_star_points(cx, cy, 9)}"/>')
    return f"""<rect width="500" height="250" fill="#1EB53A"/>
<rect width="500" height="{21*u:.2f}" fill="#fff"/>
<rect width="500" height="{10*u:.2f}" fill="#0099B5"/>
<rect y="{10*u:.2f}" width="500" height="{u:.2f}" fill="#CE1126"/>
<rect y="{21*u:.2f}" width="500" height="{u:.2f}" fill="#CE1126"/>
<circle cx="58" cy="39" r="29" fill="#fff"/>
<circle cx="70" cy="39" r="27" fill="#0099B5"/>
{''.join(stars)}"""


def flag_kyrgyzstan(uid="kg"):
    """Kyrgyzstan flag (2023 law), 3:5 (viewBox 500x300). Red field; yellow
    sun with 40 straight rays. Ray disc diameter = 3/5 flag height; sun disc
    = 3/5 of ray disc; tunduk (red ring with two crossing sets of 4 laths)
    diameter = 1/2 of ray disc."""
    cx, cy = 250, 150
    R = 300 * 3 / 5 / 2          # ray disc radius = 90
    r = R * 3 / 5                # sun disc radius = 54
    t = R / 2                    # tunduk radius = 45
    rays = []
    for i in range(40):
        a = math.radians(i * 9 - 90)
        da = math.radians(4.2)
        p1 = (cx + r * 0.92 * math.cos(a - da), cy + r * 0.92 * math.sin(a - da))
        p2 = (cx + R * math.cos(a), cy + R * math.sin(a))
        p3 = (cx + r * 0.92 * math.cos(a + da), cy + r * 0.92 * math.sin(a + da))
        rays.append(f"{p1[0]:.2f},{p1[1]:.2f} {p2[0]:.2f},{p2[1]:.2f} {p3[0]:.2f},{p3[1]:.2f}")
    tr = t - 4  # inner radius of ring stroke
    laths = []
    for d in (-24, -8, 8, 24):
        x = math.sqrt(max(tr * tr - d * d, 0))
        # horizontal set bowing toward the centre, vertical set the same, rotated
        laths.append(f'<path d="M{cx - x:.2f} {cy + d} Q{cx} {cy + d * 0.35:.2f} {cx + x:.2f} {cy + d}"/>')
        laths.append(f'<path d="M{cx + d} {cy - x:.2f} Q{cx + d * 0.35:.2f} {cy} {cx + d} {cy + x:.2f}"/>')
    return f"""<rect width="500" height="300" fill="#E8112D"/>
{''.join(f'<polygon fill="#FFEF00" points="{p}"/>' for p in rays)}
<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFEF00"/>
<clipPath id="{uid}tc"><circle cx="{cx}" cy="{cy}" r="{tr}"/></clipPath>
<g clip-path="url(#{uid}tc)" stroke="#E8112D" stroke-width="5" fill="none">{''.join(laths)}</g>
<circle cx="{cx}" cy="{cy}" r="{t - 4}" fill="none" stroke="#E8112D" stroke-width="8"/>"""


def _flag_file(code):
    """Flag body from assets/flags/<code>.svg (inner markup of the <svg>)."""
    import re
    raw = (ROOT / "assets" / "flags" / f"{code}.svg").read_text()
    return lambda uid=None: re.sub(r"^.*?<svg[^>]*>|</svg>\s*$", "", raw, flags=re.S)


FLAGS = {
    "pakistan": (flag_pakistan, 900, 600),
    "uzbekistan": (flag_uzbekistan, 500, 250),
    "kyrgyzstan": (flag_kyrgyzstan, 500, 300),
    # Kosovo: blue field, gold map, six white stars; official ratio 1:1.4
    "kosovo": (_flag_file("xk"), 840, 600),
}


def flag(country, width=180, wave=True, uid=None):
    """Flag as inline SVG. `wave=True` adds a waving shading overlay."""
    fn, vw, vh = FLAGS[country.lower()]
    uid = uid or f"f{country[:2]}{width}"
    height = round(width * vh / vw)
    body = fn(uid)
    if not wave:
        return f'<svg width="{width}" height="{height}" viewBox="0 0 {vw} {vh}">{body}</svg>'
    # Wave: one feDisplacementMap that shifts pixels vertically only (the G
    # channel of a generated sine map), plus a light/shadow overlay that
    # follows the same folds. Both use the same wave function.
    amp = vh * 0.05
    k = 2.4 * math.pi

    def wy(t):  # vertical offset at fraction t of the width
        return amp * math.sin(t * k + 0.6) * (0.35 + 0.65 * t)

    N = 48
    gstops = "".join(
        f"<stop offset='{i/N:.4f}' stop-color='rgb(128,{round(128 + 127 * wy(i/N) / amp)},128)'/>"
        for i in range(N + 1))
    from urllib.parse import quote
    mapsvg = (f"<svg xmlns='http://www.w3.org/2000/svg' width='{vw}' height='{vh}'><defs>"
              f"<linearGradient id='g'>{gstops}</linearGradient></defs>"
              f"<rect width='{vw}' height='{vh}' fill='url(#g)'/></svg>")
    sstops = "".join(
        f'<stop offset="{i/40:.3f}" stop-color="{"#fff" if math.cos(i/40*k+0.6) > 0 else "#000"}" '
        f'stop-opacity="{0.22*abs(math.cos(i/40*k+0.6)):.3f}"/>' for i in range(41))
    pad = amp * 1.3
    return f"""<svg width="{width}" height="{round(height*(1+2*pad/vh))}" viewBox="0 {-pad:.1f} {vw} {vh+2*pad:.1f}">
<defs>
 <linearGradient id="{uid}s" x1="0" x2="1">{sstops}</linearGradient>
 <filter id="{uid}w" filterUnits="userSpaceOnUse" primitiveUnits="userSpaceOnUse" x="0" y="{-pad:.1f}" width="{vw}" height="{vh+2*pad:.1f}" color-interpolation-filters="sRGB">
  <feImage href="data:image/svg+xml,{quote(mapsvg)}" x="0" y="{-pad:.1f}" width="{vw}" height="{vh+2*pad:.1f}" preserveAspectRatio="none" result="m"/>
  <feDisplacementMap in="SourceGraphic" in2="m" scale="{-2*amp:.2f}" xChannelSelector="R" yChannelSelector="G"/>
 </filter>
</defs>
<g filter="url(#{uid}w)">{body}<rect width="{vw}" height="{vh}" fill="url(#{uid}s)"/></g>
</svg>"""
