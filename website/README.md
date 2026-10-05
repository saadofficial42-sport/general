# Company website

A multi-page static website for a Rawalpindi–Islamabad manpower recruitment
and HR consultancy. There's no build step: open `index.html` in a browser to
preview.

## Pages

| File | Page |
| --- | --- |
| `index.html` | Home |
| `recruitment.html` | Industries & roles: searchable directory of positions by category |
| `countries.html` | Destination countries with flags, sectors, roles and visa routes |
| `consultancy.html` | Corporate HR & business consultancy services |
| `visas.html` | Visit visas, student consultancy (study abroad), residency by investment |
| `partnerships.html` | Partnership types and models (worldwide and in Pakistan) |
| `about.html` | Company, mission, vision, values, ethical recruitment |
| `contact.html` | Enquiry form (employer / job seeker / partner / consultancy) and FAQ |
| `privacy.html`, `terms.html` | Legal pages. Have a lawyer review before launch |
| `404.html` | Not-found page |

## Where to edit things

- **Company name, phone, WhatsApp, email, address, map link, hours, social
  links, form endpoint:** `assets/js/config.js`. The header, footer and
  contact blocks on every page read from it. The page `<title>` and meta tags
  also contain the name, so find and replace it in the `.html` files too.
- **Industries, job titles, countries:** `assets/js/data.js`. The directory,
  country explorer, flag strips and counters all update from it.
- **Styles:** `assets/css/site.css`. **Animations and behaviour:**
  `assets/js/site.js`.
- **Logo:** `assets/img/`. See `../brand/README.md` to regenerate the PNGs.
- **Flags:** `assets/flags/` (flag-icons, MIT licence).

## Forms

With `formEndpoint` empty, the forms hand the enquiry over to WhatsApp. To
receive submissions by email, create a form at [Formspree](https://formspree.io)
(or similar) and paste its URL into `formEndpoint`.

## Before launch

1. Replace the placeholder name, contact details and map link in `config.js`.
2. Replace `https://example.com` in `sitemap.xml` and `robots.txt` with the
   live domain.
3. Review the privacy policy and terms.

## Hosting

`.github/workflows/deploy-website.yml` publishes this folder to GitHub Pages.
One-time setup: **Settings → Pages → Source: GitHub Actions**, and allow the
deploying branch under **Settings → Environments → github-pages**. Netlify,
Vercel or Cloudflare Pages also work: point them at the `website/` folder with
no build command.
