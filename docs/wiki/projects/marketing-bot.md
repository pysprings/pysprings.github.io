# marketing-bot

| | |
|---|---|
| **Status** | Active |
| **Path** | [AI/ML](../../paths/ai-ml.md) |
| **Prereqs** | [Pydantic](../lightning-talks/pydantic.md), [Instructor](../lightning-talks/instructor.md) |
| **Repo** | [:material-github: pysprings/lightning-talks (marketing-bot)](https://github.com/pysprings) |

## Overview

A clean-architecture AI planning system that applies the **Deming Cycle** (Plan-Do-Check-Adjust) to LLM-driven task management. The objective: "Increase participation in the Colorado Springs Python User Group."

## Architecture

```
domain.py       → Domain models (Objective, State, Adjustments)
usecases.py     → Abstract use cases (Planner, Executor, DemingCycle)
adapters.py     → LLM integrations (SimplePlanner, SimpleExecutor)
driver.py       → Entry point with dependency injection
```

## Key Concepts

- **Deming Cycle (PDCA)** — Plan, Do, Check, Adjust applied to AI systems
- **Dependency injection** — Clean separation between business logic and LLM adapters
- **Abstract base classes** — `Planner` and `Executor` protocols
- **Structured output** — Pydantic models via the Instructor library
- **Tool-based execution** — Extensible action pattern
- **State management** — Track LLM-driven progress across iterations

## Try It

1. Clone the repo and `cd marketing-bot`
2. Install: `pip install -e .`
3. Set API key: `export OPENAI_API_KEY=sk-...`
4. Run: `python driver.py`

## Where to Go Next

- [RLM](rlm.md) — A different LLM orchestration architecture
- [DSPy Series](../series/dspy-mastery.md) — Systematic framework that formalizes many of these patterns
