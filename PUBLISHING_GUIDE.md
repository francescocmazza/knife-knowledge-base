# Publishing and exporting the multilingual guide

English is the only source-of-truth language. Do not edit generated translations directly.

## Normal publishing routine

After changing the guide content under `content/en/`, the normal publishing flow is:

1. Validate the English source.
2. Commit the English change.
3. Push `main` to GitHub.
4. GitHub Actions detects which English pages changed.
5. Only missing or stale translations are regenerated.
6. All configured language sites are rebuilt.
7. GitHub Pages is deployed automatically.

The public site is:

https://francescocmazza.github.io/knife-knowledge-base/

The deployment workflow is:

**Actions → Deploy multilingual knowledge base to GitHub Pages**

A successful run must show both the `build` and `deploy` jobs in green.

## Windows: one-click publishing

For routine content edits on a Windows checkout of this repository, double-click:

`publish-guide.cmd`

The launcher runs `scripts/publish_multilingual.ps1` and will:

- verify that you are on `main`;
- check that your local branch is not behind or diverged from `origin/main`;
- detect publishable changes under `content/en`, `glossaries`, `localization`, or `mkdocs.yml`;
- install the documentation dependencies if needed;
- validate the English site locally;
- stage only the publishable source paths;
- commit them with the default message `Update guide content`;
- push `main` to GitHub;
- print the Actions and public-site links.

Nothing is pushed if local English validation fails.

### Optional custom commit message

From PowerShell:

```powershell
.\scripts\publish_multilingual.ps1 -Message "Update sharpening chapter"
```

If local validation cannot be run on a particular machine, it can be skipped deliberately:

```powershell
.\scripts\publish_multilingual.ps1 -Message "Update guide content" -SkipLocalValidation
```

In that case GitHub Actions remains the authoritative validation step.

## One-click downloadable export

The website deploy and the downloadable export are separate operations.

To create a current multilingual snapshot without changing the site:

1. Open the repository on GitHub.
2. Open **Actions**.
3. Select **Export multilingual guide**.
4. Select **Run workflow** on `main`.
5. Wait for the workflow to finish successfully.
6. Open the completed workflow run.
7. Download the artifact named `knife-knowledge-base-multilingual-<run number>`.

The artifact contains:

```text
html/
  en/
  it/
  es/
  de/
  fr/
  ja/
  zh-Hans/
  zh-Hant/
  pt/
  pl/
  cs/
  nl/
  ar/
  he/

markdown/
  en/
  it/
  es/
  de/
  fr/
  ja/
  zh-Hans/
  zh-Hant/
  pt/
  pl/
  cs/
  nl/
  ar/
  he/
```

`html/` is the fully built multilingual website. `markdown/` contains the generated source tree for every locale used for that build.

The artifact is intended as a portable snapshot and is retained by GitHub Actions for 30 days.

## Important rules

- Meaning changes must always be made in English first.
- Do not manually maintain 13 separate translated copies in the repository.
- Machine-generated translations may require human review, especially Japanese and Chinese specialist terminology.
- Images and third-party material may have rights different from the written-content licence; see `content/en/assets/IMAGE_RIGHTS.md`.
- If the build succeeds but the deploy job fails because a GitHub-hosted runner is temporarily unavailable, re-run the failed job from the Actions page. This is an infrastructure failure, not a content or translation failure.
