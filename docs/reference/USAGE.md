# Usage

Current canonical notebook: **OOC Particle Flow v5.2**. Its scientific Input cells are unchanged from the validated v5.1 notebook used for the Windows Run 3 test.

## 1. Repository files

Keep these two files together unless you intentionally change the package path:

```
OOC_Particle_Flow_v5.2.nb
TemporalProjections_v1.1.0.wl
```

By default, the notebook uses its own directory as `packageDirectory`.

## 2. Open and initialize

Open:

```
OOC_Particle_Flow_v5.2.nb
```

Evaluate:

1. **Initialization**
2. **Core Functions**

The initialization section:

- clears the global context,
- loads `TemporalProjections_v1.1.0.wl`,
- prepares the output folder,
- sets plot defaults,
- launches parallel kernels,
- prints the Wolfram version and kernel count.

## 3. Configure the input folder

In **Import Images**, edit:

```wl
imageFolder := "C:\path\to\experiment";
subFolder := FileNameJoin[{"relative", "folder", "containing", "TIFFs"}];
```

The notebook then forms:

```wl
fileFolder = FileNameJoin[{imageFolder, subFolder}];
```

### Recommended folder convention

A typical layout is:

```
experiment/
└── run_folder/
    └── ch1/
        ├── run1.example.000000.tif
        ├── run1.example.000001.tif
        ├── ...
        └── run2.example.000000.tif
```

The TIFFs for all candidate runs can be in the same folder.

## 4. Discover runs

Evaluate the discovery cell.

The notebook creates `runRegistry` and displays a table:

```
runIndex    runIdentifier
1           run1
2           run2
...
```

Select the desired run by setting:

```wl
runIndex = 1;
```

The actual filename prefix is then stored in:

```wl
runIdentifier
```

Do not manually substitute a filename fragment for `runIndex`; it is an integer registry index.

## 5. Check the preflight output

Before import, the notebook prints:

- input folder,
- selected run,
- number of TIFF files,
- first file,
- last file,
- maximum full-path length.

The preflight validator checks whether files are accessible.

### Windows / OneDrive note

Long synced paths can fail in `Import` even when `FileNames` can see them.

If paths approach the traditional Windows 260-character limit:

- shorten the folder hierarchy,
- move/copy the active test sequence to a shorter local path,
- ensure OneDrive files are actually available offline.

The notebook warns when a selected path is unusually long.

## 6. Import the raw sequence

Evaluate **Raw TIFF import**.

The workflow preserves the historical behavior of taking the final imported image/page from each multipage TIFF.

Post-import validation checks:

- that the final imported object is an `Image`,
- image dimensions,
- image type consistency.

## 7. Inspect orientation

The notebook defines:

```wl
rotationSwitch = 0;
rotationAngle = Pi/2;
```

The orientation controls are primarily for viewing/utility operations. The stored raw sequence is not rotated unless `rotateImage` is explicitly applied.

## 8. Select the crop

Use the interactive crop selector and drag the two locator points.

This assigns:

```wl
rowRange
columnRange
```

If the same imaging geometry is reused, these ranges can be stored and assigned directly on later runs.

Then process the crop sequence.

## 9. Temporal diagnostics

The notebook calculates temporal:

- minimum,
- maximum,
- mean,
- standard deviation.

These diagnostics are useful for identifying:

- persistent structures,
- unstable regions,
- changing illumination,
- particle-motion regions.

They do not themselves alter the particle images.

## 10. Configure preprocessing parameters

The main parameters in the current workflow are:

```wl
topHatScale = 5;
meanCorrectionIntervals = {1 ;; All};
useFlatCorrection = 0;
maxFilterScale = 1;
referenceFrameThreshold = 0.05;
segmentationMethod = "Entropy";
particleSizeThreshold = 5;
```

### Temporal correction intervals

If illumination/background conditions change during a long sequence, use multiple spans, for example:

```wl
meanCorrectionIntervals = {
    1 ;; 500,
    501 ;; 1000,
    1001 ;; All
};
```

The intervals should collectively correspond to the frames you intend to process.

### Segmentation method

The default frame-wise segmentation is:

```wl
segmentationMethod = "Entropy";
```

The notebook also retains:

```wl
segmentationMethod = "MinimumError";
```

Changing `segmentationMethod` does **not** change the persistent artifact-mask method.

## 11. Run the enhancement chain

Evaluate in order:

1. morphological top-hat filtering,
2. temporal background correction,
3. particle CNR enhancement,
4. mean-luminance extraction,
5. histogram matching / deflickering.

Progress indicators are included for full-sequence processing operations.

## 12. Persistent artifact mask

The persistent artifact detector is intentionally:

```wl
artifactMask =
    MorphologicalBinarize[
        artifactMeanImage,
        Method -> "Entropy"
    ];
```

Do not replace this with `segmentationMethod` merely for convenience. The fixed method is an intentional part of the current workflow.

## 13. Segment particles

The notebook performs, for every matched frame:

1. `Binarize[..., Method -> segmentationMethod]`,
2. subtraction of `artifactMask`,
3. `DeleteSmallComponents[..., particleSizeThreshold]`.

Inspect the resulting masks before relying on centroid output.

## 14. Extract centroids

Evaluate **Get particle coordinates**.

The notebook builds:

```wl
particleCentroids
```

and plots the number of detected components versus frame index.

The centroid data can then be used as the detection input for downstream PTV/tracking workflows.

## 15. Output folders

For a selected run, the notebook creates a run-specific output tree containing folders such as:

```
Output/
└── <subFolder>/
    └── <runIdentifier>/
        ├── 1 Cropped Images/
        ├── 2 Enhanced Images/
        ├── 3 Particle Masks/
        ├── CSV/
        ├── Compressed Data/
        └── ProcessingParameters.wl
```

The precise set of outputs depends on which export cells are evaluated.

## 16. Restart points

Optional restart/import cells are present for:

- cropped images,
- enhanced images,
- particle masks,
- particle centroids.

They are intentionally commented by default.

This prevents **Evaluate Notebook** from accidentally replacing fresh in-memory results with an older saved intermediate result.

Enable a restart cell only when resuming from an existing processing folder.

## 17. Processing record

At the end of a run, evaluate the processing-record cell.

It writes `ProcessingParameters.wl` with fields including:

- timestamp,
- Wolfram version,
- operating system,
- input folder,
- run identifier,
- frame count,
- crop ranges,
- top-hat scale,
- background-correction intervals,
- correction mode,
- enhancement scale,
- histogram reference settings,
- segmentation method,
- fixed artifact-mask method,
- small-component threshold.

This file should be retained with processed outputs.

## 18. Notebook snapshot

The notebook can save itself and export a PDF snapshot into the run output directory.

This is useful for recording the parameter state and interactive notebook configuration used for a particular processed example.

## 19. Progress indicators

The refactored tester notebook includes progress/activity indicators for:

- raw TIFF import,
- full-sequence crop,
- cropped-image export,
- temporal projections,
- top-hat filtering,
- temporal background correction,
- CNR enhancement,
- mean-luminance extraction,
- histogram matching,
- temporal-mean calculations,
- particle segmentation/cleanup,
- mask temporal projections,
- enhanced-image and mask export,
- optional restart imports,
- centroid extraction.

## 20. Common troubleshooting

### Input folder does not exist

Check:

```wl
DirectoryQ[fileFolder]
```

and verify `imageFolder` and `subFolder`.

### No TIFF files found

The active raw-file discovery pattern is:

```
*.tif
```

Check the actual extension and folder level.

### Wrong run selected

Inspect the run registry and change the integer `runIndex`.

### A path works on another PC but not this one

Common causes:

- OneDrive folder not synced locally,
- different account-specific path prefix,
- excessive Windows path depth,
- permissions,
- changed experiment folder structure.

### `ColorNegate::imginv` or background-correction failures

Check that:

- imported sequence elements are `Image` objects,
- `filteredImages` contains images,
- every selected `meanCorrectionIntervals` span is nonempty,
- each calculated mean image is an `Image`.

### Later Mathematica version gives slightly different masks

First distinguish:

- small numerical/thresholding version drift,
- parameter changes,
- genuine algorithm changes.

The historical reference was produced under Mathematica 12.1.1 on Windows.
