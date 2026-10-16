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
    svc = "".join(f"<div style='display:flex;align-items:center;gap:10px'><div style='width:38px;height:38px;border-radius:50%;background:{GREEN};display:flex;align-items:center;justify-content:center;flex:none'>"
                  f"{icon(ic, 21, '#fff', 2.3)}</div><span style='font-family:Archivo;font-weight:700;font-size:18px;color:{NAVY}'>{t}</span></div>"
                  for ic, t in SERVICES[:8])
    crow = lambda ic, t, sz=19, f="Archivo", w=700: (f"<div style='display:flex;align-items:center;gap:12px'><div style='width:42px;height:42px;border-radius:50%;background:{GOLD};display:flex;align-items:center;justify-content:center;flex:none'>"
                                          f"{icon(ic, 22, NAVY, 2.4)}</div><span style='font-family:{f};font-weight:{w};font-size:{sz}px;color:#fff;line-height:1.2'>{t}</span></div>")
    nums = " &nbsp;|&nbsp; ".join(PHONES)
    return f"""
<div style='position:absolute;inset:0;background:#fff'></div>
<svg style='position:absolute;left:0;top:0' width='{W}' height='{H}'>{globe(W*0.5, H*0.17, 300, GREEN, .05)}</svg>
<div style='position:absolute;left:0;top:0;width:{W}px;height:16px;background:linear-gradient(90deg,{GREEN} 0 70%,{GOLD} 70%)'></div>
<div style='position:absolute;left:0;right:0;top:{H*0.045:.0f}px;display:flex;justify-content:center'>
 <div style='border-radius:50%;padding:10px;background:#fff;box-shadow:0 14px 34px rgba(6,41,29,.25)'>{logo_img('logo-badge', 'width:270px;height:270px')}</div></div>
<div style='position:absolute;left:0;right:0;top:{H*0.33:.0f}px;text-align:center'>
 <div style='font-family:Anton;font-size:74px;line-height:1;color:{GREEN};letter-spacing:2px'>RS LINKS CONSULTANTS</div>
 <div style='font-family:PlexMono;font-weight:700;font-size:20px;letter-spacing:8px;color:{NAVY};margin-top:8px'>PVT. LTD.</div>
 <div style='font-family:Dancing;font-weight:700;font-size:44px;color:#A87508;margin-top:10px'>{TAGLINE_EN}</div>
 <div style='font-family:PlexMono;font-weight:700;font-size:17px;letter-spacing:3px;color:#5A6470;margin-top:8px'>RECRUITMENT · CONSULTANCY · VISA SERVICES</div></div>
<div style='position:absolute;left:{W*0.08:.0f}px;right:{W*0.08:.0f}px;top:{H*0.535:.0f}px;display:grid;grid-template-columns:1fr 1fr;gap:14px 24px;
 padding:22px 24px;border:2px solid {GREEN}22;border-radius:22px;background:#F6FAF7'>{svc}</div>
<div style='position:absolute;left:0;top:{H*0.765:.0f}px;width:{W}px;height:{H*0.235:.0f}px;background:linear-gradient(120deg,{GREEN},{DEEP})'></div>
<div style='position:absolute;left:0;top:{H*0.765:.0f}px;width:{W}px;height:6px;background:{GOLD}'></div>
<div style='position:absolute;left:{W*0.08:.0f}px;right:{W*0.08:.0f}px;top:{H*0.79:.0f}px;display:flex;flex-direction:column;gap:12px'>
 {crow('phone', nums, 24, 'Anton', 400)}
 <div style='display:flex;gap:30px'>{crow('mail', EMAIL)}{crow('gear', WEBSITE)}</div>
 {crow('pin', ADDRESS + ', Pakistan', 18)}</div>"""


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
 <div style='background:#fff;border-radius:18px;padding:8px 18px;box-shadow:0 8px 20px #0006'>{logo_img('logo-horizontal-light', 'width:380px;height:96px')}</div></div>"""


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
