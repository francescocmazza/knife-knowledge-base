# Translations

English under `content/en/` is the sole source of truth.

The GitHub Pages workflow automatically generates localized website versions during deployment. Generated translations are stored in the GitHub Actions cache rather than committed as authoritative source files. This keeps the repository English-first while avoiding repeated translation of unchanged pages.

## Translation provider

GitHub Models was fully retired by GitHub on July 30, 2026, so the multilingual builder now uses the OpenAI API for machine translation.

Repository setup requires an Actions secret named `OPENAI_API_KEY`. The default translation model is `gpt-5-mini`; it can be changed through the `OPENAI_MODEL` environment variable without changing the English source.

Production deployments use strict translation mode: if a required non-English translation cannot be generated and is not already present in the translation cache, the build fails instead of silently replacing that page with English. This protects the live multilingual site from provider outages or missing credentials.

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
