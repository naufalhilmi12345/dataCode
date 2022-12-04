from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from collections import namedtuple
from .forms import *
# from login.views import *
# from .models import *
from django.views.generic.edit import DeleteView
# Create your views here.


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def profile(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM medikago.pengguna where username=%s", [request.session['username']])
        row_pengguna = namedtuplefetchall(cursor)[0]
        if request.session['role'] == 'administrator':
            cursor.execute("SELECT * FROM medikago.administrator where username=%s", [request.session['username']])
            row_role = namedtuplefetchall(cursor)[0]
        elif request.session['role'] == 'dokter':
            cursor.execute("SELECT * FROM medikago.dokter where username=%s", [request.session['username']])
            row_role = namedtuplefetchall(cursor)[0]
        elif request.session['role'] == 'pasien':
            cursor.execute("SELECT distinct alergi FROM medikago.pasien natural join medikago.alergi_pasien where username=%s", [request.session['username']])
            row_role = namedtuplefetchall(cursor)
    return render(request,'Profile Pengguna.html', {'row_pengguna': row_pengguna, 'row_role':row_role})

def create_tindakan_poliklinik(request):
    if (request.method == 'POST' and request.session['role'] == 'administrator'):
        cursor = connection.cursor()
        select_tp = "select id_tindakan_poli from medikago.tindakan_poli order by char_length(id_tindakan_poli) desc, id_tindakan_poli desc"
        cursor.execute(select_tp)

        fetch_id_tindakan_poli= cursor.fetchone()[0].split('TP')
        id_tindakan_poli = 'TP' + str(int(fetch_id_tindakan_poli[1]) + 1)
        id_poliklinik = request.POST["IDPoliklinik"]
        nama_tindakan = request.POST["NamaTindakan"]
        deskripsi = request.POST["Deskripsi"]
        tarif = request.POST["Tarif"]

        cursor.execute(
            "insert into medikago.tindakan_poli values (%s,%s,%s,%s,%s)",
            [id_tindakan_poli, id_poliklinik, nama_tindakan, tarif, deskripsi]
        )
        return redirect('/fiturhilmi/view_daftar_tindakan_poliklinik')

    form = CreateTindakanPoliklinikForm()
    args = {'form': form}
    return render(request, 'Create Tindakan Poliklinik.html', args)


def create_tindakan(request):
    if (request.method == 'POST' and request.session['role'] == 'administrator'):
        cursor = connection.cursor()
        select_no = "select no_urut from medikago.tindakan order by char_length(no_urut) desc, no_urut desc limit 1"
        cursor.execute(select_no)

        fetch_no_urut= cursor.fetchone()
        no_urut = str(int(fetch_no_urut[0]) + 1)
        # id_transaksi = request.POST["IDTransaksi"]
        # id_konsultasi = request.POST["IDKonsultasi"]
        # catatan = request.POST["Catatan"]
        # biaya = str(0)
        # id_tindakan_klinik = request.POST["IDTindakanKlinik"]
        
        # cursor.execute(
        #     "insert into medikago.tindakan values (%s,%s,%s,%s,%s)",
        #     [id_konsultasi, no_urut, biaya, catatan, id_transaksi]
        # )
        # cursor.execute(
        #     "insert into medikago.daftar_tindakan values (%s, %s, %s)", 
        #     [id_konsultasi, no_urut, id_tindakan_klinik]
        # )
        form = CreateTindakanForm(request.POST)    
        id_konsultasi = form.data['IDKonsultasi']
        id_transaksi = form.data['IDTransaksi']
        catatan = form.data['Catatan']
        id_tindakan_poli = form.data['IDTindakanKlinik']
        biaya = 0


        cursor.execute("set search_path to medikago")
        cursor.execute("insert into tindakan values (%s, %s, %s, %s, %s)", [id_konsultasi, no_urut, biaya, catatan, id_transaksi])
        cursor.execute("insert into daftar_tindakan values (%s, %s, %s)", [id_konsultasi, no_urut, id_tindakan_poli])
        # cursor.execute(
        #     "insert into medikago.tindakan values (%s,%s,%s,%s,%s,%s)",
        #     [id_konsultasi, no_urut, tanggal, biaya, catatan, id_transaksi]
        # )
        return redirect('/fiturhilmi/view_daftar_tindakan')

    form = CreateTindakanForm()
    args = {'form': form}
    return render(request, 'Create Tindakan.html', args)

def view_daftar_tindakan_poliklinik(request):
    dataset = []
    cursor = connection.cursor()
    cursor.execute("select * from medikago.tindakan_poli")
    dataset = namedtuplefetchall(cursor)
    context = {
        'hasilTindakanPoliklinik' : dataset,
    }
    return render(request, 'Daftar Tindakan Poliklinik.html', context)
    # response = {}
    # return render(request,'Daftar Tindakan.html', response)

def view_daftar_tindakan(request):
    dataset = []
    cursor = connection.cursor()
    cursor.execute("select T.id_konsultasi, T.no_urut, T.biaya, T.catatan, T.id_transaksi,  STRING_AGG(D.id_tindakan_poli, ', \n') as agg from medikago.tindakan T natural join medikago.daftar_tindakan D group by T.id_konsultasi, T.no_urut, T.biaya, T.catatan, T.id_transaksi")
    dataset = namedtuplefetchall(cursor)
    context = {
        'hasilTindakan' : dataset,
    }
    return render(request, 'Daftar Tindakan.html', context)
    # response = {}
    # return render(request,'Daftar Tindakan.html', response)

def update_tindakan(request, id):
    cursor = connection.cursor()
    if (request.method == 'POST' and request.session['role'] == 'administrator'):
        catatan = request.POST.get("Catatan")
        if catatan != "":
            cursor.execute("update medikago.tindakan set catatan ='" + catatan +"' where no_urut ='" + id + "';")
        return redirect('/fiturhilmi/view_daftar_tindakan')

    cursor.execute("select id_konsultasi from medikago.tindakan where no_urut='"+ id +"';")
    id_konsultasi = cursor.fetchone()[0]
    no_urut = id
    cursor.execute("select biaya from medikago.tindakan where no_urut='"+ id +"';")
    biaya = cursor.fetchone()[0]
    cursor.execute("select id_transaksi from medikago.tindakan where no_urut='"+ id +"';")
    id_transaksi = cursor.fetchone()[0]
    cursor.execute("select no_urut, string_agg(id_tindakan_poli, ', ') as agg from medikago.daftar_tindakan where no_urut='"+ id +"' group by no_urut;")
    id_tindakan_poli = cursor.fetchone()[1]
    # daftar_id_tindakan_poli = []
    # for option in id_tindakan_poli:
    #     daftar_id_tindakan_poli.append(option)
    form = UpdateTindakanForm()
    # args = {'form':form, 'id_tindakan_poli':id_tindakan_poli, 'id_konsultasi':id_konsultasi,
    #         'no_urut':no_urut, 'biaya':biaya, 'id_transaksi':id_transaksi, "id":id}
    args = {'form':form, 'id_tindakan_poli':id_tindakan_poli, 'id_konsultasi':id_konsultasi,
            'no_urut':no_urut, 'biaya':biaya, 'id_transaksi':id_transaksi, "id":id}
    return render(request, 'Update Tindakan.html', args)


def update_tindakan_poliklinik(request, id):
    cursor = connection.cursor()
    if (request.method == 'POST' and request.session['role'] == 'administrator'):
        nama_tindakan = request.POST.get("NamaTindakan")
        deskripsi = request.POST.get("Deskripsi")
        tarif = request.POST.get("Tarif")
        id_poliklinik = request.POST.get("IDPoliklinik")

        if id_poliklinik != "":
            cursor.execute("update medikago.tindakan_poli set id_poliklinik ='" + id_poliklinik +"' where id_tindakan_poli ='" + id + "';")

        if nama_tindakan != "":
            cursor.execute("update medikago.tindakan_poli set nama_tindakan ='" + nama_tindakan +"' where id_tindakan_poli ='" + id + "';")
        
        if deskripsi != "":
            cursor.execute("update medikago.tindakan_poli set deskripsi ='" + deskripsi +"' where id_tindakan_poli ='" + id + "';")

        if tarif != "":
            cursor.execute("update medikago.tindakan_poli set tarif ='" + tarif +"' where id_tindakan_poli ='" + id + "';")

        return redirect('/fiturhilmi/view_daftar_tindakan_poliklinik')

    # cursor.execute("select id_tindakan_poli from medikago.tindakan_poli")
    # id_tp = namedtuplefetchall(cursor)
    # form = UpdateTindakanPoliklinikForm()
    # args = {'form': form, 'id_tp' : id_tp, "id" : id}
    # return render(request, 'Update Tindakan Poliklinik.html', args)

    #Kayaknya salah disini, coba langsung id_tindakan_poli = id
    cursor.execute("select id_tindakan_poli from medikago.tindakan_poli where id_tindakan_poli='"+ id +"';")
    id_tindakan_poli = cursor.fetchone()[0]
    
    # cursor.execute("select id_poliklinik from medikago.tindakan_poli where id_tindakan_poli='"+ id +"';")
    # id_poliklinik = cursor.fetchone()[0]

    form = UpdateTindakanPoliklinikForm()
    args = {'form':form, 'id_tindakan_poli':id_tindakan_poli, "id":id}
    return render(request, 'Update Tindakan Poliklinik.html', args)

def delete(request):
    # if (request.method == 'GET' and request.session['role'] == 'administrator'):
    #     cursor = connection.cursor()
    #     delete_t = "delete from medikago.tindakan where no_urut = '" + id + "'"
    #     cursor.execute(delete_t)
    #     return redirect('/fiturhilmi/view_daftar_tindakan')
    id_konsultasi = request.POST.get('id1')
    no_urut = request.POST.get('id2')
    cursor = connection.cursor()
    # cursor.execute("delete from medikago.daftar_tindakan where id_konsultasi = %s and no_urut = %s", [id_konsultasi, no_urut])
    # cursor.execute("delete from medikago.tindakan where id_konsultasi = %s and no_urut = %s", [id_konsultasi, no_urut])
    cursor.execute(f"delete from medikago.tindakan where id_konsultasi = '{id_konsultasi}' and no_urut = '{no_urut}';")
    return redirect('fiturhilmi:view_daftar_tindakan')

def delete_poliklinik(request):
#     # if (request.method == 'GET' and request.session['role'] == 'administrator'):
#     #     cursor = connection.cursor()
#     #     delete_tp = "delete from medikago.tindakan_poli where id_tindakan_poli = '" + id + "'"
#     #     cursor.execute(delete_tp)
#     #     return redirect('/fiturhilmi/view_daftar_tindakan_poliklinik')
    id_tindakan_poli = request.POST.get('id_tindakan_poli')
    cursor = connection.cursor()
    cursor.execute("delete from medikago.tindakan_poli where id_tindakan_poli = '" + id_tindakan_poli + "';")
    return redirect('fiturhilmi:view_daftar_tindakan_poliklinik')

def delete_poliklinik_(request):
    return redirect('fiturhilmi:view_daftar_tindakan_poliklinik')

