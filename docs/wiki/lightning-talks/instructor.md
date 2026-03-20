# Instructor: Structured LLM Outputs

| | |
|---|---|
| **Difficulty** | :material-star::material-star::material-star: |
| **Path(s)** | [AI/ML](../../paths/ai-ml.md) |
| **Prereqs** | [Jinja2](jinja2.md), [Pydantic](pydantic.md) |
| **Unlocks** | [DSPy Series](../series/dspy-mastery.md), [RLM Project](../projects/rlm.md), [marketing-bot](../projects/marketing-bot.md) |
| **Repo** | [:material-github: pysprings/lightning-talks/instructor](https://github.com/pysprings/lightning-talks/tree/master/instructor) |

## Overview

The [Instructor](https://python.useinstructor.com/) library patches OpenAI's client to return validated **Pydantic models** instead of raw text. This talk demonstrates it by building a tool that reads source code and generates CRC (Class-Responsibility-Collaboration) card diagrams using an LLM.

## Key Concepts

- **Structured outputs** — Force LLMs to return data matching a Pydantic schema
- **`instructor.patch()`** — Wraps the OpenAI client to add `response_model` support
- **Prompt templates** — Jinja2 templates for dynamic prompt construction
- **Pydantic validation** — Type-checked, validated responses from the LLM
- **Pipeline pattern** — Source code → prompt template → LLM → Pydantic model → Graphviz diagram

## The Code

- [`crc-cards.py`](https://github.com/pysprings/lightning-talks/blob/master/instructor/crc-cards.py) — Main script
- [`prompt.txt`](https://github.com/pysprings/lightning-talks/blob/master/instructor/prompt.txt) — Jinja2 prompt template

### Pydantic Models

```python
from pydantic import BaseModel

class Collaborator(BaseModel):
    name: str
    description: str

class Card(BaseModel):
    name: str
    responsibilities: str
    collaborators: list[Collaborator]

class CardStack(BaseModel):
    cards: list[Card]
```

### Structured LLM Call

```python
import instructor
from openai import OpenAI

client = instructor.patch(OpenAI())
response = client.chat.completions.create(
    model="gpt-4o",
    response_model=CardStack,  # <-- Forces structured output
    messages=[{"role": "user", "content": rendered_prompt}],
    temperature=0,
)
# response is a validated CardStack instance, not raw text
```

### The Pipeline

```
Source File → Jinja2 Template → Rendered Prompt → LLM → CardStack → Graphviz DOT
```

## Try It

1. Clone: `git clone https://github.com/pysprings/lightning-talks`
2. `cd instructor`
3. Install deps: `pip install instructor openai pydantic jinja2 graphviz`
4. Set your OpenAI API key: `export OPENAI_API_KEY=sk-...`
5. Run: `python crc-cards.py some_python_file.py`
6. **Challenge:** Add a new Pydantic model for function signatures and modify the prompt to extract them too

## Further Reading

- [Instructor docs](https://python.useinstructor.com/)
- [Pydantic docs](https://docs.pydantic.dev/)

## Where to Go Next

- [DSPy Mastery Series](../series/dspy-mastery.md) — Systematic AI development framework that builds on these structured output concepts
- [RLM Project](../projects/rlm.md) — LLM orchestration with code execution
- [marketing-bot](../projects/marketing-bot.md) — Clean architecture for AI planning systems
