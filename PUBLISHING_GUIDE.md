# Publishing and exporting the multilingual guide

English under `content/en/` is the only source of truth. Translations are committed under `translations/<locale>/` and are refreshed during editing, not by GitHub Actions.

## Normal publishing routine

After changing the English guide:

1. Edit and approve the English source.
2. Ask Claude Code to check the translation status and refresh only missing/stale translated pages.
3. Commit the English change and the corresponding translation updates together.
4. GitHub Actions validates that every required translation matches the current English source hash.
5. All configured language sites are rebuilt from committed files.
6. GitHub Pages is deployed automatically.

There is **no paid translation API in the publishing pipeline**. GitHub Actions never sends guide content to OpenAI, GitHub Models or another translation service.

The public site is:

https://francescocmazza.github.io/knife-knowledge-base/

The deployment workflow is:

**Actions → Deploy multilingual knowledge base to GitHub Pages**

A successful production run must show both `build` and `deploy` in green.

## Translation files and stale-page protection

Each locale mirrors the Markdown tree under `content/en/`, for example:

```text
content/en/10-sharpening/the-burr.md
translations/it/10-sharpening/the-burr.md
translations/ja/10-sharpening/the-burr.md
```

Every translated Markdown file contains a `source_hash` in YAML front matter. `scripts/multilingual_site.py` recalculates the expected hash from the current English page, locale, glossary and translation schema. If the committed file is missing or its hash is outdated, it is reported as missing/stale.

Production publishing and multilingual exports use:

```text
python scripts/multilingual_site.py --require-translations
```

This means a stale translation blocks publication instead of silently showing English text under another language.

For local development, strict mode can be omitted; missing/stale translations then fall back to English only for that local build and display a warning.

## Updating translations with Claude Code

Claude Code should be used before publishing whenever English content has changed. It should:

- run/check the multilingual builder to identify missing/stale locale/page pairs;
- translate only those pages from the current English source;
- preserve Markdown, links, image paths, HTML, formulas, steel grades, product names and HRC values;
- avoid adding, correcting or reconciling claims that are not in English;
- write the translated files under `translations/<locale>/`;
- write the exact current `source_hash` required by the builder;
- run `python scripts/multilingual_site.py --require-translations` until it passes.

English remains authoritative. A translation may improve wording in its own language but must not change technical meaning.

## Windows: one-click publishing

For routine publishing from a Windows checkout, double-click:

`publish-guide.cmd`

The launcher runs `scripts/publish_multilingual.ps1` and will:

- verify that you are on `main`;
- check that local `main` is not behind/diverged from `origin/main`;
- detect publishable changes under `content/en`, `translations`, `glossaries`, `localization`, or `mkdocs.yml`;
- install documentation dependencies if needed;
- validate English plus all committed translations locally;
- refuse to publish if any translation is missing/stale;
- stage English and translations together;
- commit and push `main`;
- print the Actions and public-site links.

Optional custom commit message:

```powershell
.\scripts\publish_multilingual.ps1 -Message "Update sharpening chapter"
```

Local validation can deliberately be skipped with `-SkipLocalValidation`, but GitHub Actions will still reject a production deployment if translations are incomplete.

## One-click downloadable multilingual export

Go to **Actions → Export multilingual guide → Run workflow** on `main`.

The artifact `knife-knowledge-base-multilingual-<run number>` contains:

```text
html/      complete built website for every configured locale
markdown/  per-locale source trees used for that build
```

The export reads committed translations only and makes no paid API calls.

## One-click PDF export

Go to **Actions → Export PDF guides → Run workflow**. Choose `all` or a single language and choose whether editorial placeholders should be hidden or shown.

Translated PDF exports first validate the committed translation set. If anything is missing/stale, the export stops and tells you to refresh translations before trying again.

The artifact is named `knife-knowledge-base-pdf-<run number>` and contains files such as:

```text
Knife-Knowledge-Base-EN-v42.pdf
Knife-Knowledge-Base-IT-v42.pdf
Knife-Knowledge-Base-JA-v42.pdf
Knife-Knowledge-Base-AR-v42.pdf
```

Each PDF is A4, has a cover and clickable contents, uses the same rendered images/diagrams as the website, and contains no website navigation UI.

## Automatic version numbers and publication dates

Every published website page and PDF reports a progressive version and publication/export date, e.g. `v42 · 2026-08-07`.

- The version is the repository commit count at the built commit (`git rev-list --count HEAD`).
- The date is the actual build/export date in `Europe/Rome`, formatted `YYYY-MM-DD`.
- Re-exporting the same commit later keeps the version but updates the export date.
- A PDF built from the same commit as the live website has the same version number.

The shared implementation is `scripts/publication_metadata.py`.

## Important rules

- Meaning changes must always be made in English first.
- Do not publish an English change without refreshing the affected committed translations.
- Machine-assisted translations may require human review, especially Japanese, Chinese, Arabic and specialist knife terminology.
- Images and third-party material may have rights different from the written-content licence; see `content/en/assets/IMAGE_RIGHTS.md`.
- PDF export only creates a downloadable artifact; it never modifies the repository or the live site.
