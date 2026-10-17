# First complete processing run

This tutorial follows the **existing** v5.2 notebook; it is not a new implementation or a separate command-line workflow. It assumes an authorized copy of the notebook and a compatible image sequence.

## 1. Initialize and select a run

1. Open `OOC_Particle_Flow_v5.2.nb` and evaluate **Initialization** and **Core Functions**.
2. Set `imageFolder` and `subFolder` in **Import Images**.
3. Evaluate discovery to populate `runRegistry`.
4. Choose the numeric `runIndex`; inspect preflight warnings before importing.
5. Evaluate the raw TIFF import cell. The workflow keeps the final imported image/page of each TIFF.

## 2. Crop and inspect

Use the interactive crop selector to establish `rowRange` and `columnRange`, or retain the appropriate numeric full-frame bounds. The raw sequence is not implicitly rotated merely because a preview orientation is configured. Evaluate the cropped-image sequence.

## 3. Enhance the particle images

Run the existing preprocessing cells in order:

1. Morphological top-hat filtering.
2. Interval-based temporal background correction.
3. Contrast/CNR enhancement.
4. Histogram matching (deflickering) after selecting the reference frame.

Common parameters include `topHatScale`, `meanCorrectionIntervals`, `maxFilterScale`, `referenceFrameThreshold`, and `referenceFrameIndex`. See the [full methods reference](../reference/METHODS.md).

## 4. Segment and extract detections

The persistent artifact mask uses **fixed Entropy** morphology; the per-frame `segmentationMethod` is configurable separately. Remove small components, inspect the resulting binary masks, and evaluate **Get particle coordinates** to obtain `particleCentroids`.

This step provides frame-wise detections; the notebook's historical tracking/MNNT headings are placeholders, **not an implemented end-to-end trajectory tracker**.

## 5. Export and retain provenance

Export the required images, masks, and centroid data as appropriate. Evaluate **Processing record** only after the crop and histogram-reference variables contain concrete values. The current export rejects unresolved bounds/index values and verifies a native Wolfram `Put`/`Get` round trip.

Archive the resulting `ProcessingParameters.wl` with the processed outputs. The notebook can also export a PDF snapshot for the run.

For optional restart points, troubleshooting, and the exact output tree, consult the [usage reference](../reference/USAGE.md).
