"""Small wall direction signs (2026-10-16): ground floor + 2nd floor, arrow pointing up to the office
(Office No. 20, 3rd Floor). Size 18 x 24 in portrait (to confirm with user). Print files: PNG at 288 ppi
+ PDF built from the PNG (same method as the gate banners)."""
from common import C, OUTPUT, PHONES, font_css, icon, logo_img, whatsapp_icon, _launch

GREEN, DEEP, GOLD, NAVY = C["green"], "#06291D", C["gold2"], "#0A1B25"
W_IN, H_IN, PX = 18, 24, 72          # css px per inch; rendered at 4x -> 288 ppi
SCALE = 4
EMAIL = "hr@rslinksconsultants.com"

SIGNS = {
    "Ground-Floor": {"kicker": "RS LINKS OFFICE", "big": "3RD FLOOR", "sub": "Please go up 3 floors",
                     "ur": "ہمارا دفتر تیسری منزل پر ہے", "ur_sub": "براہِ کرم اوپر تشریف لائیں"},
    "2nd-Floor": {"kicker": "ALMOST THERE!", "big": "ONE FLOOR UP", "sub": "Office No. 20 is on the 3rd floor",
                  "ur": "صرف ایک منزل اوپر", "ur_sub": "آفس نمبر 20 — تیسری منزل"},
}


def build(s):
    w, h = W_IN * PX, H_IN * PX
    nums = "".join(f"<div style='font-family:Anton;font-size:44px;color:{NAVY};line-height:1.08;letter-spacing:.5px'>{n}</div>" for n in PHONES)
    arrow = (f"<svg width='520' height='470' viewBox='0 0 520 470'><defs><linearGradient id='ag' x1='0' y1='0' x2='0' y2='1'>"
             f"<stop offset='0' stop-color='#FFE27A'/><stop offset='1' stop-color='{GOLD}'/></linearGradient></defs>"
             f"<path d='M260 10 L510 260 L370 260 L370 460 L150 460 L150 260 L10 260Z' fill='url(#ag)' stroke='#fff' stroke-width='14' stroke-linejoin='round'/>"
             f"<path d='M260 70 L440 240' stroke='#fff' stroke-width='10' stroke-linecap='round' opacity='.45'/></svg>")
    body = f"""
<div style='position:absolute;inset:0;background:linear-gradient(170deg,{GREEN} 0%,{DEEP} 62%)'></div>
<svg style='position:absolute;left:0;top:0' width='{w}' height='{h}'>
 <circle cx='{w*0.9}' cy='{h*0.12}' r='260' fill='#ffffff0b'/><circle cx='{w*0.05}' cy='{h*0.55}' r='200' fill='#ffffff08'/>
 <rect x='22' y='22' width='{w-44}' height='{h-44}' rx='30' fill='none' stroke='{GOLD}' stroke-width='6'/></svg>
<div style='position:absolute;left:60px;right:60px;top:56px;height:150px;background:#fff;border-radius:26px;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 26px #0006'>
 {logo_img('logo-horizontal-light', 'width:620px;height:126px')}</div>
<div style='position:absolute;left:0;right:0;top:236px;text-align:center'>
 <div style='font-family:PlexMono;font-weight:700;font-size:34px;letter-spacing:8px;color:{GOLD}'>{s['kicker']}</div></div>
<div style='position:absolute;left:0;right:0;top:296px;display:flex;justify-content:center;filter:drop-shadow(0 18px 24px #0008)'>{arrow}</div>
<div style='position:absolute;left:0;right:0;top:780px;text-align:center'>
 <div style='font-family:Anton;font-size:150px;line-height:1;color:#fff;letter-spacing:3px'>{s['big']}</div>
 <div style='font-family:Archivo;font-weight:800;font-size:40px;color:#DCEBE3;margin-top:10px'>{s['sub']}</div>
 <div style='font-family:Nastaliq;font-weight:700;font-size:62px;color:{GOLD};direction:rtl;line-height:1.75;margin-top:6px'>{s['ur']}</div>
 <div style='font-family:Nastaliq;font-size:36px;color:#fff;direction:rtl;line-height:1.7'>{s['ur_sub']}</div></div>
<div style='position:absolute;left:60px;right:60px;top:1262px;background:{GOLD};border-radius:22px;padding:18px 26px;display:flex;align-items:center;gap:20px;box-shadow:0 8px 20px #0005'>
 <div style='width:84px;height:84px;border-radius:50%;background:{NAVY};display:flex;align-items:center;justify-content:center;flex:none'>{icon('pin', 48, GOLD, 2.4)}</div>
 <div style='font-family:Archivo;color:{NAVY}'>
  <div style='font-weight:900;font-size:44px;line-height:1.1'>Office No. 20, 3rd Floor</div>
  <div style='font-weight:700;font-size:28px;line-height:1.3'>Satellite Shopping Centre, Sixth Road, Rawalpindi</div></div></div>
<div style='position:absolute;left:60px;right:60px;top:1432px;height:250px;background:#fff;border-radius:22px;display:flex;align-items:center;gap:24px;padding:0 30px;box-shadow:0 8px 20px #0005'>
 {whatsapp_icon(96)}<div>{nums}</div>
 <div style='margin-left:auto;text-align:right;font-family:Archivo'>
  <div style='font-weight:900;font-size:30px;color:{GREEN}'>Turning Your Dreams<br>into Reality</div>
  <div style='display:flex;align-items:center;gap:8px;justify-content:flex-end;margin-top:12px'>{icon('mail', 26, GREEN, 2.2)}
   <span style='font-weight:700;font-size:22px;color:{NAVY}'>{EMAIL}</span></div></div></div>
"""
    return w, h, body


def main():
    from playwright.sync_api import sync_playwright
    from PIL import Image
    out = OUTPUT / "for-printer"
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        b = _launch(pw)
        for name, s in SIGNS.items():
            w, h, body = build(s)
            html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:{w}px;height:{h}px;overflow:hidden}}</style></head>"
                    f"<body><div style='position:relative;width:{w}px;height:{h}px;overflow:hidden'>{body}</div></body></html>")
            tmp = OUTPUT / ".tmp" / f"sign-{name}.html"
            tmp.parent.mkdir(parents=True, exist_ok=True)
            tmp.write_text(html, encoding="utf-8")
            pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=SCALE)
            pg.goto(tmp.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
            stem = out / f"RS-Links_Direction-Sign_{name}_{W_IN}x{H_IN}in"
            pg.screenshot(path=str(stem) + ".png")
            pg.close()
            im = Image.open(str(stem) + ".png").convert("RGB")
            im.save(str(stem) + ".pdf", "PDF", resolution=float(PX * SCALE))
            im.resize((w, h), Image.LANCZOS).save(str(stem) + "_preview.png")
            print(stem)
        b.close()


if __name__ == "__main__":
    main()
