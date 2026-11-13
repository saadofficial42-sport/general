"""Greece — Factory Workers & Waiters, English (2026-11-13). Partner: Mr. Shahid. Facts from user: factory workers,
waiters; accommodation; medical; work permit from tax-payer companies; walk-in embassy appointment included in the
package. Cost / partner share / rate are internal and NOT shown on the ad.
Design: "Aegean arches" — warm white marble page with Greek-key meander bands, two tall arched-window photo panels
(factory | waiters) with terracotta captions, Aegean-blue title, terracotta package checklist cards, deep-blue CTA."""
from common import PHONES, PHOTOS, font_css, icon, logo_img, render, whatsapp_icon
from greece_ecycle import flag_gr, meander

AEG, AEG2, TERRA, SAND, MARBLE, INK = "#0D5EAF", "#073B73", "#C8553D", "#F3E6D3", "#FBF8F2", "#14233A"
EMAIL = "hr@rslinksconsultants.com"


def arch(src, pos, label, w, h):
    return (f"<div style='width:{w}px'><div style='width:{w}px;height:{h}px;border-radius:{w // 2}px {w // 2}px 18px 18px;padding:10px;background:#fff;box-shadow:0 18px 34px #14233A33;box-sizing:border-box'>"
            f"<div style='width:100%;height:100%;border-radius:{w // 2 - 10}px {w // 2 - 10}px 10px 10px;overflow:hidden'><img src='{src}' style='width:100%;height:100%;object-fit:cover;object-position:{pos}'></div></div>"
            f"<div style='margin:-34px auto 0;position:relative;width:{w - 60}px;background:{TERRA};border-radius:14px;padding:12px 0;text-align:center;font:400 38px Anton;color:#fff;letter-spacing:2px;box-shadow:0 10px 18px #C8553D55'>{label}</div></div>")


def build():
    fac, wai = (PHOTOS / "rslinks_worker_hero.png").as_uri(), (PHOTOS / "sa_waiter2.jpg").as_uri()
    items = [("home", "ACCOMMODATION", "Provided"), ("medical", "MEDICAL", "Provided"),
             ("doc", "WORK PERMIT", "From tax-payer companies"), ("calendar", "EMBASSY APPOINTMENT", "Walk-in appointment included in package")]
    cards = "".join(f"<div style='display:flex;align-items:center;gap:16px;background:#fff;border-radius:18px;padding:14px 18px;border-left:8px solid {TERRA};box-shadow:0 8px 18px #14233A1A'>"
                    f"<span style='width:62px;height:62px;border-radius:50%;background:{AEG};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 32, '#fff', 2.2)}</span>"
                    f"<div><div style='font:400 30px Anton;color:{AEG2};letter-spacing:1px;line-height:1.1'>{a}</div><div style='font:700 19px Archivo;color:#4A5568;margin-top:2px'>{b}</div></div></div>" for ic, a, b in items)
    nums = "".join(f"<div style='display:flex;align-items:center;gap:8px'>{whatsapp_icon(32)}<span style='font:400 29px Anton;color:#fff;letter-spacing:.5px'>{n}</span></div>" for n in PHONES)
    body = f"""
<div class='abs' style='inset:0;background:radial-gradient(circle at 85% 15%,#fff,{MARBLE} 45%,{SAND})'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:34px;background:{AEG}'></div><div class='abs' style='top:0;left:0;opacity:.9'>{meander(1080, '#fff')}</div>
<div class='abs' style='top:58px;left:36px'>{logo_img('logo-horizontal-light', 'width:280px;height:72px;object-position:left')}</div>
<div class='abs' style='top:62px;right:40px'>{flag_gr(120)}</div>
<div class='abs' style='top:150px;left:0;width:1080px;text-align:center'>
 <div style='display:inline-block;background:{TERRA};color:#fff;font:800 20px Archivo;letter-spacing:5px;padding:8px 20px;border-radius:999px'>NOW HIRING · EUROPE</div>
 <div style='font:400 128px Anton;color:{AEG};line-height:.95;letter-spacing:4px;margin-top:10px'>WORK IN GREECE</div>
 <div style='font:700 26px Archivo;color:{INK};margin-top:6px;letter-spacing:1px'>Work permit jobs · Apply today</div></div>

<div class='abs' style='top:400px;left:60px;display:flex;gap:40px'>{arch(fac, 'center 25%', 'FACTORY WORKERS', 460, 440)}{arch(wai, 'center 20%', 'WAITERS', 460, 440)}</div>

<div class='abs' style='top:905px;left:40px;right:40px;display:grid;grid-template-columns:1fr 1fr;gap:14px 16px'>{cards}</div>
<div class='abs' style='top:1112px;left:0;width:1080px;text-align:center;font:800 22px Archivo;color:{TERRA};letter-spacing:1px'>SEND YOUR CV ON WHATSAPP</div>

<div class='abs' style='top:1160px;left:0;width:1080px;height:190px;background:linear-gradient(100deg,{AEG2},{AEG})'></div>
<div class='abs' style='top:1160px;left:0;opacity:.35'>{meander(1080, '#fff')}</div>
<div class='abs' style='top:1210px;left:36px;display:grid;grid-template-columns:auto auto;gap:14px 30px'>{nums}</div>
<div class='abs' style='top:1212px;right:40px;width:380px;text-align:right'>
 <div style='font:400 44px Anton;color:#fff;letter-spacing:1px;line-height:1.05'>APPLY NOW!</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:12px'>{icon('mail', 22, '#fff', 2)}<span style='font:800 20px Archivo;color:#fff'>{EMAIL}</span></div></div>"""
    return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><style>{font_css()}html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{MARBLE}'>{body}</div></body></html>")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Greece-Factory-Workers-Waiters.png"))
