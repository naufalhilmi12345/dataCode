from django.shortcuts import render, redirect
from .forms import *
from django.db import connection
from datetime import datetime

# Create your views here.
def read_transaksi(request):
    cursor = connection.cursor()
    if (request.session['role'] == 'administrator' or request.session['role'] == 'dokter'):
        cursor.execute('select * from medikago.transaksi order by tanggal desc')
        hasil = cursor.fetchall()
        response = {'hasil': hasil}
        return render(request,'read_transaksi.html', response)
    else:
        cursor.execute("select no_rekam_medis from medikago.pasien where username like '{}'".format(request.session['username']))
        nmr_rekam_medis = cursor.fetchall()[0][0]
        cursor.execute("select * from medikago.transaksi where no_rekam_medis like '{}' order by tanggal desc".format(nmr_rekam_medis))
        hasil = cursor.fetchall()
        response = {'hasil': hasil}
        return render(request,'read_transaksi.html', response)

def delete_transaksi(request, pk):
    if (request.session['role'] == 'administrator'):
        cursor = connection.cursor()
        cursor.execute('delete from medikago.transaksi where id_transaksi like ' + "'" + pk + "'")
        return redirect('/fiturnaufal/read_transaksi')
    else:
        return redirect('/fiturnaufal/read_transaksi')

def create_transaksi(request):
    if (request.session['role'] == 'administrator'):
        cursor = connection.cursor()
        if request.method == 'POST':
            form = pembuatan_transaksi(request.POST)
            if form.is_valid():
                nomor_rmp = form.cleaned_data['nomor_rmp']
                cursor.execute("select id_transaksi from medikago.transaksi order by id_transaksi desc limit 1")
                id_transaksi_terakhir = int(cursor.fetchall()[0][0])
                cursor.execute("insert into medikago.transaksi values ('{}','{}','{}','{}','{}','{}')"
                .format((id_transaksi_terakhir+1),datetime.now().date(),'Created',0,datetime.now(),nomor_rmp))
            return redirect('/fiturnaufal/read_transaksi')
        else:
            form = pembuatan_transaksi()
            response = {
                'form' : form
            }
            return render(request, 'create_transaksi.html', response)
    else:
        return redirect('/fiturnaufal/read_transaksi')


def update_transaksi(request, pk):
    if (request.session['role'] == 'administrator'):
        cursor = connection.cursor()
        if request.method =='POST':
            form = pembuatan_transaksi(request.POST)
            tanggal = request.POST.get('Tanggal')
            status = request.POST.get('Status')
            waktu_pembayaran = request.POST.get('Waktu_Pembayaran')
            cursor.execute("update medikago.transaksi set tanggal = '{}', status = '{}', waktu_pembayaran = '{}' where id_transaksi like '{}'"
            .format(tanggal, status, waktu_pembayaran, pk))
            return redirect('/fiturnaufal/read_transaksi')
        else: 
            cursor.execute('select no_rekam_medis, total_biaya, id_transaksi from medikago.transaksi where id_transaksi like ' + "'" + pk + "'")
            hasil = cursor.fetchall()
            form = transaksi(initial={
                'Nomor_Rekam_Medis_Pasien': hasil[0][0],
                'Total_Biaya': hasil[0][1],
                'Id_Transaksi': hasil[0][2]
            })
            args = {'form': form}
            return render(request, 'update_transaksi.html', args)
    else:
        return redirect('/fiturnaufal/read_transaksi')