"""Demand 2026-10-14: Saudi Arabia — Lineman Grade 1 & Grade 2 (demands/2026-10-14-saudi-lineman/ref.jpg —
another agency's ad, content source only: no layout/photos/logo/licence/employer name reused).
Facts: Lineman Grade 1 salary 1900 + food · Grade 2 salary 1500 + food (currency not printed; shown as SAR) ·
interview in Lahore 15 Oct 2026 (Thursday) & 16 Oct 2026 (Friday) · duty 8 hours · age 21–35 ·
medical, transport, accommodation · other benefits per Saudi labour law. No post counts in source. Urdu only."""
from common import WHATSAPP

N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"

DATA = {
    "stem": "RS-Links-Saudi-Arabia-Lineman",
    "country": "saudi",
    "photo": "lineman_tower",      # drop a real photo here to replace the silhouette scene
    "phones": ["+92 317 0363690", WHATSAPP],
    "email": "hr@rslinksconsultants.com",
    "layout": {"header_h": 140, "hero_h": 440, "head_top": 40, "gap": 14, "grade_h": 170, "grade_head_h": 64,
               "info_h": 250, "int_w": 440, "bar_h": 72, "cta_top": 1146},
    "ur": {
        "urgent": "فوری ضرورت",
        "kicker": "فوری ضرورت برائے سعودی عرب",
        "title": "لائن مین",
        "opener": "سعودی عرب کی ایک معروف کمپنی کے لیے",
        "role": "لائن مین",
        "grade_word": "گریڈ",
        "grades": [("1", "1900"), ("2", "1500")],
        "food": "کھانا",
        "int_title": "انٹرویو شیڈول",
        "int_city": "لاہور",
        "dates": [("15", "اکتوبر", "بروز جمعرات"), ("16", "اکتوبر", "بروز جمعہ")],
        "facts": [("clock", "ڈیوٹی ٹائم", f"{N('08')} گھنٹے"), ("user", "عمر", f"{N('21')} سے {N('35')} سال")],
        "benefits": [("medical", "میڈیکل"), ("bus", "ٹرانسپورٹ"), ("home", "رہائش"), ("doc", "باقی مراعات سعودی لیبر لاء کے مطابق")],
        "apply": "ابھی رابطہ کریں!",
        "apply_sub": f"اپنی {N('CV')} واٹس ایپ کریں اور انٹرویو کے لیے رجسٹر ہوں",
    },
}
