---
id: s-crit-residual
type: study
phase: 1
status: drafted
primary_outcome: Whether the model's actions deviate in the direction the decoded belief deviates from the true posterior.
grounding: derived
depends_on: [{node: r-phase-c-stakevec, edge: needs}, {node: c-inst-derived, edge: needs}, {node: c-inst-grounded, edge: calibrates}]
---

## Purpose

Validates the probe rather than the model, and does so without depending on any control condition. Precondition for the testimony work in later phases.

## Content

Fourth of the four criteria — promoted from "arguably a criterion" to a full member of the set in the reconciled amendments (R15), since the testimony work in phase 3 already treats it as a precondition, which is a stronger claim than arguable. On `r-phase-c-stakevec` checkpoints: examine the probe's residuals — the specific ways the decoded belief departs from the true posterior — and ask whether the model's *actions* follow those departures rather than the true value.

**Primary outcome, precisely.** Whether the model's actions deviate in the direction the decoded belief deviates from the true posterior. The motivating problem: the probe is fit to predict the true posterior, so the decoded belief is regularized toward truth by construction, and a *systematically wrong* internal belief is invisible to ordinary decodability measurement. Residual-following closes that gap. Noise should not predict behaviour; a genuine internal state should.

**What a positive result validates, precisely — this is easy to overstate.** A positive result validates the **probe**, not the model's correctness — it shows the probe is reading something the network actually uses to act, rather than reconstructing the reference from the input independent of what the network does with it. It is also the one criterion here that needs no control condition of its own, since the residual pattern itself is the check.

**Downstream dependency, stated so it isn't lost.** Phase 3 (branch T)'s central claim — that "lying" can be operationalized as divergence between a report and a causally validated internal posterior — depends on this study succeeding. Without a validated residual-following result, "the reporter's belief" in phase 3 is not a defensible measurement, it is a probe artifact wearing the vocabulary of belief.

## Migration source

Reconciled R12. Dependency noted in R30 (branch T).
