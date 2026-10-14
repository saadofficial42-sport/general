"""Turkey factory-worker ad (2026-10-14). Converts another agency's ad; the photo is kept at the
user's explicit request ("picture same"). Interview dates (21-23 Sep 2026) are already past, so they
are replaced by 'online interview with delegation - share your CV'."""
from common import C, PHOTOS, WHATSAPP, font_css, flag, icon, logo_img, page, render, whatsapp_icon

RED, NAVY, GOLD = "#E30A17", "#0D2D63", "#FFD23F"
PHONES = ["+92 317 0363690", WHATSAPP]
EMAIL = "hr@rslinksconsultants.com"


def build():
    photo = (PHOTOS / "turkey_factory_worker_src-ad.png").as_uri()
    nums = "".join(f"<div class='num' style='display:block;font-size:50px;color:{NAVY};line-height:1.06'>{n}</div>" for n in PHONES)
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:150px;background:#fff'></div>
<div class='abs' style='top:15px;left:26px;width:500px;height:120px'>{logo_img('logo-horizontal-light', 'width:500px;height:120px;object-position:left')}</div>
<div class='abs' style='top:30px;right:34px;text-align:right'>
 <div class='script' style='font-size:40px;color:{C['green']};line-height:1'>Your Future, Our Priority</div>
 <div class='mono' style='font-size:15px;color:#5A6470;letter-spacing:3px;margin-top:10px'>OVERSEAS EMPLOYMENT</div></div>
<div class='abs' style='top:150px;left:0;width:1080px;height:6px;background:{RED}'></div>

<div class='abs' style='top:156px;left:0;width:1080px;height:860px;background:linear-gradient(160deg,#F9F8F4,#E9EEF5)'></div>
<div class='abs' style='top:156px;right:0;width:500px;height:860px;overflow:hidden'>
 <img src='{photo}' style='width:100%;height:100%;object-fit:cover;object-position:center top;display:block'>
 <div style='position:absolute;inset:0;background:linear-gradient(90deg,#F2F3F5 0,#F2F3F500 18%)'></div></div>

<div class='abs' style='top:186px;left:36px;width:560px'>
 <div style='display:inline-block;background:{RED};border-radius:10px;padding:6px 16px'><span class='mono' style='font-size:20px;color:#fff;letter-spacing:3px'>URGENT REQUIREMENT</span></div>
 <div class='anton' style='font-size:118px;line-height:.95;color:{NAVY};margin-top:14px'>JOBS IN</div>
 <div style='display:flex;align-items:center;gap:16px'><div class='anton' style='font-size:136px;line-height:1;color:{RED}'>TURKEY</div>
  <div style='filter:drop-shadow(0 4px 8px #0005)'>{flag('tr', 110, True, 'trf')}</div></div>
</div>

<div class='abs' style='top:520px;left:36px;width:540px;height:120px;background:{NAVY};border-radius:20px;display:flex;align-items:center;gap:20px;padding:0 24px;box-sizing:border-box;box-shadow:0 8px 20px #0003'>
 <div class='ic' style='width:76px;height:76px;border-radius:50%;background:{GOLD};display:flex;align-items:center;justify-content:center'>{icon('gear', 44, NAVY, 2.2)}</div>
 <div class='anton' style='font-size:60px;color:#fff;line-height:1'>FACTORY WORKER</div></div>

<div class='abs' style='top:660px;left:36px;width:540px;height:150px;background:#fff;border:5px solid {GOLD};border-radius:20px;display:flex;align-items:center;gap:20px;padding:0 24px;box-sizing:border-box;box-shadow:0 8px 20px #0002'>
 <div style='width:84px;height:84px;border-radius:50%;background:{RED};display:flex;align-items:center;justify-content:center;font-family:Archivo;font-weight:900;font-size:54px;color:#fff'>₺</div>
 <div><div class='mono' style='font-size:20px;color:#5A6470;letter-spacing:3px'>SALARY</div>
  <div style='display:flex;align-items:baseline;gap:10px'><span class='num' style='font-size:82px;color:{NAVY};line-height:1'>28,000</span><span class='anton' style='font-size:38px;color:{RED}'>LIRA</span></div></div></div>

<div class='abs' style='top:830px;left:36px;width:540px;height:160px;background:linear-gradient(120deg,{RED},#B00712);border-radius:20px;display:flex;align-items:center;gap:20px;padding:0 24px;box-sizing:border-box;box-shadow:0 8px 20px #0003'>
 <div style='width:84px;height:84px;border-radius:18px;background:#fff;display:flex;align-items:center;justify-content:center;flex:none'>{icon('video', 48, RED, 2.2)}</div>
 <div><div class='anton' style='font-size:30px;color:#fff;line-height:1.1'>INTERVIEW WITH DELEGATION</div>
  <div class='anton' style='font-size:72px;color:{GOLD};line-height:1'>ONLINE</div></div></div>

<div class='abs' style='top:1016px;left:0;width:1080px;height:334px;background:linear-gradient(100deg,{NAVY},{C['green']})'></div>
<div class='abs' style='top:1040px;left:36px;width:1008px;display:flex;align-items:center;gap:16px'>
 {icon('doc', 40, GOLD, 2.2)}<div class='anton' style='font-size:46px;color:#fff;line-height:1'>SHARE YOUR CV ON WHATSAPP</div></div>
<div class='abs' style='top:1112px;left:36px;height:150px;background:#fff;border-radius:26px;display:flex;align-items:center;gap:18px;padding:0 32px 0 16px;box-shadow:0 8px 20px #0006'>
 {whatsapp_icon(92)}<div>{nums}</div></div>
<div class='abs' style='top:1146px;right:36px;width:420px;text-align:right'>
 <div class='anton' style='font-size:58px;color:{GOLD};line-height:1'>APPLY NOW!</div>
 <div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:14px'>{icon('mail', 26, GOLD, 2)}<span style='font-size:24px;font-weight:700;color:#fff'>{EMAIL}</span></div></div>
<div class='abs' style='top:1290px;left:0;width:1080px;height:60px;background:{GOLD};display:flex;align-items:center;justify-content:center'>
 <span style='font-size:18px;font-weight:800;color:{NAVY};letter-spacing:.5px;white-space:nowrap'>RS LINKS CONSULTANTS PVT. LTD. &nbsp;·&nbsp; Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi</span></div>
"""
    return page(body, ".canvas{font-family:'Archivo',sans-serif;background:#F9F8F4}.num{font-family:'Anton',sans-serif;letter-spacing:.5px}")


if __name__ == "__main__":
    print(render(build(), "RS-Links-Turkey-Factory-Worker-English.png"))
