param(
    [string]$Message = "Update guide content",
    [switch]$SkipLocalValidation
)

$ErrorActionPreference = "Stop"

function Stop-WithMessage([string]$Text) {
    Write-Host ""
    Write-Host "ERROR: $Text" -ForegroundColor Red
    exit 1
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Stop-WithMessage "Git is not available in PATH."
}

try {
    $repoRoot = (git rev-parse --show-toplevel 2>$null).Trim()
} catch {
    Stop-WithMessage "Run this script from inside the knife-knowledge-base repository."
}

if (-not $repoRoot) {
    Stop-WithMessage "Run this script from inside the knife-knowledge-base repository."
}

Set-Location $repoRoot

$branch = (git branch --show-current).Trim()
if ($branch -ne "main") {
    Stop-WithMessage "Current branch is '$branch'. Switch to main before using the one-click publishing routine."
}

Write-Host "Checking the remote main branch..."
git fetch origin main

$localHead = (git rev-parse HEAD).Trim()
$remoteHead = (git rev-parse origin/main).Trim()
$mergeBase = (git merge-base HEAD origin/main).Trim()

if ($localHead -ne $remoteHead) {
    if ($mergeBase -eq $localHead) {
        Stop-WithMessage "Your local main is behind origin/main. Run 'git pull --ff-only' first, then re-apply or save your edits if necessary."
    }
    if ($mergeBase -ne $remoteHead) {
        Stop-WithMessage "Local main and origin/main have diverged. Resolve the Git history before publishing."
    }
}

$trackedChanges = git status --porcelain -- content/en glossaries localization mkdocs.yml
if (-not $trackedChanges) {
    Stop-WithMessage "No publishable source changes were found under content/en, glossaries, localization or mkdocs.yml."
}

if (-not $SkipLocalValidation) {
    if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
        Stop-WithMessage "Python is not available in PATH. Install Python or run again with -SkipLocalValidation and rely on GitHub Actions validation."
    }

    Write-Host "Checking documentation dependencies..."
    python -c "import mkdocs, yaml" 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Installing documentation dependencies..."
        python -m pip install -r requirements-docs.txt
        if ($LASTEXITCODE -ne 0) {
            Stop-WithMessage "Could not install documentation dependencies."
        }
    }

    Write-Host "Validating the English source locally..."
    python scripts/multilingual_site.py --locales en
    if ($LASTEXITCODE -ne 0) {
        Stop-WithMessage "English validation failed. Nothing was committed or pushed."
    }
}

Write-Host "Staging source changes..."
git add -- content/en glossaries localization mkdocs.yml

$staged = git diff --cached --name-only
if (-not $staged) {
    Stop-WithMessage "Nothing was staged."
}

Write-Host "Files that will be published:"
$staged | ForEach-Object { Write-Host "  $_" }

Write-Host "Committing changes..."
git commit -m $Message
if ($LASTEXITCODE -ne 0) {
    Stop-WithMessage "Git commit failed."
}

Write-Host "Pushing main to GitHub..."
git push origin main
if ($LASTEXITCODE -ne 0) {
    Stop-WithMessage "Git push failed. Your commit remains local and can be pushed later."
}

Write-Host ""
Write-Host "Published source successfully." -ForegroundColor Green
Write-Host "GitHub Actions will now translate stale pages, rebuild every configured language and deploy GitHub Pages."
Write-Host "Actions: https://github.com/francescocmazza/knife-knowledge-base/actions"
Write-Host "Site:    https://francescocmazza.github.io/knife-knowledge-base/"
Write-Host ""
Write-Host "For a downloadable multilingual snapshot, run the 'Export multilingual guide' workflow from the Actions tab."
