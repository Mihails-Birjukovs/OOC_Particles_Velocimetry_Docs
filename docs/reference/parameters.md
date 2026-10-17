# Processing parameter reference — OOC v5.2

These controls are taken from the **validated v5.2 notebook**. Recorded Run 3 values and defaults are distinguished below.

| Parameter | Notebook assignment | Scientific role |
| --- | --- | --- |
| `imageFolder` / `subFolder` | User-specific root and relative subfolder | Build input path via `FileNameJoin` |
| `runIndex` | Initially `1` | Integer index into discovered `runRegistry`, not a run name |
| `runIdentifier` | Derived from registry | Exact run prefix used to filter frame filenames |
| `selectedImages` / `imageIndices` | `1 ;; All` / `1 ;; All` | Select frames before / during cropping |
| `rowRange` / `columnRange` | Initially full image, then interactive selector | Numeric bounds for `ImageTake`; validate before export |
| `topHatScale` | **5** | `DiskMatrix` spatial scale for morphological top-hat |
| `meanCorrectionIntervals` | `{1 ;; All}` | Per-interval temporal mean backgrounds; nonempty, ordered, complete spans |
| `useFlatCorrection` | **0** | 0 = subtractive; 1 = flat-field-style division |
| `maxFilterScale` | **1** | Local `MaxFilter` scale in the CNR enhancement |
| `referenceFrameThreshold` | **0.05** | Eligibility threshold for first histogram reference frame |
| `referenceFrameIndex` | **Calculated** | First frame satisfying standardized mean-luminance criterion; never assume it equals 1 |
| `segmentationMethod` | **"Entropy"** | Per-frame `Binarize`; alternative `"MinimumError"` is retained |
| `particleSizeThreshold` | **5** | Removes components of 1–5 pixels |
| Artifact-mask segmentation | Fixed **"Entropy"** | `MorphologicalBinarize` on temporal mean of matched enhanced images; **independent** of `segmentationMethod` |

## Diagnostics and optional controls

| Control | Notebook value | Description |
| --- | --- | --- |
| `rotationSwitch`, `rotationAngle` | `0`, `Pi/2` | Viewing/utility rotation; processing images are not rotated automatically |
| `checkupIDs`, `chunkCountProjection` | `1 ;; All`, 2 | Temporal projection diagnostic selection and chunk size |
| `maskCheckupIDs`, `maskChunkCountProjection` | `1 ;; All`, 2 | Mask diagnostic projection selection and chunk size |
| `detectChannelWalls` | 0 | Optional wall detector not active by default |
| `notebookID` | 2 | Saved notebook/PDF suffix, not a scientific threshold |

`TemporalProjections` calls set `"WorkingType" -> "Real32"`, `"StandardDeviationConvention" -> "Sample"` and `"ShowProgress" -> True`.

## What did the accepted Run 3 actually use?

Native Windows Mathematica 12.1.1 recorded a 100-frame run with full-field crop bounds `{0,1024}` / `{0,1344}` and histogram reference **frame 12**. These were **evaluated per-run values**, not universally recommended crop settings. The verified `ProcessingParameters.wl` association contains 17 fields.

For a new acquisition, inspect and re-evaluate all crop, correction, and histogram-reference variables. The processing-record exporter rejects symbolic crop bounds and an invalid reference-frame index.

See [annotated WL examples](wolfram-examples.md), [illustrated pipeline](../pipeline/index.md), and [full usage guide](USAGE.md).
