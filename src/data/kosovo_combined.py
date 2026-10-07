"""Demand 2026-10-07: Kosovo — three source ads combined (demands/2026-10-07-kosovo/).
Facts (verbatim from the sources):
 Ad 1: General Factory Worker 15, CE Category Driver 3, Precast Concrete Installation Worker 10
       (total 28) · Male · Salary minimum 500€ · Nationality Pakistan · Age limit none
 Ad 2: Cleaning General Worker 04 · Male · Salary minimum 500€ · Pakistan · Age limit none
 Ad 3: General Factory Worker 16 · Male · Salary €500–€700 · Pakistan · Age 25–50 years
 All: Accommodation free · Total hours 8 · Days in week 5–6 · Bonus & overtime as per law
The two General Factory Worker demands have different salary/age terms, so they are
kept as separate rows (not summed). Total = 15+3+10+4+16 = 48."""
from common import C

N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"

DATA = {
    "stem": "RS-Links-Kosovo-All-Jobs",
    "country": "kosovo",
    "blue": "#244AA5",
    "gold": "#F0C850",
    "layout": {"header_h": 168, "hero_h": 268, "title_top": 22, "title_top_ur": 0, "seal_top": 14,
               "gap": 14, "thead_h": 50, "row_h": 76, "total_h": 54, "term_h": 90,
               "cols": [130, 200, 170], "cta_top": 1240},
    "en": {
        "kicker": "URGENT REQUIREMENT",
        "title_a": "WORK IN", "title_b": "KOSOVO",
        "tagline": "Build your future with great opportunities!",
        "from": "Pakistan", "to": "Kosovo",
        "total_n": "48", "total_label": "TOTAL<br>VACANCIES",
        "th": ["POSITION", "VACANCIES", "SALARY", "AGE LIMIT"],
        "rows": [
            {"art": "factory", "name": "General Factory Worker", "posts": "15",
             "sal_label": "Minimum", "salary": "€500", "age": "None"},
            {"art": "ce_truck", "name": "CE Category Driver", "posts": "03",
             "sal_label": "Minimum", "salary": "€500", "age": "None"},
            {"art": "precast", "name": "Precast Concrete Installation Worker", "posts": "10",
             "sal_label": "Minimum", "salary": "€500", "age": "None"},
            {"art": "cleaner", "name": "Cleaning General Worker", "posts": "04",
             "sal_label": "Minimum", "salary": "€500", "age": "None"},
            {"art": "factory", "name": "General Factory Worker", "posts": "16",
             "salary": "€500 – €700", "sal_px": 26, "age": "25 – 50 Years"},
        ],
        "total_row": "Total Vacancies",
        "terms_title": "FACILITIES &amp; T&amp;C · ALL POSITIONS",
        "terms": [("male", "GENDER", "Male", None),
                  ("user", "NATIONALITY", "Pakistan", "pakistan"),
                  ("home", "ACCOMMODATION", "Free", None),
                  ("clock", "TOTAL HOURS", "8 Hours", None),
                  ("calendar", "DAYS IN WEEK", "5 – 6 Days", None),
                  ("money", "BONUS &amp; OVERTIME", "As per Law", None)],
        "apply": "APPLY NOW!",
        "apply_sub": "Your skills can take you further!",
    },
    "ur": {
        "kicker": "فوری ضرورت",
        "title": "کوسووو میں ملازمت",
        "tagline": "بہترین مواقع کے ساتھ اپنا مستقبل بنائیں!",
        "from": "پاکستان", "to": "کوسووو",
        "total_n": "48", "total_label": "کل<br>آسامیاں",
        "th": ["عہدہ", "آسامیاں", "تنخواہ", "عمر کی حد"],
        "rows": [
            {"art": "factory", "name": "جنرل فیکٹری ورکر", "posts": "15",
             "sal_label": "کم از کم", "salary": "€500", "age": "کوئی حد نہیں"},
            {"art": "ce_truck", "name": f"{N('CE')} کیٹیگری ڈرائیور", "posts": "03",
             "sal_label": "کم از کم", "salary": "€500", "age": "کوئی حد نہیں"},
            {"art": "precast", "name": "پری کاسٹ کنکریٹ انسٹالیشن ورکر", "posts": "10",
             "sal_label": "کم از کم", "salary": "€500", "age": "کوئی حد نہیں"},
            {"art": "cleaner", "name": "کلیننگ جنرل ورکر", "posts": "04",
             "sal_label": "کم از کم", "salary": "€500", "age": "کوئی حد نہیں"},
            {"art": "factory", "name": "جنرل فیکٹری ورکر", "posts": "16",
             "salary": "€500 – €700", "sal_px": 26, "age": f"{N('25 – 50')} سال"},
        ],
        "total_row": "کل آسامیاں",
        "terms_title": "سہولیات اور شرائط — تمام عہدوں کے لیے",
        "terms": [("male", "جنس", "صرف مرد", None),
                  ("user", "قومیت", "پاکستانی", "pakistan"),
                  ("home", "رہائش", "مفت", None),
                  ("clock", "کل اوقات کار", f"{N(8)} گھنٹے", None),
                  ("calendar", "ہفتے میں دن", f"{N('5 – 6')} دن", None),
                  ("money", "بونس اور اوور ٹائم", "قانون کے مطابق", None)],
        "apply": "ابھی اپلائی کریں!",
        "apply_sub": "آپ کی مہارت آپ کو آگے لے جا سکتی ہے!",
    },
}
