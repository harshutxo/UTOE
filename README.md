# UTOE: Universal Theory of Everything

**Randomness, Chaos and the Infinite Within**, by Harsh Goyal.

UTOE follows one principle across physics, biology, mind and society: small
differences, amplified by nonlinear dynamics, decide the outcome, and the
structures that last are those whose maintenance outweighs their decay. It is
not a physicists' theory of everything (it unifies no forces); it is a
cross-scale framework with a concrete experimental test.

## Contents

| File | What it is |
|---|---|
| `UTOE-Universal-Theory-of-Everything.pdf` | The main paper (built from `toe-merged.md`) |
| `Heavy-Water-Experiment.pdf` | Protocol and simulation results for the heavy-water test (built from `heavy-water-experiment.md`) |
| `heavy_water/simulate.py` | Simulation of the experiment: data generation, analysis and power analysis |
| `heavy_water/*.png`, `results.json` | Simulation outputs |
| `build_pdf.py` | Builds a PDF from a Markdown source (KaTeX math, headless Chrome) |
| `.katex/` | Local copy of KaTeX 0.16.11 so builds work offline |
| `quantum-randomness-and-chaotic-amplification.md`, `Quantum-Randomness-and-the-Infinite-Within.pdf` | Earlier single-topic draft |
| `1753232722188.pdf` | Original 2025 paper, *Theory of Everything and Quantum-Driven Social Evolution* |
| `Harsh_Goyal_Emergent_Reality_Framework.pdf` | Earlier notes on the emergent reality framework |

## The heavy-water experiment in one paragraph

If some mutations come from protons tunneling across DNA base pairs, growing
cells in heavy water (D₂O) should suppress them, because deuterium tunnels
about 300 times less. The experiment measures how the ratio of transitions
(which tunneling causes) to transversions (which it does not) changes with the
D₂O fraction, in 900 mutation-accumulation lines of mismatch-repair-deficient
*E. coli*. The simulation shows this detects a 10% quantum share with 85% power
at a 5% false-positive rate, and that an in vitro kinetics experiment is needed
to rule out a classical look-alike.

## Rebuilding

```
pip install numpy scipy matplotlib markdown
python heavy_water/simulate.py                                          # simulation, figures, results.json
python build_pdf.py                                                     # main paper
python build_pdf.py heavy-water-experiment.md Heavy-Water-Experiment.pdf
```

`build_pdf.py` expects Google Chrome at its default Windows location.
