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

## 3b. Normal Claude chat (claude.ai / mobile app)

Chat conversations don't auto-stream anywhere — and shouldn't (the brain
wants distilled knowledge, not every conversation). Two doors:

**Zero setup, always works:** at the end of a useful chat, say
*"Summarize the durable knowledge from this conversation as a short
markdown note I can file."* Copy the result → GitHub → this repo →
`raw/` → Add file → paste → Commit (phone works fine). Auto-ingest does
the rest. ~30 seconds.

**One-time setup, then one phrase per chat:**

1. claude.ai → Settings → Connectors → add the **GitHub** connector and
   authorize your GitHub account with access to this repo. (On a
   company-managed Claude account this may be admin-controlled — if the
   connector isn't available, use the zero-setup door above.)
2. Add to your claude.ai personal preferences / profile instructions:
   *"I maintain a knowledge vault at github.com/vaishshukla420-pixel/Sec-brain.
   When I say 'file this to my brain', distill this conversation's
   durable knowledge into a markdown note and commit it via the GitHub
   connector to the vault's `raw/` folder as `YYYY-MM-DD-<topic>.md`.
   Never edit other folders."*
3. Then in ANY chat: **"file this to my brain"** → the note lands in
   `raw/` → the pipeline ingests it like anything else.

**Reading the brain from chat:** with the connector, ask *"check my
Sec-brain — read index.md and the relevant wiki pages — what do I know
about X?"*. Even smoother: create a claude.ai **Project** called
"Sec-brain" and sync this repo's `index.md` + `wiki/` into its project
knowledge — every chat inside that Project answers from your brain
automatically (re-sync after big ingests).

Note: claude.ai's built-in "memory" is a separate, app-internal
convenience — the vault is the durable, portable brain you own in git.

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

### Moving the WHOLE vault to another account (content included)

> **Self-setup shortcut:** you only need steps 0-1 by hand. After
> cloning, open Claude Code in the folder and say **"this is my copy
> now, set it up"** — the agent reads `BOOTSTRAP.md` and performs the
> rest itself (merge, repointing, laptop hooks, automation, verify),
> asking before each step that touches anything outside the repo.

The vault is plain files in git — nothing is tied to any GitHub or
Claude account. Full move, ~10 minutes:

1. **Copy the repo.** On the new owner's laptop:
   ```bash
   git clone https://github.com/vaishshukla420-pixel/Sec-brain.git ~/Sec-brain
   cd ~/Sec-brain
   ```
   Create a fresh repo in the new GitHub account (github.com/new —
   **private recommended** for a personal brain; do NOT initialize it
   with a README), then repoint and push everything:
   ```bash
   git remote set-url origin https://github.com/<NEW-USER>/Sec-brain.git
   git push -u origin --all
   ```
   (Alternative: the old owner clicks Settings → Transfer ownership —
   one click, moves history and Actions, but not secrets.)
2. **Consolidate to main.** If the content lives on a working branch:
   ```bash
   git checkout main
   git merge claude/implementability-review-99t3an   # fast-forwards
   git push -u origin main
   ```
3. **Make it yours.** Replace the old account name in the docs:
   ```bash
   sed -i 's|vaishshukla420-pixel|<NEW-USER>|g' README.md SETUP.md
   git commit -am "docs: repoint vault references" && git push
   ```
   (Or open Claude Code in the folder and just ask it to do this.)
4. **Re-arm automation — three options, by budget:**
   - **No cloud, zero extra cost (fine!):** skip all secrets and disable
     the two workflows (repo → Actions → each workflow → "···" →
     Disable) so pushes to `raw/` don't show failed runs. Files dropped
     in `raw/` simply wait; the next interactive session notices them
     (the schema ingests whenever `raw/` has files), or a local cron
     running `scripts/ingest.sh` sweeps hourly on your subscription
     while the laptop is on.
   - **Cloud on your subscription (no API billing):** run
     `claude setup-token` locally, save the output as a
     `CLAUDE_CODE_OAUTH_TOKEN` repository secret, and swap the
     credential line in both workflow files as commented there. Runs
     count against your plan limits.
   - **Cloud on API billing:** add `ANTHROPIC_API_KEY`
     (console.anthropic.com) as the secret — pay per run.
   Whichever you choose, check Settings → Actions is enabled/disabled
   to match.
5. **Verify.** `python3 scripts/vault_check.py` (expect: OK), open
   `claude` in the folder and ask it something, and if the key was
   added: upload a test file to `raw/` via GitHub web and watch the
   `brain-ingest` Action process it.

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
