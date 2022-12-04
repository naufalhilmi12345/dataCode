# Generated by Django 2.2.5 on 2020-05-05 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiturhilmi', '0002_auto_20200504_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltindakan',
            name='IDKonsultasi',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10),
        ),
        migrations.AlterField(
            model_name='modeltindakan',
            name='IDTindakanKlinik',
            field=models.TextField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=50),
        ),
        migrations.AlterField(
            model_name='modeltindakan',
            name='IDTransaksi',
            field=models.TextField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=50),
        ),
    ]