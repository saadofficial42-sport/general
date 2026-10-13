"""First LinkedIn post image (1200 x 1200, rendered at 2x)."""
from common import C, OUTPUT, WHATSAPP, font_css, icon, logo_img, whatsapp_icon
from common import _launch
from office_banners import ADDRESS, EMAIL, FLAGS, PHONE2, TAGLINE_EN, WEBSITE

GREEN, GOLD, NAVY = C["green"], C["gold"], "#0A1B25"
S = 1200
SERVICES = [("shield", "HR Consultancy"), ("user", "Recruitment &amp; Manpower"), ("doc", "Student Consultancy"),
            ("chat", "Career Advisory"), ("money", "Tax Consultancy"), ("visa", "Visa &amp; Documentation"),
            ("megaphone", "Marketing Support"), ("gear", "Website Development")]
FLAG_CODES = ["pk", "sa", "ae", "qa", "kw", "om", "bh", "uz", "kg", "kz", "ro", "pl", "de", "rs", "it"]


def build():
    svc = "".join(
        f"<div style='display:flex;align-items:center;gap:14px;background:#fff;border-radius:16px;padding:14px 16px;box-shadow:0 4px 12px #0002'>"
        f"<div style='width:52px;height:52px;border-radius:50%;background:{GREEN};display:flex;align-items:center;justify-content:center;flex:none'>"
        f"{icon(ic, 28, '#fff', 2.2)}</div><div style='font-weight:800;font-size:23px;color:{NAVY};line-height:1.15'>{t}</div></div>"
        for ic, t in SERVICES)
    flags = "".join(f"<img src='{(FLAGS / (c + '.svg')).as_uri()}' style='width:54px;height:36px;object-fit:cover;border-radius:5px;"
                    f"box-shadow:0 2px 5px #0004'>" for c in FLAG_CODES)
    row = lambda ic, t, f="Archivo", sz=24: (f"<div style='display:flex;align-items:center;gap:12px'>{ic}"
                                           f"<span style='font-family:{f};font-weight:800;font-size:{sz}px;color:#fff'>{t}</span></div>")
    circ = lambda n: (f"<div style='width:40px;height:40px;border-radius:50%;background:{GOLD};display:flex;align-items:center;justify-content:center'>"
                      f"{icon(n, 22, NAVY, 2.4)}</div>")
    return f"""<div style='position:relative;width:{S}px;height:{S}px;overflow:hidden;font-family:Archivo;background:{C['offwhite']}'>
 <div style='position:absolute;left:0;top:0;width:{S}px;height:430px;background:linear-gradient(120deg,#06291D,{GREEN} 60%,#0F5A3E)'></div>
 <svg style='position:absolute;left:0;top:0' width='{S}' height='430'><path d='M820 430 L1100 0 L1130 0 L850 430Z' fill='{GOLD}' opacity='.3'/>
  <path d='M880 430 L1160 0 L1172 0 L892 430Z' fill='{GOLD}' opacity='.5'/></svg>
 <div style='position:absolute;left:56px;top:46px;background:#fff;border-radius:18px;padding:10px 18px;box-shadow:0 6px 16px #0005'>
  {logo_img('logo-horizontal-light', 'width:380px;height:96px')}</div>
 <div style='position:absolute;left:60px;top:196px;width:900px'>
  <div style='font-family:PlexMono;font-weight:700;font-size:22px;color:{C['gold2']};letter-spacing:5px'>WE ARE NOW ON LINKEDIN</div>
  <div style='font-family:Anton;font-size:64px;line-height:1.03;color:#fff;margin-top:10px'>YOUR TRUSTED CONSULTANCY PARTNER<br>
   <span style='color:{C['gold2']}'>FOR PEOPLE &amp; BUSINESSES</span></div>
  <div style='font-family:Dancing;font-weight:700;font-size:32px;color:#DCEBE3;margin-top:6px'>{TAGLINE_EN}</div>
 </div>
 <div style='position:absolute;left:56px;right:56px;top:462px'>
  <div style='font-family:Anton;font-size:32px;color:{GREEN};letter-spacing:1px;margin-bottom:14px'>OUR SERVICES</div>
  <div style='display:grid;grid-template-columns:1fr 1fr;gap:14px 18px'>{svc}</div>
  <div style='display:flex;align-items:center;gap:16px;margin-top:22px'>
   <div style='font-family:Anton;font-size:24px;color:{GREEN};white-space:nowrap'>WE CONNECT:</div>
   <div style='display:flex;flex-wrap:wrap;gap:8px'>{flags}</div></div>
 </div>
 <div style='position:absolute;left:0;bottom:0;width:{S}px;height:196px;background:linear-gradient(100deg,{NAVY},{GREEN})'></div>
 <div style='position:absolute;left:56px;bottom:26px;display:grid;grid-template-columns:auto auto;gap:14px 46px'>
  {row(whatsapp_icon(40), WHATSAPP, 'Anton', 30)}{row(circ('mail'), EMAIL)}
  {row(whatsapp_icon(40), PHONE2, 'Anton', 30)}{row(circ('gear'), WEBSITE)}
  <div style='grid-column:1/3'>{row(circ('pin'), ADDRESS, 'Archivo', 21)}</div>
 </div>
</div>"""


def main():
    from playwright.sync_api import sync_playwright
    out = OUTPUT / "linkedin"
    out.mkdir(parents=True, exist_ok=True)
    tmp = OUTPUT / ".tmp" / "li-post.html"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{font_css()}html,body{{width:{S}px;height:{S}px;margin:0;overflow:hidden}}</style></head>"
                   f"<body>{build()}</body></html>", encoding="utf-8")
    with sync_playwright() as pw:
        b = _launch(pw)
        pg = b.new_page(viewport={"width": S, "height": S}, device_scale_factor=2)
        pg.goto(tmp.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        pg.screenshot(path=str(out / "RS-Links-LinkedIn-First-Post.png"))
        b.close()
    print(out / "RS-Links-LinkedIn-First-Post.png")


if __name__ == "__main__":
    main()
