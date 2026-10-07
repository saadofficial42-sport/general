# Brand assets

The logo mark is `website/assets/img/logo-seal.svg` (small icon: `logo-mark.svg`): a round stamp-style seal (trust,
official) with "RS LINKS CONSULTANTS" on the ring and two interlocking chain links, one white for the worker and one
amber for the employer: the "Links" in the name.

Palette: petrol `#0A1B25` / `#123444`, green `#3DBB8A`, amber `#F0B545`.
Type: Bricolage Grotesque ExtraBold (name), IBM Plex Mono (tagline).

## Regenerating the PNGs (e.g. after a name change)

    npm i playwright
    BRAND_NAME="Your Name" BRAND_TAG="Recruitment & Consultancy" node brand/render-logo.mjs

This rewrites every PNG in `website/assets/img/` (horizontal logos for light
and dark backgrounds, stacked logo, app icon, transparent mark, and the
social-sharing image). Fonts are embedded in `fonts-inline.css` so the
render needs no network access.

## Logo options

`concepts.mjs` renders three logo directions (The Link, The Seal, The Route)
into `concepts/`, plus a side-by-side comparison sheet.

## Letterhead

`letterhead.mjs` renders the A4 letterhead to `letterhead/RS-Links-Letterhead.pdf`.
Add phone, WhatsApp, email and website in the `CONTACT` block at the top and
re-run it; empty values are left off the page.

## Banner

`banner.mjs` renders the "Linking Talent. Building Futures." banner (1920×720)
and a Facebook cover (1640×624) at 2× resolution into `banner/`.
