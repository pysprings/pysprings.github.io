# Recursive Language Models (RLM)

| | |
|---|---|
| **Status** | Active |
| **Path** | [AI/ML](../../paths/ai-ml.md) |
| **Prereqs** | [Instructor](../lightning-talks/instructor.md) |
| **Repo** | [:material-github: pysprings/rlm](https://github.com/pysprings/rlm) |

## Overview

An implementation of Recursive Language Models in **77 lines of Python**, based on the 2025 MIT paper by Zhang, Kraska, and Khattab. The key insight: instead of feeding entire documents into an LLM's context window (where quality degrades with length), store the document as a Python variable and let the LLM write code to explore it.

## How It Works

```
User Query → Main LLM → Writes Python Code → Executes in REPL
                              ↓
                      Calls Sub-LLM on Chunks
                              ↓
                      Reads Print Output
                              ↓
                      Iterates Until Done
```

## Architecture (8 Chapters)

The project uses **literate programming** — the presentation slides are the source of truth, and the Python code is automatically extracted from them using [Entangled](../projects/entangled.md).

1. **Title & Problem** — Context rot: LLMs degrade on long documents
2. **Build Steps 1–6** — REPL namespace, sub-LLM, conversation loop, FINAL signaling, print capture, full assembly
3. **Implementation** — The complete 77-line function
4. **Chatbot** — Interactive variant
5. **Demo** — Live examples with Project Gutenberg books

## Key Concepts

- Literate programming (markdown → tangled Python)
- Python `exec()` and namespace manipulation
- LLM orchestration (main model + sub-model)
- Exception-based control flow (`FINAL()` signal)
- REPL environment simulation

## Try It

1. Clone: `git clone https://github.com/pysprings/rlm`
2. `cd rlm && pip install -e .`
3. Browse the slides: `mkdocs serve` → <http://localhost:8000>
4. Run the demo: `python code/demo.py`

## Where to Go Next

- [marketing-bot](marketing-bot.md) — Another architecture for LLM-driven systems
- [Entangled](entangled.md) — Deep dive into the literate programming tool used here
