# The Narrow Corridor
## From Local Checkability to the Frontiers of P versus NP

*A guided walk: the Cook–Levin theorem proved in full, the barrier theorems, and the modern programs — meta-complexity, hardness magnification, and the algorithmic method — that define where a proof must pass.*

> **Status and provenance (read first).** This is an AI-assisted study document, produced in dialogue between a student and Anthropic's Claude. It claims no new results. Chapters 1–9 are exposition of known material; Chapter 10 is clearly labeled speculation, with an epistemic tier system ([T1]/[T2]/[T3]) and a verification checklist (§10.9). Citations were generated from the AI's memory; bibliography entries marked **[verified 2026-06]** have been checked against publisher/DBLP records, and all others should be treated as unverified. Corrections are welcome.

---

## Abstract

We present a self-contained path through the P versus NP problem, organized as the route one would actually walk when attacking it. We begin at the foundation: a complete proof of the *window lemma*, the load-bearing step of the Cook–Levin theorem, showing that local consistency of $2\times 3$ windows in a computation tableau suffices to certify a global Turing machine computation. We assemble the full reduction establishing the NP-completeness of SAT. We then survey the three classical barrier theorems — relativization, natural proofs, and algebrization — which eliminate entire categories of proof technique, and develop the three surviving research programs: meta-complexity (the study of the Minimum Circuit Size Problem and its relatives), hardness magnification (which compresses the full separation into barely-superlinear lower bounds), and Williams' algorithmic method (the only technique to have produced a lower bound past all known barriers, in the form of $\mathsf{NEXP} \not\subseteq \mathsf{ACC}^0$). We analyze the two precise bottlenecks of the current frontier — the parameters of the Easy Witness Lemma and the absence of a structure theorem for $\mathsf{TC}^0$ — and show that the *locality barrier* is the magnification construction itself read in reverse. We close with the regions outside the map: the possibility that $\mathsf{P} = \mathsf{NP}$, formal independence, Impagliazzo's five worlds, and physical escape hatches. An annotated bibliography is provided.

---

## Chapter 0. Introduction: the problem

### 0.1 Statement

A decision problem is in $\mathsf{P}$ if some deterministic Turing machine solves it in time polynomial in the input length. It is in $\mathsf{NP}$ if proposed solutions can be *verified* in polynomial time: $L \in \mathsf{NP}$ iff there is a polynomial-time verifier $V$ and a polynomial $p$ such that

$$x \in L \iff \exists w,\ |w| \le p(|x|),\ V(x, w) = 1.$$

Clearly $\mathsf{P} \subseteq \mathsf{NP}$. The P versus NP problem asks whether the inclusion is strict: **is finding a solution genuinely harder than checking one?**

### 0.2 Why it matters

The question is the formal shadow of an everyday asymmetry: appreciating a proof versus discovering it, grading homework versus doing it, checking a key versus picking a lock. If $\mathsf{P} = \mathsf{NP}$ (with feasible constants), search collapses to recognition: mathematics becomes mechanizable wherever proofs are short, most of cryptography dies, and optimization, learning, and design problems across science become tractable in principle. If $\mathsf{P} \ne \mathsf{NP}$, a permanent gap separates creativity from verification, and the modern cryptographic world rests on (a strengthening of) that gap. It is one of the seven Clay Millennium Prize Problems.

### 0.3 The plan of this document

The document follows the order of the actual conversation that produced it, which happens to be the logical order of an assault on the problem:

1. **Chapters 1–2** prove that SAT is NP-complete (Cook–Levin), with full rigor at the step textbooks usually wave through: the window lemma. This is what makes P vs NP a question about *one* problem.
2. **Chapter 3** presents the three barrier theorems that destroy the classical techniques.
3. **Chapters 4–7** develop the live programs: meta-complexity, hardness magnification, the algorithmic method with its Easy Witness Lemma, and the $\mathsf{TC}^0$ frontier.
4. **Chapter 8** synthesizes these into the *narrow corridor*: the constraints any successful proof must satisfy simultaneously.
5. **Chapter 9** surveys what may lie outside the map.
6. **Chapter 10** is original to this document: a formalization of the open problem at the frontier of World 3 — the *Domain Condensation Conjecture* — with full proofs of the elementary lemmas that localize the gap between Hirahara's partial-MCSP hardness and the open total case, structural constraints on any solution, and a conditional blueprint for excluding Heuristica.

---

## Chapter 1. The window lemma

The Cook–Levin theorem encodes a Turing machine computation as a *tableau* — a grid whose rows are configurations — and asserts that the global correctness of the computation is equivalent to the legality of every local $2 \times 3$ *window*. This chapter proves that claim, which is the precise point where the locality of computation is cashed in.

### 1.1 Setup and conventions

Fix a nondeterministic Turing machine $N$ with state set $Q$, tape alphabet $\Gamma$, and transition relation $\delta$. Tableau symbols come from $\Sigma = \Gamma \cup Q \cup \{\#\}$, with $Q$, $\Gamma$, $\{\#\}$ pairwise disjoint.

**Configurations.** A *configuration* of width $N$ is a string $C = \#\, u\, q\, a\, v\, \#$ with $u, v \in \Gamma^*$, $q \in Q$, $a \in \Gamma$: exactly one state symbol, and the head reads the symbol $a$ immediately to its right.

**One step.** $C \vdash C'$ holds in the following cases:

- if $(q', b, R) \in \delta(q, a)$: $\quad \#\, u\, q\, a\, v\, \# \;\vdash\; \#\, u\, b\, q'\, v\, \#$
- if $(q', b, L) \in \delta(q, a)$ and $u = u'c$ with $c \in \Gamma$: $\quad \#\, u'\, c\, q\, a\, v\, \# \;\vdash\; \#\, u'\, q'\, c\, b\, v\, \#$
- if $(q', b, L) \in \delta(q, a)$ and $u = \varepsilon$: $\quad \#\, q\, a\, v\, \# \;\vdash\; \#\, q'\, b\, v\, \#$ (the head bounces at the wall)
- if $q$ is a halting state: $C \vdash C$ (self-loop convention, so the tableau can be filled below a halt).

**Windows.** The window $W_j$ between rows $i$ and $i+1$ consists of cells $(i, j-1), (i, j), (i, j+1)$ on top and $(i+1, j-1), (i+1, j), (i+1, j+1)$ below. A $2 \times 3$ array is **legal** iff it occurs at some position in some pair of configurations $C \vdash C'$.

**Key observation.** Each step changes only the string positions $\{h-1, h, h+1\}$, where $h$ is the position of the state symbol in $C$. (Inspect the four cases above.)

### 1.2 Three facts about legal windows

Write a window as top $(a_1, a_2, a_3)$, bottom $(b_1, b_2, b_3)$.

**(F1) Boundary persistence.** For each position $p$: $b_p = \#$ iff $a_p = \#$.
*Proof.* In configurations, $\#$ occurs only at the two ends and is never altered by any step. $\square$

**(F2) No state on top fixes the center.** If no $a_p$ is a state symbol, then $b_2 = a_2$.
*Proof.* In any $C \vdash C'$ realizing the window at position $j$, the state position $h$ lies outside $\{j-1, j, j+1\}$. Position $j$ changes only if $h \in \{j-1, j, j+1\}$ — contradiction. (Note the *edge* cells of the window may legitimately change: a head just outside the window can write into $b_1$ or $b_3$. This is exactly why the argument is run through window *centers*.) $\square$

**(F3) State in the center pins the transition.** If $a_2 = q \in Q$ and $a_3 = a \in \Gamma$, then the bottom is exactly one of:

1. $(a_1,\, b,\, q')$ for some $(q', b, R) \in \delta(q, a)$;
2. $(q',\, a_1,\, b)$ for some $(q', b, L) \in \delta(q, a)$, if $a_1 \in \Gamma$;
3. $(\#,\, q',\, b)$ for some $(q', b, L) \in \delta(q, a)$, if $a_1 = \#$;
4. $(a_1,\, q,\, a)$ if $q$ is halting.

*Proof.* A configuration has a unique state symbol, so in any realization $C \vdash C'$, the head sits at the window's center reading $a$. The four cases of $\vdash$ then determine the three affected cells, which are precisely the window's columns. $\square$

### 1.3 The lemma

> **Theorem (window lemma).** Suppose row $i$ of the tableau is a configuration $C$ of width $N$ whose state symbol sits at position $k \le N - 2$ (the head is not reading the boundary $\#$), and every window $W_j$, $2 \le j \le N-1$, between rows $i$ and $i+1$ is legal. Then row $i+1$ is the configuration $C'$ for some single legal transition $C \vdash C'$.

*Proof.* Write $C = c_1 \cdots c_N$ with $c_k = q$ and $c_{k+1} = a \in \Gamma$. Denote row $i+1$ by $d_1 \cdots d_N$.

**Boundary.** $W_2$ has $a_1 = \#$ on top, so by (F1) $d_1 = \#$; symmetrically $d_N = \#$ via $W_{N-1}$.

**Far from the head.** Take any $j$ with $2 \le j \le N - 1$ and $|j - k| \ge 2$. Then none of the positions $j-1, j, j+1$ equals $k$, so the top of $W_j$ contains no state symbol. By (F2), $d_j = c_j$.

**At the head.** The window $W_k$ has top $(c_{k-1}, q, a)$. By (F3) its bottom — i.e., the triple $(d_{k-1}, d_k, d_{k+1})$ — matches exactly one transition $\tau \in \delta(q, a)$, or the halt loop. Combining with the far cells:

- $\tau = (q', b, R)$: row $i+1$ is $\#\, c_2 \cdots c_{k-1}\, b\, q'\, c_{k+2} \cdots \#$ — precisely $C'$ for the right move.
- $\tau = (q', b, L)$, $c_{k-1} \in \Gamma$: row $i+1$ is $\cdots c_{k-2}\, q'\, c_{k-1}\, b\, c_{k+2} \cdots$ — precisely the left move (position $k-2$ is unchanged by the far-cell case, as required).
- $\tau = (q', b, L)$, $c_{k-1} = \#$ (so $k = 2$): row $i+1$ is $\#\, q'\, b\, c_4 \cdots \#$ — the left move at the wall.
- Halting: row $i+1 = C$.

In every case row $i+1$ equals the successor of $C$ under one single transition; in particular it is itself a configuration. $\blacksquare$

### 1.4 Remarks

1. **Redundancy.** Only $W_k$ and the "far" windows were used. The windows $W_{k-1}$ and $W_{k+1}$ are legal but redundant: the overlap structure makes consistency automatic. The proof needs strictly less than the construction provides.
2. **Side hypotheses.** The hypotheses "row $i$ is a configuration" and "head not at the boundary" are discharged in the full reduction by induction from the start clauses and by choosing the tableau wide enough (width $n^k + 3$ for a time-$n^k$ machine) that the head cannot reach the right boundary within the time bound.
3. **Nondeterminism.** $\delta(q,a)$ is a set; the window $W_k$ selects one transition. Nothing requires different windows to agree, because only one window carries the transition information.

---

## Chapter 2. The Cook–Levin theorem

> **Theorem (Cook 1971, Levin 1973).** SAT is NP-complete.

### 2.1 The construction

Let $L \in \mathsf{NP}$, decided by an NTM $N$ in time $n^k$. For input $w$ of length $n$, consider an $n^k \times (n^k + 3)$ tableau whose first row is the start configuration $\#\, q_0\, w_1 \cdots w_n\, \sqcup \cdots \sqcup\, \#$. The width choice guarantees the head never reaches the right boundary — exactly the side condition the window lemma needs.

**Variables.** For each cell $(i, j)$ and each symbol $s \in \Sigma$, a Boolean variable $x_{i,j,s}$, meaning "cell $(i,j)$ contains $s$." That is $|\Sigma| \cdot O(n^{2k}) = O(n^{2k})$ variables.

**The formula** $\varphi = \varphi_{\text{cell}} \wedge \varphi_{\text{start}} \wedge \varphi_{\text{move}} \wedge \varphi_{\text{accept}}$:

- $\varphi_{\text{cell}}$: every cell contains exactly one symbol — at least one via the clause $\bigvee_s x_{i,j,s}$, at most one via $\neg x_{i,j,s} \vee \neg x_{i,j,t}$ for each pair $s \ne t$.
- $\varphi_{\text{start}}$: row 1 is literally the start configuration — a conjunction of the appropriate literals $x_{1,j,s}$.
- $\varphi_{\text{move}}$: for every $i$ and every $2 \le j \le N-1$, the window $W_j$ is legal. A window has 6 cells over a fixed alphabet, so the set of legal $2\times 3$ arrays is a **finite list depending only on $N$'s transition table, not on $n$**. Legality of one window is therefore a fixed-size formula: a disjunction, over legal arrays, of the conjunction of the 6 corresponding variables. Facts (F1)–(F3) live here: the finite list is precisely the set for which those facts hold.
- $\varphi_{\text{accept}}$: $\bigvee_{i,j} x_{i,j,q_{\text{acc}}}$.

### 2.2 Correctness

This is where the window lemma carries the entire weight.

**($\varphi$ satisfiable $\Rightarrow w \in L$).** A satisfying assignment picks, via $\varphi_{\text{cell}}$, a unique symbol per cell, so it *is* a tableau. $\varphi_{\text{start}}$ makes row 1 a configuration; the window lemma, applied inductively up the rows, says each row $i+1$ follows from row $i$ by one legal transition of $N$. The tableau is therefore a genuine computation branch, and $\varphi_{\text{accept}}$ makes it accepting. Hence $w \in L$.

**($w \in L \Rightarrow \varphi$ satisfiable).** Write any accepting branch into the tableau (repeating the halting configuration if it halts early); all windows are legal by construction.

Without the lemma, $\varphi_{\text{move}}$ would certify only "locally plausible" tables and the reduction would be unsound. The lemma is the load-bearing step.

### 2.3 Size, uniformity, and 3SAT

$\varphi$ has $O(n^{2k})$ clauses, each of constant size, and its structure is so regular that it is computable in polynomial time (with more care, in logarithmic space). SAT $\in \mathsf{NP}$ is immediate (guess an assignment, verify). Hence SAT is NP-complete. A standard gadget — or encoding the window disjunctions directly into clauses of width 3 — yields the NP-completeness of 3SAT, and from there Karp's 21 reductions populate the entire landscape.

**Consequence.** $\mathsf{P} = \mathsf{NP}$ iff SAT $\in \mathsf{P}$. The problem is concentrated into a single object. Everything that follows is about that object.

---

## Chapter 3. The barrier theorems

Three theorems eliminate whole categories of proof technique. They are not folklore caution; each is a formal impossibility result about a precisely defined class of arguments.

### 3.1 Relativization (Baker–Gill–Solovay 1975)

Diagonalization — the technique behind undecidability and the time hierarchy theorems — *relativizes*: it goes through unchanged if every machine is granted an arbitrary oracle. Baker, Gill, and Solovay constructed an oracle $A$ with $\mathsf{P}^A = \mathsf{NP}^A$ and an oracle $B$ with $\mathsf{P}^B \ne \mathsf{NP}^B$. Therefore **no relativizing argument can resolve P vs NP** in either direction. Pure diagonalization is dead on arrival.

### 3.2 Natural proofs (Razborov–Rudich 1997)

Since $\mathsf{P} \subseteq \mathsf{P/poly}$, it suffices to prove SAT requires super-polynomial circuits, and real lower bounds exist nearby: parity requires exponential-size constant-depth circuits (Håstad), clique requires exponential-size monotone circuits (Razborov). But essentially every combinatorial lower-bound technique works by exhibiting a property of functions that is (a) **constructive** — efficiently decidable from the truth table — and (b) **large** — satisfied by a random function with noticeable probability. Razborov and Rudich proved: any such *natural property* useful against $\mathsf{P/poly}$ would break pseudorandom function generators. If standard cryptography exists, **no natural proof separates P from NP.** The monotone-circuit success does not transfer: the monotone world provably diverges from the general one.

### 3.3 Algebrization (Aaronson–Wigderson 2008/2009)

Arithmetization — the technique behind $\mathsf{IP} = \mathsf{PSPACE}$ — escapes relativization. Aaronson and Wigderson showed it hits a third wall: techniques that survive *algebraic* oracles (low-degree extensions of Boolean oracles) also cannot resolve P vs NP. The combination "diagonalization + arithmetization," by itself, is insufficient.

### 3.4 What survives

Three programs are known to be consistent with all three barriers: **Geometric Complexity Theory** (Mulmuley–Sohoni; representation theory of orbit closures of the determinant and permanent — principled, but its occurrence-obstruction route was refuted by Bürgisser–Ikenmeyer–Panova, and even proponents speak in generational timescales), **the algorithmic method** (Williams; Chapter 6 — the only program with a delivered lower bound), and **meta-complexity / hardness magnification** (Chapters 4–5). This document follows the second and third, and their convergence.

---

## Chapter 4. Meta-complexity: the barrier as research object

### 4.1 MCSP

The **Minimum Circuit Size Problem**: given the full truth table of a Boolean function (length $N = 2^n$) and a size parameter $s$, decide whether the function has a circuit of size $\le s$. MCSP $\in \mathsf{NP}$ — a small circuit is its own certificate. Whether MCSP is NP-hard has been open since the 1970s.

The structural reason this problem is special: **a natural property in the Razborov–Rudich sense is essentially an efficient algorithm for (a version of) MCSP** — a procedure distinguishing easy truth tables from random ones. The natural proofs barrier, viewed from here, is not a wall but the object of study. Meta-complexity metabolizes the obstruction instead of colliding with it.

### 4.2 Three results that changed the field's mood

1. **Worst-case to average-case (Hirahara 2018).** A reduction from worst-case to average-case hardness for MCSP-type (Kolmogorov-complexity-type) problems — the kind of equivalence long believed impossible for NP-complete problems, established for meta-computational ones. Since "P $\ne$ NP in practice" requires average-case hardness, meta-complexity is the only territory where that bridge exists.
2. **NP-hardness of partial MCSP (Hirahara 2022).** The partial-function variant of MCSP is NP-hard under randomized reductions — the first structural crack in the fifty-year wall.
3. **Characterizations of cryptography (Liu–Pass 2020; Hirahara).** One-way functions exist **iff** time-bounded Kolmogorov complexity is mildly hard on average. The existence of cryptography is literally equivalent to a meta-complexity statement. The deepest open questions of the field are being restated as one question: *how hard is it to detect structure?*

---

## Chapter 5. Hardness magnification, and the locality barrier as its reflection

### 5.1 A representative theorem

Let Gap-MCSP$[s]$ be: given a truth table $T$ of length $N = 2^n$, distinguish "$T$ has a circuit of size $\le s$" from "$T$ is far from every circuit of size $\ll s$," with $s \approx 2^{\sqrt n}$.

> **Theorem (Oliveira–Pich–Santhanam style; parameters idealized).** If Gap-MCSP$[s]$ has no circuits of size $N^{1+\varepsilon}$ for some $\varepsilon > 0$, then $\mathsf{NP} \not\subseteq \mathsf{P/poly}$ — hence $\mathsf{P} \ne \mathsf{NP}$.

Barely-superlinear hardness for one compression problem magnifies into the full separation. Lower bounds of strength $n^{1+\varepsilon}$ are already known for *other* explicit problems; the entire question compresses into proving one almost-trivial-looking bound for one specific problem.

### 5.2 Proof sketch (by contrapositive)

Assume $\mathsf{NP} \subseteq \mathsf{P/poly}$; we build $N^{1+o(1)}$-size circuits for Gap-MCSP$[s]$.

1. **The witness is microscopic.** A yes-certificate is a circuit of size $s$, describable in $\approx s \log s \approx 2^{\sqrt n}$ bits — vanishing next to $N = 2^n$. Gap-MCSP is an NP problem whose witnesses are exponentially shorter than its input. This asymmetry is the entire engine.
2. **Compress the verification.** In the gap regime, distinguishing "consistent with some size-$s$ circuit" from "far from all of them" requires only $\mathrm{poly}(s, n)$ sampled coordinates of $T$, by a counting/VC-dimension argument over the bounded richness of the size-$s$ class. (For the exact, gapless version one uses *anti-checkers*: by an LP-duality/minimax argument, any truth table too hard for size $s$ has a small set of coordinates on which every size-$s$ circuit already fails.) The $N$-sized question collapses to a kernel of size $\mathrm{poly}(s, n) \ll N$.
3. **Deploy the assumption on the kernel.** "Does there exist a size-$s$ circuit consistent with these sampled pairs?" is an NP question about an instance of size $\mathrm{poly}(s, n)$. By the assumption, it is solved by a circuit of size $\mathrm{poly}(s, n) = N^{o(1)}$ — a tiny, all-powerful gadget.
4. **Wire it up.** The full circuit is an oblivious routing/hashing layer of size $N \cdot \mathrm{polylog}(N)$ feeding the $N^{o(1)}$-size gadget. Total: $N^{1+o(1)}$. The weak lower bound is false under the assumption. $\blacksquare$

### 5.3 The locality barrier is this proof read backwards

Inspect the object built in step 4: a structureless routing network plus a tiny oracle blob — and the blob *exists unconditionally* as an oracle gate, whether or not NP is easy. Now observe that every lower-bound technique we possess at the $n^{1+\varepsilon}$ scale (gate elimination, wire-counting) is **local**: its argument survives granting the circuit a few small oracle gadgets for free. But the magnification construction *is* a near-linear circuit-with-small-gadgets for Gap-MCSP$[s]$. Therefore **no local technique can prove the bound magnification needs: the bound is false in the local world.** This is the locality barrier of Chen–Hirahara–Oliveira–Pich–Rajgopal–Santhanam — not an external obstruction discovered on the road, but the magnification construction itself, turned around and pointed at the toolbox.

Hence the present tableau: $n^{1+\varepsilon}$ bounds are proven for other problems, by methods that provably cannot transfer to the one problem where the payout is $\mathsf{P} \ne \mathsf{NP}$. What is missing is a fundamentally **non-local** lower-bound technique. Exactly one is known to exist.

---

## Chapter 6. The algorithmic method

### 6.1 The premise

> **Theorem schema (Williams 2010).** If satisfiability of circuits from a class $\mathcal{C}$ on $n$ inputs is decidable in time $2^n / n^{\omega(1)}$ — beating brute force by any super-polynomial factor — then $\mathsf{NEXP} \not\subseteq \mathcal{C}$.

Hardness from easiness: a fast SAT algorithm for $\mathcal{C}$ is proof that $\mathcal{C}$-circuits have exploitable global structure, and exploitable structure is what a maximally hard function cannot have. Instantiated with a real algorithm, this delivered the landmark:

> **Theorem (Williams 2011).** $\mathsf{NEXP} \not\subseteq \mathsf{ACC}^0$.

This remains the only lower bound ever proven past all known barriers.

### 6.2 The conversion, as one contradiction chain

Assume toward contradiction $\mathsf{NEXP} \subseteq \mathcal{C}$ (say $\mathcal{C} = \mathsf{ACC}^0$) and hold the fast $\mathcal{C}$-SAT algorithm.

1. **Compress the witnesses.** The Easy Witness Lemma (§6.4) yields: every NEXP verifier has, on every yes-instance, a witness whose $2^n$-bit string is the truth table of a poly-size circuit.
2. **Guess the compressed form.** For a language in $\mathsf{NTIME}(2^n)$, guess the poly-size circuit $W$ encoding the witness — polynomially many bits instead of exponentially many.
3. **Verify with the SAT algorithm.** Checking that $W$'s truth table is a valid witness compiles (using the assumption $\mathsf{NEXP} \subseteq \mathcal{C}$ again, to place the verification circuitry in $\mathcal{C}$) into an unsatisfiability question for a $\mathcal{C}$-circuit. The fast algorithm answers it in time $2^n / n^{\omega(1)}$.
4. **Contradict diagonalization.** Every $\mathsf{NTIME}(2^n)$ language has been decided in nondeterministic time $2^n / n^{\omega(1)}$, violating the nondeterministic time hierarchy theorem — unconditional, and proven by diagonalization. $\blacksquare$

### 6.3 The fuel: an actual ACC$^0$-SAT algorithm

Two old tools, newly aimed: the **Beigel–Tarui structure theorem** (building on Yao), converting any $\mathsf{ACC}^0$ circuit into a quasipolynomial-size *symmetric function of ANDs* — a global algebraic restructuring of the entire circuit, the decisively non-local move — and **Coppersmith's fast rectangular matrix multiplication**, batch-evaluating that object on all $2^n$ inputs faster than one at a time. The lower bound exists *because* $\mathsf{ACC}^0$ has a structure theorem; the algorithm is the cash value of the structure.

**Why every barrier misses it.** Relativization: broken by the PCP/easy-witness ingredients and by an algorithm that reads the circuit's actual anatomy. Natural proofs: the argument is constructive about one diagonal language, never statistical about random functions. Locality: Beigel–Tarui is a whole-circuit rewrite that does not survive oracle-gadget substitution. It threads all needles, uniquely.

### 6.4 The fragile joint: the Easy Witness Lemma

> **Lemma (Impagliazzo–Kabanets–Wigderson 2002).** If $\mathsf{NEXP} \subseteq \mathsf{P/poly}$, then every NEXP verifier has, on every yes-instance, a witness that is the truth table of a poly-size circuit.

*Proof shape — a self-defeating loop.* Suppose not: $\mathsf{NEXP} \subseteq \mathsf{P/poly}$, yet some verifier has a yes-instance all of whose witnesses are hard.

- The smallness assumption triggers a collapse: $\mathsf{NEXP} \subseteq \mathsf{P/poly} \Rightarrow \mathsf{NEXP} = \mathsf{MA}$ (descending from Babai–Fortnow–Lund interactive proofs for EXP: if the prover strategy has small circuits, Merlin sends the circuit and Arthur spot-checks it).
- The hard witnesses become a weapon: by hardness-vs-randomness (Nisan–Wigderson, Impagliazzo–Wigderson), any truth table of high circuit complexity fuels a pseudorandom generator. A nondeterministic machine guesses a witness, treats it as a hard function, and derandomizes Arthur.
- Composing: $\mathsf{NTIME}(2^n)$ is simulated in nondeterministic time far below $2^n$ (with slight advice, infinitely often), violating the nondeterministic time hierarchy. $\blacksquare$

The assumption "hardness does not exist" survives only by making everything — even the certificates of exponential computations — compressible.

### 6.5 Why the conclusion reads NEXP (now NQP) and not NP

Run a finger over the ingredients:

- The collapse step exploits the **algebraic self-correctability** of EXP-complete problems: arithmetized versions are random-self-reducible. **SAT has nothing comparable.** NP-complete problems are locally *checkable* — that is the PCP theorem, and Chapter 1 was its seed — but not randomly *self-correctable*; Feigenbaum–Fortnow-type results show that non-adaptive random self-reducibility of SAT would collapse the polynomial hierarchy. The missing ingredient is plausibly missing for a fundamental reason.
- Karp–Lipton at NP scale yields only $\mathsf{PH} = \Sigma_2^p$, too weak to feed the loop; and the hierarchy contradiction needs quantitative *room* that exists at exponential time and evaporates at polynomial time.

**Murray–Williams (2018)** repaired what could be repaired: an easy witness lemma at NP/NQP scale, replacing the BFL collapse with a bootstrapping win-win recursion against an almost-everywhere nondeterministic hierarchy. The price is quantitative — a *fixed-polynomial* lemma (if $\mathsf{NP} \subseteq \mathsf{SIZE}(n^k)$, witnesses have circuits of size $n^{g(k)}$ with $g$ polynomial in $k$). Compose: fixed-poly EWL $\times$ quasipolynomial Beigel–Tarui blowup $\times$ the hierarchy's demand for super-savings — and the smallest nondeterministic class with enough slack is quasipolynomial time:

> **Theorem (Murray–Williams 2018).** $\mathsf{NQP} \not\subseteq \mathsf{ACC}^0$.

The theorem's strength is the fixed point of three parameter curves. $\mathsf{NP} \not\subseteq \mathsf{ACC}^0$ awaits either a polynomial-blowup structure theorem for $\mathsf{ACC}^0$ or a constant-exponent witness compression at NP scale — and any genuinely new checkability-vs-correctability property of SAT would detonate here first. Subsequent refinements (Chen–Ren and others) convert even nontrivial *derandomization* (CAPP) into **average-case** lower bounds — precisely the currency hardness magnification accepts.

---

## Chapter 7. The TC$^0$ wall

### 7.1 The class and the scoreboard

$\mathsf{TC}^0$: constant depth, polynomial size, majority/threshold gates — one rung above $\mathsf{ACC}^0$, and the physical location of the frontier. $\mathsf{NQP} \not\subseteq \mathsf{ACC}^0$ is proven; against $\mathsf{TC}^0$ it is currently consistent with all known theorems that **all of NEXP sits inside depth-three majority circuits**. Everyone believes $\mathsf{TC}^0$ cannot compute graph connectivity; nobody can prove it fails to compute anything in nondeterministic exponential time.

### 7.2 Why the algorithmic engine stalls

Williams' method needs fuel: a SAT (or even CAPP) algorithm for $\mathsf{TC}^0$ with super-polynomial savings. For $\mathsf{ACC}^0$ the fuel came from Beigel–Tarui. Threshold gates refuse the treatment: majority has no low-degree polynomial representation over any convenient ring; it is algebraically *incompressible* in exactly the way AND/OR/MOD gates are not. $\mathsf{ACC}^0$ fell because it has a structure theorem; $\mathsf{TC}^0$ stands because, as far as anyone knows, it has none. Partial fuel exists — probabilistic-polynomial-method #SAT algorithms for depth-2 threshold circuits with restricted wire counts (Alman–Chan–Williams) — nothing that ignites the conversion for the full class.

### 7.3 The barrier acquires teeth

Naor and Reingold constructed candidate pseudorandom *functions* computable in $\mathsf{TC}^0$, secure under standard assumptions (DDH/factoring). So $\mathsf{TC}^0$ is plausibly the smallest class that **contains cryptography**. Unwound through Razborov–Rudich: any natural lower-bound proof against $\mathsf{TC}^0$ breaks those PRFs. For $\mathsf{ACC}^0$ the natural-proofs barrier was procedural caution — nobody believes $\mathsf{ACC}^0$ computes PRFs, and it duly fell to a non-natural proof. At $\mathsf{TC}^0$ the barrier becomes a live adversary: the class is strong enough to hide structure from every statistical test, and a statistical test is what a combinatorial lower-bound technique *is*. The fortress is garrisoned by the very hardness one is trying to prove.

### 7.4 How thin the wall is

- **Impagliazzo–Paturi–Saks (1997):** depth-$d$ threshold circuits require $n^{1 + c^{-d}}$ wires — a bound decaying toward trivial with depth.
- **Kane–Williams (2016):** depth-2 threshold circuits require on the order of $n^{1.5}$ gates.
- **Chen–Tell (2019):** improving IPS to $n^{1+\varepsilon}$ wires *with $\varepsilon$ independent of depth*, for one specific explicit problem in $\mathsf{NC}^1$, already separates $\mathsf{NC}^1$ from $\mathsf{TC}^0$.

The distance between known and needed is a difference in how a tiny exponent depends on $d$ — with the locality barrier explaining why every existing technique stops working over precisely that distance.

*(A resonance worth recording: constant-depth threshold circuits are idealized neural networks; transformer-style architectures are, in the relevant sense, $\mathsf{TC}^0$-flavored objects. The class nobody can prove weak is the class that models the machines now writing about it.)*

---

## Chapter 8. Synthesis: the narrow corridor

Assemble the document into one map.

1. **The window lemma** made computation locally checkable; local checkability made SAT universal (Cook–Levin); universality concentrated P vs NP into one problem.
2. **The three classical barriers** — relativization, natural proofs, algebrization — eliminated every classical weapon, each by a theorem.
3. **Meta-complexity** turned the strongest barrier into a research object: natural properties *are* MCSP algorithms; cryptography's existence *is* a Kolmogorov-complexity statement; the worst-case/average-case bridge exists only here.
4. **Hardness magnification** compressed the required blow to a barely-superlinear bound for one compression problem — and its own construction, read backwards, is the **locality barrier**: no local technique can land the blow, because in the local (gadget-extended) world the blow is provably unsound.
5. **The algorithmic method** is the unique known non-local cannon, with one confirmed kill ($\mathsf{NEXP} \not\subseteq \mathsf{ACC}^0$, upgraded to $\mathsf{NQP}$). Its weakest joint is the **Easy Witness Lemma**, blocked at NP for want of a self-correction property SAT probably lacks; its fuel line ends at **TC$^0$**, the first wall garrisoned by cryptography itself.

The corridor, in one sentence: **find a Williams-style nontrivial algorithm whose existence implies a barely-superlinear, non-local lower bound for a compression problem, and the magnification gearbox does the rest.** Any successful proof built from recognizable technique must be simultaneously non-relativizing, non-natural, non-algebrizing, and non-local — and every theorem surveyed here is consistent with exactly that one corridor.

This is not a proof of $\mathsf{P} \ne \mathsf{NP}$. It is an honest map of where one must pass.

---

## Chapter 9. Outside the map

Speculation, clearly marked, with mathematical handrails where they exist.

### 9.1 P = NP might simply be true

The map is infrastructure for proving hardness; an algorithm ignores barriers entirely (they constrain lower-bound proofs, not upper bounds). The honest version is a *galactic* algorithm — $n^{10000}$, or constants the size of the universe: mathematically world-ending, practically inert. Knuth, late in life, leaned this way. A haunting adjacent fact: by Levin's universal search, an asymptotically optimal algorithm for SAT is *already writable today*; if $\mathsf{P} = \mathsf{NP}$, the witnessing algorithm may in a precise sense already exist, with only its runtime analysis missing.

### 9.2 Formal independence

Perhaps P vs NP is unprovable in ZFC. Status: no evidence, and two contentful reasons for skepticism. The statement is arithmetic — about finite objects — and the known independence machinery (forcing, large cardinals) has essentially never reached that floor. And Ben-David–Halevi showed: if $\mathsf{P} \ne \mathsf{NP}$ were independent of PA (plus true $\Pi_1$ sentences), SAT would have nearly-polynomial-time algorithms — independence would *almost be* $\mathsf{P} = \mathsf{NP}$. The plausible cousin — unprovability of circuit lower bounds in *bounded arithmetic* (Razborov) — is the natural-proofs barrier in logician's clothes, and is on-map: meta-complexity again.

### 9.3 Impagliazzo's five worlds

A theorem "$\mathsf{P} \ne \mathsf{NP}$" fixes one bit; civilization depends on finer structure. **Algorithmica** ($\mathsf{P} = \mathsf{NP}$); **Heuristica** (worst-case hardness, average-case ease — hardness exists but is never met); **Pessiland** (average-case hardness without one-way functions — hard problems, no cryptography to show for them); **Minicrypt** (one-way functions, no public-key); **Cryptomania** (the believed world). $\mathsf{P} \ne \mathsf{NP}$ could be proven without learning which world is ours. Pinning the world is the average-case question — and the Liu–Pass/Hirahara characterizations show its borders are *equivalent to Kolmogorov-complexity statements*: this region is being annexed by the map in real time, and is the safest bet for the next decade's progress.

### 9.4 Physics

Quantum computing does not brute-force NP: Bennett–Bernstein–Brassard–Vazirani proved Grover's $\sqrt N$ speedup optimal for unstructured search; $\mathsf{NP} \subseteq \mathsf{BQP}$ would be a shock comparable to $\mathsf{P} = \mathsf{NP}$. Exotica: closed timelike curves would give $\mathsf{P}_{\text{CTC}} = \mathsf{PSPACE}$ (Aaronson–Watrous) — time travel solves SAT, generally read as evidence against time travel. Aaronson has proposed elevating intractability to physical law: *no physical process solves NP-complete problems with polynomial resources* — a sibling of the second law of thermodynamics.

### 9.5 The frame itself

Each barrier is a theorem about a *formalized class of known techniques*. A proof from sufficiently alien mathematics — as Fermat's Last Theorem required machinery centuries beyond its statement's language, as GCT imports representation theory wholesale — might be non-classifiable: not threading the needles but not made of thread. The corridor is where a proof must pass *if built from anything currently recognizable as technique*. That conditional is the map's edge, drawn honestly.

---

## Chapter 10. The Domain Condensation Conjecture

*This chapter is original synthesis produced in the working session that generated this document. Unlike Chapters 1–9, which survey and rigorize known material, this chapter formulates a research target. Epistemic status is therefore tracked explicitly throughout, in three tiers:*

- **[T1]** *proved here, elementary and self-contained — the reader can verify every step;*
- **[T2]** *cited from the literature — statements given informally where exact parameters require verification against the original papers (a checklist is provided in §10.9);*
- **[T3]** *conjectured or proposed — clearly original speculation, possibly false, possibly known.*

*The elementary results [T1] are simple enough that they are very likely known, at least as folklore, to specialists; the contribution claimed here is only the organization of the problem around them.*

### 10.1 Preliminaries

**Circuits.** Circuits are over the basis $\{\wedge, \vee, \neg\}$ with fan-in two; $|C|$ denotes the number of gates. For a total function $f : \{0,1\}^n \to \{0,1\}$, $\mathrm{cc}(f)$ is the minimum size of a circuit computing $f$. We identify $f$ with its truth table, a string of length $N = 2^n$.

**Partial tables.** A *partial table* is a string $T \in \{0,1,*\}^N$, identified with a partial function on $\{0,1\}^n$. Its *domain* $D(T) = \{x : T(x) \ne *\}$ is the set of defined positions; $m(T) = |D(T)|$. The *domain indicator* is the total Boolean function $\chi_{D(T)}$, and the *domain complexity* of $T$ is $\mathrm{dc}(T) := \mathrm{cc}(\chi_{D(T)})$. A total $f \in \{0,1\}^N$ *completes* $T$, written $f \sqsupseteq T$, if $f(x) = T(x)$ for all $x \in D(T)$. A circuit $C$ completes $T$ if the function it computes does.

**Encoding convention.** Instances are presented in the *dense encoding*: the full string over $\{0,1,*\}$ of length $N$, so the input length is $\Theta(N)$ and "polynomial time" means $\mathrm{poly}(N)$. (The literature also studies *sparse* encodings — lists of (input, value) pairs — for which the lemmas below need re-examination; see §10.6.3 for why the dense regime is in fact forced.)

**The promise problems.** For size parameters $s < S$ (functions of $n$, suppressed where clear):

- **Gap-MCSP$[s, S]$.** Input: total $f \in \{0,1\}^N$. YES if $\mathrm{cc}(f) \le s$; NO if $\mathrm{cc}(f) > S$.
- **Gap-pMCSP$[s, S]$.** Input: partial $T \in \{0,1,*\}^N$. YES if some circuit of size $\le s$ completes $T$; NO if no circuit of size $\le S$ completes $T$ (equivalently: every circuit of size $\le S$ disagrees with $T$ somewhere on $D(T)$).
- **Gap-pMCSP$^{d}[s, S]$.** The restriction of Gap-pMCSP$[s,S]$ to instances with $\mathrm{dc}(T) \le d$.

**Kolmogorov analogues.** Fix a time-efficient universal machine $U$. For a string $z$ and time bound $t$, $K^t(z) = \min\{|p| : U(p) \text{ outputs } z \text{ within } t \text{ steps}\}$. **Gap-MINKT** is the promise problem: given $(z, 1^t, 1^s)$, YES if $K^t(z) \le s$; NO if $K^{t'}(z) > s + \omega(\log |z|)$ for $t' = \mathrm{poly}(t)$ (Hirahara's parameterization [T2]; the gap is in both program length and time). The partial analogue **Gap-pMINKT** takes $z \in \{0,1,*\}^N$ and asks about completions; the *domain description complexity* is the least length of a program deciding membership in $D(z)$ within $\mathrm{poly}(N)$ steps.

**Reductions.** "NP-hard under randomized reductions" means: there is a probabilistic polynomial-time many-one reduction from an NP-complete problem, mapping YES to YES and NO to NO with probability $\ge 2/3$ (over the reduction's coins), the promise being respected on the support. All composition claims below are under this convention.

### 10.2 Background theorems [T2]

The chapter relies on the following results; statements are faithful in shape, with parameters to be verified (§10.9).

> **Theorem 10.A (Hirahara 2022).** Gap-pMCSP is NP-hard under randomized polynomial-time reductions, for some nontrivial gap regime. *(Verified June 2026: FOCS 2022, pp. 968–979; the reductions are randomized, as stated.)* An important precursor is Ilango (FOCS 2020), which establishes hardness for partial-function and constant-depth-formula versions of MCSP; delineating precisely which hardness statement each of the two papers proves is part of checklist item (V1). The sources should also be consulted for the exact gap $(s, S)$, the encoding, and whether an agreement-gap ("robust") version is established — this last point matters in §10.7.

> **Theorem 10.B (Hirahara 2018).** If $\mathsf{DistNP} \subseteq \mathsf{AvgP}$, then Gap-MINKT has a polynomial-time algorithm. Consequently (with standard randomized adaptations), if Gap-MINKT is NP-hard under randomized reductions, then $\mathsf{NP} \not\subseteq \mathsf{BPP}$ implies $\mathsf{DistNP} \not\subseteq \mathsf{AvgBPP}$ — i.e., Heuristica is excluded.

> **Theorem 10.C (Murray–Williams 2017; Saks–Santhanam 2020 — screening).** NP-hardness of MCSP under *deterministic* polynomial-time many-one reductions implies breakthrough separations (e.g., $\mathsf{EXP} \ne \mathsf{ZPP}$); under sufficiently *local/oblivious* reductions, stronger breakthroughs. Hence any near-term hardness proof is forced to be randomized and instance-adaptive.

> **Theorem 10.D (Liu–Pass 2020).** One-way functions exist iff $K^{t}$ is mildly hard on average over uniformly random strings (for some/all polynomial $t$, per the source's quantification).

> **Theorem 10.E (Impagliazzo–Levin 1990, universal extrapolation; Hirahara 2022b, average-case symmetry of information).** If one-way functions do not exist, then every polynomial-time samplable distribution admits efficient "extrapolation" (next-block prediction / compression to near the entropy), and time-bounded Kolmogorov complexity satisfies average-case symmetry of information. Informally: a world without cryptography is algorithmically tame — efficiently generated objects cannot hide structure from efficient algorithms. (Important caveat: the hypothesis "OWFs do not exist" carries infinitely-often/almost-everywhere quantifier subtleties that any use of this theorem must track; see §10.8.)

> **Theorem 10.F (folklore; cf. Ben-David–Chor–Goldreich–Luby).** If one-way functions exist, then $\mathsf{DistNP} \not\subseteq \mathsf{AvgBPP}$: inverting a OWF on samplable inputs yields a distributional NP problem hard on average, and search-to-decision translations apply.

### 10.3 The elementary lemmas [T1]

> **Lemma 10.1 (the NO direction is free).** Let $T$ be a NO instance of Gap-pMCSP$[s, S]$. Then *every* total completion $f \sqsupseteq T$ satisfies $\mathrm{cc}(f) > S$.

*Proof.* Let $f \sqsupseteq T$ and let $C$ be any circuit computing $f$. Then $C$ agrees with $T$ on all of $D(T)$, i.e., $C$ completes $T$. Since $T$ is a NO instance, $|C| > S$. As $C$ was arbitrary, $\mathrm{cc}(f) > S$. $\blacksquare$

> **Lemma 10.2 (zero-fill on simple domains).** Define the *zero-fill* $Z(T) \in \{0,1\}^N$ by $Z(T)(x) = T(x)$ for $x \in D(T)$ and $Z(T)(x) = 0$ otherwise. Then $Z$ is computable in deterministic time $O(N)$, and: if $T$ is a YES instance of Gap-pMCSP$[s, S]$, then
> $$\mathrm{cc}(Z(T)) \;\le\; s + \mathrm{dc}(T) + 1.$$

*Proof.* Let $C$ be a circuit of size $\le s$ completing $T$ (one exists by the YES promise), and let $D$ be a circuit of size $\mathrm{dc}(T)$ computing $\chi_{D(T)}$. Consider the circuit $C'(x) := C(x) \wedge D(x)$, of size $\le s + \mathrm{dc}(T) + 1$. For $x \in D(T)$: $D(x) = 1$ and $C(x) = T(x)$ (since $C$ completes $T$), so $C'(x) = T(x) = Z(T)(x)$. For $x \notin D(T)$: $D(x) = 0$, so $C'(x) = 0 = Z(T)(x)$. Hence $C'$ computes $Z(T)$. $\blacksquare$

**Remark 10.2.1 (the witness is existential — this kills the naive trap).** The map $T \mapsto Z(T)$ never sees $C$. The bound on $\mathrm{cc}(Z(T))$ is purely existential: YES-membership in Gap-MCSP asks only that a small circuit *exist*, not that the reduction find one. This dissolves what one might call the *value trap* — the intuition that filling the stars correctly requires solving the search problem. Filling values is free. What is *not* free is the term $\mathrm{dc}(T)$: the complexity of the domain itself. The trap was never about the values.

> **Lemma 10.3 (totality is the simple-domain special case).** The identity map sends Gap-MCSP$[s, S]$ instances to Gap-pMCSP$^{O(1)}[s, S]$ instances: a total table is a partial table with full domain, whose indicator is the constant 1, of circuit size $O(1)$.

*Proof.* Immediate from the definitions; YES and NO conditions coincide verbatim. $\blacksquare$

> **Theorem 10.4 (equivalence).** For any parameter $d = d(n)$ with $s + d + 1 \le S$:
> 1. Gap-pMCSP$^{d}[s, S]$ reduces to Gap-MCSP$[s + d + 1,\, S]$ by the deterministic linear-time map $Z$.
> 2. Gap-MCSP$[s, S]$ reduces to Gap-pMCSP$^{O(1)}[s, S]$ by the identity.
>
> Consequently, NP-hardness of total Gap-MCSP (under randomized reductions, in any gap regime $[\,s' , S\,]$ with $s' = s + d + 1$) is **equivalent** to NP-hardness of partial Gap-pMCSP restricted to domain complexity $d$, up to the stated parameter translation.

*Proof.* (1) YES: by Lemma 10.2, $\mathrm{cc}(Z(T)) \le s + d + 1$, so $Z(T)$ is a YES instance of Gap-MCSP$[s+d+1, S]$. NO: by Lemma 10.1, $\mathrm{cc}(Z(T)) > S$. The map respects the promise and is deterministic, hence composes with randomized reductions. (2) is Lemma 10.3. The equivalence statement chains (1) and (2) with the hypothesized hardness. $\blacksquare$

**Interpretation.** Theorem 10.4 localizes the entire distance between Theorem 10.A (partial hardness — proven) and the open target (total hardness) in a single parameter: **the circuit complexity of the domain**. Hirahara's reduction, by the architecture such a reduction must have, hides its cryptographic gadgetry in *where the holes are*, not in what would fill them. If the holes could be forced into a simple pattern, the problem would already be solved by a one-gate argument.

> **Lemma 10.5 (Kolmogorov analogue).** Define zero-fill on partial strings analogously. Suppose $z \in \{0,1,*\}^N$ has a completion $w$ with $K^t(w) \le s$, and the membership function of $D(z)$ is computable by a program of length $d$ running in time $t_D$ per query. Then
> $$K^{t''}(Z(z)) \;\le\; s + d + O(\log(s + d)) \quad \text{for } t'' = O(t + N \cdot t_D + N).$$
> Moreover every completion of a NO instance of Gap-pMINKT remains NO (the analogue of Lemma 10.1), with the time-bound bookkeeping $t \mapsto t''$ absorbed into the $\mathrm{poly}(t)$ slack that Gap-MINKT's promise already provides, whenever $t \ge N^{\Omega(1)}$.

*Proof sketch.* The program: run the $s$-bit program to print $w$ in time $t$; run the $d$-bit domain decider on each index; zero out non-domain positions. The $O(\log)$ overhead pays for delimiting the two programs (standard pairing). The NO direction is verbatim Lemma 10.1 with "circuit of size $S$" replaced by "program of length $S$ and time $t'$", noting that a program printing a completion in time $t'$ in particular determines a completion. The time-slack condition is what makes the $t''$ overhead legal inside the promise; this is the one place where parameters must be matched to the exact MINKT formulation used. $\square$

> **Lemma 10.6 (anti-interpolation / density bound).** Every partial table $T$ with $m$ defined points has a completion of circuit complexity $O(m \cdot n)$: the DNF with one term per defined 1-point completes $T$ (zero elsewhere). Consequently, Gap-pMCSP$[s, S]$ has no NO instances unless $S < O(m n)$ — meaningful instances require $m = \Omega(S / n)$: **the domain must be large relative to the NO threshold.**

*Proof.* The DNF has $\le m$ terms of $\le n$ literals each. $\blacksquare$

### 10.4 The conjecture [T3]

> **Conjecture 10.7 (Domain Condensation, strong form).** There exist polynomials $p, q$ and a probabilistic polynomial-time algorithm $\Lambda$ (the *condenser*) such that for all $n, s, S$ with $S \ge p(s, n)$, given a Gap-pMCSP$[s, S]$ instance $T$, the output $T' = \Lambda(T; r)$ satisfies, with probability $\ge 2/3$ over $r$:
> 1. *(Simplicity)* $\mathrm{dc}(T') \le q(s, n')$, where $n'$ is the output input-length;
> 2. *(YES transfer)* if $T$ is YES at size $s$, then $T'$ is YES at size $s' \le q(s, n')$;
> 3. *(NO transfer)* if $T$ is NO at size $S$, then $T'$ is NO at size $S' \ge S^{\Omega(1)}$, with $s' + \mathrm{dc}(T') + 1 \le S'$.
>
> **Weak form:** as above with quasipolynomial $q$ and $S' \ge S^{o(1)}$ losses, which still suffices for the payout chain below with degraded but nontrivial parameters. **MINKT form:** the same statement mutatis mutandis for Gap-pMINKT, with domain description complexity in place of $\mathrm{dc}$.

**What a solution must look like.** By Theorem 10.4, a condenser composes with $Z$ to give a randomized reduction Gap-pMCSP $\to$ Gap-MCSP. So a solution is exactly: a randomized algorithm transforming arbitrary-domain partial instances into simple-domain ones, with existential witness transfer (Remark 10.2.1: the YES witness for $T'$ need never be computed) and parameter losses bounded as stated. A *refutation* is equally well-defined: e.g., an oracle relative to which Gap-pMCSP is hard but every condenser fails, which would prove that condensation, like the hardness it serves, must be non-relativizing (cf. §10.6.5).

### 10.5 The payout chain

> **Proposition 10.8 [T1 given T2/T3].** Conjecture 10.7 (MCSP form) $+$ Theorem 10.A (with compatible gap parameters) $\Rightarrow$ Gap-MCSP is NP-hard under randomized polynomial-time reductions.

*Proof.* Compose: NP-complete problem $\to$ (Thm 10.A) $\to$ Gap-pMCSP $\to$ (Conj 10.7) $\to$ Gap-pMCSP$^{q(s,n')}$ $\to$ (Thm 10.4(1), deterministic) $\to$ Gap-MCSP. Randomized many-one reductions with two-sided error compose with constant error inflation, repaired by standard amplification of the first two stages. Parameter compatibility — the gap of Theorem 10.A must exceed the condenser's losses plus the $+\,\mathrm{dc}+1$ of zero-fill — is the hypothesis "compatible gap parameters." $\blacksquare$

> **Proposition 10.9 [T1 given T2/T3].** Conjecture 10.7 (MINKT form) $+$ partial-MINKT hardness (the MINKT face of Theorem 10.A) $\Rightarrow$ Gap-MINKT is NP-hard under randomized reductions $\Rightarrow$ (Theorem 10.B) **Heuristica is excluded**: $\mathsf{NP} \not\subseteq \mathsf{BPP} \Rightarrow \mathsf{DistNP} \not\subseteq \mathsf{AvgBPP}$.

The MINKT track is emphasized because Theorem 10.B is stated for MINKT; whether the 2018 machinery applies directly to Gap-MCSP is a verification item (§10.9), and the MCSP$\leftrightarrow$MINKT translation is itself a known nontrivial issue (short programs yield small circuits only with $\mathrm{poly}(N) = 2^{O(n)}$ blowup in one direction).

### 10.6 Structural constraints on any condenser [T1 observations, with computations]

Formalizing the target immediately yields *shape theorems*: properties any solution is forced to have, and dead ends provably closed. Documenting these is part of the deliverable — failed attempts, made precise, are reusable.

**10.6.1 The fill/shrink trade-off.** The two monotone moves on partial tables are *filling* (defining stars: domain grows) and *shrinking* (starring defined entries: domain shrinks). Filling preserves NO for free (Lemma 10.1: more constraints, fewer completions — formally, completions of the filled table are completions of $T$) but threatens YES (the filled values must be computable jointly with $T$, which is where $\mathrm{dc}$ enters). Shrinking preserves YES for free (a circuit completing $T$ completes any sub-table) but threatens NO: the NO promise guarantees only that each circuit of size $\le S$ errs on *at least one* defined point, and shrinking may delete exactly those points. Any condenser must either thread both monotone directions or act non-monotonically; pure strategies in one direction provably fail (10.6.2–10.6.3).

**10.6.2 Hashing/re-indexing fails by witness non-transfer.** Suppose the condenser re-indexes via a hash $h : \{0,1\}^n \to \{0,1\}^{n'}$, defining $T'(y) := T(x)$ when $x$ is a (unique) defined preimage. For YES transfer one needs a small circuit completing $T'$; the natural candidate is $C \circ h^{-1}$, but inverting $h$ on $D(T)$ is a computation whose complexity is comparable to that of $D(T)$ itself — the quantity we are trying to eliminate reappears inside the witness. Generic re-indexing conserves domain complexity; it relocates it from the instance into the witness.

**10.6.3 Sparsification fails by gap inversion [T1, with the computation].** Suppose the condenser selects $m'$ defined points and outputs the *list* (equivalently, a tiny dense table over $\{0,1\}^{\lceil \log m' \rceil}$ with a hardwired index map $\sigma$). YES transfers: $C \circ \sigma$ has size $\le s + \widetilde O(m' n)$, and $\sigma$, being a hardwired list, is "simple" by fiat. But the output lives on $n' = \lceil \log m' \rceil$ inputs, where *every* total function has circuits of size $O(2^{n'}/n') = O(m'/\log m')$ (Lupanov's bound; even the weaker DNF bound of Lemma 10.6 suffices for a coarser version of this argument). So for the output to have NO instances at all, its threshold must satisfy $S' < O(m'/\log m')$. Meanwhile, YES transfer through a hardwired index map forces $s' = s + \widetilde\Theta(m' n) > m'$. Hence $S' < s'$: the gap inverts and the promise problem trivializes. **Consequence: the condensed instance must remain dense** — its domain a noticeable fraction of a full cube — so that Lemma 10.6 leaves room above $S'$. The dense encoding of §10.1 is forced, not chosen.

**10.6.4 Forced randomness [T2 + T1].** By Theorem 10.C, a deterministic condenser would (composed with a derandomized front end, or directly if Theorem 10.A's reduction were derandomized) place us in the regime where NP-hardness of MCSP under deterministic reductions yields breakthrough separations. A correct near-term solution is therefore *expected* to be randomized and instance-adaptive. Conjecture 10.7's shape passes the screen; any proposed deterministic condenser should be treated as a red flag and checked against Theorem 10.C first.

**10.6.5 Relativization ledger [T1].** Lemmas 10.1–10.6 and Theorem 10.4 relativize verbatim (all arguments are syntactic manipulations of circuits with possible oracle gates). Theorem 10.A's proof does not relativize (it must not, by known oracle worlds for MCSP-type problems). Therefore in the composed proof of Proposition 10.8, the entire non-relativizing load is carried by Theorem 10.A *and possibly the condenser*. Whether condensation itself must be non-relativizing is open and is the cleanest first question to attack on the negative side: an oracle separation here would be a publishable theorem mapping where the difficulty lives.

**10.6.6 A conservation heuristic [T3, informal].** Every elementary move examined — fill, shrink, hash, sparsify — *conserves* domain complexity: it reappears as witness size (10.6.2), as gap loss (10.6.3), or as the $\mathrm{dc}$ term itself (10.6.1). We record the heuristic: *domain complexity behaves as a conserved quantity under relativizing, information-oblivious transformations.* If the heuristic is right, a condenser must genuinely *destroy* information — compress the domain's description — which is precisely the kind of operation that Theorem 10.E makes available in worlds without one-way functions. This motivates the route of §10.8.

### 10.7 The enabling sub-conjecture: robust partial hardness [T3]

The NO promise of Gap-pMCSP is brittle: each forbidden circuit may err on a single point. Define the *robust* variant:

> **Gap-pMCSP$_{\delta}[s, S]$.** YES: some circuit of size $\le s$ completes $T$. NO: every circuit of size $\le S$ disagrees with $T$ on $\ge \delta \cdot m(T)$ defined points.

> **Sub-conjecture 10.10 (robust partial hardness).** Theorem 10.A holds for Gap-pMCSP$_{\delta}$ with constant (or mildly shrinking) $\delta$.

Two remarks. First, this may already be implicit in the source: Theorem 10.A is proved via hardness of *learning* programs, and learning-theoretic hardness is naturally an *agreement-gap* statement (no efficient hypothesis achieves good agreement), which is exactly robustness. Verifying this against Hirahara (2022) is checklist item (V3) and is the single highest-value literature check in this chapter. Second, robustness is what makes sampling-based condensation thinkable: with $\delta$-robustness, a candidate simple sub-domain need only retain a $\delta$-fraction witness of *each* of the $2^{O(S \log S)}$ forbidden circuits' error sets, and union bounds over circuits become available — e.g., $O(t)$-wise independent sample sets with $t = \Theta(S \log S)$ have domain indicators of circuit complexity $\mathrm{poly}(t, n)$ and standard tail bounds. The honest accounting: this places $\mathrm{dc}(T') = \mathrm{poly}(S, n)$, while Theorem 10.4 needs $\mathrm{dc}(T') \lesssim S' - s'$; the parameters are within striking distance but not closed, and §10.6.1's warning applies — the sampled domain $D(T) \cap R$ inherits complexity from $D(T)$, so sampling alone does not finish. It must be combined with domain *replacement*, which is where the next section's tools enter.

### 10.8 The proposed route: a win-win on the existence of cryptography [T3]

This section assembles the chapter's components into a concrete attack, with its two open links named. The key strategic observation comes first, because it removes an objection raised twice earlier in this document.

**10.8.1 The branch mismatch dissolves for the Heuristica payout [T1 given T2].** A win-win on "do one-way functions exist?" previously appeared to suffer from mismatched conclusions (worst-case hardness in one branch, average-case in the other). For the specific goal *exclude Heuristica*, the mismatch is illusory:

- **If OWFs exist:** by Theorem 10.F, $\mathsf{DistNP} \not\subseteq \mathsf{AvgBPP}$ directly. Heuristica is excluded *in this branch unconditionally* — no condensation needed.
- **If OWFs do not exist:** Theorem 10.E's toolkit (universal extrapolation, average-case symmetry of information) becomes available to the reduction. If, *using these tools*, Domain Condensation can be carried out in this branch, then Propositions 10.8–10.9 deliver Gap-MINKT NP-hardness *in this branch*, and Theorem 10.B excludes Heuristica given $\mathsf{NP} \not\subseteq \mathsf{BPP}$.

Both branches land on the same statement. Therefore:

> **Proposed Theorem 10.11 [T3 — conditional blueprint].** Assume (L1) robust partial hardness (Sub-conjecture 10.10, MINKT form), and (L2) the no-OWF branch of Domain Condensation below. Then $\mathsf{NP} \not\subseteq \mathsf{BPP} \Rightarrow \mathsf{DistNP} \not\subseteq \mathsf{AvgBPP}$: Heuristica is excluded.

The win-win does not need to prove condensation in *all* worlds — only in worlds without cryptography, where the conservation heuristic of 10.6.6 plausibly fails (information *can* be destroyed, because efficiently generated structure cannot hide).

**10.8.2 The no-OWF condenser (link L2), in detail.** In the no-OWF branch, on instance $T$ drawn from the (samplable!) output distribution of the Theorem 10.A reduction:

1. *Learn the domain.* $D(T)$ is given explicitly; the task is to *compress* it: find a small circuit $\widetilde D$ with $|D(T) \,\triangle\, \widetilde D| \le \varepsilon \, m(T)$. Universal extrapolation (Theorem 10.E) provides exactly this kind of power over samplable distributions: efficiently generated sets cannot be incompressible-on-average. The quantifier caveat is real and must be engineered around: "no OWFs" yields inverters/extrapolators that succeed infinitely often unless one assumes the a.e. form; the standard mitigations (padding tricks; working with the i.o. conclusion since excluding Heuristica is itself an i.o./a.e.-sensitive statement; or running the argument at infinitely many input lengths) are exactly the craft problem, honestly unsolved here.
2. *Replace the domain.* Output $T'$ with domain $\widetilde D$ (simple by construction): $T'(x) = T(x)$ on $D(T) \cap \widetilde D$, and on $\widetilde D \setminus D(T)$ either fill with $0$ or, better, fill by extrapolation. YES transfer: a circuit completing $T$ agrees with $T'$ on all but $\le \varepsilon \, m$ points of $\widetilde D$ — so YES survives in the *approximate* sense.
3. *Absorb the error with robustness.* This is where (L1) pays: with $\delta$-robust NO and $\varepsilon < \delta/2$, the $\varepsilon$-fraction of corrupted points cannot turn a NO instance YES-looking, and the output is a simple-domain instance of the *tolerant* problem (YES: some size-$s$ circuit agrees on $\ge 1 - \varepsilon$ of the domain; NO: every size-$S'$ circuit disagrees on $\ge \delta - \varepsilon$). Zero-fill (Lemma 10.2 adapted to the tolerant setting — the adaptation is routine on the NO side and needs an approximate-witness version on the YES side) then yields a *total* tolerant Gap-MCSP/MINKT instance.
4. *Close the loop.* Tolerant total Gap-MINKT hardness suffices for Theorem 10.B's machinery if (verification item) the 2018 algorithmic side tolerates agreement gaps — plausible, since the 2018 algorithm operates by compression arguments that degrade gracefully, but this is exactly the kind of claim this document refuses to assert without checking.

**10.8.3 What failure teaches.** If (L2) fails *provably* — if even in no-OWF worlds the domain cannot be condensed — that is a theorem of independent significance: it would exhibit a samplable object whose structure is information-theoretically present but average-case-inaccessible despite the absence of cryptography, contradicting the spirit (and possibly the letter, via Theorem 10.D) of the meta-complexity characterizations. The attack is therefore *falsifiable in a productive direction*: its failure modes are themselves results. This is the property one wants in a research target, and the reason this chapter bets on it.

### 10.9 Verification checklist [discharge before claiming anything]

- **(V1)** Hirahara 2022: exact problem formulation (dense table vs. list; MCSP vs. MINKT face), exact gap $(s, S)$, success probability. *Partially discharged (June 2026): venue (FOCS 2022, pp. 968–979) and randomized reduction type confirmed; the gap and encoding remain to be checked, as does the precise division of labor between this paper and Ilango (FOCS 2020) on partial-function hardness.*
- **(V2)** Parameter compatibility in Proposition 10.8: Theorem 10.A's gap must dominate condenser losses $+\ \mathrm{dc} + 1$.
- **(V3)** Whether Theorem 10.A is already *robust* (agreement-gap) as proved — the learning formulation suggests yes; this would discharge (L1) by citation.
- **(V4)** Whether the simple-domain observation (Lemma 10.2 / Theorem 10.4) appears in prior work — check Hirahara 2022, Ilango's papers on partial/conditional variants (his FOCS 2020 paper, "Constant Depth Formula and Partial Function Versions of MCSP are Hard," is the first place to look), and surveys; claim no novelty until checked.
- **(V5)** The MCSP$\leftrightarrow$MINKT bridge for the payout chain: whether Theorem 10.B (2018) applies to Gap-MCSP directly or only Gap-MINKT; whether tolerant versions suffice (10.8.2, step 4).
- **(V6)** Quantifier hygiene for Theorem 10.E in the win-win: i.o. vs. a.e. non-existence of OWFs; match to the i.o./a.e. structure of the Heuristica statement.
- **(V7)** Theorem 10.C's exact reduction classes, to confirm Conjecture 10.7's randomized shape is necessary rather than merely expected.

### 10.10 Summary of the chapter, in five sentences

The values in a partial truth table are free (Lemmas 10.1–10.2); the open problem of total MCSP/MINKT hardness is *exactly* the circuit complexity of the domain (Theorem 10.4). Domain Condensation (Conjecture 10.7) is the well-posed missing step, with forced shape (randomized, dense-output, non-relativizing-or-prove-otherwise) established by elementary computations (§10.6). Robust partial hardness (Sub-conjecture 10.10) is the enabling refinement, possibly already implicit in the literature (V3). The win-win on one-way functions needs condensation only in worlds without cryptography — where the tools to destroy hidden structure provably exist — and both branches land on the same conclusion, excluding Heuristica (Proposed Theorem 10.11). Every component is either proved here, cited with a verification flag, or stated as a falsifiable conjecture whose refutation would itself be a theorem.

---

## Annotated bibliography

*Reliability note: these entries were compiled from the AI assistant's memory. Items marked **[verified 2026-06]** were checked against DBLP/publisher records in June 2026; treat all others as unverified until checked.*

### Textbooks and surveys (start here)

1. **M. Sipser**, *Introduction to the Theory of Computation*, 3rd ed., Cengage, 2012. — The window-lemma proof of Cook–Levin (Theorem 7.37) that Chapters 1–2 rigorize.
2. **S. Arora, B. Barak**, *Computational Complexity: A Modern Approach*, Cambridge University Press, 2009. — The standard graduate text: barriers, PCPs, circuit lower bounds, derandomization.
3. **O. Goldreich**, *Computational Complexity: A Conceptual Perspective*, Cambridge University Press, 2008.
4. **S. Aaronson**, "P ≟ NP," in *Open Problems in Mathematics*, Springer, 2016. — The best single survey of the problem's status and philosophy.
5. **A. Wigderson**, *Mathematics and Computation*, Princeton University Press, 2019. — The field's worldview, by one of its architects.
6. **Simons Institute**, "Meta-Complexity: A Basic Introduction for the Meta-Perplexed," Simons Institute blog, 2024 **[verified 2026-06]**, together with the Simons Institute Meta-Complexity program materials (2023) and Allender's survey (ref. 20). — Orientation for Chapters 4–5.

### Foundations (Chapters 1–2)

7. **S. A. Cook**, "The complexity of theorem-proving procedures," *STOC* 1971. — SAT is NP-complete.
8. **L. A. Levin**, "Universal sequential search problems," *Problemy Peredachi Informatsii* 9(3), 1973. — Independent discovery; universal search (§9.1).
9. **R. M. Karp**, "Reducibility among combinatorial problems," in *Complexity of Computer Computations*, 1972. — The 21 problems; the landscape.
10. **M. R. Garey, D. S. Johnson**, *Computers and Intractability*, Freeman, 1979. — The classic catalogue of NP-completeness.

### Barriers (Chapter 3)

11. **T. Baker, J. Gill, R. Solovay**, "Relativizations of the P =? NP question," *SIAM J. Computing* 4(4), 1975.
12. **A. A. Razborov, S. Rudich**, "Natural proofs," *J. Computer and System Sciences* 55(1), 1997.
13. **S. Aaronson, A. Wigderson**, "Algebrization: a new barrier in complexity theory," *ACM ToCT* 1(1), 2009.
14. **A. A. Razborov**, "Lower bounds on the monotone complexity of some Boolean functions," *Doklady AN SSSR* 281, 1985; and **J. Håstad**, "Almost optimal lower bounds for small depth circuits," *STOC* 1986. — The real lower bounds that exist nearby.
15. **K. D. Mulmuley, M. Sohoni**, "Geometric complexity theory I," *SIAM J. Computing* 31(2), 2001; and **P. Bürgisser, C. Ikenmeyer, G. Panova**, "No occurrence obstructions in geometric complexity theory," *J. AMS* 32, 2019. — The GCT program and the refutation of its occurrence-obstruction route.

### Meta-complexity (Chapter 4)

16. **V. Kabanets, J.-Y. Cai**, "Circuit minimization problem," *STOC* 2000, pp. 73–79. **[verified 2026-06]** — MCSP enters the modern era.
17. **S. Hirahara**, "Non-black-box worst-case to average-case reductions within NP," *FOCS* 2018.
18. **S. Hirahara**, "NP-Hardness of Learning Programs and Partial MCSP," *FOCS* 2022, pp. 968–979. **[verified 2026-06]**
19. **Y. Liu, R. Pass**, "On one-way functions and Kolmogorov complexity," *FOCS* 2020.
20. **E. Allender**, "The new complexity landscape around circuit minimization," *LATA* 2020 (survey).

### Hardness magnification and the locality barrier (Chapter 5)

21. **I. C. Oliveira, R. Santhanam**, "Hardness magnification for natural problems," *FOCS* 2018.
22. **I. C. Oliveira, J. Pich, R. Santhanam**, "Hardness magnification near state-of-the-art lower bounds," *CCC* 2019.
23. **D. M. McKay, C. D. Murray, R. R. Williams**, "Weak lower bounds on resource-bounded compression imply strong separations of complexity classes," *STOC* 2019.
24. **L. Chen, S. Hirahara, I. C. Oliveira, J. Pich, N. Rajgopal, R. Santhanam**, "Beyond natural proofs: hardness magnification and locality," *ITCS* 2020, 70:1–70:48 / *J. ACM* 2022. **[verified 2026-06 (ITCS version)]** — The locality barrier.

### The algorithmic method (Chapter 6)

25. **R. Williams**, "Improving exhaustive search implies superpolynomial lower bounds," *STOC* 2010.
26. **R. Williams**, "Nonuniform ACC circuit lower bounds," *CCC* 2011 / *J. ACM* 61(1), 2014. — NEXP ⊄ ACC⁰.
27. **R. Impagliazzo, V. Kabanets, A. Wigderson**, "In search of an easy witness: exponential time vs. probabilistic polynomial time," *J. CSS* 65(4), 2002. — The Easy Witness Lemma.
28. **C. D. Murray, R. R. Williams**, "Circuit lower bounds for nondeterministic quasi-polytime: an easy witness lemma for NP and NQP," *STOC* 2018. — NQP ⊄ ACC⁰.
29. **R. Beigel, J. Tarui**, "On ACC," *Computational Complexity* 4, 1994. — The structure theorem (with A. Yao's precursor, *FOCS* 1990).
30. **L. Babai, L. Fortnow, C. Lund**, "Non-deterministic exponential time has two-prover interactive protocols," *Computational Complexity* 1, 1991.
31. **N. Nisan, A. Wigderson**, "Hardness vs randomness," *J. CSS* 49(2), 1994; **R. Impagliazzo, A. Wigderson**, "P = BPP if E requires exponential circuits," *STOC* 1997.
32. **L. Chen, H. Ren**, "Strong average-case lower bounds from non-trivial derandomization," *STOC* 2020.

### The TC⁰ frontier (Chapter 7)

33. **R. Impagliazzo, R. Paturi, M. E. Saks**, "Size–depth tradeoffs for threshold circuits," *SIAM J. Computing* 26(3), 1997.
34. **D. M. Kane, R. Williams**, "Super-linear gate and super-quadratic wire lower bounds for depth-two and depth-three threshold circuits," *STOC* 2016.
35. **M. Naor, O. Reingold**, "Number-theoretic constructions of efficient pseudo-random functions," *J. ACM* 51(2), 2004. — PRFs in TC⁰; the barrier's teeth.
36. **L. Chen, R. Tell**, "Bootstrapping results for threshold circuits 'just beyond' known lower bounds," *STOC* 2019.
37. **J. Alman, T. M. Chan, R. Williams**, "Polynomial representations of threshold functions and algorithmic applications," *FOCS* 2016.

### Outside the map (Chapter 9)

38. **S. Ben-David, S. Halevi**, "On the independence of P versus NP," Technion technical report TR-714, 1992.
39. **A. A. Razborov**, "Unprovability of lower bounds on circuit size in certain fragments of bounded arithmetic," *Izvestiya RAN* 59, 1995.
40. **R. Impagliazzo**, "A personal view of average-case complexity," *Structure in Complexity Theory* 1995. — The five worlds.
41. **C. H. Bennett, E. Bernstein, G. Brassard, U. Vazirani**, "Strengths and weaknesses of quantum computing," *SIAM J. Computing* 26(5), 1997. — Grover is optimal.
42. **S. Aaronson, J. Watrous**, "Closed timelike curves make quantum and classical computing equivalent," *Proc. Royal Society A* 465, 2009.
43. **S. Aaronson**, "NP-complete problems and physical reality," *SIGACT News*, 2005.
44. **D. E. Knuth**, "Twenty questions for Donald Knuth," informit.com, 2014. — The contrarian lean toward P = NP.

### Chapter 10 additions (World 3 / Domain Condensation)

45. **R. Ilango**, "Approaching MCSP from above and below: hardness for a conditional variant and AC^0[p]," *ITCS* 2020. — NP-hardness for a conditional variant; one rung of the ladder.
46. **R. Ilango, B. Loff, I. C. Oliveira**, "NP-hardness of circuit minimization for multi-output functions," *CCC* 2020. — Another rung.
47. **W. J. Masek**, "Some NP-complete set covering problems," unpublished manuscript, 1979. — Minimum DNF is NP-hard; the ladder's first rung.
48. **M. Saks, R. Santhanam**, "Circuit Lower Bounds from NP-Hardness of MCSP Under Turing Reductions," *CCC* 2020, 26:1–26:13. **[verified 2026-06]** — Screening theorems (with Murray–Williams, ref. 49) constraining the shape of any hardness proof.
49. **C. D. Murray, R. R. Williams**, "On the (non) NP-hardness of computing circuit complexity," *Theory of Computing* 13(1), 2017 (conference version *CCC* 2015). **[verified 2026-06]** — Screening: deterministic-reduction hardness implies breakthroughs.
50. **R. Impagliazzo, L. A. Levin**, "No better ways to generate hard NP instances than picking uniformly at random," *FOCS* 1990. — Universal extrapolation; the engine of the no-OWF branch.
51. **S. Hirahara**, "Symmetry of information from meta-complexity," *CCC* 2022. — Average-case symmetry of information without one-way functions.
52. **S. Hirahara**, "Average-case hardness of NP from exponential worst-case hardness assumptions," *STOC* 2021. — Heuristica squeezed into the intermediate-time band.
53. **R. Ilango, H. Ren, R. Santhanam**, "Robustness of average-case meta-complexity via pseudorandomness," *STOC* 2022. — OWFs from K^t hardness over samplable distributions.
54. **S. Ben-David, B. Chor, O. Goldreich, M. Luby**, "On the theory of average case complexity," *J. CSS* 44(2), 1992. — DistNP, AvgP, search-to-decision; the formal frame of Chapter 10's payout.
55. **R. Ilango**, "Constant Depth Formula and Partial Function Versions of MCSP are Hard," *FOCS* 2020, pp. 424–433. **[verified 2026-06]** — Partial-function MCSP hardness preceding Hirahara 2022; see checklist item (V1).
56. **S. Hirahara, I. C. Oliveira, R. Santhanam**, "NP-hardness of Minimum Circuit Size Problem for OR-AND-MOD circuits," *CCC* 2018. **[verified 2026-06]** — A rung of the restricted-variant ladder.

### Reading order suggestion

Sipser (1) for Chapters 1–2 → Arora–Barak (2) chapters on barriers → Aaronson's survey (4) for the panorama → Williams (25, 26) and IKW (27) for the engine → Oliveira–Santhanam (21) and the locality paper (24) for the gearbox → Hirahara (17, 18) and Liu–Pass (19) for where the field is going. The Simons Institute's 2023 Meta-Complexity program lectures (freely available) are the best on-ramp to the current frontier.

---

*Document produced from a conversation that began with six tiles of a Turing machine tableau and ended at the edge of provability — which is about the correct blast radius for this problem.*

