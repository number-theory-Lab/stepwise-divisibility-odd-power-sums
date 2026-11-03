# Stepwise Divisibility of Odd Power Sums

**Classification, Minimal Scaling and Prime-Factor Criteria**  
โครงงานคณิตศาสตร์เชิงทฤษฎีและการตรวจเชิงคำนวณ

> **Release status: pre-publication package.** Replace every author placeholder and complete `PREPUBLICATION_CHECKLIST.md` before creating a public release. No DOI has been assigned yet, and this package does not claim peer review or established worldwide novelty.

## Author / ผู้จัดทำ

- Author: **[REPLACE WITH AUTHOR NAME]**
- Affiliation: **[OPTIONAL — ADD ONLY WITH PERMISSION]**
- Corresponding contact: **[OPTIONAL — USE A SAFE PUBLIC CONTACT METHOD]**

Do not publish a home address, personal phone number, private email, student ID, class schedule, signature, or other sensitive personal information. A student should review public-release decisions with a teacher or parent/guardian.

## Abstract (English)

This project studies divisibility of odd-power sums over the arithmetic progression \(d,2d,\ldots,nd\), where \(n\geq 2\), \(d\) is a positive even integer, and \(k\geq 3\) is odd. Let \(P_k(n)=\sum_{j=1}^{n}j^k\), \(S_k(n,d)=d^kP_k(n)\), \(r=\min\{n,(k-1)/2\}\), and \(D_r(n,d)=d^r n(n-1)\cdots(n-r+1)\). The report proves the universal classification that \(D_r(n,d)\mid S_k(n,d)\) for every positive even \(d\) and every odd \(k\geq3\) if and only if \(n\in\{2,3,5\}\).

The report also presents: (D) a necessary odd-prime criterion for the least admissible starting value; (A) a finite formula for the least admissible even integer \(d^*(n)\); (B) a finite Carmichael-period certificate for checking all odd exponents; and (C) a prime-adic criterion for the actual maximal depth \(H(n,d,k)\). The accompanying Python program uses exact integer arithmetic to reproduce the finite checks stated in the report. These computational checks support reproducibility over the stated ranges; they do not replace the general proofs.

## บทคัดย่อ (ภาษาไทย)

โครงงานนี้ศึกษาการหารลงตัวของผลบวกกำลังคี่ของลำดับเลขคณิต \(d,2d,\ldots,nd\) เมื่อ \(n\geq2\), \(d\) เป็นจำนวนเต็มบวกคู่ และ \(k\geq3\) เป็นจำนวนเต็มคี่ กำหนด \(P_k(n)=\sum_{j=1}^{n}j^k\), \(S_k(n,d)=d^kP_k(n)\), \(r=\min\{n,(k-1)/2\}\) และ \(D_r(n,d)=d^r n(n-1)\cdots(n-r+1)\) รายงานพิสูจน์การจำแนกแบบสากลว่า \(D_r(n,d)\mid S_k(n,d)\) สำหรับทุก \(d\) คู่บวกและทุก \(k\) คี่ตั้งแต่ 3 ก็ต่อเมื่อ \(n\in\{2,3,5\}\)

ผลต่อยอดประกอบด้วยเกณฑ์จำนวนเฉพาะคี่ที่จำเป็น (D), สูตรจำกัดขั้นสำหรับค่าเริ่มต้นต่ำสุด \(d^*(n)\) (A), ใบรับรองคาบ Carmichael สำหรับตรวจทุกเลขชี้กำลังคี่ (B) และเกณฑ์จำนวนขั้นสูงสุดจริง \(H(n,d,k)\) (C) โปรแกรม Python ใช้การคำนวณจำนวนเต็มแบบ exact arithmetic เพื่อทำซ้ำการตรวจเชิงคำนวณตามช่วงที่ระบุในรายงาน การตรวจเหล่านี้ไม่ใช่สิ่งทดแทนบทพิสูจน์ทั่วไป

## Main files

| File | Description |
|---|---|
| `staircase_verification.py` | Python verification program extracted from Appendix B of the report. |
| `report/Stepwise_Odd_Power_Sums_Report_TH.pdf` | PDF report for reading and citation. |
| `report/Stepwise_Odd_Power_Sums_Report_TH.docx` | Editable Word source. Review for personal information before public release. |
| `LICENSE` | MIT License for the Python software only. |
| `LICENSE-REPORT.md` | Proposed CC BY 4.0 license for the report text and document, subject to author confirmation and third-party-rights review. |
| `.zenodo.json` | Zenodo metadata template. Replace the creator placeholder before releasing. |
| `CITATION.cff` | GitHub citation metadata template. Replace the author placeholder. |
| `TEST_RESULTS.txt` | Output summary from a local run of the supplied Python script. |
| `AI_USE_AND_CONTRIBUTIONS.md` | Suggested transparent disclosure of AI-assisted preparation. |

## Reproducibility

### Requirements

- Python 3.9 or newer
- Python standard library only; no third-party packages are required

### Run

From the repository root:

```bash
python staircase_verification.py
```

The program prints a dictionary of the reproduced checks and several examples. It uses integer and modular arithmetic rather than floating-point approximations.

### Finite checks reproduced from the report

The bundled program was executed successfully in the preparation environment. It reproduced these counts:

| Check | Range / construction | Count |
|---|---|---:|
| Classification counterexamples | \(n=2,\ldots,100\), excluding \(2,3,5\); \(d=2\), with \(k=7\) for \(n=9\) and \(k=5\) otherwise | 96 |
| Sufficiency examples | \(n\in\{2,3,5\}\), 30 even values of \(d\), 100 odd exponents | 9,000 |
| Formula A checks | \(n=2,\ldots,100\), 100 odd exponents for each computed \(d^*(n)\) | 9,900 |
| Direct supplementary checks for B examples | Five listed \((n,d^*(n))\) pairs, \(k=3,5,\ldots,1001\) | 2,500 |
| Maximal-depth table | \(n=5\), 10 even values of \(d\), 16 odd exponents | 160 |
| Candidate-divisor classification | Even divisors of \(\operatorname{lcm}(1,\ldots,n)\), \(n=2,\ldots,20\) | 3,207 total; 153 pass D; 147 satisfy the A criterion |

These are finite software checks, not independent proofs of statements quantified over all integers. In particular, the classification theorem and formula A rely on the mathematical arguments in the report.

## Scope and research-status statement

- The document itself states that global novelty has **not** been established and that the literature comparison is not an exhaustive survey.
- The finite program checks are limited to the ranges printed above.
- The report should receive an independent mathematical review, especially the valuation lemma and the proofs of results D and A, before being described as peer-reviewed or submitted as a validated result.
- Do not describe the repository timestamp or a DOI as proof that the mathematical ideas are globally original.

## Citation

Before release, update the author name in `CITATION.cff` and `.zenodo.json`. After Zenodo publication, add the actual version-specific DOI here. **No DOI is available at package-preparation time.**

Suggested citation before a DOI exists:

> [AUTHOR NAME]. (2026). *Stepwise Divisibility of Odd Power Sums: Classification, Minimal Scaling and Prime-Factor Criteria* (Version 0.1.0-prepublication). GitHub repository.

For formal citations, prefer the version-specific DOI assigned by Zenodo after publication. Zenodo also creates a concept DOI linking the versions; follow Zenodo's guidance on which identifier to cite.

## Licenses

- Python software: MIT License (`LICENSE`).
- Report/document: proposed Creative Commons Attribution 4.0 International (`LICENSE-REPORT.md`), only after the author confirms they have the rights to license the text and any included third-party material.
- Mathematical ideas, methods, and theories are not made exclusive by adding a software or document license. Licensing protects eligible expression and software; it does not itself establish novelty or confer a patent.
- For a mixed-license Zenodo deposit, select and declare both licenses in the Zenodo deposit interface where supported. Do not silently apply one license to every file.

## Zenodo from GitHub

1. Create the GitHub repository and upload this package's contents.
2. Replace all author placeholders and complete `PREPUBLICATION_CHECKLIST.md`.
3. Connect GitHub to Zenodo, then enable this repository in Zenodo's GitHub settings.
4. Create a GitHub release (for example, tag `v0.1.0`). Zenodo can archive new releases from an enabled repository.
5. Review Zenodo's metadata and file licenses before publishing. Confirm creators, title, description, language, keywords, and mixed licenses.
6. Publish only after all details are correct. Zenodo assigns DOI(s) when the record is published; do not invent or pre-fill a DOI.

See the official guides:
- [Zenodo: enable a GitHub repository](https://help.zenodo.org/docs/github/enable-repository/)
- [Zenodo: `.zenodo.json` metadata](https://help.zenodo.org/docs/github/describe-software/zenodo-json/)
- [Zenodo: licenses and rights](https://help.zenodo.org/docs/deposit/describe-records/licenses/)
- [Zenodo: DOI versioning](https://zenodo.org/help/versioning)
- [GitHub: creating releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)

## Acknowledgment and AI-use disclosure

See `AI_USE_AND_CONTRIBUTIONS.md`. Adapt it to accurately describe who did the mathematical work, who wrote and tested the program, and what AI tools assisted with. Do not claim that the student independently authored material that was substantially generated by a tool or another contributor.
