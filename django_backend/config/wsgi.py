"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, please see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# Log database info for debugging
from django.db import connection
from django.conf import settings

db_engine = settings.DATABASES['default'].get('ENGINE', 'unknown')
db_name = settings.DATABASES['default'].get('NAME', 'unknown')
print(f"[WSGI] Database engine: {db_engine}", file=sys.stderr)
print(f"[WSGI] Database name: {db_name}", file=sys.stderr)

try:
    from taman.models import Taman
    count = Taman.objects.count()
    print(f"[WSGI] Taman count on startup: {count}", file=sys.stderr)
except Exception as e:
    print(f"[WSGI] Error counting Taman: {e}", file=sys.stderr)
