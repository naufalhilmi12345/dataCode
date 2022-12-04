from django import forms
from django.forms import widgets
from django.db import connection

cursor = connection.cursor()
cursor.execute("SELECT id_dokter FROM medikago.dokter")
select = cursor.fetchall()
cursor.execute("SELECT kode_rs FROM medikago.rs_cabang")
select1 = cursor.fetchall()

id_dokter = [tuple([select[x][0], select[x][0]]) for x in range(len(select))]
kode_rs = [tuple([select1[y][0], select1[y][0]]) for y in range(len(select1))]

# DAFTAR DOKTER
class DaftarDokterForm(forms.Form):
    dropdown_id_dokter = forms.CharField(label="Id Dokter", widget=forms.Select(choices=id_dokter, attrs={
        'class': 'form-control'
    }))
    dropdown_kode_rs = forms.CharField(label="Kode RS", widget=forms.Select(choices=kode_rs, attrs={
        'class': 'form-control'
    }))

# UPDATE DOKTER
class UpdateDokter(forms.Form):
    dropdown_id_dokter = forms.CharField(label="Id Dokter", widget=forms.Select(choices=id_dokter, attrs={
        'class': 'form-control'
    }))
    dropdown_kode_rs = forms.CharField(label="Kode RS", widget=forms.Select(choices=kode_rs, attrs={
        'class': 'form-control'
    }))

# CREATE LAYANAN POLIKLINIK
class CreatePoliklinikForm(forms.Form):
    nama_layanan = forms.CharField(label='Nama Layanan', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}) )
    deskripsi = forms.CharField(label='Deskripsi', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    dropdown_kode_rs = forms.CharField(label="Kode RS", widget=forms.Select(choices=kode_rs, attrs={
        'class': 'form-control'
    }))
    hari = forms.CharField(label='Hari', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    mulai = forms.CharField(label='Waktu Mulai', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    selesai = forms.CharField(label='Waktu Selesai', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    kapasitas = forms.CharField(label='Kapasitas', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))

# UPDATE LAYANAN POLIKLINIK
class UpdateLayananPoliklinik(forms.Form):
    id_poliklinik = forms.CharField(label='ID Poliklinik', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': False, 'readonly':'readonly'}) )
    nama_layanan = forms.CharField(label='Nama Layanan', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}) )
    deskripsi = forms.CharField(label='Deskripsi', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}) )
    dropdown_kode_rs = forms.CharField(label="RS Cabang Penyedia Layanan", widget=forms.Select(choices=kode_rs, attrs={
        'class': 'form-control'
    }))

# UPDATE JADWAL POLIKLINIK
class UpdateJadwalPoliklinik(forms.Form):
    id_jadwal_poliklinik = forms.CharField(label='ID Jadwal Poliklinik', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True, 'readonly':'readonly'}) )
    hari = forms.CharField(label='Hari', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}) )
    mulai = forms.CharField(label='Waktu Mulai', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}) )
    selesai = forms.CharField(label='Waktu Selesai', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}) )
    kapasitas = forms.CharField(label='Kapasitas', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}) )
    dropdown_id_dokter = forms.CharField(label="Id Dokter", widget=forms.Select(choices=id_dokter, attrs={
        'class': 'form-control'
    }))
    id_poliklinik = forms.CharField(label='ID Poliklinik', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True, 'readonly':'readonly'}) )

