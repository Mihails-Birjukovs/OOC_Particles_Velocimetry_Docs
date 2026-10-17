# OOC Particle Velocimetry

**Documentation for OOC Particle Flow v5.2 — a Mathematica/Wolfram Language workflow for particle-image analysis.**

This site explains the research workflow from raw DynamicStudio TIFF sequences to cropped and enhanced images, binary particle masks, and particle-centroid coordinates. It documents the software's algorithms, configuration, outputs, and validation evidence.

## Start here

- [Set up the notebook](getting-started/index.md) — prerequisites and where each file belongs.
- [Process your first run](tutorials/first-run.md) — a step-by-step walkthrough of the existing pipeline.
- [Read the scientific methods](methods/index.md) — image enhancement, segmentation, artifact rejection, and centroid extraction.
- [Understand the evidence](validation/index.md) — what was validated and what remains unproven.

## Validated baseline

The current software is **v5.2**, promoted from the user-tested v5.1 notebook after an end-to-end run in Windows Mathematica 12.1.1. The version promotion changed notebook identity and explanatory text, not executable processing cells.

The accepted validation includes raw-to-cropped image equality on 100 frames, matching detected-particle counts at 99 independently plotted vertices across historical and revised runs, and notebook-level smoke/structure tests. **Count agreement does not establish pixelwise equivalence of enhanced images or masks, nor exact matching centroid coordinates.**

## Availability and scope

The source-code repository is currently **private**, while this site is designed for public scientific documentation. Repository links and code downloads may therefore require authorization from the repository owner.

The repository's original software and documentation are MIT-licensed. **Experimental acquisitions, processed-image archives, and numeric measurement fixtures are not covered by that software license.** See [licensing](licensing/index.md).

This website is a documentation layer; it does not host raw TIFFs, historical processed archives, or the Mathematica notebook itself.
