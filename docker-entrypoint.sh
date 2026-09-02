#!/bin/sh
# Substitute BACKEND_URL and PORT env vars into nginx config at runtime
BACKEND_URL="${BACKEND_URL:-http://backend.railway.internal:8000}"
PORT="${PORT:-80}"
sed -i "s|\${BACKEND_URL}|${BACKEND_URL}|g" /etc/nginx/conf.d/default.conf
sed -i "s|\${PORT}|${PORT}|g" /etc/nginx/conf.d/default.conf
exec nginx -g "daemon off;"
