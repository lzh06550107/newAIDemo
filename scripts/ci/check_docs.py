#!/usr/bin/env python3
"""Validate the documentation-only project baseline, without external dependencies."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

REQUIRED_DOCUMENTS = (
    "AGENTS.md",
    "README.md",
    "docs/ai/PROJECT.md",
    "docs/ai/STATE.md",
    "docs/ai/DECISIONS.md",
    "docs/ai/ACCEPTANCE.md",
    "docs/ai/TESTING.md",
)
REQUIRED_INFRASTRUCTURE = (
    "scripts/ci/verify.sh",
    "scripts/ci/check_docs.py",
    "scripts/ci/tests/test_check_docs.py",
    ".github/workflows/ci.yml",
)
STATE_SECTIONS = (
    "Current branch",
    "Current commit",
    "Current task",
    "Completed",
    "Pending",
    "Known issues",
    "CI status",
    "Deployment status",
    "Runtime verification",
    "Next step",
)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def validate(root: Path) -> list[str]:
    """Return actionable validation errors for the given checkout root."""
    root = root.resolve()
    errors: list[str] = []
    contents: dict[str, str] = {}
    for relative in (*REQUIRED_DOCUMENTS, *REQUIRED_INFRASTRUCTURE):
        path = root / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")
            continue
        try:
            value = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError) as exc:
            errors.append(f"unable to read UTF-8 file {relative}: {exc}")
            continue
        if not value.strip():
            errors.append(f"empty required file: {relative}")
            continue
        contents[relative] = value
        if relative.endswith(".md") and not re.search(r"^#\s+\S", value, re.MULTILINE):
            errors.append(f"Markdown H1 title missing: {relative}")

    for relative in REQUIRED_DOCUMENTS:
        if relative not in contents:
            continue
        path = root / relative
        for match in MARKDOWN_LINK.finditer(contents[relative]):
            raw_url = match.group(1).strip().split(None, 1)[0].strip("<>")
            if raw_url.startswith("#"):
                continue
            parsed = urlsplit(raw_url)
            if parsed.scheme or parsed.netloc:
                continue
            if not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(root):
                errors.append(f"link escapes repository: {relative}: {raw_url}")
            elif not destination.is_file():
                errors.append(f"broken relative link: {relative}: {raw_url}")

    state = contents.get("docs/ai/STATE.md", "")
    for section in STATE_SECTIONS:
        if not re.search(rf"^##\s+{re.escape(section)}(?:\s|$)", state, re.IGNORECASE | re.MULTILINE):
            errors.append(f"STATE.md section missing: {section}")

    testing = contents.get("docs/ai/TESTING.md", "")
    if testing and "scripts/ci/verify.sh" not in testing:
        errors.append("TESTING.md must document scripts/ci/verify.sh")

    workflow = contents.get(".github/workflows/ci.yml", "")
    if workflow and "bash scripts/ci/verify.sh" not in workflow:
        errors.append("ci.yml must invoke the shared verification entry point")

    readme = contents.get("README.md", "")
    if readme and "docs/ai/STATE.md" not in readme:
        errors.append("README.md must reference docs/ai/STATE.md")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    root = parser.parse_args().root
    errors = validate(root)
    if errors:
        for message in errors:
            print(f"ERROR: {message}")
        print(f"Documentation baseline: FAILED ({len(errors)} issue(s))")
        return 1
    print("Documentation baseline: PASS (required files, sections, and relative links)")
    print("Scope: documentation/infrastructure ONLY; not application build or runtime verification")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
