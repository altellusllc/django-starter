#!/bin/bash
# Activate Python environment and load .env
. .venv/bin/activate
export $(grep -v '^#' .env | xargs)

# Determine Django host/port (for flexibility when running multiple instances)
DJANGO_HOST=${DJANGO_HOST:-0.0.0.0}
DJANGO_PORT=${DJANGO_PORT:-8002}
export DJANGO_HOST DJANGO_PORT

# Auto-install JS dependencies if needed
if [ ! -d node_modules ]; then
  echo "Installing JS dependencies..."
  npm install
fi

# Determine webpack public host if not set (e.g. Tailscale IP or other)
if [ -z "$WEBPACK_DEV_HOST" ]; then
  WEBPACK_DEV_HOST=$(hostname -I | awk '{print $1}')
  export WEBPACK_DEV_HOST
  echo "Using WEBPACK_DEV_HOST=$WEBPACK_DEV_HOST"
fi

# Start webpack dev server in background
echo "Starting webpack dev server..."
npm run dev &
WEBPACK_PID=$!

# Start Django dev server in background
echo "Starting Django server at ${DJANGO_HOST}:${DJANGO_PORT}..."
python manage.py runserver "${DJANGO_HOST}:${DJANGO_PORT}" &
DJANGO_PID=$!

# Cleanup function to stop both servers
cleanup() {
  echo "Shutting down servers..."
  kill -TERM "$WEBPACK_PID" "$DJANGO_PID" 2>/dev/null
  exit
}

# Trap signals and perform cleanup
trap cleanup SIGINT SIGTERM

# Wait for any server to exit
wait -n

# When one exits, cleanup others
cleanup
