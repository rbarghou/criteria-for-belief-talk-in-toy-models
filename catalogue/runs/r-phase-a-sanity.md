---
id: r-phase-a-sanity
type: run
phase: 1
status: drafted
depends_on: [{node: c-training, edge: needs}, {node: c-substrate, edge: needs}]
produces: checkpoints, logs
---

## Purpose

Supervised on the reference action. Debugging instrument only; results are not evidence about belief.

## Content

Cross-entropy on action positions, target = the payoff-maximizing action given the opponent's *true* policy (which the generator, not the model, knows). Run first, on rung 0, once the engine and tokenizer exist and before the diversity sweep, purely to confirm the substrate transitions at all — cheap, clean curves, fast feedback on plumbing bugs.

**Restriction, stated to prevent misuse downstream:** this phase smuggles in a label — the target depends on hidden state the model never observes — and does not satisfy the revealed-preference criterion (`program/orientation.md` §7). It is a debugging instrument only. Do not report Phase A findings as evidence about belief, and do not let a clean Phase A curve substitute for Phase B (`r-phase-b-main`) as a reference.

## Migration source

Protocol rev.2 §8 Phase A.
