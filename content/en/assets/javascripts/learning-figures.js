(() => {
  const figures = [
    {
      match: "/01-foundations/five-dimensions-of-knife-steel/",
      file: "five-dimensions-radar.svg",
      alt: "Radar chart of the five dimensions used to describe knife steel",
      caption: "The five dimensions provide an educational map of a steel's character; they are not an absolute quality score."
    },
    {
      match: "/03-blade-construction/self-sharpening-full-damascus/",
      file: "self-sharpening-damascus.svg",
      alt: "Diagram of differential wear in a full Damascus cutting edge",
      caption: "Original diagram based on the layered-steel concept presented in the training slides."
    },
    {
      match: "/04-geometry-and-bevels/single-and-double-bevels/",
      file: "single-vs-double-bevel.svg",
      alt: "Cross-section comparison of single and double bevel edges",
      caption: "A simplified cross-section makes the basic geometric difference easier to visualize."
    },
    {
      match: "/05-knife-types/overview/",
      file: "knife-types-and-motion.svg",
      alt: "Knife profiles and their most common cutting motions",
      caption: "Adapted from the profile and cutting-style concepts in the original agent-training slides."
    },
    {
      match: "/10-sharpening/whetstone-preparation/",
      file: "whetstone-preparation.svg",
      alt: "Diagram comparing soaking, splash-and-go preparation and keeping a whetstone wet",
      caption: "The correct preparation depends on the stone; manufacturer instructions always prevail."
    },
    {
      match: "/10-sharpening/the-burr/",
      file: "burr-cross-section.svg",
      alt: "Cross-section diagram showing how a sharpening burr forms",
      caption: "The burr is a thin lip of steel still attached to the apex, not loose grinding residue."
    }
  ];

  function assetRoot() {
    const parts = location.pathname.split("/").filter(Boolean);
    const repo = parts.indexOf("knife-knowledge-base");
    if (repo < 0 || !parts[repo + 1]) return "/knife-knowledge-base/en/";
    return `/${parts.slice(0, repo + 2).join("/")}/`;
  }

  function placeFigure() {
    const article = document.querySelector("article.md-content__inner");
    if (!article || article.querySelector(".kb-learning-figure")) return;
    const item = figures.find((entry) => location.pathname.includes(entry.match));
    if (!item) return;

    const figure = document.createElement("figure");
    figure.className = "kb-learning-figure";
    const image = document.createElement("img");
    image.src = `${assetRoot()}assets/diagrams/${item.file}`;
    image.alt = item.alt;
    image.loading = "lazy";
    image.decoding = "async";
    const caption = document.createElement("figcaption");
    caption.textContent = item.caption;
    figure.append(image, caption);

    const h1 = article.querySelector("h1");
    const insertionPoint = h1?.nextElementSibling?.nextElementSibling || h1?.nextElementSibling;
    if (insertionPoint) insertionPoint.insertAdjacentElement("afterend", figure);
    else article.prepend(figure);
  }

  document.addEventListener("DOMContentLoaded", placeFigure);
  if (window.document$?.subscribe) window.document$.subscribe(placeFigure);
})();
