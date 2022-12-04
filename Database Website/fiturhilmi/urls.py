from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import *
from . import views

app_name = 'fiturhilmi'

urlpatterns = [
	path('admin/', admin.site.urls),
	path('create_tindakan', create_tindakan, name = 'create_tindakan'),
	path('profile', profile, name = 'profile'),
	path('view_daftar_tindakan', view_daftar_tindakan, name = 'view_daftar_tindakan'),
	path('update_tindakan/<id>/', update_tindakan, name = 'update_tindakan'),
	path('create_tindakan_poliklinik', create_tindakan_poliklinik, name = 'create_tindakan_poliklinik'),
	path('view_daftar_tindakan_poliklinik', view_daftar_tindakan_poliklinik, name = 'view_daftar_tindakan_poliklinik'),
	path('update_tindakan_poliklinik/<id>/', update_tindakan_poliklinik, name = 'update_tindakan_poliklinik'),
	url('delete', delete, name='delete'),
	url('delete_poliklinik', delete_poliklinik, name='delete_poliklinik'),
	url('delete_poliklinik_', delete_poliklinik_, name='delete_poliklinik_')
]