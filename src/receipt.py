"""RS Links payment receipt (2026-10-23): very simple, two copies on one A4 page (Customer Copy / Office Copy) with a
dashed cut line. Basic fields only, no phone numbers (user). Outputs: output/receipt/RS-Links-Payment-Receipt-A4.pdf/.png"""
from common import C, OUTPUT, _launch, font_css, logo_img
from office_banners import ADDRESS

GREEN, INK = C["green"], "#1E2A24"
PX = 96
W, H = round(8.27 * PX), round(11.69 * PX)


def line(label, w="1fr"):
    return (f"<div style='display:flex;align-items:flex-end;gap:10px;height:46px'>"
            f"<span style='font:700 14px Archivo;color:{INK};white-space:nowrap'>{label}</span>"
            f"<span style='flex:1;border-bottom:1.5px solid #9AA59F;height:22px'></span></div>")


def box(label):
    return (f"<span style='display:inline-flex;align-items:center;gap:6px;margin-right:22px'>"
            f"<span style='width:14px;height:14px;border:1.5px solid {INK};border-radius:3px'></span>"
            f"<span style='font:600 14px Archivo;color:{INK}'>{label}</span></span>")


def receipt(copy):
    return f"""<div style='position:relative;height:100%;padding:30px 46px;box-sizing:border-box;display:flex;flex-direction:column'>
 <div style='display:flex;align-items:center;gap:14px;padding-bottom:12px;border-bottom:3px solid {GREEN}'>
  {logo_img('logo-badge', 'width:62px;height:62px')}
  <div style='flex:1'><div style='font-family:Anton;font-size:24px;color:{GREEN};letter-spacing:.5px;line-height:1'>RS LINKS CONSULTANTS PVT. LTD.</div>
   <div style='font:600 11.5px Archivo;color:#5A655F;margin-top:5px'>{ADDRESS}</div></div>
  <div style='text-align:right'><div style='font-family:Anton;font-size:28px;color:{INK};letter-spacing:1px;line-height:1'>PAYMENT RECEIPT</div>
   <div style='display:inline-block;margin-top:6px;font:800 11px Archivo;letter-spacing:2px;color:#fff;background:{GREEN};padding:3px 10px;border-radius:4px'>{copy.upper()}</div></div></div>
 <div style='display:grid;grid-template-columns:1fr 1fr;gap:4px 34px;margin-top:12px'>{line('Receipt No.')}{line('Date')}</div>
 {line('Received from (Name)')}
 <div style='display:grid;grid-template-columns:1fr 1fr;gap:4px 34px'>{line('CNIC / Passport No.')}{line('Amount (Rs.)')}</div>
 {line('Amount in words')}
 {line('Payment for')}
 <div style='display:flex;align-items:flex-end;height:50px'><span style='font:700 14px Archivo;color:{INK};margin-right:16px'>Payment method:</span>{box('Cash')}{box('Bank Transfer')}{box('Online')}{box('Cheque')}</div>
 <div style='flex:1'></div>
 <div style='display:flex;justify-content:space-between;align-items:flex-end'>
  <div style='width:240px;text-align:center'><div style='border-top:1.5px solid #9AA59F;padding-top:5px;font:700 13px Archivo;color:{INK}'>Received by (Name &amp; Signature)</div></div>
  <div style='width:150px;height:80px;border:1.5px dashed #B6BFBA;border-radius:8px;display:flex;align-items:center;justify-content:center;font:600 12px Archivo;color:#9AA59F'>Company Stamp</div>
  <div style='width:200px;text-align:center'><div style='border-top:1.5px solid #9AA59F;padding-top:5px;font:700 13px Archivo;color:{INK}'>Payer's Signature</div></div></div></div>"""


def page():
    half = H // 2
    return f"""<div style='position:relative;width:{W}px;height:{H}px;background:#fff'>
<div style='position:absolute;left:0;top:0;width:{W}px;height:{half}px'>{receipt('Customer Copy')}</div>
<div style='position:absolute;left:24px;right:24px;top:{half}px;border-top:1.5px dashed #9AA59F'></div>
<div style='position:absolute;left:50%;top:{half - 9}px;transform:translateX(-50%);background:#fff;padding:0 10px;font:600 11px Archivo;color:#9AA59F'>✂ cut here</div>
<div style='position:absolute;left:0;top:{half}px;width:{W}px;height:{H - half}px'>{receipt('Office Copy')}</div></div>"""


def main():
    from playwright.sync_api import sync_playwright
    out = OUTPUT / "receipt"
    out.mkdir(parents=True, exist_ok=True)
    f = OUTPUT / ".tmp" / "receipt.html"
    f.parent.mkdir(exist_ok=True)
    f.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{font_css()}@page{{size:{W}px {H}px;margin:0}}"
                 f"html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden}}</style></head><body>{page()}</body></html>", encoding="utf-8")
    stem = out / "RS-Links-Payment-Receipt-A4"
    with sync_playwright() as pw:
        b = _launch(pw)
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=300 / PX)
        pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
        pg.screenshot(path=str(stem) + ".png")
        pg.pdf(path=str(stem) + ".pdf", width="8.27in", height="11.69in", print_background=True)
        b.close()
    print(stem)


if __name__ == "__main__":
    main()
