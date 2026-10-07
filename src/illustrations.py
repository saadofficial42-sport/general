"""Semi-flat SVG illustrations of trades and landmarks (viewBox 0 0 200 200
for trades). Used when no real photo exists in assets/photos/."""
from common import C, PHOTOS

SKIN = "#C98C5E"
SKIN_D = "#A86F45"
HAIR = "#1B1B1B"
INK = "#10212E"


def _bg(uid, c1, c2):
    return (f'<defs><radialGradient id="{uid}g" cx=".5" cy=".38" r=".7">'
            f'<stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></radialGradient></defs>'
            f'<rect width="200" height="200" fill="url(#{uid}g)"/>')


def rider(uid="rd"):
    return f"""{_bg(uid, '#EAF6EF', '#BFE3CF')}
<path d="M0 168 H200 V200 H0z" fill="#9FCDB4"/>
<path d="M0 172 H200" stroke="#fff" stroke-width="2" stroke-dasharray="14 10" opacity=".8"/>
<ellipse cx="102" cy="176" rx="82" ry="6" fill="#000" opacity=".14"/>
<!-- delivery box -->
<rect x="22" y="70" width="52" height="46" rx="5" fill="{C['gold']}"/>
<rect x="22" y="84" width="52" height="9" fill="{C['green']}"/>
<rect x="22" y="70" width="52" height="46" rx="5" fill="none" stroke="#C98A1E" stroke-width="2"/>
<path d="M36 116 L36 124 M62 116 L62 124" stroke="{INK}" stroke-width="4"/>
<!-- wheels -->
<circle cx="52" cy="152" r="22" fill="{INK}"/><circle cx="52" cy="152" r="9" fill="#9BA7B0"/>
<circle cx="152" cy="152" r="22" fill="{INK}"/><circle cx="152" cy="152" r="9" fill="#9BA7B0"/>
<!-- scooter body -->
<path d="M30 140 Q34 120 62 122 L118 122 Q127 122 130 132 L136 148 L72 150 Q40 152 30 140Z" fill="{C['emerald2']}"/>
<path d="M126 128 L138 80 L152 80 L147 100 Q160 120 162 148 L136 148Z" fill="#17803B"/>
<path d="M30 140 Q34 120 62 122" stroke="#fff" stroke-width="2" fill="none" opacity=".5"/>
<circle cx="151" cy="90" r="5" fill="{C['gold2']}"/>
<path d="M140 80 L162 70" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
<path d="M60 120 Q86 108 112 116 L110 124 L62 126Z" fill="{INK}"/>
<!-- rider -->
<path d="M90 118 L120 120 L130 142" stroke="#16325C" stroke-width="13" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M126 144 L138 144" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
<path d="M80 120 Q76 86 98 70 L114 72 Q122 96 106 122Z" fill="#1F4E8C"/>
<path d="M96 74 L100 112" stroke="{C['gold']}" stroke-width="3"/>
<path d="M108 82 Q128 92 150 76" stroke="#1F4E8C" stroke-width="10" fill="none" stroke-linecap="round"/>
<circle cx="152" cy="75" r="5.5" fill="{SKIN}"/>
<rect x="100" y="60" width="9" height="10" fill="{SKIN_D}"/>
<circle cx="104" cy="50" r="17" fill="#F9F8F4"/>
<path d="M87 50 A17 17 0 0 1 121 50 L121 54 L87 54Z" fill="{C['green']}"/>
<path d="M108 46 Q122 44 122 56 L108 56Z" fill="#26476E"/>"""


def driver(uid="dv"):
    return f"""{_bg(uid, '#EEF3FB', '#C9D8EF')}
<path d="M0 162 H200 V200 H0z" fill="#AFC3E2"/>
<path d="M0 170 H200" stroke="#fff" stroke-width="2" stroke-dasharray="14 10" opacity=".8"/>
<ellipse cx="102" cy="168" rx="90" ry="6" fill="#000" opacity=".15"/>
<path d="M12 146 L15 122 Q22 112 46 108 L70 84 Q78 76 94 76 L134 76 Q148 76 158 88 L174 106 Q192 110 194 126 L194 142 Q194 150 186 150 L18 150 Q10 150 12 146Z" fill="#FBFBFD" stroke="{INK}" stroke-width="3"/>
<path d="M76 88 Q82 82 96 82 L110 82 L110 106 L58 106Z" fill="#2B5A8E"/>
<path d="M116 82 L134 82 Q144 82 152 92 L162 106 L116 106Z" fill="#2B5A8E"/>
<!-- driver in front window -->
<path d="M126 106 Q126 92 138 90 Q150 92 150 106Z" fill="{C['navy']}"/>
<circle cx="139" cy="88" r="8" fill="{SKIN}"/>
<path d="M131 86 Q131 77 139 77 Q147 77 147 85Z" fill="{HAIR}"/>
<path d="M146 98 Q156 100 158 106" stroke="{SKIN}" stroke-width="4" fill="none"/>
<path d="M88 76 L134 76" stroke="{INK}" stroke-width="2"/>
<path d="M113 82 L113 146 M60 112 L60 146" stroke="#C7CFD8" stroke-width="2"/>
<rect x="96" y="114" width="12" height="3" rx="1.5" fill="#9BA7B0"/>
<rect x="148" y="114" width="12" height="3" rx="1.5" fill="#9BA7B0"/>
<path d="M14 132 L194 132" stroke="#D5DCE4" stroke-width="2"/>
<path d="M184 116 L194 118 L194 126 L182 124Z" fill="{C['gold2']}"/>
<rect x="12" y="120" width="8" height="8" rx="2" fill="{C['red']}"/>
<circle cx="52" cy="150" r="21" fill="{INK}"/><circle cx="52" cy="150" r="9" fill="#9BA7B0"/>
<circle cx="156" cy="150" r="21" fill="{INK}"/><circle cx="156" cy="150" r="9" fill="#9BA7B0"/>"""


def factory(uid="fc"):
    return f"""{_bg(uid, '#EEF2F7', '#CBD6E4')}
<rect x="0" y="0" width="200" height="200" fill="none"/>
<!-- shelves in background -->
<rect x="140" y="40" width="54" height="96" fill="#B6C3D4"/>
<rect x="144" y="48" width="46" height="16" fill="#7E95B3"/><rect x="144" y="72" width="46" height="16" fill="#8FA4BF"/><rect x="144" y="96" width="46" height="16" fill="#7E95B3"/>
<!-- worker -->
<path d="M62 132 Q58 92 76 80 L112 80 Q130 92 126 132Z" fill="{C['navy']}"/>
<path d="M86 80 L94 96 L102 80" fill="#fff" opacity=".9"/>
<rect x="89" y="68" width="10" height="12" fill="{SKIN_D}"/>
<circle cx="94" cy="56" r="16" fill="{SKIN}"/>
<path d="M77 54 Q78 36 95 36 Q112 36 112 52 L77 52Z" fill="{C['navy']}"/>
<path d="M108 50 L122 52 L110 56Z" fill="{C['navy']}"/>
<path d="M112 92 Q124 108 132 116" stroke="{C['navy']}" stroke-width="11" fill="none" stroke-linecap="round"/>
<path d="M74 92 Q66 110 74 120" stroke="{C['navy']}" stroke-width="11" fill="none" stroke-linecap="round"/>
<circle cx="134" cy="118" r="6" fill="#E8EDF2"/><circle cx="76" cy="122" r="6" fill="#E8EDF2"/>
<!-- ironing table + garment -->
<rect x="20" y="128" width="164" height="9" rx="4" fill="#5C6B7A"/>
<path d="M50 137 L40 176 M150 137 L160 176" stroke="#5C6B7A" stroke-width="5"/>
<path d="M44 128 L112 128 L108 120 L50 120Z" fill="{C['emerald']}"/>
<path d="M118 128 L158 128 Q160 112 146 108 L128 108 Q118 112 118 128Z" fill="#F4F6F8" stroke="{INK}" stroke-width="2.5"/>
<path d="M128 108 Q130 98 142 100 L146 108" stroke="{INK}" stroke-width="4" fill="none"/>
<!-- folded stack + box -->
<rect x="22" y="104" width="22" height="7" fill="#2E5E9E"/><rect x="22" y="111" width="22" height="7" fill="#7FA6D6"/><rect x="22" y="118" width="22" height="9" fill="#2E5E9E"/>
<rect x="8" y="150" width="54" height="40" fill="#C8935A"/>
<rect x="8" y="150" width="54" height="8" fill="#B07B45"/>
<rect x="31" y="150" width="8" height="40" fill="#E2B988"/>"""


def tailor(uid="tl"):
    return f"""{_bg(uid, '#FBF4E6', '#EFD9AE')}
<!-- tailor -->
<path d="M28 150 Q22 98 44 86 L84 86 Q100 98 98 150Z" fill="#A9C7E8"/>
<path d="M36 150 Q34 106 48 92 L60 120 L72 92 Q88 106 88 150Z" fill="#26364A"/>
<rect x="56" y="72" width="10" height="14" fill="{SKIN_D}"/>
<circle cx="61" cy="58" r="16" fill="{SKIN}"/>
<path d="M45 56 Q44 38 62 38 Q78 38 78 54 Q70 46 58 48 Q50 50 45 56Z" fill="{HAIR}"/>
<path d="M50 66 Q61 82 72 66" stroke="{HAIR}" stroke-width="3" fill="none" opacity=".6"/>
<path d="M48 86 L50 140 M74 86 L72 140" stroke="{C['gold2']}" stroke-width="5"/>
<path d="M48 96 L50 96 M48 106 L50 106 M48 116 L50 116 M74 96 L72 96 M74 106 L72 106" stroke="{INK}" stroke-width="1.5"/>
<path d="M86 104 Q100 120 112 134" stroke="#A9C7E8" stroke-width="11" fill="none" stroke-linecap="round"/>
<circle cx="113" cy="136" r="6" fill="{SKIN}"/>
<!-- table -->
<rect x="10" y="148" width="186" height="10" rx="3" fill="#6B4A2B"/>
<path d="M30 158 L30 196 M176 158 L176 196" stroke="#6B4A2B" stroke-width="7"/>
<!-- fabric -->
<path d="M84 148 L196 148 L196 138 Q160 132 120 138 Q100 140 84 142Z" fill="{C['navy']}"/>
<!-- sewing machine -->
<rect x="104" y="136" width="86" height="12" rx="3" fill="{C['green']}"/>
<rect x="164" y="82" width="20" height="56" rx="4" fill="{C['green']}"/>
<rect x="110" y="80" width="74" height="20" rx="9" fill="{C['green']}"/>
<rect x="110" y="80" width="22" height="40" rx="6" fill="{C['green']}"/>
<path d="M118 86 L176 86" stroke="{C['gold']}" stroke-width="3"/>
<path d="M121 120 L121 134" stroke="#9BA7B0" stroke-width="2.5"/>
<circle cx="188" cy="96" r="10" fill="#2E5E4A"/><circle cx="188" cy="96" r="4" fill="{C['gold']}"/>
<rect x="150" y="72" width="8" height="10" rx="2" fill="{C['red']}"/>"""


TRADES = {"rider": rider, "driver": driver, "factory": factory, "tailor": tailor}


def photo_or_art(key, uid=None):
    """Real photo from assets/photos/<key>.(jpg|jpeg|png|webp) if present,
    otherwise the illustration. Returns HTML filling its container."""
    for ext in ("jpg", "jpeg", "png", "webp"):
        p = PHOTOS / f"{key}.{ext}"
        if p.exists():
            return f"<img src='{p.as_uri()}' style='width:100%;height:100%;object-fit:cover;display:block'>"
    art = TRADES[key](uid or key)
    return f'<svg viewBox="0 0 200 200" width="100%" height="100%" preserveAspectRatio="xMidYMid slice">{art}</svg>'


# ---------------------------------------------------------------- landmarks

def tashkent_tv_tower(x, base, h, fill):
    """Tashkent TV Tower silhouette: three splayed legs, shaft, two pods, spire."""
    s = h / 375
    def X(v): return x + v * s
    def Y(v): return base - v * s
    return f"""<g fill="{fill}">
<path d="M{X(-34)} {Y(0)} L{X(-5)} {Y(95)} L{X(5)} {Y(95)} L{X(34)} {Y(0)} L{X(24)} {Y(0)} L{X(0)} {Y(70)} L{X(-24)} {Y(0)}Z"/>
<path d="M{X(-3)} {Y(0)} L{X(-5)} {Y(95)} L{X(5)} {Y(95)} L{X(3)} {Y(0)}Z"/>
<rect x="{X(-5)}" y="{Y(240)}" width="{10*s}" height="{145*s}"/>
<rect x="{X(-14)}" y="{Y(105)}" width="{28*s}" height="{12*s}" rx="{4*s}"/>
<ellipse cx="{x}" cy="{Y(200)}" rx="{15*s}" ry="{8*s}"/>
<rect x="{X(-17)}" y="{Y(232)}" width="{34*s}" height="{24*s}" rx="{10*s}"/>
<ellipse cx="{x}" cy="{Y(240)}" rx="{20*s}" ry="{7*s}"/>
<rect x="{X(-3.5)}" y="{Y(330)}" width="{7*s}" height="{92*s}"/>
<rect x="{X(-1.2)}" y="{Y(375)}" width="{2.4*s}" height="{48*s}"/>
</g>"""


def registan(x, base, w, fill):
    """Registan (Samarkand): three madrasa portals with ribbed domes and minarets."""
    s = w / 300
    def X(v): return x + v * s
    def Y(v): return base - v * s
    parts = []
    for cx, pw, ph in ((50, 70, 80), (150, 84, 96), (250, 70, 80)):
        parts.append(f'<rect x="{X(cx-pw/2)}" y="{Y(ph)}" width="{pw*s}" height="{ph*s}"/>')
        for mx in (cx - pw / 2 - 8, cx + pw / 2 + 2):
            parts.append(f'<rect x="{X(mx)}" y="{Y(ph+30)}" width="{6*s}" height="{(ph+30)*s}"/>'
                         f'<rect x="{X(mx-1.5)}" y="{Y(ph+34)}" width="{9*s}" height="{5*s}"/>')
    parts.append(f'<ellipse cx="{X(100)}" cy="{Y(78)}" rx="{20*s}" ry="{24*s}"/><rect x="{X(80)}" y="{Y(78)}" width="{40*s}" height="{78*s}"/>')
    parts.append(f'<ellipse cx="{X(205)}" cy="{Y(74)}" rx="{17*s}" ry="{21*s}"/><rect x="{X(188)}" y="{Y(74)}" width="{34*s}" height="{74*s}"/>')
    return f'<g fill="{fill}">{"".join(parts)}</g>'


def skyline(width, height, fill, seed_offset=0):
    """Generic modern tower row for a city silhouette band."""
    import random
    r = random.Random(42 + seed_offset)
    x, parts = 0, []
    while x < width:
        w = r.randint(26, 60)
        h = r.randint(int(height * .25), int(height * .8))
        parts.append(f'<rect x="{x}" y="{height-h}" width="{w}" height="{h}"/>')
        if r.random() < .3:
            parts.append(f'<rect x="{x + w/2 - 1.5}" y="{height-h-14}" width="3" height="14"/>')
        x += w + r.randint(2, 10)
    return f'<g fill="{fill}">{"".join(parts)}</g>'


def mountains(width, height, far="#9FB7C9", near="#6E8BA3", snow="#FFFFFF"):
    """Tian Shan-style snow-capped ridge, two layers."""
    import random
    r = random.Random(7)
    def ridge(base_h, amp, n, fill, caps):
        pts, x = [(0, height)], 0
        peaks = []
        step = width / n
        for i in range(n + 1):
            x = i * step
            y = height - base_h - (amp * (0.55 + 0.45 * r.random()) if i % 2 else amp * 0.25 * r.random())
            pts.append((x, y))
            if i % 2:
                peaks.append((x, y))
        pts.append((width, height))
        d = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts) + "Z"
        out = f'<path d="{d}" fill="{fill}"/>'
        if caps:
            for (px, py) in peaks:
                out += (f'<path d="M{px - step*0.32:.1f},{py + amp*0.28:.1f} L{px:.1f},{py:.1f} L{px + step*0.32:.1f},{py + amp*0.28:.1f} '
                        f'L{px + step*0.12:.1f},{py + amp*0.2:.1f} L{px:.1f},{py + amp*0.3:.1f} L{px - step*0.14:.1f},{py + amp*0.18:.1f}Z" fill="{snow}"/>')
        return out
    return ridge(height * .35, height * .6, 12, far, True) + ridge(height * .12, height * .4, 9, near, False)


def yurt(x, base, w, fill="#F9F8F4", trim="#E53935"):
    """Kyrgyz yurt silhouette with a decorative band and door."""
    h = w * 0.62
    return f"""<g>
<path d="M{x} {base} L{x} {base - h*0.5} Q{x + w*0.5} {base - h*1.25} {x + w} {base - h*0.5} L{x + w} {base}Z" fill="{fill}"/>
<path d="M{x} {base - h*0.5} Q{x + w*0.5} {base - h*1.25} {x + w} {base - h*0.5}" stroke="{trim}" stroke-width="{w*0.05:.1f}" fill="none"/>
<rect x="{x}" y="{base - h*0.42}" width="{w}" height="{h*0.1:.1f}" fill="{trim}"/>
<rect x="{x + w*0.4}" y="{base - h*0.3}" width="{w*0.2}" height="{h*0.3}" fill="#8A4B2A"/>
<circle cx="{x + w*0.5}" cy="{base - h*0.93}" r="{w*0.06:.1f}" fill="{trim}"/></g>"""


def girih_pattern(pid, color, opacity=0.14, size=80):
    """<pattern> of 8-point Islamic stars for Silk Road backgrounds."""
    c = size / 2
    r1, r2 = size * 0.34, size * 0.16
    import math as m
    star = " ".join(f"{c + (r1 if i % 2 == 0 else r2*1.6) * m.cos(m.radians(i*22.5)):.1f},{c + (r1 if i % 2 == 0 else r2*1.6) * m.sin(m.radians(i*22.5)):.1f}" for i in range(16))
    return (f'<pattern id="{pid}" width="{size}" height="{size}" patternUnits="userSpaceOnUse">'
            f'<g fill="none" stroke="{color}" stroke-width="1.6" opacity="{opacity}">'
            f'<polygon points="{star}"/><rect x="{c - r2}" y="{c - r2}" width="{2*r2}" height="{2*r2}" transform="rotate(45 {c} {c})"/>'
            f'<path d="M0 0 L{size*0.16} {size*0.16} M{size} 0 L{size*0.84} {size*0.16} M0 {size} L{size*0.16} {size*0.84} M{size} {size} L{size*0.84} {size*0.84}"/></g></pattern>')


def _worker(x, base, s=1.0, shirt=None, pose="stand", flip=False, uid="w"):
    """Factory worker in cap and polo. pose: 'iron', 'pack', 'carry'."""
    shirt = shirt or C["navy"]
    tf = f"translate({x} {base}) scale({-s if flip else s} {s})"
    arms = {
        "iron": f'<path d="M16 -118 Q34 -96 52 -84" stroke="{shirt}" stroke-width="13" fill="none" stroke-linecap="round"/><circle cx="54" cy="-82" r="7" fill="#E8EDF2"/>'
                f'<path d="M-16 -118 Q-26 -96 -14 -84" stroke="{shirt}" stroke-width="13" fill="none" stroke-linecap="round"/><circle cx="-12" cy="-82" r="7" fill="#E8EDF2"/>',
        "pack": f'<path d="M16 -118 Q30 -100 30 -86" stroke="{shirt}" stroke-width="13" fill="none" stroke-linecap="round"/>'
                f'<path d="M-16 -118 Q-30 -100 -30 -86" stroke="{shirt}" stroke-width="13" fill="none" stroke-linecap="round"/>'
                f'<circle cx="30" cy="-84" r="7" fill="#E8EDF2"/><circle cx="-30" cy="-84" r="7" fill="#E8EDF2"/>',
        "carry": f'<path d="M14 -122 Q34 -112 36 -96" stroke="{shirt}" stroke-width="13" fill="none" stroke-linecap="round"/>'
                 f'<path d="M-14 -122 Q-6 -104 4 -96" stroke="{shirt}" stroke-width="13" fill="none" stroke-linecap="round"/>',
    }[pose]
    legs = (f'<path d="M-10 -70 L-12 0 M10 -70 L12 0" stroke="#22303F" stroke-width="15" stroke-linecap="round"/>'
            f'<path d="M-20 0 L-4 0 M4 0 L22 0" stroke="#111" stroke-width="7" stroke-linecap="round"/>') if pose == "carry" else ""
    box = (f'<rect x="-6" y="-124" width="62" height="50" fill="#C8935A"/><rect x="-6" y="-124" width="62" height="9" fill="#B07B45"/>'
           f'<rect x="20" y="-124" width="10" height="50" fill="#E2B988"/>'
           f'<circle cx="38" cy="-98" r="7" fill="#E8EDF2"/><circle cx="4" cy="-96" r="7" fill="#E8EDF2"/>') if pose == "carry" else ""
    return f"""<g transform="{tf}">{legs}
<path d="M-26 -66 Q-30 -122 -16 -134 L16 -134 Q30 -122 26 -66Z" fill="{shirt}"/>
<path d="M-8 -134 L0 -120 L8 -134" fill="#fff" opacity=".9"/>
<rect x="-6" y="-146" width="12" height="13" fill="{SKIN_D}"/>
<circle cx="0" cy="-160" r="17" fill="{SKIN}"/>
<path d="M-18 -162 Q-17 -182 1 -182 Q19 -182 18 -164Z" fill="{shirt}"/><path d="M14 -166 L30 -163 L16 -159Z" fill="{shirt}"/>
{arms}{box}</g>"""


def factory_scene(w, h, ur=False):
    """Factory floor with big windows onto Tashkent (TV Tower) and Samarkand
    (Registan), three workers: ironing, packing, carrying goods; hosiery
    stock shelves and boxes."""
    floor_y = h * 0.86
    win = (f'<rect x="{w*0.05}" y="{h*0.08}" width="{w*0.9}" height="{h*0.5}" rx="8" fill="#BFD9EE"/>'
           f'<g clip-path="url(#fswin)">'
           f'<rect x="0" y="0" width="{w}" height="{h}" fill="url(#fssky)"/>'
           f'<g transform="translate(0 {h*0.58 - 70})" opacity=".55">{skyline(int(w), 70, "#7FA3C4", 9)}</g>'
           f'{registan(w*0.12, h*0.58, 260, "#8FB0CC")}{tashkent_tv_tower(w*0.78, h*0.58, h*0.48, "#6E95BA")}</g>'
           + "".join(f'<rect x="{w*0.05 + i*w*0.18 - 3}" y="{h*0.08}" width="6" height="{h*0.5}" fill="#E9EEF3"/>' for i in range(1, 5)))
    shelves = "".join(
        f'<rect x="{sx}" y="{h*0.36}" width="120" height="{floor_y - h*0.36}" fill="#9AAFC6"/>'
        + "".join(f'<rect x="{sx+6}" y="{h*0.38 + k*34}" width="108" height="24" fill="{["#2E5E9E","#7FA6D6","#1E9E4A","#F0B443"][k%4]}" opacity=".9"/>' for k in range(int((floor_y - h*0.4)//34)))
        for sx in ([w*0.03] if not ur else [w*0.97 - 120]))
    tables = (f'<rect x="{w*0.24}" y="{floor_y-118}" width="{w*0.62}" height="14" rx="4" fill="#5C6B7A"/>'
              f'<path d="M{w*0.27} {floor_y-104} L{w*0.27} {floor_y} M{w*0.83} {floor_y-104} L{w*0.83} {floor_y}" stroke="#5C6B7A" stroke-width="8"/>'
              f'<rect x="{w*0.3}" y="{floor_y-132}" width="110" height="14" fill="{C["emerald"]}"/>'
              f'<path d="M{w*0.3+70} {floor_y-118} L{w*0.3+118} {floor_y-118} Q{w*0.3+120} {floor_y-140} {w*0.3+104} {floor_y-146} L{w*0.3+84} {floor_y-146} Q{w*0.3+70} {floor_y-138} {w*0.3+70} {floor_y-118}Z" fill="#F4F6F8" stroke="{INK}" stroke-width="3"/>'
              f'<rect x="{w*0.6+18}" y="{floor_y-176}" width="96" height="58" fill="#C8935A"/><rect x="{w*0.6+18}" y="{floor_y-176}" width="96" height="10" fill="#B07B45"/>'
              f'<rect x="{w*0.6+60}" y="{floor_y-176}" width="12" height="58" fill="#E2B988"/>'
              f'<rect x="{w*0.6+130}" y="{floor_y-140}" width="44" height="9" fill="#2E5E9E"/><rect x="{w*0.6+130}" y="{floor_y-131}" width="44" height="9" fill="#7FA6D6"/>')
    behind = (_worker(w*0.33, floor_y - 40, 1.0, C["navy"], "iron") +
              _worker(w*0.57, floor_y - 40, 1.0, C["green"], "pack"))
    workers = _worker(w*0.93 if not ur else w*0.07, floor_y + 6, 0.95, "#1F4E8C", "carry", flip=ur)
    stack = "".join(f'<rect x="{(w*0.12 if not ur else w*0.84)}" y="{floor_y - 44*(k+1)}" width="70" height="42" fill="#C8935A" stroke="#B07B45" stroke-width="2"/>' for k in range(3))
    return f"""<defs><clipPath id="fswin"><rect x="{w*0.05}" y="{h*0.08}" width="{w*0.9}" height="{h*0.5}" rx="8"/></clipPath>
<linearGradient id="fssky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9CC7EA"/><stop offset="1" stop-color="#E3F0FA"/></linearGradient>
<linearGradient id="fswall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E7ECF2"/><stop offset="1" stop-color="#D3DCE6"/></linearGradient></defs>
<rect width="{w}" height="{h}" fill="url(#fswall)"/>{win}
<rect y="{floor_y}" width="{w}" height="{h-floor_y}" fill="#B9C4CF"/>
<path d="M0 {floor_y} H{w}" stroke="#9AA8B6" stroke-width="3"/>{shelves}{stack}{behind}{tables}{workers}"""


def ce_truck(uid="ce"):
    """CE category: articulated lorry (tractor unit + trailer)."""
    return f"""{_bg(uid, '#EEF3FB', '#C9D8EF')}
<path d="M0 150 H200 V200 H0z" fill="#AFC3E2"/>
<rect x="8" y="70" width="120" height="66" rx="4" fill="#F4F6F8" stroke="{INK}" stroke-width="3"/>
<rect x="16" y="80" width="104" height="10" fill="{C['navy']}" opacity=".85"/>
<path d="M128 132 L128 88 Q130 78 142 78 L166 78 Q176 78 182 90 L192 108 L192 132Z" fill="{C['navy']}"/>
<path d="M146 86 L166 86 Q172 86 176 94 L182 106 L146 106Z" fill="#9CC7EA"/>
<circle cx="160" cy="96" r="6" fill="{SKIN}"/><path d="M153 106 Q153 98 160 98 Q167 98 167 106Z" fill="#26364A"/>
<rect x="8" y="132" width="186" height="8" fill="{INK}"/>
<circle cx="36" cy="146" r="14" fill="{INK}"/><circle cx="36" cy="146" r="6" fill="#9BA7B0"/>
<circle cx="68" cy="146" r="14" fill="{INK}"/><circle cx="68" cy="146" r="6" fill="#9BA7B0"/>
<circle cx="168" cy="146" r="14" fill="{INK}"/><circle cx="168" cy="146" r="6" fill="#9BA7B0"/>
<rect x="186" y="112" width="8" height="8" fill="{C['gold2']}"/>"""


def precast_worker(uid="pc"):
    """Precast concrete installation: crane hook lowering a panel, worker in hard hat + vest."""
    return f"""{_bg(uid, '#FFF6E5', '#F5DEB0')}
<path d="M0 168 H200 V200 H0z" fill="#C9B79A"/>
<path d="M150 0 L150 40 M150 40 L150 60" stroke="{INK}" stroke-width="3"/>
<path d="M144 60 Q150 70 156 60" stroke="{INK}" stroke-width="3" fill="none"/>
<path d="M150 64 L118 88 M150 64 L182 88" stroke="{INK}" stroke-width="2"/>
<rect x="112" y="88" width="76" height="70" fill="#A9AFB5" stroke="#7D848B" stroke-width="3"/>
<path d="M122 100h56M122 116h56M122 132h56" stroke="#8F969D" stroke-width="2"/>
<rect x="20" y="150" width="90" height="18" fill="#A9AFB5" stroke="#7D848B" stroke-width="2"/>
<path d="M52 150 Q48 108 62 98 L86 98 Q98 108 94 150Z" fill="#C6E24A"/>
<path d="M58 100 L58 148 M90 100 L90 148" stroke="#F4F6F8" stroke-width="4"/>
<rect x="69" y="86" width="10" height="12" fill="{SKIN_D}"/>
<circle cx="74" cy="72" r="15" fill="{SKIN}"/>
<path d="M56 72 Q56 50 74 50 Q92 50 92 72Z" fill="{C['gold2']}"/><rect x="52" y="68" width="44" height="6" rx="3" fill="#E8B400"/>
<path d="M92 108 Q108 104 114 96" stroke="#C6E24A" stroke-width="10" fill="none" stroke-linecap="round"/>
<circle cx="115" cy="95" r="6" fill="#5C6B7A"/>"""


def cleaner(uid="cl"):
    """Cleaning worker with mop and trolley."""
    return f"""{_bg(uid, '#EAF6F3', '#C3E6DD')}
<path d="M0 166 H200 V200 H0z" fill="#D9E3EA"/>
<ellipse cx="64" cy="170" rx="38" ry="6" fill="#9CC7EA" opacity=".8"/>
<rect x="128" y="104" width="54" height="56" rx="4" fill="{C['navy']}"/>
<rect x="134" y="86" width="16" height="20" rx="3" fill="{C['gold2']}"/><rect x="156" y="80" width="14" height="26" rx="3" fill="#2DB0E0"/>
<circle cx="138" cy="164" r="6" fill="{INK}"/><circle cx="174" cy="164" r="6" fill="{INK}"/>
<path d="M78 158 L76 118 M92 158 L96 118" stroke="#3F4E5E" stroke-width="12" stroke-linecap="round"/>
<path d="M68 122 Q64 82 78 72 L100 72 Q112 82 108 122Z" fill="#2C4F7C"/>
<path d="M76 74 L76 120 M102 74 L102 120" stroke="#7E8C9A" stroke-width="5"/>
<rect x="84" y="60" width="10" height="13" fill="{SKIN_D}"/>
<circle cx="89" cy="46" r="15" fill="{SKIN}"/>
<path d="M73 44 Q73 28 89 28 Q105 28 105 42Z" fill="{C['navy']}"/><path d="M101 40 L116 43 L103 46Z" fill="{C['navy']}"/>
<path d="M70 84 Q56 100 52 112" stroke="#2C4F7C" stroke-width="10" fill="none" stroke-linecap="round"/>
<circle cx="51" cy="113" r="6" fill="#2DB0E0"/>
<path d="M58 70 L34 162" stroke="#8A5A12" stroke-width="4"/>
<path d="M18 160 L52 160 L50 170 L20 170Z" fill="#2DB0E0"/>"""


TRADES.update({"ce_truck": ce_truck, "precast": precast_worker, "cleaner": cleaner})


def kosovo_skyline(w, h, fill, accent=None):
    """Kosovo landmarks: Prizren fortress on its hill + Sinan Pasha Mosque
    (dome and tall minaret) on the left; Pristina's NEWBORN monument
    (block letters) and modern blocks on the right."""
    accent = accent or fill
    b = h
    hill = f'<path d="M0 {b} L0 {b-60} Q80 {b-120} 170 {b-96} Q230 {b-80} 260 {b-40} L260 {b}Z"/>'
    fort = (f'<rect x="70" y="{b-142}" width="80" height="34"/>'
            + "".join(f'<rect x="{70 + i*12}" y="{b-150}" width="7" height="9"/>' for i in range(7))
            + f'<rect x="132" y="{b-170}" width="16" height="30"/>')
    mosque = (f'<rect x="250" y="{b-70}" width="90" height="70"/>'
              f'<path d="M262 {b-70} Q295 {b-130} 328 {b-70}Z"/>'
              f'<rect x="293" y="{b-140}" width="4" height="14"/>'
              f'<rect x="352" y="{b-175}" width="12" height="175"/><path d="M350 {b-175} L358 {b-205} L366 {b-175}Z"/>'
              f'<rect x="349" y="{b-140}" width="18" height="5"/>')
    blocks = "".join(f'<rect x="{x}" y="{b-hh}" width="{ww}" height="{hh}"/>' for x, ww, hh in
                     ((600, 46, 90), (652, 30, 130), (690, 54, 70), (900, 40, 110), (946, 60, 80), (1012, 50, 120)))
    newborn = (f'<g transform="translate(740 {b-12})"><rect x="-6" y="0" width="160" height="12" fill="{accent}"/>'
               f'<text x="74" y="-4" text-anchor="middle" font-family="Anton" font-size="44" letter-spacing="2" fill="{accent}">NEWBORN</text></g>')
    return f'<g fill="{fill}">{hill}{fort}{mosque}{blocks}</g>'
