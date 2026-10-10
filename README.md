# copr-iosevka
A repository that contains rpm build specs for all Iosevka fonts

## Development setup

`build.py` needs Python 3.14 and the `copr` client library. The Python version is pinned in `.python-version` and dependencies are locked in `uv.lock`.

### Prerequisites

Install [uv](https://docs.astral.sh/uv/) (no system Python required):

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Setup

```bash
git clone <repo-url>
cd copr-iosevka
uv sync --managed-python
```

`uv sync` downloads Python 3.14 if it isn't already installed, creates `.venv/`, and installs the locked dependencies. `--managed-python` ensures a uv-managed interpreter is used rather than a system or Homebrew one.

Verify:

```bash
uv run python --version
uv run python -c "from copr.v3 import Client; print('ok')"
```

### Copr credentials

`build.py` authenticates through `~/.config/copr`. Generate the token at <https://copr.fedorainfracloud.org/api/> and save the config block there. Tokens expire periodically, so regenerate it if you get authentication errors. Never commit this file.

### Running

```bash
uv run build.py -r/--release {release}
```

### Adding dependencies

```bash
uv add <package>
```

Commit `pyproject.toml` and `uv.lock` afterwards. Do not commit `.venv/`.
