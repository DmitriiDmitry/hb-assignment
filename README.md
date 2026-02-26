# hb-assignment

UI end-to-end tests for a home-improvement quote flow using **Python + Pytest + Selenium** with a lightweight Page Object pattern.

## Stack

- Python 3.14+
- Pytest
- Selenium WebDriver (Chrome)
- Faker
- python-dotenv
- Ruff (dev)

## Project Structure

- `conftest.py` - shared pytest fixtures (`browser`, `base_url`, `thank_you_url`, `zip_code`)
- `pages/base_page.py` - common page methods
- `pages/landing_page.py` - landing page object and checks
- `pages/locators.py` - landing page locators
- `tests/test_order_creation.py` - smoke flow: create order to thank-you page
- `tests/test_cancelling_order.py` - regression flow: cancel flow and verify return to landing page
- `utils/utils.py` - random test data generators
- `.env-example` - required environment variables template

## Prerequisites

1. Install Google Chrome.
2. Make sure a compatible ChromeDriver is available to Selenium.
   - Either keep ChromeDriver on your `PATH`, or
   - rely on Selenium Manager support in your environment.
3. Install Python 3.14 or newer.

## Setup

1. Install dependencies (preferred):

```bash
uv sync
```

Alternative (without `uv`):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

2. Configure environment variables:

```bash
cp .env-example .env
```

Set values in `.env`:

- `BASE_URL` - landing page URL under test
- `THANK_YOU_URL` - expected final URL after successful submit
- `ZIP_CODE` - zip code used in tests

## Run Tests

Run all tests:

```bash
uv run pytest -q
```

Run by marker:

```bash
uv run pytest -m smoke -q
uv run pytest -m regression -q
```

Run a single file:

```bash
uv run pytest tests/test_order_creation.py -q
```

## Lint

```bash
uv run ruff check .
uv run ruff format .
```

## Notes

- Browser fixture scope is `function`; each test opens and quits a new Chrome session.
- Current flows include direct Selenium steps for the multi-step wizard; a dedicated Page Object for wizard steps is a good next refactor.
- Tests depend on production-like UI selectors (`data-autotest-*`); selector changes in the app will require locator updates.
