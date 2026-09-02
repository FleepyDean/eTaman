#!/bin/sh
# Substitute BACKEND_URL env var into nginx config at runtime
# Default to backend's public Railway domain
BACKEND_URL="${BACKEND_URL:-http://backend.railway.internal:8000}"
sed -i "s|\${BACKEND_URL}|${BACKEND_URL}|g" /etc/nginx/conf.d/default.conf
exec nginx -g "daemon off;"
