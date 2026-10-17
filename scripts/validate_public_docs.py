#!/usr/bin/env python3
"""Fail-closed validation of publicly publishable OOC documentation only.

Do not turn this into a recursive copy from the private source repository.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
EXPECTED = {
    "index.md",
    "getting-started/index.md",
    "tutorials/first-run.md",
    "methods/index.md",
    "examples/index.md",
    "validation/index.md",
    "licensing/index.md",
    "reference/USAGE.md",
    "reference/METHODS.md",
}
BLOCKED_EXTENSIONS = {".nb", ".wl", ".7z", ".tif", ".tiff", ".csv", ".pdf", ".edoc"}
BLOCKED_PATHS = (r"D:\\\\BIG DATA", r"/mnt/data/", r"/home/oai/")


def main() -> None:
    actual = {p.relative_to(DOCS).as_posix() for p in DOCS.rglob("*") if p.is_file()}
    if actual != EXPECTED:
        raise SystemExit(f"Unexpected/missing public documentation files: {sorted(actual ^ EXPECTED)}")
    for name in actual:
        p = DOCS / name
        if p.suffix.lower() in BLOCKED_EXTENSIONS:
            raise SystemExit(f"Disallowed public artifact: {name}")
        data = p.read_text(encoding="utf-8")
        for private_fragment in BLOCKED_PATHS:
            if private_fragment in data:
                raise SystemExit(f"Unreviewed internal path in public page: {name}")
        if re.search(r"(?i)(?:password|api[_-]?key|secret)[ \t]*[:=][ \t]*[\w-]{8,}", data):
            raise SystemExit(f"Possible credentials in public page: {name}")
    print(f"Public documentation allowlist verified: {len(actual)} Markdown pages")


if __name__ == "__main__":
    main()
