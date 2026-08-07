#!/usr/bin/env python3
"""Shared publication metadata: version, date and commit SHA.

Both the website build (``multilingual_site.py``) and the PDF export
(``export_pdf_guides.py``) call this module so the two publication
channels always agree on the version number and never compute it
independently.

The version is the number of commits reachable from the checked-out
commit (``git rev-list --count HEAD``). It is purely derived from
existing repository history:

- it never requires a manual edit or a dedicated "bump version" commit;
- the same commit always produces the same version number, on the
  website and in a PDF export alike;
- re-running an export against an unchanged commit keeps the same
  version number and only the export date changes.

Getting an accurate count in CI requires a full checkout (GitHub's
``actions/checkout`` defaults to a shallow, single-commit clone, which
would make every build report version 1); the workflows that use this
module set ``fetch-depth: 0`` accordingly.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
PUBLICATION_TIMEZONE = ZoneInfo("Europe/Rome")


@dataclass(frozen=True)
class PublicationMetadata:
    version: int
    commit_sha: str
    commit_sha_short: str
    publication_date: str  # ISO YYYY-MM-DD, Europe/Rome calendar date

    @property
    def version_label(self) -> str:
        return f"v{self.version}"

    @property
    def compact_footer(self) -> str:
        """Language-neutral form suitable for every locale without translation."""
        return f"{self.version_label} · {self.publication_date}"

    @property
    def full_label(self) -> str:
        return f"Version {self.version} · commit {self.commit_sha_short}"


def _run_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def get_version() -> int:
    return int(_run_git(["rev-list", "--count", "HEAD"]))


def get_commit_sha() -> tuple[str, str]:
    full = _run_git(["rev-parse", "HEAD"])
    short = _run_git(["rev-parse", "--short", "HEAD"])
    return full, short


def get_publication_date() -> str:
    return datetime.now(PUBLICATION_TIMEZONE).strftime("%Y-%m-%d")


def get_metadata() -> PublicationMetadata:
    full_sha, short_sha = get_commit_sha()
    return PublicationMetadata(
        version=get_version(),
        commit_sha=full_sha,
        commit_sha_short=short_sha,
        publication_date=get_publication_date(),
    )


def main() -> int:
    """CLI entry point: print metadata as JSON for shell/CI consumption."""
    import json

    meta = get_metadata()
    print(
        json.dumps(
            {
                "version": meta.version,
                "version_label": meta.version_label,
                "commit_sha": meta.commit_sha,
                "commit_sha_short": meta.commit_sha_short,
                "publication_date": meta.publication_date,
                "compact_footer": meta.compact_footer,
                "full_label": meta.full_label,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
