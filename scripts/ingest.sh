#!/usr/bin/env bash
# Headless ingest sweep — safe to run from cron on any machine where the
# `claude` CLI is authenticated and this repo has a configured remote:
#
#   0 * * * * /path/to/Sec-brain/scripts/ingest.sh >> /path/to/Sec-brain/.ingest.log 2>&1
#
# Exits silently when the inbox is empty or another sweep is already running.
set -euo pipefail
cd "$(dirname "$0")/.."

# Never run two sweeps at once.
exec 9>".ingest.lock"
flock -n 9 || exit 0

# Pick up sources added remotely (e.g. committed to raw/ via GitHub web/mobile).
git pull --rebase --quiet || true

# Anything waiting in the inbox?
pending=$(find raw -maxdepth 1 -type f ! -name '.gitkeep' | head -1)
[ -z "$pending" ] && exit 0

# Run the loop. CLAUDE.md drives the behavior; the schema commits the result.
# If prompts still block a fully unattended run, replace the two flag lines
# with --dangerously-skip-permissions — but only on a machine you trust, and
# remember that raw/ contents are untrusted input (see CLAUDE.md Rules).
claude -p "Ingest every file in raw/ following CLAUDE.md. Then run python3 scripts/vault_check.py and fix anything it reports before committing." \
  --permission-mode acceptEdits \
  --allowedTools "Bash(git add:*)" "Bash(git commit:*)" "Bash(git mv:*)" "Bash(mv:*)" "Bash(mkdir:*)" "Bash(python3:*)"

git push --quiet || true
