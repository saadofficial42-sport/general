"""2026-10-14: Uzbekistan factory workers — new ad (user request). New from user today: accommodation,
food and transport FREE; ticket by the company (replaces the earlier "ticket from Punjab" note).
Other facts reused from the 2026-10-06 factory demand (demands/2026-10-06-uzbekistan-combined, section B):
Tashkent & Samarkand · 50 posts · hosiery, packing, ironing, shifting goods · $400 · duty 10 hours + overtime ·
age 21–35 · visa B-2 · processing 30–35 days · medical · other benefits per local labour law. Urdu only."""
from common import WHATSAPP

N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"

DATA = {
    "stem": "RS-Links-Uzbekistan-Factory-Workers-v3",
    "country": "uzbekistan",
    "photo": "uz_factory",            # real photo slot (shared with the all-jobs ad)
    "scene": "factory",
    "palette": {"char": "#0B2E44", "char2": "#0B3E5C", "em": "#0A8FB0", "gold": "#F0B443", "tiles_from": "#0B4F6C"},
    "phones": ["+92 317 0363690", WHATSAPP],
    "email": "hr@rslinksconsultants.com",
    "layout": {"header_h": 140, "hero_h": 400, "pic_w": 470, "title_top": 22, "tiles_h": 120, "gap": 14,
               "li_gap_ur": 16, "li_px_ur": 26, "li_lh_ur": 1.75, "cta_top": 1196},
    "ur": {
        "urgent": "فوری ضرورت",
        "kicker": "فوری ضرورت برائے ازبکستان",
        "title": "فیکٹری ورکرز",
        "title_en": "FACTORY WORKERS",
        "where": "تاشقند اور ثمرقند",
        "opener": "بہتر مستقبل کی جانب ایک مضبوط قدم",
        "tiles": [("money", "تنخواہ", "$400", True, 40, "امریکی ڈالر", 1.05),
                  ("user", "آسامیاں", "50", True, 40, "", .8),
                  ("clock", "ڈیوٹی", f"{N(10)} گھنٹے", False, 0, "+ اوور ٹائم", 1.05),
                  ("calendar", "عمر", f"{N('21 – 35')} سال", False, 0, "", 1.05),
                  ("visa", "ویزا", "B-2", True, 36, "", .8)],
        "duties_title": "کام کی نوعیت",
        "duties": ["ہوزری ورکرز", "پیکنگ", "استری (آئرننگ)", "سامان شفٹ کرنا",
                   f"پروسیسنگ ٹائم: {N('30 – 35')} دن", f"ویزا کیٹیگری: {N('B-2')}"],
        "req_title": "مفت سہولیات",
        "reqs": ["رہائش مفت", "کھانا مفت", "ٹرانسپورٹ مفت", "ٹکٹ کمپنی کی طرف سے",
                 "میڈیکل کی سہولت", "دیگر مراعات مقامی لیبر لاء کے مطابق"],
        "apply": "ابھی رابطہ کریں!",
        "apply_sub": f"اپنی {N('CV')} اور کاغذات نیچے دیے گئے نمبرز پر واٹس ایپ کریں",
    },
}
