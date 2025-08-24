# College Enterprise Resource Planner

This is a College Enterprise Resource Planner Developed by me for my college. I use Python/Django Framwork for building an fully functional web application.

## Quick summary
- Django project using a custom user model and `main_app` for core models.
- Uses PostgreSQL for development/CI. Tests run in a temporary test database.

## Prerequisites
- Python 3.11
- PostgreSQL (local) or rely on CI service container
- Git

## Setup (local)
1. Create a virtualenv and activate it:

```bash
python -m venv .venv
.\.venv\Scripts\activate    # Windows (cmd / powershell)
# source .venv/bin/activate    # macOS / Linux
```

2. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Create a `.env` file (example values):

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=Colledge_ERP
DB_USER=postgres
DB_PASSWORD=123
DB_HOST=localhost
DB_PORT=5432
```

4. Make migrations and migrate:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (optional):

```bash
python manage.py createsuperuser
```

6. Run the dev server:

```bash
python manage.py runserver
```

## Tests
- Run tests locally:

```bash
python manage.py test
```

Notes:
- Tests use a temporary test database (Django prefixes DB name with `test_`).
- If you see unique-constraint errors in tests when creating related models, use `get_or_create(...)` or ensure each test uses a unique user (for example use `uuid` in email).

## CI (GitHub Actions)
- Workflow file: `.github/workflows/ci.yml`.
- CI starts a `postgres:13` service and sets env vars; ensure your `settings.py` reads DB credentials from environment.
- CI runs tests with `python manage.py test --parallel=1` to avoid concurrency-related races.

## Common issues & fixes
- Missing psycopg2: add `psycopg2-binary` to `requirements.txt` (already included).
- settings.DATABASES improperly configured: ensure `ENGINE` is `django.db.backends.postgresql` and env vars match CI `.yml`.
- Duplicate-key in tests: use `get_or_create`, unique test users, or set `--parallel=1`.

## Contributing
- Follow repository style. Add tests for new behavior. Run tests locally before pushing.

## Where test data lives
- For Postgres: created inside the running Postgres server/container. CI uses an ephemeral container; local tests create a local temporary DB.

If you want, I can add a short `Makefile` or scripts to automate setup and test commands.
