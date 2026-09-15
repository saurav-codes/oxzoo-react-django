# oxzoo-react-django

Official ox deploy example: a Django 5.2 LTS API behind gunicorn with a React 18 SPA built by Vite, deployed to one Ubuntu VPS from a single `ox.toml` at the repo root. nginx serves the built frontend and proxies the API paths to a systemd-managed gunicorn process; ox runs every install/build hook as the unprivileged project user and switches traffic only after the health check passes.

## Stack

| Layer | Tool | Version |
| --- | --- | --- |
| Backend | Django + gunicorn | django 5.2.17, gunicorn 23.0.0 |
| Python tooling | uv (`uv.lock`, `.python-version`) | Python 3.13 |
| Frontend | React + Vite (npm) | react/react-dom 18.3.1, vite 5.4.21 |
| Serving | nginx + systemd | provisioned by ox |

## Environment flow

- **Backend env is runtime env**: `hello/views.py` reads `GREETING_TAG` from `os.environ` on every request, so `GET /api/greeting` returns `hello world oxzoo-react-django_{GREETING_TAG}` with whatever the ox Environment editor currently holds. `DJANGO_SECRET_KEY` is read the same way.
- **Frontend env is build-time env**: `vite.config.js` sets `envPrefix: ["GREETING_", "VITE_"]`, so `GREETING_TAG` present during `npm run build` is baked into the bundle via `import.meta.env.GREETING_TAG`. Changing the tag means rebuilding the SPA.
- **nginx** serves `dist/` (`spa = true`) with an `index.html` fallback and keeps proxying the `[frontend] api_paths` (`/api`, `/health`) to the app; `GET /health` returns `200` with body `ok`.

## Deploy with ox

1. In the ox dashboard, create a project from the clone URL: `https://github.com/saurav-codes/oxzoo-react-django.git`
2. **Before the first deploy**, set `GREETING_TAG` (and `DJANGO_SECRET_KEY`) in the project's Environment editor. The build hook bakes `GREETING_TAG` into the SPA, so it must exist before the first deploy.
3. Press **Deploy**. ox runs `uv sync --frozen` and `npm install` (release-local installs), `npm run build`, starts the `web` process (`uv run gunicorn hello.wsgi:application` on `127.0.0.1:9107`), and polls `http://127.0.0.1:9107/health` before switching traffic.

Django needs no migrate hook in this example: there are no models, so `settings.py` ships `DATABASES = {}` and the manifest defines no migrate hook.

## Expected output

Visiting the domain (placeholder tag shown for `GREETING_TAG`):

```text
frontend: hello world oxzoo-react-django_{GREETING_TAG}
backend: hello world oxzoo-react-django_{GREETING_TAG}
```

The frontend line is baked at build time; the backend line reflects the live process environment.
