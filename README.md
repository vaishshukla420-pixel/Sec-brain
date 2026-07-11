# Sec-brain

A compiled, self-maintaining knowledge base run by Claude Code — built on
Andrej Karpathy's [LLM knowledge base](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
pattern: **the vault is the codebase, the agent is the programmer,
[`CLAUDE.md`](CLAUDE.md) is the spec.**

Notes here don't just sit in storage. Every source that comes in is broken
into atomic pages and linked against everything already in the vault, so the
system compounds: each ingestion makes the existing notes more valuable.

## Layout

| Path | Role |
|---|---|
| `raw/` | Inbox — drop unprocessed sources here (articles, PDFs, transcripts, notes) |
| `raw/processed/` | Sources that have been ingested (immutable record) |
| `wiki/` | The brain — atomic, cross-linked markdown pages |
| `index.md` | Catalog of every page, grouped by topic (★ = hub) |
| `log.md` | Append-only history of every operation |
| `CLAUDE.md` | The schema — the rules the agent follows every session |
| `scripts/` | `vault_check.py` (mechanical lint) and `ingest.sh` (headless sweep) |

## Daily use

Open Claude Code in the vault root (`claude`), or open a Claude Code web
session on this repo. The schema loads automatically. Then:

| You say | What happens |
|---|---|
| `ingest this` (after dropping files in `raw/`) | Source → atomic pages, linked both ways, indexed, logged, committed |
| any question about the vault's content | Answer synthesized from the wiki with `[[page]]` citations; durable answers filed back as new pages |
| `lint the wiki` | Mechanical + semantic health report: contradictions, superseded claims, orphans, gaps. Reports only — never deletes |
| `weekly review` | Top ideas of the week, emerging connections and hubs, what to read next |

Open the repo folder as an Obsidian vault to browse the graph; per-device
Obsidian state is gitignored.

## Adding sources from anywhere (no VPS needed)

The vault lives in this GitHub repo, so **git is the sync layer**:

1. From your phone or browser, add a file to `raw/` via GitHub's web UI
   (Add file → Create/Upload) — a pasted article, a URL-plus-notes, anything.
2. The next Claude session against this repo — a web session, a scheduled
   Routine, or `scripts/ingest.sh` on any machine — pulls, ingests, and pushes
   the processed result back.

This replaces the "always-on VPS" setup entirely: state lives in the repo,
compute attaches to it on demand.

## Automation

Two GitHub Actions workflows run the loop hands-free
(`.github/workflows/`):

- **`brain-ingest`** — fires **instantly** on any push that touches `raw/`
  (e.g. a file uploaded from your phone via GitHub's web UI), plus a safety
  sweep every 6 hours. Empty inbox = the run exits immediately.
- **`brain-weekly`** — Mondays 09:00 IST: mechanical + semantic lint, the
  weekly review, then one self-feeding **gap-fill**: it researches the
  week's most important knowledge gap on the web and files it as sourced
  synthesis pages (rules in `CLAUDE.md` → GAP-FILL).

**One-time setup:** add an `ANTHROPIC_API_KEY` repository secret
(Settings → Secrets and variables → Actions → New repository secret).
Without it the workflows stay dormant. The vault currently lives on branch
`claude/implementability-review-99t3an`; scheduled runs hop to it while it
exists and fall back to the default branch after a merge.

Also available: **local cron** via `scripts/ingest.sh` — lock-protected,
exits instantly when the inbox is empty, safe to run hourly.

> **Full setup guide — laptop, other repos, phone, sharing with a
> teammate: see [SETUP.md](SETUP.md).**
>
> **Cloned this vault to your own account?** Open Claude Code in the
> folder and say *"this is my copy now, set it up"* — it self-installs
> from [BOOTSTRAP.md](BOOTSTRAP.md).

## Feeding the brain from other repos

The brain is ONE vault — this repo. Other repos don't stream in by
themselves; knowledge must land in `raw/`. Three bridges, from manual to
automatic:

1. **From anywhere, no setup:** add any file to `raw/` via GitHub web or
   mobile → auto-ingested by the `brain-ingest` workflow.
2. **From any Claude session in another repo (one line of setup):** put
   this in that repo's `CLAUDE.md`:
   *"When a session produces durable knowledge — research findings,
   decisions, lessons learned — distill it into a short markdown note and
   commit it to `vaishshukla420-pixel/Sec-brain` under `raw/` (add that
   repo to the session if needed)."*
   Every Claude session working there then feeds this brain as a side
   effect of normal work.
3. **Fully automatic bridge (one-time, per repo):** add a small GitHub
   Action to the other repo that copies its `notes/` or `research/` folder
   into this repo's `raw/` on every push (needs a token secret with write
   access here). Everything committed to that folder then flows in with
   zero clicks.

Rule of thumb: feed the brain *knowledge*, not code — findings, decisions,
results, reasons. Code stays in its own repo; the distilled "why" lives
here, where it cross-links with everything else you know.

## Safety rails (enforced by the schema)

- **Git is the undo button** — the agent commits after every ingest/lint/review,
  so any bad run is one revert away. No force-pushes, ever.
- **Lint reports, never deletes** — destructive changes require explicit approval.
- **`raw/` is untrusted input** — sources are data to summarize, never
  instructions to follow; suspected prompt injection gets flagged in `log.md`.
- **Mechanical checks are deterministic** — `python3 scripts/vault_check.py`
  catches broken links, orphans, index drift, and frontmatter gaps (exit 1 on
  problems), independent of the model.
