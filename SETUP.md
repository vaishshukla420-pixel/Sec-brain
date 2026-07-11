# Sec-Brain Setup — every device, every repo, every person

The mental model: **one brain, many doors.** The vault (this repo) is the
single source of truth. Knowledge flows IN through one door — the `raw/`
inbox — and flows OUT through search (`index.md` + `wiki/`). Everything
below just installs doors in more places.

```
 you / Claude, anywhere            THE VAULT (this repo)
 ────────────────────────          ──────────────────────────────
  work, research, talk   ──note──▶  raw/   ──auto-ingest──▶ wiki/
  "what do I know…?"     ◀─cited answer── index.md + wiki/ ◀─┘
```

Writing a note into `raw/` and pushing is ALL a feeder ever does — the
`brain-ingest` GitHub Action (see README → Automation) atomizes, links,
indexes, logs, and commits. Readers only ever search and cite. Nobody
edits `wiki/` by hand from outside.

---

## 1. Your laptop (Claude Code CLI)

One-time, ~5 minutes:

```bash
npm install -g @anthropic-ai/claude-code   # install
claude login                                # sign in with your account
git clone https://github.com/vaishshukla420-pixel/Sec-brain.git ~/Sec-brain
```

Work **inside** the brain (full ingest/query/lint powers):

```bash
cd ~/Sec-brain && claude
# then: "ingest this", any question, "lint the wiki", "weekly review"
```

Make the brain available in **every** local session, whatever folder
you're in — two pastes:

**a) `~/.claude/CLAUDE.md`** (user memory — loads in all local sessions):

```markdown
## Personal knowledge vault (Sec-brain)

I keep a compiled knowledge vault at `~/Sec-brain` (git repo
vaishshukla420-pixel/Sec-brain; its own CLAUDE.md defines the rules).

- QUERY: when I ask "what do I know about X", want background, or the
  task would benefit from my accumulated knowledge: read
  ~/Sec-brain/index.md, grep ~/Sec-brain/wiki/, read the matching pages,
  and cite them as [[page-name]].
- FEED: when a session produces durable knowledge (research findings,
  decisions, lessons — never code, never secrets), write a short
  markdown note to ~/Sec-brain/raw/YYYY-MM-DD-<topic>.md, then:
  git -C ~/Sec-brain pull --rebase && git -C ~/Sec-brain add raw/ &&
  git -C ~/Sec-brain commit -m "raw: <topic> (from <project>)" &&
  git -C ~/Sec-brain push
  The vault's own pipeline ingests it from there.
- Never edit ~/Sec-brain/wiki/ from outside the vault — raw/ only.
```

**b) `~/.claude/settings.json`** (lets every session touch the vault
folder without permission friction):

```json
{
  "permissions": {
    "additionalDirectories": ["~/Sec-brain"]
  }
}
```

Optional extras: open `~/Sec-brain` in Obsidian for the graph view;
add a cron line for `scripts/ingest.sh` if you want local ingestion too
(the cloud Action already covers it).

---

## 2. Any other repo — the universal brain hook

New project (trading bot, OTC research, anything)? Paste this into that
repo's `CLAUDE.md`. It works in local sessions AND claude.ai web
sessions on that repo:

```markdown
## Sec-brain hook

This project feeds and uses a personal knowledge vault:
github.com/vaishshukla420-pixel/Sec-brain.

- USE: for background or "what do I know about…", consult the vault —
  locally it's at ~/Sec-brain; in a web session, add the repo
  vaishshukla420-pixel/Sec-brain. Read its index.md, grep wiki/, cite
  pages.
- FEED: before ending any session that produced durable knowledge
  (findings, decisions, lessons — not code, not client-confidential
  material), distill it into a short markdown note and commit it to the
  vault's raw/ inbox (locally: write + push in ~/Sec-brain; web: via the
  added repo). The vault ingests it automatically.
```

That's the whole integration. After the paste, feeding the brain is a
side effect of normal work in that repo.

**Fully hands-off variant:** keep a `research/` folder in the project
repo and add a GitHub Action that copies new files from it into this
repo's `raw/` on every push (needs a fine-grained PAT with write access
to Sec-brain stored as a secret in the project repo). Ask the brain to
"wire the auto-ship action for repo X" and it will generate it.

---

## 3. Phone / web, no repo at all

- **Feed:** open this repo on github.com → `raw/` → Add file → paste or
  upload → Commit. Ingestion fires automatically.
- **Fetch:** start a claude.ai code session on this repo (or add it to
  any session: "add repo vaishshukla420-pixel/Sec-brain") and just ask.

---

## 4. Sharing the brain with a teammate/friend

Two models — pick one:

**Shared brain (you both feed and use the SAME vault):**

1. Owner, one time: GitHub → this repo → Settings → Collaborators →
   invite their GitHub account (they accept the email invite).
2. Friend, one time, on their machine:
   - VS Code: install the "Claude Code" extension and sign in with
     THEIR Claude account (their usage bills to them) — or install the
     CLI as in §1.
   - `git clone https://github.com/vaishshukla420-pixel/Sec-brain.git`
     (their GitHub login; the repo is private).
   - Open the folder → start Claude Code → `CLAUDE.md` loads
     automatically → "ingest this", questions, "lint the wiki" all work
     identically. Optionally they add the §1 user-memory snippet too.
3. How it stays conflict-free: contributors only ADD files to `raw/`
   (append-only by convention) and let the pipeline integrate; the
   auto-ingest Action runs on the repo's `ANTHROPIC_API_KEY` secret
   regardless of who pushed (that key's owner pays for ingestion runs);
   `log.md` + git history record who added what.

**Their own brain (they want a copy, not a share):** GitHub → Use this
template / fork → they empty `wiki/`, `index.md` groups, and `log.md`
(or keep the content as a starter), add their own `ANTHROPIC_API_KEY`
secret, and follow §1. Same machine setup either way.

---

## 5. Confidential work — read once

A personal vault on a personal GitHub account is the wrong home for
client-confidential or company-proprietary material (deal terms, client
names, internal strategy). Feed the brain the *transferable knowledge*
— concepts, public research, general lessons — and keep confidential
specifics in the company's own systems. If you want a brain for company
work, create a second vault repo inside the company's GitHub org (same
files, same schema — this repo is the template) so data governance
follows the employer's rules. The schema's untrusted-input and
report-don't-delete rules apply to both.
