# apitest

Automated REST API tests written with pytest. The default target is the free
public demo API https://jsonplaceholder.typicode.com, so the suite runs
anywhere with no credentials.

## What is covered
- CRUD: list, get, create, update, delete
- Negative case: unknown resource returns 404
- Parametrised filtering
- JSON schema validation
- Content-Type and response time checks

## Setup
```bash
python -m venv .venv
. .venv/Scripts/activate      # Windows Git Bash; use .venv/bin/activate on Linux or macOS
pip install -r requirements.txt
cp .env.example .env          # optional
```

## Run
```bash
pytest                                   # everything
pytest -m smoke                          # quick checks
pytest --html=reports/report.html --self-contained-html
```

## Configuration
Set in `.env` or the environment: `BASE_URL`, `TIMEOUT_SECONDS`, `MAX_RESPONSE_SECONDS`.

## CI
`.github/workflows/ci.yml` runs the suite on every push and pull request and
uploads the HTML report as an artifact.

## Adding a test
Add a `test_*.py` file under `tests/` and use the `session`, `base_url` and
`timeout` fixtures from `conftest.py`.
