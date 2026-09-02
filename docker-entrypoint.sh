#!/bin/sh
# Substitute BACKEND_HOST env var into nginx config at runtime
sed -i "s/\${BACKEND_HOST}/${BACKEND_HOST:-backend.railway.internal}/g" /etc/nginx/conf.d/default.conf
exec nginx -g "daemon off;"
