#!/bin/sh
# chmod +x ./run.sh

export APP_MODULE=${APP_MODULE-app.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8000}

exec python3 -m uvicorn --reload --host $HOST --port $PORT "$APP_MODULE"
