"""RS Links presentation folder / file cover (2026-10-16).
Front and back panels 9 x 12 in (standard A4/letter presentation folder), plus a flat spread
(back | front, 18 x 12 in) with 0.125 in bleed. Rendered at 96 css px/in x3 = 288 dpi; PDFs built from PNG."""
from common import C, OUTPUT, PHONES, font_css, icon, logo_img, _launch
from office_banners import ADDRESS, FLAGS, SERVICES, TAGLINE_EN, TAGLINE_UR, WEBSITE

GREEN, DEEP, GOLD, NAVY, CREAM = C["green"], "#06291D", C["gold2"], "#0A1B25", "#F7F3EA"
PX, SCALE, BLEED = 96, 3, 0.125
W, H = int((9 + 2 * BLEED) * PX), int((12 + 2 * BLEED) * PX)
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
    svc = "".join(f"<div style='display:flex;align-items:center;gap:10px'><div style='width:38px;height:38px;border-radius:50%;background:{GOLD};display:flex;align-items:center;justify-content:center;flex:none'>"
                  f"{icon(ic, 21, NAVY, 2.3)}</div><span style='font-family:Archivo;font-weight:700;font-size:18px;color:#fff'>{t}</span></div>"
                  for ic, t in SERVICES[:8])
    return f"""
<div style='position:absolute;inset:0;background:linear-gradient(165deg,#0E5A3F 0%,{GREEN} 35%,{DEEP} 100%)'></div>
<svg style='position:absolute;left:0;top:0' width='{W}' height='{H}'>{globe(W*0.82, H*0.20, 260, '#ffffff', .07)}
 <circle cx='{W*0.1}' cy='{H*0.48}' r='160' fill='#ffffff07'/></svg>
<div style='position:absolute;left:0;top:{H*0.06:.0f}px;width:14px;height:{H*0.28:.0f}px;background:{GOLD}'></div>
<div style='position:absolute;left:{W*0.09:.0f}px;top:{H*0.07:.0f}px;width:{W*0.62:.0f}px;background:#fff;border-radius:26px;padding:22px 26px;box-shadow:0 16px 36px #0007'>
 {logo_img('logo-horizontal-light', f'width:{W*0.62-52:.0f}px;height:{(W*0.62-52)*0.25:.0f}px')}</div>
<div style='position:absolute;left:{W*0.09:.0f}px;top:{H*0.27:.0f}px;width:{W*0.82:.0f}px'>
 <div style='font-family:PlexMono;font-weight:700;font-size:19px;letter-spacing:4px;color:{GOLD};white-space:nowrap'>RECRUITMENT · CONSULTANCY · VISA SERVICES</div>
 <div style='font-family:Anton;font-size:76px;line-height:1.02;color:#fff;margin-top:12px'>YOUR TRUSTED<br>CONSULTANCY <span style='color:{GOLD}'>PARTNER</span></div>
 <div style='font-family:Dancing;font-weight:700;font-size:46px;color:#DCEBE3;margin-top:10px'>{TAGLINE_EN}</div>
 <div style='width:160px;height:5px;background:{GOLD};border-radius:3px;margin-top:22px'></div>
 <div style='display:grid;grid-template-columns:1fr 1fr;gap:14px 26px;margin-top:26px'>{svc}</div></div>
{waves(W, H, 'f')}
<div style='position:absolute;left:{W*0.09:.0f}px;right:{W*0.09:.0f}px;bottom:{H*0.03:.0f}px;display:flex;flex-direction:column;align-items:center;gap:2px'>
 <div style='font-family:Nastaliq;font-size:26px;color:#fff;direction:rtl;line-height:1.8;white-space:nowrap'>{TAGLINE_UR}</div>
 <div style='font-family:Archivo;font-weight:800;font-size:22px;color:{GOLD};letter-spacing:1px'>{WEBSITE}</div></div>"""


def back():
    flags = "".join(f"<img src='{(FLAGS / (c + '.svg')).as_uri()}' style='width:62px;height:42px;object-fit:cover;border-radius:5px;box-shadow:0 2px 6px #0003'>" for c in FLAG_CODES)
    row = lambda ic, t, sz=24, f="Archivo": (f"<div style='display:flex;align-items:center;gap:16px'><div style='width:54px;height:54px;border-radius:50%;background:{GREEN};display:flex;align-items:center;justify-content:center;flex:none'>"
                                            f"{icon(ic, 28, '#fff', 2.2)}</div><span style='font-family:{f};font-weight:700;font-size:{sz}px;color:{NAVY};line-height:1.25'>{t}</span></div>")
    nums = "<br>".join(PHONES)
    svc = "".join(f"<div style='font-family:Archivo;font-weight:700;font-size:18px;color:{NAVY};display:flex;align-items:center;gap:8px'>{icon('check', 18, GREEN, 3)}{t}</div>" for _, t in SERVICES[8:])
    return f"""
<div style='position:absolute;inset:0;background:{CREAM}'></div>
<svg style='position:absolute;left:0;top:0' width='{W}' height='{H}'>{globe(W*0.18, H*0.16, 220, GREEN, .06)}</svg>
<div style='position:absolute;left:{W*0.09:.0f}px;top:{H*0.05:.0f}px;width:{W*0.82:.0f}px'>
 <div style='font-family:Anton;font-size:52px;color:{GREEN};line-height:1'>WHERE WE CONNECT YOU</div>
 <div style='font-family:Archivo;font-weight:700;font-size:21px;color:#4A5868;margin-top:8px'>Pakistan · GCC · Central Asia · Europe</div>
 <div style='display:flex;flex-wrap:wrap;gap:10px;margin-top:20px'>{flags}</div>
 <div style='font-family:Anton;font-size:30px;color:{NAVY};margin-top:22px'>ALSO OFFERING</div>
 <div style='display:grid;grid-template-columns:1fr 1fr;gap:10px 20px;margin-top:12px'>{svc}</div>
 <div style='background:#fff;border-radius:24px;box-shadow:0 10px 26px #0002;padding:18px 26px;margin-top:22px;display:flex;flex-direction:column;gap:12px;border-top:8px solid {GOLD}'>
  <div style='font-family:Anton;font-size:34px;color:{GREEN}'>GET IN TOUCH</div>
  {row('phone', nums, 26, 'Anton')}{row('mail', EMAIL)}{row('gear', WEBSITE)}{row('pin', ADDRESS, 22)}</div></div>
{waves(W, H, 'b')}
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
    spread = f"<div style='position:absolute;left:0;top:0;width:{W}px;height:{H}px'>{back()}</div><div style='position:absolute;left:{W}px;top:0;width:{W}px;height:{H}px'>{front()}</div>"
    jobs = [("Front_9x12in", front(), W), ("Back_9x12in", back(), W), ("Spread_18x12in", spread, 2 * W)]
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
