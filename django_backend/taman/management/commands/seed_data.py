from django.core.management.base import BaseCommand
from taman.seed_data import seed_database

class Command(BaseCommand):
    help = 'Seed the database with initial eTaman data'

    def handle(self, *args, **kwargs):
        seed_database()
        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))
