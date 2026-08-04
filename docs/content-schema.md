# Content Schema

Every core knowledge page should begin with YAML front matter.

```yaml
---
title: Example Title
status: draft
audience: commercial-training
language: en
reviewed: 2026-08-04
translation_priority: high
---
```

## Required fields

- `title`: public page title;
- `status`: `draft`, `review`, `approved`, or `deprecated`;
- `audience`: intended readership;
- `language`: source language code;
- `reviewed`: date of the latest editorial review;
- `translation_priority`: `high`, `medium`, or `low`.

## Recommended page structure

1. Short definition
2. Why it matters
3. Practical explanation
4. Important limits or common misunderstanding
5. Customer-facing summary
6. Social-content angles
7. Related pages

## Translation rule

Localized files must record the source revision or commit. When the English source changes meaning, affected translations must return to `needs-update` status.
