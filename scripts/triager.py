"""
scripts/triager.py
Simple GitHub Issue Triager (ready-to-PR)

What this file contains
- A single-file Python utility that fetches open issues from a GitHub repo,
  heuristically classifies them (bug/feature/docs/question/other), prints a
  concise summary and remembers which issue IDs it's already shown so future
  runs only show new items.

Why add it as a utility script?
- Low-risk developer tooling that lives under scripts/ and helps maintainers
  and contributors get a quick view of open issues.

Usage (examples)
- Run locally (recommended):
    python scripts/triager.py --repo sentient-agi/ROMA

- Use an env var to increase GitHub rate limits (recommended):
    export GITHUB_TOKEN=ghp_xxx       # macOS / Linux / Termux
    setx GITHUB_TOKEN "ghp_xxx"     # Windows (persist)
    $env:GITHUB_TOKEN = "ghp_xxx"   # PowerShell (session)

- Provide token inline (less secure):
    python scripts/triager.py --repo sentient-agi/ROMA --
