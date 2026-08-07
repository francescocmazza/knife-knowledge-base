# Image Audit Against Presentation Materials

First pass: 2026-08-07 (written text only, presentation files not yet available)
Second pass: 2026-08-07 (checked against the supplied presentation slides)
Third pass: 2026-08-07 (independent publication review after PDF inspection)

Scope: every non-catalog explanatory diagram currently published on the site and in the PDF export, checked against the owner's presentation slides, the approved English text and the already-approved Xinzuo catalog images.

## Source material

The five presentation files supplied for review were:

- `Formazione Agenti A.pdf`
- `Formazione Agenti B.pdf`
- `Formazione Agenti C.pdf`
- `Formazione Agenti D.pdf`
- `Slides uso pietra.pdf`

Two presentation-derived visuals remain useful after the third-pass review:

- `Formazione Agenti A`, slide 14 (`Tipi di affilatura`) — used as a schematic overview of grind/bevel cross-section geometries.
- `Formazione Agenti D`, slide 5 (`Acciaio "damasco puro", full damascus`) — used only for the modern full-Damascus panel in the rendered guide.

`Formazione Agenti D`, slide 3 was again rejected for the handedness/opposite-hand placeholder because both photographs show ordinary right-handed use and do not demonstrate compensated opposite-hand technique.

## Third-pass decisions

| Visual / file | Section | Third-pass action | Reason |
|---|---|---|---|
| `five-dimensions-radar.svg` (`FIG-STEEL-DIMENSIONS`) | The Five Dimensions of Knife Steel | **Corrected** | The previous blue polygon implied arbitrary steel scores even though no steel, scale or test method was identified. The plotted polygon was removed. The figure now shows only the five-axis comparison framework; values should be plotted only when all axes are supported by a consistent method. |
| `single-vs-double-bevel.svg` (`FIG-BEV-CROSS-SECTION`) | Single and Double Bevels | **Withdrawn from published output; placeholder restored** | The two cross-sections were drawn with inconsistent orientation, which makes the comparison technically ambiguous. The guide now prefers a placeholder over publishing a misleading generated diagram. |
| `bevel-families.svg` (`VIS-BEV-02`) | Single and Double Bevels | **Kept with corrected description** | The source slide is useful, but these drawings are better described as schematic grind/bevel cross-section geometries, not as a universal taxonomy of equivalent edge bevels. The caption and note were corrected accordingly. |
| `damascus-structure-comparison.svg` (`VIS-SELF-01`) | Self-Sharpening Full Damascus | **Modern panel kept; historical panel excluded from rendered guide** | The modern panel is useful because it shows alternating layers extending through the blade to the cutting-edge region. The historical comparison panel must not be presented as proof that historical wootz is a forge-welded alternating-layer construction. The rendered guide therefore crops to the modern panel only and explains that limitation explicitly. |
| `knife-types-and-motion.svg` (`FIG-KNIFE-MOTION`) | Knife Types and Cutting Styles | **Withdrawn from published output; placeholder restored** | Several generated silhouettes were not reliable enough representations of their named knife profiles for a technical guide. The existing catalog shape index remains the verified visual reference while a better motion-specific graphic is prepared. |
| `whetstone-preparation.svg` (`FIG-STONE-PREPARATION-COMPARE`) | Preparing Water Stones | **Kept** | The figure accurately distinguishes absorbent soaking, splash-and-go preparation and keeping the working surface wet, while preserving the approved rule that manufacturer instructions prevail. |
| `burr-cross-section.svg` (`FIG-BURR-CROSS-SECTION`) | Understanding the Burr | **Withdrawn from published output; placeholder restored** | Although the burr fold direction was plausible, the 'before the apex is reached' panel already looked like a complete sharp apex. That can teach the wrong geometry. A verified replacement is preferred. |
| `VIS-BEV-04` | Handedness and Opposite-Hand Compensation | **Left as placeholder** | The candidate presentation photographs do not show the comparison the label requires. |

## Publication behaviour

The third-pass corrections are implemented as a post-audit rendering layer loaded after the original learning-figure system. This lets the live site and the browser-rendered PDF export share exactly the same correction rules without modifying translated source trees.

The correction layer:

- removes the three withdrawn generated figures from the rendered article;
- restores explicit editorial placeholders for them;
- corrects the five-dimensions caption;
- corrects the bevel-geometry caption and source note;
- crops the Damascus presentation image to the modern full-Damascus panel only;
- leaves unrelated approved catalog images and verified diagrams untouched.

## Rights / provenance caution

Presentation-derived material is not automatically cleared merely because it appears in an internal presentation. The repository owner's permission to use the presentation does not establish ownership of every embedded third-party element. `content/en/assets/IMAGE_RIGHTS.md` therefore treats presentation-derived crops as restricted project-use material unless underlying rights provenance is independently confirmed.

No confidential Musashi material is used.

## Current status

### Corrected and kept

- `five-dimensions-radar.svg`
- `whetstone-preparation.svg`
- `bevel-families.svg` with revised terminology
- modern full-Damascus panel from `damascus-structure-comparison.svg`

### Withdrawn from rendered publication pending verified replacements

- `single-vs-double-bevel.svg`
- `knife-types-and-motion.svg`
- `burr-cross-section.svg`

### Still intentionally open

- `VIS-BEV-04` — Handedness and Opposite-Hand Compensation
- existing steering, knife-comparison, sharpening and other planned placeholders already tracked by the visual plan

The governing rule remains: **a placeholder is preferable to a technically misleading illustration.**
