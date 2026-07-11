#!/usr/bin/env python3
"""Mechanical vault lint: broken wikilinks, orphan pages, index drift, frontmatter gaps.

Stdlib only. Exit 0 when clean, 1 when problems are found.
The semantic half of linting (contradictions, superseded claims, coverage gaps)
is the agent's job — see the LINT section of CLAUDE.md.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
INDEX = ROOT / "index.md"

# [[target]], [[target|alias]], [[target#heading]]
LINK_RE = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")
REQUIRED_FIELDS = ("title", "date", "type", "source")
VALID_TYPES = {"concept", "claim", "synthesis", "hub"}


def frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fields = {}
    for line in text[3:end].strip().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def main():
    problems = []
    pages = {p.stem: p for p in sorted(WIKI.glob("*.md"))}
    incoming = {name: 0 for name in pages}

    for name, path in pages.items():
        text = path.read_text(encoding="utf-8")

        fields = frontmatter(text)
        if fields is None:
            problems.append(f"frontmatter: wiki/{name}.md has no frontmatter block")
        else:
            missing = [f for f in REQUIRED_FIELDS if not fields.get(f)]
            if missing:
                problems.append(f"frontmatter: wiki/{name}.md missing {', '.join(missing)}")
            if fields.get("type") and fields["type"] not in VALID_TYPES:
                problems.append(
                    f"frontmatter: wiki/{name}.md type '{fields['type']}' not in {sorted(VALID_TYPES)}"
                )

        for target in LINK_RE.findall(text):
            target = target.strip()
            if target not in pages:
                problems.append(f"broken link: wiki/{name}.md -> [[{target}]]")
            elif target != name:
                incoming[target] += 1

    for name, count in sorted(incoming.items()):
        if count == 0:
            problems.append(f"orphan: wiki/{name}.md has no incoming links from other wiki pages")

    if INDEX.exists():
        indexed = {t.strip() for t in LINK_RE.findall(INDEX.read_text(encoding="utf-8"))}
        for name in pages:
            if name not in indexed:
                problems.append(f"index drift: wiki/{name}.md is not listed in index.md")
        for target in sorted(indexed - set(pages)):
            problems.append(f"index drift: index.md lists [[{target}]] but wiki/{target}.md does not exist")
    else:
        problems.append("index drift: index.md is missing")

    if problems:
        print(f"vault_check: {len(problems)} problem(s)")
        for p in problems:
            print(f"  - {p}")
        return 1

    links = sum(incoming.values())
    print(f"vault_check: OK — {len(pages)} pages, {links} internal links, index in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
