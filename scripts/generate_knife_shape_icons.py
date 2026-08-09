#!/usr/bin/env python3
"""Generate the original silhouette icons used by the Xinzuo knife-shape atlas."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "content" / "en" / "assets" / "icons" / "knife-shapes"


SHAPES: dict[str, tuple[str, str]] = {
    "paring-curved": ("Curved paring knife", "M18 60 Q92 16 215 31 L350 34 L350 66 L224 65 Q94 84 18 60 Z"),
    "paring-straight": ("Straight paring knife", "M18 52 Q92 33 210 36 L350 36 L350 67 L210 65 Q80 64 18 52 Z"),
    "paring-flat-cut": ("Flat-cut paring knife", "M18 44 L224 40 L350 40 L350 68 L210 68 L18 58 Z"),
    "utility": ("Utility knife", "M18 53 Q115 28 246 35 L350 37 L350 68 L220 66 Q90 65 18 53 Z"),
    "ultimate-utility": ("Ultimate utility knife", "M18 60 Q118 22 262 31 L350 35 L350 68 L205 66 Q78 74 18 60 Z"),
    "steak": ("Steak knife", "M18 54 Q116 27 254 34 L350 37 L350 68 L208 65 Q82 68 18 54 Z"),
    "butter": ("Butter knife", "M18 38 Q10 48 18 62 L350 68 L350 41 L62 38 Z"),
    "cheese": ("Cheese knife", "M18 55 Q92 29 230 33 L350 37 L350 68 L205 65 Q82 71 18 55 Z"),
    "chef": ("Western chef's knife", "M18 68 Q86 16 222 23 L350 34 L350 75 L178 78 Q82 79 18 68 Z"),
    "gyuto": ("Gyuto", "M18 67 Q92 22 236 28 L350 36 L350 73 L172 77 Q76 77 18 67 Z"),
    "santoku": ("Santoku", "M18 71 Q54 24 126 23 Q248 25 350 37 L350 76 L160 79 Q70 80 18 71 Z"),
    "bunka": ("Bunka", "M18 72 L104 26 L224 29 L350 39 L350 77 L154 80 Q66 81 18 72 Z"),
    "nakiri": ("Nakiri", "M18 42 L56 27 L350 36 L350 81 L18 80 Z"),
    "viking": ("Xinzuo Viking knife", "M18 70 Q66 18 166 22 Q260 26 350 39 L350 77 L158 80 Q62 81 18 70 Z"),
    "boning": ("Boning knife", "M18 58 Q94 31 214 38 L350 42 L350 68 L204 64 Q82 73 18 58 Z"),
    "honesuki": ("Honesuki", "M18 70 L142 30 L350 42 L350 78 L18 78 Z"),
    "fillet": ("Fillet knife", "M18 56 Q112 25 258 37 L350 42 L350 65 L215 62 Q82 70 18 56 Z"),
    "carving": ("Carving knife", "M18 55 Q118 27 270 35 L350 40 L350 67 L208 65 Q80 69 18 55 Z"),
    "roast-carving": ("Roast carving knife", "M18 58 Q116 19 268 30 L350 38 L350 69 L196 67 Q72 75 18 58 Z"),
    "granton-carving": ("Granton carving knife", "M18 55 Q118 27 270 35 L350 40 L350 67 L208 65 Q80 69 18 55 Z"),
    "ham": ("Ham knife", "M18 55 Q128 28 286 37 L350 41 L350 65 L214 63 Q82 68 18 55 Z"),
    "bread": ("Bread knife", "M18 56 Q100 23 246 31 L350 38 L350 70 L192 68 Q75 73 18 56 Z"),
    "frozen-food": ("Frozen-food knife", "M18 65 Q96 20 225 28 L350 38 L350 72 L192 72 Q76 79 18 65 Z"),
    "chinese-slicer": ("Chinese slicing knife", "M18 38 L350 38 L350 82 L18 82 Z"),
    "cleaver": ("Cleaver", "M18 30 L350 37 L350 86 L18 86 Z"),
    "chopper": ("Chopper", "M18 29 L350 38 L350 86 L18 84 Z"),
    "bone-chopper": ("Bone chopper", "M18 22 L350 34 L350 89 L18 89 Z"),
    "deba": ("Deba", "M18 72 Q56 25 139 21 Q250 25 350 40 L350 81 L18 81 Z"),
    "sashimi": ("Sashimi knife", "M18 53 Q126 18 285 34 L350 42 L350 66 L204 63 Q74 68 18 53 Z"),
    "sakimaru": ("Sakimaru", "M18 58 Q75 27 160 32 L350 42 L350 67 L205 64 Q82 72 18 58 Z"),
    "kiritsuke": ("Kiritsuke", "M18 65 L76 30 L245 34 L350 41 L350 72 L190 70 Q73 75 18 65 Z"),
    "granton-chef": ("Granton-edge chef's knife", "M18 68 Q86 16 222 23 L350 34 L350 75 L178 78 Q82 79 18 68 Z"),
}


WESTERN = {
    "paring-curved", "paring-straight", "paring-flat-cut", "utility", "ultimate-utility",
    "steak", "butter", "cheese", "chef", "viking", "boning", "fillet", "carving",
    "roast-carving", "granton-carving", "ham", "bread", "frozen-food", "granton-chef",
}
CHINESE = {"chinese-slicer", "cleaver", "chopper", "bone-chopper"}


def handle(slug: str) -> str:
    if slug in CHINESE:
        return """<path d="M350 45h23v31h-23z" fill="#8c2f2f"/><rect x="373" y="37" width="91" height="47" rx="18" fill="#3f2b24"/><path d="M389 40v41m19-43v45m19-45v45m19-43v41" stroke="#8f6654" stroke-width="3"/>"""
    if slug in WESTERN:
        return """<path d="M350 42h24v35h-24z" fill="#8c2f2f"/><path d="M374 35h88q13 0 13 13v24q0 13-13 13h-88z" fill="#3f2b24"/><circle cx="404" cy="60" r="4" fill="#e5cfa7"/><circle cx="444" cy="60" r="4" fill="#e5cfa7"/>"""
    return """<path d="M350 41h24v38h-24z" fill="#8c2f2f"/><path d="M374 32l18-7h65l18 12v46l-18 12h-65l-18-7z" fill="#3f2b24"/><path d="M390 30v60m66-60v60" stroke="#d9c6a4" stroke-width="3"/>"""


def details(slug: str) -> str:
    if slug in {"granton-carving", "granton-chef"}:
        return """<g fill="#f7f4ee" stroke="#7e8790" stroke-width="1.4">
<ellipse cx="112" cy="56" rx="11" ry="4"/><ellipse cx="145" cy="54" rx="11" ry="4"/>
<ellipse cx="178" cy="53" rx="11" ry="4"/><ellipse cx="211" cy="52" rx="11" ry="4"/>
<ellipse cx="244" cy="51" rx="11" ry="4"/>
</g>"""
    if slug in {"bread", "frozen-food"}:
        return """<path d="M45 53q9-9 18 0t18 0t18 0t18 0t18 0t18 0t18 0t18 0t18 0t18 0t18 0t18 0t18 0" fill="none" stroke="#f7f4ee" stroke-width="5"/>"""
    if slug == "cheese":
        return """<g fill="#f7f4ee"><ellipse cx="120" cy="50" rx="12" ry="6"/><ellipse cx="170" cy="49" rx="12" ry="6"/><ellipse cx="220" cy="50" rx="12" ry="6"/></g>"""
    return ""


def svg(slug: str, title: str, blade: str) -> str:
    detail_markup = details(slug)
    detail_line = f"  {detail_markup}\n" if detail_markup else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 110" role="img" aria-labelledby="title desc">
  <title id="title">{title} silhouette</title>
  <desc id="desc">Original educational side-profile icon for the Xinzuo knife-shape guide.</desc>
  <rect width="490" height="110" rx="12" fill="#f7f4ee"/>
  <path d="{blade}" fill="#cbd1d5" stroke="#263238" stroke-width="3" stroke-linejoin="round"/>
{detail_line}\
  {handle(slug)}
</svg>
'''


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for slug, (title, blade) in SHAPES.items():
        (OUTPUT / f"{slug}.svg").write_text(svg(slug, title, blade), encoding="utf-8")
    print(f"Generated {len(SHAPES)} knife-shape icons in {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
