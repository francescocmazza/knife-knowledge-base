# Knife Knowledge Base

An open, practical knowledge base on kitchen knives—covering steels, blade geometry, construction, sharpening, maintenance, safety, and product education.

## Purpose

This project is designed for practical learning, commercial training, customer education, and marketing content. It is not intended to be an academic paper or a substitute for manufacturer-specific technical documentation.

The goal is to make knife knowledge easier to understand without turning useful simplifications into misleading claims.

## Website

The knowledge base is published as a searchable multilingual website with GitHub Pages:

**https://francescocmazza.github.io/knife-knowledge-base/**

Every approved change to the English core automatically rebuilds the website in all configured languages. The current deployment includes English, Italian, Spanish, German, French, Japanese, Simplified Chinese, Traditional Chinese, Portuguese, Polish, Czech, Dutch, Arabic, and Hebrew.

The site includes a language selector. English is published under `/en/`, while each localized version uses its BCP-47 locale path, such as `/it/`, `/ja/`, `/zh-Hans/`, and `/zh-Hant/`.

Machine-generated translations display a visible notice and remain open to human correction through pull requests. If a translation service is temporarily unavailable, the corresponding language path remains online and clearly displays the current English source as a fallback.

## Source-of-truth language

English is the sole source-of-truth language for this project. All translations and localized exports are derived from the English core. Changes that affect meaning must first be made in English.

The localization architecture supports any standard locale code, including:

- Italian (`it`)
- Spanish (`es`)
- German (`de`)
- French (`fr`)
- Japanese (`ja`)
- Simplified Chinese (`zh-Hans`)
- Traditional Chinese (`zh-Hant`)
- Arabic and other right-to-left languages

## Current scope

The first version covers:

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

See [the English content index](content/en/README.md).

## Project structure

```text
content/en/          English source of truth
translations/        Space for reviewed localized content
localization/        Locale configuration and translation rules
glossaries/          Controlled terminology
scripts/             Multilingual translation and site build tools
editorial/           Social and marketing content planning
sources/             Source-handling rules
assets/              Original or authorized visual material
exports/             Generated PDF, DOCX, HTML, and other formats
```

## Contributing

Corrections, questions, and new-topic proposals are welcome through GitHub Issues. Changes to the knowledge base should be submitted through pull requests.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting material.

## Images and third-party material

Only original, properly licensed, or explicitly authorized images may be added. Confidential manuals, proprietary slide decks, and third-party images must not be uploaded unless the repository owner has clear permission to publish them.

## License

Except where otherwise noted, the original written content is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license.

Commercial use requires separate prior written permission from the copyright holder. See [LICENSE.md](LICENSE.md).

© 2026 Francesco Claudio Mazza
