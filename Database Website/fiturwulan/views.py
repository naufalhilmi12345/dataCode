from django.shortcuts import render, redirect, reverse
from django.db import connection
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from medikago.settings import STATIC_DIR
import os
from collections import namedtuple

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

# DAFTAR DOKTER
def daftar_dokter(request):
    if (request.method == 'POST' and request.session['role'] == 'administrator'):
        cursor = connection.cursor()
        select_sk = "select id_dokter from medikago.dokter order by id_dokter desc limit 1"
        cursor.execute(select_sk)
        select_sk1 = "select kode_rs from medikago.rs_cabang order by kode_rs desc limit 1"
        cursor.execute(select_sk1)

        id_dokter = request.POST["dropdown_id_dokter"]  
        kode_rs = request.POST["dropdown_kode_rs"]  

        try: 
            cursor.execute(
            "insert into medikago.dokter_rs_cabang values (%s,%s)",
            [id_dokter, kode_rs])
        except:
            return redirect(reverse("fiturwulan:daftar_dokter"))
        return redirect(reverse('fiturwulan:view_dokter'))

    daftar_dokter = DaftarDokterForm()
    args = {'daftar_dokter': daftar_dokter}
    return render(request, 'daftar_dokter.html', args)

# VIEW DOKTER
def view_dokter(request):
    dataset = []
    cursor = connection.cursor()
    cursor.execute("select * from medikago.dokter_rs_cabang")
    dataset = namedtuplefetchall(cursor)
    return render(request, 'view_dokter.html', {'table': dataset})

# UPDATE DOKTER
def update_dokter(request):
    cursor = connection.cursor()
    if(request.method == "GET" and request.session["role"] == "administrator"):
        forms = UpdateDokter()
        args = {'forms': forms}
        return render(request, 'update_dokter.html', args)

    elif (request.method == 'POST' and request.session['role'] == 'administrator'):
        id_dokter_sebelum = request.GET["id_dokter"]
        id_rs_sebelum = request.GET["kode_rs"]
        cursor = connection.cursor()
        dokter = request.POST["dropdown_id_dokter"]
        rs = request.POST["dropdown_kode_rs"]
        cursor.execute(f"UPDATE medikago.dokter_rs_cabang SET id_dokter = '{dokter}', kode_rs = '{rs}' where id_dokter = '{id_dokter_sebelum}' and kode_rs = '{id_rs_sebelum}'")
        return redirect(reverse("fiturwulan:view_dokter"))

# DELETE DOKTER 
def delete_dokter(request):
    if (request.method == 'GET' and request.session["role"] == 'administrator'):
        cursor = connection.cursor()

        if(request.GET["id_dokter"] and request.GET["kode_rs"]):
            id_dokter = request.GET["id_dokter"]
            kode_rs = request.GET["kode_rs"]
            cursor.execute(f"DELETE FROM medikago.dokter_rs_cabang WHERE kode_rs = '{kode_rs}' AND id_dokter = '{id_dokter}'")

        return redirect(reverse('fiturwulan:view_dokter'))

# CREATE LAYANAN POLIKLINIK
def create_layanan_poliklinik(request):
    if (request.method == 'POST'):
        cursor = connection.cursor()
        cursor.execute("select count(*) from medikago.layanan_poliklinik")
        fetch_id = cursor.fetchone()[0]
        id_poliklinik = str(fetch_id + 1)

        cursor.execute("select count(*) from medikago.jadwal_layanan_poliklinik")
        fetch_id1 = cursor.fetchone()[0]
        id_jadwal_poliklinik = fetch_id1 + 1

        nama = request.POST["nama_layanan"]    
        deskripsi = request.POST["deskripsi"]
        kode_rs = request.POST["dropdown_kode_rs"]
        hari = request.POST["hari"]
        mulai = request.POST["mulai"]
        selesai = request.POST["selesai"]
        kapasitas = request.POST["kapasitas"]
        
        cursor.execute("select id_dokter from medikago.jadwal_layanan_poliklinik")
        fetch_id2 = cursor.fetchone()[0]
        id_dokter = fetch_id2

        cursor.execute(
            "insert into medikago.layanan_poliklinik values (%s,%s,%s,%s)",
            [id_poliklinik, kode_rs, nama, deskripsi]
        )

        cursor.execute(
            "insert into medikago.jadwal_layanan_poliklinik values (%s,%s,%s,%s,%s,%s,%s)",
            [id_jadwal_poliklinik, mulai, selesai, hari, kapasitas, id_dokter, id_poliklinik]
        )

        return redirect('fiturwulan:view_layanan_poliklinik')

    form = CreatePoliklinikForm()
    args = {'form': form}
    return render(request, 'create_layanan_poliklinik.html', args)

# VIEW LAYANAN POLIKLINIK
def view_layanan_poliklinik(request):
    dataset = []
    cursor = connection.cursor()
    cursor.execute("select * from medikago.layanan_poliklinik")
    dataset = namedtuplefetchall(cursor)
    return render(request, 'view_layanan_poliklinik.html', {'table': dataset})

# UPDATE LAYANAN POLIKLINIK
def update_layanan_poliklinik(request, id):
    cursor = connection.cursor()

    if (request.method == 'GET' and request.session['role'] == 'administrator'):
        cursor.execute("select * from medikago.layanan_poliklinik where id_poliklinik ='" + id + "';")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        data_layanan = {}
        data_layanan['id_poliklinik'] = data[0]['id_poliklinik']
        form = UpdateLayananPoliklinik(initial=data_layanan)


    elif (request.method == 'POST' and request.session['role'] == 'administrator'):
        kode_rs = request.POST.get("dropdown_kode_rs")
        nama = request.POST.get("nama_layanan")
        deskripsi = request.POST.get("deskripsi")

        if kode_rs != "":
            cursor.execute("update medikago.layanan_poliklinik set kode_rs_cabang ='" + kode_rs +"' where id_poliklinik ='" + id + "';")
        
        if nama != "":
            cursor.execute("update medikago.layanan_poliklinik set nama ='" + nama +"' where id_poliklinik ='" + id + "';")
        
        if deskripsi != "":
            cursor.execute("update medikago.layanan_poliklinik set deskripsi ='" + deskripsi +"' where id_poliklinik ='" + id + "';")

        form = UpdateLayananPoliklinik(request.POST)
        return redirect('fiturwulan:view_layanan_poliklinik')

    cursor.execute("select id_poliklinik from medikago.layanan_poliklinik")
    idpoli = namedtuplefetchall(cursor)
    args = {'form': form, 'idpoli' : idpoli, "id" : id}
    return render(request, 'update_layanan_poliklinik.html', args)

# DELETE LAYANAN POLIKLINIK
def delete_layanan_poliklinik(request, id):
    if (request.method == 'GET' and request.session['role'] == 'administrator'):
        cursor = connection.cursor()
        delete_layanan = "delete from medikago.layanan_poliklinik where id_poliklinik = '" + id + "'"
        cursor.execute(delete_layanan)
        return redirect(reverse('fiturwulan:view_layanan_poliklinik'))

# VIEW JADWAL POLIKLINIK
def view_jadwal_poliklinik(request):
    dataset = []
    cursor = connection.cursor()
    cursor.execute("select * from medikago.jadwal_layanan_poliklinik")
    dataset = namedtuplefetchall(cursor)
    return render(request, 'view_jadwal_poliklinik.html', {'table': dataset})

# UPDATE JADWAL POLIKLINIK
def update_jadwal_poliklinik(request, id):
    cursor = connection.cursor()

    if (request.method == 'GET' and request.session['role'] == 'administrator'):
        cursor.execute("select * from medikago.jadwal_layanan_poliklinik where id_jadwal_poliklinik ='" + id + "';")
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        data_layanan = {}
        data_layanan['id_poliklinik'] = data[0]['id_poliklinik']
        data_layanan['id_jadwal_poliklinik'] = data[0]['id_jadwal_poliklinik']
        form = UpdateJadwalPoliklinik(initial=data_layanan)

    elif (request.method == 'POST' and request.session['role'] == 'administrator'):
        hari = request.POST.get("dropdown_kode_rs")
        mulai = request.POST.get("nama_layanan")
        selesai = request.POST.get("deskripsi")
        kapasitas = request.POST.get("deskripsi")
        id_dokter = request.POST.get("dropdown_id_dokter")

        if hari != "":
            cursor.execute("update medikago.jadwal_layanan_poliklinik set hari ='" + hari +"' where id_jadwal_poliklinik ='" + id + "';")
        
        if mulai != "":
            cursor.execute("update medikago.jadwal_layanan_poliklinik set waktu_mulai ='" + mulai +"' where id_jadwal_poliklinik ='" + id + "';")
        
        if selesai != "":
            cursor.execute("update medikago.jadwal_layanan_poliklinik set waktu_selesai ='" + selesai +"' where id_jadwal_poliklinik ='" + id + "';")

        if kapasitas != "":
            cursor.execute("update medikago.jadwal_layanan_poliklinik set kapasitas ='" + kapasitas +"' where id_jadwal_poliklinik ='" + id + "';")
        
        if id_dokter != "":
            cursor.execute("update medikago.jadwal_layanan_poliklinik set id_dokter ='" + id_dokter +"' where id_jadwal_poliklinik ='" + id + "';")

        form = UpdateJadwalPoliklinik(request.POST)
        return redirect('fiturwulan:view_jadwal_poliklinik')

    cursor.execute("select id_jadwal_poliklinik from medikago.jadwal_layanan_poliklinik where id_jadwal_poliklinik='"+ id +"';")
    idjad = namedtuplefetchall(cursor)
    args = {'form': form, 'idjad' : idjad, "id" : id}
    return render(request, 'update_jadwal_poliklinik.html', args)

# DELETE JADWAL POLIKLINIK
def delete_jadwal_poliklinik(request, id):
    if (request.method == 'GET' and request.session['role'] == 'administrator'):
        cursor = connection.cursor()
        delete_jadwal = "delete from medikago.jadwal_layanan_poliklinik where id_jadwal_poliklinik = '" + id + "'"
        cursor.execute(delete_jadwal)
        return redirect(reverse('fiturwulan:view_jadwal_poliklinik'))
