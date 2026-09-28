# Brand assets

The logo mark is `website/assets/img/logo-mark.svg`: a hex nut (industry,
trades) holding a worker figure made of a head and two rising chevrons
(growth, moving forward).

Palette: petrol `#0A1B25` / `#123444`, green `#3DBB8A`, amber `#F0B545`.
Type: Bricolage Grotesque ExtraBold (name), IBM Plex Mono (tagline).

## Regenerating the PNGs (e.g. after a name change)

    npm i playwright
    BRAND_NAME="Your Name" BRAND_TAG="Recruitment & Consultancy" node brand/render-logo.mjs

This rewrites every PNG in `website/assets/img/` (horizontal logos for light
and dark backgrounds, stacked logo, app icon, transparent mark, and the
social-sharing image). Fonts are embedded in `fonts-inline.css` so the
render needs no network access.
