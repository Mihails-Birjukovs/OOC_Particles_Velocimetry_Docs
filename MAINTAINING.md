# Maintaining the public OOC documentation

## Authoritative sources and safe publication boundary

The private `Mihails-Birjukovs/OOC_Particles_Velocimetry` repository is the authoritative development and scientific documentation source. This public repository is a **reviewed snapshot** of only the approved documentation pages.

| Private source path | Public destination |
| --- | --- |
| `site-content/index.md` | `docs/index.md` |
| `site-content/getting-started/index.md` | `docs/getting-started/index.md` |
| `site-content/tutorials/first-run.md` | `docs/tutorials/first-run.md` |
| `site-content/methods/index.md` | `docs/methods/index.md` |
| `site-content/examples/index.md` | `docs/examples/index.md` |
| `site-content/validation/index.md` | `docs/validation/index.md` |
| `site-content/licensing/index.md` | `docs/licensing/index.md` |
| `docs/USAGE.md` | `docs/reference/USAGE.md` |
| `docs/METHODS.md` | `docs/reference/METHODS.md` |

These nine pages formed the initial publication allowlist. The expanded science pages are maintained alongside them in the private source repository, with an explicitly updated allowlist and Zensical navigation. The pipeline SVG is an original schematic; experimental imagery remains under separate rights review. New content requires explicit scientific/privacy review and changes to `scripts/validate_public_docs.py` and `zensical.toml`.

## Updating the site

1. Edit and review the authoritative documentation in the private repository.
2. Select only approved public pages; do **not** clone the entire private `docs/` tree into this public repository.
3. Update the corresponding destination page here. Keep private notebooks, lab paths, personal data and third-party/dataset material out.
4. Run `python scripts/validate_public_docs.py` and `zensical build --clean --strict`.
5. Open a PR in this public repository. GitHub Actions checks the build without deploying a PR.
6. Merge only after review. Pushes to `main` trigger GitHub Pages publication (after Pages is enabled in Settings).

The two repositories deliberately do **not** share workflow credentials or automate private-source access. This prevents accidental transfer of unreviewed research material.

## Data and code licensing

This public repo includes only original public documentation under the MIT license. Experimental acquisitions, segmentation images, centroid fixtures and processed archives remain outside this publishing workflow and require separate licensing/permissions decisions.

## Initial migration

The first public version was prepared from the private repository's Zensical foundation, merged in private PR #7 on 2026-10-17. The site's `site_url`, document root, and publishing workflow were adapted for the new public-repository URL.

## Extended science pages

The private source copies for `pipeline/index.md`, `assets/pipeline-v5.2.svg`, `reference/parameters.md`, `reference/wolfram-examples.md`, `tutorials/synthetic-sequence.md`, and `tutorials/real-run1.md` live under `site-content/` and map to equivalent paths under the public `docs/` tree. Only reviewed text and original diagrams cross this boundary.
