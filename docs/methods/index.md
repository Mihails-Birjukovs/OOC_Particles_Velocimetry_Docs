# Processing methods

The validated v5.2 pipeline takes acquired TIFF images through the following stages:

```text
Run discovery → final-page TIFF import → crop
  → temporal projections (diagnostics)
  → morphological top-hat
  → temporal background correction
  → particle contrast enhancement
  → histogram matching
  → persistent-artifact suppression + frame-wise segmentation
  → small-component removal → particle centroids
  → processing metadata and optional exports
```

## Scientific boundaries

The persistent-artifact segmentation is deliberately fixed to `MorphologicalBinarize[..., Method -> "Entropy"]` while the particle-frame segmentation method remains selectable. Preserve this distinction when comparing methods or porting the workflow.

The notebook provides detection coordinates; it does not claim to implement the historical unimplemented MNNT trajectory-tracking placeholders.

The [full methods guide](../reference/METHODS.md) explains each stage, current parameters, and Wolfram-version sensitivity. [First-run instructions](../tutorials/first-run.md) give the execution order.

## Extended scientific guides

- [Illustrated processing pipeline](../pipeline/index.md)
- [Actual v5.2 processing parameters](../reference/parameters.md)
- [Annotated Wolfram Language Input cells](../reference/wolfram-examples.md)
- [Runnable synthetic sequence](../tutorials/synthetic-sequence.md)
- [Real Run 1 reproducibility case](../tutorials/real-run1.md)
