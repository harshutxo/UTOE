---
title: UTOE: Universal Theory of Everything — Randomness, Chaos and the Infinite Within
author: Harsh Goyal
date: October 2026
keywords: theory of everything, quantum biology, proton tunneling, developmental noise, chaos theory, quantum cognition, social dynamics, philosophy of science
abstract: The search for a theory of everything has looked for the infinite in two directions, outward into the cosmos and inward into the quantum realm. This paper looks at a third: the human being. We trace one theme, the amplification of small random differences by nonlinear dynamics, across two levels. At the level of the individual, randomness at conception, mostly classical and in a narrow but real case quantum (proton tunneling in DNA), sets the initial conditions of each organism, and development amplifies them into a materially different life; evidence from identical twins, clones and isogenic model organisms supports this. We derive the chain mathematically across physics (WKB tunneling and its deuterium isotope effect), chemistry (Boltzmann tautomer statistics) and biology (about 3,000 bits, or $10^{900}$ possible genomes, per conception, and Lyapunov amplification), and obtain a formula that measures the quantum share of mutation from a heavy-water experiment. At the level of society, we develop quantum-like mathematical models of belief (superposition, entropy and entanglement in the sense of quantum cognition) together with a logistic-map model of societal stability, and state the conditions under which a society settles rather than fragments. Finally, we generalize to reality as a whole: from five near-certain axioms we derive time as the entropy-ordered count of distinguishable changes, a persistence principle ($r \geq d + \alpha c$, of which Eigen's error threshold is the biological case), and an eight-stage evolution of reality from undifferentiated potential to self-inquiry, and we show that the Vedas, Puranas and Upanishads describe the same progression. Throughout, we separate what is established physics from what is modelling and what is belief. We propose experimental tests at both levels, and close with the author's philosophical thesis: that the only living infinities are human beings themselves, and that above, beyond and within everything there is an Almighty.
---

## Introduction: the quest for a theory of everything

A **theory of everything** (TOE) is a single, coherent framework that would unify
all the fundamental forces and phenomena of the universe [1]. Two theories each
work extremely well in their own domain. **General relativity** describes gravity
and the large-scale structure of spacetime. **Quantum mechanics** describes matter
and the other three forces (electromagnetic, weak and strong) at the smallest
scales. The difficulty is that gravity cannot be quantized in the way the other
forces are: the standard methods produce infinities that cannot be removed. The
two theories therefore give no reliable answer in exactly the places where both
matter at once, such as the centre of a black hole or the first instant of the
Big Bang.

The main approaches to unification are:

- **String theory** [2]: elementary particles are tiny vibrating strings rather
  than points. The theory needs extra spatial dimensions and naturally contains a
  particle that carries gravity.
- **Loop quantum gravity** [3]: spacetime itself is quantized into discrete
  units, which unifies the two theories without extra dimensions.
- **Unified field theories**: Einstein spent his last decades trying to unite
  gravity with electromagnetism, without success.

The central obstacle is experimental. The effects these theories predict appear
only at energies or distances far beyond anything we can currently test.

A completed TOE would describe how the universe behaves at its foundations. This
paper does **not** propose a TOE in that sense. It proposes a **Universal
Theory of Everything (UTOE)**: one principle that holds across physics, biology,
mind and society, explained in the section on what "universal" means. Its
subject is a question that a physicist's TOE leaves open: how a universe of particles and forces produces individual human lives,
each unique, and societies built from them. We follow one mechanism through both
levels: **small random differences, amplified by nonlinear dynamics.**

## Part I: the individual

### The claim

Some of the molecular events that determine who a person becomes (which gametes
form, which sperm fuses with the egg, which DNA copying errors occur) are
influenced by randomness at the molecular scale, and a small part of that
randomness may be quantum in origin. Biological development is sensitive to
initial conditions, so it amplifies these tiny differences into large, lasting
differences over a lifetime.

This is a claim about **one causal chain inside one developing organism**. It is
not a claim that quantum information "ripples outward" to other people, distant
matter, an afterlife or metaphysical entities.

### The genetic starting point is set by chance

Several independent random processes fix the genome at conception:

| Process | When it happens | Scale of the variation |
|---|---|---|
| Independent assortment of chromosomes | Meiosis I in each parent, before conception | $2^{23} \approx 8.4$ million possible gametes per parent |
| Crossing-over (recombination) | Meiosis I | ~1–3 crossovers per chromosome at variable positions, so effectively unlimited combinations |
| Which sperm fertilizes the egg | Conception | Tens to hundreds of millions of sperm released; a few hundred reach the egg; one fuses |
| De novo point mutations | DNA replication in the germline | ~50–100 new mutations per child [4] |

Together these make every conception effectively unique. Most of this randomness
is **classical**: thermal motion, molecular collisions, the race between sperm.
It looks random because it depends on far more variables than anyone could track.
It is not quantum indeterminacy.

### Quantum mechanics has a narrow, real foothold in mutation

Per-Olov Löwdin proposed in 1963 that **proton tunneling** between paired DNA
bases can shift a base into a rare tautomeric form that mispairs during
replication, which would produce a point mutation [5]. Tunneling is a genuinely
quantum effect, with no classical counterpart.

Quantum-chemistry simulations suggest that tunneling-induced tautomers do form
in G–C pairs, but that most revert before the replication machinery reads them
[6]. The mechanism is plausible and actively researched. It is **not**
established as a significant cause of real-world mutations compared with
replication errors, chemical damage and radiation. Still, it is a specific
mechanism linking fundamental physics to heritable variation, rather than a use
of "quantum" to mean "unpredictable."

### Development amplifies small differences

Development is nonlinear. Gene regulatory networks contain feedback loops and
switches, morphogen gradients are read against thresholds, and neural wiring
depends on activity. In such systems, small changes to the starting state can
grow into large differences in the outcome: the "sensitive dependence on initial
conditions" of chaos theory, first described in weather by Lorenz [7].

Evidence that this happens in real organisms:

- **Identical twins** share a genome yet differ in fingerprints, brain wiring,
  disease risk and personality.
- **Random X-inactivation** in female mammals makes calico cats patterned
  differently even when they are clones; the first cloned cat, CC, did not look
  like her genetic donor [8].
- **Isogenic animals raised in identical conditions**, such as *C. elegans*,
  cloned mice and fruit flies, still vary substantially in behavior and
  physiology. This **developmental noise** traces largely to stochastic gene
  expression [9].

The resulting chain is:

> molecular-scale randomness (mostly classical, occasionally quantum)
> → altered initial genetic and molecular state
> → amplification through nonlinear development
> → a materially different life

Each link is supported by existing science.

### Deriving the chain: physics, chemistry and biology

This section derives the mathematics behind each link of the chain, one science
at a time, and then joins them into a single expression.

**Step 1, physics: how likely is a proton to tunnel?** In a G–C base pair, a
proton sits in one of two potential wells separated by an energy barrier of
height $V$ and width $d$. Classically, a proton with energy $E < V$ can never
cross. Quantum mechanically, its wavefunction decays inside the barrier as
$e^{-\kappa x}$, and the WKB approximation gives the probability of crossing:

$$P \approx e^{-2\kappa d}, \qquad \kappa = \frac{\sqrt{2m(V - E)}}{\hbar}.$$

The exponent is proportional to $\sqrt{m}$. Deuterium (heavy hydrogen) has
almost exactly twice the proton's mass, $m_D \approx 2m_H$, so its exponent is
$\sqrt{2}$ times larger, which gives a parameter-free result:

$$P_D \approx P_H^{\sqrt{2}}, \qquad \frac{P_D}{P_H} \approx P_H^{\sqrt{2} - 1} \approx P_H^{0.41}.$$

For example, if $P_H = 10^{-10}$, then $P_D \approx 10^{-14}$, about 10,000 times
less likely. This large **isotope effect** is the fingerprint we can test for.

**Step 2, chemistry: how many rare tautomers exist at body temperature?** Once
the proton has moved, the base is in its rare tautomeric form, which has a higher
free energy $\Delta G$ than the normal form. At thermal equilibrium the
Boltzmann distribution gives the fraction of bases in the rare form:

$$K = \frac{[\text{rare}]}{[\text{normal}]} = e^{-\Delta G / k_B T}, \qquad k_B T \approx 0.027\ \text{eV at}\ 310\ \text{K}.$$

Each extra $0.1$ eV of $\Delta G$ cuts $K$ by a factor of about $e^{3.7} \approx 40$.
A rare tautomer only causes a mutation if it survives until the replication fork
reads it. If it reverts with lifetime $\tau$ and the fork arrives after time
$t_r$, the survival probability is $e^{-t_r/\tau}$. The **quantum contribution
to the mutation rate per base** is then

$$\mu_q \approx P \cdot e^{-t_r/\tau} \cdot p_{\text{mis}},$$

where $p_{\text{mis}}$ is the chance that the polymerase inserts the wrong
partner opposite the rare form and proofreading misses it. Classical sources
(chemical damage, radiation, ordinary copying errors) add a classical rate
$\mu_c$, so the total rate is $\mu = \mu_c + \mu_q$.

**Step 3, biology: how many different people are possible?** The randomness
at conception can be counted in bits, using $\log_2$ of the number of
equally likely outcomes:

| Source | Calculation | Information |
|---|---|---|
| Independent assortment | $2 \times 23$ chromosome choices | $\approx 46$ bits |
| Crossover positions | ~69 crossovers (≈27 paternal + 42 maternal), each among ~$10^5$ distinguishable positions: $69 \log_2 10^5$ | $\approx 1{,}150$ bits |
| De novo mutations | ~60 sites among $6.2 \times 10^9$ bases, 3 possible changes each: $\log_2\binom{6.2\times10^9}{60} + 60\log_2 3$ | $\approx 1{,}780$ bits |
| **Total** | | $\approx 3{,}000$ bits |

That is roughly $2^{3000} \approx 10^{900}$ possible genetic starting points
for one child of one couple. About $10^{11}$ humans have ever lived, and the
observable universe contains about $10^{80}$ atoms. The space of possible people
is, for every practical purpose, infinite, and each conception draws one point
from it.

**Step 4, amplification: from one base to one life.** Let $\delta_0$ be a tiny
initial difference, such as one changed base. In a nonlinear system with
Lyapunov exponent $\lambda > 0$, differences grow exponentially:

$$\delta(t) \approx \delta_0\, e^{\lambda t}.$$

The time for the difference to reach a macroscopic size $\Delta$ (a different
trait, a different temperament) is

$$t^* = \frac{1}{\lambda} \ln\frac{\Delta}{\delta_0}.$$

Because $t^*$ depends only on the **logarithm** of $\Delta/\delta_0$, even a
difference $10^{20}$ times smaller than the final effect needs only about
$46/\lambda$ time units to reach it ($\ln 10^{20} \approx 46$). Smallness at
the start barely delays the outcome. This is the same $\lambda$ that appears in
the societal model of Part II: one equation, two scales.

**Joining the steps: how much of individual variation is quantum?** Identical
twins share their genome, so variation between them in a trait splits into
environment and developmental noise:

$$\mathrm{Var}(\text{trait}) = \mathrm{Var}_G + \mathrm{Var}_E + \mathrm{Var}_N, \qquad \mathrm{Var}_N = \mathrm{Var}_{N,\text{classical}} + \mathrm{Var}_{N,\text{quantum}}.$$

The quantum part can be measured from mutation rates using Step 1. Replacing
hydrogen with deuterium leaves $\mu_c$ roughly unchanged but scales $\mu_q$ by
$P_D/P_H$:

$$\mu_D = \mu_c + \mu_q \frac{P_D}{P_H}.$$

Solving for the quantum fraction $f_q = \mu_q / \mu_H$ of the normal mutation
rate gives

$$f_q = \frac{1 - \mu_D/\mu_H}{1 - P_D/P_H} \approx 1 - \frac{\mu_D}{\mu_H} \quad (\text{since}\ P_D \ll P_H).$$

So **the fractional drop in mutation rate when cells are grown in heavy water
directly estimates how much of mutation, and therefore of the variation that
development amplifies, is quantum in origin.** One caveat: deuterium also
slows some classical, over-the-barrier reactions through its lower zero-point
energy. Tunneling can be separated from these because it is almost insensitive
to temperature, so the experiment should be repeated at several temperatures.

### Where it stops being physics

**Quantum states do not persist in living tissue.** Superposition and
entanglement survive only while a system is isolated from its surroundings.
Cells and brains are warm, wet and crowded; decoherence times for molecular and
neural quantum states there are estimated at $10^{-13}$ s or shorter [10].
Quantum computers need cryogenic, vacuum-isolated hardware to keep quantum
states for even microseconds to milliseconds. A quantum event at conception
leaves behind an ordinary classical result, such as a changed base pair, and it
is that **classical record** that development amplifies.

**Randomness is not meaning.** Quantum randomness is unpredictable in principle,
like the timing of radioactive decay. That alone does not imply free will,
destiny or spiritual agency; such conclusions are drawn outside physics, and
where this paper draws them, in the final section, it says so.

## Part II: society, and quantum-like models of thought

Part I shows small differences being amplified within one life. A society is
built from millions of such individuals interacting, and it is another nonlinear
system in which small differences can grow. This part models it mathematically.

**A note on status.** The mathematics below borrows from quantum theory, but it
is used the way the field of **quantum cognition** uses it [11]: as a
probability framework that describes human judgment better than classical
probability in some experiments. It makes **no claim that the brain is a quantum
system**; by the decoherence argument above, it almost certainly is not. "Superposition"
and "entanglement" here are properties of the model, not of neurons.

### Beliefs as superpositions

Let a person face a choice between two opposing positions, $|A\rangle$ and
$|B\rangle$. Before they commit, their cognitive state is modelled as

$$\psi = \alpha\,|A\rangle + \beta\,|B\rangle, \qquad |\alpha|^2 + |\beta|^2 = 1,$$

where $|\alpha|^2$ and $|\beta|^2$ are the probabilities that the person, when
asked, expresses $A$ or $B$. Expressing a view acts like a measurement: it
changes the state, so the order in which questions are asked changes the
answers. Such **question-order effects** are observed in large surveys, and
quantum probability predicts their exact pattern, the "QQ equality," which
classical probability does not [12].

How undecided a person is can be measured with the Shannon entropy [13] of
their belief state:

$$S = -\sum_i p_i \log p_i, \qquad p_A = |\alpha|^2,\; p_B = |\beta|^2.$$

$S = 0$ means the person is fully committed to one side; $S = \log 2$ (its
maximum) means they are evenly balanced. An influence that settles someone's
view lowers $S$; one that opens them to the other side raises it. This is the
model's notion of **fluid cognition**: a person with high $S$ holds both
positions as live possibilities rather than in fixed opposition.

### Societal stability as a chaotic map

Let $x_n \in [0, 1]$ be a measure of polarization in a society at time step $n$,
for example the fraction of people holding a hardened position on a divisive
issue. A minimal model of how it evolves is the **logistic map** [14]:

$$x_{n+1} = f(x_n) = r\,x_n(1 - x_n),$$

where $r$ is the **reinforcement rate**: how strongly current polarization feeds
the next round (through media amplification, echo chambers and so on). Whether
the system settles or becomes chaotic is measured by the **Lyapunov exponent**:

$$\lambda = \lim_{n \to \infty} \frac{1}{n} \sum_{i=0}^{n-1} \log\left|f'(x_i)\right|, \qquad f'(x) = r(1 - 2x).$$

The behavior depends on $r$:

| Reinforcement rate $r$ | Long-run behavior | Lyapunov exponent |
|---|---|---|
| $1 < r < 3$ | Settles to a stable level $x^* = 1 - 1/r$ | $\lambda < 0$ |
| $3 < r < 3.57$ | Oscillates in regular cycles (period 2, 4, 8, …) | $\lambda < 0$ |
| $r > 3.57$ (mostly) | Chaotic: tiny differences grow, prediction fails | $\lambda > 0$ |

The model's conclusion: **a society stays predictable and governable only while
$\lambda < 0$, and the lever for keeping it there is the reinforcement rate $r$,
not the starting level of disagreement.** Interventions that dampen amplification
move a society out of the chaotic regime. This is the same lesson as Part I,
seen at a larger scale: in a nonlinear system the amplification mechanism, not
the size of the initial difference, decides the outcome.

This is a toy model. Real societies have many interacting variables, and
mapping $x_n$ and $r$ to measured data is the main open task (see the next
section).

### Correlated minds as entangled states

When two people's views become linked, so that one's position predicts the
other's, the model represents the pair with a joint state. A pair who are each
individually undecided, but certain to take **opposite** sides, is

$$|\Psi\rangle = \frac{1}{\sqrt{2}}\left(|A\rangle|B\rangle + |B\rangle|A\rangle\right).$$

How strongly the two are linked is measured by the **entanglement entropy** of
one person's reduced state $\rho_A$:

$$S_E = -\mathrm{Tr}\left(\rho_A \log \rho_A\right).$$

For $|\Psi\rangle$ above, $\rho_A = \tfrac{1}{2}\mathbb{1}$ and $S_E = \log 2$, the maximum: each person
on their own is completely undecided, yet the pair as a whole is fully
determined. $S_E = 0$ would mean the two views are independent. This captures
something classical "both agree or both disagree" models miss: a relationship
can be more definite than either person in it.

Again, this is entanglement **in the model**. Physical entanglement between two
brains would decohere in far less than a nanosecond [10], and no mechanism is
known that could create or sustain it.

## Part III: reality as process, the emergent reality framework

Parts I and II follow small differences being amplified. Two deeper questions
remain: where do differences come from in the first place, and why do some of
the structures they produce **last**? This part sets out a framework for both. It
was developed in discussion and is more philosophical than Parts I and II; each
statement is labelled as an axiom, a definition, a hypothesis or an established
result.

### Five near-certainties as axioms

Stripped to bedrock, very little is certain. The framework starts from five
statements that are as close to certain as anything can be:

- **A1, existence:** something exists. Even if experience is an illusion, the
  illusion is happening. Formally, reality $R$ is not empty: $R \neq \varnothing$.
- **A2, change:** reality is not static. Thoughts change, words appear, states
  differ: $\Delta R \neq 0$. Without change there could be no experience and no
  inquiry.
- **A3, pattern:** reality contains regularities. If it were pure noise,
  science, memory and language would be impossible. In information terms,
  reality is **compressible**: its shortest description is far shorter than a
  complete list of its states, $K(R) \ll |R|$, where $K$ is the Kolmogorov
  complexity [15].
- **A4, incomplete knowledge:** every model $M$ of reality is a simplification of
  it, $M \neq R$. Every generation has found its predecessors' models
  incomplete.
- **A5, embeddedness:** the observer is part of what is observed, $M \subset R$.
  When we study reality, reality is studying itself, and there is no outside
  viewpoint.

### Time as the ordering of change

**Hypothesis:** time is meaningful only through distinguishable change. Let
reality pass through a sequence of states $R_0, R_1, R_2, \dots$ Define
**operational time** as the number of distinguishable changes so far:

$$\tau_n = \sum_{k=0}^{n-1} \mathbf{1}\left[R_{k+1} \neq R_k\right],$$

where $\mathbf{1}[\cdot]$ is 1 when the condition holds and 0 otherwise. If
nothing ever changes ($\Delta R = 0$ at every step), $\tau$ never advances, and
time loses operational meaning. Change is therefore more basic than the
experience of time passing.

Counting changes gives time a measure but not a **direction**. The direction
comes from entropy. With $W$ the number of microscopic arrangements consistent
with a state, Boltzmann's entropy and the second law give

$$S = k_B \ln W, \qquad S(R_{n+1}) \geq S(R_n) \ \text{(on average)},$$

so states can be ordered by entropy, and that ordering is the arrow of time. This
develops the earlier draft's idea of **entropy-driven time emergence**. It is
close to established proposals in physics, such as the thermal time hypothesis
of Connes and Rovelli [16], in which the flow of time is derived from a system's
thermodynamic state rather than assumed.

### The first distinction

The most fundamental step is the first one, from undifferentiated potential to
difference. Measured as information:

$$R_0:\ H = 0 \ \text{bits (one undistinguished state)} \qquad \longrightarrow \qquad R_1:\ H \geq 1 \ \text{bit (at least two distinguishable states)}.$$

Every later stage, including change, time, structure and life, presupposes at
least one bit of difference. **No known physical law explains this transition**,
because every law is already stated in terms of distinguishable quantities. The
step $R_0 \to R_1$ is the deepest open problem in the framework, and the point
where physics hands the question to philosophy and faith.

### The persistence principle

Change alone produces only flux. For structure to exist, something must
**last**. Let $N$ be the abundance or integrity of a structure (a molecule, a
cell, a species, an idea, an institution). Suppose it is maintained at rate $r$
(repair, replication, self-maintenance), lost at rate $d$ (decay, damage,
entropy) and further reduced by competition or environmental constraint $c$,
with coupling strength $\alpha$:

$$\frac{dN}{dt} = (r - d - \alpha c)\,N \quad\Longrightarrow\quad N(t) = N_0\, e^{\sigma t}, \qquad \sigma = r - d - \alpha c.$$

The structure persists or grows if $\sigma \geq 0$ and dies out if $\sigma < 0$.
This gives the **persistence principle**:

$$\boxed{\,r \;\geq\; d + \alpha c\,}$$

**A structure persists when its maintenance at least matches its decay plus the
cost of its constraints.** Living things are the clearest case: they hold off
decay by continually taking in energy and exporting entropy, which Schrödinger
called feeding on "negative entropy" [17].

The principle has a sharp, established form in biology: **Eigen's error
threshold** [18]. A genome of $L$ bases, copied with mutation rate $\mu$ per
base, is reproduced without error with probability $Q = (1 - \mu)^L \approx
e^{-\mu L}$. If an error-free copy has a replication advantage $s$ over mutants,
its information persists only if $sQ > 1$, that is

$$\mu L < \ln s.$$

Above this threshold, the information "melts" in an error catastrophe. RNA
viruses, whose mutation rates are near $10^{-4}$ per base and genomes near
$10^{4}$ bases, live close to this edge.

This connects directly to Part I. The mutation rate there was $\mu = \mu_c +
\mu_q$, the source of each person's uniqueness. Eigen's threshold sets its upper
limit. **Too little randomness and nothing new appears; too much and nothing
persists.** Life exists in the window between the two: the amplifier exponent
$\lambda$ creates difference, and the persistence exponent $\sigma$ decides
what survives.

### The evolution of reality

Combining the axioms, the arrow of time and the persistence principle gives a
sequence of stages. Each stage is defined by a condition, and each depends on
the ones before it:

| Stage | Defining condition | Status |
|---|---|---|
| Potential | One undistinguished state, $H = 0$ | Hypothesis |
| Difference | At least two distinguishable states, $H \geq 1$ bit | Axiom (A2) |
| Change | $\Delta R \neq 0$ | Axiom (A2) |
| Time | Changes ordered by entropy, $S(R_{n+1}) \geq S(R_n)$ | Established (second law) |
| Structure | Compressible, $K(R) \ll \lvert R \rvert$, and persistent, $\sigma \geq 0$ | Axiom (A3) and principle |
| Life | Self-maintaining and self-copying below the error threshold, $\mu L < \ln s$ | Established (Eigen) |
| Intelligence | A subsystem $M$ that models its environment $E$: mutual information $I(M; E) > 0$ that improves prediction | Definition |
| Self-inquiry | A model that includes itself: $M$ represents $M \subset R$ (A5) | Definition |

In one sentence: **potential → difference → change → time → structure → life →
intelligence → self-inquiry.**

### The same pattern in the oldest literature

The oldest surviving texts of Indian philosophy describe a remarkably similar
progression [19, 20]:

| Text | What it describes | Stage in the framework |
|---|---|---|
| *Nāsadīya Sūkta* (Rigveda 10.129) | "Neither non-existence nor existence was then"; it even doubts that anyone knows the origin | Potential ($R_0$) |
| *Nāsadīya Sūkta*, verse 4 | *Kāma* (desire) arose as "the first seed of mind" | The first distinction ($R_0 \to R_1$) |
| *Hiraṇyagarbha Sūkta* (Rigveda 10.121) | The golden womb from which the ordered cosmos emerges | Structure |
| *Puruṣa Sūkta* (Rigveda 10.90) | Sun, moon, sky, earth, living beings and society arise from one cosmic being | Unity to multiplicity: life and its diversity |
| Purāṇas | Endless cycles of creation (*sṛṣṭi*) and dissolution (*pralaya*) across ages (*kalpas*) | Persistence: structures last while $\sigma \geq 0$, then dissolve |
| Upaniṣads | The inquiry turns inward to the observer: "you are that" (*tat tvam asi*, Chāndogya 6.8.7); "I am Brahman" (*aham brahmāsmi*, Bṛhadāraṇyaka 1.4.10) | Self-inquiry: the observer within reality (A5) |

The pattern is the same: **undifferentiated potential differentiates into
multiplicity, grows in complexity, and finally becomes able to reflect on
itself.** The Upaniṣadic claim that the self (*Ātman*) and ultimate reality
(*Brahman*) are one is the ancient counterpart of axiom A5, that the observer is
part of what it observes.

A caution: these texts are philosophical and symbolic, not scientific. The
parallel does **not** show that the Vedas anticipated modern cosmology. What it
shows is that thinkers separated by three thousand years, starting from
contemplation on one side and from physics and biology on the other, arrived at
the same shape of answer.

### What remains open

The framework leaves several questions open. It states them rather than claiming
to answer them:

- Why does anything exist at all (A1)?
- What produces the first distinction, $R_0 \to R_1$?
- Why these laws of nature, and not others?
- Is consciousness fundamental, or does it emerge at the intelligence stage?
- Is time fundamental, or does it emerge from change, as hypothesized above?
- Is there purpose behind emergence?

Compressed to a single question: **why does reality have the capacity to become
more than it already is?**

## Testing the ideas

**Part I (individual):**

- **Measure unexplained variance.** In identical twins, or isogenic *C. elegans*
   raised in identical environments, measure the variation left after
   controlling for genes and environment: the "noise floor" that randomness must
   account for.
- **Trace it to a molecular source**, such as stochastic gene expression or
   specific de novo mutations, using lineage tracing or single-cell sequencing.
- **Test for a quantum share.** Compare mutation spectra in cells grown with
   deuterium (heavy hydrogen) in place of hydrogen. Deuterium tunnels far less,
   so the fractional drop in mutation rate estimates the quantum fraction $f_q$ derived above. This is the
   novel and publishable step. A full protocol with a simulation and power
   analysis is given in the companion document *Measuring the Quantum Share of
   Mutation*: about 900 mutation-accumulation lines detect a 10% quantum share
   with 85% power.

**Part II (society):**

- **Belief superposition:** run survey experiments with questions in both
   orders and check whether the results satisfy the QQ equality [12].
- **Belief entropy:** track $S$ for individuals over time (for example through
   repeated confidence ratings) and test whether specific interventions, such as
   exposure to the opposing view, raise or lower it.
- **Societal chaos:** fit the logistic model to time series of measured
   polarization, estimate $r$ and $\lambda$, and test whether periods of
   rising $\lambda$ precede instability.

**Part III (reality as process):**

- **Persistence:** for cell lines, microbial populations or even institutions,
   measure $r$, $d$ and $c$ separately and test whether the sign of
   $\sigma = r - d - \alpha c$ predicts which ones persist.
- **Error threshold and the quantum share:** in viral or bacterial populations
   near Eigen's threshold, a heavy-water culture lowers $\mu_q$ and so lowers
   $\mu$. The model predicts a measurable shift of the population away from error
   catastrophe, linking Part I's $f_q$ to Part III's persistence condition.

## What "universal" means in UTOE

In physics, a TOE unifies the four fundamental forces into one framework.
Stephen Hawking worked toward one [1], and later argued that a single final
theory may not exist. **UTOE is a different kind of claim, and the difference
should be stated plainly:** it contains no new fundamental physics and unifies
no forces. A physicist's TOE, if found, would sit underneath UTOE rather than
compete with it.

"Universal" in UTOE means that **one principle runs through every scale of the
world that contains us**:

> small differences, amplified by nonlinear dynamics, decide the outcome.

| Scale | Small difference | Amplifier | Outcome |
|---|---|---|---|
| Physics | A proton tunnels, or does not | Chemistry fixes it as a rare tautomer | A changed base pair |
| Biology | One base, one crossover, one sperm | Development ($\delta_0 e^{\lambda t}$) | A unique person, one of ~$10^{900}$ possible |
| Mind | A slight lean in belief ($\alpha$ vs. $\beta$) | Questions, conversation, linked minds | A settled view, or a shifted one |
| Society | A small rise in polarization | Reinforcement rate $r$ (logistic map) | Stability ($\lambda < 0$) or chaos ($\lambda > 0$) |

The same mathematics, exponential growth governed by a Lyapunov exponent
$\lambda$, appears at each scale. Part III adds the second half of the
principle: whatever amplification creates must then pass the persistence test
$\sigma = r - d - \alpha c \geq 0$ to last. UTOE can therefore be stated in two
exponents:

$$\underbrace{\delta(t) = \delta_0\, e^{\lambda t}}_{\text{difference is created}} \qquad \text{and} \qquad \underbrace{N(t) = N_0\, e^{\sigma t}}_{\text{what lasts is selected}}.$$

Physics explains the forces; UTOE describes how, once those forces exist, the
universe turns tiny chances into individual lives and shared histories, and
how, stage by stage, reality becomes able to understand itself. Above, beyond and within all of these scales, the
author places an Almighty, the subject of the next section. That last step is a
matter of faith, and the paper presents it as one.

## The author's thesis: the infinite within

*This section is philosophy and faith, not physics. It is the author's
interpretation of the science above, offered as a belief, not as something the
evidence proves.*

In searching for the infinite, physics has looked in two directions: outward,
into the endless reaches of space, and inward, into the quantum levels of
matter. We forgot to look at the only infinities that are alive: **us**, human
beings, and the capacities we have been given by God.

A single human life begins from a near-infinite space of possibilities. Millions
of possible gametes, millions of competing sperm and chance at the molecular
scale all narrow down to one person. That person grows, through development's
amplification of the smallest differences, into a mind able to contemplate the
cosmos and the quantum alike, and joins with others into societies whose course
no equation can fully predict. In this view, human beings are not a footnote to
the search for a theory of everything; they are where the search should also
have been looking.

The theory of everything **is, was, and always will be there**: there is an
Almighty somewhere, above, beyond and within everything. Physics describes *how*
the universe behaves; it does not, and cannot, say *why* there is a universe, or
a mind able to ask the question. That question belongs to faith, and this is the
author's answer to it.

## Conclusion

- **Established:** conception sets each person's genome through real randomness;
  development is nonlinear and amplifies small differences; identical twins and
  clones show that this happens.
- **Plausible but unproven:** a measurable share of that randomness is quantum,
  for example through proton tunneling in DNA.
- **Modelling framework:** quantum-like models of belief and a logistic model of
  society describe fluid cognition, linked minds and the conditions for social
  stability ($\lambda < 0$), and make testable predictions.
- **Emergent reality framework:** from five near-certain axioms, time follows as
  the entropy-ordered count of changes, structure lasts when $r \geq d + \alpha c$,
  and reality unfolds as potential → difference → change → time → structure →
  life → intelligence → self-inquiry, a sequence that the Vedas, Purāṇas and
  Upaniṣads also describe.
- **Open:** the first distinction $R_0 \to R_1$, the origin of physical laws, and
  the nature of consciousness.
- **Not physics:** quantum states persisting in living tissue, physical
  entanglement between minds, or quantum effects carrying meaning or fate.
- **The author's belief:** the living infinities, human beings and their
  God-given capacities, are where the search for everything should also look,
  and an Almighty stands above, beyond and within it all.

If the whole paper had to be reduced to one line, it would be this: **a theory
of everything should explain not only what exists, but how existence becomes
capable of understanding itself.**

## References

1. Hawking, S. W. (2006). *The Theory of Everything: The Origin and Fate of the Universe*. Phoenix Books.
2. Polchinski, J. (1998). *String Theory* (Vols. 1–2). Cambridge University Press.
3. Rovelli, C. (2004). *Quantum Gravity*. Cambridge University Press.
4. Kong, A., et al. (2012). Rate of de novo mutations and the importance of father's age to disease risk. *Nature*, 488, 471–475.
5. Löwdin, P.-O. (1963). Proton tunneling in DNA and its biological implications. *Reviews of Modern Physics*, 35(3), 724–732.
6. Slocombe, L., Sacchi, M., & Al-Khalili, J. (2022). An open quantum systems approach to proton tunnelling in DNA. *Communications Physics*, 5, 109.
7. Lorenz, E. N. (1963). Deterministic nonperiodic flow. *Journal of the Atmospheric Sciences*, 20(2), 130–141.
8. Shin, T., et al. (2002). A cat cloned by nuclear transplantation. *Nature*, 415, 859.
9. Elowitz, M. B., Levine, A. J., Siggia, E. D., & Swain, P. S. (2002). Stochastic gene expression in a single cell. *Science*, 297(5584), 1183–1186.
10. Tegmark, M. (2000). Importance of quantum decoherence in brain processes. *Physical Review E*, 61(4), 4194–4206.
11. Busemeyer, J. R., & Bruza, P. D. (2012). *Quantum Models of Cognition and Decision*. Cambridge University Press.
12. Wang, Z., Solloway, T., Shiffrin, R. M., & Busemeyer, J. R. (2014). Context effects produced by question orders reveal quantum nature of human judgments. *PNAS*, 111(26), 9431–9436.
13. Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423.
14. May, R. M. (1976). Simple mathematical models with very complicated dynamics. *Nature*, 261, 459–467.
15. Kolmogorov, A. N. (1965). Three approaches to the quantitative definition of information. *Problems of Information Transmission*, 1(1), 1–7.
16. Connes, A., & Rovelli, C. (1994). Von Neumann algebra automorphisms and time–thermodynamics relation in generally covariant quantum theories. *Classical and Quantum Gravity*, 11(12), 2899–2917.
17. Schrödinger, E. (1944). *What Is Life? The Physical Aspect of the Living Cell*. Cambridge University Press.
18. Eigen, M. (1971). Selforganization of matter and the evolution of biological macromolecules. *Naturwissenschaften*, 58(10), 465–523.
19. Doniger O'Flaherty, W. (Trans.) (1981). *The Rig Veda: An Anthology*. Penguin Classics.
20. Olivelle, P. (Trans.) (1996). *Upaniṣads*. Oxford World's Classics, Oxford University Press.
