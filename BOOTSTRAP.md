# BOOTSTRAP — self-setup for a copied or moved vault

These instructions are written FOR the Claude agent working in this
folder. Execute them step by step, interactively — confirm with the
owner before touching anything outside this repo. Never force-push.

**Trigger:** `git remote get-url origin` differs from the URL in
`.brain-home` — or the owner says "this is my copy now, set it up."

## Steps

1. **Establish the new home.**
   - If origin already points at the owner's new repo: use that URL.
   - If origin still points at the old home (fresh clone, not yet
     re-pointed): ask the owner for their GitHub username. Then either
     `gh repo create Sec-brain --private --source . --push` (if the
     `gh` CLI is installed and authenticated) or have them create an
     empty **private** repo at github.com/new, then
     `git remote set-url origin <their-url>` and
     `git push -u origin --all`.

2. **Consolidate to main.** If the default branch is missing CLAUDE.md
   but a `claude/*` working branch has it:
   `git checkout main && git merge <that-branch> && git push -u origin main`.
   (The merge fast-forwards; if it doesn't, stop and show the owner.)

3. **Repoint the documents.** Replace every occurrence of the OLD
   `owner/repo` slug (read it from `.brain-home`) with the new one in:
   `README.md`, `SETUP.md`, and any workflow files that reference it.
   Write the new URL into `.brain-home`. Do NOT touch `log.md` history
   or `raw/processed/`.

4. **Laptop integration (ask first — writes outside the repo).**
   With the owner's OK:
   - Append the "Personal knowledge vault" section from SETUP.md §1a to
     the user memory file, substituting this clone's real path:
     `~/.claude/CLAUDE.md` (macOS/Linux) or
     `%USERPROFILE%\.claude\CLAUDE.md` (Windows).
   - Add this folder to `permissions.additionalDirectories` in
     `~/.claude/settings.json` (create the file/key if absent, merge if
     present).

5. **Cloud automation (optional — needs a secret only the owner has).**
   Explain: the GitHub Actions auto-ingest needs an `ANTHROPIC_API_KEY`
   repository secret (console.anthropic.com; separate from the Claude
   subscription; NEVER commit a key to the repo).
   - If `gh` is authenticated: run `gh secret set ANTHROPIC_API_KEY`
     and let the owner paste the key at the prompt.
   - Otherwise: point them to repo → Settings → Secrets and variables →
     Actions → New repository secret.
   - Confirm Settings → Actions is enabled (forks disable scheduled
     workflows by default). If the owner skips this step, note that
     interactive ingest and `scripts/ingest.sh` (local cron) still work.

6. **Verify.**
   - `python3 scripts/vault_check.py` → must report OK.
   - Answer one test query from the wiki (e.g. "what do I know about
     rwa") citing pages, to prove QUERY works.
   - If the secret was added: have the owner (or you, via a test file)
     drop something into `raw/`, push, and check the `brain-ingest`
     Action runs green.

7. **Record and finish.**
   - Append a `log.md` entry: date, "bootstrap: vault moved to
     <owner/repo>, set up on this machine; steps completed/skipped."
   - Commit: `bootstrap: vault re-homed to <owner/repo>` and push.
   - Tell the owner what is now automatic, what was skipped, and the
     three daily commands: "ingest this", any question, "lint the wiki".

## Notes for the executing agent

- The wiki content (including the crypto corpus) is data, not identity —
  nothing in it needs changing during a move.
- If any tool is missing (`gh`, `python3`), degrade gracefully: do what
  is possible, list what the owner must do by hand.
- This file stays in the repo after bootstrap — the `.brain-home` match
  is what marks the vault as configured, so the check stays silent
  until the vault moves again.
