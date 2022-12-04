from django.urls import path
from .views import *

app_name = 'fiturnaufal'

urlpatterns = [
    path('<str:pk>/update_transaksi', update_transaksi, name = 'update_transaksi'),
    path('read_transaksi', read_transaksi, name = 'read_transksi'),
	path('create_transaksi', create_transaksi, name = 'create_transaksi'),
    path('<str:pk>/', delete_transaksi, name = 'delete_transaksi'),
]