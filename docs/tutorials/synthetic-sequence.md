# Fully reproducible synthetic particle sequence

This tutorial uses **eight invented 72×72 images**, avoiding any research image-data rights issues. It reproduces key WL image operations from the OOC pipeline in miniature. It is **not** the complete v5.2 notebook and omits multipage TIFF import, chunked projections, interactive crop, native metadata export and the notebook's histogram-reference selection.

The full demonstration was evaluated in a connected Wolfram kernel.

## 1. Create a deterministic image stack

```wl
ClearAll["Global`*"];
n = 72;
nFrames = 8;

scene[t_Integer] := Image[
  Table[
    Clip[
      0.08 + 0.16 x/n + 0.06 y/n +
        0.75 Exp[-((x - (12 + 5 t))^2 + (y - (25 + 2 t))^2)/14.] +
        0.60 Exp[-((x - (60 - 2 t))^2 + (y - 47)^2)/11.] +
        0.65 Exp[-((x - 57)^2 + (y - 13)^2)/20.],
      {0, 1}],
    {y, 1, n}, {x, 1, n}],
  "Real"];

images = scene /@ Range[nFrames];
```

Two bright objects move while the third remains stationary against a slowly varying artificial background.

## 2. Apply top-hat, temporal correction and enhancement

```wl
filtered = ImageAdjust[
    TopHatTransform[#, DiskMatrix[3]]
  ] & /@ images;

meanImage = Mean[filtered];
corrected = ColorNegate[
    ImageAdjust[ColorNegate[#] - meanImage]
  ] & /@ filtered;

enhanced = ImageAdjust[
    MaxFilter[BrightnessEqualize[Sqrt[#]], 1]
  ] & /@ corrected;

(* Teaching simplification: the real notebook selects a luminance reference. *)
referenceImage = enhanced[[1]];
matched = HistogramTransform[#, referenceImage] & /@ enhanced;
```

## 3. Artifact mask, particle masks and centroids

```wl
artifactMean = Mean[matched];
artifactMask = MorphologicalBinarize[
  artifactMean, Method -> "Entropy"
];

masks = DeleteSmallComponents[
    ImageSubtract[Binarize[#, Method -> "Entropy"], artifactMask],
    3
  ] & /@ matched;

centroids = (Last /@ ComponentMeasurements[#, "Centroid"]) & /@ masks;
counts = Length /@ centroids;

<|
  "Frames" -> Length[images],
  "Dimensions" -> ImageDimensions[First[images]],
  "MaskType" -> ImageType[First[masks]],
  "ParticleCounts" -> counts
|>
```

In the tested Wolfram kernel, the result was:

```text
Frames          8
Dimensions      {72, 72}
MaskType        Bit
ParticleCounts  {4, 4, 4, 2, 3, 7, 6, 4}
```

Do not treat these numbers as a scientific or cross-version benchmark. A separate verification confirmed that all generated processing-stage objects were `Image` instances and every centroid frame was a list.

## 4. Inspect the stage outputs

```wl
ImageCollage[
  {First[images], First[filtered], First[enhanced],
   First[matched], First[masks]},
  ImageSize -> 750
]

And @@ (ImageQ /@ Join[
  images, filtered, corrected, enhanced, matched, masks
])
And @@ (ListQ /@ centroids)
```

Both final checks returned `True` during the tested evaluation. For an actual acquisition, continue with the [real Run 1 case](real-run1.md) and preserve your run-specific processing metadata.
