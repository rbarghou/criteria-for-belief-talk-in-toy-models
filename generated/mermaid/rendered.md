# Rendered Mermaid DAGs

*Generated from `index.md`. Do not edit by hand.*

## Program overview

```mermaid
%% Research-program overview
flowchart LR

prior["Prior-art<br/>claims"]
components["Shared<br/>components"]
runs["Training<br/>runs"]
studies["Pre-registered<br/>studies"]

prior -->|calibrates| studies
components -->|needs| runs
components -->|needs / enables| studies
runs -->|needs| studies
studies -->|presupposes / enables| studies
```

## Shared foundation and run production

```mermaid
%% Shared foundation and run production
flowchart LR

terminology["Shared<br/>terminology"]
substrate["Game and data<br/>substrate"]
solver["Reference<br/>solver"]
grounded["Probe-free<br/>instruments"]
derived["Probe-based<br/>instruments"]
training["Training<br/>framework"]
verification["Solver<br/>verification"]
prediction["Prediction<br/>run"]
policy["Policy-gradient<br/>run family"]
support["Supporting<br/>run family"]

terminology -->|needs| substrate
substrate -->|needs| solver
solver -->|needs| grounded
grounded -->|calibrates| derived
substrate -->|needs| training
solver -->|needs| training
solver -->|needs| verification
training -->|needs| prediction
training -->|needs| policy
training -->|needs| support
```

## Calibration and interpretability spine

```mermaid
%% Calibration and interpretability spine
flowchart TB

diversity["Diversity<br/>sweep"]
grounded["Probe-free<br/>instruments"]
boundary["Diversity-boundary<br/>prior art"]
transition["Behavioral<br/>transition"]
prediction["Prediction<br/>run"]
derived["Probe-based<br/>instruments"]
composition["Compositional-data<br/>prior art"]
tooling["Tooling<br/>validation"]
decoding["Decodability<br/>over training"]

diversity -->|needs| transition
grounded -->|needs| transition
boundary -->|calibrates| transition
transition -->|presupposes| decoding
prediction -->|needs| decoding
derived -->|needs| decoding
composition -->|needs| decoding
tooling -->|enables| decoding
```

## Grounded causal evidence

```mermaid
%% Grounded causal evidence
flowchart LR

prediction["Prediction-run<br/>checkpoints"]
stake["Stake-vector<br/>checkpoints"]
grounded["Probe-free<br/>instruments"]
decoding["Decodability<br/>timing"]
causal["Causal<br/>structure"]
counting["Counting versus<br/>retrieval"]

prediction -->|needs| causal
stake -->|needs| causal
grounded -->|needs| causal
decoding -->|selects target| causal
prediction -->|needs| counting
grounded -->|needs| counting
```

## Derived criterion suite

```mermaid
%% Derived criterion suite
flowchart LR

checkpoints["Phase-1 checkpoint corpus:<br/>prediction and stake-vector runs"]
derived["Probe-based<br/>instruments"]
criteria["Three derived criteria:<br/>off-manifold coherence<br/>path independence<br/>residual following"]
multirun["Multi-consumer<br/>run · stub"]
tooling["Tooling<br/>validation"]
multi["Multi-consumer<br/>criterion · stub"]

checkpoints -->|needs| criteria
derived -->|needs| criteria
multirun -->|needs| multi
derived -->|needs| multi
tooling -->|enables| multi
```

## Action-channel comparisons

```mermaid
%% Action-channel comparisons
flowchart LR

outputs["Policy-output runs:<br/>action-only and auxiliary"]
decoding["Decodability<br/>timing"]
payoff["Payoff-only<br/>comparison"]
channels["Action-channel comparison:<br/>action-only, single stake,<br/>stake vector"]
demand["Representation versus<br/>behavioral demand"]
behavior["Action-behavior runs:<br/>action-only and stake vector"]
grounded["Probe-free<br/>instruments"]
rational["Belief<br/>rationalizability"]

outputs -->|needs| payoff
decoding -->|calibrates| payoff
channels -->|needs| demand
decoding -->|enables| demand
behavior -->|needs| rational
grounded -->|needs| rational
```

## Training history and replication

```mermaid
%% Training history and replication
flowchart LR

prediction["Prediction<br/>run"]
curriculum["Curriculum<br/>run"]
decoding["Decodability<br/>timing"]
persistence["Belief<br/>persistence"]
seeds["Seed-replication<br/>run"]
derived["Probe-based<br/>instruments"]
tooling["Tooling<br/>validation"]
multiplicity["Algorithm-multiplicity<br/>prior art"]
uniqueness["Circuit<br/>uniqueness · stub"]

prediction -->|needs| persistence
curriculum -->|needs| persistence
decoding -->|calibrates| persistence
seeds -->|needs| uniqueness
derived -->|needs| uniqueness
tooling -->|enables| uniqueness
multiplicity -->|calibrates| uniqueness
```
