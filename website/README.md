# Recruitment agency website

A single-page website for a Rawalpindi–Islamabad recruitment consultancy and
licensed Overseas Employment Promoter (OEP). Everything lives in
`index.html`: no build step, no dependencies. Open it in a browser to preview.

## Before launch, replace the placeholders

1. **Business name.** "Margalla Global Recruitment" is a placeholder. Find and
   replace it throughout `index.html` (title, meta tags, logo, footer, JSON-LD).
2. **Contact details and licence number.** Edit the `SITE` object near the
   bottom of `index.html`. Phone, WhatsApp, email, address, hours and the
   BE&OE licence number update everywhere on the page from there.
3. **Enquiry form.** With `formEndpoint` empty, the form hands the enquiry to
   WhatsApp. To receive submissions by email, create a free form at
   [Formspree](https://formspree.io) (or similar) and paste its URL into
   `formEndpoint`.
4. **Job listings.** The `JOBS` array holds sample openings. Replace them with
   real, BE&OE-approved demands, then delete the "Sample listings" note.

## Hosting

`.github/workflows/deploy-website.yml` publishes the `website/` folder to
GitHub Pages on every push that touches it.

One-time setup: repository **Settings → Pages → Build and deployment → Source:
GitHub Actions**. GitHub Pages on a private repository needs a paid GitHub
plan; otherwise make the repository public or host on Netlify/Vercel/Cloudflare
Pages by pointing them at the `website/` folder (no build command).

Custom domain: add it under Settings → Pages, then create the DNS records your
registrar needs (a `CNAME` record for `www` pointing to
`<username>.github.io`).
