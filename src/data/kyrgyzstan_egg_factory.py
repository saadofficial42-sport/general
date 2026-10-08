"""Demand 2026-10-08: Kyrgyzstan — egg packing factory (demands/2026-10-08-kyrgyzstan-egg-packing/ref.jpg).
Facts (verbatim from source): urgent requirement for Kyrgyzstan · visa in 10 days · opportunity to
work in industry/factory · Egg Packing Factory · Factory Worker (05) · salary $450 (monthly) ·
duty 10 hours daily · age 18 to 50 years · accommodation, medical, transport by the factory ·
all other facilities as per Kyrgyzstan labour law."""
from common import C

N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"

DATA = {
    "stem": "RS-Links-Kyrgyzstan-Egg-Packing-Factory-Workers",
    "country": "kyrgyzstan",
    "art": "egg_packer",
    "accent": "#D6202F",
    "layout": {"header_h": 186, "band_h": 170, "title_top": 22, "title_top_ur": 0,
               "scene_h": 640, "circle_r": 200, "circle_cy": 330, "badge_tops": [96, 262, 428],
               "big_text": True, "badge_w": 300,
               "route_top": 586, "doc_h": 74, "doc_gap": 18, "cta_top": 1240},
    "en": {
        "title": "FACTORY WORKERS",
        "dest": "for Kyrgyzstan",
        "urgent": "URGENT",
        "opener": "EGG PACKING FACTORY · Work in industry / factory",
        "from": "Pakistan", "to": "Kyrgyzstan",
        "badges_start": [
            {"icon": "money", "label": "MONTHLY SALARY", "value": "$450", "size": 50, "sub": "per month", "color": C["green"]},
            {"icon": "clock", "label": "DUTY", "value": "10 HOURS", "size": 40, "sub": "daily", "color": C["green"]},
            {"icon": "user", "label": "AGE LIMIT", "value": "18 – 50", "size": 40, "sub": "years", "color": C["green"]},
        ],
        "badges_end": [
            {"icon": "home", "label": "ACCOMMODATION", "value": "By factory", "num": False},
            {"icon": "medical", "label": "MEDICAL", "value": "By factory", "num": False},
            {"icon": "bus", "label": "TRANSPORT", "value": "By factory", "num": False},
        ],
        "highlights": [
            ("user", "05 POSTS", "Factory Worker", C["navy"]),
            ("visa", "VISA IN 10 DAYS", "Kyrgyzstan visa", "#D6202F"),
            ("shield", "LABOUR LAW", "All other facilities as per Kyrgyzstan labour law", C["green"]),
        ],
        "apply": "APPLY NOW!",
        "note": "Contact RS Links Consultants on WhatsApp.",
    },
    "ur": {
        "title": "فیکٹری ورکرز کی ضرورت",
        "dest": "کرغزستان کے لیے",
        "urgent": "فوری",
        "opener": "ایگ پیکنگ فیکٹری — انڈسٹری / فیکٹری میں کام کا موقع",
        "from": "پاکستان", "to": "کرغزستان",
        "badges_start": [
            {"icon": "money", "label": "تنخواہ (ماہانہ)", "value": "$450", "size": 48, "color": C["green"]},
            {"icon": "clock", "label": "ڈیوٹی", "value": f"{N(10)} گھنٹے روزانہ", "num": False, "color": C["green"]},
            {"icon": "user", "label": "عمر کی حد", "value": f"{N('18 – 50')} سال", "num": False, "color": C["green"]},
        ],
        "badges_end": [
            {"icon": "home", "label": "رہائش", "value": "فیکٹری کی طرف سے", "num": False},
            {"icon": "medical", "label": "میڈیکل", "value": "فیکٹری کی طرف سے", "num": False},
            {"icon": "bus", "label": "ٹرانسپورٹ", "value": "فیکٹری کی طرف سے", "num": False},
        ],
        "highlights": [
            ("user", f"{N('05')} آسامیاں", "فیکٹری ورکر", C["navy"]),
            ("visa", f"{N(10)} دن میں ویزہ", "کرغزستان ویزہ", "#D6202F"),
            ("shield", "لیبر لاء", "دیگر تمام سہولیات کرغزستان لیبر لاء کے مطابق", C["green"]),
        ],
        "apply": "ابھی اپلائی کریں!",
        "note": "آر ایس لنکس کنسلٹنٹس سے واٹس ایپ پر رابطہ کریں",
    },
}
