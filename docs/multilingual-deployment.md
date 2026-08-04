# Multilingual GitHub Pages deployment

The public website is generated from the English source under `content/en/`.

## Deployment flow

1. A pull request validates the English site only and does not call a translation model.
2. A merge or direct push to `main` restores the translation cache.
3. `scripts/multilingual_site.py` compares each English page with the cached source hash for every configured locale.
4. Missing or stale translations are generated through GitHub Models.
5. Unchanged translations are reused from the GitHub Actions cache.
6. MkDocs Material builds one complete site under `site/<locale>/`.
7. GitHub Pages publishes the combined artifact.

## Source-of-truth rule

English remains the only authoritative content. Generated translations are deployment outputs and do not independently define meaning.

Every translated page includes:

- its locale;
- the English source hash;
- a `machine-translated` status;
- a visible human-review notice.

If translation generation fails, the language route is still published with a clearly marked English fallback. A later deployment will retry because no valid translation is cached.

## Adding or removing a language

Edit `localization/locales.yml` and set:

```yaml
xx:
  name: Language name
  status: automatic
  direction: ltr
  deploy: true
  mkdocs_language: xx
```

Use `direction: rtl` for right-to-left languages. The `mkdocs_language` value controls the translated interface supplied by MkDocs Material.

## Human-reviewed translations

The `translations/` directory is reserved for future human-reviewed versions. A reviewed translation should preserve the English page path and identify the source revision. The build system can later be extended to prefer reviewed files over generated translations.
