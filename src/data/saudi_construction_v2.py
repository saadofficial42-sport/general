"""2026-10-13: Saudi Arabia construction — redesign of the user's own ad
(demands/2026-10-13-saudi-construction/user-ad-v2-source.jpg), same content, new theme.
Content from the user's ad: Electrician 08, Plumber 10, Painter 10, Shuttering Carpenter 10,
Steel Fixer 10, each 1200 + 300 SAR · facilities: accommodation,
food 3 times, medical, transport, kitchen facility · 2-year contract · duty 9 hours · age 21–37 ·
best salary in Saudi Riyal · bring complete documents · urgent CV selection.
Phone order per user: 0317 first."""
from common import WHATSAPP

N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"

DATA = {
    "stem": "RS-Links-Saudi-Arabia-Construction-Navy",
    "country": "saudi",
    "photo": "rslinks_construction_engineer",
    "tagline": "Your Future, Our Priority",
    "trust_en": "BUILD YOUR FUTURE WITH US",
    "phones": ["+92 317 0363690", WHATSAPP],
    "email": "hr@rslinksconsultants.com",
    "address": "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi",
    "layout": {"header_h": 130, "hero_h": 420, "photo_w": 330, "head_top": 22, "head_top_ur": 14, "gap": 12,
               "card_h": 124, "fac_h": 54, "fac_block_h": 226, "bar_h": 62, "cta_top": 1150},
    "en": {
        "sticker": ["BETTER", "FUTURE", "APPLY TODAY"],
        "title_a": "SAUDI ARABIA", "title_b": "URGENT HIRING",
        "field": "Top opportunities in construction",
        "ribbon": "A golden opportunity to work with a renowned &amp; reputable Saudi company",
        "posts": "POSTS",
        "jobs": [("bolt", "Electrician", "", "08"), ("wrench", "Plumber", "", "10"), ("roller", "Painter", "", "10"),
                 ("hammer", "Shuttering Carpenter", "", "10"), ("rebar", "Steel Fixer", "", "10")],
        "best": ["BEST SALARY", "Paid in Saudi Riyal"],
        "fac_title": "FACILITIES BY THE COMPANY",
        "facilities": [("home", "Accommodation"), ("food", "Food (3 times a day)"),
                       ("medical", "Medical facility"), ("bus", "Transport"), ("gear", "Kitchen facility"),
                       ("check", "Other benefits as per labour law"),
                       ("clock", "Duty: 9 hours"), ("calendar", "Contract: 2 years"), ("user", "Age limit: 21 – 37 years")],
        "docs": "Bring your complete documents",
        "cv": "URGENT CV SELECTION",
        "apply": "APPLY NOW!",
        "trust": ["AUTHENTIC", "TRANSPARENT", "RELIABLE"],
    },
    "ur": {
        "sticker": ["مستقبل بہتر", "آج ہی", "اپلائی کریں"],
        "title_a": "سعودی عرب", "title_b": "فوری بھرتی",
        "field": "کنسٹرکشن فیلڈ میں بہترین مواقع",
        "ribbon": "معروف اور معتبر سعودی کمپنی کے ساتھ کام کرنے کا سنہری موقع",
        "posts": "آسامیاں",
        "jobs": [("bolt", "الیکٹریشن", "Electrician", "08"), ("wrench", "پلمبر", "Plumber", "10"), ("roller", "پینٹر", "Painter", "10"),
                 ("hammer", "شٹرنگ کارپینٹر", "Shuttering Carpenter", "10"), ("rebar", "اسٹیل فکسر", "Steel Fixer", "10")],
        "best": ["بہترین تنخواہ", "سعودی ریال میں"],
        "fac_title": "کمپنی کی طرف سے سہولیات",
        "facilities": [("home", "رہائش کمپنی کی طرف سے"), ("food", f"کھانا ({N(3)} وقت)"),
                       ("medical", "میڈیکل کی سہولت"), ("bus", "ٹرانسپورٹ"), ("gear", "کچن کی سہولت"),
                       ("check", "دیگر مراعات لیبر لاء کے مطابق"),
                       ("clock", f"ڈیوٹی: {N(9)} گھنٹے"), ("calendar", f"کنٹریکٹ: {N(2)} سال"), ("user", f"عمر کی حد: {N('21 – 37')} سال")],
        "docs": "اپنے مکمل دستاویزات ساتھ لائیں",
        "cv": f"فوری {N('CV')} سلیکشن",
        "apply": "اپنی درخواست دیں!",
        "trust": ["مستند", "شفاف", "قابلِ اعتماد"],
    },
}
