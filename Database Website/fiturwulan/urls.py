from django.urls import path
from .views import *

app_name = 'fiturwulan'

urlpatterns = [
    path('daftar_dokter', daftar_dokter, name = 'daftar_dokter'),
    path('view_dokter', view_dokter, name = 'view_dokter'),
	path('create_layanan_poliklinik', create_layanan_poliklinik, name = 'create_layanan_poliklinik'),
    path('view_layanan_poliklinik', view_layanan_poliklinik, name = 'view_layanan_poliklinik'),
    path('view_jadwal_poliklinik', view_jadwal_poliklinik, name = 'view_jadwal_poliklinik'),
    path('update_dokter', update_dokter, name = 'update_dokter'),
    path('update_layanan_poliklinik/<id>/', update_layanan_poliklinik, name = 'update_layanan_poliklinik'),
    path('update_jadwal_poliklinik/<id>/', update_jadwal_poliklinik, name = 'update_jadwal_poliklinik'),
    path('delete_dokter', delete_dokter, name = 'delete_dokter'),
    path('delete_layanan_poliklinik/<id>/', delete_layanan_poliklinik, name = 'delete_layanan_poliklinik'),
    path('delete_jadwal_poliklinik/<id>/', delete_jadwal_poliklinik, name = 'delete_jadwal_poliklinik'),
]