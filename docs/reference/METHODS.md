# Methods

## Overview

The notebook implements a particle-image preprocessing and detection workflow intended for low-contrast image sequences used in particle velocimetry. The current refactored tester version preserves the active v5.1 processing chain while improving robustness and reproducibility.

The active sequence is:

```
raw multipage TIFF
    ↓
select final imported TIFF image/page
    ↓
crop
    ↓
temporal projections / diagnostics
    ↓
morphological top-hat filtering
    ↓
interval-wise temporal background correction
    ↓
particle CNR enhancement
    ↓
histogram matching / deflickering
    ↓
persistent-artifact mask
    ↓
frame-wise particle segmentation
    ↓
small-component removal
    ↓
particle centroids
```

## 1. Input discovery and frame ordering

The notebook does not rely on `SetDirectory` for normal processing. Instead, `imageFolder` and `subFolder` are combined with `FileNameJoin`, and files are discovered using their full paths.

Expected frame names end in a numeric token before `.tif`, for example:

```
run11.example.000000.tif
run11.example.000001.tif
...
```

Only the final numeric filename token is converted to an integer. This avoids evaluating the rest of the basename as Wolfram Language input.

A run registry is constructed from the filename prefix before the first period. `runIndex` selects an entry from this registry, while `runIdentifier` stores the actual discovered identifier. Matching is exact up to the following period, so a prefix such as `run1` does not inadvertently match `run10` or `run11`.

## 2. TIFF import behavior

The DynamicStudio TIFFs used with this workflow can contain multiple imported elements/pages. The historical v5.1 workflow retained:

```wl
Last @ Import[file, IncludeMetaInformation -> None]
```

The refactored notebook deliberately preserves this behavior.

Before import, the notebook checks whether all selected files exist and warns about very long Windows paths. After import, it verifies that the final element of each imported TIFF is an `Image`, and checks consistency of image dimensions and image types.

## 3. Cropping

The user selects a region of interest interactively using two locators. The resulting `rowRange` and `columnRange` can be recorded and reused for repeated experiments with the same geometry.

The crop itself does not change the scientific processing method; it restricts subsequent processing to the selected field of view.

## 4. Temporal projections

`TemporalProjections_v1.1.0.wl` computes per-pixel temporal:

- minimum,
- maximum,
- mean,
- standard deviation.

The implementation is chunked and memory-bounded. Statistics are merged across chunks rather than constructing one extremely large time-channel image.

The package supports sample or population standard deviation. The notebook uses:

```wl
"StandardDeviationConvention" -> "Sample"
```

for the standard processing path.

These projection images are primarily diagnostic. For example, the temporal standard-deviation / mean ratio can highlight pixels with large relative temporal fluctuations.

## 5. Morphological top-hat filtering

Each cropped image is processed with:

```wl
ImageAdjust @ TopHatTransform[image, DiskMatrix[topHatScale]]
```

The morphological opening implicit in the top-hat transform estimates broader, slowly varying background structure. Subtracting this opening emphasizes smaller bright particle-scale structures.

The parameter `topHatScale` is therefore a spatial scale parameter in pixels.

Default in the current tester notebook:

```wl
topHatScale = 5;
```

## 6. Temporal background correction

The filtered sequence can be divided into one or more temporal intervals:

```wl
meanCorrectionIntervals = {1 ;; All};
```

A temporal mean image is calculated for each interval.

Two correction modes are retained:

### Subtractive correction

Default:

```wl
meanCorrection[image_, meanImage_] := ImageAdjust[image - meanImage]
```

The active workflow performs this after polarity inversion and then restores polarity.

### Flat-field-style correction

Optional:

```wl
meanCorrectionFlat[image_, meanImage_] :=
    ImageAdjust[ImageMultiply[image, meanImage^-1]]
```

This mode is selected with:

```wl
useFlatCorrection = 1;
```

The default is `0`, corresponding to the subtractive method.

## 7. Particle CNR enhancement

After temporal correction, the notebook applies:

```wl
ImageAdjust @ MaxFilter[BrightnessEqualize @ Sqrt[image], maxFilterScale]
```

This combines:

- square-root intensity compression,
- brightness equalization,
- a local maximum filter,
- final image adjustment.

The goal is to strengthen particle visibility before segmentation while retaining image geometry.

Default:

```wl
maxFilterScale = 1;
```

## 8. Deflickering by histogram matching

The mean luminance is computed for every enhanced frame. The mean-luminance series is standardized, and the notebook chooses the **first** frame satisfying:

```
Abs[standardized mean luminance] <= referenceFrameThreshold
```

Default:

```wl
referenceFrameThreshold = 0.05;
```

That frame becomes the histogram reference image.

Each enhanced frame is then transformed using:

```wl
HistogramTransform[frame, referenceImage]
```

This remaps intensities but does not move image geometry or particle coordinates.

## 9. Persistent-artifact suppression

Persistent dirt, optical structures, stuck objects, or other quasi-stationary features can survive ordinary particle segmentation. The workflow therefore forms the temporal mean of the matched sequence and constructs an artifact mask:

```wl
artifactMeanImage = Mean @ imagesEnhancedMatched;
artifactMask =
    MorphologicalBinarize[
        artifactMeanImage,
        Method -> "Entropy"
    ];
```

### Important design choice

The artifact mask is intentionally fixed to `"Entropy"`.

It is **not** controlled by `segmentationMethod`.

This is deliberate and should be preserved unless the scientific method itself is intentionally changed.

## 10. Frame-wise particle segmentation

Particle segmentation is performed independently for each matched frame:

```wl
Binarize[frame, Method -> segmentationMethod]
```

Default:

```wl
segmentationMethod = "Entropy";
```

An alternative retained in the notebook is:

```wl
"MinimumError"
```

The persistent artifact mask is subtracted from each frame mask.

## 11. Small-component removal

After artifact-mask subtraction, small connected components are removed:

```wl
DeleteSmallComponents[mask, particleSizeThreshold]
```

Default:

```wl
particleSizeThreshold = 5;
```

With this value, connected components containing 1–5 pixels are discarded.

## 12. Particle centroid extraction

Each binary particle mask is analyzed with:

```wl
ComponentMeasurements[mask, "Centroid"]
```

The resulting centroid coordinates are geometric component centroids and may therefore be subpixel-valued.

The output structure is one list of particle coordinates per frame:

```
particleCentroids = {
    {{x1,y1}, {x2,y2}, ...},   (* frame 1 *)
    {{x1,y1}, {x2,y2}, ...},   (* frame 2 *)
    ...
}
```

## 13. Optional channel-wall detection

The notebook retains a **Segment Channel Boundaries** section for optional/future use. It combines adaptive thresholding, Gaussian smoothing, closing, opening, and dilation to construct a wall/exclusion mask.

This section is not part of the current active particle-mask pipeline unless explicitly enabled.

## 14. Outputs and provenance

The workflow can export:

- cropped TIFF images,
- enhanced/matched TIFF images,
- particle-mask TIFF images,
- compressed particle-centroid data,
- a `ProcessingParameters.wl` record,
- a notebook/PDF snapshot of the run state.

The processing record contains principal parameters together with Wolfram version, operating system, selected run, crop ranges, and segmentation settings.

## 15. Version sensitivity

The historical reference output was generated with Mathematica 12.1.1 on Windows.

Later Wolfram versions can differ slightly in floating-point operations, `BrightnessEqualize`, or thresholding. Small last-bit or threshold-level differences should therefore be separated from genuine algorithmic changes when performing regression comparisons.

## Scientific origins and primary references

OOC Particle Flow v5.2 is a simplified and optimized continuation of Mihails Birjukovs's earlier [OOC CNR Boost for PIV Mathematica repository](https://github.com/Mihails-Birjukovs/OOC_particle_flow_CNR_boost_for_PIV). The peer-reviewed journal publication of the OOC flow study is [Šints et al., *PLOS ONE* 20(6), e0322069 (2025)](https://doi.org/10.1371/journal.pone.0322069), also available as [arXiv:2409.13650](https://arxiv.org/abs/2409.13650).

The predecessor README also cites image-analysis methods in [*Applied Sciences* (2021)](https://doi.org/10.3390/app11209710), [*Experiments in Fluids* (2022)](https://doi.org/10.1007/s00348-022-03445-2), and [*Experiments in Fluids* (2023)](https://doi.org/10.1007/s00348-023-03671-2). These are background references; the actual v5.2 Input cells define implemented features. See the [Research & References website page](../research/index.md).
