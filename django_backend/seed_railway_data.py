"""
Seed the Railway PostgreSQL database with initial eTaman data.
Run this in the Railway backend service shell:
    python seed_railway_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from taman.seed_data import seed_database

if __name__ == '__main__':
    seed_database()
