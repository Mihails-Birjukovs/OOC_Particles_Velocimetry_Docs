// Pinned MathJax 3.2.2 used by all OOC public Markdown pages.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true, processEnvironments: true,
    tags: "all", tagSide: "right", useLabelIds: true
  },
  options: { ignoreHtmlClass: ".*|", processHtmlClass: "arithmatex" }
};
if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    if (!window.MathJax || !MathJax.typesetPromise) return;
    MathJax.startup.output.clearCache();
    MathJax.typesetClear();
    MathJax.texReset();
    MathJax.typesetPromise();
  });
}
