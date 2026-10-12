"""Demand 2026-10-12: Saudi Arabia — Helpers (General Workers) for a leading super mart.
Facts (user text): 15 posts · salary 1100 SAR + 200 SAR · accommodation by company ·
documents: original passport, picture, CNIC, FRC, PCC, biometric, medical, NAVTTC (user wrote
"NAVTCC") · advance basis: 2000 Riyal at Wakala, remaining payment after visa · "1 x Month"
(shown as processing time 1 month — to confirm)."""
from common import C

N = lambda v: f"<span class='num' style='font-family:Archivo;font-weight:800;letter-spacing:0'>{v}</span>"
GREEN = "#006C35"

DATA = {
    "stem": "RS-Links-Saudi-Arabia-Supermart-Helpers",
    "country": "saudi",
    "green": GREEN,
    "photos": ["rslinks_worker_hero", "rslinks_team_scan", "rslinks_worker_pack"],
    "layout": {"header_h": 150, "hero_h": 580, "head_top": 26, "head_top_ur": 6, "thumb_top": 372, "thumb_h": 180,
               "gap": 14, "tile_h": 110, "doc_h": 60, "docs_block_h": 180, "pay_h": 112, "cta_top": 1236},
    "en": {
        "urgent": "URGENT",
        "opener": "For one of the leading Super Marts in Saudi Arabia",
        "title": "HELPERS",
        "subtitle": "(GENERAL WORKERS)",
        "posts_n": "15", "posts_word": "POSTS",
        "tiles": [
            ("money", "SALARY", "1100 + 200 SAR", True, 44, 1.5, GREEN),
            ("home", "ACCOMMODATION", "By company", False, 0, 1.05, C["navy"]),
            ("calendar", "PROCESSING TIME", "1 MONTH", True, 40, 1.0, "#B7791F"),
        ],
        "docs_title": "DOCUMENTS REQUIRED",
        "documents": ["Original Passport", "Picture", "CNIC", "FRC", "PCC", "Biometric", "Medical", "NAVTTC"],
        "pay_title": "PAYMENT: ADVANCE BASIS",
        "pay": ["2000 SAR at Wakala", "Remaining payment after visa"],
        "apply": "APPLY NOW!",
    },
    "ur": {
        "urgent": "فوری ضرورت",
        "opener": "سعودی عرب کے ایک معروف سپر مارٹ کے لیے",
        "title": "ہیلپرز",
        "subtitle": "(جنرل ورکرز)",
        "posts_n": "15", "posts_word": "آسامیاں",
        "tiles": [
            ("money", "تنخواہ", "1100 + 200 SAR", True, 44, 1.5, GREEN),
            ("home", "رہائش", "کمپنی کی طرف سے", False, 0, 1.05, C["navy"]),
            ("calendar", "پروسیسنگ ٹائم", f"{N(1)} مہینہ", False, 0, 1.0, "#B7791F"),
        ],
        "docs_title": "مطلوبہ دستاویزات",
        "documents": ["اصل پاسپورٹ", "تصویر", f"شناختی کارڈ", f"{N('FRC')}", f"{N('PCC')}", "بائیو میٹرک", "میڈیکل", f"{N('NAVTTC')}"],
        "pay_title": "ادائیگی: ایڈوانس بیسز",
        "pay": [f"{N('2000')} ریال وکالہ پر", "باقی ادائیگی ویزا کے بعد"],
        "apply": "ابھی اپلائی کریں!",
    },
}
