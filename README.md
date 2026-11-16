# Studio Cost Raid Backend

Basic backend project setup for Studio Cost Raid. We will measure a cloud server.

## Setup

1. Clone the repository:
   - On GitHub, copy the HTTPS URL for this repo.
   - In your terminal, run: `git clone <REPO_URL>`
2. Change into the project folder:
   - `cd studio-cost-raid-backend`
3. Create and activate a virtual environment:
   - (Windows PowerShell)
     - `python -m venv venv`
     - `.\venv\Scripts\Activate.ps1`
4. Check which Python you are using:
   - `python -c "import sys; print(sys.executable)"`
5. Install dependencies:
   - `pip install -r requirements.txt`
6. Run the app:
   - `python run.py`

   ## Environment variables

1. Copy `.env.example` to `.env`.
2. Set these variables in `.env`:

   - `FLASK_ENV` – environment name, e.g. `development`.
   - `DATABASE_URL` – dev database URL, e.g. `sqlite:///dev.db` (uses `instance/dev.db`).
   - `JWT_SECRET_KEY` – secret key for signing JWTs. Use a long random string in your real `.env`. Do **not** commit the real value.

   ## Migrations

Run these commands from the project root with the virtual environment activated:

1. Initialize migrations (only needed once, if `migrations/` does not exist yet):

   ```bash
   flask db init
   ```

2. Generate a new migration whenever the models change:

   ```bash
   flask db migrate -m "describe your change"
   ```

3. Apply migrations to the local database:

   ```bash
   flask db upgrade
   ```