# Employee contracts

Per-employee input files (`<name>.json`) and generated contracts (`.docx`/`.pdf`)
live here. They contain personal data (CNIC, salary) and are excluded from Git.

Generate a contract:

    node scripts/make-contract.js contracts/<name>.json

The RS Links letterhead in `templates/letterhead/` is applied as the page
background (`first.jpg` on page 1 with REF/DATE, `cont.jpg` on later pages).
