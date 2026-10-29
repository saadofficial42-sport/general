"""Purple colour version of the round badge logo (2026-10-29, user): green -> dark purples, yellow/gold -> white.
Everything else (navy ring, cream band, text, layout) is unchanged. Because both chain links are now white, each link
gets a thin dark-purple outline so the two links still read as separate interlocking pieces. The two small diamonds
on the cream ring were gold; white would vanish on cream, so they use the dark purple instead.
Outputs output/logo-vector/RS-Links-Round-Logo-Purple.(ai|eps|svg) + _2000px.png"""
import logo_vector as lv

lv.GRN_L, lv.GRN, lv.GRN_D = "#8E5CC9", "#5B2A86", "#2E1050"
lv.GOLD, lv.GOLD_D = "#FFFFFF", "#4A1D73"
_link = lv.link


def link(cx, cy, color):
    outline = _link(cx, cy, "#2E1050").replace("stroke-width='30'", "stroke-width='38'")
    return outline + _link(cx, cy, color)


lv.link = link

if __name__ == "__main__":
    lv.main("RS-Links-Round-Logo-Purple")
