# Translations

English under `content/en/` is the sole source of truth.

The GitHub Pages workflow automatically generates localized website versions during deployment. Generated translations are stored in the GitHub Actions cache rather than committed as authoritative source files. This keeps the repository English-first while avoiding repeated translation of unchanged pages.

## Current automatic deployment locales

- Italian (`it`)
- Spanish (`es`)
- German (`de`)
- French (`fr`)
- Japanese (`ja`)
- Simplified Chinese (`zh-Hans`)
- Traditional Chinese (`zh-Hant`)
- Portuguese (`pt`)
- Polish (`pl`)
- Czech (`cs`)
- Dutch (`nl`)
- Arabic (`ar`)
- Hebrew (`he`)

## Rules

- Meaning changes must first be approved in English.
- Automatic translations must not introduce new technical or commercial claims.
- Every generated page records the English source hash and displays a machine-translation notice.
- When the English source changes, only stale pages are translated again.
- Japanese, Simplified Chinese, and Traditional Chinese require terminology review by a competent speaker familiar with kitchen knives.
- Human-reviewed translations may later be stored in this directory and used as overrides instead of machine-generated versions.

The deployment configuration is defined in `localization/locales.yml`, and the builder is located at `scripts/multilingual_site.py`.
