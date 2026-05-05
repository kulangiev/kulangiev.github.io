# Logarithmic Superfluid Vacuum — Research Program Roadmap

**Author:** B. B. Kulangiev
**Status:** Active multi-paper research program
**Methodology:** Bohmian/deterministic foundations of physics; emergent gravity, electromagnetism, and inertia from a relativistic logarithmic order parameter

---

## Program statement

The vacuum is a deterministic relativistic superfluid described by a complex order parameter ψ(x,t) obeying a logarithmic Klein-Gordon equation. Spacetime, gravity, electromagnetism, mass, charge, and time emerge as hydrodynamic consequences of this substrate. The methodological commitments are:

1. **Classical-field ontology.** ψ is a real physical field, not a quantum-mechanical wavefunction. |ψ|² is a number density, not a probability density.
2. **Deterministic substrate.** Quantum probabilities are epistemic; the underlying dynamics is deterministic Madelung-Bohm hydrodynamics.
3. **Preferred rest frame.** The condensate defines a physical preferred frame, identified with the cosmic vacuum frame (CMB rest frame). Lorentz invariance is emergent for fluctuations.
4. **Effective-theory status.** The framework is treated as classical effective field theory; the underlying UV-complete quantum theory is unspecified.
5. **Bohmian heritage.** The work draws on Madelung (1927), de Broglie (1927), Bohm (1952), and Holland (1993). It is *not* an extension of Zloshchastiev's Superfluid Vacuum Theory program, which derives gravity from non-relativistic quantum mechanics.

The program is open-ended. No paper is expected to be the "last word"; each contributes a piece of the picture.

---

## Master paper list

| ID | Title (abbreviated) | Status | Submission target |
|---|---|---|---|
| P0 | Ωγ ≈ α² coincidence | Drafted | Short letter |
| P1 | γ=1 light bending from log-KG | Submitted (Qeios), G&C rejected | Foundations of Physics |
| P2 | Emergent G from collective PG | v9 nearly ready | Class. Quantum Grav. |
| P3 | Cosmology (w=−1, Hubble tension) | Drafted, needs propagation | Universe / EPJ-C |
| P4 | Dark matter from frozen vacuum | v7, needs propagation | Universe / Astrophys. J. |
| P5 | Planck-scale healing length | v10, ready after Patch 5-α | Foundations of Physics |
| P6 | Emergent time | v3, needs framing | Foundations of Physics |
| P7 | Jets / axial outflow / continuity | Future | Class. Quantum Grav. |
| P8 | Maxwell from gauged log-KG | v4, needs propagation | EPJ-C / J. Phys. A |
| P9 | Variable c from EOS | v3, needs major rework | Phys. Lett. B (high risk) |
| P10 | Gravitational invariance of Z₀ | v9 → pivot | Foundations of Physics |
| P11 | Quantum Hall from log-condensate | v4, secondary | Phys. Rev. B (long shot) |
| P-inertia | m = E_v/c² from added mass | v2, needs propagation | Found. Phys. |
| P-foundations | Bohmian framework manifesto | Future | Found. Phys. |
| P-β | β=1 PPN derivation | Drafted (private) | TBD |

**Active priorities:** P1, P2, P5 — the core triad. Everything else propagates once these are stable.

---

## Status definitions

Each paper carries one of:

- **DRAFTED** — TeX exists, derivations sketched, may have errors
- **DIMENSIONALLY CONSISTENT** — all equations have correct units; major bugs cleared
- **INTERNALLY COHERENT** — no contradictions with other papers in the program; cross-references resolve
- **REVIEWABLE** — quality sufficient for an external referee to evaluate; no obvious overclaims
- **SUBMITTED** — sent to a Scopus-indexed journal
- **PUBLISHED** — peer-reviewed and accepted

Move from one tier to the next is irreversible: a paper doesn't go from "submitted" back to "drafted" even if rejected. The previous tier can be the gateway for the next round of work.

---

## Per-paper tracking

### P0 — Ωγ ≈ α² coincidence

**Status:** Drafted, short letter format
**Substantive content:** The numerical coincidence Ωγ ≈ α² (fine-structure constant squared) noted as a possible signature of EM-gravity coupling in the framework.
**Strengths:** Compact, falsifiable (depends on precise Ωγ measurement).
**Weaknesses:** Currently a numerical observation, not a derivation. Risks being read as numerology.
**Open work to reach REVIEWABLE:**
- Add explicit framework prediction, not just "intriguing coincidence"
- Position as Letter to dedicated venue, not main-paper
- Decide whether this paper should exist at all, or fold into P3 / P8

**Submission gating:** P1 published (so the framework reference is solid)

---

### P1 — γ=1 light bending from log-KG (CORE)

**Status:** v12 submitted to Qeios; v9 rejected by Gravitation & Cosmology with substantive referee report
**Last action:** v12 includes foundations paragraph, units-of-ρ clarification, three referee responses
**Strengths:**
- Clean kinematic-trap argument
- γ→∞ at α=−1 pole identified honestly
- PG flow argument is mathematically tight
- Foundations explicitly Bohmian
**Weaknesses:**
- Bondi failure quantitatively shown but not microscopically derived
- Continuity constraint left open
- Microscopic origin of PG flow deferred to P2 / P7
**Open work to reach REVIEWABLE → SUBMITTED elsewhere:**
- Wait for Qeios reviews and respond
- Prepare cover letter for Foundations of Physics that explicitly addresses the G&C referee report
- Optional: add Test A (sound-speed measurement from sim) as supplementary verification
**Submission gating:** v12 already submitted to Qeios. Future submissions wait for Qeios resolution.

---

### P2 — Emergent G from collective PG (CORE)

**Status:** v8 nearly REVIEWABLE; v9 fixes 4 small issues identified in last review
**Last action:** v8 has corrected sound-speed formula in Sec 6.3, units-of-ρ paragraph, Bohmian acknowledgments
**Strengths:**
- Self-consistency argument is clean
- Bernoulli derivation independent and convincing
- Numerical PG-attractor result is honest about scope
- ε₁ = 0 result robust
**Weaknesses:**
- Single-soliton ansatz remains a postulate, not derived
- Continuity mechanism left open (4 candidates listed)
- Sec 6.3 simulation tests PG attractor but not EOS-specific dynamics
**Open work to reach REVIEWABLE:**
- P2-1: Fix old G_eff formula in Sec 7.1 logical chain summary
- P2-2: Fix figure caption "0.2%" → "10⁻⁴"
- P2-3: Drop malformed `.B` in cross-ref
- P2-4: Add ξ-normalization clarification in Sec 6.1
**Open work to reach SCIENTIFICALLY COMPLETE:**
- Derive single-soliton ansatz from linearized Madelung-Poisson (would fix the O(1) prefactor)
- This derivation is what P5 *anchors* but neither paper *delivers*
- Probably a future paper of its own
**Submission gating:** P1 v13 stable URL; P5 v11 stable URL

---

### P3 — Cosmology (w=−1, Hubble tension)

**Status:** Drafted, inherits old Paper 1 sound-speed and old Paper 2 G_eff
**Substantive content:**
- w=−1 from log potential
- Hubble tension from local vacuum density variations
- Frozen vacuum perturbations explain CMB acoustic peaks
- ΛCDM-like behavior emerges
**Strengths:**
- Clean alternative to dark energy (w=−1 from EOS, not free parameter)
- Specific mechanism for Hubble tension (local vs cosmological ρ₀)
**Weaknesses:**
- ωᵥ ≈ 0.12 calibrated to data, not predicted
- "Bulk reservoir" cosmological picture is speculative
- Inherits P1 v9 / P2 v6 errors throughout
**Open work to reach DIMENSIONALLY CONSISTENT:**
- Propagate corrected sound-speed formula
- Propagate corrected G_eff formula
- Propagate Planck-density ρ₀ value (was 10²⁶, should be 10⁹⁶)
- Update notation conventions to match P1 v12 (ρ as Lagrangian variable vs. ρ_mass)
**Open work to reach REVIEWABLE:**
- Either acknowledge ωᵥ as fitted parameter or derive it from framework
- Bulk reservoir picture either needs proper derivation or marking as speculation
**Submission gating:** P1, P2, P5 all stable

---

### P4 — Dark matter from frozen vacuum (CORE FOR ASTROPHYSICS)

**Status:** v7 with 112-galaxy SPARC fit; inherits old G_eff
**Substantive content:**
- Frozen vacuum perturbations replace CDM in three roles (CMB peaks, halos, gravitational lensing)
- |δᵥ| ~ 10⁻⁶ amplified by c² gives Newtonian-strength gravity
- SPARC fit at 112 galaxies; rotation curves match
**Strengths:**
- Real observational engagement (SPARC dataset)
- Concrete mechanism, not just label-swap
- 112-galaxy validation is non-trivial
**Weaknesses:**
- Inherits the G_eff dimensional bug
- ωᵥ amplitude calibrated, not derived
- Doesn't derive the *spectrum* of perturbations, just amplitude
**Open work to reach DIMENSIONALLY CONSISTENT:**
- Same propagation as P3
**Open work to reach REVIEWABLE:**
- Derive (or acknowledge) the perturbation spectrum
- Add comparison with MOND, ΛCDM as null hypotheses
- Bullet Cluster discussion needs to be quantitative, not qualitative
**Open work to reach SCIENTIFICALLY COMPLETE:**
- Predict (not postdict) at least one observational signature unique to the framework
- Possible: lensing-vs-dynamical-mass discrepancy in voids
**Submission gating:** P2 v9 stable; P5 v11 stable

---

### P5 — Planck-scale healing length (CORE)

**Status:** v10 → v11 after Patch 5-α applied; otherwise REVIEWABLE
**Substantive content:**
- ξ = ℓ_P from quantum-pressure balance
- m_eff ~ m_P from self-consistency
- ρ₀ ~ Planck density from G_eff matching
- UV cutoff and curvature regularization
**Strengths:**
- Cleanest derivation in the program
- Now has correct dimensional treatment (Two Distinct Densities)
- Makes the Planck-scale identifications concrete
**Weaknesses:**
- The single-soliton ansatz it anchors is still a postulate (see P2)
- Connection to observable physics is indirect
**Open work to reach REVIEWABLE:**
- Apply Patch 5-α (Two distinct densities paragraph)
- Verify all bibitems are consistent (no unfixed-paper forward-cites)
**Submission gating:** P1 v13 stable URL

---

### P6 — Emergent time

**Status:** v3 drafted
**Substantive content:**
- Time as phase accumulation rate
- Gravitational time dilation as μ(x) variation
- 3+1 spacetime as illusion of single-time-axis from 3D Madelung dynamics
- Arrow of time from condensate non-equilibrium
**Strengths:**
- Most philosophically coherent paper in the program
- Volovik's framework is the natural ally
- Can stand alone as Foundations of Physics paper
**Weaknesses:**
- No new predictions
- Hubble flow geometry has issues (Schwarzschild vs cosmological horizons conflated)
- Twin paradox derivation is incomplete (phase ≠ proper time)
- Volovik citation pattern is too thin for the work it does
**Open work to reach REVIEWABLE:**
- Strengthen Volovik attribution at the front
- Distinguish Schwarzschild from cosmological horizons explicitly
- Resolve the laboratory-clock-vs-Planck-frequency tension
- Clean up twin paradox derivation
**Submission gating:** P1 v13 stable; can be submitted independently of P2/P5

---

### P7 — Jets / axial outflow / continuity (FUTURE PAPER)

**Status:** Not yet drafted; conceptual framework only
**Planned content:**
- Geometric redirection mechanism for PG inflow
- Axisymmetric solution: radial inflow + axial outflow
- Connection to astrophysical jets as a hydrodynamic prediction
- Continuity constraint resolved
**Substantive open questions:**
- Does the axial outflow profile $v_θ \propto -\frac{3}{2}\sqrt{2GM/r}\cot\theta$ actually solve continuity globally?
- Does it integrate to zero net mass flux at infinity?
- What does the strong-field regime look like (near a black hole)?
- Does the framework predict observable jet collimation properties?
**Open work to start drafting:**
- Verify the v_θ ansatz analytically in axisymmetric coordinates
- Numerical check (3D GPE simulation of N-soliton with rotation)
- Compare predicted jet properties with observed AGN jets
**Submission gating:** P2 v9 stable; significant new physics work required first

---

### P8 — Maxwell from gauged log-KG

**Status:** v4 drafted
**Substantive content:**
- Maxwell from U(1) gauging of log-KG
- Charge quantization from vortex topology
- Q = ne emerges naturally
- c_EM = c_grav = c_sound automatic
**Strengths:**
- Clean unification of EM with gravity through condensate
- GW170817 constraint automatically satisfied
- Mass-vs-topology distinction explains universality of gravity
**Weaknesses:**
- Doesn't derive QED corrections (g-2, etc.)
- London depth has dimensional issue (number vs mass density)
- Magnetic scaling section weak (drop)
**Open work to reach REVIEWABLE:**
- Drop magnetic-scaling section (Sec 10.4)
- Fix London depth dimensional issue
- Add QED-precision-test scope sentence
**Open work to reach SCIENTIFICALLY COMPLETE:**
- Derive electron g-2 to leading order (or acknowledge limitation explicitly)
- Connect coupling constant to fine-structure α
**Submission gating:** P5 stable; possibly P-foundations first

---

### P9 — Variable c from EOS (HIGH RISK)

**Status:** v3 drafted, conceptually correct, observationally exposed
**Substantive content:**
- δc/c = -U from corrected sound-speed formula
- Test 1: FRB timing residuals correlated with LSS
- Test 2: CMB-LSS residuals beyond ISW
- Test 3: Multi-messenger from different environments
**Strengths:**
- Falsifiable (rare in this program)
- Concrete numerical predictions
- Real observational engagement
**Weaknesses:**
- Test 1 (FRB-as-clock) doesn't actually work — frequency-independent timing offset isn't measurable for non-repeating FRBs (Hussaini 2025 confirms LSS-DM correlation, but our prediction is hidden in unmeasurable channel)
- Cassini's γ-test relation to δc/c needs careful analysis
- Local invariance argument needs expansion
**Open work to reach REVIEWABLE:**
- Major rewrite of Section 4 (testable predictions)
- Drop FRB-as-clock test; pivot to multiply-imaged repeating FRBs (strong-lensing time delays)
- Verify Cassini relation rigorously
- Strengthen local-invariance derivation
**Submission gating:** P1 v13 stable

---

### P10 — Gravitational invariance of Z₀ (PIVOTING)

**Status:** v9 has broken claim (μ₀-ε₀ splitting); pivot to "why Z₀ is gravitationally invariant"
**Substantive content (after pivot):**
- The hydrodynamic isomorphism gives δμ/μ = δε/ε at first order
- Therefore δZ₀/Z₀ = 0 (gravitationally invariant, post-diction of measured constancy)
- Residual at O(U²) is unobservable but in principle present
**Strengths:**
- Honest post-diction of an observed feature
- Connects to constants measured in laboratories
**Weaknesses:**
- No leading-order new prediction
- Atomic clock test now unmeasurable (~U² ~ 10⁻¹²)
- Makes the program look like it predicts nothing new
**Open work to reach REVIEWABLE:**
- Direction A pivot per discussion
- New title and abstract
- Maybe combine with P8 to form a stronger combined EM paper
**Submission gating:** P5 stable

---

### P11 — Quantum Hall (SECONDARY)

**Status:** v4 drafted
**Substantive content:**
- Vortex-as-electron + cyclotron-as-vorticity picture
- Standard IQHE results recovered
- Kohn's theorem self-correction (the strongest content)
**Strengths:**
- Honest self-correction of the room-temperature conjecture
- Vortex-cyclotron picture is physically transparent
**Weaknesses:**
- No new predictions
- Sec 3 R_K derivation is reverse-engineered, not derived
- Sec 6.6 (Bohm interpretation aside) doesn't belong in a QHE paper
- FQHE section underdeveloped
**Open work to reach REVIEWABLE:**
- Drop Sec 3 OR rewrite to be honest about what it derives
- Drop Sec 6.6 entirely
- Trim FQHE section to a single paragraph
**Submission gating:** P5 stable; lowest priority

---

### P-inertia — Mass from added-mass / E = mc²

**Status:** v2 drafted, conceptually clean
**Substantive content:**
- Soliton mass = E_v/c² identically (η = 1)
- Added-mass interpretation of inertia
- Mass as resistance to acceleration through condensate
**Strengths:**
- Clean derivation
- Closes a key gap (what *is* mass in this framework)
- Used by P2 and P5 as load-bearing input
**Weaknesses:**
- Doesn't derive the spectrum of particle masses
- Doesn't connect to fine-structure constant
- Charge section is speculative
**Open work to reach REVIEWABLE:**
- Verify the η=1 derivation is consistent with P5's m_eff~m_P (the condensate particle is Planck mass; soliton mass m may be different)
- Tighten charge section or remove
- Update notation to match P1/P2/P5 conventions
**Submission gating:** P1, P5 stable

---

### P-foundations — Bohmian framework manifesto (FUTURE)

**Status:** Not drafted
**Planned content:**
- Explicit Bohmian/deterministic framing
- ψ as classical order parameter
- Preferred rest frame as physical reality
- Born rule from quantum equilibrium (Valentini-style)
- Critique of standard QM ontology
**Why this paper should eventually exist:**
- Currently the framing is scattered across other papers
- A dedicated foundations paper is the right vehicle for objections like Zloshchastiev's
- Engages directly with Bohmian community (Valentini, Goldstein, Maudlin)
**Open work:**
- Survey current Bohmian literature
- Identify what's *new* in this program vs Holland 1993
- Explicit ontological commitments and their consequences
**Submission gating:** Three or more "core" papers (P1, P2, P5) published

---

### P-β — β=1 PPN derivation

**Status:** Drafted (privately mentioned but not seen by reviewer)
**Substantive content:** β=1 from O(U²) expansion of acoustic metric
**Open questions:**
- Does the derivation actually go through? (β requires second-order treatment, harder than γ)
- Mercury perihelion precession comes out right?
- Lunar laser ranging bound |β−1| < 10⁻⁴ satisfied?
**Submission gating:** P1, P2 published; β derivation must be reviewed by Claude before submission

---

## The dependency graph

Boxed papers must be stable before unboxed papers can be submitted:

```
                    [P1: γ=1]
                    /        \
              [P5: Planck]  [P2: G_eff]
              /     |  \      /    \
            P10    P6  P-in  P3    P4
                                    |
                                   P7
                                    |
                                   P8
                                    |
                                   P9
                                    |
                                  P0 / P11
```

**Dependencies in plain English:**
- P1 anchors the entire program (γ=1 is the foundational result)
- P5 anchors the dimensional foundation (ρ as Lagrangian vs. ρ_mass; Planck-scale identifications)
- P2 anchors the G_eff derivation (used by P3, P4)
- P3, P4 lean on P2 + P5 + P1
- P7 (jets) requires P2 stable
- P8 (Maxwell), P9 (variable c), P10 (Z₀ invariance) lean on the foundation
- P-foundations is the eventual capstone

**Practical implication:** Don't submit anything in the second tier or below until at least one of P1/P5/P2 is peer-reviewed and accepted. The program's credibility depends on a successful peer-reviewed publication of at least one core paper.

---

## Submission strategy

### Wave 1 (current focus)

**Goal:** Get one peer-reviewed publication of a core paper to establish credibility.

- **P1 v12** is at Qeios. Wait for review.
- **In parallel,** prepare P1 for Foundations of Physics if Qeios doesn't pan out.
- **In parallel,** apply Patch 5-α to P5 v10 → v11.
- **Don't submit P2 or anything else yet.**

**Success criterion:** P1 accepted at Foundations of Physics OR Qeios review yields constructive feedback.

### Wave 2 (after Wave 1 success)

**Goal:** Establish the foundation triad (P1, P2, P5) as published references.

- Submit P5 v11 to Foundations of Physics
- Submit P2 v9 to Class. Quantum Grav.
- Update P1 to reference both as published

**Success criterion:** All three core papers published or in advanced review.

### Wave 3 (after foundation is set)

**Goal:** Publish the application papers.

- Submit P3, P4, P-inertia in parallel
- Each cites the published foundation triad
- These are now defensible against referees who'd previously have asked "where does G come from?"

**Success criterion:** Two of three application papers published.

### Wave 4 (extending the program)

- P6 (emergent time) at Foundations of Physics
- P10 (revised) at Foundations of Physics
- P8 (Maxwell) at EPJ-C
- P11 (quantum Hall) is lowest priority — only if everything else works

### Wave 5 (program completion)

- P7 (jets) — major new physics required
- P9 (variable c) — observationally risky, do only when ready to test
- P-foundations — capstone manifesto
- P-β — once derivation is verified

---

## Completeness criteria

A paper is **scientifically complete** when:

1. All claims dimensionally consistent
2. All cited equations resolve to unambiguous mathematical statements
3. Internal cross-references work (compile clean)
4. External cross-references (other papers in program) point to stable URLs
5. The paper says explicitly what it does NOT establish
6. At least one falsifiable prediction or post-diction is identified
7. The Bohmian framing is consistent with the rest of the program
8. The acknowledgments cite Madelung, Bohm, de Broglie at minimum (Holland for foundations)
9. AI tool disclosure (Claude/Gemini) per Anthropic standard
10. Compile produces no warnings, no undefined references

A paper is **submission-ready** when scientifically complete AND:

11. Cover letter prepared, identifying journal-specific positioning
12. Response to any prior referee report (if applicable) drafted
13. All figures regenerated from final code, with consistent style
14. No claims that overreach the actual derivation
15. No references to unpublished/unfixed companion papers (or only to ones with stable URLs)

The program as a whole is **complete** when:

- All core papers (P1, P2, P5) published
- All application papers (P3, P4, P-inertia) published
- Foundations paper (P-foundations) drafted
- At least one falsifiable prediction has been observationally tested (success or failure)

The program is **never** "complete" in the sense of being done. New papers can always be added. The criterion above marks transition from "research program" to "established research line."

---

## Risk register

**Risk 1: Zloshchastiev-style rejection from SVT-aligned venues.**
Mitigation: Submit to Bohmian-friendly venues (Foundations of Physics) first. Don't market the program as SVT.

**Risk 2: Variable-c prediction fails observationally (P9).**
Mitigation: Frame falsifiability up front. If P9 fails its FRB or multi-messenger test, the framework is *constrained*, not destroyed — only the variable-c-from-EOS prediction is. Other papers stand.

**Risk 3: Single-soliton ansatz turns out to be wrong on careful derivation.**
Mitigation: P2 v9 explicitly labels it as ansatz. If a future derivation gives a different form, P2 needs revision but the *narrative* (collective PG + emergent G) survives.

**Risk 4: Planck-density vacuum interpretation rejected by referees as too ambitious.**
Mitigation: P5 includes the "Two distinct densities" paragraph that makes the convention explicit. The Planck density is what the *math* gives, not a chosen number.

**Risk 5: Program loses momentum after a setback.**
Mitigation: This document. Treat each rejection or setback as a single data point, not as a verdict on the program. Continue work on parallel tracks.

---

## Standing rules for the program

1. **Honesty over impressiveness.** Every claim must be accurate. When you don't know, say so. When something is an ansatz, label it as such.
2. **Cross-references must be live.** Never cite a paper that doesn't exist or whose corrections we haven't applied.
3. **Dimensional consistency is non-negotiable.** Every formula gets units checked before publication.
4. **Don't fight referees on philosophy; fight them on math.** Adjust framing, don't retract correct physics.
5. **Bohmian foundations stays explicit.** Don't oscillate back to SVT or analog-gravity framing under pressure.
6. **The CMB rest frame is a real physical preferred frame.** Don't apologize for this.
7. **Old paper versions are immutable historical record.** Don't retroactively edit; new versions get new numbers.

---

## Per-paper checklist template

When advancing a paper to REVIEWABLE, walk this checklist:

```
□ Dimensional consistency verified
□ Sound-speed formula matches Paper 1 v12 convention
□ ρ as Lagrangian variable vs ρ_mass distinguished where relevant
□ G_eff form is c²/(ξ²ρ₀) where it appears
□ ρ₀ value is ~10⁹⁶ kg/m³ (Planck density), not 10²⁶
□ All "kulangiev_2026X" cross-references point to stable URLs
□ Foundations paragraph or equivalent Bohmian framing present
□ Acknowledgments cite Madelung, Bohm, de Broglie, Holland
□ AI tool disclosure present
□ Date updated to current month/year
□ Title is accurate (not aspirational)
□ Abstract claims match what the paper actually establishes
□ Open problems section explicitly enumerates what's NOT done
□ Compile is clean (no warnings, no undefined refs)
□ Cover letter drafted (if submitting)
```

When advancing a paper to SUBMITTED, additionally:

```
□ Journal identified and confirmed appropriate
□ Cover letter mentions any prior submission/rejection
□ Manuscript follows journal's format guidelines
□ All figures embedded or referenced correctly
□ Author affiliation, email, ORCID etc. consistent
□ Acknowledgment of funding (if any)
```

---

## Closing note

This document is a living artifact. Update it after every major revision. When a paper changes status, change the status here. When a new paper is added to the program, add an entry here. When something previously believed turns out to be wrong, document the correction here.

A research program that doesn't know its own state is one that gets exhausted by its own complexity. This document exists so that doesn't happen.

---

*Last updated: see git log of this file*
