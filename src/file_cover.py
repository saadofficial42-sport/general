"""RS Links file cover (2026-10-16, rev. 2): holds A4 sheets in bulk.
Panels 9.25 x 12.25 in (235 x 311 mm) + 0.5 in spine; front mostly white, back green.
Flat spread = back | spine | front (19 x 12.25 in) with 0.125 in bleed. Rendered at 96 css px/in x3 = 288 dpi; PDFs built from PNG."""
from common import C, OUTPUT, PHONES, font_css, icon, logo_img, _launch
from office_banners import ADDRESS, FLAGS, SERVICES, TAGLINE_EN, TAGLINE_UR, WEBSITE

GREEN, DEEP, GOLD, NAVY, CREAM = C["green"], "#06291D", C["gold2"], "#0A1B25", "#F7F3EA"
PX, SCALE, BLEED = 96, 3, 0.125
PANEL_W, PANEL_H, SPINE = 9.25, 12.25, 0.5   # holds A4 (8.27 x 11.69 in) with margin; 0.5 in spine for bulk
W, H = int((PANEL_W + 2 * BLEED) * PX), int((PANEL_H + 2 * BLEED) * PX)
SW = int(SPINE * PX)
EMAIL = "hr@rslinksconsultants.com"
FLAG_CODES = ["pk", "sa", "ae", "qa", "kw", "om", "bh", "uz", "kg", "kz", "my", "ro", "pl", "de", "xk", "rs", "it", "bg", "es", "lt", "cz", "md", "ba"]


def waves(w, h, uid):
    """Flowing gold/green ribbons that run across the spine, so the spread reads as one piece."""
    return (f"<svg style='position:absolute;left:0;top:0' width='{w}' height='{h}' viewBox='0 0 {w} {h}'>"
            f"<defs><linearGradient id='g{uid}' x1='0' y1='0' x2='1' y2='0'><stop offset='0' stop-color='{GOLD}'/><stop offset='1' stop-color='#C9922A'/></linearGradient></defs>"
            f"<path d='M0 {h*0.85} C {w*0.3} {h*0.80}, {w*0.6} {h*0.91}, {w} {h*0.85} L{w} {h} L0 {h}Z' fill='{DEEP}'/>"
            f"<path d='M0 {h*0.82} C {w*0.3} {h*0.77}, {w*0.6} {h*0.88}, {w} {h*0.82}' stroke='url(#g{uid})' stroke-width='10' fill='none'/>"
            f"<path d='M0 {h*0.837} C {w*0.3} {h*0.787}, {w*0.6} {h*0.897}, {w} {h*0.837}' stroke='{GREEN}' stroke-width='18' fill='none' opacity='.9'/>"
            f"</svg>")


def globe(cx, cy, r, color, op):
    lines = "".join(f"<ellipse cx='{cx}' cy='{cy}' rx='{r * k:.0f}' ry='{r}' fill='none' stroke='{color}' stroke-width='2'/>" for k in (1, .66, .33))
    lat = "".join(f"<path d='M{cx - r * (1 - t * t) ** .5:.0f} {cy + r * t:.0f} H{cx + r * (1 - t * t) ** .5:.0f}' stroke='{color}' stroke-width='2'/>" for t in (-.66, -.33, 0, .33, .66))
    return f"<g opacity='{op}'>{lines}{lat}<path d='M{cx} {cy - r} V{cy + r}' stroke='{color}' stroke-width='2'/></g>"


def front():
    svc = "".join(f"<div style='display:flex;align-items:center;gap:10px'><div style='width:40px;height:40px;border-radius:50%;background:{GREEN};display:flex;align-items:center;justify-content:center;flex:none'>"
                  f"{icon(ic, 22, '#fff', 2.3)}</div><span style='font-family:Archivo;font-weight:700;font-size:19px;color:{NAVY}'>{t}</span></div>"
                  for ic, t in SERVICES[:8])
    return f"""
<div style='position:absolute;inset:0;background:#fff'></div>
<svg style='position:absolute;left:0;top:0' width='{W}' height='{H}'>{globe(W*0.84, H*0.14, 250, GREEN, .05)}
 <path d='M{W} 0 L{W} {H*0.34} L{W*0.80} 0Z' fill='{GREEN}' opacity='.08'/></svg>
<div style='position:absolute;left:0;top:{H*0.08:.0f}px;width:16px;height:{H*0.26:.0f}px;background:{GREEN}'></div>
<div style='position:absolute;left:0;top:{H*0.34:.0f}px;width:16px;height:{H*0.06:.0f}px;background:{GOLD}'></div>
<div style='position:absolute;left:{W*0.09:.0f}px;top:{H*0.08:.0f}px'>
 {logo_img('logo-horizontal-light', f'width:{W*0.66:.0f}px;height:{W*0.66*0.25:.0f}px;object-position:left')}</div>
<div style='position:absolute;left:{W*0.09:.0f}px;top:{H*0.28:.0f}px;width:{W*0.82:.0f}px'>
 <div style='font-family:PlexMono;font-weight:700;font-size:19px;letter-spacing:4px;color:#A87508;white-space:nowrap'>RECRUITMENT · CONSULTANCY · VISA SERVICES</div>
 <div style='font-family:Anton;font-size:80px;line-height:1.02;color:{GREEN};margin-top:12px'>YOUR TRUSTED<br>CONSULTANCY <span style='color:{GOLD}'>PARTNER</span></div>
 <div style='font-family:Dancing;font-weight:700;font-size:46px;color:{NAVY};margin-top:10px'>{TAGLINE_EN}</div>
 <div style='width:160px;height:5px;background:{GOLD};border-radius:3px;margin-top:22px'></div>
 <div style='display:grid;grid-template-columns:1fr 1fr;gap:16px 26px;margin-top:28px'>{svc}</div></div>
<svg style='position:absolute;left:0;top:0' width='{W}' height='{H}'>
 <path d='M0 {H*0.90} C {W*0.3} {H*0.86}, {W*0.6} {H*0.95}, {W} {H*0.90} L{W} {H} L0 {H}Z' fill='{GREEN}'/>
 <path d='M0 {H*0.875} C {W*0.3} {H*0.835}, {W*0.6} {H*0.925}, {W} {H*0.875}' stroke='{GOLD}' stroke-width='8' fill='none'/></svg>
<div style='position:absolute;left:{W*0.09:.0f}px;right:{W*0.09:.0f}px;bottom:{H*0.022:.0f}px;display:flex;justify-content:space-between;align-items:center'>
 <div style='font-family:Nastaliq;font-size:24px;color:#fff;direction:rtl;line-height:1.8;white-space:nowrap'>{TAGLINE_UR}</div>
 <div style='font-family:Archivo;font-weight:800;font-size:20px;color:{GOLD}'>{WEBSITE}</div></div>"""


def back():
    flags = "".join(f"<img src='{(FLAGS / (c + '.svg')).as_uri()}' style='width:62px;height:42px;object-fit:cover;border-radius:5px;box-shadow:0 2px 6px #0003'>" for c in FLAG_CODES)
    row = lambda ic, t, sz=24, f="Archivo": (f"<div style='display:flex;align-items:center;gap:16px'><div style='width:54px;height:54px;border-radius:50%;background:{GREEN};display:flex;align-items:center;justify-content:center;flex:none'>"
                                            f"{icon(ic, 28, '#fff', 2.2)}</div><span style='font-family:{f};font-weight:700;font-size:{sz}px;color:{NAVY};line-height:1.25'>{t}</span></div>")
    nums = "<br>".join(PHONES)
    svc = "".join(f"<div style='font-family:Archivo;font-weight:700;font-size:18px;color:#fff;display:flex;align-items:center;gap:8px'>{icon('check', 18, GOLD, 3)}{t}</div>" for _, t in SERVICES[8:])
    return f"""
<div style='position:absolute;inset:0;background:linear-gradient(165deg,#0E5A3F 0%,{GREEN} 40%,{DEEP} 100%)'></div>
<svg style='position:absolute;left:0;top:0' width='{W}' height='{H}'>{globe(W*0.18, H*0.16, 220, '#ffffff', .07)}</svg>
<div style='position:absolute;left:{W*0.09:.0f}px;top:{H*0.05:.0f}px;width:{W*0.82:.0f}px'>
 <div style='font-family:Anton;font-size:52px;color:#fff;line-height:1'>WHERE WE CONNECT YOU</div>
 <div style='font-family:Archivo;font-weight:700;font-size:21px;color:{GOLD};margin-top:8px'>Pakistan · GCC · Central Asia · Europe</div>
 <div style='display:flex;flex-wrap:wrap;gap:10px;margin-top:20px'>{flags}</div>
 <div style='font-family:Anton;font-size:30px;color:#fff;margin-top:22px'>ALSO OFFERING</div>
 <div style='display:grid;grid-template-columns:1fr 1fr;gap:10px 20px;margin-top:12px'>{svc}</div>
 <div style='background:#fff;border-radius:24px;box-shadow:0 10px 26px #0002;padding:18px 26px;margin-top:22px;display:flex;flex-direction:column;gap:12px;border-top:8px solid {GOLD}'>
  <div style='font-family:Anton;font-size:34px;color:{GREEN}'>GET IN TOUCH</div>
  {row('phone', nums, 26, 'Anton')}{row('mail', EMAIL)}{row('gear', WEBSITE)}{row('pin', ADDRESS, 22)}</div></div>
<div style='position:absolute;left:0;right:0;bottom:{H*0.16:.0f}px;height:6px;background:{GOLD}'></div>
<div style='position:absolute;left:0;right:0;bottom:{H*0.035:.0f}px;display:flex;justify-content:center'>
 <div style='background:#fff;border-radius:18px;padding:8px 18px;box-shadow:0 8px 20px #0006'>{logo_img('logo-horizontal-light', 'width:300px;height:76px')}</div></div>"""


def shot(pg, body, w, path):
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:{w}px;height:{H}px;overflow:hidden}}</style></head>"
            f"<body><div style='position:relative;width:{w}px;height:{H}px;overflow:hidden'>{body}</div></body></html>")
    tmp = OUTPUT / ".tmp" / "file-cover.html"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(html, encoding="utf-8")
    pg.set_viewport_size({"width": w, "height": H})
    pg.goto(tmp.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
    pg.screenshot(path=str(path))


def main():
    from playwright.sync_api import sync_playwright
    from PIL import Image
    out = OUTPUT / "for-printer"
    out.mkdir(parents=True, exist_ok=True)
    spine = (f"<div style='position:absolute;left:{W}px;top:0;width:{SW}px;height:{H}px;background:{DEEP};display:flex;align-items:center;justify-content:center'>"
             f"<div style='transform:rotate(-90deg);white-space:nowrap;font-family:Anton;font-size:26px;letter-spacing:6px;color:{GOLD}'>RS LINKS CONSULTANTS PVT. LTD.</div></div>")
    spread = (f"<div style='position:absolute;left:0;top:0;width:{W}px;height:{H}px'>{back()}</div>{spine}"
              f"<div style='position:absolute;left:{W + SW}px;top:0;width:{W}px;height:{H}px'>{front()}</div>")
    jobs = [("Front_9.25x12.25in", front(), W), ("Back_9.25x12.25in", back(), W), ("Spread-with-Spine_19x12.25in", spread, 2 * W + SW)]
    with sync_playwright() as p:
        b = _launch(p)
        pg = b.new_page(device_scale_factor=SCALE)
        for name, body, w in jobs:
            stem = out / f"RS-Links_File-Cover_{name}"
            shot(pg, body, w, str(stem) + ".png")
            im = Image.open(str(stem) + ".png").convert("RGB")
            im.save(str(stem) + ".pdf", "PDF", resolution=float(PX * SCALE))
            im.resize((w // 2, H // 2), Image.LANCZOS).save(str(stem) + "_preview.png")
            print(stem)
        b.close()


if __name__ == "__main__":
    main()
