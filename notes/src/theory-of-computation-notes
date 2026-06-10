# Theory of Computation — Self-Study Notes

*Companion notes for a first pass through the theory of computation, written for a student who has completed discrete mathematics and linear algebra and is working through Velleman's* How to Prove It. *Primary textbook: Sipser,* Introduction to the Theory of Computation *(3rd ed.). These notes are a map and a coach, not a replacement for the book — the book has the full proofs and, crucially, the exercises.*

---

## How to use these notes

1. **The exercises are the course.** Reading theory feels like progress; it mostly isn't. The ratio to aim for is roughly 30% reading, 70% solving. After each Sipser section, do the recommended problems below *before* looking at any solutions. Being stuck for 30–60 minutes on a problem is not failure — it is the mechanism by which the material installs itself.
2. **Reprove the theorems.** After reading a proof, close the book and reproduce it on paper from the idea alone. If you can't, you read it; you didn't learn it. The proofs in this subject are a small toolbox of tricks (simulation, diagonalization, pumping, reduction) used over and over — your goal is to own the tricks, not memorize the instances.
3. **Definitions are exact or they are nothing.** Half of all beginner errors are imprecise definitions. When you define a DFA or a reduction, every quantifier matters. Velleman has trained you for exactly this; apply it ruthlessly.
4. **Keep an error log.** Every time you get an exercise wrong or a proof has a gap, write one line: what you believed, why it was false. Review the log weekly. This single habit roughly doubles retention.
5. **Checkpoints.** Each part below ends with a self-test: "you are ready to move on when..." Take them seriously; the subject is cumulative.

---

## Part 0 — Prerequisites in active use

You already have these; here is what the course will actually demand of each.

- **Sets, functions, relations:** alphabets $\Sigma$, strings $\Sigma^*$, languages $L \subseteq \Sigma^*$. A *language* is just a set of strings; "decide a language" means "compute its membership function." Internalize that problems = languages.
- **Induction:** structural induction on strings and on grammar derivations will be your daily bread. Practice: prove that every string in $\{a,b\}^*$ with equal counts of $a$ and $b$... etc. — Sipser Ch. 0 problems.
- **Proof by contradiction and contrapositive:** the pumping lemmas and all undecidability proofs are contradictions. Velleman Ch. 3 is the relevant training.
- **Counting and pigeonhole:** finite automata arguments are pigeonhole arguments in disguise.
- **Diagonalization:** if you have seen Cantor's proof that $\mathbb{R}$ is uncountable, you have seen the single most important proof technique in this subject. If not, read it now (Sipser §4.2 covers it); the halting problem is the same proof wearing a different costume.

---

## Part I — Finite automata and regular languages (Sipser Ch. 1)

### I.1 The objects

- **DFA** $M = (Q, \Sigma, \delta, q_0, F)$: finite states, deterministic transition function $\delta : Q \times \Sigma \to Q$. The machine *has no memory beyond its current state* — this is the entire point of the model.
- **NFA**: $\delta : Q \times \Sigma_\varepsilon \to \mathcal{P}(Q)$; accepts if *some* computation path accepts. Nondeterminism = existential guessing. This is your first encounter with the concept that will later define NP; pay attention to how it feels.
- **Regular expressions**: the algebraic syntax for the same class.

### I.2 The theorems that matter, with their proof ideas

1. **NFA = DFA (subset construction).** Idea: a DFA can track the *set* of states the NFA could be in. Cost: $2^{|Q|}$ states. *Trick learned: simulation — one machine pretends to be another.* This trick reappears in every chapter of the subject, all the way up to the universal Turing machine and Cook–Levin.
2. **Regular expressions = automata.** Idea: induction on regex structure (one direction); state elimination / GNFA (the other). *Trick learned: syntax ↔ machine translations.*
3. **Pumping lemma.** Every regular language $L$ has a pumping length $p$: any $s \in L$ with $|s| \ge p$ splits as $s = xyz$ with $|xy| \le p$, $|y| \ge 1$, and $xy^iz \in L$ for all $i \ge 0$. Idea: pigeonhole on states — a long string must revisit a state, and the loop can be pumped. *Trick learned: finiteness forces repetition.*
   - **The #1 beginner error:** the pumping lemma gives *you* the string $s$ to choose, but the *adversary* chooses the split $xyz$. Your proof must defeat **every** legal split, not exhibit one bad split. Write pumping proofs as games: "Adversary picks $p$. I pick $s = \ldots$. For **any** split with $|xy| \le p$, $y$ consists only of ..., so pumping gives ... $\notin L$."
4. *(Optional but recommended)* **Myhill–Nerode.** $L$ is regular iff the relation "$x \equiv_L y$ iff no suffix distinguishes them" has finitely many classes. Cleaner than pumping for many non-regularity proofs, and the right way to *think* about what a state is: a state is an equivalence class of pasts.

### I.3 Exercises (Sipser 3rd ed.)

Minimum set: 1.4 (a,c,e), 1.5 (a,c), 1.7, 1.16, 1.21, 1.29 (pumping practice), 1.31, 1.36, 1.46. Stretch: 1.63, 1.51 (Myhill–Nerode).

### I.4 Checkpoint

You are ready to move on when you can: design a DFA/NFA for a verbal spec in minutes; convert NFA→DFA mechanically; run the pumping game correctly on $\{0^n1^n\}$ and on $\{ww^R\}$; and explain in one sentence why "finite memory" and "regular" are the same idea.

---

## Part II — Context-free languages (Sipser Ch. 2)

*Strategic note: if your goal is the complexity-theory ladder, this part can be done at 70% depth. It matters for parsing and for the cultural literacy of the field, but the road to P vs NP runs through Parts III–IV. Do not stall here.*

- **CFGs**: rules $A \to w$; derivations; parse trees; ambiguity. Languages of nested/recursive structure: $\{0^n 1^n\}$, balanced parentheses, most programming-language syntax.
- **PDAs**: NFA + one stack. Theorem: CFG = PDA (read the construction; reproducing it from scratch is optional).
- **CFL pumping lemma**: long strings pump as $uvxyz$ with $v, y$ pumped together. Use it on $\{a^n b^n c^n\}$ — the canonical non-CFL — and understand *why* one stack can match two blocks but not three.
- **Closure facts** worth memorizing: CFLs closed under union, concatenation, star; **not** closed under intersection or complement (use $\{a^nb^nc^m\} \cap \{a^mb^nc^n\}$).

Exercises: 2.4, 2.6 (a,b), 2.9, 2.16, 2.17, 2.30 (a,b), 2.31. Checkpoint: you can write grammars from specs, and you can articulate exactly what a stack can and cannot remember.

---

## Part III — Computability (Sipser Ch. 3–5) — *the heart of the subject*

### III.1 The Turing machine and the Church–Turing thesis (Ch. 3)

- **The model**: finite control + infinite tape + head. Configurations, the yields relation, acceptance. *You have already seen this formalized with unusual rigor if you have read the companion document's Chapter 1 — the configuration strings $\#\,u\,q\,a\,v\,\#$ there are exactly Sipser's.*
- **Robustness**: multitape = single tape (quadratic slowdown); nondeterministic TM = deterministic TM (exponential slowdown — *remember this asymmetry; it is the embryo of P vs NP*). The model doesn't care about bells and whistles. That robustness is the evidence for:
- **Church–Turing thesis**: "algorithm" = "Turing machine." Not a theorem — a definition justified by a century of every proposed model coinciding. From Ch. 4 on, Sipser writes algorithms in prose; your job is to trust, and occasionally spot-check, that the compilation to TMs is routine.
- **Key vocabulary**: *decidable* (TM halts on all inputs with the right answer) vs. *Turing-recognizable* (TM accepts members; may loop on non-members). The gap between these two is where all the drama lives.

### III.2 Decidability and the first impossibility (Ch. 4)

- Decidable examples: $A_{\mathsf{DFA}}$, $E_{\mathsf{DFA}}$, $A_{\mathsf{CFG}}$ — get fluent with "language about machines" notation; the objects of study are now themselves inputs.
- **The universal TM**: a TM $U$ that simulates any TM from its description. Philosophically: software. Technically: the simulation trick at full power.
- **Diagonalization and $A_{\mathsf{TM}}$**: the halting/acceptance problem is undecidable. The proof is Cantor's diagonal: assume decider $H$, build $D$ that runs $H$ on $\langle M, \langle M \rangle\rangle$ and does the opposite, run $D$ on itself, contradiction. **Memorize this proof until you can produce it cold.** It is four lines and it is the foundation stone of the entire negative side of computer science.
- $A_{\mathsf{TM}}$ is recognizable but not decidable; its complement is not even recognizable. Theorem: decidable = recognizable ∧ co-recognizable.

### III.3 Reducibility (Ch. 5) — *the most important skill in the book*

- **The schema**: to prove $B$ undecidable, show "a decider for $B$ would yield a decider for $A_{\mathsf{TM}}$." You construct, from input $\langle M, w\rangle$, an instance of $B$ whose answer reveals whether $M$ accepts $w$. The construction usually builds a *new machine* $M'$ whose behavior is rigged.
- **The #1 beginner error here:** direction confusion. To prove $B$ is hard, reduce the known-hard problem **to** $B$ (hard $\le$ B), never $B$ to the hard problem. Tattoo this on the inside of your skull: *you use a solver for $B$ as a subroutine to solve the hard thing.* Every semester, half the class gets this backwards at least once.
- Practice targets: $\mathrm{HALT}_{\mathsf{TM}}$, $E_{\mathsf{TM}}$, $\mathrm{REGULAR}_{\mathsf{TM}}$, $EQ_{\mathsf{TM}}$.
- **Rice's theorem** (do the exercise version): *every* nontrivial property of the language of a TM is undecidable. After proving three reductions by hand, Rice's theorem is the pattern, extracted.
- **Mapping reducibility** $A \le_m B$: a computable $f$ with $x \in A \iff f(x) \in B$. This is the formal skeleton; in Part IV the same skeleton with a polynomial-time budget becomes the central tool of complexity theory. Same idea, new accounting.

### III.4 Exercises

Minimum: 3.5, 3.8, 4.3, 4.10, 4.12, 4.17, 5.1, 5.2, 5.4, 5.9, 5.10, 5.22, 5.28 (Rice). Stretch: 5.30, 5.35.

### III.5 Checkpoint

Ready to move on when: you can produce the $A_{\mathsf{TM}}$ diagonalization cold; you can design a rigged machine $M'$ for a new reduction without a template; you never confuse reduction direction (test: explain aloud why reducing $B$ to $A_{\mathsf{TM}}$ proves nothing about $B$'s hardness); and you can state precisely the difference between decidable and recognizable.

---

## Part IV — Complexity theory (Sipser Ch. 7–8) — *the destination*

### IV.1 Time complexity and P (Sipser §7.1–7.2)

- **Definitions**: running time of a TM; $\mathsf{TIME}(t(n))$; the class $\mathsf{P} = \bigcup_k \mathsf{TIME}(n^k)$. Why polynomial? Closure under composition (a poly-time algorithm calling poly-time subroutines stays poly-time) and model-independence (all reasonable deterministic models agree on P up to polynomial translation). P is not "fast"; P is "scalable in principle, robustly defined."
- Get fluent in analyzing simple algorithms as TMs at the level of "this is clearly polynomial" — the Church–Turing-style trust, with a budget.

### IV.2 NP, two equivalent ways (§7.3)

1. **Verifier definition**: $L \in \mathsf{NP}$ iff there is a poly-time verifier $V$ and polynomial $p$ with $x \in L \iff \exists w, |w| \le p(|x|), V(x,w)=1$. The string $w$ is the *certificate*.
2. **Machine definition**: $L$ is decided by a nondeterministic TM in polynomial time.

Prove their equivalence yourself (Sipser does; reproduce it). The verifier view is the one to internalize: **NP is the class of problems whose solutions are short and checkable.** Examples to hold in mind: SAT, CLIQUE, HAMPATH, SUBSET-SUM, COMPOSITES.

- $\mathsf{P} \subseteq \mathsf{NP}$ trivially. Whether the inclusion is strict is the P vs NP problem. Notice where the difficulty sits: to show $\mathsf{P} \ne \mathsf{NP}$ you must prove a *lower bound* — that no clever algorithm among infinitely many candidates works. Lower bounds against all algorithms are the hardest kind of statement in the field; the companion document's Chapters 3–7 are about exactly why.

### IV.3 Polynomial-time reductions and NP-completeness (§7.4–7.5)

- $A \le_p B$: mapping reducibility with a polynomial-time $f$. Same skeleton as Ch. 5; new budget. Same direction warning as Ch. 5 — it bites here even harder, because now it silently invalidates hardness proofs instead of loudly failing.
- **NP-complete** = in NP, and every NP problem reduces to it. The maximal difficulty class within NP: one efficient algorithm for one NP-complete problem collapses everything ($\mathsf{P} = \mathsf{NP}$).
- **Cook–Levin theorem**: SAT is NP-complete. Sipser's proof is the tableau argument — and here you hold an unusual advantage: *the companion document's Chapters 1–2 prove the window lemma (the step Sipser compresses) in complete detail.* Read Sipser §7.4 first, then the companion's version, then close both and reconstruct the whole proof: variables, the four formula parts, and why $2\times 3$ windows suffice. If you can do that, you understand Cook–Levin better than most graduating CS majors.
- **The reduction zoo** (§7.5): 3SAT, CLIQUE, VERTEX-COVER, HAMPATH, SUBSET-SUM. Each reduction is a gadget-engineering exercise. Do at least four end-to-end with full correctness proofs (both directions of the iff — another classic omission).
- **The #1 beginner error here:** proving only one direction of "$x \in A \iff f(x) \in B$." Half a reduction is zero reduction. Always write both directions explicitly, even when one is "obvious."

### IV.4 A taste of what's beyond (§7.5+, Ch. 8–9 selections)

- **coNP** and the asymmetry of certificates: short proofs of *yes* vs. short proofs of *no*. SAT vs. TAUTOLOGY. Open: $\mathsf{NP} \stackrel{?}{=} \mathsf{coNP}$.
- **Space** (Ch. 8, optional first pass): PSPACE, Savitch's theorem, $\mathsf{NL}$. Read for culture; return later.
- **Hierarchy theorems** (§9.1): more time provably buys more power — $\mathsf{TIME}(n) \subsetneq \mathsf{TIME}(n^3)$, etc., by diagonalization. These are among the very few unconditional separations we possess, and the nondeterministic version is the engine inside Williams' method (companion document, Chapter 6). Notice the irony early: diagonalization *works* for time hierarchies and *provably cannot* resolve P vs NP by itself (relativization — companion Chapter 3). Sitting with that tension is the beginning of research-level understanding.
- **Oracles and relativization** (§9.2): read the Baker–Gill–Solovay discussion after the hierarchy theorems; it closes the loop with the companion document's barrier chapter.

### IV.5 Exercises

Minimum: 7.6, 7.7, 7.9, 7.12, 7.21, 7.22, 7.24, 7.28, 7.36; then 9.13, 9.14 (hierarchy). Stretch: 7.45, 7.46, 8.10 (Savitch).

### IV.6 Checkpoint (= end of the book, Stage 1 complete)

Ready when you can: state both NP definitions and prove equivalence; produce the Cook–Levin proof in outline with the window lemma stated precisely; execute a novel NP-completeness reduction with a two-directional correctness proof; explain to a non-expert, accurately, what P vs NP asks and why it is hard to resolve; and prove the time hierarchy theorem's diagonalization.

---

## Suggested 14-week schedule (≈ 8–10 focused hours/week)

| Weeks | Material | Deliverable to yourself |
|---|---|---|
| 1 | Ch. 0 + proof warm-up | 10 solved problems; error log started |
| 2–3 | Ch. 1 automata | All Part I minimum exercises |
| 4 | Ch. 1 pumping + Myhill–Nerode | 5 clean non-regularity proofs |
| 5–6 | Ch. 2 CFLs (70% depth) | Part II exercises |
| 7 | Ch. 3 TMs, Church–Turing | Reproduce multitape simulation |
| 8 | Ch. 4 diagonalization | $A_{\mathsf{TM}}$ proof cold, on paper, twice |
| 9–10 | Ch. 5 reductions + Rice | 6 reductions end-to-end |
| 11 | §7.1–7.3 P and NP | Verifier ⇔ NTM proof reproduced |
| 12 | §7.4 Cook–Levin (+ companion Ch. 1–2) | Full proof reconstruction from memory |
| 13 | §7.5 NP-completeness zoo | 4 reductions with both directions |
| 14 | §9.1–9.2 hierarchies, oracles | Hierarchy proof + write a 1-page summary of what relativization means |

Slipping by a few weeks is normal and irrelevant; skipping exercises to stay on schedule defeats the purpose. The schedule serves the problems, not the reverse.

---

## Common pitfalls — the complete list, for your error log's first page

1. Pumping lemma: choosing the split yourself instead of defeating all splits.
2. Reduction direction: reducing the new problem to the hard one (proves nothing) instead of the hard one to the new.
3. One-directional reduction correctness proofs.
4. Confusing *decidable* with *recognizable*; forgetting deciders must halt on **all** inputs.
5. "Nondeterminism = parallelism / randomness." It is neither: it is existential quantification over computation paths.
6. Believing the Church–Turing thesis is a theorem (it's a definition with overwhelming evidence).
7. Treating P as "practically fast" and NP as "exponential" (NP is about *verification*, and contains P).
8. In Cook–Levin: forgetting that window legality must be proven *sufficient*, not just necessary — the exact gap the companion document's Chapter 1 fills.
9. Quantifier sloppiness in definitions ("for some" vs. "for all") — Velleman's training, applied or abandoned.
10. Reading proofs without reproducing them.

---

## After this book: the bridge to Stage 2 and beyond

When the Part IV checkpoint passes, you have completed Stage 1 of the ladder. Next moves, in order: Erickson's *Algorithms* NP-hardness chapter for reduction fluency at scale (Stage 2); Mitzenmacher–Upfal for the probability that randomized complexity needs (Stage 3); then Arora–Barak (Stage 4), where the companion document's Chapters 3–7 turn from a travel brochure into a hiking map. Reread the companion document at the end of each stage — measuring how much more of it has become transparent is the most honest progress bar you will find.

*One closing note on morale: every theorem in this subject was once incomprehensible to the person who proved it. The feeling of "I am too slow for this" is not diagnostic of anything except that the material is real. Persist; the subject is finite and you are not on a clock.*

