A strong Lefschetz family among equigenerated monomial almost complete intersections
Author: Ke-kuk Chow
Prepared: 7 November 2026

STATUS
Research manuscript prepared for author review. Not submitted to arXiv or a
journal. No arXiv identifier or manuscript DOI has been assigned. The author
name is the only personal information provided; no affiliation or email has
been invented. Global priority and external peer review are not certified.

EXACT SCOPE
For characteristic-zero fields and a>=4, the paper proves SLP of
k[x,y,z]/(x^a,y^a,z^a,x^(a-2)yz). This is the second positive infinite
family of GLN Conjecture 1 in arXiv:2006.14453v4, not the entire iff
classification. The arbitrary-extra-CI conclusion is a corollary of the
proved endpoint control and the standard almost-centered tensor mechanism.
The proof is self-contained, with prior general machinery attributed.

CONTENTS
main.tex           Main manuscript.
references.bib     Editable bibliography.
main.bbl           Prebuilt bibliography for arXiv processing.
anc/verify.py      Exact original-coordinate verification script.
anc/verification.json  Recorded finite verification results.
anc/README.txt     Instructions and the boundary of the computations.

BUILD
Use pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX, inside this directory:
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  bibtex main
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
Alternatively use latexmk -pdf main.tex.
No shell escape, external figure, custom style file, network download or
nonstandard font is required on a normal TeX Live installation.

AI ASSISTANCE
The manuscript discloses substantial assistance from OpenAI Codex for
derivations, drafting and computational checks. AI is not an author.
The author should review the entire manuscript before public submission.

SUBMISSION
Suggested primary arXiv category: math.AC. Preparation does not select an
arXiv license, satisfy endorsement, or constitute submission. The author
retains the decision about public release and journal submission.
