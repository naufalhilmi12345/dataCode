from django.urls import path
from .views import *

app_name = 'login'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('', homepage, name='homepage'),
    path('daftar_admin', daftar_admin, name = 'daftar_admin'),
    path('regis_dokter', daftar_dokter, name = 'daftar_dokter'),
    path('daftar_pasien', daftar_pasien, name = 'daftar_pasien'),
]