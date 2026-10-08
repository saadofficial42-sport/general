"""Demand 2026-10-08: Uzbekistan — Tissue Packing Staff (demands/2026-10-08-uzbekistan-tissue/ref.jpg).
Facts (verbatim): urgent recruitment, new vacancies for Uzbekistan · Job: tissue packing staff ·
salary $350 (for tissue packers) · duty 12 hours (overtime, for tissue packers) · food /
accommodation by company · contract period 1 year.
Not stated: number of posts, city, age, visa, processing time, salary period."""
from common import C

N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"

DATA = {
    "stem": "RS-Links-Uzbekistan-Tissue-Packing-Staff",
    "country": "uzbekistan",
    "photo": "tissue_packer",
    "layout": {"photo_h": 640, "head_top": 330, "head_top_ur": 300, "gap": 18,
               "tile_h": 186, "note_h": 96, "cta_top": 1240},
    "en": {
        "kicker": "URGENT RECRUITMENT · NEW VACANCIES",
        "title": "TISSUE PACKING STAFF",
        "sub": "FOR UZBEKISTAN",
        "tiles": [
            ("money", "SALARY", "$350", "Tissue packers", C["green"], True, 60),
            ("clock", "DUTY", "12 HOURS", "With overtime", "#1E6FCC", True, 52),
            ("home", "FOOD &amp; ACCOMMODATION", "By company", "", "#B7791F", False, 0),
            ("calendar", "CONTRACT", "1 YEAR", "Contract period", C["red"], True, 52),
        ],
        "note": "Pakistan → Uzbekistan",
        "apply": "APPLY TODAY!",
        "apply_sub": "Contact RS Links Consultants on WhatsApp",
    },
    "ur": {
        "kicker": "ازبکستان کے لیے نئی اور فوری بھرتی!",
        "title": "ٹشو پیکنگ اسٹاف",
        "sub": "ازبکستان",
        "tiles": [
            ("money", "تنخواہ", "$350", "ٹشو پیکرز کے لیے", C["green"], True, 60),
            ("clock", "ڈیوٹی", f"{N(12)} گھنٹے", "اوور ٹائم کے ساتھ", "#1E6FCC", False, 0),
            ("home", "کھانا / رہائش", "کمپنی دے گی", "", "#B7791F", False, 0),
            ("calendar", "معاہدہ مدت", f"{N(1)} سال", "", C["red"], False, 0),
        ],
        "note": "پاکستان سے ازبکستان",
        "apply": "آج ہی رابطہ کریں!",
        "apply_sub": "آر ایس لنکس کنسلٹنٹس — واٹس ایپ",
    },
}
