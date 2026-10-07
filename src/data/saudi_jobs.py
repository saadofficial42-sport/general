"""Demand 2026-10-07: Saudi Arabia — two source ads combined (demands/2026-10-07-saudi/).
 Picker / Checker: salary 1200 + 200 · duty 10 hours · age 21–33 · education minimum Matric ·
   language: "FA (basic English) — should know reading, writing and speaking"
 Factory Helper: salary 1100 + 200 · duty 10 hours · age 21–35 · education minimum Matric ·
   basic English (speaking, reading) · work: loading/unloading, checking, packing
 Both: accommodation, medical, transport by company · other benefits as per Saudi labour law ·
   "for a renowned company in Saudi Arabia" · interviews ongoing.
 Currency and salary period are NOT stated in the sources (shown exactly as "1200 + 200")."""
from common import C

N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"
B = lambda v: f"<b style='font-weight:800'>{v}</b>"

DATA = {
    "stem": "RS-Links-Saudi-Arabia-Picker-Checker-Factory-Helper",
    "country": "saudi",
    "green": "#006C35",
    "layout": {"hero_h": 340, "head_top": 172, "head_top_ur": 150, "gap": 14,
               "scene_h": 280, "col_h": 670, "strip_h": 92, "cta_top": 1240},
    "en": {
        "kicker": "URGENT REQUIREMENT",
        "title": "SAUDI ARABIA",
        "opener": "For a renowned company in Saudi Arabia",
        "jobs": [
            {"scene": "picker_scene", "title": "Picker / Checker", "badge": "AGE 21–33",
             "salary": {"label": "SALARY", "value": "1200 + 200"},
             "rows": [("clock", f"{B('Duty:')} 10 hours"),
                      ("user", f"{B('Age:')} 21 – 33 years"),
                      ("doc", f"{B('Education:')} Minimum Matric"),
                      ("chat", f"{B('Language:')} Basic English — read, write &amp; speak")]},
            {"scene": "helper_scene", "title": "Factory Helper", "badge": "AGE 21–35",
             "salary": {"label": "SALARY", "value": "1100 + 200"},
             "rows": [("clock", f"{B('Duty:')} 10 hours"),
                      ("user", f"{B('Age:')} 21 – 35 years"),
                      ("doc", f"{B('Education:')} Minimum Matric"),
                      ("chat", f"{B('Language:')} Basic English — speak &amp; read")],
             "tasks_title": "WORK DETAILS", "tasks": ["Loading / Unloading", "Checking", "Packing"]},
        ],
        "shared": [("home", "ACCOMMODATION", "By company", 1),
                   ("medical", "MEDICAL", "By company", 1),
                   ("bus", "TRANSPORT", "By company", 1)],
        "law": "Other benefits as per Saudi labour law",
        "interviews": "INTERVIEWS ONGOING",
        "apply_sub": "Contact RS Links Consultants on WhatsApp",
    },
    "ur": {
        "kicker": "فوری ضرورت برائے",
        "title": "سعودی عرب",
        "opener": "سعودی عرب کی مشہور کمپنی کے لیے درج ذیل آسامیوں کی فوری ضرورت ہے",
        "jobs": [
            {"scene": "picker_scene", "title": "پکر / چیکر", "badge": f"عمر {N('21 – 33')}",
             "salary": {"label": "سیلری", "value": "1200 + 200"},
             "rows": [("clock", f"{B('ڈیوٹی ٹائم:')} {N(10)} گھنٹے"),
                      ("user", f"{B('عمر کی حد:')} {N('21 – 33')} سال"),
                      ("doc", f"{B('تعلیم:')} کم از کم میٹرک"),
                      ("chat", f"{B('زبان:')} بیسک انگلش — لکھنا، پڑھنا اور بولنا")]},
            {"scene": "helper_scene", "title": "فیکٹری ہیلپر", "badge": f"عمر {N('21 – 35')}",
             "salary": {"label": "سیلری", "value": "1100 + 200"},
             "rows": [("clock", f"{B('ڈیوٹی:')} {N(10)} گھنٹے"),
                      ("user", f"{B('عمر کی حد:')} {N('21 – 35')} سال"),
                      ("doc", f"{B('تعلیم:')} کم از کم میٹرک"),
                      ("chat", f"{B('زبان:')} بیسک انگلش — بولنا اور پڑھنا")],
             "tasks_title": "کام کی تفصیل", "tasks": ["لوڈنگ اَن لوڈنگ", "چیکنگ", "پیکنگ"]},
        ],
        "shared": [("home", "رہائش", "کمپنی دے گی", 1),
                   ("medical", "میڈیکل", "کمپنی دے گی", 1),
                   ("bus", "ٹرانسپورٹ", "کمپنی دے گی", 1)],
        "law": "باقی مراعات سعودی لیبر لاء کے مطابق ملیں گی",
        "interviews": "انٹرویو جاری ہیں",
        "apply_sub": "آر ایس لنکس کنسلٹنٹس سے واٹس ایپ پر رابطہ کریں",
    },
}
