# Experiment Plan

## Experiment 1 — Plasticity

**Question:** Does enabling synaptic plasticity allow an association to be recalled?

**Variables:**

- Learning rate
- Pre-synaptic activity
- Post-synaptic activity

**Expected comparison:** Plasticity OFF vs Plasticity ON.

## Experiment 2 — Decay

**Question:** How does the retention factor affect short-term memory?

**Variables:**

- Retention factor $\lambda$
- Number of time steps

**Measure:**

- Synaptic strength
- Recall activation

## Experiment 3 — Repetition

**Question:** Does repeated co-activation strengthen the memory trace?

**Variables:**

- Number of repetitions
- Learning rate

## Experiment 4 — Interference

**Question:** What happens when competing information modifies the same synaptic state?

The implementation should vary the competing association and measure changes in recall of the original association.

## Experiment 5 — Delay

**Question:** How does recall change as more time passes after learning?

The implementation should vary delay steps and measure recall after each delay.

## Integrity Rules

These experiments are plans, not reported results. No result, plot, or benchmark should be described until it has been generated and checked by the team.

TODO(Person 2): Implement the experiment functions.
TODO(Person 4): Add automated tests for expected qualitative behavior.
