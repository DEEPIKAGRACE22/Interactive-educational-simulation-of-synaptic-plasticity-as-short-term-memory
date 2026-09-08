# Git Workflow

The team uses a protected integration path:

```text
main
  |
develop
  |
feature branch
  |
Pull Request
  |
Code Review
  |
develop
  |
Testing
  |
main
```

## Team Ownership

- Person 1: `feature/scientific-foundation`
- Person 2: `feature/synaptic-memory`
- Person 3: `feature/interactive-ui`
- Person 4: `feature/testing-integration`

Teammates must not push directly to `main`. Work should be committed to the relevant feature branch, reviewed through a pull request, merged into `develop`, tested, and promoted to `main` only when the integration is ready.

TODO(Person 4): Document repository branch protections and release checks.
