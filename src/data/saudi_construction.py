"""Demand 2026-10-13: Saudi Arabia — construction trades + NAVTTC-certified workers
(demands/2026-10-13-saudi-construction/). Facts from the source ad:
 Building Electrician 8 · Plumber 10 · Building Painter 10 · Shuttering Carpenter 10 · Steel Fixer 10,
 each 1200 + 300 Riyal. NAVTTC block (source printed "NewTech"; user: it's NAVTCC = NAVTTC):
 loading/unloading workers & construction workers, 1200 + 300, total salary 1500 Riyal, age 21–37 (no count).
 Duty 9 hours · contract 2 years · accommodation, medical, transport by company · other benefits per
 local labour law · bring complete documents · CV selection ongoing · urgent visa · immediate departure.
 Employer name in the source is omitted per RS Links ad rules."""
from common import C

N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"
GREEN = "#006C35"

DATA = {
    "stem": "RS-Links-Saudi-Arabia-Construction-Trades",
    "country": "saudi",
    "green": GREEN,
    "hero_photo": "saudi_construction_hero",   # drop a real photo here to replace the silhouette scene
    "phones": ["+92 317 0363690", "+92 371 9051589"],   # 0317 first (user, 2026-10-13)
    "layout": {"header_h": 150, "hero_h": 440, "head_top": 30, "head_top_ur": 10, "gap": 14,
               "thead_h": 48, "row_h": 64, "table_w": 640, "term_h": 96, "note_h": 84, "cta_top": 1222},
    "en": {
        "kicker": "URGENT REQUIREMENT",
        "country": "SAUDI ARABIA",
        "badges": ["URGENT VISA", "IMMEDIATE DEPARTURE"],
        "opener": "A renowned company in Saudi Arabia requires:",
        "th": ["POSITION", "POSTS", "SALARY"],
        "rows": [("bolt", "Building Electrician", "08"), ("wrench", "Plumber", "10"), ("roller", "Building Painter", "10"),
                 ("hammer", "Shuttering Carpenter", "10"), ("rebar", "Steel Fixer", "10")],
        "cert_word": "CERTIFIED",
        "cert_roles": [("box", "Loading &amp; Unloading Workers"), ("crane", "Construction Workers")],
        "total_label": "TOTAL SALARY",
        "basic": "1200 + 300 SAR",
        "age": "Age: 21 – 37 Years",
        "terms": [("clock", "DUTY", "9 Hours", 26, 0.9), ("calendar", "CONTRACT", "2 Years", 26, 0.9),
                  ("home", "BY COMPANY", "Accommodation, Medical, Transport", 19, 1.6),
                  ("doc", "OTHER BENEFITS", "As per Saudi labour law", 19, 1.25)],
        "docs": "Bring your complete documents",
        "cv": "CV SELECTION ONGOING",
        "apply": "APPLY NOW!",
    },
    "ur": {
        "kicker": "فوری ضرورت",
        "country": "سعودی عرب",
        "badges": ["فوری ویزہ", "فوری روانگی"],
        "opener": "سعودی عرب کی ایک معروف کمپنی کے لیے درج ذیل افراد درکار ہیں:",
        "th": ["عہدہ", "آسامیاں", "تنخواہ"],
        "rows": [("bolt", "بلڈنگ الیکٹریشن", "08"), ("wrench", "پلمبر", "10"), ("roller", "بلڈنگ پینٹر", "10"),
                 ("hammer", "شٹرنگ کارپینٹر", "10"), ("rebar", "اسٹیل فکسر", "10")],
        "cert_word": "سرٹیفائیڈ",
        "cert_roles": [("box", "لوڈنگ اَن لوڈنگ ورکرز"), ("crane", "کنسٹرکشن ورکرز")],
        "total_label": "کل تنخواہ",
        "basic": "1200 + 300 SAR",
        "age": f"عمر: {N('21 – 37')} سال",
        "terms": [("clock", "ڈیوٹی", f"{N(9)} گھنٹے", 26, 0.9), ("calendar", "معاہدہ", f"{N(2)} سال", 26, 0.9),
                  ("home", "کمپنی کی طرف سے", "رہائش، میڈیکل، ٹرانسپورٹ", 21, 1.6),
                  ("doc", "دیگر مراعات", "مقامی لیبر لاء کے مطابق", 21, 1.25)],
        "docs": "اپنے مکمل کاغذات کے ہمراہ تشریف لائیں",
        "cv": "سی وی سلیکشن جاری ہے",
        "apply": "ابھی اپلائی کریں!",
    },
}
