from django import forms
import datetime

class login_form(forms.Form):
    username = forms.CharField(max_length = 50)
    password = forms.CharField(widget = forms.PasswordInput())

class DaftarAdministrator(forms.Form):
    username = forms.CharField(max_length = 50)
    password = forms.CharField(max_length = 50)
    no_id = forms.CharField(max_length = 50)
    nama = forms.CharField(max_length = 50)
    ttl = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Tanggal Lahir',
        'type' : 'date',
        'required' : True
    }))
    email = forms.CharField(max_length = 50)
    alamat = forms.CharField(max_length = 50)

class DaftarDokter(forms.Form):
    username = forms.CharField(max_length = 50)
    password = forms.CharField(max_length = 50)
    no_id = forms.CharField(max_length = 50)
    nama = forms.CharField(max_length = 50)
    ttl = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Tanggal Lahir',
        'type' : 'date',
        'required' : True
    }))
    email = forms.CharField(max_length = 50)
    alamat = forms.CharField(max_length = 50)
    sip = forms.CharField(max_length = 50)
    spesialisasi = forms.CharField(max_length = 50)

class DaftarPasien(forms.Form):
    username = forms.CharField(max_length = 50)
    password = forms.CharField(max_length = 50)
    no_id = forms.CharField(max_length = 50)
    nama = forms.CharField(max_length = 50)
    ttl = forms.DateField(widget = forms.DateInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Tanggal Lahir',
        'type' : 'date',
        'required' : True
    }))
    email = forms.CharField(max_length = 50)
    alamat = forms.CharField(max_length = 50)
    alergi = forms.CharField(max_length = 50)
