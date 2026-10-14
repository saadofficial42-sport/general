"""Demand 2026-10-14: Saudi Arabia — Checker & Receiver for a well-known super market
(demands/2026-10-14-saudi-checker-receiver/ref.jpg; employer name omitted per ad rules).
Facts: urgent visa · immediate departure · salary 1300 riyal; food free (user 2026-10-14, replaces the 200 riyal food line) · duty 08 hours + 1 hour rest ·
visa: Istiqdam · contract 2 years · accommodation, medical, transport by company · other benefits per
local labour law · bring complete documents · test & interview ongoing · WhatsApp documents + CV.
Duties as listed in the source. No post count / age in source. Urdu only."""
from common import WHATSAPP

N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"

DATA = {
    "stem": "RS-Links-Saudi-Arabia-Checker-Receiver",
    "country": "saudi",
    "photo": "rslinks_worker_hero",   # real RS Links photo: worker scanning / checking a carton
    "thumbs": ["rslinks_team_scan", "rslinks_worker_pack"],
    "brand_logo": {"file": "panda_logo_src-ad.png", "w": 220, "caption": "سعودی عرب کی مشہور سپر مارکیٹ", "side": "کے لیے", "gap": 2},
    "jacket": "CHECKER",
    "phones": ["+92 317 0363690", WHATSAPP],
    "email": "hr@rslinksconsultants.com",
    "layout": {"header_h": 140, "hero_h": 460, "pic_w": 470, "title_top": 12, "tiles_h": 110, "gap": 14,
               "li_gap_ur": 3, "li_px_ur": 18, "li_lh_ur": 1.75, "cta_top": 1196, "thumb_h": 112},
    "ur": {
        "urgent": "فوری ضرورت",
        "kicker": "",
        "title": "چیکر اینڈ ریسیور",
        "title_en": "CHECKER &amp; RECEIVER",
        "where": "فوری ویزہ • فوری روانگی",
        "opener": "ٹیسٹ اور انٹرویو جاری ہیں",
        "tiles": [("money", "تنخواہ", "1300 SAR", True, 36, "", 1.25),
                  ("food", "کھانا", "مفت", False, 0, "کمپنی کی طرف سے", 1.0),
                  ("clock", "ڈیوٹی", "08 + 1", True, 36, "گھنٹے (1 گھنٹہ ریسٹ)", 1.1),
                  ("calendar", "معاہدہ", f"{N(2)} سال", False, 0, "", .85),
                  ("visa", "ویزا", "استقدام", False, 0, "", .85)],
        "duties_title": "ذمہ داریاں",
        "duties": ["مال وصول کرتے وقت سامان کی مقدار اور ریکارڈ چیک کرنا",
                   f"اسٹور اور گودام میں {N('CCTV')} نگرانی کرنا",
                   "چوری، نقصان یا سامان ضائع ہونے کی روک تھام",
                   "سپلائرز سے آنے والے سامان کی چیکنگ اور گنتی",
                   "سامان میں کمی یا مشکوک سرگرمی کی رپورٹ کرنا",
                   "اسٹور، گودام اور سیلز ایریا میں گشت کرنا",
                   "اسٹاک کی مناسب نگرانی کرنا",
                   "نقصان یا واقعے کی تحقیقات میں مدد اور روزانہ رپورٹ",
                   "کمپنی کے حفاظتی اصولوں پر عمل کروانا"],
        "req_title": "سہولیات و شرائط",
        "reqs": ["کھانا مفت (کمپنی کی طرف سے)",
                 "رہائش کمپنی کی طرف سے",
                 "میڈیکل کمپنی کی طرف سے",
                 "ٹرانسپورٹ کمپنی کی طرف سے",
                 "دیگر مراعات مقامی لیبر لاء کے مطابق",
                 f"معاہدے کی مدت: {N(2)} سال",
                 "خواہشمند حضرات اپنے مکمل کاغذات ساتھ لائیں"],
        "apply": "ابھی واٹس ایپ کریں!",
        "apply_sub": f"اپنے تمام کاغذات اور {N('CV')} نیچے دیے گئے نمبرز پر بھیجیں",
    },
}
