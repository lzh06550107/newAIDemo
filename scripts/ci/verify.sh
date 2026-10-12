#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

bash -n scripts/ci/verify.sh
python3 -B -m unittest discover -s scripts/ci/tests -p 'test_*.py' -v
python3 -B scripts/ci/check_docs.py --root "$ROOT"

printf '%s\n' 'Verification complete: docs-only baseline; application testing is not configured.'
