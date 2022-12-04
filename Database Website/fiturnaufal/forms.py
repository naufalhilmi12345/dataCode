from django import forms
from django.db import connection

class transaksi(forms.Form):
    Id_Transaksi = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control',
        'type' : 'text',
        'readonly' : True
    }))
    Tanggal = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Tanggal',
        'type' : 'date',
        'required' : True
    }))
    Status = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Status',
        'type' : 'text',
        'required' : True
    }))
    Total_Biaya = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control',
        'type' : 'text',
        'readonly' : True
    }))
    Waktu_Pembayaran = forms.DateTimeField(widget = forms.DateTimeInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Waktu Pembayaran',
        'type' : 'datetime-local',
        'required' : True
    }))
    Nomor_Rekam_Medis_Pasien = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control',
        'type' : 'text',
        'readonly' : True
    }))

cursor = connection.cursor()
cursor.execute('select no_rekam_medis from medikago.pasien')
hasil = cursor.fetchall()
nomor_rmp_list = []
for nmr_pasien in hasil:
    nomor_rmp_list.append((nmr_pasien[0], nmr_pasien[0]))

class pembuatan_transaksi(forms.Form):
    nomor_rmp = forms.ChoiceField(label='Nomor Rekam Medis Pasien', choices=nomor_rmp_list, widget=forms.Select)