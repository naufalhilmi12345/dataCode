from django import forms
from django.db import connection
from django.forms import widgets
import datetime

class CreateSesiKonsultasi(forms.Form):
	cursor = connection.cursor()

	select1 = []
	cursor.execute("select no_rekam_medis from medikago.pasien")
	select1 = cursor.fetchall()
	no_rekam_medis_pasien = forms.ChoiceField(label='Nomor Rekam Medis Pasien', choices=[(i[0], i[0]) for i in select1], widget=forms.Select(attrs={'class': 'form-control', 'required': True}))
	
	tanggal = forms.DateField(label='Tanggal (yyyy-mm-dd)', initial=datetime.date.today, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
	
	select2 = []
	cursor.execute("select id_transaksi from medikago.transaksi")
	select2 = cursor.fetchall()
	id_transaksi = forms.ChoiceField(label='ID Transaksi', choices=[(i[0], i[0]) for i in select2],	widget=forms.Select(attrs={'class': 'form-control', 'required': True}))

class UpdateSesiKonsultasi(forms.Form):
	tanggal = forms.DateField(label='Tanggal (yyyy-mm-dd)', initial=datetime.date.today, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
	status = forms.CharField(label='Status', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))

class CreateRSCabang(forms.Form):
	kode_rs_cabang = forms.CharField(label='Kode RS', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
	nama = forms.CharField(label='Nama', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
	tanggal_pendirian = forms.DateField(label='Tanggal Pendirian (yyyy-mm-dd)', widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
	jalan = forms.CharField(label='Jalan', max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
	nomor = forms.CharField(label='Nomor', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
	kota = forms.CharField(label='Kota', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))

class UpdateRSCabang(forms.Form):
	nama = forms.CharField(label='Nama', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
	tanggal_pendirian = forms.DateField(label='Tanggal Pendirian (yyyy-mm-dd)', widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
	jalan = forms.CharField(label='Jalan', max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
	nomor = forms.CharField(label='Nomor', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
	kota = forms.CharField(label='Kota', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))