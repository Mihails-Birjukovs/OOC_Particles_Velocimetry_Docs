# Real Run 1 — 100-frame image-processing case

This is an authentic experimental input with a carefully documented **historical-v5 versus v5.2** boundary.

The private research repository stores the 100-TIFF **`Raw_images_for_testing.7z`** archive and the corresponding **`run1_mucins_oste.7z`** historical processed archive. The latter contains 100 cropped, enhanced and particle-mask frames from **v5**, not freshly executed v5.2 outputs.

## What has been verified?

An independent read-only decoder inspected the last TIFF page in each DynamicStudio file. Its uncompressed strips form a single `uint16` plane of **1024 × 1344** pixels. The stored `ImageDepth=12` metadata can mislead generic readers into interpreting a nonexistent 12-plane volume.

- **100/100** raw final-page TIFF arrays exactly match archived historical v5 cropped TIFFs.
- An independent 8-connected-component measurement on the **100 historical v5 masks** now agrees with **100/100 saved Run 2 Mathematica detection counts**, including frame 28 = **207**.
- The 100-frame total is **21,322** detected components.

This is stronger **count-level evidence** than the older 99-point PDF plot comparison. It is **not** proof of equal v5/v5.2 mask pixels or identical centroid coordinates.

## Reproducing the current v5.2 run locally

1. With authorized Git LFS access, retrieve the raw archive from the private repository and check its SHA-256 against the private manifest.
2. Extract to a short local Windows folder. Do not rewrite original TIFF headers or pixel arrays.
3. Open `OOC_Particle_Flow_v5.2.nb` alongside `TemporalProjections_v1.1.0.wl` in Mathematica.
4. In **Import Images**, set `imageFolder` and `subFolder`; discover the run prefix `mucini_oste220_1_01`, then select its integer `runIndex`.
5. Evaluate the crop, top-hat, temporal background correction, particle CNR, histogram matching, fixed-Entropy artifact mask, frame segmentation and centroid-extraction cells.
6. Save the enhanced/mask images and centroid records intentionally. Export and verify a fresh `ProcessingParameters.wl` association.

The native **Run 3** already completed 100-frame processing under Windows Mathematica 12.1.1 and exported a verified 17-field processing record with reference frame 12. A historical v5 image should **never** be relabeled as a v5.2 image.

## Real imagery and permissions

A low-resolution **real** figure showing raw frame 51, a historical v5 enhanced frame, the historical v5 mask, and an independently calculated centroid overlay has been prepared and scientifically checked **inside the private repository**. Publication of that derived experimental imagery remains under a separate rights-review gate. The MIT license for software/documentation does **not** automatically license experimental imagery.

Until the figure's publication permissions are explicitly confirmed, this public tutorial provides verified numerical results and the reproduction steps but does **not** redistribute raw TIFFs or mask images.

For a fully open, executable image-analysis demonstration, follow the [synthetic-sequence tutorial](synthetic-sequence.md).
