#!/usr/bin/env python3
"""Translate the English Markdown core and build one MkDocs site per locale."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from publication_metadata import PublicationMetadata, get_metadata  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "content" / "en"
LOCALES = ROOT / "localization" / "locales.yml"
GLOSSARY = ROOT / "glossaries" / "master-terms.yml"
BASE_CONFIG = ROOT / "mkdocs.yml"
CACHE = ROOT / ".translation-cache"
WORK = ROOT / ".site-work"
SITE = ROOT / "site"
BASE_URL = "https://francescocmazza.github.io/knife-knowledge-base"
MODEL_ENDPOINT = "https://models.github.ai/inference/chat/completions"
PROMPT_VERSION = "2026-08-04-v1"
DEFAULT_MODEL = "openai/gpt-4o"


def args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--translate", action="store_true")
    parser.add_argument("--locales", nargs="*")
    parser.add_argument("--model", default=os.getenv("GITHUB_MODELS_MODEL", DEFAULT_MODEL))
    return parser.parse_args()


def read_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def split_document(text: str) -> tuple[dict[str, Any], str]:
    if text.startswith("---\n") and "\n---\n" in text:
        raw, body = text.split("\n---\n", 1)
        return yaml.safe_load(raw[4:]) or {}, body
    return {}, text


def join_document(metadata: dict[str, Any], body: str) -> str:
    front = yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{front}\n---\n\n{body.lstrip()}"


def digest(locale: str, source: str, glossary: str) -> str:
    raw = "\0".join((PROMPT_VERSION, locale, source, glossary)).encode()
    return hashlib.sha256(raw).hexdigest()


def cache_files(locale: str, relative: Path) -> tuple[Path, Path]:
    page = CACHE / locale / relative
    return page, page.with_suffix(page.suffix + ".sha256")


def get_cached(locale: str, relative: Path, expected: str) -> str | None:
    page, marker = cache_files(locale, relative)
    if page.exists() and marker.exists() and marker.read_text().strip() == expected:
        return page.read_text(encoding="utf-8")
    return None


def set_cached(locale: str, relative: Path, expected: str, body: str) -> None:
    page, marker = cache_files(locale, relative)
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(body, encoding="utf-8")
    marker.write_text(expected + "\n", encoding="utf-8")


def call_model(body: str, code: str, name: str, glossary: str, token: str, model: str) -> str:
    prompt = f"""Translate this public kitchen-knife knowledge-base page from English to {name} ({code}).
Return only translated Markdown, with no YAML front matter and no outer code fence.
Preserve all Markdown structure, relative link destinations, URLs, image paths, HTML, code, formulas, steel grades, product names and HRC values.
Translate visible link text and headings. Keep customary knife names such as Gyuto, Santoku, Bunka, Nakiri, Usuba, Deba, Honesuki, Sujihiki and Yanagiba recognizable.
Do not add, remove, correct or reconcile claims. Keep the clear, detailed, non-specialist commercial-training tone.

Project glossary:
{glossary[:12000]}

Source Markdown:
{body}
"""
    payload = {
        "model": model,
        "temperature": 0.1,
        "max_tokens": 16000,
        "messages": [
            {"role": "system", "content": "You are a faithful technical translator. English is the authoritative source."},
            {"role": "user", "content": prompt},
        ],
    }
    request = urllib.request.Request(
        MODEL_ENDPOINT,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2026-03-10",
        },
        method="POST",
    )
    last: Exception | None = None
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                data = json.loads(response.read().decode("utf-8"))
            result = data["choices"][0]["message"]["content"].strip()
            if result.startswith("```") and result.endswith("```"):
                result = re.sub(r"^```(?:markdown)?\s*", "", result)
                result = re.sub(r"\s*```$", "", result)
            if not result:
                raise RuntimeError("empty model response")
            return result.rstrip() + "\n"
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError, RuntimeError) as exc:
            last = exc
            status = getattr(exc, "code", None)
            if status not in (429, 500, 502, 503, 504):
                break
            time.sleep(min(60, 3 * (2**attempt)))
    raise RuntimeError(f"translation failed for {code}: {last}")


def title_from(body: str, fallback: str | None = None) -> str | None:
    found = re.search(r"^#\s+(.+?)\s*$", body, re.MULTILINE)
    return found.group(1).strip() if found else fallback


def prepare_docs(code: str, cfg: dict[str, Any], do_translate: bool, token: str | None, model: str, glossary: str) -> Path:
    target = WORK / "docs" / code
    shutil.rmtree(target, ignore_errors=True)
    target.mkdir(parents=True)
    for source_path in sorted(SOURCE.rglob("*")):
        if not source_path.is_file():
            continue
        relative = source_path.relative_to(SOURCE)
        if relative.name == "README.md":
            continue
        output = target / relative
        output.parent.mkdir(parents=True, exist_ok=True)
        if code == "en" or source_path.suffix.lower() != ".md":
            shutil.copy2(source_path, output)
            continue

        source_text = source_path.read_text(encoding="utf-8")
        metadata, body = split_document(source_text)
        expected = digest(code, source_text, glossary)
        translated = get_cached(code, relative, expected)
        fallback = False
        if translated is None and do_translate and token:
            try:
                translated = call_model(body, code, cfg["name"], glossary, token, model)
                set_cached(code, relative, expected, translated)
            except Exception as exc:
                print(f"::warning file={source_path}::{exc}", file=sys.stderr)
        if translated is None:
            translated = body
            fallback = True

        metadata = dict(metadata)
        metadata.update({
            "title": title_from(translated, metadata.get("title")),
            "language": code,
            "source_language": "en",
            "translation_status": "fallback-english" if fallback else "machine-translated",
            "human_review_required": True,
            "source_hash": expected,
        })
        notice = (
            '!!! warning "Translation notice"\n'
            '    This page was generated automatically from the English source and may require human review, especially for specialist terminology.\n\n'
        )
        if fallback:
            notice = (
                '!!! warning "Translation temporarily unavailable"\n'
                '    The current English source is displayed because an updated translation could not be generated during this deployment.\n\n'
            )
        output.write_text(join_document(metadata, notice + translated), encoding="utf-8")
    return target


def localize_nav(node: Any, docs: Path) -> Any:
    if isinstance(node, list):
        return [localize_nav(item, docs) for item in node]
    if isinstance(node, dict):
        result: dict[str, Any] = {}
        for label, value in node.items():
            if isinstance(value, str) and value.endswith(".md"):
                page = docs / value
                if page.exists():
                    metadata, body = split_document(page.read_text(encoding="utf-8"))
                    label = str(metadata.get("title") or title_from(body, label))
                result[label] = value
            else:
                result[label] = localize_nav(value, docs)
        return result
    return node


def build(
    code: str,
    cfg: dict[str, Any],
    locales: dict[str, dict[str, Any]],
    docs: Path,
    metadata: PublicationMetadata,
) -> None:
    config = read_yaml(BASE_CONFIG)
    config["copyright"] = f"{config.get('copyright', '')} · {metadata.compact_footer}"
    config["site_url"] = f"{BASE_URL}/{code}/"
    config["docs_dir"] = str(docs)
    config["site_dir"] = str(SITE / code)
    config["edit_uri"] = "edit/main/content/en/" if code == "en" else ""
    config["nav"] = localize_nav(config.get("nav", []), docs)

    theme = dict(config.get("theme", {}))
    theme["language"] = cfg.get("mkdocs_language", code)
    theme["direction"] = cfg.get("direction", "ltr")
    if code != "en":
        theme["features"] = [
            item for item in theme.get("features", [])
            if item not in {"content.action.edit", "content.action.view"}
        ]
    config["theme"] = theme
    config["extra"] = {
        **dict(config.get("extra", {})),
        "alternate": [
            {"name": data["name"], "link": f"/knife-knowledge-base/{locale}/", "lang": locale}
            for locale, data in locales.items() if data.get("deploy")
        ],
    }

    config_path = WORK / "configs" / f"mkdocs.{code}.yml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(yaml.safe_dump(config, allow_unicode=True, sort_keys=False), encoding="utf-8")
    subprocess.run([sys.executable, "-m", "mkdocs", "build", "--strict", "-f", str(config_path)], cwd=ROOT, check=True)


def root_index(locales: dict[str, dict[str, Any]]) -> None:
    SITE.mkdir(parents=True, exist_ok=True)
    links = "".join(
        f'<li><a href="{html.escape(code)}/">{html.escape(data["name"])}</a></li>'
        for code, data in locales.items() if data.get("deploy")
    )
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=en/"><link rel="canonical" href="{BASE_URL}/en/">
<title>Knife Knowledge Base</title></head><body><ul>{links}</ul><p><a href="en/">Continue in English</a></p></body></html>"""
    (SITE / "index.html").write_text(page, encoding="utf-8")
    (SITE / ".nojekyll").write_text("\n", encoding="utf-8")


def main() -> int:
    options = args()
    locale_cfg = read_yaml(LOCALES).get("locales", {})
    selected = options.locales or [code for code, cfg in locale_cfg.items() if cfg.get("deploy")]
    missing = [code for code in selected if code not in locale_cfg]
    if missing:
        raise SystemExit(f"Unknown locales: {', '.join(missing)}")

    shutil.rmtree(WORK, ignore_errors=True)
    shutil.rmtree(SITE, ignore_errors=True)
    token = os.getenv("GITHUB_TOKEN")
    glossary = GLOSSARY.read_text(encoding="utf-8") if GLOSSARY.exists() else ""
    if options.translate and not token:
        print("::warning::GITHUB_TOKEN is unavailable; translated sites will display English fallbacks", file=sys.stderr)

    metadata = get_metadata()
    print(f"Publication metadata: {metadata.full_label} · {metadata.publication_date}")

    for code in selected:
        print(f"Preparing {code}")
        docs = prepare_docs(code, locale_cfg[code], options.translate, token, options.model, glossary)
        print(f"Building {code}")
        build(code, locale_cfg[code], locale_cfg, docs, metadata)
    root_index(locale_cfg)
    print(f"Built {len(selected)} locale(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
