"""Regression checks that reject broken or missing documentation."""

from __future__ import annotations

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "check_docs", PROJECT_ROOT / "scripts/ci/check_docs.py"
)
assert SPEC is not None and SPEC.loader is not None
check_docs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_docs)


class DocumentationValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for relative in (*check_docs.REQUIRED_DOCUMENTS, *check_docs.REQUIRED_INFRASTRUCTURE):
            source = PROJECT_ROOT / relative
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)

    def test_valid_checkout(self) -> None:
        self.assertEqual(check_docs.validate(self.root), [])

    def test_missing_document_is_rejected(self) -> None:
        (self.root / "docs/ai/PROJECT.md").unlink()
        errors = check_docs.validate(self.root)
        self.assertTrue(any("missing required file: docs/ai/PROJECT.md" in x for x in errors))

    def test_broken_relative_link_is_rejected(self) -> None:
        readme = self.root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "\n[bad](docs/missing.md)\n", encoding="utf-8")
        errors = check_docs.validate(self.root)
        self.assertTrue(any("broken relative link" in x for x in errors))

    def test_missing_state_section_is_rejected(self) -> None:
        state = self.root / "docs/ai/STATE.md"
        value = state.read_text(encoding="utf-8")
        state.write_text(value.replace("## Current task", "## Unnamed task"), encoding="utf-8")
        errors = check_docs.validate(self.root)
        self.assertTrue(any("STATE.md section missing: Current task" in x for x in errors))

    def test_missing_ci_entry_point_is_rejected(self) -> None:
        ci = self.root / ".github/workflows/ci.yml"
        ci.write_text("name: no verification\n", encoding="utf-8")
        errors = check_docs.validate(self.root)
        self.assertTrue(any("ci.yml must invoke" in x for x in errors))


if __name__ == "__main__":
    unittest.main()
