"""
Seed the Railway PostgreSQL database with initial taman data.
Run this in the Railway backend service shell:
    python seed_railway_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from taman.models import Taman, Daerah, StatusTanah, Facility

# --- Seed Daerah ---
daerah_list = [
    'Johor Bahru', 'Kluang', 'Batu Pahat', 'Muar', 'Kulai',
    'Segamat', 'Tangkak', 'Mersing', 'Pontian', 'Kota Tinggi',
    'Pengerang', 'Labis',
]
for nama in daerah_list:
    Daerah.objects.get_or_create(nama=nama, defaults={'status': 'Active'})
print(f'Seeded {len(daerah_list)} daerah')

# --- Seed Status Tanah ---
status_list = [
    ('Pemilikan Kerajaan Negeri', 'Tanah milik kerajaan negeri'),
    ('Pemilikan PBT', 'Tanah milik Pihak Berkuasa Tempatan'),
    ('Sewaan', 'Tanah disewa daripada pemilik persendirian'),
    ('Rizab Hutan', 'Kawasan hutan simpan kekal'),
]
for nama, keterangan in status_list:
    StatusTanah.objects.get_or_create(nama=nama, defaults={'keterangan': keterangan, 'status': 'Active'})
print(f'Seeded {len(status_list)} status tanah')

# --- Seed Facilities ---
facilities = [
    ('Tandas', 'Infrastruktur'),
    ('Taman Permainan', 'Kemudahan'),
    ('Tempat Letak Kereta', 'Infrastruktur'),
    ('Surau / Tempat Ibadat', 'Infrastruktur'),
]
for nama, kategori in facilities:
    Facility.objects.get_or_create(nama=nama, defaults={'kategori': kategori, 'status': 'Active'})
print(f'Seeded {len(facilities)} facilities')

# --- Seed Taman ---
taman_data = [
    {
        'nama': 'Taman Merdeka',
        'lokasi': 'Jalan Taman Merdeka, Johor Bahru',
        'daerah': 'Johor Bahru',
        'keluasan': '30',
        'jenis': 'Taman Tempatan',
        'pbt': 'MBJB',
        'latitude': '1.4655',
        'longitude': '103.7583',
        'tandas': True, 'playground': True, 'parking': True, 'surau': True,
        'deskripsi': 'Taman Merdeka merupakan sebuah taman awam yang luas dan mendamaikan di tengah bandaraya Johor Bahru. Ia menawarkan persekitaran yang sesuai untuk riadah keluarga dengan kemudahan yang lengkap.',
    },
    {
        'nama': 'Taman Rekreasi Gunung Lambak',
        'lokasi': 'Jalan Gunung Lambak, Kluang',
        'daerah': 'Kluang',
        'keluasan': '50',
        'jenis': 'Taman Rekreasi',
        'pbt': 'Rizab Hutan',
        'latitude': '2.0358',
        'longitude': '103.3217',
        'tandas': True, 'playground': False, 'parking': True, 'surau': True,
        'deskripsi': 'Destinasi popular bagi pendaki dan pencinta alam. Taman Rekreasi Gunung Lambak di Kluang menyajikan keindahan alam semula jadi hutan simpan yang sesuai untuk aktiviti lasak dan santai.',
    },
    {
        'nama': 'Taman Botani Batu Pahat',
        'lokasi': 'Jalan Kluang, Batu Pahat',
        'daerah': 'Batu Pahat',
        'keluasan': '15',
        'jenis': 'Taman Botani',
        'pbt': 'Majlis Perbandaran',
        'latitude': '1.8456',
        'longitude': '102.9283',
        'tandas': True, 'playground': True, 'parking': True, 'surau': False,
        'deskripsi': 'Taman Botani ini menyimpan pelbagai spesies flora yang unik. Sesuai sebagai tempat pembelajaran sambil beriadah, terutamanya bagi penduduk sekitar Batu Pahat.',
    },
    {
        'nama': 'Taman Hutan Bandar Muar',
        'lokasi': 'Jalan Salleh, Muar',
        'daerah': 'Muar',
        'keluasan': '12',
        'jenis': 'Taman Awam',
        'pbt': 'Majlis Perbandaran',
        'latitude': '2.0658',
        'longitude': '102.5683',
        'tandas': True, 'playground': True, 'parking': True, 'surau': True,
        'deskripsi': 'Terletak di muara Sungai Muar, taman ini sangat sesuai untuk riadah petang sambil menikmati pemandangan matahari terbenam dan pesona bot-bot nelayan.',
    },
    {
        'nama': 'Taman Rekreasi Kulai',
        'lokasi': 'Jalan Kulai Besar, Kulai',
        'daerah': 'Kulai',
        'keluasan': '150',
        'jenis': 'Taman Rekreasi',
        'pbt': 'Majlis Perbandaran',
        'latitude': '1.6733',
        'longitude': '103.6033',
        'tandas': True, 'playground': True, 'parking': True, 'surau': True,
        'deskripsi': 'Sebuah taman rekreasi berskala besar di Kulai yang mempunyai tasik buatan, trek joging yang teduh, dan pelbagai kemudahan riadah untuk semua lapisan umur.',
    },
    {
        'nama': 'Taman Persisir Pantai Pontian',
        'lokasi': 'Jalan Pantai, Pontian',
        'daerah': 'Pontian',
        'keluasan': '5',
        'jenis': 'Taman Awam',
        'pbt': 'Majlis Daerah',
        'latitude': '1.4856',
        'longitude': '103.3883',
        'tandas': True, 'playground': True, 'parking': True, 'surau': False,
        'deskripsi': 'Taman ini menawarkan pemandangan Selat Melaka yang indah. Ia merupakan kawasan tumpuan penduduk tempatan bersiar-siar sambil menikmati bayu laut pada waktu petang.',
    },
    {
        'nama': 'Taman Hutan Lipur Air Terjun Sungai Tampok',
        'lokasi': 'Jalan Tampok, Tangkak',
        'daerah': 'Tangkak',
        'keluasan': '100',
        'jenis': 'Taman Rekreasi',
        'pbt': 'Rizab Hutan',
        'latitude': '2.2658',
        'longitude': '102.7183',
        'tandas': True, 'playground': False, 'parking': True, 'surau': True,
        'deskripsi': 'Taman rekreasi terkenal dengan air terjun yang sejuk dan jernih di kaki Gunung Ledang. Sangat sesuai untuk perkelahan keluarga dan aktiviti berkhemah.',
    },
    {
        'nama': 'Taman Rekreasi Bentayan Segamat',
        'lokasi': 'Jalan Bentayan, Segamat',
        'daerah': 'Segamat',
        'keluasan': '8',
        'jenis': 'Taman Awam',
        'pbt': 'Majlis Perbandaran',
        'latitude': '2.5058',
        'longitude': '102.8183',
        'tandas': True, 'playground': True, 'parking': True, 'surau': False,
        'deskripsi': 'Taman awam utama di pusat bandar Segamat. Dilengkapi dengan taman permainan kanak-kanak dan kawasan hijau yang luas untuk aktiviti komuniti setempat.',
    },
    {
        'nama': 'Taman Sri Mersing',
        'lokasi': 'Jalan Endau, Mersing',
        'daerah': 'Mersing',
        'keluasan': '10',
        'jenis': 'Taman Awam',
        'pbt': 'Majlis Daerah',
        'latitude': '2.4283',
        'longitude': '103.8283',
        'tandas': True, 'playground': True, 'parking': True, 'surau': True,
        'deskripsi': 'Taman rekreasi di tebing Sungai Johor ini sering menjadi lokasi acara komuniti dan persinggahan pelancong yang berkunjung ke daerah bersejarah ini.',
    },
    {
        'nama': 'Taman Persisir Pantai Mersing',
        'lokasi': 'Jalan Jeti, Mersing',
        'daerah': 'Mersing',
        'keluasan': '6',
        'jenis': 'Taman Awam',
        'pbt': 'Majlis Daerah',
        'latitude': '2.4558',
        'longitude': '103.8383',
        'tandas': True, 'playground': True, 'parking': True, 'surau': True,
        'deskripsi': 'Terletak berhampiran jeti utama ke pulau-pulau, taman ini menawarkan kawasan santai dengan pemandangan laut yang tenang untuk warga Mersing dan pelancong.',
    },
]

created_count = 0
for data in taman_data:
    obj, was_created = Taman.objects.get_or_create(
        nama=data['nama'],
        defaults=data
    )
    if was_created:
        created_count += 1
        print(f'Created: {data["nama"]}')
    else:
        print(f'Already exists: {data["nama"]}')

print(f'\nDone! Seeded {created_count} taman, {len(daerah_list)} daerah, {len(status_list)} status tanah, {len(facilities)} facilities.')
