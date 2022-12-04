from django import forms
from django.db import connection
from django.forms import widgets
import datetime


class CreateTindakanPoliklinikForm(forms.Form):
	cursor = connection.cursor()
	pilihan_id_poliklinik = []
	cursor.execute("select id_poliklinik from medikago.layanan_poliklinik")
	pilihan_id_poliklinik = cursor.fetchall()
	IDPoliklinik = forms.ChoiceField(label='ID Poliklinik', choices=[(i[0], i[0]) for i in pilihan_id_poliklinik], widget=forms.Select(attrs={'class': 'form-control'}))
	

	# IDPoliklinik = forms.CharField(label='ID Poliklinik', widget=forms.Select(choices=dropdown1, attrs={'class': 'form-control', 'required': True}))
	NamaTindakan = forms.CharField(label='Nama Tindakan', max_length=50, widget=forms.Textarea(attrs={'cols': 120, 'rows': 2}))
	Deskripsi = forms.CharField(label='Deskripsi', max_length=50, widget=forms.Textarea(attrs={'cols': 120, 'rows': 2}), required=False)
	Tarif = forms.IntegerField(label='Tarif')

class UpdateTindakanPoliklinikForm(forms.Form):
	cursor = connection.cursor()
	pilihan_id_tindakan_poli = []
	cursor.execute("select id_tindakan_poli from medikago.tindakan_poli")
	pilihan_id_tindakan_poli = cursor.fetchall()
	# IDTindakanPoliklinik = forms.ChoiceField(label='ID Tindakan Poliklinik', choices=[(i[0], i[0]) for i in pilihan_id_tindakan_poli], widget=forms.Select(attrs={'class': 'form-control', 'readonly':True}))
	cursor = connection.cursor()
	pilihan_id_poliklinik = []
	cursor.execute("select id_poliklinik from medikago.layanan_poliklinik")
	pilihan_id_poliklinik = cursor.fetchall()
	IDPoliklinik = forms.ChoiceField(label='ID Poliklinik', choices=[(i[0], i[0]) for i in pilihan_id_poliklinik], widget=forms.Select(attrs={'class': 'form-control'}))
	NamaTindakan = forms.CharField(label='Nama Tindakan', max_length=50)
	Deskripsi = forms.CharField(label='Deskripsi', max_length=50, widget=forms.Textarea(attrs={'cols': 120, 'rows': 2}), required=False)
	Tarif = forms.IntegerField(label='Tarif')

class CreateTindakanForm(forms.Form):
	cursor = connection.cursor()
	pilihan_id_konsultasi = []
	pilihan_id_transaksi = []
	cursor.execute("select id_konsultasi from medikago.sesi_konsultasi")
	pilihan_id_konsultasi = cursor.fetchall()
	IDKonsultasi = forms.ChoiceField(label='ID Konsultasi', choices=[(i[0], i[0]) for i in pilihan_id_konsultasi], widget=forms.Select(attrs={'class': 'form-control'}))
	cursor.execute("select id_transaksi from medikago.transaksi")
	pilihan_id_transaksi = cursor.fetchall()
	IDTransaksi = forms.ChoiceField(label='ID Transaksi', choices=[(i[0], i[0]) for i in pilihan_id_transaksi], widget=forms.Select(attrs={'class': 'form-control'}))
	Catatan = forms.CharField(label='Catatan', widget=forms.Textarea(attrs={'cols': 120, 'rows': 2}), required=False)
	pilihan_id_tindakan_poli = []
	cursor.execute("select id_tindakan_poli from medikago.tindakan_poli")
	options = cursor.fetchall()
	for option in options:
		nomor = (option[0], option[0])
		pilihan_id_tindakan_poli.append(nomor)
	IDTindakanKlinik = forms.MultipleChoiceField(choices=pilihan_id_tindakan_poli, label = 'ID Tindakan Poliklinik', widget=forms.CheckboxSelectMultiple())
 
	# IDTindakanKlinik = forms.ChoiceField(label='Daftar ID Tindakan Klinik', choices=[(i[0], i[0]) for i in pilihan_id_tindakan_poli], widget=forms.Select(attrs={'class': 'form-control'}))

class UpdateTindakanForm(forms.Form):
	# IDKonsultasi = forms.CharField(label='ID Konsultasi', widget=forms.Select(choices=dropdown3, attrs={'class': 'form-control', 'required': True}))
	# NoUrut = forms.IntegerField(label='No Urut', max_length=3)
	# Biaya = forms.IntegerField(label='Biaya', max_length=50)
	Catatan = forms.CharField(label='Catatan', max_length=50, widget=forms.Textarea(attrs={'cols': 120, 'rows': 2}), required=False)
	# IDTransaksi = forms.CharField(label='ID Transaksi', widget=forms.Select(choices=dropdown4, attrs={'class': 'form-control', 'required': True}))
	# IDTindakanKlinik = forms.CharField(label='Daftar ID Tindakan Klinik', widget=forms.Select(choices=dropdown5, attrs={'class': 'form-control', 'required': True}))


# from django import forms

# from .models import ModelTindakan, ModelTindakanPoliklinik
# from django.forms import ModelForm

# class CreateTindakanForm(forms.ModelForm):

#     Catatan = forms.CharField(required=False, widget=forms.Textarea)

#     class Meta:
#         model = ModelTindakan
#         fields = [
#             'IDKonsultasi',
#             'IDTransaksi',
#             'Catatan',
#             'IDTindakanKlinik'
#         ]
#         labels  = {
#         'IDKonsultasi':'ID Konsultasi',
#         'IDTransaksi' : 'ID Transaksi',
#         'IDTindakanKlinik' : 'ID Tindakan Klinik'
#         }

# class CreateTindakanPoliklinikForm(forms.ModelForm):

#     Deskripsi = forms.CharField(required=False, widget=forms.Textarea)

#     class Meta:
#         model = ModelTindakanPoliklinik
#         fields = [
#             'IDPoliklinik',
#             'NamaTindakan',
#             'Deskripsi',
#             'Tarif'
#         ]
#         labels  = {
#         'IDPoliklinik':'ID Poliklinik',
#         'NamaTindakan' : 'Nama Tindakan'
#         }

# class UpdateTindakanPoliklinikForm(forms.ModelForm):

#     class Meta:
#         model = ModelTindakanPoliklinik
#         fields = [
#             'NamaTindakan',
#             'Deskripsi',
#             'Tarif'
#         ]
#         labels  = {
#         'IDPoliklinik':'ID Poliklinik',
#         'NamaTindakan' : 'Nama Tindakan'
#         }

# class UpdateTindakanForm(forms.ModelForm):

#     class Meta:
#         model = ModelTindakan
#         fields = [
#             'Catatan'
#         ]
