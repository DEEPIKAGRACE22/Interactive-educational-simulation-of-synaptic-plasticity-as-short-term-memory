# Short-Term Memory Model

## Educational Modeling Decision

The initial educational model intentionally separates learning from decay.

### Learning

A new co-activation modifies the synaptic state:

$$S_{new} = S_{old} + \eta x^T y$$

where:

- $\eta$ is the plasticity or learning rate.
- $x$ is presynaptic activity.
- $y$ is postsynaptic activity.

### Decay

When time passes without new learning:

$$S_{new} = \lambda S_{old}$$

where $\lambda$ is the retention factor.

This separation is intentional. Learning changes the state because of co-activation; decay changes the state because time passes without new learning. The implementation should not prematurely combine both processes until the scientific model has been reviewed.

## Scope and Simplification

These equations describe a simplified educational model. They are not a complete account of biological short-term memory, synaptic plasticity, or the BDH mechanism. Future documentation must state which behaviors are model assumptions, which are observations from project experiments, and which claims are supported by external sources.

TODO(Person 1): Review notation, assumptions, and citations before Milestone 1.
TODO(Person 2): Implement learning and decay as separate model operations.
