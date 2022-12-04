# from django.db import models
# from django.core.exceptions import ValidationError

# # Create your models here.


# class ModelTindakan(models.Model):
# 	KONSULTASI_CHOICES = (
# 	('1', '1'),
# 	('2', '2'),
# 	('3', '3'),
# 	('4', '4'),
# 	('5', '5'),
# 	)

# 	TRANSAKSI_CHOICES = (
# 	('1', '1'),
# 	('2', '2'),
# 	('3', '3'),
# 	('4', '4'),
# 	('5', '5'),
# 	)

# 	TINDAKAN_KLINIK_CHOICES = (
# 	('1', '1'),
# 	('2', '2'),
# 	('3', '3'),
# 	('4', '4'),
# 	('5', '5'),
# 	)

# 	IDKonsultasi		= models.CharField(max_length=10, choices=KONSULTASI_CHOICES)
# 	IDTransaksi 		= models.CharField(max_length=50, choices=TRANSAKSI_CHOICES)
# 	Catatan				= models.TextField(max_length=100)
# 	IDTindakanKlinik 	= models.CharField(max_length=50, choices=TINDAKAN_KLINIK_CHOICES)


# class ModelTindakanPoliklinik(models.Model):
# 	POLIKLINIK_CHOICES = (
# 	('1', '1'),
# 	('2', '2'),
# 	('3', '3'),
# 	('4', '4'),
# 	('5', '5'),
# 	)

# 	IDPoliklinik		= models.CharField(max_length=10, choices=POLIKLINIK_CHOICES)
# 	NamaTindakan 		= models.CharField(max_length=20)
# 	Deskripsi			= models.TextField(max_length=50)
# 	Tarif			 	= models.CharField(max_length=20)
