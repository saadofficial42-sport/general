"""Demand 2026-10-07: Serbia — "Schedule of Required Personnel" (demands/2026-10-07-serbia/).
User first said Kosovo; the document is in Serbian dinars and cites Serbian law, and the user
confirmed Serbia. All figures verbatim from the source:
  Cleaner 35 · 80,000–110,000 Din · €680–€940 · 6 months
  Warehouse Worker 45 · 80,000–110,000 Din · €680–€940 · 6 months
  Factory Worker 70 · 85,000–115,000 Din · €725–€980 · 6 months      Total 150
  1 EUR ≈ 117 Din (subject to change). 40 h/week (8 h/day, 5 days); max 48 h/week incl. overtime.
  Accommodation: employer shared apartments OR housing allowance 15,000–25,000 Din/month (€130–€215).
  Health insurance: mandatory, per Serbian law. Meals: food allowance 12,000–20,000 Din/month
  (€100–€170) OR company canteen. Transport: public transport pass OR allowance 5,000–8,000 Din/month
  (€45–€70). Annual leave: min 20 working days paid. Overtime: 126% weekdays, 135% Sundays & public
  holidays. Language: basic English preferred."""
from common import C

N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"

DATA = {
    "stem": "RS-Links-Serbia-Cleaner-Warehouse-Factory",
    "country": "serbia",
    "blue": "#0C4076",
    "gold": "#F0C850",
    "layout": {"header_h": 160, "hero_h": 262, "title_top": 22, "title_top_ur": 0, "seal_top": 14,
               "gap": 12, "thead_h": 46, "row_h": 82, "total_h": 50,
               "term_h": 100, "term_px": (16, 15), "term_w": 700, "term_cols": 3,
               "cols": [120, 230, 150], "cta_top": 1250},
    "en": {
        "kicker": "NOW HIRING",
        "title_a": "WORK IN", "title_b": "SERBIA",
        "tagline": "Monthly salary up to €980 · 6-month contract",
        "from": "Pakistan", "to": "Serbia",
        "total_n": "150", "total_label": "TOTAL<br>REQUIRED",
        "th": ["POSITION", "QTY", "MONTHLY SALARY", "CONTRACT"],
        "rows": [
            {"art": "cleaner", "name": "Cleaner", "posts": "35",
             "salary": "€680 – €940", "sal_px": 26, "sal_sub": "80,000 – 110,000 Din", "age": "6 months"},
            {"art": "warehouse", "name": "Warehouse Worker", "posts": "45",
             "salary": "€680 – €940", "sal_px": 26, "sal_sub": "80,000 – 110,000 Din", "age": "6 months"},
            {"art": "factory", "name": "Factory Worker", "posts": "70",
             "salary": "€725 – €980", "sal_px": 26, "sal_sub": "85,000 – 115,000 Din", "age": "6 months"},
        ],
        "total_row": "Total Required",
        "terms_title": "GENERAL EMPLOYMENT TERMS",
        "terms": [("clock", "WORKING HOURS", "40 hrs/week<br>(8 hrs/day, 5 days/week)", None),
                  ("overtime", "MAXIMUM HOURS", "48 hrs/week<br>including overtime", None),
                  ("money", "OVERTIME PAY", "126% weekdays<br>135% Sundays &amp; holidays", None),
                  ("home", "ACCOMMODATION", "Shared apartment, or<br>€130–€215 / month allowance", None),
                  ("food", "MEALS", "Company canteen, or<br>€100–€170 / month allowance", None),
                  ("bus", "TRANSPORT", "Transport pass, or<br>€45–€70 / month allowance", None),
                  ("shield", "HEALTH INSURANCE", "Mandatory, as per<br>Serbian law", None),
                  ("calendar", "ANNUAL LEAVE", "Minimum 20 working<br>days paid", None),
                  ("chat", "LANGUAGE", "Basic English<br>preferred", None)],
        "footnote": "Allowances in dinars per month: accommodation 15,000–25,000 Din · food 12,000–20,000 Din · transport 5,000–8,000 Din.<br>Euro amounts are approximate (1 EUR ≈ 117 Din) and subject to change.",
        "apply": "APPLY NOW!",
        "apply_sub": "Your skills can take you further!",
    },
    "ur": {
        "kicker": "بھرتی جاری ہے",
        "title": "سربیا میں ملازمت",
        "tagline": f"ماہانہ تنخواہ {N('€980')} تک • {N(6)} ماہ کا کنٹریکٹ",
        "from": "پاکستان", "to": "سربیا",
        "total_n": "150", "total_label": "کل<br>آسامیاں",
        "th": ["عہدہ", "تعداد", "ماہانہ تنخواہ", "کنٹریکٹ"],
        "rows": [
            {"art": "cleaner", "name": "کلینر", "posts": "35",
             "salary": "€680 – €940", "sal_px": 26, "sal_sub": f"{N('80,000 – 110,000')} دینار", "age": f"{N(6)} ماہ"},
            {"art": "warehouse", "name": "ویئر ہاؤس ورکر", "posts": "45",
             "salary": "€680 – €940", "sal_px": 26, "sal_sub": f"{N('80,000 – 110,000')} دینار", "age": f"{N(6)} ماہ"},
            {"art": "factory", "name": "فیکٹری ورکر", "posts": "70",
             "salary": "€725 – €980", "sal_px": 26, "sal_sub": f"{N('85,000 – 115,000')} دینار", "age": f"{N(6)} ماہ"},
        ],
        "total_row": "کل مطلوبہ افراد",
        "terms_title": "ملازمت کی عمومی شرائط",
        "terms": [("clock", "اوقات کار", f"ہفتے میں {N(40)} گھنٹے ({N(8)} گھنٹے، {N(5)} دن)", None),
                  ("overtime", "زیادہ سے زیادہ اوقات", f"اوور ٹائم سمیت ہفتے میں {N(48)} گھنٹے", None),
                  ("money", "اوور ٹائم کی ادائیگی", f"عام دن {N('126%')} • اتوار و تعطیلات {N('135%')}", None),
                  ("home", "رہائش", f"شیئرڈ اپارٹمنٹ، یا<br>{N('€130 – €215')} ماہانہ الاؤنس", None),
                  ("food", "کھانا", f"کمپنی کینٹین، یا<br>{N('€100 – €170')} ماہانہ الاؤنس", None),
                  ("bus", "ٹرانسپورٹ", f"ٹرانسپورٹ پاس، یا<br>{N('€45 – €70')} ماہانہ الاؤنس", None),
                  ("shield", "ہیلتھ انشورنس", "سربیا کے قانون کے مطابق لازمی", None),
                  ("calendar", "سالانہ چھٹی", f"کم از کم {N(20)} ورکنگ دن (تنخواہ کے ساتھ)", None),
                  ("chat", "زبان", "بنیادی انگریزی کو ترجیح", None)],
        "footnote": f"ماہانہ الاؤنس دینار میں: رہائش {N('15,000 – 25,000')} • کھانا {N('12,000 – 20,000')} • ٹرانسپورٹ {N('5,000 – 8,000')}<br>یورو رقم تخمینی ہے ({N('1 EUR ≈ 117')} دینار) اور تبدیل ہو سکتی ہے۔",
        "apply": "ابھی اپلائی کریں!",
        "apply_sub": "آپ کی مہارت آپ کو آگے لے جا سکتی ہے!",
    },
}
