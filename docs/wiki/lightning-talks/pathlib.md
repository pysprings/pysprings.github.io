# pathlib

| | |
|---|---|
| **Difficulty** | :material-star: |
| **Path(s)** | [Stdlib Deep Dives](../../paths/stdlib-deep-dives.md) |
| **Prereqs** | Basic Python |
| **Unlocks** | [caching](caching.md), [zipapp](zipapp.md) |
| **Repo** | [:material-github: pysprings/lightning-talks/pathlib](https://github.com/pysprings/lightning-talks/tree/main/pathlib) |

## Overview

Modern, object-oriented file path handling with Python's `pathlib` module (stdlib since Python 3.4). Replaces the older `os.path` functional approach with a cleaner API.

## Key Concepts

- **`Path` objects** replace string-based paths — use `/` operator instead of `os.path.join()`
- **Cross-platform** by default — no need to worry about path separators
- **Built-in file operations** — `Path.read_text()`, `Path.write_text()`, `Path.glob()`
- **Rich attribute access** — `.name`, `.suffix`, `.parent`, `.stem`

## The Code

[`pathlib/README.md`](https://github.com/pysprings/lightning-talks/blob/main/pathlib/README.md) — Full comparison of `os.path` vs `pathlib`

### Before (os.path)

```python
import os.path

fname = os.path.join(".", "test.py")
os.path.abspath("../../test.py")
os.path.basename("../../test.py")
os.path.splitext("test.py")
```

### After (pathlib)

```python
from pathlib import Path

fname = Path(".") / "test.py"
Path("../../test.py").resolve()
Path("../../test.py").name  # "test.py"

# Glob returns a generator
all_python_files = Path(".").glob("**/*.py")

# Direct file I/O — no open() needed
Path("myfile.md").write_text("# Here's a title!")
```

## Try It

1. Open a Python REPL
2. Try these one-liners:
```python
from pathlib import Path
print(list(Path(".").glob("*.py")))       # find all .py files
print(Path(__file__).parent.resolve())     # directory of current script
```
3. **Challenge:** Rewrite a script that uses `os.path.join` and `os.path.exists` to use `pathlib` instead

## Further Reading

- [pathlib docs](https://docs.python.org/3/library/pathlib.html)
- [os.path → pathlib correspondence table](https://docs.python.org/3/library/pathlib.html#correspondence-to-tools-in-the-os-module)

## Where to Go Next

- [caching](caching.md) — Optimize function performance with `functools.lru_cache`
- [zipapp](zipapp.md) — Package your Python app as a single `.pyz` file (uses pathlib for file handling)
