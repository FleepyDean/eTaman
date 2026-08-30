import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from taman.models import Facility

facilities = [
    ('Tandas', 'Infrastruktur'),
    ('Taman Permainan', 'Kemudahan'),
    ('Tempat Letak Kereta', 'Infrastruktur'),
    ('Surau / Tempat Ibadat', 'Infrastruktur'),
]

created = 0
for nama, kategori in facilities:
    obj, was_created = Facility.objects.get_or_create(
        nama=nama,
        defaults={'kategori': kategori, 'status': 'Active'}
    )
    if was_created:
        created += 1
        print(f'Created: {nama}')
    else:
        print(f'Already exists: {nama}')

print(f'\nDone. {created} new facility(s) added.')
