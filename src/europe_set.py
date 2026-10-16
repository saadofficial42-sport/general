"""Europe set (2026-10-16): Belarus, Kosovo, Ukraine, Serbia — RS Links conversions of the user's own
English drafts (demands/2026-10-16-europe-set/). Facts copied exactly; unverifiable claims ("safe",
"legal", "100% genuine", "legitimate", "secure your future", "direct employer") dropped per ad rules.
Each ad uses a different layout + palette. All carry common.PHONES + email + office address."""
from common import PHONES, PHOTOS, flag, font_css, icon, logo_img, render, whatsapp_icon

EMAIL = "hr@rslinksconsultants.com"
ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi"
P = lambda n: (PHOTOS / f"{n}.png").as_uri()


def page(body, bg):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{font_css()}"
            f"html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}}"
            f".abs{{position:absolute}}.an{{font-family:Anton;letter-spacing:.5px}}.ar{{font-family:Archivo}}"
            f".mono{{font-family:PlexMono;font-weight:700}}.sc{{font-family:Dancing;font-weight:700}}</style></head>"
            f"<body><div style='position:relative;width:1080px;height:1350px;overflow:hidden;background:{bg};font-family:Archivo'>{body}</div></body></html>")


def contact_bar(top, bg, card, ink, accent, title="APPLY NOW!", sub="Send your CV on WhatsApp or email"):
    nums = "".join(f"<div class='an' style='font-size:33px;color:{ink};line-height:1.08'>{n}</div>" for n in PHONES)
    return (f"<div class='abs' style='top:{top}px;left:0;width:1080px;height:{1350-top}px;background:{bg}'></div>"
            f"<div class='abs' style='top:{top+16}px;left:30px;height:{1350-top-56}px;background:{card};border-radius:22px;display:flex;align-items:center;gap:14px;padding:0 24px 0 14px;box-shadow:0 8px 18px #0005'>"
            f"{whatsapp_icon(66)}<div>{nums}</div></div>"
            f"<div class='abs' style='top:{top+18}px;right:32px;width:500px;text-align:right'>"
            f"<div class='an' style='font-size:52px;color:{accent};line-height:1'>{title}</div>"
            f"<div class='ar' style='font-size:19px;font-weight:700;color:#fff;margin-top:6px;white-space:nowrap'>{sub}</div>"
            f"<div style='display:flex;align-items:center;justify-content:flex-end;gap:8px;margin-top:10px'>{icon('mail', 26, accent, 2)}"
            f"<span class='ar' style='font-size:25px;font-weight:700;color:#fff'>{EMAIL}</span></div></div>"
            f"<div class='abs' style='bottom:0;left:0;width:1080px;height:40px;background:#00000040;display:flex;align-items:center;justify-content:center;gap:8px'>"
            f"{icon('pin', 20, accent, 2.4)}<span class='ar' style='font-size:18px;font-weight:700;color:#fff'>{ADDRESS}</span></div>")


# ------------------------------------------------------------------ 1. BELARUS — 2x2 photo grid, white + red/green
def belarus():
    RED, GRN, INK = "#C8102E", "#007C30", "#14161C"
    jobs = [("by_car_mechanic", "CAR MECHANIC", "gear"), ("by_auto_painter", "AUTOMOTIVE PAINTER", "roller"),
            ("by_butcher", "BUTCHER / DEBONER", "box"), ("by_tailor", "FEMALE TAILOR", "scissors")]
    cards = "".join(
        f"<div style='position:relative;width:500px;height:262px;border-radius:22px;overflow:hidden;box-shadow:0 10px 22px #0003'>"
        f"<img src='{P(n)}' style='width:100%;height:100%;object-fit:cover;object-position:center 25%'>"
        f"<div style='position:absolute;left:0;right:0;bottom:0;height:64px;background:{RED if i % 3 == 0 else GRN};display:flex;align-items:center;gap:12px;padding:0 18px'>"
        f"<div style='width:44px;height:44px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center'>{icon(ic, 26, RED if i % 3 == 0 else GRN, 2.3)}</div>"
        f"<span class='an' style='font-size:34px;color:#fff'>{t}</span></div></div>"
        for i, (n, t, ic) in enumerate(jobs))
    facts = [("money", "SALARY", "$600", "per month"), ("home", "PROVIDED BY EMPLOYER", "Accommodation", "&amp; Transportation"),
             ("clock", "DUTY HOURS", "8 Hours", "per day"), ("calendar", "PROCESSING TIME", "2 Months", "")]
    fx = "".join(
        f"<div style='flex:1;border-radius:18px;background:#fff;border:3px solid {INK}14;box-shadow:0 6px 14px #0002;padding:12px 14px'>"
        f"<div style='display:flex;align-items:center;gap:8px'>{icon(ic, 26, RED, 2.3)}<span class='mono' style='font-size:14px;color:#5A6070;letter-spacing:1px'>{l}</span></div>"
        f"<div class='an' style='font-size:{44 if v[0] in '$28' else 32}px;color:{INK};line-height:1.1;margin-top:6px'>{v}</div>"
        f"<div class='ar' style='font-size:18px;font-weight:700;color:{GRN}'>{s}</div></div>" for ic, l, v, s in facts)
    docs = "".join(f"<div style='display:flex;align-items:center;gap:10px;background:#fff;border-radius:999px;padding:8px 18px'>{icon(ic, 26, GRN, 2.3)}"
                   f"<span class='ar' style='font-size:21px;font-weight:800;color:{INK}'>{t}</span></div>"
                   for ic, t in (("idcard", "Passport"), ("doc", "CV"), ("video", "Video of relevant work (2–3 min)")))
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:250px;background:#fff'></div>
<div class='abs' style='top:0;left:0;width:22px;height:250px;background:repeating-linear-gradient(180deg,{RED} 0 14px,#fff 14px 22px)'></div>
<div class='abs' style='top:20px;left:46px'>{logo_img('logo-horizontal-light', 'width:400px;height:100px;object-position:left')}</div>
<div class='abs' style='top:16px;right:30px;filter:drop-shadow(0 4px 8px #0004)'>{flag('by', 170, True, 'byx')}</div>
<div class='abs' style='top:126px;left:46px'><span class='mono' style='font-size:22px;color:{GRN};letter-spacing:4px'>WORK OPPORTUNITIES IN</span>
 <div class='an' style='font-size:84px;color:{RED};line-height:1'>BELARUS <span style='color:{INK};font-size:44px'>· 4 SKILLED TRADES</span></div></div>
<div class='abs' style='top:250px;left:0;width:1080px;height:8px;background:linear-gradient(90deg,{RED} 0 66%,{GRN} 66%)'></div>
<div class='abs' style='top:276px;left:30px;right:30px;display:flex;flex-wrap:wrap;gap:20px'>{cards}</div>
<div class='abs' style='top:842px;left:30px;right:30px;display:flex;gap:12px'>{fx}</div>
<div class='abs' style='top:1014px;left:30px;right:30px;height:96px;border-radius:20px;background:{GRN};display:flex;align-items:center;gap:14px;padding:0 20px'>
 <span class='an' style='font-size:28px;color:#fff;white-space:nowrap'>REQUIRED DOCUMENTS</span>{docs}</div>
<div class='abs' style='top:1120px;left:0;right:0;text-align:center'><span class='sc' style='font-size:40px;color:{RED}'>Skilled Hands, Brighter Tomorrows</span></div>
{contact_bar(1176, INK, '#fff', INK, '#FFD23F')}"""
    return page(body, "#F2F3F5")


# ------------------------------------------------------------------ 2. KOSOVO — dark vacancy board, two tables
def kosovo():
    BLU, GOLD, INK = "#1C3F94", "#F0C850", "#0B1736"
    admin = [("Administrative Assistant", 8, 600), ("Legal Assistant", 10, 700), ("Translator / Interpreter", 8, 700),
             ("Customer Service Specialist", 10, 600), ("Data Entry Operator", 8, 550), ("IT Support Specialist", 8, 750),
             ("Software Developer", 6, 900), ("Graphic Designer", 5, 700), ("Marketing Specialist", 6, 700),
             ("Social Media Specialist", 6, 650), ("Sales Representative", 6, 650), ("Event Coordinator", 4, 700),
             ("Driver", 5, 600), ("Cleaning Personnel", 6, 500), ("Office Support Staff", 4, 500)]
    cons = [("General Construction Worker", 20, 550), ("Mason", 12, 650), ("Formwork Carpenter", 10, 650),
            ("Steel Fixer / Rebar Worker", 10, 650), ("Plasterer", 8, 600), ("Tile Setter", 8, 650),
            ("Construction Painter", 8, 600), ("Construction Electrician", 6, 750), ("Plumber", 6, 750),
            ("Welder", 4, 750), ("Heavy Equipment Operator", 4, 800), ("Construction Foreman", 4, 900)]

    def table(title, ic, rows, accent, rh):
        head = (f"<div style='display:flex;align-items:center;gap:10px;background:{accent};padding:10px 14px'>{icon(ic, 28, INK, 2.4)}"
                f"<span class='an' style='font-size:28px;color:{INK}'>{title}</span></div>"
                f"<div style='display:flex;padding:6px 14px;background:#ffffff14'><span class='mono' style='flex:1;font-size:14px;color:{accent}'>JOB TITLE</span>"
                f"<span class='mono' style='width:62px;text-align:center;font-size:14px;color:{accent}'>SEATS</span>"
                f"<span class='mono' style='width:78px;text-align:right;font-size:14px;color:{accent};white-space:nowrap'>EUR</span></div>")
        body = "".join(
            f"<div style='display:flex;align-items:center;height:{rh}px;padding:0 14px;background:{'#ffffff0d' if i % 2 else 'transparent'}'>"
            f"<span class='ar' style='flex:1;font-size:18px;font-weight:700;color:#fff;white-space:nowrap'>{n}</span>"
            f"<span class='an' style='width:62px;text-align:center;font-size:22px;color:{accent}'>{s}</span>"
            f"<span class='an' style='width:78px;text-align:right;font-size:24px;color:#fff'>€{e}</span></div>" for i, (n, s, e) in enumerate(rows))
        tot = sum(s for _, s, _ in rows)
        foot = (f"<div style='display:flex;align-items:center;padding:8px 14px;border-top:2px solid {accent}'><span class='an' style='flex:1;font-size:22px;color:{accent}'>TOTAL SEATS</span>"
                f"<span class='an' style='font-size:28px;color:{accent}'>{tot}</span></div>")
        return f"<div style='flex:1;background:{INK};border-radius:20px;overflow:hidden;border:2px solid {accent}55'>{head}{body}{foot}</div>"
    perks = "".join(f"<div style='flex:1;display:flex;flex-direction:column;align-items:center;gap:6px'>"
                    f"<div style='width:58px;height:58px;border-radius:50%;background:{GOLD};display:flex;align-items:center;justify-content:center'>{icon(ic, 30, INK, 2.3)}</div>"
                    f"<span class='ar' style='font-size:17px;font-weight:800;color:{INK};text-align:center;line-height:1.15'>{t}</span></div>"
                    for ic, t in (("plane", "Visa &amp; Ticket<br>Assistance"), ("home", "Accommodation<br>Provided"),
                                  ("medical", "Medical<br>Insurance"), ("food", "Food<br>Allowance"), ("user", "Professional<br>Guidance")))
    body = f"""
<div class='abs' style='inset:0;background:linear-gradient(160deg,#122A6B,#071029)'></div>
<div class='abs' style='top:18px;left:28px;background:#fff;border-radius:16px;padding:4px 14px'>{logo_img('logo-horizontal-light', 'width:330px;height:84px')}</div>
<div class='abs' style='top:14px;right:28px;filter:drop-shadow(0 4px 8px #0008)'>{flag('xk2', 140, True, 'xkx')}</div>
<div class='abs' style='top:122px;left:30px;right:30px;display:flex;align-items:flex-end;justify-content:space-between'>
 <div><div class='mono' style='font-size:20px;color:{GOLD};letter-spacing:4px'>EUROPE WORK VISA</div>
  <div class='an' style='font-size:92px;color:#fff;line-height:1'>KOSOVO <span style='color:{GOLD}'>27 JOBS</span></div></div>
 <div style='text-align:right;width:330px;height:100px;border-radius:16px;overflow:hidden;display:flex;gap:6px'>
  <img src='{P("xk_construction")}' style='width:50%;height:100%;object-fit:cover'><img src='{P("xk_office")}' style='width:50%;height:100%;object-fit:cover'></div></div>
<div class='abs' style='top:252px;left:24px;right:24px;display:flex;gap:14px'>
 {table('ADMINISTRATIVE &amp; PROFESSIONAL', 'user', admin, GOLD, 37)}{table('CONSTRUCTION SECTOR', 'crane', cons, '#FFB547', 37)}</div>
<div class='abs' style='top:850px;left:562px;width:494px;text-align:center'><div class='an' style='font-size:62px;color:#fff;line-height:1'>200 SEATS</div><div class='ar' style='font-size:20px;font-weight:700;color:#C9D4EE'>across 27 job titles · salaries in euro / month</div></div>
<div class='abs' style='top:1030px;left:24px;right:24px;height:132px;background:#fff;border-radius:20px;display:flex;align-items:center;padding:0 10px'>{perks}</div>
{contact_bar(1176, '#050B1E', '#fff', INK, GOLD, 'APPLY NOW!', 'Limited seats · CV on WhatsApp or email')}"""
    return page(body, "#071029")


# ------------------------------------------------------------------ 3. UKRAINE — yellow/blue split cards
def ukraine():
    BLU, YEL, INK = "#0057B7", "#FFD500", "#0A1A33"

    def card(img, title, need, target_l, target_v, x):
        rows = [("user", "REQUIRED", need), ("chart" if False else "check", target_l, target_v),
                ("money", "MINIMUM SALARY", "USD 1,000 / month"), ("gift", "PERFORMANCE BONUSES", "Extra premiums for high-quality &amp; diligent work")]
        li = "".join(f"<div style='display:flex;gap:12px;padding:7px 0;border-top:1px solid #0A1A3318'>"
                     f"<div style='width:40px;height:40px;border-radius:12px;background:{BLU};display:flex;align-items:center;justify-content:center;flex:none'>{icon(ic, 22, YEL, 2.3)}</div>"
                     f"<div><div class='mono' style='font-size:14px;color:#5A6880'>{l}</div><div class='ar' style='font-size:{24 if len(v) < 22 else 18}px;font-weight:800;color:{INK};line-height:1.2'>{v}</div></div></div>"
                     for ic, l, v in rows)
        return (f"<div class='abs' style='top:500px;left:{x}px;width:495px;height:520px;background:#fff;border-radius:24px;overflow:hidden;box-shadow:0 12px 26px #0004'>"
                f"<img src='{P(img)}' style='width:100%;height:150px;object-fit:cover;object-position:center top;display:block'>"
                f"<div style='background:{BLU};padding:8px 20px'><span class='an' style='font-size:44px;color:{YEL}'>{title}</span></div>"
                f"<div style='padding:4px 20px'>{li}</div></div>")
    strip = "".join(f"<div style='flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;border-left:{'0' if i == 0 else '2px solid #ffffff30'}'>"
                    f"{icon(ic, 30, YEL, 2.2)}<span class='ar' style='font-size:17px;font-weight:800;color:#fff;text-align:center;line-height:1.15;margin-top:4px'>{t}</span></div>"
                    for i, (ic, t) in enumerate((("home", "Free<br>Accommodation"), ("bus", "Transportation<br>Provided"), ("clock", "8 Hours<br>Duty / Day"),
                                                 ("calendar", "5 Days<br>a Week"), ("doc", "Approx. 2 Months<br>Processing"), ("user", "Age<br>23–42 Years"))))
    body = f"""
<div class='abs' style='top:0;left:0;width:1080px;height:480px;overflow:hidden'><img src='{P("ua_hero")}' style='width:1080px;height:480px;object-fit:cover;object-position:right 30%'></div>
<div class='abs' style='top:0;left:0;width:1080px;height:480px;background:linear-gradient(90deg,{INK} 0,{INK}F0 42%,{INK}00 75%)'></div>
<div class='abs' style='top:22px;left:30px;background:#fff;border-radius:16px;padding:4px 14px'>{logo_img('logo-horizontal-light', 'width:360px;height:90px')}</div>
<div class='abs' style='top:22px;right:28px;filter:drop-shadow(0 4px 8px #0008)'>{flag('ua', 140, True, 'uax')}</div>
<div class='abs' style='top:140px;left:34px;width:600px'>
 <div style='display:inline-block;background:#E53935;border-radius:10px;padding:6px 16px'><span class='mono' style='font-size:20px;color:#fff;letter-spacing:3px'>URGENT RECRUITMENT FOR</span></div>
 <div class='an' style='font-size:120px;color:#fff;line-height:1;margin-top:10px'>UKRAINE</div>
 <div style='display:inline-block;background:{YEL};padding:6px 16px;margin-top:6px'><span class='an' style='font-size:32px;color:{INK}'>SKILLED CONSTRUCTION WORKERS</span></div>
 <div class='ar' style='font-size:22px;font-weight:700;color:#DCE6F5;margin-top:14px'>Limited vacancies · Build your future in Ukraine</div></div>
<div class='abs' style='top:480px;left:0;width:1080px;height:560px;background:linear-gradient(180deg,{YEL} 0 6px,#E9EEF6 6px)'></div>
{card('ua_tile_installer', 'CERAMIC TILE INSTALLERS', '15–20 skilled workers', 'EXPECTED OUTPUT', '10–14 m² per person / day', 30)}
{card('ua_plasterer', 'PLASTERING WORKERS', '12 skilled workers', 'TARGET', '3-person team to complete 100 m² / day', 555)}
<div class='abs' style='top:1080px;left:30px;right:30px;height:0'></div>
<div class='abs' style='top:1124px;left:0;width:1080px;height:0'></div>
<div class='abs' style='top:1040px;left:0;width:1080px;height:110px;background:{BLU};display:flex'>{strip}</div>
{contact_bar(1166, INK, YEL, INK, YEL)}"""
    return page(body, "#E9EEF6")


# ------------------------------------------------------------------ 4. SERBIA — two big photos, red/blue diagonal
def serbia():
    RED, BLU, INK = "#C6363C", "#0C4076", "#0D1B2A"

    def half(img, title, sal, x):
        return (f"<div class='abs' style='top:250px;left:{x}px;width:507px;height:560px;border-radius:24px;overflow:hidden;box-shadow:0 12px 26px #0005'>"
                f"<img src='{P(img)}' style='width:100%;height:390px;object-fit:cover;object-position:center 20%;display:block'>"
                f"<div style='position:absolute;top:300px;left:0;background:{RED};padding:6px 20px 6px 22px;clip-path:polygon(0 0,100% 0,92% 100%,0 100%)'>"
                f"<span class='an' style='font-size:52px;color:#fff;line-height:1'>{title}</span></div>"
                f"<div style='height:170px;background:{BLU};display:flex;flex-direction:column;align-items:center;justify-content:center'>"
                f"<span class='mono' style='font-size:18px;color:#BFD3EE;letter-spacing:3px'>SALARY</span>"
                f"<span class='an' style='font-size:76px;color:#fff;line-height:1'>{sal}</span>"
                f"<span class='ar' style='font-size:20px;font-weight:700;color:#BFD3EE'>per month</span></div></div>")
    tiles = "".join(f"<div style='flex:1;background:#fff;border-radius:18px;box-shadow:0 6px 14px #0002;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:6px'>"
                    f"<div style='width:52px;height:52px;border-radius:50%;background:{BLU};display:flex;align-items:center;justify-content:center'>{icon(ic, 28, '#fff', 2.3)}</div>"
                    f"<span class='mono' style='font-size:14px;color:#5A6880;margin-top:6px'>{l}</span>"
                    f"<span class='ar' style='font-size:21px;font-weight:800;color:{INK};text-align:center;line-height:1.15'>{v}</span></div>"
                    for ic, l, v in (("home", "ACCOMMODATION", "Provided by employer"), ("bus", "TRANSPORTATION", "Provided by employer"),
                                     ("clock", "DUTY HOURS", "8 hours per day"), ("calendar", "PROCESSING TIME", "90 to 120 days")))
    docs = "".join(f"<div style='display:flex;align-items:center;gap:10px'><span class='an' style='width:34px;height:34px;border-radius:50%;background:{RED};color:#fff;font-size:20px;display:flex;align-items:center;justify-content:center'>{i+1}</span>"
                   f"<span class='ar' style='font-size:21px;font-weight:700;color:#fff'>{t}</span></div>"
                   for i, t in enumerate(("Updated CV", "National Identity Card (NIC)", "Passport", "Recent Photograph", "Experience Certificate")))
    body = f"""
<svg class='abs' style='left:0;top:0' width='1080' height='1350'><path d='M0 0 H1080 V180 L0 300Z' fill='{RED}'/><path d='M0 300 L1080 180 V200 L0 320Z' fill='#fff'/><path d='M0 320 L1080 200 V250 L0 370Z' fill='{BLU}'/></svg>
<div class='abs' style='top:20px;left:30px;background:#fff;border-radius:16px;padding:4px 14px'>{logo_img('logo-horizontal-light', 'width:360px;height:90px')}</div>
<div class='abs' style='top:18px;right:28px;filter:drop-shadow(0 4px 8px #0006)'>{flag('rs2', 150, True, 'rsx')}</div>
<div class='abs' style='top:124px;left:34px'><span class='an' style='font-size:76px;color:#fff;line-height:1'>SERBIA <span style='color:#FFE0E0'>JOB OPPORTUNITY</span></span></div>
{half('rs_plaster_mason', 'PLASTER MASON', '€700–€800', 24)}
{half('rs_tile_mason', 'TILE MASON', '€700–€900', 549)}
<div class='abs' style='top:830px;left:24px;right:24px;height:132px;display:flex;gap:12px'>{tiles}</div>
<div class='abs' style='top:978px;left:24px;right:24px;height:184px;background:{BLU};border-radius:22px;display:flex;padding:14px 22px;gap:22px'>
 <div style='width:220px;display:flex;flex-direction:column;justify-content:center'>{icon('doc', 52, '#FFD23F', 2)}<span class='an' style='font-size:36px;color:#FFD23F;line-height:1.05;margin-top:6px'>REQUIRED<br>DOCUMENTS</span></div>
 <div style='flex:1;display:grid;grid-template-columns:1fr 1fr;gap:8px 18px;align-content:center'>{docs}</div></div>
{contact_bar(1176, INK, '#fff', INK, '#FFD23F', 'LIMITED VACANCIES', 'Apply now · CV on WhatsApp or email')}"""
    return page(body, "#EEF2F7")


if __name__ == "__main__":
    from common import overflow_report
    for name, fn in (("Belarus-Skilled-Trades", belarus), ("Kosovo-27-Jobs", kosovo), ("Ukraine-Construction", ukraine), ("Serbia-Masons", serbia)):
        print(render(fn(), f"RS-Links-{name}-English.png"))
