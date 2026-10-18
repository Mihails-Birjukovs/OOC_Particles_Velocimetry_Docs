<section class="ooc-hero" aria-label="OOC Particle Flow documentation">
  <div class="ooc-eyebrow">Scientific image analysis · Wolfram Mathematica · Validated v5.2</div>
  <h1>OOC Particle Velocimetry</h1>
  <p>A reproducible particle-image enhancement and detection workflow for low-contrast organ-on-a-chip experiments. From microscopy frames to binary masks, centroid coordinates and processing provenance.</p>
  <div class="ooc-actions">
    <a class="ooc-link ooc-link-primary" href="getting-started/index.md">Get started</a>
    <a class="ooc-link" href="pipeline/index.md">Explore the pipeline</a>
    <a class="ooc-link" href="tutorials/real-run1.md">Real-data example</a>
  </div>
</section>

<img class="ooc-brand-mark" src="assets/inm-horizontal.svg" alt="Official Institute of Numerical Modelling, University of Latvia logo" />

<div class="ooc-identity">
  <div><small>Software & documentation</small><strong>Mihails Birjukovs</strong><br />Institute of Numerical Modelling (INM), University of Latvia</div>
  <div><small>Experimental data & credit</small><strong>Institute of Solid State Physics (ISSP)</strong><br />Betija Ziediņa and Gunita Kojāne · University of Latvia</div>
</div>

**Documentation for OOC Particle Flow v5.2 — a Mathematica/Wolfram Language workflow for particle-image analysis.**

This site explains the research workflow from raw DynamicStudio TIFF sequences to cropped and enhanced images, binary particle masks, and particle-centroid coordinates. It documents the software's algorithms, configuration, outputs, and validation evidence.

## Start here

- [Set up the notebook](getting-started/index.md) — prerequisites and where each file belongs.
- [Process your first run](tutorials/first-run.md) — a step-by-step walkthrough of the existing pipeline.
- [Explore the illustrated pipeline](pipeline/index.md) — the implemented stages and their outputs.
- [Run a reproducible synthetic example](tutorials/synthetic-sequence.md) — executable Wolfram code without experimental inputs.
- [Review the real 100-frame Run 1 case](tutorials/real-run1.md) — independent TIFF and detection-count checks.
- [Read the scientific methods](methods/index.md) — image enhancement, segmentation, artifact rejection, and centroid extraction.
- [Understand the evidence](validation/index.md) — what was validated and what remains unproven.

## Validated baseline

The current software is **v5.2**, promoted from the user-tested v5.1 notebook after an end-to-end run in Windows Mathematica 12.1.1. The version promotion changed notebook identity and explanatory text, not executable processing cells.

The accepted validation includes raw-to-cropped image equality on 100 frames, matching detected-particle counts at 99 independently plotted vertices across three PDF runs, plus a separate **100/100** historical-v5-mask-to-saved-Run-2 count comparison, and notebook-level smoke/structure tests. **Count agreement does not establish pixelwise equivalence of enhanced images or masks, nor exact matching centroid coordinates.**

## Availability and scope

The source-code repository is currently **private**, while this site is designed for public scientific documentation. Repository links and code downloads may therefore require authorization from the repository owner.

The repository's original software and documentation are MIT-licensed. **Experimental acquisitions, processed-image archives, and numeric measurement fixtures are not covered by that software license.** See [licensing](licensing/index.md).

This website is a documentation layer; it does not host raw TIFFs, historical processed archives, or the Mathematica notebook itself.

## Origins and credits

This streamlined v5.2 implementation continues Mihails Birjukovs's original [CNR-boost for PIV Mathematica framework](https://github.com/Mihails-Birjukovs/OOC_particle_flow_CNR_boost_for_PIV). Its organ-on-a-chip scientific application was published in [Šints et al., *PLOS ONE* (2025)](https://doi.org/10.1371/journal.pone.0322069), the journal version of [arXiv:2409.13650](https://arxiv.org/abs/2409.13650).

**ISSP owns the experimental data**, with principal experimental contributions by **Betija Ziediņa** and **Gunita Kojāne**. **Mihails Birjukovs (INM)** developed the code and this documentation. ISSP authorized the reduced-resolution Run 1 example for publication here. See [Credits & data provenance](credits/index.md), [Research & references](research/index.md), and [Licensing](licensing/index.md).
