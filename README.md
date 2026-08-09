# Knife Knowledge Base

An open, practical knowledge base on kitchen knives—covering steels, blade geometry, construction, sharpening, maintenance, safety, and product education.

## Purpose

This project is designed for practical learning, commercial training, customer education, and marketing content. It is not intended to be an academic paper or a substitute for manufacturer-specific technical documentation.

The goal is to make knife knowledge easier to understand without turning useful simplifications into misleading claims.

## Website and active languages

The knowledge base is published as a searchable multilingual website with GitHub Pages.

The current active languages are:

- English (`en`) — source of truth
- Italian (`it`)
- Simplified Chinese (`zh-Hans`)

Other locale definitions remain in the repository for possible future use, but they are inactive and are not built, validated, automatically translated, exported, or published.

## English is the source of truth

All technical or factual changes must first be made in the English files under:

```text
content/en/
```

Active translations live under:

```text
translations/it/
translations/zh-Hans/
```

Each translated Markdown file contains a `source_hash`. The build compares that hash with the current English source. If English changes, the matching translation becomes stale.

The publishing workflow now refreshes stale active translations automatically before strict validation. It uses local Marian/OPUS-MT models inside GitHub Actions, so no translation API key or paid translation API is required.

The system reuses unchanged translated lines whenever possible and machine-translates only changed/inserted English lines. Simplified Chinese is explicitly targeted as `cmn_Hans`.

Automatic translation still requires human review for important technical wording, especially specialist Chinese terminology.

---

# Editing the knowledge base — normal workflow

For routine edits, the intended process is now:

```text
Edit English → create branch/PR → automatic IT + zh-Hans refresh → strict validation → merge → automatic commit/deploy
```

## 1. Find the English page

The master content is under:

```text
content/en/
```

Examples:

```text
content/en/index.md                         Home page
content/en/01-foundations/                 Foundations
content/en/02-steels-and-metallurgy/       Steels and metallurgy
content/en/03-blade-construction/           Blade construction
content/en/04-geometry-and-bevels/          Geometry and bevels
content/en/05-knife-types/                  Knife types
content/en/08-use-and-safety/               Use and safety
content/en/10-sharpening/                   Sharpening
content/en/assets/                          Images and other content assets
```

## 2. Edit directly on GitHub

For a simple text correction, no local software is required.

1. Open the repository on GitHub.
2. Click **Code**.
3. Open `content` → `en`.
4. Open the appropriate `.md` file.
5. Click the pencil icon: **Edit this file**.
6. Make the English change.
7. Use **Preview** when useful.
8. Click **Commit changes…**.
9. Choose **Create a new branch for this commit and start a pull request**.

For normal knowledge-base edits, do not put an unfinished English-only change directly on `main`.

## 3. You do not need to translate the edit manually

When the PR changes English content, **Deploy multilingual knowledge base to GitHub Pages** automatically:

1. detects stale/missing active translations;
2. loads the local English→Italian and English→Chinese translation models;
3. reuses unchanged translated lines;
4. translates changed/inserted lines;
5. updates the translation hash in the Actions workspace;
6. runs strict multilingual validation.

The PR is considered translation-complete when the validator reports:

```text
0 missing
0 stale
```

On a pull request, these generated translation changes stay in the temporary Actions workspace; the workflow does not push a bot commit onto the PR branch.

## 4. Merge when the checks are green

Once the English content is correct and the relevant checks are green, merge the PR into `main`.

On the resulting `main` push, the deployment workflow runs the same translation refresh again, then:

1. builds all active languages;
2. commits any refreshed files under `translations/` using `github-actions[bot]`;
3. uploads the Pages artifact;
4. deploys the multilingual website.

The bot uses the repository `GITHUB_TOKEN`, so its translation commit does not start an infinite second workflow loop.

## 5. What the translator protects

`scripts/auto_translate.py` is designed to preserve the structure and literals that should not be translated, including:

- Markdown headings and list markers;
- link destinations;
- inline code;
- URLs;
- HTML tags;
- inline math;
- fenced code blocks and commands;
- Markdown table structure;
- unchanged existing translation lines.

If a previous page cannot be safely aligned line-by-line, the helper falls back to translating the current page rather than silently treating an unknown old translation as current.

## 6. Human translation corrections are still allowed

A purely linguistic correction to Italian or Simplified Chinese may be made directly under `translations/<locale>/` when the English meaning is already correct.

Do not introduce a new technical or commercial claim only in a translation. If the meaning itself must change, edit English first.

## 7. Adding a new article

1. Create the English `.md` file under the appropriate `content/en/` section.
2. Follow the style of nearby articles.
3. Add the page to `mkdocs.yml` if it should appear in navigation.
4. Open a PR.
5. The automatic workflow generates the missing active translations in CI and validates them.
6. After merge, the `main` workflow commits those generated translation files and deploys them.

## 8. Renaming, moving, or deleting an article

Structural changes require more care because the source and translation trees must remain aligned.

For a rename or move:

1. rename/move the English file;
2. rename/move the corresponding Italian and Simplified Chinese files so existing reviewed wording is retained;
3. update `mkdocs.yml` and internal links;
4. let CI refresh content/hash differences;
5. merge only after strict validation passes.

For deletion, remove the corresponding active translation files and update navigation/internal links.

## 9. Images

Content images principally belong under:

```text
content/en/assets/
```

Only original, properly licensed, or explicitly authorized images may be added. See `content/en/assets/IMAGE_RIGHTS.md`.

## 10. Local validation

Strict multilingual validation remains:

```bash
python scripts/multilingual_site.py --require-translations
```

Automatic translation is:

```bash
python scripts/auto_translate.py
```

Local automatic translation requires `requirements-translation.txt` plus a CPU-compatible PyTorch installation. For routine browser-based edits, GitHub Actions is the easier route.

## 11. Generate PDFs

After the desired content is on `main`:

1. open **Actions**;
2. select **Export PDF guides**;
3. click **Run workflow**;
4. choose `all`, `en`, `it`, or `zh-Hans`;
5. choose whether editorial placeholders are hidden or shown;
6. run the workflow;
7. download the artifact from the workflow Summary page.

For `it`, `zh-Hans`, or `all`, the PDF workflow refreshes stale active translations automatically before export. English-only export skips the translation models.

## 12. Downloadable multilingual export

Use **Actions → Export multilingual guide → Run workflow**.

The workflow refreshes stale active translations before building and produces an artifact containing:

```text
html/      complete built website for every active locale
markdown/  per-locale source trees used for that build
```

## Automatic translation implementation

The active models are:

```text
Helsinki-NLP/opus-mt-en-it
Helsinki-NLP/opus-mt-en-zh
```

The dependency set is pinned in `requirements-translation.txt`, with Transformers kept below v5 because the Marian translation integration used here relies on the v4-compatible direct model/tokenizer path.

The workflow caches Hugging Face model files when possible. Translation happens on the GitHub-hosted runner; guide content is not sent to a paid translation API.

## Publishing architecture

The key components are:

```text
content/en/                         English source of truth
translations/                      Committed localized content
localization/locales.yml            Active/inactive locale configuration
scripts/auto_translate.py           Automatic stale-translation refresh
scripts/multilingual_site.py        Hash validation and multilingual site build
glossaries/master-terms.yml         Controlled terminology
.github/workflows/pages.yml         PR validation and GitHub Pages deployment
.github/workflows/export-pdf.yml    PDF export
.github/workflows/export-multilingual.yml  Downloadable multilingual export
```

See `PUBLISHING_GUIDE.md` for the detailed publishing behavior and operational notes.

## Current content scope

The current knowledge base covers:

- the five main dimensions used to explain knife steel;
- alloying elements;
- monosteel, clad, Damascus, and full Damascus construction;
- the self-sharpening effect in selected full Damascus blades;
- single- and double-bevel geometry;
- major knife types and cutting styles;
- safe use and carrying;
- water-stone preparation;
- burr formation, detection, and removal;
- a practical sharpening workflow.

## Contributing

Corrections, questions, and new-topic proposals are welcome through GitHub Issues and pull requests. Read `CONTRIBUTING.md` before submitting material.

## Images and third-party material

Several images are cropped or adapted from the Xinzuo product catalog and are used with authorization from the repository owner. They remain the property of their copyright holder, are not covered by the CC BY-NC-SA 4.0 license below, and require separate authorization for commercial reuse. See `content/en/assets/IMAGE_RIGHTS.md`.

## License

Except where otherwise noted, the original written content is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license.

Commercial use requires separate prior written permission from the copyright holder. See `LICENSE.md`.

© 2026 Francesco Claudio Mazza
