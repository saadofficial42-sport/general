# Employee contracts

Per-employee input files (`<name>.json`) and generated contracts (`.docx`/`.pdf`)
live here. They contain personal data (CNIC, salary) and are excluded from Git.

Generate a contract:

    node scripts/make-contract.js contracts/<name>.json

Optionally place the company letterhead image at `contracts/letterhead.png`; it
replaces the text letterhead at the top of every page.
