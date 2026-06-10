# P vs NP — Study Notes and an Annotated Map

Self-study materials on computational complexity, produced during an extended dialogue with an AI assistant (Anthropic's Claude) and organized as a learning map toward the research frontier — posted publicly for corrections, suggestions, and anyone walking a similar path.

## Honest framing — read this first

- **What this is:** study notes, an expository survey, and one clearly labeled speculative chapter. A second-year CS student's learning map, co-written with an AI.
- **What this is not:** a claim of new results, and emphatically **not** a proof or attack on P vs NP.
- **Verification status:** citations were generated from the AI's memory. Bibliography entries marked **[verified 2026-06]** were checked against DBLP/publisher records; all others should be treated as unverified. The survey's final chapter carries an explicit verification checklist (§10.9) tracking exactly what remains to be checked. Corrections via issues are very welcome — that is the main reason this is public.
- **Epistemic tiers:** the speculative chapter labels every claim **[T1]** (proved in the document, elementary, self-contained), **[T2]** (cited from literature, parameters hedged), or **[T3]** (conjecture/speculation, possibly false, possibly already known).

## Contents

| Path | Description |
|---|---|
| `survey/p-vs-np-corridor.md` | *The Narrow Corridor* — a survey: a fully rigorous proof of the Cook–Levin window lemma, the complete SAT reduction, the barrier theorems, the live research programs (meta-complexity, hardness magnification, the algorithmic method), the TC⁰ frontier, and a final speculative chapter formulating the **Domain Condensation Conjecture** with full proofs of its elementary lemmas. |
| `notes/theory-of-computation-notes.md` | Self-study companion for Sipser's *Introduction to the Theory of Computation*: study method, per-chapter proof tricks and exercise lists, common pitfalls, checkpoints, and a 14-week schedule. |
| `survey/src/`, `notes/src/` | Pandoc-dialect sources of the same documents, for LaTeX/PDF conversion. The top-level copies use GitHub's math dialect so they render in the browser. |
| `convert.py` | Sync script: edit only the files under `src/`, then run `python3 convert.py` to regenerate the display copies. |

## Reading order

1. Learning the basics: start with `notes/`, alongside Sipser.
2. Know Cook–Levin already: read `survey/` Chapters 1–2 for the window lemma at full rigor, then Chapters 3–8 for the map of the frontier.
3. Chapter 10 (Domain Condensation) is for readers who know the meta-complexity literature — especially anyone who can answer its §10.9 checklist. If a lemma there is known folklore, please open an issue saying so; that is precisely the feedback sought.

## Converting to LaTeX

From the `src/` copies: `pandoc survey/src/p-vs-np-corridor.md -o corridor.tex` (or `-o corridor.pdf` with a LaTeX toolchain).

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — share and adapt with attribution. See `LICENSE`.
