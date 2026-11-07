# A strong Lefschetz family among equigenerated monomial almost complete intersections

**Author:** Ke-kuk Chow  
**Manuscript and GitHub distribution:** 7 November 2026.

[Read the seven-page paper (PDF)](chow-gln-support-three-lefschetz.pdf) · [Download the complete LaTeX source ZIP](chow-gln-support-three-lefschetz-source.zip) · [Browse the main source](main.tex) · [Verification code](verify.py)

## Status

This repository distributes an author-authorized research preprint, with its sources and auxiliary exact checks. It has **not been submitted to arXiv or a journal** and has not undergone external peer review. No arXiv identifier or manuscript DOI has been assigned. GitHub hosting does not constitute journal publication or arXiv acceptance.

The original PDF and source ZIP are preserved. Their bundled author-review notes record the preparation status; the author subsequently authorized this GitHub distribution.

## Precise result

For every characteristic-zero field $k$ and every integer $a\ge4$, the paper proves that

$$
A_a=k[x,y,z]/(x^a,y^a,z^a,x^{a-2}yz)
$$

has the **strong Lefschetz property**, with $L=x+y+z$. Thus every map $L^{j-i}:(A_a)_i\to(A_a)_j$, for $0\le i<j$, has maximal rank.

This establishes the **second positive infinite family** in Gasanova--Lundqvist--Nicklasson's Conjecture 1, using the numbering in arXiv:2006.14453v4, section 5.1. It does not establish the full conjectural classification or its exclusion of all other exponent patterns.

The proof uses an actual module extension, reduces all possible rank conflicts to two maps, and explicitly proves that the two connecting maps are nonzero. It also establishes that the endpoint sums of the actual graded Jordan intervals belong to $\{3a-5,3a-4\}$.

As a corollary, SLP persists after adjoining arbitrary truncated polynomial variables. This includes the arbitrary-variable expectation preceding the original conjecture. The corollary uses the established almost-centered tensor mechanism; the manuscript attributes that machinery and supplies a self-contained proof for the endpoint condition used here. No positive-characteristic classification is claimed.

## Relation to earlier work

The manuscript distinguishes the support-three family above from the support-two family already proved by Gasanova, Lundqvist and Nicklasson, and from subsequent support-two and symmetric-Hilbert-series results. It credits the classical monomial-complete-intersection lowering operator, graded Jordan decomposition and tensor theory. Its specific calculation concerns the actual connecting maps, rather than treating a Hilbert-function splitting as an operator splitting.

- Gasanova, Lundqvist and Nicklasson, *On decomposing monomial algebras with the Lefschetz properties*: [arXiv:2006.14453v4](https://arxiv.org/html/2006.14453v4#S5.SS1), [DOI](https://doi.org/10.1016/j.jpaa.2021.106968).
- Chase and Jonsson Kling, *The strong Lefschetz property for some monomial almost complete intersections*: [arXiv:2507.18516v1](https://arxiv.org/html/2507.18516v1), [DOI](https://doi.org/10.1007/s13348-026-00514-1).

The available literature review does not certify global priority. The exact theorem, proof and attribution should be assessed from the manuscript; this repository does not claim a complete solution of GLN Conjecture 1.

## Build the paper

The repository provides `main.tex`, `references.bib` and the prebuilt `main.bbl`. In this directory, or after extracting the source ZIP, run:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Alternatively use `latexmk -pdf main.tex`. The source requires standard LaTeX packages and no shell escape or external images. `SOURCE_README.txt` preserves the original preparation instructions.

## Reproduce the auxiliary checks

Requires Python 3 and its standard library only:

```text
python verify.py --output replay.json
```

Compare the parsed JSON with `verification.json`; see `VERIFICATION.txt`. The script checks 34 actual connecting-map certificates for $a=4,\ldots,20$ and all 334 degree-to-degree power maps for the five stated small parameter choices, using exact rational arithmetic in the original monomial coordinates. It also recovers the actual graded Jordan intervals.

The universal result rests on the mathematical proof, not finite checks. `SHA256SUMS` lists the distribution-file checksums. The original ZIP contains ancillary files under `anc/`; the same GLN-only verifier and results are also provided at the repository root for direct browsing.

## AI assistance

As disclosed in the paper, OpenAI Codex substantially assisted with mathematical derivations, drafting and computational checks. The AI system is not an author. This disclosure does not constitute external mathematical review or certification.

## Citation and reuse

Cite Ke-kuk Chow, *A strong Lefschetz family among equigenerated monomial almost complete intersections*, research preprint, 2026. `CITATION.cff` supplies machine-readable metadata. No open-source or Creative Commons license has been selected; public availability alone does not grant an additional reuse license.
