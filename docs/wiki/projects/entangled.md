# Entangled: Literate Programming

| | |
|---|---|
| **Status** | Active |
| **Repo** | [:material-github: pysprings/lightning-talks (entangled)](https://github.com/pysprings) |

## Overview

A demonstration of [Entangled](https://entangled.github.io/), a tool for **literate programming** — writing code inside narrative markdown documents. The markdown is the source of truth; Python files are automatically generated ("tangled") from it.

## Key Concepts

- **Literate programming** — Code embedded in explanatory prose
- **Named code blocks** — `{.python #identifier file=path/to/file}` syntax
- **Noweb references** — `<<reference>>` for composing code from named blocks
- **Bidirectional sync** — Tangle (markdown → Python) and Stitch (Python → markdown)
- **Watch mode** — `entangled watch` for live sync during development

## How It Works

You write markdown with annotated code blocks:

````markdown
```{.python #main file=my_app.py}
<<imports>>
<<main-function>>
```
````

Entangled assembles the final Python file from these blocks, maintaining source mappings back to the markdown.

## Used In

- [RLM Project](rlm.md) — The entire presentation is literate-programmed with Entangled

## Further Reading

- [Entangled documentation](https://entangled.github.io/)
- [CONVENTIONS.md](https://github.com/pysprings) — PySprings conventions for Entangled syntax
