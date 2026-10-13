"""RS Links LinkedIn company page cover (1128 x 191 px, rendered at 2x = 2256 x 382).

LinkedIn overlays the company logo at the bottom-left and crops the edges on mobile,
so key content sits in the centre/right and the far-left ~280 px is kept decorative.
"""
from common import C, OUTPUT, font_css, icon, logo_img
from common import _launch
from office_banners import FLAGS, TAGLINE_EN, WEBSITE

GREEN, GOLD, NAVY = C["green"], C["gold"], "#0A1B25"
W, H = 1128, 191
FLAG_CODES = ["sa", "ae", "qa", "kw", "om", "uz", "kg", "kz", "ro", "pl", "de", "rs", "it", "es"]


def build():
    flags = "".join(f"<img src='{(FLAGS / (c + '.svg')).as_uri()}' style='width:34px;height:23px;object-fit:cover;border-radius:3px;"
                    f"box-shadow:0 1px 3px #0005'>" for c in FLAG_CODES)
    svcs = ["Manpower Recruitment", "HR Consultancy", "Student &amp; Career Consultancy"]
    chips = "".join(f"<span style='background:#ffffff1A;border:1px solid {GOLD}88;border-radius:999px;padding:3px 10px;"
                    f"font-size:11.5px;font-weight:700;color:#fff;white-space:nowrap'>{s}</span>" for s in svcs)
    return f"""<div style='position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:Archivo;
 background:linear-gradient(110deg,#06291D 0%,{GREEN} 45%,#0F5A3E 100%)'>
 <svg style='position:absolute;left:0;top:0' width='{W}' height='{H}'>
  <circle cx='120' cy='40' r='150' fill='#ffffff08'/><circle cx='1060' cy='210' r='170' fill='#ffffff07'/>
  <path d='M0 {H} L360 0 L392 0 L32 {H}Z' fill='{GOLD}' opacity='.18'/>
  <path d='M60 {H} L420 0 L432 0 L72 {H}Z' fill='{GOLD}' opacity='.35'/>
 </svg>
 <div style='position:absolute;left:300px;top:24px;width:470px'>
  <div style='font-family:Anton;font-size:38px;line-height:1.02;color:#fff;letter-spacing:.5px'>
   CONNECTING PAKISTANI TALENT<br><span style='color:{C['gold2']}'>WITH GLOBAL OPPORTUNITIES</span></div>
  <div style='font-family:Dancing;font-weight:700;font-size:20px;color:#DCEBE3;margin-top:4px'>{TAGLINE_EN}</div>
  <div style='display:flex;gap:6px;margin-top:8px'>{chips}</div>
 </div>
 <div style='position:absolute;right:26px;top:22px;width:300px;display:flex;flex-direction:column;align-items:flex-end;gap:9px'>
  <div style='background:#fff;border-radius:10px;padding:5px 10px;box-shadow:0 3px 10px #0005'>
   {logo_img('logo-horizontal-light', 'width:180px;height:46px')}</div>
  <div style='display:grid;grid-template-columns:repeat(7,34px);gap:5px'>{flags}</div>
  <div style='font-size:11px;font-weight:800;color:{C['gold2']};letter-spacing:1.5px;white-space:nowrap'>GCC · CENTRAL ASIA · EUROPE</div>
 </div>
</div>"""


def main():
    from playwright.sync_api import sync_playwright
    out = OUTPUT / "linkedin"
    out.mkdir(parents=True, exist_ok=True)
    tmp = OUTPUT / ".tmp" / "linkedin.html"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{font_css()}html,body{{width:{W}px;height:{H}px;margin:0;overflow:hidden}}</style></head>"
                   f"<body>{build()}</body></html>", encoding="utf-8")
    with sync_playwright() as pw:
        b = _launch(pw)
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        pg.goto(tmp.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        pg.screenshot(path=str(out / "RS-Links-LinkedIn-Cover_1128x191.png"))
        b.close()
    print(out / "RS-Links-LinkedIn-Cover_1128x191.png")


if __name__ == "__main__":
    main()
