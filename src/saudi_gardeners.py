"""Saudi Arabia — General Workers / Gardeners, Urdu (2026-10-20). Facts: user message (salary 1200 SAR, 8 hours
daily; documents CV, passport, CNIC, passport-size photo; after approval NAVTCC + medical) plus the source ad the user
sent (demands/2026-10-20-saudi-general-workers/ref.jpg): well-known facility-management & catering services company
(not named), General Workers (gardening or loading/unloading), salary 1000 + 200 riyal + overtime, duty 8 hours +
overtime, 2-year contract, basic English speaking required, accommodation / medical / transport by the company,
other benefits per labour law. Dropped from the source: urgent visa / departure, "no fee", self selection,
the other agency's name / address / numbers.
Design: "garden poster" — deep leaf-green page with soft leaf shapes, gold accents, tall rounded photo frame,
leaf-shaped salary badge, two-step documents flow, cream CTA with all four numbers.
Photos: real RS Links general-worker photo. A gardener photo slot (assets/photos/ksa_gardener.*) is shown as a
second frame once a real gardener photo exists — no drawing is used in its place."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

LEAF, LEAF2, LIME, GOLD, CREAM, INK = "#0F5132", "#083A23", "#7BC043", "#F5C542", "#FFF8E7", "#132018"
EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"
N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.75: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def photo(key):
    for e in ("jpg", "jpeg", "png", "webp"):
        p = PHOTOS / f"{key}.{e}"
        if p.exists():
            return p.as_uri()
    return None


def leaves():
    shapes = [(80, 700, 140, -30, .10), (980, 160, 180, 40, .08), (960, 980, 120, -60, .10), (520, 110, 90, 20, .06), (130, 1060, 100, 70, .07)]
    s = "".join(f"<path transform='translate({x} {y}) rotate({r}) scale({k / 100})' d='M0 -100 C 60 -60, 60 60, 0 100 C -60 60, -60 -60, 0 -100Z M0 -100 V100' fill='{LIME}' opacity='{o}' stroke='{LIME}' stroke-opacity='{o}' stroke-width='3'/>"
                for x, y, k, r, o in shapes)
    return f"<svg width='1080' height='1350' style='display:block'>{s}</svg>"


def build():
    worker, gardener = photo("rslinks_worker_hero"), photo("ksa_gardener")
    frame = lambda uri, w, h, pos="center 25%": (f"<div style='width:{w}px;height:{h}px;border-radius:{w // 2}px {w // 2}px 28px 28px;overflow:hidden;border:6px solid {GOLD};box-shadow:0 18px 36px #0008;flex:none'>"
                                                   f"<img src='{uri}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'></div>")
    pics = (f"<div style='display:flex;gap:16px;align-items:flex-end'>{frame(gardener, 210, 400)}{frame(worker, 210, 340)}</div>" if gardener
            else frame(worker, 380, 470))
    docs = [("user", "سی وی"), ("idcard", "پاسپورٹ"), ("idcard", "شناختی کارڈ"), ("camera", "پاسپورٹ سائز تصویر")]
    doc_li = "".join(f"<div style='display:flex;align-items:center;gap:10px'><span style='width:40px;height:40px;border-radius:12px;background:{LEAF};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 22, GOLD, 2.2)}</span>"
                     f"{T(t, 25, INK, 'font-weight:700', 1.7)}</div>" for ic, t in docs)
    after = [("doc", "NAVTCC"), ("medical", "میڈیکل")]
    after_li = "".join(f"<div style='display:flex;align-items:center;gap:10px;background:#ffffff1a;border-radius:14px;padding:4px 16px'>{icon(ic, 30, GOLD, 2.2)}"
                       + (f"<span style='font:400 32px Anton;color:#fff;letter-spacing:1px'>{t}</span>" if t.isascii() else T(t, 28, '#fff', 'font-weight:700', 1.6))
                       + "</div>" for ic, t in after)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'><span style='line-height:0'>{whatsapp_icon(32)}</span><span class='num' style='font-size:29px;color:{INK};line-height:1.2'>{n}</span></div>" for n in PHONES)
    body = f"""<div class='ur-on' dir='rtl'>
<div class='abs' style='top:0;left:0;width:1080px;height:1350px;background:radial-gradient(circle at 25% 30%,#1A7A4A,{LEAF} 45%,{LEAF2})'></div>
<div class='abs' style='top:0;left:0'>{leaves()}</div>
<div class='abs' style='top:22px;right:26px;background:#fff;border-radius:18px;padding:4px 16px;box-shadow:0 6px 16px #0006'>{logo_img('logo-horizontal-light', 'width:360px;height:90px;object-position:right')}</div>
<div class='abs' style='top:22px;left:28px;display:flex;align-items:center;gap:14px;direction:ltr'>
 <div style='filter:drop-shadow(0 4px 8px #0008)'>{flag('saudi', 140, True, 'sag')}</div>
 <div style='background:{GOLD};border-radius:14px;padding:0 18px 8px;display:flex;align-items:center;gap:8px;box-shadow:0 6px 14px #0006'>{icon('megaphone', 28, LEAF2, 2.3)}{T('فوری ضرورت', 32, LEAF2, 'font-weight:700', 1.6)}</div></div>

<div class='abs' style='top:150px;left:40px'>{pics}</div>
<div class='abs' style='top:150px;right:40px;width:560px;text-align:right'>
 {T('برائے سعودی عرب', 34, GOLD, 'font-weight:700', 1.7)}
 {T('جنرل ورکرز', 86, '#fff', 'font-weight:700;margin-top:24px;text-shadow:0 6px 16px #0006', 1.85)}
 {T('(گارڈننگ یا لوڈنگ اَن لوڈنگ)', 32, LIME, 'font-weight:700;margin-top:6px;margin-bottom:16px', 1.7)}
 <div style='font:400 40px Anton;color:#fff;letter-spacing:2px;direction:ltr;text-align:right;line-height:1.1'>GENERAL WORKERS</div>
 <div style='font:800 20px Archivo;color:{GOLD};letter-spacing:1px;direction:ltr;text-align:right;margin-top:4px'>GARDENING · LOADING / UNLOADING</div>
 {T('معروف فیسلٹی مینجمنٹ و کیٹرنگ سروسز کمپنی کے لیے', 22, '#DDEFE2', 'font-weight:700;margin-top:18px', 1.8)}</div>

<div class='abs' style='top:640px;left:40px;right:40px;height:158px;display:flex;gap:14px'>
 <div style='flex:1.5;background:radial-gradient(circle at 30% 25%,#FFE89A,{GOLD} 55%,#D9A21E);border-radius:90px 18px 90px 18px;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 14px 28px #0007'>
  {T('تنخواہ', 22, LEAF2, 'font-weight:700;margin-bottom:8px', 1.5)}
  <div style='direction:ltr;display:flex;align-items:baseline;gap:8px'><span class='num' style='font-size:50px;color:{LEAF2};line-height:1'>1000 + 200</span><span class='num' style='font-size:22px;color:{LEAF2}'>SAR</span></div>
  {T('+ اوور ٹائم', 20, LEAF2, 'font-weight:700;margin-top:8px', 1.5)}</div>
 {''.join(f"<div style='flex:1;background:#fff;border-radius:18px;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 14px 28px #0006'>"
          f"<div style='width:44px;height:44px;border-radius:50%;background:{LEAF};display:flex;align-items:center;justify-content:center'>{icon(ic, 25, GOLD, 2.3)}</div>"
          f"{T(v, 25, INK, 'font-weight:700;margin-top:14px', 1.5)}{T(l, 17, '#4D5E54', 'font-weight:700;margin-top:10px', 1.5)}</div>"
          for ic, v, l in [('clock', f"{N(8)} گھنٹے", 'ڈیوٹی + اوور ٹائم'), ('calendar', f"{N(2)} سال", 'معاہدہ'), ('chat', 'بیسک انگلش', 'بول چال لازمی')])}</div>
<div class='abs' style='top:806px;left:40px;right:40px;height:72px;border-radius:999px;background:#ffffff1a;border:2px solid {GOLD};display:flex;align-items:center;gap:26px;padding:0 26px'>
 {T('بذمہ کمپنی:', 26, GOLD, 'font-weight:700', 1.6)}
 {''.join(f"<div style='display:flex;align-items:center;gap:8px'>{icon(ic, 28, GOLD, 2.3)}{T(t, 25, '#fff', 'font-weight:700', 1.6)}</div>" for ic, t in [('home', 'رہائش'), ('medical', 'میڈیکل'), ('bus', 'ٹرانسپورٹ')])}
 {T('دیگر مراعات لیبر لاء کے مطابق', 21, '#DDEFE2', 'font-weight:700;margin-inline-start:auto', 1.6)}</div>

<div class='abs' style='top:896px;left:40px;right:40px;height:242px;display:flex;gap:16px'>
 <div style='flex:1.35;background:{CREAM};border-radius:22px;padding:6px 22px;box-shadow:0 12px 26px #0006'>
  {T('درکار دستاویزات', 32, LEAF, 'font-weight:700', 1.7)}
  <div style='display:grid;grid-template-columns:1fr 1fr;gap:20px 12px;margin-top:10px'>{doc_li}</div></div>
 <div style='flex:1;background:linear-gradient(160deg,#1E8A54,{LEAF2});border:3px solid {GOLD};border-radius:22px;padding:6px 22px;display:flex;flex-direction:column'>
  {T('منظوری کے بعد', 32, GOLD, 'font-weight:700', 1.7)}
  <div style='display:flex;flex-direction:column;gap:12px;margin-top:6px'>{after_li}</div></div></div>

<div class='abs' style='top:1160px;left:0;width:1080px;height:190px;background:{CREAM}'></div>
<div class='abs' style='top:1152px;left:0;width:1080px;height:8px;background:{GOLD}'></div>
<div class='abs' style='top:1178px;left:28px;width:560px;height:150px;display:grid;grid-template-columns:1fr 1fr;align-content:center;gap:10px 14px;direction:ltr'>{nums}</div>
<div class='abs' style='top:1170px;right:34px;width:430px;text-align:right'>
 {T('ابھی رابطہ کریں!', 40, LEAF, 'font-weight:700', 1.6)}
 {T(f"اپنی {N('CV')} اور دستاویزات واٹس ایپ کریں", 21, INK, 'font-weight:700', 1.7)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr;margin-top:4px'>{icon('mail', 22, LEAF, 2)}<span style='font:800 21px Archivo;color:{INK}'>{EMAIL}</span></div>
 <div style='direction:ltr;text-align:right;font:600 13px Archivo;color:#5A6A60;margin-top:6px'>{ADDRESS}</div></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{LEAF}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Saudi-Arabia-General-Workers-Gardeners-Urdu.png"))
