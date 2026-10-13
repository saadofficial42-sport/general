"""Redesign of RS-Links-Uzbekistan-All-Jobs (same facts as data/uzbekistan_all.py) in the trio
photo-column style. Job pictures: assets/photos/uz_rider.*, uz_driver.*, uz_factory.* when supplied;
silhouette placeholders until then. Phone order per user: 0317 first."""
import copy

from common import WHATSAPP
from data.uzbekistan_all import DATA as OLD

PHOTOS = {"rider": "uz_rider", "driver": "uz_driver", "factory": "uz_factory"}

DATA = {
    "stem": "RS-Links-Uzbekistan-All-Jobs-v2",
    "country": "uzbekistan",
    "blue": "#0A8FB0", "deep": "#0B3E5C", "green_stripe": "#1EB53A",
    "phones": ["+92 317 0363690", WHATSAPP],
    "email": "hr@rslinksconsultants.com",
    "layout": {"header_h": 140, "band_h": 170, "title_top": 22, "title_top_ur": 0, "route_top": 30, "route_top_ur": 30,
               "route_x": 470, "gap": 12, "col_h": 548, "photo_h": 200, "panel_h": 262, "cta_top": 1156},
}
for lang in ("en", "ur"):
    t = copy.deepcopy(OLD[lang])
    for j in t["jobs"]:
        j["photo"] = PHOTOS[j["art"]]
    DATA[lang] = t
