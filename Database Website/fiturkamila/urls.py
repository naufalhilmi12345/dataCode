from django.urls import path, include
from .views import *

app_name = 'fiturkamila'

urlpatterns = [
    path('create_sesi_konsultasi', create_sesi_konsultasi, name = 'create_sesi_konsultasi'),
    path('view_sesi_konsultasi', view_sesi_konsultasi, name = 'view_sesi_konsultasi'),
    path('update_sesi_konsultasi/<id>/', update_sesi_konsultasi, name = 'update_sesi_konsultasi'),
    path('delete_sesi_konsultasi/<id>/', delete_sesi_konsultasi, name = 'delete_sesi_konsultasi'),
    path('create_rs_cabang', create_rs_cabang, name = 'create_rs_cabang'),
    path('view_rs_cabang', view_rs_cabang, name = 'view_rs_cabang'),
    path('update_rs_cabang/<id>/', update_rs_cabang, name = 'update_rs_cabang'),
    path('delete_rs_cabang/<id>/', delete_rs_cabang, name = 'delete_rs_cabang'),
]