# Aurora — Mental Health Support Web Application

A Flask web application that combines a conversational AI assistant with tools for mood tracking, journaling, community features, mental health resources, and a directory of mental health professionals (including booking flows).

The runnable application lives in the [`Mental Health Chatbot/`](Mental%20Health%20Chatbot/) directory.

## Features

- **AI chat** — Streaming chat backed by a local [Ollama](https://ollama.com/) API (`deepseek-r1:7b`); conversations are stored per user when logged in.
- **Accounts** — Registration, login/logout, and dashboard (`/user/...`).
- **Mood tracking** — Log moods and view stats (`/api/mood/...`).
- **Journal & goals** — Journal entries, prompts, and personal goals (`/user/journal`, `/user/goals`, etc.).
- **Resources** — Curated resource listings and bookmarks (`/user/resources`, data in `data/resources.json`).
- **Community** — Forums, groups, and events (`/community/...`).
- **Professionals** — Browse psychologists, psychiatrists, and counselors; detail pages and session booking (`/professionals/professional-help/...`).
- **Referral & work plan** — Helper pages for finding professionals (`/referral`) and generating a personal work plan (`/workplan`) via API routes under `/api/`.

## Tech stack

- **Backend:** Python 3, [Flask](https://flask.palletsprojects.com/), [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/), [Flask-Login](https://flask-login.readthedocs.io/), [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/)
- **Database:** SQLite by default (configurable via `DATABASE_URL`)
- **AI:** HTTP requests to Ollama’s local generate API (see [Configuration](#configuration))

## Prerequisites

- Python 3.9+ recommended
- [Ollama](https://ollama.com/) installed and running, with the **`deepseek-r1:7b`** model pulled, for chat and other AI-assisted endpoints:

  ```bash
  ollama pull deepseek-r1:7b
  ```

## Setup

1. **Clone** this repository and go into the app folder:

   ```bash
   cd "Mental Health Chatbot"
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   The app also imports **Flask-Bootstrap** and **Flask-Login**. If you see import errors after installing `requirements.txt`, install them explicitly:

   ```bash
   pip install Flask-Bootstrap Flask-Login
   ```

4. **Environment variables** — Create a `.env` file in `Mental Health Chatbot/` (optional; defaults exist for local dev). See [Configuration](#configuration).

## Configuration

| Variable | Purpose |
|----------|---------|
| `SECRET_KEY` | Flask session security; change for any shared or production deployment. |
| `DATABASE_URL` | SQLAlchemy URI (default: `sqlite:///mental_health.db`). |
| `DEEPSEEK_API_URL` | Referenced in `config.py` for flexibility; the chat service uses Ollama’s generate endpoint (see `services/deepseek_service.py`). |

Default development settings are defined in [`Mental Health Chatbot/config.py`](Mental%20Health%20Chatbot/config.py).

## Running the app

From `Mental Health Chatbot/`:

```bash
python app.py
```

Then open **http://127.0.0.1:5000/** in a browser.

For production-style serving, `gunicorn` is listed in `requirements.txt`; configure it to target the Flask application factory pattern as needed (e.g. `create_app()` in `app.py`).

## Project layout (high level)

| Path | Role |
|------|------|
| `app.py` | Application factory, blueprints, DB init |
| `config.py` | Environment-based configuration |
| `db.py` | SQLAlchemy instance |
| `models/` | ORM models (users, conversations, mood, journal, community, etc.) |
| `controllers/` | Route blueprints (pages, API, user, community, professionals, …) |
| `services/` | AI / DeepSeek-Ollama integration |
| `templates/` | Jinja2 HTML templates |
| `static/` | CSS and JavaScript |
| `data/` | JSON data for resources and professionals (where applicable) |

## Disclaimer

This software is a **student project** and is **not** a substitute for professional medical or mental health advice, diagnosis, or treatment. If you are in crisis, contact local emergency services or a crisis hotline in your area.
