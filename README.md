# pysprings.github.io

Source for [pysprings.org](https://pysprings.org) — the Southern Colorado Python User Group website.

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Local Development

```bash
pip install mkdocs-material
mkdocs serve
```

Then open <http://localhost:8000>.

## Deployment

Pushes to `master` automatically deploy via GitHub Actions. See `.github/workflows/deploy.yml`.

## Contributing

To add or update a wiki page:

1. Fork this repo
2. Edit files under `docs/`
3. Preview with `mkdocs serve`
4. Open a PR

Wiki pages live in `docs/wiki/`. Each lightning talk, series, and project has its own page. Stub pages have an "Edit on GitHub" link — contributions welcome.
