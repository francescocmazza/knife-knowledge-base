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

## One-click PDF export

This produces professionally formatted, printable PDF guides — one per language — instead of a website snapshot. It does not touch the live website in any way.

No command line is needed. Everything happens on the GitHub website:

1. Open GitHub.
2. Open the repository.
3. Click **Actions**.
4. Click **Export PDF guides**.
5. Click **Run workflow**.
6. Select **all** (one PDF per configured language) or a single language.
7. Select whether the editorial `IMAGE PLACEHOLDER` boxes should be **hide**-den or **show**n in the printed guide. Choose `hide` for a clean reader-facing guide, or `show` to also see which visuals are still awaiting production.
8. Click **Run workflow**.
9. Wait for the green check next to the run.
10. Open the completed run.
11. Download the artifact named `knife-knowledge-base-pdf-<run number>` under **Artifacts**.

The artifact contains one file per requested language, for example:

```text
Knife-Knowledge-Base-EN.pdf
Knife-Knowledge-Base-IT.pdf
Knife-Knowledge-Base-JA.pdf
Knife-Knowledge-Base-AR.pdf
```

Each PDF is a self-contained A4 guide with a cover page, a clickable table of contents, every chapter in the same order as the website navigation, and the same approved images and diagrams shown on the live site — captured after the page has fully rendered, not a screenshot of the raw source. Website navigation, search, the language selector and GitHub edit buttons are never included.

The PDF export reuses the same translation cache as the website and the multilingual export, so choosing a single language does not retranslate or rebuild the languages you did not select.

### Why the PDF is not generated directly from Markdown

Several diagrams, approved catalog images and their captions are inserted into the page by JavaScript after the website loads, not written directly into the Markdown source. Converting the Markdown files alone (for example with Pandoc) would silently miss those images. The export workflow instead renders every chapter in a real browser, waits for that script to finish, and only then captures the page — so the PDF always matches what a reader sees on the website.

## Important rules

- Meaning changes must always be made in English first.
- Do not manually maintain 13 separate translated copies in the repository.
- Machine-generated translations may require human review, especially Japanese and Chinese specialist terminology.
- Images and third-party material may have rights different from the written-content licence; see `content/en/assets/IMAGE_RIGHTS.md`.
- If the build succeeds but the deploy job fails because a GitHub-hosted runner is temporarily unavailable, re-run the failed job from the Actions page. This is an infrastructure failure, not a content or translation failure.
- The PDF export (**Actions → Export PDF guides**) only produces a downloadable artifact. It never modifies the repository, the website, or the GitHub Pages deployment.
