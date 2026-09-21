# Boomkraft Outreach

Operations repo for Boomkraft's personalized lead outreach: scraping lead
context, drafting customized emails, and sending them from the Boomkraft
account.

## Folder structure

- **`templates/`** — Reusable email templates and prompt snippets (subject
  lines, body structures, tone/voice guides) used as the base for
  personalized emails. No lead-specific or personal data belongs here — this
  folder is meant to be committed to Git.

- **`leads/`** — Lead lists (CSV/JSON) with prospect details: names, emails,
  companies, websites, LinkedIn URLs, and any scraped notes. This contains
  personal data and is excluded from Git via `.gitignore` — keep it local or
  in a secure store.

- **`drafts/`** — Generated, per-lead email drafts pending review/approval
  before sending. Also contains personal data and is excluded from Git.

- **`scripts/`** — Automation scripts: scraping lead context, generating
  drafts, and sending approved emails. Scripts are committed; the data they
  read/write (in `leads/` and `drafts/`) is not.

## Rules

Outreach rules and constraints (tone, compliance, what's allowed/not) live in
`CLAUDE.md` at the repo root.
