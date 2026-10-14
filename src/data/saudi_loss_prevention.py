"""Demand 2026-10-14: Saudi Arabia — Loss Prevention Officer (demands/2026-10-14-saudi-loss-prevention/ref.jpg,
another agency's ad used as a content source only: its layout, photo, logos and employer name are not reused).
Facts: across all regions in KSA · base salary SAR 1,300 · meal allowance SAR 200 · duty 8+1 hours incl. 1 hour
break · weekly rest as per company policy · visa: Istiqdam · 9 duties · requirements: high school diploma minimum,
operational knowledge (vendor receiving, documentation verification, warehouse & retail processes), honesty /
discipline / responsibility, physically fit & alert, basic English or Arabic, experience preferred.
Not in source: number of posts, age, contract length, accommodation, ticket, medical.
Urdu only (user request)."""
from common import WHATSAPP

N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"

DATA = {
    "stem": "RS-Links-Saudi-Arabia-Loss-Prevention-Officer",
    "country": "saudi",
    "photo": "loss_prevention_officer",   # drop a real photo here to replace the placeholder scene
    "phones": ["+92 317 0363690", WHATSAPP],
    "email": "hr@rslinksconsultants.com",
    "layout": {"header_h": 140, "hero_h": 400, "pic_w": 470, "title_top": 26, "tiles_h": 120, "gap": 14,
               "li_gap_ur": 8, "li_px_ur": 19, "li_lh_ur": 1.75, "cta_top": 1196},
    "ur": {
        "urgent": "فوری ضرورت",
        "kicker": "سعودی عرب کی ایک معروف ریٹیل کمپنی کے لیے",
        "title": "لاس پریوینشن آفیسر",
        "title_en": "LOSS PREVENTION OFFICER",
        "where": "سعودی عرب کے تمام ریجنز میں",
        "opener": "اثاثوں کی حفاظت اور اسٹور و ویئر ہاؤس کے بہترین نظم و نسق کا حصہ بنیں",
        "tiles": [("money", "بنیادی تنخواہ", "1300 SAR", True, 36, "", 1.25),
                  ("food", "کھانے کا الاؤنس", "200 SAR", True, 36, "", 1.05),
                  ("clock", "ڈیوٹی", "8 + 1", True, 36, f"{N(1)} گھنٹہ وقفہ شامل", 1.05),
                  ("calendar", "ہفتہ وار چھٹی", "کمپنی پالیسی کے مطابق", False, 0, "", 1.45),
                  ("visa", "ویزا", "استقدام", False, 0, "", .7)],
        "duties_title": "ذمہ داریاں",
        "duties": ["وینڈرز سے آنے والے سامان کی وصولی کی نگرانی و تصدیق",
                   "اسٹور اور ویئر ہاؤس کی نگرانی، چوری و نقصان کی روک تھام",
                   "ڈیلیوری کا پرچیز آرڈر اور انوائس سے موازنہ",
                   "کمی، نقصان یا مشکوک سرگرمی کی فوری رپورٹ",
                   "سیلز فلور، اسٹاک روم اور ویئر ہاؤس میں باقاعدہ گشت",
                   "اسٹاک کی ہینڈلنگ اور اسٹوریج کے طریقہ کار کی نگرانی",
                   "اندرونی و بیرونی نقصان کی تحقیقات میں معاونت",
                   "روزانہ رپورٹس کی درست اور بروقت تیاری",
                   "کمپنی پالیسی اور حفاظتی قواعد پر عمل درآمد"],
        "req_title": "مطلوبہ اہلیت",
        "reqs": ["تعلیم: کم از کم ہائی اسکول ڈپلومہ",
                 "وینڈر ریسیونگ، دستاویزات کی تصدیق، ویئر ہاؤس اور ریٹیل اسٹور کے کام کی سمجھ",
                 "ایمانداری، نظم و ضبط اور ذمہ داری",
                 "جسمانی طور پر فٹ اور ہر وقت چوکس",
                 "انگریزی یا عربی میں بنیادی بات چیت",
                 "لاس پریوینشن، ویئر ہاؤس یا ریٹیل کا تجربہ رکھنے والوں کو ترجیح"],
        "apply": "ابھی اپلائی کریں!",
        "apply_sub": f"اپنی {N('CV')} واٹس ایپ یا ای میل کریں",
    },
}
