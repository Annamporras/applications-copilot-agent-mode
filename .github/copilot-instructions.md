## OctoFit Tracker — Copilot agent instructions

This repository is a workshop scaffold for the OctoFit Tracker app (React frontend + Django REST backend + MongoDB). The goal of this file is to give an AI coding agent the minimal, actionable context needed to be productive immediately.

Key files to read first
- `README.md` — high-level exercise description and links.
- `docs/octofit_story.md` — project goals, the intended stack (React + Django REST + MongoDB), and workshop steps.
- `.github/instructions/octofit_tracker_setup_project.instructions.md` — repository-specific operational rules (must-read; contains setup commands, port rules and workspace conventions).

High-level architecture (what to keep in mind)
- Frontend: React app under `frontend/` (expected). Serve on port 3000 in Codespaces.
- Backend: Django REST API under `backend/` (expected). Serve on port 8000 in Codespaces.
- Database: MongoDB is the intended DB (mongo/mongod on port 27017). Use Django ORM / djongo integration; do not write direct Mongo scripts for schema creation.

Strict workspace and operational rules (from `.github/instructions`)
- Never change directories in agent mode. Always run commands that reference the full path to the project folder (for example: `python3 -m venv /path/to/octofit-tracker/backend/venv`).
- Forwarded ports allowed: 8000 (public), 3000 (public), 27017 (private). Do not propose or open additional ports.

Common, concrete commands (examples taken from the project instructions)
- Create venv: `python3 -m venv octofit-tracker/backend/venv`
- Activate and install: `source octofit-tracker/backend/venv/bin/activate && pip install -r octofit-tracker/backend/requirements.txt`
- Check mongod: `ps aux | grep mongod`

Project-specific conventions
- Use Django's ORM for DB work (the setup expects djongo/pymongo integration). Avoid ad-hoc Mongo shell scripts for schema or initial data.
- When editing or adding Django apps, follow Django project layout conventions. Place backend code under `backend/` and keep the repository-level README in sync.
- Preserve existing file formatting and style. Make minimal, local changes unless asked to refactor.

How to add a small feature safely (example: add a backend API endpoint)
1. Locate the Django project under `backend/` (create it there if missing). Use explicit paths when running management commands.
2. Add a serializer, view, and URL in the appropriate app. Use existing naming patterns (models -> serializers -> views -> urls).
3. Add a basic test (fast, focused) under the app's `tests/` directory.
4. Run the minimal test locally (or in Codespace) and report test output.

What not to do
- Do not change directories in commands; do not introduce new forwarded ports; do not assume a DB other than MongoDB.
- Do not change the intended stack without explicit direction from the repo owner.

When you finish a change
- Run quick validation: lint / run the focused tests you added. Report the steps you ran and the observed output.
- Open a concise PR description that includes: what changed, where, and a short verification checklist (commands run + success/fail).

If info is missing
- If files expected by the `docs` or `.github/instructions` (for example `backend/requirements.txt` or `frontend/`) are missing, create a minimal scaffold and document assumptions in your PR. Mention the exact paths you created (e.g. `octofit-tracker/backend/requirements.txt`).

Feedback request
- If any of these rules are unclear or you need an additional example (for example a minimal Django app scaffold or a React component pattern used here), ask and I will extend this file with a code example and a small test harness.
