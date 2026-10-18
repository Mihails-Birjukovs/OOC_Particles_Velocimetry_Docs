# Research, references & software origins

## Where the present framework came from

The validated **OOC Particle Flow v5.2** Mathematica notebook is a **simplified, optimized continuation** of Mihails Birjukovs's earlier [**OOC particle-flow CNR boost for PIV**](https://github.com/Mihails-Birjukovs/OOC_particle_flow_CNR_boost_for_PIV) implementation.

The predecessor repository contains `OOC_Particle_Flow_v3a_article_ready.nb`, with an MIT license and copyright © 2024 Mihails Birjukovs. It describes particle-image SNR/CNR enhancement for organ-on-a-chip microscopy and optional mask/coordinate extraction. The present v5.2 focuses on a streamlined preprocessing and detection pipeline and adds improved workflow robustness, reproducibility records and QA.

**Lineage is not algorithmic identity:** only implemented Input cells in the current notebook define current behavior. Earlier notebook sections, PIV approaches and tracking-related literature do **not** imply that v5.2 contains a completed PIV/PTV solver or trajectory linker.

## Primary OOC journal publication

**Šints, V., Cīmurs, J., Birjukovs, M., et al. (2025).** [*Physical model of serum supplemented medium flow in organ-on-a-chip systems*](https://doi.org/10.1371/journal.pone.0322069). **PLOS ONE 20(6)**, e0322069. DOI: [10.1371/journal.pone.0322069](https://doi.org/10.1371/journal.pone.0322069).

This peer-reviewed paper, published **17 June 2025**, is the journal publication of the [arXiv:2409.13650 preprint](https://arxiv.org/abs/2409.13650). The article discusses organ-on-a-chip flow measurements, rheology, modelling and image-based velocimetry, and identifies the earlier Mathematica code repository among its processing approaches.

**Recommended citation:** use the published **PLOS ONE** article as primary for the OOC scientific application. Retain the arXiv link for preprint history.

## Further methods and image-analysis background

The earlier repository's README explicitly cites these papers as methodological background:

1. **Birjukovs et al. (2021).** [*Resolving Gas Bubbles Ascending in Liquid Metal from Low-SNR Neutron Radiography Images*](https://doi.org/10.3390/app11209710). *Applied Sciences* **11(20)**, 9710. Background on enhancement and segmentation for difficult images.
2. **Birjukovs et al. (2022).** [*Particle tracking velocimetry in liquid gallium flow around a cylindrical obstacle*](https://doi.org/10.1007/s00348-022-03445-2). *Experiments in Fluids* **63**, 99. Background on low-SNR particle detection and tracking methodology.
3. **Birjukovs, Shevchenko & Eckert (2023).** [*An image processing pipeline for in situ dynamic X-ray imaging of directional solidification of metal alloys in thin cells*](https://doi.org/10.1007/s00348-023-03671-2). *Experiments in Fluids* **64**, 131. Background on image processing under low-contrast experimental conditions.

These are **scientific references**, not a statement that all algorithms from these papers have been implemented in this particular notebook.

## From earlier research code to v5.2

| Earlier framework | Current v5.2 |
| --- | --- |
| `OOC_Particle_Flow_v3a_article_ready.nb` | `OOC_Particle_Flow_v5.2.nb` and its generated readable `.wl` mirror |
| Research-era implementation for OOC flow image enhancement, masking and coordinates | Focused, organized and tested preprocessing and particle-detection workflow |
| Paper-oriented exploration and optional analysis | Documented stages, input validation, reproducible processing record, strict QA and worked examples |
| Historical methods and preliminary PIV/tracking-related headings | No claim of a completed, validated PIV/PTV trajectory solver |

The [Methods](../methods/index.md), [parameter reference](../reference/parameters.md), and [Run 1 validation example](../tutorials/real-run1.md) document exactly what v5.2 does and what has been independently verified.

## Citation guidance

For scientific flow/rheology results from the organ-on-a-chip study, cite **Šints et al. (2025)**. For the underlying algorithmic image-analysis methods, cite whichever of the above works actually underpin the method being discussed. For the software itself, link this project and identify **Mihails Birjukovs (2026)** as developer; a machine-readable software citation is planned separately.

The [Credits & provenance](../credits/index.md) page distinguishes INM code authorship from ISSP experimental-data ownership.