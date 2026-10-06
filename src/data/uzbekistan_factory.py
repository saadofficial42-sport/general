"""Demand 2026-10-06: Uzbekistan factory workers (Tashkent & Samarkand).
Source: demands/2026-10-06-uzbekistan-combined/ref-factory.jpg (re-sent by user as "Uzbekistan").
Facts: section B of facts.md."""
from common import C

N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"

DATA = {
    "stem": "RS-Links-Uzbekistan-Factory-Workers",
    "layout": {"scene_h": 690, "head_top": 160, "head_top_ur": 140, "cities_top": 598,
               "details_top": 836, "details_h": 146, "fac_top": 1042, "note_top": 1160, "cta_top": 1240},
    "en": {
        "kicker": "URGENT REQUIREMENT FOR",
        "country": "UZBEKISTAN",
        "subhead": "FACTORY WORKERS",
        "cities": "Tashkent &amp; Samarkand",
        "posts_label": "TOTAL", "posts_n": "50", "posts_word": "POSTS",
        "jobs_title": "JOBS",
        "jobs": [("sock", "Hosiery Workers"), ("box", "Packing"), ("iron", "Ironing"), ("dolly", "Shifting Goods")],
        "jobs_note": "Work includes packing, ironing, shifting goods, etc.",
        "details_title": "SALARY &amp; DETAILS",
        "salary": {"label": "SALARY", "value": "$400", "sub": "US dollars"},
        "details": [("clock", "DUTY", "10 Hours + Overtime"),
                    ("user", "AGE LIMIT", "21 – 35 Years"),
                    ("calendar", "PROCESSING TIME", "30 – 35 Days"),
                    ("visa", "VISA CATEGORY", "B-2")],
        "fac_title": "FACILITIES",
        "facilities": [("home", "Accommodation", 1), ("medical", "Medical", 0.85),
                       ("bus", "Transport by company", 1.1), ("gift", "Other benefits as per local labour law", 2.1)],
        "note": "Note: Ticket from Punjab",
        "tagline": "Uzbekistan — New Destination, New Opportunities",
        "apply": "APPLY NOW!",
        "apply_sub": "A strong step towards a better future.",
    },
    "ur": {
        "kicker": "فوری ضرورت برائے",
        "country": "ازبکستان",
        "subhead": "فیکٹری ورکرز",
        "cities": "تاشقند اور ثمرقند",
        "posts_label": "تعداد", "posts_n": "50", "posts_word": "آسامیاں",
        "jobs_title": "ملازمتیں",
        "jobs": [("sock", "ہوزری ورکرز"), ("box", "پیکنگ"), ("iron", "استری کرنا"), ("dolly", "سامان شفٹ کرنا")],
        "jobs_note": "جس میں پیکنگ، استری کرنا، سامان شفٹ کرنا وغیرہ شامل ہوگا۔",
        "details_title": "تنخواہ و دیگر تفصیلات",
        "salary": {"label": "تنخواہ", "value": "$400", "sub": "ڈالر"},
        "details": [("clock", "ڈیوٹی", f"{N(10)} گھنٹے + اوور ٹائم"),
                    ("user", "عمر کی حد", f"{N('21 – 35')} سال"),
                    ("calendar", "پروسیسنگ ٹائم", f"{N('30 – 35')} دن"),
                    ("visa", "ویزا کیٹیگری", N("B-2"))],
        "fac_title": "سہولیات",
        "facilities": [("home", "رہائش", 0.8), ("medical", "میڈیکل", 0.8),
                       ("bus", "ٹرانسپورٹ بذمہ کمپنی", 1.2), ("gift", "دیگر مراعات مقامی لیبر لاء کے مطابق", 1.7)],
        "note": "نوٹ: ٹکٹ پنجاب سے ہوگا",
        "tagline": "ازبکستان — نئی منزل، نئے مواقع",
        "apply": "ابھی اپلائی کریں!",
        "apply_sub": "بہتر مستقبل کی جانب ایک مضبوط قدم",
    },
}
