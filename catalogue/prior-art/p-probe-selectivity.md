---
id: p-probe-selectivity
type: prior-art
status: imported
confidence: well established
---

## Purpose

Probe success must be reported against a matched-capacity control, since capacity alone buys performance.

## Content

Hewitt & Liang, "Designing and Interpreting Probes with Control Tasks": a probe's success must be reported against a matched-capacity control, since sufficient probe capacity alone — with no real signal at all — can achieve high performance by memorizing the training set's input-output mapping. Selectivity is the gap between real-task and control-task performance at matched capacity, not raw accuracy or R² on its own.

This is the direct source for the reporting requirement in `c-inst-derived`: every decodability number is reported as excess over random-init, raw-feature, and shuffled-target controls, and selectivity is defined exactly as the gap between real-target and shuffled-target performance at matched capacity. Without this, a rising raw decodability curve would be compatible with the probe having simply learned the task's marginal structure rather than reading anything from the network.

## Migration source

Hewitt & Liang, control tasks
