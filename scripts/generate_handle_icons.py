#!/usr/bin/env python3
"""Generate original handle-shape and handle-material icons for the guide."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ICON_ROOT = ROOT / "content" / "en" / "assets" / "icons"


MATERIALS = {
    "rosewood": ("Rosewood", "#6f3028", "wood"),
    "red-wood": ("Red wood", "#7e3d2d", "wood"),
    "pakka-wood": ("Pakka wood", "#b47c45", "laminate"),
    "ebony": ("Ebony", "#202124", "wood"),
    "figured-sycamore": ("Figured sycamore", "#c89b67", "figure"),
    "micarta": ("Micarta", "#7a4f3b", "weave"),
    "desert-ironwood": ("Desert ironwood", "#5e3729", "figure"),
    "olivewood": ("Olivewood", "#b48650", "figure"),
    "carbon-fiber-resin": ("Carbon fiber with resin", "#27333a", "resin-weave"),
    "red-sandalwood": ("Red sandalwood", "#71322b", "wood"),
    "oak": ("Oak", "#a57a4d", "wood"),
    "walnut": ("Walnut", "#694737", "wood"),
    "resin": ("Resin", "#274b57", "resin"),
    "carbon-fiber": ("Carbon fiber", "#20262b", "weave"),
    "black-g10": ("Black G10", "#171a1d", "laminate"),
    "buffalo-horn": ("Buffalo horn", "#2b2927", "figure"),
    "imitation-ox-bone": ("Imitation white ox bone", "#ded5bf", "laminate"),
    "copper": ("Copper", "#9d5638", "laminate"),
    "metal-composite-spacers": ("Metal and composite spacers", "#69757c", "laminate"),
}


HANDLE_SHAPES = {
    "full-tang-riveted": ("Western full-tang scales", "M18 31 Q34 20 58 23 L197 33 Q220 35 232 52 Q220 69 197 71 L58 80 Q34 82 18 70 Z", 3),
    "sculpted-western": ("Sculpted Western handle", "M18 38 Q46 18 80 31 Q118 43 155 26 Q199 10 232 44 Q220 78 181 81 Q135 70 97 82 Q48 93 18 64 Z", 1),
    "octagonal-wa": ("Octagonal wa-style handle", "M18 36 L45 20 H199 L232 36 V74 L199 90 H45 L18 74 Z", 0),
    "faceted-hidden-tang": ("Faceted hidden-tang handle", "M18 42 L52 20 H198 L232 36 V70 L198 88 H52 L18 68 Z", 0),
    "segmented-hidden-tang": ("Segmented hidden-tang handle", "M18 34 L44 21 H202 L232 38 V72 L202 89 H44 L18 76 Z", 0),
    "cylindrical-chinese": ("Cylindrical Chinese handle", "M18 41 Q18 22 40 19 H202 Q232 20 232 55 Q232 90 202 91 H40 Q18 88 18 69 Z", 0),
}


def material_motif(kind: str) -> str:
    if kind == "wood":
        return '<path d="M17 39c28-22 43 19 70-3s43 18 70-2 44 17 70-4" fill="none" stroke="#fff" stroke-opacity=".42" stroke-width="5"/><path d="M20 73c27-20 42 17 68-2s42 15 68-2 43 15 69-4" fill="none" stroke="#fff" stroke-opacity=".24" stroke-width="3"/>'
    if kind == "figure":
        return '<path d="M14 26c25 35 51 35 76 0s51-35 76 0 51 35 76 0M14 82c25-35 51-35 76 0s51 35 76 0 51-35 76 0" fill="none" stroke="#fff" stroke-opacity=".38" stroke-width="5"/>'
    if kind == "weave":
        return '<path d="M10 18l84 84m-45-84l84 84m-45-84l84 84m-45-84l84 84m-45-84l70 70M10 102l84-84m-45 84l84-84m-45 84l84-84m-45 84l84-84m-45 84l70-70" stroke="#fff" stroke-opacity=".32" stroke-width="5"/>'
    if kind == "laminate":
        return '<path d="M12 31h216M12 48h216M12 65h216M12 82h216" stroke="#fff" stroke-opacity=".38" stroke-width="5"/>'
    if kind == "resin-weave":
        return '<path d="M12 85Q54 20 96 85T180 85T264 85" fill="none" stroke="#c88d59" stroke-width="9" stroke-opacity=".75"/><path d="M20 20l82 82m-36-82l82 82m-36-82l82 82m-36-82l72 72" stroke="#fff" stroke-opacity=".25" stroke-width="4"/>'
    return '<path d="M10 78Q54 15 96 78T180 78T264 78" fill="none" stroke="#d3a76f" stroke-width="12" stroke-opacity=".75"/>'


def material_svg(title: str, color: str, kind: str) -> str:
    initials = "".join(part[0] for part in title.split() if part.lower() not in {"with"})[:3].upper()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 250 120" role="img" aria-labelledby="title desc">
  <title id="title">{title} material icon</title>
  <desc id="desc">Original educational icon indicating the visual family of {title}.</desc>
  <rect x="4" y="4" width="242" height="112" rx="18" fill="{color}" stroke="#263238" stroke-width="4"/>
  {material_motif(kind)}
  <rect x="171" y="68" width="63" height="38" rx="12" fill="#f7f4ee" fill-opacity=".9"/>
  <text x="202.5" y="94" text-anchor="middle" font-family="Arial, sans-serif" font-size="21" font-weight="700" fill="#263238">{initials}</text>
</svg>
'''


def handle_svg(title: str, path: str, rivets: int) -> str:
    rivet_markup = "".join(f'<circle cx="{70 + index * 54}" cy="55" r="6" fill="#e4cda8" stroke="#263238" stroke-width="2"/>' for index in range(rivets))
    separators = ""
    if "Segmented" in title:
        separators = '<path d="M57 24v62m120-62v62" stroke="#d9c6a4" stroke-width="8"/>'
    if "Faceted" in title or "Octagonal" in title:
        separators += '<path d="M35 36h180M35 74h180" stroke="#fff" stroke-opacity=".22" stroke-width="3"/>'
    if "Cylindrical" in title:
        separators = '<path d="M55 24v62m30-64v66m30-65v64m30-64v64m30-65v66" stroke="#8f6654" stroke-width="4"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 250 110" role="img" aria-labelledby="title desc">
  <title id="title">{title} icon</title>
  <desc id="desc">Original educational handle-profile icon for the Xinzuo handle guide.</desc>
  <rect width="250" height="110" rx="14" fill="#f7f4ee"/>
  <path d="{path}" fill="#5b392c" stroke="#263238" stroke-width="4" stroke-linejoin="round"/>
  {separators}{rivet_markup}
</svg>
'''


def main() -> None:
    material_dir = ICON_ROOT / "handle-materials"
    shape_dir = ICON_ROOT / "handle-shapes"
    material_dir.mkdir(parents=True, exist_ok=True)
    shape_dir.mkdir(parents=True, exist_ok=True)
    for slug, (title, color, kind) in MATERIALS.items():
        (material_dir / f"{slug}.svg").write_text(material_svg(title, color, kind), encoding="utf-8")
    for slug, (title, path, rivets) in HANDLE_SHAPES.items():
        (shape_dir / f"{slug}.svg").write_text(handle_svg(title, path, rivets), encoding="utf-8")
    print(f"Generated {len(MATERIALS)} material icons and {len(HANDLE_SHAPES)} handle-shape icons")


if __name__ == "__main__":
    main()
