"""Urdu version of saudi_technical.py (same facts, same layout family, RTL)."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon
from saudi_technical import ADDRESS, EMAIL, GOLD, NAVY, NAVY2, SECTIONS, TEAL

UR_TITLES = {"MECHANICAL": "مکینیکل", "ELECTRONICS": "الیکٹرانکس", "ELECTRICAL": "الیکٹریکل", "CIVIL": "سول"}
UR_JOBS = ["لانڈری ایکوپمنٹ ٹیکنیشن", "بوائلر ٹیکنیشن", "فائر فائٹنگ ٹیکنیشن", "جنریٹر مکینیکل ٹیکنیشن", "لانڈری ایکوپمنٹ آپریٹر",
           "میڈیکل گیس ٹیکنیشن", "<span class=num>STP / WTP</span> ٹیکنیشن", "<span class=num>HVAC</span> ٹیکنیشن", "چلر ٹیکنیشن", "<span class=num>STP / WTP</span> آپریٹر",
           "آڈیو اینڈ ویڈیو ٹیکنیشن", "<span class=num>CCTV</span> ٹیکنیشن", "فائر الارم ٹیکنیشن", "ٹیلیفون اینڈ نیٹ ورکنگ ٹیکنیشن",
           "ایلیویٹر (لفٹ) ٹیکنیشن", "جنریٹر الیکٹریکل ٹیکنیشن", "گارڈنر ٹیکنیشن", "فرنیچر کارپینٹر"]
T = lambda s, px, c, extra="", lh=1.7: f"<div class='t' style='font-size:{px}px;color:{c};line-height:{lh};{extra}'>{s}</div>"


def table(title, ic, color, rows, names, rh=42):
    head = (f"<div style='display:flex;align-items:center;gap:10px;padding:0 14px;height:52px;background:{color}'>{icon(ic, 26, NAVY, 2.4)}"
            f"{T(UR_TITLES[title], 28, NAVY, 'font-weight:700', 1.6)}"
            f"<span style='margin-inline-start:auto'>{T('آسامیاں • تنخواہ (ریال)', 15, NAVY, 'font-weight:700', 1.5)}</span></div>")
    body = "".join(
        f"<div style='display:flex;align-items:center;height:{rh}px;padding:0 14px;background:{'#ffffff0c' if i % 2 else 'transparent'}'>"
        f"<div style='flex:1;min-width:0'>{T(nm, 18, '#fff', 'font-weight:700;white-space:nowrap', 1.6)}</div>"
        f"<span class='num' style='width:44px;text-align:center;font-size:22px;color:{color}'>{h}</span>"
        f"<span class='num' style='width:118px;text-align:left;font-size:22px;color:#fff'>{s} <span style='color:{GOLD}'>+ 200</span></span></div>"
        for i, ((_, h, s), nm) in enumerate(zip(rows, names)))
    return f"<div style='background:{NAVY2};border-radius:18px;overflow:hidden;border:1.5px solid {color}66'>{head}{body}</div>"


def build():
    total = sum(h for *_, rows in SECTIONS for _, h, _ in rows)
    it = iter(UR_JOBS); names = [[next(it) for _ in sec[3]] for sec in SECTIONS]
    tb = [table(*SECTIONS[i], names[i]) for i in range(4)]
    nums = "".join(f"<div class='num' style='display:block;font-size:34px;color:{NAVY};line-height:1.06'>{n}</div>" for n in PHONES)
    facts = "".join(f"<div style='flex:1;display:flex;align-items:center;gap:10px;padding:0 12px;border-inline-start:{'0' if i == 0 else '2px solid #0A1F3322'}'>"
                    f"{icon(ic, 30, TEAL, 2.2)}<div>{T(l, 15, '#5A6B7B', 'font-weight:700', 1.5)}{T(v, 21, NAVY, 'font-weight:700', 1.5)}</div></div>"
                    for i, (ic, l, v) in enumerate((("clock", "ڈیوٹی", "<span class=num>8</span> گھنٹے روزانہ"), ("calendar", "معاہدہ", "<span class=num>2</span> سال"),
                                                     ("user", "عمر کی حد", "<span class=num>35</span> سال تک"), ("food", "فوڈ الاؤنس", "<span class=num>200</span> ریال شامل"),
                                                     ("home", "رہائش و سہولیات", "فراہم"))))
    prov = "".join(f"<div style='display:flex;align-items:center;gap:10px;margin-top:4px'>{icon(ic, 26, GOLD, 2.4)}{T(t, 22, '#fff', 'font-weight:700', 1.9)}</div>"
                   for ic, t in (("home", "رہائش اور دیگر سہولیات کمپنی کی طرف سے"), ("food", "فوڈ الاؤنس شامل (<span class=num>+200</span> ریال)"),
                                 ("check", "دیگر مراعات سعودی لیبر لاء کے مطابق")))
    photo = (PHOTOS / "rslinks_construction_engineer.png").as_uri()
    grid = "".join(f"<path d='M{x} 0 V1350'/>" for x in range(0, 1080, 36)) + "".join(f"<path d='M0 {y} H1080'/>" for y in range(0, 1350, 36))
    body = f"""
<div class='abs' style='inset:0;background:linear-gradient(170deg,#0F2B47,{NAVY} 45%,#06121F)'></div>
<svg class='abs' style='left:0;top:0' width='1080' height='1350'><g stroke='#ffffff08' stroke-width='1'>{grid}</g></svg>
<div class='abs' style='left:0;top:0;width:380px;height:330px;overflow:hidden;clip-path:polygon(0 0,100% 0,82% 100%,0 100%)'>
 <img src='{photo}' style='width:100%;height:100%;object-fit:cover;object-position:center 70%'>
 <div class='abs' style='inset:0;background:linear-gradient(270deg,{NAVY}aa,#0000 40%)'></div></div>
<div class='abs' style='left:20px;top:18px;filter:drop-shadow(0 4px 8px #0008)'>{flag('saudi', 120, True, 'tsau')}</div>
<div class='abs' style='right:30px;top:22px;background:#fff;border-radius:16px;padding:4px 14px'>{logo_img('logo-horizontal-light', 'width:340px;height:84px')}</div>
<div class='abs' style='right:32px;top:118px;width:660px;text-align:right'>
 <div style='display:inline-block;background:{GOLD};padding:0 16px 6px;border-radius:8px'>{T('فوری ضرورت برائے سعودی عرب', 22, NAVY, 'font-weight:700', 1.7)}</div>
 {T('ٹیکنیکل اور <span style="color:#18A39A">مینٹیننس</span> اسٹاف', 58, '#fff', 'font-weight:700;margin-top:34px', 1.4)}</div>
<div class='abs' style='right:24px;top:344px;width:548px'>{tb[0]}</div>
<div class='abs' style='left:24px;top:344px;width:470px;display:flex;flex-direction:column;gap:12px'>{tb[1]}{tb[2]}{tb[3]}</div>
<div class='abs' style='left:24px;top:914px;width:470px;height:142px;border-radius:18px;background:{GOLD};display:flex;flex-direction:column;align-items:center;justify-content:center'>
 <div style='display:flex;align-items:baseline;gap:12px'><span class='num' style='font-size:76px;color:{NAVY};line-height:1'>{total}</span>{T('آسامیاں', 46, NAVY, 'font-weight:700', 1.4)}</div>
 {T('<span class=num>18</span> عہدے • تنخواہ ریال + <span class=num>200</span> فوڈ الاؤنس', 18, NAVY, 'font-weight:700;margin-top:14px', 1.6)}</div>
<div class='abs' style='right:24px;top:836px;width:548px;height:220px;border-radius:18px;background:{NAVY2};border:1.5px solid {TEAL}66;padding:6px 18px;box-sizing:border-box'>
 {T('کمپنی کی طرف سے سہولیات', 24, TEAL, 'font-weight:700', 1.6)}{prov}</div>
<div class='abs' style='left:24px;right:24px;top:1068px;height:98px;background:#fff;border-radius:18px;display:flex;align-items:center;padding:0 6px'>{facts}</div>
<div class='abs' style='left:0;top:1176px;width:1080px;height:174px;background:{TEAL}'></div>
<div class='abs' style='left:24px;top:1190px;height:128px;background:#fff;border-radius:22px;display:flex;align-items:center;gap:12px;padding:0 22px 0 12px;box-shadow:0 8px 18px #0005;direction:ltr'>{whatsapp_icon(66)}<div>{nums}</div></div>
<div class='abs' style='right:30px;top:1196px;width:600px;text-align:right'>
 {T('اپنی <span class=num>CV</span> بھیجیں — واٹس ایپ یا ای میل', 30, NAVY, 'font-weight:700', 1.8)}
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;direction:ltr;margin-top:14px'>{icon('mail', 24, NAVY, 2.2)}<span style='font-family:Archivo;font-size:24px;font-weight:800;color:{NAVY}'>{EMAIL}</span></div></div>
<div class='abs' style='left:0;bottom:0;width:1080px;height:30px;background:{NAVY};display:flex;align-items:center;justify-content:center;gap:8px;direction:ltr'>
 {icon('pin', 18, GOLD, 2.4)}<span style='font-family:Archivo;font-size:16px;font-weight:700;color:#fff'>{ADDRESS}</span></div>"""
    return (f"<!doctype html><html lang='ur' dir='rtl'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.t{{font-family:'Nastaliq',serif}}.num{{font-family:'Anton','Nastaliq',sans-serif;direction:ltr;unicode-bidi:isolate;display:inline-block;letter-spacing:.5px}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Saudi-Arabia-Technical-Maintenance-Staff-Urdu.png"))
