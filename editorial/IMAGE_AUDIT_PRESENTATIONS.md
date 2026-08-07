# Image Audit Against Presentation Materials

First pass: 2026-08-07 (written text only, presentation files not yet available)
Second pass: 2026-08-07 (completed against the actual presentation slides, supplied after the first pass)
Scope: every non-catalog, self-generated explanatory diagram currently published on the site and in the PDF export, checked against the owner's presentation slides, the approved English text, and the already-approved Xinzuo catalog images.

## Source material

The five presentation files were supplied and reviewed in full for this second pass:

- `Formazione Agenti A.pdf` (20 slides)
- `Formazione Agenti B.pdf` (26 slides)
- `Formazione Agenti C.pdf` (10 slides)
- `Formazione Agenti D.pdf` (12 slides)
- `Slides uso pietra.pdf` (2 slides)

All 70 slides were read page by page. Most are commercial/catalog pages (product photography, pricing, competitor comparisons, sales scripts) that are explicitly out of scope for technical diagrams and were not used, per the instruction not to include obsolete prices, old commercial claims, or unrelated slide content.

A first crop of the "Tipi di affilatura" chart (see below) left a sliver of the Xinzuo brand stamp visible in the bottom-left corner; this was caught during PDF contact-sheet review and fixed with a tighter crop that excludes the entire logo/page-number footer band of the source slide.

Two slides contained technically usable, correct diagrams not otherwise available from the approved catalog images, and were cropped and added:

- `Formazione Agenti A.pdf`, slide 14 ("Tipi di affilatura") — a chart of seven bevel-family cross-sections (V, convex, asymmetric V, compound double V, concave, single-sided, single-sided with urasuki).
- `Formazione Agenti D.pdf`, slide 5 ("Acciaio 'damasco puro', full damascus") — a technical cross-section comparison of historic Damascus steel and modern full-Damascus steel, explicitly showing the layered structure continuing to the cutting edge in both cases.

One slide was considered and deliberately **not** used:

- `Formazione Agenti D.pdf`, slide 3 ("Destrorso con coltello per destro") shows two photographs, but both depict the *same* normal right-handed grip (cutting salmon, then tuna) — neither shows the mismatched/compensated technique that the open `VIS-BEV-04` ("Handedness and Opposite-Hand Compensation") placeholder needs. Using this slide there would have implied a comparison that isn't actually pictured. Per "if there is any doubt, prefer placeholder over a wrong figure," `VIS-BEV-04` remains an open placeholder rather than being filled with a visual that doesn't show what it would claim to show.

No burr-formation diagram, whetstone-preparation diagram (beyond the real photograph already used for `VIS-STONE-01`), or knife-motion/arrow diagram was found anywhere in the five files.

## Audit table

| Visual / file | Section | Previous source type | Action | New source | Reason | Confidence |
|---|---|---|---|---|---|---|
| `five-dimensions-radar.svg` (`FIG-STEEL-DIMENSIONS`) | The Five Dimensions of Knife Steel | Generated | **A. Kept** | — (unchanged) | Axis labels match the five dimensions named in the approved text exactly. No numeric or absolute-ranking claim is made; matches the approved "not an absolute quality score" caveat. No presentation slide covers this concept as a generic (non-brand-specific) chart. No error found. | High |
| `single-vs-double-bevel.svg` (`FIG-BEV-CROSS-SECTION`) | Single and Double Bevels | Generated | **A. Kept** | — (unchanged) | Registered purpose (`VIS-BEV-01`) is a narrow, simple double-vs-single-bevel silhouette, not a full bevel-family chart. Single-bevel side matches the text's "nearly flat reverse around the urasuki." No error found for the scope this diagram claims. | High |
| — (new) | Single and Double Bevels — after the symmetrical/asymmetrical double-bevel section | Placeholder (`VIS-BEV-02`, never generated) | **B. Filled with a presentation image** | `Formazione Agenti A.pdf`, slide 14, cropped to the bevel-shape chart only (title bar, logo and page number removed) → `bevel-families.svg` | The slide's "Tipi di affilatura" chart shows exactly the seven bevel families the placeholder called for, correctly labelled, with no pricing or unrelated commercial content. Labels are in Italian in the source image itself (not translated, to avoid altering presentation artwork); the caption and a note explain what each label means and that the chapter text covers each shape. | High |
| `self-sharpening-damascus.svg` (was `FIG-SELF-DIFFERENTIAL-WEAR`, then placeholder `VIS-SELF-01`) | The Self-Sharpening Effect in Full Damascus Blades | Generated → withdrawn to placeholder in the first pass | **B. Filled with a presentation image** (supersedes the first-pass placeholder) | `Formazione Agenti D.pdf`, slide 5, cropped to the two structural diagrams only (bullet text, logo and the "structurally identical to Bintie steel" commercial claim removed) → `damascus-structure-comparison.svg` | The original generated diagram was removed in the first pass because its apex was drawn as a solid, unlayered shape, contradicting the chapter's central claim that the layers must reach the apex. This presentation diagram shows the opposite, and correctly: both the "ancient Damascus" and "HezHen Pure Damascus" cross-sections show the layer pattern running all the way to the labelled "CUTTING EDGE" point — exactly the structural claim the chapter makes. The specific HRC numbers visible in the source diagram describe the particular steels tested there; the caption and a note make clear these are not a general ranking of all Damascus knives, to avoid the "unsupported absolute steel rankings" the project's editorial safeguards exclude. | High |
| `whetstone-preparation.svg` (`FIG-STONE-PREPARATION-COMPARE`) | Preparing Water Stones | Generated | **A. Kept** | — (unchanged) | Compares absorbent-stone soaking, splash-and-go and keep-wet approaches without a fixed soak time, matching the approved "depends on the stone" caveat. The presentations' own whetstone slides (`Formazione Agenti C`, `Formazione Agenti D`, `Slides uso pietra`) give a fixed "15° guide, 15–20 passes" instruction set, which the project has already and deliberately declined to present as a universal rule — reinforcing that this generated diagram, which avoids that fixed-instruction framing, is the more correct choice here. No error found. | High |
| `burr-cross-section.svg` (`FIG-BURR-CROSS-SECTION`) | Understanding the Burr | Generated | **A. Kept** | — (unchanged) | Checked the fold direction explicitly: the abrasion arrow acts on one face and the burr bends to the opposite side, matching the approved definition precisely. No burr-formation diagram exists anywhere in the five presentation files to compare against or replace it with. No error found. | High |
| `knife-types-and-motion.svg` (`FIG-KNIFE-MOTION`) | Knife Types and Cutting Styles | Generated | **A. Kept, caption corrected (first pass)** | — (image unchanged) | Profile-vs-motion associations are consistent with the approved text. No presentation slide shows cutting motion with arrows/annotations; the presentations only show static named product photography, which doesn't provide a technical improvement over the existing diagram. The caption's false claim of being "adapted from the training slides" was already corrected in the first pass. | Medium-high (image content); High (caption correction) |
| — (considered, not used) | Single and Double Bevels — "Handedness and Opposite-Hand Compensation" (`VIS-BEV-04`) | Placeholder (never generated) | **D. Left as placeholder** | `Formazione Agenti D.pdf`, slide 3 considered and rejected | Both photographs on this slide show the same normal right-handed grip; neither depicts the mismatched/compensated technique the placeholder needs. Using it would misrepresent what the image actually shows. Placeholder left open pending a genuine two-case photograph or diagram. | High (that this slide does not fit) |

## Diagrams still without any generated or presentation image (no action needed)

Steering/handedness force diagrams (`VIS-BEV-03`, `VIS-BEV-04`) and the various knife-shape comparison placeholders (`VIS-KNIFE-02` and others already listed in `editorial/STRUCTURE_AND_VISUAL_AUDIT.md`) still have no image at all — they are open `IMAGE PLACEHOLDER` entries, and nothing in the five presentation files provided a correct, complete visual for them. They remain placeholders, consistent with the owner's priority order (placeholder over a wrong or incomplete figure).

## Summary

- **Removed (generated, contained a real error):** `self-sharpening-damascus.svg` — apex not shown as layered, contradicting the chapter's central claim. (First pass.)
- **Replaced with a presentation image:**
  - `VIS-SELF-01` ("Differential Wear Mechanism") ← `Formazione Agenti D.pdf`, slide 5 — supersedes the placeholder from the first pass.
  - `VIS-BEV-02` ("Main Bevel Families") ← `Formazione Agenti A.pdf`, slide 14 — a previously-open placeholder, now filled.
- **Replaced with a catalog image:** none — no catalog image covers a technical cross-section/mechanism diagram.
- **Placeholders remaining open by deliberate choice:** `VIS-BEV-04` (Handedness and Opposite-Hand Compensation) — a candidate slide exists but does not show the needed comparison; `VIS-BEV-03` and the knife-shape comparison placeholders — no presentation or catalog source found.
- **Kept after review, no change:** `five-dimensions-radar.svg`, `single-vs-double-bevel.svg`, `whetstone-preparation.svg`, `burr-cross-section.svg`, `knife-types-and-motion.svg`.
