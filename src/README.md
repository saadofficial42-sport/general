# Ad generator

- `common.py`: shared fonts (local TTFs in `assets/fonts/`), brand colours,
  accurate flags (`flag("pakistan")`, `flag("uzbekistan")`, waving or flat),
  WhatsApp icon, line icons, logo loading and derivation, and
  `render(html, "name.png")`, which renders a 1080×1350 PNG into `output/`.
- One `style_<name>.py` per design style. Each takes a data dict with EN and UR
  text and writes `output/RS-Links-<Country>-<Role>-{English,Urdu}.png`.
- Add a country's flag to `FLAGS` in `common.py` after checking its official spec.

Requires: `pip install playwright pillow`. Chromium is taken from
`/opt/pw-browsers/chromium` when present; otherwise run `playwright install chromium`.

## Styles
- `style_corporate_grid.py` — corporate navy/gold grid; data: `data/uzbekistan_combined.py`.
  Run: `cd src && python3 style_corporate_grid.py uzbekistan_combined`

## Photos
Drop real photos into `assets/photos/` named `rider`, `driver`, `factory`, `tailor`
(`.jpg/.png/.webp`); they replace the illustrations automatically (cropped to circles).
