# Django Starter with Webpack & Tailwind

This is a base Django project template preconfigured with:
- Modern JS/CSS bundling via Webpack (ES6, SCSS)
- Tailwind CSS (no CDN; compiled with PostCSS)
- django-webpack-loader for seamless integration
- A sample home page at `/` demonstrating the setup
- A single `start.sh` script to launch both servers

## Prerequisites
- Python 3.8+ (3.10/3.11 recommended)
- Node.js & npm (>=16)
- Git

## Setup
1. Clone this repo and enter it:
   ```bash
   git clone <repo-url> myproject
   cd myproject
   ```
2. Create & activate a Python virtualenv:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Create a `.env` file in the project root with required vars, e.g.:
   ```ini
   DJANGO_SECRET_KEY=your-secret-key
   POSTGRES_DB=...      # if using Postgres
   POSTGRES_USER=...
   POSTGRES_PASSWORD=...
   POSTGRES_HOST=...
   POSTGRES_PORT=...
   ```
4. Install Python deps:
   ```bash
   pip install -r requirements.txt
   ```

## Development
Run `start.sh` to launch both servers:
```bash
./start.sh
```
This will:
- Install JS dependencies (`npm install`) if `node_modules` is missing
- Start Webpack Dev Server on `WEBPACK_DEV_HOST:WEBPACK_DEV_PORT` (defaults to your host IP and 8080)
- Start Django on `DJANGO_HOST:DJANGO_PORT` (defaults to `0.0.0.0:8002`)

### Environment Overrides
- **WEBPACK_DEV_HOST**: host for Webpack bundles (default: first non-loopback IP)
- **WEBPACK_DEV_PORT**: Webpack port (default: 8080)
- **DJANGO_HOST**: Django bind address (default: 0.0.0.0)
- **DJANGO_PORT**: Django port (default: 8002)

Visit in browser:
- Django site → `http://<DJANGO_HOST>:<DJANGO_PORT>/`
- Webpack HMR → bundles served from `http://<WEBPACK_DEV_HOST>:<WEBPACK_DEV_PORT>/static/dist/`

## Production Build
```bash
npm ci && npm run build
python manage.py collectstatic
```

## Template Usage
In `templates/base.html`, bundles are injected:
```django
{% load render_bundle from webpack_loader %}
{% render_bundle 'main' 'css' %}
... your HTML ...
{% render_bundle 'main' 'js' %}
```

## Project Structure
```
├── assets/              # Front-end source (JS & SCSS)
├── static/dist/         # Compiled assets
├── core/                # Django project settings + URLs
├── templates/           # HTML templates
├── start.sh             # Launch Webpack & Django
├── webpack.common.js    # Webpack configs
├── tailwind.config.js   # Tailwind setup
└── requirements.txt     # Python deps
```

## Customization
- Add your JS/SCSS under `assets/`.
- Extend Tailwind via `tailwind.config.js`.
- Tweak Webpack settings in `webpack.common.js`, etc.

---
Happy coding! 🚀