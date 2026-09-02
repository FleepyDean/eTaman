"""
Quick diagnostic command to verify database connection and data.
Run in Railway backend shell:
    python manage.py check_db
"""
from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings

class Command(BaseCommand):
    help = 'Check database connection and count taman records'

    def handle(self, *args, **kwargs):
        db = settings.DATABASES['default']
        self.stdout.write(f"Database ENGINE: {db.get('ENGINE', 'unknown')}")
        self.stdout.write(f"Database NAME: {db.get('NAME', 'unknown')}")
        self.stdout.write(f"Database HOST: {db.get('HOST', 'unknown')}")

        with connection.cursor() as cursor:
            cursor.execute("SELECT current_database(), current_user;")
            row = cursor.fetchone()
            self.stdout.write(f"Connected DB: {row[0]}, User: {row[1]}")

        from taman.models import Taman
        count = Taman.objects.count()
        self.stdout.write(self.style.SUCCESS(f"Taman count: {count}"))
