# OOC Particle Velocimetry — Public Documentation

This repository publishes the **Zensical documentation website** for the validated **OOC Particle Flow v5.2** Mathematica/Wolfram Language particle-image processing framework.

**Documentation site:** https://mihails-birjukovs.github.io/OOC_Particles_Velocimetry_Docs/

The source-code repository (`Mihails-Birjukovs/OOC_Particles_Velocimetry`) remains **private**. This public documentation repository intentionally contains **no notebook code**, experimental TIFF files, processed archive payloads, raw data, or measurement fixtures. The publicly reviewed pages explain methods, use, validation scope and licensing.

## Content

- [Getting started](docs/getting-started/index.md) and [first-run tutorial](docs/tutorials/first-run.md)
- [Methods](docs/methods/index.md) and detailed [algorithm reference](docs/reference/METHODS.md)
- [Full usage reference](docs/reference/USAGE.md)
- [Examples](docs/examples/index.md) and [validation](docs/validation/index.md)
- [Licensing and dataset permissions](docs/licensing/index.md)

## Build locally

Install Python 3.12+ and Zensical, then run:

```bash
python -m pip install zensical
python scripts/validate_public_docs.py
zensical serve
```

The strict build command used by CI is `zensical build --clean --strict`. GitHub Actions builds pull requests and publishes merged `main` updates through GitHub Pages when the repository has **Settings → Pages → Source → GitHub Actions** configured.

## Maintenance and provenance

The approved documentation originates from the private source repository's `site-content/` plus two curated references, `docs/USAGE.md` and `docs/METHODS.md`. Changes are **reviewed and copied explicitly**; there is no connector or GitHub Action with access to private source material from this public repository.

See [MAINTAINING.md](MAINTAINING.md) for the one-to-one source mapping and publication rules.

## License

Original software documentation in this public repository is available under the [MIT License](LICENSE), © 2026 Mihails Birjukovs. **The license does not cover experimental data**, which are not distributed here.
