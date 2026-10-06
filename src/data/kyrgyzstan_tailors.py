"""Demand 2026-10-06 (split): experienced tailors for Kyrgyzstan.
Facts: demands/2026-10-06-uzbekistan-combined/facts.md (section C); the user
confirmed the destination country is Kyrgyzstan, and re-sent the source ad: salary $500–$800 monthly."""
from common import C

N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:700;letter-spacing:0'>{v}</span>"

DATA = {
    "stem": "RS-Links-Kyrgyzstan-Tailors",
    "country": "kyrgyzstan",
    "art": "tailor",
    "accent": "#D6202F",
    "layout": {"header_h": 186, "band_h": 170, "title_top": 22, "title_top_ur": 4,
               "scene_h": 512, "circle_r": 172, "circle_cy": 268, "badge_tops": [86, 210, 334],
               "route_top": 458, "doc_h": 74, "doc_gap": 18, "cta_top": 1240},
    "en": {
        "title": "TAILORS REQUIRED",
        "dest": "for Kyrgyzstan",
        "urgent": "URGENT",
        "opener": "Our respected client urgently needs experienced tailors",
        "from": "Pakistan", "to": "Kyrgyzstan",
        "badges_start": [
            {"icon": "money", "label": "MONTHLY SALARY", "value": "$500–$800", "size": 32, "sub": "US dollars"},
            {"icon": "clock", "label": "DUTY", "value": "10 HOURS", "sub": "daily"},
            {"icon": "home", "label": "ACCOMMODATION &amp; FOOD", "value": "By company", "num": False, "sub": "(as per country)"},
        ],
        "badges_end": [
            {"icon": "doc", "label": "CONTRACT", "value": "Legal contract", "num": False},
            {"icon": "medical", "label": "MEDICAL", "value": "Medical facility", "num": False},
            {"icon": "visa", "label": "VISA", "value": "Visa process", "num": False},
        ],
        "docs_title": "DOCUMENTS REQUIRED TO APPLY",
        "documents": [
            ("doc", "CV / Resume"), ("video", "Recent working video"), ("visa", "Passport first page"),
            ("visa", "Passport second page"), ("idcard", "CNIC (front)"), ("idcard", "CNIC (back)"),
            ("camera", "Passport-size photo (white background)"), ("shield", "Police clearance / verification certificate"),
            ("family", "Family Registration Certificate (FRC)"),
        ],
        "apply": "APPLY NOW!",
        "note": "Only serious and experienced candidates should contact.",
    },
    "ur": {
        "title": "ٹیلرز کی ضرورت ہے",
        "dest": "کرغزستان کے لیے",
        "urgent": "فوری",
        "opener": "ہمارے معزز کلائنٹ کو تجربہ کار ٹیلرز کی فوری ضرورت ہے",
        "from": "پاکستان", "to": "کرغزستان",
        "badges_start": [
            {"icon": "money", "label": "ماہانہ تنخواہ", "value": "$500 – $800", "size": 30, "sub": "امریکی ڈالر"},
            {"icon": "clock", "label": "ڈیوٹی کا وقت", "value": f"{N(10)} گھنٹے روزانہ", "num": False},
            {"icon": "home", "label": "رہائش اور کھانا", "value": "کمپنی کی جانب سے", "num": False, "sub": "(ممالک کے مطابق)"},
        ],
        "badges_end": [
            {"icon": "doc", "label": "معاہدہ", "value": "قانونی معاہدہ", "num": False},
            {"icon": "medical", "label": "میڈیکل", "value": "میڈیکل سہولت", "num": False},
            {"icon": "visa", "label": "ویزا", "value": "ویزا پروسس", "num": False},
        ],
        "docs_title": "درخواست کے لیے مطلوبہ دستاویزات",
        "documents": [
            ("doc", f"ریزیومے / {N('CV')}"), ("video", "ریسنٹ ورکنگ ویڈیو"), ("visa", "پاسپورٹ کا پہلا صفحہ"),
            ("visa", "پاسپورٹ کا دوسرا صفحہ"), ("idcard", "شناختی کارڈ (فرنٹ)"), ("idcard", "شناختی کارڈ (بیک)"),
            ("camera", "پاسپورٹ سائز تصویر (سفید بیک گراؤنڈ)"), ("shield", "پولیس کلیئرنس / ویریفکیشن سرٹیفکیٹ"),
            ("family", f"فیملی رجسٹریشن سرٹیفکیٹ ({N('FRC')})"),
        ],
        "apply": "ابھی اپلائی کریں!",
        "note": "صرف سنجیدہ اور تجربہ کار امیدوار رابطہ کریں۔",
    },
}
