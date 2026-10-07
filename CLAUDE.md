# Boomkraft Outreach Rules

Rules Claude must follow when scraping leads, drafting, and sending emails
from the Boomkraft account in this repo. Fill in the `TODO` sections with
your specifics — until then, Claude should treat the defaults below as
placeholders, not confirmed policy, and ask before sending anything.

## Tone & voice

TODO — describe the tone (formal/casual), voice, and any banned claims or
required disclaimers for outreach emails.

## Compliance

TODO — confirm/adjust. Defaults until specified otherwise:
- Every email includes an unsubscribe/opt-out instruction and Boomkraft's
  physical mailing address (CAN-SPAM).
- No purchased/scraped email lists without a lawful basis to contact them.
- Honor opt-outs and do-not-contact requests permanently — track them
  somewhere in `leads/` and check before every send.
- No misleading subject lines or sender information.

## Send limits & cadence

TODO — confirm/adjust. Defaults until specified otherwise:
- Draft-first: no email sends automatically without explicit human approval.
- Max sends per day: TODO (placeholder: 50/day).
- Delay between individual sends: TODO (placeholder: a few seconds, to avoid
  spam-filter triggers).
- No more than one initial outreach email per lead; follow-up cadence: TODO.

## Data handling

- Lead data (`leads/`) and drafts (`drafts/`) contain personal data and must
  never be committed to Git (enforced by `.gitignore`).
- Scraping should only pull publicly available website content; see
  `README.md` for what's in scope.

## Recruitment ad design rules (RS Links)

- **Every ad must include a prominent picture of the positions being advertised, showing people
  doing the job** (e.g. a rider riding a bike, a driver at the wheel, a worker on the factory
  floor, a tailor at a sewing machine, a cleaner mopping). Small icon-sized thumbnails alone are
  not enough: at least one large hero image or scene, or a large picture per job card.
- Use real photos from `assets/photos/` when available; otherwise use the illustrations in
  `src/illustrations.py` (add a new one for any trade that doesn't have one yet).
- Never reuse photos from other agencies' ads (they are content sources only).
