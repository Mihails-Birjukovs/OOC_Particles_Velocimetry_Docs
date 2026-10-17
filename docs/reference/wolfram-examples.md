# Annotated Wolfram Language code

These explanations reflect actual **v5.2 notebook Input cells**, with some mappings shortened for readability. They are **not** a complete standalone replacement for the interactive notebook. The authoritative source is `OOC_Particle_Flow_v5.2.nb` in the private research repository.

## Parse numbered TIFF frames (Input cell 03)

```wl
frameIndex[file_String] := Module[
  {token = Last @ StringSplit[FileBaseName @ file, "."]},
  If[StringMatchQ[token, DigitCharacter..],
    FromDigits @ token,
    Missing["FrameIndex", token]]
];
```

This avoids evaluating arbitrary filename text as WL expressions. The run discovery step uses `SortBy[files, frameIndex]` and selects the exact prefix, followed by a period.

## Temporal diagnostics (Input cell 20)

```wl
projectionResult = TemporalProjections[
  croppedImages[[checkupIDs]],
  "ChunkSize" -> Ceiling @ N[
    Length[croppedImages[[checkupIDs]]] / chunkCountProjection
  ],
  "WorkingType" -> "Real32",
  "StandardDeviationConvention" -> "Sample",
  "ShowProgress" -> True
];
```

These temporal projections provide **diagnostics**; the enhancement chain still receives the original cropped sequence.

## Morphological top-hat and particle enhancement (cells 29 and 34)

```wl
topHatScale = 5;
filteredImages = ImageAdjust @
  TopHatTransform[#, DiskMatrix[topHatScale]] & /@ croppedImages;

(* After the separate temporal background-correction stage: *)
maxFilterScale = 1;
imagesEnhanced = ImageAdjust @
  MaxFilter[BrightnessEqualize @ Sqrt @ #, maxFilterScale] & /@
    imagesCorrected;
```

These abbreviated sequential maps are explanatory. The original notebook uses `parallelMapWithProgress` and run-specific timing.

## Histogram-reference selection (cell 37)

```wl
referenceFrameThreshold = 0.05;
referenceFrameIndex = 1 + LengthWhile[
  meanLuminanceSeriesStandardized,
  Abs[#] > referenceFrameThreshold &
];
If[referenceFrameIndex > Length @ imagesEnhanced, Abort[]];
referenceImage = imagesEnhanced[[referenceFrameIndex]];
```

This finds the **first** frame whose absolute standardized mean luminance is within the selected threshold. It does not use a fixed frame index.

## Persistent-artifact suppression and segmentation (cell 41)

```wl
segmentationMethod = "Entropy";
particleSizeThreshold = 5;

artifactMeanImage = Mean @ imagesEnhancedMatched;
artifactMask = MorphologicalBinarize[
  artifactMeanImage, Method -> "Entropy"
];

particleMasks = DeleteSmallComponents[
    ImageSubtract[
      Binarize[#, Method -> segmentationMethod],
      artifactMask
    ],
    particleSizeThreshold
  ] & /@ imagesEnhancedMatched;
```

The artifact mask uses **fixed Entropy** while the per-frame method is separately configurable. This is intentional scientific behavior, not a coding accident.

## Component centroids (cell 50)

```wl
particleCentroids = (
  Last /@ ComponentMeasurements[#, "Centroid"]
) & /@ particleMasks;

particleCountSeries = Length /@ particleCentroids;
```

The output is one list of coordinates for **each frame**, not linked trajectories. A `"Centroid"` may be subpixel-valued.

## Processing-record validation (cell 53)

Before the notebook writes `ProcessingParameters.wl`, it checks conditions including:

```wl
MatchQ[processingRecord["CropRowRange"], {_?NumericQ, _?NumericQ}]
MatchQ[processingRecord["CropColumnRange"], {_?NumericQ, _?NumericQ}]
IntegerQ[processingRecord["ReferenceFrameIndex"]]
1 <= processingRecord["ReferenceFrameIndex"] <= processingRecord["FrameCount"]
```

The actual cell also checks that required values exist, aborts on failure, then verifies the saved association using `Put` and `Get`. The excerpt above is a **partial explanation**, not a runnable full export cell.

For standalone runnable examples, see [synthetic sequence](../tutorials/synthetic-sequence.md).
