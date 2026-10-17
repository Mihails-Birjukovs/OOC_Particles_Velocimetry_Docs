# Validation and reproducibility

The current release is **OOC Particle Flow v5.2**, a filename/title promotion of the v5.1 notebook whose executable Input cells were validated in Windows Mathematica 12.1.1.

## Established results

| Evidence | Accepted result |
| --- | --- |
| Raw final-page TIFF to historical cropped image | **100/100** exact uint16 pixel matches |
| Run 1 / Run 2 / Run 3 plotted particle counts | **99/99** independently available vertices matched |
| Complete Run 2 count series | **21,322** detections across 100 frames, including frame 28 = 207 |
| Notebook structure QA | **16/16** passed |
| Actual processing-cell synthetic QA | **7/7** passed |
| Metadata-export QA | **6/6** passed |
| On-PC Run 3 | 100 frames processed; verified **17-field** record under Windows Mathematica 12.1.1 |

The PDF graphs simplify one collinear point and do not independently plot frame 28; its value comes from the saved Run 2 notebook.

## Limits of the evidence

Matching component counts **does not prove** identity of enhanced pixels, binary-mask pixels, or individual centroid coordinates. Additional paired native outputs would be required for those stronger comparisons. The smoke and structure checks were performed in a connected Wolfram kernel and do not replace the separate Windows run.

The full source validation notes are maintained with the private repository and should be read when assessing numerical or scientific-method changes.
