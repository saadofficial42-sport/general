"""Uzbekistan — consolidated 10-position ad, Urdu (2026-11-17). Same facts and layout family as
uzbekistan_kuljeet_campaign.py (Registan majolica), set right-to-left in Nastaliq."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon
from uzbekistan_kuljeet_campaign import COB, COB2, TQ, SAF, SAF2, INK, EMAIL, tile_bg

N = lambda v: f"<span class='num'>{v}</span>"
T = lambda s, px, c, extra="", lh=1.8: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def card(title, photos, roles, tag, tag_col, note=""):
    ph = "".join(f"<div style='flex:1;height:128px;border-radius:12px;overflow:hidden'><img src='{(PHOTOS / f).as_uri()}' style='width:100%;height:100%;object-fit:{fit};object-position:{pos};background:#EEF1F6'></div>" for f, pos, fit in photos)
    rl = "".join(f"<div style='display:flex;align-items:center;justify-content:space-between;gap:10px;border-bottom:1px dashed #D8DEEA;height:40px;padding-top:4px;box-sizing:border-box'>"
                 f"{T(r, 21, INK, 'font-weight:700;white-space:nowrap', 1.7)}"
                 f"<span style='background:{SAF};color:{INK};font:400 22px Anton;padding:1px 10px;border-radius:8px;white-space:nowrap;direction:ltr'>{s}</span></div>" for r, s in roles)
    nt = T(note, 16, '#55607A', 'font-weight:700', 1.6) if note else ""
    return (f"<div style='background:#fff;border-radius:20px;padding:10px 12px 12px;box-sizing:border-box;box-shadow:0 14px 28px #0007;display:flex;flex-direction:column'>"
            f"<div style='display:flex;gap:8px'>{ph}</div>{T(title, 28, COB, 'font-weight:700;margin-top:2px', 1.75)}{rl}"
            f"<div style='margin-top:auto;padding-top:6px;display:flex;align-items:center;justify-content:space-between;gap:8px'>"
            f"<span style='background:{tag_col};border-radius:999px;padding:0 12px'>{T(tag, 16, '#fff', 'font-weight:700', 1.7)}</span>{nt}</div></div>")


def build():
    P = lambda f: (PHOTOS / f).as_uri()
    SELF, CO = "رہائش و کھانا: اپنا", "رہائش و کھانا: کمپنی کی طرف سے"
    a = card("ڈرائیورز اور رائیڈرز", [("driver_taxi.jpg", "center 40%", "cover"), ("kw_rider.jpg", "center 30%", "cover"), ("uz_ecycle_rider_ref.jpg", "center 30%", "cover")],
             [("ٹیکسی ڈرائیورز", "$900 – 1,100"), ("بائیک رائیڈرز", "$1,000 – 1,300"), ("سائیکلسٹ", "$900 – 1,100")], SELF, "#6B7280", "ڈرائیورز کے لیے لائسنس لازمی")
    b = card("فیکٹری اور ٹیلرنگ", [("uz_factory_line_ref.jpg", "center 35%", "cover"), ("kg_tailor_juki.jpg", "62% 30%", "cover")],
             [("فیکٹری ورکرز", "$400 – 500"), ("ٹیلرز", "$500 – 600")], CO, "#1E9E55")
    c = card("انڈسٹریل پلانٹ", [("uz_pir_1_ref.jpg", "center 30%", "cover"), ("uz_pir_2_ref.jpg", "center 30%", "cover"), ("uz_pir_4_ref.jpg", "center 30%", "cover")],
             [(f"{N('PIR')}&nbsp; پینل کیمیکل ٹیکنالوجسٹ", "$1,500"), (f"{N('PIR')}&nbsp; پینل لائن آپریٹر", "$1,500"), ("بیسالٹ لائن آپریٹر", "$1,500"), ("بیسالٹ لائن مکینک", "$1,500")],
             CO, "#1E9E55", f"کم از کم {N(3)} سال تجربہ")
    d = card("انگلش ٹیچرز", [("teacher_man.jpg", "center", "contain"), ("teacher_woman.jpg", "center 30%", "cover")],
             [("انگلش ٹیچرز", "$3,000")], SELF, "#6B7280")
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(30)}<span style='font:400 28px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""<div dir='rtl'>
<div class='abs' style='inset:0;background:{COB};background-image:{tile_bg()}'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:330px;overflow:hidden'><img src='{P("uz_registan_ref.jpg")}' style='width:100%;height:100%;object-fit:cover;object-position:center 45%;transform:scaleX(-1)'>
 <div style='position:absolute;inset:0;background:linear-gradient(270deg,{COB2}f2 0%,{COB2}bb 45%,{COB2}22 75%),linear-gradient(0deg,{COB} 0%,{COB}00 25%)'></div></div>
<div class='abs' style='top:22px;right:30px;background:#fff;border-radius:14px;padding:2px 12px;box-shadow:0 6px 14px #0006'>{logo_img('logo-horizontal-light', 'width:250px;height:64px;object-position:right')}</div>
<div class='abs' style='top:24px;left:30px;filter:drop-shadow(0 6px 10px #0007)'>{flag('uzbekistan', 120, True, 'uzku')}</div>
<div class='abs' style='top:88px;right:40px;width:1000px'>
 <div style='display:inline-block;background:{SAF};border-radius:8px;padding:0 16px'>{T(f"فوری ضرورت · {N(10)} شعبے", 24, INK, 'font-weight:700', 1.65)}</div>
 {T(f"ازبکستان میں کام کریں", 72, '#fff', 'font-weight:700;margin-top:-4px;text-shadow:0 6px 18px #0008', 1.7)}
 {T(f"متعدد آسامیاں · عمر {N(21)} تا {N(42)} سال · تنخواہ تقریباً (ڈالر ماہانہ)", 21, '#DDE5F7', 'font-weight:700;margin-top:4px', 1.7)}</div>

<div class='abs' style='top:306px;left:24px;right:24px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:372px 426px;gap:14px'>{a}{b}{c}{d}</div>

<div class='abs' style='top:1128px;left:24px;right:24px;height:52px;border-radius:14px;background:linear-gradient(270deg,{SAF},{SAF2});display:flex;align-items:center;justify-content:center;gap:10px'>
 {icon('doc', 24, INK, 2.3)}{T(f"کاغذات: پاسپورٹ (اگلا پچھلا صفحہ، {N('PDF')} اسکین) · شناختی کارڈ · اسٹوڈیو تصویر  |  ٹکٹ امیدوار خود لے گا", 18, INK, 'font-weight:700;white-space:nowrap', 1.6)}</div>

<div class='abs' style='top:1192px;left:0;width:1080px;height:158px;background:{COB2}'></div>
<div class='abs' style='top:1192px;left:0;width:1080px;height:5px;background:linear-gradient(90deg,{TQ},{SAF},{TQ})'></div>
<div class='abs' style='top:1208px;left:30px;right:30px;display:grid;grid-template-columns:auto auto auto;justify-content:space-between;gap:6px 0;direction:ltr'>{nums}</div>
<div class='abs' style='top:1290px;left:30px;right:30px;display:flex;justify-content:space-between;align-items:center'>
 {T(f"اپنی {N('CV')} واٹس ایپ کریں", 26, SAF2, 'font-weight:700', 1.7)}
 <span style='display:flex;align-items:center;gap:8px;direction:ltr'>{icon('mail', 22, '#fff', 2)}<span style='font:800 21px Archivo;color:#fff'>{EMAIL}</span></span></div>
</div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{COB}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Uzbekistan-10-Positions-Campaign-Urdu.png"))
