# Caching with lru_cache

| | |
|---|---|
| **Difficulty** | :material-star::material-star: |
| **Path(s)** | [Stdlib Deep Dives](../../paths/stdlib-deep-dives.md) |
| **Prereqs** | [Python Basics](../../paths/getting-started.md) |
| **Unlocks** | [Multiprocessing](multiprocess.md) |
| **Repo** | [:material-github: pysprings/lightning-talks/caching](https://github.com/pysprings/lightning-talks/tree/main/caching) |

## Overview

Python's `functools.lru_cache` provides transparent memoization — cache the return values of expensive function calls so repeated calls with the same arguments return instantly.

## Key Concepts

- **Memoization** — Store computed results and return them for repeated inputs
- **`@lru_cache`** decorator — One-line addition to any pure function
- **Cache sizing** — Control memory usage with `maxsize` parameter
- **Cache management** — `.cache_info()` and `.cache_clear()` methods
- **LRU eviction** — Least Recently Used items are dropped when cache is full

## The Code

[`caching/`](https://github.com/pysprings/lightning-talks/tree/main/caching) in the lightning-talks repo.

### Basic Usage

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# First call computes; subsequent calls with same n return cached result
fibonacci(100)

# Inspect cache performance
print(fibonacci.cache_info())
# CacheInfo(hits=98, misses=101, maxsize=128, currsize=101)
```

### When to Use It

- **Pure functions** — Same input always gives same output
- **Expensive computations** — Database lookups, API calls, complex math
- **Recursive algorithms** — Fibonacci, dynamic programming

### When NOT to Use It

- Functions with side effects
- Functions where arguments aren't hashable
- When you need cache expiration (use `cachetools` or Redis instead)

## Try It

1. Clone the repo: `git clone https://github.com/pysprings/lightning-talks`
2. `cd caching` and run the examples
3. **Challenge:** Write a recursive factorial function, then add `@lru_cache`. Compare timing with and without caching for `factorial(500)` called 1000 times.

## Further Reading

- [`functools` documentation](https://docs.python.org/3/library/functools.html)
- Python 3.9+ added `@cache` as a shorthand for `@lru_cache(maxsize=None)`

## Where to Go Next

- [Multiprocessing](multiprocess.md) — When caching can't speed things up, parallelize instead
- The caching → optimization concept reappears in [DSPy Session 7](../series/dspy-mastery.md) (prompt optimization)
