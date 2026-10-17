# Getting started

## Prerequisites

- Wolfram Mathematica / Wolfram Language **12.1 or newer**; the accepted full-data run used **12.1.1 on Windows**.
- Access to the software repository and its **`OOC_Particle_Flow_v5.2.nb`** notebook.
- The adjacent **`TemporalProjections_v1.1.0.wl`** helper package.
- A local DynamicStudio-compatible TIFF sequence to analyze.

The project's GitHub repository is currently private. The public documentation site does **not** distribute the executable notebook or experimental datasets.

## Arrange the files

```text
OOC_Particles_Velocimetry/
├── OOC_Particle_Flow_v5.2.nb
└── TemporalProjections_v1.1.0.wl
```

Place both files in the same directory, or adjust `packageDirectory` in the notebook intentionally. Open the notebook in Mathematica and evaluate **Initialization** followed by **Core Functions**.

## Configure one acquisition

In **Import Images**, set `imageFolder` and `subFolder` to the location of your input TIFFs. Evaluate run discovery, inspect `runRegistry`, and select a numeric `runIndex`. The preflight validator checks existence and warns about problematic long paths.

Continue with the [first-run tutorial](../tutorials/first-run.md), or consult the [complete usage reference](../reference/USAGE.md) for every stage and restart point.

## Reproducibility note

Do not re-use a saved `ProcessingParameters.wl` from a different session. After establishing numeric crop bounds and a histogram-reference index, evaluate the processing-record cell to write and round-trip-verify the record for the current run.
