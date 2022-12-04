from django.shortcuts import render, redirect
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from collections import namedtuple
from .forms import *

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def create_sesi_konsultasi(request):
    if (request.method == 'POST' and request.session['role'] == 'administrator'):
        cursor = connection.cursor()
        cursor.execute("select id_konsultasi from medikago.sesi_konsultasi order by id_konsultasi desc limit 1")
        fetch_id = cursor.fetchone()[0].split('konsul')
        id_konsultasi = 'konsul' + str(int(fetch_id[1]) + 1)

        no_rekam_medis_pasien = request.POST["no_rekam_medis_pasien"]     # [dari forms.py]
        tanggal = request.POST.get("tanggal")
        biaya = 0
        status = "Booked"
        id_transaksi = request.POST["id_transaksi"]

        cursor.execute(
            "insert into medikago.sesi_konsultasi values (%s,%s,%s,%s,%s,%s)",
            [id_konsultasi, no_rekam_medis_pasien, tanggal, biaya, status, id_transaksi]
        )
        return redirect('/fiturkamila/view_sesi_konsultasi')

    form = CreateSesiKonsultasi()
    args = {'form': form}
    return render(request, 'create_sesi_konsultasi.html', args)

def view_sesi_konsultasi(request):
    dataset = []
    cursor = connection.cursor()
    if (request.session['role'] == 'pasien'):
        cursor.execute("select no_rekam_medis from medikago.pasien where username like '{}'".format(request.session['username']))
        nmr_rekam_medis = cursor.fetchall()[0][0]
        cursor.execute("select * from medikago.sesi_konsultasi where no_rekam_medis_pasien like '{}'".format(nmr_rekam_medis))
        dataset = namedtuplefetchall(cursor)
        return render(request, 'view_sesi_konsultasi.html', {'table': dataset})
    else:
        cursor.execute("select * from medikago.sesi_konsultasi")
        dataset = namedtuplefetchall(cursor)
        return render(request, 'view_sesi_konsultasi.html', {'table': dataset})

def update_sesi_konsultasi(request, id):
    cursor = connection.cursor()
    if (request.method == 'POST' and request.session['role'] == 'administrator'):
        tanggal = request.POST.get("tanggal")
        status = request.POST.get("status")

        if tanggal == "":
            cursor.execute("select tanggal from medikago.sesi_konsultasi where id_konsultasi='"+ id +"';")
            tanggal = cursor.fetchone()[0]
        
        if status == "":
            cursor.execute("select status from medikago.sesi_konsultasi where id_konsultasi='"+ id +"';")
            status = cursor.fetchone()[0]

        cursor.execute("update medikago.sesi_konsultasi set tanggal ='"+ tanggal +"',status ='"+ status +"' where id_konsultasi ='"+ id +"';")
        return redirect('/fiturkamila/view_sesi_konsultasi')

    cursor.execute("select id_konsultasi from medikago.sesi_konsultasi where id_konsultasi='"+ id +"';")
    idkonsul = cursor.fetchone()[0]
    
    cursor.execute("select no_rekam_medis_pasien from medikago.sesi_konsultasi where id_konsultasi='"+ id +"';")
    nopasien = cursor.fetchone()[0]

    cursor.execute("select id_transaksi from medikago.sesi_konsultasi where id_konsultasi='"+ id +"';")
    idtrans = cursor.fetchone()[0]

    form = UpdateSesiKonsultasi()
    args = {'form':form, 'idkonsul':idkonsul, 'nopasien':nopasien, 'idtrans':idtrans, "id":id}
    return render(request, 'update_sesi_konsultasi.html', args)

def delete_sesi_konsultasi(request, id):
    if (request.method == 'GET' and request.session['role'] == 'administrator'):
        cursor = connection.cursor()
        delete_sk = "delete from medikago.sesi_konsultasi where id_konsultasi = '" + id + "'"
        cursor.execute(delete_sk)
        return redirect('/fiturkamila/view_sesi_konsultasi')
    
def create_rs_cabang(request):
    if (request.method == 'POST' and request.session['role'] == 'administrator'):
        cursor = connection.cursor()
        select_rs = "select * from medikago.rs_cabang order by kode_rs desc"
        cursor.execute(select_rs)

        kode_rs = request.POST.get('kode_rs_cabang')
        nama = request.POST["nama"]     # [dari forms.py]
        tanggal_pendirian = request.POST.get("tanggal_pendirian")
        jalan = request.POST["jalan"]
        nomor = request.POST["nomor"]
        kota = request.POST["kota"]
        
        cursor.execute(
            "insert into medikago.rs_cabang values (%s, %s, %s, %s, %s, %s)", 
            [kode_rs, nama, tanggal_pendirian, jalan, nomor, kota]
        )
        return redirect('/fiturkamila/view_rs_cabang')
    
    form = CreateRSCabang()
    args = {'form': form}
    return render(request, 'create_rs_cabang.html', args)

def view_rs_cabang(request):
    dataset = []
    cursor = connection.cursor()
    cursor.execute("select * from medikago.rs_cabang")
    dataset = namedtuplefetchall(cursor)
    return render(request, 'view_rs_cabang.html', {'table': dataset})

def update_rs_cabang(request, id):
    cursor = connection.cursor()
    if (request.method == 'POST' and request.session['role'] == 'administrator'):
        nama = request.POST.get("nama")
        tanggal_pendirian = request.POST.get("tanggal_pendirian")
        jalan = request.POST.get("jalan")
        kota = request.POST.get("kota")
        nomor = request.POST.get("nomor")

        if nama != "":
            cursor.execute("update medikago.rs_cabang set nama ='" + nama +"' where kode_rs ='" + id + "';")
        
        if tanggal_pendirian != "":
            cursor.execute("update medikago.rs_cabang set tanggal_pendirian ='" + tanggal_pendirian +"' where kode_rs ='" + id + "';")
        
        if jalan != "":
            cursor.execute("update medikago.rs_cabang set jalan ='" + jalan +"' where kode_rs ='" + id + "';")
        
        if kota != "":
            cursor.execute("update medikago.rs_cabang set kota ='" + kota +"' where kode_rs ='" + id + "';")
        
        if nomor != "":
            cursor.execute("update medikago.rs_cabang set nomor ='" + nomor +"' where kode_rs ='" + id + "';")

        return redirect('/fiturkamila/view_rs_cabang')

    cursor.execute("select kode_rs from medikago.rs_cabang where kode_rs='"+ id +"';")
    koders = cursor.fetchone()[0]

    form = UpdateRSCabang()
    args = {'form': form, 'koders' : koders, "id" : id}
    return render(request, 'update_rs_cabang.html', args)

def delete_rs_cabang(request, id):
    if (request.method == 'GET' and request.session['role'] == 'administrator'):
        cursor = connection.cursor()
        delete_rs = "delete from medikago.rs_cabang where kode_rs = '" + id + "'"
        cursor.execute(delete_rs)
        return redirect('/fiturkamila/view_rs_cabang')